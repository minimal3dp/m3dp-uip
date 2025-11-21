"""
Diagnosis API Endpoints

Handles image upload, vision analysis, and diagnostic recommendations.
"""

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from app.core.config import settings

router = APIRouter()


class DiagnosisRequest(BaseModel):
    """Request model for text-based diagnosis."""

    description: str
    printer_model: str | None = None
    filament_type: str | None = None
    print_settings: dict | None = None


class DiagnosisResponse(BaseModel):
    """Response model for diagnosis results."""

    issue_type: str  # "Mechanical", "Slicer", "Material"
    classification: str  # e.g., "Under-extrusion", "Layer Shift"
    confidence: float
    recommendations: list[str]
    calculator_needed: str | None = None  # e.g., "rotation_distance"
    csv_reference: str | None = None


@router.post("/analyze/image", response_model=DiagnosisResponse)
async def analyze_image(
    file: UploadFile = File(...),
    _printer_model: str | None = Form(None),
    _filament_type: str | None = Form(None),
):
    """
    Analyze uploaded image for print defects.

    Uses Gemini Vision API to classify the defect and route
    to the appropriate CSV knowledge base.

    Args:
        file: Uploaded image file (JPEG, PNG, WebP)
        _printer_model: Optional printer model for context (unused in stub)
        _filament_type: Optional filament type for context (unused in stub)

    Returns:
        DiagnosisResponse with classification and recommendations

    Raises:
        HTTPException: If file type is invalid or processing fails
    """
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

    # TODO: Implement vision API integration
    # 1. Send image to Gemini Vision API
    # 2. Parse structured JSON response
    # 3. Route to appropriate CSV loader
    # 4. Return recommendations

    # Mock response for now
    return DiagnosisResponse(
        issue_type="Mechanical",
        classification="Under-extrusion",
        confidence=0.85,
        recommendations=[
            "Check extruder rotation distance calibration",
            "Verify hotend temperature is correct for filament",
            "Inspect for partial nozzle clog",
        ],
        calculator_needed="rotation_distance",
        csv_reference="Klipper Calibrations - Extruder Rotation Distance.csv",
    )


@router.post("/analyze/text", response_model=DiagnosisResponse)
async def analyze_text(_request: DiagnosisRequest):
    """
    Analyze text description of print issue.

    Uses NLP to classify the issue and route to appropriate
    knowledge base section.

    Args:
        _request: DiagnosisRequest with issue description and context (unused in stub)

    Returns:
        DiagnosisResponse with classification and recommendations
    """
    # TODO: Implement text analysis
    # 1. Parse description with NLP/embeddings
    # 2. Match to CSV descriptions
    # 3. Return recommendations

    # Mock response for now
    return DiagnosisResponse(
        issue_type="Slicer",
        classification="Poor surface quality",
        confidence=0.75,
        recommendations=[
            "Adjust layer height for better resolution",
            "Enable adaptive layer heights",
            "Reduce print speed for outer walls",
        ],
        calculator_needed=None,
        csv_reference="OrcaSlicer Recommendations - Quality Settings.csv",
    )


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
