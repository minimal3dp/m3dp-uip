#!/bin/bash
# M3DP-UIP Server Startup Script
# Kills any running server and starts a fresh instance

set -e

PROJECT_DIR="/Users/wilsonm/development/m3dp-uip"
BACKEND_DIR="$PROJECT_DIR/backend"
PORT=8000
HOST="0.0.0.0"

echo "🔧 M3DP-UIP Server Manager"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Kill any existing process on port 8000
echo "🛑 Checking for existing server on port $PORT..."
if lsof -ti:$PORT > /dev/null 2>&1; then
    PID=$(lsof -ti:$PORT)
    echo "   Found process: $PID"
    echo "   Killing existing server..."
    kill -9 $PID 2>/dev/null || true
    sleep 1
    echo "   ✅ Server stopped"
else
    echo "   ℹ️  No server running on port $PORT"
fi

echo ""
echo "🚀 Starting M3DP-UIP server..."
echo "   Project: $PROJECT_DIR"
echo "   Backend: $BACKEND_DIR"
echo "   URL: http://$HOST:$PORT"
echo "   Docs: http://$HOST:$PORT/docs"
echo ""

# Start the server
cd "$BACKEND_DIR"
uv run uvicorn app.main:app --host "$HOST" --port "$PORT" --reload
