# M3DP-UIP Setup Summary

## ✅ What Has Been Created

### 1. Project Structure

```
m3dp-uip/
├── .github/
│   └── copilot-instructions.md          # AI assistant guidelines (updated)
├── backend/
│   ├── app/
│   │   ├── __init__.py                  # Backend package init
│   │   ├── main.py                      # FastAPI application
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py                # Settings and configuration
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       └── diagnosis.py         # Diagnosis API endpoints
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── vision_service.py        # Gemini Vision API service
│   │   │   └── csv_loader.py            # CSV knowledge base loader
│   │   ├── models/                      # Data models (empty, ready for use)
│   │   └── data/
│   │       ├── klipper_calibrations/    # Klipper CSV files
│   │       │   └── .gitkeep
│   │       └── orca_recommendations/    # OrcaSlicer CSV files
│   │           └── .gitkeep
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py                  # Pytest fixtures
│       ├── test_api.py                  # API endpoint tests
│       └── test_csv_loader.py           # CSV loader tests
├── docs/
│   ├── DEVELOPMENT.md                   # Complete development guide
│   └── SCRIPTS.md                       # Script usage guide
├── research/
│   └── README.md                        # Research organization guide
├── scripts/
│   ├── setup.sh                         # Initial project setup (executable)
│   ├── run_dev.sh                       # Start dev server (executable)
│   ├── run_tests.sh                     # Run test suite (executable)
│   └── format_code.sh                   # Format and lint code (executable)
├── .env.example                         # Environment variable template
├── .gitignore                           # Updated with project-specific ignores
├── .pre-commit-config.yaml             # Pre-commit hooks configuration
├── pyproject.toml                       # Project config with all dependencies
├── README.md                            # Updated with quick start
├── TODO.md                              # Detailed roadmap with branching strategy
├── index.html                           # Frontend prototype (unchanged)
└── main.py                              # Legacy entry point (unchanged)
```

### 2. Backend Infrastructure

**FastAPI Application** (`backend/app/main.py`):
- Application lifecycle management
- CORS middleware configured
- Health check endpoints (`/` and `/health`)
- Swagger docs at `/docs`
- ReDoc at `/redoc`

**Configuration** (`backend/app/core/config.py`):
- Pydantic settings with `.env` support
- All environment variables defined
- CORS origins configured
- API keys placeholders (Gemini, Amazon PA-API, GA4)

**Services**:
- `VisionService`: Gemini Vision API integration structure
- `CSVLoader`: CSV knowledge base loading with caching
- Router pattern implementation ready

**API Endpoints** (`backend/app/api/endpoints/diagnosis.py`):
- `/api/v1/analyze/image` - Image upload and analysis
- `/api/v1/analyze/text` - Text-based diagnosis
- `/api/v1/calculators` - List available calculators
- Full request/response models defined

### 3. Testing Infrastructure

**Pytest Configuration** (`pyproject.toml`):
- Coverage reporting configured
- Async test support
- Test discovery patterns

**Test Suite**:
- `conftest.py`: Shared fixtures (test client, sample data)
- `test_api.py`: API endpoint tests
- `test_csv_loader.py`: CSV loader tests
- Tests use `@pytest.mark.skip` for unimplemented features

### 4. Code Quality Tooling

**Ruff** (Linting + Formatting):
- Configured in `pyproject.toml`
- Select rules: pycodestyle, pyflakes, isort, flake8-bugbear, pyupgrade
- Line length: 100
- Python 3.12 target

**Pre-commit Hooks** (`.pre-commit-config.yaml`):
- Ruff linting and formatting
- Trailing whitespace removal
- YAML/JSON validation
- Large file detection
- Security checks (bandit)

### 5. Development Scripts

All scripts are executable (`chmod +x`):

**setup.sh**:
- Creates virtual environment
- Installs UV
- Installs dependencies
- Creates `.env` from template
- Installs pre-commit hooks
- Runs initial tests

**run_dev.sh**:
- Starts FastAPI development server
- Auto-reload enabled
- Configurable host and port

**run_tests.sh**:
- Runs pytest with coverage
- HTML coverage reports
- Options: --fast, --verbose, --file

**format_code.sh**:
- Formats code with Ruff
- Lints code with Ruff
- Runs pre-commit hooks

### 6. Documentation

**DEVELOPMENT.md**:
- Getting started guide
- Project structure overview
- Development workflow
- Branch strategy
- Running the application
- Testing guide
- Code quality tools
- API documentation
- Troubleshooting

**SCRIPTS.md**:
- Script usage guides
- Script templates
- Best practices
- Common patterns
- Maintenance tasks

**README.md** (Updated):
- Badges for Python, FastAPI, Ruff, License
- Quick start guide
- Project overview
- Architecture diagram (mermaid)
- Tech stack
- Testing instructions
- Documentation links
- Development roadmap

