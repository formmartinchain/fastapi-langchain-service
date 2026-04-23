"""FastAPI dependency providers."""

from fastapi import Request

from fastapi_langchain_service.chains.chat import build_chat_chain
from fastapi_langchain_service.config import Settings
from fastapi_langchain_service.services.chat import ChatService


def get_request_settings(request: Request) -> Settings:
    return request.app.state.settings


def get_chat_service(request: Request) -> ChatService:
    service: ChatService | None = getattr(request.app.state, "chat_service", None)
    if service is None:
        settings = get_request_settings(request)
        service = ChatService(chain=build_chat_chain(settings))
        request.app.state.chat_service = service
    return service
