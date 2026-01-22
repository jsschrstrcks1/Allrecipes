#!/usr/bin/env python3
"""Add batch 60 - More ancient and historic cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-bandel-bengali-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bandel (Bengali Smoked Cheese)",
        "category": "mains",
        "attribution": "16th century Portuguese-Bengali tradition",
        "source_note": "Traditional Indian smoked cheesemaking",
        "description": "One of the few traditional Indian cheeses, Bandel was introduced by Portuguese traders to Bengal in the 16th century. Smoked over coconut husk or paddy straw, it's a unique fusion of European technique and South Asian ingredients.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "2-3 hours",
        "total_time": "2-3 days including smoking",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "full fat"},
            {"item": "lemon juice", "quantity": "1/4", "unit": "cup", "prep_note": "or vinegar"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "coconut husk or paddy straw", "quantity": "", "unit": "", "prep_note": "for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185°F (85°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat and add lemon juice slowly while stirring."},
            {"step": 3, "text": "Curds will separate from whey. Add more acid if needed."},
            {"step": 4, "text": "Let rest 10 minutes."},
            {"step": 5, "text": "Strain through cheesecloth, rinse curds with cold water."},
            {"step": 6, "text": "Add salt, mix well."},
            {"step": 7, "text": "Form into small disc shapes (2-3 inches diameter)."},
            {"step": 8, "text": "Press lightly for 1-2 hours to firm up."},
            {"step": 9, "text": "Prepare smoking chamber with coconut husk or paddy straw."},
            {"step": 10, "text": "Cold smoke cheese discs for 12-24 hours."},
            {"step": 11, "text": "Repeat smoking over 2-3 days for intense flavor."},
            {"step": 12, "text": "Store wrapped in cool, dry place. Eat within 2-3 weeks."}
        ],
        "temperature": "185°F (85°C) for curdling; cold smoke",
        "notes": [
            "Named after Bandel port near Kolkata where Portuguese traded",
            "Coconut husk smoking gives distinctive tropical smoky flavor",
            "One of India's only traditional smoked cheeses",
            "Nearly extinct - few producers remain in West Bengal",
            "Best eaten grilled or fried until golden"
        ],
        "tags": ["cheese", "indian", "bengali", "portuguese", "traditional", "smoked", "historical"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-kalari-kashmiri-dogra",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kalari (Kashmiri Dogra Cheese)",
        "category": "mains",
        "attribution": "Ancient Dogra tribal tradition",
        "source_note": "Traditional Kashmiri cheesemaking",
        "description": "Made by the Gaddi and Bakarwal nomadic tribes of Jammu & Kashmir, Kalari is India's answer to mozzarella. This stretched-curd cheese is traditionally fried until golden and eaten with bread - a 1000+ year old tradition.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "3-4 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw preferred"},
            {"item": "sour buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "for acidification"},
            {"item": "rennet or sour whey", "quantity": "1/4", "unit": "cup", "prep_note": "traditional uses previous whey"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add sour buttermilk and sour whey from previous batch."},
            {"step": 3, "text": "Let curdle 30-45 minutes."},
            {"step": 4, "text": "Cut curds and let rest under whey."},
            {"step": 5, "text": "Allow curds to acidify for 2-3 hours until stretchable."},
            {"step": 6, "text": "Drain curds, knead until smooth."},
            {"step": 7, "text": "Heat water to 170°F (77°C)."},
            {"step": 8, "text": "Stretch curds in hot water until elastic and smooth."},
            {"step": 9, "text": "Form into flat disc or dome shape."},
            {"step": 10, "text": "Salt surface lightly."},
            {"step": 11, "text": "Can be eaten fresh or stored in brine."},
            {"step": 12, "text": "Traditional serving: slice and pan-fry until golden brown."}
        ],
        "temperature": "95°F (35°C) for curd; 170°F (77°C) for stretching",
        "notes": [
            "Made by Gaddi and Bakarwal nomadic herding communities",
            "One of India's only stretched-curd (pasta filata) cheeses",
            "Best when fried - develops crispy golden exterior",
            "Served with traditional Dogri bread",
            "Nearly lost tradition - few producers remain"
        ],
        "tags": ["cheese", "indian", "kashmiri", "traditional", "tribal", "pasta-filata", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-lor-turkish-whey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Lor (Turkish Whey Cheese)",
        "category": "mains",
        "attribution": "Ancient Anatolian tradition",
        "source_note": "Traditional Turkish whey cheesemaking",
        "description": "Turkey's ricotta, Lor has been made by Anatolian shepherds for millennia. Made from the whey of other cheeses, it's a fresh, mild cheese used in savory böreks and sweet desserts throughout Turkey.",
        "servings_yield": "8-12 oz cheese",
        "prep_time": "10 minutes",
        "cook_time": "30-45 minutes",
        "total_time": "1-2 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from cheese making"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": "optional, for richer lor"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp", "prep_note": "if needed"}
        ],
        "instructions": [
            {"step": 1, "text": "Use whey immediately after cheesemaking while still warm."},
            {"step": 2, "text": "If cold, heat whey to 185-195°F (85-90°C)."},
            {"step": 3, "text": "Add fresh milk if richer lor is desired."},
            {"step": 4, "text": "Stir gently, watch for white curds rising."},
            {"step": 5, "text": "If curds don't form, add lemon juice."},
            {"step": 6, "text": "Let curds collect on surface for 10-15 minutes."},
            {"step": 7, "text": "Skim curds gently with slotted spoon."},
            {"step": 8, "text": "Transfer to cloth-lined strainer."},
            {"step": 9, "text": "Drain 1-2 hours until desired consistency."},
            {"step": 10, "text": "Salt to taste."},
            {"step": 11, "text": "Eat fresh within 2-3 days."}
        ],
        "temperature": "185-195°F (85-90°C)",
        "notes": [
            "Made throughout Turkey wherever cheese is produced",
            "Essential filling for Turkish böreks and gözleme",
            "Also used in desserts like lor tatlısı",
            "Very mild, fresh, creamy flavor",
            "Must be used quickly - doesn't keep well"
        ],
        "tags": ["cheese", "turkish", "anatolian", "traditional", "whey", "fresh", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cabrales-spanish-blue-cave",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cabrales (Spanish Cave-Aged Blue)",
        "category": "mains",
        "attribution": "Ancient Asturian Picos de Europa tradition",
        "source_note": "Traditional Spanish blue cheesemaking",
        "description": "Made in the limestone caves of the Picos de Europa mountains for over 2000 years, Cabrales is Spain's most famous blue cheese. Traditionally made from a blend of cow, goat, and sheep milk, it develops intense blue veins in natural caves.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "primary milk"},
            {"item": "raw goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "traditional blend"},
            {"item": "raw sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional"},
            {"item": "mesophilic starter", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cow, goat, and sheep milk (proportions vary by season)."},
            {"step": 2, "text": "Heat to 86°F (30°C)."},
            {"step": 3, "text": "Add mesophilic culture and P. roqueforti. Ripen 60 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 60-90 minutes."},
            {"step": 5, "text": "Cut curds into large 1-inch cubes."},
            {"step": 6, "text": "Let curds rest, then drain gently."},
            {"step": 7, "text": "Pack curds loosely into molds - no pressing."},
            {"step": 8, "text": "Drain naturally 2-3 days, flipping regularly."},
            {"step": 9, "text": "Salt all surfaces generously."},
            {"step": 10, "text": "Age in natural limestone cave (45-48°F, 90% humidity)."},
            {"step": 11, "text": "Pierce with needles after 3-4 weeks to encourage blue veining."},
            {"step": 12, "text": "Age minimum 3 months; 6 months for intense flavor."}
        ],
        "temperature": "86°F (30°C) for make; 45-48°F (7-9°C) for cave aging",
        "notes": [
            "PDO protected since 1981",
            "Must be aged in natural caves of Cabrales region",
            "One of the world's strongest blue cheeses",
            "Traditionally wrapped in maple or sycamore leaves",
            "Blend of milks varies by season - spring has most sheep milk"
        ],
        "tags": ["cheese", "spanish", "asturian", "traditional", "blue", "cave-aged", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-blue-dorset-vinney-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Blue Vinney (Dorset Skimmed Blue)",
        "category": "mains",
        "attribution": "17th century English farmhouse tradition",
        "source_note": "Traditional English blue cheesemaking",
        "description": "An ancient English blue made from skimmed milk left after buttermaking, Blue Vinney was made on Dorset farms for centuries. Nearly extinct by the 1970s, it's been revived by dedicated cheesemakers preserving England's heritage.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-5 months aging",
        "ingredients": [
            {"item": "skimmed cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "traditionally after cream removed for butter"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Use skimmed milk (cream removed for butter - traditional)."},
            {"step": 2, "text": "Heat to 86°F (30°C)."},
            {"step": 3, "text": "Add mesophilic culture and P. roqueforti. Ripen 60 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently and raise temperature slightly to 90°F (32°C)."},
            {"step": 7, "text": "Drain whey and pack curds loosely into molds."},
            {"step": 8, "text": "Drain naturally 2-3 days."},
            {"step": 9, "text": "Salt and age at 50-55°F with high humidity."},
            {"step": 10, "text": "Pierce after 3 weeks to encourage blue mold."},
            {"step": 11, "text": "Age 3-5 months until well-veined."}
        ],
        "temperature": "86-90°F (30-32°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Nearly extinct - revived in the 1980s",
            "Made from skimmed milk creates drier, harder texture than Stilton",
            "'Vinney' may derive from Old English 'fynig' meaning moldy",
            "Traditionally blue mold was encouraged by storing near boots or harnesses",
            "Low fat content means it ages differently than other blues"
        ],
        "tags": ["cheese", "english", "dorset", "traditional", "blue", "skimmed", "historical", "revived"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-vieux-boulogne-french-washed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vieux Boulogne (World's Smelliest Cheese)",
        "category": "mains",
        "attribution": "Northern French washed-rind tradition",
        "source_note": "Traditional French washed-rind cheesemaking",
        "description": "Scientifically proven to be the world's smelliest cheese in a Cranfield University study, Vieux Boulogne is washed with beer. Despite its powerful aroma, the interior is mild and creamy - a classic washed-rind paradox.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "7-9 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "beer", "quantity": "1", "unit": "cup", "prep_note": "local French beer traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 40-50 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently without raising temperature."},
            {"step": 6, "text": "Drain and ladle curds into square molds."},
            {"step": 7, "text": "Drain naturally 24-48 hours, flipping regularly."},
            {"step": 8, "text": "Salt surfaces."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "Wash with beer every 2-3 days."},
            {"step": 11, "text": "Continue for 7-9 weeks until rind is orange-red and very pungent."},
            {"step": 12, "text": "Interior should be soft and creamy despite powerful exterior aroma."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Cranfield University study found it 'smelliest' using electronic nose",
            "From Pas-de-Calais region of northern France",
            "Beer washing contributes to unique aroma compounds",
            "Interior is surprisingly mild and creamy",
            "Pairs well with local beers"
        ],
        "tags": ["cheese", "french", "traditional", "washed-rind", "stinky", "beer-washed"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-casu-axedu-sardinian-sour",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Casu Axedu (Sardinian Sour Cheese)",
        "category": "mains",
        "attribution": "Ancient Sardinian shepherd tradition",
        "source_note": "Traditional Sardinian fresh cheesemaking",
        "description": "A simple, ancient Sardinian fresh cheese made by naturally souring milk, Casu Axedu is one of the Mediterranean's most basic cheeses. Made for millennia by shepherds, it's the ancestor of many modern acid-set cheeses.",
        "servings_yield": "1 lb cheese",
        "prep_time": "10 minutes",
        "cook_time": "N/A",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "or goat's milk"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour fresh sheep's milk into earthenware crock or glass jar."},
            {"step": 2, "text": "Cover loosely and leave at warm room temperature."},
            {"step": 3, "text": "Let milk sour naturally for 24-48 hours."},
            {"step": 4, "text": "Milk will thicken and set like yogurt."},
            {"step": 5, "text": "When fully curdled, line colander with cloth."},
            {"step": 6, "text": "Gently ladle curdled milk into cloth."},
            {"step": 7, "text": "Let drain 4-8 hours until desired consistency."},
            {"step": 8, "text": "Salt lightly if desired."},
            {"step": 9, "text": "Eat fresh within 2-3 days."}
        ],
        "temperature": "Warm room temperature for souring",
        "notes": [
            "One of the simplest and oldest cheese techniques",
            "'Axedu' means 'sour' in Sardinian",
            "No rennet, no heat, no added cultures",
            "Relies on natural milk bacteria for acidification",
            "Similar ancient cheeses found throughout Mediterranean"
        ],
        "tags": ["cheese", "sardinian", "italian", "traditional", "ancient", "fresh", "simple", "acid-set"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-mizithra-greek-ancient-whey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mizithra (Greek Ancient Whey Cheese)",
        "category": "mains",
        "attribution": "Ancient Greek Byzantine tradition",
        "source_note": "Traditional Greek whey cheesemaking",
        "description": "Made in Greece since Byzantine times, Mizithra is produced from sheep and goat milk whey. Fresh Mizithra is soft and mild; aged Mizithra becomes hard and sharp - used for grating over pasta like Greek ricotta salata.",
        "servings_yield": "8-12 oz cheese",
        "prep_time": "10 minutes",
        "cook_time": "30-45 minutes",
        "total_time": "Fresh: same day; Aged: 3-4 months",
        "ingredients": [
            {"item": "sheep/goat whey", "quantity": "1", "unit": "gallon", "prep_note": "from feta or kefalotyri making"},
            {"item": "sheep's or goat's milk", "quantity": "1", "unit": "cup", "prep_note": "optional, for richer mizithra"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "for fresh; 2 tbsp for aged"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh whey immediately after making sheep/goat cheese."},
            {"step": 2, "text": "Heat whey to 185-195°F (85-90°C)."},
            {"step": 3, "text": "Add fresh milk if richer cheese is desired."},
            {"step": 4, "text": "Stir gently as curds rise to surface."},
            {"step": 5, "text": "Let curds collect for 10-15 minutes."},
            {"step": 6, "text": "Skim curds into cloth-lined mold."},
            {"step": 7, "text": "FRESH MIZITHRA: drain briefly, salt lightly, eat within days."},
            {"step": 8, "text": "AGED MIZITHRA: salt generously, press in mold."},
            {"step": 9, "text": "For aged: dry for several days, then age 3-4 months."},
            {"step": 10, "text": "Aged mizithra becomes hard and grateable."}
        ],
        "temperature": "185-195°F (85-90°C)",
        "notes": [
            "PDO protected as part of traditional Greek cheesemaking",
            "Fresh is like ricotta; aged is like ricotta salata",
            "Traditional over Greek pasta dishes",
            "The word may derive from Byzantine Greek 'myzíthra'",
            "Often made alongside feta - nothing wasted"
        ],
        "tags": ["cheese", "greek", "traditional", "ancient", "whey", "byzantine", "dual-style"],
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
