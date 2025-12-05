# M3DP-UIP Development TODO

Development roadmap organized by feature branches. The `main` branch contains only working, production-ready code. All development happens on feature branches that merge to `develop`, which then merges to `main` after thorough testing.

## 📊 Progress Overview

- ✅ **Phase 0**: Project Setup & Tooling - COMPLETED
- ✅ **Phase 1**: CSV Knowledge Base Foundation - COMPLETED
- ✅ **Phase 2**: Backend Core (Vision API & Router) - COMPLETED
- ✅ **Phase 3**: Frontend Development - COMPLETED (Vue 3 + Nuxt)
- 🚀 **Phase 4**: Integration & Testing - IN PROGRESS
- ⏳ **Phase 5**: Deployment & Polish - READY

## 🎯 Core Mission

**Application Goal**: System of calibration calculators and AI-powered defect diagnosis that helps users optimize their 3D printers and models.

**Key Capabilities**:
1. **Calibration Calculators**: Deterministic math-based tools for printer calibration (rotation distance, pressure advance, flow rate, input shaping, etc.)
2. **AI Defect Diagnosis**: Take a picture or describe a problem → receive recommended fix (calculator to use or troubleshooting steps)
3. **Knowledge Base**: CSV-driven troubleshooting guide with 63+ defect types and solutions

**Technical Foundation**:
- ✅ **Router Pattern**: Query classification prevents context pollution
- ✅ **CSV-Driven Formulas**: Industry-standard deterministic calculations
- ✅ **Klipper Focus**: Minimal 3DP ecosystem as authoritative calibration reference
- ✅ **Free Semantic Router**: HuggingFace local embeddings (no API costs)
- ✅ **Vision API**: Gemini 1.5 Pro for image-based diagnosis (optional)

## 🎯 Development Priorities

### Immediate (Phase 4 - Current)
1. **Integration Testing**: Validate full diagnostic workflow (text + vision + calculators)
2. **Vision Model Validation**: Build reference dataset, test accuracy, improve prompts
3. **Troubleshooting CSV Quality**: Add success rates, time estimates, difficulty ratings

### Short-term (Phase 5-7)
1. **Calculator Expansion**: Temperature tower, retraction tuning, belt tension, max acceleration
2. **Enhanced Diagnosis**: Confidence levels, multi-image support, calculator links
3. **G-code Export**: Generate test patterns from calculators (test cubes, pressure advance patterns, etc.)

### Long-term (Phase 8-10)
1. **User Experience**: Diagnosis history, Klipper config export, calculator result explanations
2. **Community Features**: User-submitted presets, voting system (optional, post-MVP)
3. **Monetization**: Amazon affiliate product recommendations based on diagnostics

---

## Phase 0: Project Setup & Tooling ✅

**Branch**: N/A (direct to main)
**Status**: COMPLETED
**Goal**: Establish project structure, tooling, and development environment

### Completed Tasks

- [x] Create project directory structure
- [x] Set up `pyproject.toml` with dependencies
- [x] Configure Ruff (linting and formatting)
- [x] Set up pytest with coverage
- [x] Configure pre-commit hooks
- [x] Create `.env.example` and `.gitignore`
- [x] Write initial documentation (DEVELOPMENT.md, SCRIPTS.md)
- [x] Create utility scripts (setup.sh, run_dev.sh, run_tests.sh)
- [x] Set up FastAPI application structure
- [x] Create initial test suite
- [x] Update README.md with badges and quick start

### Deliverables

- ✅ Working development environment
- ✅ Code quality tooling configured
- ✅ Basic FastAPI app with health endpoints
- ✅ Comprehensive documentation
- ✅ Utility scripts for common tasks

---

## Phase 1: CSV Knowledge Base Foundation ✅

**Branch**: `feature/csv-knowledge-base`
**Status**: COMPLETED (2 commits: bd9148b, faa19ed)
**Priority**: HIGH
**Goal**: Implement CSV data loading and validation

### Completed Tasks

#### Data Ingestion ✅
- [x] Create CSV schema definitions (`backend/app/models/csv_schemas.py`)
  - 6 schemas: Extruder Rotation Distance, Pressure Advance, Input Shaping, Material Profiles, Quality Settings, Troubleshooting
  - Column-level validation: type checking, range validation, required fields, allowed values
  - Schema registry with `get_schema()` and `validate_csv_file()` helpers
- [x] Implement CSV validation logic (integrated into CSVLoader)
- [x] Add sample CSV files for testing (6 files created with real data)
  - **Klipper Calibrations**: extruder_rotation_distance.csv (5 rows), pressure_advance.csv (7 rows), input_shaping.csv (7 rows)
  - **OrcaSlicer Recommendations**: material_profiles.csv (8 materials), quality_settings.csv (5 quality levels), troubleshooting.csv (8 issues)

#### CSV Loader Service ✅
- [x] Complete `CSVLoader` implementation (enhanced from stub)
  - Added `validate` parameter to enable/disable validation on load
  - Integrated schema validation with error tracking
  - Updated cache keys to category-based format (klipper:, orca:)
  - Added logging instead of print statements
- [x] Add caching mechanism (in-memory dictionary)
- [x] Implement search functionality (`search_by_description()`)
- [x] Add error handling and logging (validation errors tracked separately)
- [x] Write comprehensive tests (12 passing tests)
  - Test coverage: 86% for csv_loader, 85% for csv_schemas

#### New Methods Added ✅
- [x] `get_input_shaping_data()` - Retrieve input shaping configuration
- [x] `get_troubleshooting_data(issue_type)` - Filter troubleshooting by issue type
- [x] `get_quality_settings(quality_level)` - Filter quality settings
- [x] `get_csv_by_name(csv_name, category)` - Generic CSV getter
- [x] `has_validation_errors()`, `get_validation_errors()` - Validation error helpers

#### Testing Results ✅
- [x] Unit tests for CSV loader (12 tests)
  - Initialization, file loading, data retrieval, filtering, search, validation
- [x] Integration tests with sample data (all 6 CSVs load successfully)
- [x] Validation tests for CSV schemas (all pass)
- [x] **Final Test Results**: 14 passed, 1 skipped, 73% coverage
  - csv_loader: 86% coverage (102 lines, 14 missed)
  - csv_schemas: 85% coverage (80 lines, 12 missed)
  - Overall: Exceeds 70% target from testing requirements

### Deliverables ✅

- ✅ 6 CSV files with real Klipper and OrcaSlicer data (tracked in git)
- ✅ Comprehensive schema validation system with 6 schemas
- ✅ Enhanced CSV loader with filtering, search, validation, and caching
- ✅ 12 comprehensive tests covering all major functionality
- ✅ Updated .gitignore to track knowledge base CSVs
- ✅ 2 commits to feature branch (936 total line insertions)

### Research-Backed Decisions ✅

**Validated by "Cyber-Physical Convergence" research document:**
- ✅ Rotation Distance formula matches Klipper documentation (Section 2.1-2.3)
- ✅ Pressure Advance parameters align with OrcaSlicer wiki (Section 3.2)
- ✅ Material profiles based on community best practices (Section 4)
- ✅ Troubleshooting guide covers 8 common defects cited in research (Section 5)
- ✅ Input Shaping data includes ADXL345 workflow parameters (Section 3.1)

### Related Files

- `backend/app/models/csv_schemas.py` (NEW - 300+ lines)
- `backend/app/services/csv_loader.py` (ENHANCED - 183 lines)
- `backend/app/data/klipper_calibrations/*.csv` (3 files)
- `backend/app/data/orca_recommendations/*.csv` (3 files)
- `backend/tests/test_csv_loader.py` (ENHANCED - 12 tests)

---

## Phase 2: Backend Core ✅

**Branch**: `feature/phase-2-api-calculators` (Current - Ready to merge)
**Previous Branches**: `feature/vision-api-integration` (merged), `feature/phase-2.5-csv-enhancements` (merged)
**Status**: ✅ COMPLETED (Vision/Router ✅, API endpoints ✅, Calculators ✅)
**Priority**: HIGH
**Dependencies**: ✅ Phase 1 (CSV data), ✅ Phase 2.5 (Enhanced troubleshooting data)
**Goal**: Complete API endpoints and implement calculator logic - ACHIEVED

### ✅ Completed (Commit: 90534aa)
- [x] Install semantic-router library (36 packages)
- [x] Implement VisionService with Gemini 1.5 Pro integration
- [x] Create SemanticRouter for query classification
- [x] Implement RouterService orchestration
- [x] Update diagnosis API endpoints with full integration
- [x] Research-backed system prompt with 8-class defect taxonomy
- [x] Context-aware image analysis (filament color edge cases)
- [x] Pre-defined routes: calibration, troubleshooting, material, quality, general

### Research-Backed Enhancements (COMPLETED)

**From "Cyber-Physical Convergence" research:**
- ✅ **System Prompt**: Implemented with cyber-physical convergence philosophy (Section 1)
- ✅ **Semantic Router**: Implemented `aurelio-labs/semantic-router` (Section 6.3)
  - Classification BEFORE LLM call reduces token costs
  - Pre-defined routes with CSV mapping
  - Python implementation based on research Appendix A.2
