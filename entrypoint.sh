#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Run migrations (if using Django or Flask-Migrate)
python manage.py migrate

# Start the application server (Django or Flask-based)
python manage.py runserver 0.0.0.0:8000
