#!/bin/bash
# Run validation in background with progress logging

cd /Users/wilsonm/development/m3dp-uip

echo "Starting validation at $(date)"
echo "Estimated completion: ~10 hours with 10 RPM rate limit"
echo "Progress will be saved to backend/reports/vision_validation_report.json"
echo ""

# Run in background, save output to log
nohup uv run python -m backend.scripts.validate_vision_model > validation_$(date +%Y%m%d_%H%M%S).log 2>&1 &

# Get the PID
PID=$!
echo "Validation running in background (PID: $PID)"
echo "Monitor progress with: tail -f validation_*.log"
echo "Or run: uv run python scripts/monitor_validation.py"
echo ""
echo "To stop: kill $PID"
