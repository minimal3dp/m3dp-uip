# Documentation Index

Complete documentation for M3DP-UIP Klipper Calibration Utility.

## Quick Navigation

### Getting Started
- **[README.md](../README.md)** - Project overview and quick start guide
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Contribution guidelines and workflow

### Technical Documentation

#### Architecture & Design
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design, data flow, technology stack
  - Directory structure
  - Request/response flow
  - Data models and validation
  - Performance considerations
  - Security architecture
  - Deployment architecture

#### API Reference
- **[API.md](./API.md)** - Complete API endpoint documentation
  - Base URLs and authentication
  - Response format and status codes
  - All 10 calculator endpoints with examples
  - Request/response models
  - Error handling
  - Rate limiting
  - Client integration examples

#### Adding New Calculators
- **[CALCULATOR_GUIDE.md](./CALCULATOR_GUIDE.md)** - Step-by-step guide for adding calculators
  - Current implementation status (10/16)
  - Calculator architecture
  - Step-by-step implementation guide
  - CSV data format
  - Pydantic models
  - HTML templates
  - Unit testing
  - Common patterns and troubleshooting

### Development

#### Local Setup
- **[development/SETUP.md](./development/SETUP.md)** - Environment configuration
  - Prerequisites (Python 3.12+, uv)
  - Virtual environment setup
  - Dependency installation
  - Running development server
  - Database setup (none - stateless)

#### Testing
- **[development/TESTING.md](./development/TESTING.md)** - Testing strategy and procedures
  - Unit test structure (42 tests)
  - Integration test examples
  - Coverage requirements
  - Running tests locally
  - Test debugging

#### Debugging
- **[development/DEBUG.md](./development/DEBUG.md)** - Troubleshooting and debugging
  - Common errors and solutions
  - Debug configuration in VS Code
  - Logging setup
  - Performance profiling
  - Database inspection (N/A - stateless)

#### Deployment
- **[deployment/RAILWAY.md](./deployment/RAILWAY.md)** - Railway production deployment
  - Quick start (5 minutes)
  - Docker configuration
  - Environment variables
  - Custom domain setup
  - HTTPS/SSL certificate
  - Monitoring and logging
  - Scaling strategies
  - Troubleshooting
  - Cost optimization

#### Docker
- **[deployment/DOCKER.md](./deployment/DOCKER.md)** - Docker containerization
  - Dockerfile explanation
  - Building images locally
  - Running containers
  - Docker Compose setup

### Project Files

#### Root Configuration
- **[pyproject.toml](../pyproject.toml)** - Project metadata and dependencies
  - Python 3.12 requirement
  - FastAPI, Uvicorn, Pydantic
  - Development tools (pytest, ruff)
  - Build system configuration

#### Environment
- **[.env.example](../.env.example)** - Environment variable template
  - Copy to `.env` for local development
  - Do not commit `.env` to git

#### Git
- **[.pre-commit-config.yaml](../.pre-commit-config.yaml)** - Git hooks
  - Auto-format with ruff
  - Lint checks
  - Type checking (mypy)

### Source Code Structure

```
backend/
├── app/
│   ├── api/endpoints/
│   │   ├── calculators.py    # 2845 lines, all 16 calculator endpoints
│   │   └── root.py           # Health checks
│   ├── templates/
│   │   ├── base.html         # Layout
│   │   ├── index.html        # Home page
│   │   └── calculator_*.html # 10 calculator forms
│   ├── data/
│   │   └── klipper_calibrations/
│   │       └── *.csv         # Calibration data (8 files)
│   ├── models/
│   │   └── csv_schemas.py    # Pydantic models
│   ├── services/
│   │   ├── csv_loader.py     # CSV file loading
│   │   └── ga4_tracker.py    # Analytics
│   ├── core/
│   │   └── config.py         # Configuration
│   └── main.py               # FastAPI app entry point
├── tests/
│   ├── test_calculators.py       # 42 unit tests
│   └── test_calculators_extra.py # 4 integration tests
└── .venv/                    # Virtual environment
```

### Research & Data

```
research/
├── EXTRACTED_FORMULAS.md         # All 16 calculator formulas
├── FDM 3D Printer Calibration Report.md
└── Klipper Calibrations.xlsx     # Source data (converted to CSV)
```

---

## Technology Stack

### Backend
- **Framework:** FastAPI 0.115+
- **Server:** Uvicorn 0.32+
- **Python:** 3.12+
- **Templating:** Jinja2 3.1+
- **Validation:** Pydantic 2.9+
- **Data:** Pandas 2.2+

### Frontend
- **HTML5** + Jinja2 templates
- **CSS:** TailwindCSS v3+ (CDN)
- **JavaScript:** HTMX 1.9.10 + Alpine.js 3.13.5
- **Total JS:** ~29KB

