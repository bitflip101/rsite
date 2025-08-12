#!/bin/bash

# Define virtual environment and requirements file paths
VENV_PATH="./rvenv"
# REQUIREMENTS_PATH="requirements.txt"
GUNICORN_CONFIG_PATH="gunicorn.conf.py"

# Check if the virtual environment exists and create it if not
if [ ! -d "$VENV_PATH" ]; then
    echo "⚙️ Creating virtual environment..."
    python3 -m venv "$VENV_PATH"
    echo "✅ Virtual environment created."
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Check if requirements are up to date
# echo "📦 Installing/updating dependencies..."
# pip install -r "$REQUIREMENTS_PATH"

# Run based on the first argument (prod or dev)
if [ "$1" == "prod" ]; then
    echo "🚀 Starting Gunicorn with production settings..."
    export DJANGO_SETTINGS_MODULE="rsite.settings.prod"
    # Use 'exec' to ensure graceful shutdown
    # exec gunicorn rsite.wsgi:application --bind 0.0.0.0:8000
    exec gunicorn -c "$GUNICORN_CONFIG_PATH" rsite.wsgi:application
elif [ "$1" == "local_gunicorn" ]; then
    echo "🧪 Starting Gunicorn for local testing with dev settings and config file..."
    export DJANGO_SETTINGS_MODULE="rsite.settings.local_gunicorn"
    # exec gunicorn rsite.wsgi:application --bind 0.0.0.0:8000
    exec gunicorn -c "$GUNICORN_CONFIG_PATH" rsite.wsgi:application
else
    echo "🧪 Starting Django development server with dev settings..."
    export DJANGO_SETTINGS_MODULE="rsite.settings.dev"
    python manage.py runserver 127.0.0.1:8000
fi