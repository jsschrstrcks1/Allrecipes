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
7. [Shardification & Indexing](#shardification--indexing)
8. [Milk Substitution Tool](#milk-substitution-tool)
9. [Adulterant Companion](#adulterant-companion)
10. [Error Resolution](#error-resolution)
11. [Cross-Repository Sync](#cross-repository-sync)

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

## Shardification & Indexing

After modifying `recipes.json`, rebuild derived data files:

### Rebuild Category Shards

Shards split recipes by category for faster loading:

```bash
python scripts/shardify_recipes.py
```

**Output files:**
- `data/recipes-index.json` - Master index with recipe summaries
- `data/recipes-{category}.json` - Full recipes by category

### Rebuild Ingredient Index

The ingredient index enables search-by-ingredient:

```bash
python scripts/build_ingredient_index.py
```

**Output:** `data/ingredient-index.json`

### When to Run

Run shardification and ingredient indexing after:
- Adding new recipes
- Removing duplicate recipes
- Bulk recipe updates
- Category changes

### Dry Run Mode

Preview changes without writing files:

```bash
python scripts/shardify_recipes.py --dry-run
python scripts/build_ingredient_index.py --dry-run
```

---

## Milk Substitution Tool

The Milk Substitution Tool (`milk-substitution.js`) allows users to switch between milk types (cow, goat, sheep) for cheese recipes.

### Files

| File | Purpose |
|------|---------|
| `milk-substitution.js` | Core JavaScript module |
| `data/milk-substitution.json` | Milk type data (fat%, protein%, yield factors) |
| `.claude/CHEESE-RECIPE-GUIDELINES.md` | Recipe detection criteria |
| `.claude/AGGREGATOR-INTEGRATION-PROMPT.md` | Integration guide for FamilyRecipeHub |

### Testing

Verify tool appears on cheese recipes:

1. Open a cheese recipe in browser
2. Check console for "Milk substitution data loaded"
3. Milk switcher panel should appear
4. Test switching milk types and verify ingredient adjustments

### Adding New Milk Types

To add an exotic milk type:

1. Edit `data/milk-substitution.json`
2. Add entry to `milk_types` with all required fields
3. Update `exotic_milks` section if applicable
4. Test detection and substitution

### Maintenance Checklist

- [ ] Verify `milk-substitution.json` is valid JSON
- [ ] Test each milk type produces correct adjustments
- [ ] Confirm detection works for cheese recipes
- [ ] Check responsive design on mobile

---

## Adulterant Companion

The Adulterant Companion (`adulterant-companion.js`) provides herb, spice, and adulterant guidance for cheese recipes.

### Files

| File | Purpose |
|------|---------|
| `adulterant-companion.js` | Core JavaScript module |
| `data/adulterants.json` | Adulterant database (156 entries) |
| `.claude/ADULTERANT-COMPANION-GUIDELINES.md` | Complete documentation |
| `styles.css` | Adulterant panel styles |

### Data Structure

Each adulterant in `data/adulterants.json` includes:
- Category and subcategory
- Flavor profile and intensity
- Compatible/incompatible cheese styles
- Addition stages (when to add)
- Base quantities and milk-type adjustments
- Maximum safe quantities and warnings
- Injection templates for recipe integration

### Adding New Adulterants

1. Edit `data/adulterants.json`
2. Add entry following existing schema:
   ```json
   {
     "id": "new-adulterant",
     "name": "New Adulterant Name",
     "category": "spice",
     "forms": ["powder"],
     "flavor_profile": ["EARTHY", "WARM"],
     "intensity": "M2",
     "compatible_styles": ["semi-soft", "hard"],
     "incompatible_styles": ["fresh", "bloomy"],
     "best_stages": ["CURD_MILL"],
     "allowed_stages": ["CURD_MILL", "RIND_RUB"],
     "base_quantity": {"amount": 0.5, "unit": "tsp", "per": "gallon"},
     "milk_adjustments": {"cow": 1.0, "goat": 0.9, "sheep": 1.4},
     "max_safe_quantity": {"amount": 1.5, "unit": "tsp", "per": "gallon"},
     "warnings": {
       "exceeded_message": "Warning message when exceeded"
     },
     "injection_templates": {
       "CURD_MILL": "Add {quantity} {name} to curds."
     }
   }
   ```
3. Update `meta.total_adulterants` count
4. Test in browser

### Prohibited Adulterants

When adding to `prohibited_adulterants` section:
- Include clear reason for prohibition
- Suggest safe alternative if available

### Integration with Milk Substitution

The Adulterant Companion automatically:
- Listens for `milkSubstitutionChanged` events
- Adjusts quantities when milk type changes
- Uses milk-type multipliers from each adulterant's `milk_adjustments`

### Maintenance Checklist

- [ ] Verify `adulterants.json` is valid JSON
- [ ] Check `meta.total_adulterants` matches actual count
- [ ] Test category filtering for each cheese style
- [ ] Verify warnings display correctly
- [ ] Test injection step generation
- [ ] Confirm responsive design on mobile

---

## Cheese Recipe Builder

The Cheese Recipe Builder (`cheese-builder.js`) is an interactive wizard for creating custom cheese recipes.

### Files

| File | Purpose |
|------|---------|
| `cheese-builder.js` | Core JavaScript module |
| `cheese-builder.html` | Wizard page |
| `data/cheese-templates.json` | Styles, flavors, base recipes |
| `.claude/CHEESE-BUILDER-GUIDELINES.md` | Complete documentation |

### Wizard Flow

1. **Milk Selection** - Type, quantity, processing
2. **Style Selection** - Fresh, soft, semi-hard, hard, etc.
3. **Flavor Profile** - Herbed, spicy, smoky, etc.
4. **Adulterant Selection** - Herbs, spices, peppers
5. **Review** - Summary and recipe matching
6. **Recipe** - Generated recipe with all adjustments

### Adding Base Recipes

To add a new base cheese recipe:

1. Edit `data/cheese-templates.json`
2. Add entry to `base_recipes` section
3. Include `adulterant_injection_point` for step insertion
4. Test in browser

### Adding Cheese Styles

1. Edit `data/cheese-templates.json`
2. Add entry to `cheese_styles` section
3. Define `best_milk_types`, `adulterant_timing`, `suggested_adulterants`

### Adding Flavor Profiles

1. Edit `data/cheese-templates.json`
2. Add entry to `flavor_profiles` section
3. Define `compatible_styles` and `suggested_adulterants`

### Maintenance Checklist

- [ ] Verify `cheese-templates.json` is valid JSON
- [ ] Test wizard navigation through all steps
- [ ] Verify milk type selection updates recommendations
- [ ] Test recipe generation produces valid output
- [ ] Check print layout renders correctly
- [ ] Verify responsive design on mobile

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
- basics
- beverages
- breads
- breakfast
- cheese
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
