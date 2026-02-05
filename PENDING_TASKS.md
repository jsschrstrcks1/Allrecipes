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

## Non-Handwritten Image Refs Cleanup

**Status:** COMPLETE
**Priority:** Medium
**Created:** 2026-02-05
**Completed:** 2026-02-05

### Description
Policy change: only handwritten recipe images should be saved and linked via `image_refs`. Non-handwritten sources (Kindle screenshots, magazine scans, typed cards, cookbook pages) should have empty `image_refs` arrays since the extracted recipe data fully represents the content.

### Resolution
- Removed `image_refs` from all non-handwritten recipes (commit `b9c9543`)
- Updated CLAUDE.md (v1.3) with Image Retention Policy section
- Updated Source Classification table with "Keep Image?" column
- Updated Non-Negotiable Rule 5 to reflect handwritten-only policy
- Updated ONBOARDING.md critical rules and schema reference
- Updated MAINTENANCE.md "Adding New Recipes" workflow

### Policy (ongoing)
- **Handwritten images**: Keep in `data/`, populate `image_refs` with filename(s)
- **Non-handwritten images**: Extract recipe data, leave `image_refs` as `[]`

---

## Kindle Bread Cookbook Source Reconciliation

**Status:** IN PROGRESS
**Priority:** Medium
**Created:** 2026-02-05
**Updated:** 2026-02-05

### Background

During image deletion audit (commit `4bae9d4`), 59 images labeled "recipes 373-433" were deleted with the claim that all recipes had been transcribed. An audit revealed this claim was not fully verified.

### Progress

**Completed:**
- [x] Merged duplicate entries: Wholewheat Honey Bread (2→1), Wholewheat Maple Bread (2→1)
- [x] Updated 8 recipes with verified Kindle location numbers

**Recipes now with proper "Kindle bread cookbook" attribution (17 total):**
- Original 9: Amish White Bread (100-113), Artichoke Pine Nut Bread (123-149), Braided Sesame Bread (157-169), Butter & Molasses Bread (187-199), Butternut Squash Bread (214-226), Buttery White Bread (237-250), Candied Hoska (262-290), Parmesan & Mozzarella Focaccia (636-650), Simple Artisan Bread (663-674)
- Added: Cinnamon Raisin Bread (347-360), Hungarian Cinnamon Swirl Bread (404-434), Gruyère Pepper & Onion Bread (483-496), Panettone (608-620), Unbleached Baguettes (717-743), Wholegrain Seed Bread (782-795), Wholewheat Honey Bread (809-821), Wholewheat Maple Bread (836-849)

**Remaining with "Digital cookbook (Kindle)" source (8 breads):**
- Unbleached Ciabatta Bread, Sweet Finnish Pulla, Oatmeal Molasses Rolls
- Honey Oatmeal Bread, Garlic Artisan Bread, Fougasse
- French Chocolate Bread, Chocolate Cinnamon Babka

These 8 may or may not be from the same bread cookbook - need additional image scanning to verify.

### Images Restored

58 bread/muffin cookbook images restored from git history for verification:
- Images 373-424: Kindle bread cookbook (944 locations), covering ~locations 187-849
- Images 425-433: Kindle MUFFIN cookbook (6172 locations) - different book!

### Remaining Actions

1. ~~Merge duplicate recipes~~ DONE
2. ~~Standardize source attribution~~ PARTIALLY DONE (17 of ~25 bread recipes)
3. **Verify completeness** - Cross-check extracted recipes against image content
4. **Re-delete images** - After verification, images can be safely deleted per non-handwritten policy

---

## Other Pending Tasks

(none currently)
