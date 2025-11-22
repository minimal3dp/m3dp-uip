"""
Calculator API Endpoints

Implements CSV-driven calibration calculators for Klipper and OrcaSlicer.

Phase 2: Direct translation of CSV formulas to Python logic.
All calculations are formula-based, not LLM-generated.
"""

import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.csv_loader import get_csv_loader
from app.services.ga4_tracker import track_calculator_use

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


class OrcaSlicerFlowRequest(BaseModel):
    """Request for OrcaSlicer Flow Rate calibration (two-pass method)."""

    old_flow_rate: float = Field(
        1.0,
        gt=0,
        le=2,
        description="Current flow rate from slicer (1.0 = 100%)",
        examples=[0.99],
    )
    pass_1_slide_value: float = Field(
        ...,
        ge=-50,
        le=50,
        description="Slide number with smoothest surface from Pass 1 (e.g., -10 for 90% slide)",
        examples=[-10],
    )
    pass_2_slide_value: float | None = Field(
        None,
        ge=-50,
        le=50,
        description="Slide number with smoothest surface from Pass 2 (optional for Pass 1 calculation)",
        examples=[-1],
    )


class OrcaSlicerFlowYoloRequest(BaseModel):
    """Request for OrcaSlicer Flow Rate YOLO calibration (single-pass method)."""

    old_flow_rate: float = Field(
        1.0,
        gt=0,
        le=2,
        description="Current flow rate from slicer (1.0 = 100%)",
        examples=[1.0],
    )
    yolo_slide_value: float = Field(
        ...,
        ge=-1,
        le=1,
        description="Slide value with smoothest surface from YOLO test (e.g., -0.035)",
        examples=[-0.035],
    )


class OrcaSlicerFlowResponse(BaseModel):
    """Response with calculated OrcaSlicer flow rate."""

    pass_1_flow: float = Field(..., description="Flow rate after Pass 1")
    pass_2_flow: float | None = Field(
        None, description="Final flow rate after Pass 2 (if provided)"
    )
    change_from_original: float = Field(
        ..., description="Percentage change from original flow rate"
    )
    slicer_config: str = Field(..., description="Slicer config value to copy")
    recommendation: str = Field(..., description="Action recommendation")


class OrcaSlicerFlowYoloResponse(BaseModel):
    """Response with calculated OrcaSlicer YOLO flow rate."""

    new_flow: float = Field(..., description="New flow rate after YOLO calibration")
    change_from_original: float = Field(
        ..., description="Percentage change from original flow rate"
    )
    slicer_config: str = Field(..., description="Slicer config value to copy")
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
                "id": "orcaslicer-flow",
                "name": "OrcaSlicer Flow Rate (Recommended)",
                "category": "Extrusion",
                "csv_source": "klipper_calibrations/flow_calibration.csv",
                "description": "Two-pass flow calibration using OrcaSlicer's built-in tool",
                "endpoint": "/api/v1/calculators/orcaslicer-flow",
                "method": "POST",
            },
            {
                "id": "orcaslicer-flow-yolo",
                "name": "OrcaSlicer Flow YOLO (Quick)",
                "category": "Extrusion",
                "csv_source": "klipper_calibrations/orcaslicer_flow_yolo.csv",
                "description": "Single-pass quick flow calibration for fast adjustments",
                "endpoint": "/api/v1/calculators/orcaslicer-flow-yolo",
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
            {
                "id": "input-shaping",
                "name": "Input Shaping",
                "category": "Mechanical",
                "csv_source": "klipper_calibrations/input_shaping.csv",
                "description": "Recommend input shaper types based on resonance frequencies",
                "endpoint": "/api/v1/calculators/input-shaping",
                "method": "POST",
            },
        ]
    )


class InputShapingRequest(BaseModel):
    """Request for input shaping recommendations.

    CSV: input_shaping.csv rows for X/Y Frequency and Shaper options.
    Frequencies measured via accelerometer (ADXL345) or manual test.
    """

    test_type: str = Field(
        "ADXL345",
        description="Test method used (manual or ADXL345)",
        examples=["ADXL345"],
    )
    x_frequency: float = Field(
        ...,
        gt=10,
        le=200,
        description="Measured resonance frequency for X axis (Hz)",
        examples=[45.2],
    )
    y_frequency: float = Field(
        ...,
        gt=10,
        le=200,
        description="Measured resonance frequency for Y axis (Hz)",
        examples=[37.8],
    )


class InputShapingResponse(BaseModel):
    """Response with recommended shaper types and config."""

    shaper_x: str = Field(..., description="Recommended shaper for X axis")
    shaper_y: str = Field(..., description="Recommended shaper for Y axis")
    max_accel: int = Field(..., description="Suggested max acceleration (mm/s²)")
    square_corner_velocity: float = Field(
        ..., description="Suggested square corner velocity (mm/s)"
    )
    klipper_config: str = Field(..., description="Klipper config snippet to copy")
    notes: str = Field(..., description="Additional tuning notes")


