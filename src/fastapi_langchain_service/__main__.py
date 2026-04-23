"""Command line entry point for local ASGI serving."""

import uvicorn

from fastapi_langchain_service.config import get_settings


def main() -> None:
    settings = get_settings()
    uvicorn.run(
        "fastapi_langchain_service.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


if __name__ == "__main__":
    main()
