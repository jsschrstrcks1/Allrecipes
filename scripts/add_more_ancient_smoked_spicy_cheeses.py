#!/usr/bin/env python3
"""Add more ancient, smoked, and super-hot pepper cheese recipes to recipes.json"""

import json

# Load existing recipes
with open('data/recipes.json', 'r') as f:
    data = json.load(f)

new_recipes = [
    # ==================== ANCIENT CHEESES ====================
    {
        "id": "ancient-egyptian-halom",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ancient Egyptian Halom (Proto-Halloumi)",
        "category": "sides",
        "attribution": "Ancient Egyptian tradition",
        "source_note": "Reconstructed from archaeological findings at Saqqara and historical records. Cheese similar to this was found in the tomb of Ptahmes (13th century BCE) and later discoveries from the 26th Dynasty (664-525 BCE).",
        "description": "A fresh cheese inspired by ancient Egyptian cheesemaking, ancestor to modern halloumi. Archaeological evidence shows Egyptians made cheese from mixed goat, sheep, and cow milk over 3,000 years ago.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "goat's milk", "quantity": "1", "unit": "quart"},
            {"item": "sheep's milk", "quantity": "1", "unit": "quart"},
            {"item": "cow's milk", "quantity": "1", "unit": "quart", "prep_note": "optional, or use more goat/sheep"},
            {"item": "lemon juice or vinegar", "quantity": "3", "unit": "tbsp", "prep_note": "as coagulant"},
            {"item": "salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks in a large pot. Ancient Egyptians used a mixture of goat, sheep, and sometimes cow or buffalo milk."},
            {"step": 2, "text": "Heat milk slowly to 185°F (85°C), stirring frequently to prevent scorching."},
            {"step": 3, "text": "Remove from heat and add lemon juice or vinegar. Stir gently."},
            {"step": 4, "text": "Let sit undisturbed for 15-20 minutes as curds form."},
            {"step": 5, "text": "Line a colander with cheesecloth. Gently ladle curds into the cloth."},
            {"step": 6, "text": "Gather edges of cheesecloth and hang to drain for 1 hour."},
            {"step": 7, "text": "Add salt and knead gently to distribute."},
            {"step": 8, "text": "Press into a mold or form by hand. Refrigerate."},
            {"step": 9, "text": "Best consumed fresh within 3-5 days, as the ancients did."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "The word 'halloumi' derives from the ancient Egyptian word 'halom' for cheese",
            "3,200-year-old cheese was discovered in the tomb of Ptahmes at Saqqara",
            "Ancient Egyptians stored cheese in clay jars, sometimes with herbs",
            "This cheese would have had a 'really, really acidy bite' according to cheese historians"
        ],
        "tags": ["cheese", "ancient", "Egyptian", "historical", "fresh cheese", "halloumi"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "polyphemus-greek-feta-odyssey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Polyphemus Greek Feta (Odyssey-Style)",
        "category": "sides",
        "attribution": "Ancient Greek tradition",
        "source_note": "Based on Homer's Odyssey (8th century BCE), which describes Polyphemus the Cyclops making cheese from sheep and goat milk in woven baskets.",
        "description": "The oldest recorded cheese recipe in Western literature, described in Homer's Odyssey. Polyphemus stored his cheese in woven baskets and aged it on racks in his cave - the precursor to modern feta.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "24 hours draining + 3 days brining",
        "total_time": "4 days",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "traditional, or use goat"},
            {"item": "goat's milk", "quantity": "1", "unit": "quart", "prep_note": "optional addition"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or 1/4 cup cultured buttermilk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add culture and stir gently. Ripen 1 hour."},
            {"step": 2, "text": "Dilute rennet in 1/4 cup cool water. Add to milk and stir gently for 1 minute."},
            {"step": 3, "text": "Let set undisturbed for 1 hour until clean break achieved."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Gently stir curds for 20 minutes to release whey."},
            {"step": 6, "text": "Line a basket or colander with cheesecloth (Greeks used woven reed baskets)."},
            {"step": 7, "text": "Ladle curds into basket. Let drain at room temperature for 24 hours, flipping every 6 hours."},
            {"step": 8, "text": "Cut drained cheese into blocks. Salt all surfaces liberally."},
            {"step": 9, "text": "Prepare brine: dissolve 1/2 cup salt in 1/2 gallon water."},
            {"step": 10, "text": "Submerge cheese blocks in brine. Age at 50-55°F (10-13°C) for minimum 3 days."},
            {"step": 11, "text": "For authentic aging, store in brine for 2-3 months in a cool cellar or cave."}
        ],
        "temperature": "86°F (30°C) for make, 50-55°F (10-13°C) for aging",
        "notes": [
            "Homer's Odyssey describes Polyphemus curdling milk and storing cheese in woven baskets",
            "The name 'feta' (meaning 'slice') wasn't used until the 17th century",
            "Greeks traditionally aged feta in wooden barrels or cool caves",
            "Authentic Greek feta must be made from sheep's milk or sheep/goat blend"
        ],
        "tags": ["cheese", "ancient", "Greek", "historical", "feta", "brined", "Odyssey"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "medieval-port-salut-trappist",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Medieval Port-Salut (Trappist Monastery Cheese)",
        "category": "sides",
        "attribution": "Trappist monastic tradition",
        "source_note": "Based on the cheese developed by Trappist monks at Notre Dame du Port-du-Salut abbey in France, perfected 1815-1873. Recipe from cheesemaking.com and Culture Cheese Magazine.",
        "description": "A semi-soft washed-rind cheese developed by French Trappist monks, meaning 'Gates of Salvation.' The signature orange rind develops through repeated brine washes that encourage beneficial bacteria.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 weeks aging",
        "total_time": "3-6 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "red bacteria culture"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": "for B. linens solution"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add mesophilic culture and stir. Ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using, then rennet diluted in 1/4 cup cool water."},
            {"step": 3, "text": "Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "CURD WASHING: Remove 2.5 quarts whey, replace with 5 cups warm water at 100°F."},
            {"step": 6, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes while stirring gently."},
            {"step": 7, "text": "Maintain 100°F for 30 minutes. Curds should mat when pressed."},
            {"step": 8, "text": "Drain whey. Pack curds into mold lined with cheesecloth."},
            {"step": 9, "text": "Press with light weight (half-gallon jar half-full of water) for 10 minutes."},
            {"step": 10, "text": "Flip and press with increasing weight over 24 hours, flipping at 30 min, 2 hrs, 4 hrs."},
            {"step": 11, "text": "Air dry at room temperature for 24 hours, turning several times."},
            {"step": 12, "text": "DEVELOP RIND: Mix B. linens and 1/4 tsp salt in 1 quart water. Let sit 16 hours."},
            {"step": 13, "text": "Move cheese to 50-55°F (10-13°C) aging space at 90% humidity."},
            {"step": 14, "text": "Spray B. linens solution on cheese every 3rd day for first 10 days."},
            {"step": 15, "text": "After 2 weeks, brush off any mold under running water. Continue aging 3-6 weeks."}
        ],
        "temperature": "90-100°F (32-38°C) for make, 50-55°F (10-13°C) for aging",
        "notes": [
            "The monks of Notre Dame du Port-du-Salut perfected this cheese over 50 years",
            "B. linens bacteria creates the signature orange rind and complex flavor",
            "High moisture curd and repeated brine washes are key to authentic Port-Salut",
            "Commercial versions today use orange dye instead of traditional bacterial ripening",
            "70% of France's 1,200 cheese varieties originated in monasteries"
        ],
        "tags": ["cheese", "medieval", "Trappist", "monastery", "washed rind", "semi-soft", "French"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ==================== CAUCASUS SMOKED CHEESES ====================
    {
        "id": "georgian-sulguni-stretched-curd",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Georgian Sulguni (Caucasus Stretched-Curd)",
        "category": "sides",
        "attribution": "Traditional Georgian (Samegrelo region)",
        "source_note": "Traditional Georgian cheese from the Samegrelo region. Recipe compiled from Georgian Recipes, Food Perestroika, and Cheesemaking.com.",
        "description": "A centuries-old brined stretched-curd cheese from Georgia, similar to mozzarella but with a firmer, layered texture and tangy flavor. Essential for khachapuri and other Georgian dishes.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "2 hours",
        "cook_time": "1-2 days aging",
        "total_time": "2 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or buffalo milk traditionally"},
            {"item": "cultured buttermilk", "quantity": "1/4", "unit": "cup", "prep_note": "for tangy starter"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine (17-18% concentration)"}
        ],
        "instructions": [
            {"step": 1, "text": "Night before: Inoculate 3/4 cup milk with 4 tsp buttermilk. Leave in warm place overnight."},
            {"step": 2, "text": "Heat milk to 95°F (35°C). Add the overnight starter and stir."},
            {"step": 3, "text": "Add rennet diluted in 1/4 cup water. Stir gently for 1 minute."},
            {"step": 4, "text": "Let set 30-45 minutes until clean break. Cut curds into 1-inch cubes."},
            {"step": 5, "text": "CHEDDAR the curds: Let them sit in whey at 95°F for up to 5 hours, stirring occasionally."},
            {"step": 6, "text": "Test for stretch: Take a small piece of curd, dip in 175°F water - it should stretch."},
            {"step": 7, "text": "Cut cheddared curd into 1-2 cm strips. Heat water to 175-180°F (80-82°C)."},
            {"step": 8, "text": "WEAR HEAT-RESISTANT GLOVES. Drop curd strips into hot water for 30 seconds."},
            {"step": 9, "text": "Stretch and knead the curds, returning to hot water as needed, until smooth and elastic."},
            {"step": 10, "text": "Salt the stretched mass (about 2 tsp per lb). Fold over itself 12-16 times."},
            {"step": 11, "text": "Form into a ball by tucking edges underneath. Place in mold to cool."},
            {"step": 12, "text": "Prepare brine: 1/4 cup salt per quart water (17-18%). Submerge cheese."},
            {"step": 13, "text": "Brine at 46-54°F (8-12°C) for 6-48 hours. Ready to eat or smoke."}
        ],
        "temperature": "95°F (35°C) for curd, 175-180°F (80-82°C) for stretching",
        "notes": [
            "Sulguni means 'pickled cheese' in Georgian due to the brining process",
            "The cheddaring step develops the tangy, sour flavor characteristic of sulguni",
            "Traditionally made from cow or water buffalo milk in the Samegrelo region",
            "Essential for khachapuri (Georgian cheese bread) - melts beautifully"
        ],
        "tags": ["cheese", "Georgian", "Caucasus", "stretched curd", "pasta filata", "sulguni", "brined"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "smoked-sulguni-georgian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Sulguni (Georgian Smoked Cheese)",
        "category": "sides",
        "attribution": "Traditional Georgian (Samegrelo region)",
        "source_note": "Smoked version of traditional Georgian sulguni. Smoking method from Food Perestroika.",
        "description": "Golden-colored smoked version of Georgian sulguni, with a firm exterior and smoky-tangy flavor. A popular appetizer cheese throughout the Caucasus region.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "Make sulguni first (2 hours)",
        "cook_time": "2 min smoke + 3 days rest",
        "total_time": "4+ days (including base cheese)",
        "ingredients": [
            {"item": "fresh sulguni cheese", "quantity": "1.5", "unit": "lbs", "prep_note": "see Georgian Sulguni recipe"},
            {"item": "wood chips", "quantity": "1/4", "unit": "cup", "prep_note": "applewood, hickory, or alder"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with finished sulguni that has been brined for at least 24 hours."},
            {"step": 2, "text": "Remove sulguni from brine and pat completely dry with paper towels."},
            {"step": 3, "text": "Let cheese air dry at room temperature for 2-4 hours until surface is tacky."},
            {"step": 4, "text": "Place sulguni on a rack that fits inside a large bowl or container."},
            {"step": 5, "text": "Using a smoking gun, load with your preferred wood chips."},
            {"step": 6, "text": "Cover the setup with plastic wrap to contain smoke."},
            {"step": 7, "text": "Light smoking gun and fill container with smoke. Let permeate for 2 minutes."},
            {"step": 8, "text": "Remove plastic and let cheese rest uncovered for 10 minutes."},
            {"step": 9, "text": "Wrap cheese and refrigerate for at least 3 days for smoke flavor to penetrate evenly."}
        ],
        "temperature": "Cold smoke only - below 90°F (32°C)",
        "notes": [
            "Traditional smoking uses beech or fruit woods",
            "The resting period is essential - fresh smoked cheese tastes acrid",
            "Color changes from white to golden-yellow after smoking",
            "Can be stored in brine after smoking for extended preservation"
        ],
        "tags": ["cheese", "Georgian", "Caucasus", "smoked", "cold smoked", "sulguni"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "armenian-chechil-string-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Armenian Chechil (Braided String Cheese)",
        "category": "sides",
        "attribution": "Traditional Armenian/Georgian",
        "source_note": "Traditional Caucasus string cheese from Armenia and Georgia. Recipe from The Armenian Kitchen and Chechil USA.",
        "description": "A pasta filata-style cheese pulled into thin strings and braided into decorative ropes. The name means 'that which unravels' in Georgian. Popular as a beer snack throughout the Caucasus.",
        "servings_yield": "About 1 lb (several braids)",
        "prep_time": "2 hours",
        "cook_time": "Overnight drying",
        "total_time": "24 hours",
        "ingredients": [
            {"item": "fresh mozzarella curd", "quantity": "2", "unit": "lbs", "prep_note": "from Italian market or pizzeria, or make your own"},
            {"item": "mahlab", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, ground cherry pit spice"},
            {"item": "nigella seeds", "quantity": "2", "unit": "tsp", "prep_note": "optional, for coating"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "for salting braids"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat water to 175-180°F (80-82°C) in a large pot."},
            {"step": 2, "text": "Cut mozzarella curd into 1-inch strips."},
            {"step": 3, "text": "WEAR HEAT-RESISTANT GLOVES. Drop curd strips into hot water for 30 seconds."},
            {"step": 4, "text": "Stretch test: Pinch and pull - curd should stretch without breaking."},
            {"step": 5, "text": "Work quickly as cheese cools fast. Make a hole in center like a doughnut."},
            {"step": 6, "text": "Using both hands, stretch cheese in opposite directions to form a large loop."},
            {"step": 7, "text": "Double the strand, stretch again. Loop and twist. Repeat until very stringy."},
            {"step": 8, "text": "Twist ends in opposite directions to create a rope."},
            {"step": 9, "text": "Intertwine into a braid. Thread one end through the other loop to secure."},
            {"step": 10, "text": "Place braids in container. Sprinkle tops with salt and pat in gently."},
            {"step": 11, "text": "If using mahlab, knead into the warm curd before stretching."},
            {"step": 12, "text": "Let dry overnight at room temperature, uncovered."},
            {"step": 13, "text": "Refrigerate until firm. Wrap individually in plastic wrap."}
        ],
        "temperature": "175-180°F (80-82°C) for stretching",
        "notes": [
            "'Chechil' means 'that separates into threads' in Armenian",
            "The more you stretch, the stringier the cheese becomes",
            "Traditionally stored in brine in clay pots",
            "Mahlab (ground cherry pit) adds a subtle almond-cherry flavor",
            "Popular beer snack throughout Armenia, Georgia, and Russia"
        ],
        "tags": ["cheese", "Armenian", "Georgian", "Caucasus", "string cheese", "braided", "pasta filata"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "smoked-chechil-armenian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Chechil (Armenian Smoked Braided Cheese)",
        "category": "sides",
        "attribution": "Traditional Armenian",
        "source_note": "Smoked version of traditional Armenian chechil. From Chechil USA and traditional Caucasus methods.",
        "description": "Hickory-smoked braided string cheese, a beloved beer snack and appetizer. The smoking intensifies the salty-tangy flavor and adds a golden color to the distinctive braids.",
        "servings_yield": "About 1 lb",
        "prep_time": "Make chechil first",
        "cook_time": "4-6 hours cold smoke + 1 week rest",
        "total_time": "1 week+",
        "ingredients": [
            {"item": "chechil braids", "quantity": "1", "unit": "lb", "prep_note": "see Armenian Chechil recipe"},
            {"item": "hickory wood chips", "quantity": "2", "unit": "cups", "prep_note": "or applewood"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with finished chechil braids that have dried overnight."},
            {"step": 2, "text": "If braids were refrigerated, bring to room temperature (2 hours)."},
            {"step": 3, "text": "Set up cold smoker - temperature must stay below 90°F (32°C)."},
            {"step": 4, "text": "Use pellet tube or smoking gun to generate smoke without heat."},
            {"step": 5, "text": "Hang braids or place on rack in smoker with good air circulation."},
            {"step": 6, "text": "Cold smoke for 4-6 hours, rotating halfway for even coverage."},
            {"step": 7, "text": "Remove from smoker. The cheese will look darker golden."},
            {"step": 8, "text": "Wrap in parchment paper and refrigerate for at least 1 week."},
            {"step": 9, "text": "The resting period allows smoke flavor to mellow and penetrate evenly."}
        ],
        "temperature": "Below 90°F (32°C) - cold smoke only",
        "notes": [
            "Hickory is traditional but applewood or alder also work well",
            "Fresh smoked cheese tastes harsh - resting is essential",
            "The braided shape creates more surface area for smoke absorption",
            "Will keep refrigerated for several weeks; freezes well"
        ],
        "tags": ["cheese", "Armenian", "Caucasus", "smoked", "cold smoked", "string cheese", "braided"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ==================== AFRICAN TRADITIONAL CHEESES ====================
    {
        "id": "ethiopian-ayib-fresh-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ethiopian Ayib (Fresh Cottage Cheese)",
        "category": "sides",
        "attribution": "Traditional Ethiopian",
        "source_note": "Traditional Ethiopian fresh cheese. Recipes from Tara's Multicultural Table, Girl Cooks World, and Brundo Spice Company.",
        "description": "A mild, fresh Ethiopian cheese similar to ricotta or cottage cheese. Served as a cooling counterbalance to spicy dishes like Doro Wat. Not aged - meant to be consumed fresh.",
        "servings_yield": "About 1 lb",
        "prep_time": "10 min",
        "cook_time": "30 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "not UHT/ultra-pasteurized"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": "freshly squeezed"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "onion juice", "quantity": "1", "unit": "tbsp", "prep_note": "optional, strained from grated onion"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in a large pot until steaming and frothy, about 180°F (82°C). Do not boil."},
            {"step": 2, "text": "Remove from heat. Slowly stir in freshly squeezed lemon juice."},
            {"step": 3, "text": "Let sit undisturbed for 10-15 minutes. Curds will separate from whey."},
            {"step": 4, "text": "Line a colander with cheesecloth. Gently ladle curds into the cloth."},
            {"step": 5, "text": "Let drain for 20 minutes to 1 hour depending on desired moisture level."},
            {"step": 6, "text": "Transfer to a bowl. Add salt and mix gently."},
            {"step": 7, "text": "Optional traditional method: Moisten with strained onion juice for authentic flavor."},
            {"step": 8, "text": "Serve immediately or refrigerate for up to 5 days."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Ayib is traditionally made from the remaining yogurt after making butter (ensera)",
            "Do not use UHT milk - the ultra-high heat prevents proper curd formation",
            "The onion juice addition mimics the flavor of traditional ensera-made ayib",
            "Serve alongside injera and spicy stews to cool the palate",
            "Similar in texture to ricotta or dry cottage cheese"
        ],
        "tags": ["cheese", "Ethiopian", "African", "fresh cheese", "ayib", "cottage cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "west-african-wagashi-fulani",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "West African Wagashi (Fulani Cheese)",
        "category": "sides",
        "attribution": "Traditional Fulani (West Africa)",
        "source_note": "Traditional cheese of the Fulani people, made across Ghana, Nigeria, Benin, Togo, Burkina Faso, and Cote d'Ivoire. Recipe from Fafa Gilbert and Savourous.",
        "description": "A firm fresh cheese introduced to West Africa by the Fulani herders. Traditionally coagulated with leaves of the Apple of Sodom plant. Often fried and served with pepper sauce.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "fresh cow's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "raw is traditional, pasteurized works"},
            {"item": "distilled white vinegar", "quantity": "3", "unit": "tbsp", "prep_note": "or Apple of Sodom leaves if available"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh milk to 180°F (82°C), stirring frequently."},
            {"step": 2, "text": "Traditional method: Add pounded Apple of Sodom (Calotropis procera) leaves or branches."},
            {"step": 3, "text": "Modern method: Add distilled white vinegar slowly while stirring."},
            {"step": 4, "text": "Stir gently until curds form and separate from whey."},
            {"step": 5, "text": "Line a colander with cheesecloth. Pour curds and whey through."},
            {"step": 6, "text": "Gather cloth edges and squeeze gently to remove excess whey."},
            {"step": 7, "text": "Add salt and mix through the curds."},
            {"step": 8, "text": "Press into a mold or shape by hand into a flat disc or rectangle."},
            {"step": 9, "text": "Let set at room temperature for a few hours until firm."},
            {"step": 10, "text": "For tangy flavor: Leave at cool room temperature (not fridge) overnight before frying."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Called wagasi in Dendi, amo in Fon, wara in Nago, and gasaru in Bariba",
            "The Fulani people traditionally use Apple of Sodom plant as coagulant",
            "Using plant branches instead of leaves keeps the cheese pure white",
            "Similar texture to halloumi or firm tofu - holds shape when fried",
            "Traditionally fried and served with hot pepper sauce (shitor) as a snack"
        ],
        "tags": ["cheese", "West African", "Fulani", "wagashi", "fresh cheese", "Ghana", "Nigeria", "Benin"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ==================== SUPER-HOT PEPPER CHEESES ====================
    {
        "id": "habanero-jack-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Habanero Jack Cheese",
        "category": "sides",
        "attribution": "Modern artisan cheesemaking",
        "source_note": "Hot pepper cheese using habaneros (100,000-350,000 Scoville). Technique from cheesemaking.com and The Hot Pepper forum.",
        "description": "A creamy Monterey Jack infused with fiery habanero peppers. The high-fat cheese mellows the fruity heat of the habaneros over aging. Serious heat for spice lovers.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized, high-fat preferred"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "habanero peppers", "quantity": "2-3", "unit": "medium", "prep_note": "blanched, seeded if less heat desired"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "SAFETY: Wear gloves when handling habaneros. Avoid touching face or eyes."},
            {"step": 2, "text": "BLANCH PEPPERS: Boil habaneros for 2 minutes to eliminate botulism risk. Cool and chop finely."},
            {"step": 3, "text": "Heat milk to 90°F (32°C). Add mesophilic culture and stir. Ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if using, then rennet diluted in 1/4 cup water."},
            {"step": 5, "text": "Let set 45-60 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 7, "text": "COLD WATER WASH: Remove 1/3 of whey. Replace with same amount cold water."},
            {"step": 8, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes, stirring gently."},
            {"step": 9, "text": "Maintain 100°F for 30 minutes. Curds should be firm when squeezed."},
            {"step": 10, "text": "Drain whey. Add salt and blanched habaneros to curds. Mix thoroughly."},
            {"step": 11, "text": "Pack into mold. Press at 10 lbs for 15 minutes."},
            {"step": 12, "text": "Flip and press at 20 lbs for 12 hours."},
            {"step": 13, "text": "Air dry 2-3 days until surface is dry. Wax or vacuum seal."},
            {"step": 14, "text": "Age at 55°F (13°C) for 2-3 months. Heat mellows and melds over time."}
        ],
        "temperature": "90-100°F (32-38°C) for make, 55°F (13°C) for aging",
        "notes": [
            "Habaneros are 100,000-350,000 Scoville units - hot but not extreme",
            "ALWAYS blanch fresh peppers before adding to cheese to prevent botulism",
            "Cold water wash creates a sweeter, moister cheese that pairs well with peppers",
            "High-fat milk helps mellow the pepper heat during aging",
            "Start with 2 peppers for first batch - adjust next time if desired"
        ],
        "tags": ["cheese", "habanero", "spicy", "hot pepper", "Jack cheese", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "trinidad-scorpion-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Trinidad Scorpion Cheddar",
        "category": "sides",
        "attribution": "Modern artisan cheesemaking",
        "source_note": "Extreme heat cheese using Trinidad Moruga Scorpion (1.2-2 million Scoville). Inspired by Pepper Joe's commercial version.",
        "description": "One of the hottest cheeses possible, infused with Trinidad Moruga Scorpion peppers - once the world's hottest. The scorpion's stinger-shaped tail delivers delayed, intense, fruity heat.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "Trinidad Scorpion peppers", "quantity": "1-2", "unit": "dried", "prep_note": "ground to powder"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "EXTREME CAUTION: Wear gloves, eye protection, and work in ventilated area. Scorpion pepper powder is extremely irritating."},
            {"step": 2, "text": "Grind dried Trinidad Scorpion peppers to fine powder in dedicated spice grinder."},
            {"step": 3, "text": "Heat milk to 90°F (32°C). Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if using, then rennet. Stir gently."},
            {"step": 5, "text": "Let set 45-60 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 7, "text": "Slowly raise to 102°F (39°C) over 30 minutes, stirring gently."},
            {"step": 8, "text": "Maintain 102°F for 30 minutes, stirring every 5 minutes."},
            {"step": 9, "text": "Drain whey. Mill curds into walnut-sized pieces."},
            {"step": 10, "text": "Add salt and Scorpion powder. Mix thoroughly with gloved hands."},
            {"step": 11, "text": "Pack into mold. Press at 10 lbs for 15 min, flip, 20 lbs for 12 hours."},
            {"step": 12, "text": "Air dry 2-3 days until rind forms. Wax or vacuum seal."},
            {"step": 13, "text": "Age at 55°F (13°C) for minimum 3 months. 6+ months for mellower heat."}
        ],
        "temperature": "90-102°F (32-39°C) for make, 55°F (13°C) for aging",
        "notes": [
            "Trinidad Moruga Scorpion reaches 1,200,000-2,009,231 Scoville units",
            "Was world's hottest pepper 2012-2013 before Carolina Reaper",
            "Named for the pointed tail resembling a scorpion's stinger",
            "START WITH ONE PEPPER - this heat level is extreme",
            "Longer aging mellows the heat and develops complexity"
        ],
        "tags": ["cheese", "Trinidad Scorpion", "super-hot", "extreme heat", "cheddar", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "seven-pot-douglah-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "7 Pot Douglah Gouda",
        "category": "sides",
        "attribution": "Modern artisan cheesemaking",
        "source_note": "Extreme heat gouda using 7 Pot Douglah pepper (1.8 million Scoville). Named because one pepper can heat 7 pots of stew.",
        "description": "A creamy gouda infused with the legendary 7 Pot Douglah, one of the world's hottest peppers with a distinctive chocolate-brown color and fruity, slightly nutty heat.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-4 months aging",
        "total_time": "2-4 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "7 Pot Douglah peppers", "quantity": "1", "unit": "dried", "prep_note": "ground to powder"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "EXTREME CAUTION: Wear gloves, eye protection, work in ventilated area. 7 Pot Douglah is among the hottest peppers."},
            {"step": 2, "text": "Grind dried 7 Pot Douglah to fine powder. One pepper is enough for this batch."},
            {"step": 3, "text": "Heat milk to 90°F (32°C). Add culture and ripen 30 minutes."},
            {"step": 4, "text": "Add calcium chloride if using, then rennet. Stir gently 1 minute."},
            {"step": 5, "text": "Let set 45-60 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 7, "text": "GOUDA WASH: Remove 1/3 whey. Replace with 170°F (77°C) water slowly while stirring."},
            {"step": 8, "text": "This raises temperature to about 100°F (38°C). Stir gently 20 minutes."},
            {"step": 9, "text": "Drain whey. Curds should mat together."},
            {"step": 10, "text": "Add salt and 7 Pot Douglah powder. Mix thoroughly with gloved hands."},
            {"step": 11, "text": "Pack into gouda mold. Press at 10 lbs 20 min, then 15 lbs 20 min, then 20 lbs 12 hours."},
            {"step": 12, "text": "Brine in saturated salt solution for 8 hours (or dry salt for 2 days)."},
            {"step": 13, "text": "Air dry 2 days. Wax with cheese wax."},
            {"step": 14, "text": "Age at 55°F (13°C) for 2-4 months."}
        ],
        "temperature": "90°F (32°C) start, 100°F (38°C) after wash, 55°F (13°C) aging",
        "notes": [
            "7 Pot Douglah reaches 1,853,396 Scoville units",
            "Named because ONE pepper can heat SEVEN pots of stew",
            "The chocolate-brown color is natural - not a 'chocolate' pepper cross",
            "Has fruity, slightly nutty flavor behind the extreme heat",
            "The gouda's curd washing creates sweetness to balance the heat"
        ],
        "tags": ["cheese", "7 Pot Douglah", "super-hot", "extreme heat", "gouda", "Caribbean", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]

# Check for duplicates
existing_ids = {r['id'] for r in data['recipes']}
recipes_to_add = [r for r in new_recipes if r['id'] not in existing_ids]
skipped = [r['id'] for r in new_recipes if r['id'] in existing_ids]

if skipped:
    print(f"Skipping {len(skipped)} duplicate(s): {skipped}")

# Add new recipes
data['recipes'].extend(recipes_to_add)
print(f"Added {len(recipes_to_add)} new recipes")

# Save
with open('data/recipes.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Total recipes now: {len(data['recipes'])}")

# List what was added
print("\nRecipes added:")
for r in recipes_to_add:
    print(f"  - {r['title']}")
