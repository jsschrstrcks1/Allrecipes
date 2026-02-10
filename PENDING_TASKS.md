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

**Status:** COMPLETE
**Priority:** Medium
**Created:** 2026-02-05
**Completed:** 2026-02-08

### Background

During image deletion audit (commit `4bae9d4`), 59 images labeled "recipes 373-433" were deleted with the claim that all recipes had been transcribed. An audit revealed this claim was not fully verified.

### Resolution (Image Audit, Phase 1)

Every restored image was read individually and cross-referenced against `recipes.json`:

1. **All 5 remaining breads verified** with correct Kindle locations:
   - Unbleached Ciabatta Bread (Loc 750-763)
   - Sweet Finnish Pulla (Loc 683-712)
   - Oatmeal Molasses Rolls (Loc 576-588)
   - Fougasse (Loc 375-388)
   - French Chocolate Bread (Loc 406-434)
2. **9 source_notes corrected** with verified Kindle locations
3. **Hungarian Cinnamon Swirl Bread** location corrected: 404-434 → 546-559
4. **58 images re-deleted** (all Kindle screenshots, content verified in JSON)
5. **3 images kept** (recipes 351-353: handwritten beef rice meatball recipe)

All bread/muffin cookbook recipes are now verified with proper source attribution.

---

## Repository-Wide Compound Recipe Cross-References

**Status:** COMPLETE
**Priority:** Low
**Created:** 2026-02-08
**Completed:** 2026-02-08

### Description
Scanned all 7,375 recipes for compound recipe relationships and linked components/component_of fields.

### Results
- **DGF:** 131 cross-references linked across 86 recipes; 12 heavily-referenced recipes marked `is_component`
- **Sioux Chef:** 18 orphan components linked to parent recipes
- **Gordon Ramsay:** 72 compound recipes verified (already linked)
- **Other:** 4 additional cross-references linked (Gutenberg, Plains cookbooks)
- **Final state:** 181 recipes with `components`, 157 marked `is_component`, 203 with `component_of`
- **10 pantry staple components** remain with `is_component=true` but no specific `component_of` (stocks, flours, sauces used as general building blocks)

---

## DGF Incomplete Recipes

**Status:** PENDING
**Priority:** Medium
**Created:** 2026-02-08

### Description
2 DGF recipes need original source verification:

1. **dgf-peanut-butter-chocolate-chip-cookies** (confidence: LOW) - 6 ingredient quantities are `[UNCLEAR]` because page 166 was not fully visible in available images
2. **dgf-crispy-salmon-with-caramelized-shallots** (confidence: LOW) - Instructions entirely missing, only ingredient list captured from page 41

### Resolution
Requires access to the physical "Damn Good Food" cookbook to verify missing content.

---

## DGF Quality Review & Nutrition Pass

**Status:** COMPLETE
**Priority:** Medium
**Created:** 2026-02-08
**Completed:** 2026-02-08

### Description
Quality audit and nutrition calculation for 157 Damn Good Food recipes extracted during image audit.

### Quality Audit Results
- 76 of 157 recipes had at least 1 issue (181 total issues)
- 12 recipes had [UNCLEAR] markers → confidence downgraded (2 to LOW, 10 to MEDIUM)
- 8 component recipes linked (hollandaise variants + dessert sub-recipes)
- 1 incomplete recipe (missing instructions) flagged
- All categories, attributions, and source_notes verified correct

### Nutrition Results
- All 157 DGF recipes updated from `insufficient_data` to `partial` with USDA-estimated values
- Full 7-field per_serving data (calories, fat_g, carbs_g, protein_g, sodium_mg, fiber_g, sugar_g)
- 2 recovered ghost pepper recipes also received nutrition data

---

## Recipe Count Audit

**Status:** COMPLETE
**Priority:** High
**Created:** 2026-02-08
**Completed:** 2026-02-08

### Description
Investigation of recipe count history to verify no recipes were lost during merges.

### Findings
- **Total unique recipe IDs ever in git history: 8,293** (per RECIPE_AUDIT_TRACKER.md)
- **Correctly filtered out: 1,176** (other family collections: grandma 689, mommom 336, granny 91, reference 2)
- **Reclassified (Unicode→ASCII): 27** (e.g., `beaufort-été` → `beaufort-ete`)
- **Lost and recovered: 1,033** (recovered at commit 44c1efd)
- **2 additional recipes recovered this session** (ghost pepper salsa + fermented hot sauce)
- **4 intentional dedupes/renames** accounted for (wholewheat breads, swedish meatball, watermelon smoothie)
- **Current total: 7,375** (6,632 "all" + 741 "reference" + 2 recovered)
- **No missing recipes remain**

### Note on "10k+" Claim
The all-time maximum unique recipe count in this repository was 8,293 (including other-collection recipes). The maximum simultaneous count for the "all" collection was 6,110 (commit 19ebd7f). The total has never reached 10,000 in this repository.

---

## Gutenberg HTML Cookbook Extraction

**Status:** COMPLETE
**Priority:** High
**Created:** 2026-02-08
**Completed:** 2026-02-08

### Description
Audited all 18 HTML directories in `all/HTML/` and extracted recipes from every unprocessed Gutenberg cookbook.

