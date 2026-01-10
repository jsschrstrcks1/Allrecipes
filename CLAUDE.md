# Other Family Recipes - AI Assistant Context

## Project Mission & Values

This is a labor of love being performed by a Reformed Baptist family. Our ethos is **Soli Deo Gloria** (Glory to God Alone).

This repository contains **digital cookbook recipes and magazine clippings** that have been collected over the years. These are reference recipes used with permission.

**Accuracy is more important than speed.** There are hundreds of real people that will be impacted by these recipes. They matter deeply to this family.

---

## Repository Structure

This is a **standalone collection repository**, part of the multi-repo Family Recipe Archive:
- **MomsRecipes** (MomMom Baker) - Family heirloom recipes
- **GrandmasRecipes** (Grandma Baker) - Michigan to Florida recipes
- **GrannysRecipes** (Granny Hudson) - Additional family collection
- **Allrecipes** (THIS REPO) - Digital cookbook recipes & magazine clippings
- **FamilyRecipeHub** (aggregator)

---

## Pending Tasks

**IMPORTANT:** Check `PENDING_TASKS.md` for deferred work that needs to be completed in future sessions.

Current pending items:
- **Nutrition Data Pass** - Add nutrition information to all reference collection muffin recipes (see tracker for details)

---

## Recipe Collections

### Collection Configuration
```json
{
  "collections": {
    "all": {
      "id": "all",
      "display_name": "Other Family Recipes",
      "folder": "data/",
      "description": "Digital cookbook recipes and magazine clippings (used with permission)"
    }
  }
}
```

---

## Image Sources & Processing

### CRITICAL: Image Dimension Requirements

**API LIMIT**: Claude's API rejects images >2000px in any dimension.

This collection contains images from multiple sources:
- **Kindle screenshots** (PNG format, 1320x2868px - OVERSIZED!)
- **iPhone photos** (variable sizes, may be oversized)
- **Magazine scans** (JPEG format, variable sizes)

### Image Processing Workflow

**BEFORE reading ANY images, check the manifest:**
```bash
python scripts/image_safeguards.py status
```

**If images need processing:**
```bash
python scripts/process_images.py
python scripts/image_safeguards.py validate
```

### Safe Image Paths

| Source Type | Original Path | Safe Path for AI |
|-------------|---------------|------------------|
| Kindle screenshots | `data/*.PNG` | `data/processed/*.jpeg` |
| iPhone photos | `data/*.jpeg` | `data/processed/*.jpeg` (if oversized) |
| Magazine scans | `data/*.jpeg` | Direct (check dimensions first) |

**ALWAYS check dimensions before reading images directly!**
**ALWAYS use `data/processed/*.jpeg` for oversized images.**

---

## OCR Correction Guidelines

### Common OCR Errors to Watch For
- `l` ↔ `1` (lowercase L vs number one)
- `O` ↔ `0` (letter O vs zero)
- `rn` ↔ `m` (r-n combination vs letter m)
- `cl` ↔ `d` (c-l combination vs letter d)
- `tsp` vs `tbsp` (critical for measurements!)

### Measurement Standardization
| Original | Standardized |
|----------|-------------|
| teaspoon, t, t. | tsp |
| tablespoon, T, Tbsp, Tbs | tbsp |
| cup, c, C | cup |
| ounce, oz | oz |
| pound, lb, # | lb |

### Temperature Format
Prefer dual format for accessibility: `350°F (175°C)`

---

## OCR Pre-Processing Safeguards

### Source Classification
Identify the image type BEFORE attempting extraction:

| Source Type | Indicators | Action |
|-------------|------------|--------|
| **Kindle screenshots** | "Location X of Y", e-reader UI | Check copyright, verify source |
| **Magazine clippings** | Printed text, newspaper/magazine layout | Process normally |
| **Typed cards** | Typewriter font, consistent spacing | Process normally |
| **Cookbook pages** | Professional layout, copyright notices | **Verify permission** |

### Completeness Check (MANDATORY)
**DO NOT extract a recipe unless ALL THREE elements are present:**

1. **Title** - Recipe name clearly visible
2. **Ingredients** - At least partial ingredient list
3. **Instructions** - At least partial directions

If any element is missing, classify as a fragment and wait for adjacent images.

### Digital Screenshot Special Handling

For e-reader/Kindle screenshots (identified by "Location X of Y" footer):

