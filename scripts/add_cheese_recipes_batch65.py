#!/usr/bin/env python3
"""Add batch 65 - More ancient and medieval European cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-caciotta-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caciotta (Italian Farmhouse Cheese)",
        "category": "mains",
        "attribution": "Ancient Italian farmhouse tradition",
        "source_note": "Modernized from traditional Italian farmhouse methods, adapted for home cheesemaking",
        "description": "The quintessential Italian farmhouse cheese, caciotta (little cheese) has been made by farming families across Italy since at least the Middle Ages. Each region has its variation - from sheep milk in Tuscany to cow milk in Umbria. Mild when young, it develops character with age.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 2-8 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "sheep, cow, or goat - or mixed"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "MA 4001 or similar"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and stir. Sprinkle culture over surface and let rehydrate 2 minutes."},
            {"step": 2, "text": "Stir culture into milk. Cover and ripen for 45 minutes at 90°F."},
            {"step": 3, "text": "Add diluted rennet and stir gently for 30 seconds. Let set for 45 minutes until clean break achieved."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes, then stir gently for 20 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 6, "text": "When curds are firm and slightly springy, drain whey. Pack curds into round molds."},
            {"step": 7, "text": "Press with 10 lbs for 30 minutes, flip, then 20 lbs for 6-8 hours or overnight."},
            {"step": 8, "text": "Remove from mold. Make brine: 1 lb salt per gallon water. Brine cheese 6-12 hours."},
            {"step": 9, "text": "Air dry on cheese mat for 2-3 days, flipping twice daily until dry to touch."},
            {"step": 10, "text": "Age at 55°F (13°C) and 85% humidity for 2-8 weeks. Turn regularly. Rub with olive oil if desired."}
        ],
        "temperature": "90-100°F curd, 55°F aging",
        "notes": [
            "Every Italian region has its own caciotta variation",
            "Sheep milk versions (Tuscany) are richest; goat versions are tangiest",
            "Can add black pepper, truffles, or herbs during molding",
            "Young caciotta (2-4 weeks) is mild and milky; aged is sharper",
            "The name means 'little cheese' - traditionally made in small wheels"
        ],
        "tags": ["cheese", "cheesemaking", "italian", "caciotta", "farmhouse-cheese", "ancient", "aged-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-canestrato-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Canestrato (Italian Basket-Molded Cheese)",
        "category": "mains",
        "attribution": "Ancient Southern Italian tradition",
        "source_note": "Modernized from traditional Southern Italian methods, adapted for home cheesemaking",
        "description": "Named for the 'canestri' (reed baskets) used as molds, canestrato is an ancient Southern Italian cheese. The basket weave pattern on the rind is its signature. Made from sheep's milk in Sicily and Puglia, this hard grating cheese develops intense flavor with long aging.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 3-12 months aging",
        "ingredients": [
            {"item": "whole sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "cow milk acceptable as substitute"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "lamb rennet traditional, diluted"},
            {"item": "non-iodized salt", "quantity": "1/4", "unit": "cup", "prep_note": "for dry salting or brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 95°F (35°C). Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add thermophilic culture and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30-45 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces (small curds for hard cheese). Stir gently for 10 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 118°F (48°C) over 40 minutes, stirring constantly."},
            {"step": 6, "text": "The high cooking temperature creates a harder, drier cheese. Curds should be very firm."},
            {"step": 7, "text": "Traditional: press curds into rush baskets. Modern: use basket-weave molds or cheese molds."},
            {"step": 8, "text": "Press with heavy weight (40 lbs) for 24 hours, flipping every few hours."},
            {"step": 9, "text": "Dry salt the surface daily for 5-7 days, or brine for 24 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) for 3-12 months. Rub with olive oil monthly. Longer aging = sharper flavor."}
        ],
        "temperature": "95-118°F curd, 55°F aging",
        "notes": [
            "Traditional molds are woven rush baskets that leave distinctive pattern",
            "Canestrato Pugliese and Siciliano have PDO protection in Italy",
            "Young canestrato is a table cheese; aged becomes a grating cheese",
            "Sheep milk gives the characteristic sharp, tangy flavor",
            "Some versions include peppercorns in the paste"
        ],
        "tags": ["cheese", "cheesemaking", "italian", "sicilian", "pugliese", "canestrato", "sheep-milk", "aged-cheese", "ancient", "grating-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-crescenza-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Crescenza/Stracchino (Italian Soft Spreading Cheese)",
        "category": "mains",
        "attribution": "Medieval Lombardy tradition",
        "source_note": "Modernized from traditional Lombard methods, adapted for home cheesemaking",
        "description": "A creamy, spreadable cheese from Lombardy with roots in the Middle Ages. The name 'stracchino' comes from 'stracca' (tired) - referring to the tired cows returning from alpine pastures. Crescenza is its fresher, creamier cousin. Both are meant to be eaten very young.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "2 hours",
        "total_time": "3 hours plus overnight draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "full-fat, fresh"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richer version"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 100°F (38°C). Add culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add diluted rennet and stir gently. Let set for 1 hour. The set will be very soft."},
            {"step": 3, "text": "Cut curd into 1-inch cubes. Be very gentle - the curd is delicate."},
            {"step": 4, "text": "Let curds rest in whey for 15 minutes. Do not stir or heat further."},
            {"step": 5, "text": "Gently ladle curds into small molds (without pressing). Let drain at room temperature."},
            {"step": 6, "text": "After 2 hours, flip the cheeses. Continue draining for 8-12 hours or overnight."},
            {"step": 7, "text": "The cheese will release whey and compact naturally. No pressing needed."},
            {"step": 8, "text": "Once drained, salt the surface lightly on all sides."},
            {"step": 9, "text": "Wrap in paper and refrigerate. Best eaten within 1 week."},
            {"step": 10, "text": "Serve at room temperature spread on bread or crackers. Also excellent melted on focaccia."}
        ],
        "temperature": "100°F (38°C)",
        "notes": [
            "Crescenza/stracchino should be creamy and slightly oozy - not firm",
            "The high moisture content means short shelf life",
            "Traditional in focaccia di Recco (focaccia stuffed with stracchino)",
            "Modern Taleggio is the aged, washed-rind cousin of stracchino",
            "Best made in small batches and eaten quickly"
        ],
        "tags": ["cheese", "cheesemaking", "italian", "lombard", "crescenza", "stracchino", "soft-cheese", "spreading-cheese", "medieval"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-formaggio-di-fossa-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Formaggio di Fossa (Italian Pit-Aged Cheese)",
        "category": "mains",
        "attribution": "Medieval Italian tradition from Romagna",
        "source_note": "Modernized interpretation - traditional pit aging adapted for home conditions",
        "description": "A remarkable cheese buried in pits (fosse) dug into the rock of Romagna since the Middle Ages. Originally to hide cheese from invaders, the anaerobic aging creates intense, complex flavors. This recipe creates the base cheese; aging conditions approximate the pit environment.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 3-4 months aging",
        "ingredients": [
            {"item": "whole sheep milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "mixed milk traditional"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brining"},
            {"item": "cloth bags", "quantity": "1", "unit": "", "prep_note": "natural fiber, for wrapping"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F (35°C). Add calcium chloride, then culture. Ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Stir gently while raising temperature to 110°F (43°C)."},
            {"step": 4, "text": "Continue stirring at 110°F for 30 minutes until curds are firm."},
            {"step": 5, "text": "Drain whey and pack curds into round molds. Press with 20 lbs for 12 hours, flipping every 3 hours."},
            {"step": 6, "text": "Brine in saturated salt solution for 8-12 hours."},
            {"step": 7, "text": "Air dry for 2-3 weeks at 55°F (13°C), developing a dry natural rind."},
            {"step": 8, "text": "Wrap cheese in natural cloth. Place in closed container with damp cloth to maintain humidity."},
            {"step": 9, "text": "Age in cool, humid place (55°F, 90% humidity) for 3-4 months. The anaerobic environment develops complex flavors."},
            {"step": 10, "text": "Traditional cheese is unearthed in November for St. Catherine's Day. Yours is ready when intensely aromatic."}
        ],
        "temperature": "95-110°F curd, 55°F aging",
        "notes": [
            "Traditional fosse are tufa rock pits lined with straw - impossible to replicate at home",
            "The wrapped, buried aging creates unique anaerobic fermentation",
            "Finished cheese has asymmetric shape from settling in the pit",
            "Flavor is intensely complex - sheepy, musty, fermented, wonderful",
            "Protected by PDO as Formaggio di Fossa di Sogliano"
        ],
        "tags": ["cheese", "cheesemaking", "italian", "romagnol", "pit-aged", "cave-aged", "medieval", "aged-cheese", "sheep-milk"],
        "confidence": {"overall": "medium", "flags": ["Home version approximates traditional pit aging"]}
    },
    {
        "id": "traditional-queso-zamorano-spanish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Zamorano (Spanish Hard Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Spanish tradition from Zamora",
        "source_note": "Modernized from traditional Zamoran methods, adapted for home cheesemaking",
        "description": "From the province of Zamora in Castile and León comes this hard sheep's milk cheese with origins predating Roman times. Made exclusively from Churra and Castellana sheep milk, it's pressed in traditional esparto grass molds that leave a distinctive zigzag pattern on the rind.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "7 hours plus 6+ months aging",
        "ingredients": [
            {"item": "whole sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "Churra or similar breed"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "lamb rennet paste", "quantity": "1/4", "unit": "tsp", "prep_note": "or liquid rennet equivalent"},
            {"item": "non-iodized salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 86°F (30°C). Add calcium chloride if using pasteurized."},
            {"step": 2, "text": "Add thermophilic culture and ripen for 45 minutes."},
            {"step": 3, "text": "Add rennet (lamb rennet paste is traditional) and let set for 30-45 minutes."},
            {"step": 4, "text": "Cut curds into very small pieces - rice-sized for hard cheese."},
            {"step": 5, "text": "Slowly raise temperature to 104°F (40°C) over 30 minutes, stirring continuously."},
            {"step": 6, "text": "Hold at 104°F for another 30-45 minutes, stirring, until curds are very firm."},
            {"step": 7, "text": "Drain whey. Pack curds tightly into zigzag-patterned molds (or use cheese mold with mat)."},
            {"step": 8, "text": "Press with heavy weight (40-50 lbs) for 24 hours, flipping every 6 hours."},
            {"step": 9, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 50-55°F (10-13°C) and 85% humidity for minimum 6 months, up to 2 years. Rub with olive oil."}
        ],
        "temperature": "86-104°F curd, 50-55°F aging",
        "notes": [
            "Protected by Denominación de Origen (DO) since 1992",
            "Traditional molds are woven from esparto grass creating zigzag pattern",
            "Minimum aging is 6 months; artisanal versions age 2+ years",
            "Flavor is intense, complex, slightly piquant with lanolin notes",
            "Often compared to Manchego but with distinctive character from Churra sheep"
        ],
        "tags": ["cheese", "cheesemaking", "spanish", "zamorano", "sheep-milk", "hard-cheese", "aged-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-robiola-piemontese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Robiola Piemontese (Piedmont Soft-Ripened Cheese)",
        "category": "mains",
        "attribution": "Ancient Piedmontese tradition, possibly Celtic origin",
        "source_note": "Modernized from traditional Piedmontese methods, adapted for home cheesemaking",
        "description": "A family of soft, surface-ripened cheeses from Piedmont with roots possibly dating to Celtic times. The name may come from Latin 'rubrum' (red) for the reddish rind, or from the town of Robbio. Made from cow, sheep, or goat milk (or mixes), robiola is creamy to runny when ripe.",
        "servings_yield": "About 8 oz cheese",
        "prep_time": "30 minutes",
        "cook_time": "1.5 hours",
        "total_time": "2 hours plus 1-2 weeks ripening",
        "ingredients": [
            {"item": "whole goat milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or sheep, cow, or mixed"},
            {"item": "mesophilic culture", "quantity": "1/16", "unit": "tsp", "prep_note": "very small amount"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "for white rind"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "very small amount"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C) - room temperature. Add cultures and Penicillium candidum. Stir well."},
            {"step": 2, "text": "Add just 2 drops of rennet (this is a lactic-set cheese, mostly acid-coagulated)."},
            {"step": 3, "text": "Cover and let set for 18-24 hours at room temperature. Curd will be very soft and yogurt-like."},
            {"step": 4, "text": "Gently ladle curd into small molds (no cheesecloth needed). Do not break up the curd."},
            {"step": 5, "text": "Let drain at room temperature for 24 hours, flipping once or twice."},
            {"step": 6, "text": "The cheese will shrink significantly as whey drains."},
            {"step": 7, "text": "Remove from mold, salt lightly on all surfaces."},
            {"step": 8, "text": "Place on draining mat in ripening container. Maintain 55°F (13°C) and 90% humidity."},
            {"step": 9, "text": "White mold will develop over 5-7 days. Flip daily."},
            {"step": 10, "text": "Ripen for 1-2 weeks until surface is fully covered and interior begins to soften. Eat at peak ripeness."}
        ],
        "temperature": "72°F set, 55°F ripening",
        "notes": [
            "Robiola is a slow, lactic-set cheese - the long set develops acidity naturally",
            "Multiple milk types create different flavor profiles",
            "Robiola di Roccaverano (goat only) has DOP protection",
            "Properly ripened robiola is creamy to oozy under a thin white rind",
            "Small format cheese - traditionally individual-serving sized"
        ],
        "tags": ["cheese", "cheesemaking", "italian", "piedmontese", "robiola", "soft-ripened", "bloomy-rind", "lactic-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queso-de-murcia-spanish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso de Murcia al Vino (Spanish Wine-Washed Goat Cheese)",
        "category": "mains",
        "attribution": "Traditional Spanish Murcia region",
        "source_note": "Modernized from traditional Murcian methods, adapted for home cheesemaking",
        "description": "A distinctive cheese from Spain's Murcia region, made from Murciano-Granadina goat milk and washed with local red wine during aging. The wine creates a deep burgundy rind and imparts subtle fruity notes. Sometimes called 'Drunken Goat' cheese in export markets.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 2-3 months aging",
        "ingredients": [
            {"item": "whole goat milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brining"},
            {"item": "dry red wine", "quantity": "2", "unit": "cups", "prep_note": "Spanish wine if possible"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 86°F (30°C). Add calcium chloride, then culture. Ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet and stir gently. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes, then stir gently for 20 minutes."},
            {"step": 4, "text": "Slowly raise temperature to 95°F (35°C) over 20 minutes while stirring."},
            {"step": 5, "text": "Drain whey. Pack curds into cylindrical molds. Press with 15 lbs for 6 hours, flipping every 2 hours."},
            {"step": 6, "text": "Remove from mold. Brine in salt solution for 4-6 hours."},
            {"step": 7, "text": "Air dry for 2-3 days until surface is dry to touch."},
            {"step": 8, "text": "Begin wine washing: pour wine into shallow dish and turn cheese in it, coating all surfaces."},
            {"step": 9, "text": "Age at 55°F (13°C) and 85% humidity. Wash with wine every 3-4 days for first month, then weekly."},
            {"step": 10, "text": "Age 2-3 months total. The rind will be deep purple-red, the paste ivory and smooth."}
        ],
        "temperature": "86-95°F curd, 55°F aging",
        "notes": [
            "The wine washing creates a distinctive color and subtle flavor",
            "Queso de Murcia (without wine) also has PDO protection",
            "Murciano-Granadina goats produce especially rich milk",
            "The finished cheese has mild, slightly sweet goat flavor with wine notes",
            "Often marketed as 'Drunken Goat' or 'Borracho' cheese"
        ],
        "tags": ["cheese", "cheesemaking", "spanish", "murcian", "goat-cheese", "wine-washed", "washed-rind", "aged-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-sbrinz-swiss-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sbrinz (Ancient Swiss Mountain Cheese)",
        "category": "mains",
        "attribution": "Swiss tradition from Central Switzerland, 2000+ years",
        "source_note": "Modernized from traditional Swiss methods, adapted for home cheesemaking",
        "description": "One of the oldest cheeses in Europe, sbrinz from Central Switzerland may be the original 'parmesan' - Roman records mention hard cheese from the Alps being exported to Rome. Aged for 2-4 years, it becomes an intensely flavored grating cheese with crystalline texture.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "7 hours plus 18 months to 4 years aging",
        "ingredients": [
            {"item": "whole raw milk", "quantity": "3", "unit": "gallons", "prep_note": "fresh from morning milking ideal"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "Streptococcus thermophilus"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "omit if using raw milk"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add rennet and let set for 25-30 minutes. The curd should be firm."},
            {"step": 3, "text": "Cut curd into very small pieces - rice-sized (3-5mm). The small curds create hard texture."},
            {"step": 4, "text": "Begin stirring and slowly raise temperature to 131°F (55°C) over 40-50 minutes."},
            {"step": 5, "text": "This high cooking temperature is characteristic of sbrinz. Stir constantly."},
            {"step": 6, "text": "Hold at 131°F for 45-60 minutes until curds are very firm and squeak when pressed."},
            {"step": 7, "text": "Drain whey immediately. Pack very hot curds into mold and press with 50 lbs."},
            {"step": 8, "text": "Press for 24 hours, flipping frequently. Apply heat lamp if curds cool too fast."},
            {"step": 9, "text": "Brine in saturated salt solution for 8-10 days (yes, days - this is a very large cheese)."},
            {"step": 10, "text": "Age at 57°F (14°C) for minimum 18 months, up to 4 years. Oil rind monthly. Turn regularly."}
        ],
        "temperature": "90-131°F curd, 57°F aging",
        "notes": [
            "Sbrinz may be the original cheese that later inspired Parmigiano-Reggiano",
            "Roman traders exported Central Swiss hard cheese over the Alps 2000+ years ago",
            "Traditional wheels are 45 kg (100 lbs) - home versions are smaller",
            "Aged sbrinz develops crunchy tyrosine crystals like parmesan",
            "Traditional serving: break off chunks with special sbrinz knife, don't slice"
        ],
        "tags": ["cheese", "cheesemaking", "swiss", "alpine", "sbrinz", "hard-cheese", "grating-cheese", "ancient", "aged-cheese"],
        "confidence": {"overall": "high", "flags": ["Very long aging time required"]}
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
