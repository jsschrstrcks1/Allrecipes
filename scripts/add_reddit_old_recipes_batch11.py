#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 11) - Depression era and nostalgic classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "amish-friendship-bread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Amish Friendship Bread",
        "category": "breads",
        "attribution": "Traditional / 1980s Chain Letter Phenomenon",
        "source_note": "A sweet sourdough bread that spread like a chain letter in the 1980s. You share the starter and recipe with friends, creating a chain of bakers. Despite the name, there's no confirmed connection to actual Amish baking traditions.",
        "description": "A sweet, cinnamon-sugar quick bread made from a fermented sourdough starter that's shared among friends. The 10-day process creates a unique tangy sweetness. Like a chain letter, but delicious - keep a cup of starter, give three away.",
        "servings_yield": "2 loaves",
        "prep_time": "15 min (plus 10 days starter)",
        "cook_time": "1 hour",
        "total_time": "1 hour 15 min (after 10-day starter)",
        "ingredients": [
            {"item": "Amish Friendship Bread starter", "quantity": "1", "unit": "cup", "prep_note": "after Day 10"},
            {"item": "vegetable oil", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "instant vanilla pudding mix", "quantity": "1", "unit": "box", "prep_note": "5.1 oz large box"},
            {"item": "baking powder", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": "for cinnamon-sugar coating"},
            {"item": "ground cinnamon", "quantity": "1 1/2", "unit": "tsp", "prep_note": "for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "STARTER (Day 1): Combine 1 cup flour, 1 cup sugar, and 1 cup milk in a gallon zip-lock bag. Mush to combine. Let sit at room temperature."},
            {"step": 2, "text": "Days 2-4: Mush the bag once daily."},
            {"step": 3, "text": "Day 5: Add 1 cup each flour, sugar, and milk. Mush well."},
            {"step": 4, "text": "Days 6-9: Mush the bag once daily."},
            {"step": 5, "text": "Day 10 - BAKING DAY: Pour starter into a large bowl. Add 1 cup each flour, sugar, and milk. Mix well."},
            {"step": 6, "text": "Remove 4 cups of starter: Keep 1 cup for yourself, give 3 cups to friends with instructions."},
            {"step": 7, "text": "Preheat oven to 325°F (165°C). Grease two 9x5-inch loaf pans."},
            {"step": 8, "text": "Mix cinnamon-sugar coating: combine 1/2 cup sugar and 1 1/2 tsp cinnamon. Coat greased pans with half of this mixture."},
            {"step": 9, "text": "To remaining starter, add oil, eggs, vanilla, 1 cup sugar, flour, pudding mix, baking powder, baking soda, 2 tsp cinnamon, and salt."},
            {"step": 10, "text": "Mix until well combined. Divide batter between prepared pans."},
            {"step": 11, "text": "Sprinkle remaining cinnamon-sugar on top."},
            {"step": 12, "text": "Bake for 50-60 minutes until a toothpick comes out clean."},
            {"step": 13, "text": "Cool 10 minutes, then turn out onto a rack."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "Two 9x5-inch loaf pans",
        "notes": [
            "The starter ferments for 10 days before baking",
            "Keep the bag at room temperature - never refrigerate during fermentation",
            "You can start your own or receive starter from a friend",
            "The 'chain letter' aspect: keep one, give three away",
            "Popular in the 1980s but has earlier European origins (Herman cake)",
            "Despite the name, no confirmed connection to actual Amish traditions"
        ],
        "tags": ["bread", "quick bread", "Amish", "friendship bread", "sourdough", "1980s", "cinnamon", "chain letter"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-fruit-cocktail-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fruit Cocktail Cake",
        "category": "desserts",
        "attribution": "1950s Vintage Recipe / Del Monte",
        "source_note": "Popular from the late 1950s through the early 1980s when canned fruit cocktail was a pantry staple. Uses the fruit AND the syrup for a super moist cake. Often topped with coconut and brown sugar that gets crunchy while baking.",
        "description": "A moist, old-fashioned cake made with a can of fruit cocktail - fruit AND syrup included. Topped with brown sugar and coconut that bakes into a crunchy, caramelized layer. No butter or oil needed - the fruit provides all the moisture.",
        "servings_yield": "12-16 servings",
        "prep_time": "10 min",
        "cook_time": "40 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cups"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "fruit cocktail", "quantity": "15", "unit": "oz can", "prep_note": "undrained - use all juice"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": "packed, for topping"},
            {"item": "sweetened flaked coconut", "quantity": "1/2", "unit": "cup", "prep_note": "for topping"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "sugar", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "evaporated milk", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "In a large bowl, whisk together flour, 1 cup sugar, baking soda, and salt."},
            {"step": 3, "text": "Add egg and entire can of fruit cocktail with all the syrup. Stir until combined."},
            {"step": 4, "text": "Pour batter into prepared pan."},
            {"step": 5, "text": "Mix brown sugar and coconut. Sprinkle evenly over batter."},
            {"step": 6, "text": "Bake for 35-40 minutes until golden and a toothpick comes out clean."},
            {"step": 7, "text": "While cake bakes, make the glaze: Combine butter, 1/2 cup sugar, and evaporated milk in a saucepan."},
            {"step": 8, "text": "Bring to a boil, stirring constantly. Boil for 2 minutes."},
            {"step": 9, "text": "Remove from heat and stir in vanilla."},
            {"step": 10, "text": "Pour hot glaze over the hot cake immediately after removing from oven."},
            {"step": 11, "text": "Let cool before serving. Even better the next day."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Do NOT drain the fruit cocktail - the syrup provides moisture",
            "No butter or oil in the batter - the fruit keeps it moist",
            "The coconut-brown sugar topping gets crunchy while baking",
            "Pour the glaze over HOT cake for best absorption",
            "Popular from the 1950s-1980s when canned fruit was king",
            "Tastes even better the next day"
        ],
        "tags": ["cake", "fruit cocktail", "1950s", "vintage", "coconut", "no oil", "potluck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "old-fashioned-applesauce-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Applesauce Cake",
        "category": "desserts",
        "attribution": "Traditional American / 1940s Recipe",
        "source_note": "A vintage spice cake that became popular during WWII rationing when applesauce was used to replace eggs and fat. The applesauce keeps it incredibly moist. Often loaded with raisins and walnuts.",
        "description": "A moist, heavily spiced cake that uses applesauce in place of most of the fat. Loaded with warm spices, raisins, and walnuts. Popular during WWII rationing and still beloved today. The applesauce keeps it moist for days.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "50 min",
        "total_time": "1 hour 10 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2 1/2", "unit": "cups"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground cloves", "quantity": "1/4", "unit": "tsp"},
            {"item": "ground allspice", "quantity": "1/4", "unit": "tsp"},
            {"item": "unsweetened applesauce", "quantity": "1 1/2", "unit": "cups"},
            {"item": "vegetable oil or melted shortening", "quantity": "1/2", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "raisins", "quantity": "1", "unit": "cup"},
            {"item": "chopped walnuts", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour a 9x13-inch pan or bundt pan."},
            {"step": 2, "text": "Soak raisins in hot water for 10 minutes to plump them. Drain well."},
            {"step": 3, "text": "In a large bowl, whisk together flour, sugar, baking soda, salt, cinnamon, nutmeg, cloves, and allspice."},
            {"step": 4, "text": "Add applesauce, oil, and eggs. Beat until well combined."},
            {"step": 5, "text": "Fold in drained raisins and walnuts."},
            {"step": 6, "text": "Pour into prepared pan."},
            {"step": 7, "text": "Bake for 45-50 minutes until a toothpick comes out clean."},
            {"step": 8, "text": "Cool in pan for 10 minutes, then turn out or serve from pan."},
            {"step": 9, "text": "Serve plain, dusted with powdered sugar, or with cream cheese frosting."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan or bundt pan",
        "notes": [
            "Use unsweetened applesauce to control sweetness",
            "Chunky or smooth applesauce both work well",
            "Popular during WWII rationing - applesauce replaced eggs and fat",
            "Stays moist for days thanks to the applesauce",
            "Soaking the raisins makes them plump and tender",
            "Great plain or with cream cheese frosting"
        ],
        "tags": ["cake", "applesauce", "spice cake", "1940s", "WWII", "raisins", "walnuts", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "poor-mans-cake-depression",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Poor Man's Cake (Depression Cake)",
        "category": "desserts",
        "attribution": "Depression Era / 1930s-1940s",
        "source_note": "A 'war cake' or 'depression cake' created when eggs, milk, and butter were scarce or rationed. Boiling the wet ingredients extracts maximum flavor from minimal ingredients. Also called 'Milkless, Eggless, Butterless Cake.'",
        "description": "A moist spice cake made without eggs, milk, or butter - born from necessity during the Depression and WWII rationing. The secret is boiling the raisins with sugar, water, and shortening to create a rich, flavorful base. Proves you don't need fancy ingredients for delicious cake.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "45 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "water", "quantity": "2", "unit": "cups"},
            {"item": "brown sugar", "quantity": "2", "unit": "cups", "prep_note": "packed"},
            {"item": "raisins", "quantity": "2", "unit": "cups"},
            {"item": "vegetable shortening or lard", "quantity": "1/2", "unit": "cup"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground cloves", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "3", "unit": "cups"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "baking powder", "quantity": "2", "unit": "tsp"},
            {"item": "chopped walnuts", "quantity": "1", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large saucepan, combine water, brown sugar, raisins, shortening, cinnamon, cloves, nutmeg, and salt."},
            {"step": 2, "text": "Bring to a boil, stirring to dissolve sugar. Boil for 5 minutes."},
            {"step": 3, "text": "Remove from heat and let cool to lukewarm (about 30 minutes)."},
            {"step": 4, "text": "Preheat oven to 325°F (165°C). Grease and flour a 9x13-inch pan or tube pan."},
            {"step": 5, "text": "In a bowl, whisk together flour, baking soda, and baking powder."},
            {"step": 6, "text": "Add dry ingredients to the cooled raisin mixture. Stir until just combined."},
            {"step": 7, "text": "Fold in walnuts if using."},
            {"step": 8, "text": "Pour into prepared pan."},
            {"step": 9, "text": "Bake for 40-45 minutes until a toothpick comes out clean."},
            {"step": 10, "text": "Cool before serving. Can be dusted with powdered sugar or glazed."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "9x13-inch pan or tube pan",
        "notes": [
            "No eggs, milk, or butter - born from Depression-era necessity",
            "Boiling the wet ingredients extracts flavor and softens raisins",
            "Must cool before adding flour or the baking soda won't work properly",
            "Also known as War Cake or Milkless Eggless Butterless Cake",
            "Some versions use 2 cups black coffee instead of water (YumYum Cake)",
            "Traveled well - sent to soldiers overseas during WWII"
        ],
        "tags": ["cake", "Depression era", "no eggs", "no milk", "no butter", "war cake", "1930s", "raisins"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mississippi-mud-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mississippi Mud Cake",
        "category": "desserts",
        "attribution": "Southern Classic / 1970s",
        "source_note": "A rich chocolate cake topped with melted marshmallows and chocolate frosting, named for its resemblance to the muddy banks of the Mississippi River. Essentially a brownie upgrade invented sometime in the 1970s. A Southern potluck staple.",
        "description": "A dense, fudgy chocolate cake topped with a layer of gooey melted marshmallows and rich chocolate frosting studded with pecans. Named for its resemblance to Mississippi River mud. Part brownie, part cake, all delicious.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "35 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "melted"},
            {"item": "cocoa powder", "quantity": "1/3", "unit": "cup", "prep_note": "unsweetened"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "vanilla extract", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cups"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "chopped pecans", "quantity": "1 1/2", "unit": "cups", "prep_note": "divided"},
            {"item": "miniature marshmallows", "quantity": "3", "unit": "cups"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for frosting"},
            {"item": "cocoa powder", "quantity": "1/3", "unit": "cup", "prep_note": "for frosting"},
            {"item": "evaporated milk", "quantity": "1/3", "unit": "cup", "prep_note": "for frosting"},
            {"item": "powdered sugar", "quantity": "3 1/2", "unit": "cups", "prep_note": "for frosting"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for frosting"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "In a large bowl, whisk melted butter and 1/3 cup cocoa until smooth."},
            {"step": 3, "text": "Beat in eggs, sugar, and 1 1/2 tsp vanilla."},
            {"step": 4, "text": "Stir in flour and salt until just combined."},
            {"step": 5, "text": "Fold in 1 cup of the pecans."},
            {"step": 6, "text": "Pour batter into prepared pan. Bake for 25-30 minutes until set."},
            {"step": 7, "text": "Remove from oven and immediately sprinkle marshmallows over hot cake."},
            {"step": 8, "text": "Return to oven for 2-3 minutes until marshmallows are puffed and slightly melted."},
            {"step": 9, "text": "For frosting: Melt 1/2 cup butter in a saucepan over medium heat."},
            {"step": 10, "text": "Whisk in 1/3 cup cocoa and evaporated milk. Cook 2-3 minutes, stirring constantly."},
            {"step": 11, "text": "Remove from heat. Whisk in powdered sugar and 1 tsp vanilla until smooth."},
            {"step": 12, "text": "Pour warm frosting over marshmallow layer. Sprinkle with remaining 1/2 cup pecans."},
            {"step": 13, "text": "Let cool completely before cutting."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Named for its resemblance to Mississippi River mud",
            "The texture is more brownie-like than cake-like",
            "Don't overbake - it should be fudgy",
            "Add marshmallows to HOT cake so they melt properly",
            "Some versions add coffee to intensify chocolate flavor",
            "A Southern potluck staple since the 1970s"
        ],
        "tags": ["cake", "chocolate", "marshmallow", "Mississippi mud", "Southern", "1970s", "pecans", "brownie"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-prune-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vintage Prune Cake with Buttermilk Glaze",
        "category": "desserts",
        "attribution": "Traditional American / 1940s Wartime Recipe",
        "source_note": "Popular during the 1940s when sugar was rationed - prunes provided natural sweetness. The spices mask any 'prune' taste, and most people can't even tell what makes it so moist. Often served with a warm buttermilk glaze.",
        "description": "A deeply moist, richly spiced cake that uses chopped prunes for natural sweetness and incredible moisture. Even people who think they don't like prunes love this cake - the spices create a warm, complex flavor. Topped with a warm buttermilk glaze.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "45 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "pitted prunes", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": "for soaking prunes"},
            {"item": "vegetable oil", "quantity": "1", "unit": "cup"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground allspice", "quantity": "1/2", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "for glaze"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp", "prep_note": "for glaze"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Place chopped prunes in a bowl, cover with 1 cup buttermilk, and let soak while preparing batter."},
            {"step": 2, "text": "Preheat oven to 350°F (175°C). Grease and flour a 9x13-inch pan or bundt pan."},
            {"step": 3, "text": "In a large bowl, whisk together oil, sugar, and eggs until well combined."},
            {"step": 4, "text": "In another bowl, whisk together flour, 1 tsp baking soda, salt, cinnamon, nutmeg, and allspice."},
            {"step": 5, "text": "Add dry ingredients to wet ingredients, alternating with the prune-buttermilk mixture."},
            {"step": 6, "text": "Stir in 1 tsp vanilla. Pour into prepared pan."},
            {"step": 7, "text": "Bake for 40-45 minutes until a toothpick comes out clean."},
            {"step": 8, "text": "While cake bakes, make glaze: Combine butter, 1 cup sugar, 1/2 cup buttermilk, and 1/2 tsp baking soda in a saucepan."},
            {"step": 9, "text": "Bring to a boil, stirring constantly. Boil for 2 minutes - it will foam up."},
            {"step": 10, "text": "Remove from heat and stir in 1 tsp vanilla."},
            {"step": 11, "text": "Poke holes all over the hot cake with a toothpick. Pour warm glaze over hot cake."},
            {"step": 12, "text": "Let cool before serving. Even better the next day."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan or bundt pan",
        "notes": [
            "Popular during 1940s sugar rationing - prunes provided natural sweetness",
            "Most people can't tell it's prune cake - the spices mask the flavor",
            "Soaking prunes in buttermilk makes them extra tender",
            "Oil keeps the cake moist longer than butter would",
            "The buttermilk glaze is essential - don't skip it",
            "Better the next day once flavors meld"
        ],
        "tags": ["cake", "prune", "spice cake", "1940s", "vintage", "buttermilk glaze", "Southern"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-snickerdoodles",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Classic Snickerdoodle Cookies",
        "category": "desserts",
        "attribution": "Dutch-German American Traditional",
        "source_note": "A classic American cookie with Dutch-German origins in New England. The defining ingredient is cream of tartar, which creates the signature tangy flavor and chewy texture. Named possibly after the German word 'Schneckennudel' (snail noodle).",
        "description": "Soft, pillowy cookies coated in cinnamon sugar with a signature tangy flavor from cream of tartar. Not just a sugar cookie with cinnamon - the cream of tartar makes them uniquely chewy with a crackly top. A beloved American classic.",
        "servings_yield": "About 36 cookies",
        "prep_time": "20 min",
        "cook_time": "10 min per batch",
        "total_time": "45 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened (2 sticks)"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups", "prep_note": "for dough"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "2 3/4", "unit": "cups"},
            {"item": "cream of tartar", "quantity": "2", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "sugar", "quantity": "3", "unit": "tbsp", "prep_note": "for coating"},
            {"item": "ground cinnamon", "quantity": "2", "unit": "tsp", "prep_note": "for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper."},
            {"step": 2, "text": "In a large bowl, cream butter and 1 1/2 cups sugar until light and fluffy."},
            {"step": 3, "text": "Beat in eggs and vanilla."},
            {"step": 4, "text": "In another bowl, whisk together flour, cream of tartar, baking soda, and salt."},
            {"step": 5, "text": "Gradually add dry ingredients to wet ingredients, mixing until just combined."},
            {"step": 6, "text": "In a small bowl, mix 3 tbsp sugar and cinnamon for the coating."},
            {"step": 7, "text": "Roll dough into 1-inch balls."},
            {"step": 8, "text": "Roll each ball in cinnamon-sugar mixture to coat completely."},
            {"step": 9, "text": "Place 2 inches apart on prepared baking sheets."},
            {"step": 10, "text": "Bake for 8-10 minutes until edges are set but centers still look slightly underdone."},
            {"step": 11, "text": "Let cool on baking sheet for 5 minutes before transferring to a wire rack."}
        ],
        "temperature": "375°F (190°C)",
        "notes": [
            "Cream of tartar is essential - it's what makes a snickerdoodle a snickerdoodle",
            "Without cream of tartar, it's just a cinnamon sugar cookie",
            "The cream of tartar creates the tangy flavor and chewy texture",
            "Roll balls in cinnamon-sugar twice for extra crackly coating",
            "Dutch-German origins, possibly named after 'Schneckennudel'",
            "Don't overbake - they firm up as they cool"
        ],
        "tags": ["cookies", "snickerdoodle", "cinnamon", "cream of tartar", "Dutch-German", "classic", "chewy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "oatmeal-cake-broiled-frosting",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Oatmeal Cake with Broiled Coconut Frosting",
        "category": "desserts",
        "attribution": "Traditional American / Quaker Oats (1920s-30s)",
        "source_note": "An old-fashioned oatmeal spice cake popular since the 1920s-30s. The signature broiled coconut-pecan topping caramelizes under the broiler. A variation of this recipe appeared on Quaker oats containers. Also known as Lazy Daisy Cake.",
        "description": "A moist, hearty oatmeal cake with warm spices, topped with a magical broiled frosting of butter, brown sugar, coconut, and pecans that caramelizes into a crunchy, gooey layer. The oats are soaked in boiling water for maximum tenderness.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "45 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "old-fashioned rolled oats", "quantity": "1", "unit": "cup"},
            {"item": "boiling water", "quantity": "1 1/2", "unit": "cups"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "granulated sugar", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "butter", "quantity": "6", "unit": "tbsp", "prep_note": "melted, for topping"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed, for topping"},
            {"item": "heavy cream or evaporated milk", "quantity": "1/4", "unit": "cup", "prep_note": "for topping"},
            {"item": "sweetened flaked coconut", "quantity": "1", "unit": "cup", "prep_note": "for topping"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "for topping"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour boiling water over oats in a bowl. Let stand 20 minutes."},
            {"step": 2, "text": "Preheat oven to 350°F (175°C). Grease a 9x13-inch metal baking pan (not glass)."},
            {"step": 3, "text": "In a large bowl, cream 1/2 cup butter with both sugars until fluffy."},
            {"step": 4, "text": "Beat in eggs and 1 tsp vanilla."},
            {"step": 5, "text": "In another bowl, whisk together flour, baking soda, cinnamon, nutmeg, and salt."},
            {"step": 6, "text": "Add dry ingredients to creamed mixture alternately with the soaked oats, mixing until combined."},
            {"step": 7, "text": "Pour into prepared pan. Bake for 35-40 minutes until a toothpick comes out clean."},
            {"step": 8, "text": "While cake bakes, make topping: Combine melted butter, brown sugar, and cream in a bowl."},
            {"step": 9, "text": "Stir in coconut, pecans, and vanilla."},
            {"step": 10, "text": "When cake is done, spread topping evenly over hot cake."},
            {"step": 11, "text": "Place under broiler 4-6 inches from heat. Broil 1-3 minutes until bubbly and golden."},
            {"step": 12, "text": "Watch carefully - it can burn quickly! Remove when golden brown."}
        ],
        "temperature": "350°F (175°C), then broil",
        "pan_size": "9x13-inch metal pan (not glass)",
        "notes": [
            "Must use a METAL pan - glass cannot go under the broiler safely",
            "Watch the broiler carefully - topping goes from perfect to burnt fast",
            "Soaking the oats in boiling water makes the cake extra tender",
            "A version appeared on Quaker oats containers",
            "Also known as Lazy Daisy Cake",
            "Popular since the 1920s-30s"
        ],
        "tags": ["cake", "oatmeal", "coconut", "pecans", "broiled frosting", "1920s", "vintage", "Quaker"],
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
