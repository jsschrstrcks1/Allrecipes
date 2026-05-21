# OCR Correction Standards — Other Family Recipes

## Common OCR Errors

- `l` ↔ `1` (lowercase L vs number one)
- `O` ↔ `0` (letter O vs zero)
- `rn` ↔ `m` (r-n combination vs letter m)
- `cl` ↔ `d` (c-l combination vs letter d)
- `tsp` vs `tbsp` — **critical for measurements** (3× difference)

## Measurement Standardization

| Original | Standardized |
|---|---|
| teaspoon, t, t. | tsp |
| tablespoon, T, Tbsp, Tbs | tbsp |
| cup, c, C | cup |
| ounce, oz | oz |
| pound, lb, # | lb |

## Temperature Format

Dual format: `350°F (175°C)`.

## Source Classification (before extraction)

| Source type | Indicators | Action | Keep image? |
|---|---|---|---|
| Kindle screenshots | "Location X of Y", e-reader UI | Check copyright, verify source | **No** — clear `image_refs` |
| Magazine clippings | Printed text, magazine layout | Process normally | **No** — clear `image_refs` |
| Typed cards | Typewriter font | Process normally | **No** — clear `image_refs` |
| Handwritten | Pen / pencil on paper | Process carefully | **Yes** — keep refs |
| Cookbook pages | Professional layout, copyright | **Verify permission** | **No** — clear `image_refs` |

## Completeness Check (mandatory)

Do not extract a recipe unless **all three** are present:

1. **Title**
2. **Ingredients** (at least partial)
3. **Instructions** (at least partial)

Missing any element → classify as a fragment and wait for adjacent images.

## Digital Screenshot Handling

For e-reader / Kindle screenshots ("Location X of Y"):

1. **Sort by Kindle location number** before processing.
2. **Verify commercial copyright** — all recipes must be used with permission.
3. **Identify the source cookbook** — record in `source_note`.
4. **Map page boundaries** — note recipes spanning multiple screenshots.
