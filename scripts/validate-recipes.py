#!/usr/bin/env python3
"""
Recipe Validation Script for Other Family Recipes
Validates recipes.json for schema compliance and common issues.

Usage:
    python scripts/validate-recipes.py
    python scripts/validate-recipes.py --strict  # Fail on warnings too
"""

import json
import sys
import re
from pathlib import Path

# Configuration
REQUIRED_FIELDS = ['id', 'title', 'ingredients', 'instructions', 'category']
OPTIONAL_FIELDS = ['attribution', 'source_note', 'description', 'servings_yield',
                   'prep_time', 'cook_time', 'total_time', 'temperature', 'pan_size',
                   'notes', 'tips', 'substitutions', 'tags', 'confidence', 'image_refs',
                   'page_continuation', 'conversions', 'nutrition', 'variant_of',
                   'variants', 'variant_notes', 'canonical_id', 'frosting', 'oven_directions',
                   'components', 'component_of', 'is_component']

VALID_CATEGORIES = ['appetizers', 'basics', 'beverages', 'breads', 'breakfast',
                    'cheese', 'desserts', 'mains', 'salads', 'sides', 'soups', 'snacks']

VALID_CONFIDENCE = ['high', 'medium', 'low']

# Measurement sanity checks (flag if exceeded)
# Note: These are generous limits - better to miss a real error than flag false positives
SANITY_LIMITS = {
    'sugar': {'max_cups': 8},
    'flour': {'max_cups': 12},
    'butter': {'max_cups': 4, 'max_tbsp': 24},  # 24 tbsp = 1.5 cups, reasonable for large batches
    'baking soda': {'max_tsp': 6},
    'baking powder': {'max_tbsp': 6},
}

# Salt is checked separately with stricter matching (to avoid "salted peanuts", "salmon", etc.)
SALT_LIMITS = {'max_cups': 0.5, 'max_tbsp': 4, 'max_tsp': 8}
# But canning/pickling/brining recipes can use much more
SALT_HEAVY_TAGS = ['canning', 'pickling', 'preserving', 'brine', 'fermented', 'cured']

# Temperature sanity (Fahrenheit)
TEMP_MIN = 200
TEMP_MAX = 550

# Cheese-making temperature range (includes aging temps and milk processing)
CHEESE_TEMP_MIN = 50  # Cave/cellar aging temps
CHEESE_TEMP_MAX = 220  # Stretched curd cheeses like mozzarella


