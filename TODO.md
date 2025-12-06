# TODO - M3DP-UIP Development Tasks

**Project:** Klipper Calibration Utility (Stateless, Formula-Driven)  
**Focus:** Complete remaining 6 calculators, fix bugs, polish UI, deploy to Railway

---

## 🚨 Critical Issues

### 1. Fix Skew Correction CSV Parsing ✅
**Priority:** HIGH  
**Error:** `Expected 2 fields in line 4, saw 4` in `skew_correction.csv`

**Action Items:**
- [x] Inspect `/backend/app/data/klipper_calibrations/skew_correction.csv`
- [x] Fix CSV format (likely missing quotes or delimiter issues)
- [x] Verify calculator loads without errors
- [x] Test skew correction calculation with valid inputs

---

## 🧮 Calculator Implementation (6/16 Remaining)

**Source:** `research/EXTRACTED_FORMULAS.md`

### Phase 1: Core Calibrations (Priority)

#### 2. Flow Calibration (Traditional) ❌
**Sheet:** Flow Calibration (Traditional Method)

**Formulas:**
- Average Wall Thickness = `(M1 + M2 + M3 + M4) / 4`
- Flow % = `(Perimeters * Line Width) / Average * 100`

**Inputs:**
- Layer Height: 0.2mm
- Perimeters: 2
- Line Width: 0.5mm
- Four wall measurements (top of cube)

**Outputs:**
- Flow % value for slicer

**STL Required:** `Flow_Cube.stl` (provide download link)

**Tasks:**
- [ ] Create CSV file: `flow_calibration_traditional.csv`
- [ ] Implement Pydantic model: `FlowCalibrationTraditionalRequest`
- [ ] Add endpoint: `/flow-calibration-traditional`
- [ ] Create Jinja2 template: `calculators/flow_calibration_traditional.html`
- [ ] Add to calculator index
- [ ] Write unit tests

---

#### 3. Extrusion Rate Smoothing (ERS) ❌
**Sheet:** Extrusion Rate Smoothing

**Formulas:**
- ERS Max = `Acceleration * Line Width * Line Height`
- 60% Experimental = `ERS Max * 0.6`
- 80% Experimental = `ERS Max * 0.8`

**Inputs:**
- External Perimeter Acceleration (mm/s²)
- Line Width (mm)
- Line Height (mm)

**Outputs:**
- ERS value for OrcaSlicer (3 recommendations: max, 60%, 80%)

**Tasks:**
- [ ] Create CSV file: `extrusion_rate_smoothing.csv`
- [ ] Implement Pydantic model: `ERSRequest`
- [ ] Add endpoint: `/extrusion-rate-smoothing`
- [ ] Create Jinja2 template: `calculators/extrusion_rate_smoothing.html`
- [ ] Add to calculator index
- [ ] Write unit tests

---

### Phase 2: Alternative Methods

#### 4. PA & OrcaSlicer ❌
**Sheet:** PA & OrcaSlicer (Alternative PA method)

**Formulas:**
- Direct Drive PA = `Start + (Measured Height * Direct Drive Step)`
- Bowden PA = `Start + (Measured Height * Bowden Step)`

**Inputs:**
- Measured Height
- Start: 0
- Direct Drive Step: 0.002
- Bowden Step: 0.02

**Outputs:**
- Pressure advance values (2 options)

**Tasks:**
- [ ] Create CSV file: `pa_orcaslicer.csv`
- [ ] Implement Pydantic model: `PAOrcaSlicerRequest`
- [ ] Add endpoint: `/pa-orcaslicer`
- [ ] Create Jinja2 template: `calculators/pa_orcaslicer.html`
- [ ] Add to calculator index
- [ ] Write unit tests

---

#### 5. Ellis Max Volumetric Speed ❌
**Sheet:** Ellis Max Volumetric Speed (Manual extrusion method)

