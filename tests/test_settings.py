"""Configuration model tests."""

from fastapi_langchain_service.config import Settings


def test_settings_defaults_to_local_environment() -> None:
    settings = Settings()

    assert settings.environment == "local"
    assert settings.api_prefix == "/api"
