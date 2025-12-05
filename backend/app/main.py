"""
FastAPI Application Entry Point

This module initializes the FastAPI application and configures
routes, middleware, CORS settings, and template rendering for the M3DP-UIP backend.
"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.endpoints import calculators  # , diagnosis  # TODO: Re-enable after refactor
from app.core.config import settings
from app.services.csv_loader import get_csv_loader

# Setup templates and static files
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
static_dir = BASE_DIR / "static"


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup: Load CSV data, initialize services
    print("🚀 Starting M3DP-UIP Backend...")
    print(f"📊 Environment: {settings.ENVIRONMENT}")

    # TODO: Load CSV knowledge base
    # TODO: Initialize vision API client
    # TODO: Initialize database connection (if using)

    yield

    # Shutdown: Cleanup resources
    print("👋 Shutting down M3DP-UIP Backend...")


# Initialize FastAPI application
app = FastAPI(
    title="M3DP-UIP API",
    description="Minimal 3DP Unified Intelligence Platform - AI-powered 3D printing diagnostics",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


# Web Page Routes (HTML Templates)
@app.get("/home", response_class=HTMLResponse, include_in_schema=False)
async def home_page(request: Request):
    """Render homepage with HTMX/Alpine.js"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/calculators-ui", response_class=HTMLResponse, include_in_schema=False)
async def calculators_page(request: Request):
    """Render calculators list page"""
    return templates.TemplateResponse("calculators.html", {"request": request})


@app.get("/calculators/rotation-distance-ui", response_class=HTMLResponse, include_in_schema=False)
async def rotation_distance_page(request: Request):
    """Render rotation distance calculator page"""
    return templates.TemplateResponse("calculator_rotation_distance.html", {"request": request})


@app.get("/calculators/pressure-advance-ui", response_class=HTMLResponse, include_in_schema=False)
async def pressure_advance_page(request: Request):
    """Render pressure advance calculator page"""
    return templates.TemplateResponse("calculator_pressure_advance.html", {"request": request})


@app.get(
    "/calculators/max-volumetric-speed-ui", response_class=HTMLResponse, include_in_schema=False
)
async def max_volumetric_speed_page(request: Request):
    """Render max volumetric speed calculator page"""
    return templates.TemplateResponse("calculator_max_volumetric_speed.html", {"request": request})


@app.get("/calculators/input-shaping-ui", response_class=HTMLResponse, include_in_schema=False)
async def input_shaping_page(request: Request):
    """Render input shaping calculator page"""
    return templates.TemplateResponse("calculator_input_shaping.html", {"request": request})


@app.get("/calculators/orcaslicer-flow-ui", response_class=HTMLResponse, include_in_schema=False)
async def orcaslicer_flow_page(request: Request):
    """Render OrcaSlicer Flow Rate calculator page"""
    return templates.TemplateResponse("calculator_orcaslicer_flow.html", {"request": request})


@app.get(
    "/calculators/orcaslicer-flow-yolo-ui", response_class=HTMLResponse, include_in_schema=False
)
async def orcaslicer_flow_yolo_page(request: Request):
    """Render OrcaSlicer Flow YOLO calculator page"""
    return templates.TemplateResponse("calculator_orcaslicer_flow_yolo.html", {"request": request})


@app.get("/calculators/run-current-ui", response_class=HTMLResponse, include_in_schema=False)
async def run_current_page(request: Request):
    """Render run current calculator page"""
    return templates.TemplateResponse("calculator_run_current.html", {"request": request})


