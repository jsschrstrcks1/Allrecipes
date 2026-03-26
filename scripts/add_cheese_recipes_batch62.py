#!/usr/bin/env python3
"""Add batch 62 - Ancient Mediterranean and Near Eastern cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-halloumi-ancient-cypriot",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Halloumi (Ancient Cypriot Grilling Cheese)",
        "category": "mains",
        "attribution": "Ancient Cypriot tradition (Byzantine era)",
        "source_note": "Modernized from traditional Cypriot methods dating to Byzantine period, adapted for home cheesemaking",
        "description": "Cyprus's beloved grilling cheese with origins in the Byzantine era. The unique property of not melting comes from the pasta filata (stretched curd) technique combined with high heat during forming. Traditionally made from sheep and goat milk.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "45 minutes",
        "cook_time": "2-3 hours",
        "total_time": "3-4 hours plus overnight pressing",
        "ingredients": [
            {"item": "whole goat milk", "quantity": "1", "unit": "gallon", "prep_note": "or sheep milk"},
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "optional, for mixed milk version"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "MA 4001 or similar"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brine"},
            {"item": "dried mint", "quantity": "2", "unit": "tbsp", "prep_note": "traditional addition"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride if using pasteurized milk and stir well."},
            {"step": 2, "text": "Sprinkle culture over surface and let rehydrate 2 minutes, then stir in thoroughly. Ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and stir gently with up-and-down motions for 30 seconds. Let set undisturbed for 45-60 minutes until clean break achieved."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes, then gently stir for 20 minutes while slowly raising temperature to 104°F (40°C)."},
            {"step": 5, "text": "Drain whey and reserve it. Pack curds into cheese molds and press lightly for 1 hour, flipping every 15 minutes."},
            {"step": 6, "text": "Heat reserved whey to 185-195°F (85-90°C). This is the key step that gives halloumi its non-melting property."},
            {"step": 7, "text": "Slice the pressed cheese into 3-inch slabs. Submerge in hot whey and cook for 30-40 minutes until cheese floats."},
            {"step": 8, "text": "Remove slabs and while still warm and pliable, fold each piece in half around a sprinkle of dried mint. Press edges together."},
            {"step": 9, "text": "Place folded cheeses in brine (1 lb salt per gallon water) and refrigerate. Ready to eat immediately or store in brine for months."},
            {"step": 10, "text": "To serve, slice and grill or pan-fry until golden brown. The high-temperature whey bath creates proteins that resist melting."}
        ],
        "temperature": "86°F curd, 185-195°F whey bath",
        "notes": [
            "The hot whey bath is what makes halloumi unique - it denatures proteins so cheese won't melt",
            "Traditional halloumi uses no starter culture, relying on natural milk bacteria",
            "Mint is traditional but optional - some add it inside, some to the brine",
            "Fresh halloumi is mild; aged halloumi becomes firm and tangy",
            "Best eaten within 2 weeks fresh, or aged in brine up to 1 year"
        ],
        "tags": ["cheese", "cheesemaking", "cypriot", "halloumi", "grilling-cheese", "ancient", "mediterranean", "pasta-filata"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-akkawi-levantine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Akkawi (Levantine White Brine Cheese)",
        "category": "mains",
        "attribution": "Named after Akka (Acre), ancient Levantine port city",
        "source_note": "Modernized from traditional Levantine methods, adapted for home cheesemaking",
        "description": "Named after the ancient port city of Akka (Acre), this mild white brine cheese is essential in Middle Eastern cuisine. Used in knafeh, manakish, and breakfast spreads, its soft texture and ability to absorb flavors made it a staple across the Levant for centuries.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "total_time": "3 hours plus overnight pressing",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "or goat milk"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "optional, for tangier flavor"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "1", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "gallon", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and stir well. If using culture, add now and ripen 20 minutes."},
            {"step": 2, "text": "Add diluted rennet and stir gently for 30 seconds. Let set undisturbed for 45-60 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes using long knife. Let rest 5 minutes for curds to heal."},
            {"step": 4, "text": "Gently stir curds for 15 minutes, keeping temperature at 90°F. Curds should remain soft and pliable."},
            {"step": 5, "text": "Line colander with cheesecloth and drain curds. Let drip for 15 minutes."},
            {"step": 6, "text": "Transfer curds to cheese mold. Press with 10 lbs weight for 2 hours, flipping halfway."},
            {"step": 7, "text": "Make brine by dissolving salt in water. Submerge pressed cheese in brine."},
            {"step": 8, "text": "Refrigerate in brine for 24 hours minimum. For traditional salty flavor, brine for 3-7 days."},
            {"step": 9, "text": "To use in cooking, soak sliced cheese in fresh water for 2-4 hours to reduce saltiness as needed."},
            {"step": 10, "text": "Store in brine refrigerated for up to 2 months. Cheese will become saltier and firmer over time."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Akkawi is intentionally mild to showcase other flavors in dishes",
            "The cheese stretches slightly when heated, perfect for knafeh",
            "Soaking time controls saltiness - longer soak for milder cheese",
            "Traditional versions use raw milk and no added culture",
            "Also spelled 'Akawi', 'Ackawi', or 'Akawieh'"
        ],
        "tags": ["cheese", "cheesemaking", "levantine", "middle-eastern", "brine-cheese", "akkawi", "ancient", "knafeh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-jibneh-arabieh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jibneh Arabieh (Arabian White Cheese)",
        "category": "mains",
        "attribution": "Traditional Arabian Peninsula cheese",
        "source_note": "Modernized from traditional Bedouin and Arabian methods, adapted for home cheesemaking",
        "description": "The classic white table cheese of the Arabian Peninsula, developed by Bedouin herders as a way to preserve precious milk. Mild, creamy, and slightly tangy, it's eaten at every meal from breakfast to dinner. The simple technique reflects desert practicality.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "20 minutes",
        "cook_time": "1.5 hours",
        "total_time": "2 hours plus overnight pressing",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "cow, goat, or sheep"},
            {"item": "white vinegar or lemon juice", "quantity": "1/2", "unit": "cup", "prep_note": "for acid-set version"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "for rennet version, diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for dry salting"},
            {"item": "nigella seeds", "quantity": "1", "unit": "tbsp", "prep_note": "optional, traditional garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "For acid-set (traditional Bedouin method): Heat milk to 180°F (82°C), stirring occasionally to prevent scorching."},
            {"step": 2, "text": "Remove from heat and slowly add vinegar or lemon juice while stirring gently. Curds will form immediately."},
            {"step": 3, "text": "For rennet-set (creamier texture): Heat milk to 90°F (32°C), add diluted rennet, and let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curds gently and let rest 10 minutes. Stir carefully for 15 minutes."},
            {"step": 5, "text": "Line colander with cheesecloth. Pour curds in and let drain 20 minutes."},
            {"step": 6, "text": "Gather cheesecloth corners and twist to form a ball. Squeeze gently to remove more whey."},
            {"step": 7, "text": "Unwrap and knead in salt. Press into mold or shape by hand into a disc."},
            {"step": 8, "text": "Press lightly for 4-6 hours or overnight in refrigerator."},
            {"step": 9, "text": "Sprinkle with nigella seeds if desired. Slice and serve with flatbread, olives, and tea."},
            {"step": 10, "text": "Store wrapped in refrigerator up to 2 weeks, or in light brine for 1 month."}
        ],
        "temperature": "180°F acid-set, 90°F rennet-set",
        "notes": [
            "Bedouin traditionally used dried calf stomach (natural rennet) or soured milk",
            "Nigella seeds (black cumin) are traditional across Arabian Gulf cheeses",
            "Fresh cheese is best within first week - it doesn't age well",
            "Can be cubed and preserved in olive oil with herbs",
            "Pairs perfectly with date syrup or honey for breakfast"
        ],
        "tags": ["cheese", "cheesemaking", "arabian", "middle-eastern", "bedouin", "fresh-cheese", "ancient", "breakfast"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-shanklish-aged-levantine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Shanklish (Aged Levantine Herb Cheese)",
        "category": "mains",
        "attribution": "Ancient Levantine aged cheese tradition",
        "source_note": "Modernized from traditional Syrian/Lebanese methods, adapted for home cheesemaking",
        "description": "A remarkable aged cheese from Syria and Lebanon, shanklish begins as strained yogurt that's shaped into balls, dried, and aged with herbs and spices. The blue-gray mold that develops is prized, not feared. This ancient preservation technique creates an intensely flavored cheese.",
        "servings_yield": "About 12 cheese balls",
        "prep_time": "30 minutes",
        "cook_time": "None",
        "total_time": "30 minutes active plus 2-4 weeks aging",
        "ingredients": [
            {"item": "plain whole milk yogurt", "quantity": "2", "unit": "quarts", "prep_note": "or homemade labneh"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "za'atar", "quantity": "1", "unit": "cup", "prep_note": "for coating"},
            {"item": "Aleppo pepper flakes", "quantity": "1/2", "unit": "cup", "prep_note": "for coating"},
            {"item": "dried thyme", "quantity": "1/4", "unit": "cup", "prep_note": "additional coating option"},
            {"item": "olive oil", "quantity": "as needed", "unit": "", "prep_note": "for storing"}
        ],
        "instructions": [
            {"step": 1, "text": "Line a colander with several layers of cheesecloth. Pour yogurt into cloth and tie corners together."},
            {"step": 2, "text": "Hang bundle over bowl and drain in refrigerator for 24-48 hours until very thick (labneh consistency)."},
            {"step": 3, "text": "Mix drained yogurt with salt. The texture should be like thick cream cheese."},
            {"step": 4, "text": "Form mixture into balls about 1.5 inches in diameter. Place on a clean cloth-lined tray."},
            {"step": 5, "text": "Air dry balls in a cool, dry place for 3-5 days, turning daily. They will form a dry skin."},
            {"step": 6, "text": "For aged shanklish: Continue drying for 1-2 weeks. A blue-gray mold may develop - this is traditional and desirable."},
            {"step": 7, "text": "Mix za'atar and Aleppo pepper. Roll dried cheese balls in the spice mixture to coat completely."},
            {"step": 8, "text": "Store in a jar, covered with olive oil. Age at cool room temperature for 1-4 weeks for stronger flavor."},
            {"step": 9, "text": "To serve, crumble or slice shanklish. Mix with diced tomatoes, onion, olive oil, and serve with flatbread."},
            {"step": 10, "text": "Aged shanklish becomes pungent and crumbly, similar to blue cheese. It's an acquired taste prized by connoisseurs."}
        ],
        "temperature": "Room temperature aging, 60-70°F (15-21°C) ideal",
        "notes": [
            "The mold that develops is Penicillium, similar to blue cheese - it's safe and traditional",
            "Fresh shanklish is mild; aged shanklish is very strong and pungent",
            "Traditional in the Levant for using up excess yogurt",
            "The spice coating helps control mold development and adds flavor",
            "Can be made from goat or sheep milk yogurt for more authentic flavor"
        ],
        "tags": ["cheese", "cheesemaking", "levantine", "syrian", "lebanese", "aged-cheese", "herb-cheese", "ancient", "yogurt-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-nabulsi-palestinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Nabulsi (Palestinian Boiled Brine Cheese)",
        "category": "mains",
        "attribution": "Named after Nablus, ancient Palestinian city",
        "source_note": "Modernized from traditional Palestinian methods, adapted for home cheesemaking",
        "description": "From the ancient city of Nablus comes this unique white cheese, distinguished by its characteristic square shape, black nigella seeds, and mahlab (cherry pit spice) flavoring. The double-cooking technique creates a cheese that holds its shape when fried.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "45 minutes",
        "cook_time": "3 hours",
        "total_time": "4 hours plus overnight brining",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "sheep milk traditional, cow milk acceptable"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "mahlab", "quantity": "1", "unit": "tbsp", "prep_note": "ground cherry pit spice"},
            {"item": "mastic gum", "quantity": "1/2", "unit": "tsp", "prep_note": "ground, optional but traditional"},
            {"item": "nigella seeds", "quantity": "2", "unit": "tbsp", "prep_note": "black seeds"},
            {"item": "non-iodized salt", "quantity": "1.5", "unit": "cups", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "gallon", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add diluted rennet and stir gently. Let set undisturbed for 45-60 minutes."},
            {"step": 2, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes, then stir gently for 15 minutes."},
            {"step": 3, "text": "Drain whey through cheesecloth-lined colander. Reserve the whey."},
            {"step": 4, "text": "Mix curds with mahlab, mastic (if using), and nigella seeds while still warm."},
            {"step": 5, "text": "Pack seasoned curds into square molds (traditionally rectangular). Press with moderate weight for 2 hours."},
            {"step": 6, "text": "Make brine: dissolve salt in water. Add pressed cheese to brine and refrigerate overnight."},
            {"step": 7, "text": "The next day, prepare cooking brine: bring reserved whey (or fresh salt water) to boil."},
            {"step": 8, "text": "Remove cheese from brine, cut into 2-inch slices. Simmer in hot whey at 185°F (85°C) for 30 minutes."},
            {"step": 9, "text": "This cooking step is crucial - it creates the squeaky texture and prevents melting when fried."},
            {"step": 10, "text": "Cool and store in fresh brine. Before eating, soak in water to reduce saltiness. Traditionally fried or used in knafeh."}
        ],
        "temperature": "95°F curd, 185°F cooking",
        "notes": [
            "Mahlab gives Nabulsi its distinctive flavor - there's no true substitute",
            "The boiling step is essential for texture - don't skip it",
            "Traditionally sold in rectangular blocks with visible nigella seeds",
            "Famous as the cheese for knafeh nabulsieh (Palestinian cheese pastry)",
            "Fresh Nabulsi squeaks against teeth when chewed - a sign of quality"
        ],
        "tags": ["cheese", "cheesemaking", "palestinian", "nabulsi", "middle-eastern", "brine-cheese", "ancient", "knafeh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-baladi-egyptian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gibna Baladi (Egyptian Village Cheese)",
        "category": "mains",
        "attribution": "Ancient Egyptian cheese tradition",
        "source_note": "Modernized from traditional Egyptian village methods, adapted for home cheesemaking",
        "description": "Egypt's everyday cheese, 'gibna baladi' means 'country cheese' or 'village cheese.' This simple fresh cheese has been made in Egyptian villages for millennia - traces of similar cheese were found in ancient Egyptian tombs. It's mild, creamy, and eaten at every meal.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "1 hour",
        "total_time": "1.5 hours plus draining time",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "water buffalo milk traditional"},
            {"item": "white vinegar or lemon juice", "quantity": "1/3", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in large pot to 185°F (85°C), stirring occasionally to prevent scorching on the bottom."},
            {"step": 2, "text": "Remove from heat. Slowly drizzle in vinegar or lemon juice while stirring gently."},
            {"step": 3, "text": "The milk will curdle immediately, separating into white curds and yellowish whey."},
            {"step": 4, "text": "Let sit undisturbed for 10 minutes to allow curds to fully form."},
            {"step": 5, "text": "Line colander with cheesecloth. Gently ladle curds into the cloth."},
            {"step": 6, "text": "Let drain for 30 minutes for soft, spreadable cheese, or 2 hours for firmer texture."},
            {"step": 7, "text": "Transfer to bowl, mix in salt to taste. For traditional mild flavor, use minimal salt."},
            {"step": 8, "text": "Press into small mold or shape into a disc by hand."},
            {"step": 9, "text": "Serve immediately with Egyptian bread (aish baladi), tomatoes, and fresh mint."},
            {"step": 10, "text": "Store refrigerated up to 1 week. Does not age - meant to be eaten fresh."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Archaeologists found 3,200-year-old cheese in Egyptian tombs - likely similar to this",
            "Water buffalo milk makes the richest, most traditional version",
            "Egyptian breakfast always includes fresh cheese with bread and vegetables",
            "Can be salted more heavily and stored in brine for longer preservation",
            "Sometimes flavored with caraway or cumin seeds"
        ],
        "tags": ["cheese", "cheesemaking", "egyptian", "fresh-cheese", "ancient", "middle-eastern", "breakfast", "village-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-domiati-egyptian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Domiati (Egyptian Pre-Salted Cheese)",
        "category": "mains",
        "attribution": "Named after Damietta, ancient Egyptian port city",
        "source_note": "Modernized from traditional Egyptian methods dating to medieval period, adapted for home cheesemaking",
        "description": "Named after the Nile Delta port of Damietta (Dumyat), this unique cheese is Egypt's most famous. Unlike most cheeses where salt is added after, Domiati has salt added to the milk before curdling. This ancient technique produces a distinctively tangy, firm white cheese.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "total_time": "3 hours plus overnight draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "water buffalo traditional, cow acceptable"},
            {"item": "non-iodized salt", "quantity": "3/4", "unit": "cup", "prep_note": "for milk - this is not a typo"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted, helps coagulation with salted milk"},
            {"item": "liquid rennet", "quantity": "1.5", "unit": "tsp", "prep_note": "diluted in 1/4 cup water, extra needed due to salt"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to 95°F (35°C). Add salt and stir until completely dissolved. The high salt slows coagulation."},
            {"step": 2, "text": "Add calcium chloride and stir well. This helps counteract the salt's effect on curd formation."},
            {"step": 3, "text": "Add diluted rennet and stir gently for 30 seconds. The salted milk needs more rennet and longer setting time."},
            {"step": 4, "text": "Cover and let set undisturbed for 2-3 hours at 95°F (35°C). The curd will be softer than typical cheese."},
            {"step": 5, "text": "When curd shows clean break, cut into 1-inch cubes. The curd will be more fragile due to salt."},
            {"step": 6, "text": "Let curds rest in whey for 30 minutes, gently stirring occasionally."},
            {"step": 7, "text": "Line molds with cheesecloth. Ladle curds gently into molds (be gentle - curds are fragile)."},
            {"step": 8, "text": "Let drain overnight in refrigerator. The cheese will self-press from its own weight."},
            {"step": 9, "text": "Fresh Domiati is ready to eat now. For aged Domiati, store in its own whey (salted) for weeks to months."},
            {"step": 10, "text": "Aged Domiati develops a sharp, tangy flavor and firmer texture. Use in cooking or crumble over dishes."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Pre-salting milk is unique to Egyptian cheesemaking - an ancient innovation",
            "Fresh Domiati is soft and mild; aged Domiati is firm, crumbly, and sharp",
            "Traditional Domiati uses raw water buffalo milk and natural rennet",
            "The extra salt inhibits unwanted bacteria during the long, warm set time",
            "Can be cubed and stored in olive oil with herbs after aging"
        ],
        "tags": ["cheese", "cheesemaking", "egyptian", "domiati", "ancient", "middle-eastern", "brine-cheese", "pickled-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-kashkaval-balkan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kashkaval (Balkan Stretched Pasta Filata Cheese)",
        "category": "mains",
        "attribution": "Ancient Balkan/Eastern Mediterranean tradition",
        "source_note": "Modernized from traditional Balkan methods, adapted for home cheesemaking",
        "description": "A stretched-curd (pasta filata) cheese found across the Balkans, Turkey, and Eastern Mediterranean. Similar to Italian caciocavallo (they share etymological roots), kashkaval is made from sheep's milk and develops a buttery, slightly sharp flavor when aged.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "4-5 hours",
        "total_time": "6 hours plus aging",
        "ingredients": [
            {"item": "whole sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "or cow milk for milder version"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "Streptococcus thermophilus"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for salting and brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add calcium chloride if using pasteurized milk. Add culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add diluted rennet and stir gently. Let set for 45 minutes until clean break achieved."},
            {"step": 3, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes, then slowly stir and raise temperature to 105°F (40°C) over 30 minutes."},
            {"step": 4, "text": "Continue stirring and heating to 115°F (46°C). Hold at this temperature, stirring, for 30 minutes."},
            {"step": 5, "text": "Let curds settle to bottom. Drain whey. Place curd mass under whey at 100°F to acidify for 2-4 hours."},
            {"step": 6, "text": "Test for stretching: curd is ready when a small piece stretches smoothly in 170°F water without breaking."},
            {"step": 7, "text": "Cut curd into slices. Heat water to 170°F (77°C). Submerge curd pieces and work them together."},
            {"step": 8, "text": "Stretch and fold the curd repeatedly until smooth, shiny, and pliable. This develops the characteristic texture."},
            {"step": 9, "text": "Form into a ball or log shape. Place in ice water bath for 30 minutes to set the shape."},
            {"step": 10, "text": "Salt by rubbing surface or brining for 24 hours. Age at 55°F (13°C) and 85% humidity for 2-6 months."}
        ],
        "temperature": "95-115°F curd, 170°F stretching",
        "notes": [
            "The name comes from Turkish 'kaşar' and shares roots with Italian 'caciocavallo'",
            "Sheep milk kashkaval is more prized than cow milk versions",
            "Young kashkaval is mild; aged kashkaval is sharp and complex",
            "Used widely in Balkan cooking - grilled, fried, melted on bread",
            "The stretching technique (pasta filata) is ancient, possibly originating in the Eastern Mediterranean"
        ],
        "tags": ["cheese", "cheesemaking", "balkan", "kashkaval", "pasta-filata", "stretched-curd", "ancient", "sheep-milk"],
        "confidence": {"overall": "high", "flags": []}
    }
]

def main():
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}

    added = 0
    skipped = 0
    for recipe in new_recipes:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            print(f"Added: {recipe['title']}")
            added += 1
        else:
            print(f"Skipped (duplicate): {recipe['title']}")
            skipped += 1

    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = str(date.today())

    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
