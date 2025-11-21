#!/bin/bash
# Format and lint code
set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Change to project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Check if virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    log_info "Activating virtual environment..."
    source .venv/bin/activate
fi

log_info "Formatting code with Ruff..."
ruff format .

log_info "Linting code with Ruff..."
ruff check . --fix

log_info "Running pre-commit hooks..."
pre-commit run --all-files || log_warn "Some hooks failed (may need manual fixes)"

log_info "Code formatting and linting complete! ✨"
