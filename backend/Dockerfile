FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app/src

COPY . /app

COPY poetry.lock pyproject.toml /app/
COPY README.md /app/


RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry config virtualenvs.in-project false

ENV PATH="/root/.local/bin:$PATH"
RUN poetry install --no-interaction --no-ansi

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]