#!/usr/bin/env python3
"""Add comprehensive Middle Eastern cheese recipes to the cheese category."""

import json

MIDDLE_EASTERN_CHEESE_RECIPES = [
    # === PALESTINIAN/LEVANTINE CHEESES ===
    {
        "id": "akkawi-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Akkawi Cheese (Palestinian White Cheese)",
        "category": "cheese",
        "attribution": "Traditional Palestinian cheese",
        "source_note": "Named after the city of Akka (Acre), this is one of the most popular Middle Eastern cheeses.",
        "description": "Soft, white brined cheese with mild, slightly salty flavor. Essential for kunafa and other Middle Eastern desserts. The cheese is soaked to remove salt before use in sweets.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-2 weeks brining",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add calcium chloride diluted in water, then rennet. Stir gently for 30 seconds."},
            {"step": 3, "text": "Let set undisturbed for 45-60 minutes until firm curd forms."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Gently stir curds for 15 minutes, maintaining temperature."},
            {"step": 6, "text": "Drain curds and ladle into molds. Press lightly at 5 lbs for 30 minutes."},
            {"step": 7, "text": "Flip and press at 10 lbs for 2-3 hours until cheese holds shape."},
            {"step": 8, "text": "Prepare brine: dissolve salt in water to create saturated solution."},
            {"step": 9, "text": "Cut cheese into blocks and submerge in brine. Store refrigerated 1-2 weeks minimum."},
            {"step": 10, "text": "For desserts: soak cheese in fresh water 24-48 hours to remove salt before using."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "The longer cheese brines, the saltier and firmer it becomes",
            "Essential for kunafa - the famous Middle Eastern dessert",
            "Soak in multiple changes of fresh water to desalt for sweet dishes",
            "Also spelled Akawi, Ackawi, or Akawieh"
        ],
        "tags": ["cheese", "Middle Eastern", "Palestinian", "brined", "white cheese", "kunafa"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "nabulsi-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Nabulsi Cheese (Palestinian Boiled Cheese)",
        "category": "cheese",
        "attribution": "Traditional Palestinian cheese",
        "source_note": "From Nablus, Palestine - unique for being boiled in brine with spices.",
        "description": "Distinctive white cheese boiled in salted whey with mastic and mahlab spices. The boiling process gives it a unique squeaky texture and aromatic flavor. Traditional for kunafa nabulsieh.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "Same day to 1 week",
        "ingredients": [
            {"item": "whole sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "cup"},
            {"item": "mastic resin (ground)", "quantity": "1/2", "unit": "tsp"},
            {"item": "mahlab (ground cherry pit kernel)", "quantity": "1/2", "unit": "tsp"},
            {"item": "nigella seeds (black cumin)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and ripen 20 minutes."},
            {"step": 2, "text": "Add rennet and let set 45 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Drain curds, reserving whey. Press curds in molds at 10 lbs for 1 hour."},
            {"step": 5, "text": "Cut pressed cheese into rectangular blocks about 3x4 inches."},
            {"step": 6, "text": "Prepare spiced brine: add salt, mastic, and mahlab to reserved whey. Bring to boil."},
            {"step": 7, "text": "Carefully lower cheese blocks into boiling brine. Simmer 10-15 minutes."},
            {"step": 8, "text": "Remove cheese and let cool. Press nigella seeds into the surface."},
            {"step": 9, "text": "Store in cooled brine in refrigerator. Use within 1 week, or keep in brine longer for preservation."}
        ],
        "temperature": "95°F (35°C) for curdling, boiling for cooking",
        "notes": [
            "Boiling is unique to Nabulsi - gives distinctive squeaky texture",
            "Mastic and mahlab are essential for authentic flavor",
            "Nigella seeds on surface are traditional visual identifier",
            "Sheep's milk is traditional but cow's milk works well"
        ],
        "tags": ["cheese", "Middle Eastern", "Palestinian", "boiled cheese", "spiced", "Nablus"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jibneh-arabieh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Jibneh Arabieh (Arabian White Cheese)",
        "category": "cheese",
        "attribution": "Traditional Arabian Peninsula cheese",
        "source_note": "The standard table cheese across the Arabian Gulf states.",
        "description": "Mild, soft white cheese popular throughout the Arabian Peninsula. Simple and versatile, it's enjoyed at breakfast with honey, dates, or flatbread. Less salty than Palestinian varieties.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "20 min",
        "cook_time": "2 hours",
        "total_time": "Fresh to 1 week",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Stir gently, then let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Gently stir curds for 10 minutes at 90°F."},
            {"step": 5, "text": "Drain curds and mix in salt evenly."},
            {"step": 6, "text": "Ladle into molds and press very lightly - just 5 lbs for 1-2 hours."},
            {"step": 7, "text": "Unmold and store in light brine or whey in refrigerator."},
            {"step": 8, "text": "Best consumed within 1 week while fresh and mild."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Jibneh simply means 'cheese' in Arabic",
            "Milder than Akkawi - less salt, shorter brining",
            "Traditional Gulf breakfast with dates and Arabic coffee",
            "Some versions add nigella seeds or dried mint"
        ],
        "tags": ["cheese", "Middle Eastern", "Arabian", "white cheese", "fresh", "breakfast cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "kashkaval-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kashkaval Cheese (Balkan-Middle Eastern Yellow Cheese)",
        "category": "cheese",
        "attribution": "Traditional Balkan/Middle Eastern cheese",
        "source_note": "Pasta filata cheese popular from the Balkans through the Levant to Egypt.",
        "description": "Semi-hard yellow cheese made using pasta filata (stretched curd) technique. Sharp, slightly tangy flavor with excellent melting properties. Popular across Turkey, Lebanon, Syria, and Egypt.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder (optional, for tang)", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and optional lipase. Ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F (41°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain whey and let curds mat together for 2-3 hours until pH reaches 5.2-5.4."},
            {"step": 6, "text": "Cut matted curd into strips. Heat water to 175°F (80°C)."},
            {"step": 7, "text": "Stretch and knead curds in hot water until smooth and elastic. Add salt while kneading."},
            {"step": 8, "text": "Form into wheel or log shape. Cool in ice water bath 20 minutes."},
            {"step": 9, "text": "Age at 55°F (13°C) for 2-3 months, turning weekly."}
        ],
        "temperature": "95-175°F (35-80°C)",
        "notes": [
            "Name derives from Italian 'caciocavallo' - cheese on horseback",
            "Sheep's milk gives more authentic flavor, cow's milk is milder",
            "Excellent for grilling - holds shape when heated",
            "Popular for breakfast in Turkey and throughout the Levant"
        ],
        "tags": ["cheese", "Middle Eastern", "Balkan", "pasta filata", "yellow cheese", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "shanklish-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Shanklish (Aged Spiced Cheese Balls)",
        "category": "cheese",
        "attribution": "Traditional Levantine cheese",
        "source_note": "Aged cheese balls rolled in herbs - popular in Syria, Lebanon, and Palestine.",
        "description": "Pungent, aged cheese formed into balls and coated with za'atar or Aleppo pepper. Develops strong blue-cheese-like flavors during aging. A beloved mezze dish served with olive oil and tomatoes.",
        "servings_yield": "About 12 cheese balls",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "strained yogurt (labneh)", "quantity": "2", "unit": "lbs"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"},
            {"item": "za'atar spice blend", "quantity": "1/2", "unit": "cup"},
            {"item": "Aleppo pepper (or red pepper flakes)", "quantity": "1/4", "unit": "cup"},
            {"item": "dried thyme", "quantity": "2", "unit": "tbsp"},
            {"item": "extra virgin olive oil for coating", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with thick labneh that has been strained 24-48 hours until very firm."},
            {"step": 2, "text": "Mix salt thoroughly into the labneh."},
            {"step": 3, "text": "Form labneh into balls about 1.5-2 inches in diameter."},
            {"step": 4, "text": "Place balls on a rack and let dry at room temperature 2-3 days, turning occasionally."},
            {"step": 5, "text": "Mix za'atar, Aleppo pepper, and thyme in a shallow dish."},
            {"step": 6, "text": "Lightly coat dried cheese balls with olive oil."},
            {"step": 7, "text": "Roll each ball in the spice mixture until well coated."},
            {"step": 8, "text": "Place in clean jar and age at cool room temperature (60-65°F) for 2-4 weeks."},
            {"step": 9, "text": "Cheese will develop stronger, more pungent flavors as it ages."}
        ],
        "temperature": "Room temperature for drying and aging",
        "notes": [
            "Also spelled shinklish, shangleesh, or chanklich",
            "Surface may develop natural mold - this is traditional and safe",
            "Serve crumbled with diced tomatoes, onions, and olive oil",
            "Can age up to several months for stronger flavor"
        ],
        "tags": ["cheese", "Middle Eastern", "Levantine", "aged", "spiced", "za'atar", "mezze"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "labneh-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Labneh (Strained Yogurt Cheese)",
        "category": "cheese",
        "attribution": "Traditional Middle Eastern cheese",
        "source_note": "The quintessential Middle Eastern fresh cheese, made from strained yogurt.",
        "description": "Thick, creamy strained yogurt cheese with tangy flavor. Served for breakfast drizzled with olive oil, or rolled into balls and preserved in oil. The foundation of many Middle Eastern cheese preparations.",
        "servings_yield": "About 2 cups",
        "prep_time": "10 min",
        "cook_time": "0",
        "total_time": "24-48 hours straining",
        "ingredients": [
            {"item": "full-fat plain yogurt", "quantity": "4", "unit": "cups"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "extra virgin olive oil for serving", "quantity": "2", "unit": "tbsp"},
            {"item": "za'atar for garnish (optional)", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt into yogurt thoroughly."},
            {"step": 2, "text": "Line a fine-mesh strainer with cheesecloth or butter muslin."},
            {"step": 3, "text": "Place strainer over a deep bowl to catch whey."},
            {"step": 4, "text": "Pour salted yogurt into lined strainer."},
            {"step": 5, "text": "Gather edges of cloth and tie to create a bundle."},
            {"step": 6, "text": "Refrigerate and strain 24 hours for spreadable labneh, 48 hours for thick labneh."},
            {"step": 7, "text": "Transfer strained labneh to serving dish."},
            {"step": 8, "text": "Create a well in center, drizzle with olive oil, sprinkle with za'atar."},
            {"step": 9, "text": "Serve with warm pita bread for dipping."}
        ],
        "temperature": "Refrigerate during straining",
        "notes": [
            "The longer you strain, the thicker the labneh",
            "Use the whey for baking or smoothies - don't discard it",
            "For labneh balls: strain 48 hours, roll into balls, preserve in olive oil with herbs",
            "Greek yogurt can substitute but authentic labneh uses regular yogurt"
        ],
        "tags": ["cheese", "Middle Eastern", "yogurt cheese", "fresh", "breakfast", "mezze", "vegetarian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jameed-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Jameed (Dried Yogurt Balls)",
        "category": "cheese",
        "attribution": "Traditional Jordanian/Bedouin cheese",
        "source_note": "Hard dried yogurt essential for mansaf - Jordan's national dish.",
        "description": "Rock-hard dried fermented yogurt, traditionally made from sheep or goat milk. Reconstituted with water to make the sauce for mansaf. A Bedouin preservation technique dating back centuries.",
        "servings_yield": "About 1 lb dried",
        "prep_time": "30 min",
        "cook_time": "0",
        "total_time": "1-2 weeks drying",
        "ingredients": [
            {"item": "goat's milk yogurt (or sheep's)", "quantity": "2", "unit": "quarts"},
            {"item": "salt", "quantity": "2", "unit": "tbsp"},
            {"item": "water for reconstituting", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Start with thick, full-fat goat's milk yogurt."},
            {"step": 2, "text": "Strain yogurt through cheesecloth for 24 hours until very thick (like labneh)."},
            {"step": 3, "text": "Mix salt thoroughly into strained yogurt."},
            {"step": 4, "text": "Form into balls about 2-3 inches in diameter."},
            {"step": 5, "text": "Place balls on a clean cloth in a well-ventilated area away from direct sunlight."},
            {"step": 6, "text": "Allow to dry for 1-2 weeks, turning occasionally, until rock-hard."},
            {"step": 7, "text": "Balls should be completely dry and hard as stone when finished."},
            {"step": 8, "text": "Store in a dry place - jameed keeps for months or even years."},
            {"step": 9, "text": "To use: soak in warm water for several hours, then blend until smooth for mansaf sauce."}
        ],
        "temperature": "Room temperature, well-ventilated",
        "notes": [
            "Traditional Bedouin preservation method for dairy",
            "Must be completely dried or it will spoil",
            "Reconstituted jameed has tangy, slightly funky flavor",
            "Essential for authentic Jordanian mansaf (lamb and rice dish)"
        ],
        "tags": ["cheese", "Middle Eastern", "Jordanian", "Bedouin", "dried", "preserved", "mansaf"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === EGYPTIAN CHEESES ===
    {
        "id": "gibna-baladi",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gibna Baladi (Egyptian Village Cheese)",
        "category": "cheese",
        "attribution": "Traditional Egyptian cheese",
        "source_note": "Simple fresh cheese made in Egyptian villages for generations.",
        "description": "Soft, fresh Egyptian white cheese with mild flavor. 'Baladi' means 'country' or 'local' - this is the simple farmhouse cheese of rural Egypt. Eaten fresh with bread and vegetables.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "20 min",
        "cook_time": "1 hour",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole buffalo milk (or cow's milk)", "quantity": "1", "unit": "gallon"},
            {"item": "white vinegar or lemon juice", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180°F (82°C), stirring occasionally to prevent scorching."},
            {"step": 2, "text": "Remove from heat and slowly add vinegar or lemon juice while stirring."},
            {"step": 3, "text": "Curds will form and separate from whey within minutes."},
            {"step": 4, "text": "Let stand 10 minutes until curds fully set."},
            {"step": 5, "text": "Line a colander with cheesecloth and pour in curds."},
            {"step": 6, "text": "Sprinkle salt over curds and mix gently."},
            {"step": 7, "text": "Gather cloth edges and squeeze gently to remove excess whey."},
            {"step": 8, "text": "Shape into a round or press into a mold for 1-2 hours."},
            {"step": 9, "text": "Refrigerate and eat fresh within 3-5 days."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Buffalo milk is traditional and gives richer flavor",
            "Very simple acid-set cheese - no cultures or rennet needed",
            "Fresh, mild flavor pairs well with ful medames (Egyptian beans)",
            "Similar to Indian paneer or Latin American queso fresco"
        ],
        "tags": ["cheese", "Middle Eastern", "Egyptian", "fresh", "white cheese", "acid-set"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "domiati-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Domiati Cheese (Egyptian Brined Cheese)",
        "category": "cheese",
        "attribution": "Traditional Egyptian cheese",
        "source_note": "Egypt's most famous cheese, named after the port city of Damietta.",
        "description": "Unique Egyptian cheese where salt is added directly to the milk before curdling. Results in a soft, very salty white cheese. Eaten fresh or aged, and essential for Egyptian baked goods like feteer meshaltet.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Fresh to several months",
        "ingredients": [
            {"item": "whole buffalo milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "salt (added to milk)", "quantity": "1/2 to 1", "unit": "cup"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "additional salt for brine", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "quart"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve salt directly into cold milk - use more salt for longer preservation."},
            {"step": 2, "text": "Heat salted milk to 100°F (38°C)."},
            {"step": 3, "text": "Add rennet diluted in water. Stir briefly, then let set 2-3 hours."},
            {"step": 4, "text": "The high salt content slows curdling - be patient."},
            {"step": 5, "text": "When curd is set, ladle gently into molds without cutting."},
            {"step": 6, "text": "Drain at room temperature for 24 hours."},
            {"step": 7, "text": "For fresh Domiati: eat within 1 week - very salty but soft."},
            {"step": 8, "text": "For aged Domiati: prepare brine with salt and water, submerge cheese."},
            {"step": 9, "text": "Age in brine for several months - develops sharper, more complex flavor."}
        ],
        "temperature": "100°F (38°C)",
        "notes": [
            "Adding salt to milk before curdling is unique to Domiati",
            "High salt acts as preservative in hot Egyptian climate",
            "Fresh Domiati is soft; aged Domiati becomes crumbly",
            "Soak in water before eating to reduce saltiness if desired"
        ],
        "tags": ["cheese", "Middle Eastern", "Egyptian", "brined", "white cheese", "Damietta"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === PERSIAN CHEESE ===
    {
        "id": "lighvan-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lighvan Cheese (Persian Sheep's Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Persian cheese",
        "source_note": "From the village of Lighvan in Iranian Azerbaijan - Persia's most famous cheese.",
        "description": "Rich, tangy sheep's milk cheese from northwest Iran. Brined and aged, it develops complex flavors with slight piquancy. The terroir of Lighvan's mountain pastures gives distinctive character.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 90°F (32°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add rennet and let set 45-60 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir curds for 20 minutes, maintaining temperature."},
            {"step": 5, "text": "Drain and ladle curds into molds. Press at 10 lbs for 1 hour."},
            {"step": 6, "text": "Flip and press at 15 lbs for 6-8 hours."},
            {"step": 7, "text": "Prepare saturated brine with salt and water."},
            {"step": 8, "text": "Submerge cheese in brine and age at 50-55°F (10-13°C) for 2-6 months."},
            {"step": 9, "text": "Longer aging develops stronger, more piquant flavor."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Lighvan village is in mountainous East Azerbaijan province",
            "Sheep graze on wild thyme and mountain herbs, affecting flavor",
            "Protected geographical indication in Iran",
            "Traditionally stored in sheep or goatskin bags for aging"
        ],
        "tags": ["cheese", "Middle Eastern", "Persian", "Iranian", "sheep's milk", "brined", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === TURKISH CHEESES ===
    {
        "id": "turkish-beyaz-peynir",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Beyaz Peynir (Turkish White Cheese)",
        "category": "cheese",
        "attribution": "Traditional Turkish cheese",
        "source_note": "Turkey's most popular cheese - similar to feta but with distinct character.",
        "description": "Brined white cheese that is the cornerstone of Turkish breakfast. Creamy, tangy, and moderately salty, it's made from cow's, sheep's, or goat's milk depending on region. Essential for Turkish cuisine.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks minimum",
        "ingredients": [
            {"item": "whole sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt for brine", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes, maintaining temperature."},
            {"step": 5, "text": "Drain curds and ladle into molds. Press lightly at 5 lbs for 30 minutes."},
            {"step": 6, "text": "Flip and press at 10 lbs for 4-6 hours."},
            {"step": 7, "text": "Cut into blocks and submerge in saturated brine."},
            {"step": 8, "text": "Brine at refrigerator temperature for minimum 2 weeks, up to several months."},
            {"step": 9, "text": "Cheese becomes firmer and tangier with longer brining."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Beyaz Peynir means simply 'white cheese' in Turkish",
            "The most consumed cheese in Turkey by far",
            "Essential component of traditional Turkish breakfast",
            "Quality varies by milk type - sheep's milk is considered premium"
        ],
        "tags": ["cheese", "Middle Eastern", "Turkish", "white cheese", "brined", "breakfast cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkish-kasar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kasar Peyniri (Turkish Yellow Cheese)",
        "category": "cheese",
        "attribution": "Traditional Turkish cheese",
        "source_note": "Turkey's beloved yellow cheese - pasta filata style similar to kashkaval.",
        "description": "Semi-hard yellow cheese made using pasta filata technique. Mild when young (taze kasar), sharp when aged (eski kasar). Excellent melting cheese, essential for Turkish toast and pide.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "Fresh to 6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F (41°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds and let mat together 2-3 hours until stretchy (pH 5.2-5.4)."},
            {"step": 6, "text": "Cut curd mass into strips."},
            {"step": 7, "text": "Heat water to 175°F (80°C). Stretch and knead curds until smooth."},
            {"step": 8, "text": "Work in salt while kneading. Form into wheel shape."},
            {"step": 9, "text": "Cool in cold water 20 minutes. For taze kasar: eat within 1-2 weeks."},
            {"step": 10, "text": "For eski kasar: age at 55°F (13°C) for 3-6 months or longer."}
        ],
        "temperature": "95-175°F (35-80°C)",
        "notes": [
            "Taze means 'fresh' - mild and elastic",
            "Eski means 'old' - aged, sharper, crumbly",
            "The stretching technique gives characteristic stringy melt",
            "Essential for Turkish grilled cheese sandwiches (tost)"
        ],
        "tags": ["cheese", "Middle Eastern", "Turkish", "pasta filata", "yellow cheese", "melting cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkish-tulum",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tulum Peyniri (Turkish Goatskin-Aged Cheese)",
        "category": "cheese",
        "attribution": "Traditional Turkish cheese",
        "source_note": "Artisanal Turkish cheese traditionally aged in goatskin bags.",
        "description": "Crumbly, pungent cheese aged in goatskin (tulum) bags. The skin imparts unique flavors and the anaerobic environment creates distinctive character. Ranges from mild to very sharp depending on age.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "goat's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 90°F (32°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add rennet and let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into small 1/4-inch pieces. Rest 5 minutes."},
            {"step": 4, "text": "Stir gently for 30 minutes while maintaining temperature."},
            {"step": 5, "text": "Drain thoroughly - curds should be quite dry."},
            {"step": 6, "text": "Mix salt into curds evenly."},
            {"step": 7, "text": "Traditional method: pack into cleaned, cured goatskin bag, press out air, seal."},
            {"step": 8, "text": "Modern method: pack tightly into crock or vacuum-seal, eliminating air."},
            {"step": 9, "text": "Age in cool cellar (50-55°F/10-13°C) for 3-6 months minimum."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Tulum means 'goatskin bag' in Turkish",
            "Traditional goatskin aging imparts unique flavors",
            "Vacuum sealing approximates anaerobic skin environment",
            "Izmir region tulum is especially prized",
            "Texture ranges from creamy to crumbly with age"
        ],
        "tags": ["cheese", "Middle Eastern", "Turkish", "goat's milk", "aged", "artisanal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkish-mihalic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mihalic Peyniri (Bursa Sheep's Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Turkish cheese",
        "source_note": "Hard, aged cheese from the Bursa region, also called Kelle peyniri.",
        "description": "Hard, granular sheep's milk cheese from Bursa province. Aged extensively for sharp, nutty flavor. Turkey's answer to Pecorino or aged Manchego. Excellent for grating or as a table cheese.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "6-12 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes."},
            {"step": 4, "text": "Slowly heat to 115°F (46°C) over 45 minutes while stirring continuously."},
            {"step": 5, "text": "Continue stirring at temperature until curds are very firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and press at 30 lbs for 2 hours, flip, then 40 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24-48 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for 6-12 months."},
            {"step": 9, "text": "Rub with olive oil monthly during aging to prevent cracking."}
        ],
        "temperature": "95-115°F (35-46°C)",
        "notes": [
            "Also known as Kelle peyniri (head cheese - from its shape)",
            "Mihalic refers to the old Byzantine name for the region",
            "Sheep's milk gives rich, lanolin-sweet undertones",
            "Aged versions are hard enough for grating"
        ],
        "tags": ["cheese", "Middle Eastern", "Turkish", "sheep's milk", "hard", "aged", "Bursa"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "turkish-ezine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ezine Peyniri (Thracian Protected Cheese)",
        "category": "cheese",
        "attribution": "Traditional Turkish cheese",
        "source_note": "Premium white cheese from Ezine district in Canakkale - geographically protected.",
        "description": "Turkey's most prestigious white cheese with geographical indication protection. Made from a blend of sheep's and goat's milk in the Ezine district. Rich, complex, and considered the finest Turkish white cheese.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Blend sheep's and goat's milk. Heat to 90°F (32°C)."},
            {"step": 2, "text": "Add starter and ripen 45 minutes."},
            {"step": 3, "text": "Add rennet and let set 60 minutes until firm curd."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 15 minutes."},
            {"step": 5, "text": "Gently stir for 20 minutes, maintaining temperature."},
            {"step": 6, "text": "Drain and ladle into molds. Press at 5 lbs for 30 minutes."},
            {"step": 7, "text": "Flip and press at 10 lbs for 6 hours."},
            {"step": 8, "text": "Submerge in saturated brine."},
            {"step": 9, "text": "Age in brine at 50-55°F (10-13°C) for 3-6 months for full flavor development."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Ezine has EU-style geographical indication protection in Turkey",
            "Traditional ratio is approximately 75% sheep, 25% goat milk",
            "The mixed milk gives complexity - sheep for richness, goat for tang",
            "Premium price in Turkey - considered the best white cheese"
        ],
        "tags": ["cheese", "Middle Eastern", "Turkish", "mixed milk", "brined", "protected origin", "premium"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ISRAELI CHEESE ===
    {
        "id": "tzfatit-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tzfatit (Israeli Safed Cheese)",
        "category": "cheese",
        "attribution": "Traditional Israeli cheese",
        "source_note": "Brined sheep's milk cheese from Safed (Tzfat) in northern Israel.",
        "description": "Creamy, brined sheep's milk cheese from the Galilee region. Semi-soft with tangy, slightly salty flavor. One of Israel's most popular traditional cheeses, dating to the Ottoman period.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-4 weeks",
        "ingredients": [
            {"item": "sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3/4", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes at temperature."},
            {"step": 5, "text": "Drain and ladle into molds. Press lightly at 5 lbs for 20 minutes."},
            {"step": 6, "text": "Flip and press at 8 lbs for 3-4 hours."},
            {"step": 7, "text": "Prepare brine with salt and water."},
            {"step": 8, "text": "Submerge cheese in brine. Age 1-4 weeks in refrigerator."},
            {"step": 9, "text": "Young Tzfatit is mild; longer brining develops stronger flavor."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Tzfat (Safed) is a mystical city in the Galilee known for this cheese",
            "Traditional cheese of the Jewish community dating centuries",
            "Softer and creamier than typical feta",
            "Often served with Israeli breakfast alongside vegetables and eggs"
        ],
        "tags": ["cheese", "Middle Eastern", "Israeli", "sheep's milk", "brined", "Galilee"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === LEBANESE CHEESE ===
    {
        "id": "lebanese-akkawi",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lebanese Akkawi (Ackawi Cheese)",
        "category": "cheese",
        "attribution": "Traditional Lebanese cheese",
        "source_note": "Lebanese version of Akkawi - the essential cheese for Lebanese sweets.",
        "description": "Smooth, elastic brined cheese crucial for Lebanese desserts like knafeh and halawet el jibn. Lebanese Akkawi is often slightly softer than Palestinian versions, prized for its stretchy texture when heated.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-2 weeks brining",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "cup"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and ripen 25 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Stir gently 30 seconds."},
            {"step": 3, "text": "Let set undisturbed 45-50 minutes until soft curd forms."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Stir very gently for 10 minutes to keep curds soft and elastic."},
            {"step": 6, "text": "Drain curds and ladle into molds. Press very lightly - 3-5 lbs for 30 minutes only."},
            {"step": 7, "text": "The goal is elastic, not firm cheese."},
            {"step": 8, "text": "Prepare brine and submerge cheese blocks."},
            {"step": 9, "text": "Brine 1-2 weeks. Soak in fresh water 24-48 hours before using in desserts."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Light pressing keeps the elastic, stretchy texture needed for sweets",
            "Must be thoroughly desalted before using in desserts",
            "The cheese should stretch when heated, not crumble",
            "Essential for halawet el jibn (sweet cheese rolls)"
        ],
        "tags": ["cheese", "Middle Eastern", "Lebanese", "brined", "white cheese", "dessert cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Middle Eastern cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in MIDDLE_EASTERN_CHEESE_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"Skipping existing: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"Added: {recipe['title']}")
            added += 1

    data['recipes'] = recipes

    # Update meta count
    if 'meta' in data:
        data['meta']['total_count'] = len(recipes)
        data['meta']['total_recipes'] = len(recipes)

    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Added: {added} recipes")
    print(f"Skipped (existing): {skipped}")
    print(f"Total recipes now: {len(recipes)}")


if __name__ == '__main__':
    add_recipes()
