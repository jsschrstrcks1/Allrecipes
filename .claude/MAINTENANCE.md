# Other Family Recipes - Maintenance Guide

*Soli Deo Gloria*

This document provides step-by-step workflows for maintaining the Other Family Recipes archive.

---

## Table of Contents

1. [Adding New Recipes](#adding-new-recipes)
2. [Processing Images](#processing-images)
3. [Transcribing from Kindle Screenshots](#transcribing-from-kindle-screenshots)
4. [Transcribing Magazine Scans](#transcribing-magazine-scans)
5. [Updating Existing Recipes](#updating-existing-recipes)
6. [Pre-Deployment Validation](#pre-deployment-validation)
7. [Error Resolution](#error-resolution)
8. [Cross-Repository Sync](#cross-repository-sync)

---

## Adding New Recipes

### Step 1: Prepare the Image

1. Add image to `data/` directory
2. Check dimensions:
   ```bash
   python scripts/image_safeguards.py status
   ```
3. If oversized (>2000px), process it:
   ```bash
   python scripts/process_images.py
   ```

### Step 2: Transcribe the Recipe

1. Read the processed image (use `data/processed/` for oversized images)
2. Extract all visible information:
   - Title
   - Ingredients (with quantities and units)
   - Instructions (numbered steps)
   - Any notes, tips, or source information

3. Create JSON entry following the schema:
   ```json
   {
     "id": "recipe-name-slug",
     "collection": "all",
     "collection_display": "Other Family Recipes",
     "title": "Recipe Name",
     "category": "desserts",
     "source_note": "Source cookbook or magazine",
     "ingredients": [...],
     "instructions": [...],
     "image_refs": ["filename.jpeg"],
     "confidence": {
       "overall": "high",
       "flags": []
     }
   }
   ```

### Step 3: Validate and Commit

```bash
python scripts/validate-recipes.py
git add data/recipes.json data/IMAGE_FILE
git commit -m "Add [recipe name] from [source]"
```

---

## Processing Images

### Check Current Status

```bash
python scripts/image_safeguards.py status
```

### Process All Oversized Images

```bash
python scripts/process_images.py
```

### Validate After Processing

```bash
python scripts/image_safeguards.py validate
```

### Image Status Values

| Status | Meaning | Action |
|--------|---------|--------|
| `valid` | Ready to read | Use directly |
| `oversized` | >2000px | Use `data/processed/` version |
| `resized` | Processed available | Use processed version |
| `broken` | Cannot read | Skip or fix |
| `processed` | Recipe extracted | No action needed |
| `skipped` | Not a recipe | No action needed |

---

## Transcribing from Kindle Screenshots

### Special Considerations

1. **Sort by location number** - Kindle shows "Location X of Y"
2. **Verify copyright** - All recipes must be used with permission
3. **Identify source cookbook** - Record in `source_note` field
4. **Check for page spans** - Recipes may span multiple screenshots

### Workflow

1. List all Kindle screenshots:
   ```bash
   ls data/*.PNG | sort
   ```

2. Check manifest for processing status:
   ```bash
   python scripts/image_safeguards.py status
   ```

3. Process oversized images first:
   ```bash
   python scripts/process_images.py
   ```

4. Transcribe in location order, noting page continuations

5. Mark processed:
   ```bash
   python scripts/image_safeguards.py mark "IMG_XXXX.PNG" processed
   ```

---

## Transcribing Magazine Scans

### Identification

Magazine scans typically have:
- Printed text (not handwritten)
- Professional layout
- Publication name visible
- Multiple columns

### Workflow

1. Check dimensions and process if needed
2. Identify the publication for attribution
3. Extract recipe including any tip boxes or sidebars
4. Note any nutritional information present
5. Validate and commit

---

## Updating Existing Recipes

### Making Corrections

1. Read the current entry from `data/recipes.json`
2. Make targeted edits using the Edit tool
3. Run validation:
   ```bash
   python scripts/validate-recipes.py
   ```
4. Commit with descriptive message

### Adding Nutrition Data

Follow the pattern in `PENDING_TASKS.md` for nutrition calculations:
- Use USDA standard values
- Document assumptions
- Set `nutrition.status` appropriately

---

## Pre-Deployment Validation

**Required before every deployment:**

```bash
# Validate recipe schema and data
python scripts/validate-recipes.py

# Check image status
python scripts/image_safeguards.py status

# Verify no broken images
python scripts/image_safeguards.py validate
```

### Strict Mode

For production deployments, use strict mode:

```bash
python scripts/validate-recipes.py --strict
```

---

## Error Resolution

### Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Missing required field | Schema violation | Add the missing field |
| Invalid category | Typo or wrong value | Use valid category from list |
| Duplicate ID | Two recipes same ID | Make IDs unique |
| Invalid JSON | Syntax error | Check brackets/commas |

### OCR Corrections

| Common Error | Should Be |
|--------------|-----------|
| `l` (lowercase L) | `1` (number one) |
| `O` (letter) | `0` (zero) |
| `rn` | `m` |
| `cl` | `d` |
| `tsp` | `tbsp` (verify context!) |

**Critical:** `tbsp` vs `tsp` = 3x difference!

---

## Cross-Repository Sync

This repository is part of the Family Recipe Archive:

| Repository | Collection | Purpose |
|------------|------------|---------|
| MomsRecipes | mom | MomMom Baker's recipes |
| GrandmasRecipes | grandma | Grandma Baker's recipes |
| GrannysRecipes | granny | Granny Hudson's recipes |
| **Allrecipes** | **all** | **Digital cookbooks & magazines** |
| FamilyRecipeHub | (aggregator) | Combined family archive |

### Sync Protocol

1. Each repository maintains its own `recipes.json`
2. FamilyRecipeHub aggregates via scheduled workflow
3. Schema must remain consistent across all repos
4. Changes to schema require coordination

---

## Valid Categories

- appetizers
- beverages
- breads
- breakfast
- desserts
- mains
- salads
- sides
- soups
- snacks

---

## Confidence Ratings

| Rating | Meaning |
|--------|---------|
| `high` | Completely clear, no ambiguity |
| `medium` | 1-3 unclear words, noted in flags |
| `low` | Significant portions unclear |

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
