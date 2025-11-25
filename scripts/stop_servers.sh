#!/usr/bin/env bash
#
# Stop M3DP-UIP development server
#
# Kills processes running on port 8000 (backend)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Stopping M3DP-UIP server...${NC}"

# Clean up PID files
rm -f /tmp/m3dp-backend.pid

# Kill processes on port 8000 (backend)
if lsof -ti:8000 >/dev/null 2>&1; then
    echo -e "${YELLOW}Stopping backend (port 8000)${NC}"
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}✓ Backend stopped${NC}"
else
    echo -e "${BLUE}Backend not running${NC}"
fi

# Clean up log files
rm -f /tmp/m3dp-backend.log

echo -e "${GREEN}Server stopped${NC}"
