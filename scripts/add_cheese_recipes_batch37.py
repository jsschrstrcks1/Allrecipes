#!/usr/bin/env python3
"""Add batch 37 of traditional cheese recipes - More monastery and ancient European cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-abbaye-de-belloc-basque",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Abbaye de Belloc (Basque Monastery Cheese)",
        "category": "mains",
        "attribution": "Basque Country, France / 1969 (Ancient Tradition)",
        "source_note": "Made by Benedictine monks at the Abbey of Notre-Dame de Belloc, continuing ancient Pyrenean sheep cheese traditions.",
        "description": "Basque monastery sheep cheese with a natural brushed rind, firm paste, and rich nutty flavor with caramel notes.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "4-6 months aging",
        "total_time": "4-6 months",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "4", "unit": "gallons", "prep_note": "Manech breed traditional"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh sheep milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 40 minutes."},
            {"step": 4, "text": "Cut curds to corn kernel size."},
            {"step": 5, "text": "Stir gently while heating to 104°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at 104°F for 30 more minutes."},
            {"step": 7, "text": "Drain curds and pack into large round mold."},
            {"step": 8, "text": "Press at 30 lbs for 1 hour, 50 lbs for 12 hours."},
            {"step": 9, "text": "Soak in saturated brine for 3 days."},
            {"step": 10, "text": "Age at 55°F, 85% humidity."},
            {"step": 11, "text": "Brush rind weekly to develop natural brown coat."},
            {"step": 12, "text": "Age 4-6 months until paste is firm and golden."}
        ],
        "temperature": "90-104°F make, 55°F aging",
        "notes": [
            "Monks have made this cheese at the abbey since 1969",
            "Continues the ancient Pyrenean sheep cheese tradition",
            "Rich sheep milk creates caramel and lanolin notes",
            "The monks pray as they work - cheese as meditation"
        ],
        "tags": ["cheese", "traditional", "french", "basque", "monastery", "sheep", "aged", "benedictine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gorgonzola-italian-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gorgonzola (Italian Creamy Blue)",
        "category": "mains",
        "attribution": "Lombardy/Piedmont, Italy / 9th Century",
        "source_note": "Named after the town of Gorgonzola near Milan. One of the world's oldest blue cheeses, made since 879 AD.",
        "description": "Italian blue cheese with a creamy to crumbly texture depending on age, and complex spicy, tangy blue flavor.",
        "servings_yield": "About 3 lbs",
        "prep_time": "3 hours",
        "cook_time": "2-4 months aging",
        "total_time": "2-4 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and P. roqueforti. Ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Let curds rest 15 minutes, then stir gently."},
            {"step": 7, "text": "Drain whey and ladle curds into cylindrical mold - do not press."},
            {"step": 8, "text": "Turn every 2 hours for first 12 hours, then twice daily for 4 days."},
            {"step": 9, "text": "Salt surfaces and age at 50-55°F, 95% humidity."},
            {"step": 10, "text": "Pierce with needles after 4 weeks to allow air for bluing."},
            {"step": 11, "text": "Age 2 months for Dolce (creamy), 3-4 months for Piccante (crumbly)."}
        ],
        "temperature": "86°F make, 50-55°F aging",
        "notes": [
            "One of the world's oldest blue cheeses, documented since 879 AD",
            "Dolce (sweet/young) is creamy; Piccante (aged) is crumbly and stronger",
            "Never pressed - the open texture allows blue mold to spread",
            "DOP protected - must be made in Lombardy or Piedmont"
        ],
        "tags": ["cheese", "traditional", "italian", "blue", "9th-century", "lombardy", "dop", "creamy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-taleggio-italian-washed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Taleggio (Italian Cave-Aged Washed-Rind)",
        "category": "mains",
        "attribution": "Val Taleggio, Lombardy / 10th Century",
        "source_note": "Named after the Val Taleggio valley where it originated. Aged in caves for the cool humid conditions.",
        "description": "Italian washed-rind cheese with a pungent orange rind, soft creamy interior, and tangy fruity flavor.",
        "servings_yield": "About 2 lbs square",
        "prep_time": "3 hours",
        "cook_time": "5-7 weeks aging",
        "total_time": "5-7 weeks",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and B. linens. Ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 1 hour."},
            {"step": 5, "text": "Cut curds into 1-inch cubes."},
            {"step": 6, "text": "Stir very gently for 10 minutes at 90°F."},
            {"step": 7, "text": "Ladle curds into square molds (8x8 inches)."},
            {"step": 8, "text": "Turn frequently for 24 hours, letting drain naturally."},
            {"step": 9, "text": "Salt and dry for 2 days."},
            {"step": 10, "text": "Age at 50-55°F, 95% humidity."},
            {"step": 11, "text": "Wash with brine every 2-3 days."},
            {"step": 12, "text": "Age 5-7 weeks until rind is orange and paste is soft."}
        ],
        "temperature": "90°F make, 50-55°F aging",
        "notes": [
            "Traditionally aged in the caves of Val Taleggio",
            "The square shape with distinctive 'T' stamp identifies authentic Taleggio",
            "Pungent aroma belies a mild, fruity taste",
            "DOP protected since 1988"
        ],
        "tags": ["cheese", "traditional", "italian", "washed-rind", "10th-century", "lombardy", "dop", "cave-aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-asiago-italian-mountain",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Asiago (Italian Alpine Cheese)",
        "category": "mains",
        "attribution": "Asiago Plateau, Veneto / 10th Century",
        "source_note": "Originally a sheep cheese, made on the Asiago plateau since around 1000 AD. Now made from cow milk.",
        "description": "Italian alpine cheese ranging from fresh and mild (Fresco) to aged and sharp (Stravecchio), with DOP protection.",
        "servings_yield": "About 3 lbs wheel",
        "prep_time": "3 hours",
        "cook_time": "2-18 months aging",
        "total_time": "2-18 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": "alpine pasture ideal"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 30 minutes."},
            {"step": 5, "text": "Cut curds to corn kernel size."},
            {"step": 6, "text": "Stir gently while heating to 115°F over 30 minutes."},
            {"step": 7, "text": "Continue stirring at 115°F for 20 more minutes."},
            {"step": 8, "text": "Drain curds and pack into round mold."},
            {"step": 9, "text": "Press at 25 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 10, "text": "Soak in brine for 2 days."},
            {"step": 11, "text": "Age at 55°F, 85% humidity."},
            {"step": 12, "text": "Fresco: 20-40 days. Mezzano: 4-6 months. Stravecchio: 15-18 months."}
        ],
        "temperature": "95-115°F make, 55°F aging",
        "notes": [
            "Originally made from sheep milk on the Asiago plateau",
            "Transitioned to cow milk as cattle became dominant",
            "Four official age categories: Fresco, Mezzano, Vecchio, Stravecchio",
            "DOP protected - must be from specific alpine regions"
        ],
        "tags": ["cheese", "traditional", "italian", "alpine", "10th-century", "veneto", "dop", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fontina-valdaostan-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fontina Val d'Aosta (Italian Mountain Cheese)",
        "category": "mains",
        "attribution": "Aosta Valley, Italy / 12th Century",
        "source_note": "Made in the Aosta Valley since at least 1270. The original Italian fondue cheese.",
        "description": "Italian mountain cheese with a washed rind, semi-soft texture, and complex nutty, earthy flavor with hints of truffle.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-4 months aging",
        "total_time": "3-4 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "4", "unit": "gallons", "prep_note": "Valdaostan cattle milk"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "calf rennet"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh raw milk to 97°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add diluted rennet and let set for 40 minutes."},
            {"step": 4, "text": "Cut curds to hazelnut size."},
            {"step": 5, "text": "Stir gently while heating to 118°F over 30 minutes."},
            {"step": 6, "text": "Continue stirring at 118°F for 15 more minutes."},
            {"step": 7, "text": "Transfer curds to large round mold."},
            {"step": 8, "text": "Press at 25 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 9, "text": "Soak in brine for 3 days."},
            {"step": 10, "text": "Age in traditional caves or cellar at 50-55°F, 90% humidity."},
            {"step": 11, "text": "Brush rind with brine every few days."},
            {"step": 12, "text": "Age 3-4 months until paste is supple with small eyes."}
        ],
        "temperature": "97-118°F make, 50-55°F aging",
        "notes": [
            "First mentioned in documents from 1270",
            "Must be made from single milking of Valdaostan cattle",
            "The original Italian fondue cheese - called 'fonduta'",
            "DOP protected - true Fontina only from Valle d'Aosta"
        ],
        "tags": ["cheese", "traditional", "italian", "alpine", "12th-century", "aosta", "dop", "fondue"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-parmigiano-reggiano-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Parmigiano-Reggiano (Italian King of Cheeses)",
        "category": "mains",
        "attribution": "Emilia-Romagna, Italy / 12th Century",
        "source_note": "Made by Benedictine and Cistercian monks since the Middle Ages. Unchanged for nearly 1000 years.",
        "description": "The original hard Italian grating cheese, aged minimum 12 months with a crystalline texture and rich umami flavor.",
        "servings_yield": "About 10 lbs wheel (home scale)",
        "prep_time": "5 hours",
        "cook_time": "12-36 months aging",
        "total_time": "12-36 months",
        "ingredients": [
            {"item": "raw cow milk (evening, skimmed)", "quantity": "4", "unit": "gallons", "prep_note": "partially skimmed"},
            {"item": "raw cow milk (morning, whole)", "quantity": "4", "unit": "gallons", "prep_note": "fresh whole milk"},
            {"item": "natural whey starter", "quantity": "1", "unit": "cup", "prep_note": "from previous batch"},
            {"item": "calf rennet", "quantity": "1.5", "unit": "tsp", "prep_note": "traditional calf rennet only"},
            {"item": "cheese salt", "quantity": "3", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Let evening milk rest overnight; skim cream from surface in morning."},
            {"step": 2, "text": "Combine skimmed evening milk with fresh morning whole milk."},
            {"step": 3, "text": "Heat combined milk to 91°F in copper cauldron."},
            {"step": 4, "text": "Add natural whey starter and stir."},
            {"step": 5, "text": "Add calf rennet and let set for 10-12 minutes."},
            {"step": 6, "text": "Break curds into rice-grain sized pieces using a 'spino' (traditional cutter)."},
            {"step": 7, "text": "Cook curds, stirring, raising temperature to 131°F over 15 minutes."},
            {"step": 8, "text": "Let curds settle to bottom for 45-60 minutes."},
            {"step": 9, "text": "Lift curd mass in cheesecloth, divide into two portions."},
            {"step": 10, "text": "Place in round molds with 'Parmigiano-Reggiano' stencil."},
            {"step": 11, "text": "Press for 2-3 days, turning regularly."},
            {"step": 12, "text": "Soak in saturated brine for 20-25 days."},
            {"step": 13, "text": "Age at 60-65°F, 85% humidity for minimum 12 months."},
            {"step": 14, "text": "Turn and brush weekly. Age 24-36 months for stravecchio."}
        ],
        "temperature": "91-131°F make, 60-65°F aging",
        "notes": [
            "Strict DOP regulations control every aspect of production",
            "Only partially skimmed evening milk combined with whole morning milk",
            "No additives permitted - only milk, salt, and rennet",
            "Each wheel is numbered and inspected before selling",
            "Crystalline texture from protein breakdown during aging"
        ],
        "tags": ["cheese", "traditional", "italian", "hard", "12th-century", "emilia-romagna", "dop", "grating", "king-of-cheeses"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-grana-padano-po-valley",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Grana Padano (Italian Po Valley Hard Cheese)",
        "category": "mains",
        "attribution": "Po Valley, Italy / 12th Century",
        "source_note": "Created by Cistercian monks at Chiaravalle Abbey around 1135. 'Grana' means grain, referring to the granular texture.",
        "description": "Italian hard grating cheese from the Po Valley, similar to Parmigiano-Reggiano but with slightly milder, sweeter flavor.",
        "servings_yield": "About 8 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "9-24 months aging",
        "total_time": "9-24 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "6", "unit": "gallons", "prep_note": "partially skimmed"},
            {"item": "natural whey starter", "quantity": "1", "unit": "cup", "prep_note": "or thermophilic culture"},
            {"item": "calf rennet", "quantity": "1.5", "unit": "tsp", "prep_note": ""},
            {"item": "lysozyme", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, traditional uses egg white"},
            {"item": "cheese salt", "quantity": "2", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Partially skim fresh milk and heat to 90°F in copper vat."},
            {"step": 2, "text": "Add whey starter (or thermophilic culture)."},
            {"step": 3, "text": "Add lysozyme if using (prevents late blowing)."},
            {"step": 4, "text": "Add calf rennet and let set for 8-12 minutes."},
            {"step": 5, "text": "Break curds into rice-grain sized pieces."},
            {"step": 6, "text": "Cook while stirring, raising temperature to 127°F."},
            {"step": 7, "text": "Let curds settle for 50-70 minutes."},
            {"step": 8, "text": "Lift curd mass in cheesecloth and place in mold with marking band."},
            {"step": 9, "text": "Press for 2 days, turning regularly."},
            {"step": 10, "text": "Soak in brine for 14-30 days."},
            {"step": 11, "text": "Age at 60°F, 85% humidity for minimum 9 months."},
            {"step": 12, "text": "Age 20-24 months for 'Riserva' quality."}
        ],
        "temperature": "90-127°F make, 60°F aging",
        "notes": [
            "Created by monks to preserve surplus milk from Po Valley dairy farms",
            "Lysozyme (from egg white) is permitted to prevent late blowing",
            "Slightly lower cooking temperature than Parmigiano-Reggiano",
            "DOP protected with production across northern Italy"
        ],
        "tags": ["cheese", "traditional", "italian", "hard", "12th-century", "po-valley", "dop", "grating", "cistercian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sbrinz-swiss-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sbrinz (Swiss Ancient Hard Cheese)",
        "category": "mains",
        "attribution": "Central Switzerland / 16th Century or Earlier",
        "source_note": "Possibly Switzerland's oldest cheese, traded over the Gotthard Pass. May predate Parmesan.",
        "description": "Swiss extra-hard cheese traditionally shaved rather than grated, with intense aromatic flavor after 18+ months aging.",
        "servings_yield": "About 6 lbs wheel",
        "prep_time": "5 hours",
        "cook_time": "18-36 months aging",
        "total_time": "18-36 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "5", "unit": "gallons", "prep_note": "alpine pasture milk"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calf rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh alpine milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 20 minutes."},
            {"step": 3, "text": "Add calf rennet and let set for 30-35 minutes."},
            {"step": 4, "text": "Cut curds very fine, to rice-grain size."},
            {"step": 5, "text": "Cook while stirring continuously, raising to 135°F over 45 minutes."},
            {"step": 6, "text": "Hold at 135°F, stirring, for 30 more minutes."},
            {"step": 7, "text": "Let curds settle briefly, then transfer to mold."},
            {"step": 8, "text": "Press at 50 lbs for 1 hour, 80 lbs for 12-24 hours."},
            {"step": 9, "text": "Soak in brine for 3-4 weeks."},
            {"step": 10, "text": "Age first 6 months at 60°F, 85% humidity."},
            {"step": 11, "text": "Then age 12-30 more months at 55°F, 75% humidity."},
            {"step": 12, "text": "Ready minimum 18 months, traditionally 2-3 years."}
        ],
        "temperature": "90-135°F make, 55-60°F aging",
        "notes": [
            "May predate Parmesan as one of the oldest alpine hard cheeses",
            "Traditionally shaved thin with a special knife (hobelkäse)",
            "The highest cooking temperature of any Swiss cheese",
            "Once important trade good over the Gotthard and Splügen passes"
        ],
        "tags": ["cheese", "traditional", "swiss", "hard", "ancient", "alpine", "shaved", "16th-century-or-earlier"],
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