**Formulas:**
- F Value = `Filament/Second * 60`
- Volumetric Flow = `Drop Off Point * Filament Diameter Value`
  - 1.75mm → 2.4
  - 2.85mm → 6.37
- 5% Safety = `Volumetric Flow * 0.95`
- 10% Safety = `Volumetric Flow * 0.9`
- Max Print Speed = `Volumetric Flow / Layer Height / Line Width`

**Inputs:**
- Drop Off Point (mm/s where extrusion fails)
- Filament Diameter (1.75mm or 2.85mm)
- Layer Height
- Line Width

**Outputs:**
- Volumetric Flow (mm³/s)
- Max Print Speed (mm/s)
- Safety margins (5%, 10%)

**Tasks:**
- [ ] Create CSV file: `ellis_max_volumetric_speed.csv`
- [ ] Implement Pydantic model: `EllisMaxVolumetricSpeedRequest`
- [ ] Add endpoint: `/ellis-max-volumetric-speed`
- [ ] Create Jinja2 template: `calculators/ellis_max_volumetric_speed.html`
- [ ] Add to calculator index
- [ ] Write unit tests

---

### Phase 3: Advanced Calibrations

#### 6. Adaptive Pressure Advance (OrcaSlicer) ❌
**Sheet:** OS Adaptive Pressure Advance

**Formulas:**
- Range = `MAX(PA values) - MIN(PA values)`
- Min PA = `MIN(PA values) - 0.005`
- Max PA = `MAX(PA values) + 0.005`
- Step = `Range / 16`

**Data Structure:**
Matrix of test results with varying:
- Speed (50-250 mm/s)
- Flow (3.95-15.8 mm³/s)
- Acceleration (1000-6000 mm/s²)
- Resulting PA values

**Inputs:**
- Matrix of test results (complex input form)

**Outputs:**
- PA range (min, max)
- Step size for adaptive tuning
- Model values for each test condition

**Tasks:**
- [ ] Design data input UI (matrix or CSV upload?)
- [ ] Create CSV file: `adaptive_pressure_advance.csv`
- [ ] Implement Pydantic model: `AdaptivePARequest`
- [ ] Add endpoint: `/adaptive-pressure-advance`
- [ ] Create Jinja2 template: `calculators/adaptive_pressure_advance.html`
- [ ] Add to calculator index
- [ ] Write unit tests

---

### Phase 4: Physics & Engineering Engine (New Strategy)

#### 7. Belt Resonance Calculator (Mersenne) ❌
**Strategy:** Domain I - Kinematic Resonance & Tension Physics

**Formulas:**
- `Tension = 4 * Density * Length^2 * Frequency^2`
- `Frequency = sqrt(Tension / (4 * Density * Length^2))`

**Inputs:**
- Span Length (mm)
- Measured Frequency (Hz) or Target Tension (N)
- Belt Type (GT2 6mm/9mm/12mm)

**Outputs:**
- Calculated Tension (N) or Target Frequency (Hz)
- Warning if tension exceeds motor radial load limits

**Tasks:**
- [ ] Create CSV file: `belt_resonance.csv`
- [ ] Implement Pydantic model: `BeltResonanceRequest`
- [ ] Add endpoint: `/belt-resonance`
- [ ] Create Jinja2 template: `calculators/belt_resonance.html`
- [ ] Add to calculator index (and update existing belt tension tool if needed)

#### 8. Stepper Motor Max Velocity (Back EMF) ❌
**Strategy:** Domain II - Electromechanical Limits

**Formulas:**
- `V_max_safe = (Voltage / (2 * Inductance * Current * Steps * 3.14159)) * (Pitch * Teeth) * 0.7`

**Inputs:**
- Supply Voltage (V)
- Inductance (mH)
- Peak Current (A)
- Steps per Revolution (200/400)
- Pulley Teeth (16/20)

**Outputs:**
- Theoretical Max Velocity (mm/s)
- "Safe" Velocity recommendation

