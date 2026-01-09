# Pending Tasks Tracker

This file tracks tasks that need to be completed in future sessions.

---

## Nutrition Data Pass

**Status:** PENDING
**Priority:** Medium
**Created:** 2026-01-09

### Description
All recipes extracted from the Kindle muffin cookbook (reference collection) need nutrition information added. The schema supports nutrition data but it was deferred during initial extraction to prioritize getting all recipes into JSON first.

### Scope
- All recipes with `"collection": "reference"` (muffin cookbook recipes)
- Approximately 50+ muffin recipes

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

## Other Pending Tasks

(none currently)