@router.post("/input-shaping", response_model=InputShapingResponse)
async def calculate_input_shaping(request: InputShapingRequest):
    """Recommend input shaper types based on resonance frequencies.

    Placeholder heuristic until CSV formulas finalized (input_shaping.csv).
    Mapping (temporary, reference Klipper docs):
    - freq < 40 Hz -> EI (strong damping)
    - 40-50 Hz -> MZV (balanced)
    - 50-60 Hz -> 2HUMP_EI (higher frequency compensation)
    - > 60 Hz -> 3HUMP_EI (broad suppression)

    Acceleration suggestion (rough heuristic):
    max_accel = min(int(min(request.x_frequency, request.y_frequency) * 100), 10000)
    square_corner_velocity fixed at 5.0 (from CSV).
    """
    logger.info(
        f"Input shaping calculation: test_type={request.test_type}, x_freq={request.x_frequency}, y_freq={request.y_frequency}"
    )

    loader = get_csv_loader()
    df = loader.get_input_shaping_data()

    # Expected DataFrame rows (after comments stripped):
    # index 0: Test Type (CSV line 5)
    # index 1: X Frequency (CSV line 6)
    # index 2: Y Frequency (CSV line 7)
    # index 3: X Shaper (CSV line 8)
    # index 4: Y Shaper (CSV line 9)
    # index 5: Max Accel (CSV line 10)
    # index 6: Square Corner Velocity (CSV line 11)
    if df is None:
        # Fallback to heuristic if CSV missing
        logger.warning("input_shaping.csv not loaded; using heuristic fallback")

        def pick_shaper(freq: float) -> str:
            if freq < 40:
                return "EI"
            if freq < 50:
                return "MZV"
            if freq < 60:
                return "2HUMP_EI"
            return "3HUMP_EI"

        shaper_x = pick_shaper(request.x_frequency)
        shaper_y = pick_shaper(request.y_frequency)
        base_freq = min(request.x_frequency, request.y_frequency)
        max_accel = min(int(base_freq * 100), 8000)
        square_corner_velocity = 5.0
    else:
        # Extract shaper option lists from Notes column (rows 3 & 4)
        try:
            x_shaper_row = df.iloc[3]  # row index 3
            scv_row = df.iloc[6]  # row index 6 (Square Corner Velocity)
        except Exception as e:
            logger.error(f"Malformed input_shaping.csv: {e}")
            raise HTTPException(status_code=500, detail="Malformed input_shaping.csv") from e

        def parse_options(notes: str) -> list[str]:
            # Notes format: "Options: MZV, ZV, EI, 2HUMP_EI, 3HUMP_EI"
            if not isinstance(notes, str) or "Options:" not in notes:
                return []
            return [opt.strip() for opt in notes.split("Options:")[-1].split(",") if opt.strip()]

        shaper_options = parse_options(x_shaper_row.get("Notes", "")) or [
            "MZV",
            "ZV",
            "EI",
            "2HUMP_EI",
            "3HUMP_EI",
        ]

        # Frequency segmentation derived from expected range (rows 1 & 2: 30-80 Hz)
        # Strategy: lower frequencies need more damping (EI), mid range MZV/ZV, higher multihump EI variants.
        def pick_from_options(freq: float) -> str:
            if freq < 40 and "EI" in shaper_options:
                return "EI"
            if 40 <= freq < 50 and "MZV" in shaper_options:
                return "MZV"
            if 50 <= freq < 60 and "2HUMP_EI" in shaper_options:
                return "2HUMP_EI"
            if freq >= 60 and "3HUMP_EI" in shaper_options:
                return "3HUMP_EI"
            # Fallback first option
            return shaper_options[0]

        shaper_x = pick_from_options(request.x_frequency)
        shaper_y = pick_from_options(request.y_frequency)

        # Max accel heuristic clamped by CSV expected range (row 5 Expected_Range: 1000-10000)
        base_freq = min(request.x_frequency, request.y_frequency)
        suggested_accel = int(base_freq * 120)  # Slightly more aggressive than *100
        max_accel = max(1000, min(suggested_accel, 10000))

        # Square corner velocity from Formula column of row 6 (value 5.0)
        square_corner_velocity = float(scv_row.get("Formula", 5.0))

    klipper_config = (
        f"[input_shaper]\n"  # Section header
        f"shaper_type_x: {shaper_x}\n"
        f"shaper_freq_x: {request.x_frequency:.1f}\n"
        f"shaper_type_y: {shaper_y}\n"
        f"shaper_freq_y: {request.y_frequency:.1f}\n"
        f"max_accel: {max_accel}\n"
        f"square_corner_velocity: {square_corner_velocity:.1f}"
    )

    notes = (
        "Frequencies sourced from input_shaping.csv (lines 6-7). Shaper options from lines 8-9. "
        "Acceleration bounded by line 10 expected range. Square corner velocity from line 11."
        " Run SHAPER_CALIBRATE for precise measurements before applying final config."
    )

    # Track calculator usage
    await track_calculator_use(
        "input_shaping",
        params={
            "shaper_x": shaper_x,
            "shaper_y": shaper_y,
            "max_accel": max_accel,
        },
    )

    return InputShapingResponse(
        shaper_x=shaper_x,
        shaper_y=shaper_y,
        max_accel=max_accel,
        square_corner_velocity=square_corner_velocity,
        klipper_config=klipper_config,
        notes=notes,
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

        # Track calculator usage
        await track_calculator_use(
            "rotation_distance",
            params={
                "within_tolerance": within_tolerance,
                "change_percent": round(change_percent, 2),
            },
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


@router.post("/orcaslicer-flow", response_model=OrcaSlicerFlowResponse)
async def calculate_orcaslicer_flow(request: OrcaSlicerFlowRequest):
    """
    Calculate OrcaSlicer Flow Rate using two-pass method (RECOMMENDED).

    **Formulas from CSV** (flow_calibration.csv, rows 5-6):
    ```
    pass_1_flow = old_flow_rate * (100 + pass_1_slide_value) / 100
    pass_2_flow = pass_1_flow * (100 + pass_2_slide_value) / 100
    ```

    **Calibration Process**:
    1. Open OrcaSlicer -> Calibration -> Flow Rate -> Pass 1
    2. Print the calibration model
    3. Feel each slide and determine the smoothest surface
    4. Note the slide number (e.g., -10 for 90% slide)
    5. Calculate Pass 1 flow rate
    6. Run Pass 2 with Pass 1 flow rate
    7. Enter Pass 2 slide value for final flow rate

    **Why Two-Pass?**: More accurate than single-pass methods.
    First pass gets you close, second pass fine-tunes.

    Args:
        request: Current flow rate and Pass 1/2 slide values

    Returns:
        Pass 1 and Pass 2 (if provided) flow rates with slicer config

    Raises:
        HTTPException: If calculation produces invalid result
    """
    logger.info(
        f"OrcaSlicer Flow: old_flow={request.old_flow_rate}, "
        f"pass_1_slide={request.pass_1_slide_value}, pass_2_slide={request.pass_2_slide_value}"
    )

    try:
        # Formula: pass_1_flow = old_flow_rate * (100 + pass_1_slide_value) / 100
        # From CSV row 5 (B20)
        pass_1_flow = request.old_flow_rate * (100 + request.pass_1_slide_value) / 100

        # If Pass 2 slide value provided, calculate final flow
        pass_2_flow = None
        if request.pass_2_slide_value is not None:
            # Formula: pass_2_flow = pass_1_flow * (100 + pass_2_slide_value) / 100
            # From CSV row 6 (B27)
            pass_2_flow = pass_1_flow * (100 + request.pass_2_slide_value) / 100

        # Determine which flow to use for config
        final_flow = pass_2_flow if pass_2_flow is not None else pass_1_flow

        # Calculate change from original
        change_from_original = ((final_flow - request.old_flow_rate) / request.old_flow_rate) * 100

        # Generate slicer config
        slicer_config = f"Flow Rate: {final_flow:.3f}"

        # Generate recommendation
        if request.pass_2_slide_value is None:
            recommendation = (
                f"✅ Pass 1 complete. Flow rate: {pass_1_flow:.3f} "
                f"({change_from_original:+.1f}% from original). "
                f"Run Pass 2 with this flow rate for final calibration."
            )
        else:
            recommendation = (
                f"✅ Calibration complete! Final flow rate: {pass_2_flow:.3f} "
                f"({change_from_original:+.1f}% from original). "
                f"Update your OrcaSlicer filament profile with this value."
            )

        # Track calculator usage
        await track_calculator_use(
            "orcaslicer_flow",
            params={
                "pass_2_completed": pass_2_flow is not None,
                "change_from_original": round(change_from_original, 2),
            },
        )

        return OrcaSlicerFlowResponse(
            pass_1_flow=round(pass_1_flow, 3),
            pass_2_flow=round(pass_2_flow, 3) if pass_2_flow is not None else None,
            change_from_original=round(change_from_original, 2),
            slicer_config=slicer_config,
            recommendation=recommendation,
        )

    except Exception as e:
        logger.error(f"Error calculating OrcaSlicer flow: {e}")
        raise HTTPException(status_code=500, detail="Calculation error") from e


@router.post("/orcaslicer-flow-yolo", response_model=OrcaSlicerFlowYoloResponse)
async def calculate_orcaslicer_flow_yolo(request: OrcaSlicerFlowYoloRequest):
    """
    Calculate OrcaSlicer Flow Rate using YOLO method (single-pass, quick).

    **Formula from CSV** (orcaslicer_flow_yolo.csv, row 4):
    ```
    new_flow = old_flow_rate + yolo_slide_value
    ```

    **Calibration Process**:
    1. Open OrcaSlicer -> Calibration -> Flow Rate -> YOLO
    2. Print the calibration model
    3. Feel each slide and determine the smoothest surface
    4. Note the slide value (e.g., -0.035)
    5. Calculate new flow rate (direct addition)

    **Why YOLO?**: Faster than two-pass method.
    Use when time is limited or for quick adjustments.

    **Note**: YOLO is less accurate than two-pass method.
    Use two-pass for best results.

    Args:
        request: Current flow rate and YOLO slide value

    Returns:
        New flow rate with slicer config

    Raises:
        HTTPException: If calculation produces invalid result
    """
    logger.info(
        f"OrcaSlicer Flow YOLO: old_flow={request.old_flow_rate}, "
        f"yolo_slide={request.yolo_slide_value}"
    )

    try:
        # Formula: new_flow = old_flow_rate + yolo_slide_value
        # From CSV row 4 (B20)
        new_flow = request.old_flow_rate + request.yolo_slide_value

        # Calculate change from original
        change_from_original = ((new_flow - request.old_flow_rate) / request.old_flow_rate) * 100

        # Generate slicer config
        slicer_config = f"Flow Rate: {new_flow:.3f}"

        # Generate recommendation
        recommendation = (
            f"✅ YOLO calibration complete! New flow rate: {new_flow:.3f} "
            f"({change_from_original:+.1f}% from original). "
            f"Update your OrcaSlicer filament profile. "
            f"For best accuracy, consider running the two-pass calibration."
        )

        # Track calculator usage
        await track_calculator_use(
            "orcaslicer_flow_yolo",
            params={
                "change_from_original": round(change_from_original, 2),
            },
        )

        return OrcaSlicerFlowYoloResponse(
            new_flow=round(new_flow, 3),
            change_from_original=round(change_from_original, 2),
            slicer_config=slicer_config,
            recommendation=recommendation,
        )

    except Exception as e:
        logger.error(f"Error calculating OrcaSlicer flow YOLO: {e}")
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

    # CSV-driven material ranges:
    # pressure_advance.csv row 'Material Type' Notes column format:
    # "PLA: 0.03-0.06, PETG: 0.06-0.08, ABS: 0.04-0.07" (additional materials appended below)
    loader = get_csv_loader()
    material_ranges: dict[str, tuple[float, float]] = {}
    try:
        pa_df = loader.get_pressure_advance_formula()
        if pa_df is not None:
            material_row = pa_df[pa_df["Name"] == "Material Type"].iloc[0]
            notes = str(material_row.get("Notes", ""))
            # Parse patterns Material: min-max
            for part in [p.strip() for p in notes.split(",") if p.strip()]:
                if ":" in part and "-" in part:
                    mat, rng = [x.strip() for x in part.split(":", 1)]
                    try:
                        low_s, high_s = [x.strip() for x in rng.split("-")]
                        low = float(low_s)
                        high = float(high_s)
                        material_ranges[mat.upper()] = (low, high)
                    except ValueError:
                        logger.debug(f"Failed to parse range segment '{part}'")
        # Extend with additional materials not present (domain knowledge)
        material_ranges.setdefault("TPU", (0.0, 0.02))
        material_ranges.setdefault("ASA", material_ranges.get("ABS", (0.04, 0.07)))
        material_ranges.setdefault("NYLON", (0.05, 0.08))
    except Exception as e:
        logger.warning(f"CSV-driven material range parsing failed: {e}; falling back to defaults")
        material_ranges = {
            "PLA": (0.03, 0.06),
            "PETG": (0.06, 0.08),
            "ABS": (0.04, 0.07),
            "TPU": (0.0, 0.02),
            "ASA": (0.04, 0.07),
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

    # Track calculator usage
    await track_calculator_use(
        "pressure_advance",
        params={
            "material_type": material_upper,
            "recommended_range": f"{recommended_range[0]:.3f}-{recommended_range[1]:.3f}",
        },
    )

    return PressureAdvanceResponse(
        recommended_range=recommended_range,
        start_value=round(start_value, 3),
        increment=increment,
        test_parameters=test_parameters,
        klipper_config=klipper_config,
        calibration_method=calibration_method,
    )
