#!/bin/bash
# Run test suite with coverage
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

# Default options
COVERAGE=true
VERBOSE=""
FILE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --fast)
            COVERAGE=false
            shift
            ;;
        --verbose)
            VERBOSE="-vv"
            shift
            ;;
        --file)
            FILE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--fast] [--verbose] [--file PATH]"
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

log_info "Running test suite..."

if [ "$COVERAGE" = true ]; then
    if [ -n "$FILE" ]; then
        pytest "$FILE" --cov=backend/app --cov-report=term-missing --cov-report=html $VERBOSE
    else
        pytest backend/tests/ --cov=backend/app --cov-report=term-missing --cov-report=html $VERBOSE
    fi

    log_info "Coverage report generated: htmlcov/index.html"
else
    if [ -n "$FILE" ]; then
        pytest "$FILE" $VERBOSE
    else
        pytest backend/tests/ $VERBOSE
    fi
fi

log_info "Tests completed! ✨"