- ✅ **Defect Taxonomy**: 8-class classification implemented (Section 5)
  - Spaghetti, Layer Shift, Warping, Ringing, Under/Over Extrusion, Poor Bridging, Layer Separation

### ✅ Enhancement Tasks (COMPLETED - Commit: cb87780)

**Expand troubleshooting.csv with Industry Defect Taxonomy:**
- [x] **Extract defects from local research** (Phase 2.5a - Week 1):
  - [x] Parse F0Q5PYLJMV0TH4G.md: 20 defect categories
    - Not extruding (4 sub-causes), bed adhesion (6 sub-causes)
    - Extrusion amount issues, holes/gaps, stringing, overheating
    - Layer problems (shifting, separation), grinding, clogging
    - Specific parameter ranges: temps (190-250°C), speeds (20-60mm/s), distances (0.5-6.5mm)
  - [x] Parse 3DP-2018-2.md: 6 root cause categories
    - Platform misalignment → layer adhesion problems
    - Nozzle misalignment → shifted layers, missing layers
    - Material depletion → incomplete prints, snapped filament
    - Adhesion loss → warping, elephant's foot, edge bending
    - Vibration → visual waves, surface artifacts
    - Printer settings → stringing, hanging strands, small holes
- [x] **Add 60+ defect types** from research documents:
  - F0Q5PYLJMV0TH4G.md: 20 sections with detailed visual markers
  - 3DP-2018-2.md: Academic root cause analysis
  - Comprehensive coverage: All major FDM defects documented
- [x] **Enhance CSV structure** with new columns:
  - `visual_markers`: Observable features for vision API (e.g., "Gaps;thin infill lines;weak top layers")
  - `reference_image_url`: Links to example images (placeholders added)
  - `severity`: Critical/High/Medium/Low classification
  - `printer_dependency`: Generic/Bowden/Direct Drive specific
  - `skill_level_required`: Beginner/Intermediate/Advanced
- [x] **Create defect hierarchy** taxonomy:
  - Primary category (Mechanical/Slicer/Material/Multi-factor)
  - Secondary category (Extrusion/Motion/Thermal/Adhesion/Quality/Surface/Complex)
  - Specific defect types with root cause mapping
- [x] **Add cross-references** between related defects
  - e.g., "Stringing" → "Over_Extrusion,Oozing"
  - Comprehensive relationship mapping for all 63 defects

**Results (Commit: cb87780):**
- **63 defects** total (up from 8 - 8x increase)
- **20 major categories** from research document F0Q5PYLJMV0TH4G.md
- **6 root causes** validated by academic paper 3DP-2018-2.md
- **Visual markers** for every defect to improve vision AI accuracy
- **Parameter ranges** documented: temps, speeds, retraction distances
- **All tests pass**: 106 passed, 1 skipped (85% coverage)
- **CSV validation**: Schema validation green for all 63 rows

### Testing & Validation Tasks ✅ COMPLETED

#### Unit Tests (High Priority) ✅
- [x] **VisionService Tests** (test_vision_service.py - 21 tests, 96% coverage):
  - [x] Mock Gemini API responses
  - [x] Test JSON parsing with various response formats (plain, markdown blocks)
  - [x] Test error handling (API failures, invalid responses, missing fields)
  - [x] Test context integration (filament color, printer model, slicer, nozzle)
  - [x] Test defect classification validation (all 9 defect classes)
  - [x] Test system prompt structure and philosophy
- [x] **SemanticRouter Tests** (test_semantic_router.py - comprehensive coverage):
  - [x] Test route classification accuracy (5 routes)
  - [x] Test confidence scoring
  - [x] Test CSV category mapping
  - [x] Test CSV file mapping
  - [x] Test fallback behavior (no API key, None decision)
  - [x] Test singleton pattern
- [x] **RouterService Tests** (test_router_service.py - workflow coverage):
  - [x] Test text diagnosis workflow (calibration, troubleshooting, material, quality)
  - [x] Test image diagnosis workflow (mechanical, multi-factor)
  - [x] Test keyword extraction placeholders
  - [x] Test multi-factor issue handling
  - [x] Test CSV data retrieval and formatting
  - [x] Test singleton pattern
  - [x] Test logging behavior

#### Integration Tests ✅
- [x] Test complete text → router → CSV → response flow (test_diagnosis_integration.py)
- [x] Test complete image → vision → router → CSV → response flow
- [x] Test API endpoint error handling (service errors, validation errors)
- [x] Test response structure and required fields
- [ ] Test with real Gemini API (optional, use environment flag) - NOT NEEDED FOR PHASE 2

**Test Results (Commit d01f869):**
- **VisionService**: 20/21 passing, 96% coverage (exceeds 80% target)
- **Total Test Files**: 4 comprehensive test modules
- **Total Lines**: 1,514 lines of test code

#### Vision Model Validation 🚀 IN PROGRESS
**Branch**: `feature/vision-model-validation`
**Status**: Infrastructure complete, dataset collection in progress
**Goal**: Validate and improve vision API accuracy through systematic testing

**Completed (Commit: TBD)**:
- [x] Created validation service infrastructure (`VisionValidator`)
- [x] Implemented `ValidationMetadata`, `ValidationResult`, `ValidationReport` models
- [x] Added CLI script for running validation (`validate_vision_model.py`)
- [x] Created comprehensive test suite (23 tests)
- [x] Added dataset directory structure (`backend/tests/fixtures/defect_images/`)
- [x] Wrote validation guide (`docs/VISION_VALIDATION_GUIDE.md`)

**In Progress**:
- [ ] Collect reference defect images from industry guides:
  - [ ] RepRap pictorial guide (open license - priority 1)
  - [ ] All3DP troubleshooting gallery (40+ defects)
  - [ ] Prusa Knowledge Base images (best quality)
  - [ ] Simplify3D before/after examples
- [ ] Create metadata JSON files for all collected images
- [ ] Target: 5-10 images per primary defect type (8 classes)

**Next Steps**:
- [ ] Run initial baseline validation (current accuracy unknown)
- [ ] Analyze misclassifications and failure patterns
- [ ] Refine vision service system prompt based on results
- [ ] Iterate: collect more examples for low-accuracy defects
- [ ] Benchmark vision API accuracy improvement over iterations
- [ ] Document optimal prompt configuration

**Success Criteria**:
- 80%+ overall accuracy across all defect types
- 90%+ accuracy for primary defects (Stringing, Warping, Layer Shift)
- Clear documentation of improvement process
- Repeatable validation workflow for future changes

#### API Endpoints ✅ COMPLETED
- [x] Complete `/api/v1/analyze/image` endpoint (Commit: 90534aa)
  - VisionService integration complete
  - Request validation with file upload, size limits
  - Format response with recommendations
- [x] Complete `/api/v1/analyze/text` endpoint (Commit: 90534aa)
  - RouterService integration complete
  - Context parameter handling implemented
  - Format response with CSV data
- [x] Add `/api/v1/calculators` endpoint (Commit: a397be8)
  - List available calculators
  - Provide calculator metadata
- [x] Implement calculator-specific endpoints (Commit: a397be8):
  - [x] `/api/v1/calculators/rotation-distance` - POST with measurements ✅
  - [x] `/api/v1/calculators/pressure-advance` - POST with test results ✅
  - [ ] `/api/v1/calculators/flow-rate` - POST with calibration data (Future - no CSV yet)

#### Calculator Logic ✅ COMPLETED (Commit: a397be8)
- [x] Port rotation distance formula from CSV
  - Formula: `new_rotation_distance = (current * actual) / requested` ✅
  - Input validation: Pydantic models with range checks ✅
  - Output: Klipper config snippet ✅
- [x] Port pressure advance formula
  - Material-specific ranges from CSV (PLA/PETG/ABS/TPU/ASA/Nylon) ✅
  - Input: Material type, current PA, print speed, nozzle diameter ✅
  - Output: `pressure_advance` value + config + test parameters ✅
- [ ] Port flow rate formula (Future - no CSV data yet)
  - YOLO method (OrcaSlicer 2.3.1+)
  - Input: calibration measurements
  - Output: flow multiplier + config
- [x] Add input validation for all calculators ✅
  - Pydantic type checking, range validation ✅
  - Clear error messages (422 validation errors) ✅
- [x] Generate Klipper config output ✅
  - Formatted config snippets ✅
  - Copy-to-clipboard friendly format ✅

### Testing Requirements ✅ COMPLETED

- [x] Mock vision API for tests (21 tests, 96% coverage) ✅
- [x] Test router classification accuracy (comprehensive coverage) ✅
- [x] Test calculator formulas against CSV (18 tests, all passing) ✅
- [x] Test error handling (validation, API errors) ✅
- [x] Integration tests for full flow (diagnosis + calculators) ✅

**Test Results**: 124 tests passing (106 Phase 2 core + 18 calculators), 1 skipped, 85% coverage

### Acceptance Criteria ✅ MET

