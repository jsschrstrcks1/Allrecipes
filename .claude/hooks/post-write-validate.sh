#!/bin/bash
# Post-write validation hook for recipe files
# Automatically validates recipes.json after modifications

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Check if the modified file is a recipe file
if [[ "$CLAUDE_FILE_PATH" == *"recipes.json"* ]] || [[ "$CLAUDE_FILE_PATH" == *"data/"*".json"* ]]; then
    cd "$PROJECT_DIR"

    # Run validation and filter to show only errors
    python scripts/validate-recipes.py 2>&1 | grep -E "(ERROR|FAIL|Invalid)" || true
fi
