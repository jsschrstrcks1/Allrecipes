#!/usr/bin/env python3
"""Add first batch of Sioux Chef recipes to recipes.json"""

import json
from datetime import datetime

# New recipes to add
new_recipes = [
    {
        "id": "maple-dressing-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple Dressing",
        "native_name": "Čhaŋháŋpi Tiktíča Mniškúmna",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 18",
        "description": "This sweet-and-sour dressing was inspired by the traditional 'sour sap,' or fermented maple sap, traditionally used to season roasting meat.",
        "servings_yield": "Makes 3/4 cup",
        "ingredients": [
            {"item": "maple vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "1/3", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp", "prep_note": "or more to taste"},
            {"item": "powdered mustard or Dijon mustard", "quantity": "generous pinch or 1 tsp", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put all of the ingredients into a small jar and shake vigorously."},
            {"step": 2, "text": "Season to taste with the salt."}
        ],
        "notes": [],
        "tips": [
            "Maple vinegar is fermented from the sap collected at the end of the maple season. Because it is lower in sugar, it is thinner and more difficult to boil into syrup. Left out, it becomes what Native Americans called 'sour sap.'",
            "Maple vinegar is available through specialty grocers and may be ordered online; substitute apple cider vinegar when maple vinegar is not available."
        ],
        "substitutions": [
            {"original": "maple vinegar", "substitute": "apple cider vinegar", "note": "Use when maple vinegar is not available"}
        ],
        "tags": ["indigenous", "native american", "dressing", "sauce", "maple", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "tamarack-honey-drizzle-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tamarack Honey Drizzle",
        "native_name": "Wičháyažipa Thúŋkče Akáštaŋpi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 20",
        "description": "The tender spring shoots of the tamarack tree are nutritious, slightly sweet, and a little piney. We keep this drizzle on hand for brushing over game and vegetables and for sweetening tea.",
        "servings_yield": "Makes 1/2 cup",
        "ingredients": [
            {"item": "honey", "quantity": "1/2", "unit": "cup"},
            {"item": "tamarack shoots or fresh rosemary", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "In a small saucepan, warm the honey and tamarack shoots until baby-bottle temperature."},
            {"step": 2, "text": "Puree in a blender or food processor, adding a little water to thin as necessary."},
            {"step": 3, "text": "Transfer to a clean glass jar and store on the counter out of sunlight."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "tamarack shoots", "substitute": "fresh rosemary", "note": "Use when tamarack is not available"}
        ],
        "tags": ["indigenous", "native american", "sauce", "honey", "drizzle", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["spring-salad-tamarack-honey-sioux-chef"]
    },
    {
        "id": "wild-greens-pesto-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Greens Pesto",
        "native_name": "Wathótho yužápi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 24",
        "description": "To make a bold, flavorful pesto, balance a range of flavors: fragrant mint, potent mustard, citrusy sorrel or purslane, bitter dandelion, neutral lamb's quarters. Making pesto the old-fashioned way by pounding together the greens, nuts, and oil yields a thick, rough sauce.",
        "servings_yield": "Makes 1 1/2 cups",
        "ingredients": [
            {"item": "wild greens", "quantity": "2", "unit": "cups", "prep_note": "some combination of sorrel, dandelion greens, purslane, lamb's quarters, wild mint, and mustard"},
            {"item": "wild onion or chopped shallot", "quantity": "1 or 1/4 cup", "unit": ""},
            {"item": "toasted sunflower seeds", "quantity": "1/4", "unit": "cup"},
            {"item": "sunflower or hazelnut oil", "quantity": "2/3 to 3/4", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "maple sugar", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Pound together the greens, onion or shallot, and sunflower seeds with a mortar and pestle or by whizzing in a food processor fitted with a steel blade."},
            {"step": 2, "text": "Slowly work in the oil and season to taste with salt and a little maple sugar."}
        ],
        "notes": [
            "To toast sunflower seeds, see page 158 or use unsalted toasted sunflower seeds, available in the bulk section of the co-op or packaged."
        ],
        "tips": [
            "If you'd like something smoother, blend it all together in a food processor fitted with a steel blade.",
            "This will keep a week or more in the refrigerator in a covered container.",
            "Wood sorrel, like its domestic cousin, adds a bright, lemony flavor to this sauce."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "pesto", "sauce", "wild greens", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["roasted-corn-wild-greens-pesto-sioux-chef"]
    },
    {
        "id": "cedar-braised-beans-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cedar-Braised Beans",
        "native_name": "Haŋté Apé uŋ Omníča Lolóbyapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 36-37",
        "description": "Just a small branch of cedar adds flavor to these beans and helps to stimulate digestion and strengthen the immune system. We make up a big batch of these beans each week, then work them into a variety of dishes—appetizers, soups, and entrées.",
        "servings_yield": "Makes 2 1/2 to 3 cups",
        "ingredients": [
            {"item": "dried beans", "quantity": "1", "unit": "cup"},
            {"item": "cold water", "quantity": "3", "unit": "cups"},
            {"item": "branch cedar", "quantity": "1", "unit": "5 to 6-inch"},
            {"item": "salt and freshly ground juniper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the beans in a large pot or bowl, and cover with water by 3 inches. Allow to soak for at least six hours or overnight."},
            {"step": 2, "text": "Drain the beans and transfer to a medium saucepan or soup pot."},
            {"step": 3, "text": "Add 3 cups of cold water to the pot and lay the cedar branch over the beans. Set the pot over high heat, bring to a boil."},
            {"step": 4, "text": "Cover and simmer until the beans are very soft. Begin tasting after about 25 minutes of simmering."},
            {"step": 5, "text": "Remove and discard the cedar. Drain and reserve the cooking liquid for soups and stews."},
            {"step": 6, "text": "Serve the beans or store in a covered container in the refrigerator for several days or freeze."}
        ],
        "notes": [
            "The first step is to soak the beans before cooking; it cuts the time in half.",
            "This recipe is easily doubled or tripled.",
            "We like to use a mix of heirloom beans for a variety of colors, textures, and flavors. Because of the varied cooking times, we cook them separately and then combine them in a soup, hot dish, or salad before finishing the dish.",
            "Be sure to save the bean cooking water for a stock to use in soups and stews."
        ],
        "tips": [
            "For Maple Beans: Stir 1 to 2 tablespoons of maple syrup into the pot before removing the beans from the stove.",
            "For Mashed Beans: Put the beans and a little of the cooking liquid into a large bowl. Using an immersion blender, food processor fitted with a steel blade, or blender, puree the beans to make a thick paste. Season with salt and ground juniper."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "beans", "side dish", "cedar", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["three-sisters-salad-sioux-chef"]
    },
    {
        "id": "spring-salad-tamarack-honey-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Spring Salad with Tamarack Honey Drizzle",
        "native_name": "Wétu Wathótho Íčhičahiya nakúŋ Wičháyažipa Thúŋkče",
        "category": "salads",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 19-20",
        "description": "One late-spring evening near the shores of Lake Vermillion, in northern Minnesota, Dana, and I set out to forage for a community dinner later that night. Right outside our doorstep the tamarack trees offered their beautiful little buds, so tender, sweet, and delicious. We harvested a full pail and then, walking back, discovered a big patch of hopniss nearby.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "hopniss, scrubbed, or yucca", "quantity": "1", "unit": "cup", "prep_note": "cut into 1-inch chunks"},
            {"item": "sunflower or nut oil", "quantity": "2", "unit": "tbsp"},
            {"item": "Tamarack Honey Drizzle, page 20", "quantity": "2 to 3", "unit": "tbsp"},
            {"item": "shredded Dried Rabbit, page 115, or good-quality turkey or bison jerky", "quantity": "1", "unit": "cup"},
            {"item": "pea shoots or sliced snap peas", "quantity": "2", "unit": "cups"},
            {"item": "mixed wild greens", "quantity": "6 to 8", "unit": "cups"},
            {"item": "sunflower sprouts", "quantity": "1", "unit": "cup"},
            {"item": "sunflower seeds", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the hopniss into a pot and cover with cold water by 2 inches. Set over high heat, bring to a boil, reduce the flame, and simmer until tender, about 10 to 20 minutes. Drain and set aside."},
            {"step": 2, "text": "In a small bowl, whisk together the oil and Tamarack Honey Drizzle."},
            {"step": 3, "text": "In a separate bowl, toss together the dried meat, pea shoots, and enough of the Tamarack Honey Drizzle-oil mixture to lightly coat."},
            {"step": 4, "text": "Arrange the greens on a large serving platter or individual plates. Arrange the meat and peas over the greens and drizzle with a little more of the Tamarack Honey Drizzle."},
            {"step": 5, "text": "Garnish with the sunflower sprouts and sunflower seeds."}
        ],
        "notes": [],
        "tips": [
            "If using yucca instead of hopniss, peel the yucca, cut into chunks, and boil until tender, 5 to 10 minutes."
        ],
        "substitutions": [
            {"original": "hopniss", "substitute": "yucca", "note": "Peel the yucca, cut into chunks, and boil until tender, 5 to 10 minutes"},
            {"original": "Dried Rabbit", "substitute": "good-quality turkey or bison jerky", "note": ""}
        ],
        "tags": ["indigenous", "native american", "salad", "spring", "hopniss", "tamarack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["tamarack-honey-drizzle-sioux-chef"],
        "is_component": False
    }
]

def main():
    # Read existing recipes
    with open('data/recipes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check for duplicate IDs
    existing_ids = {r['id'] for r in data['recipes']}
    for recipe in new_recipes:
        if recipe['id'] in existing_ids:
            print(f"ERROR: Recipe ID '{recipe['id']}' already exists!")
            return False

    # Add new recipes
    data['recipes'].extend(new_recipes)

    # Update meta
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    # Write back
    with open('data/recipes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
