# Other Family Recipes - AI Assistant Onboarding

*Soli Deo Gloria*

Welcome to the Other Family Recipes archive. This document will help you understand the project and get started quickly.

---

## Project Overview

This repository contains **digital cookbook recipes and magazine clippings** that have been collected over the years. These are reference recipes used with permission.

### Core Values

1. **Accuracy is more important than speed** - There are hundreds of real people who will use these recipes
2. **Soli Deo Gloria** - Glory to God Alone (Reformed Baptist family ethos)
3. **Preservation** - Digital cookbook recipes and magazine clippings deserve careful treatment

---

## Quick Start Checklist

Before you begin working:

- [ ] Read `CLAUDE.md` in the project root
- [ ] Check `PENDING_TASKS.md` for deferred work
- [ ] Run `python scripts/image_safeguards.py status` to understand image state
- [ ] Familiarize yourself with the recipe schema

---

## Critical Rules (Non-Negotiable)

1. **NEVER invent** ingredients, steps, temperatures, times, or yields
2. **NEVER read images >2000px** directly - use `data/processed/` versions
3. **ALWAYS mark unclear text** as `[UNCLEAR]` with best guess
4. **ALWAYS verify copyright** before processing cookbook images
5. **ALWAYS run validation** before committing recipe changes

---

## Image Processing (CRITICAL)

### API Limit Warning

Claude's API **rejects images >2000px** in any dimension. This collection includes:

| Source | Format | Typical Size | Action |
|--------|--------|--------------|--------|
| Kindle screenshots | PNG | 1320x2868 | **MUST process first** |
| iPhone photos | JPEG | Variable | Check dimensions |
| Magazine scans | JPEG | Variable | Usually OK |

### Safe Workflow

```bash
# 1. Check current status
python scripts/image_safeguards.py status

# 2. Process oversized images
python scripts/process_images.py

# 3. Validate
python scripts/image_safeguards.py validate

# 4. Use processed versions for oversized images
# GOOD: data/processed/IMG_4033.jpeg
# BAD:  data/IMG_4033.PNG (oversized!)
```

---

## Project Structure

```
Allrecipes/
├── CLAUDE.md              # Primary AI context (READ THIS)
├── PENDING_TASKS.md       # Deferred work tracking
├── data/
│   ├── recipes.json       # All recipes (main data file)
│   ├── *.jpeg, *.PNG      # Source images
│   └── processed/         # AI-safe resized images
├── scripts/
│   ├── validate-recipes.py    # Schema validation
│   ├── process_images.py      # Image resizing
│   └── image_safeguards.py    # Dimension checking
└── .claude/
    ├── MAINTENANCE.md     # Detailed workflows
    ├── ONBOARDING.md      # This file
    └── hooks/             # Automation scripts
```

---

## Recipe Schema Quick Reference

```json
{
  "id": "unique-slug",
  "collection": "all",
  "collection_display": "Other Family Recipes",
  "title": "Recipe Name",
  "category": "desserts",
  "source_note": "Kindle cookbook name / magazine source",
  "ingredients": [
    {"item": "flour", "quantity": "2", "unit": "cup", "prep_note": "sifted"}
  ],
  "instructions": [
    {"step": 1, "text": "Preheat oven to 350°F (175°C)."}
  ],
  "image_refs": ["IMG_XXXX.PNG"],
  "confidence": {
    "overall": "high|medium|low",
    "flags": []
  }
}
```

### Valid Categories

appetizers | beverages | breads | breakfast | desserts | mains | salads | sides | soups | snacks

---

## OCR Awareness

When transcribing, watch for common errors:

| Looks Like | Might Be | Context Clue |
|------------|----------|--------------|
| `l` | `1` | Numbers in quantities |
| `O` | `0` | Numbers in temperatures |
| `rn` | `m` | Words like "warm" |
| `cl` | `d` | Words like "could" |
| `tsp` | `tbsp` | **3x difference - verify!** |

---

## Measurement Standards

| Original | Standardize To |
|----------|---------------|
| teaspoon, t, t. | tsp |
| tablespoon, T, Tbsp | tbsp |
| cup, c, C | cup |
| ounce, oz | oz |
| pound, lb, # | lb |

---

## Family Repository Context

This is one of several family recipe repositories:

| Repo | Collection ID | Contents |
|------|---------------|----------|
| MomsRecipes | mom | MomMom Baker's recipes |
| GrandmasRecipes | grandma | Grandma Baker's recipes |
| GrannysRecipes | granny | Granny Hudson's recipes |
| **Allrecipes** | **all** | **This repo** - digital cookbooks |

---

## Getting Help

- **Workflows**: See `MAINTENANCE.md`
- **Schema details**: See `CLAUDE.md`
- **Pending work**: See `PENDING_TASKS.md`
- **Validation errors**: Run `python scripts/validate-recipes.py`

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
