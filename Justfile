[private]
[no-exit-message]
default:
    @just --choose

build:
  uv sync

test:
  uv run pytest tests

lint:
  uv run pre-commit run --all-files
