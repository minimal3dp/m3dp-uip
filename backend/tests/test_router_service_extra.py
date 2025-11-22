"""Additional coverage tests for RouterService and SemanticRouter edge paths."""

from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.router_service import RouterService
from app.services.semantic_router import SemanticRouter

client = TestClient(app)


def test_semantic_router_fallback_no_api_key(monkeypatch):
    """SemanticRouter should fallback to general when not initialized (no API key)."""
    # Force settings key empty and new instance
    from app.core import config as cfg
    monkeypatch.setattr(cfg.settings, "GOOGLE_GENAI_API_KEY", "")
    router = SemanticRouter()
    result = router.classify_query("extruder skipping steps")
    assert result["route_name"] == "general"
    assert result["handler"] == "llm"
    assert result["confidence"] == 0.0


@pytest.mark.asyncio
async def test_router_service_csv_lookup_calibration_keywords():
    """Force semantic router to classify calibration and verify recommendations not empty."""
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {"route_name": "calibration", "confidence": 0.9, "handler": "csv_lookup"}
        mock_router.get_csv_category.return_value = "klipper_calibrations"
        mock_router.get_csv_file.return_value = None
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("Need to fix extruder rotation distance")
        assert result["classification"] == "calibration"
        assert result["handler"] == "csv_lookup"
        assert result["recommendations"]


@pytest.mark.asyncio
async def test_router_service_troubleshooting_mapping():
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {"route_name": "troubleshooting", "confidence": 0.9, "handler": "csv_lookup"}
        mock_router.get_csv_category.return_value = "orca_recommendations"
        mock_router.get_csv_file.return_value = "troubleshooting.csv"
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("print has stringing and blobs")
        assert result["classification"] == "troubleshooting"
        assert result["handler"] == "csv_lookup"


@pytest.mark.asyncio
async def test_router_service_material_extraction_from_query():
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {"route_name": "material", "confidence": 0.9, "handler": "csv_lookup"}
        mock_router.get_csv_category.return_value = "orca_recommendations"
        mock_router.get_csv_file.return_value = "material_profiles.csv"
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("Need PETG temperature guidance")
        assert result["classification"] == "material"
        assert result["handler"] == "csv_lookup"


@pytest.mark.asyncio
async def test_router_service_quality_extraction():
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {"route_name": "quality", "confidence": 0.9, "handler": "csv_lookup"}
        mock_router.get_csv_category.return_value = "orca_recommendations"
        mock_router.get_csv_file.return_value = "quality_settings.csv"
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("Looking for ultra quality settings")
        assert result["classification"] == "quality"
        assert result["handler"] == "csv_lookup"


@pytest.mark.asyncio
async def test_router_service_unknown_route_fallback():
    # Simulate classify_query returning unknown handler
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {"route_name": "alien", "confidence": 0.2, "handler": "unknown"}
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("mysterious issue")
        assert result["handler"] == "llm"
        assert result["classification"] == "alien"


@pytest.mark.asyncio
async def test_router_service_image_diagnosis_fallback_troubleshooting(monkeypatch):
    # Mock VisionService to bypass API key check
    from app.services import vision_service as vs_mod

    class DummyVision:
        def __init__(self):
            self.api_key = "dummy"
            self.model = object()

        def is_configured(self):  # noqa: D401
            return True

        async def analyze_image(self, _image_data, _context):  # noqa: D401
            return {
                "issue_type": "Multi-factor",
                "classification": "Unknown_Defect",
                "confidence": 0.5,
                "observations": ["artifact"],
                "likely_causes": ["PLA moisture"],
            }

    monkeypatch.setattr(vs_mod, "VisionService", lambda: DummyVision())
    # Also patch RouterService to use dummy when constructing
    from app.services import router_service as rs_mod
    monkeypatch.setattr(rs_mod, "VisionService", lambda: DummyVision())
    service = RouterService()
    result = await service.diagnose_from_image(b"fake", context=None)
    assert result["handler"] == "vision_api"
    assert result["classification"] == "Unknown_Defect"
    assert isinstance(result["recommendations"], list)


@pytest.mark.asyncio
async def test_router_service_csv_lookup_no_mapping():
    """Route classified as csv_lookup but with no CSV category mapping returns error structure."""
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {
            "route_name": "mystery",
            "confidence": 0.4,
            "handler": "csv_lookup",
        }
        mock_router.get_csv_category.return_value = None
        mock_router.get_csv_file.return_value = None
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("unknown phenomenon")
        assert result["classification"] == "mystery"
        assert "error" in result
        assert result["recommendations"] == []


@pytest.mark.asyncio
async def test_router_service_mechanical_non_extrusion_fallback(monkeypatch):
    """Mechanical classification without extrusion keywords should fallback to troubleshooting search."""
    # Dummy vision returning Mechanical with classification 'Ringing' (no direct extrusion mapping)
    from app.services import vision_service as vs_mod

    class DummyVisionMech:
        def __init__(self):
            self.api_key = "x"
            self.model = object()

        def is_configured(self):
            return True

        async def analyze_image(self, _image_data, _context):
            return {
                "issue_type": "Mechanical",
                "classification": "Ringing",
                "confidence": 0.7,
                "observations": ["visible ripples"],
                "likely_causes": ["belt tension", "input shaping"]
            }

    monkeypatch.setattr(vs_mod, "VisionService", lambda: DummyVisionMech())
    from app.services import router_service as rs_mod
    monkeypatch.setattr(rs_mod, "VisionService", lambda: DummyVisionMech())
    service = RouterService()
    result = await service.diagnose_from_image(b"img", context=None)
    assert result["classification"] == "Ringing"
    # Expect recommendations populated via fallback troubleshooting path
    assert isinstance(result["recommendations"], list)
    assert result["handler"] == "vision_api"


@pytest.mark.asyncio
async def test_router_service_material_fallback_all():
    """Material route with no explicit material in query/context returns full material dataset."""
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {
            "route_name": "material",
            "confidence": 0.6,
            "handler": "csv_lookup",
        }
        mock_router.get_csv_category.return_value = "orca_recommendations"
        mock_router.get_csv_file.return_value = "material_profiles.csv"
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("general material guidance")
        assert result["classification"] == "material"
        assert result["handler"] == "csv_lookup"
        assert isinstance(result["recommendations"], list)


@pytest.mark.asyncio
async def test_router_service_quality_fallback_all():
    """Quality route with no quality level specified returns full quality settings dataset."""
    service = RouterService()
    with patch("app.services.router_service.get_semantic_router") as mock_get_router:
        mock_router = MagicMock()
        mock_router.classify_query.return_value = {
            "route_name": "quality",
            "confidence": 0.55,
            "handler": "csv_lookup",
        }
        mock_router.get_csv_category.return_value = "orca_recommendations"
        mock_router.get_csv_file.return_value = "quality_settings.csv"
        mock_get_router.return_value = mock_router
        result = await service.diagnose_from_text("improve overall output")
        assert result["classification"] == "quality"
        assert result["handler"] == "csv_lookup"
        assert isinstance(result["recommendations"], list)
