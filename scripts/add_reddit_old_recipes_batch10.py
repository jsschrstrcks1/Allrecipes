#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 10) - potluck classics and no-bake favorites."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "strawberry-pretzel-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Strawberry Pretzel Salad",
        "category": "desserts",
        "attribution": "Joys of Jell-O Cookbook (1960s)",
        "source_note": "Originated in the Joys of Jell-O cookbook in the 1960s. A wobbly 'salad' that's been a potluck and holiday favorite in the South, Midwest, and Rust Belt for nearly sixty years. Despite the name, it's definitely a dessert.",
        "description": "Three layers of deliciousness: a salty-sweet pretzel crust, a fluffy cream cheese layer, and jiggly strawberry Jell-O studded with fresh berries. Called a 'salad' but it's absolutely dessert. A Midwestern and Southern holiday staple.",
        "servings_yield": "12-16 servings",
        "prep_time": "25 min",
        "cook_time": "10 min",
        "total_time": "35 min (plus 4-6 hours chilling)",
        "ingredients": [
            {"item": "pretzel twists", "quantity": "2", "unit": "cups", "prep_note": "crushed (about 8 oz)"},
            {"item": "butter", "quantity": "3/4", "unit": "cup", "prep_note": "melted"},
            {"item": "sugar", "quantity": "3", "unit": "tbsp", "prep_note": "for crust"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "for cream cheese layer"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "strawberry Jell-O", "quantity": "6", "unit": "oz box", "prep_note": "large box"},
            {"item": "boiling water", "quantity": "2", "unit": "cups"},
            {"item": "frozen strawberries", "quantity": "20", "unit": "oz", "prep_note": "thawed, or 2 cups fresh sliced"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 2, "text": "For crust: Mix crushed pretzels, melted butter, and 3 tablespoons sugar."},
            {"step": 3, "text": "Press into the bottom of a 9x13-inch baking dish."},
            {"step": 4, "text": "Bake for 10 minutes. Cool completely."},
            {"step": 5, "text": "For cream cheese layer: Beat cream cheese and 1 cup sugar until smooth."},
            {"step": 6, "text": "Fold in Cool Whip."},
            {"step": 7, "text": "Spread over cooled crust, making sure to seal edges completely to prevent Jell-O from seeping through."},
            {"step": 8, "text": "Refrigerate while preparing Jell-O layer."},
            {"step": 9, "text": "For Jell-O layer: Dissolve Jell-O in boiling water. Stir well."},
            {"step": 10, "text": "Stir in strawberries with their juices. Let cool until slightly thickened but still pourable."},
            {"step": 11, "text": "Gently pour Jell-O mixture over cream cheese layer."},
            {"step": 12, "text": "Refrigerate for at least 4-6 hours, or overnight, until completely set."},
            {"step": 13, "text": "Cut into squares and serve chilled."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch dish",
        "notes": [
            "Seal the cream cheese layer to the edges to prevent soggy crust",
            "Use the large 6 oz box of Jell-O, not the small 3 oz",
            "Despite the name, this is definitely a dessert, not a salad",
            "A Midwest and Southern holiday tradition since the 1960s",
            "Cool the pretzel crust completely before adding cream cheese",
            "Make a day ahead - it needs at least 4 hours to set"
        ],
        "tags": ["dessert", "Jell-O", "salad", "pretzel", "strawberry", "potluck", "1960s", "no-bake"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "peach-cobbler-dump-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Peach Cobbler Dump Cake",
        "category": "desserts",
        "attribution": "Vintage Dump Cake Recipe",
        "source_note": "Part of the dump cake phenomenon from the 1960s. Uses canned peaches and cake mix for a cobbler-like dessert with almost no effort. A church potluck and family reunion staple.",
        "description": "Canned peaches topped with dry cake mix and butter - that's it! The peaches bubble up and the butter melts down to create a golden, cobbler-like dessert. Serve warm with vanilla ice cream.",
        "servings_yield": "12-15 servings",
        "prep_time": "5 min",
        "cook_time": "45 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "canned sliced peaches", "quantity": "29", "unit": "oz can", "prep_note": "in heavy syrup, undrained"},
            {"item": "yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz, dry"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted (1 stick)"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "chopped pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 2, "text": "Pour the entire can of peaches with syrup into a 9x13-inch baking dish."},
            {"step": 3, "text": "Sprinkle cinnamon over the peaches."},
            {"step": 4, "text": "Sprinkle the dry cake mix evenly over the peaches. Do not stir."},
            {"step": 5, "text": "Drizzle melted butter evenly over the cake mix."},
            {"step": 6, "text": "Sprinkle pecans on top if using."},
            {"step": 7, "text": "Bake for 40-45 minutes until golden brown and bubbly around the edges."},
            {"step": 8, "text": "Let cool for 10-15 minutes before serving."},
            {"step": 9, "text": "Serve warm with vanilla ice cream or whipped cream."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch dish",
        "notes": [
            "Do NOT stir - the layers work together as they bake",
            "Peaches in heavy syrup work better than juice-packed",
            "Can substitute peach pie filling for even more sweetness",
            "Spice cake mix adds extra warmth to this dessert",
            "Best served warm when the peaches are bubbly",
            "A vintage dump cake that tastes like cobbler"
        ],
        "tags": ["dump cake", "peach", "cobbler", "cake mix", "vintage", "easy", "potluck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-pumpkin-roll",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Classic Pumpkin Roll",
        "category": "desserts",
        "attribution": "Libby's Pumpkin (1970s)",
        "source_note": "A retro classic that dates back to the 1970s, popularized by the Libby's Pumpkin label. Rolled once while warm to set the shape, then unrolled, filled with cream cheese, and rolled again. A Thanksgiving tradition.",
        "description": "A lightly spiced pumpkin cake rolled around a sweet, fluffy cream cheese filling. The trick is rolling it while warm, then again after filling. A beautiful and impressive Thanksgiving dessert that can be made ahead and frozen.",
        "servings_yield": "10-12 servings",
        "prep_time": "25 min",
        "cook_time": "15 min",
        "total_time": "40 min (plus chilling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "3/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground ginger", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground nutmeg", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "canned pumpkin puree", "quantity": "2/3", "unit": "cup", "prep_note": "not pumpkin pie filling"},
            {"item": "powdered sugar", "quantity": "1/4", "unit": "cup", "prep_note": "for towel"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened, for filling"},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "softened, for filling"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup", "prep_note": "for filling"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for filling"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F (190°C). Grease a 15x10-inch jelly roll pan and line with parchment paper."},
            {"step": 2, "text": "In a bowl, whisk together flour, baking powder, baking soda, cinnamon, ginger, nutmeg, and salt."},
            {"step": 3, "text": "In a large bowl, beat eggs and sugar until thick, about 3 minutes."},
            {"step": 4, "text": "Beat in pumpkin. Fold in dry ingredients until just combined."},
            {"step": 5, "text": "Spread batter evenly in prepared pan."},
            {"step": 6, "text": "Bake for 13-15 minutes until cake springs back when lightly touched."},
            {"step": 7, "text": "Sprinkle powdered sugar on a clean kitchen towel."},
            {"step": 8, "text": "Immediately turn warm cake onto towel. Remove parchment paper."},
            {"step": 9, "text": "Starting at the short end, roll up cake and towel together. Cool completely, seam side down."},
            {"step": 10, "text": "For filling: Beat cream cheese, butter, 1 cup powdered sugar, and vanilla until smooth."},
            {"step": 11, "text": "Carefully unroll cooled cake. Spread filling evenly, leaving a 1-inch border."},
            {"step": 12, "text": "Roll up cake again (without towel). Wrap tightly in plastic wrap."},
            {"step": 13, "text": "Refrigerate at least 1 hour before slicing. Dust with powdered sugar before serving."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "15x10-inch jelly roll pan",
        "notes": [
            "Rolling while warm prevents cracks when you re-roll with filling",
            "Use pure pumpkin puree, NOT pumpkin pie filling",
            "Can be made weeks ahead and frozen (wrap tightly)",
            "The powdered sugar on the towel prevents sticking",
            "A 1970s classic popularized by Libby's Pumpkin",
            "Thaw frozen rolls in the refrigerator overnight"
        ],
        "tags": ["cake", "pumpkin", "roll", "cream cheese", "Thanksgiving", "1970s", "Libby's", "fall"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chocolate-eclair-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chocolate Eclair Cake",
        "category": "desserts",
        "attribution": "1980s Church Potluck Classic",
        "source_note": "An old-fashioned no-bake icebox cake that became famous in the 1980s when recipes were shared in newspapers. Also known as Chocolate Eclair Dessert or Icebox Cake. Graham crackers soften into cake-like layers after chilling.",
        "description": "Layers of graham crackers and vanilla pudding that transform into a soft, cake-like dessert after chilling overnight. Topped with chocolate frosting. Tastes remarkably like a chocolate eclair with almost no effort.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "0 min",
        "total_time": "15 min (plus 24 hours chilling)",
        "ingredients": [
            {"item": "instant vanilla pudding mix", "quantity": "2", "unit": "boxes", "prep_note": "3.4 oz each"},
            {"item": "milk", "quantity": "3", "unit": "cups", "prep_note": "cold"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "graham crackers", "quantity": "1", "unit": "box", "prep_note": "about 27 whole rectangles"},
            {"item": "chocolate frosting", "quantity": "16", "unit": "oz", "prep_note": "store-bought tub"}
        ],
        "instructions": [
            {"step": 1, "text": "Whisk together pudding mixes and cold milk for 2 minutes until thick."},
            {"step": 2, "text": "Fold Cool Whip into the pudding mixture until well combined."},
            {"step": 3, "text": "Line the bottom of a 9x13-inch dish with a single layer of graham crackers, breaking some to fit."},
            {"step": 4, "text": "Spread half of the pudding mixture over the graham crackers."},
            {"step": 5, "text": "Add another layer of graham crackers."},
            {"step": 6, "text": "Spread remaining pudding mixture over the crackers."},
            {"step": 7, "text": "Top with a final layer of graham crackers."},
            {"step": 8, "text": "Microwave frosting for 15-20 seconds to make it spreadable. Spread over top layer of crackers."},
            {"step": 9, "text": "Cover and refrigerate for at least 24 hours - this is essential!"},
            {"step": 10, "text": "The graham crackers will soften into cake-like layers."}
        ],
        "temperature": "No bake",
        "pan_size": "9x13-inch dish",
        "notes": [
            "MUST chill for 24 hours - the crackers need time to soften",
            "Use instant pudding, not cook-and-serve",
            "The longer it chills, the softer and more cake-like it becomes",
            "Also called Icebox Cake or Chocolate Eclair Dessert",
            "Popular at church potlucks since the 1980s",
            "Can substitute homemade chocolate ganache for frosting"
        ],
        "tags": ["dessert", "no-bake", "eclair", "pudding", "graham cracker", "icebox", "1980s", "potluck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "puppy-chow-muddy-buddies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Puppy Chow (Muddy Buddies)",
        "category": "snacks",
        "attribution": "Chex / General Mills",
        "source_note": "A classic no-bake snack that's been on the back of Chex cereal boxes for decades. Officially called 'Muddy Buddies' by General Mills, but known as 'Puppy Chow' or 'Monkey Munch' in different regions. Perfect for parties and gifts.",
        "description": "Crispy Chex cereal coated in melted chocolate, peanut butter, and butter, then tossed in powdered sugar until every piece is covered in white. Addictively good and impossible to stop eating.",
        "servings_yield": "About 9 cups",
        "prep_time": "10 min",
        "cook_time": "0 min",
        "total_time": "10 min (plus cooling)",
        "ingredients": [
            {"item": "Rice Chex cereal", "quantity": "9", "unit": "cups"},
            {"item": "semisweet chocolate chips", "quantity": "1", "unit": "cup"},
            {"item": "creamy peanut butter", "quantity": "1/2", "unit": "cup"},
            {"item": "butter", "quantity": "1/4", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "powdered sugar", "quantity": "1 1/2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Measure cereal into a large bowl. Set aside."},
            {"step": 2, "text": "In a microwave-safe bowl, combine chocolate chips, peanut butter, and butter."},
            {"step": 3, "text": "Microwave on high for 1 minute. Stir. Microwave 30 seconds more if needed until smooth."},
            {"step": 4, "text": "Stir in vanilla extract."},
            {"step": 5, "text": "Pour chocolate mixture over cereal. Gently fold until all cereal is evenly coated."},
            {"step": 6, "text": "Put powdered sugar in a large zip-lock bag or paper grocery bag."},
            {"step": 7, "text": "Add the coated cereal to the bag. Seal and shake vigorously until all pieces are covered in powdered sugar."},
            {"step": 8, "text": "Spread on wax paper or parchment to cool and dry."},
            {"step": 9, "text": "Store in an airtight container at room temperature."}
        ],
        "temperature": "No bake",
        "notes": [
            "Officially called 'Muddy Buddies' by General Mills",
            "Also known as 'Puppy Chow' or 'Monkey Munch' in different regions",
            "Use regular peanut butter (Jif, Skippy) - not natural style",
            "Semisweet chips work better than milk chocolate (less sweet)",
            "The bag-shaking method is traditional and mess-free",
            "Stores at room temperature for up to a week"
        ],
        "tags": ["snack", "no-bake", "Chex", "chocolate", "peanut butter", "puppy chow", "muddy buddies", "party"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chocolate-delight-layered",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chocolate Delight",
        "category": "desserts",
        "attribution": "1970s Potluck Classic",
        "source_note": "A beloved 1970s layered dessert with many names: Chocolate Lush, Robert Redford Dessert, Better Than Robert Redford, or Four-Layer Dessert. The pecan shortbread crust is the signature feature. A summer potluck staple for 50+ years.",
        "description": "Four layers of pure indulgence: a buttery pecan shortbread crust, fluffy cream cheese layer, rich chocolate pudding, and billowy Cool Whip topping. Also known as Robert Redford Dessert because it's almost too good to be true.",
        "servings_yield": "12-16 servings",
        "prep_time": "25 min",
        "cook_time": "20 min",
        "total_time": "45 min (plus 4 hours chilling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "1", "unit": "cup", "prep_note": "for crust"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened, for crust"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "divided"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup"},
            {"item": "Cool Whip", "quantity": "16", "unit": "oz", "prep_note": "divided"},
            {"item": "instant chocolate pudding mix", "quantity": "2", "unit": "boxes", "prep_note": "3.4 oz each"},
            {"item": "milk", "quantity": "3", "unit": "cups", "prep_note": "cold"},
            {"item": "chocolate shavings", "quantity": "2", "unit": "tbsp", "prep_note": "for garnish, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 2, "text": "For crust: Mix flour, softened butter, and 3/4 cup pecans until crumbly."},
            {"step": 3, "text": "Press into the bottom of a 9x13-inch baking pan."},
            {"step": 4, "text": "Bake for 18-20 minutes until golden. Cool completely."},
            {"step": 5, "text": "For cream cheese layer: Beat cream cheese and powdered sugar until smooth."},
            {"step": 6, "text": "Fold in 1 cup (half of one container) of Cool Whip."},
            {"step": 7, "text": "Spread over cooled crust."},
            {"step": 8, "text": "For pudding layer: Whisk pudding mixes with cold milk for 2 minutes until thick."},
            {"step": 9, "text": "Spread pudding over cream cheese layer immediately."},
            {"step": 10, "text": "Spread remaining Cool Whip over pudding layer."},
            {"step": 11, "text": "Sprinkle with remaining 1/4 cup pecans and chocolate shavings."},
            {"step": 12, "text": "Refrigerate for at least 4 hours before serving."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Also known as Chocolate Lush, Robert Redford Dessert, or Four-Layer Dessert",
            "The pecan shortbread crust is the signature feature",
            "Use instant pudding, not cook-and-serve",
            "Must be refrigerated - the Cool Whip won't hold at room temperature",
            "A potluck favorite for over 50 years",
            "Can make lemon or butterscotch versions with different pudding flavors"
        ],
        "tags": ["dessert", "chocolate", "layered", "pudding", "cream cheese", "pecans", "1970s", "potluck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pistachio-fluff-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pistachio Fluff Salad",
        "category": "desserts",
        "attribution": "Jell-O / 1970s Watergate Era",
        "source_note": "Also known as Watergate Salad, Green Stuff, or Green Goop. Made possible when Jell-O released pistachio pudding mix in 1976. Part of the 1970s 'Watergate' dessert craze - 'because it's full of nuts and covered up!'",
        "description": "A fluffy pale green 'salad' made with pistachio pudding, crushed pineapple, marshmallows, and Cool Whip. Sweet, fluffy, and impossibly easy. Also called Watergate Salad or simply 'the green stuff' at family gatherings.",
        "servings_yield": "8-10 servings",
        "prep_time": "5 min",
        "cook_time": "0 min",
        "total_time": "5 min (plus 2 hours chilling)",
        "ingredients": [
            {"item": "instant pistachio pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "crushed pineapple", "quantity": "20", "unit": "oz can", "prep_note": "undrained - use the juice!"},
            {"item": "miniature marshmallows", "quantity": "1 1/2", "unit": "cups"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "chopped walnuts or pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, combine dry pistachio pudding mix with the entire can of crushed pineapple including the juice."},
            {"step": 2, "text": "Stir until pudding is dissolved and mixture begins to thicken."},
            {"step": 3, "text": "Fold in the Cool Whip until well combined."},
            {"step": 4, "text": "Fold in the miniature marshmallows and nuts if using."},
            {"step": 5, "text": "Cover and refrigerate for at least 2 hours to allow marshmallows to soften."},
            {"step": 6, "text": "Serve chilled. Keeps refrigerated for up to 3 days."}
        ],
        "temperature": "No bake",
        "notes": [
            "Do NOT drain the pineapple - the juice is essential!",
            "Must use INSTANT pudding mix, not cook-and-serve",
            "Also called Watergate Salad, Green Stuff, or Pistachio Delight",
            "Part of the 1970s Watergate dessert craze",
            "The marshmallows absorb liquid and soften as it chills",
            "Can add 1 cup shredded coconut or 8 oz cream cheese for variations"
        ],
        "tags": ["salad", "fluff", "pistachio", "Watergate", "1970s", "no-bake", "marshmallow", "Cool Whip"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "old-fashioned-butterscotch-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Butterscotch Pie",
        "category": "desserts",
        "attribution": "Traditional American / Sarah Wheeler (1904)",
        "source_note": "Legend has it that Sarah Wheeler invented this pie in Connersville, Indiana, in 1904. A 'desperation pie' made from pantry staples in winter when fruit wasn't available. Brown sugar gives it a deeper, richer flavor than caramel.",
        "description": "A rich, creamy brown sugar custard pie topped with billowy meringue. Butterscotch is made with brown sugar (not white like caramel), giving it a deep, complex sweetness. A 'desperation pie' from the days before refrigeration.",
        "servings_yield": "8 servings",
        "prep_time": "25 min",
        "cook_time": "20 min",
        "total_time": "45 min (plus cooling)",
        "ingredients": [
            {"item": "9-inch pie crust", "quantity": "1", "unit": "", "prep_note": "prebaked and cooled"},
            {"item": "dark brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "all-purpose flour", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "milk", "quantity": "2", "unit": "cups"},
            {"item": "egg yolks", "quantity": "3", "unit": "large", "prep_note": "reserve whites for meringue"},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "egg whites", "quantity": "3", "unit": "large", "prep_note": "for meringue"},
            {"item": "cream of tartar", "quantity": "1/4", "unit": "tsp", "prep_note": "for meringue"},
            {"item": "sugar", "quantity": "6", "unit": "tbsp", "prep_note": "for meringue"}
        ],
        "instructions": [
            {"step": 1, "text": "In a heavy saucepan, whisk together brown sugar, flour, and salt."},
            {"step": 2, "text": "Gradually whisk in milk until smooth."},
            {"step": 3, "text": "Cook over medium heat, stirring constantly, until mixture thickens and begins to bubble."},
            {"step": 4, "text": "In a small bowl, whisk egg yolks. Temper by slowly adding 1/2 cup of hot mixture while whisking."},
            {"step": 5, "text": "Pour tempered yolks back into saucepan, whisking constantly."},
            {"step": 6, "text": "Continue cooking and stirring for 2 more minutes until very thick."},
            {"step": 7, "text": "Remove from heat. Stir in butter and vanilla."},
            {"step": 8, "text": "Keep filling hot while making meringue (prevents weeping)."},
            {"step": 9, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 10, "text": "For meringue: Beat egg whites and cream of tartar until soft peaks form."},
            {"step": 11, "text": "Gradually add sugar, beating until stiff glossy peaks form."},
            {"step": 12, "text": "Pour hot filling into prebaked pie crust."},
            {"step": 13, "text": "Immediately spread meringue over hot filling, sealing to the crust edges."},
            {"step": 14, "text": "Bake for 10-15 minutes until meringue is golden brown."},
            {"step": 15, "text": "Cool completely before slicing."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9-inch pie plate",
        "notes": [
            "Butterscotch uses brown sugar; caramel uses white sugar",
            "Keep filling hot when adding meringue to prevent weeping",
            "Seal meringue to the crust edges to prevent shrinking",
            "A 'desperation pie' made when winter fruit wasn't available",
            "Legend credits Sarah Wheeler of Indiana, 1904",
            "Dark brown sugar gives the deepest butterscotch flavor"
        ],
        "tags": ["pie", "butterscotch", "meringue", "brown sugar", "vintage", "1904", "desperation pie"],
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
