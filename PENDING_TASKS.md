# Pending Tasks Tracker

This file tracks tasks that need to be completed in future sessions.

---

## Nutrition Data Pass

**Status:** COMPLETE
**Priority:** Medium
**Created:** 2026-01-09
**Completed:** 2026-01-10

### Description
All recipes extracted from the Kindle muffin cookbook (reference collection) need nutrition information added. The schema supports nutrition data but it was deferred during initial extraction to prioritize getting all recipes into JSON first.

### Resolution
- Created `scripts/add_muffin_nutrition.py` with USDA standard nutrition values for ~200 baking ingredients
- 90 of 91 muffin recipes now have complete nutrition status (99%)
- 1 recipe (Au Gratin Potato Muffins) has partial status - only missing "to taste salt and pepper" which has negligible caloric impact

### Scope
- All recipes with `"collection": "reference"` (muffin cookbook recipes)
- 91 muffin recipes total

### Required Fields
```json
"nutrition": {
  "status": "complete|partial|insufficient_data",
  "per_serving": {
    "calories": null,
    "fat_g": null,
    "carbs_g": null,
    "protein_g": null,
    "sodium_mg": null,
    "fiber_g": null,
    "sugar_g": null
  },
  "missing_inputs": [],
  "assumptions": []
}
```

### Approach
1. Use standard nutrition databases (USDA) for ingredient values
2. Calculate per-serving values based on `servings_yield` (typically 12 muffins)
3. Document assumptions in the `assumptions` array
4. Mark `status` as "partial" if any values are estimated

### Affected Recipe IDs (reference collection muffins)
- All recipes added from IMG_4058 onwards in the reference collection
- Run query: `jq '.recipes[] | select(.collection=="reference" and (.tags | contains(["muffins"])))' recipes_master.json`

---

## Flagged Non-Recipe Content

**Status:** NEEDS REVIEW
**Priority:** Low
**Created:** 2026-01-15

### Description
15 entries were identified as non-recipe content (advertisements, addresses, OCR artifacts from scanned pages) and have been flagged with `flagged_for_review: true`. These should be reviewed and either:
- Deleted entirely if they're truly not recipes
- Unflagged and repaired if they contain valid recipe content that was misidentified

### Flagged Entries
| ID | Title | Reason |
|----|-------|--------|
| published-forthebenefit-of-175choicer | Published Forthebenefit Of | Advertisement |
| when-youeatat-bensonwoma | When Youeatat | Restaurant ad |
| douglas-bensonwoma | Douglas | Address fragment |
| rodstrom-bensonwoma | Rodstrom | Address fragment |
| dental-rooms-bensonwoma | Dental Rooms | Advertisement |
| someother-books-mybest250r | Someother Books | Book advertisement |
| allplayer-music-oursisters | Allplayer Music | Advertisement |
| estimates-furnished-oursisters | Estimates Furnished | Business ad |
| thebestingroceries-andmeats-stevensonm | Thebestingroceries Andmeats | Grocery store ad |
| philadelphia-thealumnae | Philadelphia | Address fragment |
| distributors-theeastmil | Distributors | Business listing |
| florists-theeastmil | Florists | Business listing |
| general-offices-thenewengl | General Offices | Business listing |
| perpound-elementsof | Perpound | OCR garbage/advertisement |
| breads-dutchovenc | Breads | Corrupted multi-ingredient lines |

### How to Review
```bash
# Find all flagged entries
python3 -c "
import json
for shard in ['mains', 'desserts', 'breads', 'breakfast', 'appetizers', 'sides', 'soups', 'salads', 'beverages']:
    with open(f'data/recipes-{shard}.json') as f:
        data = json.load(f)
    for r in data.get('recipes', []):
        if r.get('flagged_for_review'):
            print(f\"{shard}: {r.get('title')} ({r.get('id')})\")"
```

---

## Other Pending Tasks

(none currently)
