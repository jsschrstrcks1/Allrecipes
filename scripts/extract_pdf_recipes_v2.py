#!/usr/bin/env python3
"""
Enhanced PDF recipe extraction with intelligent parsing.
Handles vintage cookbook formatting and infers missing quantities.

Usage:
    python scripts/extract_pdf_recipes_v2.py all/PDFs/cookbook.pdf --dry-run
    python scripts/extract_pdf_recipes_v2.py --all --dry-run
    python scripts/extract_pdf_recipes_v2.py --all --add
"""

import re
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 not installed. Run: pip install PyPDF2", file=sys.stderr)
    sys.exit(1)


# Common ingredient quantity defaults (when missing, for 4 servings)
DEFAULT_QUANTITIES = {
    'salt': ('1', 'tsp'),
    'pepper': ('1/4', 'tsp'),
    'butter': ('2', 'tbsp'),
    'sugar': ('1/4', 'cup'),
    'flour': ('1', 'cup'),
    'milk': ('1', 'cup'),
    'egg': ('1', ''),
    'eggs': ('2', ''),
    'onion': ('1', 'medium'),
    'garlic': ('2', 'cloves'),
    'oil': ('2', 'tbsp'),
    'water': ('1', 'cup'),
    'baking powder': ('1', 'tsp'),
    'baking soda': ('1/2', 'tsp'),
    'vanilla': ('1', 'tsp'),
    'cinnamon': ('1/2', 'tsp'),
    'nutmeg': ('1/4', 'tsp'),
}


def extract_text_from_pdf(pdf_path, max_pages=None):
    """Extract text from PDF file."""
    text_pages = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            if max_pages:
                num_pages = min(num_pages, max_pages)

            for i in range(num_pages):
                page = reader.pages[i]
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(page_text)
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        return []
    return text_pages


def fix_vintage_text(text):
    """Fix common vintage OCR/formatting issues."""
    # Fix run-together words with measurements
    text = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', text)  # "1cup" -> "1 cup"
    text = re.sub(r'([a-z])(\d)', r'\1 \2', text)  # "cup1" -> "cup 1"

    # Fix common OCR errors
    text = text.replace('J4', '1/4')
    text = text.replace('J^', '1/2')
    text = text.replace('1Q', '1')
    text = text.replace('Qgg', 'egg')

    # Fix horizontal whitespace only (preserve newlines!)
    text = re.sub(r'[ \t]+', ' ', text)

    return text


