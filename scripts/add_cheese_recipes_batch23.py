#!/usr/bin/env python3
"""Add batch 23 of traditional cheese recipes - Middle Eastern, Asian, and lesser-known European."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-kashkaval-balkan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kashkaval (Balkan)",
        "category": "mains",
        "attribution": "Balkans/Eastern Mediterranean, Ancient",
        "source_note": "Kashkaval (also Kaşar, Kasseri, Kachkawali) is a family of stretched-curd cheeses made throughout the Balkans, Turkey, and Eastern Mediterranean since ancient times. The name may derive from the Italian 'caciocavallo.'",
        "description": "Traditional Balkan pasta filata cheese, similar to provolone but with regional variations across Bulgaria, Turkey, Greece, and beyond.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "or mixed sheep/cow"},
            {"item": "cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or use all sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 104°F over 20 minutes while stirring."},
            {"step": 6, "text": "Drain curds and let mat at 100°F for 2-3 hours until pH reaches 5.2-5.3."},
            {"step": 7, "text": "Test for stretch: place a small piece in 170°F water - it should stretch smoothly."},
            {"step": 8, "text": "Cut matted curd into strips. Heat water to 170°F with salt."},
            {"step": 9, "text": "Stretch curd in hot water until smooth and elastic, folding repeatedly."},
            {"step": 10, "text": "Form into wheel or brick shape."},
            {"step": 11, "text": "Brine for 12-24 hours."},
            {"step": 12, "text": "Age at 55°F and 85% humidity for 2-6 months."}
        ],
        "temperature": "95°F start, 104°F cook, 170°F stretch, 55°F aging",
        "notes": [
            "Kashkaval is the generic Balkan name; Kaşar is Turkish, Kasseri is Greek",
            "Young Kashkaval is mild and sliceable; aged becomes sharp and granular",
            "Excellent melting cheese used in traditional Balkan dishes",
            "Often smoked in some regions"
        ],
        "tags": ["cheese", "traditional", "balkan", "turkish", "greek", "kashkaval", "pasta-filata", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sirene-bulgarian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bulgarian Sirene (White Brine Cheese)",
        "category": "mains",
        "attribution": "Bulgaria, Ancient",
        "source_note": "Sirene is the traditional Bulgarian white brine cheese, similar to feta but typically made from cow or mixed milk. It's been a staple of Bulgarian cuisine for thousands of years.",
        "description": "Traditional Bulgarian brine cheese, tangy and crumbly - the foundation of Bulgarian cuisine from shopska salad to banitsa.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "2 hours",
        "cook_time": "2-3 weeks brining/aging",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or mixed cow/sheep"},
            {"item": "sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional, for richer flavor"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 86°F."},
            {"step": 6, "text": "Let curds settle, then drain most whey."},
            {"step": 7, "text": "Ladle curds into molds or form into a block. Press lightly for 4-6 hours."},
            {"step": 8, "text": "Cut the drained cheese into 3-4 inch blocks."},
            {"step": 9, "text": "Make brine: dissolve salt in water (about 10% solution)."},
            {"step": 10, "text": "Place cheese blocks in brine and refrigerate."},
            {"step": 11, "text": "Age in brine for 2-3 weeks minimum. Can store in brine for months."}
        ],
        "temperature": "86°F make, refrigerator aging",
        "notes": [
            "Sirene is traditionally made from cow's milk in Bulgaria, unlike Greek feta",
            "Essential for shopska salad, banitsa (cheese pastry), and many Bulgarian dishes",
            "Store submerged in brine - it will keep for months refrigerated",
            "The longer it ages in brine, the tangier and firmer it becomes"
        ],
        "tags": ["cheese", "traditional", "bulgarian", "brine-cheese", "sirene", "white-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-graviera-greek",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Greek Graviera",
        "category": "mains",
        "attribution": "Greece (Crete, Naxos), Ancient",
        "source_note": "Graviera is Greece's second most popular cheese after feta. The name derives from Gruyère, though Greek graviera developed independently and varies by region - Cretan graviera uses sheep's milk, Naxos uses cow's milk.",
        "description": "Greece's beloved hard cheese with nutty, sweet flavors - the island varieties are considered finest.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-8 months aging",
        "total_time": "3-8 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "for Cretan style"},
            {"item": "goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional, for Cretan style"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 93°F. Add calcium chloride if using pasteurized."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (small). Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 122°F over 40 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at 122°F for 30 minutes until curds are firm."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 15 lbs for 30 minutes. Flip and press at 30 lbs for 6 hours."},
            {"step": 9, "text": "Flip and press at 50 lbs for 24 hours."},
            {"step": 10, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 11, "text": "Air dry for 3-5 days."},
            {"step": 12, "text": "Age at 55°F and 85% humidity for 3-8 months, turning weekly."}
        ],
        "temperature": "93°F start, 122°F cook, 55°F aging",
        "notes": [
            "Cretan Graviera (sheep/goat milk) is considered the finest",
            "Naxos Graviera uses cow's milk and is milder",
            "The high cooking temperature creates the firm, smooth texture",
            "Excellent table cheese and for saganaki (pan-fried cheese)"
        ],
        "tags": ["cheese", "traditional", "greek", "cretan", "graviera", "hard-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tulum-turkish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Turkish Tulum (Goatskin Cheese)",
        "category": "mains",
        "attribution": "Turkey (Anatolia), Ancient",
        "source_note": "Tulum peyniri has been made in Anatolia for millennia. 'Tulum' means goatskin - the cheese was traditionally aged in goatskin bags, which gave it a distinctive flavor and allowed shepherds to transport it.",
        "description": "Ancient Turkish cheese traditionally aged in goatskin bags, with a distinctive sharp, crumbly character.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "2 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw goat's milk", "quantity": "1", "unit": "gallon", "prep_note": "or sheep's milk"},
            {"item": "sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional blend"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1 1/2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1 hour until firm curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 90°F."},
            {"step": 6, "text": "Drain whey thoroughly. Place curds in cloth and hang to drain for 24 hours."},
            {"step": 7, "text": "Crumble the drained curd and mix with salt."},
            {"step": 8, "text": "Traditional method: Pack salted curds tightly into a prepared goatskin bag."},
            {"step": 9, "text": "Modern alternative: Pack into a ceramic crock or vacuum-seal in portions."},
            {"step": 10, "text": "Age at cool room temperature (55-65°F) for 3-6 months."},
            {"step": 11, "text": "The cheese should develop a crumbly, sharp character."}
        ],
        "temperature": "90°F make, 55-65°F aging",
        "notes": [
            "Traditional tulum is aged in a goatskin (tulum) which imparts distinctive flavor",
            "Modern versions use cloth or ceramic containers",
            "The texture is crumbly like aged feta, with a sharp, complex flavor",
            "Excellent crumbled over salads or in Turkish gözleme"
        ],
        "tags": ["cheese", "traditional", "turkish", "anatolian", "goat-cheese", "tulum", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-akkawi-levantine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Akkawi (Levantine)",
        "category": "mains",
        "attribution": "Levant (Named for Acre/Akka), Ancient",
        "source_note": "Akkawi cheese is named after the city of Acre (Akko/Akka) in modern-day Israel, though it's been made throughout the Levant for centuries. It's a mild white brine cheese, essential for knafeh and other Middle Eastern sweets.",
        "description": "Mild Levantine brine cheese named after the city of Acre, essential for authentic knafeh and Middle Eastern cuisine.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "2 hours",
        "cook_time": "1-2 weeks brining",
        "total_time": "1-2 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/16", "unit": "tsp", "prep_note": "small amount for mild flavor"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture (small amount for mild cheese), stir, and ripen for 15 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 15 minutes at 90°F."},
            {"step": 6, "text": "Drain whey and transfer curds to molds."},
            {"step": 7, "text": "Press lightly at 5 lbs for 2 hours."},
            {"step": 8, "text": "Flip and press at 10 lbs for 4 hours."},
            {"step": 9, "text": "Cut into 3-4 inch blocks."},
            {"step": 10, "text": "Make brine (about 8-10% salt solution) and submerge cheese."},
            {"step": 11, "text": "Store in brine for 1-2 weeks before using. Keep refrigerated."},
            {"step": 12, "text": "Before using in desserts, soak in water to remove excess salt."}
        ],
        "temperature": "90°F make, refrigerator storage",
        "notes": [
            "Akkawi is intentionally mild - don't over-culture",
            "For knafeh and sweets, soak the cheese in fresh water for several hours to remove salt",
            "The texture should be smooth and elastic when heated",
            "Also used in savory pastries and eaten fresh with herbs"
        ],
        "tags": ["cheese", "traditional", "levantine", "middle-eastern", "akkawi", "brine-cheese", "dessert-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-nabulsi-palestinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Nabulsi Cheese (Palestinian)",
        "category": "mains",
        "attribution": "Nablus, Palestine, Ancient",
        "source_note": "Nabulsi cheese is named after the city of Nablus in the Palestinian West Bank, where it has been made for centuries. Traditionally boiled in brine with mahaleb and mastic, it has a distinctive flavor used in many Levantine sweets.",
        "description": "Traditional Palestinian white cheese from Nablus, boiled with mahaleb spice and essential for kunafa and Middle Eastern pastries.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "1-2 weeks brining",
        "total_time": "1-2 weeks",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "or goat milk"},
            {"item": "mesophilic starter culture", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"},
            {"item": "mahaleb", "quantity": "1", "unit": "tsp", "prep_note": "ground, for brine"},
            {"item": "mastic", "quantity": "1/4", "unit": "tsp", "prep_note": "crushed, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir, and ripen for 15 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 90°F."},
            {"step": 6, "text": "Drain whey and transfer curds to rectangular molds."},
            {"step": 7, "text": "Press at 10 lbs for 4-6 hours."},
            {"step": 8, "text": "Cut pressed cheese into 3x4 inch rectangular pieces."},
            {"step": 9, "text": "Make spiced brine: dissolve salt in water, add mahaleb and mastic, bring to boil."},
            {"step": 10, "text": "Boil cheese pieces in spiced brine for 5-10 minutes until they float."},
            {"step": 11, "text": "Let cool in brine and store refrigerated."},
            {"step": 12, "text": "For desserts, soak in fresh water overnight to remove excess salt."}
        ],
        "temperature": "90°F make, boiling brine",
        "notes": [
            "The boiling step in spiced brine is unique to Nabulsi cheese",
            "Mahaleb (ground cherry pits) gives the distinctive slightly bitter-almond flavor",
            "Mastic adds a subtle pine/resin note",
            "Must be desalted before use in kunafa and other sweets"
        ],
        "tags": ["cheese", "traditional", "palestinian", "nabulsi", "middle-eastern", "brine-cheese", "dessert-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-jibneh-arabieh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jibneh Arabieh (Arabian White Cheese)",
        "category": "mains",
        "attribution": "Arabian Peninsula, Ancient",
        "source_note": "Jibneh Arabieh ('Arabian cheese') is the generic term for traditional white brine cheeses made throughout the Arabian Peninsula. Simple and mild, it's been a staple food for Bedouin and settled communities alike.",
        "description": "Simple Arabian white cheese, mild and versatile - a staple food throughout the Arabian Peninsula for millennia.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "1 week brining",
        "total_time": "1 week",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "cow, sheep, goat, or camel"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "nigella seeds", "quantity": "1", "unit": "tsp", "prep_note": "optional, for habbat al-barakah style"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add diluted rennet (no starter needed for this simple cheese), stir gently."},
            {"step": 3, "text": "Let set 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Gently ladle curds into a cloth-lined colander."},
            {"step": 6, "text": "If adding nigella seeds, fold them into curds now."},
            {"step": 7, "text": "Tie cloth and hang to drain for 6-8 hours."},
            {"step": 8, "text": "Cut drained cheese into blocks."},
            {"step": 9, "text": "Make brine (about 8% salt solution) and submerge cheese."},
            {"step": 10, "text": "Store in brine, refrigerated. Ready to eat after 1 week."}
        ],
        "temperature": "90°F make, refrigerator storage",
        "notes": [
            "This is one of the simplest traditional cheeses - rennet only, no starter",
            "Nigella seeds (habbat al-barakah/black seed) are a popular addition",
            "Traditionally made from whatever milk was available: goat, sheep, cow, or camel",
            "Mild flavor, perfect with flatbread, olives, and Middle Eastern breakfast"
        ],
        "tags": ["cheese", "traditional", "arabian", "middle-eastern", "jibneh", "white-cheese", "brine-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-chhena-indian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chhena (Indian Fresh Cheese)",
        "category": "mains",
        "attribution": "Eastern India (Bengal, Odisha), Ancient",
        "source_note": "Chhena (or chhana) is a fresh acid-set cheese foundational to Eastern Indian cuisine. Unlike paneer, it's not pressed firm, remaining soft and creamy - essential for sweets like rasgulla, sandesh, and rasmalai.",
        "description": "Soft Indian fresh cheese essential for Bengali sweets - the foundation of rasgulla, sandesh, and rasmalai.",
        "servings_yield": "About 12 oz",
        "prep_time": "30 minutes",
        "cook_time": "15 minutes",
        "total_time": "45 minutes",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "full-fat essential"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": "or 1/2 cup yogurt whey"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in a heavy pot over medium-high heat until it comes to a full, rolling boil."},
            {"step": 2, "text": "Reduce heat to low. Add lemon juice one tablespoon at a time, stirring gently."},
            {"step": 3, "text": "Curds will separate from clear greenish whey almost immediately."},
            {"step": 4, "text": "Once fully separated, remove from heat. Do not overcook or curds will become rubbery."},
            {"step": 5, "text": "Let sit for 5 minutes only."},
            {"step": 6, "text": "Pour through a fine cloth-lined strainer."},
            {"step": 7, "text": "Rinse very gently with cool water to remove acidic taste."},
            {"step": 8, "text": "Gather cloth and squeeze very gently - chhena should remain soft and moist."},
            {"step": 9, "text": "Do NOT press like paneer - chhena needs to stay soft and pliable."},
            {"step": 10, "text": "Knead gently on a plate until smooth and free of lumps."},
            {"step": 11, "text": "Use immediately for best results in sweets."}
        ],
        "temperature": "Boiling",
        "notes": [
            "Chhena must be soft and smooth - over-draining makes sweets tough",
            "Fresh chhena should feel like soft, smooth playdough",
            "Unlike paneer, chhena is never pressed firm",
            "For rasgulla, the chhena must be kneaded until completely smooth with no graininess",
            "Best used fresh; doesn't store well"
        ],
        "tags": ["cheese", "traditional", "indian", "bengali", "chhena", "fresh-cheese", "sweet-cheese", "ancient"],
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
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
