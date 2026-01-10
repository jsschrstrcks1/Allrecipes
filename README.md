# Other Family Recipes

A collection of digital cookbook recipes and magazine clippings, preserved with love.

> *Soli Deo Gloria*

---

## About This Project

This archive contains reference recipes from digital cookbooks, magazines, and other sources - collected and used with permission. This is part of the multi-repo Family Recipe Archive system.

**Current Status:** 1546 recipes

---

## Multi-Repo Family Recipe Archive

This repository is part of a larger family recipe preservation project:

| Repository | Collection | Description |
|------------|------------|-------------|
| MomsRecipes | MomMom Baker | Family heirloom recipes |
| GrandmasRecipes | Grandma Baker | Michigan to Florida recipes |
| GrannysRecipes | Granny Hudson | Additional family collection |
| **Allrecipes** | **Other Recipes** | **Digital cookbooks & magazines (THIS REPO)** |
| FamilyRecipeHub | Aggregator | Combines all collections |

---

## Project Structure

```
Allrecipes/
├── CLAUDE.md                 # AI assistant context & guidelines
├── README.md                 # This file
├── index.html                # Home page with search & filters
├── recipe.html               # Recipe detail page
├── styles.css                # Stylesheet
├── script.js                 # Client-side JavaScript
├── data/
│   ├── *.jpeg               # Magazine scans
│   ├── *.PNG                # Kindle screenshots
│   ├── processed/           # AI-friendly resized images
│   ├── recipes.json         # All recipes in structured format
│   └── collections.json     # Collection metadata
├── scripts/
│   ├── validate-recipes.py  # Recipe validation
│   ├── process_images.py    # Image resizing
│   ├── image_safeguards.py  # Image validation
│   └── optimize_images.py   # JPEG optimization
└── ebook/
    ├── book.html            # Print-optimized e-book HTML
    └── print.css            # Print stylesheet
```

---

## Quick Start

### View the Website Locally

1. **Using Python (recommended):**
   ```bash
   cd Allrecipes
   python -m http.server 8000
   ```
   Then open http://localhost:8000 in your browser.

2. **Using Node.js:**
   ```bash
   npx serve .
   ```

3. **Using PHP:**
   ```bash
   php -S localhost:8000
   ```

### Host on GitHub Pages

1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Set source to your main branch and root folder
4. Your site will be live at `https://yourusername.github.io/Allrecipes/`

---

## Image Processing

This collection contains images from multiple sources that may exceed Claude's 2000px API limit:

| Source | Format | Typical Size | Action |
|--------|--------|--------------|--------|
| Kindle screenshots | PNG | 1320x2868px | Use `data/processed/` |
| iPhone photos | JPEG | Variable | Check dimensions |
| Magazine scans | JPEG | Variable | Usually safe |

### Process Oversized Images

```bash
# Preview what needs processing
python scripts/process_images.py --dry-run

# Process all oversized images
python scripts/process_images.py

# Validate image status
python scripts/image_safeguards.py status
```

---

## Generate PDF E-Book

### Method 1: Browser Print (Easiest)

1. Open `ebook/book.html` in your browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Select "Save as PDF" as the destination
4. Adjust margins to "None" or "Minimum"
5. Enable "Background graphics" for colors
6. Save

### Method 2: Using wkhtmltopdf

```bash
wkhtmltopdf \
  --enable-local-file-access \
  --page-size Letter \
  --margin-top 0.75in \
  --margin-bottom 0.75in \
  --margin-left 1in \
  --margin-right 1in \
  ebook/book.html other-family-recipes.pdf
```

---

## Recipe JSON Schema

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

## Validation

```bash
# Check JSON syntax and required fields
python scripts/validate-recipes.py

# Strict mode (fail on warnings)
python scripts/validate-recipes.py --strict
```

---

## Contributing

This is a family project. If you have:
- Additional digital cookbook recipes (with permission)
- Corrections to existing recipes
- Magazine clippings to add

Please reach out!

---

## License

This recipe collection is a family treasure. Please use respectfully.

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