def parse_ingredient_line(line):
    """Parse an ingredient line, inferring quantities if missing."""
    line = fix_vintage_text(line.strip())
    if not line or len(line) < 2:
        return None

    # Skip obvious non-ingredients
    skip_patterns = ['method', 'directions', 'instructions', 'serves', 'yield',
                     'preheat', 'oven']
    if any(line.lower().startswith(skip) for skip in skip_patterns):
        return None

    # Normalize common abbreviations with periods
    line = re.sub(r'\btsp\.', 'tsp', line)
    line = re.sub(r'\btbsp\.', 'tbsp', line)
    line = re.sub(r'\boz\.', 'oz', line)
    line = re.sub(r'\blbs?\.', 'lb', line)
    line = re.sub(r'\bfl\.\s*oz', 'fl oz', line)
    line = re.sub(r'\bpkg\.', 'pkg', line)
    line = re.sub(r'\bc\.(?=\s)', 'cup', line)
    line = re.sub(r'\bT\.(?=\s)', 'tbsp', line)
    line = re.sub(r'\bt\.(?=\s)', 'tsp', line)

    # Pattern: quantity unit item (prep note)
    patterns = [
        # Standard: 2 cups flour, 1-2 sticks butter
        r'^(\d+(?:[/-]\d+)?(?:\s*\d+/\d+)?)\s*(cups?|tablespoons?|teaspoons?|tbsp|tsp|pounds?|lb|ounces?|oz|fl\s*oz|quarts?|qt|pints?|pt|cans?|packages?|pkg|bunches?|heads?|stalks?|cloves?|slices?|pieces?|medium|med|large|lg|small|sm|sticks?|bottles?|bags?|jars?)?\s*\.?\s*(?:of\s+)?(.+?)(?:\s*,\s*(.+))?$',
        # Fraction first: 1/2 cup sugar
        r'^(\d+/\d+)\s*(cups?|tablespoons?|teaspoons?|tbsp|tsp|pounds?|lb|ounces?|oz|fl\s*oz)?\s*\.?\s*(?:of\s+)?(.+?)(?:\s*,\s*(.+))?$',
    ]

    for pattern in patterns:
        match = re.match(pattern, line, re.I)
        if match:
            quantity = match.group(1)
            unit = match.group(2) or ""
            item = match.group(3).strip()
            prep_note = match.group(4).strip() if match.group(4) else ""

            # Clean up item (remove leading periods/spaces)
            item = re.sub(r'^[\.\s]+', '', item)

            # Normalize units
            unit_map = {
                'tablespoon': 'tbsp', 'tablespoons': 'tbsp',
                'teaspoon': 'tsp', 'teaspoons': 'tsp',
                'pound': 'lb', 'pounds': 'lb',
                'ounce': 'oz', 'ounces': 'oz',
                'cup': 'cup', 'cups': 'cup',
                'can': 'can', 'cans': 'can',
                'package': 'pkg', 'packages': 'pkg',
                'stick': 'stick', 'sticks': 'stick',
                'bottle': 'bottle', 'bottles': 'bottle',
                'bag': 'bag', 'bags': 'bag',
                'fl oz': 'fl oz',
                'med': 'medium', 'lg': 'large', 'sm': 'small',
            }
            unit = unit_map.get(unit.lower(), unit.lower()) if unit else ""

            if item:  # Only return if we have an item
                return {"item": item, "quantity": quantity, "unit": unit, "prep_note": prep_note}

    # No quantity found - try to infer from defaults
    item_lower = line.lower()
    for key, (qty, unit) in DEFAULT_QUANTITIES.items():
        if key in item_lower:
            return {"item": line, "quantity": qty, "unit": unit, "prep_note": "[quantity inferred]"}

    # Return as-is with empty quantity (for items like "Salt and pepper to taste")
    if len(line) > 3 and not any(c.isdigit() for c in line[:5]):
        return {"item": line, "quantity": "", "unit": "", "prep_note": ""}

    return None


def extract_recipe_blocks(text):
    """Extract recipe blocks from text."""
    recipes = []

    # Normalize whitespace in text
    text = re.sub(r'[ \t]+', ' ', text)  # Collapse horizontal whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Normalize paragraph breaks

    # Try splitting by dashed line separators (common in obooko books)
    if '----' in text:
        blocks = re.split(r'-{5,}\s*-*', text)
        for block in blocks:
            recipe = parse_recipe_block(block.strip())
            if recipe:
                recipes.append(recipe)
        if recipes:
            return recipes

    # Fall back to title-based extraction
    title_patterns = [
        # ALL CAPS TITLE (common in vintage cookbooks)
        r'\n\s*([A-Z][A-Z\s\'\-\(\)]{4,60})\s*\n',
        # Title with all caps words
        r'\n\s*([A-Z]{2,}(?:\s+[A-Z]{2,})+)\s*\n',
    ]

    all_titles = []
    for pattern in title_patterns:
        for match in re.finditer(pattern, text):
            title = match.group(1).strip()
            # Skip non-recipe titles
            skip_words = ['contents', 'index', 'chapter', 'introduction', 'preface',
                         'page', 'copyright', 'table', 'foreword', 'acknowledgment',
                         'recipes', 'cookbook', 'book']
            if any(skip == title.lower() for skip in skip_words):
                continue
            if len(title) < 4 or len(title) > 80:
                continue
            all_titles.append((match.start(), title))

    # Sort by position and remove duplicates
    all_titles.sort(key=lambda x: x[0])
    seen_titles = set()
    unique_titles = []
    for pos, title in all_titles:
        if title.lower() not in seen_titles:
            seen_titles.add(title.lower())
            unique_titles.append((pos, title))

    # Extract content between titles
    for i, (pos, title) in enumerate(unique_titles):
        next_pos = unique_titles[i + 1][0] if i + 1 < len(unique_titles) else len(text)
        content = text[pos:next_pos]
        recipe = parse_recipe_block(content)
        if recipe:
            recipes.append(recipe)

    return recipes


