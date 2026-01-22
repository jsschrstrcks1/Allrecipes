#!/usr/bin/env python3
"""Add batch 49 - More regional Portuguese, Spanish, and Balkan cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-queijo-sao-jorge-azores",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo São Jorge (Azorean Island Cheese)",
        "category": "mains",
        "attribution": "15th century Flemish-Azorean tradition",
        "source_note": "Traditional Portuguese island cheesemaking",
        "description": "Brought to the Azores by Flemish settlers in the 15th century, São Jorge cheese evolved in the volcanic island's unique conditions. Made from raw milk of grass-fed cows on lush pastures, it develops sharp, spicy flavors with age.",
        "servings_yield": "2-3 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "4-7 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from grass-fed cows"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "sea salt preferred"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture, stir well, ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently, let set 40-50 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes - smaller than many cheeses."},
            {"step": 5, "text": "Stir gently for 15 minutes, allowing curds to firm."},
            {"step": 6, "text": "Raise temperature gradually to 100°F (38°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are quite firm and release whey easily."},
            {"step": 8, "text": "Drain whey and pack curds firmly into large wheel molds."},
            {"step": 9, "text": "Press at increasing weights: 10 lbs for 1 hour, 30 lbs for 4 hours, 50 lbs overnight."},
            {"step": 10, "text": "Flip during pressing multiple times."},
            {"step": 11, "text": "Brine for 24-36 hours."},
            {"step": 12, "text": "Air dry for 2-3 days."},
            {"step": 13, "text": "Age at 50-55°F with 85% humidity."},
            {"step": 14, "text": "Turn twice weekly, brushing rind. Age minimum 4 months, preferably 7+ months."}
        ],
        "temperature": "90-100°F (32-38°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1984",
            "Flemish settlers adapted Gouda techniques to Azorean conditions",
            "Volcanic soil creates unique mineral-rich pastures",
            "Young versions are mild; aged São Jorge is spicy and sharp",
            "Traditional wheels can weigh up to 12 kg"
        ],
        "tags": ["cheese", "portuguese", "azores", "traditional", "aged", "island"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queijo-terrincho-tras-os-montes",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo Terrincho (Trás-os-Montes Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Portuguese transhumance tradition",
        "source_note": "Traditional Portuguese sheep's milk cheesemaking",
        "description": "From the remote Trás-os-Montes region of northeastern Portugal, this sheep's milk cheese takes its name from the Terrincho sheep breed. Made by shepherds following ancient transhumance routes, it represents Portugal's pastoral heritage.",
        "servings_yield": "1.5 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Terrincho or Churra sheep"},
            {"item": "natural thistle rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional Portuguese"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare thistle rennet: steep dried thistle flowers in warm water for several hours."},
            {"step": 2, "text": "Heat sheep's milk to 85-90°F (29-32°C) - traditional method uses no added starter."},
            {"step": 3, "text": "Add strained thistle rennet liquid, stir gently."},
            {"step": 4, "text": "Let set for 45-60 minutes until firm curd forms."},
            {"step": 5, "text": "Cut curds by hand or with traditional tools into walnut-sized pieces."},
            {"step": 6, "text": "Let curds rest under whey 10-15 minutes."},
            {"step": 7, "text": "Gently stir and raise temperature to 100°F (38°C)."},
            {"step": 8, "text": "When curds are firm, drain and pack into cloth-lined molds."},
            {"step": 9, "text": "Press lightly for 2-4 hours, flipping several times."},
            {"step": 10, "text": "Dry salt surfaces over 2-3 days."},
            {"step": 11, "text": "Age at 50-55°F with 80-85% humidity."},
            {"step": 12, "text": "Turn regularly, rubbing rind. Ready in 2-4 months."}
        ],
        "temperature": "85-100°F (29-38°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected - must use Terrincho or Churra breed milk",
            "Thistle rennet gives distinctive slightly bitter, herbal notes",
            "Terrincho sheep are an ancient Portuguese breed adapted to harsh terrain",
            "Paste is ivory-white, slightly crumbly, with small eyes",
            "Traditional in regional dishes from Trás-os-Montes"
        ],
        "tags": ["cheese", "portuguese", "sheep", "traditional", "thistle-rennet"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queijo-rabaçal-central-portugal",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo Rabaçal (Central Portugal Mixed Cheese)",
        "category": "mains",
        "attribution": "Ancient central Portuguese tradition",
        "source_note": "Traditional Portuguese mixed-milk cheesemaking",
        "description": "From the limestone hills of central Portugal, Rabaçal combines sheep and goat milk in an ancient recipe. The region's chalky soil produces aromatic pastures that give the cheese its distinctive character.",
        "servings_yield": "1 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "30-60 days aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": "2/3 of blend"},
            {"item": "raw goat's milk", "quantity": "0.5", "unit": "gallon", "prep_note": "1/3 of blend"},
            {"item": "natural thistle rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep's and goat's milk in traditional ratio (approximately 2:1)."},
            {"step": 2, "text": "Heat mixed milk to 86-90°F (30-32°C)."},
            {"step": 3, "text": "Add thistle rennet liquid (steeped in warm water)."},
            {"step": 4, "text": "Let set 40-50 minutes until firm curd."},
            {"step": 5, "text": "Cut curds to hazelnut size."},
            {"step": 6, "text": "Stir gently and let rest under whey 10 minutes."},
            {"step": 7, "text": "Drain and transfer curds to traditional perforated molds."},
            {"step": 8, "text": "Press lightly, flipping several times over 4-6 hours."},
            {"step": 9, "text": "Salt surfaces by rubbing over 2-3 days."},
            {"step": 10, "text": "Age at 50-55°F with 80% humidity for 30-60 days."},
            {"step": 11, "text": "Turn every few days, developing natural rind."}
        ],
        "temperature": "86-90°F (30-32°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1996",
            "Takes name from village of Rabaçal in Coimbra district",
            "Small wheels traditionally weigh 300-500 grams",
            "Interior is white, semi-soft, with subtle eyes",
            "Flavor balances sheep's richness with goat's tang"
        ],
        "tags": ["cheese", "portuguese", "mixed-milk", "traditional", "thistle-rennet"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-idiazabal-basque-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Idiazabal (Basque Smoked Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Basque shepherds' tradition",
        "source_note": "Traditional Basque cheesemaking",
        "description": "A proud symbol of Basque culture, Idiazabal has been made by shepherds in the Pyrenees for thousands of years. Traditionally smoked over cherry or beech wood, it develops a distinctive dark rind and complex smoky-nutty flavor.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Latxa or Carranzana sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "lamb rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cherry or beech wood", "quantity": "", "unit": "", "prep_note": "for smoking, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add starter culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add lamb rennet, stir, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds to corn-kernel size."},
            {"step": 5, "text": "Stir and raise temperature to 104°F (40°C) over 30 minutes."},
            {"step": 6, "text": "Continue stirring until curds are very firm."},
            {"step": 7, "text": "Drain and pack curds tightly into cylindrical molds."},
            {"step": 8, "text": "Press at 20-30 lbs for 6-8 hours, flipping several times."},
            {"step": 9, "text": "Brine for 24-48 hours depending on size."},
            {"step": 10, "text": "Air dry for several days until surface is completely dry."},
            {"step": 11, "text": "For smoked version: cold smoke over cherry or beech wood for 10-15 days."},
            {"step": 12, "text": "Age at 50-55°F with 80-85% humidity for 2-6 months."}
        ],
        "temperature": "86-104°F (30-40°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected - made in Basque Country and Navarra",
            "Comes in smoked and unsmoked versions",
            "Latxa sheep are an ancient Basque breed with long, coarse wool",
            "Traditionally made in shepherd huts (txabolas) during transhumance",
            "Compact, oily paste with buttery, nutty, smoky notes"
        ],
        "tags": ["cheese", "spanish", "basque", "sheep", "traditional", "smoked"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-roncal-navarra-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Roncal (Navarra Aged Sheep Cheese)",
        "category": "mains",
        "attribution": "Medieval Navarrese tradition",
        "source_note": "Traditional Spanish Pyrenean cheesemaking",
        "description": "Spain's first DOP cheese (1981), Roncal comes from the Roncal Valley in the Navarrese Pyrenees. Documented since at least the 13th century, it's made only from December to July when sheep graze the valley's lush pastures.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "4-12 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Rasa or Latxa sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "lamb rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add starter culture, ripen 30 minutes."},
            {"step": 3, "text": "Add lamb rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds very small, to rice grain size."},
            {"step": 5, "text": "Stir and raise temperature to 100-104°F (38-40°C)."},
            {"step": 6, "text": "Continue stirring until curds are very dry and firm."},
            {"step": 7, "text": "Drain whey completely."},
            {"step": 8, "text": "Pack curds very firmly into cylindrical molds."},
            {"step": 9, "text": "Press heavily for 24 hours, flipping multiple times."},
            {"step": 10, "text": "Rub rind with dry salt over several days (traditional method)."},
            {"step": 11, "text": "Age at 50-55°F with 80-85% humidity."},
            {"step": 12, "text": "Turn and brush regularly. Minimum 4 months, preferably 7-12 months."}
        ],
        "temperature": "86-104°F (30-40°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Spain's first DOP cheese, protected since 1981",
            "Made only in seven villages of the Roncal Valley",
            "Production restricted to December-July milking season",
            "Hard, dense texture with granular paste",
            "Intense, piquant flavor - sharper than Manchego"
        ],
        "tags": ["cheese", "spanish", "navarra", "sheep", "traditional", "aged", "DOP"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-kashkaval-balkan-stretched",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kashkaval (Balkan Stretched Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Balkan and Turkish tradition",
        "source_note": "Traditional Balkan pasta filata cheesemaking",
        "description": "The dominant stretched-curd cheese of the Balkans, Kashkaval (from Italian 'caciocavallo') has been made throughout southeastern Europe for centuries. Each country has its variation, but the sheep's milk pasta filata technique remains constant.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep/cow blend"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add acidic whey starter from previous batch."},
            {"step": 3, "text": "Add rennet, stir gently, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds to walnut size."},
            {"step": 5, "text": "Let curds acidify under warm whey for 4-6 hours."},
            {"step": 6, "text": "Test for stretchability in hot water - should become pliable."},
            {"step": 7, "text": "Slice acidified curd into strips."},
            {"step": 8, "text": "Heat water or whey to 170-175°F (77-80°C)."},
            {"step": 9, "text": "Stretch curd strips in hot liquid, kneading until smooth."},
            {"step": 10, "text": "Form into wheel or cylinder shape."},
            {"step": 11, "text": "Place in molds to set shape."},
            {"step": 12, "text": "Brine for 24-48 hours."},
            {"step": 13, "text": "Age at 50-55°F with moderate humidity for 2-6 months."}
        ],
        "temperature": "95°F (35°C) for curd; 170-175°F (77-80°C) for stretching",
        "notes": [
            "Found throughout Bulgaria, Romania, Turkey, Greece, and the Balkans",
            "Bulgarian Kashkaval is particularly prized, made from Karakachan sheep milk",
            "Romanian Cascaval often uses cow's milk",
            "Young Kashkaval is mild and elastic; aged becomes sharp and crumbly",
            "Essential for Balkan dishes like shopska salad and banitsa"
        ],
        "tags": ["cheese", "balkan", "sheep", "traditional", "pasta-filata", "stretched"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-sirene-bulgarian-white-brine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sirene (Bulgarian White Brine Cheese)",
        "category": "mains",
        "attribution": "Ancient Thracian-Bulgarian tradition",
        "source_note": "Traditional Bulgarian brine cheesemaking",
        "description": "Bulgaria's national cheese, Sirene has been made in the Balkans for thousands of years - possibly since Thracian times. This tangy, crumbly white cheese aged in brine is essential to Bulgarian cuisine and culture.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "30-60 days aging in brine",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "or cow's milk"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": "Bulgarian yogurt works too"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F (30-32°C)."},
            {"step": 2, "text": "Add mesophilic culture (or Bulgarian yogurt), ripen 45-60 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes - relatively large."},
            {"step": 5, "text": "Let curds rest under whey 15-20 minutes."},
            {"step": 6, "text": "Gently stir and let curds settle again."},
            {"step": 7, "text": "Drain curds and transfer to cloth-lined molds or colander."},
            {"step": 8, "text": "Press lightly or let drain naturally for several hours."},
            {"step": 9, "text": "Cut consolidated curd into blocks."},
            {"step": 10, "text": "Prepare brine: dissolve 1 cup salt in 1 quart water (about 8-10% brine)."},
            {"step": 11, "text": "Submerge cheese blocks in brine."},
            {"step": 12, "text": "Store at cool room temperature or refrigerate."},
            {"step": 13, "text": "Ready in 30-60 days in brine. Keeps for months submerged."}
        ],
        "temperature": "86-90°F (30-32°C) for make; store in brine at 40-50°F",
        "notes": [
            "Similar to Greek feta but typically made from pure sheep's or cow's milk",
            "Bulgarian yogurt cultures give characteristic tangy flavor",
            "Essential in Shopska salad - the Bulgarian national dish",
            "Sheep's milk version is richer; cow's milk is milder",
            "Cheese preserved in brine keeps for many months"
        ],
        "tags": ["cheese", "bulgarian", "traditional", "brine", "white", "balkan"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-teleme-romanian-fresh-brine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Telemea (Romanian Fresh Brine Cheese)",
        "category": "mains",
        "attribution": "Ancient Romanian pastoral tradition",
        "source_note": "Traditional Romanian brine cheesemaking",
        "description": "Romania's beloved white brine cheese, Telemea has been made by shepherds in the Carpathian Mountains for centuries. Softer and creamier than Bulgarian sirene, it's essential to Romanian cuisine and pastoral culture.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "14-30 days aging in brine",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "or cow's milk"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 45-60 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into large 2-inch cubes."},
            {"step": 5, "text": "Let curds rest undisturbed 15-20 minutes."},
            {"step": 6, "text": "Very gently ladle curds into cloth-lined mold."},
            {"step": 7, "text": "Let drain naturally - no pressing - for 8-12 hours."},
            {"step": 8, "text": "Turn mold several times during draining."},
            {"step": 9, "text": "Unmold and cut into blocks."},
            {"step": 10, "text": "Prepare lighter brine: about 6-8% salt solution."},
            {"step": 11, "text": "Submerge cheese blocks in brine."},
            {"step": 12, "text": "Ready in 14-30 days. Keep refrigerated in brine."}
        ],
        "temperature": "86°F (30°C) for make; store in brine at 35-45°F",
        "notes": [
            "Softer and creamier than Greek feta or Bulgarian sirene",
            "PDO Telemea de Ibăneşti made only in Mureş County",
            "Sheep's milk version from Carpathian pastures is most prized",
            "Essential in Romanian mămăligă (polenta) dishes",
            "Traditional preservation method for mountain shepherds"
        ],
        "tags": ["cheese", "romanian", "traditional", "brine", "white", "balkan", "soft"],
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
