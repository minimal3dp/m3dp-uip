"""
Tests for SemanticRouter (query classification service).

Tests cover:
- Route initialization and configuration
- Query classification accuracy
- Confidence scoring
- CSV category mapping
- Handler assignment
- Fallback behavior when not configured
"""

import logging
from unittest.mock import MagicMock, patch

import pytest
from app.services.semantic_router import SemanticRouter, get_semantic_router


@pytest.fixture
def mock_settings():
    """Mock settings with API key configured."""
    with patch("app.services.semantic_router.settings") as mock:
        mock.GOOGLE_GENAI_API_KEY = "test-api-key"
        yield mock


@pytest.fixture
def mock_route_layer():
    """Mock RouteLayer for testing."""
    with patch("app.services.semantic_router.RouteLayer") as mock:
        yield mock


@pytest.fixture
def mock_encoder():
    """Mock OpenAIEncoder for testing."""
    with patch("app.services.semantic_router.OpenAIEncoder") as mock:
        yield mock


@pytest.fixture
def semantic_router(mock_route_layer):
    """Create SemanticRouter instance with mocked dependencies."""
    with patch("app.services.semantic_router.settings") as settings:
        settings.GOOGLE_GENAI_API_KEY = "test-key"
        with patch("app.services.semantic_router.OpenAIEncoder"):
            mock_layer = MagicMock()
            mock_route_layer.return_value = mock_layer
            router = SemanticRouter()
            router.route_layer = mock_layer
            return router


class TestSemanticRouterInitialization:
    """Test SemanticRouter initialization."""

    def test_initialization_with_api_key(self, mock_encoder, mock_route_layer):
        """Test router initializes with API key."""
        with patch("app.services.semantic_router.settings") as settings:
            settings.GOOGLE_GENAI_API_KEY = "test-key"
            router = SemanticRouter()
            assert router.routes is not None
            assert (
                len(router.routes) == 5
            )  # calibration, troubleshooting, material, quality, general
            mock_encoder.assert_called_once()
            mock_route_layer.assert_called_once()

    def test_initialization_without_api_key(self):
        """Test router handles missing API key gracefully."""
        with patch("app.services.semantic_router.settings") as mock_settings:
            mock_settings.GOOGLE_GENAI_API_KEY = None
            router = SemanticRouter()
            assert router.routes is not None
            assert router.route_layer is None

    def test_routes_have_correct_names(self, semantic_router):
        """Test all routes are defined with correct names."""
        route_names = [route.name for route in semantic_router.routes]
        assert "calibration" in route_names
        assert "troubleshooting" in route_names
        assert "material" in route_names
        assert "quality" in route_names
        assert "general" in route_names

    def test_routes_have_utterances(self, semantic_router):
        """Test all routes have example utterances."""
        for route in semantic_router.routes:
            assert len(route.utterances) > 0


class TestQueryClassification:
    """Test query classification functionality."""

    def test_classify_calibration_query(self, semantic_router):
        """Test calibration query is classified correctly."""
        mock_decision = MagicMock()
        mock_decision.name = "calibration"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("how do I calibrate e-steps")

        assert result["route_name"] == "calibration"
        assert result["handler"] == "csv_lookup"
        assert result["confidence"] > 0.5

    def test_classify_troubleshooting_query(self, semantic_router):
        """Test troubleshooting query is classified correctly."""
        mock_decision = MagicMock()
        mock_decision.name = "troubleshooting"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("my print has gaps")

        assert result["route_name"] == "troubleshooting"
        assert result["handler"] == "csv_lookup"
        assert result["confidence"] > 0.5

    def test_classify_material_query(self, semantic_router):
        """Test material query is classified correctly."""
        mock_decision = MagicMock()
        mock_decision.name = "material"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("PETG temperature settings")

        assert result["route_name"] == "material"
        assert result["handler"] == "csv_lookup"
        assert result["confidence"] > 0.5

    def test_classify_quality_query(self, semantic_router):
        """Test quality query is classified correctly."""
        mock_decision = MagicMock()
        mock_decision.name = "quality"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("draft vs quality mode")

        assert result["route_name"] == "quality"
        assert result["handler"] == "csv_lookup"
        assert result["confidence"] > 0.5

    def test_classify_general_query(self, semantic_router):
        """Test general query is classified correctly."""
        mock_decision = MagicMock()
        mock_decision.name = "general"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("hello what can you do")

        assert result["route_name"] == "general"
        assert result["handler"] == "llm"
        assert result["confidence"] >= 0.0


class TestHandlerMapping:
    """Test route to handler mapping."""

    def test_calibration_maps_to_csv_lookup(self, semantic_router):
        """Test calibration route maps to CSV lookup handler."""
        mock_decision = MagicMock()
        mock_decision.name = "calibration"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("test query")
        assert result["handler"] == "csv_lookup"

    def test_troubleshooting_maps_to_csv_lookup(self, semantic_router):
        """Test troubleshooting route maps to CSV lookup handler."""
        mock_decision = MagicMock()
        mock_decision.name = "troubleshooting"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("test query")
        assert result["handler"] == "csv_lookup"

    def test_general_maps_to_llm(self, semantic_router):
        """Test general route maps to LLM handler."""
        mock_decision = MagicMock()
        mock_decision.name = "general"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("test query")
        assert result["handler"] == "llm"


