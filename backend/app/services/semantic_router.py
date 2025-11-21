"""
Semantic Router Service

Implements efficient query classification before expensive LLM calls.
Based on research: "The Cyber-Physical Convergence" Section 6.3

Uses aurelio-labs/semantic-router library for intent classification.
"""

import logging
from typing import Any

from semantic_router import Route
from semantic_router.encoders import OpenAIEncoder
from semantic_router.routers import SemanticRouter as SRRouter

from app.core.config import settings

# Backward-compatibility alias for older tests referring to RouteLayer
RouteLayer = SRRouter

logger = logging.getLogger(__name__)


class SemanticRouter:
    """
    Routes user queries to appropriate handlers based on intent classification.

    This reduces latency and cost by avoiding full LLM inference for simple queries.
    """

    def __init__(self):
        """Initialize semantic router with predefined routes."""
        self.routes = self._define_routes()
        self.encoder = None
        self.route_layer = None

        # Initialize if API key is available
        if settings.GOOGLE_GENAI_API_KEY:
            try:
                # Use OpenAI-compatible encoder (works with many providers)
                # Could also use HuggingFaceEncoder for local execution
                self.encoder = OpenAIEncoder(
                    name="text-embedding-3-small"  # Fast, cost-effective
                )
                # semantic-router API: use SemanticRouter, exposed as RouteLayer alias for tests
                self.route_layer = RouteLayer(encoder=self.encoder, routes=self.routes)
                logger.info("Semantic router initialized with OpenAI encoder")
            except Exception as e:
                logger.warning(f"Failed to initialize semantic router: {e}")
                self.route_layer = None
        else:
            logger.warning("Semantic router not configured - missing API key")

    def _define_routes(self) -> list[Route]:
        """
        Define intent routes based on CSV knowledge base categories.

        Routes correspond to the router pattern in the application architecture.
        """
        # Calibration route - maps to klipper_calibrations/
        calibration = Route(
            name="calibration",
            utterances=[
                "how do I calibrate e-steps",
                "fix rotation distance",
                "extruder is skipping steps",
                "flow rate is too high",
                "pressure advance tuning",
                "input shaping setup",
                "resonance compensation",
                "how to measure extruder rotation distance",
                "belt tension adjustment",
                "z-axis calibration",
                "first layer height",
                "bed leveling",
                "pid tuning hotend",
                "extruder calibration guide",
            ],
        )

        # Troubleshooting route - maps to orca_recommendations/troubleshooting.csv
        troubleshooting = Route(
            name="troubleshooting",
            utterances=[
                "why is my print spaghetti",
                "layer shift on y axis",
                "nozzle clogged",
                "print detached from bed",
                "under extrusion gaps",
                "over extrusion blobs",
                "stringing between parts",
                "warping corners lifting",
                "ringing ghosting artifacts",
                "poor bridging sagging",
                "layer separation delamination",
                "print quality issues",
                "defect detection",
                "what's wrong with my print",
            ],
        )

        # Material route - maps to orca_recommendations/material_profiles.csv
        material = Route(
            name="material",
            utterances=[
                "PLA temperature settings",
                "PETG retraction distance",
                "ABS bed temperature",
                "TPU printing speed",
                "nylon moisture absorption",
                "filament recommendations",
                "material profile setup",
                "which filament for functional parts",
                "best material for outdoor use",
                "flexible filament settings",
                "ASA temperature range",
                "HIPS support material",
            ],
        )

        # Quality/Slicer route - maps to orca_recommendations/quality_settings.csv
        quality = Route(
            name="quality",
            utterances=[
                "draft vs quality mode",
                "layer height recommendations",
                "print speed settings",
                "infill density for strength",
                "wall count for functional parts",
                "fine detail settings",
                "fast print profile",
                "normal quality preset",
                "ultra quality layer height",
                "slicer settings optimization",
                "line width settings",
                "adaptive cubic infill",
            ],
        )

        # General chat route - fallback to full LLM
        general = Route(
            name="general",
            utterances=[
                "hello",
                "what can you help with",
                "how does this work",
                "what is klipper",
                "explain 3d printing",
                "recommend a printer",
                "is this tool free",
                "who made this",
            ],
        )

        return [calibration, troubleshooting, material, quality, general]

    def classify_query(self, query: str) -> dict[str, Any]:
        """
        Classify user query into intent route.

        Args:
            query: User's natural language query

        Returns:
            dict with:
                - route_name: str - Intent classification
                - confidence: float - Classification confidence (if available)
                - handler: str - Suggested handler (csv_lookup, vision_api, llm)

        Example:
            >>> router = SemanticRouter()
            >>> result = router.classify_query("My prints are coming out with gaps")
            >>> print(result)
            {'route_name': 'troubleshooting', 'confidence': 0.92, 'handler': 'csv_lookup'}
        """
        if not self.route_layer:
            # Fallback if router not initialized
            logger.warning("Semantic router not initialized, defaulting to general")
            return {"route_name": "general", "confidence": 0.0, "handler": "llm"}

        try:
            decision = self.route_layer(query)

            # Map route to handler
            handler_map = {
                "calibration": "csv_lookup",  # Direct to klipper_calibrations/
                "troubleshooting": "csv_lookup",  # Direct to troubleshooting.csv
                "material": "csv_lookup",  # Direct to material_profiles.csv
                "quality": "csv_lookup",  # Direct to quality_settings.csv
                "general": "llm",  # Full LLM inference needed
            }

            route_name = decision.name if decision else "general"
            handler = handler_map.get(route_name, "llm")

            # Semantic router doesn't provide confidence scores by default,
            # but we can infer from whether it matched a route
            confidence = 0.9 if decision and route_name != "general" else 0.5

            logger.info(f"Query classified as '{route_name}' → handler: {handler}")

            return {
                "route_name": route_name,
                "confidence": confidence,
                "handler": handler,
            }

        except Exception as e:
            logger.error(f"Error classifying query: {e}")
            return {"route_name": "general", "confidence": 0.0, "handler": "llm"}

    def get_csv_category(self, route_name: str) -> str | None:
        """
        Map route name to CSV knowledge base category.

        Args:
            route_name: Route classification from classify_query()

        Returns:
            CSV category string or None

        Example:
            >>> router.get_csv_category('calibration')
            'klipper_calibrations'
        """
        category_map = {
            "calibration": "klipper_calibrations",
            "troubleshooting": "orca_recommendations",
            "material": "orca_recommendations",
            "quality": "orca_recommendations",
        }
        return category_map.get(route_name)

    def get_csv_file(self, route_name: str) -> str | None:
        """
        Map route name to specific CSV file (if applicable).

        Args:
            route_name: Route classification from classify_query()

        Returns:
            CSV filename or None (None means search all in category)

        Example:
            >>> router.get_csv_file('material')
            'material_profiles.csv'
        """
        file_map = {
            "troubleshooting": "troubleshooting.csv",
            "material": "material_profiles.csv",
            "quality": "quality_settings.csv",
            # calibration: None (could be any of 3 Klipper CSVs)
        }
        return file_map.get(route_name)


# Global singleton instance
_router_instance: SemanticRouter | None = None


def get_semantic_router() -> SemanticRouter:
    """
    Get or create the global semantic router instance.

    Returns:
        SemanticRouter singleton
    """
    global _router_instance
    if _router_instance is None:
        _router_instance = SemanticRouter()
    return _router_instance
