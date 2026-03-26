#!/usr/bin/env python3
"""Add fifth batch of Sioux Chef recipes - Indigenous Pantry components"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "wojape-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wojape (Traditional Berry Sauce)",
        "native_name": "Wóžapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 173",
        "description": "The scent of this traditional sauce simmering on the stove takes me back to my freewheeling six-year-old self. Our family relied on the local chokecherries I gathered as a kid. We'd spread a blanket under the trees and gather buckets full. There's no need to pit them because the pits drop to the bottom of the pot as the sauce becomes thick and lush. We'd sweeten it for dessert or serve it as a tangy sauce for meat and game and vegetables, and as a dressing.",
        "servings_yield": "Makes about 4 to 6 cups",
        "ingredients": [
            {"item": "fresh berries—chokecherries or a mix of blueberries, raspberries, strawberries, elderberries, cranberries, blackberries", "quantity": "6", "unit": "cups"},
            {"item": "water", "quantity": "1 to 1 1/2", "unit": "cups"},
            {"item": "honey or maple syrup", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the berries and water into a saucepan and set over low heat."},
            {"step": 2, "text": "Bring to a simmer and cook, stirring occasionally, until the mixture is thick."},
            {"step": 3, "text": "Taste and season with honey or maple syrup as desired."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sauce", "berries", "chokecherries", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["wojape-mint-sauce-sioux-chef", "braised-sunflowers-sioux-chef"]
    },
    {
        "id": "corn-stock-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Corn Stock",
        "native_name": "Wagmíza Haŋpí",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 170",
        "description": "Save the corncobs after you've enjoyed boiled or roasted corn on the cob or you've cut the kernels for use in a recipe. This stock adds wonderful corn flavor to soups, stews, and sauces.",
        "servings_yield": "Makes about 4 cups",
        "ingredients": [
            {"item": "corncobs (kernels removed)", "quantity": "4 to 6", "unit": ""},
            {"item": "water", "quantity": "", "unit": "to cover by about 1 inch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the corncobs into a pot and cover with water by about 1 inch."},
            {"step": 2, "text": "Bring to a boil and partially cover."},
            {"step": 3, "text": "Reduce the heat and simmer until the stock tastes 'corny,' about 1 hour."},
            {"step": 4, "text": "Discard the cobs."},
            {"step": 5, "text": "Store the stock in a covered container in the refrigerator or freezer."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "stock", "corn", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["sauteed-corn-mushrooms-sioux-chef", "braised-sunflowers-sioux-chef"]
    },
    {
        "id": "wild-rice-stock-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Stock",
        "native_name": "Psíŋ Haŋpí",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 170",
        "description": "Do not discard wild rice cooking water. It makes an excellent cooking stock for soups, stews, and sauces. Wild rice stock is also the base for Wild Rice Sorbet, page 149.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "wild rice cooking water", "quantity": "", "unit": "reserved from cooking wild rice"}
        ],
        "instructions": [
            {"step": 1, "text": "Reserve the cooking water after preparing wild rice."},
            {"step": 2, "text": "Store in a covered container in the refrigerator or freezer for use in soups, stews, and sauces."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "stock", "wild rice", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "cedar-bean-stock-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cedar Bean Stock",
        "native_name": "Haŋté Apé úŋ Omníča Lolóbyapi Haŋpí",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 170",
        "description": "Reserve the leftover cooking liquid when preparing the Cedar-Braised Beans, page 36, for use in soups, stews, and sauces.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "cooking liquid from Cedar-Braised Beans, page 36", "quantity": "", "unit": "reserved"}
        ],
        "instructions": [
            {"step": 1, "text": "Reserve the cooking liquid after preparing Cedar-Braised Beans."},
            {"step": 2, "text": "Store in a covered container in the refrigerator or freezer for use in soups, stews, and sauces."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "stock", "beans", "cedar", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "puffed-wild-rice-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Puffed Wild Rice",
        "native_name": "Psíŋ Nabláhyapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 175",
        "description": "Like popcorn or puffed amaranth, puffed wild rice makes a terrific garnish for salads or soups and a great addition to griddled cakes and cookies. Light and crunchy, nutty tasting, it's a wonderful snack, too.",
        "servings_yield": "Makes 2 cups",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "1", "unit": "tbsp"},
            {"item": "wild rice, rinsed", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Pat the rice with a clean cloth or paper towels so that it's thoroughly dry."},
            {"step": 2, "text": "Heat a heavy-bottomed saucepan over high heat."},
            {"step": 3, "text": "When the pot is hot, add the oil and wild rice. Cover the pan and shake vigorously to coat the wild rice thoroughly."},
            {"step": 4, "text": "Reduce the heat to medium and continue shaking until you can hear the rice popping."},
            {"step": 5, "text": "Sprinkle the rice with a little salt before serving."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "snack", "garnish", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "smoked-salt-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Salt",
        "native_name": "",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 183",
        "description": "Smoked salts are available in the spice aisles of supermarkets, in specialty shops, and online. Making your own is relatively easy.",
        "servings_yield": "Makes 2 cups",
        "ingredients": [
            {"item": "wood chips soaked in cold water for 1 hour, drained", "quantity": "2", "unit": "cups"},
            {"item": "coarse salt", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare the grill for indirect heat (putting the hot coals on one side so that there is a cool side to work from)."},
            {"step": 2, "text": "Toss the drained wood chips on the coals."},
            {"step": 3, "text": "Spread the salt in a thin layer in an aluminum foil pan and place it on the grate away from the fire."},
            {"step": 4, "text": "Cover the grill and adjust the vent holes for medium heat. Smoke the salt for 1 hour."},
            {"step": 5, "text": "Remove, allow to cool at room temperature, and then store in a covered jar."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "salt", "smoked", "seasoning", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "sumac-lemonade-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sumac Lemonade",
        "native_name": "Čhaŋží Sú Haŋpí",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 163",
        "description": "The staghorn sumac tree's fat clusters of berries ripen around mid-August into a burnished ruddy red. They make a pretty pink lemonade.",
        "servings_yield": "Makes about 4 cups",
        "ingredients": [
            {"item": "red sumac clusters", "quantity": "12", "unit": ""},
            {"item": "cold water", "quantity": "1", "unit": "gallon"},
            {"item": "honey or maple syrup", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Pick a dozen red clusters. Rub and crunch them and add to a gallon of cold water."},
            {"step": 2, "text": "Allow them to steep for 10 to 20 minutes."},
            {"step": 3, "text": "Strain the liquid through a fine-mesh strainer or a colander lined with cheesecloth into a pitcher."},
            {"step": 4, "text": "Sweeten to taste with honey or maple syrup."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "beverage", "sumac", "lemonade"],
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
