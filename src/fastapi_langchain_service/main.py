"""ASGI application factory."""

from fastapi import FastAPI

from fastapi_langchain_service.api.router import api_router
from fastapi_langchain_service.config import Settings, get_settings
from fastapi_langchain_service.errors import add_exception_handlers
from fastapi_langchain_service.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings)

    app = FastAPI(
        title=resolved_settings.app_name,
        version="0.1.0",
        docs_url=f"{resolved_settings.api_prefix}/docs",
        openapi_url=f"{resolved_settings.api_prefix}/openapi.json",
    )
    app.state.settings = resolved_settings
    app.include_router(api_router, prefix=resolved_settings.api_prefix)
    add_exception_handlers(app)
    return app


app = create_app()
