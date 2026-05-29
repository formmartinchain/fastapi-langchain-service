# Development

This project is configured for `uv`.

Common commands:

```bash
uv sync
uv run uvicorn fastapi_langchain_service.main:app --reload
uv run pytest
uv run ruff check .
uv run mypy src tests
```

The conversion did not create a virtual environment or resolve dependencies.
Run `uv sync` when you are ready to install packages locally.
