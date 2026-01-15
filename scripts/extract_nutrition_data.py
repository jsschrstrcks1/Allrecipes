#!/usr/bin/env python3
"""
Extract and merge comprehensive nutrition data from add_all_nutrition.py
into clean JSON databases for the Allrecipes project.

This script parses the existing Python script and extracts:
- NUTRITION_DB ingredients
- Synonyms/aliases
- Standard can/jar sizes
- Unit conversions
- Equipment filtering words
- OCR correction patterns
"""

import json
import re
import sys
from pathlib import Path

def extract_nutrition_db(content):
    """Extract NUTRITION_DB dictionary from Python file content."""
    # Find the start of NUTRITION_DB
    match = re.search(r'NUTRITION_DB\s*=\s*\{', content)
    if not match:
        return {}

    start = match.end() - 1

    # Find matching closing brace
    brace_count = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

    db_str = content[start:end]

    # Clean up for eval - remove comments
    lines = []
    for line in db_str.split('\n'):
        # Remove inline comments
        if '#' in line:
            # But preserve strings with # in them
            in_string = False
            clean_line = []
            for i, char in enumerate(line):
                if char in '"\'':
                    in_string = not in_string
                if char == '#' and not in_string:
                    break
                clean_line.append(char)
            line = ''.join(clean_line)
        lines.append(line)

    db_str = '\n'.join(lines)

    try:
        # Safe eval with only basic types
        return eval(db_str, {"__builtins__": {}}, {})
    except Exception as e:
        print(f"Warning: Could not parse NUTRITION_DB: {e}")
        return {}


def extract_synonyms(content):
    """Extract synonyms dictionary from normalize_ingredient function."""
    # Find the synonyms dict in normalize_ingredient
    match = re.search(r'synonyms\s*=\s*\{', content)
    if not match:
        return {}

    start = match.end() - 1

    # Find matching closing brace
    brace_count = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

    syn_str = content[start:end]

    # Clean up comments
    lines = []
    for line in syn_str.split('\n'):
        if '#' in line:
            in_string = False
            clean_line = []
            for i, char in enumerate(line):
                if char in '"\'':
                    in_string = not in_string
                if char == '#' and not in_string:
                    break
                clean_line.append(char)
            line = ''.join(clean_line)
        lines.append(line)

    syn_str = '\n'.join(lines)

    try:
        return eval(syn_str, {"__builtins__": {}}, {})
    except Exception as e:
        print(f"Warning: Could not parse synonyms: {e}")
        return {}


def extract_equipment_words(content):
    """Extract EQUIPMENT_WORDS set."""
    match = re.search(r'EQUIPMENT_WORDS\s*=\s*\{', content)
    if not match:
        return set()

    start = match.end() - 1
    brace_count = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

    eq_str = content[start:end]

    # Clean comments
    lines = []
    for line in eq_str.split('\n'):
        if '#' in line:
            in_string = False
            clean_line = []
            for char in line:
                if char in '"\'':
                    in_string = not in_string
                if char == '#' and not in_string:
                    break
                clean_line.append(char)
            line = ''.join(clean_line)
        lines.append(line)

    eq_str = '\n'.join(lines)

    try:
        return eval(eq_str, {"__builtins__": {}}, {})
    except:
        return set()


def extract_can_jar_sizes(content):
    """Extract STANDARD_CAN_SIZES and STANDARD_JAR_SIZES."""
    can_sizes = {}
    jar_sizes = {}

    # Can sizes
    match = re.search(r'STANDARD_CAN_SIZES\s*=\s*\{([^}]+)\}', content)
    if match:
        try:
            can_str = '{' + match.group(1) + '}'
            # Remove comments
            can_str = re.sub(r'#[^\n]*', '', can_str)
            can_sizes = eval(can_str, {"__builtins__": {}}, {})
        except:
            pass

    # Jar sizes
    match = re.search(r'STANDARD_JAR_SIZES\s*=\s*\{([^}]+)\}', content)
    if match:
        try:
            jar_str = '{' + match.group(1) + '}'
            jar_str = re.sub(r'#[^\n]*', '', jar_str)
            jar_sizes = eval(jar_str, {"__builtins__": {}}, {})
        except:
            pass

    return can_sizes, jar_sizes


