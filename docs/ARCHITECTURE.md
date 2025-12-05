# M3DP-UIP Architecture

## Overview

M3DP-UIP is a **stateless, server-side rendered web application** built with FastAPI and Jinja2. The architecture prioritizes simplicity, formula accuracy, and zero AI dependencies.

## Design Philosophy

1. **Formula-Driven:** All calculations come from CSV data and Klipper documentation
2. **Stateless:** No sessions, cookies, or persistent state
3. **Server-Side Rendering:** HTML templates with Jinja2, minimal client-side JavaScript
4. **Type-Safe:** Pydantic models for request validation
5. **CSV-Centric:** All calibration data loaded from structured CSV files

## Technology Stack

### Backend
- **Framework:** FastAPI 0.115+ (async, fast, auto-docs)
- **Server:** Uvicorn 0.32+ (ASGI)
- **Templating:** Jinja2 3.1+ (server-side rendering)
- **Data Processing:** Pandas 2.2+ (CSV loading and manipulation)
- **Validation:** Pydantic 2.9+ (request/response models)
- **Environment:** Python 3.12+ (type hints, performance)

### Frontend
- **HTML5** + Jinja2 templates (server-side rendering)
- **Styling:** TailwindCSS v3+ (CDN, ~50KB)
- **Interactivity:** HTMX 1.9.10 (~14KB) + Alpine.js 3.13.5 (~15KB)
- **Total JS:** ~29KB (minimal footprint)

