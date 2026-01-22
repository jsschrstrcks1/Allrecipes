#!/usr/bin/env python3
"""Add comprehensive Swiss cheese recipes to the cheese category."""

import json

SWISS_CHEESE_RECIPES = [
    # === CLASSIC SWISS AOP CHEESES ===
    {
        "id": "ch-emmentaler-aop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Emmentaler AOP (Real Swiss Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "The original 'Swiss cheese' from the Emme Valley in Bern canton. AOP protected since 2006.",
        "description": "The authentic Swiss cheese with iconic large eyes, made with raw milk from grass-fed cows. Nutty, buttery, and slightly sweet - this is the real deal, not the processed imitation.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "4-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk (grass-fed)", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Propionibacterium freudenreichii", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride (only if not raw)", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C). Add thermophilic starter and Propionibacterium, ripen 20 minutes."},
            {"step": 2, "text": "Raise temperature to 95°F (35°C). Add rennet diluted in water. Let set 30-40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into rice-sized pieces (1/8 inch) - tiny curds are essential for Emmentaler texture."},
            {"step": 4, "text": "Heat slowly to 130°F (54°C) over 45-60 minutes while stirring constantly. This high cook is critical."},
            {"step": 5, "text": "Hold at 130°F and stir until curds are very firm and squeak, about 45 minutes more."},
            {"step": 6, "text": "Transfer curds under whey to large mold. Press at 30 lbs for 1 hour, flip, then 50 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 48 hours, turning halfway."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-3 weeks, then move to warm room 68-72°F (20-22°C) for 4-8 weeks for eye development."},
            {"step": 9, "text": "Return to 55°F cave for minimum 4 months, up to 12 months for full flavor development."}
        ],
        "temperature": "90-130°F (32-54°C)",
        "notes": [
            "True Emmentaler AOP must be made in specific Swiss regions with raw milk",
            "Propionibacteria create CO2 during aging, forming the characteristic eyes",
            "Traditional wheels weigh 170-220 lbs - scale up for authenticity",
            "Eyes should be cherry-sized to walnut-sized, evenly distributed",
            "No eyes = 'blind' cheese, indicates fermentation problems"
        ],
        "tags": ["cheese", "Swiss", "AOP", "Alpine", "eye cheese", "raw milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-appenzeller-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Appenzeller (Herbed Brine Washed)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From the Appenzell region of northeastern Switzerland. Made for over 700 years with a secret herbal brine.",
        "description": "Switzerland's most aromatic cheese, washed with a secret herbal brine called 'Sulz' containing wine, spices, and 25+ herbs. Tangy, spicy, and complex with a distinctive orange rind.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "dry white wine", "quantity": "1", "unit": "cup"},
            {"item": "cider vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "dried thyme", "quantity": "1", "unit": "tbsp"},
            {"item": "dried savory", "quantity": "1", "unit": "tbsp"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp"},
            {"item": "juniper berries, crushed", "quantity": "1/2", "unit": "tsp"},
            {"item": "black pepper, cracked", "quantity": "1/2", "unit": "tsp"},
            {"item": "garlic powder", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare herbal brine: Combine wine, vinegar, and herbs. Simmer 10 minutes, strain, add 2 tbsp salt. Cool and refrigerate."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Heat slowly to 118°F (48°C) over 40 minutes while stirring."},
            {"step": 6, "text": "Hold at temperature and stir until curds shrink and firm, about 30 minutes."},
            {"step": 7, "text": "Drain and press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 8, "text": "Brine in standard salt solution for 12 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) and 90% humidity. Wash rind with herbal brine every 2-3 days for first month, then weekly."},
            {"step": 10, "text": "Age minimum 3 months (Classic), 4-6 months (Surchoix), or 6+ months (Extra)."}
        ],
        "temperature": "90-118°F (32-48°C)",
        "notes": [
            "The real Sulz recipe is a closely guarded secret with 25+ herbs",
            "This simplified version captures the spirit of the original",
            "Classic = mild, Surchoix = medium, Extra = strong",
            "The herbal brine gives Appenzeller its distinctive spicy kick",
            "Orange rind develops from the wine and herb wash"
        ],
        "tags": ["cheese", "Swiss", "washed-rind", "herbed", "Appenzell", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-raclette-valais",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Raclette du Valais (Traditional Melting Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From the Valais canton. Name comes from French 'racler' (to scrape). Medieval shepherds melted it by fire.",
        "description": "The ultimate melting cheese from the Swiss Alps. When heated, it becomes creamy and aromatic without separating. Traditionally scraped onto potatoes, pickles, and onions.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk (ideally raw)", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F (40°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Continue stirring at 105°F until curds are firm but still moist, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 25 lbs for 12 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity for 3-6 months."},
            {"step": 9, "text": "Wash rind with light brine weekly to develop characteristic tan color."}
        ],
        "temperature": "90-105°F (32-40°C)",
        "notes": [
            "Lower cook temperature than Gruyere preserves more moisture for melting",
            "Traditional raclette meal: melted cheese over boiled potatoes with cornichons and pickled onions",
            "Half-wheel is traditionally held near fire, melted portion scraped onto plate",
            "Modern raclette machines use small slices under heating element",
            "Best melting cheese - stays creamy without separating"
        ],
        "tags": ["cheese", "Swiss", "Valais", "melting", "raclette", "Alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-sbrinz-aop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sbrinz AOP (Extra-Hard Alpine Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Switzerland's oldest and hardest cheese, possibly predating Parmesan. Traded through Gotthard Pass for centuries.",
        "description": "Ancient Swiss grating cheese, harder than Parmesan. Intensely savory with crystalline texture. Traditionally broken into shards rather than cut, or shaved paper-thin with a Sbrinzhobel.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "18-36 months aging",
        "ingredients": [
            {"item": "raw cow's milk (grass-fed)", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride (only if not raw)", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C). Add starter, ripen 20 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add rennet. Let set 30 minutes until very firm break."},
            {"step": 3, "text": "Cut curds into tiny rice-sized pieces. Rest 5 minutes."},
            {"step": 4, "text": "Heat very slowly to 130°F (54°C) over 60 minutes while stirring constantly."},
            {"step": 5, "text": "Hold at 130°F and stir vigorously until curds are extremely firm, about 45 minutes."},
            {"step": 6, "text": "Drain and press immediately at 40 lbs for 1 hour, then 60 lbs for 24 hours."},
            {"step": 7, "text": "Brine for 3-4 weeks, turning daily. This extended brining is unique to Sbrinz."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for minimum 18 months, preferably 24-36 months."},
            {"step": 9, "text": "Rub with olive oil monthly during aging."}
        ],
        "temperature": "90-130°F (32-54°C)",
        "notes": [
            "Sbrinz may be the ancestor of Italian grana cheeses",
            "Traditional wheels weigh 55-100 lbs",
            "The extended brining (weeks vs hours) is unique to Sbrinz",
            "So hard it's traditionally broken apart, not cut",
            "Serve shaved thin or break into chunks for eating"
        ],
        "tags": ["cheese", "Swiss", "AOP", "extra-hard", "grating", "ancient", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-tete-de-moine-aop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tête de Moine AOP (Shaved Rosettes)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Monastery cheese from Bellelay Abbey since 12th century. Name means 'monk's head' - shaved from the top like a tonsure.",
        "description": "Unique Swiss cheese traditionally shaved into delicate rosettes using a Girolle. The shaving releases aromatic compounds, intensifying flavor. Fruity, nutty, and elegant.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 118°F (48°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Stir at temperature until curds are firm, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 7, "text": "Brine for 12-18 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90% humidity for minimum 75 days (3 months)."},
            {"step": 9, "text": "Wash rind with light brine every few days during first month."},
            {"step": 10, "text": "To serve: Use a Girolle to shave into thin rosettes, or slice very thin."}
        ],
        "temperature": "90-118°F (32-48°C)",
        "notes": [
            "Named 'monk's head' because it's shaved from top like a tonsure",
            "The Girolle tool was invented in 1982 to create the signature rosettes",
            "Shaving aerates the cheese, releasing intense aromas",
            "Keep cylinder shape during aging - flat sides, curved edges",
            "Must be from raw milk for AOP designation"
        ],
        "tags": ["cheese", "Swiss", "AOP", "monastery", "Girolle", "semi-hard"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-vacherin-mont-dor-seasonal",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vacherin Mont d'Or (Seasonal Spoon Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Seasonal cheese from Jura Mountains, made only August-March. So soft it's eaten with a spoon.",
        "description": "Switzerland's most decadent cheese, bound in spruce bark that imparts resinous notes. When ripe, the interior is completely liquid and eaten with a spoon. Bake whole and dip bread.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "3-4 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk (from mountain pastures)", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"},
            {"item": "spruce bark strips", "quantity": "2-3", "unit": "strips", "prep_note": "food-grade, soaked overnight"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak spruce bark in water overnight to make pliable."},
            {"step": 2, "text": "Heat milk to 86°F (30°C). Add starter and Geotrichum, ripen 30 minutes."},
            {"step": 3, "text": "Add very small amount of rennet. Let set 60-90 minutes for very soft curd."},
            {"step": 4, "text": "Cut curds very gently into 1-inch cubes. Rest 20 minutes."},
            {"step": 5, "text": "Ladle curds gently into molds. Do NOT press. Drain naturally at room temp 24-48 hours, flipping frequently."},
            {"step": 6, "text": "Salt surfaces lightly when cheese holds shape."},
            {"step": 7, "text": "Wrap cheese circumference snugly with spruce bark strip, securing with food-safe string."},
            {"step": 8, "text": "Place in wooden box slightly larger than cheese."},
            {"step": 9, "text": "Age at 55°F (13°C) and 95% humidity for 3-4 weeks until rind wrinkles and interior liquefies."},
            {"step": 10, "text": "To serve: Cut off top rind and spoon out the creamy interior, or bake at 350°F for 20 minutes and dip bread."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Made only late August to March when cows descend from summer pastures",
            "The spruce bark imparts resinous, piney notes essential to flavor",
            "When perfectly ripe, interior should be completely spoonable",
            "Traditional to bake whole and dip bread into molten center",
            "Must be consumed quickly once ripe - very perishable"
        ],
        "tags": ["cheese", "Swiss", "seasonal", "soft", "spruce-bark", "spoonable", "Jura"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-vacherin-fribourgeois-fondue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vacherin Fribourgeois AOP (Fondue Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From Fribourg canton. Essential component of fondue moitié-moitié (half-and-half with Gruyère).",
        "description": "Semi-soft washed-rind cheese from Fribourg, crucial for authentic Swiss fondue. Creamier and milder than Gruyère, it provides the silky texture in moitié-moitié fondue.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Gently stir at 95°F for 20 minutes."},
            {"step": 5, "text": "Slowly heat to 104°F (40°C) over 30 minutes while stirring."},
            {"step": 6, "text": "Drain and press lightly at 10 lbs for 30 min, flip, 15 lbs for 6 hours."},
            {"step": 7, "text": "Brine for 8-12 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity for 3-4 months."},
            {"step": 9, "text": "Wash rind with light brine 2-3 times weekly during aging."}
        ],
        "temperature": "90-104°F (32-40°C)",
        "notes": [
            "Essential for fondue moitié-moitié: half Vacherin Fribourgeois, half Gruyère",
            "Lower cook temperature creates creamier, more meltable texture than Gruyère",
            "Washed rind gives subtle earthy notes",
            "Six variants exist based on milk and aging: Classique, Extra, Rustic, etc.",
            "Often eaten young as table cheese as well"
        ],
        "tags": ["cheese", "Swiss", "AOP", "Fribourg", "fondue", "washed-rind", "melting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-schabziger-green",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Schabziger (Green Herb Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From canton Glarus, made since 15th century. Colored green with blue fenugreek (Zigerklee). Also called Sapsago.",
        "description": "Switzerland's most unusual cheese - a hard, cone-shaped grating cheese tinted green with blue fenugreek clover. Intensely pungent, used sparingly to flavor dishes. World's oldest branded cheese.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "buttermilk", "quantity": "1", "unit": "gallon"},
            {"item": "skim milk", "quantity": "1", "unit": "gallon"},
            {"item": "blue fenugreek (Zigerklee), dried", "quantity": "2", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine buttermilk and skim milk. Heat slowly to 190°F (88°C) - the high heat causes proteins to precipitate."},
            {"step": 2, "text": "Hold at temperature until curds form and whey separates clearly."},
            {"step": 3, "text": "Drain curds through fine cheesecloth. Press lightly to remove excess moisture."},
            {"step": 4, "text": "Grind dried blue fenugreek to fine powder."},
            {"step": 5, "text": "Mix drained curds with salt and fenugreek powder until evenly green."},
            {"step": 6, "text": "Pack very firmly into small cone-shaped molds or cylindrical molds."},
            {"step": 7, "text": "Press at 20 lbs for 24 hours."},
            {"step": 8, "text": "Unmold and dry at room temperature for 2 weeks."},
            {"step": 9, "text": "Age at 55°F (13°C) for 3-6 months until very hard."},
            {"step": 10, "text": "To use: Grate sparingly over potatoes, pasta, bread, or into soups."}
        ],
        "temperature": "190°F (88°C)",
        "notes": [
            "World's oldest trademarked cheese (since 1463)",
            "Blue fenugreek (Trigonella caerulea) is different from regular fenugreek",
            "Very pungent - use sparingly as a flavoring, not eating cheese",
            "Traditional cone shape is iconic - Stöckli molds still used today",
            "Nearly fat-free due to skim milk and buttermilk base"
        ],
        "tags": ["cheese", "Swiss", "herbed", "green", "grating", "Glarus", "fenugreek"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-letivaz-alpage-aop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "L'Etivaz AOP (Raw Milk Alpine)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Made only in summer on Alpine pastures (alpage) above 1000m. Cooked over wood fire in copper cauldrons.",
        "description": "Artisanal Alpine cheese made only during summer on high mountain pastures. Milk is heated over wood fire, giving subtle smoky notes. Gruyère's wild cousin - more intense and complex.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "5-24 months aging",
        "ingredients": [
            {"item": "raw cow's milk (mountain pasture)", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Ideally, heat milk over wood fire in copper cauldron for authentic smoky notes."},
            {"step": 2, "text": "Heat fresh raw milk to 90°F (32°C). Add starter, ripen 20 minutes."},
            {"step": 3, "text": "Raise to 95°F (35°C). Add rennet. Let set 35 minutes."},
            {"step": 4, "text": "Cut curds into small rice-sized pieces. Rest 5 minutes."},
            {"step": 5, "text": "Heat slowly to 130°F (54°C) over 45 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at temperature and stir until curds are very firm, about 40 minutes."},
            {"step": 7, "text": "Drain and press at 30 lbs for 1 hour, flip, 45 lbs for 24 hours."},
            {"step": 8, "text": "Brine for 36-48 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) for minimum 5 months, up to 24 months for complex flavor."},
            {"step": 10, "text": "Rub wheels regularly with brine during aging."}
        ],
        "temperature": "90-130°F (32-54°C)",
        "notes": [
            "Made only May-October on Alpine pastures above 1000m elevation",
            "Traditional copper cauldrons over wood fire give subtle smoky character",
            "Milk must be processed within hours of milking",
            "Only 70 alpine chalets are certified to produce L'Etivaz",
            "Gruyère's rustic ancestor - stronger and more variable"
        ],
        "tags": ["cheese", "Swiss", "AOP", "Alpine", "alpage", "raw milk", "artisanal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-tomme-vaudoise-soft",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tomme Vaudoise (Soft Washed-Rind)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From canton Vaud. Unique among Swiss cheeses as a small, soft, washed-rind tomme.",
        "description": "Small, soft, washed-rind cheese from Vaud canton. Unlike most Swiss cheeses, it's meant to be eaten young and creamy. Mild and buttery with delicate earthy rind notes.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet. Let set 60 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 15 minutes."},
            {"step": 4, "text": "Gently ladle curds into small molds (4-inch diameter). Do not press."},
            {"step": 5, "text": "Drain at room temperature 12-24 hours, flipping every 4 hours."},
            {"step": 6, "text": "Salt all surfaces lightly."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity for 2-4 weeks."},
            {"step": 8, "text": "Wash rind with light brine every 2-3 days."},
            {"step": 9, "text": "Ready when rind is slightly sticky and interior is soft and creamy."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Unusual for Switzerland - a soft, quick-ripening washed rind",
            "Small wheels, typically 7-10 oz each",
            "Best eaten within a few weeks of peak ripeness",
            "Mild compared to French washed-rind cheeses",
            "Often served as breakfast or dessert cheese in Vaud"
        ],
        "tags": ["cheese", "Swiss", "Vaud", "soft", "washed-rind", "tomme", "quick"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-berner-alpkaese-aop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Berner Alpkäse AOP (Bernese Alpine Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Made only on summer Alpine pastures in the Bernese Oberland. Hand-crafted by mountain farmers (Sennen).",
        "description": "Premium Alpine cheese made only during summer on Bernese mountain pastures. Rich, complex, and intensely flavored from cows grazing on wildflower meadows. Each wheel reflects its unique alp.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "6-18 months aging",
        "ingredients": [
            {"item": "raw cow's milk (alpine pasture)", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use freshest raw milk possible from mountain pasture cows."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add starter, ripen 25 minutes."},
            {"step": 3, "text": "Raise to 95°F (35°C). Add rennet. Let set 35 minutes."},
            {"step": 4, "text": "Cut curds into small 1/4-inch pieces. Rest 5 minutes."},
            {"step": 5, "text": "Heat slowly to 125°F (52°C) over 50 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at temperature and stir until curds are firm, about 40 minutes."},
            {"step": 7, "text": "Drain and press at 25 lbs for 1 hour, flip, 40 lbs for 24 hours."},
            {"step": 8, "text": "Brine for 24-36 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) for minimum 6 months, up to 18 months."},
            {"step": 10, "text": "Rub with brine weekly during first months, then monthly."}
        ],
        "temperature": "90-125°F (32-52°C)",
        "notes": [
            "Made only June-September on Alpine pastures above 1200m",
            "Each alp produces unique flavor based on its specific flora",
            "Bernese Oberland contains famous alps like Grindelwald and Lauterbrunnen",
            "The Sennen (alpine dairymen) are highly skilled artisans",
            "Hobelkäse variant is aged longer and shaved into curls"
        ],
        "tags": ["cheese", "Swiss", "AOP", "Bern", "Alpine", "alpage", "raw milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-gruyere-aop-cave",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gruyère AOP (Cave-Aged Swiss)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "From the town of Gruyères in Fribourg. Cave-aged for exceptional depth. Essential for fondue.",
        "description": "The king of Swiss cheeses, cave-aged for complex nutty, fruity flavor. Gruyère has been made since at least 1115 AD. Essential for fondue, French onion soup, and croque monsieur.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "6-18 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Propionibacterium (small amount)", "quantity": "1/32", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 90°F (32°C). Add starter and tiny amount of Propionibacterium, ripen 20 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add rennet. Let set 40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch pieces. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 130°F (54°C) over 50 minutes while stirring constantly."},
            {"step": 5, "text": "Hold at temperature and stir until curds are very firm, about 40 minutes."},
            {"step": 6, "text": "Drain and press at 30 lbs for 1 hour, flip, 50 lbs for 24 hours."},
            {"step": 7, "text": "Brine for 24-36 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity for 6-18 months."},
            {"step": 9, "text": "Wash rind with brine weekly during first 3 months, then monthly."}
        ],
        "temperature": "90-130°F (32-54°C)",
        "notes": [
            "Less Propionibacterium than Emmental = smaller, fewer eyes or none",
            "Gruyère classifications: Mild (5-6 mo), Reserve (10+ mo), Vieux (14+ mo)",
            "Cave aging develops complex nutty, fruity notes",
            "Essential for fondue moitié-moitié with Vacherin Fribourgeois",
            "First mentioned in writing in 1115 AD"
        ],
        "tags": ["cheese", "Swiss", "AOP", "Gruyère", "cave-aged", "fondue", "Alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-tilsiter-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Swiss Tilsiter (Royalp)",
        "category": "cheese",
        "attribution": "Traditional Swiss cheese",
        "source_note": "Swiss version of Prussian Tilsit cheese. Made in Switzerland since 19th century. Known locally as Tilsiter or Royalp.",
        "description": "Semi-hard washed-rind cheese with small irregular eyes. Mild to tangy depending on age. Popular everyday cheese in German-speaking Switzerland.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-5 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 20% of whey. Add warm water to bring temp to 100°F (38°C)."},
            {"step": 5, "text": "Stir at temperature for 30 minutes."},
            {"step": 6, "text": "Drain and press at 10 lbs for 30 min, flip, 20 lbs for 8 hours."},
            {"step": 7, "text": "Brine for 8-12 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90% humidity for 2-5 months."},
            {"step": 9, "text": "Wash rind with light brine weekly."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Swiss Tilsiter is milder than German/Baltic versions",
            "Green label = mild, Red label = aged/strong (in Switzerland)",
            "Washed-curd technique gives sweeter, milder flavor",
            "Small irregular eyes form from natural gas production",
            "Popular sandwich and snacking cheese in Switzerland"
        ],
        "tags": ["cheese", "Swiss", "Tilsiter", "washed-rind", "washed-curd", "semi-hard"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ch-fondue-blend",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Swiss Fondue Cheese Blend (Moitié-Moitié)",
        "category": "cheese",
        "attribution": "Traditional Swiss preparation",
        "source_note": "The classic Swiss fondue uses equal parts Gruyère and Vacherin Fribourgeois.",
        "description": "Not a single cheese but the traditional Swiss fondue preparation. Gruyère provides nutty depth while Vacherin Fribourgeois gives creamy meltability. The definitive Alpine comfort food.",
        "servings_yield": "4-6 servings",
        "prep_time": "15 min",
        "cook_time": "20 min",
        "total_time": "35 min",
        "ingredients": [
            {"item": "Gruyère AOP, grated", "quantity": "8", "unit": "oz"},
            {"item": "Vacherin Fribourgeois, grated", "quantity": "8", "unit": "oz"},
            {"item": "dry white wine (Fendant or similar)", "quantity": "1", "unit": "cup"},
            {"item": "garlic clove", "quantity": "1", "unit": "clove"},
            {"item": "cornstarch", "quantity": "1", "unit": "tbsp"},
            {"item": "kirsch (cherry brandy)", "quantity": "2", "unit": "tbsp"},
            {"item": "nutmeg, freshly grated", "quantity": "1/8", "unit": "tsp"},
            {"item": "white pepper", "quantity": "to taste", "unit": ""},
            {"item": "crusty bread cubes", "quantity": "1", "unit": "loaf", "prep_note": "for dipping"}
        ],
        "instructions": [
            {"step": 1, "text": "Toss grated cheeses with cornstarch to coat evenly."},
            {"step": 2, "text": "Rub inside of fondue pot (caquelon) with cut garlic clove."},
            {"step": 3, "text": "Add wine to pot and heat over medium until simmering."},
            {"step": 4, "text": "Reduce heat to low. Add cheese handful at a time, stirring in figure-8 pattern after each addition."},
            {"step": 5, "text": "Wait until each addition melts before adding more. Stir constantly."},
            {"step": 6, "text": "When all cheese is melted and smooth, stir in kirsch, nutmeg, and pepper."},
            {"step": 7, "text": "Transfer to fondue stand over low flame to keep warm."},
            {"step": 8, "text": "Serve immediately with bread cubes, boiled potatoes, and pickles."}
        ],
        "temperature": "Low simmer",
        "notes": [
            "Moitié-moitié means 'half-and-half' - equal parts of each cheese",
            "Figure-8 stirring prevents separation",
            "Never let fondue boil or it will become stringy",
            "Traditional to drink white wine or kirsch with fondue (not water!)",
            "The crust at the bottom (la religieuse) is a prized treat"
        ],
        "tags": ["cheese", "Swiss", "fondue", "Gruyère", "Vacherin", "Alpine", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Swiss cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in SWISS_CHEESE_RECIPES:
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