class TestCSVCategoryMapping:
    """Test CSV category mapping methods."""

    def test_get_csv_category_calibration(self, semantic_router):
        """Test calibration maps to klipper_calibrations directory."""
        category = semantic_router.get_csv_category("calibration")
        assert category == "klipper_calibrations"

    def test_get_csv_category_troubleshooting(self, semantic_router):
        """Test troubleshooting maps to orca_recommendations directory."""
        category = semantic_router.get_csv_category("troubleshooting")
        assert category == "orca_recommendations"

    def test_get_csv_category_material(self, semantic_router):
        """Test material maps to orca_recommendations directory."""
        category = semantic_router.get_csv_category("material")
        assert category == "orca_recommendations"

    def test_get_csv_category_quality(self, semantic_router):
        """Test quality maps to orca_recommendations directory."""
        category = semantic_router.get_csv_category("quality")
        assert category == "orca_recommendations"

    def test_get_csv_category_unknown(self, semantic_router):
        """Test unknown route returns None."""
        category = semantic_router.get_csv_category("unknown_route")
        assert category is None


class TestCSVFileMapping:
    """Test CSV file mapping methods."""

    def test_get_csv_file_calibration(self, semantic_router):
        """Test calibration route suggests multiple possible files."""
        csv_file = semantic_router.get_csv_file("calibration")
        # Calibration could map to multiple CSVs, should return None for now
        assert csv_file is None or "calibration" in csv_file.lower()

    def test_get_csv_file_troubleshooting(self, semantic_router):
        """Test troubleshooting maps to specific CSV."""
        csv_file = semantic_router.get_csv_file("troubleshooting")
        assert csv_file == "troubleshooting.csv"

    def test_get_csv_file_material(self, semantic_router):
        """Test material maps to specific CSV."""
        csv_file = semantic_router.get_csv_file("material")
        assert csv_file == "material_profiles.csv"

    def test_get_csv_file_quality(self, semantic_router):
        """Test quality maps to specific CSV."""
        csv_file = semantic_router.get_csv_file("quality")
        assert csv_file == "quality_settings.csv"

    def test_get_csv_file_unknown(self, semantic_router):
        """Test unknown route returns None."""
        csv_file = semantic_router.get_csv_file("unknown_route")
        assert csv_file is None


class TestFallbackBehavior:
    """Test fallback behavior when router not configured."""

    def test_classify_without_route_layer(self):
        """Test classification falls back gracefully without route layer."""
        with patch("app.services.semantic_router.settings") as mock_settings:
            mock_settings.GOOGLE_GENAI_API_KEY = None
            router = SemanticRouter()
            router.route_layer = None

            result = router.classify_query("test query")

            assert result["route_name"] == "general"
            assert result["handler"] == "llm"
            assert result["confidence"] == 0.0

    def test_classify_with_none_decision(self, semantic_router):
        """Test classification handles None decision from route layer."""
        semantic_router.route_layer.return_value = None

        result = semantic_router.classify_query("ambiguous query")

        assert result["route_name"] == "general"
        assert result["handler"] == "llm"


class TestConfidenceScoring:
    """Test confidence score assignment."""

    def test_matched_route_high_confidence(self, semantic_router):
        """Test matched route (non-general) has high confidence."""
        mock_decision = MagicMock()
        mock_decision.name = "calibration"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("calibrate e-steps")

        assert result["confidence"] >= 0.8  # High confidence for matched route

    def test_general_route_lower_confidence(self, semantic_router):
        """Test general route has lower confidence."""
        mock_decision = MagicMock()
        mock_decision.name = "general"
        semantic_router.route_layer.return_value = mock_decision

        result = semantic_router.classify_query("hello")

        assert result["confidence"] <= 0.9  # Lower confidence for general


class TestSingletonPattern:
    """Test singleton pattern for get_semantic_router."""

    def test_get_semantic_router_returns_same_instance(self):
        """Test singleton returns same instance on multiple calls."""
        with (
            patch("app.services.semantic_router.settings") as mock_settings,
            patch("app.services.semantic_router.OpenAIEncoder"),
            patch("app.services.semantic_router.RouteLayer"),
        ):
            mock_settings.GOOGLE_GENAI_API_KEY = "test-key"

            # Clear any existing instance
            import app.services.semantic_router as sr_module

            sr_module._router_instance = None

            router1 = get_semantic_router()
            router2 = get_semantic_router()

            assert router1 is router2

    def test_get_semantic_router_creates_instance_once(self):
        """Test singleton creates instance only once."""
        with (
            patch("app.services.semantic_router.settings") as mock_settings,
            patch("app.services.semantic_router.OpenAIEncoder") as mock_encoder,
            patch("app.services.semantic_router.RouteLayer"),
        ):
            mock_settings.GOOGLE_GENAI_API_KEY = "test-key"

            # Clear any existing instance
            import app.services.semantic_router as sr_module

            sr_module._router_instance = None

            get_semantic_router()
            get_semantic_router()
            get_semantic_router()

            # Encoder should only be instantiated once
            assert mock_encoder.call_count == 1


class TestLogging:
    """Test logging behavior."""

    def test_classification_logs_result(self, semantic_router, caplog):
        """Test query classification logs the result."""
        caplog.set_level(logging.INFO)

        mock_decision = MagicMock()
        mock_decision.name = "calibration"
        semantic_router.route_layer.return_value = mock_decision

        semantic_router.classify_query("test query")

        assert "classified as" in caplog.text.lower()
        assert "calibration" in caplog.text

    def test_fallback_logs_warning(self, caplog):
        """Test fallback behavior logs warning."""
        caplog.set_level(logging.WARNING)

        with patch("app.services.semantic_router.settings") as mock_settings:
            mock_settings.GOOGLE_GENAI_API_KEY = None
            router = SemanticRouter()

            router.classify_query("test query")

            assert "not initialized" in caplog.text.lower()