**Tasks:**
- [ ] Create CSV file: `stepper_max_velocity.csv`
- [ ] Implement Pydantic model: `StepperMaxVelocityRequest`
- [ ] Add endpoint: `/stepper-max-velocity`
- [ ] Create Jinja2 template: `calculators/stepper_max_velocity.html`
- [ ] Add to calculator index

#### 9. Screws Tilt Adjust Visualizer ❌
**Strategy:** Domain IV - Geometric & Thermal Topology

**Formulas:**
- `Turns = Minutes / 60`
- `Degrees = Minutes * 6`
- `Z_Change = (Minutes / 60) * Pitch`

**Inputs:**
- Klipper Output String (e.g., "CW 01:15")
- Screw Type (M3/M4/M5)

**Outputs:**
- Rotations (Turns + Degrees)
- Vertical Movement (mm)
- Visual aid (clock face representation?)

**Tasks:**
- [ ] Create CSV file: `screws_tilt_adjust.csv`
- [ ] Implement Pydantic model: `ScrewsTiltRequest`
- [ ] Add endpoint: `/screws-tilt-adjust`
- [ ] Create Jinja2 template: `calculators/screws_tilt_adjust.html`
- [ ] Add to calculator index

#### 10. Frame Thermal Expansion (Z-Drift) ❌
**Strategy:** Domain IV - Geometric & Thermal Topology

**Formulas:**
- `Delta_Z = Frame_Height * 23.4e-6 * (Chamber_Temp - Ambient_Temp)`

**Inputs:**
- Frame Height (mm)
- Ambient Temp (°C)
- Chamber Temp (°C)

**Outputs:**
- Predicted Z-Drift (mm)
- Warning/Recommendation

**Tasks:**
- [ ] Create CSV file: `frame_thermal_expansion.csv`
- [ ] Implement Pydantic model: `FrameThermalExpansionRequest`
- [ ] Add endpoint: `/frame-thermal-expansion`
- [ ] Create Jinja2 template: `calculators/frame_thermal_expansion.html`
- [ ] Add to calculator index

#### 11. VFA Speed Avoidance ❌
**Strategy:** Domain I - Kinematic Resonance

**Formulas:**
- `f_observed = V_print / P_vfa`
- `RPM = (V * 60) / (Pitch * Teeth)`

**Inputs:**
- Print Speed (mm/s)
- Measured Ripple Distance (mm)
- Pulley Teeth

**Outputs:**
- Identified Frequency (Hz)
- Probable Cause (Belt vs Motor)

**Tasks:**
- [ ] Create CSV file: `vfa_speed_avoidance.csv`
- [ ] Implement Pydantic model: `VFASpeedAvoidanceRequest`
- [ ] Add endpoint: `/vfa-speed-avoidance`
- [ ] Create Jinja2 template: `calculators/vfa_speed_avoidance.html`
- [ ] Add to calculator index

#### 12. Input Shaper Acceleration Limit ❌
**Strategy:** Domain I - Kinematic Resonance

**Formulas:**
- `a_max_mzv = 3500 * (f_n / 34)^2`
- `a_max_zv = 67 * f_n^2 * tolerance`

**Inputs:**
- Resonance Freq X/Y (Hz)
- Shaper Type X/Y

**Outputs:**
- Recommended Max Acceleration (mm/s²)
- Limiting Axis note

**Tasks:**
- [ ] Create CSV file: `input_shaper_limits.csv`
- [ ] Implement Pydantic model: `InputShaperLimitRequest`
- [ ] Add endpoint: `/input-shaper-limits`
- [ ] Create Jinja2 template: `calculators/input_shaper_limits.html`
- [ ] Add to calculator index

#### 13. Filament Spool Remainder ❌
**Strategy:** Domain V - Material Management

**Formulas:**
- `Length = (Mass_Total - Mass_Spool) / (Density * pi * radius^2)`

