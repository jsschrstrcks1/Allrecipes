---
name: collection-sync
description: "Keeps the Allrecipes aggregator in sync with its 3 source repositories (Grandmasrecipes, Grannysrecipes, MomsRecipes). Detects changes, identifies new/modified/deleted recipes, validates cross-collection indexes, and checks for duplicates."
version: 1.0.0
---

# Collection Sync

> Three kitchens, one family cookbook.

## Purpose

Allrecipes is the aggregator hub for three family recipe collections. This skill ensures the aggregator stays in sync with the source repos, catches duplicates across collections, and maintains cross-collection search indexes.

## When to Fire

- On `/sync` command
- At session start (quick check)
- After bulk recipe changes in any source repo
- When cross-collection features are being worked on

## Source Repositories

| Collection | Repository | Owner |
|-----------|-----------|-------|
| Grandma Baker | `/home/user/Grandmasrecipes/` | Grandma Baker's recipes |
| Granny Hudson | `/home/user/Grannysrecipes/` | Granny Hudson's recipes |
| MomMom Baker | `/home/user/MomsRecipes/` | MomMom Baker's recipes |

## Available Scripts

```bash
# Aggregate all collections
python3 scripts/aggregate_collections.py

# Aggregate cooking tips
python3 scripts/aggregate_tips.py

# Find duplicates across collections
python3 scripts/analyze_duplicates.py
python3 scripts/check-duplicates.py

# Build ingredient index
python3 scripts/build-ingredient-index.py

# Build search shards
python3 scripts/build_shards.py
```

## Sync Workflow

### 1. Quick Status Check (Session Start)

For each source repo, compare:
- Last commit timestamp in source repo vs. last sync timestamp
- Recipe count in source vs. count in aggregator
- Any new files in source `data/` directories

Report:
```
## Sync Status — [date]
| Collection | Source Recipes | Aggregated | Last Sync | Status |
|-----------|--------------|-----------|-----------|--------|
| Grandma Baker | 245 | 245 | 2026-03-20 | ✅ Current |
| Granny Hudson | 180 | 178 | 2026-03-15 | ⚠️ 2 new recipes |
| MomMom Baker | 150 | 150 | 2026-03-22 | ✅ Current |
```

### 2. Full Sync

```bash
# Step 1: Check for changes
python3 scripts/check-duplicates.py  # Find cross-collection duplicates first

# Step 2: Aggregate
python3 scripts/aggregate_collections.py

# Step 3: Rebuild indexes
python3 scripts/build-ingredient-index.py
python3 scripts/build_shards.py

# Step 4: Aggregate tips
python3 scripts/aggregate_tips.py
```

### 3. Duplicate Detection

Cross-collection duplicates are expected — the same dish may appear in multiple grandmothers' collections. Handle them as:

- **Same dish, different recipe** — Keep both, note the cross-reference ("See also Granny Hudson's version")
- **Identical recipe** — Flag for review (which collection should be primary?)
- **Similar name, different dish** — Clarify in metadata

```bash
python3 scripts/analyze_duplicates.py
```

### 4. Validation

After sync, verify:
- All source recipes are represented in the aggregator
- No orphaned entries (recipe in aggregator but deleted from source)
- Cross-collection search returns results from all 3 collections
- Ingredient index includes all unique ingredients
- Search shards are current

## Sync Status Tracking

Maintain a sync status file or memory entry:
```json
{
  "last_sync": "2026-03-25T14:30:00Z",
  "collections": {
    "grandma": {"recipe_count": 245, "last_commit": "abc123"},
    "granny": {"recipe_count": 180, "last_commit": "def456"},
    "mommom": {"recipe_count": 150, "last_commit": "ghi789"}
  }
}
```

## Integration

- **cognitive-memory** — Remember sync state across sessions
- **recipe-validation** — Validate aggregated data after sync
- **nutrition-estimator** — Ensure nutrition data propagates to aggregator
- **careful-not-clever** — Never merge recipes without checking. Duplicates need human review.

## What NOT to Do

- Never delete a recipe from a source repo through the aggregator
- Never modify source recipes from the aggregator (read-only from sources)
- Never assume two similarly-named recipes are the same without checking
- Never run a full re-aggregate without checking duplicates first

---

*Soli Deo Gloria* — Three grandmothers' legacies, faithfully preserved together.
