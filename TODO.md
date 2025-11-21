# M3DP-UIP Development TODO

Development roadmap organized by feature branches. The `main` branch contains only working, production-ready code. All development happens on feature branches that merge to `develop`, which then merges to `main` after thorough testing.

## 📊 Progress Overview

- ✅ **Phase 0**: Project Setup & Tooling - COMPLETED
- ✅ **Phase 1**: CSV Knowledge Base Foundation - COMPLETED
- ⏳ **Phase 2**: Backend Core (Vision API & Router) - READY
- ⏳ **Phase 3**: Frontend Development - READY
- ⏳ **Phase 4**: Integration & Testing - READY
- ⏳ **Phase 5**: Deployment & Polish - READY

## 🎯 Key Research Insights

**Based on**: "The Cyber-Physical Convergence" research document (Nov 2025)

### Validated Architecture Decisions
- ✅ **Router Pattern**: Research confirms classification-first approach avoids context pollution
- ✅ **CSV-Driven Formulas**: Industry standard is deterministic calculations, not LLM generation
- ✅ **Klipper Focus**: Minimal 3DP ecosystem cited as authoritative reference for calibration

### New Opportunities Identified
- 🔬 **Semantic Router**: Implement query classification before LLM calls (aurelio-labs/semantic-router)
- 🔬 **Edge AI Monitoring**: Consider PrintGuard integration for defect detection (>15 FPS on Pi Zero 2)
- 🔬 **Slice-100K Dataset**: Future opportunity for G-code analysis and translation
- 🔬 **ShapeLLM**: 3D-aware AI for future advanced features

### Integration Targets
- **Obico/PrintGuard**: Visual defect detection post-MVP
- **Semantic Router**: Efficient query classification in RAG pipeline
- **Klipper-Backup**: Configuration version control integration

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

## Phase 2: Backend Core ⏳

**Branch**: `feature/vision-api-integration`
**Status**: READY TO START
**Priority**: HIGH
**Dependencies**: ✅ Phase 1 (CSV data loaded and validated)
**Goal**: Integrate Gemini Vision API and implement router logic

### Research-Backed Enhancements

**From "Cyber-Physical Convergence" research:**
- 📚 **System Prompt**: Use research Section 1 for diagnostician persona definition
- 📚 **Semantic Router**: Implement `aurelio-labs/semantic-router` for query classification (Section 6.3)
  - Classification BEFORE LLM call reduces token costs
  - Pre-defined routes: Calibration, Troubleshooting, Material, Quality
  - Python implementation example provided in research Appendix A.2
- 📚 **Defect Taxonomy**: Research Section 5 provides 8-class defect classification
  - Spaghetti, Layer Shift, Warping, Ringing, Under/Over Extrusion, Poor Bridging, Layer Separation

### Tasks

#### Vision API Integration
- [ ] Set up Google Generative AI client (Gemini 1.5 Pro)
- [ ] Implement `VisionService.analyze_image()` method
- [ ] Create system prompt for 3D printing diagnostician (use research Section 1 philosophy)
- [ ] Add image preprocessing logic (resize, format conversion)
- [ ] Handle API errors and rate limits (retry logic, exponential backoff)
- [ ] Add support for dark/shiny filament edge cases (research Section 5.3)

#### Semantic Router Implementation (NEW)
- [ ] Install `semantic-router` library (`uv pip install semantic-router`)
- [ ] Define routes for Calibration, Troubleshooting, Material, Quality
- [ ] Create route utterances based on CSV categories
- [ ] Integrate router BEFORE vision API call for text queries
- [ ] Add route confidence scoring
- [ ] Implement fallback to vision API for low-confidence routes

#### Router Logic
- [ ] Implement issue classification (Mechanical/Slicer/Material/Multi-factor)
- [ ] Create confidence scoring system (0.0-1.0 with thresholds)
- [ ] Map classifications to CSV categories:
  - Mechanical → klipper_calibrations/
  - Slicer → orca_recommendations/quality_settings.csv
  - Material → orca_recommendations/material_profiles.csv
- [ ] Add fallback logic for low confidence (<0.6)
- [ ] Handle multi-factor issues (e.g., "Warping" = Material + Mechanical)

#### API Endpoints
- [ ] Complete `/api/v1/analyze/image` endpoint
- [ ] Complete `/api/v1/analyze/text` endpoint
- [ ] Add `/api/v1/calculators` endpoint
- [ ] Implement calculator-specific endpoints

#### Calculator Logic
- [ ] Port rotation distance formula from CSV
- [ ] Port pressure advance formula
- [ ] Port flow rate formula
- [ ] Add input validation
- [ ] Generate Klipper config output

### Testing Requirements

- [ ] Mock vision API for tests
- [ ] Test router classification accuracy
- [ ] Test calculator formulas against CSV
- [ ] Test error handling
- [ ] Integration tests for full flow

