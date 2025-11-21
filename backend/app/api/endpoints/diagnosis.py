"""
Diagnosis API Endpoints

Handles image upload, vision analysis, and diagnostic recommendations.

Phase 2: Integrated with RouterService, VisionService, and SemanticRouter.
"""

import logging

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.core.config import settings
from app.services.router_service import get_router_service

router = APIRouter()
logger = logging.getLogger(__name__)


class DiagnosisRequest(BaseModel):
    """Request model for text-based diagnosis."""

    query: str = Field(..., min_length=1, description="Description of the issue")
    printer_model: str | None = Field(None, description="Printer model (e.g., Ender 3)")
    filament_type: str | None = Field(None, description="Filament type (e.g., PLA, PETG)")
    filament_color: str | None = Field(
        None, description="Filament color (important for dark/shiny filaments)"
    )
    slicer: str | None = Field(None, description="Slicer used (e.g., OrcaSlicer)")
    nozzle_size: float | None = Field(None, description="Nozzle size in mm")


class DiagnosisResponse(BaseModel):
    """Response model for diagnosis results."""

    issue_type: str = Field(..., description="Mechanical, Slicer, Material, or Multi-factor")
    classification: str = Field(..., description="Specific defect classification")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    handler: str = Field(..., description="Handler used: vision_api, csv_lookup, or llm")
    observations: list[str] | None = Field(None, description="Observable issues (vision only)")
    likely_causes: list[str] | None = Field(None, description="Probable root causes")
    recommendations: list[dict] = Field(..., description="CSV-backed recommendations")
    csv_category: str | None = Field(None, description="CSV category used")
    csv_file: str | None = Field(None, description="Specific CSV file used")


