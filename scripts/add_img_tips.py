#!/usr/bin/env python3
"""
Add recovered tips from IMG Kindle cookbook images to recipes_master.json

This script processes all the tips found during the comprehensive
image audit of IMG_4695-5063 and adds them to the appropriate recipes.
"""

import json
from pathlib import Path
from datetime import datetime

RECIPES_FILE = Path(__file__).parent.parent / "all" / "recipes_master.json"

# Comprehensive list of recovered tips from IMG images
# Format: recipe_title -> {tips: [...], other_updates}
IMG_RECOVERED_TIPS = {
    # === BATCH 4695-4750 (37-page Skillet Dinners cookbook) ===

    "Cheesy Pasta Skillet": {
        "tips": ["**Serve with Roasted Asparagus."]
    },

    "Goldie Chicken": {
        "tips": [
            "Scrape the bottom of the skillet with a wooden spatula to get all the browned bits dissolved (this is called deglazing the pan).",
            "**Serve with Sriracha Zucchini."
        ]
    },

    "Hamburger Steaks": {
        "tips": ["**Serve with mashed potatoes or rice and green beans."]
    },

    "Philly Cheesesteak": {
        "tips": ["Place the open rolls in the oven for 3-5 minutes or until the cheese is melted."]
    },

    "Spicy Shrimp Pasta": {
        "tips": ["Cook for another 3-4 minutes until the noodles and shrimp are combined with the cheese."]
    },

    "Double Decker Tacos": {
        "tips": ["I use onions, lettuce, cheese, and hot sauce for toppings."]
    },

    "Simple Shrimp Gumbo": {
        "tips": [
            "Transfer the oil and flour mixture (the roux) to a large soup pot.",
            "Serve over rice."
        ]
    },

    "Corn Soup": {
        "tips": ["Season with salt and pepper before serving."]
    },

    "Chicken Tortilla Soup": {
        "tips": ["Top with tortilla strips, cheese, and sour cream before serving."]
    },

    "Pepperoni Roll-Ups": {
        "tips": ["Serve with warm marinara sauce."]
    },

    "Chicken Nuggets": {
        "tips": ["Place the oats, parsley, garlic powder, onion powder, salt in your food processor and pulse until powdery."]
    },

    "One Pot Mac and Cheese": {
        "tips": [
            "Cover and let sit for five minutes then serve.",
            "**Serve with Cheesy Garlic Bread."
        ]
    },

    "Garlic Butter Shrimp Pasta": {
        "tips": ["Stir frequently to prevent sticking."]
    },

    "Salmon Patties": {
        "tips": ["**Serve with Mediterranean Vegetables."]
    },

    "Sriracha Zucchini": {
        "tips": ["This is a great side dish for Goldie Chicken."]
    },

    "Mediterranean Vegetables": {
        "tips": ["Serve immediately."]
    },

    # === BATCH 4751-4850 (Juicing & Quiche cookbooks) ===

    "Super Detox Apple Delight": {
        "tips": ["To improve the taste, you could add a little sea salt to the juice, stir and drink."]
    },

    "Exotic Delight": {
        "tips": [
            "Make sure not to overdo it on the ginger or you might not be able to stomach the strong taste.",
            "This juice is extremely good for sore throats and inflammation."
        ]
    },

    "Cleansing Lime Juice": {
        "tips": ["You can skip the ginger if you find the taste too pungent."]
    },

    "Green Juice Immune Booster": {
        "tips": ["A little garlic or ginger will add a little twist to the taste and make it more interesting."]
    },

    "Practical Deep Pie Crust": {
        "tips": [
            "Remember to be patient and try to keep your house nice and cool while making it.",
            "You can keep that dough refrigerated for a few days or can freeze it for a few months.",
            "If you are baking the pie crust alone, then it should normally take about 30 minutes."
        ]
    },

    "Extreme Blue Cheese Quiche": {
        "tips": ["When it's blended in the quiche, creamy and warm, it is just out of this world."]
    },

    "Cheese and Ham Quiche": {
        "tips": ["This would go perfectly with steamed broccoli or a vegetable medley."]
    },

    "Mixed Vegetable Quiche": {
        "tips": ["Serve with a garden salad or some corn fritters."]
    },

    "Awesome Spinach Quiche": {
        "tips": ["I like to use parmesan cheese with the spinach and some other seasonings, but you could choose other milder cheeses as well."]
    },

    "Mexican Style Quiche": {
        "tips": ["Combine quiche and Mexican casserole in one for a family surprise."]
    },

    "Bacon Quiche": {
        "tips": ["I love serving this bacon and cheese quiche for breakfast. It is much easier for me to mix all the ingredients in one bowl and leave it to cook for an hour than making 4 or 6 plates filled with bacon and eggs. Your family will love it, I promise."]
    },

    "Fresh Tomato Quiche": {
        "tips": [
            "Make sure you use fresh herbs if you can, they just add a little extra flavor to the quiche everyone likes.",
            "Slice and serve with your favorite side dishes."
        ]
    },

    "Herbs and Onions Quiche": {
        "tips": ["It may not be the best quiche to make if you are hosting your first romantic date because you might have onion breath! But I guarantee it's totally worth it otherwise."]
    },

    "Delightful Crab Quiche": {
        "tips": ["If you can't afford crab or prefer the imitation crab, then go for it."]
    },

    "Special Chicken Quiche": {
        "tips": [
            "Make sure you use cooked chicken as the time the quiche will stay in the oven with the other ingredients is not quite enough to fully cook chicken.",
            "A Caesar salad is awesome with this quiche."
        ]
    },

    # === BATCH 4851-4950 (Chili & Lebanese cookbooks) ===

    "Jan's Prize-Winning Chili": {
        "tips": ["Top servings with shredded cheese, sour cream and minced onion."]
    },

    "White Chicken Chili": {
        "tips": ["Garnish with cheese before serving."]
    },

    "Mom's Firehouse Chili": {
        "tips": ["Top with corn."]
    },

    "Donair": {
        "tips": ["Place a lid on your seasoned beef and place everything into the fridge for about four hours to marinate. More time is better."]
    },

    "Kibbee Lebanese Style": {
        "tips": [
            "Preferably this dish should be about 8 inches (pan size).",
            "At this point you should not see any pinkness in the meat.",
            "If you have a thermometer the temperature readout should be 160 degrees Fahrenheit or 70 Celsius."
        ]
    },

    "Lebanese Bean Salad": {
        "tips": ["Put the container in the fridge for about two hours to let everything marinate and cool off."]
    },

    "Lebanese Rice Pilaf": {
        "tips": [
            "Let everything relax for about 10 minutes before cooking.",
            "Make sure you turn the heat down to its lowest level and let the rice cook until it becomes fluffy. Make sure to not open the pot while the rice is cooking (we need the pressure to build up inside the pot).",
            "Add some almonds to the oil mix and fry them until they are nice and toasted. You will eventually notice a nice fragrance from the cooked almonds.",
            "Overall the almond frying process should take about 5 minutes."
        ]
    },

    "Labneh": {
        "tips": [
            "Allow everything to drain for at least twenty four hours ideally.",
            "Make sure to put a lid on this container and keep it in the fridge."
        ]
    },

    "Fattoosh": {
        "tips": ["Chill the salad in the fridge."]
    },

    # === BATCH 4951-5063 (Burrito cookbook) ===

    "Chipotle Mexican Steak and Cilantro Lime Rice Burritos": {
        "tips": ["Work the steaks to absorb the marinade before placing them in the fridge for half an hour."]
    },

    "Carnitas Burritos with Poblano-Corn Salsa": {
        "tips": [
            "On a grill roast the poblano pepper until it is charred, then place it in a large bowl and using plastic seal it. Do not disturb it for 15 minutes.",
            "You can serve with pico de gallo or ranch dressing and barbecue sauce."
        ]
    },

    "Crispy Black Bean Quinoa Burrito": {
        "tips": [
            "The crispy black bean quinoa burrito is one of my favorite burritos, I take it as my lunch or even as my supper.",
            "It is very easy to prepare and if you want to have a burrito for lunch or supper, I would recommend this.",
            "Serve with creamy avocado yogurt dip."
        ]
    },

    "Slow Cooker Pork Burrito": {
        "tips": [
            "There are many types of burritos you can make from pork; this is one of my favorites.",
            "It is also very easy to prepare and I am sure everybody in the family will appreciate it.",
            "You can heat the tortillas using the microwave or a pan.",
            "You can serve as it is or add a little amount of cheese on top and place it in a broiler for 5 seconds."
        ]
    },

    "Crispy Beef Burrito with Poblano Queso": {
        "tips": ["Everybody in the family is sure to love this - seasoned beef with black beans and poblano pepper, cheese and corn all under a delicious tortilla."]
    },

    "Sweet Potato Burrito Smothered in Avocado Salsa Verde": {
        "tips": [
            "Sounds very complicated, well it's not - very easy to prepare and the ingredients are easily available.",
            "Toppings to use: 1 1/2 cups chopped romaine lettuce, 1 small red onion finely chopped, finely chopped jalapeño (optional), sour cream (optional)."
        ]
    },

    "Over-Stuffed Frito Burrito": {
        "tips": [
            "It is one of the tastiest burritos ever.",
            "You can serve with pico de gallo or ranch dressing and barbecue sauce."
        ]
    },

    "Chipotle Shrimp Burrito with Simple Avocado Cream": {
        "tips": [
            "Put the shrimp in a gallon freezer pouch, together with the mixture. Marinate it and place the bag in the fridge for 2 hours.",
            "Place this mixture in the fridge for 40 minutes."
        ]
    },

    "Black Bean and Butternut Squash Burrito": {
        "tips": [
            "You can use the stove or microwave for heating garlic.",
            "You are allowed to use water but only in small amounts.",
            "Toppings of choice: avocado, salsa, vegan sour cream, spinach/lettuce, cilantro, etc."
        ]
    },

    "Chicken Burrito with Poblano Sauce": {
        "tips": [
            "The sour cream-poblano sauce is spicy and cool at the same time and it's a genius sauce since it reheats perfectly for leftovers.",
            "These burritos reheat like champs.",
            "You can bake all of them then reheat leftovers quickly in the microwave and throw them in the oven to crisp up the tortillas.",
            "Prepare the poblanos directly over fire. Turn them after a few minutes making sure they cook evenly on both sides, use tongs for this. When you are done, place them in a bowl and cover it with plastic.",
            "The recipe yields 4-5 large burritos."
        ]
    },

    "Simple Kale and Black Bean Burrito": {
        "tips": [
            "You can use the stove or microwave for warming beans.",
            "You can also use a small saucepan but this depends on the number of burritos you want to make."
        ]
    },

    "Burrito De La Calle": {
        "tips": ["2 steaks of your choice (I like New York strips)."]
    },

    "Kale and Feta Burrito": {
        "tips": ["You may think that making a burrito from vegetables is hard. Well I'm not only here to tell you that it's easy but I will also show you how."]
    },
}


