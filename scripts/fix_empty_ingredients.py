#!/usr/bin/env python3
"""
Extract structured ingredients from vintage narrative recipe instructions.

These Gutenberg recipes have ingredients embedded in their instruction text
(e.g., "Take two tablespoons of sugar, half a cup of currants...").
This script parses the text to create structured ingredient entries.

Conservative approach: only extract what's clearly stated. Use empty strings
for quantity/unit when not clearly specified.
"""

import json
import re
import sys


# Number words to digits
NUMBER_WORDS = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
    'eleven': '11', 'twelve': '12', 'fifteen': '15', 'twenty': '20',
    'a': '1', 'an': '1',
    'half': '1/2', 'quarter': '1/4', 'third': '1/3',
    'half a': '1/2', 'a half': '1/2',
    'half an': '1/2',
    'a quarter': '1/4',
    'a third': '1/3',
    'one-half': '1/2', 'one-quarter': '1/4', 'one-third': '1/3',
    'three-quarters': '3/4', 'two-thirds': '2/3',
}

# Unit patterns
UNIT_MAP = {
    'tablespoon': 'tbsp', 'tablespoons': 'tbsp', 'table-spoon': 'tbsp',
    'table-spoons': 'tbsp', 'tablespoonfuls': 'tbsp', 'tablespoonful': 'tbsp',
    'teaspoon': 'tsp', 'teaspoons': 'tsp', 'tea-spoon': 'tsp',
    'tea-spoons': 'tsp', 'teaspoonfuls': 'tsp', 'teaspoonful': 'tsp',
    'cup': 'cup', 'cups': 'cup', 'cupfuls': 'cup', 'cupful': 'cup',
    'pint': 'pint', 'pints': 'pint',
    'quart': 'quart', 'quarts': 'quart',
    'gallon': 'gallon', 'gallons': 'gallon',
    'pound': 'lb', 'pounds': 'lb', 'lb': 'lb', 'lbs': 'lb',
    'ounce': 'oz', 'ounces': 'oz', 'oz': 'oz',
    'gill': 'gill', 'gills': 'gill',
    'dozen': 'dozen',
    'slice': 'slice', 'slices': 'slice',
    'sprig': 'sprig', 'sprigs': 'sprig',
    'bunch': 'bunch', 'bunches': 'bunch',
    'head': 'head', 'heads': 'head',
    'clove': 'clove', 'cloves': 'clove',
    'pinch': 'pinch',
    'dash': 'dash',
    'drop': 'drop', 'drops': 'drop',
    'pair': 'pair', 'pairs': 'pair',
    'can': 'can', 'cans': 'can',
    'bottle': 'bottle', 'bottles': 'bottle',
    'glass': 'glass', 'glasses': 'glass',
    'wineglass': 'wineglass',
    'package': 'package', 'packages': 'package',
    'stick': 'stick', 'sticks': 'stick',
    'sheet': 'sheet', 'sheets': 'sheet',
    'handful': 'handful',
    'saltspoon': 'saltspoon', 'saltspoons': 'saltspoon',
    'dessertspoon': 'dessertspoon', 'dessertspoons': 'dessertspoon',
    'piece': 'piece', 'pieces': 'piece',
}

# Words that are NOT food items (filter junk from extraction)
NOT_FOOD = {
    'it', 'them', 'this', 'that', 'all', 'the', 'some', 'each', 'any',
    'time', 'hour', 'hours', 'minute', 'minutes', 'moment', 'moments',
    'way', 'manner', 'dish', 'pan', 'pot', 'oven', 'fire', 'heat',
    'may be substituted', 'may be used', 'should be', 'must be',
    'paste', 'rich paste', 'the same', 'good', 'cold', 'hot', 'warm',
    'one', 'two', 'three', 'a', 'an', 'nice', 'fine', 'large', 'small',
    'your', 'more', 'less', 'other', 'these', 'those', 'such', 'very',
}

