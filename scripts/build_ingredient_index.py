#!/usr/bin/env python3
"""
Build Ingredient Index - Create searchable ingredient index from recipes.json

This script:
1. Reads the main recipes.json file
2. Extracts and normalizes all ingredients
3. Creates ingredient-index.json mapping ingredients to recipe IDs

Usage:
    python scripts/build_ingredient_index.py [--dry-run]
"""

import json
import os
import re
import sys
from datetime import datetime
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
INDEX_FILE = os.path.join(DATA_DIR, 'ingredient-index.json')


def normalize_ingredient(item):
    """
    Normalize an ingredient name for indexing.
    - Lowercase
    - Remove parenthetical notes
    - Remove common modifiers
    - Singularize common plurals
    """
    if not item:
        return None

    # Lowercase
    item = item.lower().strip()

    # Remove parenthetical content
    item = re.sub(r'\([^)]*\)', '', item).strip()

    # Remove common preparation words at start
    prep_words = ['fresh', 'frozen', 'canned', 'dried', 'chopped', 'diced',
                  'minced', 'sliced', 'grated', 'shredded', 'crushed',
                  'ground', 'whole', 'large', 'medium', 'small', 'thin',
                  'thick', 'cooked', 'raw', 'hot', 'cold', 'warm', 'chilled',
                  'softened', 'melted', 'room temperature', 'packed']

    words = item.split()
    while words and words[0] in prep_words:
        words.pop(0)
    item = ' '.join(words)

    # Common singularization
    if item.endswith('ies') and len(item) > 4:
        item = item[:-3] + 'y'  # berries -> berry
    elif item.endswith('oes'):
        item = item[:-2]  # tomatoes -> tomato
    elif item.endswith('es') and not item.endswith('cheese'):
        item = item[:-2]  # peaches -> peach
    elif item.endswith('s') and not item.endswith(('ss', 'us', 'is')):
        item = item[:-1]  # eggs -> egg

    return item if item else None


def extract_base_ingredient(item):
    """
    Extract the base ingredient, removing brand names and specific varieties.
    """
    if not item:
        return None

    # Common brand removals
    item = re.sub(r'\b(brand|style)\b', '', item, flags=re.IGNORECASE)

    # Keep the main ingredient word(s)
    return item.strip()


def load_recipes():
    """Load all recipes from main recipes.json"""
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('recipes', [])


def build_index(dry_run=False):
    """Build ingredient index from recipes"""
    print(f"Loading recipes from {RECIPES_FILE}...")
    recipes = load_recipes()
    print(f"Loaded {len(recipes)} recipes")

    # Map: normalized ingredient -> list of recipe IDs
    ingredient_map = defaultdict(set)

    # Also track original forms for display
    original_forms = defaultdict(set)

    for recipe in recipes:
        recipe_id = recipe.get('id')
        if not recipe_id:
            continue

        ingredients = recipe.get('ingredients', [])
        for ing in ingredients:
            item = ing.get('item', '')
            if not item:
                continue

            # Normalize for indexing
            normalized = normalize_ingredient(item)
            if normalized:
                ingredient_map[normalized].add(recipe_id)
                original_forms[normalized].add(item.lower())

    # Convert sets to sorted lists
    index_entries = []
    for ingredient in sorted(ingredient_map.keys()):
        if ingredient:  # Skip empty
            entry = {
                'ingredient': ingredient,
                'variants': sorted(original_forms[ingredient]),
                'recipe_count': len(ingredient_map[ingredient]),
                'recipe_ids': sorted(ingredient_map[ingredient])
            }
            index_entries.append(entry)

    # Create index data
    index_data = {
        'meta': {
            'title': 'Ingredient Index',
            'description': 'Index of ingredients mapped to recipes',
            'total_ingredients': len(index_entries),
            'total_recipes': len(recipes),
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'version': '1.0.0'
        },
        'ingredients': index_entries
    }

    # Stats
    print(f"\nIngredient Index Statistics:")
    print(f"  Unique ingredients: {len(index_entries)}")
    print(f"  Total recipes indexed: {len(recipes)}")

    # Top 20 most common ingredients
    top_ingredients = sorted(index_entries, key=lambda x: x['recipe_count'], reverse=True)[:20]
    print(f"\nTop 20 most common ingredients:")
    for ing in top_ingredients:
        print(f"  {ing['ingredient']}: {ing['recipe_count']} recipes")

    if dry_run:
        print(f"\n[DRY RUN] Would write index with {len(index_entries)} ingredients")
        return

    # Write index file
    print(f"\nWriting index to {INDEX_FILE}...")
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"Ingredient index created successfully!")


if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    build_index(dry_run=dry_run)
