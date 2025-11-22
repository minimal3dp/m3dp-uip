"""Tests for LLMService."""

import json
from unittest.mock import MagicMock, patch

import pytest
from app.services.llm_service import LLMService


@pytest.fixture
def mock_settings():
    """Mock settings with API key."""
    with patch("app.services.llm_service.settings") as mock:
        mock.GOOGLE_GENAI_API_KEY = "test-key"
        mock.GEMINI_MODEL = "gemini-1.5-pro"
        yield mock


@pytest.fixture
def mock_genai():
    """Mock genai module."""
    with patch("app.services.llm_service.genai") as mock:
        yield mock


@pytest.fixture
def llm_service(mock_genai, mock_settings):  # noqa: ARG001
    """Create LLMService with mocks."""
    mock_model = MagicMock()
    mock_genai.GenerativeModel.return_value = mock_model
    service = LLMService()
    service.model = mock_model
    return service


@pytest.fixture
def valid_llm_response():
    """Valid LLM response."""
    return {
        "diagnosis": "Likely under-extrusion issue",
        "likely_causes": ["Partial nozzle clog", "Low flow rate"],
        "recommendations": [
            {"step": 1, "action": "Cold pull to clear nozzle", "rationale": "Removes debris"},
            {"step": 2, "action": "Calibrate flow rate", "rationale": "Ensures proper extrusion"},
        ],
        "csv_hint": "Check Klipper rotation distance calibration",
    }


class TestLLMServiceInitialization:
    """Test LLMService initialization."""

    def test_initialization_with_key(self, mock_genai, mock_settings):  # noqa: ARG002
        """Test service initializes with API key."""
        service = LLMService()
        assert service.api_key == "test-key"
        assert service.model_name == "gemini-1.5-pro"
        mock_genai.configure.assert_called_once()

    def test_initialization_without_key(self):
        """Test service handles missing key."""
        with (
            patch("app.services.llm_service.genai"),
            patch("app.services.llm_service.settings") as settings,
        ):
            settings.GOOGLE_GENAI_API_KEY = None
            settings.GEMINI_MODEL = "gemini-1.5-pro"
            service = LLMService()
            assert not service.is_configured()
            assert service.model is None

    def test_initialization_failure(self):
        """Test initialization handles model creation failure."""
        with (
            patch("app.services.llm_service.settings") as settings,
            patch("app.services.llm_service.genai") as genai,
        ):
            settings.GOOGLE_GENAI_API_KEY = "key"
            settings.GEMINI_MODEL = "gemini-1.5-pro"
            genai.GenerativeModel.side_effect = Exception("init fail")
            service = LLMService()
            assert service.model is None


class TestDiagnose:
    """Test diagnose method."""

    @pytest.mark.asyncio
    async def test_diagnose_success(self, llm_service, valid_llm_response):
        """Test successful diagnosis."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_llm_response)
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await llm_service.diagnose("My print has gaps")

        assert result["diagnosis"] == "Likely under-extrusion issue"
        assert len(result["likely_causes"]) == 2
        assert len(result["recommendations"]) == 2
        assert result["csv_hint"] == "Check Klipper rotation distance calibration"

    @pytest.mark.asyncio
    async def test_diagnose_with_context(self, llm_service, valid_llm_response):
        """Test diagnosis with context."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_llm_response)
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        context = {"printer_model": "Prusa MK4", "filament_type": "PLA"}
        result = await llm_service.diagnose("gaps between layers", context)

        # Verify context was included in prompt
        call_args = llm_service.model.generate_content.call_args
        prompt = call_args[0][0]
        assert "Prusa MK4" in prompt
        assert "PLA" in prompt
        assert result is not None

    @pytest.mark.asyncio
    async def test_diagnose_not_configured(self):
        """Test diagnosis when not configured."""
        with patch("app.services.llm_service.settings") as settings:
            settings.GOOGLE_GENAI_API_KEY = None
            settings.GEMINI_MODEL = "gemini-1.5-pro"
            with patch("app.services.llm_service.genai"):
                service = LLMService()
                with pytest.raises(ValueError, match="not configured"):
                    await service.diagnose("test query")

    @pytest.mark.asyncio
    async def test_diagnose_model_not_initialized(self, llm_service):
        """Test diagnosis when model is None."""
        llm_service.model = None
        with pytest.raises(RuntimeError, match="not initialized"):
            await llm_service.diagnose("test")

    @pytest.mark.asyncio
    async def test_diagnose_json_in_markdown(self, llm_service, valid_llm_response):
        """Test parsing JSON from markdown blocks."""
        mock_response = MagicMock()
        mock_response.text = f"```json\n{json.dumps(valid_llm_response)}\n```"
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await llm_service.diagnose("test")
        assert result["diagnosis"] == "Likely under-extrusion issue"

    @pytest.mark.asyncio
    async def test_diagnose_json_in_generic_block(self, llm_service, valid_llm_response):
        """Test parsing JSON from generic code blocks."""
        mock_response = MagicMock()
        mock_response.text = f"```\n{json.dumps(valid_llm_response)}\n```"
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await llm_service.diagnose("test")
        assert result is not None

    @pytest.mark.asyncio
    async def test_diagnose_invalid_json(self, llm_service):
        """Test handling of invalid JSON."""
        mock_response = MagicMock()
        mock_response.text = "not json"
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        with pytest.raises(RuntimeError, match="Invalid JSON"):
            await llm_service.diagnose("test")

    @pytest.mark.asyncio
    async def test_diagnose_missing_fields(self, llm_service):
        """Test handling of missing required fields."""
        incomplete = {"diagnosis": "test"}
        mock_response = MagicMock()
        mock_response.text = json.dumps(incomplete)
        llm_service.model.generate_content = MagicMock(return_value=mock_response)

        with pytest.raises(ValueError, match="missing fields"):
            await llm_service.diagnose("test")

    @pytest.mark.asyncio
    async def test_diagnose_api_exception(self, llm_service):
        """Test handling of API exceptions."""
        llm_service.model.generate_content = MagicMock(side_effect=Exception("API error"))

        with pytest.raises(RuntimeError, match="LLM error"):
            await llm_service.diagnose("test")
