"""
Router Service

Coordinates diagnosis workflow: classification → retrieval → recommendation.

Based on research architecture (Section 1):
"The Router classifies issue type, Retrieval fetches relevant CSV data,
Calculator renders precise formula-based solutions."
"""

import logging
from typing import Any

from app.services.csv_loader import get_csv_loader
from app.services.semantic_router import get_semantic_router
from app.services.vision_service import VisionService

logger = logging.getLogger(__name__)


class RouterService:
    """
    Orchestrates the diagnostic workflow.

    Flow:
    1. Semantic Router classifies intent (text queries)
    2. Vision Service analyzes images (if provided)
    3. Router logic maps classification to CSV category
    4. CSV Loader retrieves relevant data
    5. Response builder formats recommendations
    """

    def __init__(self):
        """Initialize router with service dependencies."""
        self.semantic_router = get_semantic_router()
        self.vision_service = VisionService()
        self.csv_loader = get_csv_loader()

    async def diagnose_from_text(
        self,
        query: str,
        context: dict | None = None,
    ) -> dict[str, Any]:
        """
        Diagnose issue from text description.

        Args:
            query: User's text description of the problem
            context: Optional context (printer, filament, etc.)

        Returns:
            Structured diagnosis with recommendations
        """
        logger.info(f"Text diagnosis request: {query[:100]}...")

        # Step 1: Classify intent with semantic router
        classification = self.semantic_router.classify_query(query)
        route_name = classification["route_name"]
        confidence = classification["confidence"]

        logger.info(f"Semantic router classification: {route_name} (confidence: {confidence})")

        # Step 2: Determine handler based on classification
        if classification["handler"] == "csv_lookup":
            # Direct CSV lookup - most efficient
            result = await self._handle_csv_lookup(route_name, query, context)
        else:
            # Fallback to full LLM (not implemented yet)
            result = {
                "classification": route_name,
                "confidence": confidence,
                "handler": "llm",
                "message": "LLM handler not yet implemented",
                "recommendations": [],
            }

        return result

    async def diagnose_from_image(
        self,
        image_data: bytes,
        context: dict | None = None,
    ) -> dict[str, Any]:
        """
        Diagnose issue from image.

        Args:
            image_data: Raw image bytes
            context: Optional context (printer, filament, etc.)

        Returns:
            Structured diagnosis with recommendations
        """
        logger.info("Image diagnosis request")

        # Step 1: Analyze image with vision API
        vision_result = await self.vision_service.analyze_image(image_data, context)

        # Step 2: Route to appropriate CSV based on vision classification
        issue_type = vision_result["issue_type"]
        classification = vision_result["classification"]

        logger.info(f"Vision classification: {classification} ({issue_type})")

        # Step 3: Retrieve relevant CSV data
        csv_data = self._get_csv_data_for_classification(issue_type, classification, vision_result)

        # Step 4: Build response
        return {
            "classification": classification,
            "issue_type": issue_type,
            "confidence": vision_result["confidence"],
            "observations": vision_result["observations"],
            "likely_causes": vision_result["likely_causes"],
            "recommendations": csv_data,
            "handler": "vision_api",
        }

    async def _handle_csv_lookup(
        self,
        route_name: str,
        query: str,
        context: dict | None = None,
    ) -> dict[str, Any]:
        """
        Handle CSV lookup based on semantic route.

        Args:
            route_name: Semantic route classification
            query: Original user query
            context: Optional context

        Returns:
            Structured response with CSV data
        """
        # Get CSV category and file
        csv_category = self.semantic_router.get_csv_category(route_name)
        csv_file = self.semantic_router.get_csv_file(route_name)

        if not csv_category:
            return {
                "classification": route_name,
                "error": f"No CSV mapping for route: {route_name}",
                "recommendations": [],
            }

        # Retrieve CSV data
        if route_name == "calibration":
            # Calibration route - search all Klipper CSVs
            recommendations = self._get_calibration_data(query)
        elif route_name == "troubleshooting":
            # Troubleshooting - search by query keywords
            recommendations = self._get_troubleshooting_data(query)
        elif route_name == "material":
            # Material - extract material type from query or context
            material_type = self._extract_material_type(query, context)
            recommendations = self._get_material_data(material_type)
        elif route_name == "quality":
            # Quality - extract quality level from query
            quality_level = self._extract_quality_level(query)
            recommendations = self._get_quality_data(quality_level)
        else:
            recommendations = []

        return {
            "classification": route_name,
            "confidence": 0.85,  # High confidence for direct CSV lookup
            "csv_category": csv_category,
            "csv_file": csv_file,
            "recommendations": recommendations,
            "handler": "csv_lookup",
        }

    def _get_csv_data_for_classification(
        self,
        issue_type: str,
        classification: str,
        vision_result: dict,
    ) -> list[dict]:
        """
        Retrieve CSV data based on vision classification.

        Args:
            issue_type: Mechanical/Slicer/Material/Multi-factor
            classification: Specific defect name
            vision_result: Full vision API result

        Returns:
            List of recommendation dicts from CSV
        """
        recommendations = []

        # Map issue type to CSV category
        if issue_type == "Mechanical":
            # Search Klipper calibrations
            if "Extrusion" in classification or "Under_Extrusion" in classification:
                data = self.csv_loader.get_rotation_distance_formula()
                if data is not None:
                    recommendations.extend(data.to_dict("records"))
            # Could also check pressure advance, input shaping, etc.

        elif issue_type == "Material":
            # Search material profiles - extract material from vision result
            material_hint = self._extract_material_from_vision(vision_result)
            if material_hint:
                data = self.csv_loader.get_material_recommendations(material_hint)
                if data is not None:
                    recommendations.extend(data.to_dict("records"))

        elif issue_type == "Slicer":
            # Search quality settings or troubleshooting
            data = self.csv_loader.get_troubleshooting_data(classification)
            if data is not None:
                recommendations.extend(data.to_dict("records"))

        # If multi-factor or no specific match, search troubleshooting
        if not recommendations:
            data = self.csv_loader.get_troubleshooting_data(classification)
            if data is not None:
                recommendations.extend(data.to_dict("records"))

        return recommendations

    def _get_calibration_data(self, query: str) -> list[dict]:
        """Search Klipper calibration CSVs based on query keywords."""
        keywords = query.lower()
        recommendations = []

        if any(word in keywords for word in ["extruder", "e-step", "rotation", "extrusion"]):
            data = self.csv_loader.get_rotation_distance_formula()
            if data is not None:
                recommendations.extend(data.to_dict("records"))

        if any(word in keywords for word in ["pressure", "advance", "blob", "gap"]):
            data = self.csv_loader.get_pressure_advance_formula()
            if data is not None:
                recommendations.extend(data.to_dict("records"))

        if any(
            word in keywords for word in ["input", "shaping", "ringing", "ghosting", "resonance"]
        ):
            data = self.csv_loader.get_input_shaping_data()
            if data is not None:
                recommendations.extend(data.to_dict("records"))

        return recommendations

    def _get_troubleshooting_data(self, query: str) -> list[dict]:
        """Search troubleshooting CSV based on query keywords."""
        # Try to extract defect type from query
        defect_keywords = {
            "under extrusion": "Under_Extrusion",
            "over extrusion": "Over_Extrusion",
            "stringing": "Stringing",
            "layer shift": "Layer_Shift",
            "warping": "Warping",
            "ringing": "Ringing",
            "ghosting": "Ringing",
            "bridging": "Poor_Bridging",
            "separation": "Layer_Separation",
            "delamination": "Layer_Separation",
        }

        query_lower = query.lower()
        for keyword, defect_type in defect_keywords.items():
            if keyword in query_lower:
                data = self.csv_loader.get_troubleshooting_data(defect_type)
                if data is not None and not data.empty:
                    return data.to_dict("records")

        # Fallback: return all troubleshooting data
        data = self.csv_loader.get_csv_by_name("troubleshooting", "orca")
        return data.to_dict("records") if data is not None else []

    def _get_material_data(self, material_type: str | None) -> list[dict]:
        """Get material profile data."""
        if material_type:
            data = self.csv_loader.get_material_recommendations(material_type)
            if data is not None and not data.empty:
                return data.to_dict("records")

        # Fallback: return all materials
        data = self.csv_loader.get_csv_by_name("material_profiles", "orca")
        return data.to_dict("records") if data is not None else []

    def _get_quality_data(self, quality_level: str | None) -> list[dict]:
        """Get quality settings data."""
        if quality_level:
            data = self.csv_loader.get_quality_settings(quality_level)
            if data is not None and not data.empty:
                return data.to_dict("records")

        # Fallback: return all quality levels
        data = self.csv_loader.get_csv_by_name("quality_settings", "orca")
        return data.to_dict("records") if data is not None else []

    def _extract_material_type(self, query: str, context: dict | None = None) -> str | None:
        """Extract material type from query or context."""
        if context and "filament_type" in context:
            return context["filament_type"]

        # Search query for material keywords
        materials = ["PLA", "PLA+", "PETG", "ABS", "ASA", "TPU", "Nylon", "HIPS"]
        query_upper = query.upper()
        for material in materials:
            if material in query_upper:
                return material

        return None

    def _extract_quality_level(self, query: str) -> str | None:
        """Extract quality level from query."""
        levels = ["Draft", "Normal", "Quality", "Fine", "Ultra"]
        query_lower = query.lower()
        for level in levels:
            if level.lower() in query_lower:
                return level
        return None

    def _extract_material_from_vision(self, vision_result: dict) -> str | None:
        """Extract material hint from vision API result."""
        # Check likely causes for material mentions
        causes = " ".join(vision_result.get("likely_causes", []))
        materials = ["PLA", "PETG", "ABS", "ASA", "TPU", "Nylon"]
        for material in materials:
            if material in causes:
                return material
        return None


# Global singleton instance
_router_instance: RouterService | None = None


def get_router_service() -> RouterService:
    """
    Get or create the global router service instance.

    Returns:
        RouterService singleton
    """
    global _router_instance
    if _router_instance is None:
        _router_instance = RouterService()
    return _router_instance
