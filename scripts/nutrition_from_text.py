#!/usr/bin/env python3
"""
Calculate nutrition for paragraph-style recipes by extracting ingredients from instruction text.

Handles:
1. "See instructions" recipes (Stevenson, Cheese Book, other Gutenberg)
2. Forme of Cury medieval recipes
3. OCR garbage / non-recipe content
"""

import json
import re
import sys
import os

# Import the comprehensive NUTRITION_DB and helpers from existing script
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from add_all_nutrition import (
    NUTRITION_DB, normalize_ingredient, normalize_unit, parse_quantity,
    get_nutrition_for_ingredient, is_equipment, infer_servings
)

# =============================================================================
# TEXT-BASED INGREDIENT EXTRACTION
# =============================================================================

# Common measurement words and their numeric equivalents
WORD_NUMBERS = {
    "a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "half": 0.5, "quarter": 0.25,
    "dozen": 12, "few": 3, "several": 4, "couple": 2,
}

# Unit patterns for text extraction
UNIT_PATTERNS = [
    # Full words
    "cups?", "tablespoons?", "teaspoons?", "ounces?", "pounds?",
    "pints?", "quarts?", "gallons?",
    # Abbreviations
    "tbsp\\.?", "tsp\\.?", "oz\\.?", "lb\\.?", "lbs\\.?",
    # Historical
    "cupfuls?", "tablespoonfuls?", "teaspoonfuls?", "dessertspoonfuls?",
    "saltspoonfuls?", "wineglasses?", "gills?", "teacups?",
    # Baking-specific
    "cans?", "packages?", "slices?", "pieces?", "heads?", "bunches?",
    "cloves?", "stalks?", "sprigs?", "loaves?",
]

# Build a set of known food items from the NUTRITION_DB for matching
KNOWN_FOODS = set()
for food_name in NUTRITION_DB.keys():
    KNOWN_FOODS.add(food_name)
    # Also add common variants
    words = food_name.split()
    if len(words) >= 2:
        # Add last word as partial match (e.g., "flour" from "all-purpose flour")
        KNOWN_FOODS.add(words[-1])

# Additional common foods that appear in paragraph-style recipes
EXTRA_FOODS = {
    "bread": {"cup": {"cal": 120, "fat": 2, "carbs": 22, "protein": 4, "sodium": 200, "fiber": 1, "sugar": 2},
              "slice": {"cal": 75, "fat": 1, "carbs": 14, "protein": 3, "sodium": 130, "fiber": 1, "sugar": 1.5},
              "": {"cal": 75, "fat": 1, "carbs": 14, "protein": 3, "sodium": 130, "fiber": 1, "sugar": 1.5}},
    "toast": {"slice": {"cal": 75, "fat": 1, "carbs": 14, "protein": 3, "sodium": 130, "fiber": 1, "sugar": 1.5},
              "": {"cal": 75, "fat": 1, "carbs": 14, "protein": 3, "sodium": 130, "fiber": 1, "sugar": 1.5}},
    "cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.5, "protein": 28, "sodium": 700, "fiber": 0, "sugar": 0.5},
               "oz": {"cal": 113, "fat": 9, "carbs": 0.4, "protein": 7, "sodium": 175, "fiber": 0, "sugar": 0.1},
               "tbsp": {"cal": 28, "fat": 2.3, "carbs": 0.1, "protein": 1.8, "sodium": 44, "fiber": 0, "sugar": 0},
               "": {"cal": 113, "fat": 9, "carbs": 0.4, "protein": 7, "sodium": 175, "fiber": 0, "sugar": 0.1}},
    "meat": {"lb": {"cal": 1000, "fat": 65, "carbs": 0, "protein": 90, "sodium": 300, "fiber": 0, "sugar": 0},
             "cup": {"cal": 250, "fat": 16, "carbs": 0, "protein": 22, "sodium": 75, "fiber": 0, "sugar": 0},
             "": {"cal": 200, "fat": 12, "carbs": 0, "protein": 20, "sodium": 60, "fiber": 0, "sugar": 0}},
    "fish": {"lb": {"cal": 500, "fat": 10, "carbs": 0, "protein": 100, "sodium": 400, "fiber": 0, "sugar": 0},
             "": {"cal": 150, "fat": 3, "carbs": 0, "protein": 30, "sodium": 120, "fiber": 0, "sugar": 0}},
    "vegetables": {"cup": {"cal": 40, "fat": 0.5, "carbs": 8, "protein": 2, "sodium": 30, "fiber": 3, "sugar": 3},
                   "": {"cal": 30, "fat": 0.3, "carbs": 6, "protein": 1.5, "sodium": 20, "fiber": 2, "sugar": 2}},
    "fruit": {"cup": {"cal": 70, "fat": 0.3, "carbs": 18, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 13},
              "": {"cal": 60, "fat": 0.2, "carbs": 15, "protein": 0.8, "sodium": 1, "fiber": 2.5, "sugar": 11}},
}


