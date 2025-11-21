"""
FastAPI Application Entry Point

This module initializes the FastAPI application and configures
routes, middleware, and CORS settings for the M3DP-UIP backend.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import diagnosis
from app.core.config import settings


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


# Health check endpoint
@app.get("/")
async def root():
    """Root endpoint - health check."""
    return {
        "status": "healthy",
        "service": "M3DP-UIP API",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Detailed health check endpoint."""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "csv_loaded": False,  # TODO: Check if CSV data is loaded
        "vision_api_ready": False,  # TODO: Check vision API connection
    }


# Include routers
app.include_router(diagnosis.router, prefix="/api/v1/diagnosis", tags=["diagnosis"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