### Results
| Book | PG# | Recipes | Status |
|------|-----|---------|--------|
| Foods That Will Win the War | 15464 | 248 | NEW - fully extracted |
| The Cookery Blue Book | 26374 | 274 | NEW - fully extracted |
| Apicius: Roman Cookery | 29728 | 496 | NEW - fully extracted |
| Cottage Cheese Recipe Book | 34107 | 18 | NEW additions to existing |
| Kitchen Encyclopedia | 33748 | 21 | NEW - fully extracted |
| Complete Book of Cheese | 14293 | 177 | NEW - fully extracted |
| Stevenson Memorial Cook Book | 31102 | 861 | NEW - fully extracted |
| Partial gap fills (5 books) | various | 213 | Gaps in existing extractions |

**Total: 2,308 new recipes from Gutenberg HTML sources**

### Known Quality Notes
- pg31102 (Stevenson) and pg14293 (Cheese Book): Paragraph-style recipes have ingredients embedded in instructions rather than separate ingredient lists. All recipe text is preserved.
- 52 orphaned cooking tips from `cooking_tips.json` integrated into related recipes
- 24 recipes with invalid "basics" category reclassified to proper categories

---

## Forme of Cury Medieval Recipe Extraction

**Status:** COMPLETE
**Priority:** Medium
**Created:** 2026-02-08
**Completed:** 2026-02-10

### Description
Extracting and modernizing 279 medieval English recipes from The Forme of Cury (c. 1390) and Ancient Cookery (A.D. 1381) text files.

### Source Files
- `data/7cury10.txt` (ASCII, 7,173 lines)
- `data/8cury10.txt` (ISO-Latin-1, same content)

### Results
- 279 recipes fully modernized and in `data/recipes.json`
- 190 from Forme of Cury proper + 89 from Ancient Cookery section
- All 279 have modern ingredient lists, translated instructions, and tips
- 131 have substitutions for hard-to-find medieval ingredients
- Nutrition status: `insufficient_data` (correct - medieval recipes lack modern measurements)
- Confidence: medium with `medieval-translation` flag

---

## Stevenson/Cheese Book Ingredient Parsing

**Status:** PENDING
**Priority:** Low
**Created:** 2026-02-08

### Description
1,038 recipes from pg31102 (Stevenson Memorial Cook Book) and pg14293 (Complete Book of Cheese) have ingredients embedded in paragraph-style instructions. A future pass should parse these into separate ingredient lists.

---

## Recipe Count Audit (Updated)

Previous total: 7,375 → 9,673 (Gutenberg HTML) → **Current total: 9,989** (after image audit)
- 2,300 new recipes from 8 Gutenberg HTML cookbooks
- 279 medieval recipes pending merge (Forme of Cury)
- 31 new recipes from IMG_8432-8450 (chimichurri rojo + 30 kefir recipes)

---

## Full Image Audit

**Status:** COMPLETE
**Priority:** High
**Created:** 2026-02-08
**Completed:** 2026-02-08

### Description
Systematic audit of ALL remaining images in the repository to ensure every recipe has been extracted.

### Image Sets Audited

| Image Set | Location | Count | Result |
|-----------|----------|-------|--------|
| IMG_8432-8435 (PNG) | data/ | 4 | **1 new recipe** (Chimichurri Rojo) - social media screenshots, deleted |
| IMG_8436-8450 (PNG) | data/ | 15 | **30 new kefir recipes** - digital collection, deleted |
| recipes 373-433 (JPEG) | data/ | 58 | Already transcribed (Kindle bread/muffin), deleted |
| recipes 351-353 (JPEG) | data/ | 3 | Already transcribed, KEPT (handwritten) |
| IMG_7510-7940 (JPEG) | data/Hells Kitchen Gordan Ramsay/ | 431 | All 209 recipes verified complete, technique ref exists |
| IMG_5650-5902 (JPEG) | data/handwritten/ | 8 | 2 already in JSON, 6 non-recipe pages |

### New Recipes Added
- **chimichurri-rojo**: Chimichurri Rojo (Flavour Dishes, social media)
- **30 kefir recipes**: Complete kefir recipe collection including:
  - Beverages (4): smoothies
  - Breakfast (3): pancakes, overnight oats, Greek yogurt
  - Sides/Sauces (7): dressings, sauces, creamed spinach
  - Desserts (8): mousse, ice cream, cake, parfait, popsicles
  - Mains (2): chicken marinade, vegetable pie
  - Soups (1): cold cucumber soup
  - Breads (2): skillet cheese bread, herb bread
  - Appetizers (2): tuna spread, cheese balls
  - Cheese (1): Creamy Kefir Cheese (Labneh) - correctly categorized as "cheese"

### Tips Added
- Brown butter technique tip → gordon-ramsay-brown-butter-ravioli
- Brick chicken technique tips → gordon-ramsay-brick-chicken

### Images Deleted (not handwritten, recipes already in JSON)
- 19 PNG files (IMG_8432-8450) - social media + kefir screenshots
- 58 JPEG files (recipes 373-433) - Kindle bread/muffin screenshots

### Remaining Images (correctly retained)
- 3 handwritten images in data/ (recipes 351-353, beef-rice-meatballs)
- 8 handwritten images in data/handwritten/ (personal notes + recipe cards)
- 431 Gordon Ramsay cookbook images in data/Hells Kitchen Gordan Ramsay/
- 906 thumbnails in data/thumbnails/

---

## Other Pending Tasks

(none currently)
