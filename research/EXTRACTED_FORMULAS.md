# Extracted Calculator Formulas from Klipper Calibrations.xlsx

## Summary of Available Calculators

Total sheets found: **16**
Implemented in M3DP-UIP: **2**
Remaining to implement: **14**

---

## 1. Extruder Rotation Distance ✅ IMPLEMENTED

**Sheet**: Extruder Rotation Distance

### Formulas:
- **Rotation Distance** = `Full Steps Per Rotation * Micro Steps / E Steps`
  - Cell A13: `=B13*C13/D13`
  - Example: `200 * 32 / 400 = 16`

- **E-Steps** = `Full Steps Per Rotation * Micro Steps / Rotation Distance`
  - Cell A16: `=B16*C16/D16`
  - Example: `200 * 32 / 8 = 800`

- **Measure and Trim** = `previous_rotation_distance * actual_extrude_distance / requested_extrude_distance`
  - Cell A29: `=B29*C29/D29`
  - Example: `20.112 * 101 / 100 = 20.313`

### Inputs:
- Initial mark distance (default: 120mm)
- Requested extrude distance (default: 100mm)
- Subsequent mark distance (measured)
- Previous rotation distance

### Outputs:
- New rotation distance for `printer.cfg`

---

## 2. Flow Calibration ❌ NOT IMPLEMENTED

**Sheet**: Flow Calibration (Traditional Method)

### Formulas:
- **Average Wall Thickness** = `(Measure1 + Measure2 + Measure3 + Measure4) / 4`
  - Cell B32: `=(B28+B29+B30+B31)/4`

- **Flow %** = `(Perimeters * Line Width) / Average * 100`
  - Cell B33: `=(B14*B15)/B32*100`
  - Example: `(2 * 0.5) / 0.9475 * 100 = 105.54%`

### Inputs:
- Layer Height: 0.2mm
- Perimeters: 2
- Line Width: 0.5mm
- Four wall measurements (top of cube)

### Outputs:
- Flow % value for slicer

### STL File Required:
- `Flow_Cube.stl`

---

## 3. OrcaSlicer Flow Calibration ❌ NOT IMPLEMENTED

**Sheet**: OrcaSlicer Flow Calibration (Recommended)

### Formulas:
- **Pass 1 Flow** = `Old Flow Rate * (100 + Pass1 Slide Value) / 100`
  - Cell B20: `=B18*(100+B19)/100`
  - Example: `0.99 * (100 + -10) / 100 = 0.891`

- **Pass 2 Flow** = `Pass 1 Flow * (100 + Pass2 Slide Value) / 100`
  - Cell B27: `=B25*(100+B26)/100`
  - Example: `0.891 * (100 + -1) / 100 = 0.882`

### Inputs:
- Old Flow Rate (from slicer)
- Pass 1 Slide Value (smoothest slide from test)
- Pass 2 Slide Value (smoothest slide from 2nd test)

### Outputs:
- New Flow Rate for OrcaSlicer

---

## 4. OrcaSlicer Flow YOLO ❌ NOT IMPLEMENTED

**Sheet**: OrcaSlicer Flow YOLO (Single-pass method)

### Formulas:
- **New Flow** = `Old Flow Rate + YOLO Slide Value`
  - Cell B20: `=B18+B19`
  - Example: `1.0 + -0.035 = 0.965`

### Inputs:
- Old Flow Rate
- YOLO Slide Value (smoothest slide from single test)

### Outputs:
- New Flow Rate

---

## 5. Run Current (TMC2208/2209) ❌ NOT IMPLEMENTED

**Sheet**: Run Current

### Formulas:
- **Run Current** = `ROUNDDOWN(Peak Current * RMS Factor, 1)`
  - Cell B15: `=rounddown(B13*B14,1)`
  - Example: `ROUNDDOWN(1.5 * 0.707, 1) = 1.0`

