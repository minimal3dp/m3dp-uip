"""Additional deep error branch tests for VisionService.

Targets un-covered branches:
- __init__ failure to initialize Gemini model (exception path)
- JSON decode error inside ```json code block
- JSON decode error inside generic ``` block
- Missing required fields inside a markdown code block
"""

import json
from unittest.mock import MagicMock, patch

import pytest
from app.services.vision_service import VisionService


@pytest.fixture
def sample_image():
    return b"fake-image"


@pytest.mark.asyncio
async def test_init_model_failure_logs_and_sets_model_none():
    """GenAI model construction exception should log error and leave model None."""
    with (
        patch("app.services.vision_service.settings") as settings,
        patch("app.services.vision_service.genai") as genai,
        patch("app.services.vision_service.logger") as logger,
    ):
        settings.GOOGLE_GENAI_API_KEY = "key"
        settings.GEMINI_MODEL = "gemini-1.5-pro"
        settings.VISION_MOCK_ENABLED = False
        genai.GenerativeModel.side_effect = Exception("boom")
        service = VisionService()
        assert service.model is None
        assert logger.error.called


@pytest.mark.asyncio
async def test_json_decode_error_in_markdown_json_block(sample_image):
    """Invalid JSON within ```json block triggers JSONDecodeError -> RuntimeError path."""
    with (
        patch("app.services.vision_service.settings") as settings,
        patch("app.services.vision_service.genai") as genai,
    ):
        settings.GOOGLE_GENAI_API_KEY = "key"
        settings.GEMINI_MODEL = "gemini-1.5-pro"
        settings.VISION_MOCK_ENABLED = False
        mock_model = MagicMock()
        genai.GenerativeModel.return_value = mock_model
        service = VisionService()
        service.model = mock_model
        bad_response = MagicMock()
        bad_response.text = "```json\n{not valid json}\n```"
        mock_model.generate_content.return_value = bad_response
        with pytest.raises(RuntimeError, match="Invalid JSON response"):
            await service.analyze_image(sample_image)


@pytest.mark.asyncio
async def test_json_decode_error_in_generic_block(sample_image):
    """Invalid JSON within generic ``` block triggers decode error path."""
    with (
        patch("app.services.vision_service.settings") as settings,
        patch("app.services.vision_service.genai") as genai,
    ):
        settings.GOOGLE_GENAI_API_KEY = "key"
        settings.GEMINI_MODEL = "gemini-1.5-pro"
        settings.VISION_MOCK_ENABLED = False
        mock_model = MagicMock()
        genai.GenerativeModel.return_value = mock_model
        service = VisionService()
        service.model = mock_model
        bad_response = MagicMock()
        bad_response.text = "```\n{still not valid json}\n```"
        mock_model.generate_content.return_value = bad_response
        with pytest.raises(RuntimeError, match="Invalid JSON response"):
            await service.analyze_image(sample_image)


@pytest.mark.asyncio
async def test_missing_fields_inside_markdown_block(sample_image):
    """Missing required fields after parsing valid JSON in code block triggers ValueError."""
    with (
        patch("app.services.vision_service.settings") as settings,
        patch("app.services.vision_service.genai") as genai,
    ):
        settings.GOOGLE_GENAI_API_KEY = "key"
        settings.GEMINI_MODEL = "gemini-1.5-pro"
        settings.VISION_MOCK_ENABLED = False
        mock_model = MagicMock()
        genai.GenerativeModel.return_value = mock_model
        service = VisionService()
        service.model = mock_model
        incomplete = {"issue_type": "Mechanical", "classification": "Under_Extrusion"}
        bad_response = MagicMock()
        bad_response.text = f"```json\n{json.dumps(incomplete)}\n```"
        mock_model.generate_content.return_value = bad_response
        with pytest.raises(ValueError, match="missing fields"):
            await service.analyze_image(sample_image)


@pytest.mark.asyncio
async def test_api_runtime_exception_wraps_as_runtimeerror(sample_image):
    """Generic exceptions during API call are wrapped as RuntimeError."""
    with (
        patch("app.services.vision_service.settings") as settings,
        patch("app.services.vision_service.genai") as genai,
    ):
        settings.GOOGLE_GENAI_API_KEY = "key"
        settings.GEMINI_MODEL = "gemini-1.5-pro"
        settings.VISION_MOCK_ENABLED = False
        mock_model = MagicMock()
        genai.GenerativeModel.return_value = mock_model
        service = VisionService()
        service.model = mock_model
        mock_model.generate_content.side_effect = RuntimeError("Network timeout")
        with pytest.raises(RuntimeError, match="Vision API error"):
            await service.analyze_image(sample_image)
