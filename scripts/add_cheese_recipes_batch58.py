#!/usr/bin/env python3
"""Add batch 58 - More traditional cheeses and final tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-edam-dutch-ball",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Edam (Dutch Ball Cheese)",
        "category": "mains",
        "attribution": "14th century North Holland tradition",
        "source_note": "Traditional Dutch cheesemaking",
        "description": "Named for the port town from which it was shipped, Edam has been made since the 14th century. Its distinctive spherical shape and low fat content made it ideal for long sea voyages - it was the world's most popular cheese in the 17th-18th centuries.",
        "servings_yield": "2 lb ball",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1-10 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "2% fat traditional"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "red cheese wax", "quantity": "", "unit": "", "prep_note": "traditional coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat part-skim milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest 5 minutes."},
            {"step": 6, "text": "Drain 1/3 of whey, replace with hot water (similar to Gouda)."},
            {"step": 7, "text": "Stir and raise temperature to 104°F (40°C) over 30 minutes."},
            {"step": 8, "text": "Continue stirring until curds are quite firm."},
            {"step": 9, "text": "Drain whey, pack curds into spherical molds (or use ball-shaped press)."},
            {"step": 10, "text": "Press heavily, rotating to achieve round shape."},
            {"step": 11, "text": "Brine for 12-24 hours."},
            {"step": 12, "text": "Air dry, wax with red wax. Age at 55°F: 1-4 months for mild, 10+ months for aged."}
        ],
        "temperature": "86-104°F (30-40°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Lower fat than Gouda - about 40% vs 48% fat in dry matter",
            "The red wax coating became its trademark",
            "Dutch East India Company shipped Edam around the world",
            "Its long-keeping properties made it invaluable for sea voyages",
            "Cannonballs were supposedly made from old, dried Edam rinds"
        ],
        "tags": ["cheese", "dutch", "traditional", "washed-curd", "ball", "waxed"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-mozzarella-bufala-campana",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mozzarella di Bufala Campana",
        "category": "mains",
        "attribution": "12th century Campanian water buffalo tradition",
        "source_note": "Traditional Italian pasta filata cheesemaking",
        "description": "The original and most prized mozzarella, made from the milk of Italian water buffalo in Campania since the 12th century. Its porcelain-white color, creamy texture, and delicate flavor are unmatched by cow's milk versions.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "Same day (fresh)",
        "ingredients": [
            {"item": "fresh water buffalo milk", "quantity": "2", "unit": "gallons", "prep_note": "or highest quality cow milk"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp", "prep_note": "optional, speeds acidification"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat buffalo milk to 90°F (32°C)."},
            {"step": 2, "text": "If using citric acid, add now for faster acidification."},
            {"step": 3, "text": "Add thermophilic culture, ripen 45-60 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Let curds rest under whey for 3-5 hours until pH reaches 5.2."},
            {"step": 7, "text": "Test: piece of curd should stretch smoothly in hot water."},
            {"step": 8, "text": "Cut acidified curd into strips."},
            {"step": 9, "text": "Heat water to 170-180°F (77-82°C)."},
            {"step": 10, "text": "Submerge curd strips, begin kneading when pliable."},
            {"step": 11, "text": "Stretch and fold until smooth, shiny, and elastic."},
            {"step": 12, "text": "Form into balls, drop into cold salted water."},
            {"step": 13, "text": "Store in brine or whey. Best eaten within 24-48 hours."}
        ],
        "temperature": "90°F (32°C) for curd; 170-180°F (77-82°C) for stretching",
        "notes": [
            "DOP protected since 1996 - authentic only from Campania and nearby regions",
            "Buffalo milk has twice the fat of cow milk, creating luxurious texture",
            "Should weep slightly when cut - sign of freshness",
            "True buffalo mozzarella is porcelain white, not yellow",
            "Must be eaten very fresh - quality degrades rapidly"
        ],
        "tags": ["cheese", "italian", "campania", "traditional", "pasta-filata", "buffalo", "fresh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-feta-greek-pdo",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Greek Feta (PDO Brine Cheese)",
        "category": "mains",
        "attribution": "Ancient Greek tradition (Homer era)",
        "source_note": "Traditional Greek brine cheesemaking",
        "description": "Greece's most famous cheese, feta has been made for at least 8,000 years - Homer describes its making in the Odyssey. Tangy, crumbly, and stored in brine, it's essential to Greek cuisine and now PDO protected.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "2-3 months aging in brine",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": "minimum 70%"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon", "prep_note": "maximum 30%"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "extra for tang"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep and goat milk (at least 70% sheep per PDO rules)."},
            {"step": 2, "text": "Heat to 86°F (30°C)."},
            {"step": 3, "text": "Add mesophilic culture - use extra for characteristic tang. Ripen 60 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Let curds rest 10 minutes, then stir very gently."},
            {"step": 7, "text": "Drain curds into cloth-lined molds."},
            {"step": 8, "text": "Let drain naturally 24 hours, flipping several times."},
            {"step": 9, "text": "Cut drained cheese into blocks."},
            {"step": 10, "text": "Dry salt blocks for 2-3 days."},
            {"step": 11, "text": "Prepare brine: 7-8% salt solution."},
            {"step": 12, "text": "Submerge blocks in brine, age refrigerated 2-3 months minimum."}
        ],
        "temperature": "86°F (30°C) for make; refrigerate in brine",
        "notes": [
            "PDO protected since 2002 - must be made in specific Greek regions",
            "The Cyclops Polyphemus makes cheese in Homer's Odyssey - possibly feta",
            "Must be at least 70% sheep milk; goat milk adds tang",
            "Crumbly texture comes from acid development and brine storage",
            "Can age in brine for months - flavor intensifies over time"
        ],
        "tags": ["cheese", "greek", "traditional", "ancient", "brine", "sheep", "PDO"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cheddar-english-original",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cheddar (English Original)",
        "category": "mains",
        "attribution": "12th century Somerset tradition",
        "source_note": "Traditional English cheesemaking",
        "description": "The world's most copied cheese originated in the village of Cheddar, Somerset, where it was aged in the famous Cheddar Gorge caves. The 'cheddaring' process of stacking and turning curds is what makes it unique.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "3-24 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from grass-fed cows"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "annatto", "quantity": "4", "unit": "drops", "prep_note": "optional for color"},
            {"item": "cheesecloth", "quantity": "", "unit": "", "prep_note": "for bandaging"},
            {"item": "lard", "quantity": "2", "unit": "tbsp", "prep_note": "for sealing cloth"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto if desired."},
            {"step": 2, "text": "Add mesophilic culture, ripen 45-60 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently and raise temperature to 102°F (39°C) over 30 minutes."},
            {"step": 6, "text": "When curds are firm, drain whey."},
            {"step": 7, "text": "CHEDDARING: Cut curd mass into slabs, stack 2-3 high."},
            {"step": 8, "text": "Flip and restack every 15 minutes for 2 hours. Slabs become smooth and 'chicken breast' texture."},
            {"step": 9, "text": "Mill cheddared curds into thumb-sized pieces."},
            {"step": 10, "text": "Salt milled curds thoroughly."},
            {"step": 11, "text": "Pack into molds, press heavily for 24 hours."},
            {"step": 12, "text": "Bandage with lard-sealed cheesecloth."},
            {"step": 13, "text": "Age at 55°F: mild 3-6 mo, medium 6-12 mo, sharp 12-24 mo, extra sharp 24+ mo."}
        ],
        "temperature": "86-102°F (30-39°C) for make; 55°F (13°C) for aging",
        "notes": [
            "West Country Farmhouse Cheddar has PDO protection",
            "The cheddaring step is unique to this cheese family",
            "Traditional cloth-binding allows cheese to breathe and develop complex flavors",
            "Cheddar Gorge caves provided ideal natural aging conditions",
            "King Henry II bought 10,420 lbs of cheddar in 1170"
        ],
        "tags": ["cheese", "english", "somerset", "traditional", "cheddared", "aged", "cloth-bound"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-raclette-swiss-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Raclette (Swiss Alpine Melting Cheese)",
        "category": "mains",
        "attribution": "Medieval Valais tradition",
        "source_note": "Traditional Swiss alpine cheesemaking",
        "description": "Named for the French 'racler' (to scrape), Raclette has warmed Swiss mountain dwellers since at least the 12th century. The half-wheel is traditionally held near fire, and the melted surface scraped onto potatoes.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "alpine pasture ideal"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "gallon", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 5, "text": "Stir and raise temperature to 104°F (40°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are firm but still moist."},
            {"step": 7, "text": "Drain whey and pack curds into wheel molds."},
            {"step": 8, "text": "Press at moderate weight for 24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55°F with 95% humidity."},
            {"step": 11, "text": "Wash with brine every few days to develop light brown rind."},
            {"step": 12, "text": "Age 3-6 months until aromatic and melts smoothly."}
        ],
        "temperature": "90-104°F (32-40°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOP protected from Valais, Switzerland",
            "Traditional serving: half-wheel by fire, scrape melted layer onto plate",
            "Modern raclette grills melt individual slices",
            "Served with boiled potatoes, pickled onions, cornichons",
            "The aroma when melting is distinctively pungent and appealing"
        ],
        "tags": ["cheese", "swiss", "alpine", "traditional", "melting", "washed-rind"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-grana-padano-po-valley",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Grana Padano (Po Valley Hard Cheese)",
        "category": "mains",
        "attribution": "12th century Cistercian monastery tradition",
        "source_note": "Traditional Italian grana cheesemaking",
        "description": "Created by Cistercian monks at Chiaravalle Abbey around 1135, Grana Padano predates Parmigiano-Reggiano. Made across the Po Valley, it's slightly milder and made year-round, unlike its seasonal cousin.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "9-24 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "part-skim, from two milkings"},
            {"item": "natural whey starter", "quantity": "1/2", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "calf rennet"},
            {"item": "cheese salt", "quantity": "", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine part-skim evening milk with morning milk (or partially skim whole milk)."},
            {"step": 2, "text": "Heat to 90°F (32°C) in copper cauldron."},
            {"step": 3, "text": "Add natural whey starter, ripen briefly."},
            {"step": 4, "text": "Add calf rennet, let set 10-15 minutes."},
            {"step": 5, "text": "Break curd very finely using 'spino' tool."},
            {"step": 6, "text": "Raise temperature to 127°F (53°C) while stirring."},
            {"step": 7, "text": "Let curds settle to bottom, forming single mass."},
            {"step": 8, "text": "Lift curd mass in cloth, divide, place in molds."},
            {"step": 9, "text": "Press with weights, flipping regularly for 2 days."},
            {"step": 10, "text": "Brine for 14-30 days."},
            {"step": 11, "text": "Age on wooden shelves at 60-65°F."},
            {"step": 12, "text": "Minimum 9 months; 18-24 months for Riserva."}
        ],
        "temperature": "90-127°F (32-53°C) for make; 60-65°F (15-18°C) for aging",
        "notes": [
            "DOP protected - made across Po Valley (larger area than Parmigiano)",
            "Slightly milder than Parmigiano-Reggiano",
            "Lysozyme (egg-based preservative) is allowed, unlike in Parmigiano",
            "Monks created it to preserve surplus milk",
            "The granular texture gives it the name 'grana'"
        ],
        "tags": ["cheese", "italian", "traditional", "hard", "grana", "aged", "monastery"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-sbrinz-swiss-ancient-grana",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sbrinz (Swiss Ancient Hard Cheese)",
        "category": "mains",
        "attribution": "Roman-era Central Swiss tradition",
        "source_note": "Traditional Swiss hard cheesemaking",
        "description": "One of Europe's oldest cheeses, Sbrinz may date to Roman times when it was traded across the Alps. This extremely hard Swiss cheese is traditionally shaved into thin curls called 'Möckli' and can age for several years.",
        "servings_yield": "3-4 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "18-36 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons", "prep_note": "from Central Swiss cows"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 15-20 minutes."},
            {"step": 3, "text": "Add rennet, let set 25-30 minutes."},
            {"step": 4, "text": "Cut curds extremely fine - smaller than rice grains."},
            {"step": 5, "text": "Stir continuously while raising temperature to 133°F (56°C) - very high."},
            {"step": 6, "text": "Continue stirring for 45-60 minutes until curds are very dry."},
            {"step": 7, "text": "Press curds under whey briefly."},
            {"step": 8, "text": "Transfer to molds, press very heavily for 24 hours."},
            {"step": 9, "text": "Brine for 3-4 weeks."},
            {"step": 10, "text": "Age standing on edge (not flat) at 60°F with low humidity."},
            {"step": 11, "text": "Turn regularly. Minimum 18 months; traditionally 36 months or more."}
        ],
        "temperature": "90-133°F (32-56°C) for make; 60°F (15°C) for aging",
        "notes": [
            "AOP protected - made only in Central Switzerland",
            "May be ancestor to Italian grana cheeses - traded over Alps for centuries",
            "Extremely hard - eaten in thin shavings (Möckli), not grated",
            "Lower moisture than any other Swiss cheese",
            "The high cooking temperature creates dense, granular texture"
        ],
        "tags": ["cheese", "swiss", "traditional", "ancient", "hard", "aged", "grana"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-paneer-indian-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Paneer (Indian Fresh Cheese)",
        "category": "mains",
        "attribution": "Ancient South Asian tradition",
        "source_note": "Traditional Indian acid-set cheesemaking",
        "description": "The cheese of the Indian subcontinent, Paneer is a simple acid-set cheese that doesn't melt - perfect for curries. Made across South Asia for centuries, its firm texture holds up beautifully in cooking.",
        "servings_yield": "1 lb cheese",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "total_time": "2-3 hours including pressing",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "full fat essential"},
            {"item": "lemon juice", "quantity": "1/4", "unit": "cup", "prep_note": "or white vinegar"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185-190°F (85-88°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat."},
            {"step": 3, "text": "Add lemon juice slowly while stirring gently."},
            {"step": 4, "text": "Curds will separate from greenish whey - add more acid if needed."},
            {"step": 5, "text": "Let sit 5-10 minutes."},
            {"step": 6, "text": "Line colander with cheesecloth, pour in curds and whey."},
            {"step": 7, "text": "Rinse curds with cold water to stop cooking and remove acid taste."},
            {"step": 8, "text": "Gather cloth, squeeze out excess whey."},
            {"step": 9, "text": "Add salt if using, knead briefly to distribute."},
            {"step": 10, "text": "Form into block, wrap in cloth."},
            {"step": 11, "text": "Press under heavy weight (cast iron pan, books) for 1-2 hours."},
            {"step": 12, "text": "Refrigerate. Use within 1 week."}
        ],
        "temperature": "185-190°F (85-88°C)",
        "notes": [
            "Does not melt - perfect for frying and adding to curries",
            "Full-fat milk makes creamier, more tender paneer",
            "Pressing time determines firmness - less for soft, more for firm",
            "Essential for saag paneer, paneer tikka, palak paneer",
            "Can be made in 30 minutes - the fastest homemade cheese"
        ],
        "tags": ["cheese", "indian", "traditional", "fresh", "acid-set", "non-melting", "quick"],
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
