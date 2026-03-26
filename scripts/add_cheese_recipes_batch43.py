#!/usr/bin/env python3
"""Add batch 43 - More ancient European cheeses and preservation tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Ancient European Cheeses
    {
        "id": "traditional-reblochon-savoyard",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Reblochon (Savoyard Washed-Rind)",
        "category": "mains",
        "attribution": "Savoie, France / 13th Century",
        "source_note": "Name comes from 'reblocher' (to milk again). Farmers hid the richest milk from tax collectors, then made cheese.",
        "description": "French washed-rind cheese from the Alps with a creamy interior and earthy, nutty flavor. Essential for tartiflette.",
        "servings_yield": "About 1 lb round",
        "prep_time": "3 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "high-fat, from second milking"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently for 15 minutes at 90°F - do not heat further."},
            {"step": 7, "text": "Ladle curds into flat round molds (5-inch diameter)."},
            {"step": 8, "text": "Turn frequently for 6-8 hours as cheese drains."},
            {"step": 9, "text": "Salt all surfaces."},
            {"step": 10, "text": "Age at 55°F, 95% humidity."},
            {"step": 11, "text": "Wash with light brine every 2-3 days."},
            {"step": 12, "text": "Age 4-6 weeks until rind is orange-pink and paste is creamy."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "The 'rebloche' or second milking is richer in fat",
            "Farmers would under-report milk to avoid taxes, then make cheese with the hidden portion",
            "Essential ingredient for tartiflette (Savoyard potato dish)",
            "AOC protected since 1958"
        ],
        "tags": ["cheese", "traditional", "french", "savoyard", "washed-rind", "13th-century", "aoc", "alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-epoisses-burgundy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Époisses (Burgundy Washed-Rind)",
        "category": "mains",
        "attribution": "Burgundy, France / 16th Century",
        "source_note": "Created by Cistercian monks, perfected by local farmers. Napoleon's favorite cheese. Washed with marc de Bourgogne.",
        "description": "Intensely pungent Burgundian washed-rind cheese with a sticky orange rind and unctuous, spoonable interior.",
        "servings_yield": "About 8 oz round",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1", "unit": "gallon", "prep_note": "full fat"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "marc de Bourgogne", "quantity": "1/2", "unit": "cup", "prep_note": "or brandy mixed with brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add all cultures. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed, then small amount of diluted rennet."},
            {"step": 4, "text": "Let set for 1.5-2 hours until soft curd forms."},
            {"step": 5, "text": "Ladle curds very gently into small round molds."},
            {"step": 6, "text": "Let drain naturally for 48 hours, turning several times."},
            {"step": 7, "text": "Salt lightly."},
            {"step": 8, "text": "Age at 55°F, 95% humidity."},
            {"step": 9, "text": "After 1 week, begin washing with marc de Bourgogne mixed with brine."},
            {"step": 10, "text": "Wash every 2-3 days for 6-8 weeks."},
            {"step": 11, "text": "Rind becomes sticky, orange, and very aromatic."},
            {"step": 12, "text": "Interior should be spoonable when ripe."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "Reportedly Napoleon's favorite cheese",
            "So pungent it's banned on Paris public transport",
            "Marc de Bourgogne is pomace brandy from Burgundy winemaking",
            "AOC protected - must be made in specific Burgundy communes"
        ],
        "tags": ["cheese", "traditional", "french", "burgundy", "washed-rind", "16th-century", "aoc", "pungent", "cistercian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-munster-alsatian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Munster (Alsatian Monastery Cheese)",
        "category": "mains",
        "attribution": "Alsace/Vosges, France / 7th Century",
        "source_note": "Created by Benedictine monks in the Vosges mountains. Name comes from 'monasterium' (monastery).",
        "description": "Alsatian washed-rind cheese with a pungent aroma, soft paste, and complex savory flavor. Traditionally served with caraway.",
        "servings_yield": "About 1 lb round",
        "prep_time": "3 hours",
        "cook_time": "5-8 weeks aging",
        "total_time": "5-8 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "Vosgienne cattle traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tbsp", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 3/4-inch cubes."},
            {"step": 6, "text": "Stir gently for 20 minutes at 90°F."},
            {"step": 7, "text": "Ladle curds into round molds."},
            {"step": 8, "text": "Turn frequently for 24 hours."},
            {"step": 9, "text": "Salt surfaces."},
            {"step": 10, "text": "Age at 55-60°F, 95% humidity."},
            {"step": 11, "text": "Wash with brine every 2-3 days."},
            {"step": 12, "text": "Age 5-8 weeks until rind is orange-red and paste is soft."}
        ],
        "temperature": "90°F make, 55-60°F aging",
        "notes": [
            "One of the oldest French cheeses, from 7th century monasteries",
            "Traditionally served with cumin or caraway seeds",
            "German version is called Münster (slightly different)",
            "AOC protected as Munster or Munster-Géromé"
        ],
        "tags": ["cheese", "traditional", "french", "alsatian", "washed-rind", "7th-century", "monastery", "aoc", "benedictine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-livarot-norman",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Livarot (Norman 'Colonel' Cheese)",
        "category": "mains",
        "attribution": "Normandy, France / 13th Century",
        "source_note": "Called 'The Colonel' for the five stripes around it resembling military rank insignia. One of Normandy's oldest cheeses.",
        "description": "Norman washed-rind cheese bound with sedge grass stripes, with a pungent rind and creamy, spicy interior.",
        "servings_yield": "About 1 lb round",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "partially skimmed cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "traditionally from evening milk"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "sedge grass or raffia", "quantity": "5", "unit": "strips", "prep_note": "for binding"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat partially skimmed milk to 90°F."},
            {"step": 2, "text": "Add cultures and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently for 20 minutes."},
            {"step": 7, "text": "Ladle curds into round molds."},
            {"step": 8, "text": "Turn frequently for 24-48 hours."},
            {"step": 9, "text": "Salt all surfaces."},
            {"step": 10, "text": "Wrap 5 strips of sedge grass around the circumference at equal intervals."},
            {"step": 11, "text": "Age at 55°F, 95% humidity, washing with brine every 2-3 days."},
            {"step": 12, "text": "Age 6-8 weeks until rind is reddish-orange and pungent."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "Called 'The Colonel' - the 5 stripes represent colonel's rank insignia",
            "Sedge grass (laîche) stripes prevent cheese from collapsing as it softens",
            "One of Normandy's strongest-smelling cheeses",
            "AOC protected since 1975"
        ],
        "tags": ["cheese", "traditional", "french", "norman", "washed-rind", "13th-century", "aoc", "banded"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-langres-champagne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Langres (Champagne Washed-Rind)",
        "category": "mains",
        "attribution": "Champagne, France / 18th Century",
        "source_note": "Distinctive for its concave top (fontaine) which traditionally holds Champagne or marc. Never turned during aging.",
        "description": "Champagne washed-rind cheese with a distinctive hollow top, pungent orange rind, and creamy interior.",
        "servings_yield": "About 8 oz",
        "prep_time": "3 hours",
        "cook_time": "5-6 weeks aging",
        "total_time": "5-6 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1", "unit": "gallon", "prep_note": "full fat"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "marc de Champagne", "quantity": "1/4", "unit": "cup", "prep_note": "or Champagne, for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add cultures and ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed, then small amount of diluted rennet."},
            {"step": 4, "text": "Let set for 1.5-2 hours until soft curd."},
            {"step": 5, "text": "Ladle curds gently into molds."},
            {"step": 6, "text": "Let drain for 48 hours but DO NOT TURN. This creates the concave top."},
            {"step": 7, "text": "Salt all surfaces including the hollow."},
            {"step": 8, "text": "Age at 55°F, 95% humidity."},
            {"step": 9, "text": "Wash with marc de Champagne mixed with brine every 2-3 days."},
            {"step": 10, "text": "Age 5-6 weeks. The hollow deepens as cheese ripens."},
            {"step": 11, "text": "Serve with Champagne pooled in the fontaine."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "The fontaine (hollow) is created by NOT turning during draining",
            "Traditionally Champagne or marc is poured into the hollow before serving",
            "Smaller and more delicate than many washed rinds",
            "AOC protected since 1991"
        ],
        "tags": ["cheese", "traditional", "french", "champagne", "washed-rind", "18th-century", "aoc", "fontaine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mont-d-or-seasonal",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mont d'Or / Vacherin du Haut-Doubs (Seasonal Spruce Box Cheese)",
        "category": "mains",
        "attribution": "Jura Mountains, France/Switzerland / 18th Century",
        "source_note": "Made only from August 15 to March 15 when cows return from alpine pastures. Bound with spruce bark and aged in spruce boxes.",
        "description": "Seasonal washed-rind cheese wrapped in spruce bark, with an incredibly creamy, spoonable texture and woodsy, earthy flavor.",
        "servings_yield": "About 1 lb",
        "prep_time": "3 hours",
        "cook_time": "3-4 weeks aging",
        "total_time": "3-4 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "Montbéliarde cattle"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "spruce bark strip", "quantity": "1", "unit": "strip", "prep_note": "food-safe, soaked"},
            {"item": "spruce wood box", "quantity": "1", "unit": "", "prep_note": "for aging"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add cultures and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently at 90°F for 20 minutes."},
            {"step": 7, "text": "Ladle curds into flat round molds."},
            {"step": 8, "text": "Turn frequently for 24 hours."},
            {"step": 9, "text": "Salt surfaces, then wrap circumference with soaked spruce bark."},
            {"step": 10, "text": "Place in spruce wood box."},
            {"step": 11, "text": "Age at 55°F, 95% humidity, washing every 2-3 days."},
            {"step": 12, "text": "Age 3-4 weeks until surface is wrinkled and interior is liquid."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "Only made from mid-August to mid-March by AOC regulation",
            "The spruce bark and box impart distinctive resinous flavor",
            "Traditionally eaten by cutting off top and scooping with bread",
            "Can be warmed in oven in its box for fondue-like experience"
        ],
        "tags": ["cheese", "traditional", "french", "jura", "washed-rind", "seasonal", "spruce", "aoc", "18th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-ossau-iraty-basque-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ossau-Iraty (Basque Sheep Cheese)",
        "category": "mains",
        "attribution": "Basque Country / Ancient",
        "source_note": "Made in the Pyrenees since prehistoric times. Named after the Ossau valley and Iraty forest.",
        "description": "Basque sheep cheese with a natural brushed rind, firm texture, and rich nutty flavor with hints of herbs and flowers.",
        "servings_yield": "About 4 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "3", "unit": "gallons", "prep_note": "Manech or Basco-Béarnaise breed"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30-40 minutes."},
            {"step": 4, "text": "Cut curds to corn kernel size."},
            {"step": 5, "text": "Stir gently while heating to 100-104°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at temperature for 30 more minutes."},
            {"step": 7, "text": "Drain curds and pack into round mold."},
            {"step": 8, "text": "Press at 30 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 2-3 days."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "Brush rind weekly to develop natural coat."},
            {"step": 12, "text": "Age 3 months minimum, up to 12 months for stronger flavor."}
        ],
        "temperature": "90-104°F make, 55°F aging",
        "notes": [
            "Ancient cheese from Basque shepherds in the Pyrenees",
            "Named for Ossau valley (Béarn) and Iraty forest (Basque Country)",
            "Sheep milk gives rich, lanolin-tinged flavor",
            "AOC protected - must use specific sheep breeds"
        ],
        "tags": ["cheese", "traditional", "french", "basque", "sheep", "ancient", "pyrenees", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cantal-auvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cantal (France's Oldest Cheese)",
        "category": "mains",
        "attribution": "Auvergne, France / 2000+ Years",
        "source_note": "Possibly France's oldest cheese, mentioned by Pliny the Elder. Made in the volcanic Cantal mountains.",
        "description": "Ancient Auvergnat cheese with a natural grey rind, firm crumbly texture, and tangy, buttery flavor.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "1-6 months aging",
        "total_time": "1-6 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "4", "unit": "gallons", "prep_note": "Salers cattle traditional"},
            {"item": "mesophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "3/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently while heating to 100°F over 30 minutes."},
            {"step": 7, "text": "Drain whey and let curds mat."},
            {"step": 8, "text": "Cut matted curds into blocks. Stack and turn (cheddaring) for 2 hours."},
            {"step": 9, "text": "Mill curds, add salt, rest 12-24 hours (tomme fraîche stage)."},
            {"step": 10, "text": "Mill again, pack into mold, press at 100 lbs for 48 hours."},
            {"step": 11, "text": "Age at 50°F, 95% humidity."},
            {"step": 12, "text": "Age 1 month (Cantal Jeune), 2-6 months (Entre-Deux), 6+ months (Vieux)."}
        ],
        "temperature": "90-100°F make, 50°F aging",
        "notes": [
            "Pliny the Elder mentioned cheese from Cantal region in 1st century AD",
            "Unique two-day pressing process with intermediate milling",
            "The 'tomme fraîche' (fresh curd stage) is eaten locally on aligot",
            "AOC protected since 1956"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "ancient", "2000-years", "aoc", "cheddar-style"],
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