@router.post("/analyze/image", response_model=DiagnosisResponse)
async def analyze_image(
    file: UploadFile = File(..., description="Image file (JPEG, PNG, WebP)"),
    printer_model: str | None = Form(None, description="Printer model"),
    filament_type: str | None = Form(None, description="Filament type"),
    filament_color: str | None = Form(None, description="Filament color"),
    slicer: str | None = Form(None, description="Slicer used"),
    nozzle_size: float | None = Form(None, description="Nozzle size (mm)"),
):
    """
    Analyze uploaded image for print defects using Gemini Vision API.

    **Phase 2 Implementation** - Full integration with RouterService and VisionService.

    This endpoint:
    1. Validates the uploaded image
    2. Calls Gemini Vision API for defect classification
    3. Routes to appropriate CSV knowledge base
    4. Returns structured recommendations

    **8-Class Defect Taxonomy** (from research):
    - Spaghetti, Under_Extrusion, Over_Extrusion, Stringing,
    - Layer_Shift, Warping, Ringing, Poor_Bridging, Layer_Separation

    Args:
        file: Uploaded image file (JPEG, PNG, WebP)
        printer_model: Optional printer model for context
        filament_type: Optional filament type (e.g., PLA, PETG)
        filament_color: Optional color (important for dark/shiny filaments)
        slicer: Optional slicer name
        nozzle_size: Optional nozzle diameter in mm

    Returns:
        DiagnosisResponse with classification and CSV-backed recommendations

    Raises:
        HTTPException: If file type is invalid, size too large, or API fails
    """
    logger.info(f"Image analysis request: {file.filename}, type: {file.content_type}")

    # Validate file type
    if file.content_type not in settings.ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(settings.ALLOWED_IMAGE_TYPES)}",
        )

    # Validate file size
    contents = await file.read()
    if len(contents) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size: {settings.MAX_UPLOAD_SIZE / 1024 / 1024}MB",
        )

    # Build context dict
    context = {}
    if printer_model:
        context["printer_model"] = printer_model
    if filament_type:
        context["filament_type"] = filament_type
    if filament_color:
        context["filament_color"] = filament_color
    if slicer:
        context["slicer"] = slicer
    if nozzle_size:
        context["nozzle_size"] = nozzle_size

    # Call router service
    try:
        router_service = get_router_service()
        result = await router_service.diagnose_from_image(
            contents, context=context if context else None
        )

        return DiagnosisResponse(
            issue_type=result["issue_type"],
            classification=result["classification"],
            confidence=result["confidence"],
            handler=result["handler"],
            observations=result.get("observations"),
            likely_causes=result.get("likely_causes"),
            recommendations=result.get("recommendations", []),
            csv_category=result.get("csv_category"),
            csv_file=result.get("csv_file"),
        )
    except ValueError as e:
        logger.error(f"Vision API configuration error: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
    except RuntimeError as e:
        logger.error(f"Vision API runtime error: {e}")
        raise HTTPException(status_code=500, detail=f"Vision API error: {e}") from e
    except Exception as e:
        logger.error(f"Unexpected error in image analysis: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e


@router.post("/analyze/text", response_model=DiagnosisResponse)
async def analyze_text(request: DiagnosisRequest):
    """
    Analyze text description of print issue using Semantic Router.

    **Phase 2 Implementation** - Uses semantic-router for efficient query classification.

    This endpoint:
    1. Classifies query intent using semantic router (fast, cost-effective)
    2. Routes directly to appropriate CSV knowledge base
    3. Returns recommendations without expensive LLM inference

    **Router Categories**:
    - Calibration → klipper_calibrations/
    - Troubleshooting → orca_recommendations/troubleshooting.csv
    - Material → orca_recommendations/material_profiles.csv
    - Quality → orca_recommendations/quality_settings.csv
    - General → LLM fallback (not yet implemented)

    Args:
        request: DiagnosisRequest with issue description and context

    Returns:
        DiagnosisResponse with classification and CSV-backed recommendations

    Raises:
        HTTPException: If query processing fails
    """
    logger.info(f"Text analysis request: {request.query[:100]}...")

    # Build context dict
    context = {}
    if request.printer_model:
        context["printer_model"] = request.printer_model
    if request.filament_type:
        context["filament_type"] = request.filament_type
    if request.filament_color:
        context["filament_color"] = request.filament_color
    if request.slicer:
        context["slicer"] = request.slicer
    if request.nozzle_size:
        context["nozzle_size"] = request.nozzle_size

    # Call router service
    try:
        router_service = get_router_service()
        result = await router_service.diagnose_from_text(
            request.query, context=context if context else None
        )

        return DiagnosisResponse(
            issue_type=result.get("issue_type", result["classification"]),
            classification=result["classification"],
            confidence=result["confidence"],
            handler=result["handler"],
            observations=result.get("observations"),
            likely_causes=result.get("likely_causes"),
            recommendations=result.get("recommendations", []),
            csv_category=result.get("csv_category"),
            csv_file=result.get("csv_file"),
        )
    except Exception as e:
        logger.error(f"Error in text analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Text analysis error: {e}") from e


@router.get("/calculators")
async def list_calculators():
    """
    List available calculators and their CSV sources.

    Returns metadata about each calculator type available.
    """
    return {
        "calculators": [
            {
                "id": "rotation_distance",
                "name": "Extruder Rotation Distance",
                "category": "Mechanical",
                "csv_source": "Klipper Calibrations - Extruder Rotation Distance.csv",
                "description": "Calculate correct rotation distance for extruder stepper motor",
            },
            {
                "id": "pressure_advance",
                "name": "Pressure Advance",
                "category": "Mechanical",
                "csv_source": "Klipper Calibrations - Pressure Advance.csv",
                "description": "Optimize pressure advance for better corner quality",
            },
            {
                "id": "flow_rate",
                "name": "Flow Rate",
                "category": "Material",
                "csv_source": "Klipper Calibrations - Flow Rate.csv",
                "description": "Calculate correct flow multiplier for filament",
            },
        ]
    }