def parse_recipe_block(block):
    """Parse a single recipe block into structured data."""
    if not block or len(block) < 20:
        return None

    lines = block.split('\n')
    lines = [l.strip() for l in lines if l.strip()]

    if not lines:
        return None

    # Find the title - might not be the first line (could be a header)
    title = None
    title_idx = 0

    # Skip common headers (book titles, page headers)
    header_patterns = [
        r'^\d+\s+\w+\s+recipes?$',  # "300 Chicken Recipes"
        r'^recipes?$',
        r'^page\s+\d+',
        r'^\d+$',  # Just a page number
    ]

    for i, line in enumerate(lines[:3]):  # Check first 3 lines
        is_header = any(re.match(p, line, re.I) for p in header_patterns)
        if not is_header and len(line) > 3:
            # Check if this looks like a recipe title (ALL CAPS or Title Case, not too long)
            if line.isupper() or (line[0].isupper() and len(line) < 60):
                title = line
                title_idx = i
                break

    if not title:
        title = lines[0]
        title_idx = 0

    # Clean up title
    title = re.sub(r'\s+', ' ', title)
    if title.isupper():
        title = title.title()

    # Skip non-recipe blocks
    skip_words = ['contents', 'index', 'chapter', 'introduction', 'preface',
                 'copyright', 'table of', 'foreword', 'acknowledgment',
                 'chicken recipes', 'beef recipes', 'pork recipes']
    if any(skip in title.lower() for skip in skip_words):
        return None

    # Parse remaining lines (after title)
    ingredients = []
    instructions = []
    in_instructions = False

    for line in lines[title_idx + 1:]:
        line = line.strip()
        if not line:
            continue

        # Skip page headers that appear mid-block
        if re.match(r'^\d+\s+\w+\s+recipes?$', line, re.I):
            continue

        # Check for instruction markers
        if any(word in line.lower() for word in ['method:', 'directions:', 'instructions:', 'procedure:']):
            in_instructions = True
            continue

        # Ingredient patterns: starts with number, fraction, or measurement word
        is_ingredient = (
            re.match(r'^[\d½¼¾⅓⅔]', line) or
            re.match(r'^\d+[/-]\d+', line) or
            re.match(r'^(one|two|three|four|five|six|small|large|medium)\s', line.lower())
        )

        # Lines with lots of periods or long sentences are likely instructions
        instruction_words = ['bake', 'cook', 'mix', 'stir', 'combine', 'serve', 'preheat', 'heat', 'pour', 'drain', 'fry', 'boil', 'simmer']
        line_lower = line.lower()
        has_instruction_word = any(re.search(r'\b' + word + r'\b', line_lower) for word in instruction_words)
        is_instruction = (
            len(line) > 80 or
            line.count('.') >= 2 or
            has_instruction_word
        )

        if not in_instructions and is_ingredient and not is_instruction:
            ing = parse_ingredient_line(line)
            if ing:
                ingredients.append(ing)
        elif is_instruction or (len(ingredients) > 0 and len(line) > 40):
            in_instructions = True
            if len(line) > 15:
                instructions.append(line)

    # Need at least 2 ingredients to be a valid recipe
    if len(ingredients) < 2:
        return None

    return {
        'title': title,
        'ingredients': ingredients,
        'instructions': instructions
    }


def determine_category(title):
    """Determine recipe category based on title."""
    title_lower = title.lower()

    categories = {
        'soups': ['soup', 'broth', 'chowder', 'stew', 'bisque', 'gumbo'],
        'salads': ['salad', 'slaw'],
        'desserts': ['cake', 'pie', 'cookie', 'pudding', 'dessert', 'sweet', 'candy',
                    'ice cream', 'custard', 'tart', 'cobbler', 'brownie', 'fudge'],
        'breads': ['bread', 'roll', 'muffin', 'biscuit', 'scone', 'cornbread', 'toast'],
        'breakfast': ['egg', 'omelet', 'omelette', 'breakfast', 'pancake', 'waffle', 'french toast'],
        'sides': ['sauce', 'gravy', 'dressing', 'pickle', 'preserve', 'jam', 'jelly',
                 'vegetable', 'potato', 'rice', 'beans'],
        'beverages': ['drink', 'beverage', 'punch', 'tea', 'coffee', 'lemonade', 'cider'],
        'appetizers': ['appetizer', 'dip', 'spread', 'canape', 'hors d\'oeuvre'],
    }

    for category, keywords in categories.items():
        if any(word in title_lower for word in keywords):
            return category

    return 'mains'


