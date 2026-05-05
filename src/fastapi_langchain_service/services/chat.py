"""Service layer for chat requests."""

from time import perf_counter
from typing import Any

from langchain_core.runnables import Runnable

from fastapi_langchain_service.observability import scrub_metadata
from fastapi_langchain_service.schemas.chat import ChatRequest, ChatResponse


class ChatService:
    def __init__(self, chain: Runnable[dict[str, Any], str]) -> None:
        self._chain = chain

    async def answer(self, request: ChatRequest) -> ChatResponse:
        started = perf_counter()
        metadata = scrub_metadata(request.metadata)
        answer = await self._chain.ainvoke(
            {
                "message": request.message,
                "session_id": request.session_id or "anonymous",
                "metadata": metadata,
            }
        )
        latency_ms = (perf_counter() - started) * 1000
        return ChatResponse(
            answer=answer,
            session_id=request.session_id,
            provider="langchain",
            latency_ms=round(latency_ms, 2),
        )