### Acceptance Criteria

- Vision API integration works with real images
- Router correctly classifies issue types >85% accuracy
- Calculators produce correct outputs
- API endpoints return proper JSON responses
- All tests pass with >80% coverage

### Related Files

- `backend/app/services/vision_service.py`
- `backend/app/api/endpoints/diagnosis.py`
- `backend/app/api/endpoints/calculators.py` (new)
- `backend/tests/test_vision_service.py` (new)
- `backend/tests/test_diagnosis.py` (new)

---

## Phase 3: Frontend Development ⏳

**Branch**: `feature/react-frontend`
**Status**: READY TO START
**Priority**: MEDIUM
**Dependencies**: Phase 2 (API must be functional)
**Goal**: Migrate from HTML prototype to React + Vite application

### Tasks

#### Project Setup
- [ ] Initialize Vite + React project
- [ ] Configure Tailwind CSS
- [ ] Set up TypeScript
- [ ] Configure ESLint and Prettier
- [ ] Set up React Router

#### Components
- [ ] Create `DiagnosticWizard` component
- [ ] Create `ImageUpload` component
- [ ] Create `AnalysisResults` component
- [ ] Create calculator components:
  - [ ] `RotationDistanceCalculator`
  - [ ] `PressureAdvanceCalculator`
  - [ ] `FlowRateCalculator`
- [ ] Create `ConfigOutput` component

#### State Management
- [ ] Set up React Context or Zustand
- [ ] Implement upload state
- [ ] Implement analysis results state
- [ ] Implement calculator state

#### API Integration
- [ ] Create API client with axios/fetch
- [ ] Implement image upload
- [ ] Implement text analysis
- [ ] Handle loading states
- [ ] Handle error states

#### UI/UX
- [ ] Port glass morphism styles
- [ ] Implement responsive design
- [ ] Add loading animations
- [ ] Add error messages
- [ ] Add success feedback

### Testing Requirements

- [ ] Component tests with React Testing Library
- [ ] Integration tests with Mock Service Worker
- [ ] E2E tests with Playwright
- [ ] Accessibility tests

### Acceptance Criteria

- All prototype functionality ported to React
- Responsive design works on mobile/tablet/desktop
- API integration works correctly
- All UI states handled properly
- Tests pass with >70% coverage

### Related Files

- `frontend/` (new directory)
- `frontend/src/components/`
- `frontend/src/hooks/`
- `frontend/src/services/`
- `index.html` (archive after migration)

---

## Phase 4: Integration & Testing ⏳

**Branch**: `feature/integration-testing`
**Status**: READY TO START
**Priority**: MEDIUM
**Dependencies**: Phases 2 & 3
**Goal**: End-to-end testing and integration validation

### Tasks

#### Integration Tests
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

- All integration points work correctly
- Performance meets targets (<2s response time)
- Error handling is comprehensive
- Documentation is complete

### Related Files

- `backend/tests/integration/` (new)
- `frontend/tests/e2e/` (new)
- `docs/USER_GUIDE.md` (new)
- `docs/TROUBLESHOOTING.md` (new)

---

## Phase 5: Deployment & Polish ⏳

**Branch**: `feature/deployment`
**Status**: READY TO START
**Priority**: LOW
**Dependencies**: Phases 2, 3, 4
**Goal**: Deploy to Vercel and polish for production

### Tasks

#### Deployment Setup
- [ ] Configure Vercel project
- [ ] Set up environment variables
- [ ] Configure custom domain
- [ ] Set up SSL/HTTPS
- [ ] Configure CI/CD pipeline

#### Monitoring & Analytics
- [ ] Set up Google Analytics 4
- [ ] Add error tracking (Sentry)
- [ ] Add performance monitoring
- [ ] Create monitoring dashboard

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

### Acceptance Criteria

- Application deployed to production
- All monitoring in place
- SEO optimized
- Branding consistent with minimal3dp.com

### Related Files

- `vercel.json` (new)
- `frontend/public/` (assets)
- `.github/workflows/` (CI/CD)

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

### Phase 7: AI Monitoring Integration (NEW)
**Branch**: `feature/ai-monitoring`
**Research Source**: Section 5 (Visual AI: Defect Detection and Process Control)
**Priority**: HIGH (Post-MVP safety feature)

- [ ] **PrintGuard Integration** (recommended by research)
  - ShuffleNetv2 architecture optimized for edge devices
  - >15 FPS on Raspberry Pi Zero 2 (40x faster than Obico)
  - Real-time spaghetti detection
  - Integration with diagnostic workflow
  - GitHub: Research cites open-source availability
- [ ] **Obico Integration** (alternative/complementary)
  - 7M+ hours training data
  - Self-hosted or SaaS deployment options
  - Cloud-based monitoring for remote users
