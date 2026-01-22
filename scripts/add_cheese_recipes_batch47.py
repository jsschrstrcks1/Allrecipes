#!/usr/bin/env python3
"""Add batch 47 - More traditional European cheeses and cheesemaking tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-cave-aging-natural",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Natural Cave Aging Techniques",
        "category": "mains",
        "attribution": "Traditional cave aging wisdom",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "For millennia, natural caves have provided ideal cheese aging environments. Understanding cave conditions helps replicate them at home or choose appropriate aging spaces.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "natural cave", "quantity": "1", "unit": "", "prep_note": "or simulated environment"},
            {"item": "temperature monitoring", "quantity": "", "unit": "", "prep_note": "thermometer and hygrometer"},
            {"item": "aging shelves", "quantity": "", "unit": "", "prep_note": "wood, stone, or food-safe material"},
            {"item": "cheese turning schedule", "quantity": "", "unit": "", "prep_note": "varies by cheese type"}
        ],
        "instructions": [
            {"step": 1, "text": "Understand why caves work: stable temperature (50-55°F year-round), high humidity (85-95%), minimal air circulation, natural bacteria and molds."},
            {"step": 2, "text": "Limestone caves are ideal - the porous rock regulates humidity naturally and harbors beneficial microorganisms."},
            {"step": 3, "text": "If using a natural cave, test for contaminants and ensure proper drainage. Standing water breeds unwanted bacteria."},
            {"step": 4, "text": "Home alternatives: basement corners, wine refrigerators, modified chest freezers with temperature controllers."},
            {"step": 5, "text": "Create humidity: place water pans in aging space, or use damp towels that don't touch cheese."},
            {"step": 6, "text": "Air circulation should be minimal but present - stagnant air encourages bad molds."},
            {"step": 7, "text": "Wooden shelves absorb and release moisture, helping regulate humidity. Season new wood with brine."},
            {"step": 8, "text": "Stone or slate shelves stay cool and wick moisture - traditional in many regions."},
            {"step": 9, "text": "Keep different cheese types separated - strong washed rinds can affect milder cheeses."},
            {"step": 10, "text": "Monitor daily at first, then weekly once conditions stabilize."},
            {"step": 11, "text": "Turn cheeses regularly - prevents moisture pooling and ensures even rind development."},
            {"step": 12, "text": "Some caves develop unique 'house cultures' over years - this is desirable and gives regional character."}
        ],
        "temperature": "50-55°F (10-13°C) for most aged cheeses",
        "notes": [
            "Roquefort caves in France are UNESCO protected for their unique microclimate",
            "Cheddar takes its name from the Cheddar Gorge caves where it was aged",
            "Many modern 'cave-aged' cheeses use climate-controlled rooms, not true caves",
            "Natural caves may harbor wild molds - good for blue cheeses, may need control for others",
            "Wine coolers with humidity trays make excellent home cheese caves"
        ],
        "tags": ["cheese", "technique", "tip", "aging", "cave", "traditional"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "cheesemaking-tip-regional-terroir-milk",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Understanding Terroir in Cheese",
        "category": "mains",
        "attribution": "Traditional cheesemaking wisdom",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Like wine, cheese expresses terroir - the unique characteristics of place. Understanding how pasture, climate, breed, and season affect milk helps create distinctive cheeses.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "knowledge of local pastures", "quantity": "", "unit": "", "prep_note": "what grows where your milk comes from"},
            {"item": "seasonal awareness", "quantity": "", "unit": "", "prep_note": "how milk changes through the year"},
            {"item": "breed characteristics", "quantity": "", "unit": "", "prep_note": "different animals, different milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Terroir (from French 'terre' for land) encompasses soil, climate, altitude, vegetation, and traditional practices of a place."},
            {"step": 2, "text": "Alpine cheeses taste different from lowland cheeses partly because mountain pastures contain different herbs and flowers."},
            {"step": 3, "text": "Spring milk is rich and grassy; summer milk may be lighter; fall milk is creamy; winter (hay-fed) milk is different again."},
            {"step": 4, "text": "Traditional breeds produce milk suited to local cheesemaking. Holstein makes more milk; heritage breeds make richer milk."},
            {"step": 5, "text": "Sheep's milk is naturally richer in fat and protein than cow's milk, affecting cheese texture fundamentally."},
            {"step": 6, "text": "Goat's milk has smaller fat globules and different proteins - why goat cheese has distinctive texture and tang."},
            {"step": 7, "text": "Water buffalo milk is extremely rich - mozzarella di bufala's luxurious texture comes from this."},
            {"step": 8, "text": "Even the bacteria present in traditional wooden equipment and aging caves contribute to terroir."},
            {"step": 9, "text": "Protected designation of origin (PDO/DOP/AOC) rules often specify region, breed, feed, and methods to preserve terroir."},
            {"step": 10, "text": "To develop your own terroir: source local milk, use consistent methods, age in consistent conditions over time."},
            {"step": 11, "text": "Keep notes on how your cheese varies with seasons - this is your terroir expressing itself."},
            {"step": 12, "text": "Embrace variation rather than fighting it - traditional cheese has character, not uniformity."}
        ],
        "temperature": "N/A",
        "notes": [
            "Comté from different alpine valleys tastes subtly different despite identical methods",
            "Parmigiano-Reggiano regulations specify what cows can eat to preserve terroir",
            "Some makers 'follow the grass' - moving animals to different pastures seasonally",
            "Urban cheesemakers can develop terroir through consistent sourcing and methods",
            "Your 'house culture' of beneficial bacteria becomes part of your terroir over time"
        ],
        "tags": ["cheese", "technique", "tip", "terroir", "traditional", "milk"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "cheesemaking-tip-rind-washing-techniques",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Washed Rind Techniques",
        "category": "mains",
        "attribution": "Monastic and artisan traditions",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Washed-rind cheeses develop their distinctive orange rinds and powerful aromas through regular washing with brine, alcohol, or local beverages. This technique was perfected in medieval monasteries.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "brine solution", "quantity": "1", "unit": "quart", "prep_note": "2-3% salt in water"},
            {"item": "B. linens culture", "quantity": "1/16", "unit": "tsp", "prep_note": "optional - develops naturally too"},
            {"item": "washing liquid options", "quantity": "", "unit": "", "prep_note": "brine, beer, wine, cider, spirits"},
            {"item": "soft cloth or brush", "quantity": "", "unit": "", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Washed-rind technique encourages Brevibacterium linens and related bacteria that create orange color and strong aroma."},
            {"step": 2, "text": "Start washing 2-3 days after cheese is made, once surface is dry to touch."},
            {"step": 3, "text": "Basic brine wash: dissolve 2-3 tbsp salt per quart of water. Some add B. linens culture to accelerate development."},
            {"step": 4, "text": "Dip cloth in wash solution, wring until just damp, wipe all surfaces of cheese."},
            {"step": 5, "text": "During first 2-3 weeks, wash every 2-3 days. This is critical period for establishing bacteria."},
            {"step": 6, "text": "After rind bacteria established, reduce to weekly washing."},
            {"step": 7, "text": "High humidity (90-95%) essential - bacteria need moisture to thrive."},
            {"step": 8, "text": "Aging temperature 50-55°F - slightly warmer than most cheeses to encourage bacterial growth."},
            {"step": 9, "text": "Regional wash variations: Époisses uses marc (grape pomace brandy), Chimay uses Trappist beer, others use local cider."},
            {"step": 10, "text": "Alcohol in wash adds flavor and controls unwanted molds while bacteria establish."},
            {"step": 11, "text": "Rind will progress: white → pink → orange → reddish-brown as bacteria mature."},
            {"step": 12, "text": "Strong ammonia smell indicates overripeness - cheese should smell pungent but not overpowering when cut."}
        ],
        "temperature": "50-55°F (10-13°C) for aging with 90-95% humidity",
        "notes": [
            "Monks developed washed-rind cheeses partly because Lenten fasting rules allowed cheese but not meat",
            "The 'stink' is mostly on the rind - interior is usually mild and creamy",
            "Reusing wash solution from batch to batch inoculates new cheeses with established culture",
            "Many washed-rind cheeses are ready in 4-8 weeks - faster than hard aged cheeses",
            "Store washed-rind cheeses wrapped loosely - they need to breathe"
        ],
        "tags": ["cheese", "technique", "tip", "washed-rind", "traditional", "monastic"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-reblochon-tartiflette-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Reblochon (Tartiflette Alpine Cheese)",
        "category": "mains",
        "attribution": "Medieval Savoyard alpine tradition",
        "source_note": "Traditional French alpine cheesemaking",
        "description": "Born from medieval tax evasion, Reblochon comes from 're-blocher' meaning 'to milk again.' Farmers would incompletely milk cows during tax assessments, then fully milk them afterwards for this rich, creamy cheese.",
        "servings_yield": "1 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "high fat content, ideally second milking"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "for white rind"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "light brine", "quantity": "1", "unit": "quart", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Traditionally made from second, richer milking."},
            {"step": 2, "text": "Add mesophilic culture and P. candidum. Ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently for 10 minutes - do NOT heat curds further."},
            {"step": 6, "text": "Drain most whey, leaving curds quite wet."},
            {"step": 7, "text": "Ladle wet curds into small molds (traditional size is 3.5 inches diameter)."},
            {"step": 8, "text": "Press very lightly - just enough to consolidate. Heavy pressing ruins texture."},
            {"step": 9, "text": "Flip after 1 hour, then again after 2 hours."},
            {"step": 10, "text": "Press casein label into top surface (traditional identification mark)."},
            {"step": 11, "text": "Salt surfaces lightly or brief brine for 30 minutes."},
            {"step": 12, "text": "Age at 55°F with 95% humidity."},
            {"step": 13, "text": "Wash with light brine every 2-3 days for first week, then once weekly."},
            {"step": 14, "text": "Ready when rind is pinkish-orange and interior is soft and creamy, about 4-6 weeks."}
        ],
        "temperature": "90°F (32°C) for make; 55°F (13°C) for aging",
        "notes": [
            "AOC protected since 1958, must be made from raw milk in Haute-Savoie",
            "Green casein label = fermier (farmstead); red label = fruitier (cooperative)",
            "Essential ingredient in tartiflette, the Savoyard potato dish",
            "Should be soft and yielding when pressed - not runny but not firm",
            "Best eaten at room temperature when interior is almost flowing"
        ],
        "tags": ["cheese", "french", "alpine", "traditional", "washed-rind", "savoie"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-vacherin-mont-dor-spruce",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vacherin Mont d'Or (Spruce-Wrapped Winter Cheese)",
        "category": "mains",
        "attribution": "Ancient Jura mountain winter tradition",
        "source_note": "Traditional French-Swiss seasonal cheesemaking",
        "description": "A magical winter cheese made only from September to March when cows return from alpine pastures. Wrapped in spruce bark and aged in spruce boxes, it becomes so creamy it's eaten with a spoon - a centuries-old tradition in the Jura mountains.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-4 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from hay-fed cows, autumn/winter"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "spruce bark strips", "quantity": "2-3", "unit": "", "prep_note": "fresh, flexible, food-safe"},
            {"item": "spruce wood box", "quantity": "1", "unit": "", "prep_note": "for aging and serving"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "This cheese traditionally made only September-March from hay-fed milk."},
            {"step": 2, "text": "Heat milk to 86°F (30°C) - lower than most cheeses."},
            {"step": 3, "text": "Add mesophilic culture, ripen 30 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 40-50 minutes for soft curd."},
            {"step": 5, "text": "Cut curds into 1-inch cubes - larger than most cheeses."},
            {"step": 6, "text": "Stir very gently for 10 minutes. Do not heat."},
            {"step": 7, "text": "Let curds settle, drain most whey."},
            {"step": 8, "text": "Ladle curds into molds lined with cloth."},
            {"step": 9, "text": "Let drain naturally - minimal or no pressing."},
            {"step": 10, "text": "Flip several times over 24 hours."},
            {"step": 11, "text": "Soak spruce bark in brine to soften, then wrap around cheese circumference."},
            {"step": 12, "text": "Secure bark with string or let it overlap."},
            {"step": 13, "text": "Light salt or brief brine."},
            {"step": 14, "text": "Age at 50-55°F with 95% humidity for 3-4 weeks, washing occasionally."},
            {"step": 15, "text": "Transfer to spruce box slightly smaller than cheese - sides will bulge attractively."},
            {"step": 16, "text": "Ready when top yields to gentle pressure and interior is spoonable."}
        ],
        "temperature": "86°F (30°C) for make; 50-55°F (10-13°C) for aging",
        "notes": [
            "AOC in France and Switzerland - both countries claim origin",
            "Spruce bark contributes resinous flavor and holds shape as cheese softens",
            "Traditionally eaten by cutting hole in top and spooning out interior",
            "Can be baked in box for 15-20 minutes at 350°F for fondue-like texture",
            "Only available autumn through early spring - true seasonal cheese"
        ],
        "tags": ["cheese", "french", "swiss", "alpine", "traditional", "seasonal", "soft-ripened"],
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