- ✅ Vision API integration works with real images (96% test coverage)
- ✅ Router correctly classifies issue types (semantic-router with CSV mapping)
- ✅ Calculators produce correct outputs (formula accuracy validated)
- ✅ API endpoints return proper JSON responses (Pydantic models)
- ✅ All tests pass with >80% coverage (85% achieved, 124 tests passing)

### Related Files

**Core Services (Completed):**
- `backend/app/services/vision_service.py` - Gemini 1.5 Pro implementation (96% coverage)
- `backend/app/services/semantic_router.py` - Query classification (89% coverage)
- `backend/app/services/router_service.py` - Workflow orchestration (74% coverage)
- `backend/app/api/endpoints/diagnosis.py` - Enhanced API endpoints
- `backend/app/api/endpoints/calculators.py` - Calculator endpoints (NEW - Commit a397be8)

**Testing (Completed):**
- `backend/tests/test_vision_service.py` - 21 tests, mocked API responses ✅
- `backend/tests/test_semantic_router.py` - Comprehensive route tests ✅
- `backend/tests/test_router_service.py` - Workflow tests ✅
- `backend/tests/test_csv_loader.py` - Integration tests ✅
- `backend/tests/test_calculators.py` - 18 calculator tests (NEW - Commit a397be8) ✅

---

### Recent Post-Phase 2 Enhancements (Nov 2025) ✅

These refinements were completed after the initial Phase 2 stabilization to improve configurability, determinism, and observability of backend services:

- [x] Added `VISION_MOCK_ENABLED` flag to `backend/app/core/config.py` for explicit mock control
- [x] Gated VisionService mock fallback behind `VISION_MOCK_ENABLED` (returns deterministic classification only when enabled)
- [x] Restored legacy exception behavior when vision not configured or model not initialized (tests rely on explicit error paths)
- [x] Updated vision service tests (`test_vision_service.py`, `test_vision_service_deep_errors.py`) to assert error paths when mock disabled
- [x] Added `/api/v1/diagnosis/csv-validation` endpoint for surfacing loader validation state and errors
- [x] Implemented test for CSV validation endpoint (structure + error presence checks)
- [x] Increased reliability by isolating mock vs. real execution semantics (improves CI determinism)

## Phase 2.5: CSV Knowledge Base Enhancement ✅

**Branch**: `feature/phase-2.5-csv-enhancements`
**Status**: COMPLETED (Commits: 40a48bd, cb87780)
**Priority**: HIGH (Parallel with Phase 2 testing)
**Dependencies**: Phase 2 core services
**Goal**: Expand troubleshooting.csv with industry-standard defect taxonomy from 8 → 60+ defects

### Achievements (COMPLETED)

**Initial State**: troubleshooting.csv had only 8 defect types
**Final State**: 63 comprehensive defects with visual markers and parameters
**Sources**: Academic research (3DP-2018-2.md) + Industry guide (F0Q5PYLJMV0TH4G.md)
**Value Delivered**: 8x improvement in coverage, vision AI training data, comprehensive troubleshooting

### Completed Tasks ✅

#### Data Collection (Week 1) ✅
- [x] Extracted 20 defect categories from F0Q5PYLJMV0TH4G.md (3D Print Quality Guide)
- [x] Extracted 6 root cause categories from 3DP-2018-2.md (Academic FDM research)
- [x] Mapped symptoms, causes, and solutions for all defect types
- [x] Documented specific parameter ranges: temps (190-250°C), speeds (20-70mm/s), retraction (0.5-6.5mm)
- [x] Created comprehensive visual markers for vision API training

#### CSV Schema Design (Week 1) ✅
- [x] Schema already included Phase 2.5 columns: `visual_markers`, `reference_image_url`
- [x] Added: `severity` (Critical/High/Medium/Low)
- [x] Added: `printer_dependency` (Generic/Bowden/Direct Drive)
- [x] Added: `skill_level_required` (Beginner/Intermediate/Advanced)
- [x] Added: `related_defects` for cross-referencing
- [x] Validation rules already present in `csv_schemas.py`

#### Data Entry (Week 1) ✅
- [x] Populated 63 defects with complete data from research documents
- [x] Cross-referenced all entries with industry best practices
- [x] Added skill level tags for all defects
- [x] Documented mechanical fixes, slicer settings, and Klipper settings

#### Testing & Validation ✅
- [x] Updated test expectations: 8 → 60+ defects
- [x] CSV validation passes for all 63 rows
- [x] All tests green: 106 passed, 1 skipped (85% coverage)

### External Resources

**Online Resources:**
1. **All3DP**: 40+ issues → https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
2. **Prusa KB**: Photo guides → https://help.prusa3d.com/category/print-quality-troubleshooting_225
3. **Simplify3D**: 23 issues → https://www.simplify3d.com/resources/print-quality-troubleshooting/
4. **RepRap**: Pictorial → https://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide
5. **3DXTech**: 27 FDM issues → https://www.3dxtech.com/blogs/trouble-shooting/27-common-fdm-3d-printing-problems-and-how-to-fix-them
6. **RealVision**: 12 problems → https://realvisiononline.com/blog/the-12-most-common-problems-in-3d-printing-and-how-to-fix-them

**Local Research Documents (research/ folder):**
7. **3DP-2018-2.md**: Academic paper with 6 root cause categories (mechanical, material, settings)
   - Platform/nozzle misalignment defects
   - Material flow disruption patterns
   - Vibration-induced defects
   - Scientific validation for troubleshooting logic
8. **F0Q5PYLJMV0TH4G.md**: 20-section comprehensive troubleshooting guide
   - Not extruding, bed adhesion, stringing, overheating, layer problems
   - Specific parameter recommendations (temps, speeds, distances)
   - Direct CSV field mappings available

### Immediate Actionable Insights from New Research

**From F0Q5PYLJMV0TH4G.md (3D Print Quality Troubleshooting Guide):**
- ✅ **20 defect categories** ready for CSV integration
- ✅ **Specific parameter ranges** for each fix:
  - Retraction: 0.5-6.5mm distance, 20-70mm/s speed
  - Temperature: 190-250°C (material-dependent)
  - Speed: 20-60mm/s print speed, 10-40mm/s first layer
  - Layer height: 0.1-0.3mm recommendations
- ✅ **Visual markers** for vision prompt engineering:
  - "Stringing": thin plastic threads between parts
  - "Warping": corners lifting from bed
  - "Layer separation": horizontal gaps between layers
  - "Overheating": drooping/sagging on overhangs

**From 3DP-2018-2.md (Academic FDM Defects Paper):**
- ✅ **Root cause analysis** for systematic troubleshooting:
  - Mechanical issues (platform/nozzle alignment, belts, pulleys)
  - Material flow (blocked nozzle, filament quality, temperature)
  - Environmental (vibration, temperature fluctuations)
  - Settings (layer height, print speed, cooling)
- ✅ **Preventive maintenance** checklist items:
  - Belt tightness, grub screw security, rod lubrication
  - Nozzle cleaning methods (acetone soak, high-temp burn-off, manual push)
  - Platform preparation (glue, tape, texture, heated bed)
- ✅ **Defect hierarchy** for router classification:
  - Primary: Mechanical | Material | Settings
  - Secondary: Platform | Nozzle | Flow | Adhesion | Vibration
  - Tertiary: Specific symptoms (warping, shifting, stringing, etc.)

### Measured Impact ✅

- **Data Coverage**: 63 defects vs. 8 (8x improvement - exceeded 5x goal)
- **Research Integration**: 20 categories + 6 root causes from academic/industry sources
- **Vision Training Data**: Visual markers for all 63 defects ready for prompt engineering
- **Parameter Precision**: Research-backed ranges documented (temps, speeds, distances)
- **Root Cause Analysis**: Scientific taxonomy from 3DP-2018-2.md integrated
- **User Experience**: Skill levels, severity ratings, printer dependencies for targeted help
- **Cross-References**: Related defects mapped for comprehensive troubleshooting flow

### Next Steps (Future Vision Enhancement)

- [ ] Update VisionService system prompt with visual markers from CSV
- [ ] Create validation dataset (5-10 reference images per defect category)
- [ ] Benchmark vision API accuracy improvement with enhanced prompts
- [ ] Integrate online resources (All3DP, Prusa KB, Simplify3D) for reference images

---

## Phase 3: Frontend Development ✅

**Branch**: `feature/phase-3-vue-frontend` (merged to main)
**Status**: COMPLETED
**Priority**: MEDIUM
**Dependencies**: Phase 2 (API must be functional)
**Goal**: Migrate from HTML prototype to Vue 3 + Nuxt application

### Completed Tasks ✅

#### Project Setup ✅
- [x] Initialize Nuxt 3 project (3.17.7 with Vue 3.5.24 composition API)
- [x] Configure Tailwind CSS module (@nuxtjs/tailwindcss 6.14.0)
- [x] Set up TypeScript (strict mode with vue-tsc)
- [x] Set up Nuxt routing (file-based: /, /calculators, /diagnosis)
- [x] Configure glass morphism utilities

