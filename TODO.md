# M3DP-UIP Development TODO

Development roadmap organized by feature branches. The `main` branch contains only working, production-ready code. All development happens on feature branches that merge to `develop`, which then merges to `main` after thorough testing.

## 📊 Progress Overview

- ✅ **Phase 0**: Project Setup & Tooling - COMPLETED
- 🔄 **Phase 1**: Data Foundation - IN PROGRESS
- ⏳ **Phase 2**: Backend Core - READY
- ⏳ **Phase 3**: Frontend Development - READY
- ⏳ **Phase 4**: Integration & Testing - READY
- ⏳ **Phase 5**: Deployment & Polish - READY

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

## Phase 1: Data Foundation 🔄

**Branch**: `feature/csv-knowledge-base`
**Status**: IN PROGRESS
**Priority**: HIGH
**Goal**: Implement CSV data loading and validation

### Tasks

#### Data Ingestion
- [ ] Create CSV schema definitions
- [ ] Implement CSV validation logic
- [ ] Write `scripts/ingest_csv.py` for data loading
- [ ] Add sample CSV files for testing
- [ ] Create data migration scripts

#### CSV Loader Service
- [ ] Complete `CSVLoader` implementation
- [ ] Add caching mechanism
- [ ] Implement search functionality
- [ ] Add error handling and logging
- [ ] Write comprehensive tests

#### Documentation
- [ ] Document CSV file format requirements
- [ ] Create guide for adding new CSVs
- [ ] Document data validation rules
- [ ] Add examples of CSV queries

### Testing Requirements

- [ ] Unit tests for CSV loader
- [ ] Integration tests with sample data
- [ ] Validation tests for CSV schemas
- [ ] Performance tests for large CSVs

### Acceptance Criteria

- CSV files load successfully on startup
- Search functionality works accurately
- All tests pass with >80% coverage
- Documentation is complete and clear

### Related Files

- `backend/app/services/csv_loader.py`
- `backend/app/data/klipper_calibrations/`
- `backend/app/data/orca_recommendations/`
- `scripts/ingest_csv.py`
- `backend/tests/test_csv_loader.py`

---

## Phase 2: Backend Core ⏳

**Branch**: `feature/vision-api-integration`
**Status**: READY TO START
**Priority**: HIGH
**Dependencies**: Phase 1 (CSV data must be loaded)
**Goal**: Integrate Gemini Vision API and implement router logic

### Tasks

#### Vision API Integration
- [ ] Set up Google Generative AI client
- [ ] Implement `VisionService` class
- [ ] Create system prompt for diagnostician
- [ ] Add image preprocessing logic
- [ ] Handle API errors and rate limits

#### Router Logic
- [ ] Implement issue classification (Mechanical/Slicer/Material)
- [ ] Create confidence scoring system
- [ ] Map classifications to CSV categories
- [ ] Add fallback logic for low confidence

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
- Additional calculators (Input Shaping, Retraction, etc.)
- Multi-language support
- User accounts and saved configurations
- Print history tracking

### Phase 7: Amazon Integration
**Branch**: `feature/amazon-paapi`
- Amazon PA-API integration
- Product recommendations
- Affiliate link tracking
- Dynamic pricing

### Phase 8: Community Features
**Branch**: `feature/community`
- User-submitted calibrations
- Community voting system
- Discussion forum
- Print profile sharing

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

### Immediate (This Week)
1. ✅ Complete Phase 0 (Setup) - DONE
2. 🔄 Start Phase 1 (CSV Foundation)
3. Add sample CSV files for testing
4. Complete CSV loader implementation

### Short Term (Next 2 Weeks)
1. Complete Phase 1 (CSV Foundation)
2. Start Phase 2 (Vision API)
3. Set up Gemini API integration
4. Implement router logic

### Medium Term (Next Month)
1. Complete Phase 2 (Backend Core)
2. Start Phase 3 (React Frontend)
3. Port prototype to React
4. API integration

### Long Term (Next Quarter)
1. Complete Phase 3 (Frontend)
2. Complete Phase 4 (Integration)
3. Complete Phase 5 (Deployment)
4. Launch MVP to production

---

## Notes & Decisions

### Architecture Decisions
- **Router Pattern**: Avoid context window pollution by classifying first
- **CSV-Driven**: All calculators based on spreadsheet formulas, not LLM generation
- **UV Environment**: All Python development uses UV for faster dependency management
- **Ruff**: Single tool for linting and formatting (replaces Black, isort, flake8)

### Cost Optimization
- Cache CSV data in memory (avoid repeated file reads)
- Batch vision API calls when possible
- Use prompt compression techniques
- Sample data for development/testing (not full CSVs)

### Quality Standards
- Test coverage: >80% for critical paths
- Response time: <2s for API calls
- Mobile-first design
- Accessibility: WCAG 2.1 AA compliance

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