### Design System
- **Primary Background:** Slate-900 (#0f172a)
- **Primary Accent:** Amber-500 (#f59e0b)
- **Font Stack:** System fonts (-apple-system, Segoe UI, Helvetica)
- **Source:** m3dp-design-system

### Deployment
- **Platform:** Railway (Docker)
- **Container:** Python 3.12 base image
- **Environment:** .env configuration

## Directory Structure

```
m3dp-uip/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints/
│   │   │       ├── calculators.py    # 2845 lines, all 16 calculator endpoints
│   │   │       └── root.py           # Health checks, home routes
│   │   ├── templates/
│   │   │   ├── base.html             # Layout, nav, footer
│   │   │   ├── index.html            # Home page, hero
│   │   │   ├── calculator_*.html     # 16 calculator forms
│   │   │   └── ...
│   │   ├── data/
│   │   │   └── klipper_calibrations/
│   │   │       ├── rotation_distance.csv
│   │   │       ├── pressure_advance.csv
│   │   │       ├── skew_correction.csv
│   │   │       └── ... (8 CSV files)
│   │   ├── models/
│   │   │   └── csv_schemas.py        # Pydantic CSV data models
│   │   ├── services/
│   │   │   ├── csv_loader.py         # CSV file loading
│   │   │   ├── ga4_tracker.py        # Analytics tracking
│   │   │   └── ...
│   │   ├── core/
│   │   │   └── config.py             # Environment configuration
│   │   └── main.py                   # FastAPI application entry
│   ├── tests/
│   │   ├── test_calculators.py       # 42 calculator tests
│   │   └── test_calculators_extra.py # 4 additional tests
│   └── .venv/                        # Python virtual environment
├── research/
│   ├── EXTRACTED_FORMULAS.md         # All 16 calculator formulas
│   ├── FDM 3D Printer Calibration Report.md
│   └── Klipper Calibrations.xlsx     # Source data (16 calculators)
├── docs/
│   ├── ARCHITECTURE.md               # This file
│   ├── API.md                        # API endpoint documentation
│   ├── CALCULATOR_GUIDE.md           # How to add calculators
│   ├── deployment/
│   │   ├── RAILWAY.md                # Railway deployment guide
│   │   └── DOCKER.md                 # Docker configuration
│   └── development/
│       ├── SETUP.md                  # Development environment setup
│       ├── TESTING.md                # Test suite documentation
│       └── DEBUG.md                  # Debugging guides
├── scripts/
│   └── start_server.sh               # Server startup script
├── .vscode/
│   ├── settings.json                 # Python interpreter, auto-format
│   └── launch.json                   # Debug configurations
├── .env.example                      # Environment template
├── .pre-commit-config.yaml           # Git hooks
├── pyproject.toml                    # Dependencies, project config
├── README.md                         # Quick start guide
├── CONTRIBUTING.md                   # Contribution guidelines
└── TODO.md                           # Sprint tracking
```

## Request/Response Flow

```
┌─────────────┐
│   Browser   │
│  (HTMX)     │
└──────┬──────┘
       │ HTTP GET/POST
       ▼
┌──────────────────────────────────────┐
│    FastAPI Application (main.py)     │
│  - CORS middleware                   │
│  - Error handlers                    │
│  - Lifespan management               │
└──────────────┬───────────────────────┘
               │
       ┌───────┴──────────┐
       ▼                  ▼
┌──────────────┐   ┌─────────────────┐
│ Calculators  │   │ CSV Data        │
│ (API Logic)  │   │ Loader          │
│              │   │ (pandas)        │
│ - Validation │   │                 │
│ - Formula    │   │ - Load CSV      │
│   execution  │   │ - Parse rows    │
│ - Response   │   │ - Cache in RAM  │
└──────────────┘   └─────────────────┘
       │
       ▼
┌──────────────────────────────────────┐
│    Jinja2 Template Rendering         │
│  - Data interpolation                │
│  - Conditional blocks                │
│  - Loops                             │
└──────────────┬───────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ HTML + CSS   │
        │ (TailwindCSS)│
        │              │
        │ + JavaScript │
        │ (HTMX,       │
        │  Alpine.js)  │
        └──────────────┘
```

## Data Flow for Calculators

### 1. Calculator Request (Client → Server)

```python
# User submits form via HTMX
POST /api/v1/calculators/rotation_distance
{
  "current_rotation_distance": 33.5,
  "requested_extrusion": 100,
  "actual_extrusion": 98.5
}
```

### 2. Request Validation (Pydantic)

```python
class RotationDistanceRequest(BaseModel):
    current_rotation_distance: float = Field(..., gt=0, le=100)
    requested_extrusion: float = Field(..., gt=0, le=500)
    actual_extrusion: float = Field(..., gt=0, le=500)

# Pydantic validates:
# - Type checking (float)
# - Range validation (gt=greater than, le=less than or equal)
# - Required fields
# - Returns 422 if invalid
```

### 3. Calculation (Pure Math)

```python
# Formula from CSV/research
new_rd = current_rd * (requested / actual)
new_rd = 33.5 * (100 / 98.5) = 33.9137

# Change calculation
change_percent = ((new_rd - old_rd) / old_rd) * 100
change_percent = ((33.9137 - 33.5) / 33.5) * 100 = 1.23%

# Tolerance check
within_tolerance = abs(change_percent) <= 2.0  # True
```

### 4. Response Generation

```python
class RotationDistanceResponse(BaseModel):
    new_rotation_distance: float  # 33.9137
    change_percent: float  # 1.23
    within_tolerance: bool  # True
    klipper_config: str  # "rotation_distance = 33.9137"
    recommendation: str  # "Update config and test"
```

### 5. Template Rendering

```jinja2
<!-- calculator_rotation_distance.html -->
<div class="result-box">
  <h3>New Rotation Distance: {{ response.new_rotation_distance }}</h3>
  <p>Change: {{ response.change_percent }}%</p>
  {% if response.within_tolerance %}
    <p class="text-green">✓ Within tolerance</p>
  {% endif %}
  <code>{{ response.klipper_config }}</code>
</div>
```

### 6. HTML Response (Server → Client)

```html
<!-- Rendered HTML sent to browser -->
<div class="result-box">
  <h3>New Rotation Distance: 33.9137</h3>
  <p>Change: 1.23%</p>
  <p class="text-green">✓ Within tolerance</p>
  <code>rotation_distance = 33.9137</code>
</div>
```

## CSV Data Schema

All calibration data is stored in CSV files with the following structure:

```csv
parameter,value,unit,formula,notes
rotation_distance,33.5,mm,"new_rd = old_rd * (requested / actual)","E-steps calibration"
```

### CSV Loader Service

```python
class CSVLoader:
    def load_csv(self, filename: str) -> pd.DataFrame:
        # 1. Check cache (avoid repeated file reads)
        # 2. Load CSV from data/klipper_calibrations/
        # 3. Parse rows into Pydantic models
        # 4. Return DataFrame for use in calculations
        pass
```

## Error Handling

### Request Validation Errors (422)

```python
# If user submits invalid data
{
  "detail": [
    {
      "type": "greater_than",
      "loc": ["body", "current_rotation_distance"],
      "msg": "Input should be greater than 0",
      "input": -5
    }
  ]
}
```

### Calculation Errors (400)

```python
# If calculation fails
{
  "detail": "Invalid input parameters for pressure advance"
}
```

### Server Errors (500)

```python
# If CSV cannot be loaded
{
  "detail": "Internal server error"
}
```

## Performance Considerations

### Startup
- CSV files loaded into memory on app startup (~10ms)
- Jinja2 templates compiled (~100ms)
- Total startup time: ~500ms

### Request Handling
- Request validation: ~1ms
- Calculator execution: ~0.5ms
- Template rendering: ~5ms
- Total per-request: ~10ms
- Throughput: ~100 requests/second

### Caching Strategy
- **CSV Data:** Cached in memory (singleton pattern)
- **Templates:** Compiled by Jinja2 (automatic)
- **Static Files:** CDN recommended for production (TailwindCSS, HTMX, Alpine.js)

## Security

### CORS Headers
```python
# Allow requests from trusted domains
CORSMiddleware(
    allow_origins=["*"],  # Configure in production
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### Input Validation
- Pydantic enforces strict type checking
- Range validation prevents invalid inputs
- SQL injection not applicable (no database)

### Environment Secrets
- `.env.example` provided
- Sensitive values in `.env` (git-ignored)
- Loaded via `pydantic-settings`

## Stateless Architecture

### Why Stateless?
1. **Scalability:** No sticky sessions needed
2. **Reliability:** Any replica can handle any request
3. **Simplicity:** No cache invalidation problems
4. **Testing:** Easier to test without mocks

### No Sessions/Cookies
- Each request is independent
- User state stored in form submissions
- Results returned immediately (no database writes)

## Testing Strategy

### Unit Tests (42 tests)
```bash
pytest backend/tests/test_calculators.py
```
- Formula accuracy validation
- Input validation edge cases
- Response format verification
- CORS header presence

### Integration Tests (4 tests)
```bash
pytest backend/tests/test_calculators_extra.py
```
- End-to-end calculator flows
- Multi-step calibration sequences
- Error scenarios

### Coverage Target
- Calculators: 69% (prioritized)
- Models: 85% (strict validation)
- Services: 60% (CSV loading)
- Overall: 53% (includes dev-only routes)

## Deployment Architecture

### Development
```
Local Machine
    ↓
.venv (Python 3.12)
    ↓
uvicorn --reload (auto-restart on changes)
    ↓
localhost:8000 (browser access)
```

### Production
```
GitHub (main branch)
    ↓
Railway (auto-deploy on push)
    ↓
Docker image build
    ↓
Python 3.12 container
    ↓
Uvicorn (production settings)
    ↓
https://minimal3dp.com (custom domain)
```

### Environment Variables
```bash
# .env or Railway config
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info
ALLOWED_ORIGINS=https://minimal3dp.com
DATABASE_URL=  # (none - stateless)
```

## Future Enhancements

1. **Database Integration** (optional)
   - Store user calculations for history
   - Track popular calibrations
   - A/B test formula variations

2. **Advanced Calculators** (6 remaining)
   - Flow Calibration (Traditional)
   - PA & OrcaSlicer
   - Ellis Max Volumetric Speed
   - Extrusion Rate Smoothing
   - Adaptive Pressure Advance
   - Skew Correction (complete)

3. **Hardware Affiliate Links**
   - Recommended hotends, nozzles, heaters
   - Printer model compatibility matrix
   - Commission tracking via `/go/{product_id}`

4. **Mobile App**
   - React Native or Flutter
   - Same calculator backend
   - Offline mode with local CSV storage

5. **Internationalization**
   - Multiple language support
   - Unit conversion (metric/imperial)
   - Regional printer profiles

## Related Documentation

- [API Documentation](./API.md) - Endpoint reference
- [Calculator Guide](./CALCULATOR_GUIDE.md) - How to add new calculators
- [Railway Deployment](./deployment/RAILWAY.md) - Production deployment
- [Testing Guide](./development/TESTING.md) - Running and writing tests
- [Development Setup](./development/SETUP.md) - Local environment configuration
