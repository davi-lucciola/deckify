# Build Stage
FROM python:3.13-alpine AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /deckify-api

RUN apk update && \
    apk add gcc

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev

# Runtime Stage
FROM python:3.13-alpine AS runtime

WORKDIR /deckify-api

COPY --from=builder /deckify-api/.venv /deckify-api/.venv
COPY ./app /deckify-api/app

ENV PATH="/deckify-api/.venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]