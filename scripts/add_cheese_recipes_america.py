#!/usr/bin/env python3
"""Add comprehensive American artisan cheese recipes to the cheese category."""

import json

AMERICAN_CHEESE_RECIPES = [
    # === WISCONSIN CHEESES ===
    {
        "id": "colby-cheese-wisconsin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Colby Cheese (Wisconsin Original)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Invented in Colby, Wisconsin in 1885 by Joseph F. Steinwand.",
        "description": "America's first original cheese, created in Wisconsin. Milder and moister than cheddar due to the washed-curd process, with a springy, open texture and sweet, milky flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "1-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "annatto coloring (optional)", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto if using for traditional orange color. Add starter culture, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 30-45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "THE KEY STEP: Drain off whey and replace with same-temperature water. This 'washed curd' technique removes lactose and creates Colby's characteristic mild flavor."},
            {"step": 6, "text": "Stir curds in water for 15 minutes, then drain completely."},
            {"step": 7, "text": "Salt curds and pack into mold without pressing firmly - maintain open texture."},
            {"step": 8, "text": "Press at 20 lbs for 30 min, flip, then 30 lbs for 3-6 hours."},
            {"step": 9, "text": "Air dry 2-3 days until rind forms. Age at 55°F (13°C) for 1-3 months."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Joseph Steinwand created Colby in 1885 at his father's cheese factory",
            "The washed-curd process distinguishes it from cheddar",
            "Traditional Colby is orange from annatto, but white versions exist",
            "Longhorn Colby is simply Colby molded into a half-moon shape"
        ],
        "tags": ["cheese", "American", "Wisconsin", "washed-curd", "original American"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "brick-cheese-wisconsin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Brick Cheese (Wisconsin)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Created in Wisconsin in 1877 by John Jossi, a Swiss immigrant.",
        "description": "Another Wisconsin original, named for its brick shape and the bricks used to press it. Starts mild and sweet, develops pungent, earthy flavors as it ages. Essential for authentic Detroit-style pizza.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 96°F (36°C). Add starter and B. linens culture, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 30 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Stir gently while maintaining 96°F for 30 minutes."},
            {"step": 5, "text": "Drain and ladle into brick-shaped molds."},
            {"step": 6, "text": "Press with actual bricks (traditional) or weights at 15-20 lbs for 12 hours, flipping several times."},
            {"step": 7, "text": "Brine for 24 hours in saturated solution."},
            {"step": 8, "text": "Age at 55-60°F (13-16°C) and 95% humidity. Wash rind with light brine every 2-3 days."},
            {"step": 9, "text": "Ready in 2-3 weeks for mild brick, 2-3 months for strong, pungent brick."}
        ],
        "temperature": "96°F (36°C)",
        "notes": [
            "John Jossi created brick cheese in Dodge County, Wisconsin in 1877",
            "Named both for its shape and the bricks traditionally used to press it",
            "Young brick is mild; aged brick is quite pungent",
            "Detroit-style pizza traditionally uses brick cheese for its buttery melt"
        ],
        "tags": ["cheese", "American", "Wisconsin", "washed-rind", "pizza cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "american-muenster",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "American Muenster",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "American adaptation of Alsatian Munster, developed by German immigrants.",
        "description": "Mild, smooth American cheese with characteristic orange-tinted rind from annatto. Much milder than European Munster, it's a beloved melting cheese for sandwiches and burgers.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp"},
            {"item": "paprika (for rind)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter culture, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Drain and ladle into molds. Press at 10 lbs for 30 min, flip, 15 lbs for 4 hours."},
            {"step": 6, "text": "Brine for 8-12 hours."},
            {"step": 7, "text": "Mix annatto with water and brush on rind, or dust with paprika for orange color."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for 2-4 weeks. May wash with light brine occasionally."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "American Muenster is deliberately milder than French/German originals",
            "The orange rind is cosmetic - annatto or paprika for color",
            "Perfect melting cheese for grilled cheese sandwiches",
            "Wisconsin produces most American Muenster"
        ],
        "tags": ["cheese", "American", "German-style", "mild", "melting cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === CALIFORNIA CHEESES ===
    {
        "id": "dry-jack-california",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Dry Jack (California Aged)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Accidental creation during WWI when Monterey Jack was aged longer.",
        "description": "Born from necessity during WWI when Italian cheese imports stopped, Dry Jack is Monterey Jack aged 7-12 months. Hard, granular, and nutty, it's California's answer to Parmesan.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "7-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "cocoa powder (for rind)", "quantity": "2", "unit": "tbsp"},
            {"item": "black pepper (for rind)", "quantity": "1", "unit": "tbsp"},
            {"item": "vegetable oil (for rind)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Hold at 102°F, stirring until curds are quite firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and press at 30 lbs for 1 hour, flip, 40 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine for 24 hours in saturated solution."},
            {"step": 8, "text": "Air dry 3-5 days. Mix cocoa, pepper, and oil into paste. Rub on rind."},
            {"step": 9, "text": "Age at 55°F (13°C) for minimum 7 months, up to 2 years. Re-coat rind as needed."}
        ],
        "temperature": "88-102°F (31-39°C)",
        "notes": [
            "Created during WWI when Parmesan imports were unavailable",
            "Vella Cheese Company's version is legendary",
            "Traditional cocoa-pepper rind coating is distinctive",
            "Excellent grating cheese with sweet, nutty flavor"
        ],
        "tags": ["cheese", "American", "California", "aged", "grating", "Parmesan-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "teleme-california",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Teleme (California)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Created by Greek immigrants in California, adapted from Touloumotiri.",
        "description": "Uniquely Californian soft cheese with Greek origins. Incredibly creamy and tangy, it becomes almost liquid when ripe. Traditionally coated in rice flour to absorb moisture.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"},
            {"item": "rice flour (for coating)", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60-90 minutes until very soft curd."},
            {"step": 3, "text": "Cut curds into 2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Very gently ladle curds into molds without stirring. Do not press."},
            {"step": 5, "text": "Drain at room temperature 12-24 hours, flipping every 4-6 hours."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Coat all surfaces with rice flour - this is the traditional Teleme finish."},
            {"step": 8, "text": "Age at 50°F (10°C) and high humidity for 2-4 weeks. Re-coat with rice flour as needed."}
        ],
        "temperature": "88°F (31°C)",
        "notes": [
            "Greek immigrants created Teleme in early 1900s California",
            "Rice flour coating is traditional and functional",
            "Becomes incredibly runny when fully ripe",
            "Peluso Cheese Company is the most famous producer"
        ],
        "tags": ["cheese", "American", "California", "Greek-style", "soft", "rice-flour coated"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "humboldt-fog",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Humboldt Fog (Bloomy Ash-Line Goat Cheese)",
        "category": "cheese",
        "attribution": "Cypress Grove Creamery",
        "source_note": "Created by Mary Keehn at Cypress Grove Creamery in Humboldt County, California.",
        "description": "Iconic American goat cheese with a distinctive layer of vegetable ash running through its center. Creamy, tangy, and sophisticated, it put American artisan cheese on the world map.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "3-5 weeks aging",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops"},
            {"item": "vegetable ash", "quantity": "2", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 72°F (22°C). Add starter and both mold cultures. Ripen 1 hour."},
            {"step": 2, "text": "Add rennet (just a few drops). Let set at room temperature 12-18 hours."},
            {"step": 3, "text": "Gently ladle half the curds into molds. Sprinkle vegetable ash evenly across surface."},
            {"step": 4, "text": "Ladle remaining curds on top of ash layer. Do not press."},
            {"step": 5, "text": "Drain at room temperature 24-48 hours, flipping carefully every 8-12 hours."},
            {"step": 6, "text": "Salt surfaces lightly. Dust exterior with vegetable ash."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity for 3-5 weeks until white bloomy rind develops."},
            {"step": 8, "text": "The ash line should remain visible when cut."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Named for the fog that rolls through Humboldt County, California",
            "Mary Keehn started Cypress Grove in 1983",
            "The ash line is purely decorative but visually stunning",
            "One of the most celebrated American artisan cheeses"
        ],
        "tags": ["cheese", "American", "California", "goat cheese", "bloomy rind", "ash-ripened", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === EAST COAST CHEESES ===
    {
        "id": "vermont-cheddar-clothbound",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vermont Cheddar (Clothbound)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Traditional English-style cheddar made in Vermont since the 1800s.",
        "description": "Authentic clothbound cheddar in the English tradition, wrapped in cheesecloth and aged in caves. Sharp, complex, and crumbly with earthy, nutty notes from the natural rind.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "5 hours",
        "total_time": "12-24 months aging",
        "ingredients": [
            {"item": "raw or pasteurized cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"},
            {"item": "cheesecloth", "quantity": "1", "unit": "yard"},
            {"item": "lard or butter (for cloth)", "quantity": "4", "unit": "oz"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Drain whey. Allow curds to mat into a slab. CHEDDARING: Cut slab into strips, stack and flip every 15 minutes for 2 hours. Curds become smooth and chicken-breast-like."},
            {"step": 6, "text": "Mill (cut) cheddared curds into finger-sized pieces. Add salt, mix thoroughly."},
            {"step": 7, "text": "Pack into mold, press at 30 lbs for 1 hour, flip, 50 lbs for 24 hours."},
            {"step": 8, "text": "Rub lard into cheesecloth. Wrap cheese tightly in greased cloth."},
            {"step": 9, "text": "Age at 55°F (13°C) and 80% humidity for 12-24 months. Turn weekly. Mold growth on cloth is normal."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Cheddaring is the key step - stacking and flipping develops texture",
            "Clothbound aging allows the cheese to breathe and develop complex flavors",
            "Cabot, Grafton, and Jasper Hill all make acclaimed Vermont cheddars",
            "The cloth should be larded to prevent excessive moisture loss"
        ],
        "tags": ["cheese", "American", "Vermont", "cheddar", "clothbound", "aged", "English-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jasper-hill-harbison",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Jasper Hill Harbison (Spruce-Wrapped)",
        "category": "cheese",
        "attribution": "Jasper Hill Farm",
        "source_note": "Created by Jasper Hill Farm in Greensboro, Vermont.",
        "description": "Luxurious soft-ripened cheese wrapped in spruce bark. The bark imparts woodsy, sweet flavors while containing the oozy, spoonable interior. A masterpiece of American cheesemaking.",
        "servings_yield": "About 12 oz",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "6-10 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "spruce bark strips (food-safe)", "quantity": "2-3", "unit": "strips"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and mold cultures. Ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently ladle into small molds (4-inch diameter). Do not press."},
            {"step": 5, "text": "Drain at room temperature 24-36 hours, flipping every 8-12 hours."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity for 3-4 weeks until bloomy rind develops."},
            {"step": 8, "text": "When rind is established, wrap cheese with soaked spruce bark strip, securing with string."},
            {"step": 9, "text": "Continue aging 2-4 more weeks. Cheese should become soft and spoonable inside."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Named for Anne Harbison, an early Greensboro settler",
            "Spruce bark must be food-safe and properly prepared",
            "Best eaten by cutting top and spooning out the interior",
            "The bark infuses gentle evergreen notes"
        ],
        "tags": ["cheese", "American", "Vermont", "soft-ripened", "spruce-wrapped", "bloomy rind", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === AMERICAN BLUE CHEESES ===
    {
        "id": "maytag-blue-iowa",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maytag Blue (Iowa)",
        "category": "cheese",
        "attribution": "Maytag Dairy Farms",
        "source_note": "Created in 1941 by Fred Maytag II (of appliance family) in Newton, Iowa.",
        "description": "America's first farmstead blue cheese, created when the Maytag appliance family diversified into dairy. Dense, crumbly, and lemony with bold blue veining. A true American original.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk (preferably Holstein)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60-90 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 30 minutes at 88°F. Curds should remain large and soft."},
            {"step": 5, "text": "Drain and ladle into tall cylindrical molds, salting between layers."},
            {"step": 6, "text": "Do not press. Drain at room temperature 3-5 days, flipping twice daily."},
            {"step": 7, "text": "Pierce with sterilized skewer - create 50+ holes throughout."},
            {"step": 8, "text": "Age at 50°F (10°C) and 95% humidity for 4-6 months. Blue veining should be extensive."}
        ],
        "temperature": "88°F (31°C)",
        "notes": [
            "Fred Maytag II started the dairy when WWII limited appliance production",
            "Uses Iowa State University's culture strain from 1941",
            "Known for its dense, fudgy texture and lemony tang",
            "One of the first American cheeses to win international recognition"
        ],
        "tags": ["cheese", "American", "Iowa", "blue cheese", "farmstead", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "point-reyes-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Point Reyes Blue",
        "category": "cheese",
        "attribution": "Point Reyes Farmstead Cheese Company",
        "source_note": "Created by the Giacomini family in Point Reyes, California.",
        "description": "Coastal California blue cheese with bold, tangy flavor balanced by sweet cream notes. Made from the milk of Holstein cows grazing on the foggy Point Reyes peninsula.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and P. roqueforti, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 15 minutes."},
            {"step": 4, "text": "Gently ladle curds into molds without pressing."},
            {"step": 5, "text": "Drain at room temperature 2-3 days, flipping every 8-12 hours."},
            {"step": 6, "text": "Salt all surfaces liberally."},
            {"step": 7, "text": "Pierce extensively with sterilized needle or skewer."},
            {"step": 8, "text": "Age at 52°F (11°C) and 95% humidity for 3-4 months."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "The Giacomini family has farmed Point Reyes since 1959",
            "Coastal fog and sea air contribute to unique terroir",
            "Won numerous American Cheese Society awards",
            "Balances bold blue flavor with creamy sweetness"
        ],
        "tags": ["cheese", "American", "California", "blue cheese", "farmstead", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "rogue-river-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rogue River Blue (Leaf-Wrapped)",
        "category": "cheese",
        "attribution": "Rogue Creamery",
        "source_note": "Created by Rogue Creamery in Central Point, Oregon. World Cheese Awards winner.",
        "description": "World champion blue cheese wrapped in grape leaves macerated in pear brandy. Seasonal cheese made only in autumn when milk is richest. Fruity, complex, and utterly unique.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "8-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk (autumn milk preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "Syrah grape leaves", "quantity": "6-8", "unit": "leaves"},
            {"item": "pear brandy (Clear Creek preferred)", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Macerate grape leaves in pear brandy for 2-3 months before use."},
            {"step": 2, "text": "Heat autumn milk to 88°F (31°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 75 minutes."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently stir for 30 minutes. Ladle into molds without pressing."},
            {"step": 6, "text": "Drain 3-4 days, flipping twice daily. Salt surfaces."},
            {"step": 7, "text": "Pierce and age at 50°F (10°C) for 3-4 months unwrapped."},
            {"step": 8, "text": "Wrap in brandy-soaked grape leaves, securing with string."},
            {"step": 9, "text": "Continue aging 4-6 more months. The leaves infuse fruity, boozy notes."}
        ],
        "temperature": "88°F (31°C)",
        "notes": [
            "Won World's Best Cheese at 2019 World Cheese Awards",
            "Only made September through December when milk is richest",
            "Syrah grape leaves from local Rogue Valley vineyards",
            "Clear Creek pear brandy is traditional"
        ],
        "tags": ["cheese", "American", "Oregon", "blue cheese", "leaf-wrapped", "seasonal", "award-winning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ALPINE-STYLE AMERICAN CHEESES ===
    {
        "id": "pleasant-ridge-reserve",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pleasant Ridge Reserve (Alpine-Style)",
        "category": "cheese",
        "attribution": "Uplands Cheese Company",
        "source_note": "Created by Mike Gingrich and Dan Patenaude in Dodgeville, Wisconsin.",
        "description": "America's most-awarded cheese, made only when cows graze on pasture (May-October). Alpine-style raw milk cheese with complex, grassy, nutty flavors that change throughout the season.",
        "servings_yield": "About 10 lbs (traditional wheel)",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "12-18 months aging",
        "ingredients": [
            {"item": "raw cow's milk (pasture-grazed)", "quantity": "5", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Propionibacterium (optional)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use only pasture-grazed raw milk for authentic flavor. Heat to 92°F (33°C)."},
            {"step": 2, "text": "Add thermophilic starter and optional propioni. Ripen 20 minutes."},
            {"step": 3, "text": "Raise to 95°F (35°C). Add calcium chloride, then rennet. Let set 35 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces (rice-sized). Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 125°F (52°C) over 45 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at 125°F and stir until curds are very firm, about 45 minutes more."},
            {"step": 7, "text": "Drain and press immediately at 40 lbs for 30 min, flip, 60 lbs for 24 hours."},
            {"step": 8, "text": "Brine for 48 hours in saturated solution."},
            {"step": 9, "text": "Age at 55°F (13°C) and 95% humidity for 12-18 months. Wash and flip 3x weekly initially, then weekly."}
        ],
        "temperature": "92-125°F (33-52°C)",
        "notes": [
            "Only made May-October when cows graze on pasture",
            "Has won American Cheese Society Best of Show 4 times - more than any other cheese",
            "Based on French Beaufort tradition",
            "Each wheel reflects the specific pasture rotation of that week"
        ],
        "tags": ["cheese", "American", "Wisconsin", "Alpine-style", "raw milk", "pasture-grazed", "award-winning"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === TRIPLE CREAM AMERICAN ===
    {
        "id": "cowgirl-creamery-mt-tam",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cowgirl Creamery Mt Tam (Triple Cream)",
        "category": "cheese",
        "attribution": "Cowgirl Creamery",
        "source_note": "Created by Sue Conley and Peggy Smith at Point Reyes Station, California.",
        "description": "Luscious triple-cream cheese named for nearby Mount Tamalpais. Made with organic Straus Family milk, it's buttery, mushroomy, and melts on the tongue. An icon of California artisan cheese.",
        "servings_yield": "About 12 oz",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "3-5 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and heavy cream for high butterfat content (triple cream is 75%+ fat in dry matter)."},
            {"step": 2, "text": "Heat to 72°F (22°C). Add starter and mold cultures. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 12-18 hours until soft curd."},
            {"step": 4, "text": "Very gently ladle into molds. Do not disturb curds more than necessary."},
            {"step": 5, "text": "Drain at room temperature 24-36 hours, flipping very carefully every 8-12 hours."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity for 3-5 weeks until bloomy rind develops fully."},
            {"step": 8, "text": "Interior should become oozy and soft when ripe."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Named for Mount Tamalpais in Marin County",
            "Sue Conley and Peggy Smith founded Cowgirl in 1997",
            "Triple cream means 75%+ butterfat in dry matter",
            "Serve at room temperature for best texture"
        ],
        "tags": ["cheese", "American", "California", "triple cream", "bloomy rind", "organic", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === FRESH AMERICAN CHEESES ===
    {
        "id": "cheese-curds-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Curds (Fresh, Squeaky)",
        "category": "cheese",
        "attribution": "Traditional American cheese",
        "source_note": "Fresh cheese curds, beloved in Wisconsin and Quebec for their squeak.",
        "description": "The freshest possible cheese - curds before they're pressed into wheels. The characteristic 'squeak' against teeth only lasts 12-24 hours. Essential for authentic poutine.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain whey. Let curds mat together for 15 minutes."},
            {"step": 6, "text": "Cut matted curds into strips. Stack and flip every 15 minutes (cheddaring) for 1-2 hours until smooth and shiny."},
            {"step": 7, "text": "Cut cheddared curds into bite-sized pieces. Salt while still warm."},
            {"step": 8, "text": "EAT IMMEDIATELY for maximum squeak! Best within 12 hours."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "The squeak is caused by protein structure and disappears as curds age",
            "Wisconsin cheese curds are a beloved snack and state icon",
            "Also essential for authentic Quebec poutine",
            "Fried cheese curds are a state fair classic"
        ],
        "tags": ["cheese", "American", "Wisconsin", "fresh", "curds", "squeaky", "poutine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === MEXICAN-AMERICAN CHEESES ===
    {
        "id": "queso-oaxaca-string",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Oaxaca (String Cheese)",
        "category": "cheese",
        "attribution": "Traditional Mexican cheese",
        "source_note": "From Oaxaca, Mexico - similar to mozzarella, wound into balls.",
        "description": "Mexican string cheese with excellent melting properties. Like mozzarella, it's a pasta filata (stretched curd) cheese, but wound into a distinctive ball shape. Essential for quesadillas.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup cool water. Add to cold milk, stir well."},
            {"step": 2, "text": "Heat milk to 90°F (32°C) while stirring gently."},
            {"step": 3, "text": "Add rennet diluted in water. Stir 30 seconds, then stop. Let set 10 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Heat slowly to 105°F (41°C) while stirring gently."},
            {"step": 6, "text": "Drain whey. Heat water to 170°F (77°C)."},
            {"step": 7, "text": "Add curds to hot water. When stretchy, pull into long ribbons or ropes."},
            {"step": 8, "text": "Salt while stretching. Wind ribbons into a ball shape."},
            {"step": 9, "text": "Cool in ice water. Use immediately or refrigerate up to 1 week."}
        ],
        "temperature": "90-170°F (32-77°C)",
        "notes": [
            "Also called quesillo - 'little cheese'",
            "Pull into long ribbons for authentic appearance",
            "Winds into ball like a ball of yarn",
            "Essential for authentic quesadillas and tlayudas"
        ],
        "tags": ["cheese", "American", "Mexican", "pasta filata", "string cheese", "melting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-chihuahua-menonita",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Chihuahua (Mexican Mennonite)",
        "category": "cheese",
        "attribution": "Traditional Mexican cheese",
        "source_note": "Created by Mennonite communities who settled in Chihuahua, Mexico in 1920s.",
        "description": "Mild, buttery Mexican cheese created by Mennonite immigrants. Similar to young cheddar or Colby, it melts beautifully and is the traditional cheese for queso fundido and chile rellenos.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain some whey, add same-temperature water (washed-curd for mild flavor)."},
            {"step": 6, "text": "Stir 15 more minutes, then drain completely."},
            {"step": 7, "text": "Salt curds, pack into mold. Press at 15 lbs for 30 min, flip, 25 lbs for 6-8 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-4 weeks. Can eat fresh or aged."}
        ],
        "temperature": "88-100°F (31-38°C)",
        "notes": [
            "Mennonites from Canada settled in Chihuahua in 1922",
            "Also called Queso Menonita",
            "Washed-curd technique gives mild, sweet flavor",
            "The cheese of choice for queso fundido"
        ],
        "tags": ["cheese", "American", "Mexican", "Mennonite", "melting", "mild"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cotija-mexican-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cotija (Mexican Aged)",
        "category": "cheese",
        "attribution": "Traditional Mexican cheese",
        "source_note": "Named for the town of Cotija in Michoacan, Mexico.",
        "description": "Mexico's Parmesan - a hard, salty, crumbly cheese for grating and finishing. Young cotija is softer; aged cotija (anejo) is hard and intensely flavored. Essential for elotes and tacos.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (coarse)", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes - small for hard cheese. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F (41°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Continue stirring at temperature until curds are quite firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and salt heavily - cotija is a salty cheese."},
            {"step": 7, "text": "Press at 30 lbs for 1 hour, flip, 50 lbs for 24 hours."},
            {"step": 8, "text": "Air dry 1 week, then age at 55°F (13°C) for 3-12 months."},
            {"step": 9, "text": "Young cotija (3 months) crumbles; aged cotija (anejo, 12 months) grates."}
        ],
        "temperature": "90-105°F (32-41°C)",
        "notes": [
            "Named for Cotija de la Paz in Michoacan",
            "Traditional cotija is made from raw milk during rainy season",
            "Very salty - the 'Mexican Parmesan'",
            "Essential crumbled on elotes (street corn) and tacos"
        ],
        "tags": ["cheese", "American", "Mexican", "aged", "grating", "salty", "crumbly"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-panela-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Panela (Mexican Fresh)",
        "category": "cheese",
        "attribution": "Traditional Mexican cheese",
        "source_note": "Fresh Mexican cheese named for the basket (panela) molds it's made in.",
        "description": "Fresh, mild Mexican cheese that softens when heated but doesn't melt. Its basket-weave texture comes from traditional draining molds. Perfect for grilling and salads.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day to 2 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes at 90°F."},
            {"step": 5, "text": "Ladle curds into basket-weave molds (or regular molds). Do not press - drain naturally."},
            {"step": 6, "text": "Flip every 30 minutes for first 2 hours, then let drain 4-8 hours total."},
            {"step": 7, "text": "Salt all surfaces."},
            {"step": 8, "text": "Refrigerate and eat within 1 week. Best within 2-3 days."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Panela means 'little basket' - refers to traditional molds",
            "Softens when heated but does not melt",
            "Can be grilled or pan-fried - holds its shape",
            "Mild, milky flavor perfect for fresh applications"
        ],
        "tags": ["cheese", "American", "Mexican", "fresh", "non-melting", "basket-weave"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add American artisan cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in AMERICAN_CHEESE_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"Skipping existing: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"Added: {recipe['title']}")
            added += 1

    data['recipes'] = recipes

    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Added: {added} recipes")
    print(f"Skipped (existing): {skipped}")
    print(f"Total recipes now: {len(recipes)}")


if __name__ == '__main__':
    add_recipes()
