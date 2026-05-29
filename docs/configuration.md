# Configuration

Settings are loaded from environment variables and an optional `.env` file.

| Variable | Default | Purpose |
| --- | --- | --- |
| `APP_NAME` | `FastAPI LangChain Service` | Display name for API docs and health checks. |
| `ENVIRONMENT` | `local` | Runtime environment label. |
| `API_PREFIX` | `/api` | Prefix for API routes and OpenAPI docs. |
| `LOG_LEVEL` | `INFO` | Root logging level. |
| `HOST` | `127.0.0.1` | Local Uvicorn host for the console entry point. |
| `PORT` | `8000` | Local Uvicorn port for the console entry point. |
| `RELOAD` | `false` | Uvicorn reload flag for the console entry point. |
| `OPENAI_API_KEY` | empty | Enables the OpenAI LangChain provider when set. |
| `OPENAI_MODEL` | `gpt-4o-mini` | Chat model name passed to LangChain. |
| `OPENAI_TEMPERATURE` | `0.2` | Chat model temperature. |
| `CHAIN_SYSTEM_PROMPT` | concise assistant prompt | System message for the chat prompt. |
