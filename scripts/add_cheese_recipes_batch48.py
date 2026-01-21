#!/usr/bin/env python3
"""Add batch 48 - Ancient and regional European cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-pecorino-di-fossa-pit-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino di Fossa (Pit-Aged Sheep Cheese)",
        "category": "mains",
        "attribution": "Medieval Marche pit-aging tradition",
        "source_note": "Traditional Italian underground aging",
        "description": "A unique cheese aged in ancient tufa pits in the Marche and Emilia-Romagna regions. The practice dates to at least the 1400s when cheeses were buried to hide them from marauding armies. The anaerobic environment creates an incomparable flavor.",
        "servings_yield": "2 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3 hours",
        "total_time": "3-4 months total (including pit aging)",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "or cow/sheep blend"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "straw or hay", "quantity": "", "unit": "", "prep_note": "for pit lining"},
            {"item": "cotton cloth bags", "quantity": "", "unit": "", "prep_note": "for wrapping cheeses"}
        ],
        "instructions": [
            {"step": 1, "text": "First make a standard pecorino: heat milk to 95°F (35°C), add culture."},
            {"step": 2, "text": "Add rennet after 20 minutes, let set 30-40 minutes."},
            {"step": 3, "text": "Cut curds to walnut size, stir gently."},
            {"step": 4, "text": "Raise temperature to 113°F (45°C) while stirring."},
            {"step": 5, "text": "Drain, mold, and press conventionally for 24 hours."},
            {"step": 6, "text": "Dry salt all surfaces and age for 60-90 days until rind forms."},
            {"step": 7, "text": "Prepare the pit: traditionally flask-shaped tufa caves, 3m deep."},
            {"step": 8, "text": "Line pit bottom and walls with clean straw."},
            {"step": 9, "text": "Wrap each aged cheese in cotton cloth bag."},
            {"step": 10, "text": "Stack wrapped cheeses in pit, separated by straw layers."},
            {"step": 11, "text": "Seal pit opening with wooden lid, then plaster to make airtight."},
            {"step": 12, "text": "Leave sealed for 90-100 days (traditionally August to November)."},
            {"step": 13, "text": "Unseal on Saint Catherine's Day (November 25) traditionally."},
            {"step": 14, "text": "Remove cheeses - shapes will be irregular from compression and fermentation."}
        ],
        "temperature": "95-113°F (35-45°C) for make; ambient pit temperature for aging",
        "notes": [
            "The irregular, amber-colored cheese has intense, complex flavors unlike any surface-aged cheese",
            "DOP protected since 2009 - must be aged in specific pit areas",
            "Originally a way to hide cheese from medieval invaders",
            "Home version: use food-grade container buried in cool ground, sealed airtight",
            "Flavor notes include honey, mushroom, and fermented grain"
        ],
        "tags": ["cheese", "italian", "sheep", "traditional", "ancient", "pit-aged", "marche"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-caciocavallo-silano-horseback",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caciocavallo Silano (Horseback Cheese)",
        "category": "mains",
        "attribution": "Ancient southern Italian stretched-curd tradition",
        "source_note": "Traditional Italian pasta filata cheesemaking",
        "description": "An ancient stretched-curd cheese from southern Italy, Caciocavallo ('cheese on horseback') is named for the way pairs are tied together and hung over a pole to age. Records exist from at least 500 BC, making it one of Italy's oldest cheeses.",
        "servings_yield": "2 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "2-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Podolica or similar breed"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "from previous batch, acidic"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "gallon", "prep_note": "saturated"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 100°F (38°C)."},
            {"step": 2, "text": "Add acidic whey starter from previous batch."},
            {"step": 3, "text": "Add rennet, stir gently, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into small pieces."},
            {"step": 5, "text": "Let curds rest under warm whey for 4-5 hours to acidify."},
            {"step": 6, "text": "Test acidity: cut strip of curd, stretch in hot water - should become pliable."},
            {"step": 7, "text": "Cut acidified curd into strips."},
            {"step": 8, "text": "Heat water to 175-185°F (80-85°C)."},
            {"step": 9, "text": "Submerge curd strips and begin kneading when pliable."},
            {"step": 10, "text": "Stretch and fold repeatedly until smooth and elastic."},
            {"step": 11, "text": "Form into traditional gourd or tear-drop shape with small head."},
            {"step": 12, "text": "Tie string around neck, leaving enough to hang in pairs."},
            {"step": 13, "text": "Cool in cold water, then brine for 8-24 hours."},
            {"step": 14, "text": "Hang pairs over wooden pole to age."},
            {"step": 15, "text": "Age at 55°F with moderate humidity: 2-3 months for mild, up to 12 months for sharp."}
        ],
        "temperature": "100°F (38°C) for curd; 175-185°F (80-85°C) for stretching",
        "notes": [
            "Name may derive from hanging cheese 'a cavallo' (astride) a pole",
            "DOP Caciocavallo Silano must come from specific southern regions",
            "Podolica breed milk from transhumant herds is traditional",
            "Young versions are mild and stretchy; aged versions are sharp and granular",
            "Can be grilled or pan-fried when young - surface caramelizes beautifully"
        ],
        "tags": ["cheese", "italian", "traditional", "pasta-filata", "aged", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-ragusano-sicilian-rectangular",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ragusano (Sicilian Rectangular Cheese)",
        "category": "mains",
        "attribution": "Ancient Sicilian pasta filata tradition",
        "source_note": "Traditional Sicilian stretched-curd cheesemaking",
        "description": "A unique rectangular stretched-curd cheese from Ragusa province in Sicily, Ragusano has been made since at least the 1500s. Its distinctive rectangular shape comes from being pressed between boards - unusual for pasta filata cheese.",
        "servings_yield": "2 lb block",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "4-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Modicana breed if possible"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "acidic, from previous batch"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional Sicilian"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "sea salt preferred"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup", "prep_note": "for rind treatment"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add acidic whey starter."},
            {"step": 3, "text": "Add lamb rennet paste dissolved in water, let set 30-40 minutes."},
            {"step": 4, "text": "Break curd using traditional 'rotula' tool into small pieces."},
            {"step": 5, "text": "Let curds acidify under whey for 18-24 hours until pH reaches 5.0-5.2."},
            {"step": 6, "text": "Cut acidified curd mass into strips."},
            {"step": 7, "text": "Heat water to 175°F (80°C)."},
            {"step": 8, "text": "Stretch curd strips in hot water until very elastic."},
            {"step": 9, "text": "Form into large rectangular mass."},
            {"step": 10, "text": "Place between two wooden boards (traditional 'mastredda' molds)."},
            {"step": 11, "text": "Press and turn regularly for 24-48 hours to form rectangular shape."},
            {"step": 12, "text": "Brine for 24-48 hours depending on size."},
            {"step": 13, "text": "Age hanging by rope in ventilated rooms."},
            {"step": 14, "text": "Rub rind with olive oil periodically during 4-12 month aging."}
        ],
        "temperature": "95°F (35°C) for curd; 175°F (80°C) for stretching",
        "notes": [
            "DOP protected - one of Sicily's oldest and most prestigious cheeses",
            "Modicana is an ancient Sicilian cattle breed that nearly went extinct",
            "Traditional blocks weigh 10-16 kg (22-35 lbs)",
            "Young cheese is mild; aged versions develop complex, slightly piquant flavor",
            "Grated over Sicilian pasta dishes like pasta alla Norma"
        ],
        "tags": ["cheese", "italian", "sicilian", "traditional", "pasta-filata", "aged"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-provolone-valpadana-giant",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Provolone Valpadana (Giant Italian Stretched Cheese)",
        "category": "mains",
        "attribution": "Northern Italian pasta filata tradition",
        "source_note": "Traditional Italian stretched-curd cheesemaking",
        "description": "While provolone originated in southern Italy, Provolone Valpadana from the Po Valley became the DOP standard. Made in enormous sizes (up to 100+ kg), it comes in dolce (mild) and piccante (sharp) versions based on rennet type.",
        "servings_yield": "2-3 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "3-12+ months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons", "prep_note": "from Po Valley breeds traditionally"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or natural whey starter"},
            {"item": "calf rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "for dolce version"},
            {"item": "lamb/kid rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "for piccante version"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "gallon", "prep_note": "saturated"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 100°F (38°C)."},
            {"step": 2, "text": "Add starter culture (thermophilic for faster acidification, or natural whey)."},
            {"step": 3, "text": "Add rennet: calf rennet for dolce (mild), lamb/kid paste for piccante (sharp)."},
            {"step": 4, "text": "Let set 20-30 minutes until firm."},
            {"step": 5, "text": "Cut curds into small pieces."},
            {"step": 6, "text": "Stir and raise temperature to 118°F (48°C) over 30 minutes."},
            {"step": 7, "text": "Let curds acidify under whey for 3-5 hours until stretchable."},
            {"step": 8, "text": "Cut curd mass into strips."},
            {"step": 9, "text": "Heat water to 175-185°F (80-85°C)."},
            {"step": 10, "text": "Stretch and knead curd until smooth and very elastic."},
            {"step": 11, "text": "Form into desired shape: cylinder, pear, cone, or salami."},
            {"step": 12, "text": "Tie with cord and hang to set shape while still warm."},
            {"step": 13, "text": "Cool in cold water, then brine for 12-24 hours."},
            {"step": 14, "text": "Hang to age at 55°F with moderate humidity."},
            {"step": 15, "text": "Dolce: age 2-3 months. Piccante: age 6 months to 2+ years."}
        ],
        "temperature": "100-118°F (38-48°C) for curd; 175-185°F (80-85°C) for stretching",
        "notes": [
            "DOP Provolone Valpadana comes in many shapes: salami, melon, pear, cone, cylinder",
            "Traditional giant wheels can weigh 100+ kg and age for years",
            "Lamb/kid rennet creates the enzymes that develop sharp piccante flavor",
            "Smoked provolone is a popular variation",
            "Dolce version melts beautifully; piccante is better for grating"
        ],
        "tags": ["cheese", "italian", "traditional", "pasta-filata", "aged"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-scamorza-smoked-pear",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Scamorza (Smoked Pear-Shaped Cheese)",
        "category": "mains",
        "attribution": "Southern Italian pasta filata tradition",
        "source_note": "Traditional Italian stretched-curd cheesemaking",
        "description": "A stretched-curd cheese from southern Italy, Scamorza is essentially mozzarella that's been hung to dry and develop flavor. The name means 'beheaded' referring to its pinched pear shape. Often smoked for additional flavor.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1-2 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "or buffalo milk"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "hardwood chips", "quantity": "1", "unit": "cup", "prep_note": "for smoking, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add thermophilic culture, ripen 45-60 minutes."},
            {"step": 3, "text": "Add rennet, stir gently, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest under whey for 3-4 hours until pH reaches 5.2-5.3."},
            {"step": 6, "text": "Test stretchability: small piece should stretch in hot water."},
            {"step": 7, "text": "Cut acidified curd into strips."},
            {"step": 8, "text": "Heat water to 170-175°F (77-80°C)."},
            {"step": 9, "text": "Stretch and knead curd until smooth and elastic."},
            {"step": 10, "text": "Form into ball, then pinch and twist top to create pear shape with 'head.'"},
            {"step": 11, "text": "Tie string around neck for hanging."},
            {"step": 12, "text": "Cool in cold salted water briefly."},
            {"step": 13, "text": "Hang to dry for 24-48 hours."},
            {"step": 14, "text": "For smoked scamorza: cold smoke for 2-4 hours with hardwood."},
            {"step": 15, "text": "Continue aging hung in cool, ventilated space for 1-2 weeks."}
        ],
        "temperature": "95°F (35°C) for curd; 170-175°F (77-80°C) for stretching",
        "notes": [
            "Fresh scamorza is white; smoked scamorza has golden-brown exterior",
            "Texture is firmer and drier than mozzarella but still stretchy when heated",
            "Excellent for grilling - holds shape while developing crispy exterior",
            "Traditional in southern Italian cuisine, especially Molise and Campania",
            "Can substitute for mozzarella when firmer texture desired"
        ],
        "tags": ["cheese", "italian", "traditional", "pasta-filata", "smoked", "quick"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-burrata-cream-filled-mozzarella",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Burrata (Cream-Filled Mozzarella)",
        "category": "mains",
        "attribution": "Pugliese innovation (1920s)",
        "source_note": "Traditional Italian stretched-curd with cream filling",
        "description": "Invented in the 1920s in Puglia as a way to use mozzarella scraps, burrata has a mozzarella shell filled with stracciatella (shredded mozzarella curds) and cream. When cut, the creamy interior flows out luxuriously.",
        "servings_yield": "4 burrata balls",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "Same day (fresh)",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "for mozzarella shell"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for filling"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Make mozzarella curd: heat milk to 95°F (35°C), add culture, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 30-40 minutes."},
            {"step": 3, "text": "Cut curds, let acidify under whey 3-4 hours until stretchable."},
            {"step": 4, "text": "Cut acidified curd into strips."},
            {"step": 5, "text": "Reserve about 1/4 of the curd strips for stracciatella filling."},
            {"step": 6, "text": "For stracciatella: stretch reserved curd in hot water, then pull into thin shreds."},
            {"step": 7, "text": "Mix shredded curd with cold heavy cream and pinch of salt. Set aside."},
            {"step": 8, "text": "For shell: stretch remaining curd in 170°F (77°C) water until very smooth."},
            {"step": 9, "text": "Form into thin disc, about 6 inches diameter."},
            {"step": 10, "text": "Working quickly, place 2-3 tbsp stracciatella mixture in center."},
            {"step": 11, "text": "Gather edges up and twist to seal, forming pouch shape."},
            {"step": 12, "text": "Pinch off excess at top, smooth seal."},
            {"step": 13, "text": "Place immediately in cold salted water to set shape."},
            {"step": 14, "text": "Store in brine or fresh water. Best eaten same day at room temperature."}
        ],
        "temperature": "95°F (35°C) for curd; 170°F (77°C) for stretching",
        "notes": [
            "Must be eaten very fresh - stracciatella spoils quickly",
            "Bring to room temperature before serving for best texture",
            "Traditional serving: drizzle with olive oil, serve with tomatoes and bread",
            "IGP protected since 2016",
            "The name means 'buttered' in Italian dialect, referring to creamy interior"
        ],
        "tags": ["cheese", "italian", "traditional", "pasta-filata", "fresh", "cream"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-caciotta-toscana-farmstead",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caciotta Toscana (Tuscan Farmstead Cheese)",
        "category": "mains",
        "attribution": "Ancient Tuscan farmstead tradition",
        "source_note": "Traditional Italian farmstead cheesemaking",
        "description": "Caciotta is the everyday farmstead cheese of central Italy - every farm traditionally made their own version. Simple, versatile, and quick to mature, it represents the practical side of Italian cheesemaking passed down through generations.",
        "servings_yield": "1 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "2-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep/mixed milk"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add mesophilic culture, stir well, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 1 minute."},
            {"step": 4, "text": "Let set for 30-40 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently for 10 minutes, letting curds heal."},
            {"step": 7, "text": "Raise temperature slowly to 100°F (38°C) over 20 minutes."},
            {"step": 8, "text": "Continue stirring until curds are firm and slightly squeaky."},
            {"step": 9, "text": "Drain whey and transfer curds to basket molds."},
            {"step": 10, "text": "Press lightly: 5 lbs for 30 minutes, flip, 10 lbs for 2 hours."},
            {"step": 11, "text": "Salt surfaces by rubbing or brief brining (2-4 hours)."},
            {"step": 12, "text": "Air dry for 1-2 days until surface is dry to touch."},
            {"step": 13, "text": "Age at 50-55°F with 85% humidity."},
            {"step": 14, "text": "Turn daily first week, then weekly. Ready in 2-8 weeks depending on preference."}
        ],
        "temperature": "90-100°F (32-38°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Caciotta simply means 'little cheese' - the basic farmstead wheel",
            "Infinite variations exist: with truffles, herbs, pepper, wrapped in leaves",
            "Sheep's milk version is richer; cow's milk is milder",
            "Young caciotta is soft and milky; older versions are firmer with more flavor",
            "Perfect beginner cheese - forgiving and quick to mature"
        ],
        "tags": ["cheese", "italian", "traditional", "tuscan", "farmstead", "beginner"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-crescenza-stracchino-lombardy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Crescenza/Stracchino (Lombardy Fresh Cheese)",
        "category": "mains",
        "attribution": "Ancient Lombard pastoral tradition",
        "source_note": "Traditional Italian fresh cheesemaking",
        "description": "An ancient soft cheese from Lombardy, Crescenza (also called Stracchino) was traditionally made from the milk of 'tired' (stracche) cows descending from alpine pastures. The gentle, spreadable cheese is a staple of northern Italian cuisine.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "2-3 hours",
        "total_time": "1-2 weeks to ready",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "high fat preferred"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/8", "unit": "tsp", "prep_note": "less than usual"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to just 86°F (30°C) - cooler than most cheeses."},
            {"step": 2, "text": "Add mesophilic culture, stir gently, ripen 30 minutes."},
            {"step": 3, "text": "Add just half the usual amount of rennet for a soft set."},
            {"step": 4, "text": "Let set for 45-60 minutes - curd will be very soft."},
            {"step": 5, "text": "Cut curds into large 2-inch cubes - minimal cutting."},
            {"step": 6, "text": "Let curds rest 5 minutes."},
            {"step": 7, "text": "Very gently ladle curds into rectangular molds - do not stir or break."},
            {"step": 8, "text": "Let drain naturally - no pressing. Turn molds every 30 minutes."},
            {"step": 9, "text": "After 4-6 hours of draining, salt surfaces lightly."},
            {"step": 10, "text": "Continue turning for 24 hours as cheese consolidates."},
            {"step": 11, "text": "Unmold and wrap loosely in paper or cloth."},
            {"step": 12, "text": "Refrigerate and consume within 1-2 weeks."}
        ],
        "temperature": "86°F (30°C) for make; refrigerate for storage",
        "notes": [
            "Texture should be soft, creamy, and spreadable",
            "Traditional in focaccia di Recco - melted inside crispy bread",
            "Name 'stracchino' from Lombard 'stracch' meaning tired",
            "Very mild, milky flavor with slight tang",
            "Can substitute for cream cheese in many applications"
        ],
        "tags": ["cheese", "italian", "traditional", "lombardy", "fresh", "soft", "spreadable"],
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
