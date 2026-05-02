# Compound Recipes — Other Family Recipes

Some cookbooks (especially professional ones like Gordon Ramsay's) contain
**compound recipes** — dishes that include multiple sub-recipes (sauces,
garnishes, components).

## Hybrid Approach

Use **both** approaches simultaneously:

1. **Complete compound recipe** — the full dish with all sub-recipes inline.
2. **Separate component recipes** — each sub-recipe as its own searchable entry.

## Example: Beef Wellington

```
gordon-ramsay-beef-wellington          (COMPLETE)
├── Contains full inline instructions for ALL components
├── components: ["gordon-ramsay-duxelles", "gordon-ramsay-red-wine-jus"]
│
├─► gordon-ramsay-duxelles               (STANDALONE)
│   component_of: ["gordon-ramsay-beef-wellington"]
│   is_component: true
│
└─► gordon-ramsay-red-wine-jus           (STANDALONE)
    component_of: ["gordon-ramsay-beef-wellington"]
    is_component: true
```

## Schema Fields

| Field | Type | Description |
|---|---|---|
| `components` | array | IDs of sub-recipes extracted from this compound recipe |
| `component_of` | array | IDs of parent recipes this is a component of |
| `is_component` | boolean | True if this recipe is primarily used as a component |
| `tips` | array | Chef tips, technique notes from the cookbook |
| `substitutions` | array | `{original, substitute, note}` for suggested swaps |
