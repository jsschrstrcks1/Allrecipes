#!/usr/bin/env python3
"""Add second batch of Sioux Chef recipes to recipes.json"""

import json
from datetime import datetime

# New recipes to add
new_recipes = [
    {
        "id": "duck-egg-aioli-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Duck Egg Aioli",
        "native_name": "Magáksica Witka na Pšíŋkčeka Iyúlthuŋ",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 23",
        "description": "This homemade sauce has a velvety texture and rich flavor. It's a great foundation for the variety of sauces we use to dress grilled or roasted vegetables, daub on meats, and slather on savory cakes.",
        "servings_yield": "Makes about 1 1/2 cups",
        "ingredients": [
            {"item": "duck egg yolks, at room temperature", "quantity": "2", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "dry mustard or Dijon mustard", "quantity": "1 tsp or 1 tbsp", "unit": ""},
            {"item": "sunflower oil", "quantity": "1 to 1 1/4", "unit": "cups"},
            {"item": "maple vinegar", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "In a small bowl, whisk the egg yolk until thick and sticky."},
            {"step": 2, "text": "Whisk in the salt, sumac, juniper, and mustard."},
            {"step": 3, "text": "Slowly drip in the oil, a little at a time. Once the mix begins to thicken, whisk in the remaining oil in a slow, steady stream."},
            {"step": 4, "text": "Whisk in the maple vinegar. Season to taste with the juniper."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "maple vinegar", "substitute": "apple cider vinegar", "note": "Use if maple vinegar isn't available"}
        ],
        "tags": ["indigenous", "native american", "sauce", "aioli", "duck eggs", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["deviled-duck-eggs-sioux-chef"]
    },
    {
        "id": "deviled-duck-eggs-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Deviled Duck Eggs",
        "native_name": "Magáksica Witka na Wathótho yužápi nakúŋ Waŋčázi Čhamní",
        "category": "appetizers",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 21",
        "description": "Duck eggs are bigger and far richer-tasting than chicken eggs. If they're not available, simply substitute 1 jumbo chicken egg for each duck egg in any given dish. This makes a terrific starter course or a nice, light lunch.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "duck eggs", "quantity": "4", "unit": ""},
            {"item": "Duck Egg Aioli, page 23", "quantity": "1/2", "unit": "cup"},
            {"item": "maple syrup", "quantity": "", "unit": "splash, or more to taste"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "sumac", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the eggs into a large pot and cover with cold water by 3 inches. Set over a medium flame, bring to a boil, reduce the heat, and simmer for 8 minutes."},
            {"step": 2, "text": "Remove, drain, and run the eggs under cold water."},
            {"step": 3, "text": "Peel, slice in half, then remove the yolks to a food processor fitted with a steel blade."},
            {"step": 4, "text": "Add the remaining ingredients and process until very smooth. Adjust the seasoning."},
            {"step": 5, "text": "Spoon the yolk mixture back into the white halves."}
        ],
        "notes": [],
        "tips": [
            "Find duck eggs at most natural food co-ops and farmers markets. You may substitute 1 jumbo chicken egg per 1 duck egg.",
            "Find smoked salt in the spice sections of most grocery stores, co-ops, specialty shops, and online. To make your own, see page 183."
        ],
        "substitutions": [
            {"original": "duck eggs", "substitute": "jumbo chicken eggs", "note": "Substitute 1 jumbo chicken egg for each duck egg"}
        ],
        "tags": ["indigenous", "native american", "appetizer", "eggs", "duck eggs"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["duck-egg-aioli-sioux-chef"],
        "is_component": False
    },
    {
        "id": "roasted-corn-wild-greens-pesto-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Roasted Corn with Wild Greens Pesto",
        "native_name": "Wagmíza na Wathótho yužápi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 13",
        "description": "Corn, when it's just picked, is full of natural sugars that caramelize to perfection on the grill or in a hot oven. Nothing could be easier or more satisfying than freshly roasted sweet corn.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "large ears fresh, sweet corn", "quantity": "4 to 6", "unit": ""},
            {"item": "sunflower or hazelnut oil", "quantity": "", "unit": ""},
            {"item": "Wild Greens Pesto, page 24", "quantity": "2 to 3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare a hot charcoal grill or preheat the broiler to high."},
            {"step": 2, "text": "Shuck the corn and rub lightly with the oil."},
            {"step": 3, "text": "Set the corn directly on the grill or under the broiler and roast, rolling the cobs occasionally, until all sides are nicely browned, being careful they don't burn, about 5 to 7 minutes' total cooking time."},
            {"step": 4, "text": "Serve with dollops of Wild Greens Pesto."}
        ],
        "notes": [
            "1 ear of corn will yield about 1 cup of corn kernels.",
            "Save those corn cobs for Corn Stock, page 170."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "corn", "grilled", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["wild-greens-pesto-sioux-chef"],
        "is_component": False
    },
    {
        "id": "wojape-mint-sauce-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wojape Mint Sauce",
        "native_name": "Wóžapi nakúŋ Čheyáka Iyúlthuŋ",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 15",
        "description": "This is terrific with bitter greens such as watercress, dandelion, or sorrel. Store in a covered container in the refrigerator for 3 to 5 days.",
        "servings_yield": "Makes about 1/2 cup",
        "ingredients": [
            {"item": "Wojape, page 173", "quantity": "1/4", "unit": "cup"},
            {"item": "maple vinegar, page 18", "quantity": "1", "unit": "tbsp"},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "maple syrup", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "generous pinch"},
            {"item": "chopped mint", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Whisk all the ingredients together in a small bowl."},
            {"step": 2, "text": "Taste and adjust the seasonings."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sauce", "mint", "wojape", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["three-sisters-salad-sioux-chef"]
    },
    {
        "id": "salad-griddled-squash-apples-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Salad of Griddled Squash, Apples, Wild Greens, and Toasted Walnuts",
        "native_name": "Wathókeca Íčhičahiya nakúŋ Čhaŋháŋpi Tiktíča Mniškúmna",
        "category": "salads",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 17",
        "description": "A sweet-savory toss-up, this hearty salad makes great use of leftover roasted squash or pumpkin. Use any of the winter squash varieties.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "small acorn or delicata squash, seeded, peeled, and sliced into pieces 1 inch long and 1/4 inch thick", "quantity": "1", "unit": ""},
            {"item": "medium or 2 small apples, cored and cut into rounds", "quantity": "1", "unit": ""},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "chopped sage leaves", "quantity": "1", "unit": "tsp"},
            {"item": "mixed wild greens", "quantity": "6 to 8", "unit": "cups"},
            {"item": "Maple Dressing, page 18", "quantity": "1/4", "unit": "cup"},
            {"item": "dried cranberries", "quantity": "1/4", "unit": "cup"},
            {"item": "toasted, chopped walnuts", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Brush the squash and apple pieces with a little of the oil."},
            {"step": 2, "text": "Heat a skillet or griddle over medium-high heat and pan-roast the squash until nicely toasted on both sides and tender, about 5 to 10 minutes per side. Remove and set aside."},
            {"step": 3, "text": "Toast the apple slices on each side until slightly browned, about 1 to 2 minutes per side. Remove and set aside."},
            {"step": 4, "text": "Toss the greens, sage, and cranberries with the dressing and arrange on a serving platter or individual serving plates."},
            {"step": 5, "text": "Arrange the squash and apple over the greens and drizzle with a little more dressing as desired, and scatter the walnuts over all."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "salad", "squash", "apples", "fall"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["maple-dressing-sioux-chef"],
        "is_component": False
    },
    {
        "id": "three-sisters-salad-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Three Sisters Summertime Salad with Smoked Trout",
        "native_name": "Blokétu Wathótho Íčhičahiya",
        "category": "salads",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 14",
        "description": "Together, the three 'sisters' are a nutritional powerhouse. The corn's complex carbohydrates, the protein-rich beans, and the squash's vitamins make a complete meal. Corn nuts are tossed in for crunch, but sunflower and pepita seeds work equally well, too.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "summer squash, cut into 1/4-inch slices", "quantity": "1", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "1", "unit": "tbsp"},
            {"item": "Roasted Corn, page 13, kernels cut from cob", "quantity": "2", "unit": "ears"},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1", "unit": "cup"},
            {"item": "Wojape Mint Sauce, page 15", "quantity": "1/4", "unit": "cup"},
            {"item": "dandelion greens (plus mix of wild greens)", "quantity": "", "unit": ""},
            {"item": "smoked trout, cut into half-inch strips", "quantity": "4", "unit": "oz"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat a griddle or large heavy skillet over high heat, brush with oil, and sear the squash slices on both sides, about 3 minutes. Set aside."},
            {"step": 2, "text": "Turn the corn, beans, and summer squash into a large mixing bowl."},
            {"step": 3, "text": "Toss with just enough mint sauce to lightly coat and serve on a bed of the mixed greens."},
            {"step": 4, "text": "Lay the trout over the salad."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "salad", "three sisters", "corn", "beans", "squash", "trout"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["cedar-braised-beans-sioux-chef", "wojape-mint-sauce-sioux-chef"],
        "is_component": False
    },
    {
        "id": "sauteed-corn-mushrooms-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sautéed Corn Mushrooms with Fresh Corn and Fried Sage",
        "native_name": "Wagmíza na Wagmíza Aíčhaǧe na Phežíȟota Čheúŋpapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 29-31",
        "description": "This dish reminds me of the year I spent in Mexico, where corn is celebrated in all of its forms. Corn smut or maize mushrooms are considered a delicacy and it's no wonder. They impart a sweet, earthy corn flavor to soups, stews, and sautés and are especially delicious cooked with corn. This is delicious served over Corn Cakes, page 51, or Crispy Bean Cakes, page 38.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "diced fresh mushrooms", "quantity": "3", "unit": "cups"},
            {"item": "corn mushrooms or dried, reconstituted wild mushrooms, such as chanterelles", "quantity": "1", "unit": "cup"},
            {"item": "chopped wild onions or shallots", "quantity": "1/4", "unit": "cup"},
            {"item": "sweet corn kernels", "quantity": "2", "unit": "cups"},
            {"item": "soaked and cooked hominy, page 31", "quantity": "1", "unit": "cup"},
            {"item": "Corn Stock, page 170, or mushroom soaking water", "quantity": "1/4", "unit": "cup"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "chopped sage", "quantity": "2", "unit": "tsp"},
            {"item": "chopped mint", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "sage leaves", "quantity": "6", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Film the skillet with 2 tablespoons of the oil and set over medium heat and sauté the fresh mushrooms with the corn mushrooms until very dark, about 5 to 7 minutes."},
            {"step": 2, "text": "Add the onions and continue cooking until the onion is translucent."},
            {"step": 3, "text": "Then add the corn kernels and hominy. Cook, stirring occasionally, until the fresh corn is just cooked and tender, about 5 minutes."},
            {"step": 4, "text": "Stir in the corn stock, chopped sage, and mint and cook until the liquid reduces by half. Season with salt and juniper to taste."},
            {"step": 5, "text": "In a small skillet, heat the remaining oil over high flame and fry the sage leaves until dark and crisp, about 15 to 30 seconds per side."},
            {"step": 6, "text": "Serve the corn hot or at room temperature topped with the fried sage leaves."}
        ],
        "notes": [
            "To reconstitute wild mushrooms, simply cover with warm water and let sit until plump. Drain, reserving the soaking water, and squeeze out any excess moisture. Use as you would fresh mushrooms."
        ],
        "tips": [
            "To prepare hominy or dried corn, soak in water to cover overnight. Drain and turn into a pot and cover with water by 2 inches. Set over medium-high heat, bring to a boil, reduce the heat, and simmer until the kernels are tender, 10 to 25 minutes. Drain and proceed with the recipe.",
            "If you know a corn farmer and can get your hands on fresh corn mushrooms, by all means use those in this dish. Otherwise, use frozen or canned and drained corn mushrooms available in Mexican and specialty stores and online."
        ],
        "substitutions": [
            {"original": "corn mushrooms (huitlacoche)", "substitute": "dried reconstituted wild mushrooms such as chanterelles", "note": ""}
        ],
        "tags": ["indigenous", "native american", "corn", "mushrooms", "huitlacoche", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
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
