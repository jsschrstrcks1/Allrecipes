#!/usr/bin/env python3
"""Add comprehensive Dutch cheese recipes to the cheese category."""

import json

DUTCH_CHEESE_RECIPES = [
    # === CLASSIC DUTCH AGED GOUDAS ===
    {
        "id": "dutch-aged-gouda-oud",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Oud Gouda (Aged Dutch Gouda)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Classic aged Gouda from the Netherlands, minimum 10-12 months aging.",
        "description": "Oud (old) Gouda develops deep caramel notes and crystalline texture through extended aging. The cheese becomes firm, crumbly, and intensely flavorful with characteristic tyrosine crystals that provide pleasant crunch.",
        "servings_yield": "About 8-10 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "6 hours",
        "total_time": "10-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture (Flora Danica)", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"},
            {"item": "cheese wax or vacuum seal bags", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set for 45-60 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Remove 30% of the whey. Replace with same amount of 175°F (80°C) water to raise temperature to 100°F (38°C). This is the critical 'washing' step."},
            {"step": 5, "text": "Stir continuously for 30 minutes at 100°F (38°C) until curds shrink and firm."},
            {"step": 6, "text": "Drain curds and press into wheel mold at 30 lbs for 30 minutes."},
            {"step": 7, "text": "Flip cheese and press at 40 lbs for 12 hours."},
            {"step": 8, "text": "Brine in saturated salt solution for 24-48 hours (3 hours per pound)."},
            {"step": 9, "text": "Air dry at room temperature for 2-3 days until rind forms."},
            {"step": 10, "text": "Wax or vacuum seal. Age at 55°F (13°C) and 80-85% humidity for 10-12 months minimum."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Oud means 'old' in Dutch - aged minimum 10-12 months",
            "Washing curds with hot water removes lactose, sweetening the cheese",
            "Tyrosine crystals develop during extended aging, adding pleasant crunch",
            "Traditional in the Netherlands as a special occasion cheese"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "aged", "hard", "crystalline"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-extra-aged-gouda-overjarig",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Overjarig Gouda (Extra-Aged Dutch Gouda)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Premium extra-aged Gouda, 18+ months aging for intense flavor.",
        "description": "Overjarig (over a year) Gouda is the pinnacle of Dutch cheese aging. Deep amber color, intense butterscotch and caramel notes, and abundant crunchy crystals characterize this prestigious cheese.",
        "servings_yield": "About 8-10 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "6 hours",
        "total_time": "18-36 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture (Flora Danica)", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"},
            {"item": "cheese wax", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 50-60 minutes until very firm curd."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes for denser texture."},
            {"step": 4, "text": "Remove 35% whey. Add 180°F (82°C) water to raise to 102°F (39°C). Slightly higher temp for firmer cheese."},
            {"step": 5, "text": "Stir 40 minutes at temperature until curds are very firm."},
            {"step": 6, "text": "Press at 35 lbs for 30 min, flip, 50 lbs for 24 hours for dense texture."},
            {"step": 7, "text": "Brine 36-48 hours in saturated solution."},
            {"step": 8, "text": "Air dry 3-4 days. Apply wax in two coats."},
            {"step": 9, "text": "Age at 55°F (13°C) for minimum 18 months, ideally 24-36 months. Turn weekly first 3 months, then monthly."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Overjarig literally means 'over a year old'",
            "Smaller curd size and higher cook temp create denser paste for longer aging",
            "Cheese will lose 15-20% weight during extended aging",
            "Premium pricing reflects the patience required"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "extra-aged", "premium", "crystalline"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SPICED DUTCH CHEESES ===
    {
        "id": "dutch-komijnekaas",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Komijnekaas (Dutch Cumin Gouda)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Traditional Dutch Gouda flavored with cumin seeds, a centuries-old specialty.",
        "description": "Komijnekaas is Gouda studded with whole cumin seeds. The warm, earthy spice complements the sweet, buttery cheese. A Dutch tradition dating to medieval times when spices were added as preservatives.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "whole cumin seeds", "quantity": "3", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast cumin seeds lightly in dry pan to release oils. Cool completely."},
            {"step": 2, "text": "Heat milk to 86°F (30°C). Add starter and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Remove 30% whey, add hot water to raise to 100°F (38°C)."},
            {"step": 6, "text": "Stir 25 minutes at temperature."},
            {"step": 7, "text": "Add toasted cumin seeds to curds, mix thoroughly."},
            {"step": 8, "text": "Drain and press at 20 lbs for 30 min, flip, 30 lbs for 8 hours."},
            {"step": 9, "text": "Brine 12 hours. Wax when dry."},
            {"step": 10, "text": "Age at 55°F (13°C) for 2-4 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Komijn is Dutch for cumin",
            "Toasting cumin first intensifies flavor and kills any bacteria",
            "Cumin was historically added for its preservative properties",
            "Popular with dark rye bread and Dutch beer"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "spiced", "cumin", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-leidse-kaas",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Leidse Kaas (Leiden Cheese with Cumin and Caraway)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Protected Dutch cheese from Leiden, made with both cumin and caraway seeds.",
        "description": "Leidse kaas is a semi-hard cheese from Leiden characterized by its combination of cumin AND caraway seeds. The crossed keys of Leiden are traditionally stamped on the rind. Made with partially skimmed milk for a firmer texture.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "partially skimmed cow's milk (2%)", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "whole cumin seeds", "quantity": "2", "unit": "tbsp"},
            {"item": "whole caraway seeds", "quantity": "1", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast cumin and caraway seeds separately until fragrant. Cool completely and mix."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 40-50 minutes."},
            {"step": 4, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 104°F (40°C) over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at temperature until curds are firm, about 20 minutes."},
            {"step": 7, "text": "Add seed mixture to curds, distribute evenly."},
            {"step": 8, "text": "Drain and press at 25 lbs for 30 min, flip, 35 lbs for 12 hours."},
            {"step": 9, "text": "Brine 16-20 hours in saturated solution."},
            {"step": 10, "text": "Age at 55°F (13°C) for 3-12 months. Rub rind weekly with brine solution."}
        ],
        "temperature": "90-104°F (32-40°C)",
        "notes": [
            "Leiden cheese dates to the 16th century",
            "Traditionally made with buttermilk from butter production",
            "Crossed keys of Leiden branded on authentic wheels",
            "Lower fat from skimmed milk allows longer aging without becoming greasy"
        ],
        "tags": ["cheese", "Dutch", "Leiden", "spiced", "cumin", "caraway", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-boeren-leidse",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Boeren-Leidse met Sleutels (Farmhouse Leiden Cheese)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "EU Protected Designation of Origin farmhouse cheese from Leiden region.",
        "description": "Boeren-Leidse met sleutels ('Farmhouse Leiden with keys') is the protected farmhouse version of Leiden cheese. Made only on farms in the Leiden region using raw milk from the farm's own cows. The crossed keys emblem indicates authenticity.",
        "servings_yield": "About 8-12 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "6-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk (farm-fresh, partially skimmed)", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture or clabber", "quantity": "1/2", "unit": "cup"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "whole cumin seeds", "quantity": "4", "unit": "tbsp"},
            {"item": "whole caraway seeds", "quantity": "2", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use raw milk within 24 hours of milking. Skim cream for butter, retain buttermilk for starter."},
            {"step": 2, "text": "Heat milk to 88°F (31°C). Add fresh buttermilk or starter, ripen 1 hour."},
            {"step": 3, "text": "Add rennet and let set 45 minutes until firm."},
            {"step": 4, "text": "Cut curds into small cubes. Stir gently while heating to 102°F (39°C)."},
            {"step": 5, "text": "Continue stirring until curds are quite firm."},
            {"step": 6, "text": "Mix cumin and caraway into curds."},
            {"step": 7, "text": "Press into traditional flat wheel shape at 30 lbs for 1 hour, flip and press overnight at 40 lbs."},
            {"step": 8, "text": "Brand with crossed keys stamp while cheese is still soft."},
            {"step": 9, "text": "Brine 24 hours per 2 lbs of cheese."},
            {"step": 10, "text": "Age on wooden boards at 55°F (13°C) for 6-12 months. Rub weekly with cloth dampened in brine."}
        ],
        "temperature": "88-102°F (31-39°C)",
        "notes": [
            "Boeren means 'farmer' - must be made on the farm",
            "Sleutels means 'keys' - the Leiden city symbol",
            "PDO protected since 1997 by EU law",
            "Raw milk gives more complex flavor than pasteurized versions"
        ],
        "tags": ["cheese", "Dutch", "Leiden", "farmhouse", "raw milk", "PDO", "cumin", "caraway"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SPECIALTY DUTCH CHEESES ===
    {
        "id": "dutch-maasdam-swiss-style",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maasdam (Dutch Swiss-Style Cheese)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Dutch cheese developed in the 1980s as an alternative to imported Emmental.",
        "description": "Maasdam was created by Dutch cheesemakers to compete with Swiss Emmental. It features large round eyes, sweet nutty flavor, and supple texture. Aged shorter than Swiss cheese, it's milder and more affordable.",
        "servings_yield": "About 6-8 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "4-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "5", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii (for eyes)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add thermophilic starter and P. shermanii. Ripen 15 minutes."},
            {"step": 2, "text": "Raise temperature to 95°F (35°C). Add calcium chloride, then rennet. Let set 30-40 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes - small for this style."},
            {"step": 4, "text": "Let curds rest 5 minutes, then begin stirring."},
            {"step": 5, "text": "Slowly heat to 122°F (50°C) over 45 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at 122°F, stirring until curds are quite firm, about 30 minutes."},
            {"step": 7, "text": "Drain and press at 20 lbs for 30 min, flip, 35 lbs for 12-24 hours."},
            {"step": 8, "text": "Brine in saturated solution for 24 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) for 2 weeks, then move to warm room 68-72°F (20-22°C) for 2-3 weeks for eye development."},
            {"step": 10, "text": "Return to 55°F for 2-8 more weeks until desired flavor develops."}
        ],
        "temperature": "90-122°F (32-50°C)",
        "notes": [
            "Named after the Maas River (Meuse) region",
            "Developed as affordable Emmental alternative for Dutch market",
            "Shorter aging than Swiss cheese gives milder flavor",
            "The warm room period is essential for signature large eyes"
        ],
        "tags": ["cheese", "Dutch", "Swiss-style", "eye cheese", "semi-hard"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-roomano-pradera",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Roomano Pradera (Dutch Aged Parmesan-Style)",
        "category": "cheese",
        "attribution": "Dutch artisan cheese",
        "source_note": "Premium aged Dutch cheese with Parmesan-like characteristics, aged 4+ years.",
        "description": "Roomano Pradera is an intensely aged Dutch cheese with crystalline texture similar to Parmigiano-Reggiano. Aged 4 or more years, it develops deep umami notes, crunchy crystals, and butterscotch sweetness.",
        "servings_yield": "About 8-10 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "6 hours",
        "total_time": "4-5 years aging",
        "ingredients": [
            {"item": "partially skimmed cow's milk", "quantity": "6", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use partially skimmed milk (remove cream from evening milk, combine with morning milk)."},
            {"step": 2, "text": "Heat to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45-50 minutes until very firm."},
            {"step": 4, "text": "Cut curds into rice-sized pieces - as small as possible."},
            {"step": 5, "text": "Slowly heat to 131°F (55°C) over 45 minutes while stirring constantly. High cook temperature is essential."},
            {"step": 6, "text": "Hold at temperature, stirring until curds are very dry and firm, about 30-40 minutes."},
            {"step": 7, "text": "Drain and press immediately at 40 lbs for 30 min, flip, 50 lbs for 48 hours."},
            {"step": 8, "text": "Brine in saturated solution for 3-4 days, turning daily."},
            {"step": 9, "text": "Age at 55°F (13°C) and 80% humidity for minimum 4 years. Brush weekly first year, monthly thereafter."}
        ],
        "temperature": "95-131°F (35-55°C)",
        "notes": [
            "Roomano refers to Roman-style (Parmesan tradition)",
            "Pradera is a premium Dutch cheese producer",
            "Very high cooking temperature creates dense, dry texture for long aging",
            "Cheese will lose 25-30% weight during 4+ year aging"
        ],
        "tags": ["cheese", "Dutch", "Parmesan-style", "extra-aged", "grating", "crystalline"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-beemster-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Beemster Classic (Premium Polder Gouda)",
        "category": "cheese",
        "attribution": "Dutch artisan cheese",
        "source_note": "Premium Gouda from Beemster polder, known for exceptionally rich milk.",
        "description": "Beemster Classic is a premium Gouda from the Beemster polder north of Amsterdam. The UNESCO-protected polder's mineral-rich clay soil produces exceptionally creamy milk, resulting in butter-rich cheese with caramel notes.",
        "servings_yield": "About 6 lbs wheel",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "18 months aging",
        "ingredients": [
            {"item": "whole cow's milk (high-fat, ideally from polder pastures)", "quantity": "5", "unit": "gallons"},
            {"item": "mesophilic starter culture (Flora Danica)", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat rich, high-fat milk to 86°F (30°C). Add starter and ripen 30-40 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-50 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Remove 30% whey. Add hot water (175°F/80°C) to raise temperature to 100°F (38°C)."},
            {"step": 5, "text": "Stir 35-40 minutes at temperature for premium texture."},
            {"step": 6, "text": "Drain and press at 25 lbs for 30 min, flip, 35 lbs for 12 hours."},
            {"step": 7, "text": "Brine 24-30 hours in saturated solution."},
            {"step": 8, "text": "Air dry and wax with food-grade wax."},
            {"step": 9, "text": "Age at 55°F (13°C) for 18 months minimum for Classic designation."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Beemster polder was drained in 1612 - UNESCO World Heritage Site",
            "Mineral-rich clay soil creates uniquely nutritious grass",
            "Higher milk fat content produces creamier aged cheese",
            "Classic aged 18 months; XO aged 26 months; Royaal aged 30+ months"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "premium", "polder", "Beemster"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-graskaas",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Graskaas (Dutch Spring Grass Cheese)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Seasonal Dutch cheese made from first spring milk when cows return to pasture.",
        "description": "Graskaas ('grass cheese') is made in late April/early May from the first milk after cows return to fresh spring pastures. The cheese is notably yellow from beta-carotene in new grass, with distinctive sweet, grassy flavor.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "3.5 hours",
        "total_time": "4-6 weeks aging (young) to 4 months",
        "ingredients": [
            {"item": "whole cow's milk (from spring pasture, late April/May)", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use only milk from cows that have been on fresh spring pasture for at least 2 weeks."},
            {"step": 2, "text": "Heat milk to 86°F (30°C). Note the distinctly yellow color from grass beta-carotene."},
            {"step": 3, "text": "Add starter and ripen 30 minutes."},
            {"step": 4, "text": "Add calcium chloride, then rennet. Let set 40-45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 6, "text": "Remove 30% whey, replace with 100°F (38°C) water."},
            {"step": 7, "text": "Stir 25 minutes until curds firm."},
            {"step": 8, "text": "Drain and press at 20 lbs for 30 min, flip, 30 lbs for 8 hours."},
            {"step": 9, "text": "Brine 12 hours."},
            {"step": 10, "text": "Age 4-6 weeks for traditional young graskaas, or up to 4 months for more developed flavor."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Graskaas is released on third Thursday of June in Netherlands",
            "Yellow color comes from beta-carotene in fresh spring grass",
            "Flavor profile is sweeter and grassier than winter milk cheese",
            "Limited seasonal production makes it a Dutch delicacy"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "seasonal", "spring", "grass-fed"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-reypenaer-vsop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Reypenaer VSOP (Premium Aged Dutch Gouda)",
        "category": "cheese",
        "attribution": "Dutch artisan cheese",
        "source_note": "Premium aged Gouda from Reypenaer, aged in historic warehouses.",
        "description": "Reypenaer VSOP is aged 24 months in historic warehouses along Amsterdam canals. The climate-controlled natural aging develops complex butterscotch, whiskey, and caramel notes with signature crystalline texture.",
        "servings_yield": "About 8-10 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "24 months aging",
        "ingredients": [
            {"item": "whole cow's milk (from specific farms)", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture (proprietary blend)", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter culture and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 50 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Remove 30% whey. Add hot water to raise to 100°F (38°C)."},
            {"step": 5, "text": "Stir 35 minutes at temperature until curds are properly firm."},
            {"step": 6, "text": "Drain and press at 30 lbs for 30 min, flip, 40 lbs for 24 hours."},
            {"step": 7, "text": "Brine 30-36 hours in saturated solution."},
            {"step": 8, "text": "Air dry 3-4 days. Apply natural rind treatment or wax."},
            {"step": 9, "text": "Age at 55°F (13°C) and 80% humidity for 24 months. Turn weekly first 6 months, biweekly thereafter."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "VSOP means 'Very Superior Old Product' (borrowed from cognac terminology)",
            "Reypenaer ages cheese in 100+ year old Amsterdam warehouses",
            "Natural climate fluctuation contributes to complex flavor development",
            "Premium pricing reflects aging time and warehouse real estate costs"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "premium", "aged", "VSOP"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-noord-hollandse-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Noord-Hollandse Gouda (North Holland Gouda)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "EU Protected Geographical Indication cheese from North Holland province.",
        "description": "Noord-Hollandse Gouda is a PGI-protected cheese made exclusively in North Holland province. Distinguished by a stamp guaranteeing origin, it represents the classic Dutch Gouda style from the traditional heartland of Dutch cheesemaking.",
        "servings_yield": "About 8-12 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "4 weeks to 12+ months",
        "ingredients": [
            {"item": "whole cow's milk (from North Holland)", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-50 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 30% whey. Add hot water (175°F/80°C) to raise temperature to 100°F (38°C). Stir during addition."},
            {"step": 5, "text": "Stir 30-35 minutes at temperature until curds are properly firm."},
            {"step": 6, "text": "Drain and press into traditional wheel shape at 25 lbs for 30 min, flip, 35 lbs for 12 hours."},
            {"step": 7, "text": "Brine 24-36 hours in saturated solution."},
            {"step": 8, "text": "Air dry and apply casein stamp before waxing."},
            {"step": 9, "text": "Age at 55°F (13°C) for 4 weeks (jong) to 12+ months (oud)."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "PGI protected - must be made in North Holland province",
            "Traditional center of Dutch cheese production",
            "Casein stamp guarantees origin and quality",
            "Available in jong (young), belegen (mature), and oud (old) versions"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "PGI", "North Holland", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-boerenkaas",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Boerenkaas (Dutch Farmhouse Raw Milk Gouda)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Protected Dutch farmhouse cheese made with raw milk from the farm's own herd.",
        "description": "Boerenkaas ('farmer's cheese') is the protected designation for farmhouse Gouda made with raw milk from the farm's own cows. More complex and variable than factory cheese, each farm's terroir produces unique flavor profiles.",
        "servings_yield": "About 8-12 lbs wheel",
        "prep_time": "2 hours",
        "cook_time": "5 hours",
        "total_time": "2-24 months aging",
        "ingredients": [
            {"item": "raw cow's milk (same-day, from farm herd)", "quantity": "6", "unit": "gallons"},
            {"item": "mesophilic starter culture or fresh whey starter", "quantity": "1/2", "unit": "cup"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use raw milk within hours of milking - never refrigerate. Warm to 86°F (30°C)."},
            {"step": 2, "text": "Add whey starter from previous batch or culture. Ripen 30-45 minutes."},
            {"step": 3, "text": "Add rennet and let set 45-50 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Remove 30% whey, replace with hot water to raise to 100°F (38°C)."},
            {"step": 6, "text": "Stir 30 minutes at temperature."},
            {"step": 7, "text": "Drain and press at 25 lbs for 30 min, flip, 35 lbs for 12-24 hours."},
            {"step": 8, "text": "Brine 24-36 hours. Apply Boerenkaas casein stamp."},
            {"step": 9, "text": "Age on wooden boards at 55°F (13°C). Turn and brush weekly."},
            {"step": 10, "text": "Age minimum 2 months for jong, 4-12 months for belegen, 12-24+ months for oud."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Boerenkaas is legally protected - must be farmhouse, raw milk, farm's own herd",
            "Only about 300 farms in Netherlands still make true Boerenkaas",
            "No calcium chloride needed with fresh raw milk",
            "Each farm develops unique flavor from local pastures and microflora"
        ],
        "tags": ["cheese", "Dutch", "Gouda", "farmhouse", "raw milk", "Boerenkaas"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dutch-aged-edam",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Aged Edam (Oude Edammer)",
        "category": "cheese",
        "attribution": "Traditional Dutch cheese",
        "source_note": "Traditional aged version of Dutch Edam, aged 10+ months.",
        "description": "While most Edam is sold young, aged Edam develops nutty, slightly sharp flavors and firmer texture. The signature red wax exterior (or natural rind for domestic) encases a pale interior that darkens slightly with age.",
        "servings_yield": "About 3-4 lbs ball",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "10-17 months aging",
        "ingredients": [
            {"item": "partially skimmed cow's milk (2%)", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "red cheese wax (for export style)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat partially skimmed milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40-45 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 30% whey. Add hot water to raise to 104°F (40°C)."},
            {"step": 5, "text": "Stir 30 minutes at temperature until curds are firm."},
            {"step": 6, "text": "Drain and press into ball mold at 20 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 7, "text": "Brine 18-24 hours in saturated solution."},
            {"step": 8, "text": "Air dry 2-3 days. Apply red wax for export style, or develop natural rind."},
            {"step": 9, "text": "Age at 55°F (13°C) for 10-17 months. Turn weekly first 2 months, biweekly thereafter."}
        ],
        "temperature": "90-104°F (32-40°C)",
        "notes": [
            "Edam traditionally made with partially skimmed milk for lower fat content",
            "Red wax indicates export cheese; black wax indicates aged Edam",
            "Ball shape allows even aging from all surfaces",
            "Less common than young Edam but prized by connoisseurs"
        ],
        "tags": ["cheese", "Dutch", "Edam", "aged", "ball-shaped", "lower-fat"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Dutch cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in DUTCH_CHEESE_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"Skipping existing: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"Added: {recipe['title']}")
            added += 1

    data['recipes'] = recipes

    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Added: {added} recipes")
    print(f"Skipped (existing): {skipped}")
    print(f"Total recipes now: {len(recipes)}")


if __name__ == '__main__':
    add_recipes()