def extract_ingredients_from_text(text):
    """Extract ingredient mentions from paragraph-style instruction text.

    Returns list of dicts with {item, quantity, unit} matching the recipe schema.
    """
    if not text:
        return []

    text = text.lower()
    extracted = []

    # Pattern 1: "{number/fraction} {unit} (of) {food}"
    # e.g., "1 cup flour", "two tablespoons of butter", "1/2 teaspoon salt"
    number_pattern = r'(?:\d+\s*/\s*\d+|\d+\.?\d*|' + '|'.join(WORD_NUMBERS.keys()) + r')'
    unit_pattern = r'(?:' + '|'.join(UNIT_PATTERNS) + r')'

    # Full pattern: number + unit + optional "of" + food words
    full_pattern = rf'({number_pattern})\s+({unit_pattern})\s+(?:of\s+)?([a-z][a-z\s-]{{1,40}})'

    for match in re.finditer(full_pattern, text):
        qty_str = match.group(1)
        unit_str = match.group(2)
        food_str = match.group(3).strip()

        # Clean the food string - take up to first punctuation or conjunction
        food_str = re.split(r'[;,\.\!\?]|\band\b|\bwith\b|\buntil\b|\bor\b|\bthen\b|\binto\b|\bon\b|\bover\b', food_str)[0].strip()

        if len(food_str) < 2 or len(food_str) > 40:
            continue

        # Convert word numbers
        if qty_str in WORD_NUMBERS:
            qty_str = str(WORD_NUMBERS[qty_str])

        extracted.append({
            "item": food_str,
            "quantity": qty_str,
            "unit": unit_str,
            "prep_note": ""
        })

    # Pattern 2: "{number} {food}" (countable items)
    # e.g., "3 eggs", "1 onion", "2 apples"
    countable_foods = [
        "eggs?", "onions?", "tomato(?:es)?", "potato(?:es)?", "apples?",
        "lemons?", "limes?", "oranges?", "bananas?", "carrots?",
        "cloves? (?:of )?garlic", "garlic cloves?",
        "sardines?", "anchovies?", "shallots?",
    ]
    countable_pattern = rf'({number_pattern})\s+({"|".join(countable_foods)})'

    for match in re.finditer(countable_pattern, text):
        qty_str = match.group(1)
        food_str = match.group(2).strip()

        if qty_str in WORD_NUMBERS:
            qty_str = str(WORD_NUMBERS[qty_str])

        extracted.append({
            "item": food_str,
            "quantity": qty_str,
            "unit": "",
            "prep_note": ""
        })

    # Pattern 3: Identify key food nouns from text (unquantified)
    # For these, we estimate a typical serving amount
    key_food_mentions = {
        # Bread/grain items (common in canapes, sandwiches)
        "bread": ("2", "slice"),
        "toast": ("2", "slice"),
        "crackers": ("4", ""),
        "rice": ("1/2", "cup"),
        "pasta": ("1", "cup"),
        "noodles": ("1", "cup"),
        "macaroni": ("1", "cup"),
        "spaghetti": ("1", "cup"),
        # Dairy
        "cheese": ("2", "oz"),
        "butter": ("2", "tbsp"),
        "cream": ("2", "tbsp"),
        "milk": ("1/4", "cup"),
        "cream cheese": ("2", "oz"),
        "sour cream": ("2", "tbsp"),
        "whipped cream": ("2", "tbsp"),
        # Proteins
        "chicken": ("4", "oz"),
        "beef": ("4", "oz"),
        "pork": ("4", "oz"),
        "ham": ("3", "oz"),
        "bacon": ("2", "slice"),
        "sausage": ("2", "oz"),
        "salmon": ("3", "oz"),
        "lobster": ("3", "oz"),
        "shrimp": ("3", "oz"),
        "crab": ("3", "oz"),
        "sardines": ("2", "oz"),
        "tuna": ("3", "oz"),
        "oysters": ("3", "oz"),
        # Eggs
        "egg": ("1", ""),
        "eggs": ("2", ""),
        "egg yolk": ("1", ""),
        "egg white": ("1", ""),
        # Vegetables
        "onion": ("1", ""),
        "celery": ("1", "stalk"),
        "tomato": ("1", ""),
        "potato": ("1", ""),
        "lettuce": ("1", "cup"),
        "cabbage": ("1", "cup"),
        "spinach": ("1", "cup"),
        "peas": ("1/2", "cup"),
        "beans": ("1/2", "cup"),
        "corn": ("1/2", "cup"),
        "mushrooms": ("1/2", "cup"),
        "peppers": ("1", ""),
        "olives": ("4", ""),
        # Baking/condiments
        "flour": ("2", "tbsp"),
        "sugar": ("1", "tbsp"),
        "salt": ("1/4", "tsp"),
        "pepper": ("1/8", "tsp"),
        "vinegar": ("1", "tbsp"),
        "olive oil": ("1", "tbsp"),
        "oil": ("1", "tbsp"),
        "lemon juice": ("1", "tbsp"),
        "mustard": ("1", "tsp"),
        "mayonnaise": ("1", "tbsp"),
        "ketchup": ("1", "tbsp"),
        "soy sauce": ("1", "tbsp"),
        "worcestershire": ("1", "tsp"),
        "horseradish": ("1", "tsp"),
        # Spices
        "paprika": ("1/2", "tsp"),
        "cinnamon": ("1/2", "tsp"),
        "nutmeg": ("1/4", "tsp"),
        "vanilla": ("1", "tsp"),
        "cayenne": ("1/8", "tsp"),
        "curry": ("1", "tsp"),
        "ginger": ("1/2", "tsp"),
        "cloves": ("1/4", "tsp"),
        "thyme": ("1/4", "tsp"),
        "sage": ("1/4", "tsp"),
        "rosemary": ("1/4", "tsp"),
        "bay leaf": ("1", ""),
        # Baking
        "baking powder": ("1", "tsp"),
        "baking soda": ("1/2", "tsp"),
        "yeast": ("1", "tsp"),
        "gelatin": ("1", "tbsp"),
        "cornstarch": ("1", "tbsp"),
        # Herbs
        "parsley": ("1", "tbsp"),
        "chives": ("1", "tbsp"),
        "dill": ("1", "tsp"),
        # Fruits
        "lemon": ("1", ""),
        "apple": ("1", ""),
        "raisins": ("2", "tbsp"),
        # Nuts
        "walnuts": ("2", "tbsp"),
        "almonds": ("2", "tbsp"),
        "pecans": ("2", "tbsp"),
    }

    # Only add unquantified mentions if we didn't already extract a quantified version
    extracted_items = {normalize_ingredient(e["item"]) for e in extracted}

    for food, (default_qty, default_unit) in key_food_mentions.items():
        # Use word boundary matching for short words to avoid false positives
        if len(food) <= 3:
            pattern = rf'\b{re.escape(food)}\b'
            found = bool(re.search(pattern, text))
        else:
            found = food in text
        if found and normalize_ingredient(food) not in extracted_items:
            extracted.append({
                "item": food,
                "quantity": default_qty,
                "unit": default_unit,
                "prep_note": "estimated from text mention"
            })

    return extracted