def extract_unit_map(content):
    """Extract unit normalization map."""
    # Find unit_map in normalize_unit function
    match = re.search(r'unit_map\s*=\s*\{', content)
    if not match:
        return {}

    start = match.end() - 1
    brace_count = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

    unit_str = content[start:end]

    # Clean comments
    lines = []
    for line in unit_str.split('\n'):
        if '#' in line:
            in_string = False
            clean_line = []
            for char in line:
                if char in '"\'':
                    in_string = not in_string
                if char == '#' and not in_string:
                    break
                clean_line.append(char)
            line = ''.join(clean_line)
        lines.append(line)

    unit_str = '\n'.join(lines)

    try:
        return eval(unit_str, {"__builtins__": {}}, {})
    except:
        return {}


def main():
    script_path = Path(__file__).parent / "add_all_nutrition.py"

    if not script_path.exists():
        print(f"Error: {script_path} not found")
        sys.exit(1)

    print(f"Reading {script_path}...")
    content = script_path.read_text()

    print("Extracting NUTRITION_DB...")
    nutrition_db = extract_nutrition_db(content)
    print(f"  Found {len(nutrition_db)} ingredients")

    print("Extracting synonyms...")
    synonyms = extract_synonyms(content)
    print(f"  Found {len(synonyms)} synonym mappings")

    print("Extracting equipment words...")
    equipment = extract_equipment_words(content)
    print(f"  Found {len(equipment)} equipment words")

    print("Extracting can/jar sizes...")
    can_sizes, jar_sizes = extract_can_jar_sizes(content)
    print(f"  Found {len(can_sizes)} can sizes, {len(jar_sizes)} jar sizes")

    print("Extracting unit conversions...")
    unit_map = extract_unit_map(content)
    print(f"  Found {len(unit_map)} unit mappings")

    # Build comprehensive database
    output_dir = Path(__file__).parent.parent / "data" / "nutrition"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Master nutrition database
    master_db = {
        "_metadata": {
            "description": "Master nutrition database for recipe ingredient estimation",
            "version": "2.0.0",
            "sources": [
                "add_all_nutrition.py (Allrecipes)",
                "GrandmasRecipes nutrition script",
                "USDA FoodData Central"
            ],
            "last_updated": "2026-01-15",
            "ingredient_count": len(nutrition_db),
            "notes": "Values are per specified unit. Multi-unit entries preferred for flexibility."
        },
        "ingredients": nutrition_db,
        "standard_can_sizes": can_sizes,
        "standard_jar_sizes": jar_sizes,
        "unit_conversions": {
            "_description": "Historical and modern unit conversions to standard forms",
            "mappings": unit_map,
            "historical_equivalents": {
                "gill": {"cups": 0.5, "fl_oz": 4},
                "drachm": {"oz": 0.125},
                "dessertspoon": {"tsp": 2},
                "saltspoon": {"tsp": 0.25},
                "wineglass": {"cups": 0.5, "fl_oz": 4},
                "teacup": {"cups": 0.75, "fl_oz": 6},
                "coffeecup": {"cups": 1},
                "jigger": {"tbsp": 3, "oz": 1.5},
                "peck": {"quarts": 8},
                "bushel": {"pecks": 4, "quarts": 32},
                "firkin": {"gallons": 9},
                "hogshead": {"gallons": 63}
            }
        },
        "default_quantities": {
            "_description": "Default quantities when unit is missing",
            "egg": 1,
            "garlic": 1,
            "onion": 1,
            "bay leaf": 1,
            "jalapeno": 1,
            "banana": 1,
            "apple": 1,
            "lemon": 1,
            "lime": 1,
            "orange": 1,
            "pork chop": 1,
            "chicken breast": 1
        }
    }

    master_path = output_dir / "nutrition_database.json"
    print(f"\nWriting master database to {master_path}...")
    with open(master_path, 'w') as f:
        json.dump(master_db, f, indent=2)

    # Ingredient aliases (synonyms)
    aliases_db = {
        "_metadata": {
            "description": "Ingredient synonym and alias mappings for normalization",
            "version": "2.0.0",
            "sources": ["add_all_nutrition.py normalize_ingredient() function"],
            "last_updated": "2026-01-15",
            "mapping_count": len(synonyms),
            "notes": "Maps variant names, OCR artifacts, and brand names to canonical ingredient names"
        },
        "synonyms": synonyms,
        "brand_name_mappings": {
            "grandma's molasses": "molasses",
            "carnation milk": "evaporated milk",
            "gold medal flour": "flour",
            "pillsbury flour": "flour",
            "crisco": "shortening",
            "pam": "cooking spray",
            "hellmann's": "mayonnaise",
            "best foods": "mayonnaise",
            "philadelphia": "cream cheese",
            "jell-o": "gelatin",
            "knox": "gelatin",
            "bisquick": "biscuit mix",
            "jiffy": "corn muffin mix",
            "country crock": "margarine",
            "i can't believe it's not butter": "margarine"
        },
        "ocr_fixes": {
            "_description": "Common OCR artifacts and their corrections",
            "space_corruption": {
                "mayonnais e": "mayonnaise",
                "eg g yolks": "egg yolk",
                "eg g": "egg",
                "unsalt ed butter": "butter",
                "lemo n": "lemon",
                "m iniature marshmallows": "miniature marshmallows",
                "all-purpos e flour": "flour",
                "shorte ning": "shortening",
                "chick en": "chicken",
                "raspb erries": "raspberries",
                "peca ns": "pecans",
                "garl ic": "garlic",
                "papri ka": "paprika"
            },
            "ligatures": {
                "ﬂ": "fl",
                "ﬁ": "fi"
            },
            "curly_quotes": {
                "\u2019": "'",
                "\u2018": "'",
                "\u201c": "\"",
                "\u201d": "\""
            }
        },
        "prefix_removals": [
            "fresh ", "frozen ", "dried ", "canned ", "cooked ", "raw ",
            "chopped ", "diced ", "minced ", "sliced ", "cubed ",
            "grated ", "shredded ", "mashed ", "crushed ", "crumbled ",
            "melted ", "softened ", "room temperature ", "cold ", "warm ", "hot ",
            "ripe ", "peeled ", "pitted ", "seeded ", "cored ",
            "toasted ", "roasted ", "sauteed ",
            "sifted ", "packed ", "firmly packed ", "lightly packed ",
            "finely ", "coarsely ", "roughly ", "thinly ",
            "boneless ", "skinless ",
            "low-fat ", "lowfat ", "low fat ", "nonfat ", "non-fat ", "fat-free ",
            "unsalted ", "salted ",
            "pure ", "organic ", "natural ",
            "about ", "approximately ", "approx "
        ]
    }

    aliases_path = output_dir / "ingredient_aliases.json"
    print(f"Writing aliases database to {aliases_path}...")
    with open(aliases_path, 'w') as f:
        json.dump(aliases_db, f, indent=2)

    # Equipment filtering words
    equipment_db = {
        "_metadata": {
            "description": "Non-food items to filter from ingredient lists",
            "version": "1.0.0",
            "last_updated": "2026-01-15"
        },
        "equipment_words": sorted(list(equipment)) if equipment else [],
        "equipment_patterns": [
            "mixing-bowl", "mixing bowl", "double-boiler", "double boiler",
            "dover beater", "vegetable-knife", "flour sifter",
            "for the ", "cookbook", "-inch", "-sized",
            "for topping", "for serving", "for dipping", "for garnish",
            "for dusting", "(optional)", "optional"
        ]
    }

    equipment_path = output_dir / "equipment_filter.json"
    print(f"Writing equipment filter to {equipment_path}...")
    with open(equipment_path, 'w') as f:
        json.dump(equipment_db, f, indent=2)

    print("\nExtraction complete!")
    print(f"  - {master_path}: {len(nutrition_db)} ingredients")
    print(f"  - {aliases_path}: {len(synonyms)} synonyms")
    print(f"  - {equipment_path}: {len(equipment) if equipment else 0} equipment words")


if __name__ == "__main__":
    main()
