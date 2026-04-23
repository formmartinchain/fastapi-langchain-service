"""Health endpoint."""

from fastapi import APIRouter, Depends

from fastapi_langchain_service.api.dependencies import get_request_settings
from fastapi_langchain_service.config import Settings
from fastapi_langchain_service.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health(
    settings: Settings = Depends(get_request_settings),
) -> HealthResponse:
    return HealthResponse(
        status="ok",
        app_name=settings.app_name,
        environment=settings.environment,
    )
