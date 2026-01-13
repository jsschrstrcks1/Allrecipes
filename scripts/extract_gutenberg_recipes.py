#!/usr/bin/env python3
"""
Extract recipes from Project Gutenberg HTML cookbook files.

Usage:
    python scripts/extract_gutenberg_recipes.py all/HTML/pg6385-images.html --dry-run
    python scripts/extract_gutenberg_recipes.py all/HTML/pg6385-images.html --add
"""

import re
import json
import argparse
import sys
from pathlib import Path
from html import unescape


def clean_html(text):
    """Remove HTML tags and clean up text."""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def parse_title(title_raw):
    """Parse recipe title, extracting Italian name if present."""
    match = re.match(r'^(.+?)\s*\(([^)]+)\)\s*$', title_raw)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return title_raw.strip(), ""


def parse_single_ingredient(line):
    """Parse a single ingredient line."""
    line = line.strip()
    if not line or len(line) < 2:
        return None

    # Pattern with quantity
    pattern = r'^(\d+(?:[/-]\d+)?(?:\s*\d+/\d+)?)\s*(cups?|tablespoons?|teaspoons?|pounds?|ounces?|quarts?|pints?|tbsp|tsp|oz|lb|cloves?|slices?|pieces?|heads?|bunche?s?|small|medium|large|liberal)?\s*(?:of\s+)?(.+)$'

    match = re.match(pattern, line, re.I)
    if match:
        quantity = match.group(1)
        unit = match.group(2) or ""
        item = match.group(3).strip()

        # Normalize units
        unit_map = {
            'tablespoon': 'tbsp', 'tablespoons': 'tbsp',
            'teaspoon': 'tsp', 'teaspoons': 'tsp',
            'pound': 'lb', 'pounds': 'lb',
            'ounce': 'oz', 'ounces': 'oz',
            'cup': 'cup', 'cups': 'cup',
        }
        unit = unit_map.get(unit.lower(), unit.lower()) if unit else ""

        prep_note = ""
        if ',' in item:
            parts = item.split(',', 1)
            item = parts[0].strip()
            prep_note = parts[1].strip()

        return {"item": item, "quantity": quantity, "unit": unit, "prep_note": prep_note}
    else:
        # No quantity
        item = line
        prep_note = ""
        if ',' in item:
            parts = item.split(',', 1)
            item = parts[0].strip()
            prep_note = parts[1].strip()

        return {"item": item, "quantity": "", "unit": "", "prep_note": prep_note}


