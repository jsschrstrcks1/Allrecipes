#!/usr/bin/env python3
"""Add third batch of Sioux Chef recipes to recipes.json"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "braised-sunflowers-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Braised Sunflowers (or Sunchokes)",
        "native_name": "Waŋčázi/Pȟaŋǧí Lolóbyapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 32",
        "description": "We're familiar with toasted sunflower seeds and their valuable oil, but their gorgeous heads were also once an important source of food. The flavor is close to that of an artichoke. Once braised, they may be stuffed with wild rice, nuts, or beans, and they are also delicious served with a splash of Wojape or sprinkled with smoked salt.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflowers, depending on size", "quantity": "2 to 4", "unit": ""},
            {"item": "sunflower oil", "quantity": "2 to 3", "unit": "tbsp"},
            {"item": "chopped wild onions or shallots", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped sage", "quantity": "2", "unit": "tsp"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "Corn Stock, page 170, or water", "quantity": "1/4", "unit": "cup"},
            {"item": "roasted sunflower seeds for garnish", "quantity": "1/4", "unit": "cup"},
            {"item": "Wojape, page 173", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Remove the flowers and the green petal-like leaves from the sunflowers to expose the pith of the flower head. Turn the flower's head on edge to trim off the yellow face of the flower, removing just the yellow and leaving the meat. Trim off the stem."},
            {"step": 2, "text": "Film a deep pan or heavy pot with the oil and set over medium heat. Add the onions, sage, and a pinch of salt and sauté until the onions are soft."},
            {"step": 3, "text": "Add the heads with the 'face' side down and sauté for about 5 minutes."},
            {"step": 4, "text": "Turn and spoon the onions on top, add the stock, cover the pot, lower the heat, and braise the heads until tender, about 40 minutes."},
            {"step": 5, "text": "Serve warm, seasoned with smoked salt or drizzle with Wojape. Garnish with the sunflower seeds."}
        ],
        "notes": [],
        "tips": [
            "If sunflowers are unavailable, Jerusalem artichokes (sunchokes) work equally well in this recipe."
        ],
        "substitutions": [
            {"original": "sunflowers", "substitute": "1 to 1 1/2 pounds scrubbed sunchokes, sliced in half horizontally", "note": ""}
        ],
        "tags": ["indigenous", "native american", "sunflower", "sunchoke", "braised", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "griddled-maple-squash-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Griddled Maple Squash",
        "native_name": "Wagmú Čhaŋháŋpi Tiktíča Akáštaŋpi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 33",
        "description": "This simple technique for cooking squash is quick and easy. Serve the slices on salads, float them on top of soup, or stack them on corn, bean, and wild rice cakes.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "medium winter squash such as butternut or acorn", "quantity": "1", "unit": "", "prep_note": "about 2 pounds"},
            {"item": "sunflower oil", "quantity": "2 to 3", "unit": "tbsp"},
            {"item": "Coarse salt, page 183", "quantity": "", "unit": ""},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "maple syrup", "quantity": "2 to 3", "unit": "tbsp"},
            {"item": "fried sage leaves, page 29", "quantity": "6", "unit": ""},
            {"item": "toasted squash, pumpkin, or sunflower seeds, page 158, for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cut the squash in half lengthwise. Remove the seeds and cut top to bottom into thin slices about 1/4 inch thick."},
            {"step": 2, "text": "Brush the slices with a little of the oil and sprinkle with the salt and sumac."},
            {"step": 3, "text": "Heat a griddle or heavy skillet and lightly grease with the remaining oil. Griddle the squash slices until nicely browned, about 5 to 10 minutes per side."},
            {"step": 4, "text": "Brush with the maple syrup. Sprinkle with the coarse salt, garnish with the fried sage leaves and toasted seeds."},
            {"step": 5, "text": "Serve as a snack right off the griddle, a base for bean cakes, a garnish for soups and stews, or a garnish for salads."}
        ],
        "temperature": "425°F (220°C)",
        "notes": [],
        "tips": [
            "To reserve the squash seeds to roast for a garnish, see page 158."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "squash", "maple", "griddled", "side dish", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "crispy-bean-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crispy Bean Cakes",
        "native_name": "Omníča Aǧúyapi Saksáka",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 38",
        "description": "Serve these as a first course on wild greens, or make them into tiny patties for finger food. They make wonderful appetizers and snacks.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "cooked or canned beans, drained", "quantity": "2", "unit": "cups"},
            {"item": "chopped sage", "quantity": "1 to 2", "unit": "tsp"},
            {"item": "duck egg", "quantity": "1", "unit": ""},
            {"item": "chopped wild onion or shallot", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "corn flour plus a tablespoon for dusting the cakes as needed", "quantity": "1/4", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "3 to 4", "unit": "tbsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 250°F."},
            {"step": 2, "text": "In a food processor fitted with a steel blade, pulse together all of the ingredients to make a rough dough."},
            {"step": 3, "text": "Using moistened hands, form the mixture into patties about 1/2 inch thick. Dust the patties with the flour and set aside."},
            {"step": 4, "text": "Film a skillet with the oil, and set over medium heat. Working in batches, fry the patties until golden brown on each side, about 5 to 7 minutes per side."},
            {"step": 5, "text": "Transfer to a baking sheet and put in the oven to keep warm."}
        ],
        "temperature": "250°F (120°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "beans", "cakes", "appetizer", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "three-sisters-mash-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Three Sisters Mash",
        "native_name": "Wagmíza na Omníča na Wagmú Patháŋpi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 42",
        "description": "This easy side dish makes good use of leftovers; serve it with roast meat or fish; top it with a poached or fried egg for brunch.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "small summer squash or zucchini, cut into 1-inch pieces", "quantity": "1", "unit": ""},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1", "unit": "cup"},
            {"item": "sweet corn kernels", "quantity": "1", "unit": "cup"},
            {"item": "cooked hominy, page 31", "quantity": "1/2", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "chopped sage", "quantity": "2", "unit": "tsp"},
            {"item": "chopped mint", "quantity": "1", "unit": "tbsp"},
            {"item": "smoked salt", "quantity": "", "unit": "generous pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a large skillet with the oil and set over medium heat."},
            {"step": 2, "text": "Cook the onion or shallot until tender, about 3 to 5 minutes."},
            {"step": 3, "text": "Add the squash and continue cooking until tender, stirring often, about 5 minutes."},
            {"step": 4, "text": "Stir in the beans, corn, and hominy and cook until the corn is bright and tender, about 5 minutes."},
            {"step": 5, "text": "Then stir in the maple syrup, sage, and mint. Season with the smoked salt."},
            {"step": 6, "text": "Serve warm or at room temperature."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "three sisters", "corn", "beans", "squash", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["cedar-braised-beans-sioux-chef"],
        "is_component": False
    },
    {
        "id": "smoked-whitefish-white-bean-spread-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Whitefish and White Bean Spread",
        "native_name": "Hoǧáŋ Asótkaziyapi na Omníča Ská Iyúlthuŋ",
        "category": "appetizers",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 44",
        "description": "This creamy spread is great with our Amaranth Crackers, page 60, or piled high on Corn Cakes, page 51, or Wild Rice Cakes, page 63. This is the filling for Stuffed Squash Blossoms, page 28.",
        "servings_yield": "Makes 1 1/2 cups",
        "ingredients": [
            {"item": "shredded smoked whitefish or trout", "quantity": "1", "unit": "cup"},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1/2", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "maple sugar", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the whitefish, beans, and oil into a food processor fitted with a steel blade and pulse to create a rough, thick consistency."},
            {"step": 2, "text": "Season to taste with the sumac and maple sugar."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "smoked whitefish", "substitute": "smoked trout", "note": ""}
        ],
        "tags": ["indigenous", "native american", "spread", "appetizer", "fish", "smoked", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["cedar-braised-beans-sioux-chef"],
        "is_component": True,
        "component_of": ["stuffed-squash-blossoms-sioux-chef"]
    },
    {
        "id": "maple-sage-roasted-vegetables-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple-Sage Roasted Vegetables",
        "native_name": "Phežíȟota na Čhaŋháŋpi Tiktíča úŋ Wathótho Čheúŋpapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 46",
        "description": "Roasting vegetables draws out and evaporates their moisture, condensing and intensifying flavors and making the textures firmer and heartier. Use whatever is in season. Autumn squash is perfect for this, as are turnips or timpsila (prairie turnip) and sweet potatoes. These make a nice starter when garnished with toasted nuts and dried cranberries, or served over wild rice, on Corn Cakes, page 51, or on a bed of dark greens, drizzled with a little Wojape.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "small winter squash, peeled, seeded, and cut into 1/2-inch chunks", "quantity": "1", "unit": ""},
            {"item": "sunchokes, cut into 1/2-inch chunks", "quantity": "1/2", "unit": "lb"},
            {"item": "medium sweet potato, cut into 1/2-inch chunks", "quantity": "1", "unit": ""},
            {"item": "turnips, cut into 1/2-inch chunks", "quantity": "1/2", "unit": "lb"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "coarse salt", "quantity": "", "unit": "pinch"},
            {"item": "chopped sage", "quantity": "2", "unit": "tsp"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "maple vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "whole grain mustard", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 425°F."},
            {"step": 2, "text": "Toss the vegetables with enough oil to generously coat. Spread out on a baking sheet so that they are not touching, and sprinkle with a little coarse salt and fresh sage."},
            {"step": 3, "text": "Roast, shaking the pan often until the vegetables are tender and begin to brown, about 30 to 40 minutes."},
            {"step": 4, "text": "In a small bowl, mix together the maple syrup, maple vinegar, and mustard and brush over the roasted vegetables."},
            {"step": 5, "text": "Return to the oven and roast another 7 to 10 minutes to glaze."},
            {"step": 6, "text": "Remove and serve warm."}
        ],
        "temperature": "425°F (220°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "roasted", "vegetables", "maple", "sage", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    }
]

def main():
    with open('data/recipes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    for recipe in new_recipes:
        if recipe['id'] in existing_ids:
            print(f"ERROR: Recipe ID '{recipe['id']}' already exists!")
            return False

    data['recipes'].extend(new_recipes)
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    with open('data/recipes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
