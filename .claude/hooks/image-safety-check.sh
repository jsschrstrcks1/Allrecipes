#!/bin/bash
# Image Safety Check Hook for Allrecipes Aggregator
# Warns before reading potentially oversized images

FILE_PATH="${CLAUDE_FILE_PATH:-$1}"

if [[ "$FILE_PATH" == *.jpeg ]] || [[ "$FILE_PATH" == *.jpg ]] || [[ "$FILE_PATH" == *.png ]]; then
    if [[ "$FILE_PATH" == *"/processed/"* ]]; then
        exit 0
    fi
    if [[ "$FILE_PATH" == *"/data/"* ]]; then
        echo "WARNING: Image may exceed 2000px limit. Check for processed version first."
    fi
fi
exit 0
