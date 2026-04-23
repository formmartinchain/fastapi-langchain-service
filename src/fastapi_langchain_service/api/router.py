"""Top-level API router."""

from fastapi import APIRouter

from fastapi_langchain_service.api.routes import chat, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
