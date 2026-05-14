"""Chat endpoint contract tests."""

from fastapi.testclient import TestClient

from fastapi_langchain_service.main import create_app


def test_chat_uses_placeholder_without_provider_key(test_settings) -> None:
    client = TestClient(create_app(test_settings))

    response = client.post("/api/chat", json={"message": "hello"})

    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "langchain"
    assert "OPENAI_API_KEY is not configured" in body["answer"]
