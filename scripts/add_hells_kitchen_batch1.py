#!/usr/bin/env python3
"""
Add Hell's Kitchen cookbook recipes - Batch 1 (IMG_8264-8280)
Source: Hell's Kitchen cookbook (Minneapolis neighborhood community cookbook)
"""

import json
from pathlib import Path

RECIPES_FILE = Path("/home/user/Allrecipes/data/recipes.json")

# Batch 1 recipes extracted from IMG_8264-8280
BATCH1_RECIPES = [
    {
        "id": "annies-mustard-hells-kitchen",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Annie's Mustard",
        "category": "sides",
        "attribution": "Annie Omer",
        "source_note": "Hell's Kitchen cookbook (Minneapolis)",
        "description": "A homemade mustard that needs 3 months to age and mellow properly.",
        "servings_yield": "1¾ cups",
        "prep_time": "5 min",
        "cook_time": "5 min",
        "total_time": "10 min + 3 months aging",
        "ingredients": [
            {"item": "dry mustard", "quantity": "½", "unit": "cup", "prep_note": ""},
            {"item": "sugar", "quantity": "½", "unit": "cup", "prep_note": ""},
            {"item": "flour", "quantity": "¼", "unit": "cup", "prep_note": ""},
            {"item": "white vinegar", "quantity": "1", "unit": "cup", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix dry mustard, sugar, and flour in a bowl."},
            {"step": 2, "text": "Heat vinegar to a boil, reduce heat to a simmer, and slowly stir in mustard mixture."},
            {"step": 3, "text": "Whisk continuously until thickened, about 1 minute."},
            {"step": 4, "text": "Remove from the heat, and let cool to room temperature, whisking occasionally."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": ["The mustard takes about 3 months to age and mellow properly."],
        "tips": ["Will keep refrigerated damn near indefinitely."],
        "substitutions": [],
        "tags": ["condiment", "mustard", "make-ahead"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": [], "assumptions": []}
    },
    {
        "id": "cocktail-party-bean-dip-hells-kitchen",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cocktail Party Bean Dip",
        "category": "appetizers",
        "attribution": "Adele (friend of Mom), via Bronko Nagurski connection",
        "source_note": "Hell's Kitchen cookbook (Minneapolis). Recipe from Adele, who was married to a guy named Tip who'd played football for the Chicago Bears in the thirties and forties with Bronko Nagurski.",
        "description": "A rich, cheesy bean dip with jalapeños, perfect for parties.",
        "servings_yield": "approximately 4 cups",
        "prep_time": "20 min",
        "cook_time": "4 hours 15 min",
        "total_time": "4 hours 35 min + 4 hours soaking",
        "ingredients": [
            {"item": "dried pinto beans", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "kosher salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "peanut oil", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "dry mustard", "quantity": "½", "unit": "tsp", "prep_note": ""},
            {"item": "large white onion", "quantity": "1", "unit": "", "prep_note": "cut into chunks"},
            {"item": "unsalted butter", "quantity": "1", "unit": "cup", "prep_note": "2 sticks"},
            {"item": "provolone cheese", "quantity": "½", "unit": "lb", "prep_note": "cubed"},
            {"item": "jalapeño", "quantity": "2", "unit": "heaping tbsp", "prep_note": "minced, seeded"},
            {"item": "jalapeño liquid", "quantity": "1", "unit": "tbsp", "prep_note": "from jarred jalapeños"},
            {"item": "white onion", "quantity": "¼", "unit": "cup", "prep_note": "minced"},
            {"item": "garlic", "quantity": "3", "unit": "medium cloves", "prep_note": "mashed"}
        ],
        "instructions": [
            {"step": 1, "text": "Sort through dried beans, removing any debris such as small stones. Place in large bowl and cover with water. Soak 4 hours, drain and rinse."},
            {"step": 2, "text": "Place soaked beans, salt, oil, mustard, and onion chunks in a large, heavy pot, and pour in 6 cups water, making sure beans are well covered."},
            {"step": 3, "text": "Heat to a boil. Reduce heat, cover, and simmer, checking occasionally, until beans are very soft, about 4 hours. If at any point evaporation exposes top layer of beans, add hot water to cover."},
            {"step": 4, "text": "Drain and return to the pot."},
            {"step": 5, "text": "Mash beans with a potato masher."},
            {"step": 6, "text": "Stir together bean mixture, butter, provolone cheese, canned jalapeños, jalapeño liquid, minced onion, and mashed garlic."},
            {"step": 7, "text": "Cook bean mixture over medium heat until cheese is absorbed, about 7 minutes."},
            {"step": 8, "text": "Serve hot with corn chips or saltine crackers."}
        ],
        "temperature": "",
        "pan_size": "",
        "notes": [],
        "tips": ["If at any point evaporation exposes top layer of beans, add hot water to cover."],
        "substitutions": [],
        "tags": ["appetizer", "dip", "beans", "party", "cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": [], "assumptions": []}
    },
    {
        "id": "chile-cheese-squares-hells-kitchen",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chile-Cheese Squares",
        "category": "appetizers",
        "attribution": "",
        "source_note": "Hell's Kitchen cookbook (Minneapolis)",
        "description": "Cheesy baked squares with green chiles and jalapeños that freeze well.",
        "servings_yield": "about 35 squares",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "45 min",
        "ingredients": [
            {"item": "eggs", "quantity": "4", "unit": "", "prep_note": "beaten"},
            {"item": "all-purpose flour", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "baking powder", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "Jane's Krazy Mixed-Up Salt", "quantity": "¾", "unit": "tsp", "prep_note": "or comparable seasoned salt"},
            {"item": "Monterey Jack cheese", "quantity": "4", "unit": "cups", "prep_note": "shredded (1 pound)"},
            {"item": "Mexican-style processed cheese", "quantity": "1", "unit": "8-oz log", "prep_note": ""},
            {"item": "canned chopped green chiles", "quantity": "8", "unit": "oz", "prep_note": ""},
            {"item": "canned chopped jalapeños", "quantity": "2", "unit": "oz", "prep_note": ""},
            {"item": "unsalted butter", "quantity": "¼", "unit": "cup", "prep_note": "melted (½ stick)"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "Coat a 9 × 13-inch pan with a thin layer of butter to prevent sticking."},
            {"step": 3, "text": "Mix beaten eggs, flour, milk, baking powder, Jane's Krazy Mixed-Up Salt, Monterey Jack cheese, shredded cheese, and canned chiles and jalapeños in a large bowl."},
            {"step": 4, "text": "Stir in melted butter. Fold cheese mixture lightly into the pan with a rubber spatula."},
            {"step": 5, "text": "Place on the center rack of the oven, and bake about 30 minutes, removing when cheese starts to bubble and browns but is still soft."},
            {"step": 6, "text": "Cool before cutting, and reheat right before serving."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9 × 13-inch",
        "notes": [],
        "tips": ["These freeze very well in waxed paper.", "Cool before cutting, and reheat right before serving."],
        "substitutions": [{"original": "Jane's Krazy Mixed-Up Salt", "substitute": "comparable seasoned salt", "note": ""}],
        "tags": ["appetizer", "cheese", "chiles", "freezer-friendly", "party"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "nutrition": {"status": "insufficient_data", "per_serving": {}, "missing_inputs": [], "assumptions": []}
    }
]


def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    # Check for duplicates
    existing_ids = {r['id'] for r in data['recipes']}
    new_recipes = []
    skipped = []

    for recipe in BATCH1_RECIPES:
        if recipe['id'] in existing_ids:
            skipped.append(recipe['id'])
        else:
            new_recipes.append(recipe)
            existing_ids.add(recipe['id'])

    if skipped:
        print(f"Skipped {len(skipped)} duplicate recipes: {skipped}")

    # Add new recipes
    data['recipes'].extend(new_recipes)
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = "2026-02-07"

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Added {len(new_recipes)} new recipes. Total: {data['meta']['total_count']}")


if __name__ == "__main__":
    main()