# Common food words for fallback detection
COMMON_FOODS = [
    'butter', 'salt', 'pepper', 'sugar', 'flour', 'eggs', 'egg',
    'milk', 'cream', 'water', 'oil', 'olive oil', 'vinegar', 'lemon',
    'lemon juice', 'lemon peel', 'orange peel', 'onion', 'onions',
    'garlic', 'parsley', 'thyme', 'bay leaf', 'bay leaves', 'nutmeg',
    'cinnamon', 'ginger', 'cloves', 'mace', 'mustard', 'bread',
    'bread crumbs', 'breadcrumbs', 'rice', 'potatoes', 'potato',
    'celery', 'carrots', 'carrot', 'turnip', 'turnips',
    'tomatoes', 'tomato', 'mushrooms', 'mushroom', 'bacon', 'ham',
    'chicken', 'beef', 'veal', 'pork', 'lamb', 'mutton', 'fowl',
    'fish', 'shrimp', 'lobster', 'oysters', 'oyster',
    'anchovies', 'anchovy', 'sardines',
    'cheese', 'wine', 'white wine', 'red wine', 'brandy', 'sherry',
    'madeira', 'stock', 'broth', 'gravy', 'sauce',
    'lard', 'suet', 'dripping', 'drippings',
    'olives', 'capers', 'pickles', 'cornichons',
    'almonds', 'walnuts', 'pecans', 'raisins', 'currants',
    'apples', 'apple', 'pears', 'pear', 'peaches', 'peach',
    'oranges', 'orange', 'lemons', 'chocolate', 'cocoa',
    'yeast', 'baking powder', 'baking soda', 'soda',
    'cornstarch', 'arrowroot', 'gelatin', 'gelatine',
    'vanilla', 'rose water', 'rosewater',
    'cayenne', 'paprika', 'allspice', 'sage', 'rosemary',
    'marjoram', 'tarragon', 'chives', 'dill', 'basil', 'oregano',
    'saffron', 'turmeric', 'cumin', 'coriander',
    'ketchup', 'catsup', 'worcestershire',
    'truffles', 'truffle', 'asparagus', 'artichoke', 'artichokes',
    'spinach', 'lettuce', 'cabbage', 'peas', 'beans', 'corn',
    'cucumbers', 'cucumber', 'radishes', 'beets',
    'cranberries', 'strawberries', 'raspberries', 'blueberries',
    'cherries', 'plums', 'grapes', 'figs', 'dates', 'prunes',
    'coconut', 'honey', 'molasses', 'syrup', 'maple syrup',
    'whipped cream', 'sour cream', 'buttermilk', 'yogurt',
]

# Build regex for units
UNIT_PATTERN = '|'.join(sorted(UNIT_MAP.keys(), key=len, reverse=True))

# Build regex for number words
NUM_PATTERN = '|'.join(sorted(NUMBER_WORDS.keys(), key=len, reverse=True))

# Numeric patterns (digits, fractions)
DIGIT_PATTERN = r'\d+(?:\s*/\s*\d+)?(?:\s+\d+/\d+)?'


def clean_item(item_raw):
    """Clean an extracted item name. Return None if it's junk."""
    item = item_raw.strip().lower()
    item = re.sub(r'\s+', ' ', item)

    # Remove trailing non-food words
    item = re.sub(r'\s+(and|or|the|a|an|some|more|well|then|till|until|about|nearly|quite|rather|also|too)$', '', item)

    # Remove leading adjective-only words when they're the entire item
    item = item.strip(' .,;:')

    # Filter out junk
    if not item or len(item) < 2:
        return None
    if item in NOT_FOOD:
        return None
    # Filter items that are clearly not food
    if re.match(r'^(the|a|an|some|your|its|my|his|her)\b', item):
        return None
    # Filter if it ends with a verb pattern suggesting it's part of a sentence
    if re.search(r'\b(is|are|was|were|be|been|being|do|does|did|have|has|had|will|would|could|should|may|might|must|shall)$', item):
        return None
    # Filter items that are just adjectives
    if item in ('cold', 'hot', 'warm', 'fresh', 'dried', 'chopped', 'minced',
                'sliced', 'diced', 'grated', 'melted', 'boiled', 'fried',
                'baked', 'roasted', 'raw', 'cooked', 'stewed', 'mixed'):
        return None

    return item