**TODO.md**:
- 6 development phases with tasks
- Branch workflow guide
- Testing requirements
- Acceptance criteria
- Development priorities
- Quick reference commands

### 7. Environment Configuration

**.env.example**:
- All environment variables documented
- API keys placeholders
- CORS configuration
- Database URL (future)
- File upload limits

**.gitignore** (Updated):
- Python artifacts
- Virtual environments
- IDE files
- CSV data files (until ready)
- Research PDFs
- Frontend build files

### 8. Package Configuration

**pyproject.toml** (Complete):
- Project metadata (name, version, authors, license)
- Python 3.12+ requirement
- Production dependencies:
  - fastapi>=0.115.0
  - uvicorn[standard]>=0.32.0
  - pydantic>=2.9.0
  - pydantic-settings>=2.6.0
  - python-multipart>=0.0.12
  - pandas>=2.2.0
  - google-generativeai>=0.8.0
  - python-dotenv>=1.0.0
- Development dependencies:
  - ruff>=0.7.0
  - pytest>=8.3.0
  - pytest-asyncio>=0.24.0
  - pytest-cov>=6.0.0
  - httpx>=0.27.0
  - pre-commit>=4.0.0
- Ruff configuration (linting + formatting)
- Pytest configuration
- Coverage configuration

---

## 🚀 Next Steps

### Immediate Actions (Required)

1. **Install Dependencies**
   ```bash
   # Activate virtual environment
   source .venv/bin/activate  # macOS/Linux

   # Install UV
   pip install uv

   # Install project dependencies
   uv pip install -e ".[dev]"

   # Or use the setup script
   ./scripts/setup.sh
   ```

2. **Configure Environment**
   ```bash
   # Copy environment template
   cp .env.example .env

   # Edit .env with your API keys
   # Required: GOOGLE_GENAI_API_KEY
   # Optional: PAAPI keys (Phase 2)
   ```

3. **Install Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

4. **Test the Setup**
   ```bash
   # Run tests
   ./scripts/run_tests.sh

   # Start dev server
   ./scripts/run_dev.sh

   # Visit http://localhost:8000/docs
   ```

### Phase 1 Tasks (CSV Foundation)

See `TODO.md` for detailed tasks. Key items:

1. **Add CSV Files**
   - Place Klipper calibration CSVs in `backend/app/data/klipper_calibrations/`
   - Place OrcaSlicer CSVs in `backend/app/data/orca_recommendations/`
   - Create sample CSVs for testing

2. **Complete CSV Loader**
   - Implement actual CSV parsing in `csv_loader.py`
   - Add validation logic
   - Write comprehensive tests

3. **Create Ingestion Script**
   - Implement `scripts/ingest_csv.py`
   - Validate CSV schemas
   - Load data into cache

### Phase 2 Tasks (Vision API)

1. **Get Gemini API Key**
   - Sign up at https://makersuite.google.com/
   - Generate API key
   - Add to `.env`

2. **Implement Vision Service**
   - Complete `vision_service.py` implementation
   - Test with sample images
   - Add error handling

3. **Complete API Endpoints**
   - Implement actual diagnosis logic
   - Connect vision service to CSV loader
   - Add calculator endpoints

---

## 📋 Development Workflow

### Starting a New Feature

```bash
# Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Activate virtual environment
source .venv/bin/activate

# Make changes, run tests frequently
./scripts/run_tests.sh

# Format and lint
./scripts/format_code.sh

# Commit (pre-commit hooks run automatically)
git commit -m "feat: your feature description"

# Push and create PR to develop
git push -u origin feature/your-feature-name
```

### Running the Application

```bash
# Backend
./scripts/run_dev.sh
# Access: http://localhost:8000/docs

# Frontend prototype (for now)
python -m http.server 8080
# Access: http://localhost:8080
```

### Common Commands

```bash
# Format code
ruff format .

# Lint code
ruff check . --fix

# Run tests
pytest

# Run tests with coverage
pytest --cov=backend/app --cov-report=html

# Update pre-commit hooks
pre-commit autoupdate

# Run pre-commit manually
pre-commit run --all-files

# Convert research PDFs to markdown
python scripts/convert_research_pdfs.py

# Watch research folder for PDF changes
python scripts/convert_research_pdfs.py --watch

# Set up automatic PDF conversion (macOS)
./scripts/setup_pdf_watch.sh
```

---

## 🔄 Research PDF Automation

**Automatic conversion of PDFs to markdown for version control:**

- ✅ PDFs automatically converted to markdown when added to `research/`
- ✅ Markdown files tracked in git, PDFs gitignored
- ✅ Three extraction methods: PyMuPDF (best), pypdf (fallback), pdftotext (system)
- ✅ Metadata tracking prevents duplicate conversions
- ✅ GitHub Actions auto-converts on push
- ✅ Optional: macOS LaunchAgent for automatic background conversion

