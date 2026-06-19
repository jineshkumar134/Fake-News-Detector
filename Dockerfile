FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (exiftool is required for image analysis, build-essential for compiling libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    exiftool \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code and frontend assets
COPY backend/ ./backend/
COPY frontend/ ./frontend/

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/backend

# Railway will override the port using the PORT env var if needed, uvicorn will listen on 8000 by default
EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
