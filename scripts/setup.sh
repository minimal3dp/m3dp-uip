#!/bin/bash
# Initial project setup script
set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Change to project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

log_info "Setting up M3DP-UIP project..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    log_error "Python 3 is not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
log_info "Found Python $PYTHON_VERSION"

# Create virtual environment
if [ ! -d ".venv" ]; then
    log_info "Creating virtual environment..."
    python3 -m venv .venv
else
    log_info "Virtual environment already exists"
fi

# Activate virtual environment
log_info "Activating virtual environment..."
source .venv/bin/activate

# Install/upgrade UV
log_info "Installing UV..."
pip install -q --upgrade uv

# Install dependencies
log_info "Installing dependencies..."
uv pip install -e .

log_info "Installing development dependencies..."
uv pip install -e ".[dev]"

# Setup .env file
if [ ! -f ".env" ]; then
    log_info "Creating .env from template..."
    cp .env.example .env
    log_warn "Please edit .env with your actual API keys"
else
    log_info ".env already exists"
fi

# Install pre-commit hooks
log_info "Installing pre-commit hooks..."
pre-commit install

# Create necessary directories
log_info "Creating data directories..."
mkdir -p backend/app/data/klipper_calibrations
mkdir -p backend/app/data/orca_recommendations
mkdir -p research/papers
mkdir -p research/articles

log_info "Running initial tests..."
pytest backend/tests/ -v || log_warn "Some tests failed (expected for new setup)"

echo ""
log_info "Setup complete! ✨"
echo ""
echo "Next steps:"
echo "  1. Activate virtual environment: source .venv/bin/activate"
echo "  2. Edit .env with your API keys"
echo "  3. Add CSV files to backend/app/data/"
echo "  4. Start development server: ./scripts/run_dev.sh"
echo ""
