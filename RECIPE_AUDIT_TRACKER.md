# Recipe Audit Tracker

> Full history audit of `data/recipes.json` from first commit to present.
> Generated: 2026-02-05

---

## Summary

| Metric | Count |
|--------|-------|
| Commits that touched `recipes.json` | 112 |
| First commit analyzed | `b60d457` (PR #34 merge) |
| Current commit | `08f83bf` (Image audit) |
| Peak unique recipe count | 6,110 (at commit `19ebd7f`) |
| Current unique recipe count | 6,057 |
| Total unique IDs ever seen | 8,293 |
| IDs no longer present | 2,236 |
| Correctly removed (other collections, junk) | 1,176 |
| Reclassified (Unicode → ASCII duplicates) | 27 |
| **Lost recipes needing recovery** | **1,033** |

---

## How Recipes Were Lost

There were **three root causes** for recipe loss in this repository:

### 1. Branch Merge Conflicts Taking Stale Data

The most damaging pattern. When a feature branch forked from an older commit and later merged back, GitHub's merge resolution sometimes took the **branch's older, smaller `recipes.json`** over main's newer, larger version. This silently dropped hundreds of recipes with no merge conflict warning because both versions were valid JSON.

**Affected merges:**
- **PR #58** (`d617443`): Dropped 1,870 unique IDs. Branch had been based on a pre-filter version.
- **PR #75** (`b4eb6f9`): Dropped 625 unique IDs. Branch missed the cheese variety additions (traditional-\*, artisan-\*, etc.).
- Multiple smaller oscillation events between commits #9-#15 where filtered (3,607 recipes) and unfiltered (5,400+ recipes) versions alternated.

### 2. Filter Oscillation (Commits #9-#15)

During the transition to a standalone collection, `recipes.json` oscillated between a filtered version (~3,607 recipes, `collection: "all"` only) and an unfiltered version (~5,400 recipes, all collections). Different branches had different versions, and merges bounced back and forth. Most recipes caught in this oscillation were eventually restored, but **some fell through the cracks** when the final filtered version was established at PR #58.

### 3. Intentional Removals (Correctly Done)

Some removals were correct:
- **1,118 recipes** from other collections (grandma, mommom, granny, reference) correctly filtered out
- **58 non-recipe entries** (OCR artifacts, ads, addresses, cookbook metadata) correctly cleaned up
- **12 Argentine cheese recipes** reverted then re-added later under different IDs

---

## Commit-by-Commit History

Every commit that touched `recipes.json`, with recipe count and changes.

`+N` = unique IDs added, `-N` = unique IDs removed, `net` = change in unique count.

Commits marked with `***` had removals.

| # | Commit | Unique | +Add | -Rem | Net | Message |
|---|--------|--------|------|------|-----|---------|
| 0 | `b60d457` | 5,189 | -- | -- | -- | Merge pull request #34 |
| 1 | `0a9d50b` | ERROR | -- | -- | -- | Delete 152 magazine recipe images |
| 2 | `055c543` | 5,277 | +88 | -0 | +88 | Add Chile Bible and Cooking With The Ancients recipes |
| 3 | `fd203e5` | 5,266 | +77 | -88 | -11 | Add 20 more CPM recipes (batch 5) *** |
| 4 | `859317d` | 5,281 | +15 | -0 | +15 | Add 17 more CPM recipes (batch 6) |
| 5 | `5de8258` | 5,293 | +12 | -0 | +12 | Add 13 more CPM recipes (batch 7) |
| 6 | `81b31f6` | 5,302 | +9 | -0 | +9 | Add 12 more CPM recipes (batch 8) |
| 7 | `906d1f0` | 5,313 | +11 | -0 | +11 | Add 14 more CPM recipes (batch 9) |
| 8 | `c99dd7b` | 5,323 | +10 | -0 | +10 | Add 13 more CPM recipes (batch 10) |
| 9 | `60bf530` | 3,607 | +88 | -1,804 | -1,716 | Filter recipes.json to standalone collection *** |
| 10 | `ab48290` | 5,329 | +1,810 | -88 | +1,722 | Add 6 Pepper Powered recipes *** |
| 11 | `d0e063a` | 3,607 | +88 | -1,810 | -1,722 | Expand nutrition database *** |
| 12 | `8ee0fb6` | 5,343 | +1,824 | -88 | +1,736 | Add 16 recipes from multiple sources *** |
| 13 | `5f8ec7c` | 3,607 | +88 | -1,824 | -1,736 | Add equipment filter *** |
| 14 | `12f070a` | 5,447 | +1,840 | -0 | +1,840 | Add 16 Cuso Cuts recipes |
| 15 | `d617443` | 3,577 | +0 | -1,870 | -1,870 | Merge pull request #58 *** |
| 16 | `4bb0765` | 3,550 | +2 | -29 | -27 | Add Bull's Eye BBQ Sauce copycat *** |
| 17 | `4c8e23c` | 3,550 | +0 | -0 | 0 | Restore 754 carelessly deleted recipe images |
| 18 | `e1c65f4` | 3,619 | +69 | -0 | +69 | Add 3 sheep's milk cream cheese recipes |
| 19 | `27ccc95` | 3,651 | +32 | -0 | +32 | Add sheep milk cheese recipes collection |
| 20 | `e2d18de` | 3,661 | +10 | -0 | +10 | Add more sheep milk cheese recipes |
| 21 | `d746d20` | 3,673 | +12 | -0 | +12 | Add 12 Argentine cheese recipes |
| 22 | `58baa6b` | 3,661 | +0 | -12 | -12 | Revert "Add 12 Argentine cheeses" *** |
| 23 | `c570e09` | 3,705 | +44 | -0 | +44 | Add 22 cheesemaking recipes |
| 24 | `8de8880` | 3,759 | +54 | -0 | +54 | Add 54 cheesemaking recipes |
| 25 | `a86f48d` | 3,791 | +32 | -0 | +32 | Add 34 more world cheesemaking recipes |
| 26 | `672ae29` | 3,820 | +29 | -0 | +29 | Add 29 more regional cheesemaking recipes |
| 27 | `640ffee` | 3,832 | +12 | -0 | +12 | Add 12 Argentine cheese recipes |
| 28 | `5eddbe4` | 3,936 | +275 | -171 | +104 | Add 8 Middle Eastern cheeses *** |
| 29 | `5dbc14d` | 3,944 | +8 | -0 | +8 | Add 8 Italian regional cheeses |
| 30 | `d03fa60` | 3,952 | +8 | -0 | +8 | Add 8 Portuguese/Latin American cheeses |
| 31 | `e952941` | 3,960 | +8 | -0 | +8 | Add 8 Eastern European/ancient cheeses |
| 32 | `7ee54c4` | 3,968 | +8 | -0 | +8 | Add 8 Mediterranean/Nordic cheeses |
| 33 | `5bf1759` | 3,834 | +173 | -307 | -134 | Fix duplicate recipe IDs *** |
| 34 | `f093dfe` | 3,976 | +315 | -173 | +142 | Add 8 global ancient cheeses *** |
| 35 | `f153d7e` | 4,149 | +173 | -0 | +173 | Merge recipes from main branch |
| 36 | `a0cc414` | 4,149 | +0 | -0 | 0 | Add 12 regional European cheeses |
| 37 | `f9c7b06` | 4,302 | +153 | -0 | +153 | Add 153 Americas/Oceania cheeses |
| 38 | `9d8e1d1` | 4,406 | +104 | -0 | +104 | Add 104 specialty cheeses |
| 39 | `8443ab5` | 4,508 | +102 | -0 | +102 | Add 156 regional cheeses |
| 40 | `2cab132` | 4,627 | +119 | -0 | +119 | Add 119 aging variant cheeses |
| 41 | `0248ea9` | 4,741 | +114 | -0 | +114 | Add 114 cheese variants |
| 42 | `3a267c9` | 4,868 | +147 | -20 | +127 | Rebase onto main: Add 127 cheeses *** |
| 43 | `13998bb` | 4,868 | +0 | -0 | 0 | Add milk_substitutions to 1,043 cheeses |
| 44 | `f2d6f6a` | 4,976 | +108 | -0 | +108 | Add 30 more authentic cheeses |
| 45 | `b044d7c` | 4,999 | +23 | -0 | +23 | Add 23 more authentic cheeses |
| 46 | `e284330` | 5,021 | +22 | -0 | +22 | Add 22 more authentic cheeses |
| 47 | `354d7fd` | 5,042 | +21 | -0 | +21 | Add 21 authentic regional cheeses |
| 48 | `a3bfb61` | 5,063 | +21 | -0 | +21 | Add 21 more authentic cheeses |
| 49 | `d1bd5bc` | 5,088 | +25 | -0 | +25 | Add 25 more cheese varieties |
| 50 | `bb10d58` | 5,156 | +68 | -0 | +68 | Add 68 protected designation cheeses |
| 51 | `c412100` | 5,224 | +68 | -0 | +68 | Add 68 regional cheeses |
| 52 | `7b91a09` | 5,298 | +74 | -0 | +74 | Add 75 worldwide cheeses |
| 53 | `3874544` | 5,369 | +71 | -0 | +71 | Add 71 regional/specialty cheeses |
| 54 | `ec41a91` | 5,451 | +82 | -0 | +82 | Add 82 cheese aging variants |
| 55 | `6acd2f3` | 5,435 | +11 | -27 | -16 | Fix validation errors *** |
| 56 | `05ee619` | 5,485 | +50 | -0 | +50 | Add 50 world cheese recipes |
| 57 | `e03d6a1` | 4,868 | +0 | -617 | -617 | Fix category and milk_substitutions *** |
| 58 | `b87b4e9` | 5,685 | +817 | -0 | +817 | Add 200 world cheese recipes |
| 59 | `c028b87` | 5,912 | +425 | -198 | +227 | Create cheesedotcom.md *** |
| 60 | `d80b802` | 5,912 | +0 | -0 | 0 | Add 48 authentic cheese recipes |
| 61 | `b173891` | 5,912 | +0 | -0 | 0 | Add 63 more cheese recipes |
| 62 | `19ebd7f` | 6,110 | +198 | -0 | +198 | Add 130+ new cheese varieties |
| 63 | `b4eb6f9` | 5,485 | +0 | -625 | -625 | Merge pull request #75 *** |
| 64 | `9faeeda` | 5,485 | +0 | -0 | 0 | Remove 17 duplicate cheese entries |
| 65 | `135ae20` | 5,621 | +136 | -0 | +136 | Merge 136 cheese recipes from PR #76 |
| 66 | `19ee185` | 5,685 | +198 | -134 | +64 | Fix 17 duplicate recipe IDs *** |
| 67 | `68f7418` | 5,819 | +134 | -0 | +134 | Merge 198 cheese recipes from PR #89 |
| 68 | `87be94c` | 5,840 | +21 | -0 | +21 | Add 21 Gordon Ramsay recipes from PR #85 |
| 69 | `e4f129c` | 5,819 | +0 | -21 | -21 | Fix validation warnings *** |
| 70 | `9758e95` | 5,722 | +21 | -118 | -97 | Deduplicate recipes and link variants *** |
| 71 | `7743a84` | 5,722 | +0 | -0 | 0 | Reclassify 1600 cheeses to cheese category |
| 72 | `4eb5094` | 5,722 | +0 | -0 | 0 | Add nutrition data to 2289 recipes |
| 73 | `de90dcf` | 5,819 | +118 | -21 | +97 | Fix OCR errors *** |
| 74 | `4cca130` | 5,819 | +0 | -0 | 0 | Calculate USDA nutrition data |
| 75 | `fc75ef2` | 5,819 | +0 | -0 | 0 | Expand nutrition database |
| 76 | `c7f739b` | 5,831 | +12 | -0 | +12 | Add initial GR Hell's Kitchen recipes |
| 77 | `df1d4b7` | 5,841 | +10 | -0 | +10 | Add more GR Hell's Kitchen recipes |
| 78 | `a8b85f1` | 5,848 | +7 | -0 | +7 | Add Caesar Salad, Mussels, Carpaccio |
| 79 | `3349796` | 5,910 | +62 | -0 | +62 | Add 55 GR Hell's Kitchen recipes |
| 80 | `60894ac` | 5,973 | +63 | -0 | +63 | Add GR image tracking manifest |
| 81 | `0130f60` | 5,974 | +1 | -0 | +1 | Add Butter Lettuce, Grilled Lamb |
| 82 | `0c5e35a` | 5,985 | +11 | -0 | +11 | Add 3 GR recipes (pages 231-247) |
| 83 | `3a715f7` | 5,985 | +0 | -0 | 0 | Add 4 GR recipes (pages 202-221) |
| 84 | `fdeb794` | 5,994 | +9 | -0 | +9 | Add 5 GR recipes (pages 253-269) |
| 85 | `235bea9` | 6,000 | +7 | -1 | +6 | Add 5 GR dessert recipes *** |
| 86 | `9a38b80` | 6,000 | +0 | -0 | 0 | Add 2 GR side dishes |
| 87 | `b72f0e9` | 6,005 | +5 | -0 | +5 | Add 5 GR side dish recipes |
| 88 | `de49d59` | 6,008 | +3 | -0 | +3 | Add 3 GR dessert recipes |
| 89 | `0403380` | 6,013 | +6 | -1 | +5 | Add GR dessert recipes *** |
| 90 | `792a107` | 6,014 | +1 | -0 | +1 | Add Blueberry Tart recipe |
| 91 | `8cb1d29` | 6,019 | +5 | -0 | +5 | Add 5 GR recipes (pages 271-427) |
| 92 | `7beae7b` | 6,020 | +1 | -0 | +1 | Add GR Kitchen Techniques & Tips |
| 93 | `d5d4f4d` | 6,020 | +0 | -0 | 0 | Add pastry crust tips |
| 94 | `c604910` | 6,020 | +0 | -0 | 0 | Fix remaining image refs |
| 95 | `7304967` | 6,021 | +1 | -0 | +1 | Add Big Back Sauce recipe |
| 96 | `01c815e` | 6,022 | +1 | -0 | +1 | Add Garlic Butter Pasta recipe |
| 97 | `a803cfc` | 6,022 | +0 | -0 | 0 | Add nutrition data to all 6,022 recipes |
| 98 | `22cdb80` | 6,024 | +2 | -0 | +2 | Add 2 GR Hell's Kitchen recipes |
| 99 | `a44da03` | 6,027 | +3 | -0 | +3 | Add 3 GR salad recipes |
| 100 | `246f4cc` | 6,029 | +2 | -0 | +2 | Add 2 more GR recipes |
| 101 | `abdbd14` | 6,030 | +1 | -0 | +1 | Add Tarte Tatin recipe |
| 102 | `5cab239` | 6,035 | +5 | -0 | +5 | Add 5 Food My Muse egg recipes |
| 103 | `18a4846` | 6,043 | +8 | -0 | +8 | Add 8 Food My Muse recipes |
| 104 | `c119890` | 6,043 | +0 | -0 | 0 | Fix validation errors |
| 105-108 | various | 6,043 | +0 | -0 | 0 | Image audit (Kindle screenshots) |
| 109 | `39b2236` | 6,045 | +2 | -0 | +2 | Image audit: add 2 new recipes |
| 110 | `08b8694` | 6,045 | +0 | -0 | 0 | Image audit: delete JPEG duplicates |
| 111 | `f7b6ced` | 6,049 | +4 | -0 | +4 | Image audit: handwritten meatball recipe |
| 112 | `08f83bf` | 6,057 | +8 | -0 | +8 | Image audit: add 8 new recipes |

---

## Classification of All 2,236 Missing IDs

### Correctly Removed (1,176 - no action needed)

| Category | Count | Reason |
|----------|-------|--------|
| `CORRECT_FILTER` | 1,118 | Recipes from other collections (grandma: 689, mommom: 336, granny: 91, reference: 2) correctly filtered out when this repo became standalone |
| `CORRECT_CLEANUP` | 58 | Non-recipe OCR artifacts, ads, addresses, cookbook metadata (e.g., "Published Forthebenefit Of", "Scale Ofpoints Forcow", "Weights Andmeasures") |

### Lost Recipes Needing Recovery (1,060)

| Category | Count | Source | How Lost |
|----------|-------|--------|----------|
| `LOST_GUTENBERG_RECIPE` | 539 | Project Gutenberg public domain cookbooks | Filter oscillation (#9-#15) then PR #58 merge took filtered version |
| `LOST_CHEESE_BAD_MERGE` | 291 | Traditional cheese varieties, cheesemaking guides | PR #75 merge (`b4eb6f9`) took stale branch version |
| `LOST_CPM_RECIPE` | 128 | ChiliPepperMadness.com recipes | Filter oscillation then PR #58 |
| `LOST_CHEESE_OTHER` | 2 | Hot sauce recipes miscategorized | Dropped in rebase/dedup operations (#42, #55) |
| ~~`RECLASSIFIED_UNICODE_DEDUP`~~ | ~~27~~ | ~~Cheese recipes with Unicode chars in IDs~~ | ~~Replaced with ASCII equivalents already in file (e.g., `beaufort-été` → `beaufort-ete`)~~ |
| `LOST_GORDON_RAMSAY` | 23 | gordonramsay.com recipes (21 `gr-*`) + 2 Hell's Kitchen | 21 lost in validation/dedup oscillation (#69-#73); 2 replaced without preserving old ID |
| `LOST_CUSOCUTS_RECIPE` | 16 | CusoCuts grilling/BBQ recipes | Filter oscillation then PR #58 |
| `LOST_WEBSITE_RECIPE` | 14 | Various websites (Food52, TheChoppingBlock, etc.) | Filter oscillation then PR #58 |
| `LOST_HBH_RECIPE` | 8 | Half Baked Harvest Mexican recipes | Filter oscillation then PR #58 |
| `LOST_PP_RECIPE` | 6 | PepperPowered.com curry/hot sauce recipes | Filter oscillation (#11) then PR #58 |
| `LOST_OTHER` | 6 | Misc (Peruvian, handwritten, user-provided) | Filter oscillation then PR #58 |

---

## Recovery Plan — COMPLETED

Recovery executed on 2026-02-05 using `scripts/recover_lost_recipes.py`.

### Recovery Results

| Category | Listed | Recovered | Already Present | Not Found | Notes |
|----------|--------|-----------|-----------------|-----------|-------|
| LOST_GUTENBERG_RECIPE | 539 | 539 | 0 | 0 | From `12f070a` |
| LOST_CPM_RECIPE | 128 | 128 | 0 | 0 | From `12f070a` |
| LOST_CUSOCUTS_RECIPE | 16 | 16 | 0 | 0 | From `12f070a` |
| LOST_WEBSITE_RECIPE | 14 | 14 | 0 | 0 | From `12f070a` |
| LOST_HBH_RECIPE | 8 | 8 | 0 | 0 | From `12f070a` |
| LOST_PP_RECIPE | 6 | 6 | 0 | 0 | From `12f070a` |
| LOST_OTHER | 6 | 6 | 0 | 0 | From `12f070a` |
| LOST_CHEESE_BAD_MERGE | 291 | 291 | 0 | 0 | From `19ebd7f` |
| LOST_CHEESE_OTHER | 29 | 27 | 0 | 2 | 27 were Unicode duplicates (removed); 2 IDs never existed in git |
| LOST_GORDON_RAMSAY | 23 | 23 | 0 | 0 | From various commits |
| **TOTAL** | **1,060** | **1,058** | **0** | **2** | |

### Post-Recovery Cleanup

- **27 Unicode duplicate IDs removed**: These had accented characters (é, ø, ã, etc.) and ASCII equivalents already existed in the file
- **6 Unicode IDs renamed to ASCII**: `traditional-bergkäse-austrian-alpine` → `traditional-bergkase-austrian-alpine`, etc.
- **2 IDs never existed**: `ghost-pepper-salsa-dried-chilies` and `louisiana-fermented-ghost-pepper-sauce` were not found in any commit of `data/recipes.json` across the entire git history
- **Cheese category fixed**: All LOST_CHEESE_BAD_MERGE and LOST_CHEESE_OTHER recipes set to `category: "cheese"`
- **Collection fixed**: All recovered recipes set to `collection: "all"`

### Pre-existing Data Quality Issues (NOT introduced by recovery)

- **536 Gutenberg recipes** have empty `ingredients` arrays (vintage narrative-style recipes with ingredients in instruction text)
- **1 recipe** (`peruvian-anticuchos-recipe-rumba-meats`) is a stub with empty ingredients and instructions
- **10 recipes** have empty `instructions` arrays (8 HBH crockpot stubs, 2 Peruvian stubs)

### Final Count

| Metric | Before | After |
|--------|--------|-------|
| Total recipes | 6,057 | 7,088 |
| Net recovered | — | +1,031 |

---

## Detailed Removal Event Analysis

### Event #3 (`fd203e5`) - CPM Batch 5 Merge Lost Chile Bible Recipes

- **Removed**: 88 Chile Bible / Cooking With The Ancients recipe IDs
- **Cause**: BAD_MERGE - The CPM batch 5 branch forked before commit #2 (which added the Chile Bible recipes). When it merged, it brought back a `recipes.json` without them.
- **Impact**: These 88 IDs were restored in later commits during the oscillation period and are NOT permanently lost.

### Event #9 (`60bf530`) - Filter to Standalone Collection

- **Removed**: 1,804 IDs
- **Cause**: INTENTIONAL FILTER - This commit filtered `recipes.json` to only `collection: "all"` recipes, removing granny/grandma/mommom/reference collections.
- **Impact**: Correct removal for the standalone repo. However, it also removed some `collection: "all"` recipes that had been added on other branches but not yet merged.

### Events #10-#13 - Filter Oscillation

- **Pattern**: Count swings between ~3,607 (filtered) and ~5,400 (unfiltered)
- **Cause**: Different branches had different versions. Merges alternated.
- **Impact**: Most recipes were restored, but the oscillation caused confusion.

### Event #15 (`d617443`) - PR #58 Merge

- **Removed**: 1,870 IDs in one merge
- **Cause**: BAD_MERGE - PR #58 branch had a stale, filtered `recipes.json`. The merge took the branch version.
- **Impact**: This is where the bulk of Gutenberg (539), CPM (128), CusoCuts (16), and website recipes were permanently lost. The 1,118 other-collection recipes removed here were CORRECT.

### Event #16 (`4bb0765`) - Bull's Eye BBQ Sauce

- **Removed**: 29 IDs (non-recipe OCR junk)
- **Cause**: CORRECT CLEANUP - These were cookbook metadata entries, not recipes.

### Event #22 (`58baa6b`) - Argentine Cheese Revert

- **Removed**: 12 IDs
- **Cause**: INTENTIONAL REVERT - Reverted then re-added at commit #27 under same IDs.
- **Impact**: No permanent loss.

### Event #28 (`5eddbe4`) - Middle Eastern Cheeses

- **Removed**: 171 IDs
- **Cause**: Branch rebase that dropped some earlier cheese additions.
- **Impact**: Partially a branch conflict; some IDs were restored in later cheese additions.

### Event #33 (`5bf1759`) - Fix Duplicate Recipe IDs

- **Removed**: 307 IDs
- **Cause**: Deduplication pass that consolidated duplicate cheese entries.
- **Impact**: Most were legitimate deduplication. Some unique content may have been lost.

### Event #42 (`3a267c9`) - Rebase onto Main

- **Removed**: 20 IDs (cheese recipes with special characters in IDs)
- **Cause**: Rebase conflict resolution dropped recipes with Unicode characters in IDs.
- **Impact**: 20 cheese recipes permanently lost (queso-del-país, beaufort-été, etc.).

### Event #55 (`6acd2f3`) - Fix Validation Errors

- **Removed**: 27 IDs
- **Cause**: Validation fix removed entries that failed schema validation (including cheese recipes with special character IDs).
- **Impact**: 27 cheese recipes permanently lost.

### Event #57 (`e03d6a1`) - Fix Category and Milk Substitutions

- **Removed**: 617 IDs
- **Cause**: BAD_MERGE - Commit claimed to only fix categories but actually replaced `recipes.json` with a much older version (4,868 vs 5,485 recipes).
- **Impact**: 617 IDs dropped. Most were later re-added in subsequent cheese addition commits, but this was a careless replacement.

### Event #63 (`b4eb6f9`) - PR #75 Merge

- **Removed**: 625 IDs
- **Cause**: BAD_MERGE - PR #75 branch had forked from before the cheese variety additions. Merge took branch's stale `recipes.json`.
- **Impact**: 291 cheese recipes permanently lost (traditional-\*, cheesemaking-\*, artisan-\*, british-\*, dutch-\*, etc.).

### Event #69 (`e4f129c`) - Fix Validation Warnings

- **Removed**: 21 Gordon Ramsay `gr-*` recipes
- **Cause**: Branch oscillation - different branches had different recipe sets.
- **Impact**: These 21 `gr-*` recipes were never restored.

### Event #70 (`9758e95`) - Deduplicate Recipes

- **Removed**: 118 IDs (including the 21 GR recipes that came back momentarily plus 97 cheese dedup)
- **Impact**: The 21 `gr-*` recipes were re-added here, but then lost again at event #73.

### Events #85 and #89 - Gordon Ramsay Recipe Replacements

- **Removed**: 1 ID each (`gordon-ramsay-bread-pudding-fig-jam`, `gordon-ramsay-caramel-sauce`)
- **Cause**: Recipes were updated/replaced with new transcriptions, but old IDs were dropped instead of preserved.
- **Impact**: 2 recipes with unique content replaced without backward compatibility.

---

## Appendix: Complete List of Lost Recipe IDs

See `RECIPE_AUDIT_LOST_IDS.md` for the full table of all 1,060 lost recipe IDs with titles, categories, and sources.

---

## Methodology

1. Extracted the full commit history of `data/recipes.json` (112 commits)
2. At each commit, parsed the JSON and extracted all recipe IDs
3. Diffed consecutive commits to identify additions and removals
4. Built a lifecycle tracker for every unique ID (8,293 total)
5. Classified each of the 2,236 missing IDs by:
   - Collection membership (all, grandma, mommom, granny, reference)
   - Source attribution (Gutenberg, CPM, CusoCuts, etc.)
   - Removal cause (filter, merge, dedup, cleanup)
6. Cross-referenced with commit messages and merge history

### Data Files (in /tmp/recipe_audit/)

| File | Description |
|------|-------------|
| `commits.txt` | All 112 commit hashes in chronological order |
| `ids/NNN_HASH.txt` | Recipe IDs at each commit |
| `transitions_enriched.json` | Full diff data between consecutive commits |
| `lifecycle.json` | Lifecycle of every recipe ID ever seen |
| `permanently_lost.json` | IDs present in history but not in current |
| `classified_lost.json` | Each lost ID with collection/category/source data |
| `verdicts.json` | Final classification of each lost ID |
| `verdicts_grouped.json` | Lost IDs grouped by verdict category |
