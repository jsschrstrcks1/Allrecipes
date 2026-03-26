#!/usr/bin/env python3
"""Add batch 61 - More ancient and regional cheeses plus advanced techniques."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-pecorino-romano-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Romano (Ancient Roman Legionary Cheese)",
        "category": "mains",
        "attribution": "Ancient Roman tradition (2000+ years)",
        "source_note": "Traditional Italian hard sheep cheesemaking",
        "description": "One of the world's oldest named cheeses, Pecorino Romano was part of the daily ration of Roman legionaries. Sharp, salty, and made for grating, it has been produced in Lazio since at least 100 BC - over 2000 years.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "8-12 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "3", "unit": "gallons", "prep_note": "from Lazio or Sardinian sheep"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "lamb-derived traditional"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": "generous salting traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 99-102°F (37-39°C) - warmer than many cheeses."},
            {"step": 2, "text": "Add natural whey starter (scotta innesto), ripen 15-20 minutes."},
            {"step": 3, "text": "Add lamb rennet paste, let set 20-25 minutes."},
            {"step": 4, "text": "Cut curds very small - to rice grain size."},
            {"step": 5, "text": "Stir and raise temperature to 118-122°F (48-50°C)."},
            {"step": 6, "text": "Continue stirring until curds are very dry."},
            {"step": 7, "text": "Drain and pack curds into molds, pressing hot."},
            {"step": 8, "text": "Pierce with needles to release trapped whey."},
            {"step": 9, "text": "Press heavily for 24 hours."},
            {"step": 10, "text": "Rub generously with dry salt over 2-3 months."},
            {"step": 11, "text": "Age at 50-55°F with 80% humidity."},
            {"step": 12, "text": "Minimum 8 months; traditional aging 12 months or more."}
        ],
        "temperature": "99-122°F (37-50°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1996 - made in Lazio, Sardinia, and Grosseto",
            "Roman legionaries received 27 grams daily as part of rations",
            "Lamb rennet creates characteristic sharp, piquant flavor",
            "Saltier than Parmigiano-Reggiano - traditional grating cheese",
            "Essential for authentic carbonara, amatriciana, cacio e pepe"
        ],
        "tags": ["cheese", "italian", "roman", "traditional", "ancient", "sheep", "hard", "grating"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-graviera-crete-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Graviera Kritis (Cretan Aged Cheese)",
        "category": "mains",
        "attribution": "Ancient Cretan tradition",
        "source_note": "Traditional Greek hard cheesemaking",
        "description": "Crete's most famous cheese, Graviera has been made on the island for centuries. Made primarily from sheep's milk with some goat, it's aged in mountain caves, developing sweet, nutty flavors reminiscent of Gruyère.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "minimum 80%"},
            {"item": "goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "up to 20%"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep and goat milk (at least 80% sheep)."},
            {"step": 2, "text": "Heat to 95°F (35°C)."},
            {"step": 3, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 4, "text": "Add rennet, let set 30-40 minutes."},
            {"step": 5, "text": "Cut curds to corn kernel size."},
            {"step": 6, "text": "Stir while raising temperature to 122-126°F (50-52°C)."},
            {"step": 7, "text": "Continue stirring until curds are very firm."},
            {"step": 8, "text": "Drain and pack into molds."},
            {"step": 9, "text": "Press heavily for 24 hours."},
            {"step": 10, "text": "Brine for 2-3 days."},
            {"step": 11, "text": "Age at 55-60°F with 85% humidity."},
            {"step": 12, "text": "Minimum 3 months; best at 6-12 months."}
        ],
        "temperature": "95-126°F (35-52°C) for make; 55-60°F (13-16°C) for aging",
        "notes": [
            "PDO protected - Graviera Kritis is the Cretan version",
            "High cooking temperature similar to Swiss alpine cheeses",
            "Sweet, nutty flavor develops with age",
            "Can be eaten as table cheese or grated",
            "Cretan mountain pastures give distinctive character"
        ],
        "tags": ["cheese", "greek", "cretan", "traditional", "sheep", "aged", "alpine-style"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-mahon-menorcan-spanish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mahón-Menorca (Balearic Island Cheese)",
        "category": "mains",
        "attribution": "Ancient Menorcan tradition (Bronze Age origins)",
        "source_note": "Traditional Spanish island cheesemaking",
        "description": "Made on Menorca since prehistoric times, Mahón is distinguished by its square shape from being wrapped in cloth and pressed. The orange rind comes from rubbing with butter, oil, and paprika during aging.",
        "servings_yield": "2 lb square",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Menorcan Friesian cows"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for rind"},
            {"item": "paprika", "quantity": "1", "unit": "tsp", "prep_note": "for rind color"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into small pieces."},
            {"step": 5, "text": "Stir and raise temperature to 100°F (38°C)."},
            {"step": 6, "text": "Drain and gather curds in cloth ('fogasser')."},
            {"step": 7, "text": "Tie cloth corners together, twist and press to form square shape."},
            {"step": 8, "text": "Press in square mold with weights for 24-48 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55°F."},
            {"step": 11, "text": "Rub rind with mixture of oil, butter, and paprika."},
            {"step": 12, "text": "Tierno: 2 months. Semicurado: 2-5 months. Curado: 5-12 months."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 55°F (13°C) for aging",
        "notes": [
            "PDO protected since 1985",
            "Square shape from traditional cloth-pressing (fogasser) technique",
            "Orange rind from butter/oil/paprika rubbing",
            "Bronze Age talayotic civilization may have made similar cheese",
            "Flavor ranges from mild and creamy to sharp and granular"
        ],
        "tags": ["cheese", "spanish", "menorcan", "balearic", "traditional", "ancient", "square"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-azeitao-portuguese-thistle",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo de Azeitão (Portuguese Thistle Cheese)",
        "category": "mains",
        "attribution": "19th century Setúbal tradition",
        "source_note": "Traditional Portuguese thistle-rennet cheesemaking",
        "description": "A small, soft cheese from the Arrábida region, Azeitão is made with thistle rennet which gives it a distinctive slightly bitter, herbal note. When perfectly ripe, the interior flows like honey.",
        "servings_yield": "8 oz cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-4 weeks aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "from Serra da Arrábida"},
            {"item": "cardoon thistle flowers", "quantity": "2", "unit": "tbsp", "prep_note": "dried, for rennet"},
            {"item": "warm water", "quantity": "1/2", "unit": "cup", "prep_note": "for thistle infusion"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare thistle rennet: steep dried thistle flowers in warm water for several hours."},
            {"step": 2, "text": "Strain thistle liquid through fine cloth."},
            {"step": 3, "text": "Heat sheep's milk to 82-86°F (28-30°C) - cooler than many cheeses."},
            {"step": 4, "text": "Add thistle rennet liquid, stir gently."},
            {"step": 5, "text": "Let set 60-90 minutes for soft curd."},
            {"step": 6, "text": "Cut curds very gently into large pieces."},
            {"step": 7, "text": "Ladle into small perforated molds without pressing."},
            {"step": 8, "text": "Drain naturally for 24-48 hours."},
            {"step": 9, "text": "Salt surfaces lightly."},
            {"step": 10, "text": "Age at 50-55°F with 90% humidity."},
            {"step": 11, "text": "Turn daily. Ready in 3-4 weeks when interior is soft."},
            {"step": 12, "text": "Cut top rind off and spoon out liquid interior."}
        ],
        "temperature": "82-86°F (28-30°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1996",
            "Thistle (cardoon) rennet gives slight bitter, herbal notes",
            "When ripe, interior flows like thick cream",
            "Similar to Serra da Estrela but from different region",
            "Eat at room temperature for best texture"
        ],
        "tags": ["cheese", "portuguese", "traditional", "thistle-rennet", "soft", "sheep", "flowing"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queso-tetilla-galician",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Tetilla (Galician Breast Cheese)",
        "category": "mains",
        "attribution": "Ancient Galician tradition",
        "source_note": "Traditional Spanish regional cheesemaking",
        "description": "Named for its distinctive breast-like shape (tetilla means 'small breast'), this mild Galician cheese has ancient Celtic origins. Creamy and slightly tangy, it's one of Spain's most popular table cheeses.",
        "servings_yield": "1-2 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Galician breeds"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch pieces."},
            {"step": 5, "text": "Stir gently without raising temperature."},
            {"step": 6, "text": "Drain and pack curds into breast-shaped molds."},
            {"step": 7, "text": "Press lightly to maintain soft texture."},
            {"step": 8, "text": "Turn frequently during first 24 hours."},
            {"step": 9, "text": "Brine for 12-24 hours or dry salt."},
            {"step": 10, "text": "Age at 50-55°F with 85% humidity."},
            {"step": 11, "text": "Ready in 2-4 weeks when interior is creamy."}
        ],
        "temperature": "86-90°F (30-32°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1992",
            "The conical shape was traditionally formed by hanging in cloth",
            "Celtic origins - Galicia has strong Celtic heritage",
            "Mild, creamy, slightly tangy flavor",
            "Pairs well with Galician Albariño wine"
        ],
        "tags": ["cheese", "spanish", "galician", "traditional", "celtic", "mild", "shaped"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-beaufort-alpine-gruyere",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Beaufort (French Alpine King)",
        "category": "mains",
        "attribution": "Ancient Savoyard alpine tradition",
        "source_note": "Traditional French alpine cheesemaking",
        "description": "Called the 'Prince of Gruyères,' Beaufort has been made in the Savoie Alps since Roman times. Its distinctive concave rind comes from the leather strap ('cercle') used during pressing. One of France's great mountain cheeses.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "5-15 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "from Tarine or Abondance cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 91°F (33°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-35 minutes."},
            {"step": 4, "text": "Cut curds very small - to wheat grain size."},
            {"step": 5, "text": "Stir and raise temperature to 130-135°F (54-57°C) over 45-60 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very dry."},
            {"step": 7, "text": "Press curds under whey briefly."},
            {"step": 8, "text": "Transfer to molds with concave sides (or use strap/cercle around edge)."},
            {"step": 9, "text": "Press heavily for 24 hours."},
            {"step": 10, "text": "Brine for 24-48 hours."},
            {"step": 11, "text": "Age at 50-55°F with 92-95% humidity."},
            {"step": 12, "text": "Rub with brine. Minimum 5 months; up to 15 months for Beaufort d'été or d'alpage."}
        ],
        "temperature": "91-135°F (33-57°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "AOC protected since 1968",
            "Concave sides are unique to Beaufort - from leather strap pressing",
            "No holes - unlike Emmental and Gruyère",
            "Beaufort d'été (summer) and d'alpage (mountain pasture) are most prized",
            "Tarine and Abondance breeds are required by AOC"
        ],
        "tags": ["cheese", "french", "alpine", "savoie", "traditional", "ancient", "gruyere-style"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-langres-burgundy-crater",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Langres (Burgundy Crater Cheese)",
        "category": "mains",
        "attribution": "18th century Champagne-Burgundy tradition",
        "source_note": "Traditional French washed-rind cheesemaking",
        "description": "Unique among washed-rind cheeses for its crater-shaped top (fontaine), Langres is never turned during aging - the top sinks naturally. The crater is traditionally filled with Marc de Bourgogne or Champagne before eating.",
        "servings_yield": "8-10 oz cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "annatto", "quantity": "2", "unit": "drops", "prep_note": "optional for color"},
            {"item": "brine solution", "quantity": "1", "unit": "cup", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add annatto if using."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 60 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 60-90 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest, then ladle into cylindrical molds."},
            {"step": 6, "text": "Drain naturally 24-48 hours."},
            {"step": 7, "text": "Salt surfaces after unmolding."},
            {"step": 8, "text": "CRITICAL: Never turn the cheese during aging."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "Wash sides with brine every 2-3 days."},
            {"step": 11, "text": "Top will sink naturally, forming characteristic 'fontaine' crater."},
            {"step": 12, "text": "Ready at 5-8 weeks when rind is orange and interior soft."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOC protected since 1991",
            "Never turned - this creates the unique sunken top",
            "Traditionally fill crater with Marc de Bourgogne or Champagne",
            "Similar to Époisses but with distinctive shape",
            "Interior should be soft and creamy under sticky orange rind"
        ],
        "tags": ["cheese", "french", "burgundy", "traditional", "washed-rind", "crater", "unique"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-saint-nectaire-auvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Saint-Nectaire (Auvergne Volcanic Cheese)",
        "category": "mains",
        "attribution": "17th century Auvergne tradition",
        "source_note": "Traditional French volcanic region cheesemaking",
        "description": "Made on the volcanic slopes of Auvergne since at least the 17th century, Saint-Nectaire develops its distinctive grey-orange rind from the unique microflora of the region. The volcanic soil gives the milk its distinctive mineral character.",
        "servings_yield": "1.5-2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Salers cattle"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir and raise temperature slightly to 95°F (35°C)."},
            {"step": 6, "text": "Drain and press curds into molds."},
            {"step": 7, "text": "Press at moderate weight for 12-24 hours."},
            {"step": 8, "text": "Salt surfaces by rubbing."},
            {"step": 9, "text": "Age on rye straw in cool cave (50°F)."},
            {"step": 10, "text": "Turn frequently. Natural molds develop grey/orange rind."},
            {"step": 11, "text": "Minimum 4 weeks; 6-8 weeks for full flavor."}
        ],
        "temperature": "90-95°F (32-35°C) for make; 50°F (10°C) for aging",
        "notes": [
            "AOC protected since 1955",
            "Volcanic soil gives milk unique mineral terroir",
            "Fermier (farm) has green casein label; Laitier (dairy) has green square",
            "Traditional aging on rye straw contributes to rind development",
            "Interior is semi-soft, earthy, nutty with mushroom notes"
        ],
        "tags": ["cheese", "french", "auvergne", "traditional", "volcanic", "semi-soft", "cave-aged"],
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