### Inputs:
- Peak Current (from motor spec sheet)
- RMS Factor: 0.707 (constant)

### Outputs:
- Run current value for TMC section of `printer.cfg`

---

## 6. Pressure Advance ✅ IMPLEMENTED (Basic)

**Sheet**: Pressure Advance

### Formulas:
- **Direct Drive PA** = `Start + (Measured Height * Direct Drive Factor)`
  - Cell B32: `=B28+B31*B29`
  - Example: `0 + (12.29 * 0.005) = 0.061`

- **Bowden PA** = `Start + (Measured Height * Bowden Factor)`
  - Cell B33: `=B28+B31*B30`
  - Example: `0 + (12.29 * 0.02) = 0.246`

### Inputs:
- Measured Height (from print)
- Start: 0
- Direct Drive Factor: 0.005
- Bowden Factor: 0.020

### Outputs:
- Pressure advance value for `printer.cfg`

### Commands:
- Setup: `SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500`
- Direct Drive: `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005`
- Bowden: `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.020`

---

## 7. PA & OrcaSlicer ❌ NOT IMPLEMENTED

**Sheet**: PA & OrcaSlicer (Alternative PA method)

### Formulas:
- **Direct Drive PA** = `Start + (Measured Height * Direct Drive Step)`
  - Cell B19: `=B15+B18*B16`
  - Example: `0 + (30.3 * 0.002) = 0.061`

- **Bowden PA** = `Start + (Measured Height * Bowden Step)`
  - Cell B20: `=B15+B18*B17`
  - Example: `0 + (30.3 * 0.02) = 0.606`

### Inputs:
- Measured Height
- Start: 0
- Direct Drive Step: 0.002
- Bowden Step: 0.02

---

## 8. Input Shaping ❌ NOT IMPLEMENTED

**Sheet**: Input Shaping

### Formulas:
- **X Frequency** = `Print Speed * X Rings / X Measurements`
  - Cell B41: `=B36*B37/B38`
  - Example: `100 * 3 / 14.58 = 20.58 Hz`

- **Y Frequency** = `Print Speed * Y Rings / Y Measurements`
  - Cell B42: `=B36*B39/B40`
  - Example: `100 * 6 / 16.75 = 35.82 Hz`

### Inputs:
- Print Speed (from test print, default: 100mm/s)
- X Rings count
- X Measurements (distance between rings)
- Y Rings count
- Y Measurements (distance between rings)

### Outputs:
- X Frequency (Hz) for `printer.cfg`
- Y Frequency (Hz) for `printer.cfg`

### Commands:
- `SET_VELOCITY_LIMIT ACCEL_TO_DECEL=7000`
- `SET_PRESSURE_ADVANCE ADVANCE=0`
- `SET_INPUT_SHAPER SHAPER_FREQ_X=0 SHAPER_FREQ_Y=0`
- `TUNING_TOWER COMMAND=SET_VELOCITY_LIMIT PARAMETER=ACCEL START=1500 STEP_DELTA=500 STEP_HEIGHT=5`

### STL File:
- https://www.klipper3d.org/prints/ringing_tower.stl

---

## 9. X and Y Offsets ❌ NOT IMPLEMENTED

**Sheet**: X and Y Offsets

### Formulas:
- **X Offset** = `Toolhead X Nozzle - Toolhead X Probe`
  - Cell C35: `=C30-C20`
  - Example: `224 - 188 = 36`

- **Y Offset** = `Toolhead Y Nozzle - Toolhead Y Probe`
  - Cell C36: `=C31-C21`
  - Example: `148 - 185 = -37`

### Inputs:
- Toolhead X Probe position
- Toolhead Y Probe position
- Toolhead X Nozzle position
- Toolhead Y Nozzle position

### Outputs:
- X Offset for `printer.cfg`
- Y Offset for `printer.cfg`

---

## 10. Max Volumetric Speed (OrcaSlicer) ❌ NOT IMPLEMENTED

