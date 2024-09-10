#!/bin/bash

docker network rm proxy || true

docker network create proxy

touch acme.json && chmod 600 acme.json

# Build and run the Docker Compose setup
docker-compose up --build -d

# Optional: Tail the logs of the services
docker-compose logs -f
