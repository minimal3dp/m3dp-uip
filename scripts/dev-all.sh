#!/usr/bin/env bash
################################################################################
# M3DP-UIP Full-Stack Dev Runner
#
# Starts FastAPI backend (uvicorn reload) and Nuxt frontend concurrently.
# Provides graceful shutdown (Ctrl+C) and port configurability via env vars.
#
# Usage:
#   chmod +x scripts/dev-all.sh   # first time
#   ./scripts/dev-all.sh
#
# Optional environment variables:
#   BACKEND_PORT (default 8000)
#   FRONTEND_PORT (default 3000)
#   NUXT_PUBLIC_API_BASE (override backend API base in frontend)
#
# Notes:
# - Assumes Python deps installed (e.g. `pip install .[dev]`).
# - Assumes Node deps installed in `frontend` (`npm install`).
# - Uses `uvicorn` reload + Nuxt dev server for hot updates.
################################################################################
set -euo pipefail

BACKEND_PORT="${BACKEND_PORT:-8000}"
FRONTEND_PORT="${FRONTEND_PORT:-3000}"

echo "==> Starting Backend (port $BACKEND_PORT)"
python -m uvicorn backend.app.main:app \
  --host 0.0.0.0 \
  --port "$BACKEND_PORT" \
  --reload &
BACKEND_PID=$!

echo "==> Starting Frontend (port $FRONTEND_PORT)"
pushd frontend >/dev/null
NUXT_PUBLIC_API_BASE="${NUXT_PUBLIC_API_BASE:-http://localhost:$BACKEND_PORT}" \
FRONTEND_PORT="$FRONTEND_PORT" \
npm run dev -- --port "$FRONTEND_PORT" &
FRONTEND_PID=$!
popd >/dev/null

cleanup() {
  echo "\n==> Shutting down..."
  for pid in "$FRONTEND_PID" "$BACKEND_PID"; do
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
    fi
  end
  wait "$FRONTEND_PID" 2>/dev/null || true
  wait "$BACKEND_PID" 2>/dev/null || true
  echo "==> All processes stopped."
}

trap cleanup INT TERM EXIT

echo "==> Dev environment running. Backend: http://localhost:$BACKEND_PORT | Frontend: http://localhost:$FRONTEND_PORT"
echo "==> Press Ctrl+C to stop."

wait
