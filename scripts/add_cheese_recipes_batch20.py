#!/usr/bin/env python3
"""Add batch 20 of traditional cheese recipes - Alpine and regional specialties."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-double-gloucester-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Double Gloucester",
        "category": "mains",
        "attribution": "Gloucestershire, England, 16th Century",
        "source_note": "Gloucester cheese has been made since at least the 16th century using milk from Old Gloucester cattle. 'Double' refers to the use of whole milk from two milkings, while 'Single' used the skimmed evening milk.",
        "description": "Rich, buttery English cheese with a smooth, dense texture and mellow flavor - the cheese rolled down Cooper's Hill annually.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "full-fat from two milkings"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for golden color"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk. Add annatto if using."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 94°F over 40 minutes, stirring gently."},
            {"step": 6, "text": "Hold at 94°F for 45 minutes, stirring every few minutes."},
            {"step": 7, "text": "Drain whey. Perform a brief cheddaring: stack curds for 30 minutes, flipping once."},
            {"step": 8, "text": "Mill curds into small pieces."},
            {"step": 9, "text": "Add salt and mix well."},
            {"step": 10, "text": "Pack into cloth-lined mold. Press at 20 lbs for 30 minutes."},
            {"step": 11, "text": "Flip and press at 40 lbs for 12 hours."},
            {"step": 12, "text": "Flip and press at 50 lbs for 24 hours."},
            {"step": 13, "text": "Air dry 4-5 days. Cloth-bind with lard or butter."},
            {"step": 14, "text": "Age at 55°F and 85% humidity for 3-6 months."}
        ],
        "temperature": "86°F start, 94°F cook, 55°F aging",
        "notes": [
            "Double Gloucester uses full-fat milk; Single Gloucester was made with partially skimmed milk",
            "The distinctive golden color traditionally came from summer pasture milk, now from annatto",
            "Traditional wheels are used in the annual Cooper's Hill Cheese Rolling race in Gloucestershire",
            "Double Gloucester melts well and is excellent for cheese on toast"
        ],
        "tags": ["cheese", "traditional", "english", "gloucestershire", "double-gloucester", "territorial-cheese", "16th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-scamorza-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Italian Scamorza",
        "category": "mains",
        "attribution": "Southern Italy, Medieval",
        "source_note": "Scamorza is a pasta filata cheese from southern Italy, traditionally hung to dry and often smoked. The name means 'beheaded' referring to its distinctive pear shape with a tied-off top.",
        "description": "Italian stretched-curd cheese, pear-shaped and often smoked, with a mild milky flavor and excellent melting properties.",
        "servings_yield": "About 1 lb",
        "prep_time": "3 hours",
        "cook_time": "1-2 weeks drying",
        "total_time": "1-2 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or buffalo milk traditionally"},
            {"item": "citric acid", "quantity": "1", "unit": "tsp", "prep_note": "dissolved in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "hardwood chips", "quantity": "as needed", "unit": "", "prep_note": "for smoking, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Add citric acid solution to cold milk, stir well. Heat to 90°F."},
            {"step": 2, "text": "Remove from heat, add diluted rennet, stir gently. Let set 10-15 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly heat curds to 105°F, stirring gently."},
            {"step": 5, "text": "Drain curds and let mat for 2-3 hours at 100°F until pH reaches 5.2-5.3 and curd stretches in hot water."},
            {"step": 6, "text": "Cut matted curd into strips. Heat water to 170-175°F with salt."},
            {"step": 7, "text": "Stretch curd in hot water until smooth and elastic."},
            {"step": 8, "text": "Form into pear shape, pinching off the top to create the distinctive 'beheaded' shape."},
            {"step": 9, "text": "Tie the pinched top with string for hanging."},
            {"step": 10, "text": "Cool in ice water for 30 minutes to set shape."},
            {"step": 11, "text": "Hang to dry at room temperature for 1-2 weeks."},
            {"step": 12, "text": "For Scamorza Affumicata: Cold smoke for 2-4 hours with hardwood chips."}
        ],
        "temperature": "90°F curd, 170°F stretching",
        "notes": [
            "Scamorza Bianca is the unsmoked version; Scamorza Affumicata is smoked",
            "The pear shape and tied top are distinctive to scamorza",
            "It's drier and firmer than fresh mozzarella, making it better for cooking",
            "Excellent for grilling, baking on pizza, or sliced and eaten fresh"
        ],
        "tags": ["cheese", "traditional", "italian", "pasta-filata", "scamorza", "smoked-cheese", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-caciocavallo-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caciocavallo (Southern Italian)",
        "category": "mains",
        "attribution": "Southern Italy, Ancient",
        "source_note": "Caciocavallo dates back at least to the 14th century and possibly to ancient Rome. The name means 'cheese on horseback,' likely referring to how pairs were hung over a beam like saddlebags.",
        "description": "Ancient Italian stretched-curd cheese, hung in pairs to age, developing complex flavors from mild and milky to sharp and tangy.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "2-12 months aging",
        "total_time": "2-12 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 118°F over 30 minutes, stirring."},
            {"step": 6, "text": "Drain curds and let mat at 100°F for 3-5 hours, flipping occasionally, until pH reaches 5.2-5.3."},
            {"step": 7, "text": "Cut matted curd into strips. Heat water to 175-180°F with salt."},
            {"step": 8, "text": "Stretch curd in hot water until very smooth and elastic, folding repeatedly."},
            {"step": 9, "text": "Form into traditional gourd or teardrop shape with a small head at the top."},
            {"step": 10, "text": "Tie string around the neck for hanging."},
            {"step": 11, "text": "Cool in cold water for 1 hour."},
            {"step": 12, "text": "Brine for 4-6 hours."},
            {"step": 13, "text": "Hang in pairs (traditional) at 55°F and 85% humidity."},
            {"step": 14, "text": "Age: 2-4 months for mild; 6-12 months for sharp, grating quality."}
        ],
        "temperature": "97°F start, 118°F cook, 175°F stretch, 55°F aging",
        "notes": [
            "The traditional gourd shape with a small 'head' is distinctive",
            "Hung in pairs over a beam like saddlebags - hence 'on horseback'",
            "Young caciocavallo is mild and sliceable; aged becomes sharp and gratable",
            "Caciocavallo Silano is a DOP version from specific southern Italian regions"
        ],
        "tags": ["cheese", "traditional", "italian", "pasta-filata", "caciocavallo", "aged-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-appenzeller-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Appenzeller (Swiss)",
        "category": "mains",
        "attribution": "Appenzell, Switzerland, 700+ Years",
        "source_note": "Appenzeller has been made in northeastern Switzerland for over 700 years. Its distinctive flavor comes from a secret herbal brine wash that has been passed down through generations.",
        "description": "Tangy Swiss cheese with a complex herbal flavor from its secret brine wash - one of Switzerland's most distinctive cheeses.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brine"},
            {"item": "herbal brine ingredients", "quantity": "", "unit": "", "prep_note": "see notes for suggested herbs"},
            {"item": "white wine", "quantity": "1/2", "unit": "cup", "prep_note": "for herbal brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-35 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 122°F over 40 minutes while stirring."},
            {"step": 6, "text": "Hold at 122°F for 40 minutes, stirring frequently."},
            {"step": 7, "text": "Transfer curds under whey to mold. Press at 10 lbs for 30 minutes."},
            {"step": 8, "text": "Flip and press at 30 lbs for 12 hours."},
            {"step": 9, "text": "Brine in saturated salt solution for 12-18 hours."},
            {"step": 10, "text": "Prepare herbal brine: Infuse wine with herbs, strain, add to light brine."},
            {"step": 11, "text": "Age at 55°F and 90% humidity, washing with herbal brine 2-3 times per week."},
            {"step": 12, "text": "Age 3 months minimum; 6+ months for stronger flavor."}
        ],
        "temperature": "90°F start, 122°F cook, 55°F aging",
        "notes": [
            "The traditional herbal brine recipe is a closely guarded secret with 20+ ingredients",
            "Suggested herbs for homemade version: white wine, thyme, rosemary, bay, juniper, pepper, coriander",
            "The brine wash gives Appenzeller its distinctive brown rind and complex flavor",
            "Appenzeller comes in Classic (3 months), Surchoix (4-6 months), and Extra (6+ months)"
        ],
        "tags": ["cheese", "traditional", "swiss", "appenzeller", "washed-rind", "herbal-brine", "700-years"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-beaufort-savoie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Beaufort (Savoie)",
        "category": "mains",
        "attribution": "Beaufortain, Savoie, France, Roman Era",
        "source_note": "Beaufort has been made in the French Alps since Roman times. Called 'the prince of Gruyères,' it's distinguished by its concave sides (from the wooden cerclage bands) and rich, nutty flavor.",
        "description": "Noble French Alpine cheese with a rich, complex flavor - distinguished by concave sides and centuries of mountain tradition.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "5-12 months aging",
        "total_time": "5-12 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Tarentaise or Abondance cattle traditionally"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining and rubbing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 91°F. (Traditional Beaufort uses only raw milk.)"},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (very small). Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 130°F over 30 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at 130°F for 45 minutes, stirring, until curds are very firm."},
            {"step": 7, "text": "Gather curds in cloth under the whey and transfer to mold. Use a wooden band (cerclage) around the mold that creates the distinctive concave sides."},
            {"step": 8, "text": "Press immediately at 30 lbs, increasing pressure to 75 lbs over 24 hours with multiple flips."},
            {"step": 9, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 10, "text": "Transfer to cave at 50°F and 95% humidity."},
            {"step": 11, "text": "Rub with dry salt and turn daily for first 2 weeks."},
            {"step": 12, "text": "Age minimum 5 months; 'Beaufort d'été' (summer) and 'Beaufort Chalet d'Alpage' (alpine) aged 12+ months."}
        ],
        "temperature": "91°F start, 130°F cook, 50°F aging",
        "notes": [
            "Traditional Beaufort wheels weigh 90-150 lbs - scale up significantly",
            "The concave sides come from the wooden cerclage band tightened during pressing",
            "Beaufort Chalet d'Alpage is made only in summer from high alpine pasture milk",
            "Unlike Gruyère, traditional Beaufort has no eyes (holes)",
            "The smooth, dense paste has complex flavors of butter, nuts, and flowers"
        ],
        "tags": ["cheese", "traditional", "french", "savoie", "alpine", "beaufort", "aged-cheese", "roman-era"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-ossau-iraty-basque",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ossau-Iraty (Basque Sheep Cheese)",
        "category": "mains",
        "attribution": "Basque Country (France/Spain), Ancient",
        "source_note": "Ossau-Iraty has been made by Basque shepherds in the Pyrenees for thousands of years. Named after the Ossau Valley and Iraty Forest, it's one of only two French sheep's milk cheeses with AOC/AOP status.",
        "description": "Ancient Basque sheep's milk cheese with a rich, nutty sweetness - made by Pyrenean shepherds for millennia.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Manech or Basco-Béarnaise breeds traditionally"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until firm clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 104°F over 30 minutes while stirring."},
            {"step": 6, "text": "Hold at 104°F for 30 minutes, stirring gently."},
            {"step": 7, "text": "Drain whey. Transfer curds to cloth-lined mold."},
            {"step": 8, "text": "Press at 15 lbs for 30 minutes."},
            {"step": 9, "text": "Flip and press at 30 lbs for 6 hours."},
            {"step": 10, "text": "Flip and press at 40 lbs for 12 hours."},
            {"step": 11, "text": "Dry salt or brine for 24-48 hours."},
            {"step": 12, "text": "Age at 50-55°F and 90% humidity for 3-12 months, turning weekly."},
            {"step": 13, "text": "Rub rind with olive oil if natural rind desired, or wax after 1 month."}
        ],
        "temperature": "86°F start, 104°F cook, 50-55°F aging",
        "notes": [
            "Sheep's milk produces a richer, more intensely flavored cheese than cow's milk",
            "Traditional Ossau-Iraty has a natural golden-brown rind",
            "The flavor is nutty and sweet with hints of caramel and lanolin",
            "Pairs perfectly with cherry jam (traditional Basque accompaniment)"
        ],
        "tags": ["cheese", "traditional", "french", "basque", "sheep-cheese", "ossau-iraty", "pyrenees", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-idiazabal-basque-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Idiazábal (Basque Smoked Sheep)",
        "category": "mains",
        "attribution": "Basque Country (Spain), Medieval",
        "source_note": "Idiazábal has been made by Basque shepherds since at least the medieval period. Traditionally smoked over cherry or beech wood, it developed its distinctive flavor from being stored in shepherd's huts near the hearth.",
        "description": "Smoky Basque sheep's milk cheese with intense, complex flavors - accidentally created by storage near shepherd's fires.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-6 months aging plus smoking",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Latxa or Carranzana breeds"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cherry or beech wood chips", "quantity": "as needed", "unit": "", "prep_note": "for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100-104°F over 30 minutes while stirring."},
            {"step": 6, "text": "Hold at 100-104°F for 30 minutes, stirring frequently."},
            {"step": 7, "text": "Drain whey and pack curds into cylindrical molds."},
            {"step": 8, "text": "Press at 20 lbs for 30 minutes."},
            {"step": 9, "text": "Flip and press at 40 lbs for 12-24 hours."},
            {"step": 10, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 11, "text": "Air dry for 1 week until surface is dry."},
            {"step": 12, "text": "Cold smoke over cherry or beech wood for 10-15 days (traditional method) or 2-4 days intensive."},
            {"step": 13, "text": "Age at 50°F and 85% humidity for 2-6 months."}
        ],
        "temperature": "86°F start, 100-104°F cook, 50°F aging",
        "notes": [
            "Traditional Idiazábal gets its smoke from extended exposure in shepherd's huts",
            "Unsmoked versions (ahumado sin humo) are also made but less common",
            "The cheese should have a golden-brown rind with smoky character throughout",
            "Pairs with Basque txakoli wine or Rioja",
            "The flavor intensifies with age - young is mild, aged is intensely savory"
        ],
        "tags": ["cheese", "traditional", "spanish", "basque", "sheep-cheese", "idiazabal", "smoked-cheese", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sbrinz-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sbrinz (Swiss)",
        "category": "mains",
        "attribution": "Central Switzerland, 16th Century+",
        "source_note": "Sbrinz is one of Switzerland's oldest and hardest cheeses, possibly predating Parmesan. It was a major trade item through the Gotthard Pass and may have influenced the development of Italian grana cheeses.",
        "description": "Switzerland's ancient hard cheese, intensely flavored and crystalline - historically traded across the Alps and possibly the ancestor of Parmesan.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "18-36 months aging",
        "total_time": "18-36 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from hay-fed cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F."},
            {"step": 2, "text": "Add starter culture and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 25-30 minutes until clean break."},
            {"step": 4, "text": "Cut curd into rice-sized grains (very small). Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 135°F over 40 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at 135°F for 45-60 minutes, stirring, until curds are very firm."},
            {"step": 7, "text": "Gather curds in cloth and press under whey briefly."},
            {"step": 8, "text": "Transfer to mold and press at 50 lbs immediately."},
            {"step": 9, "text": "Press at increasing weights up to 100 lbs over 24 hours with multiple flips."},
            {"step": 10, "text": "Brine for 3-4 weeks, turning daily (very long brining for Sbrinz)."},
            {"step": 11, "text": "Age at 55°F and 85% humidity for 18-36 months minimum."},
            {"step": 12, "text": "Turn weekly and brush the rind during aging."}
        ],
        "temperature": "90°F start, 135°F cook, 55°F aging",
        "notes": [
            "Traditional Sbrinz wheels weigh 55-100 lbs - scale up for authentic results",
            "The very long brining period (weeks vs hours) is unique to Sbrinz",
            "Sbrinz is so hard it's traditionally broken apart rather than cut",
            "Can be eaten in paper-thin shavings (Hobelkäse) or grated like Parmesan",
            "Some historians believe Sbrinz was the ancestor of Italian grana cheeses"
        ],
        "tags": ["cheese", "traditional", "swiss", "hard-cheese", "sbrinz", "grating-cheese", "16th-century", "aged-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
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
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