### Deployment
- **Platform:** Railway
- **Container:** Docker (Python 3.12 slim image)
- **SSL:** Let's Encrypt (automatic)

---

## Key Features

✅ **10 Working Calculators** (100% tested)
1. Extruder Rotation Distance
2. OrcaSlicer Flow Calibration (Two-Pass)
3. OrcaSlicer Flow YOLO (Single-Pass)
4. Run Current (TMC2208/2209)
5. Pressure Advance
6. Input Shaping
7. X and Y Offsets
8. Max Volumetric Speed
9. Lead Screw Rotation Distance
10. Line Widths (OrcaSlicer)

⏳ **6 Pending Calculators** (In development)
11. Skew Correction
12. Flow Calibration (Traditional)
13. PA & OrcaSlicer
14. Ellis Max Volumetric Speed
15. Extrusion Rate Smoothing (ERS)
16. Adaptive Pressure Advance

### Design
- **Formula-driven** - All calculations from verified sources
- **Stateless** - No sessions, cookies, or persistent storage
- **Server-side rendering** - HTML templates with Jinja2
- **Type-safe** - Pydantic validation on all inputs
- **CSV-centric** - Calibration data from structured files

### Quality
- **Tests:** 46/46 passing (100% success rate)
- **Coverage:** 43% overall (69% for calculators)
- **Linting:** 0 errors (ruff)
- **Type hints:** 100% on new code
- **CORS:** Pre-configured for production

---

## Common Tasks

### Run Development Server
```bash
cd backend
uvicorn app.main:app --reload
```
Then visit `http://localhost:8000`

### Run Tests
```bash
pytest backend/tests/test_calculators.py -v
```

### Format & Lint Code
```bash
ruff format .
ruff check . --fix
```

### Add New Calculator
Follow [CALCULATOR_GUIDE.md](./CALCULATOR_GUIDE.md) - detailed step-by-step instructions

### Deploy to Production
```bash
git push origin refactor/v2-lean
# Railway automatically deploys within 5 minutes
```

### Check Production Logs
```bash
# In Railway dashboard: Click project → Logs tab
# Or use Railway CLI:
railway logs
```

---

## Status Summary

| Category | Status | Details |
|----------|--------|---------|
| **Core Functionality** | ✅ Complete | 10/16 calculators working |
| **Testing** | ✅ Complete | 46/46 tests passing (100%) |
| **Code Quality** | ✅ Complete | 0 lint errors, formatted |
| **Documentation** | ✅ Complete | 4 main docs + deployment |
| **Development Setup** | ✅ Complete | venv auto-activation, debug configs |
| **Deployment Ready** | ✅ Complete | Docker, Railway, HTTPS configured |
| **Remaining Work** | ⏳ Planned | 6 additional calculators |

---

## Quick Links

### Internal Navigation
- [GitHub Repository](https://github.com/minimal3dp/m3dp-uip)
- [Railway Dashboard](https://railway.app)
- [OpenAPI Docs](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

### External Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Klipper Documentation](https://www.klipper3d.org)
- [OrcaSlicer Wiki](https://github.com/SoftFever/OrcaSlicer/wiki)
- [TailwindCSS Docs](https://tailwindcss.com/docs)

---

## Contributing

1. Read [CONTRIBUTING.md](../CONTRIBUTING.md)
2. Check [CALCULATOR_GUIDE.md](./CALCULATOR_GUIDE.md) for new calculators
3. Follow [SETUP.md](./development/SETUP.md) for development environment
4. Create branch: `feature/your-feature`
5. Make changes, test locally
6. Format with ruff: `ruff format . && ruff check . --fix`
7. Run tests: `pytest backend/tests/test_calculators.py`
8. Push and open Pull Request

---

## Support & Troubleshooting

### Documentation Issues
- Check [development/DEBUG.md](./development/DEBUG.md) for common errors
- Review [API.md](./API.md) for endpoint issues
- See [CALCULATOR_GUIDE.md](./CALCULATOR_GUIDE.md) for implementation help

### Production Issues
- Check [deployment/RAILWAY.md](./deployment/RAILWAY.md) troubleshooting section
- Review logs in Railway dashboard
- Open issue on GitHub

### Questions
1. Search existing documentation
2. Check GitHub issues
3. Open new issue with details

---

## Version Information

- **Project Version:** 0.1.0
- **Python Version:** 3.12.9
- **FastAPI Version:** 0.115+
- **Last Updated:** December 4, 2025
- **Status:** Production-ready (main branch)
- **Development Branch:** refactor/v2-lean

---

## License

Licensed under MIT License - See LICENSE file for details