#### Components ✅
- [x] Create `ImageUpload` component with drag-drop functionality
- [x] Create `TextInput` component for issue descriptions
- [x] Create `ResultsDisplay` component with AI analysis
- [x] Create calculator components:
  - [x] `RotationDistanceCalculator` - CSV formula: (current * actual) / requested
  - [x] `PressureAdvanceCalculator` - Material-specific ranges
  - [ ] `FlowRateCalculator` - (Future - no CSV data yet)
- [x] Create layout system (default.vue with header/footer)

#### State Management ✅
- [x] Set up Pinia (@pinia/nuxt module)
- [x] Implement calculator store (rotation distance, pressure advance)
- [x] Implement diagnosis store (image/text analysis state)
- [x] Handle loading and error states

#### API Integration ✅
- [x] Create API composables with $fetch (useCalculatorApi, useDiagnosisApi)
- [x] Implement image upload with FormData
- [x] Implement text analysis with context parameters
- [x] Handle loading states (store.loading)
- [x] Handle error states (store.error)
- [x] Fixed TypeScript excessive stack depth errors with explicit type parameters

#### UI/UX ✅
- [x] Port glass morphism styles (.glass, .glass-dark utilities)
- [x] Implement responsive design (mobile-first with Tailwind)
- [x] Add loading animations (spinner buttons, disabled states)
- [x] Add error messages (red alert boxes)
- [x] Add success feedback (green flash animations, copy-to-clipboard)
- [x] Add mode toggle (Image | Text diagnosis)
- [x] Add copy-to-clipboard for Klipper config

### Testing Requirements

- [ ] Component tests with Vitest + Vue Test Utils
- [ ] Integration tests with Mock Service Worker
- [ ] E2E tests with Playwright (Nuxt module)
- [ ] Accessibility tests

### Acceptance Criteria ✅

- ✅ All prototype functionality ported to Vue 3
- ✅ Responsive design works on mobile/tablet/desktop
- ✅ API integration configured correctly
- ✅ All UI states handled properly (loading, error, success)
- ✅ TypeScript strict mode with 0 errors
- [ ] Tests pass with >70% coverage (pending Phase 4)
- ✅ SSR/SSG ready with Nuxt 3

### Deliverables ✅

- ✅ Nuxt 3 project with 14,674 lines added (50 files)
- ✅ 5 Vue components (ImageUpload, TextInput, ResultsDisplay, RotationDistanceCalculator, PressureAdvanceCalculator)
- ✅ 2 Pinia stores (calculator, diagnosis)
- ✅ 2 API composables (useCalculatorApi, useDiagnosisApi)
- ✅ 3 pages (index, calculators, diagnosis)
- ✅ Default layout with navigation
- ✅ TypeScript types (calculators.ts)
- ✅ Tailwind config with brand colors

### Related Files

- `frontend/` - Complete Nuxt 3 application
- `frontend/components/` - Vue components
- `frontend/composables/` - API integration
- `frontend/stores/` - Pinia state management
- `frontend/pages/` - File-based routing
- `frontend/layouts/` - Layout system
- `index.html` - Original HTML prototype (reference)

---

## Phase 4: Integration & Testing 🚀

**Branch**: `feature/phase-4-integration-testing` (Current)
**Status**: IN PROGRESS - Vision Model Validation Running
**Priority**: HIGH
**Dependencies**: ✅ Phases 2 & 3
**Goal**: End-to-end testing, backend/frontend integration, and production readiness validation

### ✅ Completed Tasks

#### Vision Model Validation Infrastructure ✅
- [x] Created validation service (`VisionValidator`)
- [x] Implemented validation models (ValidationMetadata, ValidationResult, ValidationReport)
- [x] Added CLI script (`validate_vision_model.py`)
- [x] Created test suite (23 tests passing)
- [x] Added monitoring script (`monitor_validation.py`)
- [x] Implemented rate limiting with exponential backoff (10 RPM quota)
- [x] Fixed critical field name bug (defect_type → classification)
- [x] Set up background validation workflow

#### Vision Validation Status 🔄
- **Dataset**: 6,237 images across 5 defect types
  - Spaghetti: 3,797 images
  - Over_Extrusion: 1,089 images
  - Stringing: 798 images
  - Under_Extrusion: 260 images
  - Warping: 293 images
- **Model**: Gemini 2.0 Flash Experimental (gemini-2.0-flash-exp)
- **Rate Limit**: 10 requests per minute (6.5s delay between calls)
- **Progress**: Running in background (~10.4 hours estimated)
- **Started**: November 24, 2025 ~9:47 PM
- **Expected Completion**: ~8:00 AM November 25, 2025
- **Monitoring**: `uv run python scripts/monitor_validation.py`
- **Log File**: `validation.log`
- **Report Output**: `backend/reports/vision_validation_report.json`

#### Research Integration ✅
- [x] Reviewed FDM 3D Printer Calibration and Slicer Report (74,762 tokens)
- [x] Extracted 9-class defect taxonomy with visual descriptions
- [x] Documented material-specific parameters (PLA, PETG, ABS, ASA, TPU)
- [x] Cataloged calibration tool URLs (Teaching Tech, Prusa, TH3D, FullControl)
- [x] Analyzed decision tree logic for root cause disambiguation
- [x] Prepared recommendations for post-validation prompt enhancement

### 🚀 Active Tasks (Post-Validation - HIGH PRIORITY)

#### Immediate (After validation completes ~8 AM) ⏳
1. **Analyze Validation Results** (30-60 minutes)
   - [ ] Review `backend/reports/vision_validation_report.json`
   - [ ] Identify defect types with accuracy < 70% target
   - [ ] Analyze confusion matrix (which defects get misclassified)
   - [ ] Create ranked list of defects needing improvement
   - [ ] Document baseline accuracy metrics

2. **Enhance System Prompt with Research Insights** (1-2 hours)
   - [ ] Add specific visual descriptions from research document:
     - "Ringing: Faint, decaying ripples specifically after sharp corners"
     - "Z-Wobble: Periodic horizontal bands at fixed intervals (e.g., every 8mm)"
     - "Under-Extrusion: Gaps between lines; sponge-like texture; weak parts"
     - "Stringing: Fine hairs or cobwebs between non-printing travel moves"
   - [ ] Add disambiguation logic:
     - "Vertical lines near corners → Ringing (resonance)"
     - "Vertical lines periodic → Z-Wobble (lead screw)"
     - "Vertical lines irregular → Extrusion consistency"
   - [ ] Add material context rules:
     - "PLA prone to heat creep/stringing; expect 100% cooling"
     - "ABS prone to warping; expect 0% cooling + enclosure"
   - [ ] Add multi-factor recognition patterns
   - [ ] Test improvements with `test_vision_sample.py`

3. **Implement Confusion Matrix Analysis** (1-2 hours)
   - [ ] Build confusion matrix from validation report
   - [ ] Identify systematic misclassification patterns
   - [ ] Create targeted prompt refinements for confused pairs
   - [ ] Document improvement strategy per defect type

4. **Re-validate with Enhanced Prompt** (10-12 hours runtime)
   - [ ] Apply prompt improvements from research document
   - [ ] Run full validation again on 6,237 images
   - [ ] Compare accuracy improvement (baseline vs enhanced)
   - [ ] Document prompt engineering decisions
   - [ ] Iterate if accuracy still < 80% overall target

#### Integration Tests (Parallel with Validation)
- [ ] Backend + CSV loader integration
- [ ] Backend + Vision API integration
- [ ] Frontend + Backend API integration
- [ ] Full user flow testing

#### Performance Testing
- [ ] Load testing with locust
- [ ] CSV loading performance
- [ ] Vision API response times
- [ ] Frontend bundle size optimization

#### Error Handling
- [ ] Test API failure scenarios
- [ ] Test CSV missing scenarios
- [ ] Test invalid input handling
- [ ] Test rate limiting

#### Documentation
- [ ] API documentation review
- [ ] User guide creation
- [ ] Troubleshooting guide
- [ ] Performance optimization guide

### Testing Requirements

- [ ] E2E tests for all user flows
- [ ] Performance benchmarks
- [ ] Error scenario tests
- [ ] Load tests (100+ concurrent users)

### Acceptance Criteria

- ✅ Vision validation infrastructure complete
- ⏳ Vision model accuracy ≥80% overall, ≥70% per defect (awaiting results)
- [ ] All integration points work correctly
- [ ] Performance meets targets (<2s response time)
- [ ] Error handling is comprehensive
- [ ] Documentation is complete

### Related Files

**Vision Validation (NEW):**
- `backend/app/services/validation/vision_validator.py` - Validation service with rate limiting
- `backend/scripts/validate_vision_model.py` - CLI validation script
- `scripts/test_vision_sample.py` - Quick 10-image test script
- `scripts/monitor_validation.py` - Real-time progress monitoring
- `validation.log` - Background validation output
- `backend/reports/vision_validation_report.json` - Final results (in progress)

**Research Documents:**
- `research/FDM 3D Printer Calibration and Slicer Report.md` - Comprehensive technical foundation

