---
name: ebook-builder
description: "Generates the combined Family Recipe Archive cookbook from all three collections (Grandma Baker, Granny Hudson, MomMom Baker). Handles cross-collection table of contents, per-grandmother sections, and unified print styling."
version: 1.0.0
---

# Ebook Builder — Family Recipe Archive

> Three grandmothers. One cookbook. A family's heritage in print.

## Purpose

Generates a combined printable cookbook that aggregates recipes from all three family collections into a single `ebook/book.html` with proper attribution, categorization, and print styling.

## When to Fire

- On `/ebook` command
- After collection-sync reports new recipes
- When the user requests a combined cookbook

## Source Collections

| Collection | Source Repo | Data Location |
|-----------|-----------|---------------|
| Grandma Baker | `/home/user/Grandmasrecipes/` | `data/recipes*.json` |
| Granny Hudson | `/home/user/Grannysrecipes/` | `data/recipes*.json` |
| MomMom Baker | `/home/user/MomsRecipes/` | `data/recipes*.json` |

## Book Structure

```html
<!-- Cover Page -->
<div class="cover">
  <h1>The Family Recipe Archive</h1>
  <p>Recipes from Grandma Baker, Granny Hudson, and MomMom Baker</p>
  <p class="dedication">For the glory of God and the nourishment of family</p>
</div>

<!-- Table of Contents — by collection, then by category -->
<div class="toc">
  <h2>Table of Contents</h2>
  <h3>Grandma Baker's Kitchen</h3>
  <!-- categories and recipes -->
  <h3>Granny Hudson's Kitchen</h3>
  <!-- categories and recipes -->
  <h3>MomMom Baker's Kitchen</h3>
  <!-- categories and recipes -->
</div>

<!-- Per-Collection Sections -->
<div class="collection" data-collection="grandma">
  <h2>Grandma Baker's Kitchen</h2>
  <!-- recipes grouped by category -->
</div>
<!-- ... repeat for each collection -->

<!-- Cross-Collection Index -->
<div class="index">
  <h2>Recipe Index</h2>
  <!-- All recipes alphabetized with collection attribution -->
</div>
```

## Per-Recipe Attribution

Every recipe in the combined cookbook MUST show which grandmother it comes from:

```html
<div class="recipe" data-collection="grandma" data-category="{category}">
  <h3>{title}</h3>
  <p class="attribution">From Grandma Baker's Kitchen</p>
  <!-- ingredients, instructions, notes -->
</div>
```

## Cross-Collection Duplicate Handling

When the same dish appears in multiple collections (e.g., both grandmothers' cornbread):
- Include BOTH versions
- Cross-reference: "See also Granny Hudson's version on page X"
- Do NOT merge or combine recipes — each grandmother's version is distinct

## Print Optimization

Same rules as individual ebook-builders:
- Page breaks between recipes
- No orphaned headings
- Images sized for print (max 4in)
- Margins: 0.75in
- Collection divider pages between sections

## Workflow

1. Run `/sync` first (collection-sync) to ensure data is current
2. Aggregate recipe data from all 3 source repos
3. Group by collection, then by category within each collection
4. Generate combined `ebook/book.html`
5. Build unified index
6. Validate: all recipes present, all cross-references correct

## Integration

- **collection-sync** — Run sync BEFORE building to ensure current data
- **nutrition-estimator** — Include nutrition facts if available
- **careful-not-clever** — Never mix up which grandmother a recipe belongs to

---

*Soli Deo Gloria* — Three grandmothers' legacies, bound together in one family cookbook.
