# Use the lightweight Python 3.9 Alpine image
FROM python:3.9-alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app


# Install system dependencies and build tools
COPY requirements.txt /app/
RUN apk update && \
    apk add --no-cache \
    bash \
    python3-dev \
    gcc \
    libc-dev \
    libffi-dev \
    musl-dev \
    openssl-dev \
    libxml2-dev \
    supervisor \
    libxslt-dev \
    linux-headers && \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    pip install --upgrade markdown 

# Copy the rest of the application code
COPY . /app/

EXPOSE 8001

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:8000