1. **Sort by Kindle location number** before processing
2. **Check for commercial copyright** - All recipes must be used with permission
3. **Identify the source cookbook** - Record in `source_note`
4. **Map page boundaries** - Note which recipes span multiple screenshots

---

## Recipe Schema

```json
{
  "id": "stable-slug-like-recipe-name",
  "collection": "all",
  "collection_display": "Other Family Recipes",
  "title": "",
  "category": "desserts",
  "attribution": "",
  "source_note": "e.g., Kindle cookbook, magazine clipping",
  "description": "1-2 sentences",
  "servings_yield": "",
  "prep_time": "",
  "cook_time": "",
  "total_time": "",
  "ingredients": [
    {"item": "", "quantity": "", "unit": "", "prep_note": ""}
  ],
  "instructions": [
    {"step": 1, "text": ""}
  ],
  "temperature": "",
  "pan_size": "",
  "notes": [""],
  "tags": ["dessert", "holiday", "bread", "casserole"],
  "confidence": {
    "overall": "high|medium|low",
    "flags": []
  },
  "image_refs": ["IMG_001.PNG"],
  "page_continuation": {"continues_from": "", "continues_to": ""},
  "conversions": {
    "has_conversions": true,
    "conversion_assumptions": [],
    "ingredients_metric": [],
    "temperature_c": ""
  },
  "nutrition": {
    "status": "complete|partial|insufficient_data",
    "per_serving": {},
    "missing_inputs": [],
    "assumptions": []
  }
}
```

---

## Quality Checklist

- [ ] Cross-check ingredient quantities against instructions
- [ ] Flag implausible amounts (e.g., "4 cups salt" is probably an OCR error)
- [ ] Preserve original voice where possible
- [ ] Verify temperatures are reasonable (most baking: 300-425°F)
- [ ] Check that liquid-to-dry ratios make sense
- [ ] Ensure baking times align with temperatures and pan sizes

---

## Project Structure

```
Allrecipes/
├── CLAUDE.md                 # This file
├── README.md                 # Setup and hosting instructions
├── index.html                # Home page
├── recipe.html               # Recipe detail page
├── styles.css                # Stylesheet
├── script.js                 # Client-side rendering
├── data/
│   ├── *.jpeg               # Magazine scans
│   ├── *.PNG                # Kindle screenshots (OVERSIZED!)
│   ├── processed/           # AI-friendly versions (<=2000px)
│   │   └── *.jpeg
│   ├── recipes.json         # All recipes
│   ├── collections.json     # Collection metadata
│   ├── processed_images.json # Scan processing log
│   └── image_manifest.json  # Image validation status
├── scripts/
│   ├── validate-recipes.py  # Recipe validation
│   ├── process_images.py    # Image resizing for AI
│   ├── image_safeguards.py  # Broken image detection
│   └── optimize_images.py   # JPEG optimization
└── ebook/
    ├── book.html            # Print-optimized HTML
    └── print.css            # Print stylesheet
```

---

## Image Processing Scripts

### Resize Images for AI Processing
```bash
# Preview what will be processed
python scripts/process_images.py --dry-run

# Process all images
python scripts/process_images.py
```

### Image Safeguards
```bash
# Validate all images and create manifest
python scripts/image_safeguards.py validate

# Check current status
python scripts/image_safeguards.py status

# Get next unprocessed image
python scripts/image_safeguards.py next

# Mark an image as processed/skipped
python scripts/image_safeguards.py mark "IMG_4033.PNG" processed
python scripts/image_safeguards.py mark "IMG_4034.PNG" skipped "Not a recipe"
```

### Image Status Values
| Status | Meaning |
|--------|---------|
| `valid` | Ready to process |
| `oversized` | Valid but >2000px (use processed version) |
| `resized` | Processed version available |
| `broken` | Cannot read (skip) |
| `processed` | Recipe extraction complete |
| `skipped` | Not a recipe |

---

## Non-Negotiable Rules

1. **Do NOT invent** ingredients, steps, temperatures, times, or yields
2. If anything is **unreadable or ambiguous**, mark it as `[UNCLEAR]` with best guesses
3. **Preserve original intent**, but normalize spelling and formatting
4. **Verify copyright/permission** before processing commercial cookbook images
5. **Never discard a scan reference** - keep all image_refs

---

## Categories
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

## Validation

```bash
# Check JSON syntax and recipe schema
python scripts/validate-recipes.py

# Strict mode (fail on warnings)
python scripts/validate-recipes.py --strict
```

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
