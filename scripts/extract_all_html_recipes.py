#!/usr/bin/env python3
"""
Extract recipes from ALL Project Gutenberg HTML cookbook files.
Handles multiple formats and extracts tips/notes sections.

Usage:
    python scripts/extract_all_html_recipes.py --dry-run
    python scripts/extract_all_html_recipes.py --add
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
    """Parse recipe title, extracting parenthetical notes."""
    match = re.match(r'^(.+?)\s*\(([^)]+)\)\s*$', title_raw)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return title_raw.strip(), ""


def parse_single_ingredient(line):
    """Parse a single ingredient line."""
    line = line.strip()
    if not line or len(line) < 2:
        return None

    # Pattern with fractions and units
    pattern = r'^(\d+(?:[/-]\d+)?(?:\s*\d+/\d+)?|½|⅓|¼|⅔|¾|⅛)\s*(cups?|tablespoons?|teaspoons?|pounds?|ounces?|quarts?|pints?|tbsp\.?|tsp\.?|oz\.?|lb\.?|cloves?|slices?|pieces?|heads?|bunche?s?|small|medium|large|liberal|cans?|pkg\.?|packages?)?\s*(?:of\s+)?(.+)$'

    match = re.match(pattern, line, re.I)
    if match:
        quantity = match.group(1)
        unit = match.group(2) or ""
        item = match.group(3).strip()

        # Convert Unicode fractions
        frac_map = {'½': '1/2', '⅓': '1/3', '¼': '1/4', '⅔': '2/3', '¾': '3/4', '⅛': '1/8'}
        quantity = frac_map.get(quantity, quantity)

        # Normalize units
        unit_map = {
            'tablespoon': 'tbsp', 'tablespoons': 'tbsp', 'tbsp.': 'tbsp',
            'teaspoon': 'tsp', 'teaspoons': 'tsp', 'tsp.': 'tsp',
            'pound': 'lb', 'pounds': 'lb', 'lb.': 'lb',
            'ounce': 'oz', 'ounces': 'oz', 'oz.': 'oz',
            'cup': 'cup', 'cups': 'cup',
            'can': 'can', 'cans': 'can',
            'pkg.': 'pkg', 'package': 'pkg', 'packages': 'pkg',
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


def create_recipe_id(title, book_tag):
    """Create a URL-friendly recipe ID."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return f"{slug.strip('-')[:50]}-{book_tag}"


def determine_category(title):
    """Determine recipe category based on title."""
    title_lower = title.lower()

    if any(word in title_lower for word in ['soup', 'broth', 'chowder', 'bisque', 'stew', 'consomme']):
        return 'soups'
    elif any(word in title_lower for word in ['salad', 'slaw']):
        return 'salads'
    elif any(word in title_lower for word in ['cookie', 'cooky', 'cake', 'pie', 'tart', 'pudding', 'ice cream',
                                              'dessert', 'sweet', 'candy', 'fudge', 'brownies', 'bars']):
        return 'desserts'
    elif any(word in title_lower for word in ['bread', 'roll', 'muffin', 'biscuit', 'toast']):
        return 'breads'
    elif any(word in title_lower for word in ['egg', 'omelet', 'frittata', 'scrambled', 'poached']):
        return 'breakfast'
    elif any(word in title_lower for word in ['sauce', 'gravy', 'dressing']):
        return 'sides'
    elif any(word in title_lower for word in ['drink', 'beverage', 'punch', 'cocktail', 'tea', 'coffee']):
        return 'beverages'
    elif any(word in title_lower for word in ['appetizer', 'hors', 'canape', 'dip']):
        return 'appetizers'
    elif any(word in title_lower for word in ['vegetable', 'potato', 'bean', 'spinach', 'asparagus', 'carrot']):
        return 'sides'
    else:
        return 'mains'