def create_recipe_id(title, source):
    """Create a URL-friendly recipe ID."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)

    # Add source identifier
    source_short = re.sub(r'[^a-z0-9]', '', source.lower())[:10]
    return f"{slug.strip('-')[:35]}-{source_short}"


def process_pdf(pdf_path, dry_run=False):
    """Process a single PDF and extract recipes."""
    path = Path(pdf_path)
    source_name = path.stem.replace('_', ' ').replace('-', ' ')
    source_name = re.sub(r'\s+', ' ', source_name).strip()

    print(f"Processing: {path.name}", file=sys.stderr)

    pages = extract_text_from_pdf(pdf_path)
    if not pages:
        print(f"  No text extracted", file=sys.stderr)
        return []

    # Combine all pages
    full_text = "\n\n".join(pages)
    full_text = fix_vintage_text(full_text)

    # Extract recipes
    raw_recipes = extract_recipe_blocks(full_text)
    print(f"  Found {len(raw_recipes)} potential recipes", file=sys.stderr)

    recipes = []
    for raw in raw_recipes:
        # Create full recipe object
        recipe_id = create_recipe_id(raw['title'], source_name)
        category = determine_category(raw['title'])

        # Format instructions
        instructions = []
        for i, text in enumerate(raw['instructions'][:10], 1):
            instructions.append({"step": i, "text": text})

        if not instructions:
            instructions = [{"step": 1, "text": "Method not fully extracted - see original source."}]

        recipe = {
            "id": recipe_id,
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": raw['title'],
            "category": category,
            "attribution": "",
            "source_note": f"{source_name.title()} (PDF cookbook)",
            "description": f"Vintage recipe from {source_name.title()}",
            "servings_yield": "4 servings",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": raw['ingredients'],
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": [],
            "tags": ["vintage", "pdf-extracted"],
            "confidence": {
                "overall": "medium",
                "flags": ["pdf-extraction"]
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


def main():
    parser = argparse.ArgumentParser(description='Extract recipes from PDF cookbooks')
    parser.add_argument('pdf_file', nargs='?', help='Path to PDF file')
    parser.add_argument('--all', action='store_true', help='Process all PDFs in all/PDFs/')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--add', action='store_true', help='Add to recipes.json')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of PDFs to process')
    args = parser.parse_args()

    if args.all:
        pdf_dir = Path('all/PDFs')
        pdf_files = sorted(pdf_dir.glob('*.pdf'))
        if args.limit:
            pdf_files = pdf_files[:args.limit]
    elif args.pdf_file:
        pdf_files = [Path(args.pdf_file)]
    else:
        parser.print_help()
        sys.exit(1)

    all_recipes = []
    for pdf_path in pdf_files:
        if not pdf_path.exists():
            print(f"File not found: {pdf_path}", file=sys.stderr)
            continue

        recipes = process_pdf(pdf_path, args.dry_run)
        all_recipes.extend(recipes)

    print(f"\nTotal recipes extracted: {len(all_recipes)}", file=sys.stderr)

    if args.dry_run:
        # Show samples
        for i, recipe in enumerate(all_recipes[:10]):
            print(f"\n{'='*60}")
            print(f"Recipe {i+1}: {recipe['title']}")
            print(f"Source: {recipe['source_note']}")
            print(f"Category: {recipe['category']}")
            print(f"Ingredients ({len(recipe['ingredients'])}):")
            for ing in recipe['ingredients'][:6]:
                qty = f"{ing['quantity']} {ing['unit']}".strip()
                print(f"  - {qty} {ing['item']}" if qty else f"  - {ing['item']}")
            if len(recipe['ingredients']) > 6:
                print(f"  ... and {len(recipe['ingredients'])-6} more")

        if len(all_recipes) > 10:
            print(f"\n... and {len(all_recipes)-10} more recipes")

    elif args.add and all_recipes:
        recipes_file = Path('data/recipes.json')
        with open(recipes_file, 'r') as f:
            data = json.load(f)

        existing_ids = {r['id'] for r in data['recipes']}
        added = 0
        for recipe in all_recipes:
            if recipe['id'] not in existing_ids:
                data['recipes'].append(recipe)
                existing_ids.add(recipe['id'])
                added += 1

        data['meta']['total_recipes'] = len(data['recipes'])
        data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        with open(recipes_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Added {added} new recipes to recipes.json")
    else:
        print(json.dumps(all_recipes[:5], indent=2))


if __name__ == '__main__':
    main()