def get_all_recipe_text(recipe):
    """Combine all text fields from a recipe for ingredient extraction."""
    parts = []

    # Instructions text
    for step in recipe.get("instructions", []):
        parts.append(step.get("text", ""))

    # Notes
    for note in recipe.get("notes", []):
        if isinstance(note, str):
            parts.append(note)

    # Tips
    for tip in recipe.get("tips", []):
        if isinstance(tip, str):
            parts.append(tip)

    # Description
    if recipe.get("description"):
        parts.append(recipe["description"])

    return " ".join(parts)


def calculate_text_nutrition(recipe):
    """Calculate nutrition for a paragraph-style recipe by extracting ingredients from text."""
    text = get_all_recipe_text(recipe)

    if not text or len(text) < 20:
        return None

    # Extract ingredients from text
    extracted = extract_ingredients_from_text(text)

    if not extracted:
        return None

    servings = infer_servings(recipe)
    serving_inferred = not recipe.get("servings_yield")

    total = {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}
    matched = 0
    unmatched = 0
    missing = []

    for ing in extracted:
        nutr = get_nutrition_for_ingredient(ing)
        if nutr and not nutr.get("_skipped"):
            matched += 1
            for key in total:
                total[key] += nutr.get(key, 0)
        else:
            # Try EXTRA_FOODS
            item_norm = normalize_ingredient(ing["item"])
            unit_norm = normalize_unit(ing.get("unit", ""))
            found = False

            for food_name, food_data in EXTRA_FOODS.items():
                if food_name in item_norm or item_norm in food_name:
                    qty = parse_quantity(ing.get("quantity", "1"))
                    if unit_norm in food_data:
                        base = food_data[unit_norm]
                    elif "" in food_data:
                        base = food_data[""]
                    else:
                        base = list(food_data.values())[0]
                    for key in total:
                        total[key] += base.get(key, 0) * qty
                    matched += 1
                    found = True
                    break

            if not found:
                unmatched += 1
                ing_str = f"{ing.get('quantity', '')} {ing.get('unit', '')} {ing.get('item', '')}".strip()
                if ing_str:
                    missing.append(ing_str)

    if matched == 0:
        return None

    # Calculate per-serving values
    per_serving = {
        "calories": round(total["cal"] / servings),
        "fat_g": round(total["fat"] / servings, 1),
        "carbs_g": round(total["carbs"] / servings, 1),
        "protein_g": round(total["protein"] / servings, 1),
        "sodium_mg": round(total["sodium"] / servings),
        "fiber_g": round(total["fiber"] / servings, 1),
        "sugar_g": round(total["sugar"] / servings, 1)
    }

    # Check if we got any non-zero nutrition
    has_any = any(v > 0 for v in per_serving.values())
    if not has_any:
        return None

    # Always partial for text-extracted nutrition (lower confidence than structured)
    total_items = matched + unmatched
    if unmatched == 0 and matched >= 2:
        status = "partial"  # Still partial since extracted from text
    elif matched >= 2:
        status = "partial"
    else:
        status = "partial"

    assumptions = [
        f"Estimated from instruction text ({matched} ingredients identified)",
        f"Calculated for {servings} servings"
    ]
    if serving_inferred:
        assumptions.append(f"Serving size inferred from {recipe.get('category', 'unknown')} category")

    return {
        "status": status,
        "per_serving": per_serving,
        "missing_inputs": missing[:10],
        "assumptions": assumptions
    }