def extract_betty_crocker_recipes(content, book_title, book_author):
    """Extract recipes from Betty Crocker format."""
    recipes = []
    tips = []

    # Find recipe blocks - they use <p class="recipe"> or <span class="recipe">
    recipe_pattern = r'<(?:p|span)[^>]*class="recipe"[^>]*>(.*?)</(?:p|span)>'

    matches = list(re.finditer(recipe_pattern, content, re.DOTALL | re.IGNORECASE))

    for i, match in enumerate(matches):
        title_raw = clean_html(match.group(1))
        title_raw = re.sub(r'^[★\*]+\s*', '', title_raw)  # Remove star prefix
        title_raw = re.sub(r'\s*\([^)]*Recipe\)\s*$', '', title_raw, flags=re.I)  # Remove "(KEY Recipe)"

        if not title_raw or len(title_raw) > 100 or len(title_raw) < 3:
            continue

        # Skip section headers
        if title_raw.upper() in ['DROP COOKIES', 'BAR COOKIES', 'MOLDED COOKIES', 'REFRIGERATOR COOKIES',
                                  'ROLLED COOKIES', 'PRESSED COOKIES', 'ALPHABETICAL INDEX']:
            continue

        # Get content until next recipe
        start_pos = match.end()
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        # Extract ingredients from <ul><li> tags
        ingredients = []
        li_items = re.findall(r'<li[^>]*>(.*?)</li>', recipe_content, re.DOTALL)
        for item in li_items:
            item_clean = clean_html(item)
            if item_clean:
                ing = parse_single_ingredient(item_clean)
                if ing:
                    ingredients.append(ing)

        # Extract instructions from <p> tags (not in ul)
        instructions = []
        # Get text between </ul> and next <ul> or end
        instruction_text = re.sub(r'<ul>.*?</ul>', '', recipe_content, flags=re.DOTALL)
        paras = re.findall(r'<p[^>]*>(.*?)</p>', instruction_text, re.DOTALL)

        for p in paras:
            p_clean = clean_html(p)
            if not p_clean or len(p_clean) < 10:
                continue
            # Skip metadata lines
            if p_clean.upper().startswith(('TEMPERATURE:', 'TIME:', 'AMOUNT:')):
                continue
            # Skip description lines in italics (they come after title)
            if '<i>' in p and len(p_clean) < 100:
                continue
            if p_clean and len(p_clean) > 15:
                instructions.append({"step": len(instructions) + 1, "text": p_clean})

        # Extract temperature, time, amount
        temp_match = re.search(r'TEMPERATURE[:\s]+(\d+°[^<.]+)', recipe_content, re.I)
        time_match = re.search(r'TIME[:\s]+[Bb]ake\s+(\d+[^<.]+)', recipe_content, re.I)
        amount_match = re.search(r'AMOUNT[:\s]+([^<.]+)', recipe_content, re.I)

        temperature = clean_html(temp_match.group(1)) if temp_match else ""
        cook_time = clean_html(time_match.group(1)) if time_match else ""
        servings = clean_html(amount_match.group(1)) if amount_match else ""

        if not ingredients:
            continue

        title_clean, note = parse_title(title_raw)
        recipe = {
            "id": create_recipe_id(title_clean, "betty-crocker"),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_clean.title(),
            "category": determine_category(title_clean),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": note or f"Classic cookie recipe from Betty Crocker",
            "servings_yield": servings or "varies",
            "prep_time": "",
            "cook_time": cook_time,
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": temperature,
            "pan_size": "",
            "notes": [note] if note else [],
            "tags": ["cookies", "vintage", "betty-crocker", "public-domain"],
            "confidence": {"overall": "medium", "flags": ["vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes, tips


def extract_standard_recipes(content, book_title, book_author, book_tag):
    """Extract recipes using standard patterns (margin-top, class=recipe_title, etc.)."""
    recipes = []

    patterns = [
        r'<(?:p|h[234])[^>]*style="margin-top:\s*2em"[^>]*>(.*?)</(?:p|h[234])>',
        r'<h3[^>]*class="recipe_title"[^>]*>(.*?)</h3>',
        r'<(?:p|h[234])[^>]*class="recipe"[^>]*>(.*?)</(?:p|h[234])>',
    ]

    title_matches = []
    for pattern in patterns:
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if matches:
            title_matches = matches
            break

    skip_words = ['contents', 'index', 'preface', 'introduction', 'chapter']

    for i, match in enumerate(title_matches):
        title_raw = clean_html(match.group(1))

        if any(skip in title_raw.lower() for skip in skip_words) and len(title_raw) < 30:
            continue

        if not title_raw or len(title_raw) > 150:
            continue

        start_pos = match.end()
        if i + 1 < len(title_matches):
            end_pos = title_matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        ingredients = []
        instructions = []

        # Check for structured ingredient lists
        ingredient_items = re.findall(r'<li[^>]*class="ingredient"[^>]*>(.*?)</li>', recipe_content, re.DOTALL)
        for item in ingredient_items:
            item_clean = clean_html(item)
            if item_clean:
                ing = parse_single_ingredient(item_clean)
                if ing:
                    ingredients.append(ing)

        # Parse paragraphs
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', recipe_content, re.DOTALL)

        for p in paragraphs:
            p_clean = clean_html(p)
            if not p_clean or len(p_clean) < 3:
                continue

            if '<br' in p and re.search(r'\d+\s*(cup|tablespoon|teaspoon|pound|ounce|quart)', p, re.I):
                lines = [l.strip() for l in p.replace('<br', '\n<br').split('\n') if l.strip()]
                for line in lines:
                    line_clean = clean_html(line)
                    if line_clean:
                        ing = parse_single_ingredient(line_clean)
                        if ing:
                            ingredients.append(ing)
            elif re.search(r'\d+\s*(cup|tablespoon|teaspoon|pound|ounce|quart)', p_clean, re.I) and len(p_clean) < 200:
                for line in p_clean.split('  '):
                    line = line.strip()
                    if line:
                        ing = parse_single_ingredient(line)
                        if ing:
                            ingredients.append(ing)
            else:
                if len(p_clean) > 20:
                    instructions.append({"step": len(instructions) + 1, "text": p_clean})

        if not ingredients and not instructions:
            continue

        title_clean, foreign_name = parse_title(title_raw)

        recipe = {
            "id": create_recipe_id(title_clean, book_tag),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_clean.title(),
            "category": determine_category(title_clean),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": f"Vintage recipe{': ' + foreign_name if foreign_name else ''}",
            "servings_yield": "4 servings",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": [f"Original: {foreign_name}"] if foreign_name else [],
            "tags": ["vintage", "public-domain"],
            "confidence": {"overall": "medium", "flags": ["vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes


def extract_carnation_recipes(content, book_title, book_author):
    """Extract recipes from Carnation Milk format (pg65501)."""
    recipes = []

    # Recipe titles are in h3 tags
    pattern = r'<h3[^>]*id="c\d+"[^>]*>(.*?)</h3>'
    matches = list(re.finditer(pattern, content, re.DOTALL))

    skip_titles = ['general direction', 'standard measurements', 'precautions', 'use of carnation',
                   'garnishes', 'making accurate', 'transcriber']

    for i, match in enumerate(matches):
        title_raw = clean_html(match.group(1))

        if any(skip in title_raw.lower() for skip in skip_titles):
            continue

        if not title_raw or len(title_raw) > 100 or len(title_raw) < 3:
            continue

        start_pos = match.end()
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        # Extract ingredients from <div class="verse"><p> or <p> with measurements
        ingredients = []

        verse_match = re.search(r'<div class="verse">(.*?)</div>', recipe_content, re.DOTALL)
        if verse_match:
            verse_content = verse_match.group(1)
            lines = re.findall(r'<p[^>]*>(.*?)</p>', verse_content, re.DOTALL)
            for line in lines:
                line_clean = clean_html(line)
                if line_clean:
                    ing = parse_single_ingredient(line_clean)
                    if ing:
                        ingredients.append(ing)

        # Extract instructions
        instructions = []
        paras = re.findall(r'<p[^>]*>(.*?)</p>', recipe_content, re.DOTALL)
        for p in paras:
            p_clean = clean_html(p)
            # Skip if it looks like ingredients
            if re.match(r'^\d+', p_clean) and len(p_clean) < 60:
                continue
            if p_clean and len(p_clean) > 30:
                instructions.append({"step": len(instructions) + 1, "text": p_clean})

        if not ingredients:
            continue

        recipe = {
            "id": create_recipe_id(title_raw, "carnation"),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_raw.title(),
            "category": determine_category(title_raw),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": "Vintage recipe using Carnation Milk",
            "servings_yield": "",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": [],
            "tags": ["vintage", "carnation", "public-domain"],
            "confidence": {"overall": "medium", "flags": ["vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes


def extract_tips_section(content, book_title):
    """Extract general cooking tips from the book."""
    tips = []

    # Look for tips sections
    tip_patterns = [
        (r'<h2[^>]*>.*?GENERAL DIRECTION.*?</h2>(.*?)(?=<h2|$)', 'General Directions'),
        (r'<h2[^>]*>.*?How to Get PERFECT.*?</h2>(.*?)(?=<h2|$)', 'Tips for Success'),
        (r'<h2[^>]*>.*?HOW WE MEASURE.*?</h2>(.*?)(?=<h2|$)', 'Measurement Tips'),
        (r'<h3[^>]*>.*?Garnishes.*?</h3>(.*?)(?=<h3|$)', 'Garnish Ideas'),
    ]

    for pattern, category in tip_patterns:
        matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
        for match in matches:
            paras = re.findall(r'<p[^>]*>(.*?)</p>', match, re.DOTALL)
            for p in paras:
                p_clean = clean_html(p)
                if p_clean and len(p_clean) > 30:
                    tips.append({
                        "category": category,
                        "source": book_title,
                        "tip": p_clean
                    })

    return tips


def extract_h3_italic_recipes(content, book_title, book_author, book_tag):
    """Extract recipes with h3 italic titles and verse div ingredients (Cottage Cheese, etc.)."""
    recipes = []

    # Recipe titles in h3 with italic text
    pattern = r'<h3[^>]*>\s*<i>([^<]+)</i>\s*</h3>'
    matches = list(re.finditer(pattern, content, re.DOTALL))

    skip_titles = ['salads', 'appetizers', 'breads', 'main dishes', 'desserts', 'transcriber']

    for i, match in enumerate(matches):
        title_raw = clean_html(match.group(1))

        if any(skip in title_raw.lower() for skip in skip_titles):
            continue

        if not title_raw or len(title_raw) > 100 or len(title_raw) < 3:
            continue

        start_pos = match.end()
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        # Extract ingredients from <div class="verse"><p class="t0">
        ingredients = []
        verse_match = re.search(r'<div class="verse">(.*?)</div>', recipe_content, re.DOTALL)
        if verse_match:
            verse_content = verse_match.group(1)
            lines = re.findall(r'<p[^>]*>(.*?)</p>', verse_content, re.DOTALL)
            for line in lines:
                line_clean = clean_html(line)
                if line_clean:
                    ing = parse_single_ingredient(line_clean)
                    if ing:
                        ingredients.append(ing)

        # Extract instructions from paragraphs after the verse
        instructions = []
        # Remove the verse div to get just the instruction paragraphs
        instruction_content = re.sub(r'<div class="verse">.*?</div>', '', recipe_content, flags=re.DOTALL)
        paras = re.findall(r'<p[^>]*>(.*?)</p>', instruction_content, re.DOTALL)
        for p in paras:
            p_clean = clean_html(p)
            if p_clean and len(p_clean) > 20 and not p_clean.startswith('Serves'):
                instructions.append({"step": len(instructions) + 1, "text": p_clean})

        # Extract servings
        servings_match = re.search(r'Serves\s+(\d+)', recipe_content, re.I)
        servings = f"{servings_match.group(1)} servings" if servings_match else ""

        if not ingredients:
            continue

        recipe = {
            "id": create_recipe_id(title_raw, book_tag),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_raw.title(),
            "category": determine_category(title_raw),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": "Vintage recipe",
            "servings_yield": servings,
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": [],
            "tags": ["vintage", "public-domain"],
            "confidence": {"overall": "medium", "flags": ["vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes


def extract_h3_plain_recipes(content, book_title, book_author, book_tag):
    """Extract recipes with plain h3 titles (no italic) and verse div ingredients."""
    recipes = []

    # Recipe titles in h3 with id (plain text, like <h3 id="c3">GLAZED HAM</h3>)
    pattern = r'<h3[^>]*id="c\d+"[^>]*>([^<]+)</h3>'
    matches = list(re.finditer(pattern, content, re.DOTALL))

    skip_titles = ['meats', 'vegetables', 'cakes', 'cookies', 'pies', 'desserts',
                   'breads', 'toppings', 'frostings', 'sauces', 'molasses', 'transcriber']

    for i, match in enumerate(matches):
        title_raw = clean_html(match.group(1))

        if any(skip == title_raw.lower() for skip in skip_titles):
            continue

        if not title_raw or len(title_raw) > 100 or len(title_raw) < 3:
            continue

        start_pos = match.end()
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        recipe_content = content[start_pos:end_pos]

        # Extract ingredients from <div class="verse"><p class="t0">
        ingredients = []
        # There may be multiple verse divs (for sub-recipes like "Topping" and "Ham Loaf")
        verse_matches = re.findall(r'<div class="verse">(.*?)</div>', recipe_content, re.DOTALL)
        for verse_content in verse_matches:
            lines = re.findall(r'<p[^>]*>(.*?)</p>', verse_content, re.DOTALL)
            for line in lines:
                line_clean = clean_html(line)
                if line_clean:
                    ing = parse_single_ingredient(line_clean)
                    if ing:
                        ingredients.append(ing)

        # Extract instructions from paragraphs after the verse
        instructions = []
        # Remove all verse divs to get just the instruction paragraphs
        instruction_content = re.sub(r'<div class="verse">.*?</div>', '', recipe_content, flags=re.DOTALL)
        paras = re.findall(r'<p[^>]*>(.*?)</p>', instruction_content, re.DOTALL)
        for p in paras:
            p_clean = clean_html(p)
            # Skip sub-section headers like "Topping" or "Ham Loaf"
            if p_clean and len(p_clean) > 20 and not p_clean.startswith('YIELD:'):
                instructions.append({"step": len(instructions) + 1, "text": p_clean})

        # Extract yield
        yield_match = re.search(r'YIELD:\s*([^<.]+)', recipe_content, re.I)
        servings = clean_html(yield_match.group(1)) if yield_match else ""

        # Extract temperature
        temp_match = re.search(r'(\d+)°\s*F\.?', recipe_content)
        temperature = f"{temp_match.group(1)}°F" if temp_match else ""

        if not ingredients:
            continue

        recipe = {
            "id": create_recipe_id(title_raw, book_tag),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_raw.title(),
            "category": determine_category(title_raw),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": "Vintage recipe",
            "servings_yield": servings,
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": temperature,
            "pan_size": "",
            "notes": [],
            "tags": ["vintage", "public-domain"],
            "confidence": {"overall": "medium", "flags": ["vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes


def extract_old_south_recipes(content, book_title, book_author):
    """Extract recipes from Dishes & Beverages of the Old South format (italic title with colon)."""
    recipes = []

    # Recipe pattern: <p><i>Recipe Name:</i> (instructions follow)
    pattern = r'<p><i>([^<:]+):</i>\s*([^<]+(?:<[^>]+>[^<]*)*)</p>'
    matches = list(re.finditer(pattern, content, re.DOTALL))

    for match in matches:
        title_raw = clean_html(match.group(1))
        instructions_raw = clean_html(match.group(2))

        if not title_raw or len(title_raw) > 60 or len(title_raw) < 3:
            continue

        # Skip non-recipe content
        skip_words = ['note', 'saving your', 'illustration']
        if any(skip in title_raw.lower() for skip in skip_words):
            continue

        # Parse the paragraph for ingredients and instructions
        # These are narrative-style recipes, so we keep the whole text as instructions
        instructions = [{"step": 1, "text": instructions_raw}]

        # Try to extract ingredient-like items from the text
        ingredients = []
        # Look for patterns like "two cups", "half a cup", "a pinch of salt"
        ing_patterns = [
            r'(\d+(?:\s*\d+/\d+)?)\s+(cups?|tablespoons?|teaspoons?|pounds?|pints?)\s+(?:of\s+)?([a-z\s]+?)(?:,|\.|\s+and)',
            r'(half\s+a|a|one|two|three|four)\s+(cup|tablespoon|teaspoon|pound|pint)\s+(?:of\s+)?([a-z\s]+?)(?:,|\.|\s+and)',
        ]
        for ing_pattern in ing_patterns:
            for ing_match in re.finditer(ing_pattern, instructions_raw, re.I):
                quantity = ing_match.group(1)
                unit = ing_match.group(2)
                item = ing_match.group(3).strip()
                if item and len(item) < 30:
                    ingredients.append({"item": item, "quantity": quantity, "unit": unit, "prep_note": ""})

        recipe = {
            "id": create_recipe_id(title_raw, "old-south"),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": title_raw.title(),
            "category": determine_category(title_raw),
            "attribution": book_author,
            "source_note": f"{book_title} (Project Gutenberg, public domain)",
            "description": "Classic Southern recipe from the Old South",
            "servings_yield": "",
            "prep_time": "",
            "cook_time": "",
            "total_time": "",
            "ingredients": ingredients,
            "instructions": instructions,
            "temperature": "",
            "pan_size": "",
            "notes": ["Recipe written in narrative style - quantities may be approximate"],
            "tags": ["vintage", "southern", "public-domain"],
            "confidence": {"overall": "low", "flags": ["narrative-style", "vintage-recipe"]},
            "image_refs": [],
            "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": ["all"], "assumptions": []}
        }
        recipes.append(recipe)

    return recipes


def extract_from_file(html_file):
    """Extract all recipes and tips from an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get book metadata
    title_match = re.search(r'<meta name="dc.title" content="([^"]+)"', content)
    book_title = title_match.group(1) if title_match else Path(html_file).stem
    book_title = unescape(book_title).replace('&#10;', ' - ')

    author_match = re.search(r'<meta name="dc.creator" content="([^"]+)"', content)
    book_author = author_match.group(1).split(',')[0] if author_match else ""

    filename = Path(html_file).name
    recipes = []
    tips = []

    # Use appropriate extractor based on book
    if 'pg72443' in filename:  # Betty Crocker
        recipes, tips = extract_betty_crocker_recipes(content, book_title, book_author)
    elif 'pg65501' in filename:  # Carnation/My Hundred Favorite Recipes
        recipes = extract_carnation_recipes(content, book_title, book_author)
    elif 'pg65327' in filename:  # Cottage Cheese Recipe Book
        recipes = extract_h3_italic_recipes(content, book_title, book_author, "cottage-cheese")
    elif 'pg65507' in filename:  # Grandma's Recipes (plain h3 titles)
        recipes = extract_h3_plain_recipes(content, book_title, book_author, "grandmas-molasses")
    elif 'pg65793' in filename:  # International Harvester
        recipes = extract_h3_plain_recipes(content, book_title, book_author, "harvester")
    elif 'pg28491' in filename:  # Dishes & Beverages of the Old South
        recipes = extract_old_south_recipes(content, book_title, book_author)
    else:
        # Try standard extraction
        book_tag = filename.replace('-images.html', '').replace('pg', 'gutenberg-')
        recipes = extract_standard_recipes(content, book_title, book_author, book_tag)

    # Extract tips
    tips.extend(extract_tips_section(content, book_title))

    return recipes, tips, book_title


def main():
    parser = argparse.ArgumentParser(description='Extract recipes from Gutenberg HTML files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be extracted')
    parser.add_argument('--add', action='store_true', help='Add recipes to recipes.json')
    parser.add_argument('files', nargs='*', default=['all/HTML/pg*.html'], help='Files to process')
    args = parser.parse_args()

    import glob

    all_recipes = []
    all_tips = []

    for pattern in args.files:
        for html_file in glob.glob(pattern):
            print(f"\nProcessing: {html_file}")
            recipes, tips, book_title = extract_from_file(html_file)
            print(f"  Found {len(recipes)} recipes, {len(tips)} tips from '{book_title}'")
            all_recipes.extend(recipes)
            all_tips.extend(tips)

    print(f"\n{'='*60}")
    print(f"Total: {len(all_recipes)} recipes, {len(all_tips)} tips")

    if args.dry_run:
        for r in all_recipes[:10]:
            print(f"\n  {r['title']} ({r['source_note'][:30]}...)")
            print(f"    Ingredients: {len(r['ingredients'])}, Instructions: {len(r['instructions'])}")
        if len(all_recipes) > 10:
            print(f"\n  ... and {len(all_recipes) - 10} more recipes")

    if args.add:
        # Load existing recipes
        recipes_file = Path('data/recipes.json')
        with open(recipes_file, 'r') as f:
            data = json.load(f)

        existing_recipes = data.get('recipes', [])
        existing_ids = {r['id'] for r in existing_recipes if isinstance(r, dict)}

        # Add new recipes (avoid duplicates)
        added = 0
        for recipe in all_recipes:
            if recipe['id'] not in existing_ids:
                existing_recipes.append(recipe)
                existing_ids.add(recipe['id'])
                added += 1

        data['recipes'] = existing_recipes
        data['meta']['total_recipes'] = len(existing_recipes)
        data['meta']['last_updated'] = '2026-01-13'

        with open(recipes_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"\nAdded {added} new recipes to recipes.json")
        print(f"Total recipes now: {len(existing_recipes)}")

        # Save tips to separate file
        if all_tips:
            tips_file = Path('data/cooking_tips.json')
            with open(tips_file, 'w') as f:
                json.dump(all_tips, f, indent=2)
            print(f"Saved {len(all_tips)} tips to cooking_tips.json")


if __name__ == '__main__':
    main()
