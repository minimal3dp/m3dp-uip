"""
Tests for VisionService (Gemini Vision API integration).

Tests cover:
- Initialization and configuration
- Mock API responses with various formats
- JSON parsing (with/without markdown code blocks)
- Error handling (API failures, invalid responses)
- Context integration (filament color, printer model)
- Defect classification validation
"""

import json
from unittest.mock import MagicMock, patch

import pytest
from app.services.vision_service import VisionService


@pytest.fixture
def mock_settings():
    """Mock settings with API key configured."""
    with patch("app.services.vision_service.settings") as mock:
        mock.GOOGLE_GENAI_API_KEY = "test-api-key"
        mock.GEMINI_MODEL = "gemini-1.5-pro"
        yield mock


@pytest.fixture
def mock_genai():
    """Mock google.generativeai module."""
    with patch("app.services.vision_service.genai") as mock:
        yield mock


@pytest.fixture
def vision_service(mock_genai, mock_settings):
    """Create VisionService instance with mocked dependencies.

    Depends on mock_settings to ensure GOOGLE_GENAI_API_KEY is present so
    VisionService initializes as configured instead of raising configuration errors.
    """
    mock_model = MagicMock()
    mock_genai.GenerativeModel.return_value = mock_model
    service = VisionService()
    service.model = mock_model  # Ensure model is set even if init skipped
    return service


@pytest.fixture
def sample_image_data():
    """Create sample image data."""
    return b"fake-image-data"


@pytest.fixture
def valid_api_response():
    """Valid API response matching expected format."""
    return {
        "issue_type": "Mechanical",
        "classification": "Under_Extrusion",
        "confidence": 0.85,
        "observations": [
            "Visible gaps between extrusion lines",
            "Inconsistent layer thickness",
        ],
        "likely_causes": [
            "Incorrect rotation distance",
            "Partial nozzle clog",
            "Low extrusion multiplier",
        ],
        "csv_reference": "klipper_calibrations",
        "csv_specific": "extruder_rotation_distance.csv",
    }


class TestVisionServiceInitialization:
    """Test VisionService initialization."""

    def test_initialization_with_api_key(self, mock_genai):
        """Test service initializes when API key is configured."""
        with patch("app.services.vision_service.settings") as settings:
            settings.GOOGLE_GENAI_API_KEY = "test-api-key"
            settings.GEMINI_MODEL = "gemini-1.5-pro"
            service = VisionService()
            assert service.api_key == "test-api-key"
            assert service.model_name == "gemini-1.5-pro"
            mock_genai.configure.assert_called_once_with(api_key="test-api-key")

    def test_initialization_without_api_key(self):
        """Test service handles missing API key gracefully."""
        with (
            patch("app.services.vision_service.genai"),
            patch("app.services.vision_service.settings") as mock_settings,
        ):
            mock_settings.GOOGLE_GENAI_API_KEY = None
            mock_settings.GEMINI_MODEL = "gemini-1.5-pro"
            service = VisionService()
            assert not service.is_configured()
            assert service.model is None

    def test_is_configured_returns_true_with_key(self, vision_service):
        """Test is_configured returns True when API key present."""
        assert vision_service.is_configured()

    def test_is_configured_returns_false_without_key(self):
        """Test is_configured returns False when API key missing."""
        with patch("app.services.vision_service.settings") as mock_settings:
            mock_settings.GOOGLE_GENAI_API_KEY = None
            mock_settings.GEMINI_MODEL = "gemini-1.5-pro"
            with patch("app.services.vision_service.genai"):
                service = VisionService()
                assert not service.is_configured()


