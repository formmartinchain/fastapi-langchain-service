# API

## `GET /api/health`

Returns service status and environment metadata.

Response:

```json
{
  "status": "ok",
  "app_name": "FastAPI LangChain Service",
  "environment": "local"
}
```

## `POST /api/chat`

Sends a user message to the configured LangChain runnable.

Request:

```json
{
  "message": "Write a short release note.",
  "session_id": "demo",
  "metadata": {
    "source": "example"
  }
}
```

Response:

```json
{
  "answer": "Release note text...",
  "session_id": "demo",
  "provider": "langchain",
  "latency_ms": 42.5
}
```
