# Testing

Tests are organized around API contracts and small pure helpers.

Suggested checks:

```bash
uv run pytest
uv run ruff check .
uv run mypy src tests
```

Use dependency overrides or explicit application settings in tests instead of
relying on local environment variables.
