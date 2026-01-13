#!/bin/bash
# Pre-read safety check for image files
# Prevents reading oversized images that could fail API limits

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Check if attempting to read an image file
if [[ "$CLAUDE_FILE_PATH" == *.PNG ]] || [[ "$CLAUDE_FILE_PATH" == *.jpeg ]] || [[ "$CLAUDE_FILE_PATH" == *.jpg ]]; then
    # Skip if already in processed directory
    if [[ "$CLAUDE_FILE_PATH" == *"/processed/"* ]]; then
        exit 0
    fi

    # Check if manifest exists
    MANIFEST="$PROJECT_DIR/data/image_manifest.json"
    if [[ -f "$MANIFEST" ]]; then
        FILENAME=$(basename "$CLAUDE_FILE_PATH")

        # Check if image is marked as oversized
        if grep -q "\"$FILENAME\".*\"oversized\"" "$MANIFEST" 2>/dev/null; then
            echo "WARNING: Image $FILENAME is oversized (>2000px)."
            echo "Use data/processed/ version instead."
            echo "Run: python scripts/image_safeguards.py status"
        fi
    else
        echo "WARNING: Image manifest not found. Run: python scripts/image_safeguards.py validate"
    fi
fi

exit 0
