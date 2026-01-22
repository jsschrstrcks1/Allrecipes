#!/usr/bin/env python3
"""Add batch 42 - More traditional cheeses and homestead cheesemaking tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Traditional Cheeses
    {
        "id": "traditional-queso-chihuahua-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Chihuahua (Mexican Mennonite Cheese)",
        "category": "mains",
        "attribution": "Chihuahua, Mexico / 1920s",
        "source_note": "Created by Mennonite settlers in Chihuahua. A melting cheese adapted from their Dutch heritage.",
        "description": "Mexican Mennonite cheese with excellent melting properties, mild buttery flavor, similar to mild cheddar or Colby.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "1-3 months aging",
        "total_time": "1-3 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "annatto", "quantity": "1/8", "unit": "tsp", "prep_note": "optional, for color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F."},
            {"step": 2, "text": "Add annatto if using for traditional golden color."},
            {"step": 3, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Stir gently while raising temperature to 102°F over 30 minutes."},
            {"step": 8, "text": "Drain 1/3 of whey, add warm water (washed-curd technique)."},
            {"step": 9, "text": "Continue stirring at 102°F for 30 minutes."},
            {"step": 10, "text": "Drain curds, add salt, mix well."},
            {"step": 11, "text": "Pack into mold and press at 40 lbs for 24 hours."},
            {"step": 12, "text": "Age at 55°F for 1-3 months."}
        ],
        "temperature": "88-102°F make, 55°F aging",
        "notes": [
            "Mennonites from Canada settled in Chihuahua in the 1920s",
            "Washed-curd technique creates mild, sweet flavor",
            "Excellent melting cheese for quesadillas and queso fundido",
            "Also called queso menonita"
        ],
        "tags": ["cheese", "traditional", "mexican", "mennonite", "melting", "washed-curd", "1920s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-requeson-mexican-ricotta",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Requesón (Mexican Whey Cheese)",
        "category": "mains",
        "attribution": "Mexico / Spanish Colonial",
        "source_note": "Mexican version of ricotta, made from the whey of other cheeses. Waste not, want not.",
        "description": "Mexican fresh whey cheese, creamy and mild, used in sweet and savory dishes throughout Mexico.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from making other cheese"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": "optional, increases yield"},
            {"item": "white vinegar", "quantity": "2", "unit": "tbsp", "prep_note": "or lime juice"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh, warm whey immediately after making cheese."},
            {"step": 2, "text": "Add milk if using for richer requesón."},
            {"step": 3, "text": "Heat slowly to 185-195°F, stirring occasionally."},
            {"step": 4, "text": "When foam and fine curds appear, add vinegar slowly."},
            {"step": 5, "text": "Curds will rise to surface."},
            {"step": 6, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 7, "text": "Skim curds into cheesecloth-lined strainer."},
            {"step": 8, "text": "Add salt and mix gently."},
            {"step": 9, "text": "Drain for 1 hour."},
            {"step": 10, "text": "Use fresh within 1 week."}
        ],
        "temperature": "185-195°F make",
        "notes": [
            "Never waste whey - it makes delicious requesón",
            "Traditional in Mexican breakfast tacos and pastries",
            "Sweeter and milder than Italian ricotta",
            "Can be used in enchiladas, quesadillas, or desserts"
        ],
        "tags": ["cheese", "traditional", "mexican", "whey", "ricotta-style", "fresh", "no-waste"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-anejo-mexican-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Añejo (Mexican Aged Cheese)",
        "category": "mains",
        "attribution": "Mexico / Traditional",
        "source_note": "Añejo means 'aged' - this is the Mexican answer to aged Parmesan-style cheeses.",
        "description": "Mexican aged cheese with a firm, crumbly texture and sharp, salty flavor, perfect for grating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "or part skim for firmer texture"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "paprika", "quantity": "2", "unit": "tbsp", "prep_note": "for coating rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/4-inch cubes."},
            {"step": 6, "text": "Stir gently while heating to 102°F over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are firm."},
            {"step": 8, "text": "Drain curds and salt heavily."},
            {"step": 9, "text": "Press at 50 lbs for 24 hours."},
            {"step": 10, "text": "Air dry for 1 week."},
            {"step": 11, "text": "Coat with paprika or chile powder."},
            {"step": 12, "text": "Age at 55°F for 3-6 months minimum."}
        ],
        "temperature": "90-102°F make, 55°F aging",
        "notes": [
            "The paprika or chile coating is traditional",
            "Becomes harder and sharper with age",
            "Essential for enchiladas and other Mexican classics",
            "Often called 'queso cotija añejo' or just 'añejo'"
        ],
        "tags": ["cheese", "traditional", "mexican", "aged", "hard", "grating", "paprika-coated"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-asadero-mexican-melting",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Asadero (Mexican Grilling Cheese)",
        "category": "mains",
        "attribution": "Northern Mexico / Traditional",
        "source_note": "Asadero means 'roaster' - this cheese is made for melting on the grill or in queso fundido.",
        "description": "Mexican stretched-curd cheese with exceptional melting properties, slightly tangy with a buttery flavor.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "3 hours",
        "cook_time": "6-12 hours acidification",
        "total_time": "1 day",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently while raising to 100°F."},
            {"step": 7, "text": "Drain curds and let acidify at room temperature 6-12 hours."},
            {"step": 8, "text": "Test stretch in 170°F water - should stretch smoothly."},
            {"step": 9, "text": "Stretch in hot water, adding salt as you work."},
            {"step": 10, "text": "Form into flat discs about 1/2 inch thick."},
            {"step": 11, "text": "Cool in cold water, then refrigerate."},
            {"step": 12, "text": "Use within 2 weeks."}
        ],
        "temperature": "90-100°F make, 170°F stretching",
        "notes": [
            "Similar to Oaxaca but shaped in flat discs for grilling",
            "Creates beautiful stringy melted cheese",
            "Essential for queso fundido and Northern Mexican grilling",
            "Sometimes braided like Oaxaca"
        ],
        "tags": ["cheese", "traditional", "mexican", "northern-mexico", "stretched-curd", "melting", "grilling"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # Homestead Cheesemaking Tips
    {
        "id": "cheesemaking-tip-homestead-basics",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Homestead Cheesemaking Basics",
        "category": "mains",
        "attribution": "Traditional Homestead Wisdom",
        "source_note": "For those making cheese from their own animals' milk. Different considerations than store-bought milk.",
        "description": "Essential guide for homesteaders making cheese from their own goats, cows, or sheep.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "homestead knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "ANIMAL HEALTH: Healthy animals produce the best milk. Mastitis, illness, or stress affects milk quality dramatically."},
            {"step": 2, "text": "CLEAN MILKING: Udder prep is essential. Wash and dry before milking. First squirts go to strip cup to check for issues."},
            {"step": 3, "text": "RAPID COOLING: Cool milk to 40°F within 1 hour of milking to prevent bacterial growth."},
            {"step": 4, "text": "FRESH IS BEST: Use milk within 24-48 hours for best cheese. Older milk can be used but produces inferior results."},
            {"step": 5, "text": "COLOSTRUM: Don't use colostrum (first 3-5 days after kidding/calving) for cheese - high antibodies prevent curdling."},
            {"step": 6, "text": "BREEDING SEASON: Buck/billy goat odor transfers to milk. Keep bucks separate during milking season."},
            {"step": 7, "text": "FEED AFFECTS FLAVOR: Strong feeds (onions, garlic, certain weeds) flavor the milk. Monitor what animals eat."},
            {"step": 8, "text": "SEASONAL VARIATION: Accept that spring milk differs from winter milk. Adjust recipes accordingly."},
            {"step": 9, "text": "SURPLUS MANAGEMENT: Cheese is how homesteaders preserved surplus milk before refrigeration."},
            {"step": 10, "text": "START SIMPLE: Begin with quick cheeses (chèvre, queso fresco) before attempting aged varieties."}
        ],
        "temperature": "Cool milk to 40°F within 1 hour",
        "notes": [
            "Homestead milk is often superior to commercial milk for cheesemaking",
            "Raw milk from your own healthy animals is the traditional standard",
            "Keeping detailed records helps identify what affects your cheese",
            "Each animal's milk is slightly different - you'll learn their quirks"
        ],
        "tags": ["cheese", "tips", "techniques", "homestead", "farm", "goats", "cows", "guide"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-goat-milk-specific",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Working with Goat Milk",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Goat milk behaves differently than cow milk. Understanding these differences leads to better goat cheese.",
        "description": "Specific techniques for making cheese from goat milk, addressing its unique properties.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "goat milk knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "NATURALLY HOMOGENIZED: Goat milk fat globules are smaller and stay suspended. Results in softer curds."},
            {"step": 2, "text": "LOWER RENNETING TEMP: Use 82-86°F for goat milk vs 86-90°F for cow. Higher temps = very soft curds."},
            {"step": 3, "text": "GENTLE HANDLING: Goat curds are more fragile. Cut larger, stir less, handle more gently."},
            {"step": 4, "text": "CALCIUM CHLORIDE: Very helpful for goat milk to firm up curds. Use 1/4 tsp per gallon."},
            {"step": 5, "text": "WHITE COLOR: Goat milk produces white cheese - no natural beta-carotene like cow milk."},
            {"step": 6, "text": "'GOATY' FLAVOR: Caused by capric, caprylic, and caproic fatty acids. More pronounced with age."},
            {"step": 7, "text": "REDUCING GOATINESS: Cool milk rapidly, keep bucks away, avoid stress during milking, age cheese less."},
            {"step": 8, "text": "EMBRACING GOATINESS: Many prized cheeses (chèvre, Roquefort) celebrate the distinctive goat flavor."},
            {"step": 9, "text": "BEST FOR: Soft cheeses, fresh cheeses, bloomy rinds. Can make hard cheese but requires adjustments."},
            {"step": 10, "text": "YIELD: Goat milk has less fat than cow milk, so yields are typically slightly lower."}
        ],
        "temperature": "82-86°F renneting (lower than cow)",
        "notes": [
            "French chèvre tradition is built on goat milk's unique properties",
            "Nigerian Dwarf goats produce the highest butterfat among dairy goats",
            "Seasonal breeding means most goat milk available spring-fall",
            "Many award-winning cheeses are made from goat milk"
        ],
        "tags": ["cheese", "tips", "techniques", "goat-milk", "chèvre", "guide", "homestead"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-sheep-milk-specific",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Working with Sheep Milk",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Sheep milk is the richest dairy milk and produces exceptional cheese. Special considerations apply.",
        "description": "Techniques for making cheese from sheep milk, leveraging its high fat and protein content.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "sheep milk knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "RICHEST MILK: 7-8% fat, 5-6% protein (cow: 3.5% fat, 3.3% protein). Produces rich, flavorful cheese."},
            {"step": 2, "text": "EXCELLENT YIELD: Expect 15-20% yield from sheep milk vs 10% from cow milk. More cheese per gallon."},
            {"step": 3, "text": "FAST COAGULATION: High protein means rapid, firm curd formation. May need less rennet."},
            {"step": 4, "text": "SEASONAL AVAILABILITY: Dairy sheep only lactate 4-6 months. Cheese traditionally made in lambing season."},
            {"step": 5, "text": "DISTINCTIVE FLAVOR: Lanolin-like, rich, complex. Some describe as 'sheepy' - this is desirable."},
            {"step": 6, "text": "FAMOUS SHEEP CHEESES: Roquefort, Pecorino, Manchego, Feta - many world-class cheeses are sheep."},
            {"step": 7, "text": "MIXED MILK: Traditional to blend sheep with goat or cow when sheep milk is scarce."},
            {"step": 8, "text": "TEMPERATURE SENSITIVITY: Sheep milk curds can become grainy if overheated. Watch temperatures carefully."},
            {"step": 9, "text": "LAMB RENNET: Traditional sheep cheese uses lamb rennet for authentic flavor development."},
            {"step": 10, "text": "WORTH THE EFFORT: Despite limited availability, sheep milk produces some of the world's finest cheeses."}
        ],
        "temperature": "Standard temps, but watch for overheating",
        "notes": [
            "Most sheep are milked only during lambing season",
            "East Friesian is the top dairy sheep breed",
            "Sheep milk is naturally homogenized like goat milk",
            "Rich milk means even aged hard cheeses remain moist and flavorful"
        ],
        "tags": ["cheese", "tips", "techniques", "sheep-milk", "pecorino", "guide", "homestead"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-scaling-recipes",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Scaling Recipes Up and Down",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Cheese recipes can be scaled, but not all elements scale linearly. Understanding this prevents failures.",
        "description": "Guide to properly scaling cheesemaking recipes for different batch sizes.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "scaling knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "CULTURES: Scale linearly with milk. 1/4 tsp per gallon works at any batch size."},
            {"step": 2, "text": "RENNET: Generally scales linearly, but very large batches may need slightly less per gallon."},
            {"step": 3, "text": "SALT: Scales linearly for direct salting. Brining time scales with cheese size (2 hrs/lb)."},
            {"step": 4, "text": "TIME: Heating and cooling take longer with larger volumes. Account for this."},
            {"step": 5, "text": "SET TIME: Usually the same regardless of batch size. Rennet works at similar speed."},
            {"step": 6, "text": "COOKING: Larger batches need more gradual heating to maintain even temperature."},
            {"step": 7, "text": "PRESSING: Larger cheeses need proportionally more pressing force and longer pressing time."},
            {"step": 8, "text": "AGING: Larger wheels age more slowly (less surface area to volume). Plan for longer aging."},
            {"step": 9, "text": "MINIMUM SIZE: Very small batches (under 1 gallon) can be tricky. Measurements become imprecise."},
            {"step": 10, "text": "MAXIMUM SIZE: Home equipment limits batch size. Heating 5+ gallons evenly is challenging."}
        ],
        "temperature": "N/A",
        "notes": [
            "Most home recipes are designed for 1-2 gallon batches",
            "Commercial cheese is made in 500+ gallon vats - different considerations apply",
            "Test scaled recipes with single batch before committing large quantities",
            "Write down your scaled measurements to ensure consistency"
        ],
        "tags": ["cheese", "tips", "techniques", "scaling", "batch-size", "guide", "practical"],
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
