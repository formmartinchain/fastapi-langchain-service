"""Shared pytest fixtures."""

import pytest

from fastapi_langchain_service.config import Settings


@pytest.fixture
def test_settings() -> Settings:
    return Settings(environment="test", openai_api_key=None)
