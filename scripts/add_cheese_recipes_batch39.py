#!/usr/bin/env python3
"""Add batch 39 of traditional cheese recipes - More ancient cheeses plus cheese making tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    # Cheese Making Tips and Techniques
    {
        "id": "cheesemaking-tip-milk-quality",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Milk Quality and Selection",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Fundamental principles passed down through generations of cheesemakers. The foundation of all good cheese is quality milk.",
        "description": "Essential guide to selecting and preparing milk for cheese making, covering freshness, fat content, and avoiding common pitfalls.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "fresh milk", "quantity": "varies", "unit": "", "prep_note": "the fresher the better"}
        ],
        "instructions": [
            {"step": 1, "text": "FRESHNESS: Use milk within 2-3 days of milking for best results. Older milk has higher bacterial counts that compete with cheese cultures."},
            {"step": 2, "text": "RAW VS PASTEURIZED: Raw milk produces more complex flavors but requires careful sourcing. Pasteurized works well but avoid ultra-pasteurized (UHT) - the proteins are damaged and won't form proper curds."},
            {"step": 3, "text": "HOMOGENIZATION: Non-homogenized (cream-top) milk is preferred. Homogenized milk produces weaker curds because fat globules are too small to be trapped in the protein matrix."},
            {"step": 4, "text": "FAT CONTENT: Whole milk produces richer cheese. Skim milk can be used but results in drier, less flavorful cheese. For extra richness, add cream."},
            {"step": 5, "text": "CALCIUM CHLORIDE: Add 1/4 tsp per gallon for pasteurized milk to restore calcium lost during heating. This strengthens curd formation."},
            {"step": 6, "text": "GOAT MILK: Naturally homogenized with smaller fat globules. Produces softer curds than cow milk. May need gentler handling."},
            {"step": 7, "text": "SHEEP MILK: Highest in fat and protein. Produces rich, flavorful cheese with excellent yield. Curds form quickly."},
            {"step": 8, "text": "AVOID: Milk from animals on antibiotics, milk with off-odors, milk stored in plastic for extended periods, milk that's been frozen."},
            {"step": 9, "text": "SEASONAL VARIATION: Spring/summer milk from pastured animals has more beta-carotene (yellow color) and complex flavors than winter milk."},
            {"step": 10, "text": "TESTING: If unsure about milk quality, make a small test batch first. Good milk should form a clean, firm curd that cuts cleanly."}
        ],
        "temperature": "Store milk at 38-40°F until use",
        "notes": [
            "The saying 'you can't make good cheese from bad milk' is absolutely true",
            "Local farm-fresh milk, even pasteurized, outperforms grocery store milk",
            "If using store milk, choose organic whole milk with the latest date",
            "Some grocery milk contains additives that interfere with cheesemaking"
        ],
        "tags": ["cheese", "tips", "techniques", "milk", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-temperature-control",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Temperature Control Mastery",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Temperature is the most critical variable in cheesemaking. Small differences create dramatically different cheeses.",
        "description": "Comprehensive guide to understanding and controlling temperatures throughout the cheesemaking process.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "accurate thermometer", "quantity": "1", "unit": "", "prep_note": "digital preferred, calibrated"}
        ],
        "instructions": [
            {"step": 1, "text": "RIPENING TEMPERATURE (68-90°F): Lower temps favor mesophilic cultures (soft cheeses), higher temps favor thermophilic (hard cheeses)."},
            {"step": 2, "text": "RENNETING TEMPERATURE: Most cheeses set at 86-90°F. Goat milk often lower (82-86°F). Higher temps = firmer curds but can cook proteins."},
            {"step": 3, "text": "COOKING TEMPERATURE: Gradual increases (1-2°F per minute max) prevent shocking cultures. Hard cheeses cook higher (116-130°F) than soft."},
            {"step": 4, "text": "WATER BATH METHOD: Place pot in larger pot of water for gentle, even heating. Prevents scorching and hot spots."},
            {"step": 5, "text": "HOLDING TEMPERATURE: Maintain cooking temp while stirring to expel whey. Rushing this step = wet, weak cheese."},
            {"step": 6, "text": "STRETCHING TEMPERATURE (PASTA FILATA): 170-180°F water for mozzarella-type. Too cool = won't stretch. Too hot = grainy texture."},
            {"step": 7, "text": "PRESSING TEMPERATURE: Press while curds are still warm (above 80°F) for proper knitting. Cold curds don't fuse well."},
            {"step": 8, "text": "CAVE/AGING TEMPERATURE: Most cheeses age at 50-58°F. Too warm = rapid aging, off-flavors. Too cold = aging stops."},
            {"step": 9, "text": "HUMIDITY CONTROL: High humidity (85-95%) for washed rinds, lower (75-85%) for natural rinds. Temperature affects humidity."},
            {"step": 10, "text": "THERMOMETER CALIBRATION: Test in ice water (32°F) and boiling water (212°F adjusted for altitude). A 2°F error can ruin cheese."}
        ],
        "temperature": "Various - see steps",
        "notes": [
            "Invest in a good digital thermometer - analog dairy thermometers can be inaccurate",
            "Use a timer when heating - it's easy to overshoot temperature while distracted",
            "Room temperature affects everything - cheesemaking is harder in very hot or cold kitchens",
            "Professional cheesemakers obsess over temperature for good reason"
        ],
        "tags": ["cheese", "tips", "techniques", "temperature", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-cultures-explained",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Understanding Cultures and Molds",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Cultures are the living heart of cheese. Understanding them transforms cheesemaking from recipe-following to true craft.",
        "description": "Guide to the bacteria, molds, and yeasts used in cheesemaking, including when and how to use each type.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "cheese cultures", "quantity": "varies", "unit": "", "prep_note": "see types below"}
        ],
        "instructions": [
            {"step": 1, "text": "MESOPHILIC CULTURES: Work at 68-102°F. Used for Cheddar, Gouda, Brie, Camembert, blue cheeses, feta. Most versatile type."},
            {"step": 2, "text": "THERMOPHILIC CULTURES: Work at 68-132°F, optimum 104-112°F. Used for Swiss, Parmesan, Mozzarella, Provolone. Heat-loving."},
            {"step": 3, "text": "PENICILLIUM CANDIDUM: White mold for bloomy rinds (Brie, Camembert). Creates the fluffy white exterior."},
            {"step": 4, "text": "PENICILLIUM ROQUEFORTI: Blue-green mold for blue cheeses. Different strains create different blue characteristics."},
            {"step": 5, "text": "GEOTRICHUM CANDIDUM: Yeast/mold for wrinkled rinds (French goat cheeses). Creates brainy texture on surface."},
            {"step": 6, "text": "BREVIBACTERIUM LINENS: Bacteria for washed-rind cheeses. Creates orange color and pungent aroma."},
            {"step": 7, "text": "PROPIONIBACTERIUM: Creates eyes (holes) in Swiss-type cheeses by producing CO2 during warm aging."},
            {"step": 8, "text": "CULTURE STORAGE: Keep frozen (-4°F) for long-term, refrigerated for weeks. Never refreeze thawed cultures."},
            {"step": 9, "text": "NATURAL STARTERS: Whey from previous batch, clabber, kefir, or yogurt can culture milk traditionally."},
            {"step": 10, "text": "DOSAGE: Generally 1/8-1/4 tsp per gallon. More isn't better - too much culture causes rapid acidification and bitter flavors."}
        ],
        "temperature": "Storage: -4°F frozen, 38°F refrigerated",
        "notes": [
            "Cultures are living organisms - treat them with respect",
            "Using the wrong culture type is the #1 beginner mistake",
            "Traditional cheeses used wild cultures from the environment",
            "Modern packet cultures are more consistent but less complex than traditional methods"
        ],
        "tags": ["cheese", "tips", "techniques", "cultures", "molds", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-curd-handling",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Cutting and Handling Curds",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "How you cut and handle curds determines the final texture of your cheese. This is where art meets science.",
        "description": "Techniques for cutting, stirring, and handling curds to achieve different cheese textures from soft to hard.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "curd cutting knife", "quantity": "1", "unit": "", "prep_note": "long blade reaching pot bottom"},
            {"item": "curd harp/whisk", "quantity": "1", "unit": "", "prep_note": "for fine cutting"}
        ],
        "instructions": [
            {"step": 1, "text": "CLEAN BREAK TEST: Insert knife at angle, lift gently. Curd should split cleanly with clear whey. If mushy, wait longer."},
            {"step": 2, "text": "CUT SIZE MATTERS: Large cuts (1 inch) = more moisture = softer cheese. Small cuts (rice grain) = less moisture = harder cheese."},
            {"step": 3, "text": "CUTTING TECHNIQUE: Cut vertical grid first, then hold knife at 45° and cut horizontal. Goal is even-sized cubes."},
            {"step": 4, "text": "HEALING TIME: After cutting, let curds rest 5-10 minutes. This 'heals' cut surfaces and prevents shattering during stirring."},
            {"step": 5, "text": "STIRRING: Start very gently - curds are fragile after cutting. Increase agitation gradually as curds firm up."},
            {"step": 6, "text": "CURD SIZE DURING COOKING: Curds shrink as they expel whey. Final size should be consistent - uneven = uneven moisture."},
            {"step": 7, "text": "THE SQUEEZE TEST: Grab a handful of curds, squeeze, release. Curds should mat together but break apart cleanly when pressed."},
            {"step": 8, "text": "FOR SOFT CHEESE: Minimal cutting and stirring. Ladle whole curds gently. Handle as little as possible."},
            {"step": 9, "text": "FOR HARD CHEESE: Fine cutting, extended stirring, higher cooking temps. Goal is firm, dry curds."},
            {"step": 10, "text": "WASHING CURDS: For Gouda-style, remove whey and add warm water. This removes lactose, creating sweeter cheese."}
        ],
        "temperature": "N/A",
        "notes": [
            "Patience during curd handling pays dividends in final texture",
            "Rough handling creates 'shattered' curds that won't knit properly",
            "Traditional cheesemakers develop an intuitive feel for curd readiness",
            "If in doubt, err on the side of gentler handling"
        ],
        "tags": ["cheese", "tips", "techniques", "curds", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-pressing-molding",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Pressing and Molding Techniques",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Proper pressing expels whey and fuses curds into a unified wheel. Too much or too little pressure creates problems.",
        "description": "Guide to pressing cheese properly, including pressure levels, timing, and troubleshooting common pressing issues.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "cheese mold", "quantity": "1", "unit": "", "prep_note": "with follower"},
            {"item": "cheese press", "quantity": "1", "unit": "", "prep_note": "or weights"}
        ],
        "instructions": [
            {"step": 1, "text": "MOLD PREPARATION: Line with cheesecloth for smooth rind, or use bare for textured rind (basket weave pattern)."},
            {"step": 2, "text": "FILLING: Pack curds firmly but don't crush. For even texture, add in layers, pressing each gently."},
            {"step": 3, "text": "GRADUAL PRESSURE: Start low (10-15 lbs), increase over hours. Sudden high pressure traps whey pockets inside."},
            {"step": 4, "text": "SOFT CHEESE: Minimal or no pressing. Let gravity drain whey. Pressing would destroy delicate texture."},
            {"step": 5, "text": "SEMI-HARD CHEESE: Moderate pressure (20-40 lbs) for 6-12 hours. Goal is smooth rind, slight moisture retention."},
            {"step": 6, "text": "HARD CHEESE: Heavy pressure (40-100 lbs) for 12-24 hours. Goal is very smooth, closed rind with dry interior."},
            {"step": 7, "text": "FLIPPING: Turn cheese every 30 minutes initially, then every few hours. This ensures even pressing and smooth surfaces."},
            {"step": 8, "text": "WARM PRESSING: Press while curds are warm (above 80°F). Cold curds don't knit together properly."},
            {"step": 9, "text": "TROUBLESHOOTING CRACKS: Cracks mean curds were too cold, too dry, or pressed too hard too fast."},
            {"step": 10, "text": "WHEY RELEASE: Clear whey should run steadily at first, then slow. Milky whey = pressing too hard, losing butterfat."}
        ],
        "temperature": "Press while curds are above 80°F",
        "notes": [
            "Improvised presses work fine - water jugs, bricks, anything heavy",
            "Calculate pressure as weight divided by surface area of cheese",
            "Traditional presses used large stones - very effective",
            "A too-smooth rind can indicate over-pressing"
        ],
        "tags": ["cheese", "tips", "techniques", "pressing", "molding", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-brining-salting",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Brining and Salting Methods",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Salt is essential - it preserves, develops flavor, and controls moisture. Different methods suit different cheeses.",
        "description": "Comprehensive guide to salting cheese, including dry salting, brining, and rubbing techniques.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "cheese salt", "quantity": "varies", "unit": "", "prep_note": "non-iodized, flake preferred"},
            {"item": "water", "quantity": "varies", "unit": "", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "SALT TYPES: Use cheese salt (flake) or kosher salt. NEVER use iodized salt - iodine kills beneficial bacteria and causes off-flavors."},
            {"step": 2, "text": "SATURATED BRINE: Dissolve salt in water until no more dissolves (about 23% salt). Add 1 tbsp calcium chloride per gallon to prevent soft rind."},
            {"step": 3, "text": "BRINE TIME: Rule of thumb - 2 hours per pound of cheese. Small cheeses: hours. Large wheels: days."},
            {"step": 4, "text": "BRINE TEMPERATURE: Keep at 50-55°F. Warm brine = soft rind, rapid salt uptake. Cold brine = firmer rind, slower uptake."},
            {"step": 5, "text": "FLOATING: Cheese floats in brine. Sprinkle salt on exposed top, or flip halfway through brining."},
            {"step": 6, "text": "DRY SALTING: Rub salt on all surfaces. Use about 2% of cheese weight. For blue cheese, salt in layers during molding."},
            {"step": 7, "text": "SALTING CURDS: Some cheeses (Cheddar) salt milled curds before pressing. Use 2-2.5% of curd weight."},
            {"step": 8, "text": "BRINE MAINTENANCE: Skim surface regularly, maintain salt level, keep cold. Brine lasts indefinitely if maintained."},
            {"step": 9, "text": "AFTER BRINING: Air dry until surface is no longer tacky (1-3 days) before aging or coating."},
            {"step": 10, "text": "UNDER/OVER SALTING: Under-salted cheese spoils easily and lacks flavor. Over-salted is unpleasant but safer."}
        ],
        "temperature": "Brine at 50-55°F",
        "notes": [
            "Salt does more than add flavor - it controls moisture, rind formation, and microbial activity",
            "Ancient cheese preservation relied heavily on salt",
            "Different salt granule sizes dissolve at different rates - flake salt is most consistent",
            "Some traditional cheeses use seawater or mineral-rich well water for brine"
        ],
        "tags": ["cheese", "tips", "techniques", "brining", "salting", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-aging-affinage",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Aging and Affinage",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Aging transforms fresh curds into complex, flavorful cheese. The French call this art 'affinage' - ripening.",
        "description": "Guide to aging cheese at home, including environment setup, rind care, and troubleshooting aging problems.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "aging space", "quantity": "1", "unit": "", "prep_note": "cave, refrigerator, or cellar"}
        ],
        "instructions": [
            {"step": 1, "text": "IDEAL CONDITIONS: 50-58°F temperature, 80-95% humidity depending on cheese type. Consistent is key."},
            {"step": 2, "text": "HOME CAVE OPTIONS: Wine fridge, mini-fridge with thermostat, basement corner, or plastic box in regular fridge."},
            {"step": 3, "text": "HUMIDITY CONTROL: Place water tray in aging space, use damp towels, or age in covered plastic containers."},
            {"step": 4, "text": "AIR CIRCULATION: Some airflow prevents ammonia buildup. Crack containers slightly, or install small fan."},
            {"step": 5, "text": "TURNING: Flip cheese regularly (daily for young cheese, weekly for aged) to ensure even moisture distribution."},
            {"step": 6, "text": "NATURAL RIND: Forms naturally with proper conditions. Brush weekly to control unwanted mold."},
            {"step": 7, "text": "WASHED RIND: Wipe with brine, beer, or wine every 2-3 days. Develops orange color and strong aroma."},
            {"step": 8, "text": "WAX/VACUUM: For hands-off aging, wax or vacuum seal cheese. Keeps moisture in, prevents contamination."},
            {"step": 9, "text": "UNWANTED MOLD: Blue/black mold on non-blue cheese: wipe with vinegar solution. Pink/red: discard cheese."},
            {"step": 10, "text": "PATIENCE: Most cheese needs minimum 2 months aging. The best aged cheeses take 1-3 years. Don't rush."}
        ],
        "temperature": "50-58°F aging",
        "notes": [
            "Traditional caves maintained perfect conditions naturally",
            "Modern cheese fridges try to replicate cave conditions",
            "Temperature fluctuation causes sweating and cracks",
            "The affineur's skill in aging is as important as the cheesemaker's skill in making"
        ],
        "tags": ["cheese", "tips", "techniques", "aging", "affinage", "guide", "fundamentals"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cheesemaking-tip-troubleshooting",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheese Making Tip: Troubleshooting Common Problems",
        "category": "mains",
        "attribution": "Traditional Cheesemaking Wisdom",
        "source_note": "Every cheesemaker faces problems. Learning to diagnose and fix issues is part of the craft.",
        "description": "Solutions to the most common cheesemaking problems, from weak curds to off-flavors.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "troubleshooting knowledge", "quantity": "N/A", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "WEAK/SOFT CURDS: Usually caused by ultra-pasteurized milk, insufficient rennet, or low temperature. Add calcium chloride, use more rennet, or increase temp."},
            {"step": 2, "text": "CURDS WON'T FORM: Milk may be ultra-pasteurized (UHT) or have antibiotics. Also check rennet freshness - old rennet loses potency."},
            {"step": 3, "text": "RUBBERY TEXTURE: Too much rennet, too high cooking temperature, or over-stirring. Use less rennet, lower temps, gentler handling."},
            {"step": 4, "text": "DRY/CRUMBLY CHEESE: Over-acidification, too small curd cuts, too much pressing, or too long cooking. Adjust process timing."},
            {"step": 5, "text": "WET/SLIMY CHEESE: Under-acidification, too large curd cuts, insufficient pressing, or too humid aging. Increase acid development or pressing."},
            {"step": 6, "text": "BITTER FLAVOR: Over-acidification, contamination, or using iodized salt. Check culture dosage and salt type."},
            {"step": 7, "text": "AMMONIA SMELL: Over-ripe soft cheese or poor aging ventilation. Soft cheeses are past prime; air out aging space."},
            {"step": 8, "text": "CRACKS IN RIND: Curds too cold when pressed, pressed too hard too fast, or aging humidity too low. Adjust conditions."},
            {"step": 9, "text": "UNWANTED MOLD: Contamination from environment. Sanitize everything, control aging conditions, consider different location."},
            {"step": 10, "text": "UNEVEN EYES (SWISS): Temperature fluctuation during warm-room phase, or inconsistent Propionibacteria distribution. Maintain steady conditions."}
        ],
        "temperature": "N/A",
        "notes": [
            "Keep a cheesemaking journal - it helps identify patterns in problems",
            "Most problems are caused by milk quality, temperature, or timing",
            "Failed cheese can often be used for cooking (mac and cheese, grilled cheese)",
            "Every mistake teaches something valuable"
        ],
        "tags": ["cheese", "tips", "techniques", "troubleshooting", "problems", "guide", "fundamentals"],
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
