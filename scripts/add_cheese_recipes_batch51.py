#!/usr/bin/env python3
"""Add batch 51 - Ancient world cheeses and traditional mountain cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-make-record-keeping",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Essential Record Keeping",
        "category": "mains",
        "attribution": "Artisan cheesemaking best practices",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Detailed records are the foundation of consistent cheesemaking. What works once may not work twice without documentation - and troubleshooting problems requires knowing exactly what you did.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "notebook or digital system", "quantity": "", "unit": "", "prep_note": "waterproof is best"},
            {"item": "thermometer log sheets", "quantity": "", "unit": "", "prep_note": ""},
            {"item": "pH strips or meter", "quantity": "", "unit": "", "prep_note": "for tracking acidification"},
            {"item": "cheese labeling system", "quantity": "", "unit": "", "prep_note": "tags, markers, etc."}
        ],
        "instructions": [
            {"step": 1, "text": "MILK RECORDS: Source, date, breed, pasteurized/raw, temperature when received, any abnormalities noted."},
            {"step": 2, "text": "CULTURE RECORDS: Type, brand, amount used, age of culture, any adjustments made."},
            {"step": 3, "text": "TIME LOG: Start time, culture addition, rennet addition, cutting time, each step timed."},
            {"step": 4, "text": "TEMPERATURE LOG: Milk temp at start, target temp, actual temp achieved, temp at each major step."},
            {"step": 5, "text": "pH RECORDS: Starting pH, pH at rennet, pH at drain, pH at salt - critical for troubleshooting."},
            {"step": 6, "text": "OBSERVATIONS: Curd firmness, cutting ease, whey appearance, any unusual behaviors."},
            {"step": 7, "text": "PRESSING: Weight used, duration, number of flips, final wheel weight."},
            {"step": 8, "text": "AGING: Start date, location, temperature/humidity of cave, turning schedule."},
            {"step": 9, "text": "Label each wheel with unique ID (e.g., CHD-2025-003 = Cheddar, 2025, batch 3)."},
            {"step": 10, "text": "TASTING NOTES: Sample at intervals, record flavor development, texture changes."},
            {"step": 11, "text": "OUTCOME: Success/failure, what worked, what to change next time."},
            {"step": 12, "text": "Review records before each make to refine your process continuously."}
        ],
        "temperature": "N/A",
        "notes": [
            "Without records, you cannot repeat successes or learn from failures",
            "Professional cheesemakers keep decades of records - patterns emerge over time",
            "Digital spreadsheets allow easy comparison across batches",
            "Photos of each stage are valuable records too",
            "Your records become your most valuable cheesemaking resource"
        ],
        "tags": ["cheese", "technique", "tip", "records", "documentation", "best-practices"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-appenzeller-herbal-brine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Appenzeller (Swiss Herbal Brine Cheese)",
        "category": "mains",
        "attribution": "700+ year Swiss tradition",
        "source_note": "Traditional Swiss alpine cheesemaking",
        "description": "Made in northeastern Switzerland for over 700 years, Appenzeller is washed with a secret herbal brine called 'sulz' containing wine, cider, herbs, and spices. Only three people know the full recipe, making it one of cheese's great mysteries.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "alpine pasture"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "white wine or cider", "quantity": "1", "unit": "cup", "prep_note": "for herbal brine"},
            {"item": "dried herbs", "quantity": "2", "unit": "tbsp", "prep_note": "thyme, savory, pepper, etc."}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-35 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes."},
            {"step": 5, "text": "Stir gently while raising temperature to 115°F (46°C) over 45 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very firm."},
            {"step": 7, "text": "Drain and pack curds into wheel molds."},
            {"step": 8, "text": "Press heavily for 24 hours."},
            {"step": 9, "text": "Brine in plain salt brine for 24-48 hours."},
            {"step": 10, "text": "Prepare herbal wash: steep herbs in wine/cider mixture, add salt."},
            {"step": 11, "text": "Age at 55°F with 90% humidity."},
            {"step": 12, "text": "Wash with herbal brine every 2-3 days for first month."},
            {"step": 13, "text": "Continue weekly washing for 3-6 months total aging."}
        ],
        "temperature": "90-115°F (32-46°C) for make; 55°F (13°C) for aging",
        "notes": [
            "The secret 'sulz' wash recipe is known by only three people",
            "Comes in three ages: Classic (3-4 mo), Surchoix (4-6 mo), Extra (6+ mo)",
            "The herbal wash creates golden-orange rind and distinctive spicy aroma",
            "Each farm develops slightly different flavor from their own sulz variation",
            "Protected by strict Swiss AOC regulations"
        ],
        "tags": ["cheese", "swiss", "alpine", "traditional", "washed-rind", "herbal", "secret"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gruyere-switzerland-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gruyère (Swiss Alpine Classic)",
        "category": "mains",
        "attribution": "12th century Fribourg tradition",
        "source_note": "Traditional Swiss alpine cheesemaking",
        "description": "Named for the town of Gruyères in the canton of Fribourg, this iconic Swiss cheese has been made since at least the 12th century. Its complex, nutty sweetness and excellent melting properties make it essential for fondue and gratins.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "5-18 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from grass-fed alpine cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 93°F (34°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 15-20 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 35-45 minutes."},
            {"step": 4, "text": "Cut curds very small - to wheat grain size."},
            {"step": 5, "text": "Stir gently while raising temperature to 131°F (55°C) over 45-60 minutes. This high temperature is critical."},
            {"step": 6, "text": "Continue stirring until curds are very dry and firm."},
            {"step": 7, "text": "Press curds under whey briefly before draining."},
            {"step": 8, "text": "Transfer to molds, press heavily for 24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55-57°F with 95% humidity."},
            {"step": 11, "text": "Wash with light brine solution weekly for first few months."},
            {"step": 12, "text": "Turn regularly. Minimum 5 months aging; 12-18 months for Reserve."}
        ],
        "temperature": "93-131°F (34-55°C) for make; 55-57°F (13-14°C) for aging",
        "notes": [
            "AOC/AOP protected - must be made in specific Swiss cantons",
            "The high cooking temperature (131°F) differentiates Gruyère technique",
            "Traditional wheels weigh 25-40 kg (55-88 lbs)",
            "Should have few or no eyes - unlike Emmental",
            "Essential for Swiss fondue - often blended with Vacherin Fribourgeois"
        ],
        "tags": ["cheese", "swiss", "alpine", "traditional", "fondue", "aged", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-tilsit-german-baltic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tilsit (German Baltic Cheese)",
        "category": "mains",
        "attribution": "19th century Prussian-Swiss tradition",
        "source_note": "Traditional German/Swiss cheesemaking",
        "description": "Created by Swiss immigrants in the Prussian town of Tilsit (now Russian Sovetsk) in the mid-1800s. When they couldn't replicate Swiss conditions, they accidentally created a new cheese - semi-soft, tangy, and full of small irregular holes.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "gallon", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently for 15 minutes without raising temperature."},
            {"step": 6, "text": "Raise temperature slowly to 100°F (38°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are moderately firm."},
            {"step": 8, "text": "Drain whey and pack curds loosely into molds."},
            {"step": 9, "text": "Press at moderate weight for 12-24 hours."},
            {"step": 10, "text": "Brine for 24-48 hours."},
            {"step": 11, "text": "Age at 55°F with 90-95% humidity."},
            {"step": 12, "text": "Wash with brine every 2-3 days for first 2 weeks."},
            {"step": 13, "text": "Continue aging 2-6 months, washing less frequently."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Now made in Germany, Switzerland, and internationally",
            "Distinctive irregular small holes throughout",
            "Flavor ranges from mild to pungent depending on age",
            "German Tilsit tends stronger; Swiss Tilsit is milder",
            "The 'accidental' origin story is beloved by cheesemakers"
        ],
        "tags": ["cheese", "german", "swiss", "traditional", "washed-rind", "semi-soft"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-havarti-danish-cream",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Havarti (Danish Cream Cheese)",
        "category": "mains",
        "attribution": "19th century Danish innovation",
        "source_note": "Traditional Danish cheesemaking",
        "description": "Developed by Hanne Nielsen in the 1860s after traveling to learn European cheesemaking, Havarti is a buttery, semi-soft Danish cheese. Its small irregular holes and creamy texture made it internationally beloved.",
        "servings_yield": "2 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "high fat content preferred"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-50 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest 5 minutes."},
            {"step": 6, "text": "Stir very gently for 15 minutes - do not break curds."},
            {"step": 7, "text": "Drain about 1/3 of whey, replace with same amount warm water (wash technique)."},
            {"step": 8, "text": "Stir gently 15 more minutes, gradually reaching 100°F (38°C)."},
            {"step": 9, "text": "Drain whey, keeping curds moist."},
            {"step": 10, "text": "Pack curds into molds gently - don't compress too much."},
            {"step": 11, "text": "Press at light weight for 30 minutes, flip, continue pressing at moderate weight for 6-8 hours."},
            {"step": 12, "text": "Brine for 12-24 hours."},
            {"step": 13, "text": "Age at 50°F with 85% humidity for 2-3 months."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 50°F (10°C) for aging",
        "notes": [
            "Named after Hanne Nielsen's farm, Havarthigaard",
            "The washing step (replacing whey with water) creates mild, sweet flavor",
            "Often flavored with dill, caraway, or other additions",
            "Cream Havarti is enriched with additional cream for extra richness",
            "Excellent melting cheese - perfect for sandwiches"
        ],
        "tags": ["cheese", "danish", "traditional", "semi-soft", "washed-curd", "creamy"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-port-salut-trappist-original",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Port-Salut (Trappist Original)",
        "category": "mains",
        "attribution": "19th century Trappist monastery tradition",
        "source_note": "Traditional French monastic cheesemaking",
        "description": "Created by Trappist monks at the Abbey of Notre-Dame du Port du Salut in the 1820s, this was the original monastery cheese that inspired all 'Trappist-style' cheeses. Mild, creamy, with a distinctive orange rind.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for rind"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently and raise temperature to 98°F (37°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are moderately firm but still moist."},
            {"step": 7, "text": "Drain whey and pack curds into molds."},
            {"step": 8, "text": "Press at light weight for 1 hour, flip, moderate weight for 4-6 hours."},
            {"step": 9, "text": "Brine for 8-12 hours."},
            {"step": 10, "text": "Age at 55°F with 95% humidity."},
            {"step": 11, "text": "Wash with light brine every 2-3 days for first 2 weeks."},
            {"step": 12, "text": "Continue washing weekly. Ready in 4-6 weeks."}
        ],
        "temperature": "86-98°F (30-37°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Original recipe was sold by monks in 1959 - commercial versions differ",
            "Authentic abbey-made version is called 'Entrammes' now",
            "The orange rind from B. linens bacteria is edible and flavorful",
            "Inspired many monastery cheeses: Chimay, Orval, Westmalle",
            "Interior should be smooth, creamy, and mild"
        ],
        "tags": ["cheese", "french", "trappist", "traditional", "monastery", "washed-rind"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-limburger-belgian-stinky",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Limburger (Belgian Stinky Cheese)",
        "category": "mains",
        "attribution": "Medieval Belgian tradition",
        "source_note": "Traditional Belgian washed-rind cheesemaking",
        "description": "One of the world's most pungent cheeses, Limburger originated in the Belgian province of Liège but is now primarily made in Germany. The bacteria that create its powerful aroma are the same ones found on human skin - hence the 'foot smell' reputation.",
        "servings_yield": "1 lb brick",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "6-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "essential for authentic flavor"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into large 1-inch cubes."},
            {"step": 5, "text": "Let curds rest 5-10 minutes - minimal stirring."},
            {"step": 6, "text": "Ladle curds gently into rectangular brick molds."},
            {"step": 7, "text": "Let drain naturally - no pressing or very light pressure only."},
            {"step": 8, "text": "Flip several times over 24 hours."},
            {"step": 9, "text": "Salt surfaces or brief brine."},
            {"step": 10, "text": "Age at 55°F with 95%+ humidity."},
            {"step": 11, "text": "Wash with brine every day for first week, then every 2-3 days."},
            {"step": 12, "text": "Rind turns from white to yellow to orange-red as it ages."},
            {"step": 13, "text": "Ready at 6 weeks (mild) to 12 weeks (very strong)."}
        ],
        "temperature": "86°F (30°C) for make; 55°F (13°C) for aging",
        "notes": [
            "B. linens bacteria create the legendary smell",
            "Despite the aroma, the interior is mild and creamy",
            "Traditional in Wisconsin German communities",
            "Store wrapped separately - the smell permeates everything",
            "Best eaten at room temperature on dark bread with raw onion"
        ],
        "tags": ["cheese", "belgian", "german", "traditional", "washed-rind", "stinky"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-muenster-alsatian-monastery",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Münster (Alsatian Monastery Cheese)",
        "category": "mains",
        "attribution": "7th century Alsatian monastery tradition",
        "source_note": "Traditional French-German monastery cheesemaking",
        "description": "Not to be confused with American Muenster, true Alsatian Münster has been made since the 7th century in the Vosges Mountains. This pungent washed-rind cheese is one of France's oldest, named for the monastery (munster = monastery) where monks first made it.",
        "servings_yield": "1.5 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Vosges cattle traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "brine with marc", "quantity": "1", "unit": "quart", "prep_note": "optional - marc de gewürztraminer traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 40-50 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes - relatively large."},
            {"step": 5, "text": "Let curds rest 10 minutes, then stir very gently."},
            {"step": 6, "text": "Drain whey and ladle curds into round molds."},
            {"step": 7, "text": "Let drain naturally without pressing for 24 hours, flipping several times."},
            {"step": 8, "text": "Salt surfaces or brief brine."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "Wash every 2-3 days with brine (traditionally with marc added)."},
            {"step": 11, "text": "Continue washing for 5-8 weeks until rind is sticky orange."},
            {"step": 12, "text": "Interior should be soft and almost runny when fully ripe."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOC Munster-Géromé protects the authentic Vosges versions",
            "Traditional to serve with cumin seeds sprinkled on top",
            "Interior ripens from outside in - ripe Münster bulges slightly",
            "Much stronger than American 'Muenster' which is a different cheese entirely",
            "Pairs perfectly with Alsatian gewürztraminer wine"
        ],
        "tags": ["cheese", "french", "alsatian", "traditional", "monastery", "washed-rind", "stinky"],
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
