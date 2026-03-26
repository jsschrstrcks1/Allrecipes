#!/usr/bin/env python3
"""Add batch 10 of Sioux Chef recipes - teas, beverages, pantry items"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "roasted-shell-sunflower-seeds-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Roasted in the Shell Sunflower Seeds",
        "native_name": "Waŋčázi Sú Čheúŋpapi",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 153",
        "description": "A classic snack that's easy to make at home. The seeds become wonderfully crunchy and flavorful when roasted.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "raw sunflower seeds in the shell", "quantity": "2", "unit": "cups"},
            {"item": "water", "quantity": "1", "unit": "quart"},
            {"item": "salt", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve the salt in the water in a large bowl. Add the sunflower seeds and soak for at least 8 hours or overnight."},
            {"step": 2, "text": "Preheat the oven to 325°F. Drain the seeds and spread in a single layer on a baking sheet."},
            {"step": 3, "text": "Roast, stirring occasionally, until the seeds are dry and crisp, about 30 to 40 minutes."},
            {"step": 4, "text": "Remove from the oven and allow to cool completely before serving."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sunflower", "seeds", "roasted", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "indigenous-granola-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Indigenous Granola",
        "native_name": "Ikčé Wičháša Wóyute",
        "category": "breakfast",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 154",
        "description": "This granola is packed with indigenous ingredients and makes a hearty breakfast or snack. It's wonderful with fresh berries and nut milk.",
        "servings_yield": "Makes about 6 cups",
        "ingredients": [
            {"item": "puffed wild rice", "quantity": "2", "unit": "cups"},
            {"item": "sunflower seeds", "quantity": "½", "unit": "cup"},
            {"item": "pumpkin seeds", "quantity": "½", "unit": "cup"},
            {"item": "hazelnuts, roughly chopped", "quantity": "½", "unit": "cup"},
            {"item": "dried cranberries", "quantity": "½", "unit": "cup"},
            {"item": "dried blueberries", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "¼", "unit": "cup"},
            {"item": "salt", "quantity": "½", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 300°F. Line a baking sheet with parchment paper."},
            {"step": 2, "text": "In a large bowl, combine the puffed wild rice, seeds, and nuts."},
            {"step": 3, "text": "In a small bowl, whisk together the maple syrup, oil, and salt. Pour over the dry ingredients and toss to coat."},
            {"step": 4, "text": "Spread the mixture in an even layer on the prepared baking sheet."},
            {"step": 5, "text": "Bake, stirring every 15 minutes, until golden, about 45 minutes."},
            {"step": 6, "text": "Remove from the oven and stir in the dried berries while still warm. Allow to cool completely before storing."}
        ],
        "temperature": "300°F (150°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "granola", "breakfast", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "native-granola-bars-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Native Granola Bars",
        "native_name": "Ikčé Wičháša Wóyute Okíse",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 155",
        "description": "These bars are perfect for hiking, camping, or a quick snack. They're loaded with seeds, nuts, and dried berries.",
        "servings_yield": "Makes about 16 bars",
        "ingredients": [
            {"item": "Indigenous Granola, page 154", "quantity": "3", "unit": "cups"},
            {"item": "sunflower butter", "quantity": "½", "unit": "cup"},
            {"item": "honey", "quantity": "¼", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Line an 8x8-inch baking pan with parchment paper, leaving an overhang for easy removal."},
            {"step": 2, "text": "In a small saucepan, combine the sunflower butter, honey, and maple syrup. Set over medium heat and stir until smooth and well combined."},
            {"step": 3, "text": "Put the granola in a large bowl and pour the warm mixture over it. Stir until well coated."},
            {"step": 4, "text": "Press the mixture firmly into the prepared pan, using the back of a spoon or your hands."},
            {"step": 5, "text": "Refrigerate until firm, at least 2 hours."},
            {"step": 6, "text": "Use the parchment overhang to lift the mixture from the pan. Cut into bars."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "granola bars", "snack", "hiking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["indigenous-granola-sioux-chef"],
        "is_component": False
    },
    {
        "id": "toasted-seeds-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Toasted Seeds",
        "native_name": "Sú Čheúŋpapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 158",
        "description": "Toasted seeds are versatile—use them to garnish salads, soups, and desserts, or enjoy them as a snack.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "raw seeds (pumpkin, squash, or sunflower)", "quantity": "", "unit": "as needed"},
            {"item": "sunflower oil", "quantity": "", "unit": "light coating"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 325°F."},
            {"step": 2, "text": "Toss the seeds with a light coating of oil and a pinch of salt."},
            {"step": 3, "text": "Spread in a single layer on a baking sheet."},
            {"step": 4, "text": "Toast until golden and fragrant, about 10 to 15 minutes, stirring halfway through."},
            {"step": 5, "text": "Remove from the oven and allow to cool. Store in an airtight container."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [
            "Roasted Maple Seeds: Toss the seeds with maple syrup instead of oil before toasting.",
            "Toasted Pumpkin and Squash Seeds: Remove seeds from squash, rinse, and dry well before toasting."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "seeds", "toasted", "component", "garnish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "labrador-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Labrador Tea",
        "native_name": "Swamp Tea",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 161",
        "description": "Labrador tea is made from the leaves of a shrub that grows in bogs and wetlands across the Northern Heartland. It has a distinctive, slightly resinous flavor and is rich in vitamin C.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "fresh or dried Labrador tea leaves", "quantity": "¼", "unit": "cup"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the Labrador tea leaves in a teapot or heatproof container."},
            {"step": 2, "text": "Pour the boiling water over the leaves."},
            {"step": 3, "text": "Steep for 5 to 10 minutes, depending on desired strength."},
            {"step": 4, "text": "Strain and serve. Sweeten with maple syrup if desired."}
        ],
        "notes": [
            "Caution: Use only true Labrador tea (Rhododendron groenlandicum). Some similar-looking plants can be toxic. Drink in moderation."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "cedar-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cedar Tea",
        "native_name": "Haŋté Wakhályapi",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 161",
        "description": "Cedar tea has been used for centuries by Native peoples for its medicinal properties. It's rich in vitamin C and has a pleasant, slightly piney flavor.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "fresh cedar fronds", "quantity": "¼", "unit": "cup"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the cedar fronds in a teapot or heatproof container."},
            {"step": 2, "text": "Pour the boiling water over the cedar."},
            {"step": 3, "text": "Steep for 10 to 15 minutes."},
            {"step": 4, "text": "Strain and serve. Sweeten with maple syrup if desired."}
        ],
        "notes": [
            "Use only safe species of cedar. Eastern white cedar (Thuja occidentalis) is traditionally used."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "cedar", "medicinal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "mint-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mint Tea",
        "native_name": "Čheyáka Wakhályapi",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 162",
        "description": "Mint tea is refreshing and aids digestion. Wild mint grows abundantly throughout the Northern Heartland.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "fresh wild mint leaves", "quantity": "¼", "unit": "cup"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the mint leaves in a teapot or heatproof container."},
            {"step": 2, "text": "Pour the boiling water over the mint."},
            {"step": 3, "text": "Steep for 5 to 7 minutes."},
            {"step": 4, "text": "Strain and serve hot or cold. Sweeten with maple syrup if desired."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "mint"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "bergamot-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bergamot Tea",
        "native_name": "Wačhípi Šiná Wakhályapi",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 162",
        "description": "Wild bergamot (bee balm) makes a floral, slightly spicy tea. It was traditionally used to treat colds and congestion.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "fresh or dried wild bergamot leaves and flowers", "quantity": "¼", "unit": "cup"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the bergamot in a teapot or heatproof container."},
            {"step": 2, "text": "Pour the boiling water over the bergamot."},
            {"step": 3, "text": "Steep for 10 to 15 minutes."},
            {"step": 4, "text": "Strain and serve. Sweeten with maple syrup if desired."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "bergamot", "bee balm"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "raspberry-leaf-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Raspberry Leaf Tea",
        "native_name": "Tȟakáŋheča Apé Wakhályapi",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 162",
        "description": "Raspberry leaf tea has a mild, slightly earthy flavor. It's traditionally used to support women's health.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "fresh or dried raspberry leaves", "quantity": "¼", "unit": "cup"},
            {"item": "boiling water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the raspberry leaves in a teapot or heatproof container."},
            {"step": 2, "text": "Pour the boiling water over the leaves."},
            {"step": 3, "text": "Steep for 10 to 15 minutes."},
            {"step": 4, "text": "Strain and serve. Sweeten with maple syrup if desired."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "raspberry"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "chaga-tea-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chaga Tea",
        "native_name": "Čhaǧá Wakhályapi",
        "category": "beverages",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 163",
        "description": "Chaga is a fungus that grows on birch trees and has been used for centuries in traditional medicine. It makes a dark, earthy tea that's rich in antioxidants.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "chaga chunks or powder", "quantity": "1", "unit": "oz"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup or honey (optional)", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the chaga and water in a saucepan."},
            {"step": 2, "text": "Bring to a simmer over medium heat and cook for 20 to 30 minutes."},
            {"step": 3, "text": "Strain and serve hot. Sweeten with maple syrup if desired."},
            {"step": 4, "text": "The chaga can be reused several times until the tea becomes weak."}
        ],
        "notes": [
            "Chaga can also be simmered into a thick sauce for glazing meat or vegetables."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tea", "beverage", "chaga", "medicinal", "mushroom"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sunny-butter-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sunny Butter (Sunflower Seed Butter)",
        "native_name": "Waŋčázi Wíȟdi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 166",
        "description": "This nut-free alternative to peanut butter is rich and delicious. It's great on bread, in smoothies, or as a dip for fruit.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "raw sunflower seeds", "quantity": "3", "unit": "cups"},
            {"item": "sunflower oil", "quantity": "2 to 4", "unit": "tbsp"},
            {"item": "maple syrup (optional)", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "salt", "quantity": "½", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Spread the sunflower seeds on a baking sheet and toast in a 325°F oven until golden, about 10 to 15 minutes. Allow to cool."},
            {"step": 2, "text": "Put the cooled seeds in a food processor fitted with a steel blade. Process, scraping down the sides occasionally, until the seeds begin to release their oils and form a paste, about 5 to 10 minutes."},
            {"step": 3, "text": "With the processor running, slowly add the oil until the desired consistency is reached."},
            {"step": 4, "text": "Add the maple syrup (if using) and salt. Process until smooth."},
            {"step": 5, "text": "Transfer to a clean jar and store in the refrigerator for up to 2 weeks."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sunflower", "butter", "spread", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "wild-rice-flour-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Flour",
        "native_name": "Psíŋ Aǧúyapi Blú",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 167",
        "description": "Wild rice flour adds a nutty, earthy flavor to baked goods. It's naturally gluten-free.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "wild rice", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Spread the wild rice in a single layer on a baking sheet."},
            {"step": 2, "text": "Toast in a 300°F oven until fragrant and slightly darker, about 15 to 20 minutes. Allow to cool."},
            {"step": 3, "text": "Working in batches, grind the toasted rice in a high-powered blender or spice grinder until it reaches a fine flour consistency."},
            {"step": 4, "text": "Sift to remove any large pieces. Re-grind the larger pieces if necessary."},
            {"step": 5, "text": "Store in an airtight container in a cool, dry place for up to 3 months."}
        ],
        "temperature": "300°F (150°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "flour", "component", "gluten-free"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "vegetable-flour-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vegetable Flour",
        "native_name": "Wathótho Aǧúyapi Blú",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 167",
        "description": "Dried vegetables can be ground into a flour that adds flavor and nutrition to breads, soups, and sauces.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "dried vegetables (corn, squash, mushrooms, etc.)", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Ensure the vegetables are completely dried—either purchase dried vegetables or dry them in a food dehydrator or low oven."},
            {"step": 2, "text": "Working in batches, grind the dried vegetables in a high-powered blender or spice grinder until they reach a fine flour consistency."},
            {"step": 3, "text": "Sift to remove any large pieces."},
            {"step": 4, "text": "Store in an airtight container in a cool, dry place for up to 6 months."}
        ],
        "notes": [
            "Different vegetables will yield different colored and flavored flours. Corn flour will be golden, dried mushroom flour earthy and dark."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "vegetable", "flour", "component", "dried"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "acorn-flour-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Acorn Meal/Flour",
        "native_name": "Úta Aǧúyapi Blú",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 169",
        "description": "Acorns were an important food source for many indigenous peoples. The nuts must be leached of their tannins before use.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "acorns", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Shell the acorns and remove the papery skin."},
            {"step": 2, "text": "Grind the acorn meat coarsely in a food processor or blender."},
            {"step": 3, "text": "Place the ground acorns in a large bowl and cover with cold water. Let soak for at least 24 hours, changing the water several times."},
            {"step": 4, "text": "Continue soaking and changing the water until the acorns no longer taste bitter (this can take several days)."},
            {"step": 5, "text": "Drain the acorns and spread on baking sheets. Dry in a 200°F oven until completely dry, about 2 to 3 hours."},
            {"step": 6, "text": "Grind the dried acorns to a fine flour in a high-powered blender or spice grinder."},
            {"step": 7, "text": "Store in an airtight container in the refrigerator for up to 3 months."}
        ],
        "temperature": "200°F (95°C)",
        "notes": [
            "The leaching process removes bitter tannins and makes the acorns edible. Don't skip this step!"
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "acorn", "flour", "component", "foraged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "hazelnut-flour-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hazelnut Flour",
        "native_name": "Gmá Aǧúyapi Blú",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 169",
        "description": "Hazelnut flour adds a rich, nutty flavor to baked goods. It's naturally gluten-free and high in protein.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "raw hazelnuts", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast the hazelnuts in a 350°F oven until fragrant and the skins begin to crack, about 10 to 12 minutes."},
            {"step": 2, "text": "Wrap the warm nuts in a clean kitchen towel and rub vigorously to remove the skins."},
            {"step": 3, "text": "Allow the nuts to cool completely."},
            {"step": 4, "text": "Working in batches, pulse the nuts in a food processor until finely ground, being careful not to over-process into butter."},
            {"step": 5, "text": "Sift to remove any large pieces."},
            {"step": 6, "text": "Store in an airtight container in the refrigerator for up to 3 months."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [
            "To prevent the flour from turning into butter, pulse in short bursts and don't over-process."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "hazelnut", "flour", "component", "gluten-free"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "chestnut-flour-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chestnut Flour",
        "native_name": "Čhaŋšúška Aǧúyapi Blú",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 169",
        "description": "Chestnut flour has a slightly sweet, nutty flavor. It's naturally gluten-free and wonderful in baked goods.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "chestnuts", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Score an X on the flat side of each chestnut. Roast in a 400°F oven until the shells curl back, about 20 to 25 minutes."},
            {"step": 2, "text": "While still warm, peel off the shells and papery inner skin."},
            {"step": 3, "text": "Break the chestnuts into pieces and spread on a baking sheet. Dry in a 200°F oven until completely dry, about 2 to 3 hours."},
            {"step": 4, "text": "Grind the dried chestnuts to a fine flour in a high-powered blender or spice grinder."},
            {"step": 5, "text": "Sift to remove any large pieces."},
            {"step": 6, "text": "Store in an airtight container in a cool, dry place for up to 3 months."}
        ],
        "temperature": "400°F (200°C) for roasting; 200°F (95°C) for drying",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "chestnut", "flour", "component", "gluten-free"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "game-meat-stock-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fish, Game, and Meat Stock",
        "native_name": "Hoǧáŋ, Wótȟapi, na Tȟaló Waháŋpi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 170",
        "description": "A rich stock made from game bones, fish frames, or meat scraps. Use to flavor soups, stews, and sauces.",
        "servings_yield": "Makes about 2 quarts",
        "ingredients": [
            {"item": "game bones, fish frames, or meat scraps", "quantity": "2 to 3", "unit": "pounds"},
            {"item": "cold water", "quantity": "3", "unit": "quarts"},
            {"item": "wild onion or shallot, halved", "quantity": "1", "unit": ""},
            {"item": "sage sprig", "quantity": "1", "unit": ""},
            {"item": "juniper berries", "quantity": "4 to 5", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "If using bones, roast them in a 400°F oven until browned, about 30 to 40 minutes. (Skip this step for fish frames.)"},
            {"step": 2, "text": "Place the bones or scraps in a large stockpot and cover with the cold water."},
            {"step": 3, "text": "Add the onion, sage, and juniper berries."},
            {"step": 4, "text": "Bring to a boil, then reduce heat and simmer for 2 to 4 hours (1 hour for fish stock), skimming any foam that rises to the surface."},
            {"step": 5, "text": "Strain through a fine-mesh sieve. Season with salt to taste."},
            {"step": 6, "text": "Cool and store in the refrigerator for up to 1 week, or freeze for up to 3 months."}
        ],
        "temperature": "400°F (200°C) for roasting bones",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "game", "fish", "stock", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "sprouts-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sprouts",
        "native_name": "Ičáǧa",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 174",
        "description": "Sprouts are easy to grow at home and add fresh crunch and nutrition to salads and dishes.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "seeds for sprouting (sunflower, pumpkin, beans)", "quantity": "¼", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the seeds in a clean jar and cover with water. Soak overnight."},
            {"step": 2, "text": "Drain and rinse the seeds. Cover the jar with cheesecloth or a sprouting lid."},
            {"step": 3, "text": "Place the jar in a warm spot away from direct sunlight. Rinse and drain the seeds twice a day."},
            {"step": 4, "text": "Continue rinsing and draining until the sprouts reach the desired length, usually 3 to 5 days."},
            {"step": 5, "text": "Use immediately or store in the refrigerator for up to 1 week."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sprouts", "fresh", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "corn-nuts-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Corn Nuts",
        "native_name": "Wagmíza Sú Čheúŋpapi",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 176",
        "description": "These crunchy corn kernels are addictive as a snack and make a great garnish for salads and tacos.",
        "servings_yield": "Makes about 2 cups",
        "ingredients": [
            {"item": "dried hominy or giant corn kernels", "quantity": "2", "unit": "cups"},
            {"item": "water for soaking", "quantity": "", "unit": ""},
            {"item": "sunflower oil for frying", "quantity": "", "unit": "about 2 inches deep"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak the hominy in cold water overnight. Drain and pat completely dry."},
            {"step": 2, "text": "Heat the oil in a deep pan to 350°F."},
            {"step": 3, "text": "Working in batches, fry the hominy until golden and crunchy, about 5 to 7 minutes."},
            {"step": 4, "text": "Remove with a slotted spoon and drain on paper towels."},
            {"step": 5, "text": "Season immediately with salt while still warm."},
            {"step": 6, "text": "Store in an airtight container for up to 2 weeks."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "corn", "snack", "fried", "garnish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["indigenous-tacos-sioux-chef"]
    },
    {
        "id": "culinary-ash-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Culinary Ash",
        "native_name": "Čhaȟóta Wóyute",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 182",
        "description": "Culinary ash is made from burned juniper branches or corncobs and is used to add mineral nutrients and a distinctive flavor to blue corn dishes.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "juniper branches or dried corncobs", "quantity": "", "unit": "as needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Burn the juniper branches or corncobs in a fire pit or fireplace until completely reduced to white ash."},
            {"step": 2, "text": "Allow the ash to cool completely."},
            {"step": 3, "text": "Sift the ash through a fine-mesh sieve to remove any large pieces."},
            {"step": 4, "text": "Store in an airtight container in a cool, dry place."},
            {"step": 5, "text": "Use sparingly to season blue corn dishes, add to bread dough, or sprinkle over foods."}
        ],
        "notes": [
            "Culinary ash is traditionally used in Southwestern cooking to help blue corn maintain its color and to add minerals."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "ash", "seasoning", "component", "southwestern"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "dried-apple-slices-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Dried Apple Slices",
        "native_name": "Tȟaspáŋ Pusyápi",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 177",
        "description": "Dried apples are a traditional preserved food that makes a healthy snack or ingredient in recipes.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "apples", "quantity": "", "unit": "as needed"},
            {"item": "lemon juice or maple vinegar (optional, to prevent browning)", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Core the apples and slice into ¼-inch thick rings or slices. Leave the peel on for more fiber."},
            {"step": 2, "text": "If desired, dip the slices in water mixed with a little lemon juice or maple vinegar to prevent browning."},
            {"step": 3, "text": "Arrange the slices in a single layer on dehydrator trays or baking sheets."},
            {"step": 4, "text": "Dry in a food dehydrator at 135°F until leathery but pliable, about 6 to 12 hours. Or dry in a 200°F oven for 2 to 3 hours, flipping halfway through."},
            {"step": 5, "text": "Store in an airtight container in a cool, dry place for up to 6 months."}
        ],
        "temperature": "135°F (57°C) for dehydrator; 200°F (95°C) for oven",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "apple", "dried", "preserved", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["duck-pate-dried-apple-sioux-chef"]
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

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes (batch 10 - teas/pantry)")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
