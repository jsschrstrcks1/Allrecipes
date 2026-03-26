#!/usr/bin/env python3
"""Add more cheese recipes and vintage casseroles to the database (batch 6)."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-gruyere",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gruyère Cheese",
        "category": "sides",
        "attribution": "New England Cheesemaking Supply Co.",
        "source_note": "cheesemaking.com - Classic Swiss mountain cheese with small or no holes, aged 8-14 months.",
        "description": "The classic 'mountain cheese' of France and Switzerland. Made from full fat milk with a high temperature scald for proper aging. Sweet, slightly salty, becoming earthier and more complex with age.",
        "servings_yield": "About 2 lbs from 2 gallons milk",
        "prep_time": "4 hours",
        "cook_time": "N/A",
        "total_time": "8-14 months (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallon", "prep_note": "preferably raw"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "propionic shermanii", "quantity": "1/8", "unit": "tsp", "prep_note": "for eye development"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "", "unit": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add thermophilic culture and propionic shermanii. Ripen for 10 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add diluted rennet and stir gently."},
            {"step": 3, "text": "Let set for 30-45 minutes until clean break forms."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 120°F over 30-40 minutes, stirring gently."},
            {"step": 6, "text": "Hold at 120°F for 30 minutes, stirring occasionally."},
            {"step": 7, "text": "Drain curds and press into mold at increasing pressure over 6-8 hours."},
            {"step": 8, "text": "Brine in saturated salt solution for 12 hours per pound."},
            {"step": 9, "text": "Age at 54-58°F with 85-87% humidity. Wash rind with light brine 2-3 times weekly."},
            {"step": 10, "text": "Age for minimum 8 months, up to 14 months for more complex flavor."}
        ],
        "temperature": "90°F initial, 120°F cooking, 54-58°F aging",
        "notes": [
            "Differentiated from Emmentaler by smaller or no holes",
            "High temperature scald is essential for proper aging",
            "Wipe any surface mold with saturated brine solution",
            "Flavor becomes earthier and more complex with longer aging",
            "Traditional Swiss/French alpine cheese"
        ],
        "tags": ["cheese", "homemade", "gruyere", "swiss", "alpine", "aged", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-emmental-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Emmental (Swiss) Cheese",
        "category": "sides",
        "attribution": "New England Cheesemaking Supply Co.",
        "source_note": "cheesemaking.com - The original Swiss cheese with characteristic 'eyes' from CO2 bubbles.",
        "description": "The famous hole-filled Swiss cheese from the Emmental region of Bern. Propionic bacteria consume lactic acid and release CO2, forming the characteristic 'eyes.' Nutty, slightly sweet flavor.",
        "servings_yield": "About 2 lbs from 2 gallons milk",
        "prep_time": "4 hours",
        "cook_time": "N/A",
        "total_time": "3-4 months (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallon", "prep_note": "preferably raw"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "propionic shermanii powder", "quantity": "1", "unit": "tsp", "prep_note": "dissolved in 1/4 cup warm milk"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "", "unit": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add thermophilic culture and propionic shermanii. Ripen for 10 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add diluted rennet and stir."},
            {"step": 3, "text": "Let set for 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces using vertical and horizontal cuts."},
            {"step": 5, "text": "Slowly raise temperature to 120°F over 40 minutes while stirring."},
            {"step": 6, "text": "Hold at 120°F for 30-45 minutes until curds are firm."},
            {"step": 7, "text": "Drain and press curds at increasing pressure for 6-8 hours."},
            {"step": 8, "text": "Brine for 12 hours per pound of cheese."},
            {"step": 9, "text": "Age at 50-55°F for 2-3 weeks, then move to 'warm room' at 68-72°F for 2-3 weeks for eye development."},
            {"step": 10, "text": "Return to cool aging (50°F) for another 2-3 months minimum."}
        ],
        "temperature": "90°F initial, 120°F cooking, variable aging",
        "notes": [
            "The 'warm room' phase is essential for eye (hole) development",
            "Longer aging = larger holes and more complex flavor",
            "Propionic bacteria create CO2 bubbles that form the eyes",
            "Baby Swiss is a smaller, milder, richer version",
            "Alfred Guggisberg developed Baby Swiss in Pennsylvania in the 1960s"
        ],
        "tags": ["cheese", "homemade", "swiss", "emmental", "eyes", "aged", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gouda Cheese",
        "category": "sides",
        "attribution": "New England Cheesemaking Supply Co.",
        "source_note": "cheesemaking.com - Dutch washed-curd cheese, mild when young, caramel-sweet when aged.",
        "description": "A remarkable Dutch cheese that transforms with age. Young Gouda is mild and creamy; aged Gouda develops deep golden color, caramel sweetness, and crunchy protein crystals. The 'washing' step creates its natural sweetness.",
        "servings_yield": "About 2 lbs from 2 gallons milk",
        "prep_time": "3 hours",
        "cook_time": "N/A",
        "total_time": "2 months to 2 years (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "", "unit": "for brine"},
            {"item": "cheese wax", "quantity": "", "unit": "for coating", "prep_note": "red or yellow traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add mesophilic culture and ripen for 10 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add diluted rennet."},
            {"step": 3, "text": "Let set for 45 minutes until firm clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Remove 1/3 of whey. Replace with same amount of 175°F water (the 'washing' step)."},
            {"step": 6, "text": "Raise temperature to 100°F over 30 minutes while stirring."},
            {"step": 7, "text": "Hold at 100°F for 30 minutes, stirring occasionally."},
            {"step": 8, "text": "Drain and press curds at increasing pressure for 6 hours."},
            {"step": 9, "text": "Brine for 3 hours per pound."},
            {"step": 10, "text": "Air dry for 1-3 days until rind forms. Wax the cheese."},
            {"step": 11, "text": "Age at 50-55°F. Young: 2 months. Aged: 6-12 months. Extra-aged: 2+ years."}
        ],
        "temperature": "86°F initial, 100°F cooking, 50-55°F aging",
        "notes": [
            "The 'washing' step (replacing whey with hot water) creates Gouda's sweetness",
            "Washing lowers milk sugar, reducing acid and producing mild, sweet cheese",
            "Young Gouda (2 months) is soft and buttery",
            "Aged Gouda (1+ year) develops caramel notes and crunchy crystals",
            "Traditional wax colors: red for young, black for aged"
        ],
        "tags": ["cheese", "homemade", "gouda", "dutch", "washed curd", "waxed", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-havarti",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Havarti Cheese",
        "category": "sides",
        "attribution": "New England Cheesemaking Supply Co.",
        "source_note": "cheesemaking.com - Creamy Danish cheese created by Hanne Nielsen in the 1850s.",
        "description": "A smooth, buttery Danish cheese with small irregular holes. Created in the 1850s by Hanne Nielsen after traveling Europe to learn cheesemaking. Perfect for melting, grilling, or eating fresh.",
        "servings_yield": "About 2 lbs from 2 gallons milk",
        "prep_time": "2.5 hours",
        "cook_time": "N/A",
        "total_time": "About 2 months (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "4", "unit": "gallon"},
            {"item": "mesophilic starter culture (C101)", "quantity": "1", "unit": "packet"},
            {"item": "calcium chloride", "quantity": "1", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "", "unit": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F in water bath or on stovetop."},
            {"step": 2, "text": "Add C101 mesophilic culture and ripen for 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk. Add diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Let curds rest 10 minutes, then stir gently for 10 minutes."},
            {"step": 7, "text": "Slowly raise temperature to 100°F over 30 minutes."},
            {"step": 8, "text": "Hold at 100°F for 15 minutes while stirring."},
            {"step": 9, "text": "Drain curds and press at light pressure for 30 minutes, then medium for 4-5 hours."},
            {"step": 10, "text": "Brine for 6 hours."},
            {"step": 11, "text": "Age at 50-55°F with high humidity for 2 months. Turn daily for first week."}
        ],
        "temperature": "86°F initial, 100°F cooking, 50-55°F aging",
        "notes": [
            "Created by Hanne Nielsen at her farm in the 1850s",
            "She traveled Europe learning cheesemaking techniques",
            "Named after her farm where it was first created",
            "Traditionally has open 'eyes' in its formation",
            "Excellent for grilling and melting"
        ],
        "tags": ["cheese", "homemade", "havarti", "danish", "semi-soft", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-provolone",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Provolone Cheese",
        "category": "sides",
        "attribution": "New England Cheesemaking Supply Co.",
        "source_note": "cheesemaking.com - Italian stretched-curd (pasta filata) cheese, the 'older brother' of Mozzarella.",
        "description": "An Italian stretched-curd cheese with less moisture than Mozzarella, giving it longer shelf life and richer flavor. Can be mild and sweet (Dolce) or sharp and pungent (Piccante) depending on aging.",
        "servings_yield": "About 2 lbs from 2 gallons milk",
        "prep_time": "3 hours",
        "cook_time": "N/A",
        "total_time": "2-12 months (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallon"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/4", "unit": "tsp", "prep_note": "dissolved in 1/4 cup water, for sharp flavor"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "", "unit": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F. Add thermophilic culture and lipase. Ripen for 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add diluted rennet."},
            {"step": 3, "text": "Let set for 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 118°F over 30 minutes while stirring gently."},
            {"step": 6, "text": "Hold at 118°F for 30 minutes until curds are firm and springy."},
            {"step": 7, "text": "Drain curds and let mat at 100°F until pH reaches 5.2-5.3 (about 2-3 hours)."},
            {"step": 8, "text": "Cut curd into strips. Stretch in 170-180°F water until smooth and glossy."},
            {"step": 9, "text": "Form into pear or cylinder shape. Tie with string for hanging."},
            {"step": 10, "text": "Brine for 6-8 hours. Hang to dry for 1-2 days."},
            {"step": 11, "text": "Age hanging at 55-60°F. Dolce: 2-3 months. Piccante: 6-12 months."}
        ],
        "temperature": "97°F initial, 118°F cooking, 170-180°F stretching",
        "notes": [
            "Pasta filata (stretched curd) technique same as Mozzarella",
            "Contains about 45% moisture vs Mozzarella's 52-60%",
            "Lower moisture = longer shelf life, firmer texture, richer flavor",
            "Lipase adds the characteristic sharp/piquant flavor",
            "Traditionally tied with rope and hung for aging"
        ],
        "tags": ["cheese", "homemade", "provolone", "italian", "pasta filata", "stretched curd", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-green-bean-casserole",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Classic Green Bean Casserole",
        "category": "sides",
        "attribution": "Campbell's / Dorcas Reilly (1955) / Reddit r/Old_Recipes",
        "source_note": "Created by Dorcas Reilly at Campbell's Soup Company in 1955. The original recipe card is now in the Smithsonian's National Museum of American History.",
        "description": "The iconic Thanksgiving side dish created in 1955. Green beans in creamy mushroom sauce topped with crispy fried onions. So beloved the original recipe is in the Smithsonian.",
        "servings_yield": "6 servings",
        "prep_time": "10 min",
        "cook_time": "30 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "cream of mushroom soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "soy sauce", "quantity": "1", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/8", "unit": "tsp"},
            {"item": "green beans", "quantity": "4", "unit": "cups", "prep_note": "cooked and drained, or 2 cans (14.5 oz each)"},
            {"item": "French's fried onions", "quantity": "1 1/3", "unit": "cup", "prep_note": "divided"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "In a 1.5-quart casserole dish, mix soup, milk, soy sauce, and pepper."},
            {"step": 3, "text": "Stir in green beans and 2/3 cup of the fried onions."},
            {"step": 4, "text": "Bake for 25 minutes until hot and bubbling."},
            {"step": 5, "text": "Stir the casserole."},
            {"step": 6, "text": "Top with remaining fried onions."},
            {"step": 7, "text": "Bake 5 minutes more until onions are golden brown."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Created by Dorcas Reilly at Campbell's in 1955",
            "Original recipe card is in the Smithsonian",
            "Over 40 million households serve it each Thanksgiving",
            "The soy sauce is the 'secret ingredient' many people skip",
            "Fresh green beans can be blanched and used instead of canned"
        ],
        "tags": ["casserole", "green beans", "thanksgiving", "holiday", "campbell's", "vintage", "1950s", "reddit"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-tuna-noodle-casserole",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Classic Tuna Noodle Casserole",
        "category": "mains",
        "attribution": "Campbell's (1940s) / Reddit r/Old_Recipes",
        "source_note": "A Campbell's creation from the 1940s that became a weeknight staple. The epitome of mid-century American comfort food.",
        "description": "The quintessential 1950s weeknight dinner. Egg noodles, tuna, peas, and cream of mushroom soup topped with crushed potato chips or breadcrumbs. Economical, comforting, and nostalgic.",
        "servings_yield": "6 servings",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "45 min",
        "ingredients": [
            {"item": "egg noodles", "quantity": "8", "unit": "oz", "prep_note": "cooked and drained"},
            {"item": "tuna", "quantity": "2", "unit": "cans", "prep_note": "5 oz each, drained and flaked"},
            {"item": "cream of mushroom soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "frozen peas", "quantity": "1", "unit": "cup"},
            {"item": "shredded cheddar cheese", "quantity": "1", "unit": "cup", "prep_note": "divided"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "potato chips or breadcrumbs", "quantity": "1", "unit": "cup", "prep_note": "crushed, for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F. Grease a 2-quart casserole dish."},
            {"step": 2, "text": "In a large bowl, mix cream of mushroom soup and milk until smooth."},
            {"step": 3, "text": "Add cooked noodles, tuna, peas, half the cheese, salt, and pepper. Stir to combine."},
            {"step": 4, "text": "Pour mixture into prepared casserole dish."},
            {"step": 5, "text": "Top with remaining cheese and crushed potato chips or breadcrumbs."},
            {"step": 6, "text": "Bake uncovered for 25-30 minutes until bubbly and golden on top."},
            {"step": 7, "text": "Let rest 5 minutes before serving."}
        ],
        "temperature": "375°F (190°C)",
        "notes": [
            "Crushed potato chips give authentic retro flavor and crunch",
            "Can substitute cream of celery soup for variety",
            "Add diced celery or onion for extra texture",
            "A staple of 1950s-60s American home cooking",
            "Economical protein source during and after WWII"
        ],
        "tags": ["casserole", "tuna", "noodles", "weeknight", "1950s", "vintage", "reddit", "comfort food"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-king-ranch-chicken",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "King Ranch Chicken Casserole",
        "category": "mains",
        "attribution": "Texas (1950s) / Reddit r/Old_Recipes",
        "source_note": "Named after the famous King Ranch in South Texas. Origin disputed but became a Texas potluck staple in the 1950s-60s.",
        "description": "A Tex-Mex layered casserole named after the legendary King Ranch. Layers of corn tortillas, chicken, and creamy chile-spiked sauce. A Texas potluck and church supper essential.",
        "servings_yield": "8-10 servings",
        "prep_time": "30 min",
        "cook_time": "45 min",
        "total_time": "1 hour 15 min",
        "ingredients": [
            {"item": "cooked chicken", "quantity": "4", "unit": "cups", "prep_note": "shredded (from 1 rotisserie chicken)"},
            {"item": "cream of mushroom soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "cream of chicken soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "Ro-Tel tomatoes with green chiles", "quantity": "1", "unit": "can", "prep_note": "10 oz, undrained"},
            {"item": "sour cream", "quantity": "1", "unit": "cup"},
            {"item": "onion", "quantity": "1", "unit": "medium", "prep_note": "diced"},
            {"item": "green bell pepper", "quantity": "1", "unit": "medium", "prep_note": "diced"},
            {"item": "garlic powder", "quantity": "1", "unit": "tsp"},
            {"item": "chili powder", "quantity": "1", "unit": "tsp"},
            {"item": "cumin", "quantity": "1/2", "unit": "tsp"},
            {"item": "corn tortillas", "quantity": "12", "unit": "", "prep_note": "cut into quarters"},
            {"item": "shredded cheddar cheese", "quantity": "2", "unit": "cups", "prep_note": "divided"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch baking dish."},
            {"step": 2, "text": "Sauté onion and bell pepper until softened, about 5 minutes."},
            {"step": 3, "text": "In a large bowl, mix both soups, Ro-Tel tomatoes, sour cream, garlic powder, chili powder, and cumin."},
            {"step": 4, "text": "Stir in sautéed vegetables and shredded chicken."},
            {"step": 5, "text": "Layer 1/3 of tortilla pieces in bottom of prepared dish."},
            {"step": 6, "text": "Spread 1/3 of chicken mixture over tortillas. Sprinkle with 1/3 of cheese."},
            {"step": 7, "text": "Repeat layers twice more, ending with cheese on top."},
            {"step": 8, "text": "Cover with foil and bake 30 minutes."},
            {"step": 9, "text": "Remove foil and bake 15 minutes more until bubbly and cheese is melted."},
            {"step": 10, "text": "Let rest 10 minutes before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Named after the famous King Ranch in South Texas",
            "Some say it originated at the ranch; others dispute this",
            "Ro-Tel tomatoes are essential for authentic flavor",
            "Can be assembled ahead and refrigerated before baking",
            "A Texas potluck and church supper staple since the 1950s"
        ],
        "tags": ["casserole", "chicken", "tex-mex", "texas", "tortilla", "vintage", "reddit", "potluck"],
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
