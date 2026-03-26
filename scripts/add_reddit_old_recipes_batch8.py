#!/usr/bin/env python3
"""Add more viral vintage recipes to the database (batch 8) - legendary bar cookies, urban legends, and classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "waldorf-astoria-red-velvet-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Waldorf-Astoria Red Velvet Cake",
        "category": "desserts",
        "attribution": "Adams Extract / Urban Legend Collection",
        "source_note": "The famous '$100 recipe' urban legend that circulated since the 1950s. While the Waldorf-Astoria never actually served this cake originally, the legend helped cement red velvet's place in American baking history.",
        "description": "The legendary red velvet cake from the famous urban legend. A woman supposedly paid $100 for this recipe and shared it with the world in revenge. Whether or not the story is true, the cake is undeniably delicious.",
        "servings_yield": "12-16 servings",
        "prep_time": "25 min",
        "cook_time": "30 min",
        "total_time": "55 min (plus cooling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "2 1/2", "unit": "cups", "prep_note": "sifted"},
            {"item": "sugar", "quantity": "1 1/2", "unit": "cups"},
            {"item": "vegetable oil", "quantity": "1", "unit": "cup"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "red food coloring", "quantity": "2", "unit": "oz", "prep_note": "1 bottle liquid"},
            {"item": "cocoa powder", "quantity": "1", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "white vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "cream cheese", "quantity": "16", "unit": "oz", "prep_note": "softened, for frosting"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened, for frosting"},
            {"item": "powdered sugar", "quantity": "4", "unit": "cups", "prep_note": "for frosting"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp", "prep_note": "for frosting"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease and flour two 9-inch round cake pans."},
            {"step": 2, "text": "In a large bowl, beat together sugar and oil until combined."},
            {"step": 3, "text": "Add eggs one at a time, beating well after each addition."},
            {"step": 4, "text": "In a small bowl, mix red food coloring with cocoa powder to form a paste. Add to batter."},
            {"step": 5, "text": "Add vanilla and mix well."},
            {"step": 6, "text": "In another bowl, combine sifted flour and salt."},
            {"step": 7, "text": "Add flour mixture to batter alternately with buttermilk, beginning and ending with flour."},
            {"step": 8, "text": "In a small bowl, mix baking soda with vinegar. It will fizz. Quickly fold into batter."},
            {"step": 9, "text": "Divide batter evenly between prepared pans."},
            {"step": 10, "text": "Bake for 25-30 minutes until a toothpick inserted in center comes out clean."},
            {"step": 11, "text": "Cool in pans for 10 minutes, then turn out onto wire racks to cool completely."},
            {"step": 12, "text": "For frosting: Beat cream cheese and butter until smooth. Add powdered sugar and vanilla; beat until fluffy."},
            {"step": 13, "text": "Frost between layers and over top and sides of cake."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "Two 9-inch round pans",
        "notes": [
            "The '$100 recipe' urban legend dates back to the 1950s",
            "Also known as 'Red Waldorf Cake' or '$300 Cake'",
            "The original red color came from a reaction between cocoa and vinegar/buttermilk",
            "Modern recipes use food coloring for consistent color",
            "Traditional frosting was boiled flour frosting, but cream cheese is now standard",
            "Adams Extract Company has distributed this recipe since at least the 1950s"
        ],
        "tags": ["cake", "red velvet", "urban legend", "vintage", "Waldorf Astoria", "cream cheese frosting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "neiman-marcus-250-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Neiman Marcus $250 Cookies",
        "category": "desserts",
        "attribution": "Urban Legend / Neiman Marcus (official version)",
        "source_note": "The famous urban legend about a woman charged $250 for a cookie recipe. The story is false, but it became so widespread that Neiman Marcus eventually published an actual recipe for free. The 'secret' is oats blended into a powder.",
        "description": "The legendary '$250 cookie' from the famous urban legend. The secret ingredient is oats blended into a powder, giving these chocolate chip cookies a nutty flavor with perfect texture. Now available for free, as Neiman Marcus intended.",
        "servings_yield": "About 48 cookies",
        "prep_time": "20 min",
        "cook_time": "12 min per batch",
        "total_time": "45 min",
        "ingredients": [
            {"item": "butter", "quantity": "1", "unit": "cup", "prep_note": "softened (2 sticks)"},
            {"item": "granulated sugar", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "all-purpose flour", "quantity": "2 1/2", "unit": "cups"},
            {"item": "old-fashioned oats", "quantity": "2 1/2", "unit": "cups", "prep_note": "blended to a powder"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "semisweet chocolate chips", "quantity": "2", "unit": "cups"},
            {"item": "milk chocolate bar", "quantity": "4", "unit": "oz", "prep_note": "grated"},
            {"item": "chopped walnuts", "quantity": "1 1/2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper."},
            {"step": 2, "text": "In a blender or food processor, blend the oats until they become a fine powder."},
            {"step": 3, "text": "In a large bowl, cream together butter and both sugars until light and fluffy."},
            {"step": 4, "text": "Add eggs and vanilla; beat until well combined."},
            {"step": 5, "text": "In a separate bowl, whisk together flour, powdered oats, baking powder, baking soda, and salt."},
            {"step": 6, "text": "Gradually add dry ingredients to the butter mixture, mixing until just combined."},
            {"step": 7, "text": "Stir in chocolate chips, grated chocolate bar, and walnuts."},
            {"step": 8, "text": "Roll dough into golf ball-sized balls and place 2 inches apart on prepared baking sheets."},
            {"step": 9, "text": "Bake for 10-12 minutes until edges are golden but centers still look slightly underdone."},
            {"step": 10, "text": "Let cool on baking sheet for 5 minutes before transferring to a wire rack."}
        ],
        "temperature": "375°F (190°C)",
        "notes": [
            "The 'secret ingredient' is oats blended into a fine powder",
            "The urban legend is completely false - Neiman Marcus never charged for recipes",
            "Neiman Marcus made this recipe available for free after the legend spread",
            "The grated milk chocolate bar adds extra richness",
            "Can be frozen as dough balls for fresh-baked cookies anytime",
            "The legend evolved from a similar 1948 '$25 Fudge Cake' story"
        ],
        "tags": ["cookies", "chocolate chip", "urban legend", "Neiman Marcus", "oats", "viral"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "magic-cookie-bars-hello-dolly",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Magic Cookie Bars (Hello Dolly Bars)",
        "category": "desserts",
        "attribution": "Eagle Brand / Alecia Couch (1965)",
        "source_note": "Originally submitted by 11-year-old Alecia Couch from Dallas to Clementine Paddleford's column in 1965. Named after the Broadway musical 'Hello, Dolly!' Eagle Brand later popularized them as 'Magic Cookie Bars.'",
        "description": "The original layered cookie bar - just press, layer, and pour. Graham cracker crust topped with chocolate chips, butterscotch chips, coconut, and pecans, all bound together with sweetened condensed milk. Pure magic.",
        "servings_yield": "24 bars",
        "prep_time": "10 min",
        "cook_time": "25 min",
        "total_time": "35 min (plus cooling)",
        "ingredients": [
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted"},
            {"item": "graham cracker crumbs", "quantity": "1 1/2", "unit": "cups"},
            {"item": "semisweet chocolate chips", "quantity": "1", "unit": "cup"},
            {"item": "butterscotch chips", "quantity": "1", "unit": "cup"},
            {"item": "sweetened flaked coconut", "quantity": "1 1/3", "unit": "cups"},
            {"item": "chopped pecans or walnuts", "quantity": "1", "unit": "cup"},
            {"item": "sweetened condensed milk", "quantity": "14", "unit": "oz can", "prep_note": "Eagle Brand"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C) or 325°F for glass pan."},
            {"step": 2, "text": "In a 9x13-inch baking pan, combine melted butter and graham cracker crumbs. Press firmly into the bottom of the pan."},
            {"step": 3, "text": "Layer chocolate chips evenly over the crust."},
            {"step": 4, "text": "Layer butterscotch chips over chocolate chips."},
            {"step": 5, "text": "Sprinkle coconut evenly over the chips."},
            {"step": 6, "text": "Scatter chopped nuts over the coconut."},
            {"step": 7, "text": "Pour sweetened condensed milk evenly over everything. Do not stir."},
            {"step": 8, "text": "Bake for 25-30 minutes until edges are golden brown."},
            {"step": 9, "text": "Cool completely in pan before cutting into bars."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "Also known as Seven Layer Bars, Hello Dollies, or Coconut Dream Bars",
            "Named after the Broadway musical 'Hello, Dolly!' which premiered in 1964",
            "No mixing required - the magic is in the layering",
            "The sweetened condensed milk binds everything together as it bakes",
            "Can substitute white chocolate chips for butterscotch",
            "Eagle Brand's most famous recipe since the 1960s"
        ],
        "tags": ["bars", "magic bars", "Hello Dolly", "Eagle Brand", "seven layer", "1960s", "no-mix", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "millionaires-shortbread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Millionaire's Shortbread",
        "category": "desserts",
        "attribution": "Traditional British/Scottish Recipe",
        "source_note": "A beloved British treat also known as caramel slice or 'homemade Twix bars.' Three decadent layers: buttery shortbread, soft caramel made with condensed milk, and rich chocolate topping. Popular in Scotland, UK, Australia, and New Zealand.",
        "description": "Three layers of pure indulgence: a crumbly buttery shortbread base, a thick layer of soft golden caramel, and a glossy chocolate topping. Called 'millionaire's' because regular shortbread would be jealous of these riches.",
        "servings_yield": "16-24 bars",
        "prep_time": "25 min",
        "cook_time": "40 min",
        "total_time": "1 hour 5 min (plus chilling)",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "1 1/2", "unit": "cups", "prep_note": "for shortbread"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "cold, cubed, for shortbread"},
            {"item": "sugar", "quantity": "1/4", "unit": "cup", "prep_note": "for shortbread"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": "for shortbread"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "for caramel"},
            {"item": "sweetened condensed milk", "quantity": "14", "unit": "oz can", "prep_note": "for caramel"},
            {"item": "light brown sugar", "quantity": "1/2", "unit": "cup", "prep_note": "packed, for caramel"},
            {"item": "golden syrup or corn syrup", "quantity": "2", "unit": "tbsp", "prep_note": "for caramel"},
            {"item": "semisweet chocolate chips", "quantity": "1 1/2", "unit": "cups", "prep_note": "for topping"},
            {"item": "butter", "quantity": "1", "unit": "tbsp", "prep_note": "for chocolate topping"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Line an 8x8-inch or 9x9-inch pan with parchment paper, leaving overhang for easy removal."},
            {"step": 2, "text": "For shortbread: Combine flour, 1/2 cup cold butter, sugar, and salt in a food processor. Pulse until mixture resembles coarse crumbs."},
            {"step": 3, "text": "Press shortbread mixture firmly and evenly into the prepared pan."},
            {"step": 4, "text": "Bake for 18-22 minutes until edges are just golden. Let cool while making caramel."},
            {"step": 5, "text": "For caramel: In a heavy saucepan, combine 1/2 cup butter, condensed milk, brown sugar, and golden syrup."},
            {"step": 6, "text": "Cook over medium heat, stirring constantly, until mixture thickens and turns golden caramel color, about 10-15 minutes."},
            {"step": 7, "text": "Pour hot caramel over the shortbread base. Spread evenly. Let cool for 30 minutes."},
            {"step": 8, "text": "For chocolate: Melt chocolate chips with 1 tablespoon butter in a microwave or double boiler."},
            {"step": 9, "text": "Pour melted chocolate over the caramel layer. Spread evenly."},
            {"step": 10, "text": "Refrigerate for at least 2 hours until chocolate is set."},
            {"step": 11, "text": "Use parchment overhang to lift bars from pan. Cut into squares with a sharp knife."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "8x8-inch or 9x9-inch pan",
        "notes": [
            "Also known as Caramel Slice or homemade Twix bars",
            "Scottish in origin - shortbread is their national cookie",
            "The caramel should be soft, not hard - don't overcook",
            "Store at room temperature for softer caramel, refrigerate for firmer bars",
            "Use dark chocolate for less sweetness",
            "Let chocolate set at room temperature for a glossy finish"
        ],
        "tags": ["bars", "shortbread", "caramel", "chocolate", "British", "Scottish", "millionaire"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-butterscotch-brownies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Butterscotch Brownies (Blondies)",
        "category": "desserts",
        "attribution": "Traditional American / 1950s Recipe",
        "source_note": "The original 'brownie' may actually have been blonde - Fannie Farmer's 1896 brownie recipe had no chocolate. Brown sugar-based brownies rose to popularity in the 1950s as 'butterscotch brownies' before being renamed 'blondies.'",
        "description": "The brownie's golden cousin - chewy, buttery bars with deep butterscotch flavor from brown sugar and vanilla. Some say these came before chocolate brownies. A true 1950s classic.",
        "servings_yield": "16-20 bars",
        "prep_time": "15 min",
        "cook_time": "25 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "melted"},
            {"item": "light brown sugar", "quantity": "1", "unit": "cup", "prep_note": "packed"},
            {"item": "egg", "quantity": "1", "unit": "large"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tbsp"},
            {"item": "all-purpose flour", "quantity": "1", "unit": "cup"},
            {"item": "baking powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "chopped walnuts or pecans", "quantity": "1/2", "unit": "cup", "prep_note": "optional"},
            {"item": "butterscotch chips", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease an 8x8-inch baking pan."},
            {"step": 2, "text": "In a medium saucepan, melt butter over low heat. Remove from heat."},
            {"step": 3, "text": "Stir brown sugar into the melted butter until well combined."},
            {"step": 4, "text": "Let mixture cool slightly, then beat in the egg and vanilla."},
            {"step": 5, "text": "In a small bowl, whisk together flour, baking powder, and salt."},
            {"step": 6, "text": "Add dry ingredients to the butter mixture. Stir until just combined."},
            {"step": 7, "text": "Fold in nuts and/or butterscotch chips if using."},
            {"step": 8, "text": "Spread batter evenly in the prepared pan."},
            {"step": 9, "text": "Bake for 20-25 minutes until edges are golden and a toothpick inserted in center comes out with moist crumbs."},
            {"step": 10, "text": "Do not overbake - blondies should be chewy, not cakey."},
            {"step": 11, "text": "Cool completely in pan before cutting into bars."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "8x8-inch pan",
        "notes": [
            "Fannie Farmer's 1896 'brownie' had no chocolate - blondies may be the original",
            "The generous vanilla is key to the butterscotch flavor",
            "Use dark brown sugar for deeper flavor",
            "Don't overbake - they firm up as they cool",
            "Rose to popularity in the 1950s cookbooks",
            "Also called 'blonde brownies' or 'butterscotch squares'"
        ],
        "tags": ["bars", "blondies", "butterscotch", "brownies", "1950s", "vintage", "no chocolate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "vintage-grasshopper-pie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grasshopper Pie",
        "category": "desserts",
        "attribution": "Lawrence Pugh / Bols Distillery (1949)",
        "source_note": "The Grasshopper cocktail was invented in 1949 by Lawrence Pugh at Bols Distillery. His wife had the idea to transform it into a frozen pie. First appeared in the 1963 Gourmet's Menu Cookbook. A 1960s-70s dinner party showstopper.",
        "description": "A frozen no-bake pie with a chocolate cookie crust and a light, fluffy mint filling made with creme de menthe, creme de cacao, and marshmallows. The elegant green dessert that defined 1970s dinner parties.",
        "servings_yield": "8 servings",
        "prep_time": "25 min",
        "cook_time": "0 min",
        "total_time": "25 min (plus 4 hours freezing)",
        "ingredients": [
            {"item": "Oreo cookies", "quantity": "24", "unit": "cookies", "prep_note": "crushed, for crust"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "melted, for crust"},
            {"item": "miniature marshmallows", "quantity": "3", "unit": "cups", "prep_note": "or 30 large"},
            {"item": "half-and-half or milk", "quantity": "1/2", "unit": "cup"},
            {"item": "green creme de menthe", "quantity": "1/4", "unit": "cup"},
            {"item": "white creme de cacao", "quantity": "2", "unit": "tbsp"},
            {"item": "heavy whipping cream", "quantity": "1 1/2", "unit": "cups", "prep_note": "cold"},
            {"item": "green food coloring", "quantity": "2-3", "unit": "drops", "prep_note": "optional, for brighter color"},
            {"item": "chocolate shavings", "quantity": "2", "unit": "tbsp", "prep_note": "for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "Crush Oreos in a food processor or in a zip-lock bag with a rolling pin until fine crumbs."},
            {"step": 2, "text": "Mix Oreo crumbs with melted butter. Press firmly into the bottom and up the sides of a 9-inch pie plate."},
            {"step": 3, "text": "Freeze crust for 15 minutes while making filling."},
            {"step": 4, "text": "In a saucepan, combine marshmallows and half-and-half over low heat. Stir until marshmallows are completely melted."},
            {"step": 5, "text": "Remove from heat. Stir in creme de menthe and creme de cacao. Add food coloring if desired."},
            {"step": 6, "text": "Transfer to a bowl and refrigerate until mixture begins to thicken, about 20-30 minutes, stirring occasionally."},
            {"step": 7, "text": "In a large bowl, whip heavy cream until stiff peaks form."},
            {"step": 8, "text": "Gently fold the cooled marshmallow mixture into the whipped cream until well combined."},
            {"step": 9, "text": "Pour filling into the prepared crust. Smooth the top."},
            {"step": 10, "text": "Freeze for at least 4 hours or overnight until firm."},
            {"step": 11, "text": "Garnish with chocolate shavings before serving. Let sit at room temperature for 5-10 minutes before slicing."}
        ],
        "temperature": "No bake",
        "pan_size": "9-inch pie plate",
        "notes": [
            "The Grasshopper cocktail was invented in 1949 - the pie followed soon after",
            "For non-alcoholic version, use mint extract (1 tsp) and skip the liqueurs",
            "Original recipes used Hydrox cookies before Oreos became dominant",
            "Can be made with chocolate wafer cookies instead of Oreos",
            "The green color is part of the appeal - don't skip the creme de menthe",
            "A dinner party showstopper in the 1960s-70s"
        ],
        "tags": ["pie", "grasshopper", "mint", "no-bake", "frozen", "1970s", "dinner party", "vintage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "watergate-pistachio-cookies",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Watergate Pistachio Cookies",
        "category": "desserts",
        "attribution": "Jell-O/General Foods (1970s adaptation)",
        "source_note": "Inspired by the 1970s Watergate Cake and Watergate Salad trend. When Jell-O released pistachio pudding mix in 1976, 'Watergate' became a category of pistachio desserts. The joke: 'It has lots of nuts and is covered up!'",
        "description": "Soft, chewy pistachio cookies in that signature pale green color. Made easy with cake mix and pistachio pudding - the 1970s way. All the flavors of Watergate Salad in cookie form.",
        "servings_yield": "About 36 cookies",
        "prep_time": "15 min",
        "cook_time": "10 min per batch",
        "total_time": "40 min",
        "ingredients": [
            {"item": "white or yellow cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "instant pistachio pudding mix", "quantity": "1", "unit": "box", "prep_note": "3.4 oz"},
            {"item": "vegetable oil", "quantity": "1/2", "unit": "cup"},
            {"item": "eggs", "quantity": "2", "unit": "large"},
            {"item": "chopped pistachios", "quantity": "1/2", "unit": "cup"},
            {"item": "white chocolate chips", "quantity": "1/2", "unit": "cup", "prep_note": "optional"},
            {"item": "shredded coconut", "quantity": "1/2", "unit": "cup", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Line baking sheets with parchment paper."},
            {"step": 2, "text": "In a large bowl, combine cake mix and pistachio pudding mix."},
            {"step": 3, "text": "Add oil and eggs. Mix until a soft dough forms."},
            {"step": 4, "text": "Fold in chopped pistachios and white chocolate chips and/or coconut if using."},
            {"step": 5, "text": "Roll dough into 1-inch balls. Place 2 inches apart on prepared baking sheets."},
            {"step": 6, "text": "Bake for 9-11 minutes until edges are set but centers still look slightly underdone."},
            {"step": 7, "text": "Let cool on baking sheet for 5 minutes before transferring to a wire rack."},
            {"step": 8, "text": "Cookies will be soft and chewy when cooled."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [
            "Part of the 1970s 'Watergate' dessert trend",
            "Jell-O pistachio pudding mix was released in 1976",
            "The joke: 'It's got lots of nuts and it's covered up!'",
            "Caused a pistachio pudding shortage in Washington D.C. in 1975",
            "Add coconut to mimic Watergate Salad flavors",
            "The pale green color is the signature look"
        ],
        "tags": ["cookies", "pistachio", "Watergate", "1970s", "cake mix", "vintage", "green"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "earthquake-cake",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Earthquake Cake",
        "category": "desserts",
        "attribution": "Vintage Amish / American Recipe",
        "source_note": "Found in vintage Amish cookbooks. Named for the way the cream cheese mixture creates cracks and fissures in the cake as it bakes, resembling earthquake damage. A German chocolate cake turned upside-down spectacular.",
        "description": "A German chocolate cake baked upside-down with coconut and pecans on the bottom, and cream cheese swirled through the top that creates dramatic 'earthquake' cracks as it bakes. Gooey, chocolatey, and utterly addictive.",
        "servings_yield": "12-16 servings",
        "prep_time": "15 min",
        "cook_time": "50 min",
        "total_time": "1 hour 5 min",
        "ingredients": [
            {"item": "chopped pecans", "quantity": "1", "unit": "cup"},
            {"item": "sweetened flaked coconut", "quantity": "1", "unit": "cup"},
            {"item": "German chocolate cake mix", "quantity": "1", "unit": "box", "prep_note": "15.25 oz"},
            {"item": "vegetable oil", "quantity": "1/3", "unit": "cup", "prep_note": "or as box directs"},
            {"item": "eggs", "quantity": "3", "unit": "large", "prep_note": "or as box directs"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": "or as box directs"},
            {"item": "cream cheese", "quantity": "8", "unit": "oz", "prep_note": "softened"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened"},
            {"item": "powdered sugar", "quantity": "3", "unit": "cups"},
            {"item": "chocolate chips", "quantity": "1", "unit": "cup", "prep_note": "optional, for extra chocolate"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F (175°C). Grease a 9x13-inch baking pan."},
            {"step": 2, "text": "Spread pecans evenly in the bottom of the prepared pan."},
            {"step": 3, "text": "Spread coconut evenly over the pecans."},
            {"step": 4, "text": "Prepare cake mix according to package directions with oil, eggs, and water."},
            {"step": 5, "text": "Pour cake batter evenly over the coconut and pecans. Do not stir."},
            {"step": 6, "text": "Sprinkle chocolate chips over the batter if using."},
            {"step": 7, "text": "In a bowl, beat cream cheese and butter until smooth."},
            {"step": 8, "text": "Add powdered sugar and beat until fluffy."},
            {"step": 9, "text": "Drop spoonfuls of cream cheese mixture over the batter. Do not spread - it will sink and swirl as it bakes."},
            {"step": 10, "text": "Bake for 45-55 minutes until edges are set. Center will still be slightly jiggly."},
            {"step": 11, "text": "Cool for at least 20-30 minutes before serving. Best served warm."}
        ],
        "temperature": "350°F (175°C)",
        "pan_size": "9x13-inch pan",
        "notes": [
            "The cream cheese creates 'earthquake' cracks as it sinks and the cake rises",
            "Don't try to spread the cream cheese - let it do its thing",
            "Can substitute devil's food or chocolate fudge cake mix",
            "Found in vintage Amish cookbooks",
            "Best served warm when the cream cheese is still gooey",
            "Do not overbake - the center should be slightly underdone"
        ],
        "tags": ["cake", "earthquake", "German chocolate", "cream cheese", "coconut", "pecans", "vintage", "Amish"],
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
