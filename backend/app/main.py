"""
FastAPI Application Entry Point

This module initializes the FastAPI application and configures
routes, middleware, and CORS settings for the M3DP-UIP backend.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import calculators, diagnosis
from app.core.config import settings
from app.services.csv_loader import get_csv_loader


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
app.include_router(diagnosis.router, prefix="/api/v1/diagnosis", tags=["diagnosis"])
app.include_router(calculators.router, prefix="/api/v1/calculators", tags=["calculators"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
