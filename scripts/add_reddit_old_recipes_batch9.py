#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 9) - regional classics and beloved layer cakes."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "canadian-matrimonial-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Matrimonial Cake (Date Squares)",
        "category": "desserts",
        "attribution": "Traditional Canadian / Prairie Provinces (1920s)",
        "source_note": "A beloved Canadian classic since the 1920s. Also known as date squares, date slice, or date crumbles. The name 'Matrimonial Cake' comes from the prairie provinces and may reference its use as an affordable wedding cake during the Depression.",
        "description": "A creamy date filling sandwiched between layers of buttery oat crumble. A Canadian classic since the 1920s, especially beloved in the prairie provinces where it's called Matrimonial Cake - perhaps because two layers come together, just like marriage.",
        "servings_yield": "16-24 squares",
        "prep_time": "25 min",
        "cook_time": "35 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "pitted dates", "quantity": "2", "unit": "cups", "prep_note": "chopped (about 12 oz)"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1/4", "unit": "cup", "prep_note": "for filling"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "old-fashioned rolled oats", "quantity": "1 1/2", "unit": "cups"},
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cups"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed, for crumble"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "butter", "quantity": "3/4", "unit": "cup", "prep_note": "cold, cubed"}
        ],
        "instructions": [
            {"step": 1, "text": "Make the filling: Combine dates, water, and 1/4 cup brown sugar in a saucepan."},
            {"step": 2, "text": "Cook over medium heat, stirring frequently, until dates are soft and mixture is thick, about 10 minutes."},
            {"step": 3, "text": "Remove from heat and stir in lemon juice and vanilla. Let cool while making crumble."},
            {"step": 4, "text": "Preheat oven to 350°F (175°C). Grease a 9x9-inch or 8x8-inch baking pan."},
            {"step": 5, "text": "Make the crumble: In a large bowl, combine oats, flour, 1 cup brown sugar, baking soda, and salt."},
            {"step": 6, "text": "Cut in cold butter with a pastry blender or your fingers until mixture resembles coarse crumbs."},
            {"step": 7, "text": "Press half the crumble mixture firmly into the bottom of the prepared pan."},
            {"step": 8, "text": "Spread the date filling evenly over the base."},
            {"step": 9, "text": "Sprinkle remaining crumble mixture over the date filling and press lightly."},
            {"step": 10, "text": "Bake for 30-35 minutes until top is golden brown."},
            {"step": 11, "text": "Cool completely in pan before cutting into squares."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x9-inch or 8x8-inch pan",
        "notes": [
            "Also known as Date Squares, Date Slice, Date Crumbles, or Dainties",
            "Popular in Canada since the 1920s, especially during the Depression",
            "The name 'Matrimonial Cake' is used mainly in the prairie provinces",
            "One theory: it was cheap enough to use as a wedding cake during hard times",
            "The lemon juice brightens the sweet date filling",
            "Best stored at room temperature for up to 5 days"
        ],
        "tags": ["bars", "dates", "oats", "Canadian", "vintage", "1920s", "matrimonial", "Depression era"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "harvey-wallbanger-cake-1970s",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Harvey Wallbanger Cake",
        "category": "desserts",
        "attribution": "1970s Party Cake / Galliano",
        "source_note": "Named after the famous 1970s cocktail made with vodka, Galliano liqueur, and orange juice. The cocktail was invented in 1952 by Donato 'Duke' Antone, allegedly named after a beach surfer who banged into walls after too many drinks.",
        "description": "A moist, boozy bundt cake flavored with orange juice, vodka, and Galliano liqueur - the same ingredients as the famous 1970s cocktail. Topped with a citrus-spiked glaze. The ultimate 70s party cake.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "45 min",
        "total_time": "1 hour (plus cooling)",
        "ingredients": [
            {"item": "yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "instant vanilla pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "vegetable oil", "quantity": "1/2", "unit": "cup"},
            {"item": "orange juice", "quantity": "1/2", "unit": "cup", "prep_note": "fresh preferred"},
            {"item": "vodka", "quantity": "1/4", "unit": "cup"},
            {"item": "Galliano liqueur", "quantity": "1/4", "unit": "cup"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup", "prep_note": "for glaze"},
            {"item": "orange juice", "quantity": "2", "unit": "tbsp", "prep_note": "for glaze"},
            {"item": "vodka", "quantity": "1", "unit": "tbsp", "prep_note": "for glaze"},
            {"item": "Galliano liqueur", "quantity": "1", "unit": "tbsp", "prep_note": "for glaze"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour a 10-inch bundt pan."},
            {"step": 2, "text": "In a large bowl, combine cake mix, pudding mix, eggs, oil, 1/2 cup orange juice, 1/4 cup vodka, and 1/4 cup Galliano."},
            {"step": 3, "text": "Beat with an electric mixer on medium speed for 2-3 minutes until smooth."},
            {"step": 4, "text": "Pour batter into prepared bundt pan."},
            {"step": 5, "text": "Bake for 40-50 minutes until a toothpick inserted in center comes out clean."},
            {"step": 6, "text": "Cool in pan for 10 minutes, then invert onto a wire rack."},
            {"step": 7, "text": "Poke holes all over the warm cake with a skewer or fork."},
            {"step": 8, "text": "For glaze: Whisk together powdered sugar, 2 tbsp orange juice, 1 tbsp vodka, and 1 tbsp Galliano until smooth."},
            {"step": 9, "text": "Drizzle glaze slowly over the warm cake, allowing it to soak into the holes."},
            {"step": 10, "text": "Let cool completely before serving. Flavor improves after 1-2 days."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "10-inch bundt pan",
        "notes": [
            "The cocktail was invented in 1952 but became hugely popular in the 1970s",
            "Galliano has vanilla and anise notes that complement the orange",
            "The cake improves after a day or two as flavors meld",
            "Can substitute orange liqueur (Grand Marnier) if you don't like anise",
            "Galliano was the #1 imported liqueur in the US during the 1970s",
            "Non-alcoholic version: use more orange juice in place of vodka and Galliano"
        ],
        "tags": ["cake", "bundt", "1970s", "Harvey Wallbanger", "cocktail", "boozy", "Galliano", "orange"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "southern-hummingbird-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hummingbird Cake",
        "category": "desserts",
        "attribution": "Mrs. L.H. Wiggins / Southern Living (1978)",
        "source_note": "First published in Southern Living magazine in February 1978, submitted by Mrs. L.H. Wiggins of Greensboro, North Carolina. Became the most requested recipe in the magazine's history. Originated in Jamaica as 'Doctor Bird Cake.'",
        "description": "The most requested recipe in Southern Living history - a moist, tropical layer cake loaded with bananas, crushed pineapple, and pecans, topped with cream cheese frosting. Originally from Jamaica, it became a Southern icon.",
        "servings_yield": "12-16 servings",
        "prep_time": "30 min",
        "cook_time": "30 min",
        "total_time": "1 hour (plus cooling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "3", "unit": "cups"},
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tsp"},
            {"item": "vegetable oil", "quantity": "1 1/2", "unit": "cups"},
            {"item": "eggs", "quantity": "3", "unit": "large", "prep_note": "beaten"},
            {"item": "vanilla extract", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "crushed pineapple", "quantity": "8", "unit": "oz can", "prep_note": "undrained"},
            {"item": "ripe bananas", "quantity": "2", "unit": "cups", "prep_note": "mashed (about 4 medium)"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "plus more for garnish"},
            {"item": "cream cheese", "quantity": "16", "unit": "oz", "prep_note": "softened, for frosting"},
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened, for frosting"},
            {"item": "powdered sugar", "quantity": "4", "unit": "cups", "prep_note": "for frosting"},
            {"item": "vanilla extract", "quantity": "2", "unit": "tsp", "prep_note": "for frosting"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour three 9-inch round cake pans."},
            {"step": 2, "text": "In a large bowl, whisk together flour, sugar, salt, baking soda, and cinnamon."},
            {"step": 3, "text": "Add oil, beaten eggs, and vanilla. Stir until dry ingredients are just moistened. Do not beat."},
            {"step": 4, "text": "Fold in pineapple with juice, mashed bananas, and pecans."},
            {"step": 5, "text": "Divide batter evenly among prepared pans."},
            {"step": 6, "text": "Bake for 25-30 minutes until a toothpick inserted in center comes out clean."},
            {"step": 7, "text": "Cool in pans for 10 minutes, then turn out onto wire racks to cool completely."},
            {"step": 8, "text": "For frosting: Beat cream cheese and butter until smooth."},
            {"step": 9, "text": "Add powdered sugar and vanilla; beat until light and fluffy."},
            {"step": 10, "text": "Frost between layers and over top and sides of cake."},
            {"step": 11, "text": "Garnish with additional chopped pecans. Refrigerate until serving."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Three 9-inch round pans",
        "notes": [
            "Most requested recipe in Southern Living magazine history",
            "Originally from Jamaica where it was called 'Doctor Bird Cake'",
            "Named after a Jamaican hummingbird that eats only nectar",
            "Don't overmix the batter - it should be stirred, not beaten",
            "Use very ripe bananas for best flavor",
            "The original recipe was oil-based, not butter, for extra moisture"
        ],
        "tags": ["cake", "layer cake", "Southern", "1978", "Southern Living", "banana", "pineapple", "cream cheese frosting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "southern-pig-pickin-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pig Pickin' Cake",
        "category": "desserts",
        "attribution": "Traditional Southern / North Carolina",
        "source_note": "A Southern classic that shows up at barbecues, potlucks, and church suppers. Named after 'pig pickin's' - Southern pig roasts where the meat is picked off the roasted pig. Many credit North Carolina as its birthplace.",
        "description": "A moist mandarin orange cake topped with a dreamy pineapple-pudding-whipped topping frosting. A Southern potluck staple named after the traditional pig roasts where it's often served. Also called Mandarin Orange Cake or Sunshine Cake.",
        "servings_yield": "12-16 servings",
        "prep_time": "20 min",
        "cook_time": "30 min",
        "total_time": "50 min (plus chilling)",
        "ingredients": [
            {"item": "yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "vegetable oil", "quantity": "1/2", "unit": "cup"},
            {"item": "eggs", "quantity": "4", "unit": "large"},
            {"item": "mandarin oranges", "quantity": "15", "unit": "oz can", "prep_note": "drained, reserve juice"},
            {"item": "crushed pineapple", "quantity": "20", "unit": "oz can", "prep_note": "undrained"},
            {"item": "instant vanilla pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour a 9x13-inch pan (or two 9-inch round pans for layers)."},
            {"step": 2, "text": "In a large bowl, combine cake mix, oil, eggs, and 1/2 cup of the reserved mandarin orange juice."},
            {"step": 3, "text": "Beat with an electric mixer for 2-3 minutes until smooth."},
            {"step": 4, "text": "Gently fold in the drained mandarin oranges."},
            {"step": 5, "text": "Pour batter into prepared pan."},
            {"step": 6, "text": "Bake for 25-30 minutes until a toothpick inserted in center comes out clean."},
            {"step": 7, "text": "Cool completely."},
            {"step": 8, "text": "For frosting: Drain the crushed pineapple, reserving the juice."},
            {"step": 9, "text": "In a large bowl, whisk together the pineapple juice and dry pudding mix until thick."},
            {"step": 10, "text": "Fold in the Cool Whip until well combined."},
            {"step": 11, "text": "Fold in the drained crushed pineapple."},
            {"step": 12, "text": "Spread frosting over the cooled cake."},
            {"step": 13, "text": "Refrigerate for at least 2 hours, preferably overnight, before serving."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan or two 9-inch rounds",
        "notes": [
            "Named after Southern 'pig pickin' barbecue gatherings",
            "Also known as Mandarin Orange Cake, Sunshine Cake, Pea Pickin' Cake",
            "North Carolina is often credited as its birthplace",
            "Must be refrigerated due to the Cool Whip frosting",
            "Best made a day ahead - the flavors meld and the cake stays moist",
            "A potluck and church supper favorite for generations"
        ],
        "tags": ["cake", "mandarin orange", "pineapple", "Southern", "potluck", "Cool Whip", "pig pickin"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "italian-cream-cake-southern",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Italian Cream Cake",
        "category": "desserts",
        "attribution": "Traditional Southern / 1950s-1970s",
        "source_note": "Despite the name, this cake is more Southern than Italian. Theories suggest Italian immigrant bakers in the South adapted familiar flavors. Became a celebration staple in the 1950s-1970s. Pecans are essential - grown abundantly in Southern states.",
        "description": "A tender buttermilk cake studded with coconut and pecans, topped with cream cheese frosting. Despite its name, this cake is thoroughly Southern - perhaps named 'Italian' to sound elegant. A celebration and potluck favorite since the 1950s.",
        "servings_yield": "12-16 servings",
        "prep_time": "30 min",
        "cook_time": "30 min",
        "total_time": "1 hour (plus cooling)",
        "ingredients": [
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened"},
            {"item": "vegetable shortening", "quantity": "1/2", "unit": "cup"},
            {"item": "sugar", "quantity": "2", "unit": "cups"},
            {"item": "egg yolks", "quantity": "5", "unit": "large", "prep_note": "reserve whites"},
            {"item": "all-purpose flour", "quantity": "2", "unit": "cups"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "sweetened flaked coconut", "quantity": "1", "unit": "cup"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "toasted, for cake"},
            {"item": "egg whites", "quantity": "5", "unit": "large", "prep_note": "beaten to stiff peaks"},
            {"item": "cream cheese", "quantity": "16", "unit": "oz", "prep_note": "softened, for frosting"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened, for frosting"},
            {"item": "powdered sugar", "quantity": "4", "unit": "cups", "prep_note": "for frosting"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for frosting"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup", "prep_note": "toasted, for frosting"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour three 9-inch round cake pans."},
            {"step": 2, "text": "Toast pecans at 350°F for 8-10 minutes until fragrant. Set aside."},
            {"step": 3, "text": "Cream together butter, shortening, and sugar until light and fluffy."},
            {"step": 4, "text": "Add egg yolks one at a time, beating well after each addition."},
            {"step": 5, "text": "In a separate bowl, whisk together flour, baking soda, and salt."},
            {"step": 6, "text": "Add dry ingredients to creamed mixture alternately with buttermilk, beginning and ending with flour."},
            {"step": 7, "text": "Stir in vanilla, coconut, and 1 cup toasted pecans."},
            {"step": 8, "text": "Beat egg whites to stiff peaks. Gently fold into batter."},
            {"step": 9, "text": "Divide batter among prepared pans."},
            {"step": 10, "text": "Bake for 25-30 minutes until a toothpick comes out clean."},
            {"step": 11, "text": "Cool in pans 10 minutes, then turn out onto wire racks to cool completely."},
            {"step": 12, "text": "For frosting: Beat cream cheese and butter until smooth. Add powdered sugar and vanilla; beat until fluffy."},
            {"step": 13, "text": "Fold 1 cup toasted pecans into the frosting."},
            {"step": 14, "text": "Frost between layers and over top and sides. Garnish with additional pecans."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Three 9-inch round pans",
        "notes": [
            "More Southern than Italian - origin of the name is uncertain",
            "Toasting the pecans makes a big difference in flavor",
            "The combination of butter and shortening creates ideal texture",
            "Folding whipped egg whites keeps the cake tender and light",
            "Popular at Southern celebrations since the 1950s-70s",
            "Some families have made this recipe for generations"
        ],
        "tags": ["cake", "layer cake", "Italian cream", "Southern", "coconut", "pecans", "cream cheese frosting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "alabama-lane-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Alabama Lane Cake",
        "category": "desserts",
        "attribution": "Emma Rylander Lane (1898)",
        "source_note": "Created by Emma Rylander Lane of Clayton, Alabama, and published in her 1898 cookbook 'A Few Good Things to Eat' as 'Prize Cake' after it won first prize at a Georgia fair. Became Alabama's official state cake in 2016. Made famous by Harper Lee's 'To Kill a Mockingbird.'",
        "description": "A four-layer white cake with a boozy filling of egg yolks, sugar, butter, raisins, pecans, coconut, and bourbon. Named 'Prize Cake' when it won first place at a Georgia fair in 1898. Featured in 'To Kill a Mockingbird' - Miss Maudie's was 'so loaded with shinny it made me tight.'",
        "servings_yield": "12-16 servings",
        "prep_time": "45 min",
        "cook_time": "25 min",
        "total_time": "1 hour 10 min (plus resting)",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened, for cake"},
            {"item": "sugar", "quantity": "2", "unit": "cups", "prep_note": "for cake"},
            {"item": "all-purpose flour", "quantity": "3 1/4", "unit": "cups", "prep_note": "sifted"},
            {"item": "baking powder", "quantity": "3 1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "milk", "quantity": "1", "unit": "cup"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "egg whites", "quantity": "8", "unit": "large", "prep_note": "stiffly beaten"},
            {"item": "egg yolks", "quantity": "8", "unit": "large", "prep_note": "for filling"},
            {"item": "sugar", "quantity": "1 1/4", "unit": "cups", "prep_note": "for filling"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for filling"},
            {"item": "raisins", "quantity": "1", "unit": "cup", "prep_note": "chopped"},
            {"item": "chopped pecans", "quantity": "1", "unit": "cup"},
            {"item": "sweetened flaked coconut", "quantity": "1", "unit": "cup"},
            {"item": "bourbon", "quantity": "1/2", "unit": "cup", "prep_note": "or brandy"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for filling"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour four 9-inch round cake pans."},
            {"step": 2, "text": "For cake: Cream 1 cup butter and 2 cups sugar until light and fluffy."},
            {"step": 3, "text": "Sift together flour, baking powder, and salt."},
            {"step": 4, "text": "Add dry ingredients to creamed mixture alternately with milk, beginning and ending with flour."},
            {"step": 5, "text": "Stir in 1 tsp vanilla."},
            {"step": 6, "text": "Beat egg whites to stiff peaks. Fold gently into batter."},
            {"step": 7, "text": "Divide batter among prepared pans."},
            {"step": 8, "text": "Bake for 20-25 minutes until a toothpick comes out clean. Cool completely."},
            {"step": 9, "text": "For filling: In a heavy saucepan, whisk egg yolks and 1 1/4 cups sugar."},
            {"step": 10, "text": "Add 1/2 cup butter. Cook over medium heat, stirring constantly, until thick enough to coat a spoon, about 10-15 minutes."},
            {"step": 11, "text": "Remove from heat. Stir in raisins, pecans, coconut, bourbon, and vanilla."},
            {"step": 12, "text": "Let filling cool to room temperature."},
            {"step": 13, "text": "Spread filling between layers and over top of cake. Leave sides unfrosted or frost with boiled white frosting."},
            {"step": 14, "text": "Cover and let rest for 2-3 days before serving for best flavor."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Four 9-inch round pans",
        "notes": [
            "Alabama's official state cake since 2016",
            "Created by Emma Rylander Lane of Clayton, Alabama in 1898",
            "Originally won first prize at a Georgia county fair",
            "Featured in Harper Lee's 'To Kill a Mockingbird'",
            "Best made 2-3 days ahead - the bourbon mellows and flavors meld",
            "Emma Lane's original used just raisins; pecans and coconut came later"
        ],
        "tags": ["cake", "layer cake", "Southern", "Alabama", "bourbon", "raisins", "pecans", "1898", "To Kill a Mockingbird"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "lemon-lush-dessert",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lemon Lush",
        "category": "desserts",
        "attribution": "Traditional Potluck Classic",
        "source_note": "A retro layered dessert that's been a potluck and church supper favorite for decades. Four layers of different textures and flavors in one pan. Also known as Lemon Delight or Lemon Layered Dessert.",
        "description": "Four layers of deliciousness: a buttery pecan shortbread crust, a fluffy cream cheese layer, smooth lemon pudding, and billowy Cool Whip on top. A no-bake potluck classic that's perfect for summer gatherings.",
        "servings_yield": "12-16 servings",
        "prep_time": "25 min",
        "cook_time": "20 min",
        "total_time": "45 min (plus 2 hours chilling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "1", "unit": "cup", "prep_note": "for crust"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "cold, cubed, for crust"},
            {"item": "chopped pecans", "quantity": "1/2", "unit": "cup", "prep_note": "for crust and topping"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup"},
            {"item": "Cool Whip", "quantity": "16", "unit": "oz", "prep_note": "divided (8 oz containers x 2)"},
            {"item": "instant lemon pudding mix", "quantity": "2", "unit": "boxes", "prep_note": "3.4 oz each"},
            {"item": "milk", "quantity": "3", "unit": "cups", "prep_note": "cold"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C)."},
            {"step": 2, "text": "For crust: Cut cold butter into flour until mixture resembles coarse crumbs."},
            {"step": 3, "text": "Stir in 1/4 cup pecans. Press mixture into the bottom of a 9x13-inch baking pan."},
            {"step": 4, "text": "Bake for 18-20 minutes until golden brown. Cool completely."},
            {"step": 5, "text": "For cream cheese layer: Beat cream cheese and powdered sugar until smooth."},
            {"step": 6, "text": "Fold in one 8 oz container of Cool Whip."},
            {"step": 7, "text": "Spread over cooled crust."},
            {"step": 8, "text": "For pudding layer: Whisk together pudding mixes and cold milk until thick, about 2 minutes."},
            {"step": 9, "text": "Spread pudding over cream cheese layer immediately."},
            {"step": 10, "text": "Spread remaining 8 oz Cool Whip over pudding layer."},
            {"step": 11, "text": "Sprinkle with remaining 1/4 cup pecans."},
            {"step": 12, "text": "Refrigerate for at least 2 hours (overnight is best) before serving."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Also known as Lemon Delight, Lemon Layered Dessert, or Cool Lemon Dessert",
            "A potluck and church supper classic",
            "Freeze for 30 minutes before slicing for cleanest cuts",
            "Use very cold milk for the pudding layer",
            "Best made a day ahead - layers firm up and flavors meld",
            "Can substitute chocolate or butterscotch pudding for variations"
        ],
        "tags": ["dessert", "lemon", "layered", "potluck", "Cool Whip", "cream cheese", "no-bake", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "better-than-sex-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Better Than Sex Cake",
        "category": "desserts",
        "attribution": "Traditional Potluck Classic",
        "source_note": "A famous chocolate poke cake that's been a potluck legend for decades. Also known as 'Better Than Anything Cake,' 'Better Than Robert Redford Cake,' or 'Heath Bar Cake.' The name is intentionally provocative.",
        "description": "A chocolate poke cake soaked with sweetened condensed milk and caramel sauce, topped with Cool Whip and crushed toffee bars. Sinfully rich, gooey, and absolutely addictive. The name says it all.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "35 min",
        "total_time": "50 min (plus 2 hours chilling)",
        "ingredients": [
            {"item": "German chocolate or devil's food cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "eggs", "quantity": "3", "unit": "large", "prep_note": "or as box directs"},
            {"item": "vegetable oil", "quantity": "1/3", "unit": "cup", "prep_note": "or as box directs"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": "or as box directs"},
            {"item": "sweetened condensed milk", "quantity": "14", "unit": "oz can"},
            {"item": "caramel sauce", "quantity": "12", "unit": "oz", "prep_note": "ice cream topping"},
            {"item": "Cool Whip", "quantity": "8", "unit": "oz", "prep_note": "thawed"},
            {"item": "Heath or Skor toffee bars", "quantity": "4-6", "unit": "bars", "prep_note": "crushed"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "Prepare and bake cake according to package directions in the prepared pan."},
            {"step": 3, "text": "Let cake cool for 10 minutes (cake should still be warm)."},
            {"step": 4, "text": "Using the handle of a wooden spoon, poke holes all over the top of the cake, about 1 inch apart."},
            {"step": 5, "text": "Don't poke all the way through to the bottom."},
            {"step": 6, "text": "In a bowl, combine sweetened condensed milk and caramel sauce. Mix well."},
            {"step": 7, "text": "Slowly pour the caramel mixture over the warm cake, filling the holes."},
            {"step": 8, "text": "Refrigerate for at least 2 hours, or overnight."},
            {"step": 9, "text": "Spread Cool Whip evenly over the chilled cake."},
            {"step": 10, "text": "Sprinkle crushed toffee bars generously over the top."},
            {"step": 11, "text": "Keep refrigerated until serving. The cake only gets better with time."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Also known as 'Better Than Anything Cake' for polite company",
            "Also called 'Heath Bar Cake' or 'Better Than Robert Redford Cake'",
            "The cake gets moister and more flavorful over several days",
            "Must be refrigerated due to the toppings",
            "Can substitute hot fudge sauce for caramel",
            "Use the wooden spoon handle for perfectly sized holes"
        ],
        "tags": ["cake", "poke cake", "chocolate", "caramel", "toffee", "Cool Whip", "potluck", "vintage"],
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
