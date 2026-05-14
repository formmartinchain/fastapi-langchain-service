"""Health endpoint contract tests."""

from fastapi.testclient import TestClient

from fastapi_langchain_service.main import create_app


def test_health_returns_app_metadata(test_settings) -> None:
    client = TestClient(create_app(test_settings))

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "app_name": "FastAPI LangChain Service",
        "environment": "test",
    }