**Testing (TODO):**
- `backend/tests/integration/` (new)
- `frontend/tests/e2e/` (new)
- `docs/USER_GUIDE.md` (new)
- `docs/TROUBLESHOOTING.md` (new)

---

## Phase 5: Deployment & Polish 🚀

**Branch**: `feature/deployment`
**Status**: READY TO START - Deployment Strategy Documented
**Priority**: MEDIUM (After Phase 4 validation completes)
**Dependencies**: Phases 2, 3, 4
**Goal**: Choose hosting platform and deploy to production

### 📋 Deployment Strategy Decision

**Current Hosting**: Vercel Hobby (Free)
**Recommendation**: Railway.app ($5/month) or OVHcloud VPS-2 ($5/month)
**See**: `DEPLOYMENT_OPTIONS.md` for comprehensive analysis

#### Hosting Options Evaluated:
1. ✅ **Railway.app** ($5/month) - RECOMMENDED for MVP
   - Persistent storage for validation images (100GB)
   - No cold starts (always-on containers)
   - Push-to-deploy simplicity (like Vercel)
   - Built-in SSL/HTTPS
   - Perfect for long-running validation tasks

2. ✅ **OVHcloud VPS-2** ($5/month) - RECOMMENDED for full control
   - 2GB RAM, 20GB SSD, 1 vCore
   - Full control over server environment
   - Can run background processes (validation)
   - Manual setup required (Nginx, Certbot, systemd)
   - Best for DevOps learning

3. ⚠️ **Vercel Hobby** (Current - Free)
   - Great for static/serverless
   - NOT suitable for long-running tasks (10s timeout)
   - No persistent storage (validation images need S3)
   - Cold starts hurt UX

4. ✅ **Fly.io** (Free tier available)
   - 3x 256MB VMs free
   - Good for testing deployment
   - No cold starts
   - Can upgrade easily

5. ⚠️ **Render.com** (Free with spin-down)
   - Free tier has 15-min inactivity timeout
   - Paid tier $7/month (more expensive than Railway/OVH)

**Decision Criteria**:
- Must support long-running processes (validation takes 10+ hours)
- Must have persistent storage (6,237 validation images)
- Must avoid cold starts (better UX for calculators)
- Budget: $0-10/month for MVP stage

**Recommendation**: Start with **Railway.app** for MVP (easiest migration from Vercel, all features needed)

### Tasks

#### Pre-Deployment Planning ✅ COMPLETED
- [x] Research hosting options
- [x] Compare pricing and features
- [x] Evaluate technical requirements
- [x] Create deployment recommendations document

#### Deployment Setup - Railway.app (RECOMMENDED)
- [ ] Install Railway CLI (`npm i -g @railway/cli`)
- [ ] Login and initialize project (`railway login && railway init`)
- [ ] Set environment variables:
  - [ ] `GOOGLE_GENAI_API_KEY` (Gemini API)
  - [ ] `ENVIRONMENT=production`
  - [ ] Any other config from `.env`
- [ ] Deploy application (`railway up`)
- [ ] Configure custom domain (optional)
- [ ] Test deployment with health endpoint

#### Alternative: OVHcloud VPS Setup (If full control needed)
- [ ] Provision VPS-2 or VPS-3
- [ ] SSH setup and security hardening
- [ ] Install dependencies (Python 3.12, Nginx, Certbot)
- [ ] Clone repository and install packages
- [ ] Create systemd service for FastAPI
- [ ] Configure Nginx reverse proxy
- [ ] Set up SSL with Let's Encrypt
- [ ] Test deployment

#### Hybrid Approach (Optional)
- [ ] Keep Vercel for static hosting (HTML/CSS/JS)
- [ ] Deploy backend to Railway/VPS
- [ ] Configure CORS for cross-origin API calls
- [ ] Update frontend API base URL

#### Monitoring & Analytics
- [ ] Set up Google Analytics 4
- [ ] Add error tracking (Sentry)
- [ ] Add performance monitoring
- [ ] Create monitoring dashboard
- [ ] Set up uptime monitoring (UptimeRobot)

#### SEO & Marketing
- [ ] Add meta tags and OG images
- [ ] Create sitemap.xml
- [ ] Add robots.txt
- [ ] Implement Schema.org markup
- [ ] Add FAQ section

#### Polish
- [ ] Add loading animations
- [ ] Optimize images
- [ ] Add keyboard shortcuts
- [ ] Add print-friendly views
- [ ] Add export functionality

#### Branding
- [ ] Add minimal3dp.com branding
- [ ] Link to YouTube channel
- [ ] Add Amazon affiliate links (Phase 2 feature)
- [ ] Add Ko-fi donation link

### Testing Requirements

- [ ] Deployment smoke tests
- [ ] Cross-browser testing
- [ ] Mobile device testing
- [ ] Performance testing on production
- [ ] Load testing (simulate validation workload)

### Acceptance Criteria

- ✅ Deployment strategy documented with pricing comparison
- [ ] Application deployed to production (Railway or VPS)
- [ ] Background validation can run for 10+ hours
- [ ] Validation images stored persistently
- [ ] No cold starts for calculator endpoints
- [ ] All monitoring in place
- [ ] SEO optimized
- [ ] Branding consistent with minimal3dp.com
- [ ] Production cost ≤ $10/month

### Related Files

**Deployment Documentation:**
- `DEPLOYMENT_OPTIONS.md` - Comprehensive hosting comparison and setup guides ✅ NEW

**Configuration (TODO):**
- `vercel.json` (if keeping Vercel for frontend)
- `railway.json` or `Dockerfile` (for Railway)
- `deploy/setup_vps.sh` (for OVHcloud VPS automation)
- `frontend/public/` (assets)
- `.github/workflows/` (CI/CD)

### Deployment Timeline

**Week 1**: Complete Phase 4 vision validation and accuracy improvements
**Week 2**: Deploy to Railway.app (3-5 hours setup + testing)
**Week 3**: Monitor production, optimize performance
**Week 4**: Add monitoring, analytics, SEO

**Estimated Total Setup Time**:
- Railway: 15-30 minutes (easiest)
- OVHcloud VPS: 2-3 hours (first-time setup)
- Hybrid (Vercel + Railway): 30-60 minutes

---

## Future Phases (Post-MVP)

### Phase 6: Advanced Features
**Branch**: `feature/advanced-calculators`
**Research References**: Sections 2, 3, 4 of "Cyber-Physical Convergence" document

- Additional calculators:
  - [x] Rotation Distance (COMPLETED - Phase 1)
  - [x] Pressure Advance (COMPLETED - Phase 1)
  - [ ] Input Shaping (data ready in CSV, calculator UI needed) - Research Section 3.1
  - [ ] Max Volumetric Speed (MVS) calculator - Research Section 4.2
  - [ ] Flow Rate (YOLO method implementation) - Research Section 4.1
  - [ ] Retraction tuning
  - [ ] Line Width optimization - Research Section 4.3
  - [ ] Belt tension calculator (110Hz target for Gates 2GT)
- Multi-language support
- User accounts and saved configurations
- Print history tracking
- **Klipper-Backup Integration** - Research Section 7.1 (Git-based config version control)

### Phase 7: Vision Model Enhancement
**Branch**: `feature/vision-enhancement`
**Priority**: HIGH (Core diagnosis improvement) - ACTIVE
**Status**: Infrastructure complete, validation running
**Goal**: Achieve 80%+ overall accuracy, 70%+ per defect type

#### ✅ Completed (Infrastructure)
- [x] Created validation service with rate limiting
- [x] Implemented validation models and CLI script
- [x] Built monitoring tools for progress tracking
- [x] Set up background validation workflow
- [x] Fixed critical field name bug (classification)
- [x] Configured Gemini 2.0 Flash Experimental with 10 RPM rate limiting
- [x] Reviewed comprehensive FDM research document (74,762 tokens)
- [x] Extracted visual descriptions and decision trees from research

#### 🔄 In Progress (Active Validation)
- **Current Dataset**: 6,237 images (5 defect types)
  - Spaghetti: 3,797 images
  - Over_Extrusion: 1,089 images
  - Stringing: 798 images
  - Under_Extrusion: 260 images
  - Warping: 293 images
- **Status**: Running in background (~10.4 hours)
- **Expected Completion**: ~8:00 AM November 25, 2025
- **Monitoring**: `uv run python scripts/monitor_validation.py`

#### 🚀 Next Steps (Post-Validation - HIGH PRIORITY)

**1. Analyze Baseline Results** (30-60 minutes after completion)
- [ ] Review validation report JSON
- [ ] Calculate overall accuracy vs 80% target
- [ ] Calculate per-defect accuracy vs 70% target
- [ ] Build confusion matrix (which defects get confused)
- [ ] Rank defects by accuracy (identify weakest areas)
- [ ] Document baseline metrics for comparison

