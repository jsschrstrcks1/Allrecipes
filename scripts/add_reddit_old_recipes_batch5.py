#!/usr/bin/env python3
"""Add more viral recipes from Reddit r/Old_Recipes to the database (batch 5)."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "reddit-watergate-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Watergate Salad (Pistachio Fluff)",
        "category": "desserts",
        "attribution": "Kraft Foods (1975) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Developed by Kraft Foods in 1975 when pistachio pudding launched. Named by a Chicago columnist after the Watergate scandal.",
        "description": "A fluffy green dessert salad made with pistachio pudding, crushed pineapple, and Cool Whip. Also called 'the green stuff,' pistachio fluff, or 'Shut-the-Gate-Up Salad.'",
        "servings_yield": "12 servings",
        "prep_time": "10 min",
        "cook_time": "0 min",
        "total_time": "10 min (plus chill time)",
        "ingredients": [
            {"item": "instant pistachio pudding mix", "quantity": "1", "unit": "package", "prep_note": "3.4 oz"},
            {"item": "crushed pineapple", "quantity": "1", "unit": "can", "prep_note": "20 oz, undrained"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "mini marshmallows", "quantity": "1", "unit": "cup"},
            {"item": "pecans or walnuts", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"},
            {"item": "maraschino cherries", "quantity": "1/4", "unit": "cup", "prep_note": "chopped, optional for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, combine dry pistachio pudding mix with undrained crushed pineapple. Stir until pudding dissolves."},
            {"step": 2, "text": "Fold in Cool Whip until well combined."},
            {"step": 3, "text": "Fold in mini marshmallows and chopped nuts."},
            {"step": 4, "text": "Cover and refrigerate for at least 1 hour before serving."},
            {"step": 5, "text": "Garnish with maraschino cherries if desired."}
        ],
        "notes": [
            "Also called Pistachio Delight, Green Goddess, or Funeral Salad",
            "The pineapple juice activates the pudding mix - don't drain it",
            "A cousin to Ambrosia salad but with the distinctive pistachio flavor",
            "Named after the Watergate scandal by a Chicago columnist in 1975",
            "Perfect for potlucks and holiday gatherings"
        ],
        "tags": ["salad", "dessert salad", "pistachio", "retro", "1970s", "reddit", "potluck", "no-bake"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-7up-pound-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "7UP Pound Cake",
        "category": "desserts",
        "attribution": "7UP Company (1950s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Originated in a 1950s 7UP promotional pamphlet. A Southern staple passed down through generations.",
        "description": "A moist, tender pound cake with subtle lemon-lime flavor from 7UP soda. The carbonation acts as leavening and adds incredible moisture. A Southern tradition for decades.",
        "servings_yield": "16 servings",
        "prep_time": "20 min",
        "cook_time": "75 min",
        "total_time": "1 hour 35 min",
        "ingredients": [
            {"item": "butter", "quantity": "1 1/2", "unit": "cup", "prep_note": "3 sticks, softened"},
            {"item": "sugar", "quantity": "3", "unit": "cup"},
            {"item": "eggs", "quantity": "5", "unit": "large", "prep_note": "room temperature"},
            {"item": "all-purpose flour", "quantity": "3", "unit": "cup"},
            {"item": "7UP soda", "quantity": "3/4", "unit": "cup", "prep_note": "room temperature, NOT diet"},
            {"item": "lemon extract", "quantity": "2", "unit": "tbsp"},
            {"item": "powdered sugar", "quantity": "2", "unit": "cup", "prep_note": "for glaze"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F. Grease and flour a 10-inch bundt pan."},
            {"step": 2, "text": "Cream butter and sugar until light and fluffy, about 5 minutes."},
            {"step": 3, "text": "Add eggs one at a time, beating well after each addition."},
            {"step": 4, "text": "Alternately add flour and 7UP, beginning and ending with flour. Mix on low speed."},
            {"step": 5, "text": "Stir in lemon extract."},
            {"step": 6, "text": "Pour batter into prepared pan."},
            {"step": 7, "text": "Bake for 70-75 minutes until a toothpick comes out clean."},
            {"step": 8, "text": "Cool in pan for 15 minutes, then invert onto serving plate."},
            {"step": 9, "text": "For glaze: Whisk powdered sugar and lemon juice until smooth. Drizzle over warm cake."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "MUST use regular 7UP, not diet or zero sugar",
            "Sprite can be substituted for similar results",
            "The soda provides leavening AND moisture",
            "No baking powder needed - the carbonation does the work",
            "Many Southern grandmothers' signature cake"
        ],
        "tags": ["cake", "pound cake", "7up", "soda", "southern", "vintage", "reddit", "bundt"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-coca-cola-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Coca-Cola Cake",
        "category": "desserts",
        "attribution": "Southern American (1950s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. A beloved Southern sheet cake made with Coca-Cola in both the cake and frosting. The marshmallows in the frosting are the secret.",
        "description": "A moist chocolate sheet cake made with Coca-Cola, topped with a warm fudgy frosting loaded with miniature marshmallows and pecans. The cola adds moisture and subtle caramel notes.",
        "servings_yield": "24 servings",
        "prep_time": "20 min",
        "cook_time": "35 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "sugar", "quantity": "2", "unit": "cup"},
            {"item": "butter", "quantity": "1", "unit": "cup"},
            {"item": "Coca-Cola", "quantity": "1", "unit": "cup", "prep_note": "for cake"},
            {"item": "unsweetened cocoa powder", "quantity": "3", "unit": "tbsp", "prep_note": "for cake"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "mini marshmallows", "quantity": "1 1/2", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for frosting"},
            {"item": "Coca-Cola", "quantity": "6", "unit": "tbsp", "prep_note": "for frosting"},
            {"item": "unsweetened cocoa powder", "quantity": "3", "unit": "tbsp", "prep_note": "for frosting"},
            {"item": "powdered sugar", "quantity": "3 3/4", "unit": "cup"},
            {"item": "pecans", "quantity": "1", "unit": "cup", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "Whisk together flour and sugar in a large bowl."},
            {"step": 3, "text": "In a saucepan, combine 1 cup butter, 1 cup Coca-Cola, and 3 tbsp cocoa. Bring to a boil."},
            {"step": 4, "text": "Pour hot mixture over flour and sugar; stir to combine."},
            {"step": 5, "text": "Add buttermilk, eggs, baking soda, and vanilla. Mix until smooth."},
            {"step": 6, "text": "Fold in mini marshmallows."},
            {"step": 7, "text": "Pour into prepared pan. Bake 30-35 minutes until set."},
            {"step": 8, "text": "For frosting: In a saucepan, combine 1/2 cup butter, 6 tbsp Coca-Cola, and 3 tbsp cocoa. Bring to a boil."},
            {"step": 9, "text": "Remove from heat; beat in powdered sugar until smooth. Stir in pecans."},
            {"step": 10, "text": "Pour warm frosting over warm cake. Let cool before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Must use regular Coca-Cola, not diet",
            "The marshmallows in the batter create pockets of gooey sweetness",
            "Pour frosting while both cake and frosting are warm",
            "A Cracker Barrel restaurant favorite",
            "The cola adds moisture and a subtle caramel flavor"
        ],
        "tags": ["cake", "chocolate", "coca-cola", "sheet cake", "southern", "vintage", "reddit", "marshmallows"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-lime-jello-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lime Jello Salad with Cottage Cheese",
        "category": "sides",
        "attribution": "Mid-Century American (1960s-70s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Peak popularity in the 1960s. Also called 'Moon Glow Salad' or 'Green Jello Fluff.' A Thanksgiving staple in many families.",
        "description": "A creamy, fluffy lime gelatin salad studded with crushed pineapple and cottage cheese. The quintessential retro side dish that graced every 1960s-70s holiday table.",
        "servings_yield": "12 servings",
        "prep_time": "15 min",
        "cook_time": "0 min",
        "total_time": "4 hours 15 min (including set time)",
        "ingredients": [
            {"item": "lime Jello", "quantity": "1", "unit": "package", "prep_note": "6 oz or two 3 oz packages"},
            {"item": "boiling water", "quantity": "1", "unit": "cup"},
            {"item": "crushed pineapple", "quantity": "1", "unit": "can", "prep_note": "20 oz, drained (reserve juice)"},
            {"item": "cottage cheese", "quantity": "2", "unit": "cup", "prep_note": "small curd"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "mayonnaise", "quantity": "1/2", "unit": "cup", "prep_note": "optional"},
            {"item": "chopped pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve lime Jello in 1 cup boiling water. Stir until completely dissolved."},
            {"step": 2, "text": "Add 1/2 cup reserved pineapple juice. Stir to combine."},
            {"step": 3, "text": "Refrigerate until slightly thickened but not set, about 45 minutes."},
            {"step": 4, "text": "Fold in cottage cheese, drained pineapple, and Cool Whip."},
            {"step": 5, "text": "Add mayonnaise and pecans if using."},
            {"step": 6, "text": "Pour into a 9x13-inch dish or decorative mold."},
            {"step": 7, "text": "Refrigerate until fully set, at least 4 hours or overnight."}
        ],
        "notes": [
            "Can use sugar-free Jello for lighter version",
            "Orange Jello works equally well for an orange version",
            "The mayonnaise is traditional but optional",
            "Set in a decorative mold for 'fancy' presentation",
            "A Thanksgiving and Christmas staple since the 1960s"
        ],
        "tags": ["salad", "jello", "retro", "1960s", "cottage cheese", "reddit", "holiday", "side dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-lazy-daisy-oatmeal-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lazy Daisy Oatmeal Cake",
        "category": "desserts",
        "attribution": "1930s American / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Popular since the 1930s. Named for how easy it is to throw together. The broiled coconut-pecan frosting is the star.",
        "description": "A dense, moist oatmeal cake topped with a gooey broiled coconut and pecan frosting. The frosting caramelizes under the broiler, creating an irresistible topping.",
        "servings_yield": "12-15 servings",
        "prep_time": "20 min",
        "cook_time": "40 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "old-fashioned oats", "quantity": "1", "unit": "cup"},
            {"item": "boiling water", "quantity": "1 1/4", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened, for cake"},
            {"item": "white sugar", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1 1/3", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "nutmeg", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "butter", "quantity": "6", "unit": "tbsp", "prep_note": "melted, for frosting"},
            {"item": "brown sugar", "quantity": "2/3", "unit": "cup", "prep_note": "packed, for frosting"},
            {"item": "half-and-half", "quantity": "3", "unit": "tbsp", "prep_note": "for frosting"},
            {"item": "sweetened coconut flakes", "quantity": "1", "unit": "cup"},
            {"item": "pecans", "quantity": "1/2", "unit": "cup", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch METAL pan (not glass)."},
            {"step": 2, "text": "Pour boiling water over oats; let stand 20 minutes."},
            {"step": 3, "text": "Cream 1/2 cup butter with white and brown sugar until fluffy."},
            {"step": 4, "text": "Beat in eggs and vanilla."},
            {"step": 5, "text": "Whisk together flour, baking soda, cinnamon, nutmeg, and salt."},
            {"step": 6, "text": "Add flour mixture and oatmeal to creamed mixture. Mix until combined."},
            {"step": 7, "text": "Pour into prepared pan. Bake 30-35 minutes until set."},
            {"step": 8, "text": "For frosting: Mix melted butter, brown sugar, half-and-half, coconut, and pecans."},
            {"step": 9, "text": "Spread frosting over HOT cake."},
            {"step": 10, "text": "Place under broiler 2-4 minutes until bubbly and golden. Watch carefully!"}
        ],
        "temperature": "350°F (175°C) for baking, broil for frosting",
        "notes": [
            "MUST use metal pan - glass cannot go under broiler",
            "Use large coconut flakes, not shredded",
            "Watch the broiler carefully - frosting burns quickly",
            "Spread frosting on HOT cake so it soaks in",
            "Named 'Lazy Daisy' for its easy preparation"
        ],
        "tags": ["cake", "oatmeal", "broiled frosting", "coconut", "pecans", "vintage", "reddit", "1930s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-ambrosia-salad",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ambrosia Salad",
        "category": "desserts",
        "attribution": "Southern American (1800s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Named after the food of the Greek gods. Origins trace to the 1800s South when oranges were a rare Christmas treat.",
        "description": "A fluffy fruit salad with mandarin oranges, pineapple, coconut, marshmallows, and sour cream. A Southern holiday tradition since the 1800s when fresh oranges were a Christmas luxury.",
        "servings_yield": "10 servings",
        "prep_time": "15 min",
        "cook_time": "0 min",
        "total_time": "15 min (plus chill time)",
        "ingredients": [
            {"item": "mandarin oranges", "quantity": "2", "unit": "cans", "prep_note": "11 oz each, drained"},
            {"item": "crushed pineapple", "quantity": "1", "unit": "can", "prep_note": "20 oz, drained"},
            {"item": "sweetened coconut flakes", "quantity": "1", "unit": "cup"},
            {"item": "mini marshmallows", "quantity": "2", "unit": "cup"},
            {"item": "sour cream", "quantity": "1", "unit": "cup"},
            {"item": "maraschino cherries", "quantity": "1/2", "unit": "cup", "prep_note": "halved, optional"},
            {"item": "chopped pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large bowl, combine drained mandarin oranges and drained pineapple."},
            {"step": 2, "text": "Add coconut flakes and mini marshmallows."},
            {"step": 3, "text": "Fold in sour cream until everything is well coated."},
            {"step": 4, "text": "Add cherries and pecans if using."},
            {"step": 5, "text": "Cover and refrigerate for at least 2 hours or overnight."},
            {"step": 6, "text": "Stir before serving."}
        ],
        "notes": [
            "Named after ambrosia, the food of the Greek gods",
            "Traditional Southern Christmas dish since the 1800s",
            "Oranges were a rare Christmas gift in the old South",
            "Can use Cool Whip instead of sour cream for sweeter version",
            "Some add grapes or banana slices"
        ],
        "tags": ["salad", "fruit salad", "southern", "christmas", "vintage", "reddit", "coconut", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-pineapple-upside-down-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Classic Pineapple Upside-Down Cake",
        "category": "desserts",
        "attribution": "Dole / American (1920s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Gained popularity in the 1920s with canned pineapple. The caramelized brown sugar-butter topping is irresistible.",
        "description": "A buttery yellow cake with a caramelized pineapple and cherry topping. When inverted, the glistening fruit becomes the crowning glory of this American classic.",
        "servings_yield": "10 servings",
        "prep_time": "20 min",
        "cook_time": "45 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "butter", "quantity": "1/4", "unit": "cup", "prep_note": "for topping"},
            {"item": "brown sugar", "quantity": "2/3", "unit": "cup", "prep_note": "packed, for topping"},
            {"item": "pineapple rings", "quantity": "1", "unit": "can", "prep_note": "20 oz, drained (reserve juice)"},
            {"item": "maraschino cherries", "quantity": "7-9", "unit": "", "prep_note": "for centers"},
            {"item": "butter", "quantity": "1/3", "unit": "cup", "prep_note": "softened, for cake"},
            {"item": "sugar", "quantity": "3/4", "unit": "cup", "prep_note": "for cake"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1 1/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "reserved pineapple juice plus milk", "quantity": "1/2", "unit": "cup", "prep_note": "combined"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F."},
            {"step": 2, "text": "Melt 1/4 cup butter in a 9 or 10-inch cast iron skillet or round cake pan."},
            {"step": 3, "text": "Sprinkle brown sugar evenly over melted butter."},
            {"step": 4, "text": "Arrange pineapple rings on brown sugar. Place a cherry in each ring center."},
            {"step": 5, "text": "For cake: Cream 1/3 cup butter and sugar until fluffy."},
            {"step": 6, "text": "Beat in egg and vanilla."},
            {"step": 7, "text": "Whisk together flour, baking powder, and salt."},
            {"step": 8, "text": "Alternately add flour mixture and pineapple juice/milk to creamed mixture."},
            {"step": 9, "text": "Carefully spread batter over pineapple arrangement."},
            {"step": 10, "text": "Bake 40-45 minutes until golden and a toothpick comes out clean."},
            {"step": 11, "text": "Cool in pan 5 minutes, then invert onto serving plate. Serve warm."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Cast iron skillet gives best caramelization",
            "Invert while still warm or fruit will stick",
            "Can use fresh pineapple slices for better flavor",
            "Became popular in 1920s when canned pineapple became available",
            "Serve warm with whipped cream or vanilla ice cream"
        ],
        "tags": ["cake", "pineapple", "upside-down", "vintage", "reddit", "1920s", "cast iron", "cherries"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-texas-sheet-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Texas Sheet Cake",
        "category": "desserts",
        "attribution": "Texas / Southern American (1960s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. Origin debated but gained fame in Texas in the 1960s. Lady Bird Johnson popularized it. The poured warm frosting is key.",
        "description": "A thin, moist chocolate sheet cake with a warm pourable chocolate-pecan frosting. Everything's bigger in Texas, including this crowd-pleasing cake.",
        "servings_yield": "24 servings",
        "prep_time": "20 min",
        "cook_time": "25 min",
        "total_time": "45 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "sugar", "quantity": "2", "unit": "cup"},
            {"item": "butter", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "unsweetened cocoa powder", "quantity": "1/4", "unit": "cup", "prep_note": "for cake"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for frosting"},
            {"item": "unsweetened cocoa powder", "quantity": "1/4", "unit": "cup", "prep_note": "for frosting"},
            {"item": "milk", "quantity": "6", "unit": "tbsp", "prep_note": "for frosting"},
            {"item": "powdered sugar", "quantity": "4", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for frosting"},
            {"item": "pecans", "quantity": "1", "unit": "cup", "prep_note": "chopped"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease an 18x13-inch sheet pan (or 2 smaller pans)."},
            {"step": 2, "text": "Whisk together flour and sugar in a large bowl."},
            {"step": 3, "text": "In a saucepan, bring 1 cup butter, water, and 1/4 cup cocoa to a boil."},
            {"step": 4, "text": "Pour hot mixture over flour and sugar; stir to combine."},
            {"step": 5, "text": "Add buttermilk, eggs, baking soda, and 1 tsp vanilla. Mix until smooth."},
            {"step": 6, "text": "Pour into prepared pan. Bake 20-25 minutes until set."},
            {"step": 7, "text": "5 minutes before cake is done, make frosting: Bring 1/2 cup butter, 1/4 cup cocoa, and milk to a boil."},
            {"step": 8, "text": "Remove from heat; beat in powdered sugar, vanilla, and pecans."},
            {"step": 9, "text": "Pour warm frosting over hot cake, spreading evenly."},
            {"step": 10, "text": "Let cool completely before cutting."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Pour frosting on HOT cake for best results",
            "The thin layer means more frosting-to-cake ratio",
            "Lady Bird Johnson helped popularize this recipe",
            "Perfect for potlucks and church suppers",
            "Some add a pinch of cinnamon for depth"
        ],
        "tags": ["cake", "chocolate", "sheet cake", "texas", "southern", "vintage", "reddit", "pecans", "potluck"],
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