**Inputs:**
- Total Weight (g)
- Empty Spool Weight (g)
- Filament Type (Density lookup)
- Filament Diameter (mm)

**Outputs:**
- Creating CSV file: `filament_spool_remainder.csv`
- Remaining Length (m)

**Tasks:**
- [ ] Create CSV file: `filament_spool_remainder.csv`
- [ ] Implement Pydantic model: `FilamentSpoolRemainderRequest`
- [ ] Add endpoint: `/filament-spool-remainder`
- [ ] Create Jinja2 template: `calculators/filament_spool_remainder.html`
- [ ] Add to calculator index

## 🎨 UI Improvements

### Calculator Index Page
- [ ] Add calculator cards with descriptions
- [ ] Implement search/filter functionality
- [ ] Add "Implemented" vs "Coming Soon" badges
- [ ] Group calculators by category:
  - Extruder (Rotation Distance, Flow, ERS)
  - Motion (Pressure Advance, Input Shaping)
  - Hardware (Run Current, X/Y Offsets, Lead Screw)
  - Advanced (Skew Correction, Adaptive PA)
  - OrcaSlicer (Flow YOLO, Line Widths, Max Volumetric Speed)

### Individual Calculator Pages
- [ ] Standardize form layouts
- [ ] Add input validation feedback
- [ ] Display formulas used (collapsible section)
- [ ] Add "Copy to Clipboard" for results
- [ ] Link to STL files where applicable
- [ ] Add Klipper command examples
- [ ] Implement result visualization (charts for multi-value outputs)

### Home Page
- [ ] Add hero section with project description
- [ ] Display "Quick Access" to most-used calculators
- [ ] Add "Recently Updated" section
- [ ] Link to documentation and YouTube channel

---

## 🐛 Bug Fixes

### Current Issues
- [x] Skew correction CSV parsing error (HIGH PRIORITY)
- [ ] Diagnosis endpoints removed but templates may still reference them
- [ ] Check for any remaining AI service imports
- [ ] Verify all calculator templates load correctly

### Code Cleanup
- [ ] Remove `/backend/app/services/semantic_router.py`
- [ ] Remove `/backend/app/services/router_service.py`
- [ ] Remove `/backend/app/services/vision_service.py`
- [ ] Remove `/backend/app/api/endpoints/diagnosis.py`
- [ ] Remove `/backend/validation_data/` (vision datasets)
- [ ] Remove `/backend/demo_vision.py` and `/backend/test_pages.py`
- [ ] Clean up unused imports in `main.py`

---

## 📦 Dependencies

### Backend
- [x] Remove AI libraries from `pyproject.toml`
- [x] Add `jinja2>=3.1.0`
- [ ] Verify all calculators work with current pandas version
- [ ] Consider adding `pytest-cov` for coverage reporting

### Frontend
- [ ] Verify HTMX CDN link is latest stable (1.9.10)
- [ ] Verify Alpine.js CDN link is latest stable (3.13.5)
- [ ] Verify TailwindCSS CDN link is v3+
- [ ] Check for any Vue/React remnants

---

## 🧪 Testing

### Unit Tests
- [ ] Test all 10 implemented calculators
- [ ] Test all 6 new calculators (as implemented)
- [ ] Test CSV data loading
- [ ] Test Pydantic validation
- [ ] Achieve 80%+ code coverage

### Integration Tests
- [ ] Test all API endpoints return 200
- [ ] Test calculator form submissions
- [ ] Test error handling (invalid inputs)
- [ ] Test `/api/v1/calculators` JSON response

### Manual Testing
- [ ] Test all calculator UIs on desktop
- [ ] Test all calculator UIs on mobile
- [ ] Test navigation between calculators
- [ ] Test copy-to-clipboard functionality
- [ ] Verify all formulas match `EXTRACTED_FORMULAS.md`

---

## 📚 Documentation

### Code Documentation
- [ ] Add docstrings to all calculator endpoints
- [ ] Add docstrings to all Pydantic models
- [ ] Document CSV file format requirements
- [ ] Add inline comments for complex formulas

