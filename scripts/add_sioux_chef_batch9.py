#!/usr/bin/env python3
"""Add batch 9 of Sioux Chef recipes - desserts and sweets"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "sunflower-cookies-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sunflower Cookies",
        "native_name": "Waŋčázi Aǧúyapi Skúyela",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 135",
        "description": "These cookies are a hit at our Indigenous Food Lab events. They're great for the lunchbox or the hiking trail.",
        "servings_yield": "Makes about 3 dozen",
        "ingredients": [
            {"item": "sunflower butter", "quantity": "1", "unit": "cup"},
            {"item": "maple sugar", "quantity": "½", "unit": "cup"},
            {"item": "duck or chicken egg, beaten", "quantity": "1", "unit": ""},
            {"item": "corn flour", "quantity": "1", "unit": "cup"},
            {"item": "baking soda", "quantity": "½", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "toasted sunflower seeds for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 350°F. Line a baking sheet with parchment paper."},
            {"step": 2, "text": "In a medium bowl, combine the sunflower butter and the sugar and beat vigorously until light and creamy. Beat in the egg."},
            {"step": 3, "text": "In a separate bowl, whisk together the corn flour, baking soda, and salt."},
            {"step": 4, "text": "Fold the dry ingredients into the wet and mix together to form a soft dough. If the dough is too soft, add a little more corn flour."},
            {"step": 5, "text": "Drop the dough by rounded tablespoons onto the prepared pan. Press down on each to create a uniform disc, and top with a few sunflower seeds."},
            {"step": 6, "text": "Bake until the edges are golden, about 10 to 12 minutes. Remove from the oven and cool completely."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [
            "Edible flowers: From early spring through late fall, edible flowers add lovely color and flavor to salads, desserts, and garnishes. Flowers to grow: borage, calendula, chive blossoms, cornflower, nasturtium, roses, squash blossom, and sunflowers. Foraged flowers include wild bee balm, daylilies, mint blossoms, and violet."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "cookies", "sunflower", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "autumn-harvest-cookies-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Autumn Harvest Cookies",
        "native_name": "Ptaŋyétu Wóksapi Aǧúyapi Skúyela",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 136",
        "description": "These cookies are among the most requested at our events. They're rustic yet tender, not too sweet, and loaded with good things. They are perfect after school or before a hike.",
        "servings_yield": "Makes about 4 dozen",
        "ingredients": [
            {"item": "wild rice flour", "quantity": "1", "unit": "cup"},
            {"item": "hazelnut flour", "quantity": "1", "unit": "cup"},
            {"item": "baking soda", "quantity": "½", "unit": "tsp"},
            {"item": "salt", "quantity": "½", "unit": "tsp"},
            {"item": "ground juniper", "quantity": "¼", "unit": "tsp"},
            {"item": "sunflower or hazelnut oil", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "pure vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "dried cranberries or dried chokecherries", "quantity": "½", "unit": "cup"},
            {"item": "toasted hazelnuts, coarsely chopped", "quantity": "½", "unit": "cup"},
            {"item": "toasted pumpkin seeds, coarsely chopped", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 350°F. Line a baking sheet with parchment paper."},
            {"step": 2, "text": "In a medium bowl, whisk together the flours, baking soda, salt, and juniper."},
            {"step": 3, "text": "In a large bowl, whisk together the oil, maple syrup, and vanilla. Stir the dry ingredients into the wet until the dough comes together. Fold in the cranberries, hazelnuts, and pumpkin seeds."},
            {"step": 4, "text": "Drop the dough by rounded tablespoons onto the prepared pan. Press down on each cookie to flatten to a 2-inch round."},
            {"step": 5, "text": "Bake until the edges are golden, about 10 to 12 minutes. Remove from the oven and allow to cool completely."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "cookies", "harvest", "dessert", "autumn"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "corn-cookies-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Corn Cookies",
        "native_name": "Wagmíza Aǧúyapi Skúyela",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 137",
        "description": "These make terrific sandwich cookies filled with berry jams, sunflower butter, or our sorbet.",
        "servings_yield": "Makes about 2 dozen",
        "ingredients": [
            {"item": "corn flour", "quantity": "1", "unit": "cup"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "¼", "unit": "tsp"},
            {"item": "duck or chicken egg, at room temperature", "quantity": "1", "unit": ""},
            {"item": "maple sugar", "quantity": "¼", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "¼", "unit": "cup"},
            {"item": "honey", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 350°F. Line a baking sheet with parchment paper."},
            {"step": 2, "text": "In a medium bowl, whisk together the flour, baking powder, and salt."},
            {"step": 3, "text": "In a separate bowl, beat the egg with the maple sugar until smooth. Stir in the oil and honey. Add the dry ingredients and stir until the dough forms."},
            {"step": 4, "text": "Drop the dough by rounded tablespoons onto the prepared pan. Flatten gently with moistened fingers."},
            {"step": 5, "text": "Bake until the edges are golden, about 10 to 12 minutes. Remove from the oven and cool completely."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "cookies", "corn", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "amaranth-bites-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Amaranth Bites",
        "native_name": "Waȟpé Ziží Oyúte",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 139",
        "description": "Amaranth bites are simple to make, and they satisfy a sweet craving. They are loosely based on alegría, a popular Mexican confection of popped amaranth bound with honey.",
        "servings_yield": "Makes about 2 dozen",
        "ingredients": [
            {"item": "popped amaranth, page 144", "quantity": "3", "unit": "cups"},
            {"item": "sunflower seeds", "quantity": "½", "unit": "cup"},
            {"item": "dried cranberries or blueberries", "quantity": "½", "unit": "cup"},
            {"item": "honey", "quantity": "½", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the popped amaranth, sunflower seeds, and dried cranberries in a large mixing bowl."},
            {"step": 2, "text": "In a small saucepan over medium heat, warm the honey until it becomes thin and runny."},
            {"step": 3, "text": "Pour the warm honey over the amaranth mixture and stir to coat well. Season with a pinch of salt."},
            {"step": 4, "text": "Using damp hands, form the mixture into balls about 1½ inches in diameter. Place on a parchment-lined baking sheet and allow to cool and set."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "amaranth", "snack", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["popped-amaranth-cakes-sioux-chef"],
        "is_component": False
    },
    {
        "id": "chocolate-pecan-bites-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chocolate Pecan Bites",
        "native_name": "Čhaŋšúška na Gmá Oyúte",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 140",
        "description": "Cacao originated with the Olmec people of ancient Mexico, more than three thousand years ago. The Maya cultivated cacao in the Yucatán and used the seeds to make a drink they called chocolatl. It was made by grinding toasted cacao seeds with water and seasonings. Drinking chocolate was reserved for the warrior class and the nobility—this was the beverage that Hernando Cortés was served when he visited the court of Montezuma. Here we've combined pecans with dark chocolate for a sweet and crunchy dessert. Don't tell anyone how easy they are to make.",
        "servings_yield": "Makes about 3 dozen",
        "ingredients": [
            {"item": "bittersweet chocolate, chopped, or chocolate chips", "quantity": "8", "unit": "oz"},
            {"item": "toasted pecan pieces", "quantity": "1", "unit": "cup"},
            {"item": "dried cranberries (optional)", "quantity": "½", "unit": "cup"},
            {"item": "maple sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Line a baking sheet with parchment paper."},
            {"step": 2, "text": "Place the chocolate in a bowl set over a pan of simmering water and melt, stirring often."},
            {"step": 3, "text": "Put the pecans in a large mixing bowl and pour the melted chocolate over the pecans. Stir in the dried cranberries, if using."},
            {"step": 4, "text": "Drop the mixture by tablespoons onto the prepared baking sheet. Sprinkle with the maple sugar and a pinch of salt."},
            {"step": 5, "text": "Chill until set, about 30 minutes, and serve."}
        ],
        "notes": [],
        "tips": [
            "Chestnuts: Indigenous to North America, the American chestnut was once one of the most important trees in the forests of the eastern United States, from Maine and southern Ontario to Mississippi, and from the Atlantic coast to the Appalachian Mountains. Early in the twentieth century, a fungal disease called chestnut blight wiped out the American chestnut over half of its range—nearly four billion trees. There is hope on the horizon: thanks to the American Chestnut Foundation, scientists are working to create disease-resistant American chestnuts. When they're available, we use them in our desserts, cookies, and wild rice and bean cakes. In the meantime, we substitute Italian or Chinese chestnuts."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "chocolate", "pecan", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "raspberry-rose-hip-sauce-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Raspberry-Rose-Hip Sauce",
        "native_name": "Tȟakáŋheča na Uŋžíŋžiŋtka Oíčuwa Yužápi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 142",
        "description": "Rose hips are rich in vitamin C and add a citrusy touch to this sauce. Drizzle it over cakes, ice cream, and sorbet.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "fresh or frozen raspberries", "quantity": "2", "unit": "cups"},
            {"item": "fresh or dried rose hips, stems removed", "quantity": "½", "unit": "cup"},
            {"item": "honey or maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "water", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the raspberries, rose hips, honey, and water into a small saucepan and set over medium heat."},
            {"step": 2, "text": "Bring to a simmer and cook until the mixture is thick and the rose hips are soft, about 10 minutes."},
            {"step": 3, "text": "Strain through a fine-mesh sieve, pressing on the solids to extract as much liquid as possible. Discard the solids."},
            {"step": 4, "text": "Serve warm or chilled."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "raspberry", "rose hip", "sauce", "component", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "acorn-wild-rice-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Acorn and Wild Rice Cakes",
        "native_name": "Úta na Psíŋ Aǧúyapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 143",
        "description": "These little cakes are great served with fresh berries and whipped cream or a drizzle of Wojape, page 173, or Raspberry-Rose-Hip Sauce, page 142.",
        "servings_yield": "Makes about 12 cakes",
        "ingredients": [
            {"item": "acorn flour, page 169", "quantity": "1", "unit": "cup"},
            {"item": "cooked wild rice, page 79", "quantity": "½", "unit": "cup"},
            {"item": "maple sugar", "quantity": "¼", "unit": "cup"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "¼", "unit": "tsp"},
            {"item": "duck or chicken eggs", "quantity": "2", "unit": ""},
            {"item": "sunflower oil", "quantity": "¼", "unit": "cup"},
            {"item": "water", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 350°F. Lightly grease a muffin tin or line with paper liners."},
            {"step": 2, "text": "In a large bowl, whisk together the acorn flour, cooked wild rice, maple sugar, baking powder, and salt."},
            {"step": 3, "text": "In a separate bowl, beat the eggs with the oil and water."},
            {"step": 4, "text": "Stir the wet ingredients into the dry ingredients until just combined."},
            {"step": 5, "text": "Divide the batter among the prepared muffin cups."},
            {"step": 6, "text": "Bake until a toothpick inserted into the center comes out clean, about 18 to 20 minutes."},
            {"step": 7, "text": "Remove from the oven and cool slightly before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "acorn", "wild rice", "cakes", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "popped-amaranth-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Popped Amaranth Cakes (Alegría)",
        "native_name": "Waȟpé Ziží Napópapi Aǧúyapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 144",
        "description": "Alegría, Spanish for 'joy,' describes these popped amaranth confections perfectly. They're a popular street food in Mexico City, where vendors sell them in all shapes and sizes. This is a fun project for kids—a healthy version of the familiar crispy treat.",
        "servings_yield": "Makes about 24 pieces",
        "ingredients": [
            {"item": "amaranth seeds", "quantity": "1", "unit": "cup"},
            {"item": "honey", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "dried cranberries or raisins (optional)", "quantity": "½", "unit": "cup"},
            {"item": "toasted pumpkin seeds (optional)", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "To pop the amaranth: Heat a deep, dry pot over high heat. When the pot is very hot, add 1 tablespoon of the amaranth seeds. Shake the pot continuously until the seeds pop, about 10 to 15 seconds. Transfer the popped seeds to a bowl and repeat with the remaining seeds."},
            {"step": 2, "text": "In a small saucepan, combine the honey and maple syrup. Set over medium heat and cook, stirring, until the mixture reaches 250°F on a candy thermometer (hard-ball stage), about 5 to 7 minutes."},
            {"step": 3, "text": "Remove from the heat and quickly stir in the popped amaranth, dried cranberries, and pumpkin seeds, if using."},
            {"step": 4, "text": "Turn the mixture out onto a parchment-lined baking sheet and press into an even layer about ½ inch thick."},
            {"step": 5, "text": "Allow to cool completely, then cut into squares or rectangles."}
        ],
        "notes": [],
        "tips": [
            "To pop the amaranth: Keep the pot moving so the seeds don't burn. Work in small batches—if you add too many seeds at once, they won't pop evenly."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "amaranth", "alegria", "dessert", "confection"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["amaranth-bites-sioux-chef"]
    },
    {
        "id": "wild-rice-pudding-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Pudding",
        "native_name": "Psíŋ Wóžapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 145",
        "description": "This pudding is especially good topped with our berry sauces, page 142, and a dollop of fresh whipped cream.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "cooked wild rice, page 79", "quantity": "2", "unit": "cups"},
            {"item": "sunflower milk or hazelnut milk", "quantity": "2", "unit": "cups"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "duck or chicken eggs", "quantity": "2", "unit": ""},
            {"item": "pure vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "dried cranberries", "quantity": "½", "unit": "cup"},
            {"item": "toasted hazelnuts, chopped", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 325°F. Lightly grease a 2-quart baking dish."},
            {"step": 2, "text": "In a large bowl, combine the wild rice, milk, maple syrup, eggs, vanilla, and salt. Stir well to combine."},
            {"step": 3, "text": "Fold in the dried cranberries."},
            {"step": 4, "text": "Pour the mixture into the prepared baking dish. Sprinkle with the toasted hazelnuts."},
            {"step": 5, "text": "Bake until set and golden on top, about 45 to 50 minutes."},
            {"step": 6, "text": "Serve warm or at room temperature."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [],
        "tips": [
            "Wild Rice Cakes: Spread the baked pudding mixture in a greased 8-inch square pan. Cool, then cut into squares. Pan-fry the squares in a little sunflower oil until golden and crispy on both sides."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "pudding", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sunflower-milk-sorbet-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sunflower Milk Sorbet",
        "native_name": "Waŋčázi Asáŋpi Kȟáǧapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 146-147",
        "description": "This sorbet is creamy, nutty, and delicious. It's wonderful on its own or topped with fresh berries. Sunflower seeds are rich in healthy fats and give this sorbet a lovely, light texture.",
        "servings_yield": "Makes about 1 quart",
        "ingredients": [
            {"item": "raw sunflower seeds", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the sunflower seeds in a bowl and cover with cold water. Soak for at least 4 hours or overnight. Drain."},
            {"step": 2, "text": "Put the drained sunflower seeds into a blender with 3 cups fresh water and blend on high until very smooth, about 2 minutes."},
            {"step": 3, "text": "Strain the mixture through a fine-mesh sieve or nut milk bag, pressing to extract as much liquid as possible. Discard the solids."},
            {"step": 4, "text": "Stir in the maple syrup and a pinch of salt."},
            {"step": 5, "text": "Chill the mixture thoroughly, then churn in an ice cream maker according to the manufacturer's instructions."},
            {"step": 6, "text": "Transfer to a freezer-safe container and freeze until firm, about 2 hours."}
        ],
        "notes": [],
        "tips": [
            "Sunflowers: Sunflowers were first domesticated in the Americas as far back as 3000 BCE. Native tribes in Arizona and New Mexico used them for food, dye, and decoration. Now these sunny plants are found all over the world. We use the seeds and their oil in many of our dishes. Sunflower oil has a high smoke point, is rich in vitamin E, and has a pleasant, mild flavor."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sunflower", "sorbet", "frozen", "dessert", "dairy-free"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sweet-corn-sorbet-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sweet Corn Sorbet",
        "native_name": "Wagmíza Skúya Kȟáǧapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 147",
        "description": "This sorbet captures the essence of summer. It's best made at the height of corn season when the corn is at its sweetest.",
        "servings_yield": "Makes about 1 quart",
        "ingredients": [
            {"item": "ears sweet corn, shucked", "quantity": "6", "unit": ""},
            {"item": "water", "quantity": "2", "unit": "cups"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Cut the kernels from the cobs and put into a blender. Reserve the cobs."},
            {"step": 2, "text": "Cut the reserved cobs into pieces and put into a saucepan with the water. Bring to a boil, reduce heat, and simmer for 15 minutes to make a corn stock. Strain and discard the cobs."},
            {"step": 3, "text": "Add the warm corn stock to the blender with the kernels and blend until smooth."},
            {"step": 4, "text": "Strain through a fine-mesh sieve, pressing to extract as much liquid as possible."},
            {"step": 5, "text": "Stir in the maple syrup and salt. Chill thoroughly."},
            {"step": 6, "text": "Churn in an ice cream maker according to the manufacturer's instructions. Transfer to a freezer-safe container and freeze until firm."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "corn", "sorbet", "frozen", "dessert", "summer"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "hazelnut-maple-sorbet-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hazelnut Maple Sorbet",
        "native_name": "Gmá na Čhaŋháŋpi Tiktíča Kȟáǧapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 148",
        "description": "This sorbet has a rich, nutty flavor that pairs beautifully with chocolate or fresh berries.",
        "servings_yield": "Makes about 1 quart",
        "ingredients": [
            {"item": "raw hazelnuts", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast the hazelnuts in a dry skillet over medium heat until fragrant and lightly browned, about 5 minutes. Allow to cool, then rub off the skins."},
            {"step": 2, "text": "Put the hazelnuts and water in a blender and blend on high until very smooth."},
            {"step": 3, "text": "Strain through a fine-mesh sieve or nut milk bag, pressing to extract as much liquid as possible."},
            {"step": 4, "text": "Stir in the maple syrup and salt. Chill thoroughly."},
            {"step": 5, "text": "Churn in an ice cream maker according to the manufacturer's instructions. Transfer to a freezer-safe container and freeze until firm."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "hazelnut", "maple", "sorbet", "frozen", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "wild-rice-sorbet-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Sorbet",
        "native_name": "Psíŋ Kȟáǧapi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 149",
        "description": "This unique sorbet has a subtle, earthy flavor that's quite special. It's wonderful served with fresh berries or a drizzle of Wojape.",
        "servings_yield": "Makes about 1 quart",
        "ingredients": [
            {"item": "cooked wild rice, page 79", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "2", "unit": "cups"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the cooked wild rice and water in a blender and blend until smooth."},
            {"step": 2, "text": "Strain through a fine-mesh sieve, pressing to extract as much liquid as possible."},
            {"step": 3, "text": "Stir in the maple syrup and salt. Chill thoroughly."},
            {"step": 4, "text": "Churn in an ice cream maker according to the manufacturer's instructions. Transfer to a freezer-safe container and freeze until firm."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "sorbet", "frozen", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "maple-squash-sorbet-cranberry-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple Squash Sorbet with Cranberry Sauce",
        "native_name": "Čhaŋháŋpi Tiktíča Wagmú Kȟáǧapi nakúŋ Wathókeča T'áǧa Yužápi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 149",
        "description": "This sorbet celebrates the flavors of autumn. The sweet squash and tangy cranberry sauce make a perfect pair.",
        "servings_yield": "Makes about 1 quart",
        "ingredients": [
            {"item": "roasted butternut squash puree", "quantity": "2", "unit": "cups"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "ground cinnamon (optional)", "quantity": "¼", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "Cranberry Sauce, page 108, for serving", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In a blender, combine the squash puree, water, maple syrup, cinnamon (if using), and salt. Blend until smooth."},
            {"step": 2, "text": "Chill the mixture thoroughly."},
            {"step": 3, "text": "Churn in an ice cream maker according to the manufacturer's instructions. Transfer to a freezer-safe container and freeze until firm."},
            {"step": 4, "text": "Serve topped with Cranberry Sauce."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "squash", "maple", "cranberry", "sorbet", "frozen", "dessert", "autumn"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["cranberry-sauce-sioux-chef"],
        "is_component": False
    },
    {
        "id": "blueberry-raspberry-bergamot-spoon-sweet-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Blueberry-Raspberry-Bergamot Spoon Sweet",
        "native_name": "Wíŋyawapȟi na Tȟakáŋheča na Wačhípi Šiná Skúyela Iwóheya",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 150",
        "description": "Spoon sweets are a traditional way of preserving fruit. They're wonderful spooned over yogurt, ice cream, or pancakes.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "fresh blueberries", "quantity": "2", "unit": "cups"},
            {"item": "fresh raspberries", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "fresh or dried bergamot (wild bee balm)", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all of the ingredients in a medium saucepan and set over medium heat."},
            {"step": 2, "text": "Bring to a simmer and cook, stirring occasionally, until the berries break down and the mixture thickens, about 20 to 25 minutes."},
            {"step": 3, "text": "Remove from the heat and allow to cool."},
            {"step": 4, "text": "Transfer to clean jars and refrigerate for up to 2 weeks."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "blueberry", "raspberry", "bergamot", "preserve", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "wild-apple-sauce-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Apple Sauce (Savory or Sweet)",
        "native_name": "Tȟaspáŋ Yužápi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 151",
        "description": "This sauce is versatile—make it savory with herbs and serve with roasted meats, or sweeten it for dessert. Wild crabapples or any tart apples work beautifully.",
        "servings_yield": "Makes about 3 cups",
        "ingredients": [
            {"item": "wild crabapples or tart apples, cored and roughly chopped", "quantity": "2", "unit": "pounds"},
            {"item": "cider or water", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup (for sweet version)", "quantity": "¼ to ½", "unit": "cup"},
            {"item": "chopped sage (for savory version)", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the apples and cider in a large saucepan. Set over medium heat, cover, and cook until the apples are very soft, about 20 to 30 minutes."},
            {"step": 2, "text": "Pass through a food mill or press through a fine-mesh sieve to remove the skins. Discard the skins."},
            {"step": 3, "text": "For sweet sauce: Stir in the maple syrup to taste."},
            {"step": 4, "text": "For savory sauce: Stir in the sage and salt."},
            {"step": 5, "text": "Serve warm or cold."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "apple", "sauce", "component", "versatile"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "caramelized-seed-mix-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caramelized Seed Mix",
        "native_name": "Sú Kpámni Skúyela",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 152",
        "description": "This addictive snack is perfect for munching on its own or sprinkled over salads and desserts.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "sunflower seeds", "quantity": "½", "unit": "cup"},
            {"item": "pumpkin seeds", "quantity": "½", "unit": "cup"},
            {"item": "hazelnuts, roughly chopped", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 325°F. Line a baking sheet with parchment paper."},
            {"step": 2, "text": "Toss the seeds and nuts with the maple syrup and salt."},
            {"step": 3, "text": "Spread in a single layer on the prepared baking sheet."},
            {"step": 4, "text": "Bake, stirring every 10 minutes, until golden and caramelized, about 25 to 30 minutes."},
            {"step": 5, "text": "Remove from the oven and allow to cool completely. Break into pieces."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "seeds", "caramelized", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "maple-bruleed-squash-blueberries-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple Brûléed Squash with Blueberries",
        "native_name": "Čhaŋháŋpi Tiktíča Wagmú nakúŋ Wíŋyawapȟi",
        "category": "desserts",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 159",
        "description": "This elegant dessert features roasted squash topped with maple sugar and torched until caramelized, then finished with fresh blueberries.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "small delicata or acorn squash, halved and seeded", "quantity": "2", "unit": ""},
            {"item": "sunflower oil", "quantity": "1", "unit": "tbsp"},
            {"item": "maple sugar", "quantity": "¼", "unit": "cup"},
            {"item": "fresh blueberries", "quantity": "1", "unit": "cup"},
            {"item": "fresh mint for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 400°F. Brush the squash halves with oil and place cut-side down on a baking sheet."},
            {"step": 2, "text": "Roast until tender, about 30 to 40 minutes. Remove and allow to cool slightly."},
            {"step": 3, "text": "Slice each half into wedges and arrange on a serving platter."},
            {"step": 4, "text": "Sprinkle generously with maple sugar. Using a kitchen torch, caramelize the sugar until it bubbles and browns."},
            {"step": 5, "text": "Top with fresh blueberries and garnish with mint. Serve immediately."}
        ],
        "temperature": "400°F (200°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "squash", "maple", "blueberries", "brulee", "dessert"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    }
]

def main():
    with open('data/recipes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    for recipe in new_recipes:
        if recipe['id'] in existing_ids:
            print(f"ERROR: Recipe ID '{recipe['id']}' already exists!")
            return False

    data['recipes'].extend(new_recipes)
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    with open('data/recipes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes (batch 9 - desserts/sweets)")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
