"""
Calculator API Endpoints

Implements CSV-driven calibration calculators for Klipper and OrcaSlicer.

Phase 2: Direct translation of CSV formulas to Python logic.
All calculations are formula-based, not LLM-generated.
"""

import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

router = APIRouter()


# ============================================================================
# Pydantic Models - Request/Response
# ============================================================================


class RotationDistanceRequest(BaseModel):
    """Request for rotation distance calculation."""

    current_rotation_distance: float = Field(
        ...,
        gt=0,
        le=100,
        description="Current rotation_distance from printer.cfg",
        examples=[33.5],
    )
    requested_extrusion: float = Field(
        ...,
        gt=0,
        le=500,
        description="Amount of filament requested (usually 100mm)",
        examples=[100],
    )
    actual_extrusion: float = Field(
        ..., gt=0, le=500, description="Measured actual extrusion amount", examples=[98.5]
    )


class RotationDistanceResponse(BaseModel):
    """Response with calculated rotation distance."""

    new_rotation_distance: float = Field(..., description="Corrected rotation distance value")
    change_percent: float = Field(..., description="Percentage change from current value")
    within_tolerance: bool = Field(..., description="Whether change is within ±2mm tolerance")
    klipper_config: str = Field(..., description="Klipper config snippet to copy")
    recommendation: str = Field(..., description="Action recommendation")


class PressureAdvanceRequest(BaseModel):
    """Request for pressure advance calibration guidance."""

    material_type: str = Field(
        ...,
        description="Filament material type",
        examples=["PLA", "PETG", "ABS", "TPU"],
    )
    current_pa: float | None = Field(
        None,
        ge=0,
        le=1,
        description="Current pressure advance value (if known)",
        examples=[0.05],
    )
    print_speed: float = Field(
        100,
        gt=0,
        le=500,
        description="Typical printing speed in mm/s",
        examples=[100],
    )
    nozzle_diameter: float = Field(
        0.4, gt=0, le=2, description="Nozzle diameter in mm", examples=[0.4]
    )


class PressureAdvanceResponse(BaseModel):
    """Response with pressure advance recommendations."""

    recommended_range: tuple[float, float] = Field(
        ..., description="Recommended PA range for material type"
    )
    start_value: float = Field(..., description="Starting PA value for calibration")
    increment: float = Field(..., description="Recommended test increment")
    test_parameters: dict = Field(..., description="Test print parameters")
    klipper_config: str = Field(..., description="Klipper config snippet")
    calibration_method: str = Field(..., description="Link to calibration pattern/method")


class CalculatorListResponse(BaseModel):
    """Response listing available calculators."""

    calculators: list[dict] = Field(..., description="List of available calculators")


# ============================================================================
# Calculator Endpoints
# ============================================================================


@router.get("", response_model=CalculatorListResponse)
async def list_calculators():
    """
    List all available calculators with metadata.

    Returns information about each calculator, its purpose, and CSV source.
    """
    return CalculatorListResponse(
        calculators=[
            {
                "id": "rotation-distance",
                "name": "Extruder Rotation Distance",
                "category": "Mechanical",
                "csv_source": "klipper_calibrations/extruder_rotation_distance.csv",
                "description": "Calculate correct rotation distance for extruder stepper motor",
                "endpoint": "/api/v1/calculators/rotation-distance",
                "method": "POST",
            },
            {
                "id": "pressure-advance",
                "name": "Pressure Advance",
                "category": "Extrusion",
                "csv_source": "klipper_calibrations/pressure_advance.csv",
                "description": "Optimize pressure advance for better corner quality",
                "endpoint": "/api/v1/calculators/pressure-advance",
                "method": "POST",
            },
        ]
    )


