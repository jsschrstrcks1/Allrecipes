# Other Family Recipes - AI Assistant Context

> **Version 1.2** | Updated January 2026

## Quick Start Essentials

1. **Images are stored flat** in `data/` - no subdirectories for source files
2. **Never read images >2000px** directly - use `data/processed/` versions
3. **Never invent** recipe content - mark unclear items as `[UNCLEAR]`
4. **Always run validation** before committing: `python scripts/validate-recipes.py`
5. **Check PENDING_TASKS.md** for deferred work
6. **Cheese-making recipes MUST use `category: "cheese"`** - see Cheese-Making Recipes section

## Priority Framework

When making decisions, follow this hierarchy:

1. **Accuracy-First** - Never guess or invent content
2. **Preservation-First** - Keep all source references
3. **Fidelity-First** - Preserve original voice and intent
4. **Readability-First** - Normalize formatting for clarity

---

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

## Additional Documentation

For detailed workflows and configuration, see the `.claude/` directory:

| Document | Purpose |
|----------|---------|
| `.claude/ONBOARDING.md` | Quick start guide for new sessions |
| `.claude/MAINTENANCE.md` | Step-by-step maintenance workflows |
| `.claude/mcp-servers.md` | Optional MCP server integrations |
| `.claude/skill-rules.json` | Skill activation rules |
| `.claude/settings.json` | Permissions and hook configuration |

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
  "tips": ["Chef tips, technique notes"],
  "substitutions": [{"original": "", "substitute": "", "note": ""}],
  "tags": ["dessert", "holiday", "bread", "casserole"],
  "confidence": {
    "overall": "high|medium|low",
    "flags": []
  },
  "image_refs": ["IMG_001.PNG"],
  "page_continuation": {"continues_from": "", "continues_to": ""},
  "components": ["recipe-id-of-sub-recipe"],
  "component_of": ["recipe-id-of-parent"],
  "is_component": false,
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
├── CLAUDE.md                 # This file - primary AI context
├── PENDING_TASKS.md          # Deferred work tracking
├── README.md                 # Setup and hosting instructions
├── index.html                # Home page
├── recipe.html               # Recipe detail page
├── styles.css                # Stylesheet
├── script.js                 # Client-side rendering
├── .claude/                  # AI assistant configuration
│   ├── settings.json         # Permissions and hooks
│   ├── skill-rules.json      # Skill activation rules
│   ├── ONBOARDING.md         # Quick start guide
│   ├── MAINTENANCE.md        # Detailed workflows
│   ├── mcp-servers.md        # Optional MCP integrations
│   ├── hooks/                # Automation scripts
│   │   ├── post-write-validate.sh
│   │   └── image-safety-check.sh
│   └── skills/               # Skill definitions
│       ├── recipe-transcription/
│       └── recipe-validation/
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
6. **Never read oversized images** (>2000px) directly - use processed versions
7. **Always run validation** before committing recipe changes
8. **Check PENDING_TASKS.md** for deferred work at session start
9. **Cheese-making recipes MUST use `category: "cheese"`** - recipes that create cheese as output (contain rennet, cultures, citric acid+milk, or cheese-making processes) must be categorized as cheese so the Cheese Builder tool can find them

---

## Categories
- appetizers
- beverages
- breads
- breakfast
- **cheese** (cheese-MAKING recipes only - see below)
- desserts
- mains
- salads
- sides
- soups
- snacks

---

## Compound Recipes (Multi-Component Dishes)

