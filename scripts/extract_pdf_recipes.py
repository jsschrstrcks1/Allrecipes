#!/usr/bin/env python3
"""
Extract recipes from PDF cookbook files.

Usage:
    python scripts/extract_pdf_recipes.py all/PDFs/cookbook.pdf --dry-run
    python scripts/extract_pdf_recipes.py all/PDFs/cookbook.pdf --add
"""

import re
import json
import argparse
import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 not installed. Run: pip install PyPDF2", file=sys.stderr)
    sys.exit(1)


def extract_text_from_pdf(pdf_path, max_pages=50):
    """Extract text from PDF file."""
    text = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = min(len(reader.pages), max_pages)
            for i in range(num_pages):
                page = reader.pages[i]
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        return ""
    return "\n\n".join(text)


def clean_text(text):
    """Clean extracted text."""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def parse_single_ingredient(line):
    """Parse a single ingredient line."""
    line = line.strip()
    if not line or len(line) < 3:
        return None

    # Pattern with quantity
    pattern = r'^(\d+(?:[/-]\d+)?(?:\s*\d+/\d+)?)\s*(cups?|tablespoons?|teaspoons?|pounds?|ounces?|quarts?|pints?|tbsp|tsp|oz|lb)?\s*(?:of\s+)?(.+)$'

    match = re.match(pattern, line, re.I)
    if match:
        quantity = match.group(1)
        unit = match.group(2) or ""
        item = match.group(3).strip()

        unit_map = {
            'tablespoon': 'tbsp', 'tablespoons': 'tbsp',
            'teaspoon': 'tsp', 'teaspoons': 'tsp',
            'pound': 'lb', 'pounds': 'lb',
            'ounce': 'oz', 'ounces': 'oz',
            'cup': 'cup', 'cups': 'cup',
        }
        unit = unit_map.get(unit.lower(), unit.lower()) if unit else ""

        return {"item": item, "quantity": quantity, "unit": unit, "prep_note": ""}
    else:
        return {"item": line, "quantity": "", "unit": "", "prep_note": ""}