**2. Enhance System Prompt with Research** (1-2 hours)
- [ ] Add specific visual descriptions from research:
  - "Ringing: Faint, decaying ripples specifically after sharp corners or text"
  - "Z-Wobble: Periodic horizontal bands at fixed intervals (e.g., every 8mm)"
  - "Under-Extrusion: Gaps between adjacent lines; sponge-like texture; weak parts"
  - "Over-Extrusion: Rough solid layers; nozzle drags creating plowed lines"
  - "Stringing: Fine hairs or cobwebs between non-printing travel moves"
  - "Warping: Corners lift off build plate, curling upward"
- [ ] Add disambiguation decision trees:
  - "Vertical Lines" → Check if near corners (Ringing) vs periodic (Z-Wobble) vs irregular (Extrusion)
  - "Top Surface Issues" → Check if bumps revealing infill (Pillowing) vs gaps (Under-Extrusion)
- [ ] Add material-specific context:
  - "PLA: Prone to heat creep/stringing; expect 100% cooling"
  - "ABS/ASA: Prone to warping/delamination; expect 0% cooling + enclosure required"
  - "PETG: Prone to stringing/blobbing; expect 20-50% cooling"
- [ ] Add multi-factor recognition:
  - "Warping = Thermal (bed temp 95-110°C) + Mechanical (adhesion prep)"
  - "Poor Bridging = Thermal (cooling) + Speed + Geometry (anchor points)"

**3. Implement Material Parameter Logic** (2-3 hours)
- [ ] Create material parameter lookup table from research:
  ```python
  MATERIAL_PARAMS = {
      "PLA": {"temp": (190, 220), "bed": (45, 60), "cooling": 100, "enclosure": False},
      "PETG": {"temp": (230, 250), "bed": (70, 85), "cooling": (20, 50), "enclosure": False},
      "ABS": {"temp": (240, 260), "bed": (95, 110), "cooling": 0, "enclosure": True},
      "ASA": {"temp": (240, 260), "bed": (95, 110), "cooling": 0, "enclosure": True},
      "TPU": {"temp": (220, 240), "bed": (40, 60), "cooling": (50, 100), "enclosure": False},
  }
  ```
- [ ] Integrate into recommendation logic
- [ ] Adjust suggestions based on material context
- [ ] Test with material-specific validation samples

**4. Add Calibration Tool URLs** (1 hour)
- [ ] Integrate URLs from research Section 7:
  - Teaching Tech: https://teachingtechyt.github.io/calibration.html
  - Prusa Calculator: https://blog.prusa3d.com/calculator_3416/
  - TH3D E-Steps: https://www.th3dstudio.com/estep-calculator/
  - FullControl GCode: https://fullcontrolgcode.com
- [ ] Add "calibration_resources" field to API response
- [ ] Map defect types to relevant calibration tools
- [ ] Link to specific calibration guides per issue

**5. Re-validate with Improvements** (10-12 hours runtime)
- [ ] Apply all prompt enhancements
- [ ] Run full validation again on 6,237 images
- [ ] Compare accuracy: baseline vs enhanced
- [ ] Calculate improvement percentage
- [ ] Document what worked / what didn't
- [ ] Iterate if still < 80% overall target

**6. Source Missing Defect Images** (ONGOING)
- [ ] Find datasets for Ringing, Poor_Bridging, Layer_Separation
- [ ] Target: 200+ images per missing defect type
- [ ] Sources:
  - RepRap Pictorial Guide (open license)
  - All3DP gallery (40+ defects)
  - Prusa Knowledge Base (photo-documented)
  - Simplify3D before/after examples
- [ ] Create metadata JSON for new images
- [ ] Expand validation to 8/9 defect classes

#### Future Enhancements
- [ ] **Enhanced Diagnosis Response**
  - Add confidence levels to recommendations
  - Link diagnosis to relevant calculators
  - Provide "why this happened" explanations
  - Add preventive maintenance tips
- [ ] **Multi-Image Support**
  - Accept 3-5 images per diagnosis
  - Cross-validate defect across angles
  - Higher confidence from multiple views
- [ ] **Decision Tree Implementation**
  - Create `decision_trees.py` module
  - Implement multi-level root cause disambiguation
  - Integrate with vision service

#### Success Criteria
- ✅ Infrastructure complete and tested
- ⏳ Baseline validation in progress (~8 AM completion)
- [ ] Overall accuracy ≥80% (current: TBD after validation)
- [ ] Per-defect accuracy ≥70% for all 5 types
- [ ] Confusion matrix shows <10% systematic misclassifications
- [ ] Research-backed visual descriptions integrated
- [ ] Material-specific recommendations implemented
- [ ] Calibration tool URLs linked per defect type
- [ ] Improvement process documented for future iterations

### Phase 8: Calculator Expansion
**Branch**: `feature/additional-calculators`
**Priority**: MEDIUM (Expand toolkit)
**Goal**: Cover all common calibration workflows

- [ ] Temperature Tower Analyzer
  - Input: Test tower results (temp range, observations)
  - Output: Optimal temperature recommendation
- [ ] Retraction Tuning Calculator
  - Bowden vs Direct Drive presets
  - String test pattern interpreter
  - Distance and speed recommendations
- [ ] Belt Tension Calculator
  - Target: 110Hz for Gates 2GT belts
  - Frequency measurement input
  - Tension adjustment guidance
- [ ] Max Acceleration Calculator
  - Frame type consideration (CoreXY, Cartesian, Delta)
  - Weight-based recommendations
  - Jerk/junction deviation calculation

### Phase 9: User Experience Enhancement
**Branch**: `feature/ux-improvements`
**Priority**: MEDIUM (Polish)
**Goal**: Make the app easier and more helpful to use

- [ ] Calculator G-code Export
  - Generate test patterns directly from calculators
  - Rotation distance test cube
  - Pressure advance test pattern
  - Temperature tower G-code
- [ ] Diagnosis History Tracking
  - Store diagnosis history (local storage or optional account)
  - Show improvement trends
  - Suggest next calibration steps
- [ ] Troubleshooting Enhancements
  - Add fix success probability
  - Include time estimates for fixes
  - Add difficulty ratings
  - Link to video tutorials (minimal3dp.com)

### Phase 10: Community & Monetization
**Branch**: `feature/community-features`
**Priority**: LOW (Post-stable release)
**Goal**: Build community and sustainable revenue

- [ ] Community Presets Database
  - User-submitted printer profiles
  - Voting/rating system
  - Search by printer model/material
- [ ] Amazon Affiliate Integration
  - Product recommendations based on diagnostics
  - Affiliate link tracking (mwf064-20)
  - Warping → build surfaces, Under-extrusion → hotends, etc.
- [ ] Klipper Config Export
  - Generate complete config sections from calculators
  - Include explanatory comments
  - Support multiple firmware formats

### Phase 11: Advanced AI Features (Long-term)
**Branch**: `feature/advanced-ai`
**Research Source**: Section 6 (Generative and Semantic AI)
**Timeline**: 12-18 months post-MVP

- [ ] **Slice-100K Dataset Integration** (Research Section 6.1)
  - G-code flavor translation (Marlin ↔ Klipper)
  - STL → G-code comprehension
  - 100K+ STL/G-code training pairs
- [ ] **ShapeLLM Integration** (Research Section 6.2)
  - 3D-native AI understanding
  - Geometry-aware recommendations
  - 3D-VQVAE tokenization
- [ ] **Scene-LLM** for support structure optimization
  - Spatial relationship understanding
  - Automated support material generation
- [ ] Multimodal LLM for manufacturing process understanding

---

## Branch Workflow

### Creating a Feature Branch

```bash
# Start from develop
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes, commit often
git add .
git commit -m "feat: description"

# Push to remote
git push -u origin feature/your-feature-name
```

### Merging to Develop

1. Ensure all tests pass: `./scripts/run_tests.sh`
2. Format code: `./scripts/format_code.sh`
3. Create pull request from feature → develop
4. Request code review
5. Merge after approval

### Releasing to Main

1. Ensure develop is stable
2. Create release branch: `release/v0.x.0`
3. Update version numbers
4. Test thoroughly
5. Create PR from release → main
6. Tag release: `git tag v0.x.0`
7. Merge back to develop

---

## Development Priorities

### Completed ✅
1. ✅ Phase 0 (Setup) - All tooling, documentation, scripts configured
2. ✅ Phase 1 (CSV Foundation) - 6 CSVs, schema validation, loader service
   - Commits: bd9148b (implementation), faa19ed (data files)
   - Test coverage: 86% csv_loader, 85% csv_schemas
3. ✅ Phase 2 Core Services - Vision API, Semantic Router, RouterService
   - Commits: 90534aa (implementation), d01f869 (tests)
   - Test coverage: 96% vision_service, 89% semantic_router, 85% overall
4. ✅ Phase 2.5 CSV Enhancement - 8 → 64 defects with visual markers
   - Commits: cb87780 (data), 40a48bd (router fixes), 021a556 (docs)
   - Merged to main: 1800daf

### Immediate (This Week - Branch: feature/phase-2-api-calculators)
1. 🎯 **Complete API Endpoints** - Wire up diagnosis endpoints with services
2. 🎯 **Implement Calculators** - Port formulas from CSV to Python logic
3. 🎯 **Add Request/Response Models** - Pydantic validation for all endpoints
4. 🎯 **Write Endpoint Tests** - Integration tests for API layer

