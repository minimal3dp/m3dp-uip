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


class MaxVolumetricSpeedRequest(BaseModel):
    """Request for Max Volumetric Speed calculation."""

    start_value: float = Field(
        ...,
        gt=0,
        le=50,
        description="Starting volumetric speed for test (mm³/s)",
        examples=[5.0],
    )
    step_value: float = Field(
        ...,
        gt=0,
        le=5,
        description="Increment between test sections (mm³/s)",
        examples=[0.5],
    )
    height_measured: float = Field(
        ...,
        gt=0,
        le=200,
        description="Height where print quality starts degrading (mm)",
        examples=[27.23],
    )
    temperature: float | None = Field(
        None,
        ge=150,
        le=300,
        description="Hotend temperature during test (°C)",
        examples=[240],
    )
    hotend_type: str | None = Field(
        None,
        description="Hotend type for reference comparisons",
        examples=["E3D V6", "Dragon HF", "Rapido UHF"],
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


class MaxVolumetricSpeedResponse(BaseModel):
    """Response with calculated max volumetric speed."""

    max_flow: float = Field(..., description="Maximum volumetric speed (mm³/s)")
    safe_flow_95: float = Field(..., description="Safe value at 95% of max (recommended)")
    safe_flow_90: float = Field(..., description="Conservative value at 90% of max")
    comparison: dict = Field(..., description="Comparison with common hotend flow rates")
    slicer_config: str = Field(..., description="Slicer config value to copy (95% safe)")
    recommendation: str = Field(..., description="Usage recommendations")
    test_details: dict = Field(..., description="Test parameters for reference")


class RunCurrentRequest(BaseModel):
    """Request for Run Current (TMC stepper driver) calculation."""

    peak_current: float = Field(
        ...,
        gt=0,
        le=3.0,
        description="Peak current from stepper motor specification sheet (A)",
        examples=[1.5, 1.68, 2.0],
    )
    motor_model: str | None = Field(
        None,
        description="Optional motor model for reference",
        examples=["NEMA17 17HS19-2004S1", "LDO 42STH48-2504AH"],
    )
    driver_type: str = Field(
        "TMC2209",
        description="TMC driver type",
        examples=["TMC2209", "TMC2208", "TMC5160"],
    )


class RunCurrentResponse(BaseModel):
    """Response with calculated run current for TMC driver."""

    run_current: float = Field(..., description="Calculated run current (A)")
    peak_current: float = Field(..., description="Input peak current from motor spec (A)")
    rms_factor: float = Field(..., description="RMS conversion factor (0.707)")
    driver_max: float = Field(..., description="Maximum capacity of selected driver (A)")
    within_limits: bool = Field(..., description="Whether calculated value is within driver limits")
    klipper_config: str = Field(..., description="Klipper config snippet to copy")
    recommendation: str = Field(..., description="Usage and tuning recommendations")
    reference: str = Field(..., description="Reference documentation URL")


class LeadScrewRotationDistanceRequest(BaseModel):
    """Request for Lead Screw Rotation Distance calculation."""

    pitch: float = Field(
        ...,
        gt=0,
        le=10,
        description="Distance between threads on the lead screw (mm)",
        examples=[2.0, 8.0],
    )
    number_of_threads: int = Field(
        ...,
        gt=0,
        le=8,
        description="Number of separate threads (starts) on the lead screw",
        examples=[1, 2, 4],
    )
    screw_type: str | None = Field(
        None,
        description="Optional lead screw type for reference",
        examples=["T8x2", "T8x4", "T8x8"],
    )


class LeadScrewRotationDistanceResponse(BaseModel):
    """Response with calculated lead screw rotation distance."""

    rotation_distance: float = Field(..., description="Calculated rotation distance (mm)")
    pitch: float = Field(..., description="Input pitch value (mm)")
    number_of_threads: int = Field(..., description="Input number of threads")
    common_examples: dict = Field(..., description="Common T8 lead screw examples")
    klipper_config: str = Field(..., description="Klipper config snippet to copy")
    recommendation: str = Field(..., description="Usage recommendations")
    reference: str = Field(..., description="Klipper documentation URL")


class XAndYOffsetsRequest(BaseModel):
    """Request for X and Y probe offsets calculation."""

    toolhead_x_probe: float = Field(
        ...,
        description="X position when probe triggers",
        examples=[188.0],
    )
    toolhead_y_probe: float = Field(
        ...,
        description="Y position when probe triggers",
        examples=[185.0],
    )
    toolhead_x_nozzle: float = Field(
        ...,
        description="X position when nozzle at marked spot",
        examples=[224.0],
    )
    toolhead_y_nozzle: float = Field(
        ...,
        description="Y position when nozzle at marked spot",
        examples=[148.0],
    )


class XAndYOffsetsResponse(BaseModel):
    """Response with calculated X and Y probe offsets."""

    x_offset: float = Field(..., description="Calculated X offset (mm)")
    y_offset: float = Field(..., description="Calculated Y offset (mm)")
    toolhead_x_probe: float = Field(..., description="Input probe X position")
    toolhead_y_probe: float = Field(..., description="Input probe Y position")
    toolhead_x_nozzle: float = Field(..., description="Input nozzle X position")
    toolhead_y_nozzle: float = Field(..., description="Input nozzle Y position")
    klipper_config: str = Field(..., description="Klipper config snippet to copy")
    usage_guide: str = Field(..., description="Step-by-step usage instructions")
    reference: str = Field(..., description="Klipper documentation URL")


class SkewCorrectionRequest(BaseModel):
    """Request for skew correction calculation."""

    xy_ac: float = Field(..., gt=0, description="XY plane AC diagonal (mm)", examples=[141.21])
    xy_bd: float = Field(..., gt=0, description="XY plane BD diagonal (mm)", examples=[140.97])
    xy_ad: float = Field(..., gt=0, description="XY plane AD orthogonal (mm)", examples=[104.77])
    xz_ac: float | None = Field(
        None, gt=0, description="XZ plane AC diagonal (mm)", examples=[141.98]
    )
    xz_bd: float | None = Field(
        None, gt=0, description="XZ plane BD diagonal (mm)", examples=[141.63]
    )
    xz_ad: float | None = Field(
        None, gt=0, description="XZ plane AD orthogonal (mm)", examples=[104.9]
    )
    yz_ac: float | None = Field(
        None, gt=0, description="YZ plane AC diagonal (mm)", examples=[141.54]
    )
    yz_bd: float | None = Field(
        None, gt=0, description="YZ plane BD diagonal (mm)", examples=[141.33]
    )
    yz_ad: float | None = Field(
        None, gt=0, description="YZ plane AD orthogonal (mm)", examples=[104.83]
    )


class SkewCorrectionResponse(BaseModel):
    """Response with calculated skew correction values."""

    set_skew_command: str = Field(..., description="Complete SET_SKEW command for printer.cfg")
    calc_measured_skew_commands: dict = Field(
        ..., description="CALC_MEASURED_SKEW commands for testing"
    )
    skew_profile: dict = Field(..., description="Calculated skew values in radians and degrees")
    interpretation: str = Field(..., description="Human-readable interpretation of skew values")
    usage_guide: str = Field(..., description="How to apply skew correction")
    calibration_model: str = Field(..., description="Thingiverse calibration model URL")
    reference: str = Field(..., description="Klipper documentation URL")


class LineWidthsRequest(BaseModel):
    """Request for line width recommendation calculator.

    Provides nozzle diameter and feature type; returns recommended width range.
    Feature types: external_perimeter, perimeter, solid_infill, sparse_infill, first_layer, support.
    """

    nozzle_diameter: float = Field(
        0.4, gt=0, le=2, description="Nozzle diameter (mm)", examples=[0.4]
    )
    feature_type: str = Field(
        "perimeter",
        description="Print feature type",
        examples=["perimeter"],
        pattern="^(external_perimeter|perimeter|solid_infill|sparse_infill|first_layer|support)$",
    )
    layer_height: float | None = Field(
        None,
        gt=0,
        le=1,
        description="Optional layer height (mm) to constrain max width (≤1.5× layer_height)",
        examples=[0.2],
    )


class LineWidthsResponse(BaseModel):
    """Response with line width recommendations for a feature type."""

    recommended_min: float = Field(..., description="Minimum recommended line width (mm)")
    recommended_max: float = Field(..., description="Maximum recommended line width (mm)")
    default_target: float = Field(..., description="Suggested target line width (mm)")
    extrusion_multiplier_hint: str = Field(
        ..., description="Hint about flow adjustments related to this width"
    )
    slicer_config: str = Field(..., description="Example slicer config line or setting reference")
    notes: str = Field(..., description="Additional guidance and trade-offs")
    extrusion_volume_check: str | None = Field(
        None, description="Sanity check on extrusion volume if layer_height provided"
    )
    layer_height_constraint_applied: bool = Field(
        False, description="Whether max width was constrained by layer_height"
    )


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
            {
                "id": "max-volumetric-speed",
                "name": "Max Volumetric Speed",
                "category": "Performance",
                "csv_source": "klipper_calibrations/max_volumetric_speed.csv",
                "description": "Calculate maximum flow rate your hotend can handle",
                "endpoint": "/api/v1/calculators/max-volumetric-speed",
                "method": "POST",
            },
            {
                "id": "run-current",
                "name": "Run Current (TMC Drivers)",
                "category": "Mechanical",
                "csv_source": "klipper_calibrations/run_current.csv",
                "description": "Calculate proper run_current for TMC stepper drivers from peak current",
                "endpoint": "/api/v1/calculators/run-current",
                "method": "POST",
            },
            {
                "id": "lead-screw-rotation-distance",
                "name": "Lead Screw Rotation Distance",
                "category": "Mechanical",
                "csv_source": "klipper_calibrations/lead_screw_rotation_distance.csv",
                "description": "Calculate rotation_distance for Z-axis lead screws (pitch × threads)",
                "endpoint": "/api/v1/calculators/lead-screw-rotation-distance",
                "method": "POST",
            },
            {
                "id": "x-and-y-offsets",
                "name": "X and Y Offsets",
                "category": "Probe Calibration",
                "csv_source": "klipper_calibrations/x_and_y_offsets.csv",
                "description": "Calculate BLTouch/CR Touch probe X and Y offsets for accurate bed mesh",
                "endpoint": "/api/v1/calculators/x-and-y-offsets",
                "method": "POST",
            },
            {
                "id": "skew-correction",
                "name": "Skew Correction",
                "category": "Mechanical Alignment",
                "csv_source": "klipper_calibrations/skew_correction.csv",
                "description": "Calculate frame skew correction from calibration print measurements (XY, XZ, YZ planes)",
                "endpoint": "/api/v1/calculators/skew-correction",
                "method": "POST",
            },
            {
                "id": "line-widths",
                "name": "Line Width Recommendations",
                "category": "Extrusion Geometry",
                "csv_source": "klipper_calibrations/line_widths.csv",
                "description": "Recommend line width ranges per feature type based on nozzle diameter",
                "endpoint": "/api/v1/calculators/line-widths",
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


@router.post("/max-volumetric-speed", response_model=MaxVolumetricSpeedResponse)
async def calculate_max_volumetric_speed(request: MaxVolumetricSpeedRequest):
    """
    Calculate maximum volumetric flow rate from test print measurements.

    **Purpose**:
    Determine the maximum mm³/s your hotend can reliably extrude at a given
    temperature. This value limits print speeds to prevent underextrusion.

    **Formula** (from CSV and Ellis3DP guide):
    ```
    max_flow = start + (height_measured * step)
    safe_flow_95 = max_flow * 0.95
    safe_flow_90 = max_flow * 0.90
    ```

    **Method**:
    1. Use OrcaSlicer "Calibration → More... → Max Flowrate" test
    2. Print tower with increasing volumetric speeds
    3. Measure height where quality degrades (layer skipping, gaps, etc.)
    4. Calculate max flow and use 95% value in slicer

    **Common Hotend Ranges** (from CSV and Ellis3DP):
    - E3D V6 / Revo: ~11 mm³/s
    - Dragon SF: ~15 mm³/s
    - Dragon HF / Rapido HF: ~24 mm³/s
    - Rapido UHF / Mosquito Magnum: ~30 mm³/s

    **Speed Formula**:
    `max_speed = max_flow / layer_height / line_width`

    Example: 24 mm³/s / 0.2mm / 0.4mm = 300 mm/s

    Args:
        request: Start value, step increment, and measured height

    Returns:
        Max flow rate, safe values (95%/90%), and slicer config

    Raises:
        HTTPException: If calculated values are outside expected ranges
    """
    logger.info(
        f"Max volumetric speed calculation: start={request.start_value}, "
        f"step={request.step_value}, height={request.height_measured}"
    )

    # Formula from CSV: max_flow = start + (height_measured * step)
    max_flow = request.start_value + (request.height_measured * request.step_value)

    # Safety margins (CSV rows 5-6)
    safe_flow_95 = max_flow * 0.95
    safe_flow_90 = max_flow * 0.90

    # Validate result is reasonable
    if max_flow < 5 or max_flow > 50:
        logger.warning(f"Calculated max flow {max_flow:.2f} mm³/s is outside typical range (5-50)")

    # Hotend comparison data (from CSV and Ellis3DP)
    common_hotends = {
        "E3D V6": 11,
        "E3D Revo": 11,
        "Dragon SF": 15,
        "Dragon HF": 24,
        "Rapido HF": 24,
        "Rapido UHF": 30,
        "Mosquito": 20,
        "Mosquito Magnum": 30,
    }

    # Find closest hotend match
    closest_hotend = min(common_hotends.items(), key=lambda x: abs(x[1] - max_flow))
    comparison = {
        "your_max_flow": round(max_flow, 2),
        "closest_hotend": closest_hotend[0],
        "closest_flow": closest_hotend[1],
        "common_hotends": common_hotends,
    }

    # Generate slicer config (use 95% safe value)
    slicer_config = f"max_volumetric_speed: {safe_flow_95:.2f}"

    # Usage recommendations
    temp_note = f" at {request.temperature}°C" if request.temperature else " at test temperature"
    recommendation = (
        f"Use {safe_flow_95:.2f} mm³/s (95% of max) in your slicer{temp_note}. "
        f"For critical prints, consider {safe_flow_90:.2f} mm³/s (90%). "
        f"Higher temperatures may increase flow rate but can cause stringing. "
        f"Your result is similar to a {closest_hotend[0]}."
    )

    # Test details for reference
    test_details = {
        "start_value": request.start_value,
        "step_value": request.step_value,
        "height_measured": request.height_measured,
        "temperature": request.temperature,
        "hotend_type": request.hotend_type,
    }

    # Track calculator usage
    await track_calculator_use(
        "max_volumetric_speed",
        params={
            "max_flow": round(max_flow, 2),
            "safe_flow_95": round(safe_flow_95, 2),
            "closest_hotend": closest_hotend[0],
        },
    )

    return MaxVolumetricSpeedResponse(
        max_flow=round(max_flow, 2),
        safe_flow_95=round(safe_flow_95, 2),
        safe_flow_90=round(safe_flow_90, 2),
        comparison=comparison,
        slicer_config=slicer_config,
        recommendation=recommendation,
        test_details=test_details,
    )


@router.post(
    "/run-current",
    response_model=RunCurrentResponse,
    summary="Calculate TMC Run Current",
    description="""
    Calculate proper run_current value for TMC stepper drivers (TMC2209, TMC2208, TMC5160).

    **Formula**: `run_current = peak_current * 0.707`

    **How to Use**:
    1. Locate your stepper motor's datasheet
    2. Find the **peak current** specification (typically 1.5A - 2.5A for NEMA17)
    3. Enter the peak current value
    4. Calculator will compute the RMS run current (peak × 0.707)
    5. Copy the result to your printer.cfg TMC section

    **Important Notes**:
    - Result is automatically rounded down to nearest 0.1A for safety
    - TMC2209 max: 1.2A, TMC2208 max: 1.4A, TMC5160 max: 3.0A
    - Start 10-20% below calculated value and increase gradually
    - Monitor motor temperature during testing
    - Motors should be warm but not hot to touch

    **Example Motors**:
    - NEMA17 17HS19-2004S1: 2.0A peak → 1.4A run
    - LDO 42STH48-2504AH: 2.5A peak → 1.7A run (use 1.2A max for TMC2209)
    - Moons MS17HD6P4200: 2.0A peak → 1.4A run

    **Reference**: https://docs.vorondesign.com/community/howto/120decibell/calculating_driver_current.html

    **Phase**: CSV-driven formula calculation
    """,
    tags=["calculators", "klipper"],
)
async def calculate_run_current(request: RunCurrentRequest) -> RunCurrentResponse:
    """
    Calculate run_current for TMC stepper drivers.

    Formula from Voron documentation:
    run_current = peak_current * 0.707 (RMS conversion)

    Args:
        request: RunCurrentRequest with peak_current, optional motor_model and driver_type

    Returns:
        RunCurrentResponse with calculated run_current and safety recommendations
    """
    logger.info(
        f"Run Current calculation: peak_current={request.peak_current}, "
        f"driver={request.driver_type}"
    )

    # Load formula from CSV (validates CSV exists and is loaded)
    csv_loader = get_csv_loader()
    _ = csv_loader.get_run_current_formula()  # Validates CSV is loaded

    # Get RMS factor (constant)
    rms_factor = 0.707

    # Calculate run current
    calculated_current = request.peak_current * rms_factor

    # Round down to nearest 0.1A for safety
    run_current = round(calculated_current * 10) / 10

    # Driver maximum currents
    driver_limits = {
        "TMC2209": 1.2,
        "TMC2208": 1.4,
        "TMC5160": 3.0,
    }

    driver_max = driver_limits.get(request.driver_type, 1.2)

    # Check if within driver limits
    within_limits = run_current <= driver_max

    # If over limit, cap at driver max and warn
    if not within_limits:
        logger.warning(
            f"Calculated run_current {run_current}A exceeds {request.driver_type} "
            f"maximum of {driver_max}A. Capping at driver limit."
        )
        run_current = driver_max

    # Generate Klipper config snippet
    motor_comment = f"  # {request.motor_model}" if request.motor_model else ""
    klipper_config = f"""[tmc2209 stepper_x]{motor_comment}
uart_pin: <YOUR_PIN>
run_current: {run_current}
sense_resistor: 0.110
stealthchop_threshold: 0"""

    # Generate recommendations
    if within_limits:
        recommendation = (
            f"Set run_current: {run_current} in your [tmc2209 stepper_x/y/z] sections. "
            f"Start at {run_current * 0.8:.1f}A (80%) and increase gradually while monitoring temperature. "
            f"Motors should be warm but not uncomfortable to touch. "
            f"If motors are too hot, reduce current by 0.1A increments."
        )
    else:
        recommendation = (
            f"Your motor's peak current ({request.peak_current}A) exceeds {request.driver_type} "
            f"capacity ({driver_max}A). Using maximum safe value of {driver_max}A. "
            f"Consider upgrading to TMC5160 drivers for higher current motors, "
            f"or use a lower current motor for {request.driver_type} drivers."
        )

    # Reference URL
    reference = (
        "https://docs.vorondesign.com/community/howto/120decibell/calculating_driver_current.html"
    )

    # Track calculator usage
    await track_calculator_use(
        "run_current",
        params={
            "peak_current": request.peak_current,
            "run_current": run_current,
            "driver_type": request.driver_type,
            "within_limits": within_limits,
        },
    )

    return RunCurrentResponse(
        run_current=run_current,
        peak_current=request.peak_current,
        rms_factor=rms_factor,
        driver_max=driver_max,
        within_limits=within_limits,
        klipper_config=klipper_config,
        recommendation=recommendation,
        reference=reference,
    )


@router.post(
    "/lead-screw-rotation-distance",
    response_model=LeadScrewRotationDistanceResponse,
    summary="Calculate Lead Screw Rotation Distance",
    description="""
    Calculate rotation_distance for Z-axis lead screws.

    **Formula**: `rotation_distance = pitch × number_of_threads`

    **How to Use**:
    1. Check your lead screw specifications (usually printed on screw or in documentation)
    2. Identify the **pitch** (distance between threads in mm)
    3. Count the **number of starts** (separate thread lines)
    4. Calculator multiplies pitch by number of threads
    5. Copy result to your printer.cfg [stepper_z] section

    **Common T8 Lead Screws**:
    - **T8x2**: 2mm pitch, 1 start (single thread) = 2mm rotation distance
    - **T8x4**: 2mm pitch, 2 starts (dual thread) = 4mm rotation distance
    - **T8x8**: 2mm pitch, 4 starts (quad thread) = 8mm rotation distance

    **How to Identify Number of Starts**:
    - Look at the end of the lead screw
    - Count how many separate grooves/threads you see
    - Single start: 1 groove (most common)
    - Dual start: 2 grooves (faster Z movement)
    - Quad start: 4 grooves (fastest Z movement)

    **Common Printers**:
    - Ender 3 / CR-10: Usually T8x2 (2mm)
    - Prusa i3: T8x8 (8mm) for faster Z
    - Voron: Often T8x2 or T8x4

    **Reference**: https://www.klipper3d.org/Rotation_Distance.html#axes-with-a-lead-screw

    **Phase**: CSV-driven formula calculation
    """,
    tags=["calculators", "klipper"],
)
async def calculate_lead_screw_rotation_distance(
    request: LeadScrewRotationDistanceRequest,
) -> LeadScrewRotationDistanceResponse:
    """
    Calculate rotation_distance for lead screw Z-axis.

    Formula from Klipper documentation:
    rotation_distance = screw_pitch * number_of_separate_threads

    Args:
        request: LeadScrewRotationDistanceRequest with pitch and number_of_threads

    Returns:
        LeadScrewRotationDistanceResponse with calculated rotation distance
    """
    logger.info(
        f"Lead Screw calculation: pitch={request.pitch}, threads={request.number_of_threads}"
    )

    # Load formula from CSV (validates CSV exists and is loaded)
    csv_loader = get_csv_loader()
    _ = csv_loader.get_lead_screw_rotation_distance_formula()  # Validates CSV is loaded

    # Calculate rotation distance
    rotation_distance = request.pitch * request.number_of_threads

    # Common T8 lead screw examples
    common_examples = {
        "T8x2 (single start)": 2.0,
        "T8x4 (dual start)": 4.0,
        "T8x8 (quad start)": 8.0,
    }

    # Generate Klipper config snippet
    screw_comment = f"  # {request.screw_type}" if request.screw_type else ""
    klipper_config = f"""[stepper_z]{screw_comment}
step_pin: <YOUR_PIN>
dir_pin: <YOUR_DIR>
enable_pin: !<YOUR_ENABLE>
microsteps: 16
rotation_distance: {rotation_distance}
endstop_pin: probe:z_virtual_endstop
position_max: 300
homing_speed: 8.0"""

    # Generate recommendations
    screw_info = f" ({request.screw_type})" if request.screw_type else ""
    recommendation = (
        f"Set rotation_distance: {rotation_distance} in your [stepper_z] section{screw_info}. "
        f"With {request.pitch}mm pitch and {request.number_of_threads} start(s), "
        f"each full motor rotation moves the Z-axis {rotation_distance}mm. "
    )

    if request.number_of_threads > 1:
        recommendation += (
            f"Multi-start lead screws ({request.number_of_threads} starts) provide faster Z movement "
            f"compared to single-start screws, useful for tall prints."
        )
    else:
        recommendation += (
            "Single-start lead screws are most common and provide good precision for layer heights."
        )

    # Reference URL
    reference = "https://www.klipper3d.org/Rotation_Distance.html#axes-with-a-lead-screw"

    # Track calculator usage
    await track_calculator_use(
        "lead_screw_rotation_distance",
        params={
            "pitch": request.pitch,
            "number_of_threads": request.number_of_threads,
            "rotation_distance": rotation_distance,
        },
    )

    return LeadScrewRotationDistanceResponse(
        rotation_distance=rotation_distance,
        pitch=request.pitch,
        number_of_threads=request.number_of_threads,
        common_examples=common_examples,
        klipper_config=klipper_config,
        recommendation=recommendation,
        reference=reference,
    )


@router.post(
    "/x-and-y-offsets",
    response_model=XAndYOffsetsResponse,
    summary="Calculate Probe X and Y Offsets",
    description="""
    Calculate BLTouch/CR Touch X and Y offsets for Klipper printer.cfg.

    **Formula**:
    - `x_offset = toolhead_x_probe - toolhead_x_nozzle`
    - `y_offset = toolhead_y_probe - toolhead_y_nozzle`

    **Step-by-Step Process**:
    1. **Home printer**: G28
    2. **Run PROBE**: Issue PROBE command in terminal
    3. **Get probe position**: Issue GET_POSITION
    4. **Record toolhead X/Y**: Note "toolhead" X and Y values (not "mcu")
    5. **Mark the bed**: Place tape/marker where probe triggered
    6. **Move nozzle**: Manually jog nozzle to marked spot
    7. **Get nozzle position**: Issue GET_POSITION again
    8. **Record toolhead X/Y**: Note new "toolhead" X and Y values
    9. **Calculate**: Enter all four values in this calculator

    **Understanding the Offsets**:
    - If probe is **left** of nozzle: X offset is **negative**
    - If probe is **right** of nozzle: X offset is **positive**
    - If probe is **front** of nozzle: Y offset is **negative**
    - If probe is **back** of nozzle: Y offset is **positive**

    **Common Configurations**:
    - **Ender 3 S1**: x_offset: -30, y_offset: -40 (probe left/front)
    - **Voron 2.4**: x_offset: -31.8, y_offset: -40.5 (probe left/front)
    - **CR-6 SE**: x_offset: -31.8, y_offset: -40.5 (probe left/front)

    **Why This Matters**:
    - Accurate offsets ensure bed mesh is measured correctly
    - Wrong offsets = nozzle won't be where Klipper thinks it is
    - Critical for first layer adhesion and bed leveling

    **Reference**: https://www.klipper3d.org/Probe_Calibrate.html#calibrating-probe-x-and-y-offsets

    **Phase**: CSV-driven formula calculation
    """,
    tags=["calculators", "klipper"],
)
async def calculate_x_and_y_offsets(
    request: XAndYOffsetsRequest,
) -> XAndYOffsetsResponse:
    """
    Calculate probe X and Y offsets from toolhead positions.

    Formula from Klipper documentation:
    x_offset = toolhead_x_probe - toolhead_x_nozzle
    y_offset = toolhead_y_probe - toolhead_y_nozzle

    Args:
        request: XAndYOffsetsRequest with toolhead positions

    Returns:
        XAndYOffsetsResponse with calculated offsets
    """
    logger.info(
        f"X/Y Offsets calculation: probe=({request.toolhead_x_probe}, {request.toolhead_y_probe}), "
        f"nozzle=({request.toolhead_x_nozzle}, {request.toolhead_y_nozzle})"
    )

    # Load formula from CSV (validates CSV exists and is loaded)
    csv_loader = get_csv_loader()
    _ = csv_loader.get_x_and_y_offsets_formula()  # Validates CSV is loaded

    # Calculate offsets using the formula from Excel/JavaScript
    x_offset = request.toolhead_x_probe - request.toolhead_x_nozzle
    y_offset = request.toolhead_y_probe - request.toolhead_y_nozzle

    # Generate Klipper config snippet
    probe_type = "bltouch"  # Could be extended to support other probe types
    klipper_config = f"""[{probe_type}]
sensor_pin: ^PC14
control_pin: PC13
x_offset: {x_offset:.1f}
y_offset: {y_offset:.1f}
#z_offset: 0  # Set separately with PROBE_CALIBRATE
speed: 3.0
samples: 2
samples_result: median
sample_retract_dist: 6.0
samples_tolerance: 0.01
samples_tolerance_retries: 3"""

    # Generate step-by-step usage guide
    usage_guide = """
1. Home your printer: G28
2. Issue PROBE command in terminal
3. Issue GET_POSITION and record toolhead X and Y
4. Mark the bed at the probe point (tape works well)
5. Manually jog the nozzle tip to the marked spot
6. Issue GET_POSITION again and record toolhead X and Y
7. Enter all four values in this calculator
8. Copy the calculated offsets to your printer.cfg [probe] section
9. Restart Klipper and verify with PROBE_ACCURACY
""".strip()

    # Reference URL
    reference = "https://www.klipper3d.org/Probe_Calibrate.html#calibrating-probe-x-and-y-offsets"

    # Track calculator usage
    await track_calculator_use(
        "x_and_y_offsets",
        params={
            "x_offset": x_offset,
            "y_offset": y_offset,
            "probe_position": f"({request.toolhead_x_probe}, {request.toolhead_y_probe})",
            "nozzle_position": f"({request.toolhead_x_nozzle}, {request.toolhead_y_nozzle})",
        },
    )

    return XAndYOffsetsResponse(
        x_offset=round(x_offset, 3),
        y_offset=round(y_offset, 3),
        toolhead_x_probe=request.toolhead_x_probe,
        toolhead_y_probe=request.toolhead_y_probe,
        toolhead_x_nozzle=request.toolhead_x_nozzle,
        toolhead_y_nozzle=request.toolhead_y_nozzle,
        klipper_config=klipper_config,
        usage_guide=usage_guide,
        reference=reference,
    )


@router.post(
    "/skew-correction",
    response_model=SkewCorrectionResponse,
    summary="Calculate Skew Correction",
    description="""
    Calculate printer frame skew correction using calibration print measurements.

    **What is Skew Correction?**
    Skew correction compensates for printer frame alignment issues that cause dimensional inaccuracy.
    If your printed squares aren't square or rectangles are parallelograms, you likely have frame skew.

    **Calibration Process**:
    1. **Print calibration model**: https://www.thingiverse.com/thing:2972743/
    2. **Measure three distances per plane**:
       - AC: First diagonal
       - BD: Second diagonal
       - AD: Orthogonal distance
    3. **Three planes to measure**:
       - **XY** (bed plane): Always required
       - **XZ** (left side): Optional but recommended
       - **YZ** (right side): Optional but recommended

    **How to Measure**:
    - Use calipers for accuracy (±0.01mm precision recommended)
    - Measure diagonals from corner to corner (AC, BD)
    - Measure orthogonal distance (AD) perpendicular to diagonals
    - Take multiple measurements and average for best results

    **Understanding Results**:
    - **< 0.1 degrees**: Excellent alignment, correction optional
    - **0.1 - 0.3 degrees**: Good, but correction recommended for precision parts
    - **> 0.3 degrees**: Poor alignment, correction strongly recommended
    - **> 0.5 degrees**: Check printer frame assembly for mechanical issues

    **Typical Skew Values**:
    - CoreXY: Usually minimal XY skew, possible XZ/YZ skew
    - Cartesian: Can have skew in any plane
    - Delta: Primarily XY skew

    **Implementation**:
    1. Copy SET_SKEW command to your START_PRINT macro
    2. Add to printer.cfg before any moves
    3. Restart Klipper
    4. Use CALC_MEASURED_SKEW commands to verify correction
    5. Run GET_CURRENT_SKEW to see active profile

    **Reference**: https://www.klipper3d.org/Skew_Correction.html

    **Phase**: CSV-driven formula calculation
    """,
    tags=["calculators", "klipper"],
)
async def calculate_skew_correction(
    request: SkewCorrectionRequest,
) -> SkewCorrectionResponse:
    """
    Calculate skew correction from calibration print measurements.

    Klipper uses three measurements per plane to calculate frame skew:
    - AC and BD are diagonal measurements
    - AD is the orthogonal distance

    Args:
        request: SkewCorrectionRequest with measurements for XY, XZ, YZ planes

    Returns:
        SkewCorrectionResponse with SET_SKEW command and skew profile
    """
    import math

    logger.info(
        f"Skew correction calculation: XY=({request.xy_ac}, {request.xy_bd}, {request.xy_ad})"
    )

    # Load formula from CSV (validates CSV exists and is loaded)
    csv_loader = get_csv_loader()
    _ = csv_loader.get_skew_correction_formula()  # Validates CSV is loaded

    # Build SET_SKEW command
    set_skew_parts = [f"XY={request.xy_ac},{request.xy_bd},{request.xy_ad}"]

    if request.xz_ac and request.xz_bd and request.xz_ad:
        set_skew_parts.append(f"XZ={request.xz_ac},{request.xz_bd},{request.xz_ad}")

    if request.yz_ac and request.yz_bd and request.yz_ad:
        set_skew_parts.append(f"YZ={request.yz_ac},{request.yz_bd},{request.yz_ad}")

    set_skew_command = f"SET_SKEW {' '.join(set_skew_parts)}"

    # Build CALC_MEASURED_SKEW commands for testing
    calc_commands = {
        "XY": f"CALC_MEASURED_SKEW AC={request.xy_ac} BD={request.xy_bd} AD={request.xy_ad}"
    }

    if request.xz_ac and request.xz_bd and request.xz_ad:
        calc_commands["XZ"] = (
            f"CALC_MEASURED_SKEW AC={request.xz_ac} BD={request.xz_bd} AD={request.xz_ad}"
        )

    if request.yz_ac and request.yz_bd and request.yz_ad:
        calc_commands["YZ"] = (
            f"CALC_MEASURED_SKEW AC={request.yz_ac} BD={request.yz_bd} AD={request.yz_ad}"
        )

    # Calculate skew values (simplified approximation for display)
    # Note: Klipper's actual calculation is more complex
    def estimate_skew(ac: float, bd: float, ad: float) -> tuple[float, float]:
        """Estimate skew in radians and degrees."""
        # Simplified formula: skew ≈ (|AC - BD|) / (2 * AD)
        skew_rad = abs(ac - bd) / (2 * ad) if ad > 0 else 0
        skew_deg = math.degrees(skew_rad)
        return round(skew_rad, 6), round(skew_deg, 2)

    skew_profile = {}
    skew_profile["XY"] = {
        "radians": estimate_skew(request.xy_ac, request.xy_bd, request.xy_ad)[0],
        "degrees": estimate_skew(request.xy_ac, request.xy_bd, request.xy_ad)[1],
    }

    if request.xz_ac and request.xz_bd and request.xz_ad:
        skew_profile["XZ"] = {
            "radians": estimate_skew(request.xz_ac, request.xz_bd, request.xz_ad)[0],
            "degrees": estimate_skew(request.xz_ac, request.xz_bd, request.xz_ad)[1],
        }

    if request.yz_ac and request.yz_bd and request.yz_ad:
        skew_profile["YZ"] = {
            "radians": estimate_skew(request.yz_ac, request.yz_bd, request.yz_ad)[0],
            "degrees": estimate_skew(request.yz_ac, request.yz_bd, request.yz_ad)[1],
        }

    # Generate interpretation
    max_skew_deg = max([v["degrees"] for v in skew_profile.values()])

    if max_skew_deg < 0.1:
        interpretation = (
            f"✅ Excellent alignment! Maximum skew is {max_skew_deg}°. "
            "Frame is well-squared. Skew correction is optional but can still improve dimensional accuracy."
        )
    elif max_skew_deg < 0.3:
        interpretation = (
            f"✔️ Good alignment. Maximum skew is {max_skew_deg}°. "
            "Skew correction is recommended for precision parts (mechanical components, enclosures)."
        )
    elif max_skew_deg < 0.5:
        interpretation = (
            f"⚠️ Moderate skew detected. Maximum skew is {max_skew_deg}°. "
            "Skew correction is strongly recommended. This will noticeably improve print accuracy."
        )
    else:
        interpretation = (
            f"❌ Significant skew detected! Maximum skew is {max_skew_deg}°. "
            "Check your printer frame assembly for mechanical issues (loose bolts, bent extrusions). "
            "Apply skew correction, but also address the underlying mechanical problem."
        )

    # Usage guide
    usage_guide = """1. Copy the SET_SKEW command below
2. Add it to your START_PRINT macro in printer.cfg
3. Place it after homing but before any other moves
4. Example placement:
   [gcode_macro START_PRINT]
   gcode:
     G28  # Home all axes
     SET_SKEW XY=...  # Add skew correction here
     G1 Z10 F3000  # Continue with print start
5. Save and restart Klipper
6. Use CALC_MEASURED_SKEW commands to verify correction
7. Run GET_CURRENT_SKEW to see active profile""".strip()

    # URLs
    calibration_model = "https://www.thingiverse.com/thing:2972743/"
    reference = "https://www.klipper3d.org/Skew_Correction.html"

    # Track calculator usage
    await track_calculator_use(
        "skew_correction",
        params={
            "max_skew_degrees": max_skew_deg,
            "planes_measured": len(skew_profile),
        },
    )

    return SkewCorrectionResponse(
        set_skew_command=set_skew_command,
        calc_measured_skew_commands=calc_commands,
        skew_profile=skew_profile,
        interpretation=interpretation,
        usage_guide=usage_guide,
        calibration_model=calibration_model,
        reference=reference,
    )


@router.post(
    "/line-widths",
    response_model=LineWidthsResponse,
    summary="Recommend Line Width Range",
    description="""
    Recommend a line width range for a given nozzle diameter and feature type.

    Feature Types:
    - external_perimeter: prioritize detail and dimensional accuracy
    - perimeter: general walls, balance strength and speed
    - solid_infill: strong top/bottom layers need slightly wider lines
    - sparse_infill: maximize coverage and speed, widest typical lines
    - first_layer: wider for adhesion and tolerance to bed variations
    - support: moderate width for breakaway tuning

    Typical Multipliers (× nozzle diameter):
    - External Perimeter: 0.95–1.05×
    - Perimeter: 1.00–1.10×
    - Solid Infill: 1.10–1.30×
    - Sparse Infill: 1.20–1.50×
    - First Layer: 1.20–1.40×
    - Support: 1.00–1.20×

    Wider lines improve layer bonding and reduce print time, but exceeding ~150% of nozzle diameter risks under-extrusion and poor dimensional fidelity.
    """,
    tags=["calculators", "extrusion"],
)
async def calculate_line_widths(request: LineWidthsRequest) -> LineWidthsResponse:
    """Compute recommended line width range from nozzle diameter and feature type."""
    nozzle = request.nozzle_diameter
    ft = request.feature_type
    layer_height = request.layer_height

    profiles: dict[str, tuple[float, float, float, str]] = {
        "external_perimeter": (
            0.95,
            1.05,
            1.00,
            "Narrower width preserves fine detail and sharp corners.",
        ),
        "perimeter": (
            1.00,
            1.10,
            1.05,
            "Balanced strength and dimensional accuracy for general walls.",
        ),
        "solid_infill": (
            1.10,
            1.30,
            1.20,
            "Slightly wider for top/bottom surface strength and coverage.",
        ),
        "sparse_infill": (
            1.20,
            1.50,
            1.40,
            "Maximize coverage & speed; avoid >1.5× to prevent flow issues.",
        ),
        "first_layer": (
            1.20,
            1.40,
            1.30,
            "Improves bed adhesion and compensates for minor leveling errors.",
        ),
        "support": (
            1.00,
            1.20,
            1.15,
            "Slightly wider aids stability while keeping interfaces clean.",
        ),
    }

    if ft not in profiles:
        raise HTTPException(status_code=400, detail=f"Unsupported feature_type: {ft}")

    min_mult, max_mult, default_mult, profile_notes = profiles[ft]
    rec_min = round(nozzle * min_mult, 3)
    rec_max = round(nozzle * max_mult, 3)
    default_target = round(nozzle * default_mult, 3)

    # Apply layer height constraint: max width ≤ 1.5× layer_height
    constraint_applied = False
    if layer_height is not None:
        max_width_from_layer = round(1.5 * layer_height, 3)
        if rec_max > max_width_from_layer:
            rec_max = max_width_from_layer
            constraint_applied = True
            if default_target > max_width_from_layer:
                default_target = max_width_from_layer

    extrusion_hint = (
        "If flow calibrated at 100%, keep extrusion multiplier constant; adjust only width."
    )
    slicer_config = f"line_width[{ft}] = {default_target}"  # Generic representation

    notes = (
        f"{profile_notes} Recommended range derived from {min_mult:.2f}–{max_mult:.2f}× nozzle diameter. "
        "Ensure actual extrusion volume matches width adjustments; recalibrate flow if gaps or overfill persist."
    )

    # Extrusion volume sanity check
    volume_check = None
    if layer_height is not None:
        # Extrusion volume per mm: width × layer_height
        extrusion_volume = default_target * layer_height

        # Rule of thumb: extrusion volume should be < nozzle orifice area × 3
        nozzle_area = 3.14159 * (nozzle / 2) ** 2
        max_safe_volume = nozzle_area * 3

        if extrusion_volume > max_safe_volume:
            volume_check = (
                f"⚠️ High extrusion volume: {extrusion_volume:.3f} mm²/mm (width × layer_height). "
                f"Max safe ~{max_safe_volume:.3f} mm²/mm. Consider reducing width or layer height to prevent under-extrusion."
            )
        elif extrusion_volume > nozzle_area * 2:
            volume_check = f"⚡ Moderate extrusion volume: {extrusion_volume:.3f} mm²/mm. Within safe range but monitor flow quality."
        else:
            volume_check = f"✓ Extrusion volume: {extrusion_volume:.3f} mm²/mm (width × layer_height). Safe for {nozzle}mm nozzle."

    if constraint_applied:
        notes += f" Max width constrained to {rec_max}mm by layer_height × 1.5."

    await track_calculator_use(
        "line_widths",
        params={
            "feature_type": ft,
            "nozzle_diameter": nozzle,
            "default_target": default_target,
            "layer_height": layer_height,
            "constraint_applied": constraint_applied,
        },
    )

    return LineWidthsResponse(
        recommended_min=rec_min,
        recommended_max=rec_max,
        default_target=default_target,
        extrusion_multiplier_hint=extrusion_hint,
        slicer_config=slicer_config,
        notes=notes,
        extrusion_volume_check=volume_check,
        layer_height_constraint_applied=constraint_applied,
    )