class RecipeValidator:
    def __init__(self, strict=False):
        self.strict = strict
        self.errors = []
        self.warnings = []

    def error(self, recipe_id, message):
        self.errors.append(f"ERROR [{recipe_id}]: {message}")

    def warn(self, recipe_id, message):
        self.warnings.append(f"WARNING [{recipe_id}]: {message}")

    def validate_recipe(self, recipe):
        """Validate a single recipe."""
        recipe_id = recipe.get('id', 'UNKNOWN')

        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in recipe or not recipe[field]:
                self.error(recipe_id, f"Missing required field: {field}")

        # Validate ID format (slug-like)
        if 'id' in recipe:
            if not re.match(r'^[a-z0-9-]+$', recipe['id']):
                self.error(recipe_id, f"Invalid ID format (should be lowercase slug): {recipe['id']}")

        # Validate category
        if 'category' in recipe:
            if recipe['category'] not in VALID_CATEGORIES:
                self.warn(recipe_id, f"Unknown category: {recipe['category']}")

        # Validate confidence
        if 'confidence' in recipe and recipe['confidence']:
            overall = recipe['confidence'].get('overall')
            if overall and overall not in VALID_CONFIDENCE:
                self.error(recipe_id, f"Invalid confidence level: {overall}")

        # Validate ingredients
        if 'ingredients' in recipe:
            self.validate_ingredients(recipe_id, recipe['ingredients'])

        # Validate instructions
        if 'instructions' in recipe:
            self.validate_instructions(recipe_id, recipe['instructions'])

        # Check if this is a recipe that uses non-baking temperatures
        # (cheesemaking, fermented foods, cultured dairy, bread proofing)
        tags = recipe.get('tags', [])
        category = recipe.get('category', '')
        title_lower = recipe.get('title', '').lower()

        # Recipes that legitimately use low temps (culturing, proofing, frozen desserts)
        LOW_TEMP_TAGS = ['cheese', 'cheesemaking', 'cheese-making', 'homemade cheese',
                        'fermented', 'cultured', 'yogurt', 'kefir', 'sourdough', 'yeast',
                        'bread', 'dough', 'ice cream', 'frozen', 'custard', 'crepes']
        LOW_TEMP_TITLES = ['yogurt', 'kefir', 'sour cream', 'cultured butter',
                          'creme fraiche', 'crème fraîche', 'buttermilk', 'dough',
                          'bread', 'rolls', 'ice cream', 'sherbet', 'sorbet', 'crepe']

        uses_low_temps = (
            category == 'cheese' or
            any(t.lower() in LOW_TEMP_TAGS for t in tags) or
            any(term in title_lower for term in LOW_TEMP_TITLES)
        )

        # Validate temperature
        if 'temperature' in recipe and recipe['temperature']:
            self.validate_temperature(recipe_id, recipe['temperature'], uses_low_temps)

        # Validate image_refs exist
        if 'image_refs' in recipe:
            self.validate_image_refs(recipe_id, recipe['image_refs'])

        # Check for nutrition status consistency
        if 'nutrition' in recipe and recipe['nutrition']:
            self.validate_nutrition(recipe_id, recipe['nutrition'])

        # Check conversions if present
        if 'conversions' in recipe and recipe['conversions']:
            self.validate_conversions(recipe_id, recipe['conversions'])

    def validate_ingredients(self, recipe_id, ingredients):
        """Validate ingredients list."""
        if not isinstance(ingredients, list):
            self.error(recipe_id, "Ingredients must be a list")
            return

        for i, ing in enumerate(ingredients):
            if not isinstance(ing, dict):
                self.error(recipe_id, f"Ingredient {i} must be an object")
                continue

            if 'item' not in ing:
                self.error(recipe_id, f"Ingredient {i} missing 'item' field")

            # Sanity check quantities
            item = ing.get('item', '').lower()
            qty = ing.get('quantity', '')
            unit = ing.get('unit', '').lower()

            self.check_quantity_sanity(recipe_id, item, qty, unit)

    def check_quantity_sanity(self, recipe_id, item, qty, unit):
        """Check if quantity seems reasonable."""
        if not qty or qty == '' or '[UNCLEAR]' in str(qty):
            return

        try:
            # Handle fractions
            if '/' in str(qty):
                parts = str(qty).split()
                if len(parts) == 2:  # e.g., "2 3/4"
                    whole = float(parts[0])
                    frac_parts = parts[1].split('/')
                    qty_float = whole + float(frac_parts[0]) / float(frac_parts[1])
                else:  # e.g., "3/4"
                    frac_parts = str(qty).split('/')
                    qty_float = float(frac_parts[0]) / float(frac_parts[1])
            else:
                qty_float = float(qty.replace('-', '.').split()[0])
        except (ValueError, IndexError):
            return  # Can't parse, skip check

        # Skip absurdly high values that are likely OCR errors
        if qty_float > 50:
            return

        # Check standard limits
        for check_item, limits in SANITY_LIMITS.items():
            # Use word boundary matching to avoid "salted" matching "salt"
            if re.search(rf'\b{check_item}\b', item):
                if 'cup' in unit and 'max_cups' in limits:
                    if qty_float > limits['max_cups']:
                        self.warn(recipe_id, f"Suspicious: {qty} {unit} {item} (max expected: {limits['max_cups']} cups)")
                if 'tbsp' in unit and 'max_tbsp' in limits:
                    if qty_float > limits['max_tbsp']:
                        self.warn(recipe_id, f"Suspicious: {qty} {unit} {item} (max expected: {limits['max_tbsp']} tbsp)")
                if 'tsp' in unit and 'max_tsp' in limits:
                    if qty_float > limits['max_tsp']:
                        self.warn(recipe_id, f"Suspicious: {qty} {unit} {item} (max expected: {limits['max_tsp']} tsp)")

    def validate_instructions(self, recipe_id, instructions):
        """Validate instructions list."""
        if not isinstance(instructions, list):
            self.error(recipe_id, "Instructions must be a list")
            return

        if len(instructions) == 0:
            self.error(recipe_id, "Instructions list is empty")
            return

        for i, inst in enumerate(instructions):
            if not isinstance(inst, dict):
                self.error(recipe_id, f"Instruction {i} must be an object")
                continue

            if 'text' not in inst:
                self.error(recipe_id, f"Instruction {i} missing 'text' field")

    def validate_temperature(self, recipe_id, temp, is_cheesemaking=False):
        """Validate temperature is reasonable."""
        # Extract Fahrenheit number
        match = re.search(r'(\d+)\s*°?F', temp)
        if match:
            temp_f = int(match.group(1))
            # Cheesemaking recipes can have BOTH cheese temps (aging, culturing) AND baking temps
            if is_cheesemaking:
                # Valid if in cheese range (55-220) OR baking range (200-550)
                in_cheese_range = CHEESE_TEMP_MIN <= temp_f <= CHEESE_TEMP_MAX
                in_baking_range = TEMP_MIN <= temp_f <= TEMP_MAX
                if not (in_cheese_range or in_baking_range):
                    self.warn(recipe_id, f"Temperature {temp_f}°F outside expected ranges (cheese: {CHEESE_TEMP_MIN}-{CHEESE_TEMP_MAX}°F, baking: {TEMP_MIN}-{TEMP_MAX}°F)")
            else:
                if temp_f < TEMP_MIN or temp_f > TEMP_MAX:
                    self.warn(recipe_id, f"Temperature {temp_f}°F outside typical range ({TEMP_MIN}-{TEMP_MAX}°F)")

    def validate_image_refs(self, recipe_id, image_refs):
        """Check that referenced images exist."""
        if not isinstance(image_refs, list):
            self.error(recipe_id, "image_refs must be a list")
            return

        data_dir = Path(__file__).parent.parent / 'data'
        for ref in image_refs:
            img_path = data_dir / ref
            # Also check with common extensions if exact path doesn't exist
            if not img_path.exists():
                found = False
                for ext in ['.PNG', '.jpeg', '.jpg', '.png']:
                    if (data_dir / (ref + ext)).exists():
                        found = True
                        break
                if not found:
                    self.warn(recipe_id, f"Referenced image not found: {ref}")

    def validate_nutrition(self, recipe_id, nutrition):
        """Validate nutrition data consistency."""
        status = nutrition.get('status')
        if status == 'insufficient_data':
            if not nutrition.get('missing_inputs'):
                self.warn(recipe_id, "Nutrition status is 'insufficient_data' but missing_inputs is empty")
        elif status in ['complete', 'partial']:
            per_serving = nutrition.get('per_serving', {})
            if not per_serving or all(v is None for v in per_serving.values()):
                self.warn(recipe_id, f"Nutrition status is '{status}' but no nutrition values provided")

    def validate_conversions(self, recipe_id, conversions):
        """Validate conversions data."""
        if conversions.get('has_conversions'):
            if not conversions.get('ingredients_metric'):
                self.warn(recipe_id, "has_conversions is true but ingredients_metric is empty")

    def validate_all(self, recipes_data):
        """Validate all recipes."""
        if 'recipes' not in recipes_data:
            self.error('GLOBAL', "Missing 'recipes' array in JSON")
            return

        recipes = recipes_data['recipes']
        ids_seen = set()

        for recipe in recipes:
            recipe_id = recipe.get('id', 'UNKNOWN')

            # Check for duplicate IDs
            if recipe_id in ids_seen:
                self.error(recipe_id, "Duplicate recipe ID")
            ids_seen.add(recipe_id)

            self.validate_recipe(recipe)

        # Check variant references
        for recipe in recipes:
            variant_of = recipe.get('variant_of')
            if variant_of and variant_of not in ids_seen:
                self.error(recipe.get('id'), f"variant_of references non-existent recipe: {variant_of}")

    def report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("RECIPE VALIDATION REPORT")
        print("="*60)

        if self.errors:
            print(f"\n{len(self.errors)} ERROR(S):")
            for err in self.errors:
                print(f"  {err}")
        else:
            print("\nNo errors found.")

        if self.warnings:
            print(f"\n{len(self.warnings)} WARNING(S):")
            for warn in self.warnings:
                print(f"  {warn}")
        else:
            print("\nNo warnings.")

        print("\n" + "="*60)

        if self.errors:
            return 1
        if self.strict and self.warnings:
            return 1
        return 0


def main():
    strict = '--strict' in sys.argv

    # Find recipes file
    script_dir = Path(__file__).parent
    recipes_file = script_dir.parent / 'data' / 'recipes.json'

    if not recipes_file.exists():
        print(f"ERROR: Cannot find {recipes_file}")
        sys.exit(1)

    # Load and validate
    print(f"Validating: {recipes_file}")

    try:
        with open(recipes_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON - {e}")
        sys.exit(1)

    validator = RecipeValidator(strict=strict)
    validator.validate_all(data)
    exit_code = validator.report()

    print(f"\nTotal recipes: {len(data.get('recipes', []))}")
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
