# Deployment

The included `Dockerfile` uses the official `uv` Python image and installs the
application with `uv sync --no-dev`.

Recommended runtime environment:

- set `OPENAI_API_KEY` through the platform secret manager
- set `ENVIRONMENT` to the deployment stage
- publish port `8000`
- expose `/api/health` to the platform health checker
