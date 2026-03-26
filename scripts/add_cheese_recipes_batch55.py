#!/usr/bin/env python3
"""Add batch 55 - More traditional world cheeses and safety tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-safety-food-handling",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Food Safety Essentials",
        "category": "mains",
        "attribution": "Food safety best practices",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Cheesemaking creates conditions where both good and bad bacteria can thrive. Understanding food safety principles protects your family and ensures your cheese is delicious, not dangerous.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "sanitizer solution", "quantity": "", "unit": "", "prep_note": "no-rinse food safe"},
            {"item": "pH meter or strips", "quantity": "", "unit": "", "prep_note": "for monitoring acidification"},
            {"item": "thermometer", "quantity": "", "unit": "", "prep_note": "accurate to 1°F"},
            {"item": "food-grade containers", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "SANITATION: Clean all equipment with detergent, then sanitize with no-rinse sanitizer (Star San, iodophor, or bleach solution)."},
            {"step": 2, "text": "HANDS: Wash thoroughly before handling milk or curds. Wear food-safe gloves if preferred."},
            {"step": 3, "text": "MILK QUALITY: Use the freshest milk possible. Pasteurized is safer; raw milk requires extra care and testing."},
            {"step": 4, "text": "RAW MILK: If using raw, ensure source tests negative for pathogens. Aged raw milk cheeses (60+ days) are generally safe."},
            {"step": 5, "text": "ACIDIFICATION: Proper acidification (pH dropping below 5.3) inhibits pathogens. Monitor pH especially in soft, fresh cheeses."},
            {"step": 6, "text": "TEMPERATURE: Don't let milk or curds sit in the 'danger zone' (40-140°F) without active acidification."},
            {"step": 7, "text": "AGING: Hard, aged cheeses (over 60 days) develop conditions hostile to pathogens. Fresh cheeses need refrigeration."},
            {"step": 8, "text": "MOLD: White and blue molds you add are safe. Unknown molds (black, pink, slimy) on aged cheese should be cut off with margin."},
            {"step": 9, "text": "STORAGE: Fresh cheeses at 35-40°F. Aged cheeses at 50-55°F during aging, then refrigerate."},
            {"step": 10, "text": "BRINE: Replace brine periodically or keep it acidified. Old, contaminated brine can introduce problems."},
            {"step": 11, "text": "WHEN IN DOUBT: Throw it out. Cheese is worth making again; food poisoning is not worth the risk."},
            {"step": 12, "text": "VULNERABLE POPULATIONS: Pregnant women, young children, elderly, and immunocompromised should avoid raw milk and soft aged cheeses."}
        ],
        "temperature": "N/A",
        "notes": [
            "Listeria, Salmonella, and E. coli are the main concerns in cheesemaking",
            "Proper acid development and salt content are natural preservatives",
            "Surface molds protect aged cheeses - that's why they develop rinds",
            "Commercial cheesemakers follow HACCP (Hazard Analysis Critical Control Point) protocols",
            "Home cheesemakers should maintain similar vigilance"
        ],
        "tags": ["cheese", "technique", "tip", "safety", "sanitation", "food-handling"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-brick-cheese-wisconsin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brick Cheese (Wisconsin Original)",
        "category": "mains",
        "attribution": "1877 Wisconsin invention",
        "source_note": "Traditional Wisconsin cheesemaking",
        "description": "Invented in 1877 by John Jossi, a Swiss-American cheesemaker in Wisconsin, Brick is one of America's only truly original cheeses. Named for the bricks used to press it and its rectangular shape, it develops from mild to pungent with age.",
        "servings_yield": "2 lb block",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for surface ripening"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently while raising temperature to 100°F (38°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are moderately firm."},
            {"step": 7, "text": "Drain whey and pack curds into rectangular brick-shaped molds."},
            {"step": 8, "text": "Press using actual bricks or equivalent weight for 12-24 hours."},
            {"step": 9, "text": "Unmold and brine for 12-24 hours."},
            {"step": 10, "text": "Age at 55°F with 95% humidity."},
            {"step": 11, "text": "Wash with light brine every 2-3 days for first week."},
            {"step": 12, "text": "Continue aging and occasional washing for 2-4 weeks."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Young brick is mild - aged brick is pungent like Limburger",
            "Surface develops characteristic red-orange smear",
            "Traditional for Wisconsin-style 'beer cheese' preparations",
            "Jossi was trying to create a new cheese, not copy European styles",
            "Excellent melting cheese for burgers and sandwiches"
        ],
        "tags": ["cheese", "american", "wisconsin", "traditional", "washed-rind", "original"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-liederkranz-american-stinky",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Liederkranz (American Stinky Cheese)",
        "category": "mains",
        "attribution": "1882 New York invention",
        "source_note": "Traditional American washed-rind cheesemaking",
        "description": "Created in 1882 by Emil Frey in Monroe, NY, trying to recreate Limburger for German-American singing clubs (Liederkranz means 'wreath of songs'). He created something milder but still pungent - America's own stinky cheese.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "brine", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir very gently - Liederkranz needs softer curds than brick."},
            {"step": 6, "text": "Let curds settle, drain most whey."},
            {"step": 7, "text": "Ladle curds into small rectangular molds without pressing."},
            {"step": 8, "text": "Let drain naturally 24 hours, flipping several times."},
            {"step": 9, "text": "Salt surfaces or brief brine."},
            {"step": 10, "text": "Age at 55°F with 95% humidity."},
            {"step": 11, "text": "Wash with brine every 2-3 days for first 2 weeks."},
            {"step": 12, "text": "Continue aging 4-8 weeks until surface is sticky orange and interior is soft."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Production ceased in 1985 but has been revived by artisan makers",
            "Milder and softer than Limburger, closer to Livarot",
            "Named for singing societies of German immigrants",
            "The original culture was lost when Borden stopped production",
            "Interior should be soft and spreadable when ripe"
        ],
        "tags": ["cheese", "american", "traditional", "washed-rind", "stinky", "historical"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-teleme-california-portuguese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Teleme (California Portuguese Cheese)",
        "category": "mains",
        "attribution": "California Portuguese immigrant tradition",
        "source_note": "Traditional California artisan cheesemaking",
        "description": "Brought to California by Portuguese immigrants, Teleme is a creamy, tangy cheese that softens dramatically as it ages. Made in the San Joaquin Valley since the early 1900s, it's California's hidden gem.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "2-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "extra for tang"},
            {"item": "animal rennet", "quantity": "1/8", "unit": "tsp", "prep_note": "less rennet for softer curd"},
            {"item": "rice flour", "quantity": "1/4", "unit": "cup", "prep_note": "for dusting (traditional)"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add extra mesophilic culture for tangier cheese. Ripen 45-60 minutes."},
            {"step": 3, "text": "Add diluted rennet (use less than usual for softer curd)."},
            {"step": 4, "text": "Let set 45-60 minutes until soft curd forms."},
            {"step": 5, "text": "Cut curds into large 1-inch cubes - handle gently."},
            {"step": 6, "text": "Let curds rest 15 minutes, then stir very gently."},
            {"step": 7, "text": "Drain whey and ladle curds into molds without pressing."},
            {"step": 8, "text": "Let drain naturally 24 hours, flipping several times."},
            {"step": 9, "text": "Salt surfaces lightly."},
            {"step": 10, "text": "Dust with rice flour (traditional) to prevent sticking."},
            {"step": 11, "text": "Age at 50°F with high humidity for 2-8 weeks."},
            {"step": 12, "text": "Cheese becomes increasingly soft and tangy with age."}
        ],
        "temperature": "90°F (32°C) for make; 50°F (10°C) for aging",
        "notes": [
            "Rice flour coating is traditional California twist",
            "Named for Romanian 'telemea' brought by Portuguese via Brazil",
            "Should become quite soft and spreadable when well-aged",
            "Franklin Peluso family made it famous in Los Banos, CA",
            "Tangy, lactic flavor intensifies with age"
        ],
        "tags": ["cheese", "american", "california", "portuguese", "traditional", "soft"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-turunmaa-finnish-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Turunmaa (Finnish Aged Cheese)",
        "category": "mains",
        "attribution": "Finnish dairy tradition",
        "source_note": "Traditional Finnish cheesemaking",
        "description": "Finland's most popular aged cheese, Turunmaa is a mild, Swiss-style cheese with small eyes. Named for the Turku region, it's been made since the mid-20th century and represents Finland's adaptation of European cheesemaking.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium", "quantity": "1/16", "unit": "tsp", "prep_note": "for eyes"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and Propionibacterium. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes."},
            {"step": 5, "text": "Stir gently while raising temperature to 105°F (41°C) over 45 minutes."},
            {"step": 6, "text": "Continue stirring until curds are firm."},
            {"step": 7, "text": "Drain whey, wash curds briefly with warm water."},
            {"step": 8, "text": "Pack into wheel molds, press at moderate weight for 24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55°F for 2-3 weeks, then move to 65°F for eye development."},
            {"step": 11, "text": "Return to 55°F and age 2-6 months total."}
        ],
        "temperature": "90-105°F (32-41°C) for make; 55-65°F (13-18°C) for aging",
        "notes": [
            "Mild, nutty flavor - more approachable than Swiss Emmental",
            "Small irregular eyes from Propionibacterium",
            "Finland's dairy industry is relatively young compared to Alpine countries",
            "Popular everyday cheese in Finnish households",
            "Often eaten with Finnish rye bread"
        ],
        "tags": ["cheese", "finnish", "nordic", "traditional", "swiss-style", "eyes"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-vasterbotten-swedish-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Västerbotten (Swedish King of Cheese)",
        "category": "mains",
        "attribution": "1872 Swedish accident",
        "source_note": "Traditional Swedish cheesemaking",
        "description": "Sweden's most prestigious cheese was created by accident in 1872 when a dairy maid was distracted during cheesemaking. The resulting granular, intensely flavored cheese became a Swedish national treasure - the 'King of Cheese.'",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "14-24 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "high-quality Swedish-style"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-35 minutes."},
            {"step": 4, "text": "Cut curds into small 1/4-inch pieces."},
            {"step": 5, "text": "KEY STEP: Alternate stirring and resting - stir 5 min, rest 5 min, repeat."},
            {"step": 6, "text": "During stirring, slowly raise temperature to 115°F (46°C)."},
            {"step": 7, "text": "Continue alternating stir/rest for about 2 hours total."},
            {"step": 8, "text": "This unusual process creates the unique granular texture."},
            {"step": 9, "text": "Drain whey, pack into molds, press heavily for 24 hours."},
            {"step": 10, "text": "Brine for 48-72 hours."},
            {"step": 11, "text": "Age at 50-55°F with moderate humidity."},
            {"step": 12, "text": "Minimum 14 months aging, preferably 18-24 months."}
        ],
        "temperature": "95-115°F (35-46°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "The exact technique remains somewhat mysterious - only made in one dairy",
            "Protected origin: can only be made in Burträsk, Sweden",
            "Granular texture with tyrosine crystals like aged Parmesan",
            "Intense, complex flavor - slightly bitter, very savory",
            "Traditional in Swedish crayfish parties and midsummer celebrations"
        ],
        "tags": ["cheese", "swedish", "nordic", "traditional", "aged", "prestigious"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-herve-belgian-washed-rind",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Herve (Belgian Washed-Rind Classic)",
        "category": "mains",
        "attribution": "16th century Belgian tradition",
        "source_note": "Traditional Belgian washed-rind cheesemaking",
        "description": "From the village of Herve in eastern Belgium, this cube-shaped washed-rind cheese has been made since the 16th century. Like its cousin Limburger, it develops powerful aromas but has a supple, creamy interior.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "6-10 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "brine", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 40-50 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently for 15 minutes without raising temperature."},
            {"step": 6, "text": "Drain whey and ladle curds into cube-shaped molds."},
            {"step": 7, "text": "Let drain naturally 24 hours, flipping several times."},
            {"step": 8, "text": "Salt surfaces or brief brine."},
            {"step": 9, "text": "Age at 55°F with 95% humidity."},
            {"step": 10, "text": "Wash with brine every 2-3 days for first 2 weeks."},
            {"step": 11, "text": "Continue washing weekly for 6-10 weeks total aging."},
            {"step": 12, "text": "Rind should be sticky orange-red; interior creamy."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOP protected since 1996 - must be made in Herve region",
            "Comes in various ages: doux (mild), piquant (stronger), remoudou (very strong)",
            "The cube shape is distinctive - not round like most washed-rinds",
            "Pungent aroma belies the creamy, relatively mild interior",
            "Traditional with Belgian dark beer"
        ],
        "tags": ["cheese", "belgian", "traditional", "washed-rind", "stinky", "cube"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-kefalotyri-greek-hard",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kefalotyri (Greek Hard Cheese)",
        "category": "mains",
        "attribution": "Ancient Greek tradition",
        "source_note": "Traditional Greek cheesemaking",
        "description": "One of Greece's oldest cheeses, Kefalotyri has been made for thousands of years from sheep and goat milk. Hard, salty, and sharp, it's the traditional cheese for saganaki - fried until golden and flambéed with ouzo.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": ""},
            {"item": "raw goat's milk", "quantity": "0.5", "unit": "gallon", "prep_note": "or all sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep and goat milk (or use all sheep)."},
            {"step": 2, "text": "Heat to 95°F (35°C)."},
            {"step": 3, "text": "Add thermophilic culture, ripen 20-30 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 5, "text": "Cut curds into small 1/4-inch pieces."},
            {"step": 6, "text": "Stir and raise temperature to 118°F (48°C) over 30-40 minutes."},
            {"step": 7, "text": "Continue stirring until curds are very firm and dry."},
            {"step": 8, "text": "Drain whey and pack curds firmly into molds."},
            {"step": 9, "text": "Press heavily for 24 hours."},
            {"step": 10, "text": "Brine for 48-72 hours."},
            {"step": 11, "text": "Age at 50-55°F with 80% humidity."},
            {"step": 12, "text": "Minimum 3 months; up to 12 months for sharper flavor."}
        ],
        "temperature": "95-118°F (35-48°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Name means 'head cheese' from the shape of traditional wheels",
            "The classic cheese for saganaki (fried cheese)",
            "Hard enough for grating over pasta when well-aged",
            "Sheep milk gives rich, lanolin flavor; goat adds tang",
            "Similar to Italian Pecorino Romano in use"
        ],
        "tags": ["cheese", "greek", "traditional", "hard", "sheep", "aged", "ancient"],
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
