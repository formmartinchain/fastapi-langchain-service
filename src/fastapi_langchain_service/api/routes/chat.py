"""Chat endpoint."""

from fastapi import APIRouter, Depends

from fastapi_langchain_service.api.dependencies import get_chat_service
from fastapi_langchain_service.schemas.chat import ChatRequest, ChatResponse
from fastapi_langchain_service.services.chat import ChatService

router = APIRouter()


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    return await service.answer(request)
