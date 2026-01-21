#!/usr/bin/env python3
"""Add batch 46 - More traditional and ancient cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-toma-piemontese-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Toma Piemontese (Alpine Wheel Cheese)",
        "category": "mains",
        "attribution": "Ancient Piedmont alpine tradition",
        "source_note": "Traditional Italian alpine cheesemaking",
        "description": "A centuries-old alpine cheese from Piedmont valleys, Toma is one of Italy's most ancient everyday cheeses. Made by shepherds in mountain huts using simple techniques passed down through generations.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "alpine pasture preferred"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "for dry salting"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk slowly to 90°F (32°C), stirring gently."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and stir gently for 1 minute."},
            {"step": 5, "text": "Let set for 40-50 minutes until clean break achieved."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes using traditional cross-hatch cuts."},
            {"step": 7, "text": "Stir gently for 10 minutes, letting curds heal."},
            {"step": 8, "text": "Slowly raise temperature to 104°F (40°C) over 30 minutes."},
            {"step": 9, "text": "Continue stirring until curds are firm and slightly squeaky."},
            {"step": 10, "text": "Drain whey and transfer curds to cloth-lined mold."},
            {"step": 11, "text": "Press at 10 lbs for 30 minutes, flip, press at 20 lbs for 2 hours."},
            {"step": 12, "text": "Flip again and press overnight at 30 lbs."},
            {"step": 13, "text": "Unmold and dry salt all surfaces, rubbing gently."},
            {"step": 14, "text": "Air dry for 2-3 days, turning twice daily."},
            {"step": 15, "text": "Age at 50-55°F with 85% humidity for 2-4 months, turning weekly."}
        ],
        "temperature": "90-104°F (32-40°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Toma means 'wheel' in Piedmontese dialect",
            "Young Toma is soft and mild; aged Toma develops nutty flavors",
            "Traditional versions use raw milk from a mix of morning and evening milkings",
            "Rind develops naturally - brush with dry cloth during aging"
        ],
        "tags": ["cheese", "italian", "alpine", "traditional", "piedmont", "aged"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-puzzone-di-moena-smelly",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Puzzone di Moena (Stinky Cheese of Moena)",
        "category": "mains",
        "attribution": "Ancient Trentino washed-rind tradition",
        "source_note": "Traditional Italian washed-rind cheesemaking",
        "description": "One of Italy's most pungent cheeses, Puzzone di Moena ('big stinker') has been made in the Fiemme and Fassa valleys since the 15th century. The powerful aroma belies a surprisingly delicate, sweet interior.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "high fat content"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for rind washing"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "brine solution", "quantity": "1", "unit": "gallon", "prep_note": "saturated salt brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C) and add starter culture."},
            {"step": 2, "text": "Ripen for 30 minutes with occasional stirring."},
            {"step": 3, "text": "Add diluted rennet and let set for 35-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently and raise temperature to 110°F (43°C) over 40 minutes."},
            {"step": 6, "text": "Continue stirring until curds shrink and firm up."},
            {"step": 7, "text": "Drain whey and pack curds firmly into molds."},
            {"step": 8, "text": "Press at increasing weights: 10 lbs for 1 hour, 20 lbs for 3 hours, 30 lbs overnight."},
            {"step": 9, "text": "Brine for 12-24 hours depending on size."},
            {"step": 10, "text": "Prepare wash: mix B. linens culture with small amount of brine."},
            {"step": 11, "text": "Age at 55°F with 95% humidity."},
            {"step": 12, "text": "Wash rind with bacteria solution every 2-3 days for first month."},
            {"step": 13, "text": "Continue washing weekly for 3-6 months total aging."},
            {"step": 14, "text": "Rind develops orange-pink color and strong aroma when ready."}
        ],
        "temperature": "95-110°F (35-43°C) for make; 55°F (13°C) for aging",
        "notes": [
            "The name literally means 'big stinker' in Italian",
            "Despite the powerful aroma, the paste is sweet and mild",
            "Protected by Slow Food Presidia designation",
            "Traditional makers washed with local well water containing natural bacteria"
        ],
        "tags": ["cheese", "italian", "washed-rind", "traditional", "stinky", "alpine"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-spressa-delle-giudicarie-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Spressa delle Giudicarie (Lean Ancient Cheese)",
        "category": "mains",
        "attribution": "Medieval Trentino poverty cheese",
        "source_note": "Traditional Italian low-fat cheesemaking",
        "description": "A unique 'poverty cheese' from the Giudicarie valleys of Trentino, made from skimmed milk after the cream was taken for butter. Despite humble origins, this medieval cheese developed complex flavors through long aging.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "6-24 months aging",
        "ingredients": [
            {"item": "partially skimmed cow's milk", "quantity": "2.5", "unit": "gallons", "prep_note": "traditionally after cream removed"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Let whole milk sit overnight so cream rises naturally."},
            {"step": 2, "text": "Skim cream (save for butter), use remaining milk for cheese."},
            {"step": 3, "text": "Heat skimmed milk to 93°F (34°C)."},
            {"step": 4, "text": "Add starter culture and ripen for 30 minutes."},
            {"step": 5, "text": "Add diluted rennet, stir gently, let set for 30-40 minutes."},
            {"step": 6, "text": "Cut curds into small 1/4-inch pieces."},
            {"step": 7, "text": "Raise temperature slowly to 113°F (45°C) over 45 minutes."},
            {"step": 8, "text": "Stir continuously as curds cook - this is crucial for texture."},
            {"step": 9, "text": "Let curds settle, drain most whey."},
            {"step": 10, "text": "Pack curds tightly into molds - no air pockets."},
            {"step": 11, "text": "Press heavily: 40-50 lbs pressure for 24 hours, flipping several times."},
            {"step": 12, "text": "Dry salt all surfaces generously."},
            {"step": 13, "text": "Age at 50°F with 80% humidity for minimum 6 months."},
            {"step": 14, "text": "Turn weekly, brush rind. Can age up to 24 months for intense flavor."}
        ],
        "temperature": "93-113°F (34-45°C) for make; 50°F (10°C) for aging",
        "notes": [
            "Name means 'pressed' referring to heavy pressing technique",
            "Low fat content requires longer aging for flavor development",
            "DOP protected since 2003",
            "Traditional wheels weigh 15-25 lbs and age up to 2 years",
            "Has a distinctive 'squeaky' texture when young"
        ],
        "tags": ["cheese", "italian", "alpine", "traditional", "low-fat", "aged", "medieval"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-bitto-storico-valtellina",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bitto Storico (Historic Valtellina Cheese)",
        "category": "mains",
        "attribution": "Celtic-origin alpine cheese tradition",
        "source_note": "Traditional Italian alpine cheesemaking with possible Celtic origins",
        "description": "One of Italy's oldest cheeses, Bitto Storico dates back to Celtic times in the Valtellina Alps. Made only in summer alpine pastures using traditional methods, it can age over 10 years. Historic Bitto is now protected by rebel cheesemakers who reject modern shortcuts.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "1-10+ years aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from alpine pasture, still warm"},
            {"item": "raw goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "from Orobica goats, 10-20% of total"},
            {"item": "natural calf rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "traditional preparation"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Traditionally made within 30 minutes of milking while milk still warm."},
            {"step": 2, "text": "Combine cow's milk with 10-20% goat's milk - no starter culture used."},
            {"step": 3, "text": "Milk should be at natural body temperature, about 95°F (35°C)."},
            {"step": 4, "text": "Add natural calf rennet prepared in traditional manner."},
            {"step": 5, "text": "Let set for 30-40 minutes until firm curd forms."},
            {"step": 6, "text": "Break curd using traditional 'spino' tool into rice-sized granules."},
            {"step": 7, "text": "Raise temperature to 118-125°F (48-52°C) over wood fire."},
            {"step": 8, "text": "Stir continuously for 30-40 minutes as curds cook."},
            {"step": 9, "text": "Let curds settle to bottom of copper cauldron."},
            {"step": 10, "text": "Gather curd mass with cloth and transfer to wooden mold."},
            {"step": 11, "text": "Press with traditional stone weights for 24 hours."},
            {"step": 12, "text": "Dry salt for several days, turning twice daily."},
            {"step": 13, "text": "Age in traditional 'casere' (stone cellars) at high humidity."},
            {"step": 14, "text": "Turn and care for wheels weekly. Minimum 70 days, ideally 2-10+ years."}
        ],
        "temperature": "95-125°F (35-52°C) for make; 45-50°F (7-10°C) for aging",
        "notes": [
            "Name may derive from Celtic 'bitu' meaning 'perennial'",
            "Bitto Storico rebels formed to preserve traditional methods against DOP modernization",
            "Must be made in alpine huts above 1400m elevation during summer",
            "Can age 10+ years - among the world's longest-aged cheeses",
            "Goat milk addition distinguishes historic version from commercial Bitto"
        ],
        "tags": ["cheese", "italian", "alpine", "traditional", "ancient", "celtic", "raw-milk"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-bagoss-bagolino-saffron",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bagòss (Bagolino Saffron Cheese)",
        "category": "mains",
        "attribution": "Medieval Lombard mountain tradition",
        "source_note": "Traditional Italian alpine cheesemaking with saffron",
        "description": "A rare mountain cheese from the village of Bagolino in the Brescia Alps, Bagòss has been made since at least the 1500s. Its distinctive golden interior comes from local saffron, a precious tradition that nearly died out but was revived.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4 hours",
        "total_time": "12-36 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Bruna Alpina cows"},
            {"item": "saffron threads", "quantity": "1/4", "unit": "tsp", "prep_note": "crushed, local tradition"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "raw linseed oil", "quantity": "2", "unit": "tbsp", "prep_note": "for rind treatment"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm saffron in small amount of milk for 30 minutes to extract color."},
            {"step": 2, "text": "Heat main milk to 95°F (35°C) in copper cauldron over wood fire."},
            {"step": 3, "text": "Add whey starter from previous batch."},
            {"step": 4, "text": "Add saffron-infused milk, stirring to distribute golden color."},
            {"step": 5, "text": "Add rennet and let set for 30-40 minutes."},
            {"step": 6, "text": "Break curds finely with traditional tool to grain size."},
            {"step": 7, "text": "Raise temperature to 120°F (49°C) over 45 minutes while stirring."},
            {"step": 8, "text": "Continue stirring until curds are firm and release whey easily."},
            {"step": 9, "text": "Let curds settle, gather in cloth."},
            {"step": 10, "text": "Pack into molds, press with heavy stones for 24 hours, flipping multiple times."},
            {"step": 11, "text": "Dry salt generously over several days."},
            {"step": 12, "text": "Age at 55°F with moderate humidity."},
            {"step": 13, "text": "Rub rind with raw linseed oil monthly to develop the dark brown coating."},
            {"step": 14, "text": "Age minimum 12 months, preferably 24-36 months for full complexity."}
        ],
        "temperature": "95-120°F (35-49°C) for make; 55°F (13°C) for aging",
        "notes": [
            "Only about 2,000 wheels made per year in Bagolino village",
            "Saffron tradition may date to medieval spice trade routes",
            "Linseed oil rind treatment creates distinctive dark brown exterior",
            "Protected by Slow Food Presidia",
            "Flavor combines mountain cheese nuttiness with saffron's floral notes"
        ],
        "tags": ["cheese", "italian", "alpine", "traditional", "saffron", "aged", "rare"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-canestrato-pugliese-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Canestrato Pugliese (Apulian Basket Cheese)",
        "category": "mains",
        "attribution": "Ancient Apulian sheep cheese tradition",
        "source_note": "Traditional southern Italian pecorino-style cheesemaking",
        "description": "An ancient sheep's milk cheese from Puglia, Canestrato takes its name from the woven rush baskets (canestri) used to mold it, leaving a distinctive imprint on the rind. This technique dates back to ancient Mediterranean pastoral traditions.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3 hours",
        "total_time": "2-10 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Gentile or Merino sheep"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or natural whey"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional artisan rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "local extra virgin, for rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 99°F (37°C) - slightly warmer than cow's milk cheeses."},
            {"step": 2, "text": "Add culture or natural whey starter, ripen 15-20 minutes."},
            {"step": 3, "text": "Add lamb rennet paste dissolved in small amount of water."},
            {"step": 4, "text": "Let set for 20-30 minutes until firm."},
            {"step": 5, "text": "Break curds to hazelnut size using traditional tools."},
            {"step": 6, "text": "Let curds rest under whey for 10 minutes."},
            {"step": 7, "text": "Raise temperature to 118°F (48°C), stirring gently."},
            {"step": 8, "text": "When curds are firm and squeaky, drain whey."},
            {"step": 9, "text": "Pack curds into traditional woven rush baskets (or basket-lined molds)."},
            {"step": 10, "text": "Press lightly, allowing basket weave pattern to imprint."},
            {"step": 11, "text": "Press 2-4 hours, flipping several times."},
            {"step": 12, "text": "Brine for 8-12 hours or dry salt over 2-3 days."},
            {"step": 13, "text": "Age at 50-55°F with 80-85% humidity."},
            {"step": 14, "text": "Rub with olive oil occasionally. Age 2 months for fresh, up to 10 months for aged."}
        ],
        "temperature": "99-118°F (37-48°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "DOP protected since 1996",
            "Rush basket molds create distinctive crosshatch rind pattern",
            "Young versions are mild; aged versions develop sharp, piquant flavors",
            "Traditional in Pugliese dishes with fava beans and pasta",
            "Olive oil treatment keeps rind supple and adds regional character"
        ],
        "tags": ["cheese", "italian", "sheep", "traditional", "puglia", "pecorino", "basket"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-fiore-sardo-sardinian-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fiore Sardo (Sardinian Flower Cheese)",
        "category": "mains",
        "attribution": "Bronze Age Sardinian shepherd tradition",
        "source_note": "Ancient Sardinian raw milk sheep cheese",
        "description": "Perhaps the oldest continuously-made cheese in the Mediterranean, Fiore Sardo dates back to the Bronze Age nuragic civilization of Sardinia. Still made by shepherds in mountain huts using methods unchanged for millennia, it is smoke-dried over aromatic wood.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-8 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Sarda breed sheep"},
            {"item": "lamb or kid rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional artisan preparation"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "sea salt preferred"},
            {"item": "aromatic wood", "quantity": "as needed", "unit": "", "prep_note": "olive, myrtle, or rosemary for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Use milk fresh from morning and evening milkings, still warm."},
            {"step": 2, "text": "Heat milk to 95°F (35°C) if not already warm."},
            {"step": 3, "text": "Add artisan lamb or kid rennet paste - no starter cultures traditionally used."},
            {"step": 4, "text": "Let set for 30-40 minutes until firm curd forms."},
            {"step": 5, "text": "Break curd finely using traditional wooden tool."},
            {"step": 6, "text": "Let curds settle, then gather and pack into carved wooden molds."},
            {"step": 7, "text": "Traditional molds have flower design on bottom - hence 'fiore' name."},
            {"step": 8, "text": "Press by hand and under light weights for several hours."},
            {"step": 9, "text": "Scald surface briefly with hot whey - traditional treatment."},
            {"step": 10, "text": "Dry salt all surfaces over 2-3 days."},
            {"step": 11, "text": "Smoke gently over aromatic wood (olive, myrtle, rosemary) for 10-15 days."},
            {"step": 12, "text": "Move to aging room at 50-55°F after smoking complete."},
            {"step": 13, "text": "Age minimum 3 months for table cheese, 6-8 months for grating."},
            {"step": 14, "text": "Rub rind with olive oil and sheep fat during aging."}
        ],
        "temperature": "95°F (35°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "Name means 'flower of Sardinia' from flower-stamped molds",
            "One of only two Sardinian DOP cheeses",
            "Nuragic people may have made this cheese 3,500 years ago",
            "Smoking was originally for preservation in shepherd huts",
            "Has distinctive smoky, sheepy, slightly piquant flavor"
        ],
        "tags": ["cheese", "italian", "sheep", "traditional", "sardinian", "ancient", "smoked"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-vastedda-della-valle-del-belice",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vastedda della Valle del Belìce (Sicilian Stretched Sheep Cheese)",
        "category": "mains",
        "attribution": "Ancient Sicilian stretched-curd sheep cheese",
        "source_note": "Traditional Sicilian pasta filata from sheep's milk",
        "description": "A rare and ancient stretched-curd (pasta filata) cheese made from sheep's milk in Sicily's Belìce Valley. Unlike most stretched cheeses which use cow's milk, Vastedda represents an older tradition where sheep's milk was the norm.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1-3 days fresh",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Valle del Belìce sheep"},
            {"item": "natural whey starter", "quantity": "1/4", "unit": "cup", "prep_note": "from previous batch, acidic"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 100°F (38°C)."},
            {"step": 2, "text": "Add acidic whey starter from previous batch."},
            {"step": 3, "text": "Add lamb rennet paste, stir, and let set 30-40 minutes."},
            {"step": 4, "text": "Break curd coarsely with hands or wooden tool."},
            {"step": 5, "text": "Let curds sit under warm whey for 3-4 hours to acidify."},
            {"step": 6, "text": "Test acidity: curd should stretch when heated. If not, wait longer."},
            {"step": 7, "text": "Cut acidified curd into strips."},
            {"step": 8, "text": "Heat water or whey to 175°F (80°C)."},
            {"step": 9, "text": "Submerge curd strips in hot liquid."},
            {"step": 10, "text": "When curd becomes pliable, stretch and fold repeatedly."},
            {"step": 11, "text": "Work quickly - sheep's milk is more difficult to stretch than cow's."},
            {"step": 12, "text": "Form into characteristic flat, bread-loaf shape."},
            {"step": 13, "text": "Briefly brine or salt surface lightly."},
            {"step": 14, "text": "Eat fresh within 1-3 days - does not age well."}
        ],
        "temperature": "100°F (38°C) for curd; 175°F (80°C) for stretching",
        "notes": [
            "Name may derive from Arabic 'bastarda' or Sicilian word for bread",
            "One of very few sheep's milk pasta filata cheeses in the world",
            "Slow Food Presidia protected to prevent extinction",
            "Only a handful of producers remain in the Belìce Valley",
            "Flavor is intensely sheepy with slight acidic tang"
        ],
        "tags": ["cheese", "italian", "sheep", "traditional", "sicilian", "pasta-filata", "fresh", "rare"],
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
