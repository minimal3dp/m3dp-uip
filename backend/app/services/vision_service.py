"""
Vision API Service

Handles interaction with Google Gemini Vision API for
image analysis and defect classification.

Based on research: "The Cyber-Physical Convergence" (Nov 2025)
- 8-class defect taxonomy (Section 5)
- Deterministic firmware philosophy (Section 1)
"""

import base64
import json
import logging

import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory

from app.core.config import settings

logger = logging.getLogger(__name__)


class VisionService:
    """
    Service for analyzing images using Gemini Vision API.

    System prompt guides the model to act as a 3D printing
    diagnostician and return structured JSON output.
    """

    # 8-class defect taxonomy from research (Section 5)
    DEFECT_CLASSES = [
        "Spaghetti",
        "Under_Extrusion",
        "Over_Extrusion",
        "Stringing",
        "Layer_Shift",
        "Warping",
        "Ringing",
        "Poor_Bridging",
        "Layer_Separation",
    ]

    SYSTEM_PROMPT = """You are an expert 3D printing diagnostician operating within the cyber-physical convergence paradigm.

Your expertise spans:
- **Deterministic Firmware**: Klipper kinematics (rotation distance, pressure advance, input shaping)
- **Algorithmic Slicing**: OrcaSlicer material profiles, quality settings, flow rate optimization
- **Defect Classification**: 8-class taxonomy (Spaghetti, Under/Over Extrusion, Stringing, Layer Shift, Warping, Ringing, Poor Bridging, Layer Separation)
- **Material Physics**: PLA, PLA+, PETG, ABS, ASA, TPU, Nylon, HIPS thermal and rheological properties

Philosophy: Software compensation refines, not fixes, mechanical issues. Mathematical precision in configuration is prerequisite for quality.

Analyze the provided image for print defects. Focus on OBSERVABLE evidence, not assumptions.

Return ONLY valid JSON (no markdown formatting):
{
  "issue_type": "Mechanical" | "Slicer" | "Material" | "Multi-factor",
  "classification": "<one of: Spaghetti, Under_Extrusion, Over_Extrusion, Stringing, Layer_Shift, Warping, Ringing, Poor_Bridging, Layer_Separation>",
  "confidence": <float 0.0-1.0>,
  "observations": ["<specific visible defects>"],
  "likely_causes": ["<root causes based on firmware/slicer/material>"],
  "csv_reference": "<klipper_calibrations | orca_recommendations category>",
  "csv_specific": "<specific CSV file if known, e.g., extruder_rotation_distance.csv>"
}

Edge cases to consider:
- Dark/shiny filaments may have low contrast
- Multi-factor issues (e.g., Warping = Material + Mechanical)
- Distinguish between spaghetti vs. intentional support material
"""

    def __init__(self):
        """Initialize vision service with Gemini API."""
        self.api_key = settings.GOOGLE_GENAI_API_KEY
        self.model_name = settings.GEMINI_MODEL
        self.model = None

        if self.is_configured():
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(
                    model_name=self.model_name,
                    generation_config={
                        "temperature": 0.4,  # Lower temp for more deterministic output
                        "top_p": 0.95,
                        "top_k": 40,
                        "max_output_tokens": 2048,
                    },
                    safety_settings={
                        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    },
                )
                logger.info(f"Initialized Gemini model: {self.model_name}")
            except Exception as e:
                logger.error(f"Failed to initialize Gemini API: {e}")
                self.model = None
        else:
            logger.warning("Vision API not configured - missing GOOGLE_GENAI_API_KEY")

    async def analyze_image(
        self,
        image_data: bytes,
        context: dict | None = None,
    ) -> dict:
        """
        Analyze image for print defects using Gemini Vision API.

        Args:
            image_data: Raw image bytes (JPEG, PNG, WebP)
            context: Optional context dict with keys:
                - printer_model: str
                - filament_type: str
                - filament_color: str (important for dark/shiny edge cases)
                - slicer: str
                - nozzle_size: float

        Returns:
            Structured JSON with classification and recommendations

        Raises:
            ValueError: If API not configured or image invalid
            RuntimeError: If API call fails
        """
        if not self.is_configured():
            raise ValueError("Vision API not configured - check GOOGLE_GENAI_API_KEY")

        if not self.model:
            raise RuntimeError("Gemini model not initialized")

        try:
            # Prepare image for API
            image_part = {
                "mime_type": "image/jpeg",  # Gemini auto-detects, but explicit is better
                "data": base64.b64encode(image_data).decode("utf-8"),
            }

            # Build context-aware prompt
            prompt = self.SYSTEM_PROMPT
            if context:
                context_str = "\n\nAdditional Context:\n"
                if "printer_model" in context:
                    context_str += f"- Printer: {context['printer_model']}\n"
                if "filament_type" in context:
                    context_str += f"- Material: {context['filament_type']}\n"
                if "filament_color" in context:
                    context_str += f"- Color: {context['filament_color']} (note: dark/shiny colors may reduce contrast)\n"  # noqa: E501
                if "slicer" in context:
                    context_str += f"- Slicer: {context['slicer']}\n"
                if "nozzle_size" in context:
                    context_str += f"- Nozzle: {context['nozzle_size']}mm\n"
                prompt += context_str

            # Call Gemini Vision API
            logger.info("Calling Gemini Vision API for defect analysis")
            response = self.model.generate_content([prompt, image_part])

            # Parse JSON response
            response_text = response.text.strip()

            # Handle markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif response_text.startswith("```"):
                response_text = response_text.split("```")[1].split("```")[0].strip()

            result = json.loads(response_text)

            # Validate required fields
            required_fields = [
                "issue_type",
                "classification",
                "confidence",
                "observations",
                "likely_causes",
            ]
            missing = [f for f in required_fields if f not in result]
            if missing:
                raise ValueError(f"API response missing fields: {missing}")

            # Validate classification against known defects
            if result["classification"] not in self.DEFECT_CLASSES:
                logger.warning(
                    f"Unknown classification: {result['classification']}, expected one of {self.DEFECT_CLASSES}"  # noqa: E501
                )

            logger.info(
                f"Analysis complete: {result['classification']} (confidence: {result['confidence']})"
            )
            return result

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse API response as JSON: {e}")
            logger.error(f"Response text: {response.text if 'response' in locals() else 'N/A'}")
            raise RuntimeError(f"Invalid JSON response from API: {e}") from e
        except ValueError:
            # Surface validation errors (e.g., missing fields) as ValueError without wrapping
            raise
        except Exception as e:
            logger.error(f"Vision API call failed: {e}")
            raise RuntimeError(f"Vision API error: {e}") from e

    def is_configured(self) -> bool:
        """Check if vision API is properly configured."""
        return bool(self.api_key)
