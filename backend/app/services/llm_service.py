"""
LLM Service for general diagnosis queries.

Handles queries that don't match specific CSV routes via semantic classification.
Uses Gemini 1.5 Pro to provide general troubleshooting guidance when CSV lookups
are insufficient.

Based on research: Fallback to LLM when structured data unavailable.
"""

import json
import logging
from typing import Any

import google.generativeai as genai

from app.core.config import settings

logger = logging.getLogger(__name__)


class LLMService:
    """
    Service for general LLM-based diagnosis when CSV routing fails.

    Philosophy: Use LLM as last resort after structured CSV lookup fails.
    LLMs provide flexibility but less precision than formula-based CSV data.
    """

    SYSTEM_PROMPT = """You are an expert 3D printing diagnostician with deep knowledge of:
- **Klipper Firmware**: Rotation distance, pressure advance, input shaping, kinematics
- **OrcaSlicer Settings**: Material profiles, quality presets, flow calibration
- **Common Issues**: Under/over extrusion, stringing, layer adhesion, warping, ringing

The user's query couldn't be matched to specific calibration data.
Provide concise, actionable troubleshooting steps.

Response format (JSON):
{
  "diagnosis": "<brief issue summary>",
  "likely_causes": ["<cause 1>", "<cause 2>"],
  "recommendations": [
    {
      "step": 1,
      "action": "<what to do>",
      "rationale": "<why this helps>"
    }
  ],
  "csv_hint": "<suggest which CSV/calibration might help if available>"
}

Keep responses focused and practical. Avoid generic advice like "check your settings."
"""

    def __init__(self):
        """Initialize LLM service with Gemini API."""
        self.api_key = settings.GOOGLE_GENAI_API_KEY
        self.model_name = settings.GEMINI_MODEL
        self.model = None

        if self.is_configured():
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(
                    model_name=self.model_name,
                    generation_config={
                        "temperature": 0.7,  # Balanced creativity/consistency
                        "top_p": 0.9,
                        "top_k": 40,
                        "max_output_tokens": 1024,
                    },
                )
                logger.info(f"Initialized LLM service: {self.model_name}")
            except Exception as e:
                logger.error(f"Failed to initialize LLM service: {e}")
                self.model = None
        else:
            logger.warning("LLM service not configured - missing GOOGLE_GENAI_API_KEY")

    async def diagnose(
        self,
        query: str,
        context: dict | None = None,
    ) -> dict[str, Any]:
        """
        Diagnose issue using general LLM reasoning.

        Args:
            query: User's text description
            context: Optional printer/material context

        Returns:
            Structured diagnosis with recommendations

        Raises:
            ValueError: If LLM not configured
            RuntimeError: If LLM call fails
        """
        if not self.is_configured():
            raise ValueError("LLM service not configured - check GOOGLE_GENAI_API_KEY")

        if not self.model:
            raise RuntimeError("LLM model not initialized")

        # Build context-aware prompt
        prompt = self.SYSTEM_PROMPT + f"\n\nUser Query: {query}\n"
        if context:
            prompt += "\nContext:\n"
            for key, value in context.items():
                prompt += f"- {key}: {value}\n"

        try:
            logger.info(f"LLM diagnosis request: {query[:100]}...")
            response = self.model.generate_content(prompt)

            try:
                result_text = response.text.strip()
            except Exception as e:
                logger.error(f"Failed to access response.text: {e}")
                logger.error(f"Full LLM response object: {response}")
                if response and hasattr(response, "prompt_feedback"):
                    logger.error(f"Prompt feedback: {response.prompt_feedback}")
                if response and hasattr(response, "candidates"):
                    for i, candidate in enumerate(response.candidates):
                        logger.error(f"Candidate {i} finish reason: {candidate.finish_reason}")
                        if hasattr(candidate, "safety_ratings"):
                            logger.error(
                                f"Candidate {i} safety ratings: {candidate.safety_ratings}"
                            )
                        if hasattr(candidate, "content") and hasattr(candidate.content, "parts"):
                            for part in candidate.content.parts:
                                logger.error(f"Candidate {i} part: {part}")
                raise RuntimeError(f"LLM content generation failed: {e}") from e

            # Handle markdown code blocks
            if result_text.startswith("```json"):
                result_text = result_text.split("```json")[1].split("```")[0].strip()
            elif result_text.startswith("```"):
                result_text = result_text.split("```")[1].split("```")[0].strip()

            result = json.loads(result_text)

            # Validate required fields
            required = ["diagnosis", "likely_causes", "recommendations"]
            missing = [f for f in required if f not in result]
            if missing:
                raise ValueError(f"LLM response missing fields: {missing}")

            logger.info(f"LLM diagnosis complete: {result['diagnosis'][:100]}")
            return result

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            raise RuntimeError(f"Invalid JSON from LLM: {e}") from e
        except ValueError:
            raise
        except Exception as e:
            logger.error(f"LLM API call failed: {e}")
            raise RuntimeError(f"LLM error: {e}") from e

    def is_configured(self) -> bool:
        """Check if LLM service is configured."""
        return bool(self.api_key)


# Global singleton
_llm_service_instance: LLMService | None = None


def get_llm_service() -> LLMService:
    """Get or create global LLM service instance."""
    global _llm_service_instance
    if _llm_service_instance is None:
        _llm_service_instance = LLMService()
    return _llm_service_instance