### User Documentation
- [ ] Create calculator usage guides (in `/docs/usage/`?)
- [ ] Add FAQ section
- [ ] Document Klipper command usage
- [ ] Link to STL files and calibration prints

### Developer Documentation
- [ ] Update `CONTRIBUTING.md` with calculator implementation guide
- [ ] Document Jinja2 template structure
- [ ] Document CSV data format standards
- [ ] Add architecture diagram (server-side rendering flow)

---

## 🚀 Deployment

### Railway Setup
- [ ] Create Railway project
- [ ] Connect GitHub repository
- [ ] Configure environment variables (if needed)
- [ ] Set build command: `pip install -e . && pip install jinja2`
- [ ] Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- [ ] Deploy from `refactor/v2-lean` branch

### Domain Setup
- [ ] Configure custom domain (if available)
- [ ] Set up SSL certificate
- [ ] Configure DNS records

### Smart Links
- [ ] Implement `/go/{product_id}` redirect service
- [ ] Create product ID mapping (CSV or database?)
- [ ] Test redirect functionality

---

## 📊 Analytics & Monitoring

### Basic Monitoring
- [ ] Add health check endpoint (`/health`)
- [ ] Log calculator usage (which calculators are most popular?)
- [ ] Log errors to console (Railway logs)

### Performance Optimization
- [ ] Profile calculator response times
- [ ] Optimize CSV loading (cache in memory?)
- [ ] Minify CSS/JS assets
- [ ] Enable gzip compression

---

## 🎯 Future Enhancements

### Phase 5: Community Features
- [ ] User-submitted calibration results (optional database)
- [ ] Export results as PDF
- [ ] Share results via URL (query parameters?)
- [ ] Multi-language support (i18n)

### Phase 6: Advanced Features
- [ ] Batch calculator mode (run multiple calculators in sequence)
- [ ] Calibration workflow wizard
- [ ] Integration with Klipper API (query live printer data?)
- [ ] Mobile app (PWA?)

---

## ✅ Completed Tasks

### Repository Organization
- [x] Compress research directory (11 → 3 files)
- [x] Organize root documentation (15 → 3 MD files)
- [x] Move vision AI docs to `docs/archived/`
- [x] Move phase docs to `docs/archived/`
- [x] Create `docs/development/` and `docs/deployment/` subdirectories
- [x] Relocate loose Python files to `backend/`
- [x] Remove placeholder `main.py` from root

### Dependency Cleanup
- [x] Remove `google-generativeai` from `pyproject.toml`
- [x] Remove `kaggle` from `pyproject.toml`
- [x] Remove `roboflow` from `pyproject.toml`
- [x] Remove `pymupdf` from `pyproject.toml`
- [x] Remove `pypdf` from `pyproject.toml`
- [x] Remove `pillow` from `pyproject.toml`
- [x] Add `jinja2>=3.1.0` to `pyproject.toml`

### Server Startup
- [x] Fix diagnosis module import in `__init__.py`
- [x] Comment out diagnosis endpoints in `main.py`
- [x] Install `jinja2` in virtual environment
- [x] Successfully start FastAPI server at `http://localhost:8000`

### Documentation
- [x] Rewrite `README.md` with lean refactor focus
- [x] Rewrite `TODO.md` with calculator backlog and current priorities

---

## 📝 Notes

**Current Server Status:** ✅ Running at `http://localhost:8000`
- 10 calculators accessible
- Diagnosis endpoints disabled
- Skew correction CSV has parsing warning (non-critical)

**Branch:** `refactor/v2-lean`
**Last Updated:** 2025-01-XX

**Next Session Focus:**
1. Fix skew correction CSV parsing error (Done)
2. Implement Flow Calibration (Traditional) - highest priority
3. Implement ERS calculator - second priority
4. Test all 12 calculators end-to-end
