# M3DP-UIP - Klipper Calibration Utility

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](#license)

**Stateless web application providing 16 formula-driven calculators for Klipper 3D printer calibration.**

Built for speed, accuracy, and zero AI dependencies. Part of the [minimal3dp.com](https://minimal3dp.com) ecosystem (10K+ YouTube subscribers).

---

## 🎯 Overview

M3DP-UIP is a **lean, server-side rendered web application** that transforms complex Klipper calibration formulas into simple, interactive calculators.

**Core Philosophy:**
- ✅ Formula-driven calculations (no AI, no guessing)
- ✅ Server-side rendering (Jinja2 templates)
- ✅ Minimal JavaScript footprint (HTMX + Alpine.js = ~29KB)
- ✅ Stateless architecture (no sessions, no cookies)
- ✅ Railway deployment ready (Docker)

**Design System:**
- Background: `slate-900` (#0f172a)
- Accent: `amber-500` (#f59e0b)
- Typography: System font stack
- From: `m3dp-design-system`

---

## 🧮 Calculators

### Implemented (10/16)

1. **Extruder Rotation Distance** - E-steps and rotation distance
2. **OrcaSlicer Flow Calibration** - Two-pass flow tuning
3. **OrcaSlicer Flow YOLO** - Single-pass flow method
4. **Run Current (TMC2208/2209)** - Stepper motor current
5. **Pressure Advance** - Direct drive & Bowden PA values
6. **Input Shaping** - Resonance compensation frequencies
7. **X and Y Offsets** - Probe offset calculations
8. **Max Volumetric Speed** - Safe flow rate limits
9. **Lead Screw Rotation Distance** - Z-axis rotation values
10. **Line Widths (OrcaSlicer)** - Nozzle diameter-based widths

### Remaining (6/16)

11. **Skew Correction** - XY/XZ/YZ skew commands (partial)
12. **Flow Calibration (Traditional)** - Wall thickness method
13. **PA & OrcaSlicer** - Alternative pressure advance
14. **Ellis Max Volumetric Speed** - Manual extrusion method
15. **Extrusion Rate Smoothing (ERS)** - Advanced OrcaSlicer feature
16. **Adaptive Pressure Advance** - Matrix-based PA tuning

**Source:** All formulas extracted from `research/EXTRACTED_FORMULAS.md` (derived from `Klipper Calibrations.xlsx`)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+ (3.12 recommended)
- uv (recommended) or pip

### Installation

```bash
# Clone repository
git clone <repo_url>
cd m3dp-uip

# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .

# Install Jinja2 (required for templates)
uv pip install jinja2
```

### Run Development Server

```bash
cd backend
uvicorn app.main:app --reload
```

**Server URL:** `http://localhost:8000`

### Key Endpoints

- `/` - Home page
- `/home` - Main dashboard
- `/calculators-ui` - Calculator index
- `/api/v1/calculators` - Calculator list (JSON)
- `/docs` - OpenAPI documentation

**Individual Calculators:**
- `/rotation-distance` - Extruder rotation distance
- `/flow-calibration` - OrcaSlicer flow (two-pass)
- `/flow-yolo` - OrcaSlicer flow (single-pass)
- `/run-current` - TMC2208/2209 stepper current
- `/pressure-advance` - Pressure advance values
- `/input-shaping` - Input shaping frequencies
- `/xy-offsets` - Probe offset calculations
- `/max-volumetric-speed` - Flow rate limits
- `/lead-screw` - Z-axis rotation distance
- `/line-widths` - OrcaSlicer line width recommendations

---

## 📁 Project Structure

```
m3dp-uip/
├── backend/
│   ├── app/
│   │   ├── api/endpoints/
│   │   │   └── calculators.py       # Calculator API endpoints
│   │   ├── templates/               # Jinja2 templates
│   │   │   ├── base.html           # Base template
│   │   │   ├── home.html           # Dashboard
│   │   │   └── calculators/        # Calculator templates
│   │   ├── static/                  # CSS/JS assets
│   │   ├── data/                    # Calculator CSV files
│   │   │   └── klipper_calibrations/
│   │   └── main.py                  # FastAPI application
│   └── tests/                       # Backend tests
├── research/
│   ├── EXTRACTED_FORMULAS.md        # 16 calculator formulas
│   ├── FDM 3D Printer Calibration and Slicer Report.md
│   └── Klipper Calibrations.xlsx    # Source spreadsheet
├── docs/
│   ├── development/                 # Setup guides
│   ├── deployment/                  # Railway deployment
│   └── archived/                    # Historical docs (Vision AI)
├── strategy/                        # Business planning
├── README.md                        # This file
├── TODO.md                          # Current tasks
├── CONTRIBUTING.md                  # Development guide
└── pyproject.toml                   # Dependencies
```

---

## 🛠️ Tech Stack

### Backend

- **Python 3.11+** - Core language
- **FastAPI 0.115+** - Web framework
- **Jinja2 3.1+** - Server-side templates
- **Pandas 2.2+** - CSV data processing
- **Pydantic 2.9+** - Type safety and validation
- **Uvicorn** - ASGI server

### Frontend

- **HTML5** - Semantic markup
- **Jinja2** - Server-side rendering
- **HTMX 1.9.10** (~14KB) - AJAX without JavaScript
- **Alpine.js 3.13.5** (~15KB) - Lightweight reactivity
- **TailwindCSS v3+** (CDN) - Utility-first CSS

**Total JS footprint: ~29KB** (vs. ~2MB for Vue/React)

### Deployment

- **Railway** - Primary deployment target
- **Docker** - Containerization
- **Smart Links** - `/go/{product_id}` redirects

### Development

- **Pytest** - Testing framework
- **Ruff** - Linting and formatting (recommended)
- **Type hints** - Required for all functions

---

## 📖 Formula Sources

All calculators are formula-driven, not AI-generated:

1. **Primary Source:** `research/EXTRACTED_FORMULAS.md`
   - 16 calculator specifications
   - Input requirements
   - Output formats
   - Implementation priority

2. **Original Data:** `research/Klipper Calibrations.xlsx`
   - Source spreadsheet with Excel formulas
   - Test cases and validation data

3. **Technical Foundation:** `research/FDM 3D Printer Calibration and Slicer Report.md`
   - Calibration methodology
   - Best practices
   - STL file references

---

## 🎨 Design System

**Colors (from m3dp-design-system):**
- Primary Background: `slate-900` (#0f172a)
- Secondary Background: `slate-800` (#1e293b)
- Accent: `amber-500` (#f59e0b)
- Accent Hover: `amber-600` (#d97706)
- Text: `slate-100` (#f1f5f9)
- Muted Text: `slate-400` (#94a3b8)

**Typography:**
- System font stack (native performance)
- Clear hierarchy for technical data
- Monospace for code/values

**Layout:**
- Responsive grid system
- Mobile-first approach
- Accessible form controls

---

## 🧪 Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines:

- **Code Style:** Type hints required, Ruff formatting recommended
- **Testing:** Pytest with 80%+ coverage target
- **Commit Conventions:** Conventional Commits (feat, fix, docs, etc.)
- **PR Workflow:** Feature branches, squash merges

### Running Tests

```bash
# Backend tests
cd backend
pytest

# With coverage
pytest --cov=app --cov-report=html
```

### Code Quality

```bash
# Lint and format (if using Ruff)
ruff check .
ruff format .
```

---

## 📚 Documentation

### User Guides
- [Setup Guide](docs/development/SETUP_SUMMARY.md) - Environment setup
- [Deployment Options](docs/deployment/DEPLOYMENT_OPTIONS.md) - Railway deployment

### Developer Resources
- [TODO.md](TODO.md) - Current sprint tasks and calculator backlog
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development workflow
- [GitHub Token Setup](docs/development/GITHUB_TOKEN_SETUP.md) - CI/CD setup

### Archived Documentation
- `docs/archived/` - Vision AI features (removed in v2-lean refactor)
- Phase-specific documentation (consolidated into TODO.md)

---

## 🚀 Deployment

### Railway (Recommended)

1. Create new Railway project
2. Connect GitHub repository
3. Add environment variables (if needed)
4. Deploy from `refactor/v2-lean` branch

See [Deployment Options](docs/deployment/DEPLOYMENT_OPTIONS.md) for detailed Railway setup.

### Docker

```bash
# Build image
docker build -t m3dp-uip .

# Run container
docker run -p 8000:8000 m3dp-uip
```

---

## 🗺️ Roadmap

See [TODO.md](TODO.md) for current priorities:

### Phase 1: Core Calculators
- Implement remaining 6 calculators
- Fix skew correction CSV parsing
- Add unit tests for all calculators

### Phase 2: UI Polish
- Improve calculator form layouts
- Add result visualization
- Mobile responsiveness

### Phase 3: Deployment
- Railway production deployment
- Custom domain setup
- Smart link redirects

---

## 📄 License

**Proprietary** - © 2025 Minimal 3DP

All rights reserved. This software is proprietary and may not be copied, modified, or distributed without explicit permission from Minimal 3DP.

---

## 🔗 Links

- **Website:** [minimal3dp.com](https://minimal3dp.com)
- **YouTube:** 10K+ subscribers
- **Support:** Contact through minimal3dp.com

---

**Built with ❤️ for the 3D printing community**
