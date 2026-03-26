#!/usr/bin/env python3
"""Add batch 38 of traditional cheese recipes - More ancient and prehistoric cheese traditions."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-roquefort-french-king-blues",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Roquefort (French King of Blues)",
        "category": "mains",
        "attribution": "Roquefort-sur-Soulzon, France / 79 AD",
        "source_note": "Legend says a shepherd left bread and sheep cheese in a cave while pursuing a maiden. Mentioned by Pliny the Elder in 79 AD.",
        "description": "French sheep milk blue cheese aged in the natural caves of Roquefort, with creamy texture and sharp, tangy blue flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "3", "unit": "gallons", "prep_note": "Lacaune breed traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "from Roquefort caves"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 1 hour."},
            {"step": 3, "text": "Add lamb rennet and let set for 2 hours."},
            {"step": 4, "text": "Cut curds into large 1-inch cubes."},
            {"step": 5, "text": "Let curds rest 15 minutes, then gently ladle into cylindrical molds."},
            {"step": 6, "text": "Do not press - allow to drain naturally for 3-5 days, turning regularly."},
            {"step": 7, "text": "Dry salt all surfaces."},
            {"step": 8, "text": "Age at 45-50°F in very humid conditions (95%+)."},
            {"step": 9, "text": "Pierce with needles after 3-4 weeks for air to reach mold."},
            {"step": 10, "text": "Age in cave conditions for 3-6 months."},
            {"step": 11, "text": "Wrap in foil to stop further bluing when desired level reached."}
        ],
        "temperature": "86°F make, 45-50°F cave aging",
        "notes": [
            "First cheese granted AOC protection in France (1925)",
            "Must be aged in natural caves of Roquefort-sur-Soulzon",
            "The P. roqueforti spores come from bread left in the caves",
            "Sheep milk only - any cow milk disqualifies it as Roquefort"
        ],
        "tags": ["cheese", "traditional", "french", "blue", "sheep", "cave-aged", "ancient", "aoc", "79ad"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-emmental-swiss-holes",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Emmentaler (Swiss Cheese with Eyes)",
        "category": "mains",
        "attribution": "Emmental Valley, Switzerland / 13th Century",
        "source_note": "First documented in 1293, the original 'Swiss cheese'. The distinctive large eyes come from Propionibacteria.",
        "description": "Classic Swiss cheese with large holes (eyes), mild sweet nutty flavor, and firm elastic texture.",
        "servings_yield": "About 10 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "4-12 months aging",
        "total_time": "4-12 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "8", "unit": "gallons", "prep_note": "from grass-fed cows"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium freudenreichii", "quantity": "1/8", "unit": "tsp", "prep_note": "for eye formation"},
            {"item": "liquid rennet", "quantity": "1.5", "unit": "tsp", "prep_note": "calf rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F in large copper kettle."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacteria. Ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30 minutes."},
            {"step": 4, "text": "Cut curds to wheat grain size using cheese harp."},
            {"step": 5, "text": "Stir constantly while heating slowly to 125°F over 45 minutes."},
            {"step": 6, "text": "Continue stirring at 125°F for 30 more minutes."},
            {"step": 7, "text": "Let curds settle briefly, gather in cheesecloth."},
            {"step": 8, "text": "Transfer to large wheel mold and press at 50 lbs, increasing to 100 lbs over 24 hours."},
            {"step": 9, "text": "Soak in brine for 2-3 days."},
            {"step": 10, "text": "Age 2-3 weeks at 55°F (cool room)."},
            {"step": 11, "text": "Move to warm room at 70-77°F for 4-8 weeks for eye development."},
            {"step": 12, "text": "Return to cool aging at 55°F for 4-12 months total."}
        ],
        "temperature": "90-125°F make, 55°F and 70-77°F aging",
        "notes": [
            "The 'warm room' phase is crucial for eye (hole) development",
            "Propionibacteria produce CO2 which forms the characteristic eyes",
            "Traditional wheels are enormous - 200 lbs or more",
            "AOC protected in Switzerland since 2006"
        ],
        "tags": ["cheese", "traditional", "swiss", "eyes", "holes", "13th-century", "emmental", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-comte-french-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Comté (French Gruyère-Style)",
        "category": "mains",
        "attribution": "Franche-Comté, France / 12th Century",
        "source_note": "Made in the Jura Mountains since the 12th century. France's most popular AOC cheese.",
        "description": "French alpine cheese with a firm texture, complex nutty caramel flavor, and subtle sweetness from mountain pastures.",
        "servings_yield": "About 8 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "4-18 months aging",
        "total_time": "4-18 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "6", "unit": "gallons", "prep_note": "Montbéliarde or Simmental cattle"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium", "quantity": "1/16", "unit": "tsp", "prep_note": "for small eyes"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "calf rennet"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F in copper vat."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacteria. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 30 minutes."},
            {"step": 4, "text": "Cut curds to corn kernel size."},
            {"step": 5, "text": "Stir while heating to 130°F over 40 minutes."},
            {"step": 6, "text": "Hold at 130°F, stirring, for 30 more minutes."},
            {"step": 7, "text": "Transfer curds to large round mold."},
            {"step": 8, "text": "Press at 40 lbs for 30 minutes, 70 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 2 days."},
            {"step": 10, "text": "Age at 55°F, 95% humidity."},
            {"step": 11, "text": "Rub rind with salt water (morge) twice weekly."},
            {"step": 12, "text": "Age minimum 4 months, preferably 12-18 months."}
        ],
        "temperature": "90-130°F make, 55°F aging",
        "notes": [
            "France's most produced AOC cheese",
            "Strict rules: no silage feed, specific cow breeds only",
            "Flavor varies by season - summer milk produces different taste",
            "Each wheel is graded by expert affineurs on 20-point scale"
        ],
        "tags": ["cheese", "traditional", "french", "alpine", "12th-century", "jura", "aoc", "gruyere-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-manchego-spanish-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Manchego (Spanish La Mancha Sheep Cheese)",
        "category": "mains",
        "attribution": "La Mancha, Spain / Ancient Iberian",
        "source_note": "Made in La Mancha since Bronze Age times. Named after the Manchega sheep breed and immortalized in Don Quixote.",
        "description": "Spanish sheep milk cheese with a distinctive herringbone rind pattern, rich buttery flavor, and slightly piquant finish.",
        "servings_yield": "About 3 lbs wheel",
        "prep_time": "3 hours",
        "cook_time": "2-12 months aging",
        "total_time": "2-12 months",
        "ingredients": [
            {"item": "raw Manchega sheep milk", "quantity": "3", "unit": "gallons", "prep_note": "or other sheep milk"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup", "prep_note": "for rubbing rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 6, "text": "Stir gently while heating to 104°F over 30 minutes."},
            {"step": 7, "text": "Drain curds and pack into molds with herringbone (pleita) pattern."},
            {"step": 8, "text": "Press at 25 lbs for 1 hour, 50 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 24 hours."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "Rub rind with olive oil weekly."},
            {"step": 12, "text": "Age 2 months (semi-curado), 6 months (curado), or 12+ months (viejo)."}
        ],
        "temperature": "86-104°F make, 55°F aging",
        "notes": [
            "The distinctive herringbone pattern comes from traditional esparto grass molds",
            "Must be made from Manchega sheep milk for DO protection",
            "Bronze Age cheese molds found in La Mancha archaeological sites",
            "Rubbing with olive oil creates the dark oiled rind"
        ],
        "tags": ["cheese", "traditional", "spanish", "sheep", "la-mancha", "ancient", "do", "herringbone"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queijo-serra-da-estrela-portuguese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo Serra da Estrela (Portuguese Mountain Cheese)",
        "category": "mains",
        "attribution": "Serra da Estrela, Portugal / Ancient",
        "source_note": "Portugal's most famous cheese, made in the Estrela Mountains using cardoon thistle as coagulant since ancient times.",
        "description": "Portuguese sheep cheese with a creamy to runny interior, made with thistle rennet, featuring complex earthy and slightly bitter flavors.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "raw Bordaleira sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "or other sheep milk"},
            {"item": "dried cardoon thistle", "quantity": "2", "unit": "tbsp", "prep_note": "crushed flowers"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Soak crushed cardoon thistle flowers in 1/4 cup warm water for 2-3 hours."},
            {"step": 2, "text": "Strain to get thistle extract."},
            {"step": 3, "text": "Heat sheep milk to 82-86°F (lower than typical)."},
            {"step": 4, "text": "Add thistle extract slowly while stirring."},
            {"step": 5, "text": "Let set for 1-2 hours until soft curd forms."},
            {"step": 6, "text": "Cut curds gently into large pieces."},
            {"step": 7, "text": "Ladle into flat round molds, press very lightly."},
            {"step": 8, "text": "Turn several times over 24-48 hours."},
            {"step": 9, "text": "Salt surfaces."},
            {"step": 10, "text": "Wrap circumference with cloth band (cincho)."},
            {"step": 11, "text": "Age at 50-55°F, 90% humidity for 4-8 weeks."},
            {"step": 12, "text": "Rind wrinkles as interior becomes soft to runny."}
        ],
        "temperature": "82-86°F make, 50-55°F aging",
        "notes": [
            "Thistle (cardoon) rennet creates the signature soft/runny interior",
            "The cloth band maintains shape as interior softens",
            "Cut off top and scoop out with spoon when ripe",
            "PDO protected - must use specific sheep breeds and thistle"
        ],
        "tags": ["cheese", "traditional", "portuguese", "sheep", "thistle-rennet", "mountain", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-majorero-canary",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Majorero (Canary Islands Goat Cheese)",
        "category": "mains",
        "attribution": "Fuerteventura, Canary Islands / Pre-Hispanic",
        "source_note": "Made by the Majos (indigenous Guanches) before Spanish conquest. Uses milk from the Majorera goat unique to the island.",
        "description": "Canary Islands goat cheese from Fuerteventura with a distinctive palm leaf pattern, ranging from mild when young to sharp when aged.",
        "servings_yield": "About 4 lbs wheel",
        "prep_time": "3 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "raw Majorera goat milk", "quantity": "3", "unit": "gallons", "prep_note": "or other goat milk"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "pimentón", "quantity": "2", "unit": "tbsp", "prep_note": "smoked paprika, for rind"},
            {"item": "gofio", "quantity": "2", "unit": "tbsp", "prep_note": "roasted flour, optional for rind"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds into small pieces."},
            {"step": 5, "text": "Stir gently while heating to 100°F over 20 minutes."},
            {"step": 6, "text": "Drain curds and pack into molds with palm leaf (pleita) pattern."},
            {"step": 7, "text": "Press at 30 lbs for 6 hours, 50 lbs for 12 hours."},
            {"step": 8, "text": "Soak in brine for 24 hours."},
            {"step": 9, "text": "Age at 55°F, 85% humidity."},
            {"step": 10, "text": "Rub rind with olive oil mixed with pimentón (or gofio)."},
            {"step": 11, "text": "Age 2 months (tierno), 4 months (semi-curado), or 6+ months (curado)."}
        ],
        "temperature": "86-100°F make, 55°F aging",
        "notes": [
            "The Majorera goat is native only to Fuerteventura",
            "Pre-Hispanic Majos people made this cheese before Spanish arrival",
            "Rind can be rubbed with paprika (red), gofio (yellow), or oil (natural)",
            "PDO protected since 1996"
        ],
        "tags": ["cheese", "traditional", "spanish", "canary-islands", "goat", "pre-hispanic", "pdo", "majorero"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-camembert-norman",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Camembert de Normandie (French Bloomy-Rind)",
        "category": "mains",
        "attribution": "Normandy, France / 1791",
        "source_note": "Created by Marie Harel in 1791 in the village of Camembert. The round wooden box was invented in 1890.",
        "description": "French soft-ripened cheese with a bloomy white rind, creamy to runny interior, and earthy mushroom flavors.",
        "servings_yield": "About 8 oz round",
        "prep_time": "2 hours",
        "cook_time": "3-5 weeks aging",
        "total_time": "3-5 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "1", "unit": "gallon", "prep_note": "Norman breed ideal"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": "very small amount"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture, P. candidum, and G. candidum. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed."},
            {"step": 4, "text": "Add small amount of diluted rennet."},
            {"step": 5, "text": "Let set for 1.5-2 hours until soft curd forms."},
            {"step": 6, "text": "Ladle curds gently into Camembert molds (4 inch diameter) - 5 ladles per fill."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, turning several times."},
            {"step": 8, "text": "Unmold and salt all surfaces."},
            {"step": 9, "text": "Age at 52-55°F, 90% humidity."},
            {"step": 10, "text": "White mold develops in 7-10 days."},
            {"step": 11, "text": "Age 3-5 weeks until interior is soft to runny."}
        ],
        "temperature": "90°F make, 52-55°F aging",
        "notes": [
            "Created during the French Revolution by Marie Harel",
            "True Camembert de Normandie is raw milk only (AOC)",
            "The iconic round wooden box was invented by engineer Ridel",
            "Interior should be creamy but not chalky or ammoniac"
        ],
        "tags": ["cheese", "traditional", "french", "norman", "bloomy-rind", "soft-ripened", "1791", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mozzarella-di-bufala-campana",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mozzarella di Bufala Campana (Italian Water Buffalo)",
        "category": "mains",
        "attribution": "Campania, Italy / 12th Century",
        "source_note": "Made from water buffalo milk since at least the 12th century. 'Mozzare' means to cut, referring to the stretching process.",
        "description": "Italian stretched-curd cheese made from water buffalo milk, with a porcelain-white color, elastic texture, and sweet milky flavor.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "Same day",
        "total_time": "4-5 hours",
        "ingredients": [
            {"item": "fresh water buffalo milk", "quantity": "1", "unit": "gallon", "prep_note": "or whole cow milk"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp", "prep_note": "dissolved in water"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup cool water."},
            {"step": 2, "text": "Add citric acid solution to cold milk, stir well."},
            {"step": 3, "text": "Heat milk to 90°F while stirring gently."},
            {"step": 4, "text": "Add diluted rennet, stir for 30 seconds."},
            {"step": 5, "text": "Let set for 5-10 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1-inch cubes."},
            {"step": 7, "text": "Heat slowly to 105°F while stirring gently."},
            {"step": 8, "text": "Drain curds and let rest until pH drops to 5.2 (stretches in hot water)."},
            {"step": 9, "text": "Heat water to 170-180°F."},
            {"step": 10, "text": "Cut curd into pieces, place in hot water. Stretch and fold until smooth and elastic."},
            {"step": 11, "text": "Form into balls while stretching. Pinch off (mozzare) to form individual pieces."},
            {"step": 12, "text": "Place immediately in cold salt water. Store in brine and eat within 1-2 days."}
        ],
        "temperature": "90-105°F make, 170-180°F stretching",
        "notes": [
            "Water buffalo were introduced to Italy from Asia in the Middle Ages",
            "Buffalo milk has higher fat and protein than cow milk",
            "Must be eaten very fresh - ideally within 24 hours",
            "DOP protected - true buffalo mozzarella from Campania only"
        ],
        "tags": ["cheese", "traditional", "italian", "fresh", "stretched-curd", "water-buffalo", "12th-century", "dop"],
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