**Sheet**: Max Volumetric Speed

### Formulas:
- **Max Flow Value** = `Start + (Height Measured * Step)`
  - Cell B23: `=C23+(D23*E23)`
  - Example: `5 + (27.23 * 0.5) = 18.615`

- **95% Safety Margin** = `Max Flow Value * 0.95`
  - Cell C25: `=B23*0.95`

- **90% Safety Margin** = `Max Flow Value * 0.9`
  - Cell C26: `=B23*0.9`

### Inputs:
- Start value (from OrcaSlicer calibration dialog)
- Height Measured (from print)
- Step (from OrcaSlicer calibration dialog)

### Outputs:
- Max Flow Value for OrcaSlicer Filament Section
- 95% value (recommended)
- 90% value (conservative)

---

## 11. Ellis Max Volumetric Speed ❌ NOT IMPLEMENTED

**Sheet**: Ellis Max Volumetric Speed (Manual extrusion method)

### Formulas:
- **F Value** = `Filament/Second * 60`
  - Cell D22: `=C22*60`
  - Example: `5 * 60 = 300`

- **Volumetric Flow** = `Drop Off Point * Filament Diameter Value`
  - Cell B64: `=C64*D64`
  - Example: `5 * 2.4 = 12 mm³/s` (for 1.75mm filament)

- **5% Safety** = `Volumetric Flow - (Volumetric Flow * 0.05)`
  - Cell C66: `=B64 - (B64*0.05)`

- **10% Safety** = `Volumetric Flow - (Volumetric Flow * 0.1)`
  - Cell C67: `=B64 - (B64*0.1)`

- **Max Print Speed** = `Volumetric Flow / Layer Height / Line Width`
  - Cell B71: `=C71/D71/E71`
  - Example: `11.4 / 0.2 / 0.5 = 114 mm/s`

### Inputs:
- Drop Off Point (mm/s where extrusion fails)
- Filament Diameter (1.75mm → 2.4, 2.85mm → 6.37)
- Layer Height
- Line Width

### Outputs:
- Volumetric Flow (mm³/s)
- Max Print Speed (mm/s)

---

## 12. Lead Screw Rotation Distance ❌ NOT IMPLEMENTED

**Sheet**: Lead Screw Rotation Distance

### Formulas:
- **Rotation Distance** = `Pitch * # of Threads`
  - Cell A19: `=B19*C19`
  - Example: `2 * 1 = 2` (T8x2 lead screw)

### Common Lead Screws:
- T8x8: Pitch 2mm, 4 threads → 8mm
- T8x4: Pitch 2mm, 2 threads → 4mm
- T8x2: Pitch 2mm, 1 thread → 2mm

### Inputs:
- Pitch (mm)
- Number of Threads

### Outputs:
- Rotation distance for Z axis in `printer.cfg`

---

## 13. Extrusion Rate Smoothing (ERS) ❌ NOT IMPLEMENTED

**Sheet**: Extrusion Rate Smoothing

### Formulas:
- **ERS Max** = `Acceleration * Line Width * Line Height`
  - Cell B17: `=C17*D17*E17`
  - Example: `12000 * 0.6 * 0.2 = 1440`

- **60% Experimental** = `ERS Max * 0.6`
  - Cell B19: `=B17*0.6`

- **80% Experimental** = `ERS Max * 0.8`
  - Cell B20: `=B17*0.8`

### Inputs:
- External Perimeter Acceleration (mm/s²)
- Line Width (mm)
- Line Height (mm)

### Outputs:
- ERS value for OrcaSlicer

---

## 14. Line Widths (OrcaSlicer) ❌ NOT IMPLEMENTED

**Sheet**: Line Widths

### Formulas:
All formulas follow the pattern: `Percentage * Nozzle Diameter`