Some cookbooks (especially professional ones like Gordon Ramsay's) contain **compound recipes** - dishes that include multiple sub-recipes (sauces, garnishes, components).

### Hybrid Approach

Use **BOTH** approaches simultaneously:

1. **Complete compound recipe** - The full dish with all sub-recipes inline
2. **Separate component recipes** - Each sub-recipe as its own searchable entry

### Example: Beef Wellington

```
gordon-ramsay-beef-wellington (COMPLETE)
├── Contains full inline instructions for ALL components
├── components: ["gordon-ramsay-duxelles", "gordon-ramsay-red-wine-jus"]
│
├──► gordon-ramsay-duxelles (STANDALONE)
│    component_of: ["gordon-ramsay-beef-wellington"]
│    is_component: true
│
└──► gordon-ramsay-red-wine-jus (STANDALONE)
     component_of: ["gordon-ramsay-beef-wellington"]
     is_component: true
```

### Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| `components` | array | IDs of sub-recipes extracted from this compound recipe |
| `component_of` | array | IDs of parent recipes this is a component of |
| `is_component` | boolean | True if this recipe is primarily used as a component |
| `tips` | array | Chef tips, technique notes from the cookbook |
| `substitutions` | array | `{original, substitute, note}` for suggested swaps |

### Multi-Page Recipes

For recipes spanning multiple images (5-6 photos):
- Store ALL image refs: `"image_refs": ["IMG_7510.jpeg", "IMG_7511.jpeg", ...]`
- Use `page_continuation` if splitting across entries
- Merge into single complete recipe when possible

---

## Cheese-Making Recipes (REQUIRED)

**MANDATORY:** When adding a recipe that MAKES cheese, you MUST set `"category": "cheese"`.

This ensures the Cheese Builder tool and other cheese-making utilities can find and suggest these recipes.

### What IS a Cheese-Making Recipe

A recipe belongs in the `cheese` category if it **creates cheese as the primary output**:

| Indicator | Examples |
|-----------|----------|
| **Contains rennet** | Animal, vegetable, or microbial rennet |
| **Uses cheese cultures** | Mesophilic, thermophilic, Flora Danica, etc. |
| **Has cheese-making additives** | Calcium chloride, lipase, annatto |
| **Uses cheese molds** | Penicillium candidum, P. roqueforti, Brevibacterium, Geotrichum |
| **Citric acid + milk pattern** | Quick cheeses like mozzarella, paneer, ricotta |
| **Cheese-making process phrases** | "cut the curd", "drain the whey", "press the cheese", "age the cheese" |

### What is NOT a Cheese-Making Recipe

Recipes that **use cheese as an ingredient** but don't make it belong in other categories:

| Category | Examples |
|----------|----------|
| **desserts** | Cheesecake, cheese danish, cheese frosting |
| **appetizers** | Fondue, cheese dip, fried cheese curds, cheese ball |
| **mains** | Mac and cheese, quesadillas, grilled cheese, pizza |
| **sides** | Cheese sauce, au gratin, cheese bread |
| **snacks** | Cheese crackers, cheese straws, nachos |

### Examples

```json
// ✅ CORRECT - This MAKES mozzarella
{
  "id": "30-minute-mozzarella",
  "title": "30-Minute Mozzarella",
  "category": "cheese",  // REQUIRED for cheese-making
  "ingredients": [
    {"item": "whole milk", "quantity": "1", "unit": "gallon"},
    {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
    {"item": "rennet", "quantity": "1/4", "unit": "tablet"}
  ]
}

// ✅ CORRECT - This USES mozzarella, doesn't make it
{
  "id": "caprese-salad",
  "title": "Caprese Salad",
  "category": "salads",  // NOT cheese - just uses it
  "ingredients": [
    {"item": "fresh mozzarella", "quantity": "8", "unit": "oz"},
    {"item": "tomatoes", "quantity": "2", "unit": "large"}
  ]
}
```

### Cheese-Making Tools

The repository includes specialized tools for cheese recipes:

| Tool | File | Purpose |
|------|------|---------|
| **Cheese Builder** | `cheese-builder.html` | Interactive wizard to find/customize cheese recipes |
| **Adulterant Companion** | `adulterant-companion.js` | Flavor additions (herbs, spices, washes) |
| **Milk Substitution** | `milk-substitution-tool.js` | Convert between milk types |

These tools search for `category: "cheese"` recipes. **If you don't categorize correctly, the recipe won't be found.**

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

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | Jan 2026 | Added cheese category requirement. Documented cheese-making recipe detection criteria. Added Cheese-Making Recipes section with examples and tool references. |
| 1.1 | Jan 2026 | Added .claude directory with settings, hooks, skills, and documentation. Added Quick Start Essentials and Priority Framework. Expanded Non-Negotiable Rules. |
| 1.0 | Original | Initial CLAUDE.md with recipe schema, OCR guidelines, and image processing documentation. |
