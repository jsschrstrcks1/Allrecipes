# Other Family Recipes

A large reference collection of digital cookbook recipes, magazine
clippings, and other curated sources — used alongside the family-specific
recipe repos. Includes the **butter builder**, **cheese builder**, and
**adulterant companion** tools that help cooks build, identify, and
substitute dairy products.

> *Soli Deo Gloria.*

---

## Table of Contents

- [About this project](#about-this-project)
- [Family Recipe Archive (multi-repo)](#family-recipe-archive-multi-repo)
- [What's in this repo](#whats-in-this-repo)
- [Project structure](#project-structure)
- [Quick start](#quick-start)
- [Image processing](#image-processing)
- [Generate the e-book / PDF](#generate-the-e-book--pdf)
- [Builder tools](#builder-tools)
- [Adding new recipes](#adding-new-recipes)
- [Recipe JSON schema](#recipe-json-schema)
- [Validation & integrity](#validation--integrity)
- [Audits and trackers](#audits-and-trackers)
- [Multi-LLM integration](#multi-llm-integration)
- [Contributing](#contributing)
- [License](#license)

---

## About this project

This archive contains reference recipes from digital cookbooks,
magazines, and other sources — collected and used with permission. It is
the **largest** repo in the family recipe system: ~9,989 recipes at last
count, with ongoing audits to recover lost IDs and consolidate cheese /
butter variants.

Where the other recipe repos preserve specific cooks (MomMom, Grandma,
Granny), this one is the **reference shelf** — the place to look up a
canonical béchamel, a Betty Crocker classic, or a magazine clipping
that doesn't belong to a particular grandmother.

---

## Family Recipe Archive (multi-repo)

| Repo | Collection |
|---|---|
| [MomsRecipes](https://github.com/jsschrstrcks1/MomsRecipes) | MomMom Baker (heirloom recipes) |
| [Grandmasrecipes](https://github.com/jsschrstrcks1/Grandmasrecipes) | Grandma Baker (Michigan → Florida) — also hosts the converters |
| [Grannysrecipes](https://github.com/jsschrstrcks1/Grannysrecipes) | Granny Hudson (Florida → Boston → back) |
| **Allrecipes** | **Reference cookbooks & magazines** *(this repo, ~9,989 recipes)* |

---

## What's in this repo

- A static recipe site with search & filters (HTML + CSS + vanilla JS).
- ~9,989 recipes in `data/recipes.json` — sourced from digital cookbooks
  and clippings, used with permission.
- The **butter builder**, **cheese builder**, and **adulterant
  companion** modules — interactive tools for building dairy products
  from scratch, identifying mystery cheeses, and recognizing common
  adulterants.
- A **milk-substitution** module mirroring the one in Grandma's repo,
  for offline use.
- A printable e-book (`ebook/book.html`).
- Multiple long-running audit trackers (cheese varieties, lost recipe
  IDs, image audit, overlooked tips) — see
  [Audits and trackers](#audits-and-trackers).

---

## Project structure

```
Allrecipes/
├── CLAUDE.md                       # AI assistant context
├── CAREFUL.md                      # Integrity guardrail
├── CHEESE_VARIANTS.md              # Cheese-builder variant rules
├── CHEESE_VARIETIES_TRACKER.md     # 60+ cheese varieties tracked
├── IMAGE_AUDIT.md                  # Image-coverage audit
├── OVERLOOKED_TIPS_AUDIT.md        # "Tips that should have been captured"
├── PENDING_TASKS.md                # Long-running task list
├── RECIPE_AUDIT_LOST_IDS.md        # Lost-recipe-ID audit
├── RECIPE_AUDIT_TRACKER.md         # Recipe audit master
├── cheesedotcom.md                 # Cheese.com data integration notes
├── README.md                       # This file
│
├── index.html                      # Home (search & filters)
├── recipe.html                     # Recipe detail page
├── tips.html                       # Tips index
├── butter-builder.html             # Butter builder UI
├── butter-builder.js
├── cheese-builder.html             # Cheese builder UI
├── cheese-builder.js
├── adulterant-companion.js         # Adulterant identification module
├── milk-substitution.js            # Milk substitution module
├── script.js                       # Site bundle
├── styles.css                      # Stylesheet
│
├── all/                            # Per-recipe HTML pages (where used)
├── data/
│   ├── *.jpeg                      # Magazine scans
│   ├── *.PNG                       # Kindle screenshots
│   ├── processed/                  # AI-friendly resized images
│   ├── recipes.json                # All recipes in structured form
│   └── collections.json            # Collection metadata
├── scripts/
│   ├── validate-recipes.py         # Recipe validation
│   ├── process_images.py           # Image resizing
│   ├── image_safeguards.py         # Image validation
│   └── optimize_images.py          # JPEG optimization
├── ebook/
│   ├── book.html                   # Print-optimized e-book
│   └── print.css                   # Print stylesheet
├── recovery_report.txt             # Recovery log from a past incident
├── _headers / .htaccess / .nojekyll # Host-level config
└── LICENSE                         # GNU AGPL v3
```

---

## Quick start

### View the site locally

```bash
# Python (recommended)
cd Allrecipes
python -m http.server 8000

# or Node.js
npx serve .

# or PHP
php -S localhost:8000
```

Open <http://localhost:8000>.

### Host on GitHub Pages / Netlify / Vercel

Pure static. Point the publish directory at the repo root. Cache headers
are pre-baked into `_headers` and `.htaccess`.

---

## Image processing

This collection mixes several source types that may exceed Claude's
2000 px API limit:

| Source | Format | Typical size | Action |
|---|---|---|---|
| Kindle screenshots | PNG | 1320 × 2868 px | Use `data/processed/` |
| iPhone photos | JPEG | Variable | Check dimensions |
| Magazine scans | JPEG | Variable | Usually safe |

#### Process oversized images

```bash
# Preview what needs processing
python scripts/process_images.py --dry-run

# Process all oversized images
python scripts/process_images.py

# Validate image status
python scripts/image_safeguards.py status
```

`image_safeguards.py` will refuse to commit oversized images and flags
referenced originals that don't have a processed copy.

---

## Generate the e-book / PDF

#### Browser print (easiest)

1. Open `ebook/book.html` in a browser.
2. `Ctrl+P` (or `Cmd+P`) → "Save as PDF".
3. Set margins to "None" or "Minimum"; enable "Background graphics".

#### `wkhtmltopdf`

```bash
wkhtmltopdf \
  --enable-local-file-access \
  --page-size Letter \
  --margin-top 0.75in --margin-bottom 0.75in \
  --margin-left 1in --margin-right 1in \
  ebook/book.html other-family-recipes.pdf
```

---

## Builder tools

### Butter Builder (`butter-builder.html` + `.js`)

A guided UI for building butter from cream — cultured, browned, salted,
or compound. Tracks fat percentage, water content, and shelf life. Uses
the validation rules from [`CAREFUL.md`](CAREFUL.md) so the output stays
in the realm of safe, traditional dairy practice.

### Cheese Builder (`cheese-builder.html` + `.js`)

Walks through the steps of building 60+ cheese varieties from milk,
including:

- Acidification path (mesophilic / thermophilic / direct-acid).
- Coagulation (rennet type, dose, temperature, set time).
- Cut, cook, drain, press, age.

The recognised varieties and their parameters are tracked in
[`CHEESE_VARIETIES_TRACKER.md`](CHEESE_VARIETIES_TRACKER.md). Variant
rules (low-moisture mozzarella vs. fresh, for example) are in
[`CHEESE_VARIANTS.md`](CHEESE_VARIANTS.md).

### Adulterant Companion (`adulterant-companion.js`)

Helps identify common adulterants (vegetable oils in olive oil,
non-dairy fat in butter, gum thickeners in yogurt) and explains how a
home cook can spot them. Educational only — not a substitute for a lab.

### Milk Substitution (`milk-substitution.js`)

A trimmed copy of the engine in Grandma's repo, kept here so the
reference site works standalone offline.

---

## Adding new recipes

1. **Drop the source** (Kindle screenshot, magazine scan, etc.) into
   `data/`.
2. **Resize for AI:**

   ```bash
   python scripts/process_images.py
   ```

3. **Extract** following [`CLAUDE.md`](CLAUDE.md):
   - Analyze the source for orientation and content.
   - Extract recipe data per the JSON schema.
   - Verify reuse rights — sources marked "with permission" are fine,
     but a generic web scrape is not.
   - Append to `data/recipes.json`.
4. **Validate:**

   ```bash
   python scripts/validate-recipes.py
   ```

5. **Commit** with a message referencing the source (e.g.
   `recipe: add Cook's Illustrated béarnaise (Sep 2003)`).

---

## Recipe JSON schema

```json
{
  "id": "recipe-slug",
  "collection": "all",
  "collection_display": "Other Family Recipes",
  "title": "Recipe Title",
  "category": "desserts|mains|sides|etc",
  "attribution": "Source/Author",
  "source_note": "e.g., Kindle cookbook, magazine clipping",
  "servings_yield": "4 servings",
  "prep_time": "15 minutes",
  "cook_time": "30 minutes",
  "ingredients": [
    {"item": "flour", "quantity": "2", "unit": "cups", "prep_note": "sifted"}
  ],
  "instructions": [
    {"step": 1, "text": "Preheat oven to 350°F."}
  ],
  "temperature": "350°F (175°C)",
  "tags": ["dessert", "holiday"],
  "confidence": {"overall": "high|medium|low"},
  "image_refs": ["filename.PNG"]
}
```

---

## Validation & integrity

```bash
# Full validation
python scripts/validate-recipes.py

# Strict mode (warnings become errors)
python scripts/validate-recipes.py --strict
```

Integrity rules (from [`CAREFUL.md`](CAREFUL.md)):

- **Source attribution required** for every recipe — no anonymous
  recipes.
- **Permission preserved.** If a source's license is unclear, mark
  `confidence.overall = "low"` with a flag explaining what's missing.
- **No AI-invented recipes.** Claude (or any model) may help transcribe
  and validate, but cannot author new recipes for this collection.
- **Cheese / butter rules** in [`CAREFUL.md`](CAREFUL.md) override
  spreadsheet defaults. The builder tools refuse outputs that would be
  unsafe.

---

## Audits and trackers

This repo runs several long-living audit documents. Each is updated as
work progresses; see the file headers for status.

| File | Purpose |
|---|---|
| [`RECIPE_AUDIT_TRACKER.md`](RECIPE_AUDIT_TRACKER.md) | Master recipe-audit progress |
| [`RECIPE_AUDIT_LOST_IDS.md`](RECIPE_AUDIT_LOST_IDS.md) | Recipes whose IDs went missing during refactors |
| [`CHEESE_VARIETIES_TRACKER.md`](CHEESE_VARIETIES_TRACKER.md) | 60+ cheese varieties and their parameters |
| [`CHEESE_VARIANTS.md`](CHEESE_VARIANTS.md) | Variant rules within a cheese family |
| [`IMAGE_AUDIT.md`](IMAGE_AUDIT.md) | Recipe-to-image coverage |
| [`OVERLOOKED_TIPS_AUDIT.md`](OVERLOOKED_TIPS_AUDIT.md) | Tips that originally lived only in marginalia |
| [`PENDING_TASKS.md`](PENDING_TASKS.md) | Long-running task list |
| [`cheesedotcom.md`](cheesedotcom.md) | Cheese.com integration notes |

---

## Multi-LLM integration

Defaults to **`recipe` mode** in the multi-LLM orchestrator hosted in
[ken](https://github.com/jsschrstrcks1/ken).

| Skill | Usage |
|---|---|
| `/consult gpt structure "..."` | Quick second opinion on extracted shape |
| `/orchestrate recipe "<task>"` | Full pipeline: transcribe → validate → integrate |
| Cognitive memory | Scope `/Allrecipes` |

#### Setup (per session)

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

The `recipe-transcription` and `recipe-validation` skills run inside
this pipeline. They never invent steps — anything inferred is flagged.

---

## Contributing

This is a family project. If you have:

- Additional digital cookbook recipes (with permission)
- Corrections to existing recipes
- Magazine clippings to add
- Cheese / butter expertise

Please reach out, or open a PR on a `claude/<topic>-<id>` branch.

---

## License

GNU Affero General Public License v3.0 — see [`LICENSE`](LICENSE). The
recipe source content remains under its original publishers' terms;
this repo claims no rights to it beyond compilation and presentation.

---

*"She looketh well to the ways of her household, and eateth not the
bread of idleness." — Proverbs 31:27*