def extract_ingredients_from_text(full_text):
    """Extract ingredient entries from narrative recipe text."""
    ingredients = []
    seen_items = set()

    text = full_text.replace('\n', ' ').replace('  ', ' ')

    # Pattern: "[qty_digits] [qty_words] [unit] (of) [item up to punctuation or stop word]"
    # Captures: "two tablespoons of sugar", "1/2 cup currants", "a pound of lean veal"
    pat_unit = re.compile(
        r'(?:(\d+(?:\s*/\s*\d+)?(?:\s+\d+/\d+)?)\s+)?'   # optional digit qty
        r'(?:(three-quarters|two-thirds|one-quarter|one-third|one-half|half a|half an|a quarter|a third|a half|'
        r'half|quarter|third|twenty|fifteen|twelve|eleven|three|seven|eight|four|five|nine|ten|two|six|one|an|a)\s+)?'  # optional word qty
        r'(tablespoonfuls|tablespoonful|dessertspoons|dessertspoon|teaspoonfuls|tablespoons|table-spoons|table-spoon|teaspoonful|tablespoon|saltspoons|saltspoon|wineglass|teaspoons|tea-spoons|tea-spoon|teaspoon|packages|handfuls|handful|bottles|glasses|package|gallons|bunches|cupfuls|cupful|bottles|gallon|sheets|sprigs|sticks|pieces|slices|bottle|quarts|pounds|ounces|pieces|dozen|bunch|pints|heads|glass|piece|quart|sheet|sprig|stick|slice|pound|ounce|pint|cups|pair|drop|head|gill|dash|lbs|cup|can|oz|lb)\s+'  # unit (required)
        r'(?:of\s+)?'                                       # optional "of"
        r'([a-zA-Z][-a-zA-Z\s\']+)',                        # item text
        re.IGNORECASE
    )

    for m in pat_unit.finditer(text):
        digit_qty = (m.group(1) or '').strip()
        word_qty = (m.group(2) or '').strip()
        unit_raw = m.group(3)
        item_raw = m.group(4)

        # Truncate item at stop words / punctuation
        # Stop at: and, or, with, in, into, to, for, from, over, on, at, until, when, if, then, that, which
        item_raw = re.split(
            r'\b(?:and|or|with|in|into|to|for|from|over|on|at|until|when|if|then|that|which|the\s+(?:whole|rest|same|other|mixture|duck|fowl|meat|fish|pie))\b',
            item_raw, maxsplit=1
        )[0]

        # Also truncate at period, comma, semicolon
        item_raw = re.split(r'[,;.\)\]]', item_raw, maxsplit=1)[0]

        item = clean_item(item_raw)
        if not item:
            continue

        # Build quantity
        qty = digit_qty
        if word_qty:
            word_val = NUMBER_WORDS.get(word_qty.lower(), word_qty)
            if qty:
                # e.g., "2 1/2" already captured by digit pattern
                pass
            else:
                qty = word_val

        unit = UNIT_MAP.get(unit_raw.lower(), unit_raw.lower())

        if item not in seen_items:
            seen_items.add(item)
            ingredients.append({
                'item': item,
                'quantity': qty,
                'unit': unit,
                'prep_note': ''
            })

    # Fallback: scan for common food words mentioned in the text
    text_lower = text.lower()
    for food in COMMON_FOODS:
        if food in seen_items:
            continue
        if re.search(rf'\b{re.escape(food)}\b', text_lower):
            seen_items.add(food)
            ingredients.append({
                'item': food,
                'quantity': '',
                'unit': '',
                'prep_note': 'mentioned in instructions'
            })

    return ingredients


def main():
    print("Fixing recipes with empty ingredients...")

    with open('/home/user/Allrecipes/data/recipes.json') as f:
        data = json.load(f)

    recipes = data['recipes']
    fixed_count = 0
    still_empty = 0

    for r in recipes:
        ing = r.get('ingredients', [])
        if not isinstance(ing, list) or len(ing) > 0:
            continue

        # Get all instruction text
        instructions = r.get('instructions', [])
        if not instructions:
            continue

        full_text = ' '.join(inst.get('text', '') for inst in instructions if isinstance(inst, dict))
        if not full_text.strip():
            continue

        extracted = extract_ingredients_from_text(full_text)

        if extracted:
            r['ingredients'] = extracted
            fixed_count += 1
        else:
            still_empty += 1
            print(f"  WARNING: No ingredients extracted from {r['id']}")

    print(f"\nFixed: {fixed_count} recipes")
    print(f"Still empty: {still_empty} recipes")

    with open('/home/user/Allrecipes/data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Written successfully.")


if __name__ == '__main__':
    main()