class TestAnalyzeImageBasic:
    """Test basic analyze_image functionality."""

    @pytest.mark.asyncio
    async def test_analyze_image_success(
        self, vision_service, sample_image_data, valid_api_response
    ):
        """Test successful image analysis."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_api_response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await vision_service.analyze_image(sample_image_data)

        assert result["issue_type"] == "Mechanical"
        assert result["classification"] == "Under_Extrusion"
        assert result["confidence"] == 0.85
        assert len(result["observations"]) == 2
        assert len(result["likely_causes"]) == 3

    @pytest.mark.asyncio
    async def test_analyze_image_not_configured(self, sample_image_data):
        """Test analyze_image raises error when not configured."""
        with patch("app.services.vision_service.settings") as mock_settings:
            mock_settings.GOOGLE_GENAI_API_KEY = None
            mock_settings.GEMINI_MODEL = "gemini-1.5-pro"
            with patch("app.services.vision_service.genai"):
                service = VisionService()

                with pytest.raises(ValueError, match="Vision API not configured"):
                    await service.analyze_image(sample_image_data)

    @pytest.mark.asyncio
    async def test_analyze_image_model_not_initialized(self, vision_service, sample_image_data):
        """Test analyze_image raises error when model is None."""
        vision_service.model = None

        with pytest.raises(RuntimeError, match="Gemini model not initialized"):
            await vision_service.analyze_image(sample_image_data)


class TestJSONParsing:
    """Test JSON parsing with various response formats."""

    @pytest.mark.asyncio
    async def test_parse_plain_json(self, vision_service, sample_image_data, valid_api_response):
        """Test parsing plain JSON response."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_api_response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await vision_service.analyze_image(sample_image_data)
        assert result["classification"] == "Under_Extrusion"

    @pytest.mark.asyncio
    async def test_parse_json_with_markdown_json_block(
        self, vision_service, sample_image_data, valid_api_response
    ):
        """Test parsing JSON wrapped in ```json markdown block."""
        mock_response = MagicMock()
        mock_response.text = f"```json\n{json.dumps(valid_api_response)}\n```"
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await vision_service.analyze_image(sample_image_data)
        assert result["classification"] == "Under_Extrusion"

    @pytest.mark.asyncio
    async def test_parse_json_with_generic_markdown_block(
        self, vision_service, sample_image_data, valid_api_response
    ):
        """Test parsing JSON wrapped in generic ``` markdown block."""
        mock_response = MagicMock()
        mock_response.text = f"```\n{json.dumps(valid_api_response)}\n```"
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await vision_service.analyze_image(sample_image_data)
        assert result["classification"] == "Under_Extrusion"

    @pytest.mark.asyncio
    async def test_parse_invalid_json_raises_error(self, vision_service, sample_image_data):
        """Test invalid JSON raises RuntimeError."""
        mock_response = MagicMock()
        mock_response.text = "This is not valid JSON"
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        with pytest.raises(RuntimeError, match="Invalid JSON response"):
            await vision_service.analyze_image(sample_image_data)


