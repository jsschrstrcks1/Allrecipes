#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 7) - dump cakes, candy, and classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "vintage-cherry-pineapple-dump-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cherry Pineapple Dump Cake",
        "category": "desserts",
        "attribution": "Duncan Hines / Vintage 1960s Recipe",
        "source_note": "A classic dump cake from the 1960s that became a staple at church potlucks and family gatherings. The original 'dump and bake' dessert.",
        "description": "The original dump cake - cherry pie filling and crushed pineapple topped with dry cake mix and butter. No mixing required, just dump everything in and bake. A busy mom's dream since the 1960s.",
        "servings_yield": "12-15 servings",
        "prep_time": "5 min",
        "cook_time": "45 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "crushed pineapple", "quantity": "20", "unit": "oz can", "prep_note": "with juice, undrained"},
            {"item": "cherry pie filling", "quantity": "21", "unit": "oz can"},
            {"item": "yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz, dry"},
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "cold, sliced thin (2 sticks)"},
            {"item": "chopped pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). No need to grease the pan."},
            {"step": 2, "text": "Dump the entire can of crushed pineapple with juice into a 9x13 inch baking dish. Spread evenly."},
            {"step": 3, "text": "Dump the cherry pie filling over the pineapple. Spread gently to cover."},
            {"step": 4, "text": "Sprinkle the dry cake mix evenly over the fruit layers. Do not stir."},
            {"step": 5, "text": "Arrange thin slices of cold butter evenly over the cake mix, covering as much as possible."},
            {"step": 6, "text": "Sprinkle pecans on top if using."},
            {"step": 7, "text": "Bake for 40-45 minutes until the top is golden brown and the filling is bubbling around the edges."},
            {"step": 8, "text": "Let cool for 15-20 minutes before serving. The filling will be very hot."},
            {"step": 9, "text": "Serve warm, plain or with vanilla ice cream or whipped cream."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "The original dump cake - this is where it all started",
            "Do NOT stir the layers - the magic happens as it bakes",
            "Cold butter works better than melted for even coverage",
            "Can substitute other pie fillings: blueberry, apple, peach",
            "Became a church potluck staple in the 1960s-70s",
            "Some vintage recipes add shredded coconut to the pecans"
        ],
        "tags": ["dump cake", "vintage", "1960s", "church potluck", "no-mix", "cherry", "pineapple", "easy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mamie-eisenhower-million-dollar-fudge",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mamie Eisenhower's Million Dollar Fudge",
        "category": "desserts",
        "attribution": "First Lady Mamie Eisenhower / White House Recipe",
        "source_note": "The famous fudge recipe that Mamie Eisenhower brought to the White House. President Eisenhower reportedly called it 'million dollar' fudge because it was so creamy. Original recipe from the Eisenhower Presidential Library.",
        "description": "The famous White House fudge recipe from First Lady Mamie Eisenhower. Ultra-creamy chocolate fudge made with marshmallow creme and two kinds of chocolate. President Ike's favorite sweet treat.",
        "servings_yield": "5-6 pounds (about 100 pieces)",
        "prep_time": "15 min",
        "cook_time": "15 min",
        "total_time": "30 min (plus cooling)",
        "ingredients": [
            {"item": "sugar", "quantity": "4 1/2", "unit": "cups"},
            {"item": "butter", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "pinch"},
            {"item": "evaporated milk", "quantity": "12", "unit": "oz can", "prep_note": "1 tall can"},
            {"item": "semisweet chocolate chips", "quantity": "12", "unit": "oz"},
            {"item": "German sweet chocolate", "quantity": "12", "unit": "oz", "prep_note": "broken into pieces"},
            {"item": "marshmallow creme", "quantity": "1", "unit": "pint", "prep_note": "7 oz jar, like Marshmallow Fluff"},
            {"item": "chopped walnuts or pecans", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large heavy-bottomed saucepan, combine sugar, butter, salt, and evaporated milk."},
            {"step": 2, "text": "Heat over medium-low heat, stirring constantly until sugar dissolves."},
            {"step": 3, "text": "Bring to a rolling boil. Boil for exactly 6 minutes, stirring constantly. (7 minutes for firmer fudge.)"},
            {"step": 4, "text": "While syrup boils, place chocolate chips, German chocolate, marshmallow creme, and nuts in a large heatproof bowl."},
            {"step": 5, "text": "Pour the boiling syrup over the chocolate mixture immediately."},
            {"step": 6, "text": "Beat vigorously until the chocolate is completely melted and mixture is smooth."},
            {"step": 7, "text": "Pour into a buttered 11x16-inch jellyroll pan (or two 9x13 pans)."},
            {"step": 8, "text": "Let stand at room temperature for several hours until completely set."},
            {"step": 9, "text": "Cut into 1-inch squares."}
        ],
        "temperature": "Stovetop",
        "notes": [
            "The original recipe specifies boiling for exactly 6 minutes - timing is crucial",
            "Also known as White House Fudge, Mrs. Eisenhower's Fudge",
            "Mamie's original note: 'It is better the second day'",
            "Store in a tin box in a cool place - keeps up to 6 months",
            "Original recipe from the Eisenhower Presidential Library archives",
            "President Ike was the cook in the family, but Mamie was known for this fudge"
        ],
        "tags": ["fudge", "candy", "White House", "1950s", "Mamie Eisenhower", "chocolate", "vintage", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bisquick-impossible-coconut-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Impossible Coconut Pie",
        "category": "desserts",
        "attribution": "Betty Crocker / Bisquick (1983)",
        "source_note": "Originally published by General Mills in October 1983. The 'impossible' pie trend took off in the 1970s-80s thanks to Bisquick. The pie magically creates its own crust while baking.",
        "description": "A self-crusting miracle pie that creates three layers as it bakes: a crust on the bottom, custard in the middle, and toasted coconut on top. One of Bisquick's most legendary recipes.",
        "servings_yield": "8 servings",
        "prep_time": "10 min",
        "cook_time": "50 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "flaked sweetened coconut", "quantity": "1", "unit": "cup"},
            {"item": "sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "Bisquick mix", "quantity": "1/2", "unit": "cup"},
            {"item": "butter", "quantity": "1/4", "unit": "cup", "prep_note": "melted"},
            {"item": "milk", "quantity": "2", "unit": "cups"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1 1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9-inch pie plate."},
            {"step": 2, "text": "Place all ingredients in a blender. Cover and blend on high speed for 15 seconds."},
            {"step": 3, "text": "Alternatively, beat all ingredients with a hand mixer until well combined."},
            {"step": 4, "text": "Pour mixture into the prepared pie plate."},
            {"step": 5, "text": "Let sit for 5 minutes to allow the Bisquick to settle (this helps form the crust)."},
            {"step": 6, "text": "Bake for 45-50 minutes until golden brown and a knife inserted in the center comes out clean."},
            {"step": 7, "text": "Cool before serving. Store leftovers in the refrigerator."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "The 'impossible' name comes from the crust magically forming on its own",
            "As it bakes, it creates 3 layers: crust, custard, and coconut topping",
            "Let the batter rest 5 minutes before baking for best crust formation",
            "Shredded coconut works too, though flaked is traditional",
            "This is a custard pie - must be refrigerated after cooling",
            "One of Betty Crocker's most requested vintage recipes"
        ],
        "tags": ["pie", "coconut", "Bisquick", "1980s", "self-crusting", "impossible pie", "vintage", "easy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "old-fashioned-peanut-brittle",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Peanut Brittle",
        "category": "desserts",
        "attribution": "Traditional American Candy",
        "source_note": "Classic stovetop peanut brittle recipe passed down through generations. A holiday candy-making tradition using simple ingredients and a candy thermometer.",
        "description": "Crispy, buttery, sweet-and-salty peanut brittle made the old-fashioned way on the stovetop. The baking soda creates that signature light, airy texture. A Christmas candy classic.",
        "servings_yield": "About 2 pounds",
        "prep_time": "10 min",
        "cook_time": "20 min",
        "total_time": "30 min (plus 1-2 hours cooling)",
        "ingredients": [
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "light corn syrup", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "raw peanuts", "quantity": "2", "unit": "cups", "prep_note": "Spanish peanuts preferred, unsalted"},
            {"item": "butter", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "if using unsalted peanuts"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Butter a large baking sheet or line with a silicone mat. Have all ingredients measured and ready."},
            {"step": 2, "text": "In a large heavy-bottomed saucepan, combine sugar, corn syrup, and water."},
            {"step": 3, "text": "Cook over medium heat, stirring occasionally, until mixture reaches 245°F (soft ball stage)."},
            {"step": 4, "text": "Stir in peanuts, butter, and salt. Continue cooking, stirring frequently."},
            {"step": 5, "text": "Cook until mixture reaches 300°F (hard crack stage). The mixture will turn golden and the peanuts will start to smell roasted."},
            {"step": 6, "text": "Remove from heat immediately. Working quickly, stir in baking soda and vanilla."},
            {"step": 7, "text": "The mixture will foam up and become lighter in color. This is the baking soda creating air pockets."},
            {"step": 8, "text": "Immediately pour onto prepared baking sheet. Using a buttered spatula, spread as thin as possible."},
            {"step": 9, "text": "Let cool completely, 1-2 hours, until hard and brittle."},
            {"step": 10, "text": "Break into irregular pieces. Store in an airtight container."}
        ],
        "temperature": "Stovetop to 300°F (hard crack)",
        "notes": [
            "A candy thermometer is essential - too hot and it burns, too cool and it won't set",
            "Spanish peanuts (small, red-skinned) are traditional for authentic brittle",
            "The baking soda creates the light, airy texture - don't skip it",
            "Work quickly once you remove from heat - the candy sets fast",
            "Be very careful - the candy mixture is extremely hot",
            "Stores at room temperature in airtight container for up to a month"
        ],
        "tags": ["candy", "peanut brittle", "holiday", "Christmas", "stovetop", "vintage", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "new-orleans-pecan-pralines",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "New Orleans Pecan Pralines",
        "category": "desserts",
        "attribution": "Traditional New Orleans / Louisiana Recipe",
        "source_note": "Pralines have been a New Orleans signature treat since the 1700s, introduced by French settlers. Louisiana pecans replaced the original French almonds. June 24th is National Praline Day.",
        "description": "Authentic New Orleans pralines - buttery, creamy pecan candies that melt in your mouth. Made with brown sugar, butter, and toasted pecans the way they've been made in Louisiana since the 1700s. Pronounced 'PRAH-leens' in Louisiana.",
        "servings_yield": "About 24 pralines",
        "prep_time": "10 min",
        "cook_time": "15 min",
        "total_time": "25 min (plus cooling)",
        "ingredients": [
            {"item": "granulated sugar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "light brown sugar", "quantity": "3/4", "unit": "cup", "prep_note": "packed"},
            {"item": "whole milk", "quantity": "1/2", "unit": "cup"},
            {"item": "butter", "quantity": "6", "unit": "tbsp"},
            {"item": "pecan halves", "quantity": "1 1/2", "unit": "cups", "prep_note": "toasted"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast pecans at 275°F for 20-25 minutes until fragrant and slightly browned. Set aside."},
            {"step": 2, "text": "Line baking sheets with parchment paper or silicone mats."},
            {"step": 3, "text": "Combine both sugars, milk, and butter in a medium heavy-bottomed saucepan."},
            {"step": 4, "text": "Cook over medium heat, stirring constantly, until mixture reaches 238-240°F (soft ball stage)."},
            {"step": 5, "text": "Remove from heat. Stir in vanilla and toasted pecans."},
            {"step": 6, "text": "Stir constantly until mixture becomes creamy and cloudy, and the pecans stay suspended in the mixture (about 2-3 minutes)."},
            {"step": 7, "text": "Working quickly, drop by spoonfuls onto prepared baking sheets."},
            {"step": 8, "text": "Let cool completely until set. Pralines should be firm but not too hard."}
        ],
        "temperature": "Stovetop to 238-240°F (soft ball)",
        "notes": [
            "Pronounced 'PRAH-leens' in Louisiana, not 'PRAY-leens'",
            "The perfect praline should be crisp and melt in your mouth, not chewy",
            "Humidity affects candy-making - avoid making these on rainy or very humid days",
            "Toasting the pecans first makes a big difference in flavor",
            "Named for French Marshal Comte du Plessis Praslin (1598-1675)",
            "Original French pralines used almonds; Louisiana adapted with native pecans"
        ],
        "tags": ["pralines", "candy", "New Orleans", "Louisiana", "pecans", "Southern", "French", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-apple-dump-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Apple Dump Cake",
        "category": "desserts",
        "attribution": "Vintage 1960s Recipe",
        "source_note": "Part of the dump cake phenomenon that started in the mid-1960s. This apple version uses applesauce and apple pie filling for maximum apple flavor.",
        "description": "A warm, comforting apple dessert that tastes like apple pie without any of the work. Layers of applesauce and apple pie filling topped with spice cake mix and butter. Pure apple comfort.",
        "servings_yield": "12-15 servings",
        "prep_time": "5 min",
        "cook_time": "50 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "applesauce", "quantity": "15", "unit": "oz jar", "prep_note": "unsweetened or sweetened"},
            {"item": "apple pie filling", "quantity": "21", "unit": "oz can"},
            {"item": "spice cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz, dry (or yellow cake mix)"},
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "cold, sliced thin (2 sticks)"},
            {"item": "chopped walnuts or pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp", "prep_note": "optional, for topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). No need to grease the pan."},
            {"step": 2, "text": "Spread applesauce evenly in the bottom of a 9x13 inch baking dish."},
            {"step": 3, "text": "Spoon apple pie filling over the applesauce and spread gently."},
            {"step": 4, "text": "Sprinkle the entire box of dry cake mix evenly over the fruit layers."},
            {"step": 5, "text": "If using yellow cake mix, sprinkle cinnamon over the top."},
            {"step": 6, "text": "Arrange thin slices of cold butter over the cake mix, covering as completely as possible."},
            {"step": 7, "text": "Sprinkle nuts on top if desired."},
            {"step": 8, "text": "Bake for 45-50 minutes until the top is golden brown and the filling is bubbling."},
            {"step": 9, "text": "Let cool for 15 minutes. Serve warm with vanilla ice cream or whipped cream."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Spice cake mix is traditional, but yellow cake mix with added cinnamon works too",
            "The applesauce layer adds extra moisture and apple flavor",
            "Do NOT mix or stir - the layers bake together perfectly",
            "Original recipes called for thin slices of cold butter, not melted",
            "Can add caramel sauce drizzle after baking for extra decadence"
        ],
        "tags": ["dump cake", "apple", "vintage", "1960s", "easy", "fall", "no-mix"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "grandma-sea-foam-candy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grandma's Sea Foam Candy",
        "category": "desserts",
        "attribution": "Traditional American Candy / Vintage Family Recipe",
        "source_note": "Sea foam candy is similar to divinity but made with brown sugar instead of white, and traditionally without corn syrup. A lighter, airier alternative that dates back generations.",
        "description": "A light, melt-in-your-mouth candy similar to divinity but made with brown sugar for a caramel-like flavor. No corn syrup needed. An old-fashioned treat that's naturally dairy-free.",
        "servings_yield": "About 36 pieces",
        "prep_time": "15 min",
        "cook_time": "15 min",
        "total_time": "30 min (plus setting time)",
        "ingredients": [
            {"item": "light brown sugar", "quantity": "2", "unit": "cups", "prep_note": "packed"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "white vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "egg whites", "quantity": "2", "unit": "large", "prep_note": "at room temperature"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "chopped pecans or walnuts", "quantity": "1", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Line baking sheets with parchment paper or wax paper."},
            {"step": 2, "text": "In a heavy saucepan, combine brown sugar, water, and vinegar."},
            {"step": 3, "text": "Cook over medium heat, stirring until sugar dissolves."},
            {"step": 4, "text": "Continue cooking without stirring until mixture reaches 260°F (hard ball stage)."},
            {"step": 5, "text": "While syrup cooks, beat egg whites in a stand mixer until stiff peaks form."},
            {"step": 6, "text": "With mixer running on high, slowly pour hot syrup in a thin stream into the beaten egg whites."},
            {"step": 7, "text": "Continue beating until mixture loses its gloss and holds its shape when dropped from a spoon, about 5-8 minutes."},
            {"step": 8, "text": "Quickly fold in vanilla and nuts if using."},
            {"step": 9, "text": "Drop by spoonfuls onto prepared baking sheets."},
            {"step": 10, "text": "Let stand until set, about 30 minutes to 1 hour."}
        ],
        "temperature": "Stovetop to 260°F (hard ball)",
        "notes": [
            "Sea foam uses brown sugar; divinity uses white sugar and corn syrup",
            "The vinegar helps prevent crystallization - don't skip it",
            "Humidity is the enemy - make this on a cool, dry day",
            "If mixture gets too stiff to drop, add a few drops of hot water",
            "A stand mixer makes this much easier and safer than hand beating",
            "Naturally fat-free (without the nuts) and corn-syrup-free"
        ],
        "tags": ["candy", "sea foam", "divinity", "brown sugar", "vintage", "holiday", "no corn syrup"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sock-it-to-me-cake-1970s",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sock-It-To-Me Cake (1970s)",
        "category": "desserts",
        "attribution": "Duncan Hines (1970s) / Vintage Cake Mix Recipe",
        "source_note": "First published on the back of Duncan Hines Butter Golden Cake Mix in the 1970s. Named after the popular 1960s-70s catchphrase meaning 'lay it on me.' A Southern kitchen staple.",
        "description": "A rich, moist bundt cake with a hidden ribbon of cinnamon, brown sugar, and pecans running through the middle. A clever fusion of pound cake and coffee cake that took the 1970s by storm.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "45 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "yellow or butter golden cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "sour cream", "quantity": "1", "unit": "cup"},
            {"item": "vegetable oil", "quantity": "1/3", "unit": "cup"},
            {"item": "sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "water", "quantity": "1/4", "unit": "cup"},
            {"item": "brown sugar", "quantity": "2", "unit": "tbsp", "prep_note": "packed, for filling"},
            {"item": "ground cinnamon", "quantity": "2", "unit": "tsp", "prep_note": "for filling"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "for filling"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup", "prep_note": "for glaze"},
            {"item": "milk", "quantity": "2", "unit": "tbsp", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F (190°C). Grease and flour a 10-inch bundt pan."},
            {"step": 2, "text": "In a small bowl, mix together brown sugar, cinnamon, and pecans for the filling. Set aside."},
            {"step": 3, "text": "In a large bowl, combine cake mix, sour cream, oil, sugar, eggs, and water."},
            {"step": 4, "text": "Beat with an electric mixer on medium speed for 2 minutes until smooth."},
            {"step": 5, "text": "Pour 2/3 of the batter into the prepared bundt pan."},
            {"step": 6, "text": "Sprinkle the cinnamon-pecan filling evenly over the batter."},
            {"step": 7, "text": "Carefully pour the remaining batter over the filling."},
            {"step": 8, "text": "Bake for 40-45 minutes, or until a toothpick inserted in the center comes out clean."},
            {"step": 9, "text": "Cool in pan for 10 minutes, then invert onto a serving plate."},
            {"step": 10, "text": "While cake is still warm, whisk together powdered sugar and milk for glaze."},
            {"step": 11, "text": "Drizzle glaze over the warm cake."}
        ],
        "temperature": "375°F (190°C)",
        "pan_size": "10-inch bundt pan",
        "notes": [
            "The bundt pan shape is essential to a true Sock-It-To-Me Cake",
            "The sour cream makes this incredibly moist - don't substitute",
            "Named after the popular 1960s catchphrase from 'Laugh-In'",
            "Original recipe was printed on Duncan Hines cake mix boxes",
            "The hidden cinnamon-pecan swirl is the 'secret' inside",
            "A Southern potluck favorite since the 1970s"
        ],
        "tags": ["cake", "bundt", "1970s", "Duncan Hines", "cinnamon", "pecans", "vintage", "Southern"],
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
