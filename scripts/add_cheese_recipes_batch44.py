#!/usr/bin/env python3
"""Add batch 44 - More traditional cheeses and cheesemaking heritage tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Traditional European Cheeses
    {
        "id": "traditional-salers-auvergne-raw",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Salers (Auvergne Raw Milk Cheese)",
        "category": "mains",
        "attribution": "Auvergne, France / Ancient",
        "source_note": "Made only during summer grazing season (May-October) from Salers cattle. The strictest AOC rules of any French cheese.",
        "description": "Raw milk Auvergnat cheese made on-farm during summer grazing, with robust earthy flavor and firm texture.",
        "servings_yield": "About 8 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "3-18 months aging",
        "total_time": "3-18 months",
        "ingredients": [
            {"item": "raw Salers cow milk", "quantity": "6", "unit": "gallons", "prep_note": "must be milked in presence of calf"},
            {"item": "natural whey starter", "quantity": "1", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "liquid rennet", "quantity": "1.5", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Milk Salers cow with calf present (required by AOC)."},
            {"step": 2, "text": "Transfer warm milk immediately to gerle (traditional wooden vat)."},
            {"step": 3, "text": "Add whey starter from previous batch."},
            {"step": 4, "text": "Add rennet and let set for 1 hour."},
            {"step": 5, "text": "Break curds and heat to 100°F while stirring."},
            {"step": 6, "text": "Drain whey and press curds in cloth."},
            {"step": 7, "text": "Let rest 12-24 hours (tomme stage)."},
            {"step": 8, "text": "Break up tomme, add salt, let rest again."},
            {"step": 9, "text": "Pack into large molds (35-50 kg traditional)."},
            {"step": 10, "text": "Press heavily for 48 hours."},
            {"step": 11, "text": "Age at 50°F, 95% humidity for minimum 3 months."},
            {"step": 12, "text": "Brush rind regularly. Age up to 18 months for full flavor."}
        ],
        "temperature": "100°F make, 50°F aging",
        "notes": [
            "Strictest AOC in France - must be farm-made during summer grazing",
            "Salers cattle only let down milk with calf present",
            "Traditional gerle (wooden vat) adds wild cultures",
            "Tomme Fraîche de Salers is the fresh curd used in aligot"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "raw-milk", "ancient", "aoc", "summer-only", "salers-cattle"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-laguiole-aubrac",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Laguiole (Aubrac Mountain Cheese)",
        "category": "mains",
        "attribution": "Aubrac, France / 12th Century",
        "source_note": "Created by monks at Aubrac monastery. Made during transhumance (mountain grazing) season.",
        "description": "Aubrac mountain cheese with a firm, supple texture and rich, complex flavor that intensifies with age.",
        "servings_yield": "About 6 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "4-12 months aging",
        "total_time": "4-12 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "5", "unit": "gallons", "prep_note": "Aubrac or Simmental cattle"},
            {"item": "mesophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": "or whey starter"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds into small pieces."},
            {"step": 5, "text": "Stir while heating to 100°F over 30 minutes."},
            {"step": 6, "text": "Drain whey and let curds mat into tomme."},
            {"step": 7, "text": "Cut and stack tomme blocks (cheddaring) for 4-6 hours."},
            {"step": 8, "text": "Mill curds, add salt, let rest overnight."},
            {"step": 9, "text": "Pack into mold and press at 100 lbs for 48 hours."},
            {"step": 10, "text": "Age at 50°F, 95% humidity."},
            {"step": 11, "text": "Turn and brush regularly."},
            {"step": 12, "text": "Age minimum 4 months, up to 12 months for aged."}
        ],
        "temperature": "90-100°F make, 50°F aging",
        "notes": [
            "Named after the town of Laguiole (pronounced 'lay-ol')",
            "Related to Cantal and Salers but with distinct terroir",
            "Used to make aligot (cheesy mashed potatoes)",
            "AOC protected since 1961"
        ],
        "tags": ["cheese", "traditional", "french", "aubrac", "mountain", "12th-century", "aoc", "monastery"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-beaufort-alpine-gruyere",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Beaufort (French Alpine Gruyère)",
        "category": "mains",
        "attribution": "Savoie, France / Ancient",
        "source_note": "Called 'Prince of Gruyères'. Made in high alpine pastures during summer. Concave sides from traditional molds.",
        "description": "French alpine cheese with distinctive concave sides, smooth texture, and rich fruity flavor from high mountain pastures.",
        "servings_yield": "About 10 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "5-18 months aging",
        "total_time": "5-18 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "8", "unit": "gallons", "prep_note": "Tarine or Abondance cattle"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1.5", "unit": "tsp", "prep_note": "calf rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 91°F in copper cauldron."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30 minutes."},
            {"step": 4, "text": "Cut curds to rice grain size."},
            {"step": 5, "text": "Stir continuously while heating to 130°F over 40 minutes."},
            {"step": 6, "text": "Hold at 130°F, stirring, for 30 more minutes."},
            {"step": 7, "text": "Transfer curds to concave-sided mold (cercle) under whey."},
            {"step": 8, "text": "Press at 50 lbs for 1 hour, 100 lbs for 20 hours."},
            {"step": 9, "text": "Soak in brine for 2-3 days."},
            {"step": 10, "text": "Age at 50°F, 92% humidity."},
            {"step": 11, "text": "Rub with salt (morge) twice weekly during aging."},
            {"step": 12, "text": "Age minimum 5 months. Beaufort d'Été: summer. Beaufort Chalet d'Alpage: highest quality."}
        ],
        "temperature": "91-130°F make, 50°F aging",
        "notes": [
            "The concave sides come from the cercle mold and handling",
            "No eyes (holes) unlike other Gruyère-type cheeses",
            "Beaufort Chalet d'Alpage made above 5,000 ft from single herd",
            "AOC protected with three quality grades"
        ],
        "tags": ["cheese", "traditional", "french", "alpine", "savoie", "ancient", "aoc", "gruyere-style", "mountain"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-abondance-savoyard",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Abondance (Savoyard Mountain Cheese)",
        "category": "mains",
        "attribution": "Savoie, France / 14th Century",
        "source_note": "Named after the Abondance valley and cattle breed. Featured at papal coronation of Clement VI in 1342.",
        "description": "Savoyard pressed cheese with a washed amber rind and semi-firm paste with small eyes and nutty, fruity flavor.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "4", "unit": "gallons", "prep_note": "Abondance, Tarine, or Montbéliarde cattle"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 93°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 35 minutes."},
            {"step": 4, "text": "Cut curds to hazelnut size."},
            {"step": 5, "text": "Stir while heating to 113°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at temperature for 20 more minutes."},
            {"step": 7, "text": "Transfer curds to round mold with concave top."},
            {"step": 8, "text": "Press at 30 lbs for 30 minutes, 60 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 12-24 hours."},
            {"step": 10, "text": "Age at 50-55°F, 92% humidity."},
            {"step": 11, "text": "Wash rind with brine twice weekly."},
            {"step": 12, "text": "Age minimum 3 months."}
        ],
        "temperature": "93-113°F make, 50-55°F aging",
        "notes": [
            "Served at the coronation of Pope Clement VI in 1342",
            "The concave top surface is distinctive",
            "Abondance cattle are uniquely adapted to alpine conditions",
            "AOC protected since 1990"
        ],
        "tags": ["cheese", "traditional", "french", "savoyard", "alpine", "14th-century", "aoc", "washed-rind"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tomme-de-savoie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tomme de Savoie (Savoyard Mountain Cheese)",
        "category": "mains",
        "attribution": "Savoie, France / Ancient",
        "source_note": "The peasant cheese of Savoy - made from skim milk after cream was taken for butter.",
        "description": "Rustic Savoyard cheese with a distinctive grey mottled rind, semi-firm texture, and earthy, grassy flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-4 months aging",
        "total_time": "2-4 months",
        "ingredients": [
            {"item": "partially skimmed cow milk", "quantity": "2", "unit": "gallons", "prep_note": "skim some cream off"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Skim cream from milk (traditional used cream for butter)."},
            {"step": 2, "text": "Heat skimmed milk to 90°F."},
            {"step": 3, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Stir gently while heating to 100°F over 30 minutes."},
            {"step": 8, "text": "Drain curds and pack into round mold."},
            {"step": 9, "text": "Press at 20 lbs for 30 minutes, 40 lbs for 12 hours."},
            {"step": 10, "text": "Soak in brine for 12-24 hours."},
            {"step": 11, "text": "Age at 55°F, 90% humidity."},
            {"step": 12, "text": "Let natural grey mold develop. Age 2-4 months."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "Traditional peasant cheese made from milk after cream was skimmed",
            "The grey mottled rind is natural wild molds - this is characteristic",
            "Lower fat than other Savoyard cheeses due to skimming",
            "PGI protected"
        ],
        "tags": ["cheese", "traditional", "french", "savoyard", "alpine", "ancient", "peasant-cheese", "skim-milk", "pgi"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-bleu-dauvergne-volcanic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bleu d'Auvergne (Volcanic Blue Cheese)",
        "category": "mains",
        "attribution": "Auvergne, France / 1850s",
        "source_note": "Created by Antoine Roussel who inoculated cheese with rye bread mold. Made from volcanic pasture milk.",
        "description": "Creamy Auvergnat blue cheese with well-distributed blue veining and strong, spicy, assertive flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "from volcanic pasture ideal"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 3/4-inch cubes."},
            {"step": 6, "text": "Let curds rest 15 minutes, then stir gently."},
            {"step": 7, "text": "Drain and ladle curds into mold - do not press."},
            {"step": 8, "text": "Turn every 6 hours for 2-3 days."},
            {"step": 9, "text": "Salt surfaces."},
            {"step": 10, "text": "Age at 50°F, 95% humidity."},
            {"step": 11, "text": "Pierce with needles at 3-4 weeks."},
            {"step": 12, "text": "Age 4-8 weeks until well-veined."}
        ],
        "temperature": "86°F make, 50°F aging",
        "notes": [
            "Created in 1850s when Antoine Roussel observed mold on rye bread",
            "Volcanic soil of Auvergne creates distinctive pasture flavors",
            "More assertive than Fourme d'Ambert from same region",
            "AOC protected since 1975"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "blue", "19th-century", "aoc", "volcanic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fourme-dambert-ancient-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fourme d'Ambert (Ancient Auvergnat Blue)",
        "category": "mains",
        "attribution": "Auvergne, France / 8th Century",
        "source_note": "One of France's oldest cheeses. The distinctive tall cylindrical shape gives it the name 'fourme' (form).",
        "description": "Tall cylindrical blue cheese from Auvergne with a mild, creamy character and delicate blue flavor.",
        "servings_yield": "About 4 lbs cylinder",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "mountain pasture milk"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "mild strain"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and mild P. roqueforti. Ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Let curds rest, then gently ladle into tall cylindrical molds."},
            {"step": 7, "text": "Do not press - let drain naturally for 3-4 days, turning frequently."},
            {"step": 8, "text": "Salt surfaces."},
            {"step": 9, "text": "Age at 50°F, 95% humidity."},
            {"step": 10, "text": "Pierce with needles at 3 weeks."},
            {"step": 11, "text": "Age 4-8 weeks until delicate blue veins develop."}
        ],
        "temperature": "86°F make, 50°F aging",
        "notes": [
            "May be France's oldest blue cheese, dating to Druids or before",
            "Milder and creamier than other French blues",
            "The tall 'fourme' shape is unique to this cheese",
            "AOC protected jointly with Fourme de Montbrison"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "blue", "8th-century", "aoc", "ancient", "mild-blue"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-saint-nectaire-volcanic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Saint-Nectaire (Volcanic Mountain Cheese)",
        "category": "mains",
        "attribution": "Auvergne, France / 17th Century",
        "source_note": "Named after the town of Saint-Nectaire. Louis XIV's court favorite. Made on volcanic Auvergne pastures.",
        "description": "Washed-rind Auvergnat cheese with a grey-brown natural rind, supple texture, and earthy mushroom flavors.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2.5", "unit": "gallons", "prep_note": "Salers cattle traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently at 90°F for 15 minutes."},
            {"step": 7, "text": "Drain curds and pack into flat round molds."},
            {"step": 8, "text": "Press at 25 lbs for 12 hours."},
            {"step": 9, "text": "Salt surfaces."},
            {"step": 10, "text": "Age on rye straw at 50°F, 95% humidity."},
            {"step": 11, "text": "Turn every 2-3 days. Natural molds develop grey-brown rind."},
            {"step": 12, "text": "Age 4-8 weeks until interior is supple."}
        ],
        "temperature": "90°F make, 50°F aging",
        "notes": [
            "Became famous when served at court of Louis XIV",
            "Traditional aging on rye straw contributes to rind character",
            "Volcanic pastures of Mont Dore create distinctive terroir",
            "AOC distinguishes Fermier (farm) from Laitier (dairy)"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "washed-rind", "17th-century", "aoc", "volcanic", "mountain"],
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
