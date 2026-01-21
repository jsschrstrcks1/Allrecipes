#!/usr/bin/env python3
"""Add batch 31 of traditional cheese recipes - Ancient cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-imsil-korean-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Imsil Cheese (Korean Pioneer Cheese)",
        "category": "mains",
        "attribution": "Imsil, Korea / 1960s",
        "source_note": "Korea's first domestically produced cheese, started by Belgian priest Father Didier t'Serstevens who taught locals to make cheese from surplus milk.",
        "description": "Korean Gouda-style cheese from Imsil County, with a mild creamy flavor and smooth texture, now a beloved local specialty.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "Gouda-type"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F in a large pot."},
            {"step": 2, "text": "Add mesophilic culture and stir well. Let ripen for 10 minutes."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and stir for 30 seconds."},
            {"step": 5, "text": "Let set for 45 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Slowly raise temperature to 100°F over 30 minutes, stirring gently."},
            {"step": 8, "text": "Drain 1/3 of whey and add warm water (100°F) to wash curds - this creates Gouda's sweet flavor."},
            {"step": 9, "text": "Continue cooking at 100°F for 30 more minutes."},
            {"step": 10, "text": "Drain curds and press into round mold at 10 lbs for 30 minutes."},
            {"step": 11, "text": "Flip and press at 20 lbs for 6 hours."},
            {"step": 12, "text": "Make saturated brine. Soak cheese for 8 hours, flipping halfway."},
            {"step": 13, "text": "Air dry for 2-3 days until surface is dry."},
            {"step": 14, "text": "Age at 55°F, 85% humidity for 2-3 months, turning weekly."}
        ],
        "temperature": "86-100°F make, 55°F aging",
        "notes": [
            "Imsil cheese brought dairy culture to Korea in the 1960s",
            "The town now celebrates an annual cheese festival",
            "Washed curd technique removes lactose, creating sweeter flavor",
            "Modern Imsil makes various styles but Gouda-type remains the classic"
        ],
        "tags": ["cheese", "traditional", "korean", "gouda-style", "washed-curd", "aged", "1960s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tymsborski-polish-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tymsborski (Polish Smoked Cheese)",
        "category": "mains",
        "attribution": "Tatra Mountains, Poland / Medieval",
        "source_note": "Made by Polish highlanders (górale) using traditional methods passed down for centuries. Similar to but distinct from oscypek.",
        "description": "Polish highland smoked cheese made from sheep's milk, with a distinctive spindle shape and golden smoked exterior.",
        "servings_yield": "About 4 small spindles (4 oz each)",
        "prep_time": "2 hours",
        "cook_time": "2 weeks smoking/drying",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "traditional lamb rennet preferred"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": "coarse"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm fresh sheep milk to 95°F."},
            {"step": 2, "text": "Add rennet and stir briefly."},
            {"step": 3, "text": "Let set for 30-40 minutes until firm curd forms."},
            {"step": 4, "text": "Break curds by hand into small pieces."},
            {"step": 5, "text": "Gather curds and squeeze out whey by hand."},
            {"step": 6, "text": "Knead the curd mass while still warm, stretching and folding."},
            {"step": 7, "text": "Shape into traditional spindle or lens shapes."},
            {"step": 8, "text": "Press decorative patterns using carved wooden molds."},
            {"step": 9, "text": "Soak in brine (saturated salt solution) for 24 hours."},
            {"step": 10, "text": "Hang in smokehouse with cold smoke from juniper and pine for 1-2 weeks."},
            {"step": 11, "text": "Cheese is ready when exterior is golden-brown and interior is pale yellow."}
        ],
        "temperature": "95°F make, cold smoke",
        "notes": [
            "Highlander cheeses have been made in the Tatras since medieval times",
            "Traditional smoking uses conifer wood for distinctive flavor",
            "The decorative patterns identify the cheesemaker's hut",
            "Serve sliced thin with Polish mountain honey"
        ],
        "tags": ["cheese", "traditional", "polish", "smoked", "sheep", "highland", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-parenica-slovak-steamed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Parenica (Slovak Steamed Cheese)",
        "category": "mains",
        "attribution": "Slovakia / Medieval Carpathian",
        "source_note": "Traditional Slovak pasta filata cheese formed into distinctive snail-shell spirals, made by shepherds in the Carpathian mountains.",
        "description": "Slovak steamed cheese formed into ribbon-like strips and rolled into characteristic snail-shell shapes, with a mild milky flavor.",
        "servings_yield": "About 4 spirals (4 oz each)",
        "prep_time": "2 hours",
        "cook_time": "1-2 days",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "1", "unit": "gallon", "prep_note": "or cow milk"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or soured milk"},
            {"item": "rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to 90°F."},
            {"step": 2, "text": "Add culture and let ripen 30 minutes."},
            {"step": 3, "text": "Add rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch pieces."},
            {"step": 5, "text": "Drain whey and let curds acidify at room temperature for 24 hours."},
            {"step": 6, "text": "Test curd: cut a piece and stretch in hot water. When it pulls into smooth strings, it's ready."},
            {"step": 7, "text": "Cut acidified curd into strips and place in hot water (170°F)."},
            {"step": 8, "text": "When soft and pliable, stretch into long thin ribbons."},
            {"step": 9, "text": "Salt the ribbons while stretching."},
            {"step": 10, "text": "Immediately roll each ribbon into a tight snail-shell spiral."},
            {"step": 11, "text": "Place spirals in cold water to set the shape."},
            {"step": 12, "text": "Optionally, cold smoke for 2-4 hours for smoked parenica."}
        ],
        "temperature": "90°F make, 170°F stretching",
        "notes": [
            "The snail-shell shape is formed by rolling the stretched ribbon while still hot",
            "Traditional parenica is white (unsmoked) or golden (smoked)",
            "Served as a snack or appetizer, unrolling the ribbon to eat",
            "Similar to Italian pasta filata but with distinctive Central European character"
        ],
        "tags": ["cheese", "traditional", "slovak", "pasta-filata", "spiral", "sheep", "carpathian", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-koliba-czech-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Koliba (Czech Shepherd's Cheese)",
        "category": "mains",
        "attribution": "Moravian Highlands, Czech Republic / Medieval",
        "source_note": "Named after the mountain shepherd's huts (koliba) where this cheese was traditionally made. A heritage of Wallachian shepherd culture.",
        "description": "Czech smoked sheep cheese with firm texture and distinctive smoky flavor, traditionally made in mountain shepherd huts.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "1.5", "unit": "gallons", "prep_note": "or sheep/cow blend"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep milk to 90°F."},
            {"step": 2, "text": "Add culture and let ripen 30 minutes."},
            {"step": 3, "text": "Add rennet and let set for 40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently while raising temperature to 100°F over 20 minutes."},
            {"step": 6, "text": "Drain whey and salt curds directly."},
            {"step": 7, "text": "Press into round or oval mold at 15 lbs for 1 hour."},
            {"step": 8, "text": "Flip and press at 30 lbs for 6 hours."},
            {"step": 9, "text": "Air dry for 2-3 days until surface is firm."},
            {"step": 10, "text": "Cold smoke with beech or fruit wood for 1-2 weeks."},
            {"step": 11, "text": "Age at 50-55°F for additional 2-4 weeks after smoking."}
        ],
        "temperature": "90-100°F make, cold smoke, 50-55°F aging",
        "notes": [
            "Wallachian shepherds brought sheep cheese traditions from Romania to Czech lands",
            "The koliba (hut) was the summer home for shepherds in mountain pastures",
            "Smoking was practical preservation in mountain conditions",
            "Best served with dark Czech bread and pilsner"
        ],
        "tags": ["cheese", "traditional", "czech", "smoked", "sheep", "shepherd", "moravian", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-belper-knolle-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Belper Knolle (Swiss Pepper Ball)",
        "category": "mains",
        "attribution": "Belp, Switzerland / 1990s Revival",
        "source_note": "Created by Swiss cheesemaker Margrit Jäger-Bürki based on traditional techniques. Coated in pepper and garlic, intensely flavored.",
        "description": "Small Swiss cheese balls coated in black pepper and garlic, developing an intense concentrated flavor through extended drying.",
        "servings_yield": "About 8 small balls (2 oz each)",
        "prep_time": "2 hours",
        "cook_time": "4-6 months drying",
        "total_time": "4-6 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "fresh garlic", "quantity": "4", "unit": "cloves", "prep_note": "minced very fine"},
            {"item": "black pepper", "quantity": "1/2", "unit": "cup", "prep_note": "coarsely ground"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and let ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 6, "text": "Stir gently while heating to 104°F over 30 minutes."},
            {"step": 7, "text": "Drain curds thoroughly."},
            {"step": 8, "text": "Mix in salt and minced garlic while curds are still warm."},
            {"step": 9, "text": "Form into small balls (about 2 inches diameter)."},
            {"step": 10, "text": "Roll each ball thoroughly in coarse black pepper."},
            {"step": 11, "text": "Place on drying rack at 55-60°F, 75% humidity."},
            {"step": 12, "text": "Turn every few days. Re-roll in pepper as balls shrink."},
            {"step": 13, "text": "Dry for 4-6 months until very hard and concentrated."}
        ],
        "temperature": "90-104°F make, 55-60°F drying",
        "notes": [
            "The extended drying creates an incredibly concentrated, intense cheese",
            "When fully aged, the texture is like parmesan and it grates beautifully",
            "The pepper coating is reapplied as the cheese shrinks during drying",
            "Often called 'Swiss truffle' for its intense flavor and appearance"
        ],
        "tags": ["cheese", "traditional", "swiss", "pepper-coated", "garlic", "hard", "aged", "modern-traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-bergkäse-austrian-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Austrian Bergkäse (Alpine Mountain Cheese)",
        "category": "mains",
        "attribution": "Austrian Alps / Medieval",
        "source_note": "Made in Austrian alpine huts since medieval times. Bergkäse means 'mountain cheese' and requires production at altitude from alpine pasture milk.",
        "description": "Austrian mountain cheese made from the milk of cows grazing alpine meadows, with rich complex flavor and firm smooth texture.",
        "servings_yield": "About 5 lb wheel",
        "prep_time": "4 hours",
        "cook_time": "4-12 months aging",
        "total_time": "4-12 months",
        "ingredients": [
            {"item": "raw alpine cow milk", "quantity": "4", "unit": "gallons", "prep_note": "from cows on mountain pasture"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium", "quantity": "1/16", "unit": "tsp", "prep_note": "for eye development"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "calf rennet traditional"},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh alpine milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and Propionibacterium. Let ripen 15 minutes."},
            {"step": 3, "text": "Add diluted rennet and stir for 30 seconds."},
            {"step": 4, "text": "Let set for 35 minutes until firm."},
            {"step": 5, "text": "Cut curds to rice-sized pieces."},
            {"step": 6, "text": "Heat slowly to 120°F over 40 minutes, stirring constantly."},
            {"step": 7, "text": "Maintain at 120°F for 30 more minutes until curds are firm."},
            {"step": 8, "text": "Transfer curds to round cheese mold."},
            {"step": 9, "text": "Press at 15 lbs for 30 minutes, flip, press at 25 lbs for 2 hours."},
            {"step": 10, "text": "Press at 40 lbs for 12 hours."},
            {"step": 11, "text": "Soak in saturated brine for 24 hours per pound of cheese."},
            {"step": 12, "text": "Air dry for 3-4 days."},
            {"step": 13, "text": "Age at 55°F, 85% humidity for 4-12 months, washing with brine weekly."}
        ],
        "temperature": "90-120°F make, 55°F aging",
        "notes": [
            "True Bergkäse must be made in alpine huts at altitude from alpine grazing milk",
            "The flora of alpine meadows gives distinctive flavor to the milk and cheese",
            "Eyes (holes) develop during the warm room phase from Propionibacteria",
            "Vorarlberger Bergkäse has PDO protection"
        ],
        "tags": ["cheese", "traditional", "austrian", "alpine", "mountain", "aged", "medieval", "raw-milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-piora-swiss-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Piora (Swiss Ticino Alpine Cheese)",
        "category": "mains",
        "attribution": "Piora Valley, Ticino, Switzerland / Medieval",
        "source_note": "Made in the high Piora Valley of Ticino since medieval times. One of Switzerland's most prestigious alpine cheeses.",
        "description": "Swiss alpine cheese from the Italian-speaking Ticino region, made during summer on high alpine pastures with rich, buttery flavor.",
        "servings_yield": "About 8 lb wheel",
        "prep_time": "4 hours",
        "cook_time": "6-18 months aging",
        "total_time": "6-18 months",
        "ingredients": [
            {"item": "raw alpine cow milk", "quantity": "6", "unit": "gallons", "prep_note": "from high pasture grazing"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "calf rennet", "quantity": "1.5", "unit": "tsp", "prep_note": "traditional"},
            {"item": "cheese salt", "quantity": "2", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh morning and evening milk (mixed) to 88°F."},
            {"step": 2, "text": "Add thermophilic culture and stir well. Ripen 20 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed."},
            {"step": 4, "text": "Add diluted rennet and let set for 30-35 minutes."},
            {"step": 5, "text": "Cut curds to wheat grain size."},
            {"step": 6, "text": "Stir and heat gradually to 118-122°F over 45 minutes."},
            {"step": 7, "text": "Hold at temperature while stirring for 20 more minutes."},
            {"step": 8, "text": "Transfer curds to large round mold (10-12 inch diameter)."},
            {"step": 9, "text": "Press at 20 lbs for 30 minutes, flip, 40 lbs for 2 hours, 60 lbs for 12 hours."},
            {"step": 10, "text": "Brine for 2-3 days in saturated salt solution."},
            {"step": 11, "text": "Air dry for 1 week, turning daily."},
            {"step": 12, "text": "Age at 54-57°F, 90% humidity for 6-18 months."},
            {"step": 13, "text": "Wash rind with brine every 1-2 weeks during aging."}
        ],
        "temperature": "88-122°F make, 54-57°F aging",
        "notes": [
            "Piora can only be made during the 100-day alpine grazing season",
            "The Piora Valley sits at over 6,000 feet elevation",
            "Cheese develops rich buttery, slightly fruity flavor with age",
            "One of the most prized Swiss alpine cheeses, rarely exported"
        ],
        "tags": ["cheese", "traditional", "swiss", "alpine", "ticino", "mountain", "medieval", "raw-milk", "seasonal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-juustoleipa-finnish-bread-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Juustoleipä (Finnish Bread Cheese)",
        "category": "mains",
        "attribution": "Ostrobothnia, Finland / 16th Century or Earlier",
        "source_note": "Called 'bread cheese' or 'squeaky cheese' for its texture. Traditionally made from beestings (first milk after calving) and baked in front of a fire.",
        "description": "Finnish fresh cheese baked until spotted brown, with a distinctive squeaky texture and sweet caramelized flavor, traditionally served with cloudberry jam.",
        "servings_yield": "About 1 lb disk",
        "prep_time": "1 hour",
        "cook_time": "30 minutes",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "or beestings if available"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "optional, for richness"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk (and cream if using) to 95°F."},
            {"step": 2, "text": "Add salt and stir to dissolve."},
            {"step": 3, "text": "Add diluted rennet and stir briefly."},
            {"step": 4, "text": "Let set for 30-45 minutes until firm curd forms."},
            {"step": 5, "text": "Cut curds into large chunks and let rest 5 minutes."},
            {"step": 6, "text": "Gently ladle curds into a flat round pan or traditional wooden leipäjuustomuotti."},
            {"step": 7, "text": "Press down gently to flatten into a disk about 1 inch thick."},
            {"step": 8, "text": "Let drain for 30 minutes."},
            {"step": 9, "text": "Preheat broiler to high."},
            {"step": 10, "text": "Place cheese (still in pan or transferred to oven-safe dish) 4 inches under broiler."},
            {"step": 11, "text": "Broil until top is spotted brown like bread, about 5-8 minutes."},
            {"step": 12, "text": "Flip and broil other side until spotted."},
            {"step": 13, "text": "Serve warm or at room temperature with cloudberry jam or coffee."}
        ],
        "temperature": "95°F make, broil to finish",
        "notes": [
            "Traditional juustoleipä was baked by the fire until the fat sizzled and spots appeared",
            "Beestings (colostrum) creates the richest, sweetest version",
            "The cheese keeps for months dried, and is reconstituted in hot coffee",
            "Called 'squeaky cheese' because it squeaks against teeth when eaten fresh"
        ],
        "tags": ["cheese", "traditional", "finnish", "baked", "fresh", "squeaky", "ostrobothnian", "16th-century"],
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
