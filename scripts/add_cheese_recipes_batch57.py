#!/usr/bin/env python3
"""Add batch 57 - More traditional iconic cheeses and regional varieties."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-camembert-normandy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Camembert de Normandie (French Soft-Ripened)",
        "category": "mains",
        "attribution": "1791 Norman farmhouse tradition",
        "source_note": "Traditional French bloomy-rind cheesemaking",
        "description": "The quintessential French soft-ripened cheese, Camembert was perfected by Marie Harel in Normandy in 1791. Its white bloomy rind and creamy, flowing interior when perfectly ripe have made it an icon of French gastronomy.",
        "servings_yield": "8 oz wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-5 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "Norman cattle traditional"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "for white rind"},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp", "prep_note": "optional, for wrinkled rind"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture, P. candidum, and Geotrichum if using. Ripen 60-90 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 60-90 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes - very gentle handling."},
            {"step": 5, "text": "Let curds rest 10 minutes, then ladle gently into molds."},
            {"step": 6, "text": "Traditional: ladle in 5 layers over several hours for proper texture."},
            {"step": 7, "text": "Let drain overnight at room temperature, flipping 2-3 times."},
            {"step": 8, "text": "Salt all surfaces lightly."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "White mold appears after 5-7 days - turn daily."},
            {"step": 11, "text": "When fully covered in white mold (10-14 days), wrap loosely."},
            {"step": 12, "text": "Continue aging 3-5 weeks until interior is soft and flowing."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOP Camembert de Normandie must use raw milk and be ladled by hand",
            "The iconic wooden box was invented in 1890 for shipping",
            "Ripe Camembert should bulge slightly and feel soft throughout",
            "Never eat if ammonia smell is overpowering - it's overripe",
            "Marie Harel is the traditional credited inventor, though history is debated"
        ],
        "tags": ["cheese", "french", "normandy", "traditional", "soft-ripened", "bloomy-rind"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-brie-de-meaux-french-king",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brie de Meaux (French King of Cheeses)",
        "category": "mains",
        "attribution": "8th century Île-de-France tradition",
        "source_note": "Traditional French bloomy-rind cheesemaking",
        "description": "Called 'Le Roi des Fromages' (King of Cheeses) by Talleyrand at the Congress of Vienna, Brie de Meaux has been made east of Paris since the time of Charlemagne. Larger and milder than Camembert, it has graced royal tables for centuries.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and P. candidum. Ripen 60-90 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 90-120 minutes for very soft curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes using 'pelle à brie' (brie shovel)."},
            {"step": 5, "text": "Let curds rest 15 minutes."},
            {"step": 6, "text": "Ladle curds very gently into large flat molds - 14 inches diameter traditional."},
            {"step": 7, "text": "Ladle in thin layers over 6-8 hours for proper texture."},
            {"step": 8, "text": "Drain overnight, flipping once when firm enough."},
            {"step": 9, "text": "Salt surfaces after unmolding."},
            {"step": 10, "text": "Age at 52-55°F with 95% humidity."},
            {"step": 11, "text": "Turn daily until fully covered with white mold."},
            {"step": 12, "text": "Age 4-8 weeks until interior is uniformly soft."}
        ],
        "temperature": "90°F (32°C) for make; 52-55°F (11-13°C) for aging",
        "notes": [
            "AOP protected since 1980 - must be made in Seine-et-Marne",
            "Traditional wheel is 36-37 cm diameter, weighing about 2.8 kg",
            "Brie de Melun is a smaller, tangier cousin from the same region",
            "Charlemagne reportedly enjoyed Brie in the 8th century",
            "Ripe Brie should have no chalky center - uniformly soft"
        ],
        "tags": ["cheese", "french", "traditional", "soft-ripened", "bloomy-rind", "royal"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-epoisses-burgundy-washed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Époisses de Bourgogne (Burgundy Washed-Rind)",
        "category": "mains",
        "attribution": "16th century Cistercian monastery tradition",
        "source_note": "Traditional French washed-rind cheesemaking",
        "description": "Created by Cistercian monks at the Abbey of Époisses in the 16th century, this pungent washed-rind cheese is washed with Marc de Bourgogne (local brandy). Napoleon's favorite cheese, it's so aromatic it's banned on Paris public transport.",
        "servings_yield": "8-10 oz wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Burgundy cattle"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "Marc de Bourgogne", "quantity": "1/2", "unit": "cup", "prep_note": "or other grape brandy"},
            {"item": "brine solution", "quantity": "1", "unit": "cup", "prep_note": "for mixing with marc"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 60 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 60-90 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Let rest 10 minutes, then ladle into small molds."},
            {"step": 6, "text": "Drain 24-48 hours, flipping several times."},
            {"step": 7, "text": "Salt surfaces lightly."},
            {"step": 8, "text": "Prepare wash: mix brine with Marc de Bourgogne."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "Wash with marc-brine solution every 2-3 days."},
            {"step": 11, "text": "Rind develops from white to orange to red-brown over 6-8 weeks."},
            {"step": 12, "text": "When rind is sticky and interior is liquid under the rind, it's ready."}
        ],
        "temperature": "86°F (30°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOP protected - must be washed with Marc de Bourgogne",
            "Brillat-Savarin called it 'the king of cheeses'",
            "Napoleon allegedly loved Époisses above all other cheeses",
            "Banned on Paris Metro due to powerful aroma",
            "Served in its traditional wooden box, eaten with a spoon"
        ],
        "tags": ["cheese", "french", "burgundy", "traditional", "washed-rind", "stinky", "monastery"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-taleggio-italian-washed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Taleggio (Italian Washed-Rind Square)",
        "category": "mains",
        "attribution": "10th century Lombard valley tradition",
        "source_note": "Traditional Italian washed-rind cheesemaking",
        "description": "Named for the Val Taleggio in Lombardy, this square washed-rind cheese has been made since at least the 10th century. Milder than French washed-rinds, it has a meaty, fruity flavor and soft, creamy interior.",
        "servings_yield": "2 lb square",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "5-7 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Stir gently for 10 minutes without raising temperature."},
            {"step": 6, "text": "Drain whey and pack curds into square molds."},
            {"step": 7, "text": "Let drain 8-12 hours, flipping several times."},
            {"step": 8, "text": "Salt surfaces or brief brine."},
            {"step": 9, "text": "Age at 55°F with 90-95% humidity."},
            {"step": 10, "text": "Wash with brine twice weekly for first 2-3 weeks."},
            {"step": 11, "text": "Reduce washing to weekly as rind develops."},
            {"step": 12, "text": "Ready at 5-7 weeks when rind is pinkish-orange and interior soft."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "DOP protected since 1996",
            "Traditional square shape distinguishes it from round washed-rinds",
            "Milder and more approachable than French washed-rinds",
            "Excellent melting cheese - traditional in risotto",
            "The rind is edible but some prefer to remove it"
        ],
        "tags": ["cheese", "italian", "lombardy", "traditional", "washed-rind", "square"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-fontina-val-daosta",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fontina Val d'Aosta (Italian Alpine Classic)",
        "category": "mains",
        "attribution": "12th century Val d'Aosta tradition",
        "source_note": "Traditional Italian alpine cheesemaking",
        "description": "Made in the Italian Alps since at least the 12th century, Fontina Val d'Aosta is one of Italy's great mountain cheeses. Semi-soft with a washed rind, it has a rich, buttery, slightly nutty flavor and melts beautifully.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from Valdostana cattle"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F (36°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 5, "text": "Stir and raise temperature to 118°F (48°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are firm and release whey easily."},
            {"step": 7, "text": "Drain and pack curds into molds."},
            {"step": 8, "text": "Press at moderate weight for 12-24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 50°F with 90% humidity."},
            {"step": 11, "text": "Wash with brine weekly - rind develops brownish-orange color."},
            {"step": 12, "text": "Age minimum 3 months, traditionally in natural caves."}
        ],
        "temperature": "97-118°F (36-48°C) for make; 50°F (10°C) for aging",
        "notes": [
            "DOP protected - authentic Fontina only from Val d'Aosta",
            "Valdostana is an ancient alpine breed essential for authentic Fontina",
            "Essential for fonduta - Italian fondue",
            "Swedish/Danish 'Fontina' is a different, milder cheese",
            "The pressed Matterhorn symbol identifies authentic DOP wheels"
        ],
        "tags": ["cheese", "italian", "alpine", "traditional", "washed-rind", "semi-soft"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-asiago-veneto-dual",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Asiago (Veneto Dual-Style Cheese)",
        "category": "mains",
        "attribution": "10th century Veneto highland tradition",
        "source_note": "Traditional Italian highland cheesemaking",
        "description": "From the Asiago Plateau in Veneto, this cheese comes in two distinct styles: Asiago Pressato (fresh, mild, pressed) and Asiago d'Allevo (aged, sharp, traditional). Both have been made here since at least the year 1000.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1 month (Pressato) to 24 months (d'Allevo)",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from highland pastures"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 25-35 minutes."},
            {"step": 4, "text": "For PRESSATO: cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "For D'ALLEVO: cut curds to rice grain size."},
            {"step": 6, "text": "For PRESSATO: stir gently, raise to 104°F (40°C)."},
            {"step": 7, "text": "For D'ALLEVO: stir and raise to 115°F (46°C)."},
            {"step": 8, "text": "When curds are appropriately firm, drain and mold."},
            {"step": 9, "text": "Press at moderate weight for PRESSATO; heavy weight for D'ALLEVO."},
            {"step": 10, "text": "Brine for 24-48 hours."},
            {"step": 11, "text": "PRESSATO: age 20-40 days. D'ALLEVO: age 4-24 months."},
            {"step": 12, "text": "D'Allevo classifications: Mezzano (4-6 mo), Vecchio (10+ mo), Stravecchio (15+ mo)."}
        ],
        "temperature": "95-115°F (35-46°C) for make; 50-55°F for aging",
        "notes": [
            "DOP protected since 1978",
            "Pressato is mild, sweet, soft - perfect melting cheese",
            "D'Allevo is sharp, granular, excellent for grating",
            "Originally made from sheep's milk before cattle arrived",
            "The Asiago Plateau is 1000+ meters elevation"
        ],
        "tags": ["cheese", "italian", "veneto", "traditional", "highland", "dual-style"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-pecorino-toscano-tuscan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Toscano (Tuscan Sheep Cheese)",
        "category": "mains",
        "attribution": "Etruscan-era Tuscan tradition",
        "source_note": "Traditional Tuscan sheep cheesemaking",
        "description": "The Etruscans were making sheep cheese in Tuscany 3,000 years ago. Pecorino Toscano continues this tradition - milder than Romano, it comes fresh (fresco) or aged (stagionato), essential to Tuscan cuisine.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "20 days (fresco) to 6+ months (stagionato)",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Tuscan breeds"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for rind (stagionato)"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 20-30 minutes."},
            {"step": 4, "text": "Cut curds to hazelnut size."},
            {"step": 5, "text": "For FRESCO: minimal stirring, temperature stays low."},
            {"step": 6, "text": "For STAGIONATO: stir more, raise to 113°F (45°C)."},
            {"step": 7, "text": "Drain and pack curds into molds."},
            {"step": 8, "text": "Press lightly for fresco; moderately for stagionato."},
            {"step": 9, "text": "Brine for 8-24 hours depending on size and style."},
            {"step": 10, "text": "FRESCO: age minimum 20 days, eat young."},
            {"step": 11, "text": "STAGIONATO: age 4-6+ months, rub rind with olive oil."},
            {"step": 12, "text": "Turn regularly throughout aging."}
        ],
        "temperature": "95-113°F (35-45°C) for make; 50-55°F for aging",
        "notes": [
            "DOP protected since 1996",
            "Milder than Pecorino Romano - more approachable",
            "Fresco is soft, mild, creamy - eaten as table cheese",
            "Stagionato is firmer, tangier - can be grated",
            "Traditional with Tuscan fava beans and bread"
        ],
        "tags": ["cheese", "italian", "tuscan", "sheep", "traditional", "ancient", "pecorino"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gouda-dutch-icon",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gouda (Dutch Waxed Wheel)",
        "category": "mains",
        "attribution": "12th century Dutch tradition",
        "source_note": "Traditional Dutch cheesemaking",
        "description": "Named for the city where it was traded (not made), Gouda has been produced in the Netherlands since at least the 12th century. The washed-curd technique creates its characteristic sweetness, and it ages beautifully.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1-36 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cheese wax", "quantity": "", "unit": "", "prep_note": "for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest 5 minutes."},
            {"step": 6, "text": "Drain 1/3 of whey, replace with hot water (140°F) - the washing step."},
            {"step": 7, "text": "Stir and raise temperature to 102°F (39°C) over 30 minutes."},
            {"step": 8, "text": "Continue stirring until curds are firm."},
            {"step": 9, "text": "Drain whey, pack curds firmly into round molds."},
            {"step": 10, "text": "Press heavily for 6-12 hours."},
            {"step": 11, "text": "Brine for 12-24 hours."},
            {"step": 12, "text": "Air dry, then wax. Age at 55°F: Jong (4 weeks), Belegen (4 mo), Oud (12+ mo)."}
        ],
        "temperature": "86-102°F (30-39°C) for make; 55°F (13°C) for aging",
        "notes": [
            "The washing step removes lactose, preventing excessive acid and creating sweet flavor",
            "Young Gouda is mild and creamy; aged Gouda is hard with crystals",
            "Boerenkaas (farmhouse Gouda) is made from raw milk",
            "Traditional colors: red wax for young, yellow for aged, black for extra-aged",
            "Aged Gouda develops caramel, butterscotch flavors and tyrosine crystals"
        ],
        "tags": ["cheese", "dutch", "traditional", "washed-curd", "waxed", "aged"],
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
