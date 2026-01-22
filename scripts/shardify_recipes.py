#!/usr/bin/env python3
"""
Shardify Recipes - Rebuild category shards and index from recipes.json

This script:
1. Reads the main recipes.json file
2. Generates recipes-index.json with recipe summaries
3. Generates recipes-{category}.json shard files for each category

Usage:
    python scripts/shardify_recipes.py [--dry-run]
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
RECIPES_FILE = os.path.join(DATA_DIR, 'recipes.json')
INDEX_FILE = os.path.join(DATA_DIR, 'recipes-index.json')

# Fields to include in the index (lightweight summaries)
INDEX_FIELDS = ['id', 'title', 'category', 'tags', 'collection', 'description',
                'servings_yield', 'total_time']


def load_recipes():
    """Load all recipes from main recipes.json"""
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('recipes', [])


def create_index_entry(recipe):
    """Create a lightweight index entry from a full recipe"""
    return {field: recipe.get(field, '') for field in INDEX_FIELDS}


def shardify(dry_run=False):
    """Rebuild all shards and index from recipes.json"""
    print(f"Loading recipes from {RECIPES_FILE}...")
    recipes = load_recipes()
    print(f"Loaded {len(recipes)} recipes")

    # Group recipes by category
    categories = defaultdict(list)
    for recipe in recipes:
        cat = recipe.get('category', 'uncategorized')
        categories[cat].append(recipe)

    print(f"\nCategories found: {len(categories)}")
    for cat, cat_recipes in sorted(categories.items()):
        print(f"  {cat}: {len(cat_recipes)} recipes")

    # Build index entries
    index_entries = [create_index_entry(r) for r in recipes]

    # Build shard manifest
    shards = []
    for cat in sorted(categories.keys()):
        shards.append({
            'category': cat,
            'file': f'recipes-{cat}.json',
            'count': len(categories[cat])
        })

    # Create index file
    index_data = {
        'meta': {
            'title': 'Other Family Recipes',
            'description': 'Digital cookbook recipes and magazine clippings, preserved with love',
            'total_recipes': len(recipes),
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'version': '3.0.0',
            'sharded': True,
            'shard_strategy': 'by_category'
        },
        'shards': shards,
        'recipes': index_entries
    }

    if dry_run:
        print(f"\n[DRY RUN] Would write index with {len(index_entries)} entries")
        print(f"[DRY RUN] Would create {len(shards)} shard files")
        return

    # Write index file
    print(f"\nWriting index to {INDEX_FILE}...")
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    # Write shard files
    for cat, cat_recipes in categories.items():
        shard_file = os.path.join(DATA_DIR, f'recipes-{cat}.json')
        shard_data = {
            'meta': {
                'category': cat,
                'count': len(cat_recipes),
                'shard_of': 'recipes-index.json'
            },
            'recipes': cat_recipes
        }
        print(f"Writing shard: {shard_file} ({len(cat_recipes)} recipes)")
        with open(shard_file, 'w', encoding='utf-8') as f:
            json.dump(shard_data, f, indent=2, ensure_ascii=False)

    print(f"\nShardification complete!")
    print(f"  Total recipes: {len(recipes)}")
    print(f"  Index entries: {len(index_entries)}")
    print(f"  Shard files: {len(shards)}")


if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    shardify(dry_run=dry_run)
