# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for netifaces
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy the app code
COPY ./app /app/app
COPY ./gradio_frontend.py /app/

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000 7860

# Run both FastAPI and Gradio
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & python3 gradio_frontend.py"]
