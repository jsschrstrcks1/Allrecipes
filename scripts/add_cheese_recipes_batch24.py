#!/usr/bin/env python3
"""Add batch 24 of traditional cheese recipes - Italian regional cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-piave-veneto",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Piave (Veneto)",
        "category": "mains",
        "attribution": "Belluno Province, Veneto, Italy, 1960s (formalized)",
        "source_note": "Piave cheese is named after the Piave River in the Dolomite mountains of Veneto. While the formalized version dates to the 1960s, similar cheeses have been made in the Belluno province for centuries.",
        "description": "Alpine cheese from the Dolomites with a sweet, nutty flavor that intensifies with age - Italy's answer to Parmesan for grating.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "1-18 months aging",
        "total_time": "1-18 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Alpine cattle"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-35 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (small). Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 118°F over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at 118°F for 30 minutes until curds are firm."},
            {"step": 7, "text": "Drain whey and transfer curds to mold."},
            {"step": 8, "text": "Press at 20 lbs for 30 minutes. Flip and press at 40 lbs for 12 hours."},
            {"step": 9, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 55°F and 85% humidity. Fresco: 1 month; Mezzano: 6 months; Vecchio: 12 months; Stravecchio: 18+ months."}
        ],
        "temperature": "95°F start, 118°F cook, 55°F aging",
        "notes": [
            "Piave becomes increasingly hard and intense with age",
            "Young Piave (Fresco) is mild and sliceable; aged (Vecchio) is hard and grateable",
            "The flavor develops sweet, butterscotch notes with proper aging",
            "DOP protected since 2010"
        ],
        "tags": ["cheese", "traditional", "italian", "veneto", "alpine", "piave", "hard-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-montasio-friuli",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Montasio (Friuli-Venezia Giulia)",
        "category": "mains",
        "attribution": "Julian Alps, Italy, 13th Century",
        "source_note": "Montasio was created by Benedictine monks at Moggio Udinese Abbey in the 1200s. Named after the Montasio mountain massif, it's a cornerstone of Friulian cuisine and essential for frico (crispy cheese wafers).",
        "description": "Medieval Alpine cheese from the Julian Alps, essential for making frico - the crispy cheese wafers of Friuli.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "2-18 months aging",
        "total_time": "2-18 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 93°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 25-30 minutes until clean break."},
            {"step": 4, "text": "Cut curd into rice-sized grains. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 115°F over 30 minutes while stirring constantly."},
            {"step": 6, "text": "Continue stirring at 115°F for 20 minutes until curds are firm."},
            {"step": 7, "text": "Drain whey and transfer curds to mold."},
            {"step": 8, "text": "Press at 15 lbs for 30 minutes. Flip and press at 35 lbs for 12 hours."},
            {"step": 9, "text": "Brine for 24-36 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 50-55°F and 85% humidity. Fresco: 2 months; Mezzano: 5-10 months; Stravecchio: 12-18 months."}
        ],
        "temperature": "93°F start, 115°F cook, 50-55°F aging",
        "notes": [
            "Young Montasio is semi-soft with mild, milky flavor",
            "Aged Montasio becomes hard, sharp, and excellent for grating",
            "Essential for frico - shredded cheese cooked into crispy wafers",
            "DOP protected since 1996"
        ],
        "tags": ["cheese", "traditional", "italian", "friuli", "alpine", "montasio", "monastery-cheese", "13th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-bra-piedmont",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bra (Piedmont)",
        "category": "mains",
        "attribution": "Bra, Piedmont, Italy, Medieval",
        "source_note": "Bra cheese is named after the town of Bra in Cuneo province, Piedmont, where it has been made and traded since medieval times. There are two types: Tenero (soft) and Duro (hard).",
        "description": "Piedmontese cheese from the town of Bra, made in two styles - soft Tenero for eating and hard Duro for grating.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "45 days - 6 months aging",
        "total_time": "45 days - 6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1.5", "unit": "gallons", "prep_note": ""},
            {"item": "sheep or goat milk", "quantity": "0.5", "unit": "gallon", "prep_note": "traditional blend"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 90°F. Add calcium chloride if using pasteurized."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 40-50 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes while maintaining 90°F."},
            {"step": 6, "text": "For Bra Tenero: Keep curds softer, minimal heating. For Bra Duro: Raise to 104°F."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 15 lbs for 2 hours. Flip and press at 30 lbs for 12 hours."},
            {"step": 9, "text": "Dry salt or brine for 12-24 hours."},
            {"step": 10, "text": "Age at 55°F. Bra Tenero: 45 days minimum. Bra Duro: 6+ months."}
        ],
        "temperature": "90°F for Tenero, up to 104°F for Duro, 55°F aging",
        "notes": [
            "Bra Tenero has a soft, elastic paste and mild flavor",
            "Bra Duro is hard, grainy, and sharp - suitable for grating",
            "Traditional Bra often includes small amounts of sheep or goat milk",
            "Bra d'Alpeggio is made only in summer from high pasture milk"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "bra", "mixed-milk", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-toma-piedmontese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Toma Piemontese",
        "category": "mains",
        "attribution": "Piedmont, Italy, Ancient",
        "source_note": "Toma is a generic name for traditional Alpine cheeses made throughout Piedmont and the Aosta Valley for centuries. Each valley has its own variation, but all share the characteristic semi-soft texture and earthy flavor.",
        "description": "Traditional Piedmontese Alpine cheese, varying by valley but always earthy and semi-soft - the everyday cheese of mountain communities.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "15-60 days aging",
        "total_time": "15-60 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "or partially skimmed"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 35-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently while raising temperature to 104°F over 20 minutes."},
            {"step": 6, "text": "Continue stirring at 104°F for 15 minutes."},
            {"step": 7, "text": "Drain whey and transfer curds to flat round molds."},
            {"step": 8, "text": "Press lightly at 10 lbs for 2 hours."},
            {"step": 9, "text": "Flip and press at 20 lbs for 8-12 hours."},
            {"step": 10, "text": "Dry salt or brine for 12 hours."},
            {"step": 11, "text": "Age at 50-55°F and 90% humidity for 15-60 days, turning regularly."}
        ],
        "temperature": "95°F start, 104°F cook, 50-55°F aging",
        "notes": [
            "Toma is a family of cheeses - each valley makes its own version",
            "Semi-soft texture with natural gray-brown rind",
            "Younger Toma is mild and milky; older becomes more complex",
            "Toma Piemontese has DOP status; many local tomas do not"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "alpine", "toma", "semi-soft", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-puzzone-moena",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Puzzone di Moena (Spretz Tzaorì)",
        "category": "mains",
        "attribution": "Moena, Trentino, Italy, Medieval",
        "source_note": "Puzzone di Moena (also called Spretz Tzaorì in Ladin) translates as 'stinky one from Moena.' This pungent washed-rind cheese has been made in the Fassa Valley of Trentino since medieval times.",
        "description": "Pungent Trentino cheese whose name means 'stinky one' - a traditional washed-rind Alpine cheese with intense aroma and flavor.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "light brine", "quantity": "2", "unit": "cups", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add starter and B. linens, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 35-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Raise temperature to 104°F over 20 minutes while stirring."},
            {"step": 6, "text": "Continue stirring for 20 minutes at 104°F."},
            {"step": 7, "text": "Drain whey and transfer curds to round molds."},
            {"step": 8, "text": "Press at 15 lbs for 2 hours. Flip and press at 30 lbs for 12 hours."},
            {"step": 9, "text": "Dry salt all surfaces. Let rest 24 hours."},
            {"step": 10, "text": "Age at 55°F and 95% humidity, washing with brine 2-3 times per week."},
            {"step": 11, "text": "Age for 3-6 months. The rind should become sticky and orange-brown."}
        ],
        "temperature": "95°F start, 104°F cook, 55°F aging",
        "notes": [
            "The name 'Puzzone' (stinky) is well-earned - this is a very pungent cheese",
            "The aroma is much stronger than the flavor, which is rich and savory",
            "Traditional aging was in caves of the Dolomites",
            "DOP protected as part of the Trentino cheese tradition"
        ],
        "tags": ["cheese", "traditional", "italian", "trentino", "washed-rind", "puzzone", "pungent", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-canestrato-sicilian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Canestrato (Sicilian Basket Cheese)",
        "category": "mains",
        "attribution": "Sicily, Italy, Ancient",
        "source_note": "Canestrato gets its name from 'canestro' (basket) - the woven reed baskets traditionally used to drain and shape the cheese, which leave distinctive marks on the rind. It's been made in Sicily since ancient Greek and Roman times.",
        "description": "Ancient Sicilian cheese marked by its basket mold, made from sheep's milk with a sharp, tangy flavor that intensifies with age.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "4-12 months aging",
        "total_time": "4-12 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "or mixed sheep/goat"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "traditionally lamb rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "whole black peppercorns", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for Pepato version"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Raise temperature to 118°F over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring for 20 minutes at 118°F until curds are firm."},
            {"step": 7, "text": "Drain whey. If making Pepato, fold in peppercorns now."},
            {"step": 8, "text": "Transfer curds to basket-weave molds (or regular molds with textured liner)."},
            {"step": 9, "text": "Press at 20 lbs for 2 hours. Flip and press at 40 lbs for 12 hours."},
            {"step": 10, "text": "Dry salt all surfaces over 3-4 days."},
            {"step": 11, "text": "Age at 55°F and 85% humidity for 4-12 months."}
        ],
        "temperature": "95°F start, 118°F cook, 55°F aging",
        "notes": [
            "The basket-weave pattern on the rind is the signature of canestrato",
            "Canestrato Siciliano DOP must be made from sheep's milk",
            "Canestrato Pepato has whole black peppercorns folded in",
            "Young canestrato is semi-hard and tangy; aged becomes hard and sharp"
        ],
        "tags": ["cheese", "traditional", "italian", "sicilian", "sheep-cheese", "canestrato", "basket-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-castelmagno-piedmont",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Castelmagno (Piedmont)",
        "category": "mains",
        "attribution": "Castelmagno, Piedmont, Italy, 13th Century",
        "source_note": "Castelmagno is one of Italy's most ancient and prestigious cheeses, first documented in 1277 when it was accepted as payment of debts. Made in only three communes in the Grana Valley, it develops natural blue veining with age.",
        "description": "Ancient Piedmontese cheese that develops natural blue veining - one of Italy's rarest and most prestigious cheeses since the 13th century.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "1.5", "unit": "gallons", "prep_note": "partially skimmed traditionally"},
            {"item": "sheep or goat milk", "quantity": "0.5", "unit": "gallon", "prep_note": "optional traditional addition"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 15 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 95°F."},
            {"step": 6, "text": "Drain whey. Let curds rest for 24-48 hours at room temperature, developing natural acid."},
            {"step": 7, "text": "Break up the matted curd and mix with fresh curds from a new batch (traditional method)."},
            {"step": 8, "text": "Salt the mixed curds and transfer to molds."},
            {"step": 9, "text": "Press at 20 lbs for 2 hours. Flip and press at 35 lbs for 24 hours."},
            {"step": 10, "text": "Age at 50°F and 95% humidity for 2-6 months."},
            {"step": 11, "text": "Blue veining develops naturally in cracks and crevices without inoculation."}
        ],
        "temperature": "95°F make, 50°F aging",
        "notes": [
            "Traditional Castelmagno uses curds from two consecutive days mixed together",
            "The natural blue veining comes from wild Penicillium in the aging caves",
            "Young Castelmagno is ivory and crumbly; aged develops blue-green veins",
            "One of Italy's rarest DOP cheeses, made in only 3 communes"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "blue-cheese", "castelmagno", "13th-century", "rare"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-robiola-piedmont",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Robiola (Piedmont)",
        "category": "mains",
        "attribution": "Piedmont/Lombardy, Italy, Celtic Era",
        "source_note": "Robiola is one of Italy's most ancient cheeses, possibly dating to Celtic times. The name may derive from the town of Robbio or from 'rubeolus' (reddish) describing the rind. Made in various forms throughout Piedmont and Lombardy.",
        "description": "Ancient soft Italian cheese from the hills of Piedmont and Lombardy, creamy and mild with a thin edible rind.",
        "servings_yield": "About 1 lb (several small rounds)",
        "prep_time": "2 hours",
        "cook_time": "1-3 weeks aging",
        "total_time": "1-3 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or mixed milk"},
            {"item": "goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional for mixed robiola"},
            {"item": "mesophilic starter culture", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted in 1 tbsp water"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 86°F."},
            {"step": 2, "text": "Add starter culture, stir, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet (very small amount), stir gently. Let set 12-18 hours at room temperature."},
            {"step": 4, "text": "The curd should be very soft and delicate."},
            {"step": 5, "text": "Gently ladle the soft curd into small round molds."},
            {"step": 6, "text": "Let drain at room temperature for 24 hours, flipping carefully several times."},
            {"step": 7, "text": "Unmold and salt lightly."},
            {"step": 8, "text": "Fresh Robiola can be eaten immediately."},
            {"step": 9, "text": "For aged Robiola, place at 55°F and 85% humidity for 1-3 weeks."},
            {"step": 10, "text": "A thin wrinkled rind will develop; the interior should remain creamy."}
        ],
        "temperature": "86°F make, 55°F aging if desired",
        "notes": [
            "Robiola is a family of cheeses with many regional variations",
            "Robiola di Roccaverano DOP uses goat or mixed milk",
            "Fresh Robiola is very mild and creamy; aged develops more tang",
            "The thin, wrinkled rind is edible and adds character"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "soft-cheese", "robiola", "ancient", "celtic"],
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
