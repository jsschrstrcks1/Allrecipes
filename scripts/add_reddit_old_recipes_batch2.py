#!/usr/bin/env python3
"""Add more viral recipes from Reddit r/Old_Recipes to the database (batch 2)."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "reddit-big-mamas-cinnamon-roll-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Big Mama's Cinnamon Roll Cake",
        "category": "desserts",
        "attribution": "Big Mama / u/HumawormDoc, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Depression/WWII era recipe from 'Big Mama' who raised 5 children on a farm. The basic cake was her go-to for all homemade poke cakes.",
        "description": "A moist poke cake with swirls of cinnamon sugar throughout and a sweet vanilla glaze. From a Depression-era farm grandmother who 'could make delicious meals from seemingly nothing.'",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "30-35 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "self-rising flour", "quantity": "2", "unit": "cup", "prep_note": "or 2 cups AP flour + 1 tbsp baking powder + 1/2 tsp salt"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "shortening (Crisco)", "quantity": "1/2", "unit": "cup", "prep_note": "or butter for lighter texture"},
            {"item": "white sugar", "quantity": "1 1/2", "unit": "cup"},
            {"item": "milk or buttermilk", "quantity": "1", "unit": "cup", "prep_note": "or mix of both"},
            {"item": "vanilla extract", "quantity": "2", "unit": "tsp"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": "for cinnamon swirl"},
            {"item": "cinnamon", "quantity": "4", "unit": "tsp", "prep_note": "for cinnamon swirl"},
            {"item": "milk", "quantity": "1/4", "unit": "cup", "prep_note": "for icing"},
            {"item": "butter", "quantity": "3", "unit": "tbsp", "prep_note": "for icing"},
            {"item": "powdered sugar", "quantity": "2", "unit": "cup", "prep_note": "for icing"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for icing"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "Mix together brown sugar and cinnamon for the swirl; set aside."},
            {"step": 3, "text": "In a large bowl, cream together shortening (or butter) and sugar until light and fluffy."},
            {"step": 4, "text": "Add eggs one at a time, beating well after each addition."},
            {"step": 5, "text": "Mix in vanilla extract."},
            {"step": 6, "text": "Alternately add flour and milk, beginning and ending with flour, mixing until just combined."},
            {"step": 7, "text": "Pour half the batter into prepared pan. Sprinkle with half the cinnamon-sugar mixture."},
            {"step": 8, "text": "Add remaining batter and top with remaining cinnamon-sugar. Use a knife to swirl through the batter."},
            {"step": 9, "text": "Bake 30-35 minutes until a toothpick comes out clean."},
            {"step": 10, "text": "While warm, poke holes all over with a fork or skewer."},
            {"step": 11, "text": "For icing: Melt butter with milk. Whisk in powdered sugar and vanilla until smooth."},
            {"step": 12, "text": "Pour icing over warm cake, letting it seep into the holes. Serve warm or at room temperature."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Reddit users suggest replacing Crisco with butter for lighter, fluffier texture",
            "Some reduce sugar by half for less sweetness",
            "Try pumpkin pie spice instead of cinnamon for variation",
            "Self-rising flour = AP flour + 1 tbsp baking powder + 1/2 tsp salt per 2 cups"
        ],
        "tags": ["cake", "cinnamon roll", "poke cake", "vintage", "reddit", "viral", "depression era", "WWII"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-elevator-lady-spice-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Elevator Lady Spice Cookies",
        "category": "desserts",
        "attribution": "Peg Bracken, 'The I Hate to Cook Book' (1960s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. From 'The I Hate to Cook Book' by Peg Bracken. Story goes that an elevator operator tasted the author's cookies and said 'I can sure make a better spice cooky than that' - and she was right.",
        "description": "Simple, warmly spiced molasses cookies that are easy enough for anyone who hates to cook. Soft and chewy with notes of cinnamon, cloves, and ginger.",
        "servings_yield": "About 36 cookies",
        "prep_time": "15 min",
        "cook_time": "10-12 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "shortening", "quantity": "3/4", "unit": "cup"},
            {"item": "sugar", "quantity": "1", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "molasses", "quantity": "1/4", "unit": "cup"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "baking soda", "quantity": "2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "ground cloves", "quantity": "3/4", "unit": "tsp"},
            {"item": "ground ginger", "quantity": "3/4", "unit": "tsp"},
            {"item": "turbinado sugar", "quantity": "", "unit": "for rolling", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F. Grease cookie sheets or line with parchment."},
            {"step": 2, "text": "In a stand mixer, beat shortening, sugar, egg, and molasses on medium speed until light and fluffy, about 2 minutes."},
            {"step": 3, "text": "In a separate bowl, whisk together flour, baking soda, salt, cinnamon, cloves, and ginger."},
            {"step": 4, "text": "Add dry ingredients to wet and mix until just combined."},
            {"step": 5, "text": "Chill dough for at least 10 minutes for easier handling."},
            {"step": 6, "text": "Form dough into walnut-sized balls. Roll in turbinado sugar if desired."},
            {"step": 7, "text": "Place 2 inches apart on prepared baking sheets."},
            {"step": 8, "text": "Bake at 375°F for 10-12 minutes until set."},
            {"step": 9, "text": "Let cool on pan for 10 minutes before transferring - cookies firm up as they cool."}
        ],
        "temperature": "375°F (190°C)",
        "notes": [
            "Chill dough before rolling - it's quite soft",
            "Rolling in turbinado sugar adds festive sparkle and extra crunch",
            "High altitude bakers may want to reduce baking soda slightly",
            "From Peg Bracken's classic 'The I Hate to Cook Book'"
        ],
        "tags": ["cookies", "spice", "molasses", "vintage", "reddit", "1960s", "easy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-red-dog-toast",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Red Dog Toast (Tomato Soup French Toast)",
        "category": "breakfast",
        "attribution": "Woman's Day Collector's Cook Book (1970) / u/nomoanya, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. Originally from the 1970 Woman's Day Collector's Cookbook. A savory twist on French toast using tomato soup.",
        "description": "A savory French toast made with condensed tomato soup instead of the usual egg-milk mixture. Dubbed 'one of the best breakfasts' by the original poster. Can be used to make incredible grilled cheese sandwiches.",
        "servings_yield": "4 servings",
        "prep_time": "5 min",
        "cook_time": "10 min",
        "total_time": "15 min",
        "ingredients": [
            {"item": "condensed tomato soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz, must be condensed not regular"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "paprika", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "thick bread slices", "quantity": "8", "unit": "slices", "prep_note": "brioche, sourdough, or Italian recommended"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "for frying"},
            {"item": "fresh chives", "quantity": "", "unit": "for topping", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "In a shallow bowl, beat together condensed tomato soup, eggs, paprika, and salt until well combined."},
            {"step": 2, "text": "Heat butter in a large skillet over medium heat."},
            {"step": 3, "text": "Dip bread slices in the tomato-egg mixture, coating both sides thoroughly."},
            {"step": 4, "text": "Fry in butter until golden brown on both sides, about 2-3 minutes per side."},
            {"step": 5, "text": "Serve immediately, topped with fresh chives if desired."}
        ],
        "temperature": "Medium heat",
        "notes": [
            "MUST use condensed tomato soup - regular soup is too wet and will make bread soggy",
            "Use thick, sturdy bread - avoid soft sandwich bread",
            "Use high-quality butter for best flavor",
            "Can be used to make extraordinary grilled cheese sandwiches",
            "Also excellent cut into cubes as croutons for salads or soup"
        ],
        "tags": ["breakfast", "french toast", "savory", "tomato soup", "vintage", "reddit", "1970s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-150-year-old-3-ingredient-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "150-Year-Old 3-Ingredient Cookies",
        "category": "desserts",
        "attribution": "Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. A 150-year-old family recipe passed down through generations. Beloved for its simplicity and impossibly delicious butterscotch-vanilla flavor.",
        "description": "An incredibly simple 3-ingredient cookie with rich butterscotch flavor despite no butterscotch. Thin, crisp edges with chewy centers. So easy the recipe is impossible to mess up.",
        "servings_yield": "About 24 cookies",
        "prep_time": "10 min",
        "cook_time": "20 min",
        "total_time": "50 min (including chill time)",
        "ingredients": [
            {"item": "self-rising flour", "quantity": "1", "unit": "cup", "prep_note": "or 1 cup AP flour + 1.5 tsp baking powder + 1/4 tsp salt"},
            {"item": "salted butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": "light or dark, packed"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Line baking sheets with parchment paper."},
            {"step": 2, "text": "Blend all ingredients together until well combined."},
            {"step": 3, "text": "Refrigerate dough for 20 minutes."},
            {"step": 4, "text": "Roll dough into small balls (about 1 tablespoon each)."},
            {"step": 5, "text": "Arrange on prepared baking sheet."},
            {"step": 6, "text": "Press a crosshatch pattern into each cookie with a fork (like peanut butter cookies)."},
            {"step": 7, "text": "Bake for 20 minutes, watching carefully as every oven is different."},
            {"step": 8, "text": "Let cool completely on pan - cookies continue to firm up after baking."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Cookies will be thin and pale but have incredible flavor",
            "Edges are tender-crisp, centers stay pleasantly chewy",
            "Tastes of vanilla and butterscotch despite containing neither",
            "Can use golden caster sugar or light brown sugar interchangeably",
            "Works in any oven including dorm toaster ovens",
            "Remove earlier for softer cookies - they continue baking on the pan"
        ],
        "tags": ["cookies", "3 ingredient", "easy", "vintage", "reddit", "viral", "minimal ingredients"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-damn-good-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Damn Good Cookies",
        "category": "desserts",
        "attribution": "Grace Fumerton / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. So beloved that the recipe was handed out at the creator's funeral in 2012. 'Mom always had a jar of these cookies in her kitchen.'",
        "description": "A classic oatmeal chocolate chip cookie with walnuts that earned its name. Gooey in the center fresh from the oven, with the perfect balance of chocolate, oats, and salty walnuts.",
        "servings_yield": "About 48 cookies",
        "prep_time": "15 min",
        "cook_time": "10 min",
        "total_time": "25 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened"},
            {"item": "brown sugar", "quantity": "3/4", "unit": "cup", "prep_note": "packed"},
            {"item": "white sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "old-fashioned oats", "quantity": "3", "unit": "cup"},
            {"item": "chocolate chips", "quantity": "1", "unit": "cup"},
            {"item": "walnuts", "quantity": "1", "unit": "cup", "prep_note": "chopped, optional but recommended"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F. Line baking sheets with parchment paper."},
            {"step": 2, "text": "Cream butter and both sugars until light and fluffy."},
            {"step": 3, "text": "Beat in eggs one at a time, then add vanilla."},
            {"step": 4, "text": "In a separate bowl, whisk together flour, baking soda, and salt."},
            {"step": 5, "text": "Gradually add flour mixture to butter mixture, mixing until just combined."},
            {"step": 6, "text": "Stir in oats, chocolate chips, and walnuts."},
            {"step": 7, "text": "Drop by rounded tablespoons onto prepared baking sheets."},
            {"step": 8, "text": "Bake at 325°F for 10 minutes until edges are set but centers still look slightly underdone."},
            {"step": 9, "text": "Let cool on pan for 5 minutes before transferring to wire rack."}
        ],
        "temperature": "325°F (163°C)",
        "notes": [
            "Recipe was handed out at Grace Fumerton's funeral in 2012",
            "Walnuts add a salty crunch that makes these special",
            "Fresh from the oven, cookies are gooey in the center",
            "Grace Fumerton was a mother of eight and proficient baker",
            "Simple enough that children can help make them"
        ],
        "tags": ["cookies", "oatmeal", "chocolate chip", "walnuts", "vintage", "reddit", "viral", "funeral recipe"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-worlds-best-gingerbread-1917",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "World's Best Gingerbread (1917)",
        "category": "desserts",
        "attribution": "The White House Cookbook (1917) / u/happieKampr, Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes viral recipe. From the 1917 edition of The White House Cookbook. Dubbed 'World's Best Gingerbread' by the poster who shared a triple batch.",
        "description": "A large, moist, dark, rich gingerbread cake that's not too sweet and wonderfully spicy. Over 100 years old and still the best recipe for holiday baking.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "45-50 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened"},
            {"item": "brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": "packed"},
            {"item": "molasses", "quantity": "2", "unit": "cup", "prep_note": "cooking molasses"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "fresh"},
            {"item": "ground ginger", "quantity": "2", "unit": "tbsp"},
            {"item": "cinnamon", "quantity": "2", "unit": "tsp"},
            {"item": "eggs", "quantity": "3", "unit": "large"},
            {"item": "all-purpose flour", "quantity": "4", "unit": "cup"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp", "prep_note": "dissolved in a little water"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease and flour a 9x13-inch baking pan or two 9-inch round pans."},
            {"step": 2, "text": "Mix lemon juice into milk and set aside to sour (about 5 minutes)."},
            {"step": 3, "text": "Cream butter and brown sugar until light and fluffy."},
            {"step": 4, "text": "Add molasses and beat well."},
            {"step": 5, "text": "Add the soured milk, ginger, and cinnamon. Beat thoroughly."},
            {"step": 6, "text": "Beat in eggs one at a time."},
            {"step": 7, "text": "Add half the flour and mix until combined."},
            {"step": 8, "text": "Dissolve baking soda in a little water and add to batter."},
            {"step": 9, "text": "Add remaining flour and mix until smooth."},
            {"step": 10, "text": "Pour into prepared pan(s)."},
            {"step": 11, "text": "Bake for 45-50 minutes until a toothpick inserted in center comes out clean."},
            {"step": 12, "text": "Let cool in pan for 10 minutes before serving. Excellent warm with whipped cream."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Use FRESH spices - the molasses is strongly flavored and needs fresh ginger and cinnamon to stand out",
            "Check the Reddit comments for modern tweaks and adaptations",
            "The lemon juice makes the milk act like buttermilk",
            "Recipe makes a large cake - perfect for sharing",
            "From the 1917 edition of The White House Cookbook"
        ],
        "tags": ["cake", "gingerbread", "molasses", "vintage", "reddit", "viral", "1917", "white house cookbook", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-tomato-soup-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tomato Soup Cake (Mystery Cake)",
        "category": "desserts",
        "attribution": "Campbell's / Community Cookbooks (1920s-1930s) / Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes. Originated in late 1920s/early 1930s community cookbooks. Popular during the Depression as it's made without eggs or butter. Also called 'Mystery Cake.'",
        "description": "A delightfully spicy cake made with tomato soup - the secret ingredient that makes it impossible to guess what's in it. Egg-free and dairy-free, a perfect Depression-era recipe.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "35-40 min",
        "total_time": "55 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2", "unit": "cup"},
            {"item": "sugar", "quantity": "1 1/3", "unit": "cup"},
            {"item": "baking powder", "quantity": "4", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "cinnamon", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "ground cloves", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground allspice", "quantity": "1/2", "unit": "tsp"},
            {"item": "condensed tomato soup", "quantity": "1", "unit": "can", "prep_note": "10.75 oz"},
            {"item": "shortening or vegetable oil", "quantity": "1/2", "unit": "cup"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "raisins", "quantity": "1", "unit": "cup", "prep_note": "optional"},
            {"item": "walnuts", "quantity": "1/2", "unit": "cup", "prep_note": "chopped, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Grease and flour a 9x13-inch pan or two 8-inch round pans."},
            {"step": 2, "text": "In a large bowl, sift together flour, sugar, baking powder, baking soda, cinnamon, cloves, and allspice."},
            {"step": 3, "text": "Add condensed tomato soup, shortening, and water."},
            {"step": 4, "text": "Beat with electric mixer on low speed until moistened, then on medium for 2 minutes."},
            {"step": 5, "text": "Fold in raisins and walnuts if using."},
            {"step": 6, "text": "Pour into prepared pan(s)."},
            {"step": 7, "text": "Bake for 35-40 minutes until a toothpick comes out clean."},
            {"step": 8, "text": "Cool completely. Frost with cream cheese frosting if desired."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "The spices completely mask the tomato flavor - guests will never guess the secret ingredient",
            "Called 'Mystery Cake' because people were challenged to guess what was in it",
            "Egg-free and dairy-free - perfect for Depression-era budgets",
            "Campbell's promoted this recipe in ads after seeing its popularity",
            "Cream cheese frosting is the traditional topping"
        ],
        "tags": ["cake", "tomato soup", "depression era", "vintage", "reddit", "mystery cake", "egg-free", "dairy-free"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "reddit-mamaws-no-bake-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mamaw's No-Bake Cookies",
        "category": "desserts",
        "attribution": "Reddit r/Old_Recipes",
        "source_note": "Reddit r/Old_Recipes classic. A beloved family recipe passed down through generations. One of the most frequently shared recipes on the subreddit.",
        "description": "Classic chocolate peanut butter oatmeal no-bake cookies. Ready in minutes with no oven required. A staple in grandmothers' kitchens for generations.",
        "servings_yield": "About 36 cookies",
        "prep_time": "10 min",
        "cook_time": "5 min",
        "total_time": "30 min (including set time)",
        "ingredients": [
            {"item": "sugar", "quantity": "2", "unit": "cup"},
            {"item": "butter", "quantity": "1/2", "unit": "cup"},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "cocoa powder", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "peanut butter", "quantity": "1/2", "unit": "cup", "prep_note": "creamy"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "old-fashioned oats", "quantity": "3", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Line baking sheets with wax paper or parchment paper."},
            {"step": 2, "text": "In a medium saucepan, combine sugar, butter, milk, cocoa, and salt."},
            {"step": 3, "text": "Bring to a rolling boil over medium heat, stirring constantly."},
            {"step": 4, "text": "Boil for exactly 1 minute (this is crucial for proper texture)."},
            {"step": 5, "text": "Remove from heat immediately."},
            {"step": 6, "text": "Stir in peanut butter and vanilla until smooth."},
            {"step": 7, "text": "Fold in oats until well coated."},
            {"step": 8, "text": "Working quickly, drop by spoonfuls onto prepared baking sheets."},
            {"step": 9, "text": "Let cool at room temperature until set, about 20-30 minutes."}
        ],
        "notes": [
            "The 1-minute boil is crucial - too short and they won't set, too long and they'll be dry",
            "Work quickly after adding oats - mixture sets fast",
            "If cookies don't set, mixture wasn't boiled long enough",
            "If cookies are dry/crumbly, mixture was boiled too long",
            "Store in airtight container at room temperature"
        ],
        "tags": ["cookies", "no-bake", "chocolate", "peanut butter", "oatmeal", "vintage", "reddit", "mamaw", "quick"],
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