def is_non_recipe_content(recipe):
    """Detect OCR garbage, non-recipe content like tables of contents, ads, etc."""
    rid = recipe.get("id", "")
    title = recipe.get("title", "").lower()

    # Known non-recipe patterns
    non_recipe_patterns = [
        "library-ofcongress", "popular-andstandard-books",
        "tables-", "appendix-", "index-", "contents-",
        "estimates-furnished", "distributors-",
        "thebestingroceries", "allplayer-music",
        "someother-books", "rodstrom-", "dental-rooms",
        "published-forthebenefit",
    ]
    for pattern in non_recipe_patterns:
        if pattern in rid:
            return True

    # Title checks
    non_recipe_titles = [
        "table of contents", "index", "appendix", "bibliography",
        "advertisement", "library of congress", "copyright",
        "table of", "weights and measures",
    ]
    for nr_title in non_recipe_titles:
        if nr_title in title:
            return True

    # Check if instructions are very short or look like garbage
    instructions = recipe.get("instructions", [])
    if instructions:
        all_text = " ".join(s.get("text", "") for s in instructions)
        # If text has excessive numbers/punctuation relative to words
        alpha_count = sum(1 for c in all_text if c.isalpha())
        if len(all_text) > 10 and alpha_count / len(all_text) < 0.3:
            return True

    return False


def is_forme_of_cury(recipe):
    """Detect Forme of Cury / Ancient Cookery medieval recipes."""
    rid = recipe.get("id", "")
    return "forme-of-cury" in rid or "ancient-cookery" in rid


