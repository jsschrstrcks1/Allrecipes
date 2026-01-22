#!/usr/bin/env python3
"""Add batch 40 - More ancient cheeses and advanced cheese making tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # More Ancient Cheeses
    {
        "id": "traditional-pecorino-romano-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Romano (Ancient Roman Soldier's Cheese)",
        "category": "mains",
        "attribution": "Lazio, Italy / 1st Century BC",
        "source_note": "Documented by Roman writers Varro and Pliny. Standard ration for Roman legions - 27g per soldier per day.",
        "description": "Ancient Roman sheep cheese, sharp and salty, traditionally used for grating. The original Pecorino.",
        "servings_yield": "About 5 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "8-12 months aging",
        "total_time": "8-12 months",
        "ingredients": [
            {"item": "raw sheep milk", "quantity": "4", "unit": "gallons", "prep_note": "from Sarda or local sheep"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "lamb rennet", "quantity": "1", "unit": "tsp", "prep_note": "traditional lamb paste rennet"},
            {"item": "cheese salt", "quantity": "3", "unit": "lbs", "prep_note": "coarse, for dry salting"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh sheep milk to 100°F."},
            {"step": 2, "text": "Add thermophilic culture. Ripen 15 minutes."},
            {"step": 3, "text": "Add lamb rennet (traditional) and let set for 20-25 minutes."},
            {"step": 4, "text": "Cut curds to wheat grain size."},
            {"step": 5, "text": "Cook while stirring, raising temperature to 118-120°F."},
            {"step": 6, "text": "Continue stirring at temperature for 15-20 minutes."},
            {"step": 7, "text": "Drain curds quickly and press into mold while very hot."},
            {"step": 8, "text": "Press heavily (80-100 lbs) for 24 hours, turning frequently."},
            {"step": 9, "text": "DRY SALT: Rub coarse salt into all surfaces daily for 30-40 days."},
            {"step": 10, "text": "Traditional: No brining. Salt penetrates gradually during repeated rubbings."},
            {"step": 11, "text": "Age at 55-60°F, 80% humidity for 8-12 months minimum."},
            {"step": 12, "text": "Rub surface with olive oil periodically during aging."}
        ],
        "temperature": "100-120°F make, 55-60°F aging",
        "notes": [
            "Roman legions carried pecorino as part of standard rations",
            "Traditional uses dry salting over many days, not brine",
            "Lamb rennet gives distinctive flavor - calf rennet is a substitute",
            "DOP protected - true Romano from Lazio, Sardinia, or Grosseto only"
        ],
        "tags": ["cheese", "traditional", "italian", "ancient", "roman", "sheep", "grating", "1st-century-bc", "dop"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-casu-marzu-sardinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Casu Marzu (Sardinian Live Cheese)",
        "category": "mains",
        "attribution": "Sardinia, Italy / Ancient",
        "source_note": "Controversial traditional cheese with live insect larvae. Banned in EU but still made by Sardinian families. Historical cultural practice.",
        "description": "Sardinian sheep cheese deliberately colonized by cheese fly larvae, creating an extremely soft, pungent cheese with intense flavor.",
        "servings_yield": "About 3 lbs wheel",
        "prep_time": "3 hours for base",
        "cook_time": "3-4 months development",
        "total_time": "3-4 months",
        "ingredients": [
            {"item": "pecorino sardo base", "quantity": "1", "unit": "wheel", "prep_note": "young, about 3 lbs"},
            {"item": "cheese fly eggs", "quantity": "natural", "unit": "", "prep_note": "Piophila casei - occurs naturally in Sardinia"}
        ],
        "instructions": [
            {"step": 1, "text": "HISTORICAL CONTEXT: This documents a traditional practice. Production is restricted in many jurisdictions."},
            {"step": 2, "text": "Start with a young pecorino sardo cheese, 2-3 months old."},
            {"step": 3, "text": "Cut into the rind to expose paste, or remove a section of rind."},
            {"step": 4, "text": "Traditional method: Leave in location where cheese flies (Piophila casei) are present."},
            {"step": 5, "text": "Flies lay eggs in the exposed paste."},
            {"step": 6, "text": "Larvae hatch and begin digesting the cheese fats."},
            {"step": 7, "text": "The digestive action creates soft, almost liquid texture."},
            {"step": 8, "text": "Cover loosely to allow air but prevent other contamination."},
            {"step": 9, "text": "Monitor for 2-3 months as larvae develop and cheese transforms."},
            {"step": 10, "text": "Traditional consumption: Eaten with larvae present or after removal."},
            {"step": 11, "text": "Served with Sardinian flatbread (pane carasau) and Cannonau wine."}
        ],
        "temperature": "Room temperature development",
        "notes": [
            "This is a historical/cultural documentation, not a recommendation",
            "Currently banned in the EU but protected as traditional food heritage",
            "Sardinian families continue making for personal consumption",
            "The name means 'rotten cheese' in Sardinian dialect",
            "Considered a delicacy for special occasions in Sardinian culture"
        ],
        "tags": ["cheese", "traditional", "italian", "sardinian", "ancient", "cultural-heritage", "historical"],
        "confidence": {"overall": "high", "flags": ["historical documentation only"]},
        "image_refs": []
    },
    {
        "id": "traditional-queso-de-bola-edam-philippines",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso de Bola (Filipino Christmas Edam)",
        "category": "mains",
        "attribution": "Netherlands/Philippines / 17th Century Trade",
        "source_note": "Dutch Edam became essential Filipino Christmas food through the Manila-Acapulco galleon trade. A fusion tradition.",
        "description": "Ball-shaped waxed cheese in the Dutch Edam tradition, now an essential part of Filipino Christmas celebrations.",
        "servings_yield": "About 2 lbs ball",
        "prep_time": "4 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "partially skimmed cow milk", "quantity": "2", "unit": "gallons", "prep_note": "remove some cream"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "lb", "prep_note": "for brine"},
            {"item": "red cheese wax", "quantity": "1", "unit": "lb", "prep_note": "for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Remove 10-20% of cream from milk for characteristic texture."},
            {"step": 2, "text": "Heat milk to 86°F."},
            {"step": 3, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Stir gently while heating to 95°F over 30 minutes."},
            {"step": 8, "text": "Drain 1/3 whey, add warm water to wash curds (removes lactose)."},
            {"step": 9, "text": "Continue stirring at 95°F for 30 more minutes."},
            {"step": 10, "text": "Drain and pack curds into ball-shaped mold."},
            {"step": 11, "text": "Press at 30 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 12, "text": "Soak in brine for 8 hours."},
            {"step": 13, "text": "Air dry 1-2 weeks, then coat in red wax."},
            {"step": 14, "text": "Age at 55°F for 2-6 months."}
        ],
        "temperature": "86-95°F make, 55°F aging",
        "notes": [
            "Dutch traders brought Edam to the Philippines in the 1600s",
            "Red wax coating became associated with Christmas festivities",
            "Now an essential part of Filipino Noche Buena (Christmas Eve feast)",
            "Often paired with ham and sweet bread (ensaymada)"
        ],
        "tags": ["cheese", "traditional", "dutch", "filipino", "christmas", "edam", "waxed", "17th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-fresco-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Fresco (Mexican Fresh Cheese)",
        "category": "mains",
        "attribution": "Mexico / Colonial Spanish Era",
        "source_note": "Brought by Spanish colonizers, adapted with local techniques. Essential to Mexican cuisine from tacos to enchiladas.",
        "description": "Mexican fresh cheese that crumbles easily, with a mild milky flavor and slight tang, used throughout Mexican cooking.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "2 hours draining",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "white vinegar", "quantity": "1/4", "unit": "cup", "prep_note": "or lime juice"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180-185°F, stirring occasionally to prevent scorching."},
            {"step": 2, "text": "Remove from heat."},
            {"step": 3, "text": "Add vinegar slowly while stirring gently."},
            {"step": 4, "text": "Curds will form and separate from whey within minutes."},
            {"step": 5, "text": "Let rest 10 minutes for curds to consolidate."},
            {"step": 6, "text": "Line colander with cheesecloth, ladle in curds."},
            {"step": 7, "text": "Sprinkle salt over curds, mix gently."},
            {"step": 8, "text": "Tie cheesecloth and hang to drain for 1-2 hours."},
            {"step": 9, "text": "For firmer cheese, press in mold with light weight for 1 hour."},
            {"step": 10, "text": "Refrigerate and use within 1-2 weeks."}
        ],
        "temperature": "180-185°F make",
        "notes": [
            "Does not melt when heated - perfect for sprinkling on hot dishes",
            "Lime juice gives more authentic flavor than vinegar",
            "Can be made from any milk including goat",
            "Essential topping for elote, tacos, tostadas, and enchiladas"
        ],
        "tags": ["cheese", "traditional", "mexican", "fresh", "crumbly", "colonial-era", "quick"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # Advanced Cheese Making Tips
    {
        "id": "cheesemaking-tip-rennet-guide",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Complete Guide to Rennet",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Rennet coagulates milk into curds. Understanding rennet types and usage is fundamental to cheesemaking.",
        "description": "Comprehensive guide to rennet types, sources, dosages, and proper use in cheesemaking.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "rennet", "quantity": "varies", "unit": "", "prep_note": "see types below"}
        ],
        "instructions": [
            {"step": 1, "text": "ANIMAL RENNET: From calf, kid, or lamb stomach. Traditional, produces complex flavors. Not vegetarian."},
            {"step": 2, "text": "VEGETABLE RENNET: From thistle (cardoon), fig sap, or nettles. Traditional in some regions. Can create bitter notes in aged cheese."},
            {"step": 3, "text": "MICROBIAL RENNET: From mold (Rhizomucor). Vegetarian, consistent, but may cause bitterness in long-aged cheese."},
            {"step": 4, "text": "FPC (Fermentation-Produced Chymosin): Genetically modified microbes produce identical enzyme to calf rennet. Vegetarian, consistent, good for aging."},
            {"step": 5, "text": "STRENGTH VARIES: Different brands have different strengths. Follow package directions, adjust from there."},
            {"step": 6, "text": "DILUTION: Always dilute rennet in 20x non-chlorinated water before adding. Helps distribute evenly."},
            {"step": 7, "text": "ADDING: Stir rennet in with up-and-down motion for 30 seconds, then stop all movement immediately."},
            {"step": 8, "text": "STORAGE: Keep refrigerated, away from light. Liquid rennet lasts 6-12 months, tablets longer."},
            {"step": 9, "text": "TROUBLESHOOTING: If no curd forms - rennet may be old, milk may be ultra-pasteurized, or temperature wrong."},
            {"step": 10, "text": "TRADITIONAL RENNET MAKING: Dry and preserve stomach (vell) from young animal, soak in brine to extract enzymes."}
        ],
        "temperature": "Store refrigerated at 38°F",
        "notes": [
            "Less rennet = softer curd, longer set time. More rennet = firmer curd, faster set.",
            "Animal rennet contains multiple enzymes that contribute to cheese flavor development",
            "For vegetarian cheese, use FPC for best aging results",
            "Traditional cheesemakers made their own rennet from local animals"
        ],
        "tags": ["cheese", "tips", "techniques", "rennet", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-ph-acidity",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Understanding pH and Acidity",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Acidity development is the invisible driver of cheesemaking. pH control separates beginners from masters.",
        "description": "Guide to monitoring and controlling acidity in cheesemaking, including target pH levels for different cheese types.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "pH meter or strips", "quantity": "1", "unit": "", "prep_note": "for monitoring"}
        ],
        "instructions": [
            {"step": 1, "text": "FRESH MILK: pH 6.5-6.7. Healthy, fresh milk starts slightly acidic."},
            {"step": 2, "text": "AFTER RIPENING: pH drops to 6.4-6.5 as cultures produce lactic acid."},
            {"step": 3, "text": "AT RENNETING: pH 6.4-6.5 optimal for curd formation."},
            {"step": 4, "text": "AT DRAINING: pH varies by cheese type. Cheddar: 6.0-6.1. Soft cheese: 4.6-4.8."},
            {"step": 5, "text": "AT MILLING (Cheddar-style): pH 5.2-5.4. The critical window for proper texture."},
            {"step": 6, "text": "PASTA FILATA TEST: pH 5.2 is when curds will stretch in hot water. Test small piece."},
            {"step": 7, "text": "PRESSING: pH continues to drop. Final pressed cheese often 5.0-5.3."},
            {"step": 8, "text": "SOFT CHEESE FINISH: pH 4.4-4.6 when fully drained. Higher acid = tangier flavor."},
            {"step": 9, "text": "TOO FAST: Rapid acidification = bitter cheese, weak texture. Slow cultures or reduce dose."},
            {"step": 10, "text": "TOO SLOW: Insufficient acid = safety risk, bland cheese. Check culture viability, increase dose."}
        ],
        "temperature": "N/A",
        "notes": [
            "Traditional cheesemakers didn't have pH meters but developed sensory skills",
            "Taste the whey - sourness indicates acid development",
            "Temperature affects acid development speed - warmer = faster",
            "pH meters for cheese should measure to 0.01 precision"
        ],
        "tags": ["cheese", "tips", "techniques", "ph", "acidity", "guide", "advanced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-equipment-sanitation",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Equipment and Sanitation",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Clean equipment prevents contamination. Good sanitation is the foundation of safe, consistent cheese.",
        "description": "Guide to essential cheesemaking equipment and proper sanitation practices.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "cheesemaking equipment", "quantity": "varies", "unit": "", "prep_note": "see list below"}
        ],
        "instructions": [
            {"step": 1, "text": "ESSENTIAL EQUIPMENT: Large pot (stainless), thermometer, long knife, slotted spoon, colander, cheesecloth, molds."},
            {"step": 2, "text": "NICE TO HAVE: pH meter, cheese press, calcium chloride, aging container, curd harp, draining mat."},
            {"step": 3, "text": "MATERIAL CHOICES: Stainless steel, food-grade plastic, wood (traditional). Avoid aluminum (reacts with acid)."},
            {"step": 4, "text": "PRE-SANITIZE: Before starting, sanitize all equipment that contacts milk. Hot water, then sanitizer."},
            {"step": 5, "text": "SANITIZER OPTIONS: Dilute bleach (1 tbsp/gallon), Star San, iodophor. Rinse bleach, others are no-rinse."},
            {"step": 6, "text": "WATER QUALITY: Use non-chlorinated water for diluting cultures and rennet. Chlorine kills bacteria."},
            {"step": 7, "text": "CHEESECLOTH: Wash in hot soapy water, boil to sanitize, dry completely. Replace when worn."},
            {"step": 8, "text": "MOLDS: Wash immediately after use, sanitize before next use. Dry completely."},
            {"step": 9, "text": "WOODEN EQUIPMENT: Traditional but requires special care. Season with oil, never soak, dry thoroughly."},
            {"step": 10, "text": "POST-CLEANING: Clean everything immediately after use. Dried milk residue is very difficult to remove."}
        ],
        "temperature": "N/A",
        "notes": [
            "Traditional cheesemakers used copper vats that naturally inhibited bacteria",
            "You can start with basic kitchen equipment - upgrade as skills develop",
            "Consistency in sanitation leads to consistency in cheese",
            "Never use soap residue contact surfaces - it inhibits cultures"
        ],
        "tags": ["cheese", "tips", "techniques", "equipment", "sanitation", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-seasonal-variations",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Seasonal and Milk Variations",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Milk changes throughout the year. Traditional cheesemakers worked with these variations, not against them.",
        "description": "Understanding how seasons, feed, and animal cycles affect milk and cheese production.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "seasonal awareness", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "SPRING MILK: Fresh grass = high beta-carotene (yellow), complex flavors. Best for aged cheese."},
            {"step": 2, "text": "SUMMER MILK: Peak production but can be lower in fat. Alpine summer cheese traditions for good reason."},
            {"step": 3, "text": "FALL MILK: Rich and fatty as animals prepare for winter. Excellent for aged cheese."},
            {"step": 4, "text": "WINTER MILK: From hay-fed animals. Paler, simpler flavor. Often lower in fat."},
            {"step": 5, "text": "EARLY LACTATION: Milk is rich in antibodies (colostrum), not suitable for cheesemaking."},
            {"step": 6, "text": "PEAK LACTATION: High volume but lower fat percentage. May need to add cream."},
            {"step": 7, "text": "LATE LACTATION: Lower volume, higher fat and protein. Excellent cheese yield."},
            {"step": 8, "text": "HEAT STRESS: Hot weather reduces milk quality. Traditional practice to make only soft cheese in summer."},
            {"step": 9, "text": "FEED IMPACT: Silage can create off-flavors. Grass-fed milk has different fatty acids than grain-fed."},
            {"step": 10, "text": "TERROIR: Like wine, cheese reflects its place - the soil, plants, water, and climate where animals graze."}
        ],
        "temperature": "N/A",
        "notes": [
            "Traditional alpine cheeses were made only during summer mountain grazing",
            "French AOC rules often specify seasonal production windows",
            "Many 'seasonal' cheeses exist because milk quality changes",
            "Working with nature, not against it, produces the best cheese"
        ],
        "tags": ["cheese", "tips", "techniques", "seasonal", "milk", "guide", "advanced"],
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