- [ ] Edge AI deployment guide for users
- [ ] Defect detection result integration with router logic
- [ ] Dark/shiny filament handling (research-cited edge case)
- [ ] First-layer validation (LiDAR concept from Bambu research)

### Phase 8: Semantic RAG Optimization (NEW)
**Branch**: `feature/semantic-rag`
**Research Source**: Section 6.3 (Semantic Routing and RAG)
**Priority**: MEDIUM (Cost optimization)

- [ ] Implement `semantic-router` library (aurelio-labs)
- [ ] Define route utterances for:
  - Calibration queries
  - Troubleshooting queries
  - Material selection
  - Quality settings
  - General chat
- [ ] Vector embeddings for route classification
- [ ] Route confidence thresholds
- [ ] Fallback to full LLM for edge cases
- [ ] Performance benchmarking (latency reduction)
- [ ] Token cost tracking and optimization

### Phase 9: Amazon Integration
**Branch**: `feature/amazon-paapi`
- Amazon PA-API integration
- Product recommendations based on diagnostics:
  - Warping detected → build surface products
  - Under-extrusion → hotend upgrade suggestions
  - Ringing → belt/frame stiffness products
- Affiliate link tracking (mwf064-20)
- Dynamic pricing

### Phase 10: Community Features
**Branch**: `feature/community`
- User-submitted calibrations
- Community voting system
- Discussion forum
- Print profile sharing
- **Configuration Repository** (integrate Klipper-Backup - Research Section 7.1)
- Crowdsourced defect training data

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
2. ✅ Phase 1 (CSV Foundation) - 6 CSVs, schema validation, loader service, 12 tests passing
   - Commits: bd9148b (implementation), faa19ed (data files)
   - Test coverage: 73% overall (86% csv_loader, 85% csv_schemas)
   - All CSVs validated against schemas

### Immediate (This Week)
1. 🎯 **Merge Phase 1 to develop/main** - Feature branch ready
2. 🎯 **Phase 2 Planning** - Review research insights for vision API architecture
3. 🎯 **Semantic Router Research** - Evaluate `aurelio-labs/semantic-router` implementation
4. Research validation: Cross-reference CSV formulas with Klipper documentation

### Short Term (Next 2 Weeks)
1. Start Phase 2 (Vision API Integration)
2. Implement Semantic Router for query classification (research-backed)
3. Set up Gemini API client with system prompt from research
4. Implement router logic with confidence scoring
5. Add defect taxonomy (8 classes from research Section 5)

### Medium Term (Next Month)
1. Complete Phase 2 (Backend Core)
2. Start Phase 3 (React Frontend)
3. Port prototype to React + Vite
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

**Primary Research Document**: "The Cyber-Physical Convergence: Deterministic Firmware, Algorithmic Slicing, and the Rise of Multimodal AI in Additive Manufacturing" (Nov 2025)

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
- **Slice-100K Dataset**: https://arxiv.org/abs/2407.04180 (3D printing multimodal dataset)
- **ShapeLLM**: https://arxiv.org/abs/2506.01853 (3D-native LLM)
- **Scene-LLM**: https://arxiv.org/abs/2403.11401 (3D spatial understanding)
- 🔬 **Future**: Phase 11 (12-18 months post-MVP)

#### Configuration Management (Section 7.1)
- **Klipper-Backup**: https://github.com/Staubgeborener/Klipper-Backup
- 🎯 **Planned**: Phase 6 (Git-based printer.cfg version control)

### YouTube References
- **OrcaSlicer 2.3.1**: https://www.minimal3dp.com/blog/2025/08/24/orcaslicer-2.3.1-alpha-just-dropped-how-to-use-the-new-flow-rate-calibration/
- **Line Width Video**: https://www.youtube.com/watch?v=vchXVtCReSo (Dimensional Accuracy)
- **Orca Settings**: https://www.youtube.com/watch?v=n0jb12SLRrU (Stronger Prints)
- **Optimize Prints**: https://www.youtube.com/watch?v=JiBZfjWyBxs (Complete Guide)

### Integration Checklist
- [x] Phase 1: Klipper rotation distance formulas (Section 2)
- [x] Phase 1: Pressure advance parameters (Section 3.2)
- [x] Phase 1: Material profiles (Section 4)
- [ ] Phase 2: System prompt design (Section 1 philosophy)
- [ ] Phase 2: Semantic router (Section 6.3 with Appendix A.2 code)
- [ ] Phase 2: 8-class defect taxonomy (Section 5)
- [ ] Phase 7: PrintGuard edge AI (Section 5.2)
- [ ] Phase 11: Slice-100K dataset (Section 6.1)

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
- Research references → See research/Project Report Resource Generation Guide.md
