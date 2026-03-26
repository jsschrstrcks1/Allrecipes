#!/usr/bin/env python3
"""Add batch 50 - British, Dutch, and Nordic traditional cheeses plus more tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-cloth-bound-vs-waxed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Cloth-Bound vs Waxed Rinds",
        "category": "mains",
        "attribution": "Traditional rind treatment wisdom",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "The rind treatment you choose fundamentally affects how cheese ages and develops flavor. Understanding the difference between cloth-binding and waxing helps you choose the right method for your cheese.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "cheesecloth or muslin", "quantity": "", "unit": "", "prep_note": "for cloth-binding"},
            {"item": "lard or butter", "quantity": "", "unit": "", "prep_note": "for sealing cloth"},
            {"item": "cheese wax", "quantity": "", "unit": "", "prep_note": "for waxed rinds"},
            {"item": "bandaging tools", "quantity": "", "unit": "", "prep_note": "cloth, paste, brushes"}
        ],
        "instructions": [
            {"step": 1, "text": "CLOTH-BINDING: Traditional British method. Cheese breathes, loses moisture, develops complex earthy flavors from ambient molds."},
            {"step": 2, "text": "Best for: hard aged cheeses like cheddar, Lancashire, Cheshire that benefit from long aging and flavor development."},
            {"step": 3, "text": "Method: wrap warm cheese in muslin, seal with lard or butter, maintain at 55°F with 85% humidity."},
            {"step": 4, "text": "Cloth-bound cheese requires more attention - regular turning, brushing away mold, checking for problems."},
            {"step": 5, "text": "Expect 10-15% weight loss during aging as moisture evaporates through cloth."},
            {"step": 6, "text": "WAXING: Seals cheese completely. Preserves moisture, creates milder, more consistent results."},
            {"step": 7, "text": "Best for: semi-hard cheeses, cheeses with shorter aging, when you want to preserve moisture and prevent mold."},
            {"step": 8, "text": "Method: dry cheese surface completely, heat wax to 240°F, dip or brush on multiple thin coats."},
            {"step": 9, "text": "Red wax is traditional for Gouda/Edam; black for aged versions; clear for display; any color works."},
            {"step": 10, "text": "Waxed cheese is lower maintenance - just turn occasionally, no brushing needed."},
            {"step": 11, "text": "VACUUM SEALING: Modern alternative. Completely anaerobic, prevents all rind development."},
            {"step": 12, "text": "Choose based on desired result: cloth for complex/traditional, wax for mild/consistent, vacuum for convenience."}
        ],
        "temperature": "N/A",
        "notes": [
            "Same cheddar recipe tastes completely different cloth-bound vs waxed",
            "Cloth-bound develops 'terroir' - picking up cave flavors and wild molds",
            "Waxed cheese has brighter, cleaner flavors but less complexity",
            "You can natural-rind (no treatment) - requires careful humidity control",
            "Some makers bandage with lard-soaked cloth then wax over for hybrid approach"
        ],
        "tags": ["cheese", "technique", "tip", "rind", "aging", "traditional"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cheshire-oldest-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cheshire (England's Oldest Cheese)",
        "category": "mains",
        "attribution": "Roman-era British tradition",
        "source_note": "Traditional English territorial cheesemaking",
        "description": "Mentioned in the Domesday Book (1086) and possibly made since Roman times, Cheshire may be England's oldest named cheese. The salty soil of the Cheshire plains gives milk a unique mineral character that defines this crumbly, tangy cheese.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-9 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from pastures on salty Cheshire plains traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "traditionally higher salt content"},
            {"item": "annatto", "quantity": "4", "unit": "drops", "prep_note": "for red Cheshire, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add annatto now if making 'red' Cheshire (orange-colored version)."},
            {"step": 3, "text": "Add mesophilic culture, ripen 45-60 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 45-60 minutes for relatively soft curd."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Let curds heal 5-10 minutes."},
            {"step": 7, "text": "Slowly stir and raise temperature to 90°F (32°C) over 30 minutes."},
            {"step": 8, "text": "Continue stirring until curds are firm but still moist."},
            {"step": 9, "text": "Drain whey, pile curds, cut and stack (mill) like cheddar but less aggressively."},
            {"step": 10, "text": "Salt curds generously - Cheshire is saltier than most English cheeses."},
            {"step": 11, "text": "Pack salted curds into molds, press at moderate weight overnight."},
            {"step": 12, "text": "Bandage with cloth and lard, or wax."},
            {"step": 13, "text": "Age at 55°F with 80-85% humidity: 2 months for young, up to 9 months for mature."}
        ],
        "temperature": "86-90°F (30-32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Three types: white, red (annatto colored), and blue (accidental blue mold)",
            "Salty Cheshire soil gives milk natural mineral salinity",
            "Texture is crumbly and moist, unlike waxy cheddar",
            "Blue Cheshire occurs naturally and is highly prized",
            "Was England's most popular cheese until 19th century"
        ],
        "tags": ["cheese", "english", "traditional", "territorial", "ancient", "crumbly"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gloucester-single-double",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gloucester (Single and Double)",
        "category": "mains",
        "attribution": "Medieval Gloucestershire tradition",
        "source_note": "Traditional English territorial cheesemaking",
        "description": "From the lush Severn Vale, Gloucester cheese comes in two traditional forms: Single (thin, young, mild) and Double (thick, aged, fuller). Made from the milk of rare Gloucester cattle, it was once so valuable it was rolled down Cooper's Hill annually.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Gloucester cattle traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""},
            {"item": "annatto", "quantity": "4", "unit": "drops", "prep_note": "for traditional orange color"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add annatto for traditional orange-gold color."},
            {"step": 3, "text": "Add mesophilic culture, ripen 45 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 40-50 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently and raise temperature to 95°F (35°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are moderately firm."},
            {"step": 8, "text": "Drain whey."},
            {"step": 9, "text": "For Single Gloucester: pack curds directly into thin molds (2-3 inches high)."},
            {"step": 10, "text": "For Double Gloucester: mill curds, salt, pack into thick molds (4-5 inches high)."},
            {"step": 11, "text": "Press: light for Single, heavy for Double."},
            {"step": 12, "text": "Bandage with cloth and lard."},
            {"step": 13, "text": "Single: age 2-3 months. Double: age 4-6 months or longer."}
        ],
        "temperature": "86-95°F (30-35°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Single Gloucester was traditionally made from skimmed milk for workers",
            "Double Gloucester was the richer, whole-milk version for sale",
            "PDO protected since 1996 - must use milk from Gloucestershire",
            "The Cooper's Hill cheese-rolling tradition uses Double Gloucester",
            "Gloucester cattle are a rare heritage breed critical to authentic production"
        ],
        "tags": ["cheese", "english", "traditional", "territorial", "gloucester"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-red-leicester-annatto",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Red Leicester (Annatto-Colored Cheddar)",
        "category": "mains",
        "attribution": "17th century Leicestershire tradition",
        "source_note": "Traditional English territorial cheesemaking",
        "description": "A Leicester variation of the cheddar family, Red Leicester gets its distinctive orange-red color from annatto. Developed in the 17th century partly to differentiate it from other cheeses in the market, it has a mellow, nutty flavor.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "3-9 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto", "quantity": "8", "unit": "drops", "prep_note": "for characteristic deep orange-red color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add annatto - use more than for Gloucester to achieve deep red-orange color."},
            {"step": 3, "text": "Add mesophilic culture, ripen 45 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir and raise temperature to 100°F (38°C) over 40 minutes."},
            {"step": 7, "text": "Continue stirring until curds are quite firm."},
            {"step": 8, "text": "Drain whey, pile curds, let acidify 15-20 minutes."},
            {"step": 9, "text": "Mill curds, salt thoroughly."},
            {"step": 10, "text": "Pack into molds, press heavily overnight."},
            {"step": 11, "text": "Bandage with cloth or wax."},
            {"step": 12, "text": "Age at 55°F with 85% humidity for 3-9 months."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 55°F (13°C) for aging",
        "notes": [
            "The vivid color originally helped identify Leicester cheese at market",
            "Annatto is a natural plant-based coloring from achiote seeds",
            "Texture is slightly more open and moist than cheddar",
            "Matures faster than cheddar - nice at 3-6 months",
            "Melts beautifully - excellent for Welsh rarebit"
        ],
        "tags": ["cheese", "english", "traditional", "territorial", "annatto", "colored"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-caerphilly-welsh-miners",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caerphilly (Welsh Miners' Cheese)",
        "category": "mains",
        "attribution": "19th century Welsh mining tradition",
        "source_note": "Traditional Welsh cheesemaking",
        "description": "Developed for Welsh coal miners who needed a cheese that wouldn't dry out in dusty mine conditions, Caerphilly is young, moist, and crumbly with a fresh, lemony tang. It could be made quickly and eaten within days.",
        "servings_yield": "1.5 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "extra culture for tang"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture - use slightly more than usual for tang."},
            {"step": 3, "text": "Ripen for 45-60 minutes until slightly acidic."},
            {"step": 4, "text": "Add diluted rennet, let set 40-45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently for 15 minutes without raising temperature."},
            {"step": 7, "text": "Raise temperature slowly to 95°F (35°C) over 30 minutes."},
            {"step": 8, "text": "When curds are moderately firm, drain whey."},
            {"step": 9, "text": "Pile curds and let drain further for 15 minutes."},
            {"step": 10, "text": "Break up curds gently, salt evenly."},
            {"step": 11, "text": "Pack into molds, press at moderate weight for 24 hours."},
            {"step": 12, "text": "Brine for 12-24 hours or dry salt."},
            {"step": 13, "text": "Age at 55°F with 90% humidity for 2-8 weeks."}
        ],
        "temperature": "90-95°F (32-35°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Traditional Caerphilly is very young - 2-3 weeks",
            "Modern artisan versions age longer, developing complex flavors",
            "Should be moist with fresh, slightly sour buttermilk flavor",
            "Welsh and Somerset producers both make traditional versions",
            "The high moisture content kept miners refreshed in dusty conditions"
        ],
        "tags": ["cheese", "welsh", "traditional", "fresh", "crumbly", "quick"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-leyden-dutch-cumin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Leyden (Dutch Cumin-Seed Cheese)",
        "category": "mains",
        "attribution": "Medieval Dutch tradition",
        "source_note": "Traditional Dutch spiced cheesemaking",
        "description": "A traditional Dutch cheese flavored with cumin seeds (and sometimes caraway), Leyden has been made in the Netherlands since at least the 16th century. The city's crossed keys symbol is stamped into every wheel.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "skimmed cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "traditionally partially skimmed"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cumin seeds", "quantity": "2", "unit": "tbsp", "prep_note": "whole or lightly crushed"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tbsp", "prep_note": "optional, traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine whole and skimmed milk (or use buttermilk-cultured milk traditionally)."},
            {"step": 2, "text": "Heat to 86°F (30°C)."},
            {"step": 3, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 45 minutes."},
            {"step": 5, "text": "Cut curds into small 1/4-inch cubes."},
            {"step": 6, "text": "Stir and raise temperature to 100°F (38°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are quite firm."},
            {"step": 8, "text": "Drain most whey."},
            {"step": 9, "text": "Add cumin seeds (and caraway if using) to curds, mix thoroughly."},
            {"step": 10, "text": "Salt curds and mix again."},
            {"step": 11, "text": "Pack into wheel molds with crossed-keys stamp if available."},
            {"step": 12, "text": "Press heavily for 24 hours."},
            {"step": 13, "text": "Brine for 24-48 hours."},
            {"step": 14, "text": "Age at 55°F with moderate humidity for 3-12 months."}
        ],
        "temperature": "86-100°F (30-38°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Traditional Leyden used buttermilk-cultured milk for tangier flavor",
            "The city of Leyden's crossed-keys arms are stamped on authentic wheels",
            "Cumin-Gouda is a similar modern cheese",
            "Aged Leyden develops rich, savory, almost meaty flavors",
            "Traditionally made from partially skimmed milk"
        ],
        "tags": ["cheese", "dutch", "traditional", "spiced", "cumin", "aged"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-jarlsberg-norwegian-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jarlsberg (Norwegian Swiss-Style)",
        "category": "mains",
        "attribution": "19th century Norwegian tradition, modernized 1956",
        "source_note": "Traditional Norwegian cheesemaking",
        "description": "Norway's most famous cheese, Jarlsberg combines traditional Norwegian cheesemaking with Swiss-style eye development. Though the modern recipe was perfected in 1956, it's based on a 19th-century recipe from the Jarlsberg estate.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "3-15 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "pasteurized for consistency"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium freudenreichii", "quantity": "1/16", "unit": "tsp", "prep_note": "for eye development"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacterium. Ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes."},
            {"step": 5, "text": "Stir gently for 15 minutes."},
            {"step": 6, "text": "Raise temperature gradually to 102°F (39°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are firm."},
            {"step": 8, "text": "Drain most whey, wash curds briefly with warm water to reduce acidity."},
            {"step": 9, "text": "Pack curds into large wheel molds."},
            {"step": 10, "text": "Press at moderate weight for 24 hours."},
            {"step": 11, "text": "Brine for 48-72 hours."},
            {"step": 12, "text": "Age at 55°F for 2-3 weeks."},
            {"step": 13, "text": "Move to warmer room (65-70°F) for 4-6 weeks for eye development."},
            {"step": 14, "text": "Return to cool aging for 3-15 months total."}
        ],
        "temperature": "90-102°F (32-39°C) for make; 55-70°F (13-21°C) for aging",
        "notes": [
            "The secret 'TINE' Propionibacterium culture creates the distinctive sweet, nutty flavor",
            "Eyes develop during the warm-aging phase as bacteria produce CO2",
            "Milder and sweeter than Swiss Emmentaler",
            "Authentic Jarlsberg is made only in Norway",
            "Excellent melting cheese for sandwiches and fondue"
        ],
        "tags": ["cheese", "norwegian", "traditional", "swiss-style", "eyes", "melting"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gamle-ole-danish-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gamle Ole (Danish Aged Cheese)",
        "category": "mains",
        "attribution": "Traditional Danish farmhouse tradition",
        "source_note": "Traditional Danish cheesemaking",
        "description": "Denmark's answer to aged Gouda, Gamle Ole (Old Ole) is a firm, crystalline cheese aged for extended periods. The name comes from the tradition of naming wheels after the cheesemaker who made them.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "6-36 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "high quality Danish dairy"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 35-45 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes."},
            {"step": 5, "text": "Stir gently while raising temperature to 104°F (40°C) over 45 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very firm."},
            {"step": 7, "text": "Drain most whey, wash curds with warm water to reduce acidity."},
            {"step": 8, "text": "Pack curds tightly into wheel molds."},
            {"step": 9, "text": "Press heavily for 24 hours, flipping several times."},
            {"step": 10, "text": "Brine for 48-72 hours."},
            {"step": 11, "text": "Wax or develop natural rind."},
            {"step": 12, "text": "Age at 50-55°F with moderate humidity."},
            {"step": 13, "text": "Turn weekly. Age minimum 6 months, ideally 18-36 months for 'Gamle' designation."}
        ],
        "temperature": "86-104°F (30-40°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "'Gamle' means 'old' in Danish - refers to extended aging",
            "Develops tyrosine crystals like aged Gouda and Parmigiano",
            "Flavor is sweet, caramelized, with butterscotch notes when well-aged",
            "Danish dairy tradition dates back to medieval monastic production",
            "Modern versions age 2-3 years for maximum complexity"
        ],
        "tags": ["cheese", "danish", "traditional", "aged", "crystalline"],
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