def create_recipe_id(title):
    """Create a URL-friendly recipe ID."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:50]


def determine_category(title):
    """Determine recipe category based on title."""
    title_lower = title.lower()

    if any(word in title_lower for word in ['soup', 'broth', 'chowder', 'minestra', 'zuppa', 'brodo']):
        return 'soups'
    elif any(word in title_lower for word in ['salad', 'insalata']):
        return 'salads'
    elif any(word in title_lower for word in ['cake', 'pie', 'tart', 'cookie', 'pudding', 'ice cream', 'dessert', 'dolce', 'torta', 'sweet']):
        return 'desserts'
    elif any(word in title_lower for word in ['bread', 'roll', 'muffin', 'pane']):
        return 'breads'
    elif any(word in title_lower for word in ['egg', 'uova', 'omelet', 'frittata']):
        return 'breakfast'
    elif any(word in title_lower for word in ['sauce', 'sugo']):
        return 'sides'
    elif any(word in title_lower for word in ['macaroni', 'spaghetti', 'pasta', 'noodle', 'rice', 'risotto', 'polenta', 'gnocchi']):
        return 'mains'
    elif any(word in title_lower for word in ['fish', 'cod', 'salmon', 'pesce', 'beef', 'veal', 'lamb', 'pork', 'chicken', 'turkey', 'pollo', 'vitello']):
        return 'mains'
    elif any(word in title_lower for word in ['vegetable', 'potato', 'bean', 'spinach', 'artichoke', 'asparagus']):
        return 'sides'
    else:
        return 'mains'


def extract_recipes_from_html(html_file):
    """Extract all recipes from an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get book metadata
    title_match = re.search(r'<meta name="dc.title" content="([^"]+)"', content)
    book_title = title_match.group(1) if title_match else Path(html_file).stem

    author_match = re.search(r'<meta name="dc.creator" content="([^"]+)"', content)
    book_author = author_match.group(1).split(',')[0] if author_match else ""

    recipes = []

    # Try multiple patterns for recipe titles
    patterns = [
        # Pattern 1: margin-top: 2em style (Italian cookbook, etc.)
        r'<(?:p|h[234])[^>]*style="margin-top:\s*2em"[^>]*>(.*?)</(?:p|h[234])>',
        # Pattern 2: class="recipe_title" (Pennsylvania Dutch, etc.)
        r'<h3[^>]*class="recipe_title"[^>]*>(.*?)</h3>',
        # Pattern 3: class="recipe"
        r'<(?:p|h[234])[^>]*class="recipe"[^>]*>(.*?)</(?:p|h[234])>',
    ]

    title_matches = []
    for pattern in patterns:
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if matches:
            title_matches = matches
            break

    for i, match in enumerate(title_matches):
        title_raw = clean_html(match.group(1))

        # Skip non-recipe content
        skip_words = ['contents', 'index', 'preface', 'introduction', 'soups', 'meats',
                      'fish', 'vegetables', 'desserts', 'sauces', 'salads', 'eggs',
                      'macaroni and other pastes', 'rice, etc']
        if any(skip in title_raw.lower() for skip in skip_words) and len(title_raw) < 30:
            continue

        if not title_raw or len(title_raw) > 150:
            continue

        # Get content until next title
        start_pos = match.end()
        if i + 1 < len(title_matches):
            end_pos = title_matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        # Find all paragraphs in this section
        para_pattern = r'<p[^>]*>(.*?)</p>'
        paragraphs = re.findall(para_pattern, recipe_content, re.DOTALL)

        ingredients = []
        instructions = []

        # Check for structured ingredient lists first (e.g., Pennsylvania Dutch format)
        ingredient_items = re.findall(r'<li[^>]*class="ingredient"[^>]*>(.*?)</li>', recipe_content, re.DOTALL)
        for item in ingredient_items:
            item_clean = clean_html(item)
            if item_clean:
                ing = parse_single_ingredient(item_clean)
                if ing:
                    ingredients.append(ing)

        for p in paragraphs:
            p_clean = clean_html(p)
            if not p_clean or len(p_clean) < 3:
                continue

            # Check if this looks like an ingredient list
            lines = [l.strip() for l in p.replace('<br', '\n<br').split('\n') if l.strip()]

            # If it has <br> tags and measurements, likely ingredients
            if '<br' in p and re.search(r'\d+\s*(cup|tablespoon|teaspoon|pound|ounce|quart)', p, re.I):
                for line in lines:
                    line_clean = clean_html(line)
                    if line_clean:
                        ing = parse_single_ingredient(line_clean)
                        if ing:
                            ingredients.append(ing)
            elif re.search(r'\d+\s*(cup|tablespoon|teaspoon|pound|ounce|quart)', p_clean, re.I) and len(p_clean) < 200:
                # Short paragraph with measurements - might be ingredients
                for line in p_clean.split('  '):
                    line = line.strip()
                    if line:
                        ing = parse_single_ingredient(line)
                        if ing:
                            ingredients.append(ing)
            else:
                # Instruction paragraph
                if len(p_clean) > 20:
                    instructions.append({"step": len(instructions) + 1, "text": p_clean})

        if not ingredients and not instructions:
            continue

        # Parse title
        title_clean, italian_name = parse_title(title_raw)
        recipe_id = create_recipe_id(title_clean)
        category = determine_category(title_clean)

        recipe = {
            "id": f"{recipe_id}-gutenberg",
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_clean.title(),
            "category": category,
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": f"Vintage Italian recipe{': ' + italian_name if italian_name else ''}",
            "servings_yield": "4 servings",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": [f"Original Italian: {italian_name}"] if italian_name else [],
            "tags": ["italian", "vintage", "public-domain"],
            "confidence": {
                "overall": "medium",
                "flags": ["vintage-recipe", "public-domain"]
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

    return recipes, book_title, book_author


def main():
    parser = argparse.ArgumentParser(description='Extract recipes from Project Gutenberg HTML')
    parser.add_argument('html_file', help='Path to HTML file')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--add', action='store_true', help='Add to recipes.json')
    args = parser.parse_args()

    html_path = Path(args.html_file)
    if not html_path.exists():
        print(f"Error: File not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    recipes, book_title, book_author = extract_recipes_from_html(html_path)

    print(f"Extracted {len(recipes)} recipes from '{book_title}' by {book_author}", file=sys.stderr)

    if args.dry_run:
        for i, recipe in enumerate(recipes[:5]):
            print(f"\n{'='*60}")
            print(f"Recipe {i+1}: {recipe['title']}")
            print(f"Category: {recipe['category']}")
            print(f"Ingredients ({len(recipe['ingredients'])}):")
            for ing in recipe['ingredients'][:5]:
                qty = f"{ing['quantity']} {ing['unit']}".strip()
                print(f"  - {qty} {ing['item']}" if qty else f"  - {ing['item']}")
            if len(recipe['ingredients']) > 5:
                print(f"  ... and {len(recipe['ingredients'])-5} more")
            print(f"Instructions: {len(recipe['instructions'])} steps")

        if len(recipes) > 5:
            print(f"\n... and {len(recipes)-5} more recipes")
    elif args.add:
        # Add to recipes.json
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
