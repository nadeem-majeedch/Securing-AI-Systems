# A deliberately small, hardened-enough container for the starter service.
# For P5 you will need to go further: read-only root filesystem, dropped capabilities, resource limits.

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    SAS_DB=/data/starter.db

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY rag ./rag
COPY monitoring ./monitoring

# Non-root, owning only the data directory.
RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /data /app
USER appuser

EXPOSE 8100
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8100"]