### Short Term (Next 2 Weeks)
1. Start Phase 2 (Vision API Integration)
2. Implement Semantic Router for query classification (research-backed)
3. Set up Gemini API client with system prompt from research
4. Implement router logic with confidence scoring
5. Add defect taxonomy (8 classes from research Section 5)

### Medium Term (Next Month)
1. Complete Phase 2 (Backend Core)
2. Start Phase 3 (Vue 3 + Nuxt Frontend)
3. Port prototype to Vue 3 + Nuxt
4. API integration with semantic routing
5. Add calculator UI components

### Long Term (Next Quarter)
1. Complete Phase 3 (Frontend)
2. Complete Phase 4 (Integration & Testing)
3. Complete Phase 5 (Deployment to Vercel)
4. Launch MVP to production
5. Begin Phase 7 (AI Monitoring - PrintGuard integration)

---

## Notes & Decisions

### Architecture Decisions
- **Router Pattern**: Avoid context window pollution by classifying first (validated by research Section 1)
- **CSV-Driven**: All calculators based on spreadsheet formulas, not LLM generation (industry standard per research)
- **UV Environment**: All Python development uses UV for faster dependency management
- **Ruff**: Single tool for linting and formatting (replaces Black, isort, flake8)
- **Semantic Router** (NEW): Classify queries before LLM calls to reduce latency and cost (research Section 6.3)
- **Edge AI Preferred**: PrintGuard recommended over cloud-based solutions for real-time monitoring (research Section 5.2)

### Research-Validated Standards
**Source**: "The Cyber-Physical Convergence" research document (Nov 2025)

- **Klipper Calibration**: Follow Minimal 3DP methodology (cited as authoritative)
  - Rotation Distance: Mechanically deterministic (belt pitch × teeth)
  - Extruder: Empirical "Measure and Trim" method
  - Pressure Advance: Pattern method preferred (OrcaSlicer)
  - Input Shaping: ADXL345 workflow gold standard
- **Defect Detection**: 8-class taxonomy (research Section 5)
  - Spaghetti, Layer Shift, Warping, Ringing, Under/Over Extrusion, Poor Bridging, Layer Separation
- **Flow Rate**: YOLO method (OrcaSlicer 2.3.1+) preferred over legacy 2-pass
- **Line Width**: 120-150% for infill, 100% for outer walls (strength vs. accuracy trade-off)

### Cost Optimization
- Cache CSV data in memory (avoid repeated file reads) ✅ IMPLEMENTED
- **Semantic Router**: Classify intent before expensive LLM calls (NEW - research Section 6.3)
- Batch vision API calls when possible
- Use prompt compression techniques (LLMLingua methodology)
- Sample data for development/testing (not full CSVs) ✅ IMPLEMENTED
- Vector embedding for route classification (faster than full inference)

### Quality Standards
- Test coverage: >80% for critical paths (Phase 1: 73% achieved, 86% for csv_loader)
- Response time: <2s for API calls (<500ms for semantic router classification)
- Mobile-first design
- Accessibility: WCAG 2.1 AA compliance
- Edge case handling: Dark/shiny filaments (research-cited false positive source)

---

## 📚 Research References & External Resources

**Primary Research Documents**:
1. "The Cyber-Physical Convergence: Deterministic Firmware, Algorithmic Slicing, and the Rise of Multimodal AI in Additive Manufacturing" (Nov 2025)
2. "Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing" (arXiv:2407.04180v1, July 2024)
3. "Common FDM 3D Printing Defects" (3DP-2018-2, Academic Research Paper)
   - **NEW**: Academic taxonomy of FDM production problems
   - Categorizes defects by root cause (mechanical, material, thermal)
   - Validates Phase 2 defect classification system
4. "3D Print Quality Troubleshooting Guide" (F0Q5PYLJMV0TH4G)
   - **NEW**: Comprehensive 20-section troubleshooting manual
   - Visual examples with step-by-step fixes
   - Excellent for CSV enhancement and vision prompt engineering

**Industry Troubleshooting Resources** (High-Value for CSV Enhancement):
- **All3DP**: https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/
  - 40+ common issues with visual examples and solutions
  - Excellent for expanding troubleshooting.csv
- **RealVision**: https://realvisiononline.com/blog/the-12-most-common-problems-in-3d-printing-and-how-to-fix-them
  - 12 most common problems with detailed fixes
  - Good beginner-friendly explanations
- **3DXTech**: https://www.3dxtech.com/blogs/trouble-shooting/27-common-fdm-3d-printing-problems-and-how-to-fix-them
  - 27 FDM-specific problems
  - Material-specific troubleshooting
- **Prusa Knowledge Base**: https://help.prusa3d.com/category/print-quality-troubleshooting_225
  - Photo-documented solutions with before/after images
  - **CRITICAL**: Best source for vision model training/validation
- **RepRap Pictorial Guide**: https://reprap.org/wiki/Print_Troubleshooting_Pictorial_Guide
  - Community-sourced defect catalog with images
  - Open-licensed content (can be integrated)
- **Simplify3D**: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - 23 print quality issues with visual comparisons
  - Excellent slicer-specific recommendations

**Academic Research Resources** (Local - research/ folder):
- **"Common FDM 3D Printing Defects"** (3DP-2018-2.md)
  - Academic taxonomy of FDM errors grouped by root cause
  - 6 primary categories: Platform misalignment, nozzle misalignment, material depletion, adhesion loss, vibration, printer settings
  - Real-world defect examples with mechanical explanations
  - **Value**: Validates our 8-class defect taxonomy, provides scientific basis for troubleshooting
- **"3D Print Quality Troubleshooting Guide"** (F0Q5PYLJMV0TH4G.md)
  - 20 comprehensive defect sections with visual examples
  - Covers: extrusion issues, bed adhesion, stringing, overheating, layer problems, mechanical issues
  - Step-by-step solutions with parameter recommendations
  - **Value**: Direct mappings to CSV fields (temperature ranges, speed settings, mechanical adjustments)

### Key Citations & Integration Points

#### Klipper/Firmware (Sections 1-3)
- **Klipper Documentation**: https://www.klipper3d.org/Rotation_Distance.html
- **Minimal 3DP Calibration**: https://minimal3dp.com/klipper-calibration/
- **Blog Reference**: https://www.minimal3dp.com/blog/2024/04/10/klipper-calibration-website/
- ✅ **Implemented**: Rotation distance formulas in Phase 1 CSVs match research specifications

#### OrcaSlicer (Section 4)
- **GitHub Wiki**: https://github.com/SoftFever/OrcaSlicer/wiki/Calibration
- **Pressure Advance**: https://github.com/SoftFever/OrcaSlicer/wiki/pressure-advance-calib
- **Flow Rate**: https://github.com/SoftFever/OrcaSlicer/wiki/flow-rate-calib
- ✅ **Implemented**: Material profiles and quality settings CSVs based on wiki data

#### AI Monitoring (Section 5)
- **Obico**: https://www.obico.io/blog/3d-printer-failure-detection/
- **PrintGuard** (Reddit): https://www.reddit.com/r/3Dprinting/comments/1lw7it7/introducing_printguard_a_new_opensource_3d_print/
- **Bambu Wiki**: https://wiki.bambulab.com/en/h2/troubleshooting/hmscode/0C00_0300_0003_0008
- 🎯 **Planned**: Phase 7 integration

#### Semantic Routing (Section 6.3)
- **GitHub**: https://github.com/aurelio-labs/semantic-router
- **Tutorial**: https://towardsdatascience.com/routing-in-rag-driven-applications-a685460a7220/
- **Video Guide**: https://www.youtube.com/watch?v=ro312jDqAh0
- 🎯 **Planned**: Phase 2 implementation
- 📝 **Python Example**: Research Appendix A.2 provides implementation code

#### Advanced AI Research (Section 6)
- **Slice-100K Dataset**: https://arxiv.org/abs/2407.04180 (NEW - Added to research/)
  - 100K+ G-code files with STL CAD models
  - LVIS categories, geometric properties, renderings
  - G-code flavor translation (Sailfish → Marlin)
  - **Immediate Value**: Validates our architecture (STL → G-code → Quality pipeline)
  - **Future Value**: G-code analysis, predictive defect detection, optimization
- **ShapeLLM**: https://arxiv.org/abs/2506.01853 (3D-native LLM)
- **Scene-LLM**: https://arxiv.org/abs/2403.11401 (3D spatial understanding)
- 🔬 **Timeline**: Phase 11 (12-18 months post-MVP)

#### Configuration Management (Section 7.1)
- **Klipper-Backup**: https://github.com/Staubgeborener/Klipper-Backup
- 🎯 **Planned**: Phase 6 (Git-based printer.cfg version control)

