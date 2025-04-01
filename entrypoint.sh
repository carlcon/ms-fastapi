#!/bin/bash

# Exit on error
set -e

# Load environment variables from .env file if it exists
if [ -f .env ]; then
    echo "Loading environment variables from .env file..."
    export $(cat .env | grep -v '^#' | xargs)
fi

# Default values (will be overridden by .env if present)
PORT=${PORT:-8000}
HOST=${HOST:-0.0.0.0}
WORKERS=${WORKERS:-4}
LOG_LEVEL=${LOG_LEVEL:-info}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to display usage
show_usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -p, --port PORT      Port to bind to (default: 8000)"
    echo "  -h, --host HOST      Host to bind to (default: 0.0.0.0)"
    echo "  -w, --workers N      Number of worker processes (default: 4)"
    echo "  -l, --log-level LVL  Log level (default: info)"
    echo "  --help              Show this help message"
    exit 1
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        -h|--host)
            HOST="$2"
            shift 2
            ;;
        -w|--workers)
            WORKERS="$2"
            shift 2
            ;;
        -l|--log-level)
            LOG_LEVEL="$2"
            shift 2
            ;;
        --help)
            show_usage
            ;;
        *)
            echo "Unknown option: $1"
            show_usage
            ;;
    esac
done

# Check if Python is installed
if ! command_exists python3; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command_exists pip3; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Create and activate virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Run database migrations if alembic is installed
if command_exists alembic; then
    echo "Running database migrations..."
    alembic upgrade head
fi

# Start the FastAPI application with Gunicorn
echo "Starting FastAPI application with Gunicorn..."
if [ -f "main.py" ]; then
    gunicorn main:app \
        --bind "${HOST}:${PORT}" \
        --workers "${WORKERS}" \
        --worker-class uvicorn.workers.UvicornWorker \
        --log-level "${LOG_LEVEL}" \
        --access-logfile - \
        --error-logfile - \
        --timeout 120 \
        --keep-alive 5
else
    echo "Error: main.py not found. Please ensure you have a main.py file with your FastAPI application."
    exit 1
fi
