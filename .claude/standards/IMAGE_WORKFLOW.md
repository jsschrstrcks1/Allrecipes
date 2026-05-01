# Image Workflow — Other Family Recipes

## API limit: 2000 px per image

Claude's API rejects images with any dimension > 2000 px.

This collection contains:

- **Kindle screenshots** (PNG, 1320 × 2868 px — OVERSIZED)
- **iPhone photos** (variable, may be oversized)
- **Magazine scans** (JPEG, variable)

## Before reading any images

```bash
python scripts/image_safeguards.py status
```

If processing is needed:

```bash
python scripts/process_images.py
python scripts/image_safeguards.py validate
```

## Safe Image Paths

| Source | Original | Safe path |
|---|---|---|
| Kindle screenshots | `data/*.PNG` | `data/processed/*.jpeg` |
| iPhone photos | `data/*.jpeg` | `data/processed/*.jpeg` (if oversized) |
| Magazine scans | `data/*.jpeg` | Direct (check dimensions first) |

Always check dimensions before reading directly. Always use
`data/processed/*.jpeg` for oversized images.

## Image Manifest Commands

```bash
# Validate all images and create manifest
python scripts/image_safeguards.py validate

# Current status
python scripts/image_safeguards.py status

# Get next unprocessed
python scripts/image_safeguards.py next

# Mark images
python scripts/image_safeguards.py mark "IMG_4033.PNG" processed
python scripts/image_safeguards.py mark "IMG_4034.PNG" skipped "Not a recipe"
```

## Status Values

| Status | Meaning |
|---|---|
| `valid` | Ready to process |
| `oversized` | Valid but >2000 px (use processed version) |
| `resized` | Processed version available |
| `broken` | Cannot read (skip) |
| `processed` | Recipe extraction complete |
| `skipped` | Not a recipe |
