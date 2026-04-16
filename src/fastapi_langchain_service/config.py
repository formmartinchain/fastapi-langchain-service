"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the API and LangChain provider."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "FastAPI LangChain Service"
    environment: str = "local"
    api_prefix: str = "/api"
    log_level: str = "INFO"
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = False

    openai_api_key: str | None = Field(default=None, repr=False)
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.2
    chain_system_prompt: str = "You are a concise assistant for API users."


@lru_cache
def get_settings() -> Settings:
    """Return cached process settings."""

    return Settings()
