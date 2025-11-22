#!/usr/bin/env bash
#
# Stop M3DP-UIP development servers
#
# Kills processes running on ports 8000 (backend) and 3000 (frontend)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Stopping M3DP-UIP servers...${NC}"

# Clean up PID files
rm -f /tmp/m3dp-backend.pid /tmp/m3dp-frontend.pid

# Kill processes on port 8000 (backend)
if lsof -ti:8000 >/dev/null 2>&1; then
    echo -e "${YELLOW}Stopping backend (port 8000)${NC}"
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}✓ Backend stopped${NC}"
else
    echo -e "${BLUE}Backend not running${NC}"
fi

# Kill processes on port 3000 (frontend)
if lsof -ti:3000 >/dev/null 2>&1; then
    echo -e "${YELLOW}Stopping frontend (port 3000)${NC}"
    lsof -ti:3000 | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}✓ Frontend stopped${NC}"
else
    echo -e "${BLUE}Frontend not running${NC}"
fi

# Clean up log files
rm -f /tmp/m3dp-backend.log /tmp/m3dp-frontend.log

echo -e "${GREEN}All servers stopped${NC}"
