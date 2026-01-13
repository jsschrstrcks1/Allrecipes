# Recipe Transcription Skill

## Purpose

Transcribe recipes from Kindle screenshots, magazine scans, and other digital sources into structured JSON format.

## Activation Triggers

- Working with files in `data/*.PNG`, `data/*.jpeg`, `data/processed/*.jpeg`
- Keywords: transcribe, OCR, extract, screenshot, kindle, magazine, scan

## Pre-Flight Checklist

Before transcribing any image:

1. [ ] Check image dimensions via `python scripts/image_safeguards.py status`
2. [ ] Use `data/processed/` version if image is oversized
3. [ ] For Kindle screenshots, verify copyright/permission
4. [ ] Identify source cookbook or publication

## Transcription Workflow

### Step 1: Image Assessment

```bash
python scripts/image_safeguards.py status
```

Determine image type:
- **Kindle screenshot**: Look for "Location X of Y" footer
- **Magazine scan**: Printed text, professional layout
- **Cookbook page**: Verify permission before processing

### Step 2: Completeness Check

**DO NOT transcribe unless ALL THREE elements are visible:**

1. Recipe title
2. At least partial ingredient list
3. At least partial instructions

If incomplete, note as fragment and wait for adjacent images.

### Step 3: Extract Information

Capture in order:
1. Title (exactly as shown)
2. Source attribution (cookbook name, magazine, etc.)
3. Yield/servings (if shown)
4. Prep/cook times (if shown)
5. Ingredients (quantity, unit, item, prep notes)
6. Instructions (numbered steps)
7. Tips, notes, variations
8. Temperature and pan size

### Step 4: Create JSON Entry

```json
{
  "id": "recipe-name-slug",
  "collection": "all",
  "collection_display": "Other Family Recipes",
  "title": "Recipe Name",
  "category": "category",
  "source_note": "Source cookbook or magazine",
  "ingredients": [
    {"item": "item", "quantity": "X", "unit": "cup", "prep_note": ""}
  ],
  "instructions": [
    {"step": 1, "text": "First instruction."}
  ],
  "image_refs": ["original_filename.PNG"],
  "confidence": {
    "overall": "high",
    "flags": []
  }
}
```

### Step 5: Validate

```bash
python scripts/validate-recipes.py
```

### Step 6: Mark Processed

```bash
python scripts/image_safeguards.py mark "IMG_XXXX.PNG" processed
```

## OCR Error Awareness

| Looks Like | Might Be | Check |
|------------|----------|-------|
| `l` | `1` | Quantities |
| `O` | `0` | Temperatures |
| `rn` | `m` | Word context |
| `tsp` | `tbsp` | **3x difference!** |

## Guardrails

### MUST

- Mark unclear text as `[UNCLEAR]`
- Preserve original measurements
- Verify copyright for cookbooks
- Use processed images for oversized files

### MUST NOT

- Invent or guess content
- Skip validation
- Delete source images
- Ignore dimension warnings

## Quality Standards

| Confidence | Meaning |
|------------|---------|
| `high` | Everything clear |
| `medium` | 1-3 unclear items (flagged) |
| `low` | Significant uncertainty |

---

*Accuracy is more important than speed.*
