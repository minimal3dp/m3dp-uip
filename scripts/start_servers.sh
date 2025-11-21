#!/usr/bin/env bash
#
# Start both backend and frontend dev servers for integration testing
#
# This script starts:
# - Backend (FastAPI) on http://localhost:8000
# - Frontend (Nuxt) on http://localhost:3000
#
# Press Ctrl+C to stop both servers

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
FRONTEND_DIR="$PROJECT_ROOT/frontend"

# PID file locations
BACKEND_PID_FILE="/tmp/m3dp-backend.pid"
FRONTEND_PID_FILE="/tmp/m3dp-frontend.pid"

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

    if [ -f "$FRONTEND_PID_FILE" ]; then
        FRONTEND_PID=$(cat "$FRONTEND_PID_FILE")
        if kill -0 "$FRONTEND_PID" 2>/dev/null; then
            echo -e "${BLUE}Stopping frontend (PID: $FRONTEND_PID)${NC}"
            kill "$FRONTEND_PID" 2>/dev/null || true
        fi
        rm -f "$FRONTEND_PID_FILE"
    fi

    # Kill any remaining processes on ports 8000 and 3000
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    lsof -ti:3000 | xargs kill -9 2>/dev/null || true

    echo -e "${GREEN}Servers stopped${NC}"
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
echo -e "${BLUE}  M3DP-UIP Development Servers${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check for required directories
if [ ! -d "$BACKEND_DIR" ]; then
    echo -e "${RED}Error: Backend directory not found at $BACKEND_DIR${NC}"
    exit 1
fi

if [ ! -d "$FRONTEND_DIR" ]; then
    echo -e "${RED}Error: Frontend directory not found at $FRONTEND_DIR${NC}"
    exit 1
fi

# Clean up any existing processes
check_port 8000
check_port 3000

# Start Backend Server
echo -e "${GREEN}Starting Backend Server...${NC}"
echo -e "${BLUE}  • FastAPI on http://localhost:8000${NC}"
echo -e "${BLUE}  • API Docs: http://localhost:8000/docs${NC}"
echo ""

cd "$PROJECT_ROOT"
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 > /tmp/m3dp-backend.log 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID > "$BACKEND_PID_FILE"

# Wait for backend to start
echo -e "${YELLOW}Waiting for backend to start...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Backend ready${NC}"
        break
    fi
    sleep 1
    if [ $i -eq 30 ]; then
        echo -e "${RED}✗ Backend failed to start${NC}"
        echo -e "${YELLOW}Check logs: tail -f /tmp/m3dp-backend.log${NC}"
        cleanup
    fi
done

echo ""

# Start Frontend Server
echo -e "${GREEN}Starting Frontend Server...${NC}"
echo -e "${BLUE}  • Nuxt on http://localhost:3000${NC}"
echo ""

cd "$FRONTEND_DIR"
npm run dev > /tmp/m3dp-frontend.log 2>&1 &
FRONTEND_PID=$!
echo $FRONTEND_PID > "$FRONTEND_PID_FILE"

# Wait for frontend to start
echo -e "${YELLOW}Waiting for frontend to start...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:3000 > /dev/null 2>&1; then
        echo -e "${GREEN}✓ Frontend ready${NC}"
        break
    fi
    sleep 1
    if [ $i -eq 30 ]; then
        echo -e "${RED}✗ Frontend failed to start${NC}"
        echo -e "${YELLOW}Check logs: tail -f /tmp/m3dp-frontend.log${NC}"
        cleanup
    fi
done

echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}  🚀 Servers Running${NC}"
echo -e "${GREEN}================================================${NC}"
echo ""
echo -e "${BLUE}Frontend:${NC}  http://localhost:3000"
echo -e "${BLUE}Backend:${NC}   http://localhost:8000"
echo -e "${BLUE}API Docs:${NC}  http://localhost:8000/docs"
echo ""
echo -e "${YELLOW}Test URLs:${NC}"
echo -e "  • Calculators: ${BLUE}http://localhost:3000/calculators${NC}"
echo -e "  • Diagnosis:   ${BLUE}http://localhost:3000/diagnosis${NC}"
echo ""
echo -e "${YELLOW}Logs:${NC}"
echo -e "  • Backend:  tail -f /tmp/m3dp-backend.log"
echo -e "  • Frontend: tail -f /tmp/m3dp-frontend.log"
echo ""
echo -e "${RED}Press Ctrl+C to stop both servers${NC}"
echo ""

# Keep script running and show combined logs
tail -f /tmp/m3dp-backend.log /tmp/m3dp-frontend.log &
TAIL_PID=$!

# Wait for interrupt
wait $TAIL_PID
