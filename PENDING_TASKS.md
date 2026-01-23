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

**Status:** COMPLETE
**Priority:** Low
**Created:** 2026-01-15
**Completed:** 2026-01-15

### Description
20 entries were identified as non-recipe content (advertisements, addresses, OCR artifacts from scanned pages) and flagged with `flagged_for_review: true`.

### Resolution
- 12 non-recipe entries deleted (advertisements, addresses, corrupted data)
- 1 recipe repaired: "Dutch Oven Biscuits" (was incorrectly titled "Breads")
- 7 entries had been cleaned up in earlier sessions

### Actions Taken
1. Deleted from mains shard: published-forthebenefit-of-175choicer, when-youeatat-bensonwoma, douglas-bensonwoma, rodstrom-bensonwoma, dental-rooms-bensonwoma, someother-books-mybest250r, allplayer-music-oursisters, estimates-furnished-oursisters, thebestingroceries-andmeats-stevensonm, philadelphia-thealumnae, distributors-theeastmil, for-six-to-eight-fromscratc
2. Fixed breads-dutchovenc → dutch-oven-biscuits-dutchovenc (valid biscuit recipe with wrong title)

---

## Nutrition Status Warnings

**Status:** COMPLETE
**Priority:** Low
**Created:** 2026-01-23
**Completed:** 2026-01-23

### Description
22 recipes had nutrition data inconsistencies flagged by the validator:
- 21 recipes had `status: "complete"` but `per_serving` was empty
- 1 recipe had `status: "insufficient_data"` but `missing_inputs` was empty

### Resolution
Used `scripts/add_all_nutrition.py` to calculate actual nutrition values from USDA data:
- Ran nutrition calculation script on all recipes lacking complete nutrition
- 5,569 recipes processed with USDA-based calculations
- All 22 affected recipes now have calculated `per_serving` values
- Status set to "partial" where some ingredients couldn't be matched in USDA database

### Results
- All 22 recipes now have actual calorie, fat, carbs, protein, sodium, fiber, and sugar values
- Validation passes with 0 errors, 0 warnings
- Missing ingredient inputs are documented in each recipe's `missing_inputs` array

---

## Other Pending Tasks

(none currently)
