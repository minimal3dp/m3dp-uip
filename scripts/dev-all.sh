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

# Store repo root for absolute path resolution
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Resolve Python interpreter (prefer local virtual environment)
AUTO_BOOTSTRAP_VENV="${AUTO_BOOTSTRAP_VENV:-true}" # set to false to disable auto creation

if [ -x "$REPO_ROOT/.venv/bin/python" ]; then
  PYTHON_CMD="$REPO_ROOT/.venv/bin/python"
else
  # Attempt bootstrap if requested
  if [ "$AUTO_BOOTSTRAP_VENV" = "true" ]; then
    echo "[BOOTSTRAP] Creating local virtual environment ($REPO_ROOT/.venv)"
    if command -v python3 >/dev/null 2>&1; then
      python3 -m venv "$REPO_ROOT/.venv" || { echo "[BOOTSTRAP ERROR] Failed to create venv"; exit 1; }
    elif command -v python >/dev/null 2>&1; then
      python -m venv "$REPO_ROOT/.venv" || { echo "[BOOTSTRAP ERROR] Failed to create venv"; exit 1; }
    else
      echo "[BACKEND ERROR] No python interpreter found to create venv."; exit 1
    fi
    if [ -x "$REPO_ROOT/.venv/bin/python" ]; then
      echo "[BOOTSTRAP] Installing backend dependencies (editable + dev)"
      "$REPO_ROOT/.venv/bin/python" -m pip install --upgrade pip >/dev/null 2>&1 || true
      cd "$REPO_ROOT" && "$REPO_ROOT/.venv/bin/python" -m pip install -e ".[dev]" || { echo "[BOOTSTRAP ERROR] pip install failed"; exit 1; }
    fi
  fi
  if [ -x "$REPO_ROOT/.venv/bin/python" ]; then
    PYTHON_CMD="$REPO_ROOT/.venv/bin/python"
  else
    PYTHON_CMD="$(command -v python3 || command -v python || echo python)"
  fi
fi

echo "[INFO] Using Python interpreter: $PYTHON_CMD"
if ! "$PYTHON_CMD" -c 'import sys; print(sys.version)' >/dev/null 2>&1; then
  echo "[BACKEND ERROR] Python interpreter not functional. Check installation."
  exit 1
fi

echo "==> Starting Backend (port $BACKEND_PORT)"
(
  cd backend || { echo "[BACKEND ERROR] backend directory not found"; exit 1; }
  # Run from inside backend so imports like 'from app.api...' resolve
  "$PYTHON_CMD" -m uvicorn app.main:app \
    --host 0.0.0.0 \
    --port "$BACKEND_PORT" \
    --reload
) &
BACKEND_PID=$!

sleep 1
if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
  echo "[BACKEND ERROR] Backend process failed to start. Check Python deps or uvicorn install."
  exit 1
fi

echo "==> Starting Frontend (port $FRONTEND_PORT)"
(
  cd frontend || { echo "[FRONTEND ERROR] frontend directory not found"; exit 1; }
  NUXT_PUBLIC_API_BASE="${NUXT_PUBLIC_API_BASE:-http://localhost:$BACKEND_PORT}" \
  FRONTEND_PORT="$FRONTEND_PORT" \
  npm run dev -- --port "$FRONTEND_PORT"
) &
FRONTEND_PID=$!

sleep 1
if ! kill -0 "$FRONTEND_PID" 2>/dev/null; then
  echo "[FRONTEND ERROR] Frontend process failed to start. Verify Node modules installed (npm install)."
  kill "$BACKEND_PID" 2>/dev/null || true
  exit 1
fi

cleanup() {
  echo "\n==> Shutting down..."
  for pid in "$FRONTEND_PID" "$BACKEND_PID"; do
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
    fi
  done
  wait "$FRONTEND_PID" 2>/dev/null || true
  wait "$BACKEND_PID" 2>/dev/null || true
  echo "==> All processes stopped."
}

trap cleanup INT TERM EXIT

echo "==> Dev environment running. Backend: http://localhost:$BACKEND_PORT | Frontend: http://localhost:$FRONTEND_PORT"
echo "==> Press Ctrl+C to stop."

wait
