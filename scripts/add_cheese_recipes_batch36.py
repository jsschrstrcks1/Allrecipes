#!/usr/bin/env python3
"""Add batch 36 of traditional cheese recipes - More ancient and prehistoric cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-tête-de-moine-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tête de Moine (Swiss Monk's Head Cheese)",
        "category": "mains",
        "attribution": "Bellelay Abbey, Switzerland / 12th Century",
        "source_note": "Created by monks at Bellelay Abbey in the Jura mountains. Named 'monk's head' after the shaved pate of monks.",
        "description": "Swiss monastery cheese traditionally shaved into rosettes with a girolle, with intense aromatic flavor and smooth texture.",
        "servings_yield": "About 2 lbs cylindrical wheel",
        "prep_time": "4 hours",
        "cook_time": "3-4 months aging",
        "total_time": "3-4 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "from Jura mountain pastures ideal"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium", "quantity": "1/32", "unit": "tsp", "prep_note": "small amount"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacterium. Ripen 20 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 35 minutes until firm."},
            {"step": 5, "text": "Cut curds to small rice-sized pieces."},
            {"step": 6, "text": "Stir gently while heating to 120°F over 45 minutes."},
            {"step": 7, "text": "Continue stirring at 120°F for 30 more minutes."},
            {"step": 8, "text": "Transfer curds to tall cylindrical mold (taller than wide)."},
            {"step": 9, "text": "Press at 20 lbs for 30 minutes, 40 lbs for 12 hours."},
            {"step": 10, "text": "Soak in saturated brine for 24 hours."},
            {"step": 11, "text": "Age at 55°F, 90% humidity."},
            {"step": 12, "text": "Wash with brine weekly for first month."},
            {"step": 13, "text": "Age 3-4 months. Rind becomes sticky and aromatic."}
        ],
        "temperature": "90-120°F make, 55°F aging",
        "notes": [
            "First mentioned in documents from 1192 at Bellelay Abbey",
            "Traditionally shaved with a girolle device into thin rosettes",
            "The cylindrical shape is essential for the girolle to work",
            "AOP protected - must be made in the Jura region"
        ],
        "tags": ["cheese", "traditional", "swiss", "monastery", "12th-century", "jura", "aop", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-vacherin-fribourgeois-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vacherin Fribourgeois (Swiss Fondue Cheese)",
        "category": "mains",
        "attribution": "Fribourg, Switzerland / 15th Century",
        "source_note": "Essential for traditional moitié-moitié fondue. Made in Fribourg canton since the 1400s.",
        "description": "Swiss semi-hard cheese with a sticky washed rind, creamy texture, and nutty flavor, essential for authentic fondue.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-4 months aging",
        "total_time": "3-4 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "4", "unit": "gallons", "prep_note": "alpine pasture milk"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "3/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 40 minutes."},
            {"step": 5, "text": "Cut curds to hazelnut size."},
            {"step": 6, "text": "Stir gently while heating to 104°F over 30 minutes."},
            {"step": 7, "text": "Hold at 104°F, stirring, for 30 more minutes."},
            {"step": 8, "text": "Transfer curds to round mold."},
            {"step": 9, "text": "Press at 20 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 10, "text": "Soak in brine for 2 days."},
            {"step": 11, "text": "Age at 55°F, 95% humidity."},
            {"step": 12, "text": "Wash rind with brine every 2-3 days."},
            {"step": 13, "text": "Age 3-4 months until rind is sticky and brown."}
        ],
        "temperature": "90-104°F make, 55°F aging",
        "notes": [
            "Essential for moitié-moitié fondue (half Vacherin, half Gruyère)",
            "The washed rind contributes earthy, complex flavors",
            "Melts beautifully due to moderate aging",
            "AOP protected - must be from Fribourg canton"
        ],
        "tags": ["cheese", "traditional", "swiss", "fondue", "15th-century", "washed-rind", "fribourg", "aop"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-stilton-english-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Stilton (English King of Blues)",
        "category": "mains",
        "attribution": "Leicestershire, England / 18th Century",
        "source_note": "Named after the town of Stilton where it was sold, though never made there. PDO requires production in three specific counties.",
        "description": "English blue cheese with a crusty natural rind, creamy texture, and complex blue veining, considered England's finest blue.",
        "servings_yield": "About 4 lbs cylindrical wheel",
        "prep_time": "4 hours",
        "cook_time": "9-12 weeks aging",
        "total_time": "9-12 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "local dairy"},
            {"item": "cream", "quantity": "1", "unit": "cup", "prep_note": "for extra richness"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Add cream to milk and heat to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 90 minutes until firm."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Let curds settle, then ladle into cloth-lined mold without pressing."},
            {"step": 7, "text": "Turn mold every 15 minutes for first 2 hours, then every hour for 24 hours."},
            {"step": 8, "text": "Unmold and salt all surfaces daily for 5 days."},
            {"step": 9, "text": "Smooth surface by hand-rubbing (or the sides with a knife)."},
            {"step": 10, "text": "Age at 55°F, 90% humidity."},
            {"step": 11, "text": "Pierce with needles after 5-6 weeks to allow air for bluing."},
            {"step": 12, "text": "Age 9-12 weeks total until blue veins develop throughout."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "Stilton is never pressed - the open texture is essential for bluing",
            "PDO requires production only in Derbyshire, Leicestershire, or Nottinghamshire",
            "The crusty brown rind develops naturally and is not washed",
            "Traditionally served with port at Christmas"
        ],
        "tags": ["cheese", "traditional", "english", "blue", "pdo", "18th-century", "leicestershire", "king-of-blues"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-wensleydale-english-crumbly",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Wensleydale (English Crumbly Cheese)",
        "category": "mains",
        "attribution": "Wensleydale, Yorkshire / 12th Century",
        "source_note": "Brought to Yorkshire by Cistercian monks from France. Originally a blue cheese, now primarily made white.",
        "description": "English crumbly white cheese from Yorkshire with a mild, slightly sweet flavor and moist, crumbly texture.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 weeks aging",
        "total_time": "3-6 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep milk for traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Let curds rest 5 minutes."},
            {"step": 7, "text": "Stir gently while raising temperature to 95°F over 30 minutes."},
            {"step": 8, "text": "Drain whey, leaving curds to mat for 15 minutes."},
            {"step": 9, "text": "Cut matted curds into blocks and stack (basic cheddaring)."},
            {"step": 10, "text": "Mill curds and add salt."},
            {"step": 11, "text": "Pack loosely into mold - do not press hard."},
            {"step": 12, "text": "Press at 20 lbs for 12 hours only."},
            {"step": 13, "text": "Age at 55°F, 80% humidity for 3-6 weeks."}
        ],
        "temperature": "86-95°F make, 55°F aging",
        "notes": [
            "Cistercian monks brought the recipe from Roquefort region",
            "Originally made from sheep milk and often blued",
            "Light pressing creates the characteristic crumbly texture",
            "Often paired with fruit, especially apple pie ('an apple pie without cheese is like a kiss without a squeeze')"
        ],
        "tags": ["cheese", "traditional", "english", "yorkshire", "crumbly", "12th-century", "cistercian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-lancashire-english-crumbly",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Lancashire (English Multi-Day Curd Cheese)",
        "category": "mains",
        "attribution": "Lancashire, England / Medieval",
        "source_note": "Unique process combines curds from multiple days, creating complex flavor. Nearly extinct until farmhouse revival.",
        "description": "English cheese made from curds of two or three days, with a rich buttery texture and complex tangy flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours x 3 days",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "per day, for 2-3 days"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "per day"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "per day"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Make curds as for cheddar - culture, rennet, cut, stir, drain, salt."},
            {"step": 2, "text": "Do NOT press. Cover and store curds at cool room temp overnight."},
            {"step": 3, "text": "DAY 2: Make fresh curds with new milk using same process."},
            {"step": 4, "text": "Combine Day 1 and Day 2 curds. Mix gently."},
            {"step": 5, "text": "Store combined curds overnight."},
            {"step": 6, "text": "DAY 3 (optional): Make more curds and combine with Days 1-2."},
            {"step": 7, "text": "Mill combined curds and add any remaining salt."},
            {"step": 8, "text": "Pack firmly into mold."},
            {"step": 9, "text": "Press at 50 lbs for 24 hours."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "Creamy Lancashire: age 2-3 months. Tasty Lancashire: age 4-6 months."}
        ],
        "temperature": "86-95°F make, 55°F aging",
        "notes": [
            "The multi-day curd process is unique to Lancashire",
            "Combining curds of different ages creates layered, complex flavor",
            "Nearly died out in 20th century - revived by farmhouse producers",
            "Three traditional styles: Creamy (young), Tasty (medium), Crumbly (aged)"
        ],
        "tags": ["cheese", "traditional", "english", "lancashire", "multi-day", "medieval", "farmhouse"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gloucester-english-double",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Double Gloucester (English Full-Fat)",
        "category": "mains",
        "attribution": "Gloucestershire, England / 16th Century",
        "source_note": "Made from the full-fat milk of Gloucester cattle. 'Double' refers to full-cream milk, not double the size.",
        "description": "English hard cheese with a rich orange color, firm texture, and mellow buttery flavor, made from whole Gloucester cattle milk.",
        "servings_yield": "About 3 lbs",
        "prep_time": "4 hours",
        "cook_time": "4-8 months aging",
        "total_time": "4-8 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "Gloucester cattle ideal"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto", "quantity": "1/4", "unit": "tsp", "prep_note": "for traditional orange color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add annatto for orange color, stir well."},
            {"step": 3, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Stir and heat slowly to 100°F over 40 minutes."},
            {"step": 8, "text": "Hold at 100°F, stirring, for 30 more minutes."},
            {"step": 9, "text": "Drain whey, cut curd into blocks, stack to cheddar."},
            {"step": 10, "text": "Mill curds and add salt."},
            {"step": 11, "text": "Press at 50 lbs for 24 hours."},
            {"step": 12, "text": "Age at 55°F, 85% humidity for 4-8 months."}
        ],
        "temperature": "86-100°F make, 55°F aging",
        "notes": [
            "'Double' means full-cream milk; 'Single Gloucester' uses partially skimmed",
            "Traditional Gloucester cattle produce naturally golden milk",
            "Used in the famous Cooper's Hill Cheese Rolling race",
            "PDO protected - must be made in specific counties"
        ],
        "tags": ["cheese", "traditional", "english", "gloucestershire", "hard", "16th-century", "pdo"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-maroilles-french-washed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Maroilles (French Strong Washed-Rind)",
        "category": "mains",
        "attribution": "Thiérache, Northern France / 10th Century",
        "source_note": "Created by monks at Maroilles Abbey around 960 AD. One of France's oldest and most pungent cheeses.",
        "description": "French washed-rind cheese with a powerful aroma, orange rind, and creamy interior with surprisingly subtle flavor.",
        "servings_yield": "About 1.5 lbs square",
        "prep_time": "3 hours",
        "cook_time": "5-8 weeks aging",
        "total_time": "5-8 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for orange rind"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir very gently for 20 minutes at 86°F - do not heat further."},
            {"step": 7, "text": "Ladle curds into square molds."},
            {"step": 8, "text": "Turn frequently for 24 hours, letting whey drain naturally."},
            {"step": 9, "text": "Salt all surfaces."},
            {"step": 10, "text": "Age at 55°F, 95% humidity."},
            {"step": 11, "text": "Wash with brine every 2-3 days."},
            {"step": 12, "text": "Age 5-8 weeks until rind is sticky orange and very aromatic."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "Created by monks of Maroilles Abbey around 960 AD",
            "The traditional square shape is characteristic",
            "Despite powerful aroma, the taste is surprisingly mild",
            "AOC protected since 1955"
        ],
        "tags": ["cheese", "traditional", "french", "washed-rind", "10th-century", "monastery", "aoc", "pungent"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pont-l-eveque-norman",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pont-l'Évêque (Norman Washed-Rind)",
        "category": "mains",
        "attribution": "Normandy, France / 12th Century",
        "source_note": "One of Normandy's oldest cheeses, made since the 12th century. Originally called 'Angelot' after the golden angel coins it resembled.",
        "description": "Norman washed-rind cheese with a golden-orange rind, creamy interior, and complex earthy, barnyardy flavors.",
        "servings_yield": "About 1 lb square",
        "prep_time": "3 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1.5", "unit": "gallons", "prep_note": "Norman breed ideal"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 3/4-inch cubes."},
            {"step": 6, "text": "Stir very gently for 15 minutes."},
            {"step": 7, "text": "Ladle curds into small square molds."},
            {"step": 8, "text": "Let drain naturally for 24 hours, turning frequently."},
            {"step": 9, "text": "Salt and dry for 2 days."},
            {"step": 10, "text": "Age at 55°F, 95% humidity."},
            {"step": 11, "text": "Wash with light brine or Calvados every 2-3 days."},
            {"step": 12, "text": "Age 4-6 weeks until rind is golden and interior is creamy."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "One of the oldest Norman cheeses, dating to 12th century",
            "Originally called 'Angelot' - now the name of the younger version",
            "Some producers wash with Calvados for extra Norman character",
            "AOC protected - must be made in Normandy"
        ],
        "tags": ["cheese", "traditional", "french", "norman", "washed-rind", "12th-century", "aoc"],
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
