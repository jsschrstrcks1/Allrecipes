#!/usr/bin/env python3
"""
Build an ingredient index from all recipe files.

Creates an index mapping ingredients to the recipes that use them,
enabling quick lookups for "what can I make with X?" queries.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def normalize_ingredient(ingredient: str) -> str:
    """Normalize an ingredient name for indexing."""
    # Remove quantities and measurements
    # Extract the main ingredient name
    ingredient = ingredient.lower().strip()

    # Remove common measurements
    measurements = [
        r'\d+\s*(cup|cups|tbsp|tsp|tablespoon|teaspoon|oz|ounce|lb|pound|g|kg|ml|l|liter)s?\b',
        r'\d+/\d+',
        r'^\d+\s*',
    ]

    for pattern in measurements:
        ingredient = re.sub(pattern, '', ingredient, flags=re.IGNORECASE)

    # Remove descriptors in parentheses
    ingredient = re.sub(r'\([^)]*\)', '', ingredient)

    # Clean up whitespace
    ingredient = ' '.join(ingredient.split())

    return ingredient.strip()


def extract_ingredients(recipe: dict) -> list[str]:
    """Extract and normalize ingredients from a recipe."""
    ingredients = recipe.get('ingredients', [])

    if not isinstance(ingredients, list):
        return []

    normalized = []
    for ing in ingredients:
        if isinstance(ing, str):
            norm = normalize_ingredient(ing)
            if norm:
                normalized.append(norm)
        elif isinstance(ing, dict) and 'name' in ing:
            norm = normalize_ingredient(ing['name'])
            if norm:
                normalized.append(norm)

    return normalized


def build_index(data_dir: Path) -> dict:
    """Build ingredient index from all recipes."""
    index = defaultdict(list)

    recipe_files = list(data_dir.glob('**/*.json'))

    for filepath in recipe_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                recipe = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        recipe_id = filepath.stem
        recipe_title = recipe.get('title', recipe_id)

        for ingredient in extract_ingredients(recipe):
            index[ingredient].append({
                'id': recipe_id,
                'title': recipe_title,
                'file': str(filepath.relative_to(data_dir))
            })

    return dict(index)


def main():
    data_dir = Path(__file__).parent.parent / 'data'
    output_file = data_dir / 'ingredient-index.json'

    if not data_dir.exists():
        print("No data directory found, creating empty index")
        data_dir.mkdir(parents=True, exist_ok=True)
        index = {}
    else:
        index = build_index(data_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Built ingredient index with {len(index)} unique ingredients")
    print(f"Output written to: {output_file}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