def create_recipe_id(title, source):
    """Create a URL-friendly recipe ID."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:40] + "-pdf"


def determine_category(title):
    """Determine recipe category based on title."""
    title_lower = title.lower()

    if any(word in title_lower for word in ['soup', 'broth', 'chowder', 'stew']):
        return 'soups'
    elif any(word in title_lower for word in ['salad']):
        return 'salads'
    elif any(word in title_lower for word in ['cake', 'pie', 'cookie', 'pudding', 'dessert', 'sweet', 'candy', 'ice cream']):
        return 'desserts'
    elif any(word in title_lower for word in ['bread', 'roll', 'muffin', 'biscuit']):
        return 'breads'
    elif any(word in title_lower for word in ['egg', 'omelet', 'breakfast']):
        return 'breakfast'
    elif any(word in title_lower for word in ['sauce', 'gravy', 'dressing']):
        return 'sides'
    elif any(word in title_lower for word in ['drink', 'beverage', 'punch', 'tea', 'coffee']):
        return 'beverages'
    elif any(word in title_lower for word in ['pickle', 'preserve', 'jam', 'jelly']):
        return 'sides'
    else:
        return 'mains'


def find_recipes_in_text(text, source_name):
    """Find recipe patterns in extracted text."""
    recipes = []

    # Look for common recipe title patterns
    # Pattern: ALL CAPS TITLE or Title Case followed by ingredients
    patterns = [
        # Pattern 1: ALL CAPS recipe names
        r'([A-Z][A-Z\s]{5,50})\s*(?:\d+\s*(?:cup|tablespoon|teaspoon|pound|ounce))',
        # Pattern 2: Recipe followed by colon
        r'([A-Za-z][A-Za-z\s]{5,50}):\s*(?:\d+\s*(?:cup|tablespoon|teaspoon|pound|ounce))',
    ]

    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            title = match.group(1).strip()
            if len(title) < 5 or len(title) > 60:
                continue

            # Skip common non-recipe headers
            skip_words = ['contents', 'index', 'chapter', 'introduction', 'preface', 'page']
            if any(skip in title.lower() for skip in skip_words):
                continue

            # Get surrounding text for ingredients/instructions
            start = match.start()
            end = min(start + 1000, len(text))
            recipe_text = text[start:end]

            # Try to extract ingredients
            ingredients = []
            ing_pattern = r'(\d+(?:/\d+)?\s*(?:cups?|tablespoons?|teaspoons?|pounds?|ounces?)[^.]*)'
            ing_matches = re.findall(ing_pattern, recipe_text[:500], re.I)
            for ing in ing_matches[:10]:
                parsed = parse_single_ingredient(ing.strip())
                if parsed:
                    ingredients.append(parsed)

            if len(ingredients) < 2:
                continue

            recipe_id = create_recipe_id(title, source_name)
            category = determine_category(title)

            recipe = {
                "id": recipe_id,
                "collection": "all",
                "collection_display": "Other Family Recipes",
                "title": title.title(),
                "category": category,
                "attribution": "",
                "source_note": f"{source_name} (PDF, public domain)",
                "description": "Vintage recipe from public domain cookbook",
                "servings_yield": "4 servings",
                "prep_time": "",
                "cook_time": "",
                "total_time": "",
                "ingredients": ingredients,
                "instructions": [{"step": 1, "text": "See original source for full instructions."}],
                "temperature": "",
                "pan_size": "",
                "notes": ["Extracted from PDF - verify against original"],
                "tags": ["vintage", "public-domain", "pdf-extracted"],
                "confidence": {
                    "overall": "low",
                    "flags": ["pdf-extraction", "may-need-verification"]
                },
                "image_refs": [],
                "nutrition": {
                    "status": "insufficient_data",
                    "per_serving": {},
                    "missing_inputs": ["all"],
                    "assumptions": []
                }
            }

            recipes.append(recipe)

    return recipes


def extract_recipes_from_pdf(pdf_path):
    """Extract recipes from a PDF file."""
    source_name = Path(pdf_path).stem.replace('_', ' ').replace('-', ' ').title()

    text = extract_text_from_pdf(pdf_path)
    if not text:
        return [], source_name

    recipes = find_recipes_in_text(text, source_name)
    return recipes, source_name


def main():
    parser = argparse.ArgumentParser(description='Extract recipes from PDF cookbooks')
    parser.add_argument('pdf_file', help='Path to PDF file')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--add', action='store_true', help='Add to recipes.json')
    args = parser.parse_args()

    pdf_path = Path(args.pdf_file)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    recipes, source_name = extract_recipes_from_pdf(pdf_path)

    print(f"Extracted {len(recipes)} recipes from '{source_name}'", file=sys.stderr)

    if args.dry_run:
        for i, recipe in enumerate(recipes[:5]):
            print(f"\n{'='*60}")
            print(f"Recipe {i+1}: {recipe['title']}")
            print(f"Category: {recipe['category']}")
            print(f"Ingredients ({len(recipe['ingredients'])}):")
            for ing in recipe['ingredients'][:5]:
                qty = f"{ing['quantity']} {ing['unit']}".strip()
                print(f"  - {qty} {ing['item']}" if qty else f"  - {ing['item']}")

        if len(recipes) > 5:
            print(f"\n... and {len(recipes)-5} more recipes")
    elif args.add and recipes:
        recipes_file = Path('data/recipes.json')
        with open(recipes_file, 'r') as f:
            data = json.load(f)

        existing_ids = {r['id'] for r in data['recipes']}
        added = 0
        for recipe in recipes:
            if recipe['id'] not in existing_ids:
                data['recipes'].append(recipe)
                existing_ids.add(recipe['id'])
                added += 1

        data['meta']['total_recipes'] = len(data['recipes'])
        data['meta']['last_updated'] = '2026-01-13'

        with open(recipes_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Added {added} new recipes to recipes.json")
    else:
        print(json.dumps(recipes, indent=2))


if __name__ == '__main__':
    main()
