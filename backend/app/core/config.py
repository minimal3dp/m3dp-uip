"""
Application Configuration

Uses pydantic-settings for environment variable management.
Configuration is loaded from .env file and environment variables.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    All settings can be overridden via environment variables.
    See .env.example for available options.
    """

    # Application
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    APP_NAME: str = "M3DP-UIP"

    # API Configuration
    API_V1_PREFIX: str = "/api/v1"

    # CORS Configuration
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
        "http://localhost:8000",  # FastAPI
        "https://minimal3dp.com",
        "https://*.minimal3dp.com",
    ]

    # Vision API (Gemini)
    GOOGLE_GENAI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-1.5-pro"
    VISION_MOCK_ENABLED: bool = False  # When true, use deterministic mock vision responses

    # Amazon Product API (PA-API) - Phase 2
    PAAPI_ACCESS_KEY: str = ""
    PAAPI_SECRET_KEY: str = ""
    PAAPI_ASSOCIATE_TAG: str = "mwf064-20"

    # Google Analytics
    GA4_MEASUREMENT_ID: str = "G-VQ8RPWC2MK"

    # Database (Future - Firestore or PostgreSQL)
    DATABASE_URL: str = ""

    # File Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_IMAGE_TYPES: list[str] = ["image/jpeg", "image/png", "image/webp"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.

    The settings are cached to avoid re-reading environment
    variables on every request.
    """
    return Settings()


# Global settings instance
settings = get_settings()