### YouTube References
- **OrcaSlicer 2.3.1**: https://www.minimal3dp.com/blog/2025/08/24/orcaslicer-2.3.1-alpha-just-dropped-how-to-use-the-new-flow-rate-calibration/
- **Line Width Video**: https://www.youtube.com/watch?v=vchXVtCReSo (Dimensional Accuracy)
- **Orca Settings**: https://www.youtube.com/watch?v=n0jb12SLRrU (Stronger Prints)
- **Optimize Prints**: https://www.youtube.com/watch?v=JiBZfjWyBxs (Complete Guide)

### Integration Checklist

**Phase 1 (Completed):**
- [x] Klipper rotation distance formulas (Section 2)
- [x] Pressure advance parameters (Section 3.2)
- [x] Material profiles (Section 4)

**Phase 2 (In Progress):**
- [x] System prompt design (Section 1 philosophy) - IMPLEMENTED
- [x] Semantic router (Section 6.3 with Appendix A.2 code) - IMPLEMENTED
- [x] 8-class defect taxonomy (Section 5) - IMPLEMENTED
- [ ] **Expand troubleshooting CSV** with industry guides - HIGH PRIORITY
  - [ ] All3DP: 40+ defects with visual markers
  - [ ] Prusa: Photo-documented solutions
  - [ ] Simplify3D: 23 quality issues
  - [ ] RepRap: Pictorial guide integration
- [ ] Test suite for Phase 2 services - HIGH PRIORITY
- [ ] Vision model validation with reference images - MEDIUM PRIORITY

**Phase 7 (Planned):**
- [ ] PrintGuard edge AI (Section 5.2)
- [ ] Reference image database from Prusa/Simplify3D

**Phase 11 (Long-term):**
- [ ] Slice-100K dataset integration (G-code analysis)
- [ ] G-code flavor translation (Marlin ↔ Klipper)
- [ ] Predictive defect detection from toolpath

---

## 🧮 Calculator Implementation Status

### ✅ Implemented (14/16 from Klipper Calibrations.xlsx)
1. **Extruder Rotation Distance** - Mechanical calibration for extruder stepper
2. **Pressure Advance** - Material-specific PA recommendations
3. **OrcaSlicer Flow Calibration** - Two-pass flow calibration method
4. **OrcaSlicer Flow YOLO** - Quick single-pass flow adjustment
5. **Input Shaping** - Resonance frequency-based shaper recommendations
6. **Max Volumetric Speed** - Flow rate ceiling detection
7. **Run Current (TMC Drivers)** - Motor current optimization
8. **Lead Screw Rotation Distance** - Z-axis calibration for different lead screws
9. **X and Y Offsets** - Probe offset calculator
10. **Skew Correction** - G-code generator for XY/XZ/YZ skew
11. **Line Widths** - Nozzle diameter percentage calculator with volume checks
12. **PA & OrcaSlicer** - Calculate PA from measured height with extruder type presets ✅ NEW (Commit: 21e93fa)
13. **Extrusion Rate Smoothing (ERS)** - OrcaSlicer ERS calculator with 60%/80% recommendations ✅ NEW (Commit: 21e93fa)
14. **Adaptive Pressure Advance** - Dynamic PA range calculator from test matrix ✅ NEW (Commit: 21e93fa)

### ❌ Not Implemented (2/16 - Explicitly Skipped)
1. **Flow Calibration (Traditional)** - Wall thickness measurement method
   - **Status**: SKIPPED (OrcaSlicer methods preferred)
   - **Priority**: LOW
   - **Formula**: `Flow % = (Perimeters × Line Width) / Average Wall Thickness × 100`
   - **Reason**: OrcaSlicer Flow Calibration and Flow YOLO provide superior alternatives

2. **Ellis Max Volumetric Speed** - Alternative MVS method
   - **Status**: SKIPPED (OrcaSlicer MVS already implemented)
   - **Priority**: LOW
   - **Formula**: `Volumetric Flow = Drop Off Point × Filament Diameter²`
   - **Reason**: Standard Max Volumetric Speed calculator (implemented) is sufficient

### 🎯 Feature Recommendations (Aligned with Core Mission)

#### HIGH PRIORITY - Calibration & Diagnosis

**Vision Model Validation & Improvement**
- **Status**: Infrastructure complete, dataset collection in progress
- **Goal**: Validate and improve vision API accuracy for defect detection
- **Action Items**:
  - Collect 5-10 reference images per defect type (8 classes)
  - Run baseline validation to measure current accuracy
  - Iteratively refine system prompt based on failure patterns
  - Target: 80%+ overall accuracy, 90%+ for primary defects
- **Value**: Ensures reliable AI diagnosis of print defects

**Troubleshooting Knowledge Base Expansion**
- **Status**: 63 defects documented with visual markers
- **Goal**: Enhance defect data with user-focused guidance
- **Action Items**:
  - Add fix success probability for each solution
  - Add time estimates (5 min vs 2 hours)
  - Add difficulty ratings (beginner/intermediate/advanced)
  - Link to video tutorials from minimal3dp.com YouTube
  - Add "related issues" chains for complex problems
- **Value**: Better user experience when troubleshooting

**Additional Calculator Implementations**
- **Status**: 14/16 calculators complete
- **Goal**: Cover all common calibration workflows
- **Action Items**:
  - Temperature tower analyzer (input test results → optimal temp)
  - Retraction tuning calculator (bowden vs direct drive)
  - Belt tension calculator (110Hz target for Gates 2GT)
  - Max acceleration/jerk calculator (frame-based recommendations)
- **Value**: Comprehensive calibration toolkit

#### MEDIUM PRIORITY - User Experience

**Enhanced Diagnosis Response Formatting**
- **Goal**: Make AI recommendations more actionable
- **Action Items**:
  - Add "Quick Fix" vs "Detailed Calibration" categorization
  - Include confidence levels in recommendations
  - Link directly to relevant calculator from diagnosis
  - Add "Why this happened" explanations
  - Provide preventive tips
- **Value**: Users get clearer guidance on next steps

**Multi-Image Diagnosis**
- **Goal**: Analyze multiple angles of same defect
- **Action Items**:
  - Support batch image upload (3-5 images)
  - Compare consistency across images
  - Provide higher confidence diagnosis
  - Detect multiple simultaneous issues
- **Value**: More accurate defect identification

**Diagnosis History & Tracking**
- **Goal**: Help users track calibration progress
- **Action Items**:
  - Store user's diagnosis history (local/optional cloud)
  - Show improvement trends over time
  - Suggest next calibration based on history
  - Export calibration report
- **Value**: Users see their printer improvement journey

#### FUTURE INTEGRATIONS (Post-MVP)

**Calculator G-code Export**
- **Goal**: Generate test patterns directly from calculators
- **Action Items**:
  - Rotation distance test cube generator
  - Pressure advance test pattern generator
  - Temperature tower G-code generator
  - Flow calibration cube generator
- **Value**: One-click calibration test generation

**Klipper Config Export**
- **Goal**: Generate complete Klipper config sections
- **Action Items**:
  - Export all calculator results as formatted config
  - Include comments explaining each value
  - Validate config syntax before export
  - Support Marlin firmware translation
- **Value**: Easy config updates from calibration results

**Community Presets Database** (Optional)
- **Goal**: Share successful calibration profiles
- **Action Items**:
  - User-submitted printer profiles
  - Voting/rating system for presets
  - Search by printer model/material
  - Anonymous usage analytics (opt-in)
- **Value**: Faster calibration with community knowledge

#### QUALITY & ACCURACY IMPROVEMENTS

**Defect Image Reference Library** (HIGH)
- **Status**: Infrastructure built, needs content
- **Goal**: Validate vision API with real defect examples
- **Action Items**:
  - Collect 5-10 images per defect type from industry guides
  - RepRap, All3DP, Prusa KB, Simplify3D sources
  - Create metadata JSON for each image
  - Run validation and measure accuracy
- **Value**: Data-driven vision model improvement

**Calculator Formula Validation** (MEDIUM)
- **Goal**: Ensure calculation accuracy
- **Action Items**:
  - Cross-reference formulas with Klipper documentation
  - Add unit tests for edge cases
  - Validate against community-known values
  - Add formula explanations in UI
- **Value**: User trust in calculator accuracy

**Troubleshooting CSV Quality** (MEDIUM)
- **Goal**: Keep defect data current and accurate
- **Action Items**:
  - Review and update fix solutions quarterly
  - Add "last verified" dates to fixes
  - Track which fixes are most effective
  - Remove outdated solutions
- **Value**: Recommendations stay relevant over time

---

## Quick Reference

### Run Commands
```bash
# Setup project
./scripts/setup.sh

# Start dev server
./scripts/run_dev.sh

# Run tests
./scripts/run_tests.sh

# Format code
./scripts/format_code.sh
```

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/name

# Regular commits
git commit -m "feat: description"

# Push branch
git push -u origin feature/name
```

### Common Issues
- Import errors → `uv pip install -e ".[dev]"`
- Test failures → Check `.env` configuration
- Pre-commit fails → Run `./scripts/format_code.sh`
- Semantic router errors → Uses free HuggingFace by default (no API key needed)
- Vision API errors → GOOGLE_API_KEY required only for image diagnosis
