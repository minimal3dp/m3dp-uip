"""
Vision API Service

Handles interaction with Google Gemini Vision API for
image analysis and defect classification.
"""

from app.core.config import settings


class VisionService:
    """
    Service for analyzing images using Gemini Vision API.

    System prompt guides the model to act as a 3D printing
    diagnostician and return structured JSON output.
    """

    SYSTEM_PROMPT = """You are an expert 3D printing diagnostician with deep knowledge of:
- Common print defects (under-extrusion, over-extrusion, layer shifts, warping, stringing, etc.)
- Klipper firmware calibration (rotation distance, pressure advance, input shaping)
- Slicer settings (layer height, speed, temperature, retraction)
- Material properties (PLA, PETG, ABS, TPU, etc.)

Analyze the provided image and identify any print defects or issues.

Return a JSON object with:
{
  "issue_type": "Mechanical" | "Slicer" | "Material",
  "classification": "<specific defect name>",
  "confidence": <0.0-1.0>,
  "observations": ["<list of visible issues>"],
  "likely_causes": ["<list of probable root causes>"],
  "csv_reference": "<which CSV knowledge base to use>"
}

Be specific and precise. Focus on observable defects, not assumptions.
"""

    def __init__(self):
        """Initialize vision service with Gemini API."""
        self.api_key = settings.GOOGLE_GENAI_API_KEY
        self.model_name = settings.GEMINI_MODEL

        # TODO: Initialize google-generativeai client
        # import google.generativeai as genai
        # genai.configure(api_key=self.api_key)
        # self.model = genai.GenerativeModel(self.model_name)

    async def analyze_image(
        self,
        _image_data: bytes,
        _context: dict | None = None,
    ) -> dict:
        """
        Analyze image for print defects.

        Args:
            _image_data: Raw image bytes (unused in stub)
            _context: Optional context (printer model, filament type, etc.) (unused in stub)

        Returns:
            Structured JSON with classification and recommendations
        """
        # TODO: Implement actual vision API call
        # 1. Prepare image for API
        # 2. Add context to prompt if provided
        # 3. Call Gemini Vision API
        # 4. Parse and validate JSON response

        # Mock response for now
        return {
            "issue_type": "Mechanical",
            "classification": "Under-extrusion",
            "confidence": 0.85,
            "observations": [
                "Visible gaps between extrusion lines",
                "Inconsistent layer adhesion",
                "Thin walls appear translucent",
            ],
            "likely_causes": [
                "Incorrect extruder rotation distance",
                "Partial nozzle clog",
                "Temperature too low",
            ],
            "csv_reference": "Klipper Calibrations - Extruder Rotation Distance.csv",
        }

    def is_configured(self) -> bool:
        """Check if vision API is properly configured."""
        return bool(self.api_key)