@router.post("/rotation-distance", response_model=RotationDistanceResponse)
async def calculate_rotation_distance(request: RotationDistanceRequest):
    """
    Calculate corrected extruder rotation distance.

    **Formula from CSV** (extruder_rotation_distance.csv, row 5):
    ```
    new_rotation_distance = (current * actual_extruded) / requested_extrusion
    ```

    **Calibration Process**:
    1. Mark 120mm from extruder entrance
    2. Command extrusion of 100mm
    3. Measure remaining distance (e.g., 20mm = 100mm extruded, 21.5mm = 98.5mm)
    4. Use actual extruded value in formula

    **Tolerance**: ±2mm from requested (CSV row 6)

    Args:
        request: Current rotation distance and measured extrusion values

    Returns:
        New rotation distance with Klipper config snippet

    Raises:
        HTTPException: If calculation produces invalid result
    """
    logger.info(
        f"Rotation distance calculation: current={request.current_rotation_distance}, "
        f"requested={request.requested_extrusion}, actual={request.actual_extrusion}"
    )

    # Formula: new = (current * actual) / requested
    # This is a direct translation from CSV row 5
    try:
        new_rotation_distance = (
            request.current_rotation_distance * request.actual_extrusion
        ) / request.requested_extrusion

        # Calculate change percentage
        change_percent = (
            (new_rotation_distance - request.current_rotation_distance)
            / request.current_rotation_distance
        ) * 100

        # Check tolerance (±2mm from requested, per CSV row 6)
        deviation = abs(request.actual_extrusion - request.requested_extrusion)
        within_tolerance = deviation <= 2.0

        # Generate Klipper config snippet
        klipper_config = f"rotation_distance: {new_rotation_distance:.3f}"

        # Generate recommendation
        if within_tolerance:
            recommendation = (
                f"✅ Extrusion within tolerance (±2mm). "
                f"Update rotation_distance to {new_rotation_distance:.3f} for optimal accuracy."
            )
        else:
            recommendation = (
                f"⚠️ Extrusion deviation is {deviation:.1f}mm (outside ±2mm tolerance). "
                f"Update rotation_distance to {new_rotation_distance:.3f} and re-calibrate."
            )

        return RotationDistanceResponse(
            new_rotation_distance=round(new_rotation_distance, 3),
            change_percent=round(change_percent, 2),
            within_tolerance=within_tolerance,
            klipper_config=klipper_config,
            recommendation=recommendation,
        )

    except ZeroDivisionError as e:
        logger.error("Division by zero in rotation distance calculation")
        raise HTTPException(status_code=400, detail="Requested extrusion cannot be zero") from e
    except Exception as e:
        logger.error(f"Error calculating rotation distance: {e}")
        raise HTTPException(status_code=500, detail="Calculation error") from e


@router.post("/pressure-advance", response_model=PressureAdvanceResponse)
async def calculate_pressure_advance(request: PressureAdvanceRequest):
    """
    Get pressure advance calibration parameters and recommendations.

    **Material-Specific Ranges** (from CSV row 7):
    - PLA: 0.03 - 0.06
    - PETG: 0.06 - 0.08
    - ABS: 0.04 - 0.07
    - TPU: 0.0 - 0.02 (flexible materials need very low PA)

    **Calibration Method**:
    Uses Klipper's pressure advance pattern:
    1. Print calibration pattern with varying PA values
    2. Visually inspect corners for optimal sharpness
    3. Update printer.cfg with best value

    **Test Parameters** (from CSV rows 2-6):
    - Start PA: 0.0 or current value
    - Increment: 0.005 (0.001-0.01 range)
    - Speed: User-specified (typically 100mm/s)
    - Layer Height: 0.2mm
    - Line Width: Matches nozzle diameter

    Args:
        request: Material type, current PA (optional), and print parameters

    Returns:
        Recommended PA range and calibration test parameters

    Raises:
        HTTPException: If material type is not recognized
    """
    logger.info(
        f"Pressure advance calculation: material={request.material_type}, "
        f"current_pa={request.current_pa}, speed={request.print_speed}"
    )

    # Material-specific PA ranges (from CSV row 7)
    material_ranges = {
        "PLA": (0.03, 0.06),
        "PETG": (0.06, 0.08),
        "ABS": (0.04, 0.07),
        "TPU": (0.0, 0.02),
        "ASA": (0.04, 0.07),  # Similar to ABS
        "NYLON": (0.05, 0.08),
    }

    material_upper = request.material_type.upper()
    if material_upper not in material_ranges:
        raise HTTPException(
            status_code=400,
            detail=f"Material '{request.material_type}' not recognized. "
            f"Supported: {', '.join(material_ranges.keys())}",
        )

    recommended_range = material_ranges[material_upper]

    # Start value: current PA or 0.0 (CSV row 1)
    start_value = request.current_pa if request.current_pa is not None else 0.0

    # Increment: 0.005 is standard (CSV row 2)
    increment = 0.005

    # Test parameters (CSV rows 3-6)
    test_parameters = {
        "start_pa": start_value,
        "end_pa": recommended_range[1] + 0.02,  # Slightly beyond max for comparison
        "increment": increment,
        "speed": request.print_speed,
        "layer_height": 0.2,
        "line_width": request.nozzle_diameter,
        "nozzle_diameter": request.nozzle_diameter,
    }

    # Generate Klipper config snippet
    # Use midpoint of recommended range as starting suggestion
    suggested_pa = sum(recommended_range) / 2
    klipper_config = f"pressure_advance: {suggested_pa:.3f}"

    # Calibration method reference
    calibration_method = (
        "Use Klipper's TUNING_TOWER command or OrcaSlicer's Pressure Advance "
        "calibration pattern. Look for sharpest corners with no bulging."
    )

    return PressureAdvanceResponse(
        recommended_range=recommended_range,
        start_value=round(start_value, 3),
        increment=increment,
        test_parameters=test_parameters,
        klipper_config=klipper_config,
        calibration_method=calibration_method,
    )
