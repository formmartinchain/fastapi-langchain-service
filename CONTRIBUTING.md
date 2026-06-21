# Contributing

Keep changes small and focused.

Before opening a change, run the local checks with `uv`:

```bash
uv run pytest
uv run ruff check .
uv run mypy src tests
```

Do not commit secrets or local `.env` files.