def find_recipe_by_title(recipes, title):
    """Find a recipe by title (case-insensitive, partial match)."""
    title_lower = title.lower()
    for recipe in recipes:
        recipe_title = recipe.get('title', '').lower()
        # Exact match
        if recipe_title == title_lower:
            return recipe
        # Partial match
        if title_lower in recipe_title or recipe_title in title_lower:
            return recipe
    return None


def update_recipe_with_tips(recipe, updates):
    """Update a recipe with recovered tips."""
    modified = False

    if 'tips' in updates:
        existing_notes = recipe.get('notes', [])
        for tip in updates['tips']:
            # Check if tip already exists (avoid duplicates)
            tip_exists = any(tip.lower() in note.lower() or note.lower() in tip.lower()
                           for note in existing_notes if note)
            if not tip_exists:
                existing_notes.append(tip)
                modified = True
        recipe['notes'] = existing_notes

    return modified


def main():
    print("Loading recipes_master.json...")
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    print(f"Found {len(recipes)} recipes")

    updated_count = 0
    not_found = []

    for title, updates in IMG_RECOVERED_TIPS.items():
        recipe = find_recipe_by_title(recipes, title)
        if recipe:
            if update_recipe_with_tips(recipe, updates):
                updated_count += 1
                print(f"  ✓ Updated: {recipe['title']}")
        else:
            not_found.append(title)

    # Update metadata
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    # Write back
    print(f"\nWriting {updated_count} updates to recipes_master.json...")
    with open(RECIPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Updated {updated_count} recipes with recovered IMG tips")

    if not_found:
        print(f"\n⚠ Could not find {len(not_found)} recipes (may need to be added):")
        for title in not_found:
            print(f"  - {title}")

    return updated_count, not_found


if __name__ == '__main__':
    main()
