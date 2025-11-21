#!/bin/bash
# Setup automatic PDF to markdown conversion using fswatch (macOS)

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
RESEARCH_DIR="$PROJECT_ROOT/research"

echo "📚 Setting up PDF watch for $RESEARCH_DIR"

# Check if fswatch is installed (macOS)
if ! command -v fswatch &> /dev/null; then
    echo "Installing fswatch..."
    if command -v brew &> /dev/null; then
        brew install fswatch
    else
        echo "❌ Please install Homebrew first: https://brew.sh"
        exit 1
    fi
fi

# Check Python dependencies
echo "Checking Python dependencies..."
python3 -c "import pymupdf" 2>/dev/null || pip install pymupdf
python3 -c "import pypdf" 2>/dev/null || pip install pypdf

# Create launchd plist for automatic startup (macOS)
PLIST_FILE="$HOME/Library/LaunchAgents/com.minimal3dp.pdf-converter.plist"

cat > "$PLIST_FILE" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.minimal3dp.pdf-converter</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>fswatch -0 -e ".*" -i "\\.pdf$" "$RESEARCH_DIR" | xargs -0 -n 1 -I {} python3 "$SCRIPT_DIR/convert_research_pdfs.py" --file {}</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$HOME/Library/Logs/pdf-converter.log</string>

    <key>StandardErrorPath</key>
    <string>$HOME/Library/Logs/pdf-converter.error.log</string>
</dict>
</plist>
EOF

echo "✅ Created LaunchAgent plist at $PLIST_FILE"

# Load the service
launchctl unload "$PLIST_FILE" 2>/dev/null || true
launchctl load "$PLIST_FILE"

echo ""
echo "✨ PDF watch service installed and running!"
echo ""
echo "Commands:"
echo "  Stop:    launchctl unload $PLIST_FILE"
echo "  Start:   launchctl load $PLIST_FILE"
echo "  Logs:    tail -f ~/Library/Logs/pdf-converter.log"
echo ""
echo "Any PDF added to research/ will be automatically converted to markdown!"
