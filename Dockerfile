FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml README.md ./
COPY src ./src

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "fastapi_langchain_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
