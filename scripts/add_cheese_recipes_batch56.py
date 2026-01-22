#!/usr/bin/env python3
"""Add batch 56 - More ancient and traditional cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-ossau-iraty-basque-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ossau-Iraty (Basque Pyrenean Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Basque shepherds' tradition",
        "source_note": "Traditional French Basque cheesemaking",
        "description": "Made by Basque shepherds in the French Pyrenees for over 3,000 years, Ossau-Iraty is one of Europe's oldest cheeses. Named for the Ossau Valley and Iraty Forest, this sheep's milk cheese has sustained mountain communities for millennia.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Manech or Basco-Béarnaise sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add lamb rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds to corn-kernel size."},
            {"step": 5, "text": "Stir and raise temperature to 104-109°F (40-43°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are firm and release whey easily."},
            {"step": 7, "text": "Drain whey and pack curds into traditional round molds."},
            {"step": 8, "text": "Press at moderate weight for 24 hours, flipping several times."},
            {"step": 9, "text": "Brine for 24-48 hours depending on size."},
            {"step": 10, "text": "Age at 50-55°F with 85-90% humidity."},
            {"step": 11, "text": "Turn and brush regularly. Minimum 3 months, up to 12 months."}
        ],
        "temperature": "86-109°F (30-43°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "AOC protected since 1980 - France's first sheep cheese AOC",
            "Manech sheep have distinctive red or black faces",
            "Traditional summer production in mountain huts (cayolars)",
            "Flavor ranges from mild and nutty to sharp and lanolin-rich with age",
            "Pairs perfectly with cherry jam - traditional Basque combination"
        ],
        "tags": ["cheese", "french", "basque", "sheep", "traditional", "ancient", "pyrenean"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-roquefort-blue-king",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Roquefort (King of Blue Cheeses)",
        "category": "mains",
        "attribution": "Ancient Roman-era tradition",
        "source_note": "Traditional French blue cheesemaking",
        "description": "Perhaps the world's most famous blue cheese, Roquefort has been made in the caves of Roquefort-sur-Soulzon for over 2,000 years. Legend says a shepherd left his lunch in a cave and returned to find the first Roquefort.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-9 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Lacaune sheep only"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "traditionally from cave-aged bread"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 60-90 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 60-90 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into large 1-inch cubes - handle very gently."},
            {"step": 5, "text": "Let curds rest, then ladle into molds without pressing."},
            {"step": 6, "text": "Drain naturally 3-5 days, flipping regularly."},
            {"step": 7, "text": "Salt surfaces generously over several days."},
            {"step": 8, "text": "Pierce cheese with needles to create air channels for blue mold."},
            {"step": 9, "text": "Age in natural caves or cave-like conditions (45°F, 95% humidity)."},
            {"step": 10, "text": "Blue veins develop over 3-4 weeks after piercing."},
            {"step": 11, "text": "Wrap in foil to slow mold growth once desired blueing achieved."},
            {"step": 12, "text": "Minimum 3 months aging; up to 9 months for stronger flavor."}
        ],
        "temperature": "86°F (30°C) for make; 45°F (7°C) for cave aging",
        "notes": [
            "AOC protected since 1925 - France's first protected cheese",
            "Must be aged in natural Combalou caves of Roquefort-sur-Soulzon",
            "The caves have natural 'fleurines' (fissures) that regulate temperature and humidity",
            "Lacaune sheep breed is required - milk is very rich",
            "Sharp, tangy, salty with creamy texture and blue-green veins"
        ],
        "tags": ["cheese", "french", "blue", "sheep", "traditional", "ancient", "cave-aged"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-stilton-english-king",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Stilton (English King of Cheeses)",
        "category": "mains",
        "attribution": "18th century English tradition",
        "source_note": "Traditional English blue cheesemaking",
        "description": "England's most famous cheese, Stilton has been called the 'King of English Cheeses' since the 18th century. Made only in three counties, this rich, creamy blue develops its distinctive veins through careful aging.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "9-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "high-quality pasteurized"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 60-90 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 90 minutes for very soft curd."},
            {"step": 4, "text": "Cut curds into large cubes, let rest 15 minutes."},
            {"step": 5, "text": "Ladle curds gently into draining trays - do not stir."},
            {"step": 6, "text": "Let drain overnight, milling and turning the curd mass."},
            {"step": 7, "text": "Mill curds by hand, salt thoroughly."},
            {"step": 8, "text": "Pack loosely into tall cylindrical molds - no pressing."},
            {"step": 9, "text": "Let drain 5-6 days, turning daily."},
            {"step": 10, "text": "Smooth and seal surface by rubbing."},
            {"step": 11, "text": "Age at 55°F with 90% humidity for 5-6 weeks."},
            {"step": 12, "text": "Pierce with needles to encourage blue veining."},
            {"step": 13, "text": "Continue aging 9-12 weeks total until proper blue development."}
        ],
        "temperature": "86°F (30°C) for make; 55°F (13°C) for aging",
        "notes": [
            "PDO protected - can only be made in Derbyshire, Leicestershire, and Nottinghamshire",
            "Never pressed - the open texture allows blue mold to develop",
            "Traditional to pour port into the center (though purists debate this)",
            "Should have creamy, golden paste with even blue-green veining",
            "White Stilton (unblued) is also made and often flavored with fruit"
        ],
        "tags": ["cheese", "english", "blue", "traditional", "PDO", "prestigious"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gorgonzola-italian-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gorgonzola (Italian Blue Classic)",
        "category": "mains",
        "attribution": "9th century Lombard tradition",
        "source_note": "Traditional Italian blue cheesemaking",
        "description": "One of the world's oldest blue cheeses, Gorgonzola has been made near Milan since at least 879 AD. Named for the town where tired cows stopped during transhumance, it comes in two styles: dolce (sweet/mild) and piccante (sharp).",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from Lombardy/Piedmont traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 45-60 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Let curds rest 10 minutes, then stir very gently."},
            {"step": 6, "text": "Drain whey and ladle curds into molds."},
            {"step": 7, "text": "Let drain naturally 24-48 hours, flipping frequently."},
            {"step": 8, "text": "Salt surfaces over several days."},
            {"step": 9, "text": "Age at 55°F with 90-95% humidity."},
            {"step": 10, "text": "Pierce with needles at 3-4 weeks to encourage blue veining."},
            {"step": 11, "text": "For DOLCE: age 2-3 months. For PICCANTE: age 3-4+ months."}
        ],
        "temperature": "86°F (30°C) for make; 55°F (13°C) for aging",
        "notes": [
            "DOP protected since 1996 - made only in Lombardy and Piedmont",
            "Dolce (sweet) is younger, creamier, milder - more blue-green marbling",
            "Piccante (sharp) is aged longer, firmer, more pungent",
            "Traditional story: cows were too tired to continue past Gorgonzola",
            "Excellent in risotto, with polenta, or simply with honey and walnuts"
        ],
        "tags": ["cheese", "italian", "blue", "traditional", "ancient", "lombardy"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-emmentaler-swiss-eyes",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Emmentaler (Swiss Cheese with Eyes)",
        "category": "mains",
        "attribution": "13th century Swiss tradition",
        "source_note": "Traditional Swiss alpine cheesemaking",
        "description": "The original 'Swiss cheese' with the famous holes, Emmentaler has been made in the Emme Valley since at least the 13th century. The distinctive eyes form from carbon dioxide released by Propionibacterium during aging.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "4-18 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "from grass-fed alpine cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium freudenreichii", "quantity": "1/16", "unit": "tsp", "prep_note": "essential for eyes"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacterium. Ripen 15-20 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 25-30 minutes."},
            {"step": 4, "text": "Cut curds very small - to rice grain size."},
            {"step": 5, "text": "Stir while raising temperature to 126-130°F (52-54°C) over 45-60 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very dry and firm."},
            {"step": 7, "text": "Press curds under whey briefly, then transfer to large molds."},
            {"step": 8, "text": "Press heavily for 24 hours, flipping multiple times."},
            {"step": 9, "text": "Brine for 2-3 days for traditional large wheels."},
            {"step": 10, "text": "Age at 55°F for 2-3 weeks."},
            {"step": 11, "text": "Move to warm room (68-77°F) for 4-6 weeks - eyes develop here."},
            {"step": 12, "text": "Return to cool aging for 4-18 months total."}
        ],
        "temperature": "90-130°F (32-54°C) for make; varies for aging",
        "notes": [
            "AOC protected - authentic Emmentaler only from specific Swiss regions",
            "Traditional wheels weigh 75-120 kg (165-265 lbs)",
            "The high cooking temperature (130°F) is critical for texture",
            "Eyes should be cherry to walnut size in well-made wheels",
            "Flavor is sweet, nutty, slightly fruity"
        ],
        "tags": ["cheese", "swiss", "alpine", "traditional", "eyes", "aged", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-comte-french-alpine-king",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Comté (French Alpine King)",
        "category": "mains",
        "attribution": "12th century Franche-Comté tradition",
        "source_note": "Traditional French alpine cheesemaking",
        "description": "France's most popular AOC cheese, Comté has been made in the Jura mountains since the 12th century. The cooperative 'fruitière' system where farmers pool milk dates back to this era. Each wheel requires 530 liters of milk.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "4-24 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "from Montbéliarde or French Simmental cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-35 minutes."},
            {"step": 4, "text": "Cut curds to wheat grain size using traditional 'tranche-caillé'."},
            {"step": 5, "text": "Stir while raising temperature to 131°F (55°C) over 30-45 minutes."},
            {"step": 6, "text": "Continue stirring until curds are dry and firm."},
            {"step": 7, "text": "Press curds under whey, then transfer to large hoop molds."},
            {"step": 8, "text": "Press heavily for 20-24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55°F with 92-96% humidity."},
            {"step": 11, "text": "Rub with brine and turn regularly."},
            {"step": 12, "text": "Minimum 4 months; 12-24 months for full flavor development."}
        ],
        "temperature": "90-131°F (32-55°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOC since 1958 - strict rules on breeds, feed, and production",
            "The 'fruitière' cooperative system is 800+ years old",
            "Flavor varies by season: summer milk gives fruitier cheese",
            "Should have small, sparse eyes or none at all (unlike Emmental)",
            "Graded 1-20 points; only 14+ can be sold as Comté"
        ],
        "tags": ["cheese", "french", "alpine", "traditional", "aged", "jura", "cooperative"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-manchego-spanish-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Manchego (Spanish La Mancha Sheep Cheese)",
        "category": "mains",
        "attribution": "Bronze Age Iberian tradition",
        "source_note": "Traditional Spanish sheep cheesemaking",
        "description": "Spain's most famous cheese, Manchego has been made in La Mancha for over 2,000 years - possibly since the Bronze Age. Made exclusively from Manchega sheep milk, it bears the distinctive zigzag pattern from traditional esparto grass molds.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-24 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Manchega sheep only"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for rind treatment"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add lamb rennet, let set 30-45 minutes."},
            {"step": 4, "text": "Cut curds to rice grain size."},
            {"step": 5, "text": "Stir and raise temperature to 104°F (40°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very firm."},
            {"step": 7, "text": "Drain whey and pack curds into molds with zigzag pattern inserts."},
            {"step": 8, "text": "Press heavily for 24 hours, flipping several times."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 50-55°F with 85% humidity."},
            {"step": 11, "text": "Rub rind with olive oil periodically."},
            {"step": 12, "text": "Fresco: 2 weeks. Semicurado: 3-6 months. Curado: 6-12 months. Viejo: 12+ months."}
        ],
        "temperature": "86-104°F (30-40°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1984 - must use Manchega sheep milk from La Mancha",
            "The zigzag pattern (pleita) comes from traditional esparto grass molds",
            "Manchega sheep are an ancient breed adapted to harsh La Mancha climate",
            "Young is mild and creamy; aged is hard, sharp, and complex",
            "Traditional pairing with quince paste (membrillo)"
        ],
        "tags": ["cheese", "spanish", "sheep", "traditional", "ancient", "la-mancha", "DOP"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-parmigiano-reggiano-king",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Parmigiano-Reggiano (King of Cheeses)",
        "category": "mains",
        "attribution": "12th century Emilian monastery tradition",
        "source_note": "Traditional Italian hard cheesemaking",
        "description": "Called the 'King of Cheeses,' Parmigiano-Reggiano has been made by Benedictine and Cistercian monks in Emilia-Romagna since the 12th century. Each wheel requires 550 liters of milk and at least 12 months of aging.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "12-36 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "part-skim from evening + whole from morning"},
            {"item": "natural whey starter", "quantity": "1/2", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "calf rennet only"},
            {"item": "cheese salt", "quantity": "", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine part-skim evening milk (fat skimmed overnight) with whole morning milk."},
            {"step": 2, "text": "Heat to 91-95°F (33-35°C) in traditional copper cauldron."},
            {"step": 3, "text": "Add natural whey starter from previous batch - no commercial cultures."},
            {"step": 4, "text": "Add calf rennet, let set 10-12 minutes."},
            {"step": 5, "text": "Break curd very finely using traditional 'spino' tool to rice grain size."},
            {"step": 6, "text": "Raise temperature to 131°F (55°C) while stirring."},
            {"step": 7, "text": "Let curds settle to bottom of cauldron in single mass."},
            {"step": 8, "text": "Lift curd mass in cloth, cut in two, place in wooden molds."},
            {"step": 9, "text": "Press with weights, flipping frequently for 2-3 days."},
            {"step": 10, "text": "Brine in saturated salt solution for 20-25 days."},
            {"step": 11, "text": "Age on wooden shelves at 64°F with 80% humidity."},
            {"step": 12, "text": "Turn and brush weekly. Minimum 12 months; 24-36 months for Stravecchio."}
        ],
        "temperature": "91-131°F (33-55°C) for make; 64°F (18°C) for aging",
        "notes": [
            "DOP protected - only made in Parma, Reggio Emilia, Modena, Bologna, Mantova",
            "Each wheel is stamped and certified by the Consorzio",
            "Traditional wheels weigh 38-40 kg (84-88 lbs)",
            "No additives allowed - only milk, salt, and rennet",
            "Tyrosine crystals develop during long aging - the 'crunch'"
        ],
        "tags": ["cheese", "italian", "hard", "traditional", "ancient", "DOP", "grana"],
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
