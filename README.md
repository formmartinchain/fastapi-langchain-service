# FastAPI LangChain Service

FastAPI LangChain Service is a Python API skeleton for exposing LangChain
chat workflows over HTTP. It is configured for `uv`, uses a `src/` package
layout, and keeps application wiring, chain construction, schemas, and API
routes in separate modules.

## Stack

- Python 3.12
- FastAPI
- LangChain
- LangChain OpenAI integration
- Pydantic Settings
- Uvicorn
- uv for dependency management

## Project Layout

```text
.
├── docs/
├── examples/
├── src/fastapi_langchain_service/
├── tests/
├── .env.example
├── .python-version
├── pyproject.toml
└── README.md
```

## Development

This repository is ready for `uv` workflows. A lockfile is intentionally not
included until dependency resolution is run.

```bash
uv sync
cp .env.example .env
uv run uvicorn fastapi_langchain_service.main:app --reload
```

## API

- `GET /api/health` returns application status and configuration metadata.
- `POST /api/chat` sends a message through the configured LangChain runnable.

Example request:

```bash
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "content-type: application/json" \
  -d '{"message":"Draft a concise project status update.","session_id":"demo"}'
```

## Configuration

Configuration is read from environment variables. See `.env.example` for the
available settings. The chat chain uses `OPENAI_API_KEY` when it is present and
falls back to a deterministic placeholder response when it is not configured.

## Verification

Static test files are included under `tests/`. They are not run automatically by
the repository itself.
