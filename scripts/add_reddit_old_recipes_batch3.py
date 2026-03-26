#!/usr/bin/env python3
"""Add more viral recipes from Reddit r/Old_Recipes to the database (batch 3)."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "reddit-armenian-perok-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Armenian Perok Cake",
        "category": "desserts",
        "attribution": "u/flyGERTIfly (Ninette), Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Named one of Reddit's top 5 most-discussed recipes of 2020. Recipe from Armenian diasporans in Tabriz, Iran, passed down through generations.",
        "description": "A buttery cake topped with apricot jam and a lattice crust. Like a cross between a cake and a pie. Originally posted during COVID-19 quarantine and quickly went viral.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "50 min",
        "total_time": "1 hour 10 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened (250g)"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "whole egg", "quantity": "1", "unit": "large"},
            {"item": "egg yolks", "quantity": "2", "unit": "large", "prep_note": "reserve whites for glaze"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "sour cream", "quantity": "1", "unit": "cup", "prep_note": "or Greek yogurt"},
            {"item": "all-purpose flour", "quantity": "3", "unit": "cup", "prep_note": "sifted, plus extra for lattice"},
            {"item": "baking powder", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "apricot jam", "quantity": "1", "unit": "cup", "prep_note": "or any jam of choice"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9-inch square or round baking dish."},
            {"step": 2, "text": "In a large bowl, cream together softened butter and sugar until light and fluffy."},
            {"step": 3, "text": "Add whole egg, egg yolks, vanilla, and sour cream. Mix until well combined."},
            {"step": 4, "text": "Gently fold in sifted flour, baking powder, and salt. Batter will be thick, almost like cookie dough."},
            {"step": 5, "text": "Set aside about 1/4 of the batter. Mix this portion with additional flour (2-3 tablespoons) until firm enough to roll."},
            {"step": 6, "text": "Press remaining batter evenly into prepared pan."},
            {"step": 7, "text": "Spread jam evenly over the batter."},
            {"step": 8, "text": "Roll out reserved dough and cut into strips. Arrange in a lattice pattern over the jam."},
            {"step": 9, "text": "Brush lattice with reserved egg whites for a glossy finish."},
            {"step": 10, "text": "Bake for about 50 minutes until top is golden and a knife inserted comes out clean."},
            {"step": 11, "text": "Cool before slicing. Serve with tea or coffee."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Named one of Reddit's top 5 most-discussed recipes of 2020",
            "Traditional apricot jam is used, but other flavors work well",
            "The batter is intentionally thick - more like cookie dough than cake batter",
            "Originated from Armenian diasporans in Tabriz, Iran",
            "Also known as Piróg in some Armenian families"
        ],
        "tags": ["cake", "armenian", "jam", "lattice", "vintage", "reddit", "viral", "COVID baking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-crown-o-gold-meatloaf",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crown o' Gold Meatloaf (1959)",
        "category": "mains",
        "attribution": "French's Mustard (1959) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Originally from a 1959 French's Mustard advertisement. The mustard meringue topping is the star of this retro dish.",
        "description": "A 1950s meatloaf baked in a round casserole and crowned with a savory mustard meringue topping that looks like mashed potatoes but tastes like a tangy, fluffy cloud.",
        "servings_yield": "6 servings",
        "prep_time": "20 min",
        "cook_time": "55 min",
        "total_time": "1 hour 15 min",
        "ingredients": [
            {"item": "ground lean beef", "quantity": "1 1/2", "unit": "lb"},
            {"item": "fine soft bread crumbs", "quantity": "1 1/2", "unit": "cup"},
            {"item": "ketchup", "quantity": "1/3", "unit": "cup"},
            {"item": "egg yolks", "quantity": "4", "unit": "large", "prep_note": "reserve whites for topping"},
            {"item": "yellow mustard", "quantity": "2", "unit": "tbsp", "prep_note": "for meatloaf"},
            {"item": "green bell pepper", "quantity": "3", "unit": "tbsp", "prep_note": "finely diced"},
            {"item": "minced onion", "quantity": "2", "unit": "tbsp"},
            {"item": "prepared horseradish", "quantity": "1 1/2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "egg whites", "quantity": "4", "unit": "large", "prep_note": "for meringue topping"},
            {"item": "cream of tartar", "quantity": "1/4", "unit": "tsp", "prep_note": "for meringue"},
            {"item": "yellow mustard", "quantity": "4", "unit": "tbsp", "prep_note": "for meringue topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F."},
            {"step": 2, "text": "Mix bread crumbs with ground beef in a large bowl."},
            {"step": 3, "text": "In a separate bowl, combine ketchup, egg yolks, 2 tbsp mustard, bell pepper, onion, horseradish, and salt."},
            {"step": 4, "text": "Mix wet ingredients into meat mixture until well combined."},
            {"step": 5, "text": "Pack mixture into a 9-inch round casserole dish."},
            {"step": 6, "text": "Bake at 325°F for 30 minutes."},
            {"step": 7, "text": "While meatloaf bakes, make the meringue: Beat egg whites until foamy."},
            {"step": 8, "text": "Add cream of tartar and beat until very stiff peaks form."},
            {"step": 9, "text": "Gently fold in 4 tablespoons mustard."},
            {"step": 10, "text": "Remove meatloaf from oven and swirl meringue over the top."},
            {"step": 11, "text": "Return to oven and bake 20-25 minutes more until meringue is golden brown."},
            {"step": 12, "text": "Let rest 5 minutes before slicing and serving."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "The mustard meringue is light and airy with a mellow mustard tang",
            "Best eaten with bites of both meatloaf and meringue together",
            "Reminiscent of a ketchup-and-mustard burger in flavor",
            "One Redditor described the meringue as 'the savory equivalent of Jell-O'",
            "Originally from a 1959 French's Mustard advertisement"
        ],
        "tags": ["meatloaf", "retro", "1950s", "mustard", "meringue", "reddit", "viral", "French's"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-16th-century-vindaloo",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "16th Century Vindaloo",
        "category": "mains",
        "attribution": "Chef Bhakti Sharma / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. Traditional Indo-Portuguese recipe. The name 'vindaloo' comes from Portuguese 'vinho de alhos' (meat with wine and garlic). No potatoes in authentic versions.",
        "description": "A traditional vindaloo made the way Portuguese explorers brought it to India in the 15th century. Rich with dry-roasted spices and a tangy wine vinegar marinade. No potatoes - that's a British addition.",
        "servings_yield": "4-6 servings",
        "prep_time": "30 min (plus 3 hours marinating)",
        "cook_time": "45 min",
        "total_time": "4 hours 15 min",
        "ingredients": [
            {"item": "chicken thighs", "quantity": "2", "unit": "lb", "prep_note": "cubed (or pork)"},
            {"item": "cumin seeds", "quantity": "1", "unit": "tbsp"},
            {"item": "coriander seeds", "quantity": "1", "unit": "tbsp"},
            {"item": "black peppercorns", "quantity": "1", "unit": "tsp"},
            {"item": "whole cloves", "quantity": "6", "unit": ""},
            {"item": "cinnamon stick", "quantity": "1", "unit": "small"},
            {"item": "dried red chilies", "quantity": "4-6", "unit": "", "prep_note": "adjust to taste"},
            {"item": "garlic cloves", "quantity": "8", "unit": "", "prep_note": "minced"},
            {"item": "fresh ginger", "quantity": "2", "unit": "inch", "prep_note": "minced"},
            {"item": "red wine vinegar", "quantity": "1/2", "unit": "cup"},
            {"item": "brown sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "vegetable oil", "quantity": "3", "unit": "tbsp"},
            {"item": "onion", "quantity": "1", "unit": "large", "prep_note": "thinly sliced"},
            {"item": "tomato paste", "quantity": "2", "unit": "tbsp"},
            {"item": "water or chicken broth", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Dry-roast cumin seeds, coriander seeds, peppercorns, cloves, cinnamon, and dried chilies in a pan over medium heat until fragrant, about 2-3 minutes. Let cool."},
            {"step": 2, "text": "Grind roasted spices in a food processor or spice grinder."},
            {"step": 3, "text": "Add garlic, ginger, wine vinegar, and brown sugar to the spice mixture. Blend into a paste."},
            {"step": 4, "text": "Coat chicken pieces thoroughly with the spice paste. Cover and refrigerate for at least 3 hours, preferably overnight."},
            {"step": 5, "text": "Heat oil in a large heavy pot over medium-high heat. Add sliced onion and cook until golden brown, about 10 minutes."},
            {"step": 6, "text": "Add marinated chicken with all the marinade. Cook for 5 minutes, stirring occasionally."},
            {"step": 7, "text": "Stir in tomato paste and water/broth. Bring to a simmer."},
            {"step": 8, "text": "Reduce heat to low, cover, and simmer for 35-40 minutes until chicken is tender and sauce has thickened."},
            {"step": 9, "text": "Adjust seasoning with salt. Serve with rice or naan."}
        ],
        "temperature": "Medium-high to low simmer",
        "notes": [
            "There are NO potatoes in traditional vindaloo - 'aloo' doesn't mean potato here",
            "The name comes from Portuguese 'vinho de alhos' (wine and garlic)",
            "Portuguese explorers brought this dish to India in the 15th century",
            "The tartness of wine vinegar is essential - don't substitute",
            "Can use pork instead of chicken for a more traditional version"
        ],
        "tags": ["curry", "vindaloo", "indian", "portuguese", "historical", "reddit", "spicy", "16th century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-potato-cheese-casserole",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grandma's Potato Cheese Casserole",
        "category": "sides",
        "attribution": "Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A classic comfort food casserole that appears frequently on the subreddit. Simple ingredients, maximum comfort.",
        "description": "A creamy, cheesy potato casserole with layers of sliced potatoes, cheese, and cream of chicken soup. Simple enough for weeknights, special enough for holidays.",
        "servings_yield": "8 servings",
        "prep_time": "20 min",
        "cook_time": "1 hour",
        "total_time": "1 hour 20 min",
        "ingredients": [
            {"item": "russet potatoes", "quantity": "2", "unit": "lb", "prep_note": "peeled and thinly sliced"},
            {"item": "shredded cheddar cheese", "quantity": "2", "unit": "cup"},
            {"item": "cream of chicken soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "sliced"},
            {"item": "onion", "quantity": "1", "unit": "medium", "prep_note": "thinly sliced"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "black pepper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch casserole dish."},
            {"step": 2, "text": "Layer half the sliced potatoes in the bottom of the prepared dish."},
            {"step": 3, "text": "Spread half the cream of chicken soup over the potatoes."},
            {"step": 4, "text": "Sprinkle with half the cheese."},
            {"step": 5, "text": "Dot with half the butter slices."},
            {"step": 6, "text": "Season with salt and pepper."},
            {"step": 7, "text": "Layer half the onion slices on top."},
            {"step": 8, "text": "Repeat all layers with remaining ingredients."},
            {"step": 9, "text": "Cover with foil and bake for 45 minutes."},
            {"step": 10, "text": "Remove foil and bake 15 minutes more until potatoes are tender and top is golden."},
            {"step": 11, "text": "Let rest 5 minutes before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Can substitute cream of mushroom soup if preferred",
            "Add cooked bacon bits for extra flavor",
            "Use a mandoline for evenly sliced potatoes",
            "Can be assembled ahead and refrigerated overnight before baking"
        ],
        "tags": ["casserole", "potatoes", "cheese", "comfort food", "vintage", "reddit", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]

def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}

    # Add new recipes
    added = 0
    skipped = 0
    for recipe in new_recipes:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            skipped += 1
            print(f"Skipped (exists): {recipe['title']}")

    # Update metadata
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = str(date.today())

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone! Added {added} recipes, skipped {skipped}")
    print(f"Total recipes: {data['meta']['total_count']}")

if __name__ == "__main__":
    main()
