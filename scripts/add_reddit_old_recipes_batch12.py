#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 12) - boozy cakes, fluff salads, and cookie jar classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "bacardi-rum-cake-1970s",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bacardi Rum Cake (1970s Original)",
        "category": "desserts",
        "attribution": "Bacardi / 1970s Advertisement Recipe",
        "source_note": "The original Bacardi Rum Cake recipe from their 1970s advertisements. First appeared around 1971 in magazine ads for Bacardi Dark Rum. Became a holiday staple and the definitive boozy bundt cake.",
        "description": "The legendary 1970s rum cake that launched a thousand holiday parties. A moist yellow cake studded with walnuts and soaked in a buttery rum glaze. Better the next day when the rum really sinks in.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "1 hour",
        "total_time": "1 hour 15 min",
        "ingredients": [
            {"item": "chopped walnuts or pecans", "quantity": "1", "unit": "cup"},
            {"item": "yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "instant vanilla pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "cold water", "quantity": "1/2", "unit": "cup"},
            {"item": "vegetable oil", "quantity": "1/2", "unit": "cup"},
            {"item": "dark rum", "quantity": "1/2", "unit": "cup", "prep_note": "Bacardi preferred"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "water", "quantity": "1/4", "unit": "cup", "prep_note": "for glaze"},
            {"item": "sugar", "quantity": "1", "unit": "cup", "prep_note": "for glaze"},
            {"item": "dark rum", "quantity": "1/2", "unit": "cup", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F (165°C). Grease and flour a 10-inch tube pan or 12-cup bundt pan."},
            {"step": 2, "text": "Sprinkle chopped nuts evenly over the bottom of the prepared pan."},
            {"step": 3, "text": "In a large bowl, combine cake mix, pudding mix, eggs, water, oil, and 1/2 cup rum."},
            {"step": 4, "text": "Beat on medium speed for 2 minutes until smooth."},
            {"step": 5, "text": "Pour batter over the nuts in the pan."},
            {"step": 6, "text": "Bake for 1 hour until a toothpick inserted in center comes out clean."},
            {"step": 7, "text": "Cool cake in pan while making glaze."},
            {"step": 8, "text": "For glaze: Melt butter in a saucepan. Stir in water and sugar."},
            {"step": 9, "text": "Boil for 5 minutes, stirring constantly."},
            {"step": 10, "text": "Remove from heat and carefully stir in 1/2 cup rum (it may sputter)."},
            {"step": 11, "text": "Poke holes all over the warm cake with a skewer."},
            {"step": 12, "text": "Slowly spoon and brush glaze over the cake, allowing it to absorb between additions."},
            {"step": 13, "text": "Let cake sit in pan for 30 minutes, then invert onto serving plate."}
        ],
        "temperature": "325°F (165°C)",
        "pan_size": "10-inch tube or 12-cup bundt pan",
        "notes": [
            "Original recipe from Bacardi advertisements, circa 1971",
            "Modern cake mixes are smaller (15.25 oz vs original 18.5 oz)",
            "For authentic texture, some add 3.25 oz extra cake mix",
            "Better the next day - the rum glaze continues to soak in",
            "Store tightly covered at room temperature",
            "A full cup of rum total makes this a serious adult dessert"
        ],
        "tags": ["cake", "bundt", "rum", "Bacardi", "1970s", "boozy", "holiday", "walnuts"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "orange-fluff-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Orange Fluff Salad (Orange Stuff)",
        "category": "desserts",
        "attribution": "1970s Midwest Classic",
        "source_note": "A classic Midwest 'fluff salad' that became trendy in the 1970s after Cool Whip was introduced in 1966. Also called Orange Stuff, Mandarin Orange Salad, or Orange Dream Salad. Sweet, creamy, and loaded with fruit.",
        "description": "A fluffy, creamy 'salad' with orange Jell-O, mandarin oranges, crushed pineapple, cottage cheese, and Cool Whip. Called a salad but definitely a dessert. A Midwest potluck staple since the 1970s.",
        "servings_yield": "10-12 servings",
        "prep_time": "10 min",
        "cook_time": "0 min",
        "total_time": "10 min (plus 2 hours chilling)",
        "ingredients": [
            {"item": "orange Jell-O", "quantity": "1", "unit": "box", "prep_note": "3 oz, dry powder"},
            {"item": "cottage cheese", "quantity": "2", "unit": "cups", "prep_note": "small curd"},
            {"item": "mandarin oranges", "quantity": "15", "unit": "oz can", "prep_note": "drained"},
            {"item": "crushed pineapple", "quantity": "20", "unit": "oz can", "prep_note": "drained"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "miniature marshmallows", "quantity": "1", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, sprinkle dry Jell-O powder over cottage cheese."},
            {"step": 2, "text": "Stir to combine - the Jell-O will dissolve into the cottage cheese."},
            {"step": 3, "text": "Fold in drained mandarin oranges and drained pineapple."},
            {"step": 4, "text": "Gently fold in Cool Whip until well combined."},
            {"step": 5, "text": "Fold in marshmallows if using."},
            {"step": 6, "text": "Cover and refrigerate for at least 2 hours before serving."},
            {"step": 7, "text": "Serve cold. Keeps refrigerated for 3-4 days."}
        ],
        "temperature": "No cook",
        "notes": [
            "Use DRY Jell-O powder - don't prepare it with water",
            "The Jell-O dissolves into the cottage cheese for flavor",
            "Drain the fruit well to prevent watery salad",
            "Also known as Orange Stuff, Mandarin Fluff, or Orange Dream",
            "Became popular after Cool Whip was introduced in 1966",
            "A Midwest potluck staple for decades"
        ],
        "tags": ["salad", "fluff", "orange", "Jell-O", "cottage cheese", "1970s", "Midwest", "no-cook"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-ranger-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ranger Cookies",
        "category": "desserts",
        "attribution": "Traditional American / 1940s-1950s",
        "source_note": "An American classic since the 1940s, named for their hearty, trail-worthy ingredients. Also called Texas Ranger Cookies, Cowboy Cookies, or Kitchen Sink Cookies. Loaded with oats, coconut, cornflakes (or rice cereal), and sometimes chocolate chips.",
        "description": "Hearty, chewy cookies packed with oats, coconut, and crispy cereal. Named for Texas Rangers or cowboys who needed filling trail snacks. Every bite has a different texture - chewy oats, crispy cereal, sweet coconut.",
        "servings_yield": "About 48 cookies",
        "prep_time": "20 min",
        "cook_time": "12 min per batch",
        "total_time": "45 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened"},
            {"item": "granulated sugar", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "baking powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "old-fashioned rolled oats", "quantity": "2", "unit": "cups"},
            {"item": "sweetened flaked coconut", "quantity": "1", "unit": "cup"},
            {"item": "crispy rice cereal", "quantity": "2", "unit": "cups", "prep_note": "or crushed cornflakes"},
            {"item": "chocolate chips", "quantity": "1", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Line baking sheets with parchment paper."},
            {"step": 2, "text": "In a large bowl, cream butter and both sugars until light and fluffy."},
            {"step": 3, "text": "Beat in eggs and vanilla."},
            {"step": 4, "text": "In another bowl, whisk together flour, baking soda, baking powder, and salt."},
            {"step": 5, "text": "Gradually add dry ingredients to wet, mixing until combined."},
            {"step": 6, "text": "Stir in oats, coconut, and cereal. Add chocolate chips if using."},
            {"step": 7, "text": "Drop rounded tablespoons of dough 2 inches apart onto prepared sheets."},
            {"step": 8, "text": "Bake for 10-12 minutes until edges are golden but centers look slightly underdone."},
            {"step": 9, "text": "Cool on baking sheet 5 minutes before transferring to wire rack."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Named for Texas Rangers or cowboys who needed hearty trail snacks",
            "Also known as Cowboy Cookies or Kitchen Sink Cookies",
            "Original recipes used cornflakes; rice cereal is a popular substitute",
            "Adding chocolate chips is a modern variation",
            "Each cookie has oats, coconut, AND cereal for varied texture",
            "Don't overbake - they firm up as they cool"
        ],
        "tags": ["cookies", "ranger", "oats", "coconut", "cereal", "1940s", "cowboy", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-pecan-sandies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pecan Sandies",
        "category": "desserts",
        "attribution": "Traditional American Shortbread Cookie",
        "source_note": "A buttery, crumbly shortbread cookie studded with pecans. Keebler made them famous commercially, but homemade versions have been in family recipe boxes for generations. Sometimes called Sand Tarts or Pecan Butter Cookies.",
        "description": "Buttery, melt-in-your-mouth shortbread cookies studded with chopped pecans. The signature sandy, crumbly texture comes from the high butter-to-flour ratio and minimal mixing. Way better than store-bought.",
        "servings_yield": "About 36 cookies",
        "prep_time": "15 min",
        "cook_time": "15 min per batch",
        "total_time": "45 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened (2 sticks)"},
            {"item": "powdered sugar", "quantity": "1/3", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tbsp"},
            {"item": "water", "quantity": "1", "unit": "tbsp"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "finely chopped"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F (165°C). Line baking sheets with parchment paper."},
            {"step": 2, "text": "In a large bowl, beat butter and powdered sugar until light and fluffy."},
            {"step": 3, "text": "Beat in vanilla and water."},
            {"step": 4, "text": "Add flour and salt. Mix until just combined - do not overmix."},
            {"step": 5, "text": "Fold in chopped pecans."},
            {"step": 6, "text": "Roll dough into 1-inch balls. Place 1 inch apart on prepared sheets."},
            {"step": 7, "text": "Flatten slightly with the bottom of a glass or your palm."},
            {"step": 8, "text": "Bake for 12-15 minutes until edges are just barely golden (centers will look pale)."},
            {"step": 9, "text": "Cool on baking sheet 5 minutes - cookies are fragile when warm."},
            {"step": 10, "text": "Optional: dust with powdered sugar while still slightly warm."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [
            "The 'sandy' texture comes from powdered sugar and minimal mixing",
            "Don't overmix - it develops gluten and makes cookies tough",
            "Bake until edges are barely golden - they continue cooking on the sheet",
            "Very fragile when warm - let cool before moving",
            "Keebler made them famous, but homemade are far better",
            "Store in airtight container - they stay fresh for a week"
        ],
        "tags": ["cookies", "pecan sandies", "shortbread", "pecans", "butter cookies", "classic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "classic-rice-krispie-treats",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rice Krispie Treats (Original)",
        "category": "desserts",
        "attribution": "Kellogg's / Mildred Day (1939)",
        "source_note": "Invented in 1939 by Mildred Day, a Kellogg's home economist, for a Camp Fire Girls fundraiser. Has been on the Rice Krispies box ever since. The secret to gooey treats: don't overheat the marshmallows.",
        "description": "The classic no-bake treat that's been on the Rice Krispies box since 1939. Crispy cereal held together by gooey melted marshmallows and butter. The secret to perfect treats: fresh marshmallows and don't overheat.",
        "servings_yield": "24 treats",
        "prep_time": "10 min",
        "cook_time": "5 min",
        "total_time": "15 min (plus cooling)",
        "ingredients": [
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "marshmallows", "quantity": "10", "unit": "oz", "prep_note": "about 40 regular, or 4 cups mini"},
            {"item": "Rice Krispies cereal", "quantity": "6", "unit": "cups"},
            {"item": "salt", "quantity": "1", "unit": "pinch", "prep_note": "optional but recommended"}
        ],
        "instructions": [
            {"step": 1, "text": "Grease a 9x13-inch pan with butter or cooking spray."},
            {"step": 2, "text": "In a large pot or microwave-safe bowl, melt butter over low heat."},
            {"step": 3, "text": "Add marshmallows and stir constantly until completely melted and smooth."},
            {"step": 4, "text": "IMPORTANT: Remove from heat immediately - don't let marshmallows overcook."},
            {"step": 5, "text": "Add pinch of salt if using (enhances flavor)."},
            {"step": 6, "text": "Add Rice Krispies and stir until well coated."},
            {"step": 7, "text": "Using a buttered spatula or wax paper, press mixture evenly into prepared pan."},
            {"step": 8, "text": "Don't press too hard - gently press for gooey treats."},
            {"step": 9, "text": "Let cool for 30 minutes before cutting into squares."}
        ],
        "temperature": "No bake (low stovetop heat)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Invented by Mildred Day at Kellogg's in 1939",
            "The secret: don't overheat marshmallows or treats will be hard",
            "Use fresh marshmallows - stale ones don't melt as smoothly",
            "A pinch of salt makes a surprising difference",
            "Don't press too firmly - loose pressing = gooier treats",
            "Add 1 tbsp extra butter for extra gooey treats"
        ],
        "tags": ["treats", "Rice Krispies", "no-bake", "marshmallow", "1939", "Kellogg's", "classic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "caramel-apple-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caramel Apple Salad (Snickers Salad)",
        "category": "desserts",
        "attribution": "1980s-1990s Potluck Classic",
        "source_note": "A sweet 'salad' that became popular at potlucks in the 1980s-90s. Combines fresh apples with Snickers bars, pudding, and Cool Whip for a dessert that tastes like a caramel apple. Also called Snickers Salad or Apple Snickers Salad.",
        "description": "All the flavors of a caramel apple in salad form - crisp apples, chopped Snickers bars, and a creamy pudding-Cool Whip base. A potluck favorite that walks the line between salad and dessert. Kids and adults love it.",
        "servings_yield": "10-12 servings",
        "prep_time": "15 min",
        "cook_time": "0 min",
        "total_time": "15 min (plus 1 hour chilling)",
        "ingredients": [
            {"item": "instant vanilla pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "Granny Smith apples", "quantity": "4-5", "unit": "medium", "prep_note": "cored and chopped"},
            {"item": "Snickers bars", "quantity": "4", "unit": "full-size", "prep_note": "chopped (or 8 fun-size)"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp", "prep_note": "optional, to prevent browning"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, whisk together pudding mix and milk until thick, about 2 minutes."},
            {"step": 2, "text": "Fold in Cool Whip until well combined."},
            {"step": 3, "text": "If using lemon juice, toss chopped apples with it to prevent browning."},
            {"step": 4, "text": "Fold chopped apples into the pudding mixture."},
            {"step": 5, "text": "Fold in chopped Snickers bars."},
            {"step": 6, "text": "Refrigerate for at least 1 hour before serving."},
            {"step": 7, "text": "Stir before serving and add a few extra Snickers pieces on top if desired."}
        ],
        "temperature": "No cook",
        "notes": [
            "Use tart Granny Smith apples - they contrast the sweet candy",
            "Chop the Snickers into bite-sized pieces",
            "Best served within a few hours - apples can get soft",
            "Also called Snickers Salad or Apple Snickers Salad",
            "Can substitute butterscotch pudding for more caramel flavor",
            "Became a potluck hit in the 1980s-90s"
        ],
        "tags": ["salad", "apple", "Snickers", "caramel", "pudding", "Cool Whip", "1980s", "potluck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jello-poke-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Jell-O Poke Cake",
        "category": "desserts",
        "attribution": "Jell-O / Kraft (1970s)",
        "source_note": "Invented by Kraft and featured on Jell-O boxes since the 1970s. A white cake with holes poked throughout, filled with liquid Jell-O that sets into colorful stripes. The original poke cake that inspired hundreds of variations.",
        "description": "The original poke cake - a white cake with holes poked throughout, filled with liquid Jell-O that creates colorful stripes in every slice. Topped with Cool Whip for a light, fruity dessert. The 1970s recipe that started the poke cake craze.",
        "servings_yield": "12-15 servings",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "45 min (plus 4 hours chilling)",
        "ingredients": [
            {"item": "white cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz, prepared as directed"},
            {"item": "Jell-O", "quantity": "1", "unit": "box", "prep_note": "3 oz, any flavor (strawberry is classic)"},
            {"item": "boiling water", "quantity": "1", "unit": "cup"},
            {"item": "cold water", "quantity": "1/2", "unit": "cup"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare and bake cake mix according to package directions in a 9x13-inch pan."},
            {"step": 2, "text": "Cool cake in pan for 15 minutes (cake should still be slightly warm)."},
            {"step": 3, "text": "Using the handle of a wooden spoon or a large fork, poke holes all over the cake about 1 inch apart."},
            {"step": 4, "text": "Poke all the way to the bottom of the cake."},
            {"step": 5, "text": "Dissolve Jell-O in boiling water, stirring for 2 minutes until completely dissolved."},
            {"step": 6, "text": "Stir in cold water."},
            {"step": 7, "text": "Carefully and slowly pour liquid Jell-O evenly over the cake, filling the holes."},
            {"step": 8, "text": "Refrigerate for at least 4 hours, or overnight, until Jell-O is completely set."},
            {"step": 9, "text": "Spread Cool Whip over the chilled cake."},
            {"step": 10, "text": "Keep refrigerated until serving."}
        ],
        "temperature": "Per cake mix directions",
        "pan_size": "9x13-inch pan",
        "notes": [
            "The original poke cake from Jell-O boxes, 1970s",
            "Poke holes while cake is still slightly warm for best absorption",
            "Strawberry Jell-O is the classic choice",
            "For rainbow effect, use different Jell-O colors in sections",
            "The Jell-O creates colorful stripes visible in every slice",
            "Must be refrigerated - the Jell-O needs to set"
        ],
        "tags": ["cake", "poke cake", "Jell-O", "1970s", "Cool Whip", "vintage", "colorful"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pink-stuff-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pink Stuff (Strawberry Fluff Salad)",
        "category": "desserts",
        "attribution": "Midwest Potluck Classic / 1970s",
        "source_note": "Known simply as 'Pink Stuff' at countless Midwest gatherings. A variation of the fluff salad trend using strawberry Jell-O, cottage cheese, fruit, and Cool Whip. Every family seems to have their own version.",
        "description": "The famous 'Pink Stuff' from every Midwest potluck - strawberry Jell-O, cottage cheese, crushed pineapple, and Cool Whip mixed into a fluffy pink cloud. Sweet, creamy, and impossibly easy. Everyone's grandma made this.",
        "servings_yield": "10-12 servings",
        "prep_time": "10 min",
        "cook_time": "0 min",
        "total_time": "10 min (plus 2 hours chilling)",
        "ingredients": [
            {"item": "strawberry Jell-O", "quantity": "1", "unit": "box", "prep_note": "3 oz, dry powder"},
            {"item": "cottage cheese", "quantity": "2", "unit": "cups", "prep_note": "small curd"},
            {"item": "crushed pineapple", "quantity": "20", "unit": "oz can", "prep_note": "drained well"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "miniature marshmallows", "quantity": "1", "unit": "cup", "prep_note": "optional"},
            {"item": "sliced fresh strawberries", "quantity": "1", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, sprinkle dry Jell-O powder over cottage cheese."},
            {"step": 2, "text": "Stir until Jell-O is dissolved and mixture is evenly pink."},
            {"step": 3, "text": "Fold in well-drained pineapple."},
            {"step": 4, "text": "Gently fold in Cool Whip until combined."},
            {"step": 5, "text": "Fold in marshmallows and/or fresh strawberries if using."},
            {"step": 6, "text": "Cover and refrigerate for at least 2 hours."},
            {"step": 7, "text": "Serve cold. Keeps refrigerated for 3-4 days."}
        ],
        "temperature": "No cook",
        "notes": [
            "Known as 'Pink Stuff' at every Midwest potluck",
            "Use DRY Jell-O powder - don't prepare it with water",
            "Drain the pineapple WELL or the salad will be watery",
            "Every family has their own variation",
            "Some add sliced bananas, mandarin oranges, or pecans",
            "The cottage cheese adds protein and tang"
        ],
        "tags": ["salad", "fluff", "pink stuff", "strawberry", "Jell-O", "cottage cheese", "1970s", "Midwest"],
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
