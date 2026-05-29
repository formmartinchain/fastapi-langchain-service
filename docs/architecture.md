# Architecture

The service keeps HTTP concerns, configuration, LangChain runnable creation, and
business orchestration separate.

```text
FastAPI route
  -> ChatService
  -> LangChain Runnable
  -> Model provider or placeholder runnable
```

The application factory lives in `fastapi_langchain_service.main`. It wires the
router and exception handlers and stores resolved settings on `app.state`.

The chat route depends on `ChatService`. The service receives a LangChain
`Runnable` so routes do not need to know how prompts or providers are built.
