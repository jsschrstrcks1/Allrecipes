#!/usr/bin/env python3
"""Add batch 45 - More traditional cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Traditional Cheeses
    {
        "id": "traditional-morbier-jura-ash",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Morbier (Jura Ash-Line Cheese)",
        "category": "mains",
        "attribution": "Jura, France / 19th Century",
        "source_note": "The ash line was originally vegetable ash sprinkled on evening milk curds to protect overnight before adding morning curds.",
        "description": "French pressed cheese with a distinctive black ash line through the center, semi-soft texture, and fruity, nutty flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "4 hours (2 sessions)",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "split into 2 batches"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "vegetable ash", "quantity": "2", "unit": "tbsp", "prep_note": "food-grade activated charcoal"},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "BATCH 1: Heat 1 gallon milk to 90°F. Add half culture and ripen 30 min."},
            {"step": 2, "text": "Add half rennet, let set 45 minutes, cut curds, stir while heating to 100°F."},
            {"step": 3, "text": "Drain curds and pack into mold to halfway. Press lightly for 1 hour."},
            {"step": 4, "text": "Sprinkle vegetable ash evenly over the surface of first layer."},
            {"step": 5, "text": "BATCH 2 (traditionally next morning): Repeat steps 1-3 with second gallon."},
            {"step": 6, "text": "Pack second batch curds on top of ash layer."},
            {"step": 7, "text": "Press at 20 lbs for 30 minutes, 40 lbs for 12 hours."},
            {"step": 8, "text": "Soak in brine for 12 hours."},
            {"step": 9, "text": "Age at 55°F, 95% humidity."},
            {"step": 10, "text": "Wash rind with brine twice weekly."},
            {"step": 11, "text": "Age 6-8 weeks until rind is orange-pink and paste is supple."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "Original ash was from pine wood or grape vines",
            "The two-batch method created the distinctive line",
            "Modern Morbier uses vegetable ash sprinkled on single batch",
            "AOC protected since 2000"
        ],
        "tags": ["cheese", "traditional", "french", "jura", "ash-line", "washed-rind", "19th-century", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-crowdie-scottish-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Crowdie (Scottish Fresh Cheese)",
        "category": "mains",
        "attribution": "Scottish Highlands / Ancient Celtic",
        "source_note": "One of Scotland's oldest cheeses, made by crofters for centuries. Name may come from Gaelic 'gruth' (curds).",
        "description": "Scottish fresh cheese with a crumbly, slightly grainy texture and tangy, lemony flavor. The original Highland cheese.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "24-48 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "raw milk traditional"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "heavy cream", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for richness"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to room temperature (68-72°F)."},
            {"step": 2, "text": "Stir in buttermilk."},
            {"step": 3, "text": "Cover and let stand at room temperature for 24-48 hours."},
            {"step": 4, "text": "Milk will clabber (thicken and sour)."},
            {"step": 5, "text": "Gently heat to 100°F to help curds separate."},
            {"step": 6, "text": "Pour into cheesecloth-lined colander."},
            {"step": 7, "text": "Drain for several hours until thick."},
            {"step": 8, "text": "Add salt and mix. Add cream if desired for richer texture."},
            {"step": 9, "text": "Store refrigerated, use within 1 week."}
        ],
        "temperature": "68-100°F",
        "notes": [
            "Traditional crofter cheese made without rennet",
            "The natural souring creates the characteristic tangy flavor",
            "Often mixed with cream or rolled in oats",
            "The name may relate to Gaelic word for curds"
        ],
        "tags": ["cheese", "traditional", "scottish", "highland", "fresh", "ancient", "celtic", "no-rennet"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-stracchino-italian-tired",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Stracchino (Italian 'Tired Cow' Cheese)",
        "category": "mains",
        "attribution": "Lombardy, Italy / Ancient",
        "source_note": "Name comes from 'stracca' (tired) - made from milk of cows tired from their descent from alpine pastures.",
        "description": "Italian soft, spreadable cheese with a mild, milky flavor and creamy, slightly runny texture when ripe.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "1-3 weeks aging",
        "total_time": "1-3 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": "small amount"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then small amount of diluted rennet."},
            {"step": 4, "text": "Let set for 45-60 minutes until soft curd forms."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Let rest 10 minutes, then gently ladle into flat rectangular molds."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, turning several times."},
            {"step": 8, "text": "Salt surfaces."},
            {"step": 9, "text": "Age at 50-55°F, 90% humidity for 1-3 weeks."},
            {"step": 10, "text": "Cheese becomes softer and more spreadable as it ages."}
        ],
        "temperature": "95°F make, 50-55°F aging",
        "notes": [
            "Made from milk of cows fatigued from alpine descent (transhumance)",
            "Tired cows produce richer milk with higher fat content",
            "Related to Gorgonzola and Taleggio",
            "Best eaten young when still fresh and mild"
        ],
        "tags": ["cheese", "traditional", "italian", "lombardy", "soft", "spreadable", "ancient", "transhumance"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-robiola-piemonte",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Robiola (Piedmont Fresh Cheese)",
        "category": "mains",
        "attribution": "Piedmont, Italy / Ancient",
        "source_note": "Name may come from Latin 'rubeum' (red) for the reddish rind, or from town of Robbio.",
        "description": "Piedmontese fresh to soft-ripened cheese made from various milks, with a creamy texture and mild, tangy flavor.",
        "servings_yield": "About 12 oz",
        "prep_time": "2 hours",
        "cook_time": "Fresh or 2-4 weeks aged",
        "total_time": "Fresh to 4 weeks",
        "ingredients": [
            {"item": "goat milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or cow, sheep, or blend"},
            {"item": "cow milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional for blend"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/32", "unit": "tsp", "prep_note": "optional for aged"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk(s) to 90°F."},
            {"step": 2, "text": "Add cultures and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 1 hour."},
            {"step": 4, "text": "Cut curds into 1-inch pieces."},
            {"step": 5, "text": "Let rest 10 minutes."},
            {"step": 6, "text": "Gently ladle into small round or square molds."},
            {"step": 7, "text": "Let drain at room temperature for 24-48 hours."},
            {"step": 8, "text": "Salt lightly."},
            {"step": 9, "text": "FOR FRESH: Eat within 1 week."},
            {"step": 10, "text": "FOR AGED: Age at 55°F, 90% humidity for 2-4 weeks until rind forms."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "Many varieties exist: Robiola di Roccaverano (goat, DOP), Robiola Bosina (cow/sheep)",
            "Can be eaten fresh or aged with bloomy rind",
            "Traditional to wrap aged versions in leaves",
            "One of Piedmont's most beloved cheeses"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "fresh", "soft", "ancient", "mixed-milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-castelmagno-piedmont-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Castelmagno (Piedmont Ancient Blue)",
        "category": "mains",
        "attribution": "Piedmont, Italy / 11th Century",
        "source_note": "Mentioned in documents from 1277 as payment for rent. Made in the Castelmagno valley in the Cottian Alps.",
        "description": "Ancient Piedmontese cheese that develops natural blue veining with age, crumbly texture, and intense complex flavor.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "3", "unit": "gallons", "prep_note": "from alpine pasture"},
            {"item": "sheep or goat milk", "quantity": "1", "unit": "quart", "prep_note": "optional traditional blend"},
            {"item": "natural whey starter", "quantity": "1", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat combined milks to 95°F."},
            {"step": 2, "text": "Add whey starter and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 45 minutes."},
            {"step": 4, "text": "Break curds into hazelnut-sized pieces."},
            {"step": 5, "text": "Let curds rest, then drain and let acidify overnight."},
            {"step": 6, "text": "Next day, break up curds and add salt."},
            {"step": 7, "text": "Pack into mold and press lightly for several hours."},
            {"step": 8, "text": "Age at 50°F, 85% humidity."},
            {"step": 9, "text": "Turn regularly. Natural blue mold develops in cracks."},
            {"step": 10, "text": "Age minimum 3 months. Best at 6-12 months."}
        ],
        "temperature": "95°F make, 50°F aging",
        "notes": [
            "One of Italy's most ancient cheeses, documented since 1277",
            "Blue mold develops naturally in cracks - not inoculated",
            "Becomes crumbly with age, developing intense savory flavor",
            "DOP protected - must be made in Castelmagno valley"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "blue", "11th-century", "ancient", "alpine", "dop"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-montasio-friuli-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Montasio (Friuli Ancient Cheese)",
        "category": "mains",
        "attribution": "Friuli-Venezia Giulia, Italy / 13th Century",
        "source_note": "Created by Benedictine monks at Moggio Udinese Abbey. Named after the Montasio plateau.",
        "description": "Friulian pressed cheese with sweet, nutty flavor when young, becoming sharper and crystalline with age.",
        "servings_yield": "About 4 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "2-18 months aging",
        "total_time": "2-18 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "3", "unit": "gallons", "prep_note": "from alpine pastures"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 92°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30 minutes."},
            {"step": 4, "text": "Cut curds to rice grain size."},
            {"step": 5, "text": "Stir while heating to 115°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at temperature for 20 more minutes."},
            {"step": 7, "text": "Drain curds and pack into round mold."},
            {"step": 8, "text": "Press at 30 lbs for 30 minutes, 60 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 2 days."},
            {"step": 10, "text": "Age at 50-55°F, 85% humidity."},
            {"step": 11, "text": "Fresco: 2-4 months. Mezzano: 5-10 months. Stagionato: 12+ months."}
        ],
        "temperature": "92-115°F make, 50-55°F aging",
        "notes": [
            "Created by monks to preserve surplus mountain milk",
            "Used to make frico, the famous Friulian cheese crisp",
            "Young Montasio is sweet and mild; aged is sharp and granular",
            "DOP protected since 1986"
        ],
        "tags": ["cheese", "traditional", "italian", "friuli", "13th-century", "monastery", "dop", "alpine", "benedictine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-piave-dolomites",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Piave (Dolomite Mountain Cheese)",
        "category": "mains",
        "attribution": "Belluno, Italy / Modern Traditional",
        "source_note": "Named after the Piave River flowing from the Dolomites. Modern cheese following traditional alpine methods.",
        "description": "Veneto mountain cheese with a dense, crystalline texture and sweet, nutty flavor that intensifies with age.",
        "servings_yield": "About 4 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "1-18 months aging",
        "total_time": "1-18 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "3", "unit": "gallons", "prep_note": "from Dolomite pastures"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30 minutes."},
            {"step": 4, "text": "Cut curds to small rice grain size."},
            {"step": 5, "text": "Stir while heating to 118°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at temperature for 30 more minutes."},
            {"step": 7, "text": "Drain curds and pack into round mold."},
            {"step": 8, "text": "Press at 40 lbs for 1 hour, 60 lbs for 24 hours."},
            {"step": 9, "text": "Soak in brine for 2-3 days."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "Fresco: 20-60 days. Mezzano: 2-6 months. Vecchio: 6-12 months. Stravecchio: 18+ months."}
        ],
        "temperature": "95-118°F make, 55°F aging",
        "notes": [
            "DOP protected since 2010",
            "Four aging classifications from mild to very sharp",
            "Stravecchio develops crunchy protein crystals like aged Parmesan",
            "Named after the river that flows through the Dolomite valleys"
        ],
        "tags": ["cheese", "traditional", "italian", "veneto", "dolomites", "mountain", "dop", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-bra-piedmont",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bra (Piedmont Town Cheese)",
        "category": "mains",
        "attribution": "Bra, Piedmont, Italy / Medieval",
        "source_note": "Named after the town of Bra where it was aged and traded. Made in surrounding alpine valleys.",
        "description": "Piedmontese cheese made from cow milk (or mixed), with a firm texture and savory flavor that varies from mild to sharp.",
        "servings_yield": "About 4 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "45 days to 6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "partially skimmed cow milk", "quantity": "3", "unit": "gallons", "prep_note": "some cream removed"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Partially skim milk (traditional uses evening + morning milk)."},
            {"step": 2, "text": "Heat to 95°F."},
            {"step": 3, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 4, "text": "Add diluted rennet and let set for 40 minutes."},
            {"step": 5, "text": "Cut curds to hazelnut size."},
            {"step": 6, "text": "Stir gently while heating to 104°F."},
            {"step": 7, "text": "Drain and pack into round mold."},
            {"step": 8, "text": "Press at 30 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 9, "text": "Dry salt surfaces over several days."},
            {"step": 10, "text": "Age at 50-55°F, 85% humidity."},
            {"step": 11, "text": "Bra Tenero: 45 days. Bra Duro: 6+ months."}
        ],
        "temperature": "95-104°F make, 50-55°F aging",
        "notes": [
            "Named after the town of Bra, a historic cheese trading center",
            "Bra d'Alpeggio is the summer alpine version (even more prized)",
            "Can be made from cow milk alone or blended with sheep/goat",
            "DOP protected with two main styles: Tenero (soft) and Duro (hard)"
        ],
        "tags": ["cheese", "traditional", "italian", "piedmont", "medieval", "dop", "alpine"],
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
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