class TestContextIntegration:
    """Test context parameter integration."""

    @pytest.mark.asyncio
    async def test_analyze_with_printer_context(
        self, vision_service, sample_image_data, valid_api_response
    ):
        """Test image analysis with printer context."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_api_response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        context = {
            "printer_model": "Prusa MK4",
            "filament_type": "PLA",
            "filament_color": "Black",
            "slicer": "OrcaSlicer",
            "nozzle_size": 0.4,
        }

        result = await vision_service.analyze_image(sample_image_data, context=context)

        # Verify context was passed to API
        call_args = vision_service.model.generate_content.call_args
        prompt_with_context = call_args[0][0][0]
        assert "Prusa MK4" in prompt_with_context
        assert "PLA" in prompt_with_context
        assert "Black" in prompt_with_context
        assert "OrcaSlicer" in prompt_with_context
        assert "0.4mm" in prompt_with_context
        assert "dark/shiny colors may reduce contrast" in prompt_with_context

        assert result["classification"] == "Under_Extrusion"

    @pytest.mark.asyncio
    async def test_analyze_with_partial_context(
        self, vision_service, sample_image_data, valid_api_response
    ):
        """Test image analysis with partial context."""
        mock_response = MagicMock()
        mock_response.text = json.dumps(valid_api_response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        context = {"filament_type": "PETG", "nozzle_size": 0.6}

        result = await vision_service.analyze_image(sample_image_data, context=context)

        call_args = vision_service.model.generate_content.call_args
        prompt_with_context = call_args[0][0][0]
        assert "PETG" in prompt_with_context
        assert "0.6mm" in prompt_with_context
        assert result is not None


class TestDefectClassification:
    """Test defect classification validation."""

    @pytest.mark.asyncio
    async def test_valid_defect_classification(self, vision_service, sample_image_data):
        """Test all valid defect classifications are accepted."""
        for defect in VisionService.DEFECT_CLASSES:
            response = {
                "issue_type": "Mechanical",
                "classification": defect,
                "confidence": 0.9,
                "observations": ["Test observation"],
                "likely_causes": ["Test cause"],
            }
            mock_response = MagicMock()
            mock_response.text = json.dumps(response)
            vision_service.model.generate_content = MagicMock(return_value=mock_response)

            result = await vision_service.analyze_image(sample_image_data)
            assert result["classification"] == defect

    @pytest.mark.asyncio
    async def test_unknown_classification_logged_but_accepted(
        self, vision_service, sample_image_data, caplog
    ):
        """Test unknown classification logs warning but doesn't fail."""
        response = {
            "issue_type": "Mechanical",
            "classification": "Unknown_Defect",
            "confidence": 0.5,
            "observations": ["Test observation"],
            "likely_causes": ["Test cause"],
        }
        mock_response = MagicMock()
        mock_response.text = json.dumps(response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        result = await vision_service.analyze_image(sample_image_data)
        assert result["classification"] == "Unknown_Defect"
        assert "Unknown classification" in caplog.text


class TestErrorHandling:
    """Test error handling scenarios."""

    @pytest.mark.asyncio
    async def test_missing_required_fields(self, vision_service, sample_image_data):
        """Test response with missing required fields raises error."""
        incomplete_response = {
            "issue_type": "Mechanical",
            "classification": "Under_Extrusion",
            # Missing: confidence, observations, likely_causes
        }
        mock_response = MagicMock()
        mock_response.text = json.dumps(incomplete_response)
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        with pytest.raises(ValueError, match="missing fields"):
            await vision_service.analyze_image(sample_image_data)

    @pytest.mark.asyncio
    async def test_api_call_exception(self, vision_service, sample_image_data):
        """Test API call exception is handled."""
        vision_service.model.generate_content = MagicMock(side_effect=Exception("API Error"))

        with pytest.raises(RuntimeError, match="Vision API error"):
            await vision_service.analyze_image(sample_image_data)

    @pytest.mark.asyncio
    async def test_empty_response(self, vision_service, sample_image_data):
        """Test empty response is handled."""
        mock_response = MagicMock()
        mock_response.text = ""
        vision_service.model.generate_content = MagicMock(return_value=mock_response)

        with pytest.raises(RuntimeError, match="Invalid JSON response"):
            await vision_service.analyze_image(sample_image_data)


class TestSystemPrompt:
    """Test system prompt structure."""

    def test_system_prompt_contains_defect_classes(self):
        """Test system prompt includes all defect classes."""
        for defect in VisionService.DEFECT_CLASSES:
            assert defect in VisionService.SYSTEM_PROMPT

    def test_system_prompt_mentions_key_concepts(self):
        """Test system prompt includes key concepts from research."""
        prompt = VisionService.SYSTEM_PROMPT
        assert "cyber-physical convergence" in prompt.lower()
        assert "Klipper" in prompt
        assert "OrcaSlicer" in prompt
        assert "Deterministic Firmware" in prompt
        assert "Algorithmic Slicing" in prompt
        assert "OBSERVABLE evidence" in prompt

    def test_system_prompt_includes_edge_cases(self):
        """Test system prompt addresses edge cases."""
        prompt = VisionService.SYSTEM_PROMPT
        assert "Dark/shiny filaments" in prompt
        assert "Multi-factor" in prompt
        assert "spaghetti vs. intentional support" in prompt
