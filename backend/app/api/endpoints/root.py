from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["health"])
async def root() -> dict[str, str]:
    """
    Root Endpoint - Health Check.

    Returns:
        dict: Basic service status and identification.
    """
    return {"status": "ok", "service": "m3dp-uip"}
