#!/bin/bash

# Run FastAPI backend with Python-based frontend (HTMX + Alpine.js)
# No Node.js/npm required!

set -e

echo "🚀 Starting M3DP-UIP (Python Full Stack)"
echo "=========================================="
echo ""

# Activate virtual environment
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first."
    exit 1
fi

source .venv/bin/activate

# Set environment variables
export PYTHONPATH="${PWD}/backend:${PYTHONPATH}"

# Default ports
BACKEND_PORT=${BACKEND_PORT:-8000}

echo "📡 Backend API: http://localhost:${BACKEND_PORT}"
echo "🌐 Web UI: http://localhost:${BACKEND_PORT}/home"
echo "📚 API Docs: http://localhost:${BACKEND_PORT}/docs"
echo ""
echo "Press Ctrl+C to stop..."
echo ""

# Run backend with uvicorn
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port ${BACKEND_PORT}
