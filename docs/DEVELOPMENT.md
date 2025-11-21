# M3DP-UIP Development Guide

Complete guide for setting up and developing the Minimal 3DP Unified Intelligence Platform.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Development Workflow](#development-workflow)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Code Quality](#code-quality)
7. [API Documentation](#api-documentation)

## Getting Started

### Prerequisites

- Python 3.12+
- UV (Python package manager)
- Git
- VS Code (recommended) or your preferred editor

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/minimal3dp/m3dp-uip.git
   cd m3dp-uip
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate  # Windows
   ```

3. **Install UV (if not already installed)**
   ```bash
   pip install uv
   ```

4. **Install dependencies**
   ```bash
   # Production dependencies
   uv pip install -e .

   # Development dependencies
   uv pip install -e ".[dev]"
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

6. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Project Structure

```
m3dp-uip/
├── .github/                    # GitHub configuration
│   └── copilot-instructions.md # AI coding assistant instructions
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   │   └── endpoints/
│   │   │       └── diagnosis.py
│   │   ├── core/              # Core configuration
│   │   │   └── config.py
│   │   ├── data/              # CSV knowledge base
│   │   │   ├── klipper_calibrations/
│   │   │   └── orca_recommendations/
│   │   ├── models/            # Data models
│   │   ├── services/          # Business logic
│   │   │   ├── csv_loader.py
│   │   │   └── vision_service.py
│   │   └── main.py            # FastAPI app entry point
│   └── tests/                 # Test suite
├── docs/                      # Documentation
├── research/                  # Research articles and references
├── scripts/                   # Utility scripts
├── index.html                 # Frontend prototype
├── main.py                    # Legacy entry point
├── pyproject.toml            # Project configuration
└── README.md                 # Project overview
```

## Development Workflow

### Branch Strategy

We use a feature-branch workflow:

- `main` - Production-ready code, always working
- `develop` - Integration branch for features
- `feature/*` - New features (e.g., `feature/vision-api`)
- `fix/*` - Bug fixes (e.g., `fix/csv-loader-crash`)
- `docs/*` - Documentation updates

### Creating a New Feature

1. **Create feature branch from develop**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

3. **Run quality checks**
   ```bash
   # Format code
   ruff format .

   # Lint code
   ruff check . --fix

   # Run tests
   pytest
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

5. **Create pull request to develop**

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:
```bash
feat: add vision API integration
fix: resolve CSV loader memory leak
docs: update API endpoint documentation
test: add tests for rotation distance calculator
```

## Running the Application

### Backend (FastAPI)

**Development mode (with auto-reload):**
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Using UV:**
```bash
uv run uvicorn backend.app.main:app --reload
```

**Production mode:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Access the API:
- API: http://localhost:8000
- Swagger docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Frontend Prototype

Open `index.html` in your browser or use a local server:

```bash
# Python simple HTTP server
python -m http.server 8080

# Or use VS Code Live Server extension
# Right-click index.html → Open with Live Server
```

Access: http://localhost:8080

## Testing

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest backend/tests/test_api.py
```

### Run with Coverage

```bash
pytest --cov=backend/app --cov-report=html
```

View coverage report: `open htmlcov/index.html`

### Run Specific Test

```bash
pytest backend/tests/test_api.py::test_root_endpoint
```

### Watch Mode (run tests on file changes)

```bash
pytest-watch
```

## Code Quality

### Linting with Ruff

**Check for issues:**
```bash
ruff check .
```

**Auto-fix issues:**
```bash
ruff check . --fix
```

**Check specific file:**
```bash
ruff check backend/app/main.py
```

### Formatting with Ruff

**Check formatting:**
```bash
ruff format . --check
```

**Format code:**
```bash
ruff format .
```

### Pre-commit Hooks

Pre-commit hooks run automatically on `git commit`:

- Ruff linting and formatting
- Trailing whitespace removal
- YAML/JSON validation
- Large file detection
- Security checks (bandit)

**Run manually:**
```bash
pre-commit run --all-files
```

**Update hooks:**
```bash
pre-commit autoupdate
```

## API Documentation

### Interactive API Docs

Once the server is running, access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

#### Health Check
```bash
curl http://localhost:8000/health
```

#### Analyze Image (planned)
```bash
curl -X POST http://localhost:8000/api/v1/analyze/image \
  -F "file=@print_failure.jpg" \
  -F "printer_model=Bambu Lab X1C" \
  -F "filament_type=PLA"
```

#### Analyze Text Description (planned)
```bash
curl -X POST http://localhost:8000/api/v1/analyze/text \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Print has visible gaps between layers",
    "printer_model": "Prusa MK4",
    "filament_type": "PETG"
  }'
```

## Environment Variables

Key environment variables (see `.env.example`):

- `ENVIRONMENT` - development/production
- `DEBUG` - Enable debug mode
- `GOOGLE_GENAI_API_KEY` - Gemini Vision API key
- `GA4_MEASUREMENT_ID` - Google Analytics ID
- `PAAPI_ACCESS_KEY` - Amazon Product API (Phase 2)

## Troubleshooting

### Import Errors

If you see import errors, ensure dependencies are installed:
```bash
uv pip install -e ".[dev]"
```

### Port Already in Use

If port 8000 is busy:
```bash
uvicorn app.main:app --reload --port 8001
```

### Pre-commit Hook Failures

If pre-commit hooks fail:
```bash
# Fix formatting issues
ruff format .

# Fix linting issues
ruff check . --fix

# Try commit again
git commit
```

### Database Connection Issues

Currently, no database is required. This is for future implementation.

## Next Steps

1. **Add CSV Knowledge Base**
   - Place CSV files in `backend/app/data/klipper_calibrations/`
   - Place CSV files in `backend/app/data/orca_recommendations/`

2. **Implement Vision API**
   - Get Gemini API key
   - Implement `vision_service.py` integration

3. **Build Frontend**
   - Migrate from `index.html` to React/Vite
   - Implement diagnostic wizard

4. **Add More Calculators**
   - Pressure Advance
   - Flow Rate
   - Input Shaping

See `TODO.md` for detailed development roadmap.

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pytest Documentation](https://docs.pytest.org/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [Project README](../README.md)
