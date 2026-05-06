"""Request and response models for chat."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    session_id: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    answer: str
    session_id: str | None = None
    provider: str
    latency_ms: float
