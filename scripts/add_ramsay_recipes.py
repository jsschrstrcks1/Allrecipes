#!/usr/bin/env python3
"""Add new Gordon Ramsay recipes to recipes.json"""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

NEW_RECIPES = [
    {
        "id": "creamy-asparagus-risotto-lemon-mascarpone",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Creamy Asparagus Risotto with Lemon and Mascarpone",
        "category": "mains",
        "attribution": "Gordon Ramsay",
        "source_note": "Hell's Kitchen Cookbook, pages 105-107",
        "description": "A green-hued arborio rice dish that often catches the camera as it's served as an app to Hell's Kitchen diners. Kevin Cottle mastered this in Season 6's final four competition.",
        "servings_yield": "4 servings",
        "total_time": "35 minutes",
        "temperature": "",
        "ingredients": [
            {"item": "asparagus, bottoms trimmed and discarded", "quantity": "1", "unit": "lb"},
            {"item": "kosher salt", "quantity": "", "unit": "to taste"},
            {"item": "freshly ground black pepper", "quantity": "", "unit": "to taste"},
            {"item": "vegetable stock or chicken stock", "quantity": "5 1/2", "unit": "cups"},
            {"item": "olive oil", "quantity": "1", "unit": "tbsp"},
            {"item": "white onion, finely diced", "quantity": "2/3", "unit": "cup"},
            {"item": "arborio rice or medium-grain white rice", "quantity": "1 1/3", "unit": "cups"},
            {"item": "dry white wine", "quantity": "1/3", "unit": "cup"},
            {"item": "Parmesan cheese, plus more to taste", "quantity": "1/3", "unit": "cup"},
            {"item": "lemon juice", "quantity": "1/2", "unit": "lemon"},
            {"item": "mascarpone", "quantity": "1", "unit": "tbsp"},
            {"item": "lemon zest, for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "For the asparagus puree: In a medium skillet, blanch the asparagus, whole, in boiling salted water for 2 minutes or until al dente. Remove the spears with a slotted spoon and shock in ice water. Reserve a half cup of the blanching liquid."},
            {"step": 2, "text": "Cut 2 inches from the tops and set aside. Thinly slice the bottoms and put them in the blender on low. Add just enough of the blanching water to loosen and start pureeing. Blend on high until smooth. Season with salt and pepper."},
            {"step": 3, "text": "For the risotto: In a small saucepan, heat the stock and maintain at a slow simmer."},
            {"step": 4, "text": "Heat the olive oil in heavy large saucepan over moderate heat. Add onion and saute until tender and translucent, about 4-5 minutes. Add the rice and stir 1 minute. Add wine and cook until absorbed, stirring often, 1-2 minutes."},
            {"step": 5, "text": "Add 1/2 cup of stock and simmer until the liquid is absorbed, stirring occasionally, 2-3 minutes. Continue in this manner, adding hot stock a half cup at a time until all of the stock has been added and absorbed and the rice is just tender and mixture is creamy, total cooking time 25 minutes."},
            {"step": 6, "text": "Stir in the Parmesan cheese, then add the asparagus puree, reserved asparagus tips, lemon juice, and mascarpone, stirring gently to combine and heat through. Season to taste with salt and pepper, garnish with lemon zest, and serve with more Parmesan."}
        ],
        "tags": ["risotto", "asparagus", "vegetarian", "Italian", "Hell's Kitchen"],
        "image_refs": [
            "Hells Kitchen Gordan Ramsay/IMG_7565 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7566 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7567 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7568 Medium.jpeg"
        ],
        "confidence": {"overall": "high", "flags": []},
        "nutrition": {
            "status": "insufficient_data",
            "per_serving": {},
            "missing_inputs": [],
            "assumptions": []
        }
    },
    {
        "id": "eggplant-involtini-spicy-red-pepper-emulsion",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Eggplant Involtini with Spicy Red Pepper Emulsion",
        "category": "mains",
        "attribution": "Gordon Ramsay",
        "source_note": "Hell's Kitchen Cookbook, pages 109-111",
        "description": "Involtini for vegetarians - eggplant's meaty texture makes it sturdy enough to stand up to the stuffing and rolling. A red pepper emulsion stands in for the tomato sauce that eggplant involtini is typically baked in.",
        "servings_yield": "4 servings",
        "total_time": "1 hour",
        "temperature": "450F (230C), then 350F (175C)",
        "pan_size": "8-inch-square baking dish",
        "ingredients": [
            {"item": "olive oil", "quantity": "1", "unit": "tbsp"},
            {"item": "garlic clove, thinly sliced", "quantity": "1", "unit": ""},
            {"item": "small shallot, thinly sliced", "quantity": "1/2", "unit": ""},
            {"item": "red bell peppers, cored and seeded, cut into 1/2-inch pieces", "quantity": "2", "unit": "large"},
            {"item": "kosher salt, plus more to taste", "quantity": "1/2", "unit": "tsp"},
            {"item": "sugar", "quantity": "1/2", "unit": "tsp"},
            {"item": "chicken stock", "quantity": "1/2", "unit": "cup"},
            {"item": "crushed tomatoes, with juices", "quantity": "1/4", "unit": "cup"},
            {"item": "crushed red pepper, to taste", "quantity": "", "unit": ""},
            {"item": "freshly ground black pepper", "quantity": "", "unit": "to taste"},
            {"item": "large eggplant", "quantity": "1 1/2", "unit": "lb"},
            {"item": "whole-milk ricotta cheese", "quantity": "1", "unit": "cup"},
            {"item": "fresh mozzarella cheese, shredded", "quantity": "1/4", "unit": "lb", "prep_note": "about 1 cup"},
            {"item": "large egg, lightly beaten", "quantity": "1", "unit": ""},
            {"item": "grated Parmigiano-Reggiano cheese", "quantity": "1/2", "unit": "cup"},
            {"item": "chopped fresh basil and/or flat-leaf parsley", "quantity": "1", "unit": "tbsp"},
            {"item": "olive oil for brushing", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "For the spicy red pepper emulsion: In a medium saucepan, combine olive oil and garlic over medium-low heat and saute until garlic is aromatic, about 1 minute. Add shallot and saute until translucent. Stir in peppers, salt, and sugar. Cover and cook for 5 minutes. Add chicken stock and crushed tomatoes and simmer, partially covered, until peppers are tender, about 8 minutes. Puree with an immersion blender. Transfer to a bowl and season with crushed red pepper and salt to taste."},
            {"step": 2, "text": "For the eggplant involtini: Trim the eggplant, then cut lengthwise into eight 1/4-inch-thick slices. Layer the slices in a colander set over a plate, sprinkling each layer with salt, and let stand for 30 minutes to drain."},
            {"step": 3, "text": "Preheat the oven to 450F."},
            {"step": 4, "text": "Meanwhile, in a bowl, stir together the ricotta, mozzarella, egg, 2 tablespoons Parmigiano-Reggiano, and the basil/parsley, and season with fresh pepper."},
            {"step": 5, "text": "Wipe the eggplant and pat dry with paper towels. Brush the slices on both sides with olive oil, then arrange them in a single layer on a rimmed baking sheet lined with parchment paper."},
            {"step": 6, "text": "Bake the slices in the lower third of the oven until lightly browned on the bottom, 8-10 minutes. Turn the slices over and continue to bake until browned on the second side and tender, 8-10 minutes more. Remove the eggplant from the oven. Reduce the temperature to 350F."},
            {"step": 7, "text": "Spoon a thin layer of the red pepper sauce into an 8-inch-square baking dish. Place a spoonful of the cheese mixture near one end of a slice of eggplant and roll up the slice. Place the roll, seam side down, in the dish. Repeat with remaining eggplant. Spoon the remaining sauce over the rolls, then sprinkle evenly with the remaining Parmigiano-Reggiano."},
            {"step": 8, "text": "Bake the rolls until the sauce is bubbling hot and the rolls are heated through, about 25 minutes. Allow to set 5 minutes before serving."},
            {"step": 9, "text": "Divide the rolls among the four plates and serve immediately."}
        ],
        "tags": ["vegetarian", "Italian", "eggplant", "cheese", "Hell's Kitchen"],
        "image_refs": [
            "Hells Kitchen Gordan Ramsay/IMG_7569 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7570 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7571 Medium.jpeg",
            "Hells Kitchen Gordan Ramsay/IMG_7572 Medium.jpeg"
        ],
        "confidence": {"overall": "high", "flags": []},
        "nutrition": {
            "status": "insufficient_data",
            "per_serving": {},
            "missing_inputs": [],
            "assumptions": []
        }
    }
]

def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    # Check for duplicates
    existing_ids = {r['id'] for r in data['recipes']}

    added = 0
    for recipe in NEW_RECIPES:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            print(f"Skipped (exists): {recipe['title']}")

    # Update metadata
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = str(date.today())

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nTotal recipes now: {len(data['recipes'])}")
    print(f"Added {added} new recipes")

if __name__ == "__main__":
    main()
