#!/bin/bash
# Quick test script to convert a sample PDF

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

# Activate virtual environment
source .venv/bin/activate

# Check dependencies
echo "🔧 Checking dependencies..."
python scripts/convert_research_pdfs.py --check

# Test conversion
echo ""
echo "📄 Converting research PDFs..."
python scripts/convert_research_pdfs.py

echo ""
echo "✅ Conversion complete! Check research/*.md files"