Examples:
- **Default**: `1.25 * 0.4 = 0.5mm` (125% of nozzle)
- **First Layer**: `1.1 * 0.4 = 0.44mm` (110% of nozzle)
- **Outer Wall**: `1.5 * 0.4 = 0.6mm` (150% of nozzle)

### Recommendations:
- Default: 105-150% of nozzle diameter
- First Layer: 105-115%
- Outer Wall: 105-150%
- Inner Wall: 120-125%
- Top Surface: 100-105%
- Sparse Infill: 125%
- Internal Solid Infill: 125%
- Support: 95-105%

---

## 15. Skew Correction ❌ NOT IMPLEMENTED

**Sheet**: Skew Correction

### Formulas:
- **SET_SKEW Command** = Complex concatenation of AC, BD, AD measurements for XY, XZ, YZ
  - Cell B31: Generates full Klipper command string
  - Example: `SET_SKEW XY=141.21,140.97,104.77 XZ=141.98,141.63,104.9 YZ=141.54,141.33,104.83`

- **CALC_MEASURED_SKEW Command** = Similar concatenation for verification measurements
  - Cell B44-B46: Generates CALC commands for XY, XZ, YZ

### Inputs:
- Initial measurements: AC, BD, AD for XY, XZ, YZ planes
- Verification measurements: AC, BD, AD after skew correction applied

### Outputs:
- `SET_SKEW` command for start G-code
- `CALC_MEASURED_SKEW` commands for verification

### STL File:
- https://www.thingiverse.com/thing:2972743/

---

## 16. Adaptive Pressure Advance (OrcaSlicer) ❌ NOT IMPLEMENTED

**Sheet**: OS Adaptive Pressure Advance

### Formulas:
- **Range** = `MAX(PA values) - MIN(PA values)`
  - Cell H2: Dynamic calculation from user's test results

- **Min PA** = `MIN(PA values) - 0.005`
  - Cell H3: Safety margin below minimum

- **Max PA** = `MAX(PA values) + 0.005`
  - Cell H4: Safety margin above maximum

- **Step** = `Range / 16`
  - Cell H5: Incremental step size

### Data Structure:
Matrix of test results with varying:
- Speed (50-250 mm/s)
- Flow (3.95-15.8 mm³/s)
- Acceleration (1000-6000 mm/s²)
- Resulting PA values

### Outputs:
- PA range (min, max)
- Step size for adaptive tuning
- Model values for each test condition

---

## Implementation Priority

### Phase 1 (Core Calibrations):
1. **Flow Calibration** - Baseline for all extrusion
2. **Input Shaping** - Critical for print quality
3. **Max Volumetric Speed** - Safety critical

### Phase 2 (Hardware Calibrations):
4. **Run Current** - Motor setup
5. **X & Y Offsets** - Probe calibration
6. **Lead Screw Rotation Distance** - Z axis setup

### Phase 3 (Advanced):
7. **OrcaSlicer Flow Calibration** - Modern workflow
8. **OrcaSlicer Flow YOLO** - Quick method
9. **PA & OrcaSlicer** - Alternative PA method
10. **Extrusion Rate Smoothing** - Advanced feature
11. **Line Widths** - Optimization guide
12. **Ellis Max Volumetric Speed** - Alternative method

### Phase 4 (Complex):
13. **Skew Correction** - Complex formula generation
14. **Adaptive Pressure Advance** - Matrix-based tuning

---

## Next Steps

1. Create CSV files for each calculator (follow existing pattern in `backend/app/data/klipper_calibrations/`)
2. Implement Pydantic models for request/response (follow `RotationDistanceRequest` pattern)
3. Add calculator endpoints to `backend/app/api/endpoints/calculators.py`
4. Create Vue components (follow `RotationDistanceCalculator.vue` pattern)
5. Update `/calculators` page to include new calculators
6. Write unit tests for each calculator
7. Update `PHASE4_INTEGRATION_TESTS.md` with manual testing results
