#!/usr/bin/env python3
"""Add famous recipes from Reddit r/Old_Recipes to the database."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "reddit-murder-cookies-scotch",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Murder Cookies (Scotch Cookies)",
        "category": "desserts",
        "attribution": "Cushman's Bakery / u/NearKilroy, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Named 'Murder Cookies' after being discovered while researching a murder that took place in the poster's historic Portland, Maine house.",
        "description": "A soft, chewy molasses cookie with warm spices including the distinctive flavor of mace. Originally called 'Secret Scotch Cookies' from Cushman's Bakery, renamed by the Reddit community.",
        "servings_yield": "About 60 cookies",
        "prep_time": "15 min",
        "cook_time": "12 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "3 1/2", "unit": "cup"},
            {"item": "baking soda", "quantity": "2 1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "mace", "quantity": "1", "unit": "tsp"},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "shortening", "quantity": "1", "unit": "cup"},
            {"item": "white sugar", "quantity": "1 1/2", "unit": "cup"},
            {"item": "molasses", "quantity": "1/2", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "milk", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Line baking sheets with parchment paper."},
            {"step": 2, "text": "Whisk together flour, baking soda, salt, mace, and cinnamon in a bowl; set aside."},
            {"step": 3, "text": "Cream shortening and sugar until light and creamy. Mix in molasses, then add egg and stir until combined."},
            {"step": 4, "text": "Add dry ingredients to wet on low mixer speed (or by hand), adding milk as needed until achieving a soft dough."},
            {"step": 5, "text": "Drop dough by teaspoonfuls onto prepared baking sheets. Optional: roll in sugar before baking."},
            {"step": 6, "text": "Bake for about 12 minutes until set. Bake one sheet at a time for best results."},
            {"step": 7, "text": "Cool completely on a wire rack."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Refrigerating the dough for several hours before baking prevents cookies from spreading too thin",
            "Mace is derived from the skin of the nutmeg seed and gives these cookies their distinctive flavor",
            "The r/Old_Recipes subreddit spawned a dedicated spinoff subreddit r/MurderCookie with over 600 members"
        ],
        "tags": ["cookies", "molasses", "vintage", "reddit", "viral", "murder cookies"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-nanas-devils-food-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Nana's Devil's Food Cake",
        "category": "desserts",
        "attribution": "u/iamktf (Kristin Toth), Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Family traces recipe back to mid-century Philadelphia. Despite Hungarian family heritage, the cake was named 'Nana's' by the poster's brother in the 1970s.",
        "description": "A moist, rich chocolate cake made with oil (stays moist for days!) and coffee that intensifies the chocolate flavor without imparting coffee taste. Called 'the best chocolate cake ever, guaranteed' by the family.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "40-50 min",
        "total_time": "1 hour 10 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "fine salt", "quantity": "1", "unit": "tsp"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "baking soda", "quantity": "2", "unit": "tsp"},
            {"item": "cocoa powder", "quantity": "3/4", "unit": "cup", "prep_note": "Dutch-processed recommended"},
            {"item": "white granulated sugar", "quantity": "2", "unit": "cup"},
            {"item": "vegetable oil", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "brewed or instant coffee", "quantity": "1", "unit": "cup", "prep_note": "hot"},
            {"item": "chocolate chips", "quantity": "6", "unit": "oz", "prep_note": "about 1 cup, for ganache"},
            {"item": "heavy whipping cream", "quantity": "1/2", "unit": "cup", "prep_note": "for ganache"},
            {"item": "vanilla or liqueur", "quantity": "1", "unit": "tsp", "prep_note": "for ganache"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (reduce by 25°F for glass pans). Grease and flour your pan(s)."},
            {"step": 2, "text": "Whisk together flour, salt, baking powder, baking soda, and cocoa powder; set aside."},
            {"step": 3, "text": "Mix sugar and oil, then beat in eggs and vanilla until fluffy (about 2 minutes)."},
            {"step": 4, "text": "Combine hot coffee with milk. Alternate adding this mixture and flour mixture to the batter until well combined."},
            {"step": 5, "text": "Pour into prepared pan(s) and bake until a tester inserted in the center comes out clean: 10-inch bundt 40-50 min, two 8-9\" rounds 25-35 min, 9x13 pan 40-50 min, cupcakes 20-30 min."},
            {"step": 6, "text": "For ganache: warm chocolate and cream over medium-low heat, whisking until melted. Remove from heat and whisk in vanilla."},
            {"step": 7, "text": "Cool ganache 10-15 minutes until it reaches lava-like consistency, then spoon over cooled cake."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Many bakers prefer 350°F over the original 375°F",
            "Very similar to Hershey's Black Magic Cake and Ina Garten's Beatty's Chocolate Cake",
            "Has been adapted into cupcakes, layer cakes, Black Forest Cake, and coffin-shaped cakes",
            "Works with almond milk instead of whole milk, or Greek yogurt replacing some oil"
        ],
        "tags": ["cake", "chocolate", "devils food", "vintage", "reddit", "viral", "bundt"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-grandmas-lemon-bars",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grandma's Lemon Bars",
        "category": "desserts",
        "attribution": "Grandma Caroline / u/JustHood (Megan Hood), Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. So popular it spawned its own subreddit r/JustHoodsLemonBars with 12,000+ members.",
        "description": "The most popular recipe on r/Old_Recipes - easy to make lemon bars packed with intense lemon flavor. A buttery shortbread crust topped with a sweet-yet-tart lemon filling.",
        "servings_yield": "18 squares",
        "prep_time": "15 min",
        "cook_time": "50 min",
        "total_time": "1 hour 5 min (plus cooling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup", "prep_note": "for crust"},
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened, salted"},
            {"item": "powdered sugar", "quantity": "1/2", "unit": "cup", "prep_note": "for crust"},
            {"item": "eggs", "quantity": "4", "unit": "large", "prep_note": "for filling"},
            {"item": "white sugar", "quantity": "1 1/2", "unit": "cup", "prep_note": "for filling"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "lemon rind", "quantity": "4", "unit": "tsp", "prep_note": "grated"},
            {"item": "lemon juice", "quantity": "4", "unit": "tbsp", "prep_note": "5-7 tbsp recommended"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "powdered sugar", "quantity": "1", "unit": "tbsp", "prep_note": "for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch glass baking pan."},
            {"step": 2, "text": "Make crust: Combine flour, softened butter, and sifted powdered sugar in a stand mixer. Mix on low until clumps form, then increase to medium until dough develops (1-2 minutes)."},
            {"step": 3, "text": "Press dough evenly across the pan bottom and sides, creating a 1/2-1 inch edge."},
            {"step": 4, "text": "Bake crust for 20 minutes until lightly golden."},
            {"step": 5, "text": "While crust bakes, whisk together eggs, white sugar, baking powder, lemon rind, lemon juice, vanilla, and salt until fluffy."},
            {"step": 6, "text": "Pour filling carefully over the hot crust."},
            {"step": 7, "text": "Bake 25-30 minutes until filling sets."},
            {"step": 8, "text": "Cool completely (about 4 hours)."},
            {"step": 9, "text": "Dust with powdered sugar, cut into squares, and serve."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Grandma Caroline preferred bottled lemon juice - 'much more tart, especially once baked'",
            "Hood's family doubles the lemon juice and adds zest",
            "Use room-temperature salted butter for easiest mixing",
            "As Hood said about the popularity: 'I feel like every time someone makes these bars, it reminds us of her: sour at first, but sweet in the end.'"
        ],
        "tags": ["bars", "lemon", "dessert", "vintage", "reddit", "viral", "grandma"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-whipping-cream-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Whipping Cream Cake",
        "category": "desserts",
        "attribution": "u/Jamie_of_house_m, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. From an Iowan town's centennial anniversary cookbook from 1979. The go-to birthday cake for the poster's family.",
        "description": "A dense, buttery bundt cake with just six ingredients and one brilliant technique: starting in a COLD oven. The slow warming creates a perfectly gooey bottom layer.",
        "servings_yield": "12 servings",
        "prep_time": "15 min",
        "cook_time": "75-90 min",
        "total_time": "About 2 hours",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "3 1/4", "unit": "cup", "prep_note": "divided (1/4 cup for pan)"},
            {"item": "salted butter", "quantity": "1", "unit": "cup", "prep_note": "softened"},
            {"item": "granulated sugar", "quantity": "3", "unit": "cup"},
            {"item": "eggs", "quantity": "6", "unit": "large"},
            {"item": "whipping cream", "quantity": "1", "unit": "cup", "prep_note": "unwhipped"},
            {"item": "vanilla extract", "quantity": "2", "unit": "tsp"},
            {"item": "shortening", "quantity": "", "unit": "for greasing"}
        ],
        "instructions": [
            {"step": 1, "text": "Generously grease a 12-cup bundt pan with shortening. Add 1/4 cup flour, cover with plastic wrap, turn and shake to coat the interior, then discard excess."},
            {"step": 2, "text": "Using a stand mixer with paddle attachment, beat softened butter and sugar until pale and fluffy (about 3 minutes). The mixture will be stiff rather than smooth."},
            {"step": 3, "text": "Scrape down bowl sides and incorporate eggs one at a time, mixing after each addition until the yolk disappears."},
            {"step": 4, "text": "On low speed, add remaining 3 cups flour in one-cup portions, alternating with the whipping cream, beginning and ending with flour. Mix in vanilla until silky smooth."},
            {"step": 5, "text": "Pour batter into prepared pan and smooth the top."},
            {"step": 6, "text": "Place in a COLD oven. Set temperature to 325°F. Bake for 75-90 minutes until a toothpick comes clean from the center."},
            {"step": 7, "text": "Allow to cool in pan for 30 minutes. Flip onto a cake stand or rack to cool completely."},
            {"step": 8, "text": "Serve topped with fresh whipped cream and berries."}
        ],
        "temperature": "325°F (163°C) - start in COLD oven",
        "notes": [
            "CRITICAL: Start in a COLD oven - this is what makes the cake special",
            "No chemical leavening (baking soda/powder) - relies on mechanical leavening from mixing",
            "Butter and eggs must be at room temperature for proper rise",
            "As the poster described: 'The bottom layer always seems to be just slightly undercooked, leaving the last few bites perfectly gooey.'",
            "One Reddit review: 'I CANNOT BAKE AND THIS TURNED OUT OK!'"
        ],
        "tags": ["cake", "bundt", "vintage", "reddit", "viral", "cold oven", "1970s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-depression-era-peanut-butter-bread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Depression Era Peanut Butter Bread (1932)",
        "category": "breads",
        "attribution": "Five Roses Flour Company / u/trixietravisbrown, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Originally from 'A Guide to Good Cooking' (1932) by Five Roses Flour Company. Popular during Great Depression because it requires no eggs.",
        "description": "A simple quick bread from 1932 that uses peanut butter to replace both eggs and butter. Popular during the Great Depression when both were hard to come by.",
        "servings_yield": "1 loaf",
        "prep_time": "10 min",
        "cook_time": "50-60 min",
        "total_time": "1 hour 10 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "4", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "milk", "quantity": "1 1/3", "unit": "cup"},
            {"item": "peanut butter", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F. Grease a 9x5 inch loaf pan."},
            {"step": 2, "text": "In a large bowl, whisk together flour, sugar, baking powder, and salt."},
            {"step": 3, "text": "Add peanut butter and cut into dry ingredients until mixture resembles coarse crumbs."},
            {"step": 4, "text": "Add milk and stir until just combined. Do not overmix."},
            {"step": 5, "text": "Pour batter into prepared pan."},
            {"step": 6, "text": "Bake for 50-60 minutes until a toothpick inserted in center comes out clean."},
            {"step": 7, "text": "Cool in pan for 10 minutes, then turn out onto wire rack."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "No eggs or butter needed - peanut butter provides fat and binding",
            "Most bakers recommend using MORE peanut butter than the original recipe calls for",
            "An earlier version appeared in the 1901 Settlement Cookbook by Lizzie Black Kander",
            "Over 3,900 upvotes on the r/Old_Recipes subreddit"
        ],
        "tags": ["bread", "quick bread", "peanut butter", "depression era", "vintage", "reddit", "viral", "no eggs"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-grandmas-hamburger-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grandma's Hamburger Pie",
        "category": "mains",
        "attribution": "u/Speedtrap1, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. 'This is my grandmother's Hamburger Pie recipe. It was something that she would make whenever company stopped by.'",
        "description": "A simple, hearty pie with seasoned ground beef in a creamy gravy, topped with melted cheese, all in a pie crust. Perfect for unexpected company.",
        "servings_yield": "6-8 servings",
        "prep_time": "15 min",
        "cook_time": "35 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "ground beef", "quantity": "1", "unit": "lb"},
            {"item": "onion soup mix", "quantity": "1", "unit": "packet"},
            {"item": "powdered milk", "quantity": "1/4", "unit": "cup", "prep_note": "or use 1 3/4 cup whole milk instead of powder and water"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "1 3/4", "unit": "cup", "prep_note": "omit if using whole milk"},
            {"item": "shredded cheese", "quantity": "1", "unit": "cup", "prep_note": "or more to taste"},
            {"item": "frozen pie shell", "quantity": "1", "unit": "9-inch", "prep_note": "unbaked"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 400°F."},
            {"step": 2, "text": "Brown the hamburger meat in a pan and drain the excess fat (or don't)."},
            {"step": 3, "text": "Add onion soup mix, flour, powdered milk, and water (or just whole milk). Cook on medium until thickened."},
            {"step": 4, "text": "While the meat is thickening, get out your frozen pie crust."},
            {"step": 5, "text": "Once thickened, pour the meat mixture into the pie shell (should fill to the top or just slightly below)."},
            {"step": 6, "text": "Add the cheese on top. The recipe calls for 1 cup, but let's be honest, you're going to add more and that is fine."},
            {"step": 7, "text": "Bake for 25 minutes until cheese is melted and bubbly. Enjoy!"}
        ],
        "temperature": "400°F (200°C)",
        "notes": [
            "Many make it with whole milk instead of powdered milk and water",
            "Add more cheese than the recipe calls for - everyone does!",
            "Great for unexpected company"
        ],
        "tags": ["pie", "beef", "ground beef", "comfort food", "vintage", "reddit", "grandma"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-alice-cookies-whipped-shortbread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Alice Cookies (Whipped Shortbread)",
        "category": "desserts",
        "attribution": "Sarah Conklin, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. Found on an index card tucked inside an old cookbook. Believed to be named after the woman who baked them.",
        "description": "A light, airy whipped shortbread that melts in your mouth. The defining characteristic is the long 10-minute whipping period that creates an incredibly delicate, crumbly texture.",
        "servings_yield": "About 48 cookies",
        "prep_time": "15 min",
        "cook_time": "15-18 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened"},
            {"item": "brown sugar", "quantity": "1/4", "unit": "cup", "prep_note": "packed"},
            {"item": "white sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "egg yolk", "quantity": "1", "unit": "large"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "or use salted butter"},
            {"item": "walnuts or glazed cherries", "quantity": "", "unit": "for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F."},
            {"step": 2, "text": "Beat butter, brown sugar, and white sugar together for a FULL 10 MINUTES until batter turns creamy white and texture is very light."},
            {"step": 3, "text": "Add egg yolk and beat until combined."},
            {"step": 4, "text": "Gradually add flour and salt, mixing until just combined."},
            {"step": 5, "text": "Drop by teaspoonfuls onto ungreased baking sheet."},
            {"step": 6, "text": "Top each round with a piece of walnut or glazed cherry."},
            {"step": 7, "text": "Bake at 325°F until set and very light golden, about 15-18 minutes."},
            {"step": 8, "text": "Cool COMPLETELY on the pan before transferring - cookies are very delicate."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "The 10-minute whipping time is essential - don't skip it!",
            "Cookies are extremely delicate - let cool completely on pan before moving",
            "Use good quality butter since there are so few ingredients",
            "Can top with chocolate kisses, pecans, or sprinkled sugar instead",
            "As one tester said: they 'melt in your mouth when you bite into it'"
        ],
        "tags": ["cookies", "shortbread", "whipped", "vintage", "reddit", "delicate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-apple-cream-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grandma's Apple Cream Pie",
        "category": "desserts",
        "attribution": "PostSecret / u/laniidae_, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Shared anonymously on PostSecret with the note: 'This recipe has been a family secret for 100 years. My petty vindictive aunts don't deserve to keep it to themselves. I love and miss you, Grandma!'",
        "description": "An unusual pie made with GRATED apples and a cream mixture poured on top. The shredded apples combine with the filling for even flavor distribution - 'better than a normal apple pie.'",
        "servings_yield": "8 servings",
        "prep_time": "20 min",
        "cook_time": "45 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "deep-dish pie crust", "quantity": "1", "unit": "9-inch", "prep_note": "store-bought or homemade"},
            {"item": "Granny Smith apples", "quantity": "4", "unit": "medium", "prep_note": "peeled and grated"},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "melted"},
            {"item": "white sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "tbsp"},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/4", "unit": "tsp"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large", "prep_note": "beaten"},
            {"item": "egg yolk", "quantity": "1", "unit": "large", "prep_note": "for egg wash"},
            {"item": "water", "quantity": "1", "unit": "tbsp", "prep_note": "for egg wash"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 400°F."},
            {"step": 2, "text": "Peel the apples, then GRATE them into the pie crust."},
            {"step": 3, "text": "Drizzle the grated apples with melted butter."},
            {"step": 4, "text": "In a bowl, mix together sugar, flour, cinnamon, and nutmeg."},
            {"step": 5, "text": "Mix in the milk and beaten eggs until combined."},
            {"step": 6, "text": "Pour the cream mixture over the apples."},
            {"step": 7, "text": "Whisk egg yolk with 1 tablespoon water. Brush edges of pie crust with egg wash."},
            {"step": 8, "text": "Bake at 400°F for 10 minutes, then reduce to 350°F and bake for 35 more minutes until golden brown."}
        ],
        "temperature": "400°F (200°C) then 350°F (175°C)",
        "notes": [
            "The grated apples are what make this pie special - flavor is distributed throughout",
            "Much creamier and more moist than typical apple pie",
            "'With apple pie, you have chunks of apple and the filling, but they feel separate. With the apple being grated, you get all of the filling mixed through it.'",
            "Recipe was a 100-year family secret before being shared"
        ],
        "tags": ["pie", "apple", "cream", "vintage", "reddit", "viral", "grandma", "secret recipe"],
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
