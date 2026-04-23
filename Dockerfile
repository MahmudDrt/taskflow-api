FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN cat requirements.txt && \
    python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip show uvicorn

COPY . .

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]