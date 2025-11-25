#!/usr/bin/env bash
#
# Start M3DP-UIP development server (Python fullstack)
#
# This script starts:
# - Backend (FastAPI) with Python frontend on http://localhost:8000
#
# Press Ctrl+C to stop the server

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKEND_DIR="$PROJECT_ROOT/backend"

# PID file location
BACKEND_PID_FILE="/tmp/m3dp-backend.pid"

# Cleanup function
cleanup() {
    echo -e "\n${YELLOW}Stopping servers...${NC}"

    if [ -f "$BACKEND_PID_FILE" ]; then
        BACKEND_PID=$(cat "$BACKEND_PID_FILE")
        if kill -0 "$BACKEND_PID" 2>/dev/null; then
            echo -e "${BLUE}Stopping backend (PID: $BACKEND_PID)${NC}"
            kill "$BACKEND_PID" 2>/dev/null || true
        fi
        rm -f "$BACKEND_PID_FILE"
    fi

    # Kill any remaining processes on port 8000
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true

    echo -e "${GREEN}Server stopped${NC}"
    exit 0
}

# Trap Ctrl+C and cleanup
trap cleanup INT TERM

# Check if ports are already in use
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
        echo -e "${RED}Port $port is already in use!${NC}"
        echo -e "${YELLOW}Killing existing process...${NC}"
        lsof -ti:$port | xargs kill -9 2>/dev/null || true
        sleep 2
    fi
}

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}  M3DP-UIP Development Server${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check for required directories
if [ ! -d "$BACKEND_DIR" ]; then
    echo -e "${RED}Error: Backend directory not found at $BACKEND_DIR${NC}"
    exit 1
fi

# Clean up any existing processes
check_port 8000

# Start Server (Python Fullstack)
echo -e "${GREEN}Starting Server (Python Fullstack)...${NC}"
echo -e "${BLUE}  • FastAPI + Templates on http://localhost:8000${NC}"
echo -e "${BLUE}  • API Docs: http://localhost:8000/docs${NC}"
echo ""

cd "$PROJECT_ROOT"
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload > /tmp/m3dp-backend.log 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID > "$BACKEND_PID_FILE"

# Wait for server to start
echo -e "${YELLOW}Waiting for server to start...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Server ready${NC}"
        break
    fi
    sleep 1
    if [ $i -eq 30 ]; then
        echo -e "${RED}✗ Server failed to start${NC}"
        echo -e "${YELLOW}Check logs: tail -f /tmp/m3dp-backend.log${NC}"
        cleanup
    fi
done

echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}  🚀 Server Running${NC}"
echo -e "${GREEN}================================================${NC}"
echo ""
echo -e "${BLUE}Web UI:${NC}    http://localhost:8000/home"
echo -e "${BLUE}API Docs:${NC}  http://localhost:8000/docs"
echo ""
echo -e "${YELLOW}Pages:${NC}"
echo -e "  • Calculators: ${BLUE}http://localhost:8000/calculators-ui${NC}"
echo -e "  • Diagnosis:   ${BLUE}http://localhost:8000/diagnosis-ui${NC}"
echo ""
echo -e "${YELLOW}Logs:${NC}"
echo -e "  • tail -f /tmp/m3dp-backend.log"
echo ""
echo -e "${RED}Press Ctrl+C to stop the server${NC}"
echo ""

# Keep script running and show logs
tail -f /tmp/m3dp-backend.log &
TAIL_PID=$!

# Wait for interrupt
wait $TAIL_PID