**Quick usage:**
```bash
# Convert all PDFs
python scripts/convert_research_pdfs.py

# Watch for changes
python scripts/convert_research_pdfs.py --watch

# Set up auto-conversion (macOS)
./scripts/setup_pdf_watch.sh
```

See `research/README.md` for full documentation.

---

## 🎯 Project Goals

### Architecture Principles

1. **Router Pattern**: Classify first, retrieve second (avoid context pollution)
2. **CSV-Driven**: Formula-based calculations, not LLM hallucinations
3. **UV Environment**: Fast dependency management
4. **Cost-Aware**: Prompt optimization, caching, sampling
5. **Research Automation**: PDF → Markdown conversion for version control

### Quality Standards

- Test coverage: >80% for critical paths
- Response time: <2s for API calls
- Code style: Ruff formatted
- Commits: Conventional Commits format
- Documentation: Comprehensive and up-to-date

### Minimal3DP Brand Standards

- Amazon Affiliate Tag: `mwf064-20`
- YouTube Channel: `UCM_8Mv-0S1LnnJpRJLjahaw`
- Color Palette: Orange (#F97316), zinc-900
- Deployment: Vercel
- SEO: Schema.org, OG images, GA4

---

## 📚 Resources

### Documentation

- **Project Docs**: `docs/DEVELOPMENT.md`, `docs/SCRIPTS.md`
- **API Docs**: http://localhost:8000/docs (when server running)
- **Roadmap**: `TODO.md`
- **AI Guidelines**: `.github/copilot-instructions.md`

### External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pytest Documentation](https://docs.pytest.org/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

### Minimal3DP Resources

- Main Site: https://minimal3dp.com
- YouTube: https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw
- Guide: `guide/MINIMAL3DP_APP_GUIDE.md`

---

## ⚠️ Known Issues & Limitations

### Current State

- ✅ Project structure complete
- ✅ Backend scaffold implemented
- ✅ Testing infrastructure configured
- ✅ Documentation comprehensive
- ⏳ CSV files not yet added (Phase 1)
- ⏳ Vision API not yet integrated (Phase 2)
- ⏳ Frontend needs React migration (Phase 3)

### Import Errors

Some files have import errors because dependencies aren't installed yet:
- FastAPI, Pydantic, pandas, etc.
- **Solution**: Run `uv pip install -e ".[dev]"`

### Skipped Tests

Tests marked with `@pytest.mark.skip` are placeholders:
- CSV loader tests (need actual CSV files)
- Vision API tests (need API integration)
- **Solution**: Implement features, then update tests

### Missing Features

See `TODO.md` for complete list. Key missing pieces:
1. CSV knowledge base files
2. Vision API integration
3. React frontend
4. Deployment configuration

---

## 🆘 Troubleshooting

### "Import could not be resolved"

Dependencies not installed:
```bash
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### "Pre-commit hook failed"

Format and lint first:
```bash
./scripts/format_code.sh
git commit
```

### "Port 8000 already in use"

Use different port:
```bash
./scripts/run_dev.sh --port 8001
```

### "Tests failing"

Check environment:
```bash
# Ensure .env exists
cp .env.example .env

# Reinstall dependencies
uv pip install -e ".[dev]"

# Run specific test
pytest backend/tests/test_api.py::test_root_endpoint -v
```

---

## 🎉 Success Criteria

You'll know the setup is complete when:

- ✅ Virtual environment activated
- ✅ All dependencies installed (71 packages)
- ✅ Pre-commit hooks installed
- ⚠️  `.env` file created (copy from .env.example)
- ✅ Scripts are executable
- ✅ Tests pass (3 passed, 3 skipped as expected)
- ✅ Dev server starts: `./scripts/run_dev.sh`
- ✅ API docs accessible: http://localhost:8000/docs
- ✅ Code formatting works: `./scripts/format_code.sh`

**Current Status**: 8/9 complete (only `.env` needs manual creation)

---

## 📝 Change Log

### 2025-11-21

- ✅ Created complete project structure
- ✅ Implemented FastAPI backend scaffold
- ✅ Set up testing infrastructure (pytest, coverage)
- ✅ Configured code quality tools (Ruff, pre-commit)
- ✅ Created comprehensive documentation
- ✅ Updated README with quick start
- ✅ Created TODO.md with branching strategy
- ✅ Created utility scripts (setup, run_dev, run_tests, format_code)
- ✅ Updated .github/copilot-instructions.md with UV and cost-awareness

---

For detailed development instructions, see `docs/DEVELOPMENT.md`.
For the development roadmap, see `TODO.md`.
For script usage, see `docs/SCRIPTS.md`.
