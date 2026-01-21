#!/usr/bin/env python3
"""Add batch 34 of traditional cheese recipes - Ancient British, Spanish, and Latin American cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-stinking-bishop-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Stinking Bishop (English Washed-Rind)",
        "category": "mains",
        "attribution": "Gloucestershire, England / Modern Revival of Medieval",
        "source_note": "Revived by Charles Martell in 1972 based on medieval Cistercian recipes. Named after the Stinking Bishop pear used to wash the rind.",
        "description": "Pungent English washed-rind cheese made from Gloucester cattle milk and washed with perry, with a soft creamy interior.",
        "servings_yield": "About 1 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "Gloucester cattle traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "perry or pear cider", "quantity": "1", "unit": "cup", "prep_note": "for washing rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Stir gently and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed."},
            {"step": 4, "text": "Add diluted rennet and let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently for 30 minutes at 86°F."},
            {"step": 7, "text": "Ladle curds into round mold. Press lightly for 4 hours, flipping twice."},
            {"step": 8, "text": "Salt all surfaces and let dry at room temperature for 1-2 days."},
            {"step": 9, "text": "Move to cave at 55°F, 95% humidity."},
            {"step": 10, "text": "Wash rind with perry every 2-3 days."},
            {"step": 11, "text": "Continue washing for 6-8 weeks until rind is orange-pink and pungent."},
            {"step": 12, "text": "Interior should be soft and bulging when ripe."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "The perry (pear cider) wash creates the distinctive aroma",
            "Named after the Stinking Bishop pear variety, not an ecclesiastic",
            "Featured in Wallace & Gromit's 'The Curse of the Were-Rabbit'",
            "One of England's most pungent cheeses"
        ],
        "tags": ["cheese", "traditional", "english", "washed-rind", "pungent", "perry", "gloucestershire", "medieval-revival"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-yarg-cornish-nettle",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cornish Yarg (Nettle-Wrapped Cheese)",
        "category": "mains",
        "attribution": "Cornwall, England / 1980s Revival of 17th Century",
        "source_note": "Based on a 17th-century recipe. The nettle wrapping creates a distinctive appearance and imparts subtle flavors.",
        "description": "Cornish semi-hard cheese wrapped in stinging nettle leaves, creating a beautiful edible green coating and slightly earthy flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "5-7 weeks aging",
        "total_time": "5-7 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "stinging nettle leaves", "quantity": "40-50", "unit": "leaves", "prep_note": "blanched and dried"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently while raising temperature to 95°F over 30 minutes."},
            {"step": 7, "text": "Hold at 95°F for 20 more minutes, stirring."},
            {"step": 8, "text": "Drain curds and pack into round mold."},
            {"step": 9, "text": "Press at 20 lbs for 30 minutes, flip, 40 lbs for 12 hours."},
            {"step": 10, "text": "Soak in saturated brine for 8 hours."},
            {"step": 11, "text": "Blanch nettle leaves briefly in boiling water, pat dry."},
            {"step": 12, "text": "Cover entire cheese surface with overlapping nettle leaves."},
            {"step": 13, "text": "Age at 50-55°F, 85% humidity for 5-7 weeks."}
        ],
        "temperature": "88-95°F make, 50-55°F aging",
        "notes": [
            "Blanching removes the sting from nettles",
            "The nettle coating is edible and imparts subtle grassy flavor",
            "White mold may grow through the nettles - this is expected",
            "Interior is creamy beneath the rind, firmer at center"
        ],
        "tags": ["cheese", "traditional", "english", "cornish", "nettle-wrapped", "semi-hard", "17th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cabrales-spanish-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cabrales (Spanish Cave-Aged Blue)",
        "category": "mains",
        "attribution": "Asturias, Spain / Ancient",
        "source_note": "Cave-aged blue cheese from the Picos de Europa mountains. Made for centuries in natural limestone caves.",
        "description": "Intense Spanish blue cheese aged in natural mountain caves, made from mixed milks with complex spicy blue veining.",
        "servings_yield": "About 5 lbs",
        "prep_time": "4 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "raw goat milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "raw sheep milk", "quantity": "1", "unit": "quart", "prep_note": "optional traditional blend"},
            {"item": "mesophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 1 hour."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Let curds rest 10 minutes, then stir gently for 30 minutes."},
            {"step": 6, "text": "Drain whey and salt curds directly."},
            {"step": 7, "text": "Pack curds loosely into tall cylindrical mold - do not press."},
            {"step": 8, "text": "Turn every 2 hours for 24 hours."},
            {"step": 9, "text": "Unmold and salt exterior."},
            {"step": 10, "text": "Age at 45-50°F (cave temperature) with 90-95% humidity."},
            {"step": 11, "text": "Pierce with needles after 2 weeks to allow air for blue development."},
            {"step": 12, "text": "Age 2-6 months, turning weekly. Rind develops natural molds."}
        ],
        "temperature": "86°F make, 45-50°F cave aging",
        "notes": [
            "Traditional caves in Picos de Europa maintain perfect conditions year-round",
            "Three milks creates the complex flavor - proportions vary by season",
            "No pressing allows open texture for blue mold penetration",
            "One of Spain's most intense blue cheeses - not for beginners"
        ],
        "tags": ["cheese", "traditional", "spanish", "blue", "cave-aged", "mixed-milk", "asturias", "pdo", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mahon-menorcan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mahón-Menorca (Spanish Island Cheese)",
        "category": "mains",
        "attribution": "Menorca, Spain / Ancient",
        "source_note": "Made on Menorca since prehistoric times. The distinctive square shape comes from being wrapped in cloth (fogasser).",
        "description": "Menorcan cheese with a distinctive square shape and orange rubbed rind, ranging from mild when young to sharp when aged.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-10 months aging",
        "total_time": "2-10 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "3", "unit": "gallons", "prep_note": "Menorcan Friesian traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup", "prep_note": "for rind"},
            {"item": "paprika", "quantity": "2", "unit": "tbsp", "prep_note": "for rind color"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch pieces."},
            {"step": 6, "text": "Stir gently while heating to 100°F over 30 minutes."},
            {"step": 7, "text": "Drain curds and gather into cloth (fogasser), tying corners."},
            {"step": 8, "text": "Press in cloth to form characteristic square shape."},
            {"step": 9, "text": "Press at 30 lbs for 12 hours."},
            {"step": 10, "text": "Soak in saturated brine for 24 hours."},
            {"step": 11, "text": "Age at 55°F, 85% humidity."},
            {"step": 12, "text": "Rub rind with olive oil and paprika weekly."},
            {"step": 13, "text": "Age 2 months (tierno), 5 months (semi-curado), or 10+ months (curado)."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "The fogasser cloth creates the distinctive rounded square shape",
            "Paprika and olive oil rub creates the orange rind",
            "Young Mahón is mild and buttery; aged is sharp and crystalline",
            "Archaeological evidence suggests cheesemaking on Menorca for 4,000 years"
        ],
        "tags": ["cheese", "traditional", "spanish", "menorcan", "aged", "pdo", "island", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-torta-del-casar-spanish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Torta del Casar (Spanish Creamy Sheep Cheese)",
        "category": "mains",
        "attribution": "Extremadura, Spain / Ancient",
        "source_note": "Made in Casar de Cáceres since ancient times. Uses thistle rennet which creates the distinctive creamy interior.",
        "description": "Spanish sheep milk cheese with a runny creamy interior, coagulated with wild thistle and eaten by cutting off the top.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "raw Merino sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "dried cardoon thistle", "quantity": "2", "unit": "tbsp", "prep_note": "crushed, soaked in water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Soak crushed cardoon thistle flowers in 1/4 cup warm water for 2 hours."},
            {"step": 2, "text": "Strain thistle extract and reserve liquid."},
            {"step": 3, "text": "Heat sheep milk to 82-86°F - lower temperature than usual."},
            {"step": 4, "text": "Add thistle extract slowly while stirring gently."},
            {"step": 5, "text": "Let set for 1-2 hours - thistle rennet works slowly."},
            {"step": 6, "text": "Cut delicate curds into 1-inch pieces."},
            {"step": 7, "text": "Let rest 15 minutes, then gently ladle into flat round molds."},
            {"step": 8, "text": "Press very lightly for 24 hours, turning several times."},
            {"step": 9, "text": "Salt surfaces and let dry for 2-3 days."},
            {"step": 10, "text": "Age at 50-55°F, 90% humidity for 6-8 weeks."},
            {"step": 11, "text": "Turn every few days. Rind will wrinkle as interior becomes runny."},
            {"step": 12, "text": "When ripe, cut off top and scoop creamy interior with bread."}
        ],
        "temperature": "82-86°F make, 50-55°F aging",
        "notes": [
            "Thistle (cardoon) rennet creates the signature runny interior",
            "The enzymes in thistle break down the proteins over time",
            "Traditional serving: cut off top like a lid, scoop out with crusty bread",
            "PDO protected - must be from specific sheep breeds in Extremadura"
        ],
        "tags": ["cheese", "traditional", "spanish", "sheep", "thistle-rennet", "creamy", "pdo", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-palmero-canary",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Palmero (Canary Islands Smoked)",
        "category": "mains",
        "attribution": "La Palma, Canary Islands / Ancient",
        "source_note": "Made by the Guanche people before Spanish conquest. Smoked over almond shells and prickly pear wood.",
        "description": "Canary Islands goat cheese from La Palma, traditionally smoked over almond shells and prickly pear, with a distinctive smoky flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "Palmera goat traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "almond shells", "quantity": "2", "unit": "cups", "prep_note": "for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 88°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 1 hour."},
            {"step": 4, "text": "Cut curds into small pieces."},
            {"step": 5, "text": "Stir and heat gently to 95°F over 20 minutes."},
            {"step": 6, "text": "Drain curds and pack into cylindrical mold."},
            {"step": 7, "text": "Press at 25 lbs for 4 hours, flip, 40 lbs for 12 hours."},
            {"step": 8, "text": "Soak in brine for 24 hours."},
            {"step": 9, "text": "Air dry for 1-2 weeks until firm surface."},
            {"step": 10, "text": "Cold smoke with almond shells for 2-3 weeks, a few hours each day."},
            {"step": 11, "text": "Age at 55°F for 3-6 months total."}
        ],
        "temperature": "88-95°F make, cold smoke, 55°F aging",
        "notes": [
            "Pre-Hispanic Guanche people made cheese before Spanish arrival",
            "Traditional smoking uses almond shells and prickly pear wood",
            "PDO protected - must be from La Palma goats",
            "Exterior darkens from smoking; interior remains white to ivory"
        ],
        "tags": ["cheese", "traditional", "spanish", "canary-islands", "goat", "smoked", "pdo", "ancient", "guanche"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queijo-do-pico-azorean",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo do Pico (Azorean Island Cheese)",
        "category": "mains",
        "attribution": "Pico Island, Azores / 16th Century",
        "source_note": "Made on Pico Island in the Azores since Portuguese settlement. The volcanic island's unique grass gives distinctive flavor.",
        "description": "Azorean island cheese from Pico with a buttery texture and complex flavor influenced by the volcanic island's unique pastures.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 weeks aging",
        "total_time": "3-6 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "from pasture-fed cows"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently and heat to 100°F over 30 minutes."},
            {"step": 6, "text": "Drain curds and pack into round mold."},
            {"step": 7, "text": "Press at 15 lbs for 30 minutes, flip, 30 lbs for 6 hours."},
            {"step": 8, "text": "Soak in brine for 6-8 hours."},
            {"step": 9, "text": "Age at 55°F, 85% humidity."},
            {"step": 10, "text": "Turn every other day."},
            {"step": 11, "text": "Ready in 3-6 weeks when paste is smooth and buttery."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "The volcanic soil of Pico Island creates unique pasture",
            "Cows graze on grass growing in lava rock walls",
            "Cheese has slightly salty, oceanic notes from island climate",
            "PDO protected - must be made on Pico Island"
        ],
        "tags": ["cheese", "traditional", "portuguese", "azorean", "island", "aged", "pdo", "16th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-de-cabra-al-vino-spanish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso de Cabra al Vino (Spanish Wine-Washed Goat)",
        "category": "mains",
        "attribution": "Murcia, Spain / Ancient",
        "source_note": "Murcian tradition of washing goat cheese in local red wine, creating a distinctive purple rind and wine-infused flavor.",
        "description": "Spanish goat cheese washed in red wine, creating a beautiful purple-red rind and subtle fruity, tannic notes in the paste.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "Murcian goat traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "dry red wine", "quantity": "2", "unit": "cups", "prep_note": "Monastrell or Jumilla"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes until firm curd."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently and heat to 100°F over 20 minutes."},
            {"step": 7, "text": "Drain curds and press into cylindrical mold at 25 lbs for 6 hours."},
            {"step": 8, "text": "Flip and press at 40 lbs for 12 hours."},
            {"step": 9, "text": "Soak in saturated brine for 12 hours."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "After 1 week, begin washing rind with red wine every 2-3 days."},
            {"step": 12, "text": "Continue wine washing for 2-3 months until rind is deep purple."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "Local Monastrell or Jumilla wines are traditional for washing",
            "The wine tannins preserve the rind and add flavor",
            "Purple color deepens with longer aging and more wine washes",
            "Interior remains white to pale yellow, with subtle wine notes"
        ],
        "tags": ["cheese", "traditional", "spanish", "goat", "wine-washed", "murcia", "aged", "ancient"],
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
