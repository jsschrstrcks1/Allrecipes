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
Used `scripts/add_all_nutrition.py` to calculate actual nutrition values from USDA data.

**Comprehensive updates to nutrition database:**
- Added cheesemaking ingredients: calcium chloride, rennet, starter cultures (zero cal)
- Added cheese salt with tbsp/lb/cup units
- Added exotic milk types: cow, goat, sheep, buffalo, camel, llama, rabbit
- Added gallon support for all milk types (16 cups = 1 gallon)
- Added Asian specialty ingredients: matcha, rice flour, nori, ikura, paneer
- Added Indian spices: kasuri methi, mahleb, mastic, ginger-garlic paste
- Added box/package variants for convenience mixes

### Results
| Before | After |
|--------|-------|
| 68.3% with nutrition | **99.5%** with nutrition |
| 3,521 insufficient | 29 insufficient |

- 5,790 of 5,819 recipes (99.5%) now have calculated per_serving values
- Only 29 recipes (0.5%) remain insufficient (OCR artifacts, ultra-specialty items)
- Validation passes with 0 errors, 0 warnings

---

## Other Pending Tasks

(none currently)
