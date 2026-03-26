# Recipe Validation Skill

## Purpose

Validate recipe data against the schema and quality standards before committing changes.

## Activation Triggers

- Modifying `data/recipes.json`
- Keywords: validate, check, schema, verify

## Validation Command

```bash
python scripts/validate-recipes.py
```

For strict mode (fails on warnings):

```bash
python scripts/validate-recipes.py --strict
```

## What Gets Validated

### Required Fields

- `id` - Unique slug identifier
- `collection` - Must be "all" for this repo
- `title` - Recipe name
- `category` - Must be from valid list
- `ingredients` - Array with at least one item
- `instructions` - Array with at least one step

### Optional Fields (Validated if Present)

- `source_note` - Source attribution
- `description` - Brief description
- `servings_yield` - Number of servings
- `prep_time`, `cook_time`, `total_time`
- `temperature` - Cooking temperature
- `pan_size` - Required pan/dish
- `notes` - Array of strings
- `tags` - Array of tag strings
- `confidence` - Object with `overall` and `flags`
- `image_refs` - Array of filenames
- `nutrition` - Nutrition data object

### Valid Categories

```
appetizers | beverages | breads | breakfast | desserts
mains | salads | sides | soups | snacks
```

### Sanity Limits

The validator checks for implausible values:

| Check | Limit | Why |
|-------|-------|-----|
| Salt | ≤ 4 tbsp | More is likely an error |
| Sugar | ≤ 8 cups | Reasonable max for large batches |
| Temperature | 200-550°F | Normal cooking range |
| Servings | 1-100 | Reasonable yield range |

## Error Types

### Errors (Must Fix)

- Missing required field
- Invalid category
- Duplicate recipe ID
- Malformed JSON
- Invalid field type

### Warnings (Review)

- Missing optional fields (source_note, confidence)
- Sanity limit exceeded
- Unusual ingredient quantities
- Missing image_refs

## Resolution Workflow

### Step 1: Run Validation

```bash
python scripts/validate-recipes.py
```

### Step 2: Review Output

```
Validating recipes.json...
  ✓ Recipe "chocolate-cake" valid
  ✗ Recipe "mystery-dish" - Missing required field: category
  ⚠ Recipe "salty-soup" - Warning: salt quantity (5 tbsp) exceeds limit
```

### Step 3: Fix Errors

- Missing fields: Add the field with appropriate value
- Invalid category: Use category from valid list
- Duplicate ID: Make IDs unique
- Sanity warnings: Verify against source image

### Step 4: Re-validate

```bash
python scripts/validate-recipes.py
```

### Step 5: Commit Only When Clean

Only commit when validation passes without errors.

## Guardrails

### MUST

- Run validation before every commit
- Fix all errors before proceeding
- Investigate warnings (don't ignore)
- Verify fixes against source images

### MUST NOT

- Commit with validation errors
- Ignore sanity limit warnings without verification
- Invent data to pass validation
- Disable or bypass validation

## Integration with Hooks

The `post-write-validate.sh` hook automatically runs validation when `recipes.json` is modified. Check the output for any errors.

---

*Accuracy is more important than speed.*
