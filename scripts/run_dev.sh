#!/bin/bash
# Start FastAPI development server
set -e

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

# Default values
HOST="127.0.0.1"
PORT="8000"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --host)
            HOST="$2"
            shift 2
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--host HOST] [--port PORT]"
            exit 1
            ;;
    esac
done

# Change to project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    log_info "Activating virtual environment..."
    source .venv/bin/activate
fi

log_info "Starting M3DP-UIP development server..."
log_info "Host: $HOST"
log_info "Port: $PORT"
log_info "API Docs: http://$HOST:$PORT/docs"
log_info "Press Ctrl+C to stop"

cd backend
uvicorn app.main:app --reload --host "$HOST" --port "$PORT"
