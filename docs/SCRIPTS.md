# Scripts Guide

Utility scripts for M3DP-UIP project management and operations.

## Available Scripts

### Development Scripts

Create scripts in the `scripts/` directory for common tasks:

```bash
scripts/
├── setup.sh              # Initial project setup
├── run_dev.sh           # Start development server
├── run_tests.sh         # Run test suite
├── format_code.sh       # Format and lint code
├── ingest_csv.py        # Load CSV files into database
└── generate_config.py   # Generate Klipper configs
```

## Script Usage

### setup.sh - Initial Project Setup

Automates the complete project setup process.

**Usage:**
```bash
./scripts/setup.sh
```

**What it does:**
1. Creates virtual environment
2. Installs UV
3. Installs dependencies
4. Sets up pre-commit hooks
5. Creates `.env` from `.env.example`
6. Runs initial tests

### run_dev.sh - Start Development Server

Starts the FastAPI development server with auto-reload.

**Usage:**
```bash
./scripts/run_dev.sh
```

**Options:**
```bash
./scripts/run_dev.sh --port 8001  # Use custom port
./scripts/run_dev.sh --host 0.0.0.0  # Bind to all interfaces
```

### run_tests.sh - Run Test Suite

Runs the complete test suite with coverage reporting.

**Usage:**
```bash
./scripts/run_tests.sh
```

**Options:**
```bash
./scripts/run_tests.sh --fast      # Skip coverage
./scripts/run_tests.sh --verbose   # Verbose output
./scripts/run_tests.sh --file backend/tests/test_api.py  # Specific file
```

### format_code.sh - Format and Lint

Formats code with Ruff and runs linting checks.

**Usage:**
```bash
./scripts/format_code.sh
```

**What it does:**
1. Runs `ruff format .`
2. Runs `ruff check . --fix`
3. Runs pre-commit hooks
4. Reports any unfixable issues

### ingest_csv.py - Load CSV Knowledge Base

Python script to load CSV files into the application's memory cache or database.

**Usage:**
```bash
uv run python scripts/ingest_csv.py
```

**Options:**
```bash
# Load specific category
python scripts/ingest_csv.py --category klipper

# Validate CSV structure
python scripts/ingest_csv.py --validate

# Export to JSON
python scripts/ingest_csv.py --export json
```

**What it does:**
1. Scans `backend/app/data/` for CSV files
2. Validates CSV structure and data types
3. Loads data into cache
4. Reports any errors or warnings

### generate_config.py - Generate Klipper Configs

Generates Klipper configuration files based on calculator results.

**Usage:**
```bash
python scripts/generate_config.py --calculator rotation_distance --value 20.313
```

**Examples:**
```bash
# Generate rotation distance config
python scripts/generate_config.py \
  --calculator rotation_distance \
  --value 20.313 \
  --output printer.cfg

# Generate pressure advance config
python scripts/generate_config.py \
  --calculator pressure_advance \
  --value 0.045 \
  --filament PLA

# Generate complete config from JSON
python scripts/generate_config.py \
  --from-json results.json \
  --output klipper_config.cfg
```

## Creating New Scripts

### Shell Script Template

```bash
#!/bin/bash
# Script name and description
set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Main script logic
main() {
    log_info "Starting script..."
    # Your code here
}

main "$@"
```

### Python Script Template

```python
#!/usr/bin/env python3
"""
Script name and description.

Usage:
    python script_name.py [options]
"""

import argparse
import sys
from pathlib import Path

def main():
    """Main script entry point."""
    parser = argparse.ArgumentParser(
        description="Script description"
    )
    parser.add_argument(
        "--option",
        help="Option description",
    )

    args = parser.parse_args()

    # Your logic here
    print("Script completed successfully")

if __name__ == "__main__":
    main()
```

## Script Best Practices

1. **Make scripts executable:**
   ```bash
   chmod +x scripts/your_script.sh
   ```

2. **Add shebang line:**
   ```bash
   #!/bin/bash
   # or
   #!/usr/bin/env python3
   ```

3. **Use set -e for bash scripts:**
   ```bash
   set -e  # Exit on first error
   ```

4. **Add help text:**
   ```bash
   if [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
       echo "Usage: $0 [options]"
       exit 0
   fi
   ```

5. **Check for required tools:**
   ```bash
   command -v uv >/dev/null 2>&1 || {
       echo "UV is required but not installed."
       exit 1
   }
   ```

6. **Use meaningful exit codes:**
   - `0` - Success
   - `1` - General error
   - `2` - Misuse of command
   - `130` - Script terminated by Ctrl+C

## Common Script Patterns

### Check if virtual environment is activated

```bash
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment not activated"
    echo "Run: source .venv/bin/activate"
    exit 1
fi
```

### Change to project root directory

```bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"
```

### Run with error handling

```bash
run_with_error_handling() {
    if ! "$@"; then
        log_error "Command failed: $*"
        exit 1
    fi
}

run_with_error_handling pytest
```

## Maintenance

### Regular Script Tasks

**Weekly:**
- Run `format_code.sh` before committing
- Update dependencies: `uv pip install -U -e ".[dev]"`
- Run full test suite: `run_tests.sh`

**Monthly:**
- Update pre-commit hooks: `pre-commit autoupdate`
- Review and update scripts for new workflows
- Check for security vulnerabilities: `pip-audit`

## See Also

- [Development Guide](DEVELOPMENT.md)
- [API Documentation](API.md)
- [Testing Guide](TESTING.md)
