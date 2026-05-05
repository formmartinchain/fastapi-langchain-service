"""LangChain chat runnable construction."""

from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableLambda
from langchain_openai import ChatOpenAI

from fastapi_langchain_service.config import Settings


def build_chat_chain(settings: Settings) -> Runnable[dict[str, Any], str]:
    """Build the configured chat runnable."""

    if not settings.openai_api_key:
        return RunnableLambda(_missing_provider_response)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", settings.chain_system_prompt),
            (
                "human",
                "Session: {session_id}\nMetadata: {metadata}\n\nMessage: {message}",
            ),
        ]
    )
    model = ChatOpenAI(
        api_key=settings.openai_api_key,
        model=settings.openai_model,
        temperature=settings.openai_temperature,
    )
    return prompt | model | StrOutputParser()


def _missing_provider_response(payload: dict[str, Any]) -> str:
    message = str(payload.get("message", "")).strip()
    return (
        "OPENAI_API_KEY is not configured, so the LangChain provider was not "
        f"called. Received message: {message}"
    )
