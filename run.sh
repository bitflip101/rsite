#!/bin/bash

# Define virtual environment and requirements file paths
# Use `readlink` to get the script's absolute directory, ensuring consistency
PROJECT_PATH=$(dirname "$(readlink -f "$0")")
# echo "The script directory is: $PROJECT_PATH"
VENV_PATH="./rvenv"
REQUIREMENTS_PATH="requirements.txt"
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
echo "📦 Installing/updating dependencies..."
pip install -r "$REQUIREMENTS_PATH"

# Run based on the first argument (prod or dev)
if [ "$1" == "prod" ]; then
    echo "🚀 Starting Gunicorn with production settings..."
    # Set the Django settings module
    export DJANGO_SETTINGS_MODULE="rsite.settings.prod"

    # Define the socket path
    export GUNICORN_SOCK_PATH="unix:${PROJECT_PATH}/gunicorn.sock"

    # Execute Gunicorn, passing the bind path directly as an argument
    exec gunicorn --bind "$GUNICORN_SOCK_PATH" --workers 3 rsite.wsgi:application
    # exec gunicorn --bind unix:/home/rolito/Dev/py/Rsite/rsite/gunicorn.sock --workers 4 rsite.wsgi:application
else
    echo "🧪 Starting Django development server with dev settings..."
    export DJANGO_SETTINGS_MODULE="rsite.settings.dev"
    python manage.py runserver 127.0.0.1:8000
fi