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
    # Note: Over/Under Extrusion merged into Extrusion_Issue (visual distinction too difficult)
    DEFECT_CLASSES = [
        "Spaghetti",
        "Extrusion_Issue",
        "Stringing",
        "Layer_Shift",
        "Warping",
        "Ringing",
        "Poor_Bridging",
        "Layer_Separation",
    ]

    SYSTEM_PROMPT = """You are an expert 3D printing diagnostician with deep knowledge of FDM process parameters and failure modes.

Your expertise spans:
- **Deterministic Firmware**: Klipper kinematics (rotation distance, pressure advance, input shaping)
- **Algorithmic Slicing**: OrcaSlicer material profiles, quality settings, flow rate optimization
- **Defect Classification**: 8-class taxonomy with visual discriminators
- **Material Physics**: PLA, PLA+, PETG, ABS, ASA, TPU, Nylon, HIPS thermal and rheological properties

Philosophy: Software compensation refines, not fixes, mechanical issues. Mathematical precision in configuration is prerequisite for quality.

## CRITICAL ANALYSIS PROCEDURE (Follow in Order):

**STEP 1: DESCRIBE WHAT YOU SEE**
- Describe geometry, structure, texture, and positioning
- Note if print is still attached to bed or completely detached
- Identify defect location: base/middle/top, horizontal/vertical orientation

**STEP 2: APPLY DECISION TREE** (Check conditions in this order)

1. **Complete Structural Failure?**
   - Is >30% of print mass detached and tangled?
   - Random spaghetti-like mass with no structure?
   - Print bed visible with little/no material adhered?
   → YES = **Spaghetti**

2. **Base/Corner Lifting?**
   - Are bottom corners or edges lifted >2mm from bed?
   - Curved or bent base layers creating warped foundation?
   - First layers pulling away but upper structure intact?
   → YES = **Warping**

3. **Mid-Print Layer Gaps/Splitting?**
   - Horizontal cracks or gaps BETWEEN layers (not at base)?
   - Layers separating in middle/upper sections of print?
   - Delamination visible with light gaps between layers?
   → YES = **Layer_Separation**

4. **Horizontal Span Sagging?**
   - Material drooping/sagging on HORIZONTAL bridges between two points?
   - Gravity-driven sag on overhangs or spans?
   - Poor quality on bottom of bridged sections?
   → YES = **Poor_Bridging**

5. **Thin Air Threads Between Features?**
   - Fine wispy strands in air gaps BETWEEN solid parts?
   - Oozing creates strings during travel moves (vertical/diagonal)?
   - Part structure intact, just extra thin threads attached?
   - Threads <5% of total print mass?
   → YES = **Stringing**

6. **Inconsistent Extrusion Amount?**
   - Visible gaps, holes, or missing material in layers (under)?
   - Blobs, zits, excess material, or bulging (over)?
   - Thin walls or inconsistent layer heights?
   - Rough texture from extrusion variation?
   → YES = **Extrusion_Issue**

7. **Repetitive Wave/Ripple Patterns?**
   - Regular wave patterns perpendicular to print direction?
   - Ripples/"echoes" of sharp features across surfaces?
   - Vibration-induced texture artifacts?
   → YES = **Ringing**

8. **Misaligned Layer Stacking?**
   - Layers offset horizontally creating steps/shifts?
   - Sudden displacement in X or Y during print?
   - Staircase effect from mechanical skipping?
   → YES = **Layer_Shift**

## VISUAL DISCRIMINATORS (Key Distinctions)

**Spaghetti vs Stringing:**
- Spaghetti: MASSIVE failure, >30% detached, no structure
- Stringing: MINOR threads, <5% mass, structure preserved, still attached to bed

**Stringing vs Poor_Bridging:**
- Stringing: VERTICAL/DIAGONAL threads in air (oozing during travel)
- Poor_Bridging: HORIZONTAL sag between supports (gravity + inadequate cooling)

**Warping vs Layer_Separation:**
- Warping: BASE layer lifting (adhesion issue at bed interface)
- Layer_Separation: MID-PRINT gaps (poor inter-layer bonding)

**Extrusion_Issue (covers both over and under):**
- Over: Blobs, zits, bulging, excess material
- Under: Gaps, missing material, thin walls, holes
- DO NOT distinguish between over vs under - classify as Extrusion_Issue

## SEVERITY THRESHOLDS
- Spaghetti: >30% print detached
- Stringing: Visible threads but <5% mass
- Warping: >2mm base lifting
- Layer_Separation: Visible gaps between layers
- Extrusion_Issue: Any visible inconsistency in material flow

Return ONLY valid JSON (no markdown formatting):
{
  "issue_type": "Mechanical" | "Slicer" | "Material" | "Multi-factor",
  "classification": "<one of: Spaghetti, Extrusion_Issue, Stringing, Layer_Shift, Warping, Ringing, Poor_Bridging, Layer_Separation>",
  "confidence": <float 0.0-1.0>,
  "observations": ["<specific visible defects from Step 1>"],
  "likely_causes": ["<root causes based on firmware/slicer/material>"],
  "csv_reference": "<klipper_calibrations | orca_recommendations category>",
  "csv_specific": "<specific CSV file if known, e.g., extruder_rotation_distance.csv>"
}
"""

    def __init__(self):
        """Initialize vision service with Gemini Vision API."""
        self.api_key = settings.GOOGLE_GENAI_API_KEY
        self.model_name = settings.GEMINI_MODEL

        if self.is_configured():
            genai.configure(api_key=self.api_key)

            generation_config = {
                "temperature": 0.4,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 2048,
            }

            safety_settings = {
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            }

            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=generation_config,
                safety_settings=safety_settings,
            )

            logger.info(f"Initialized Gemini Vision API with model: {self.model_name}")
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
        # Conditional mock mode when explicitly enabled
        if not self.is_configured():
            if settings.VISION_MOCK_ENABLED:
                logger.info("VisionService mock mode active (no API key)")
                return {
                    "issue_type": "Material",
                    "classification": "Stringing",
                    "confidence": 0.42,
                    "observations": [
                        "Fine wispy strands between vertical features",
                    ],
                    "likely_causes": [
                        "High nozzle temperature",
                        "Insufficient retraction distance",
                        "Moist filament increasing ooze",
                    ],
                }
            raise ValueError("Vision API not configured - check GOOGLE_GENAI_API_KEY")

        try:
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

            # Prepare image for API
            image_part = {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(image_data).decode("utf-8"),
            }

            # Call Gemini Vision API
            logger.info("Calling Gemini Vision API for defect analysis")
            response = self.model.generate_content([prompt, image_part])
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