@app.get(
    "/calculators/lead-screw-rotation-distance-ui",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def lead_screw_rotation_distance_page(request: Request):
    """Render lead screw rotation distance calculator page"""
    return templates.TemplateResponse(
        "calculator_lead_screw_rotation_distance.html", {"request": request}
    )


@app.get("/calculators/x-and-y-offsets-ui", response_class=HTMLResponse, include_in_schema=False)
async def x_and_y_offsets_page(request: Request):
    """Render X and Y offsets calculator page"""
    return templates.TemplateResponse("calculator_x_and_y_offsets.html", {"request": request})


@app.get("/calculators/skew-correction-ui", response_class=HTMLResponse, include_in_schema=False)
async def skew_correction_page(request: Request):
    """Render skew correction calculator page"""
    return templates.TemplateResponse("calculator_skew_correction.html", {"request": request})


@app.get("/calculators/line-widths-ui", response_class=HTMLResponse, include_in_schema=False)
async def line_widths_page(request: Request):
    """Render line widths calculator page"""
    return templates.TemplateResponse("calculator_line_widths.html", {"request": request})


@app.get("/calculators/additional-ui", response_class=HTMLResponse, include_in_schema=False)
async def additional_calculators_page(request: Request):
    """Render additional calculators page (coming soon)"""
    return templates.TemplateResponse("calculator_additional.html", {"request": request})


@app.get("/calculators/pa-orcaslicer-ui", response_class=HTMLResponse, include_in_schema=False)
async def pa_orcaslicer_page(request: Request):
    """Render PA & OrcaSlicer calculator page"""
    return templates.TemplateResponse("calculator_pa_orcaslicer.html", {"request": request})


@app.get(
    "/calculators/extrusion-rate-smoothing-ui", response_class=HTMLResponse, include_in_schema=False
)
async def extrusion_rate_smoothing_page(request: Request):
    """Render Extrusion Rate Smoothing calculator page"""
    return templates.TemplateResponse(
        "calculator_extrusion_rate_smoothing.html", {"request": request}
    )


@app.get(
    "/calculators/adaptive-pressure-advance-ui",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def adaptive_pressure_advance_page(request: Request):
    """Render Adaptive Pressure Advance calculator page"""
    return templates.TemplateResponse(
        "calculator_adaptive_pressure_advance.html", {"request": request}
    )


@app.get("/calculators/temperature-tower-ui", response_class=HTMLResponse, include_in_schema=False)
async def temperature_tower_page(request: Request):
    """Render Temperature Tower calculator page"""
    return templates.TemplateResponse("calculator_temperature_tower.html", {"request": request})


@app.get("/calculators/retraction-tuning-ui", response_class=HTMLResponse, include_in_schema=False)
async def retraction_tuning_page(request: Request):
    """Render Retraction Tuning calculator page"""
    return templates.TemplateResponse("calculator_retraction_tuning.html", {"request": request})


@app.get("/calculators/belt-tension-ui", response_class=HTMLResponse, include_in_schema=False)
async def belt_tension_page(request: Request):
    """Render Belt Tension calculator page"""
    return templates.TemplateResponse("calculator_belt_tension.html", {"request": request})


# @app.get("/diagnosis-ui", response_class=HTMLResponse, include_in_schema=False)
# async def diagnosis_page(request: Request):
#     """Render AI diagnosis page"""
#     return templates.TemplateResponse("diagnosis.html", {"request": request})


# API Root Endpoint
@app.get("/")
async def root():
    """Root endpoint - consolidated health + capability summary."""
    # Attempt to access CSV loader (lazy init)
    loader = get_csv_loader()
    calculators_meta = [
        {
            "id": "rotation_distance",
            "endpoint": "/api/v1/calculators/rotation-distance",
            "description": "Extruder rotation distance calibration",
        },
        {
            "id": "pressure_advance",
            "endpoint": "/api/v1/calculators/pressure-advance",
            "description": "Optimize pressure advance for corners",
        },
        {
            "id": "input_shaping",
            "endpoint": "/api/v1/calculators/input-shaping",
            "description": "Resonance compensation guidance",
        },
    ]
    return {
        "status": "healthy",
        "service": "M3DP-UIP API",
        "version": "0.1.0",
        "environment": settings.ENVIRONMENT,
        "docs": "/docs",
        "csv_loaded": loader.is_loaded(),
        "loaded_csv_files": loader.get_available_csvs(),
        "validation_error_files": list(loader.get_validation_errors().keys()),
        "calculators": calculators_meta,
    }


@app.get("/health")
async def health_check():
    """Detailed health check endpoint."""
    loader = get_csv_loader()
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "csv_loaded": loader.is_loaded(),
        "csv_count": len(loader.get_available_csvs()),
        "vision_api_ready": False,  # Placeholder until vision service integrated
    }


# Include routers
# app.include_router(diagnosis.router, prefix="/api/v1/diagnosis", tags=["diagnosis"])  # TODO: Re-enable after refactor
app.include_router(calculators.router, prefix="/api/v1/calculators", tags=["calculators"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
