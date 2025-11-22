from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["health"])  # simple health/root endpoint
async def root():
    return {"status": "ok", "service": "m3dp-uip"}