def needs_text_nutrition(recipe):
    """Check if recipe needs text-based nutrition calculation.

    Returns True for:
    - All-zero per_serving
    - Previously text-extracted (to re-extract with improved patterns)
    - Empty per_serving
    """
    n = recipe.get("nutrition", {})
    ps = n.get("per_serving", {})

    # Empty per_serving
    if not ps:
        return True

    # All-zero values
    vals = [v for v in ps.values() if isinstance(v, (int, float))]
    if vals and all(v == 0 for v in vals):
        return True

    # Previously text-extracted (re-extract with improved patterns)
    assumptions = n.get("assumptions", [])
    if any("instruction text" in a for a in assumptions):
        return True

    # Previously marked insufficient due to text parsing failure
    missing = n.get("missing_inputs", [])
    if missing and "Paragraph-style" in str(missing[0]):
        return True

    return False


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def process_recipes():
    """Process all recipes with zero nutrition and calculate from text."""
    recipes_file = "data/recipes.json"

    with open(recipes_file, 'r') as f:
        data = json.load(f)

    recipes = data.get("recipes", [])

    total_zero = 0
    updated_text = 0
    marked_insufficient = 0
    marked_forme = 0
    still_zero = 0

    for recipe in recipes:
        if not needs_text_nutrition(recipe):
            continue

        total_zero += 1
        rid = recipe.get("id", "")

        # Case 1: Non-recipe content → insufficient_data
        if is_non_recipe_content(recipe):
            recipe["nutrition"] = {
                "status": "insufficient_data",
                "per_serving": {},
                "missing_inputs": ["Non-recipe content (table of contents, advertisement, index, etc.)"],
                "assumptions": []
            }
            marked_insufficient += 1
            continue

        # Case 2: Forme of Cury / Ancient Cookery → insufficient_data
        if is_forme_of_cury(recipe):
            recipe["nutrition"] = {
                "status": "insufficient_data",
                "per_serving": {},
                "missing_inputs": ["Medieval English recipe - quantities not in modern units"],
                "assumptions": ["Original Middle English text does not contain standardized measurements"]
            }
            marked_forme += 1
            continue

        # Case 3: Try to extract nutrition from instruction text
        nutrition = calculate_text_nutrition(recipe)
        if nutrition:
            recipe["nutrition"] = nutrition
            updated_text += 1
        else:
            # Mark as insufficient_data with honest status
            recipe["nutrition"] = {
                "status": "insufficient_data",
                "per_serving": {},
                "missing_inputs": ["Paragraph-style recipe - ingredients embedded in instructions, unable to extract quantities"],
                "assumptions": []
            }
            still_zero += 1

    # Save
    with open(recipes_file, 'w') as f:
        json.dump(data, f, indent=2)

    # Also update category shards
    shard_updates = {}
    for recipe in recipes:
        cat = recipe.get("category", "mains")
        if cat not in shard_updates:
            shard_updates[cat] = []
        shard_updates[cat].append(recipe)

    for cat, cat_recipes in shard_updates.items():
        shard_file = f"data/recipes-{cat}.json"
        if os.path.exists(shard_file):
            with open(shard_file, 'r') as f:
                shard_data = json.load(f)

            # Build lookup
            shard_lookup = {r["id"]: i for i, r in enumerate(shard_data.get("recipes", []))}

            for recipe in cat_recipes:
                if recipe["id"] in shard_lookup:
                    idx = shard_lookup[recipe["id"]]
                    shard_data["recipes"][idx]["nutrition"] = recipe["nutrition"]

            with open(shard_file, 'w') as f:
                json.dump(shard_data, f, indent=2)

    print(f"\n{'='*60}")
    print(f"NUTRITION FROM TEXT - PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"Total with zero nutrition: {total_zero}")
    print(f"Updated from text extraction: {updated_text}")
    print(f"Marked insufficient (medieval): {marked_forme}")
    print(f"Marked insufficient (non-recipe): {marked_insufficient}")
    print(f"Marked insufficient (could not extract): {still_zero}")
    print(f"{'='*60}")

    return total_zero, updated_text, marked_forme, marked_insufficient, still_zero


if __name__ == "__main__":
    process_recipes()
