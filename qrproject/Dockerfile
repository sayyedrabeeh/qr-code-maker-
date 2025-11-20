# Use a slim Python base image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if any)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your project code
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (Koyeb will use this)
ENV PORT=8000

EXPOSE 8000

# Command to run the app
CMD ["gunicorn", "qrproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
