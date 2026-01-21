#!/usr/bin/env python3
"""Add batch 41 - More traditional cheeses and specialized tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Traditional Cheeses
    {
        "id": "traditional-queso-blanco-latin-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Blanco (Latin American White Cheese)",
        "category": "mains",
        "attribution": "Latin America / Colonial Era",
        "source_note": "The simplest cheese of the Americas, made without culture or rennet. Vinegar or citrus provides the acid.",
        "description": "Simple Latin American white cheese that doesn't melt, perfect for frying, grilling, or crumbling on dishes.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour draining",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "not ultra-pasteurized"},
            {"item": "white vinegar or lime juice", "quantity": "1/4", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180-190°F, stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat and slowly stir in vinegar or lime juice."},
            {"step": 3, "text": "Curds will form immediately and separate from clear whey."},
            {"step": 4, "text": "Let sit 10 minutes."},
            {"step": 5, "text": "Strain through cheesecloth-lined colander."},
            {"step": 6, "text": "Add salt and mix gently."},
            {"step": 7, "text": "Gather cloth and hang to drain for 1 hour."},
            {"step": 8, "text": "For firmer cheese, press with weight for additional hour."},
            {"step": 9, "text": "Cut into cubes for frying or crumble for topping."},
            {"step": 10, "text": "Store refrigerated up to 2 weeks."}
        ],
        "temperature": "180-190°F make",
        "notes": [
            "Does not melt - holds shape when fried or grilled",
            "Perfect for beginners - no cultures or rennet needed",
            "Similar to paneer but slightly different technique",
            "Excellent source of protein in Latin American cuisines"
        ],
        "tags": ["cheese", "traditional", "latin-american", "fresh", "simple", "no-culture", "frying"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-panela-mexican-basket",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Panela (Mexican Basket Cheese)",
        "category": "mains",
        "attribution": "Mexico / Traditional",
        "source_note": "Named for the basket molds (canastas) used to shape it. A fresh, mild cheese popular throughout Mexico.",
        "description": "Mexican fresh cheese with a smooth texture and basket-weave imprint, absorbs flavors well and softens when heated.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "2 hours",
        "cook_time": "4 hours draining",
        "total_time": "6 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture, stir, and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and stir gently for 30 seconds."},
            {"step": 5, "text": "Let set for 45 minutes until clean break."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Stir gently for 15 minutes at 90°F."},
            {"step": 8, "text": "Drain curds and add salt."},
            {"step": 9, "text": "Pack into basket-weave molds (or colander for similar effect)."},
            {"step": 10, "text": "Let drain at room temperature for 4-6 hours."},
            {"step": 11, "text": "Refrigerate and use within 2 weeks."}
        ],
        "temperature": "90°F make",
        "notes": [
            "The basket weave imprint is characteristic of authentic panela",
            "Softens when heated but doesn't fully melt",
            "Great for absorbing marinades and salsas",
            "Often served as an appetizer with herbs and chilies"
        ],
        "tags": ["cheese", "traditional", "mexican", "fresh", "basket-weave", "mild"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-oaxaca-cheese-mexican-string",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Oaxaca (Mexican String Cheese)",
        "category": "mains",
        "attribution": "Oaxaca, Mexico / Colonial Era",
        "source_note": "Created by Dominican monks who brought Italian pasta filata techniques to Oaxaca. Mexico's mozzarella.",
        "description": "Mexican stretched-curd cheese wound into a ball shape, with excellent melting properties perfect for quesadillas.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "3 hours",
        "cook_time": "1 day for acidification",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently while raising temperature to 100°F."},
            {"step": 7, "text": "Drain curds and let acidify at room temperature for several hours."},
            {"step": 8, "text": "Test: cut small piece and stretch in 170°F water. When it stretches smoothly, it's ready."},
            {"step": 9, "text": "Heat water to 170°F. Cut curd into strips, place in hot water."},
            {"step": 10, "text": "When soft, stretch into long ribbons, adding salt as you stretch."},
            {"step": 11, "text": "Wind ribbons into a ball shape while still warm."},
            {"step": 12, "text": "Cool in cold water to set shape. Refrigerate up to 2 weeks."}
        ],
        "temperature": "90-100°F make, 170°F stretching",
        "notes": [
            "Dominican monks taught local Oaxacans Italian cheese techniques",
            "The wound ball shape is distinctive to this cheese",
            "Melts beautifully - essential for authentic quesadillas",
            "Can be pulled apart into strings for eating"
        ],
        "tags": ["cheese", "traditional", "mexican", "oaxaca", "stretched-curd", "pasta-filata", "colonial-era"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cotija-mexican-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cotija (Mexican Aged Cheese)",
        "category": "mains",
        "attribution": "Cotija, Michoacán, Mexico / Pre-Colonial Origins",
        "source_note": "Named after the town of Cotija. Originally made by indigenous peoples, adapted with Spanish cattle.",
        "description": "Mexican aged cheese, salty and crumbly like Parmesan, used as a finishing cheese on Mexican dishes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": "coarse"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 6, "text": "Stir gently while heating to 100°F over 30 minutes."},
            {"step": 7, "text": "Continue stirring at 100°F until curds are firm."},
            {"step": 8, "text": "Drain curds and add salt, mixing well."},
            {"step": 9, "text": "Pack into round mold and press at 30 lbs for 12 hours."},
            {"step": 10, "text": "Flip and press at 50 lbs for 24 hours."},
            {"step": 11, "text": "Air dry for 1 week until rind forms."},
            {"step": 12, "text": "Age at 55°F, 80% humidity for 3-12 months."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "Young cotija (3 months) is softer, aged cotija is hard and crumbly",
            "Essential topping for elote (Mexican street corn)",
            "Sometimes called 'Mexican Parmesan' for its similar use",
            "The town of Cotija holds an annual cheese fair"
        ],
        "tags": ["cheese", "traditional", "mexican", "aged", "hard", "crumbly", "grating", "michoacan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # Specialized Tips
    {
        "id": "cheesemaking-tip-stretched-curd-pasta-filata",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Mastering Stretched-Curd (Pasta Filata) Cheeses",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Pasta filata cheeses (mozzarella, provolone, oaxaca) require specific techniques for proper stretching.",
        "description": "Complete guide to making stretched-curd cheeses, from acidification to stretching to shaping.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "stretching knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "THE KEY IS ACIDIFICATION: Curds must reach pH 5.2-5.3 before they will stretch. Test with pH meter or stretch test."},
            {"step": 2, "text": "STRETCH TEST: Cut small piece of curd, place in 170°F water. After 1 minute, try to stretch. If it stretches smoothly without breaking, it's ready."},
            {"step": 3, "text": "IF IT BREAKS: Curd isn't acidified enough. Let it sit longer at room temperature. Retest every 30 minutes."},
            {"step": 4, "text": "IF IT'S MUSHY: Over-acidified. Cheese will be grainy. Work faster next time."},
            {"step": 5, "text": "WATER TEMPERATURE: 170-180°F. Too cool = won't stretch. Too hot = grainy texture and fat loss."},
            {"step": 6, "text": "WORKING THE CURD: Submerge in hot water, let soften, then stretch and fold repeatedly until smooth and shiny."},
            {"step": 7, "text": "ADDING SALT: Salt during stretching for even distribution. Salt also affects final texture."},
            {"step": 8, "text": "SHAPING: Work quickly while curd is hot. Form into balls, braids, or knots as desired."},
            {"step": 9, "text": "COOLING: Plunge shaped cheese into cold/ice water to set shape and stop cooking."},
            {"step": 10, "text": "STORAGE: Store in salted whey or brine for mozzarella. Dry and age for provolone."}
        ],
        "temperature": "170-180°F stretching water",
        "notes": [
            "The stretch comes from aligned protein strands - like pulling taffy",
            "Citric acid method is faster but traditional cultures give better flavor",
            "Wearing rubber gloves protects hands from hot water",
            "Practice makes perfect - first attempts are rarely ideal"
        ],
        "tags": ["cheese", "tips", "techniques", "pasta-filata", "stretching", "mozzarella", "guide", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-blue-cheese-techniques",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Blue Cheese Techniques",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Blue cheeses require specific techniques for proper mold development. Air is essential for bluing.",
        "description": "Guide to making blue-veined cheeses, from culture addition to piercing to aging.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Penicillium roqueforti", "quantity": "varies", "unit": "", "prep_note": "different strains for different blues"}
        ],
        "instructions": [
            {"step": 1, "text": "P. ROQUEFORTI STRAINS: Different strains produce different colors (blue, green, grey) and flavors (mild to sharp)."},
            {"step": 2, "text": "ADDING CULTURE: Add to milk with other cultures. Some recipes sprinkle between curd layers during molding."},
            {"step": 3, "text": "OPEN TEXTURE: Blue mold needs air. Don't press blue cheese - the open texture allows air penetration."},
            {"step": 4, "text": "PIERCING: After 2-4 weeks, pierce cheese with sterile needles or skewer. Creates air channels for mold growth."},
            {"step": 5, "text": "PIERCING PATTERN: Pierce from top to bottom and side to side. 40-50 holes per wheel is typical."},
            {"step": 6, "text": "WHEN TO PIERCE: Too early = cheese may collapse. Too late = rind is too thick. 2-4 weeks is usually right."},
            {"step": 7, "text": "AGING CONDITIONS: High humidity (90-95%), cool temperature (45-55°F). Caves are traditional."},
            {"step": 8, "text": "MOLD DEVELOPMENT: Blue veins appear 1-2 weeks after piercing. Full development takes 2-3 months."},
            {"step": 9, "text": "CONTROLLING BLUING: Wrap in foil when desired level reached. Stops air and halts mold growth."},
            {"step": 10, "text": "FLAVOR DEVELOPMENT: Blues get sharper with age. Young blues are mild; aged can be very intense."}
        ],
        "temperature": "45-55°F aging, 90-95% humidity",
        "notes": [
            "Legend says blue cheese was discovered when cheese was left in a cave with bread mold",
            "Traditional blue cheese caves maintain perfect conditions naturally",
            "P. roqueforti is safe - different from harmful molds",
            "Salt content affects mold growth rate and final flavor"
        ],
        "tags": ["cheese", "tips", "techniques", "blue-cheese", "piercing", "guide", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-washed-rind-techniques",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Washed-Rind Cheese Techniques",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Washed-rind cheeses (Taleggio, Epoisses, Limburger) require regular washing to develop their distinctive rinds.",
        "description": "Guide to making washed-rind cheeses, from inoculation to washing schedules to aging.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Brevibacterium linens", "quantity": "varies", "unit": "", "prep_note": "orange-rind bacteria"},
            {"item": "washing solution", "quantity": "varies", "unit": "", "prep_note": "brine, beer, wine, or spirit"}
        ],
        "instructions": [
            {"step": 1, "text": "B. LINENS CULTURE: Add to milk with starter, or inoculate surface after brining. Creates orange color and aroma."},
            {"step": 2, "text": "HUMIDITY: Washed rinds need very high humidity (90-95%). Too dry = hard rind, B. linens won't thrive."},
            {"step": 3, "text": "WASHING SCHEDULE: Start after brining. Wash every 2-3 days initially, reducing frequency as rind develops."},
            {"step": 4, "text": "WASH SOLUTION: Light brine is basic. Beer adds yeast and flavor. Wine adds tannins. Spirit (marc, eau-de-vie) adds complexity."},
            {"step": 5, "text": "WASHING TECHNIQUE: Use clean cloth or brush dampened with solution. Wipe all surfaces, turning cheese."},
            {"step": 6, "text": "RIND DEVELOPMENT: Starts white/gray, becomes pink, then orange over several weeks. Sticky texture is normal."},
            {"step": 7, "text": "SMELL: Washed rinds are pungent. The bacteria produce sulfur compounds (like feet or ammonia). This is normal."},
            {"step": 8, "text": "CONTROLLING UNWANTED MOLD: Wash more frequently to suppress unwanted molds. B. linens crowds out competitors."},
            {"step": 9, "text": "RIPENING: Interior softens from outside in. When rind is established, continue aging but wash less often."},
            {"step": 10, "text": "TIMING: Most washed rinds are ready in 4-8 weeks. Longer aging = stronger flavor and softer interior."}
        ],
        "temperature": "50-60°F aging, 90-95% humidity",
        "notes": [
            "Washed rind technique was developed by monks who washed cheese while praying",
            "The strong smell is mostly in the rind - the paste is usually milder",
            "Regional washes create regional character (Époisses with marc, Chimay with beer)",
            "B. linens also contributes to the distinctive orange color"
        ],
        "tags": ["cheese", "tips", "techniques", "washed-rind", "orange-rind", "guide", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-bloomy-rind-techniques",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Bloomy-Rind (Brie/Camembert Style) Techniques",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Bloomy-rind cheeses require specific mold cultures and careful humidity control for proper rind development.",
        "description": "Guide to making white-mold cheeses like Brie and Camembert, from culture selection to aging.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Penicillium candidum", "quantity": "varies", "unit": "", "prep_note": "white mold culture"},
            {"item": "Geotrichum candidum", "quantity": "varies", "unit": "", "prep_note": "yeast for texture"}
        ],
        "instructions": [
            {"step": 1, "text": "P. CANDIDUM: Primary white mold. Add to milk or spray on surface after draining. Creates fluffy white coating."},
            {"step": 2, "text": "G. CANDIDUM: Yeast that creates wrinkled texture. Often used with P. candidum for complexity."},
            {"step": 3, "text": "MINIMUM HANDLING: Soft-ripened curds are delicate. Ladle gently, don't cut small or stir much."},
            {"step": 4, "text": "DRAINING: Let gravity do the work. No pressing for bloomy rinds - open texture traps moisture."},
            {"step": 5, "text": "SALTING: Dry salt or very short brine. Too much salt inhibits mold growth."},
            {"step": 6, "text": "DRYING PHASE: Air dry 1-2 days until surface is no longer wet. Mold needs slightly dry surface to start."},
            {"step": 7, "text": "AGING CONDITIONS: 52-55°F, 90-95% humidity. Too humid = slimy. Too dry = cracked rind."},
            {"step": 8, "text": "MOLD APPEARANCE: White fuzz appears in 5-7 days. Full coat in 10-14 days. Turn cheese daily."},
            {"step": 9, "text": "RIPENING: Mold enzymes break down paste from outside in. Watch for 'cream line' under rind."},
            {"step": 10, "text": "READINESS: When pressed gently at center, should give slightly. Interior should be creamy throughout."}
        ],
        "temperature": "52-55°F aging, 90-95% humidity",
        "notes": [
            "Different P. candidum strains produce different textures and flavors",
            "Over-ripe bloomy cheese develops ammonia smell - eat before this stage",
            "Wrapping in paper allows cheese to breathe while protecting in refrigerator",
            "Cut and wrap sections accelerate ripening of remainder"
        ],
        "tags": ["cheese", "tips", "techniques", "bloomy-rind", "brie", "camembert", "guide", "advanced"],
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
