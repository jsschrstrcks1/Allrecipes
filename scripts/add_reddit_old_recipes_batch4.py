#!/usr/bin/env python3
"""Add more viral recipes from Reddit r/Old_Recipes to the database (batch 4)."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "reddit-4-generation-banana-bread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "4-Generation Banana Bread",
        "category": "breads",
        "attribution": "Skycrest Baptist Church Cookbook (1920s) / u/daviddwatsonn, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Originally from a 1920s church cookbook in Clearwater, Florida. Has been in the Watson family for 4 generations.",
        "description": "A hand-written recipe that's been passed down through four generations. Simple ingredients but perfectly moist and flavorful with walnuts. 'Every single time someone made it, they loved it.'",
        "servings_yield": "1 loaf (10 slices)",
        "prep_time": "15 min",
        "cook_time": "60 min",
        "total_time": "1 hour 15 min",
        "ingredients": [
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "1 stick, salted, room temperature"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "ripe bananas", "quantity": "3", "unit": "medium", "prep_note": "mashed"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "walnuts", "quantity": "1/2", "unit": "cup", "prep_note": "chopped, tossed with 1 tbsp flour"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x5-inch loaf pan."},
            {"step": 2, "text": "Cream together room-temperature butter and sugar until light and fluffy. Mix thoroughly."},
            {"step": 3, "text": "Beat in eggs one at a time, mixing well after each addition."},
            {"step": 4, "text": "Add mashed bananas and vanilla, mixing until combined."},
            {"step": 5, "text": "In a separate bowl, whisk together flour, baking soda, and salt."},
            {"step": 6, "text": "Add dry ingredients to wet, mixing until just combined."},
            {"step": 7, "text": "Toss chopped walnuts with 1 tablespoon flour (prevents sinking), then fold into batter."},
            {"step": 8, "text": "Pour batter into prepared pan."},
            {"step": 9, "text": "Bake for 60 minutes or until a toothpick inserted in center comes out clean."},
            {"step": 10, "text": "Cool in pan for 10 minutes, then turn out onto wire rack."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Use room temperature butter - not cold, not melted",
            "Mix thoroughly after adding each ingredient",
            "Toss walnuts in flour before adding to prevent them from sinking",
            "Originally from Skycrest Baptist Church cookbook in Clearwater, Florida (1920s)",
            "Watson family's great-great-grandmother first made this recipe"
        ],
        "tags": ["bread", "banana", "quick bread", "vintage", "reddit", "viral", "4 generations", "walnuts"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-wacky-cake-depression",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wacky Cake (Depression Cake)",
        "category": "desserts",
        "attribution": "WWII Era / u/BlackCatKitchen, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Also known as Crazy Cake, War Cake, or Depression Cake. Made without eggs, milk, or butter - created during WWII rationing.",
        "description": "A rich, moist chocolate cake made without eggs, milk, or butter. The vinegar and baking soda create leavening through a chemical reaction. Born from wartime rationing necessity.",
        "servings_yield": "9 servings",
        "prep_time": "10 min",
        "cook_time": "30 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "unsweetened cocoa powder", "quantity": "1/3", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "white vinegar", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "vegetable oil", "quantity": "1/3", "unit": "cup"},
            {"item": "water or cooled coffee", "quantity": "1", "unit": "cup", "prep_note": "coffee enhances chocolate flavor"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Do NOT grease the pan."},
            {"step": 2, "text": "Whisk together flour, sugar, cocoa powder, baking soda, and salt directly in an 8x8-inch baking pan."},
            {"step": 3, "text": "Make 3 wells in the dry ingredients."},
            {"step": 4, "text": "Pour oil into one well, vinegar into another, and vanilla into the third."},
            {"step": 5, "text": "Pour water (or cooled coffee) over everything."},
            {"step": 6, "text": "Whisk together until just combined and no dry spots remain. Do not overmix."},
            {"step": 7, "text": "Bake for 30 minutes or until a toothpick comes out clean."},
            {"step": 8, "text": "Cool in pan. Dust with powdered sugar or frost as desired."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "No eggs, no milk, no butter - perfect for allergies or wartime rationing",
            "The vinegar + baking soda creates leavening (like a science fair volcano)",
            "You won't taste the vinegar in the finished cake",
            "Mix and bake in the same pan - minimal cleanup",
            "Using coffee instead of water enhances the chocolate flavor",
            "Recipe dates back to 1930s-1940s wartime rationing",
            "Went viral on TikTok via B. Dylan Hollis"
        ],
        "tags": ["cake", "chocolate", "depression era", "WWII", "no eggs", "no dairy", "vintage", "reddit", "viral", "wacky cake"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-funeral-potatoes",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Funeral Potatoes (Church Lady Casserole)",
        "category": "sides",
        "attribution": "LDS Church Potluck Tradition / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Also called Hash Brown Casserole or Church Lady Casserole. A staple at LDS church functions and post-funeral receptions.",
        "description": "A creamy, cheesy potato casserole topped with crunchy corn flakes. Named for its frequent appearance at funeral receptions, though it's welcome at any potluck.",
        "servings_yield": "12 servings",
        "prep_time": "15 min",
        "cook_time": "1 hour",
        "total_time": "1 hour 15 min",
        "ingredients": [
            {"item": "frozen hash browns", "quantity": "2", "unit": "lb", "prep_note": "thawed, or frozen shredded potatoes"},
            {"item": "cream of chicken soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "sour cream", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted, divided"},
            {"item": "shredded cheddar cheese", "quantity": "2", "unit": "cup"},
            {"item": "onion", "quantity": "1/2", "unit": "cup", "prep_note": "finely diced, or 2 tbsp dried minced onion"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper", "quantity": "1/4", "unit": "tsp"},
            {"item": "corn flakes", "quantity": "2", "unit": "cup", "prep_note": "crushed"},
            {"item": "paprika", "quantity": "1/2", "unit": "tsp", "prep_note": "for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch baking dish with butter."},
            {"step": 2, "text": "In a large bowl, combine thawed hash browns, cream of chicken soup, sour cream, half the melted butter, cheese, onion, salt, and pepper."},
            {"step": 3, "text": "Mix well and spread evenly into prepared baking dish."},
            {"step": 4, "text": "In a small bowl, toss crushed corn flakes with remaining melted butter."},
            {"step": 5, "text": "Spread buttered corn flakes evenly over the potato mixture."},
            {"step": 6, "text": "Sprinkle with paprika."},
            {"step": 7, "text": "Bake uncovered for 1 hour until bubbly and golden brown on top."},
            {"step": 8, "text": "Let rest 5 minutes before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Named 'Funeral Potatoes' for their presence at LDS post-funeral receptions",
            "Can substitute crushed Ritz crackers or potato chips for corn flakes",
            "Add diced ham for a heartier version",
            "Can be assembled ahead and refrigerated overnight before baking",
            "Cream of mushroom soup works as a substitute"
        ],
        "tags": ["casserole", "potatoes", "cheese", "comfort food", "vintage", "reddit", "church", "potluck", "funeral potatoes"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-hot-milk-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hot Milk Cake",
        "category": "desserts",
        "attribution": "Vintage American / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A classic vanilla sponge cake that's a cross between pound cake and angel food. Many grandmothers' go-to cake for every occasion.",
        "description": "A simple vanilla cake with a tender, fine crumb - like a cross between pound cake and angel food cake. Not too heavy, not too light, but just right. Uses hot milk for extra tenderness.",
        "servings_yield": "12 servings",
        "prep_time": "15 min",
        "cook_time": "35-40 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "sugar", "quantity": "2", "unit": "cup"},
            {"item": "baking powder", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "vanilla extract", "quantity": "2", "unit": "tsp"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease and flour a 9x13-inch pan or two 9-inch round pans."},
            {"step": 2, "text": "Whisk together flour, baking powder, and salt in a bowl; set aside."},
            {"step": 3, "text": "In a large bowl, beat eggs and sugar together until thick and pale yellow, about 3-4 minutes."},
            {"step": 4, "text": "Beat in vanilla extract."},
            {"step": 5, "text": "Gradually add flour mixture, mixing on low until just combined."},
            {"step": 6, "text": "In a small saucepan, heat milk and butter together until butter melts and mixture is HOT (not boiling)."},
            {"step": 7, "text": "With mixer on low, slowly pour hot milk mixture into batter and mix until smooth."},
            {"step": 8, "text": "Pour batter into prepared pan(s)."},
            {"step": 9, "text": "Bake for 35-40 minutes until golden and a toothpick comes out clean."},
            {"step": 10, "text": "Cool in pan 10 minutes, then turn out onto rack. Frost with chocolate frosting if desired."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "The hot milk makes the cake extra tender",
            "Some families call this 'Boiled Milk Sponge Cake'",
            "Traditional chocolate frosting is the classic pairing",
            "Many grandmothers' go-to cake for every occasion",
            "Perfect for potlucks and family gatherings"
        ],
        "tags": ["cake", "vanilla", "sponge cake", "hot milk", "vintage", "reddit", "grandma"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-old-fashioned-chess-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Chess Pie",
        "category": "desserts",
        "attribution": "Southern American Traditional / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A classic Southern custard pie with origins in England. The cornmeal creates a signature crackly sugar crust on top.",
        "description": "A simple Southern custard pie with a gooey center and crackly sugar crust. The cornmeal rises to the surface during baking, creating that trademark golden top.",
        "servings_yield": "8 servings",
        "prep_time": "10 min",
        "cook_time": "45-50 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "unbaked 9-inch pie crust", "quantity": "1", "unit": ""},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "egg yolk", "quantity": "1", "unit": "large"},
            {"item": "yellow cornmeal", "quantity": "1", "unit": "tbsp"},
            {"item": "all-purpose flour", "quantity": "1", "unit": "tbsp"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"},
            {"item": "white vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F. Place pie crust in a 9-inch pie plate; crimp edges decoratively."},
            {"step": 2, "text": "In a large bowl, whisk together sugar and melted butter."},
            {"step": 3, "text": "Beat in eggs and egg yolk one at a time."},
            {"step": 4, "text": "Whisk in cornmeal, flour, milk, vinegar, vanilla, and salt until smooth."},
            {"step": 5, "text": "Pour filling into unbaked pie crust."},
            {"step": 6, "text": "Bake for 45-50 minutes until filling is set and top is golden brown with a crackly crust."},
            {"step": 7, "text": "The center should jiggle slightly when done - it will set as it cools."},
            {"step": 8, "text": "Cool completely before slicing. Serve at room temperature."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "The cornmeal rises to create the signature crackly top",
            "Vinegar cuts the sweetness and helps set the custard",
            "Don't overbake - center should still jiggle slightly",
            "Southern tradition with English origins",
            "Some say the name comes from 'jes pie' (it's just pie)"
        ],
        "tags": ["pie", "chess pie", "custard", "southern", "vintage", "reddit", "cornmeal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-old-fashioned-buttermilk-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Buttermilk Pie",
        "category": "desserts",
        "attribution": "Southern American Traditional / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A tangy Southern custard pie similar to chess pie but uses buttermilk and flour instead of cornmeal. Smoother, creamier texture.",
        "description": "A tangy, creamy Southern custard pie. Similar to chess pie but with buttermilk for tartness and flour for a smoother texture. Simple ingredients, extraordinary flavor.",
        "servings_yield": "8 servings",
        "prep_time": "10 min",
        "cook_time": "50-55 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "unbaked 9-inch pie crust", "quantity": "1", "unit": ""},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "all-purpose flour", "quantity": "3", "unit": "tbsp"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/4", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Place pie crust in a 9-inch pie plate."},
            {"step": 2, "text": "In a large bowl, whisk together sugar and melted butter until combined."},
            {"step": 3, "text": "Beat in eggs one at a time."},
            {"step": 4, "text": "Whisk in flour until smooth with no lumps."},
            {"step": 5, "text": "Stir in buttermilk, vanilla, salt, and nutmeg if using."},
            {"step": 6, "text": "Pour filling into pie crust."},
            {"step": 7, "text": "Bake for 50-55 minutes until top is golden and center is set but still has a slight jiggle."},
            {"step": 8, "text": "Cool completely before slicing - filling firms as it cools."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "No cornmeal - uses flour for smoother texture than chess pie",
            "Buttermilk provides distinctive tangy flavor",
            "The nutmeg is traditional but optional",
            "Best served at room temperature or slightly chilled",
            "Great use for leftover buttermilk"
        ],
        "tags": ["pie", "buttermilk", "custard", "southern", "vintage", "reddit"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-vinegar-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Vinegar Pie",
        "category": "desserts",
        "attribution": "Depression Era / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A Depression-era pie made when lemons were scarce or expensive. Vinegar provides the tartness instead of citrus.",
        "description": "A chess-style custard pie using vinegar for tartness when lemons weren't available. Don't let the name fool you - it tastes like a silky lemon pie without any lemon.",
        "servings_yield": "8 servings",
        "prep_time": "10 min",
        "cook_time": "45 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "unbaked 9-inch pie crust", "quantity": "1", "unit": ""},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "1/4", "unit": "cup", "prep_note": "melted"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "tbsp"},
            {"item": "white vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/8", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Place pie crust in a 9-inch pie plate."},
            {"step": 2, "text": "In a bowl, whisk together sugar, melted butter, and eggs until smooth."},
            {"step": 3, "text": "Whisk in flour until no lumps remain."},
            {"step": 4, "text": "Add vinegar, vanilla, water, and salt. Mix well."},
            {"step": 5, "text": "Pour filling into unbaked pie crust."},
            {"step": 6, "text": "Bake for 45 minutes until set and lightly golden on top."},
            {"step": 7, "text": "Cool completely before slicing."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Created during the Depression when lemons were expensive or unavailable",
            "Use white vinegar, not apple cider - it keeps the flavor cleaner",
            "Tastes like lemon pie despite containing no lemon",
            "The vinegar flavor bakes out, leaving just pleasant tartness",
            "Similar appearance to buttermilk pie"
        ],
        "tags": ["pie", "vinegar", "custard", "depression era", "vintage", "reddit", "make-do"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-old-fashioned-divinity-candy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Divinity Candy",
        "category": "desserts",
        "attribution": "Southern American (early 1900s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. A meringue-based candy from the early 1900s South. Also called 'Sea Foam' in Wisconsin. Make on a cold, dry day for best results.",
        "description": "A light, fluffy meringue candy that's somewhere between fudge, nougat, and marshmallow. A Southern Christmas tradition since the early 1900s. Truly divine when done right.",
        "servings_yield": "About 40 pieces",
        "prep_time": "15 min",
        "cook_time": "20 min",
        "total_time": "35 min (plus setting time)",
        "ingredients": [
            {"item": "sugar", "quantity": "2 1/2", "unit": "cup"},
            {"item": "light corn syrup", "quantity": "1/2", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "egg whites", "quantity": "2", "unit": "large", "prep_note": "room temperature"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "pecans or walnuts", "quantity": "1", "unit": "cup", "prep_note": "chopped, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Line baking sheets with wax paper or parchment."},
            {"step": 2, "text": "In a heavy saucepan, combine sugar, corn syrup, water, and salt."},
            {"step": 3, "text": "Cook over medium heat, stirring until sugar dissolves."},
            {"step": 4, "text": "Continue cooking WITHOUT stirring until mixture reaches 260°F (hard ball stage) on a candy thermometer."},
            {"step": 5, "text": "Meanwhile, beat egg whites in a large bowl until stiff peaks form."},
            {"step": 6, "text": "When syrup reaches 260°F, slowly pour in a thin stream into the beaten egg whites while beating continuously on high speed."},
            {"step": 7, "text": "Continue beating until mixture holds its shape when dropped from a spoon and loses its gloss, about 5-8 minutes."},
            {"step": 8, "text": "Quickly fold in vanilla and nuts if using."},
            {"step": 9, "text": "Drop by spoonfuls onto prepared sheets."},
            {"step": 10, "text": "Let set at room temperature until firm, about 2 hours."}
        ],
        "notes": [
            "ONLY make on a cold, dry day - humidity prevents proper setting",
            "Do NOT make when rain is expected",
            "If candy doesn't set, it wasn't cooked long enough",
            "If candy is grainy, it was cooked too long",
            "Called 'Sea Foam' in Wisconsin",
            "A candy thermometer is essential",
            "Work quickly once you start pouring - it sets fast"
        ],
        "tags": ["candy", "divinity", "southern", "christmas", "vintage", "reddit", "meringue"],
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
