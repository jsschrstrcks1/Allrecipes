#!/usr/bin/env python3
"""Add new Argentine and adulterated cheese recipes."""

import json

NEW_RECIPES = [
    # === ARGENTINE CHEESES (missing varieties) ===
    {
        "id": "queso-pategras",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Pategras (Argentine Dutch-Style)",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine adaptation of Dutch Gouda/Edam, popular since European immigration waves.",
        "description": "Argentina's most popular table cheese, a semi-hard Dutch-style cheese with mild, slightly nutty flavor. Excellent for sandwiches and melting.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set for 45-60 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly raise temperature to 102°F (39°C) over 30 minutes while stirring gently. This is the washed-curd method."},
            {"step": 5, "text": "Remove 1/3 of whey, replace with same temperature water. Continue stirring 20 minutes."},
            {"step": 6, "text": "Drain curds and press at 10 lbs for 30 min, flip, then 20 lbs for 2 hours."},
            {"step": 7, "text": "Brine in saturated salt solution for 8 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 2-3 months, flipping weekly."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Pategras is derived from 'pata de gras' (duck leg) referring to its shape",
            "Washed-curd technique gives milder flavor than traditional Gouda",
            "Most consumed cheese in Argentina after Cremoso"
        ],
        "tags": ["cheese", "Argentine", "Dutch-style", "semi-hard", "table cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-mar-del-plata",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Mar del Plata",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Soft cheese originating from Mar del Plata coastal region, similar to Port Salut.",
        "description": "Soft, mild Argentine cheese from the coastal city of Mar del Plata. Creamy texture with a washed rind and buttery flavor, perfect for spreading.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "3-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens (washed rind culture)", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "brine wash (light salt solution)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens cultures, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 20 minutes at 90°F, keeping curds soft."},
            {"step": 5, "text": "Drain and mold without pressing. Let drain naturally 12-24 hours, flipping every 4 hours."},
            {"step": 6, "text": "Salt surfaces lightly or brief brine (2-3 hours)."},
            {"step": 7, "text": "Age at 55°F (13°C) and 90%+ humidity. Wash rind with light brine every 2-3 days."},
            {"step": 8, "text": "Ready in 3-4 weeks when rind develops orange-pink color."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Named after Argentina's famous beach resort city",
            "Washed rind gives characteristic aroma without strong flavor",
            "Best served at room temperature for full creaminess"
        ],
        "tags": ["cheese", "Argentine", "soft", "washed-rind", "coastal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-holanda-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Holanda Argentino (Argentine Holland Cheese)",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of Dutch Edam, rounder and milder than Magnasco.",
        "description": "Argentina's ball-shaped Dutch-style cheese, milder and younger than Magnasco Edam. Covered in distinctive red wax, popular for everyday eating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "part-skim cow's milk (2%)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "red cheese wax", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat part-skim milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes. Cut into 1/2-inch curds."},
            {"step": 3, "text": "Rest 5 minutes, then slowly heat to 100°F (38°C) over 30 minutes."},
            {"step": 4, "text": "Remove 1/3 whey, replace with same-temp water. Stir 15 minutes."},
            {"step": 5, "text": "Drain and press lightly (5 lbs) into round mold for 1 hour."},
            {"step": 6, "text": "Flip, press at 10 lbs for 6 hours."},
            {"step": 7, "text": "Brine 6 hours per pound in saturated solution."},
            {"step": 8, "text": "Air dry 2-3 days, then wax with red cheese wax. Age 6-8 weeks at 55°F."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Part-skim milk creates the characteristic lower-fat Edam texture",
            "Red wax is traditional for export and preservation",
            "Younger than Magnasco, more suitable for everyday table use"
        ],
        "tags": ["cheese", "Argentine", "Dutch-style", "Edam", "semi-hard"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-cuartirolo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Cuartirolo Argentino",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine fresh cheese inspired by Italian Quartirolo Lombardo.",
        "description": "Soft, fresh Argentine cheese with slight tang and creamy texture. Made from cow's milk, it's perfect for salads, sandwiches, and cooking.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-2 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Let set 40 minutes until soft curd forms."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently ladle curds into rectangular molds without pressing."},
            {"step": 5, "text": "Let drain at room temperature 12-24 hours, flipping every 4-6 hours."},
            {"step": 6, "text": "Salt both surfaces liberally."},
            {"step": 7, "text": "Refrigerate and age 1-2 weeks for developed flavor, or eat fresh."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Name derives from Italian 'quarta' (fourth) - made from fourth milking",
            "Traditionally rectangular in shape",
            "Can be eaten fresh (2-3 days) or aged (1-2 weeks) for stronger flavor"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "fresh", "soft"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-barra-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Barra Argentino (Bar Cheese)",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine industrial-style mild cheese, named for its bar shape.",
        "description": "Mild, semi-soft Argentine cheese shaped into rectangular bars. Excellent melting cheese, commonly used for sandwiches and pizza in Argentina.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2.5 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 100°F (38°C) over 30 minutes, stirring gently."},
            {"step": 5, "text": "Drain whey and press curds into rectangular 'bar' mold at 10 lbs for 1 hour."},
            {"step": 6, "text": "Flip and press at 20 lbs for 4-6 hours."},
            {"step": 7, "text": "Brine 4 hours per pound or dry salt surfaces."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for 2-4 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Industrial cheese commonly found in Argentine supermarkets",
            "Excellent melting properties make it ideal for pizza and sandwiches",
            "Similar to American Monterey Jack in texture and meltability"
        ],
        "tags": ["cheese", "Argentine", "semi-soft", "melting cheese", "bar shape"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-gruyeron-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Gruyerón Argentino",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine interpretation of Swiss Gruyère, adapted by European immigrants.",
        "description": "Argentina's Swiss-style hard cheese with nutty, slightly sweet flavor. Features small eyes and firm texture, excellent for fondue and gratins.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "4-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii (eye-forming)", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and P. shermanii, ripen 15 minutes."},
            {"step": 2, "text": "Heat to 95°F (35°C). Add rennet, let set 45 minutes."},
            {"step": 3, "text": "Cut curds very fine (rice-sized). Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 120°F (49°C) over 45 minutes, stirring constantly."},
            {"step": 5, "text": "Hold at 120°F for 30 minutes until curds are firm and squeaky."},
            {"step": 6, "text": "Drain and press at 15 lbs for 1 hour, flip, 25 lbs for 12 hours."},
            {"step": 7, "text": "Brine 12 hours per pound in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2 months, then move to 65°F (18°C) for eye development."},
            {"step": 9, "text": "Return to 55°F for final aging. Total 4-6 months."}
        ],
        "temperature": "90-120°F (32-49°C)",
        "notes": [
            "Eye development requires warm room period at 65°F",
            "Smaller wheels than Swiss Gruyère, adapted to home production",
            "Excellent fondue cheese when mixed with Pategras"
        ],
        "tags": ["cheese", "Argentine", "Swiss-style", "hard", "alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-de-campo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso de Campo Argentino (Farmhouse Cheese)",
        "category": "sides",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Rustic Argentine farmhouse cheese from the Pampas region.",
        "description": "Traditional farmhouse cheese from Argentine estancias. Semi-soft with natural rind, made using simple countryside methods passed down through generations.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "raw cow's milk (or pasteurized)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "coarse salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 1 hour for developed flavor."},
            {"step": 2, "text": "Add rennet, let set 45-60 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 20 minutes, keeping temperature steady."},
            {"step": 5, "text": "Drain and transfer to cloth-lined mold. Press lightly (5 lbs) for 2 hours."},
            {"step": 6, "text": "Flip and press at 10 lbs overnight."},
            {"step": 7, "text": "Rub surfaces with coarse salt. Air dry 2-3 days."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for 2-4 weeks, turning daily."}
        ],
        "temperature": "88°F (31°C)",
        "notes": [
            "Traditional estancia cheese made with raw morning milk",
            "Natural rind develops during aging",
            "Pairs perfectly with dulce de membrillo (quince paste)"
        ],
        "tags": ["cheese", "Argentine", "farmhouse", "rustic", "Pampas"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # === ADULTERATED/FLAVORED CHEESES (missing varieties) ===
    {
        "id": "espresso-rubbed-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Espresso Rubbed Cheddar",
        "category": "sides",
        "attribution": "Modern artisan cheese",
        "source_note": "Contemporary American artisan cheese combining coffee and aged cheddar.",
        "description": "Sharp cheddar coated with finely ground espresso, creating an earthy, complex flavor profile. The coffee enhances the cheddar's sharpness with subtle bitter notes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "Standard cheddar prep + rub",
        "cook_time": "Standard cheddar make time",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "finely ground espresso beans", "quantity": "1/2", "unit": "cup"},
            {"item": "cocoa powder (optional)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cheddar: heat milk to 90°F, add starter, ripen, add rennet."},
            {"step": 2, "text": "Cut curds, cook to 102°F, drain whey. Cheddar the curds (stack and turn)."},
            {"step": 3, "text": "Mill curds, salt, press at high weight for 24 hours."},
            {"step": 4, "text": "Air dry 2-3 days until surface is dry to touch."},
            {"step": 5, "text": "Mix espresso with optional cocoa powder. Coat entire surface, pressing gently."},
            {"step": 6, "text": "Age at 55°F (13°C) for 3-6 months. The coffee rub forms a protective coat."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Use high-quality single-origin espresso for best flavor",
            "Coffee rub creates natural protective coating - no wax needed",
            "Pairs excellently with dark chocolate and red wine"
        ],
        "tags": ["cheese", "cheddar", "coffee", "espresso", "flavored", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bourbon-washed-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bourbon Washed Cheddar",
        "category": "sides",
        "attribution": "American artisan cheese",
        "source_note": "Kentucky-inspired artisan cheddar washed with bourbon during aging.",
        "description": "Sharp cheddar aged with bourbon washes, developing complex caramel, vanilla, and oak notes from the whiskey. A true American original.",
        "servings_yield": "About 2 lbs",
        "prep_time": "Standard cheddar prep",
        "cook_time": "Standard cheddar make time",
        "total_time": "4-8 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "bourbon whiskey", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cheddar through pressing stage."},
            {"step": 2, "text": "Air dry cheese 3-5 days until rind forms."},
            {"step": 3, "text": "Begin bourbon washes: brush or spray entire surface with bourbon weekly."},
            {"step": 4, "text": "Age at 55°F (13°C) and 85% humidity."},
            {"step": 5, "text": "Continue bourbon washes for first 2 months, then age unwashed."},
            {"step": 6, "text": "Total aging 4-8 months for full bourbon integration."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Use quality bourbon - the cheese absorbs its flavor profile",
            "Alcohol evaporates, leaving caramel and oak notes",
            "Excellent paired with Kentucky ham or dried fruits"
        ],
        "tags": ["cheese", "cheddar", "bourbon", "whiskey", "American", "washed"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "whiskey-washed-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Whiskey Washed Gouda",
        "category": "sides",
        "attribution": "Artisan cheese",
        "source_note": "Dutch-style Gouda enhanced with whiskey washing during aging.",
        "description": "Creamy Gouda with smoky, caramel notes from whiskey washes. The spirit's complexity complements Gouda's natural sweetness.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "single malt or rye whiskey", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard Gouda: heat milk to 90°F, add starter, ripen."},
            {"step": 2, "text": "Add rennet, cut curds, wash curds with warm water."},
            {"step": 3, "text": "Drain, press, and brine as for standard Gouda."},
            {"step": 4, "text": "After brining, air dry 3 days."},
            {"step": 5, "text": "Wash with whiskey every 3-4 days for first 6 weeks."},
            {"step": 6, "text": "Age at 55°F for 3-6 months total."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Rye whiskey adds spice, single malt adds smokiness",
            "Natural rind develops orange-brown color from washing",
            "Allow to breathe 30 minutes before serving for best flavor"
        ],
        "tags": ["cheese", "Gouda", "whiskey", "washed", "Dutch-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "habanero-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Habanero Cheddar",
        "category": "sides",
        "attribution": "Artisan spicy cheese",
        "source_note": "Sharp cheddar with the fruity heat of habanero peppers.",
        "description": "Sharp cheddar studded with diced habanero peppers, delivering intense fruity heat. For serious heat lovers who want flavor with their fire.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "fresh habanero peppers, finely diced (seeds removed for less heat)", "quantity": "2-4", "unit": "peppers"},
            {"item": "dried habanero flakes (optional, for extra heat)", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Wear gloves when handling habaneros. Dice finely, removing seeds for moderate heat."},
            {"step": 2, "text": "Make standard cheddar through cheddaring stage."},
            {"step": 3, "text": "After milling curds, mix in diced habaneros and salt thoroughly."},
            {"step": 4, "text": "Press at high weight for 24 hours."},
            {"step": 5, "text": "Air dry and wax, or bandage wrap."},
            {"step": 6, "text": "Age at 55°F for 3-6 months. Heat mellows slightly with age."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Habaneros are 100,000-350,000 Scoville units - use caution",
            "Fruity habanero flavor complements sharp cheddar beautifully",
            "Heat intensifies when cheese is melted"
        ],
        "tags": ["cheese", "cheddar", "habanero", "spicy", "hot pepper"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ghost-pepper-jack",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ghost Pepper Jack",
        "category": "sides",
        "attribution": "Extreme heat artisan cheese",
        "source_note": "Monterey Jack with bhut jolokia (ghost pepper) for extreme heat seekers.",
        "description": "Creamy Monterey Jack with ghost pepper pieces for those who seek extreme heat. One of the hottest cheese varieties possible - handle with care.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "dried ghost pepper flakes", "quantity": "1-2", "unit": "tsp"},
            {"item": "fresh ghost pepper, finely minced (optional)", "quantity": "1/2", "unit": "pepper"}
        ],
        "instructions": [
            {"step": 1, "text": "WARNING: Ghost peppers are 1,000,000+ Scoville units. Wear gloves and eye protection."},
            {"step": 2, "text": "Rehydrate dried ghost pepper flakes in warm water if using."},
            {"step": 3, "text": "Make standard Monterey Jack: 90°F milk, add starter, ripen, add rennet."},
            {"step": 4, "text": "Cut curds, cook to 100°F, drain."},
            {"step": 5, "text": "Mix ghost pepper into curds with salt. Use less for milder heat."},
            {"step": 6, "text": "Press at 10 lbs for 1 hour, flip, 20 lbs for 6-12 hours."},
            {"step": 7, "text": "Age at 50-55°F for 4-8 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Ghost pepper (bhut jolokia) is one of world's hottest peppers",
            "Start with less pepper - you can always add more next batch",
            "Not recommended for those sensitive to capsaicin"
        ],
        "tags": ["cheese", "Jack", "ghost pepper", "extreme heat", "bhut jolokia"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "carolina-reaper-jack",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Carolina Reaper Jack",
        "category": "sides",
        "attribution": "Extreme heat artisan cheese",
        "source_note": "Monterey Jack with the world's hottest pepper - Carolina Reaper.",
        "description": "For the ultimate heat seekers: Monterey Jack with Carolina Reaper, the world's hottest pepper. Fruity sweetness precedes volcanic heat.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "dried Carolina Reaper flakes", "quantity": "1/2-1", "unit": "tsp"},
            {"item": "Carolina Reaper powder (optional boost)", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "EXTREME CAUTION: Carolina Reaper exceeds 2,000,000 Scoville units. Full protective gear required."},
            {"step": 2, "text": "Make standard Monterey Jack base."},
            {"step": 3, "text": "After draining, carefully mix Reaper flakes into curds with salt."},
            {"step": 4, "text": "Press and age as standard Jack cheese."},
            {"step": 5, "text": "Age 4-8 weeks. Heat does not diminish with aging."},
            {"step": 6, "text": "Label clearly to warn others of extreme heat level."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Carolina Reaper held Guinness World Record for hottest pepper",
            "Characteristic fruity-sweet flavor before the extreme heat hits",
            "A tiny amount provides massive heat - start with less"
        ],
        "tags": ["cheese", "Jack", "Carolina Reaper", "extreme heat", "world's hottest"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "scotch-bonnet-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Scotch Bonnet Cheddar",
        "category": "sides",
        "attribution": "Caribbean-inspired artisan cheese",
        "source_note": "Sharp cheddar with Caribbean scotch bonnet peppers.",
        "description": "Sharp cheddar with scotch bonnet peppers bringing Caribbean heat and distinctive fruity, slightly sweet flavor. Pairs wonderfully with tropical dishes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "scotch bonnet peppers, finely diced", "quantity": "2-3", "unit": "peppers"}
        ],
        "instructions": [
            {"step": 1, "text": "Wear gloves when handling scotch bonnets. Remove seeds for less heat."},
            {"step": 2, "text": "Make standard cheddar through cheddaring stage."},
            {"step": 3, "text": "After milling, mix in diced scotch bonnets with salt."},
            {"step": 4, "text": "Press at high weight for 24 hours."},
            {"step": 5, "text": "Wax or bandage wrap."},
            {"step": 6, "text": "Age at 55°F for 3-6 months."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Scotch bonnets are similar heat to habaneros but sweeter flavor",
            "Essential pepper in Caribbean cuisine",
            "Excellent melted on jerk chicken or tropical burgers"
        ],
        "tags": ["cheese", "cheddar", "scotch bonnet", "Caribbean", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ancho-chile-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ancho Chile Gouda",
        "category": "sides",
        "attribution": "Mexican-inspired artisan cheese",
        "source_note": "Dutch Gouda with dried ancho chiles for mild heat and complex flavor.",
        "description": "Creamy Gouda infused with dried ancho chiles, providing mild heat with rich, fruity, slightly sweet and smoky notes. Mexican-Dutch fusion at its best.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "dried ancho chiles, rehydrated and diced", "quantity": "2", "unit": "chiles"},
            {"item": "ancho chile powder", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Rehydrate ancho chiles in warm water 20 minutes. Dice finely."},
            {"step": 2, "text": "Make standard Gouda with washed-curd method."},
            {"step": 3, "text": "After draining, mix diced anchos and powder into curds with salt."},
            {"step": 4, "text": "Press and brine as standard Gouda."},
            {"step": 5, "text": "Age at 55°F for 2-4 months."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Ancho chiles are dried poblanos - mild heat (1,000-2,000 Scoville)",
            "Sweet, fruity, slightly smoky flavor complements Gouda's creaminess",
            "Excellent for quesadillas and Mexican dishes"
        ],
        "tags": ["cheese", "Gouda", "ancho chile", "Mexican", "mild heat"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "poblano-pepper-jack",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Poblano Pepper Jack",
        "category": "sides",
        "attribution": "Mexican-American artisan cheese",
        "source_note": "Monterey Jack with roasted poblano peppers.",
        "description": "Creamy Monterey Jack studded with roasted poblano peppers. Mild heat with rich, earthy pepper flavor - perfect for those who prefer flavor over fire.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour (including roasting)",
        "cook_time": "2.5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "fresh poblano peppers", "quantity": "2", "unit": "large"},
            {"item": "roasted green chiles (canned, optional addition)", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Roast poblanos under broiler until charred. Steam in bag 10 minutes, peel, seed, dice."},
            {"step": 2, "text": "Make standard Monterey Jack base."},
            {"step": 3, "text": "After draining, mix roasted poblanos into curds with salt."},
            {"step": 4, "text": "Press at 10 lbs for 1 hour, flip, 20 lbs for 6-12 hours."},
            {"step": 5, "text": "Age at 50-55°F for 4-8 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Poblanos are very mild (1,000-2,000 Scoville) - occasionally hot",
            "Roasting develops complex, earthy flavor",
            "Essential for authentic chile rellenos"
        ],
        "tags": ["cheese", "Jack", "poblano", "Mexican", "roasted pepper"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "serrano-pepper-monterey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Serrano Pepper Monterey Jack",
        "category": "sides",
        "attribution": "Mexican-American artisan cheese",
        "source_note": "Monterey Jack with fresh serrano peppers for bright, clean heat.",
        "description": "Monterey Jack with fresh serrano peppers providing bright, clean heat with crisp pepper flavor. More heat than jalapeño, less than habanero.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "fresh serrano peppers, thinly sliced", "quantity": "4-6", "unit": "peppers"}
        ],
        "instructions": [
            {"step": 1, "text": "Slice serranos into thin rounds. Remove seeds for less heat."},
            {"step": 2, "text": "Make standard Monterey Jack base."},
            {"step": 3, "text": "Mix serrano slices into drained curds with salt."},
            {"step": 4, "text": "Press and age as standard Jack."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Serranos are 10,000-25,000 Scoville units - hotter than jalapeños",
            "Bright, clean heat without the sweetness of habanero",
            "Popular in authentic Mexican cooking"
        ],
        "tags": ["cheese", "Jack", "serrano", "Mexican", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "maple-smoked-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple Smoked Cheddar",
        "category": "sides",
        "attribution": "New England artisan cheese",
        "source_note": "Sharp cheddar cold-smoked with maple wood for sweet, smoky flavor.",
        "description": "Sharp Vermont-style cheddar cold-smoked with maple wood chips. The maple smoke adds subtle sweetness and depth, perfect with apples and cured meats.",
        "servings_yield": "About 2 lbs",
        "prep_time": "Standard cheddar prep",
        "cook_time": "Standard cheddar + 4-8 hours smoking",
        "total_time": "3-6 months aging (after smoking)",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "maple wood chips for smoking", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard sharp cheddar and age at least 3 months before smoking."},
            {"step": 2, "text": "Set up cold smoker - temperature must stay below 90°F (32°C) to prevent melting."},
            {"step": 3, "text": "Soak maple chips 30 minutes, drain."},
            {"step": 4, "text": "Cold smoke cheese 4-8 hours, depending on desired intensity."},
            {"step": 5, "text": "Rest cheese unwrapped in refrigerator 1-2 weeks for smoke to mellow and penetrate."},
            {"step": 6, "text": "Vacuum seal or wax for storage."}
        ],
        "temperature": "Cold smoke: below 90°F (32°C)",
        "notes": [
            "Maple smoke is sweeter and milder than hickory",
            "New England tradition - pairs with local apples and maple syrup",
            "Must use cold smoking to prevent cheese from melting"
        ],
        "tags": ["cheese", "cheddar", "maple", "smoked", "New England", "Vermont"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chocolate-goat-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chocolate Goat Cheese",
        "category": "sides",
        "attribution": "Dessert artisan cheese",
        "source_note": "Fresh goat cheese blended with dark chocolate - a dessert cheese.",
        "description": "Creamy fresh goat cheese blended with dark chocolate for a unique dessert cheese. The tang of chèvre balances the chocolate's sweetness beautifully.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days (fresh cheese)",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "dark chocolate (70%+), finely chopped", "quantity": "4", "unit": "oz"},
            {"item": "honey or maple syrup (optional)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make fresh chèvre: heat goat milk to 72°F, add starter and rennet, let set 12-24 hours."},
            {"step": 2, "text": "Drain curds in cheesecloth 12-24 hours until thick and spreadable."},
            {"step": 3, "text": "Melt chocolate gently in double boiler, cool slightly."},
            {"step": 4, "text": "Blend chocolate into goat cheese along with salt and optional honey."},
            {"step": 5, "text": "Form into log or press into mold. Refrigerate."},
            {"step": 6, "text": "Best consumed within 2 weeks."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Use high-quality dark chocolate for best results",
            "Goat cheese tang balances chocolate sweetness",
            "Serve with fresh berries, graham crackers, or crusty bread"
        ],
        "tags": ["cheese", "goat", "chocolate", "dessert", "sweet"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "zaatar-labneh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Za'atar Labneh",
        "category": "sides",
        "attribution": "Middle Eastern traditional cheese",
        "source_note": "Lebanese strained yogurt cheese with za'atar spice blend.",
        "description": "Thick, creamy labneh rolled in za'atar - the classic Middle Eastern combination. Tangy cheese meets earthy thyme, sesame, and sumac.",
        "servings_yield": "About 1 lb",
        "prep_time": "10 min",
        "cook_time": "None",
        "total_time": "24-48 hours straining",
        "ingredients": [
            {"item": "whole milk plain yogurt (full fat)", "quantity": "32", "unit": "oz"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "za'atar spice blend", "quantity": "3", "unit": "tbsp"},
            {"item": "extra virgin olive oil", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt into yogurt thoroughly."},
            {"step": 2, "text": "Line a fine-mesh strainer with cheesecloth. Place over bowl."},
            {"step": 3, "text": "Add yogurt, gather cloth edges, and tie. Refrigerate 24-48 hours."},
            {"step": 4, "text": "The longer you strain, the thicker the labneh."},
            {"step": 5, "text": "Transfer thick labneh to serving plate. Spread za'atar over surface."},
            {"step": 6, "text": "Drizzle with olive oil. Serve with warm pita bread."}
        ],
        "temperature": "Refrigerator temperature",
        "notes": [
            "Za'atar typically contains thyme, sesame, sumac, and salt",
            "Can form into balls and preserve in olive oil",
            "Traditional Lebanese breakfast staple"
        ],
        "tags": ["cheese", "labneh", "za'atar", "Middle Eastern", "Lebanese", "yogurt"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "harissa-goat-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Harissa Goat Cheese",
        "category": "sides",
        "attribution": "North African-inspired artisan cheese",
        "source_note": "Fresh goat cheese with North African harissa chile paste.",
        "description": "Creamy fresh goat cheese swirled with spicy, smoky harissa paste. The tangy cheese tempers the harissa's heat while showcasing its complex spices.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "harissa paste", "quantity": "2-3", "unit": "tbsp"},
            {"item": "olive oil", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make fresh chèvre as standard."},
            {"step": 2, "text": "Drain until thick and spreadable, about 24 hours."},
            {"step": 3, "text": "Mix harissa with olive oil to loosen slightly."},
            {"step": 4, "text": "Fold harissa through goat cheese - don't fully mix for marbled effect."},
            {"step": 5, "text": "Add salt to taste. Form into log or serve in bowl."},
            {"step": 6, "text": "Best within 2 weeks refrigerated."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Harissa heat varies - taste before mixing and adjust amount",
            "Contains caraway, coriander, cumin in addition to chiles",
            "Excellent with grilled lamb or roasted vegetables"
        ],
        "tags": ["cheese", "goat", "harissa", "North African", "spicy", "Tunisian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "berbere-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Berbere Spiced Gouda",
        "category": "sides",
        "attribution": "Ethiopian-Dutch fusion artisan cheese",
        "source_note": "Dutch Gouda with Ethiopian berbere spice blend.",
        "description": "Creamy Gouda infused with Ethiopian berbere spice blend - warm, complex, and mildly spicy with notes of cardamom, fenugreek, and chiles.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "berbere spice blend", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard Gouda base with washed-curd method."},
            {"step": 2, "text": "After draining, mix berbere spice into curds with salt."},
            {"step": 3, "text": "Press as standard Gouda."},
            {"step": 4, "text": "Brine 8 hours per pound."},
            {"step": 5, "text": "Age at 55°F for 2-4 months. Spice mellows with age."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Berbere contains chiles, fenugreek, cardamom, coriander, and more",
            "Ethiopian spice blend - warm and complex rather than just hot",
            "Excellent with injera or crusty bread"
        ],
        "tags": ["cheese", "Gouda", "berbere", "Ethiopian", "spiced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "gochujang-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gochujang Cheddar",
        "category": "sides",
        "attribution": "Korean-American fusion artisan cheese",
        "source_note": "Sharp cheddar with Korean fermented chile paste.",
        "description": "Sharp cheddar infused with gochujang, Korean fermented chile paste. Sweet, spicy, and deeply savory - umami meets Wisconsin tradition.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "gochujang paste", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cheddar through cheddaring stage."},
            {"step": 2, "text": "After milling, work gochujang into curds with salt - it will color curds red."},
            {"step": 3, "text": "Press at high weight for 24 hours."},
            {"step": 4, "text": "Wax or bandage wrap - gochujang's sugars may cause sticking without coating."},
            {"step": 5, "text": "Age at 55°F for 3-6 months."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Gochujang is fermented - adds umami depth beyond just heat",
            "Sweet and spicy combination is signature Korean flavor",
            "Excellent melted on Korean BBQ or burgers"
        ],
        "tags": ["cheese", "cheddar", "gochujang", "Korean", "fermented", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wasabi-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wasabi Cream Cheese",
        "category": "sides",
        "attribution": "Japanese-American fusion cheese",
        "source_note": "Cream cheese with Japanese wasabi for sinus-clearing heat.",
        "description": "Rich cream cheese with wasabi's distinctive nasal heat. Unique pungency that clears the sinuses - perfect on bagels with smoked salmon.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "wasabi paste (real or prepared)", "quantity": "1-2", "unit": "tbsp"},
            {"item": "wasabi powder (for extra heat)", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat cream and milk to 75°F (24°C). Add starter, ripen 1 hour."},
            {"step": 2, "text": "Add rennet, stir gently. Let set at room temp 12-24 hours."},
            {"step": 3, "text": "Ladle curds into cheesecloth-lined strainer. Drain 12-24 hours."},
            {"step": 4, "text": "Beat drained cheese until smooth. Mix in salt and wasabi to taste."},
            {"step": 5, "text": "Adjust wasabi - it fades slightly over time."},
            {"step": 6, "text": "Refrigerate. Best within 2 weeks."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Real wasabi is expensive and subtle; prepared wasabi (horseradish-based) is hotter",
            "Wasabi heat dissipates faster than chile heat",
            "Classic pairing with smoked salmon on bagels"
        ],
        "tags": ["cheese", "cream cheese", "wasabi", "Japanese", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "miso-aged-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Miso Aged Gouda",
        "category": "sides",
        "attribution": "Japanese-Dutch fusion artisan cheese",
        "source_note": "Dutch Gouda with white miso paste for deep umami.",
        "description": "Aged Gouda enhanced with white miso paste, creating unprecedented umami depth. The fermented soybean paste amplifies Gouda's natural caramel notes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "4-8 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "white (shiro) miso paste", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard Gouda through draining stage."},
            {"step": 2, "text": "Mix miso paste into curds - it will add salt so reduce cheese salt."},
            {"step": 3, "text": "Press and brief brine (reduce time due to miso salt)."},
            {"step": 4, "text": "Age at 55°F for 4-8 months for deep flavor development."},
            {"step": 5, "text": "Miso's enzymes create unique aged character."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "White miso is milder and sweeter than red miso",
            "Miso adds glutamates (umami) that deepen with aging",
            "Revolutionary fusion - two fermented traditions meet"
        ],
        "tags": ["cheese", "Gouda", "miso", "Japanese", "umami", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "thai-chile-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Thai Chile Cream Cheese",
        "category": "sides",
        "attribution": "Thai-American fusion cheese",
        "source_note": "Cream cheese with Thai bird's eye chiles and lime.",
        "description": "Rich cream cheese with fiery Thai bird's eye chiles and lime zest. Bright, intense heat balanced by creamy richness - Southeast Asian inspiration.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "Thai bird's eye chiles, minced", "quantity": "3-5", "unit": "chiles"},
            {"item": "lime zest", "quantity": "1", "unit": "tbsp"},
            {"item": "fresh cilantro, minced (optional)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cream cheese base."},
            {"step": 2, "text": "After draining, beat until smooth."},
            {"step": 3, "text": "Mince Thai chiles very finely (wear gloves - these are 50,000-100,000 Scoville)."},
            {"step": 4, "text": "Fold in chiles, lime zest, salt, and optional cilantro."},
            {"step": 5, "text": "Refrigerate. Heat intensifies overnight."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Bird's eye chiles are very hot - start with fewer and add to taste",
            "Lime zest brightens and balances the heat",
            "Excellent with rice crackers or in spring roll wrappers"
        ],
        "tags": ["cheese", "cream cheese", "Thai", "chile", "lime", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "lemongrass-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lemongrass Cream Cheese",
        "category": "sides",
        "attribution": "Southeast Asian-inspired artisan cheese",
        "source_note": "Cream cheese infused with fresh lemongrass.",
        "description": "Light, aromatic cream cheese infused with fresh lemongrass. Citrusy and floral without being overpowering - a unique Southeast Asian twist.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min + infusion",
        "cook_time": "3 hours",
        "total_time": "36-60 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "fresh lemongrass stalks", "quantity": "2", "unit": "stalks"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Bruise lemongrass stalks and cut into 2-inch pieces."},
            {"step": 2, "text": "Heat cream and milk to 160°F with lemongrass. Steep 30 minutes off heat."},
            {"step": 3, "text": "Strain out lemongrass. Cool milk to 75°F."},
            {"step": 4, "text": "Add starter and rennet. Let set 12-24 hours."},
            {"step": 5, "text": "Drain 12-24 hours. Beat until smooth, add salt."},
            {"step": 6, "text": "Refrigerate. Flavor develops over 1-2 days."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Use only the pale lower portion of lemongrass stalks",
            "Bruising releases essential oils",
            "Pairs beautifully with tropical fruits and seafood"
        ],
        "tags": ["cheese", "cream cheese", "lemongrass", "Southeast Asian", "aromatic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # === WORLD CHEESES (underrepresented regions) ===

    # SOUTH AMERICAN
    {
        "id": "queijo-minas-frescal",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queijo Minas Frescal (Brazilian Fresh Cheese)",
        "category": "sides",
        "attribution": "Traditional Brazilian cheese",
        "source_note": "Fresh cheese from Minas Gerais state, Brazil's most consumed cheese.",
        "description": "Brazil's most popular fresh cheese from Minas Gerais. Mild, slightly salty, with a soft texture perfect for breakfast or as a snack with guava paste.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-3 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet, let set 40-50 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently ladle curds into round molds without pressing."},
            {"step": 5, "text": "Let drain 6-8 hours at room temperature, flipping twice."},
            {"step": 6, "text": "Salt all surfaces. Refrigerate 24-72 hours before eating."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Minas Gerais is Brazil's dairy heartland",
            "Classic pairing with goiabada (guava paste) - called 'Romeo e Julieta'",
            "Best eaten within 1 week fresh"
        ],
        "tags": ["cheese", "Brazilian", "fresh", "Minas Gerais", "breakfast"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queijo-coalho",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queijo Coalho (Brazilian Grilling Cheese)",
        "category": "sides",
        "attribution": "Traditional Brazilian cheese",
        "source_note": "Northeastern Brazilian cheese designed for grilling, similar to Halloumi.",
        "description": "Brazilian grilling cheese from the Northeast. High-temperature resistant, it develops a delicious charred exterior while staying soft inside. Essential for churrasco.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-7 days aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F (40°C) over 30 minutes, stirring gently."},
            {"step": 5, "text": "Drain and press at 15 lbs for 30 min, flip, 20 lbs for 4 hours."},
            {"step": 6, "text": "Brine 3-4 hours or dry salt. Age 3-7 days refrigerated."}
        ],
        "temperature": "95-105°F (35-40°C)",
        "notes": [
            "Name means 'rennet cheese' in Portuguese",
            "Grill on skewers or flat grill until charred marks appear",
            "Often served with oregano and a squeeze of lime"
        ],
        "tags": ["cheese", "Brazilian", "grilling", "Northeastern", "churrasco"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # AFRICAN
    {
        "id": "ayib-ethiopian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ayib (Ethiopian Fresh Cheese)",
        "category": "sides",
        "attribution": "Traditional Ethiopian cheese",
        "source_note": "Ethiopian cottage cheese-style cheese, served with injera and stews.",
        "description": "Ethiopian fresh cheese similar to dry cottage cheese. Mild and crumbly, it provides cooling contrast to spicy Ethiopian dishes. Essential accompaniment to injera.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "2-4 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk or yogurt", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180°F (82°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat. Stir in buttermilk or yogurt."},
            {"step": 3, "text": "Let stand 10 minutes until curds separate from whey."},
            {"step": 4, "text": "Pour into cheesecloth-lined strainer. Drain 2-4 hours."},
            {"step": 5, "text": "Crumble drained curds, mix with salt."},
            {"step": 6, "text": "Serve immediately or refrigerate up to 1 week."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Traditional accompaniment to doro wat and other spicy stews",
            "Mild flavor balances the heat of berbere-spiced dishes",
            "Can be mixed with kibe (spiced butter) for extra richness"
        ],
        "tags": ["cheese", "Ethiopian", "African", "fresh", "cottage cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wara-nigerian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wara (Nigerian Fresh Cheese)",
        "category": "sides",
        "attribution": "Traditional Nigerian cheese",
        "source_note": "West African soft cheese made by Fulani herders, coagulated with plant extract.",
        "description": "Traditional Nigerian soft cheese made by Fulani herders. Coagulated with calotropis plant juice, it has a unique slightly bitter edge and soft, tofu-like texture.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 min",
        "cook_time": "1 hour",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "fresh cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "calotropis leaf extract (or lemon juice substitute)", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185°F (85°C), stirring constantly."},
            {"step": 2, "text": "Remove from heat. Add coagulant slowly while stirring."},
            {"step": 3, "text": "Let stand 15-20 minutes until curds form."},
            {"step": 4, "text": "Ladle curds into woven basket or cheesecloth-lined mold."},
            {"step": 5, "text": "Press lightly with weight for 2-3 hours."},
            {"step": 6, "text": "Unmold and salt lightly. Best eaten same day."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Traditional coagulant is extract from Sodom apple (calotropis) plant",
            "Lemon juice creates similar texture without the slight bitterness",
            "Often fried in palm oil until golden - called 'wara elede'"
        ],
        "tags": ["cheese", "Nigerian", "African", "Fulani", "fresh"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "klila-moroccan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Klila (Moroccan Dried Cheese)",
        "category": "sides",
        "attribution": "Traditional Moroccan cheese",
        "source_note": "Moroccan dried cheese balls, traditional Berber preservation method.",
        "description": "Moroccan dried cheese made by Berber communities. Fresh cheese is salted, shaped into balls, and sun-dried for long preservation. Reconstituted in stews or eaten as snack.",
        "servings_yield": "About 12 cheese balls",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "3-7 days drying",
        "ingredients": [
            {"item": "fresh goat or cow milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup"},
            {"item": "coarse salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180°F (82°C). Add buttermilk, stir once."},
            {"step": 2, "text": "Let curds form 10 minutes. Pour into cheesecloth."},
            {"step": 3, "text": "Drain thoroughly 4-6 hours until quite dry."},
            {"step": 4, "text": "Knead in salt. Form into small balls (golf ball sized)."},
            {"step": 5, "text": "Sun dry on clean cloth 3-7 days, turning daily, until completely hard."},
            {"step": 6, "text": "Store in cool, dry place. Lasts months."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Traditional Berber cheese preservation technique",
            "Reconstitute in warm water or add directly to tagines",
            "Can be grated over couscous when dried"
        ],
        "tags": ["cheese", "Moroccan", "African", "Berber", "dried", "preserved"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # MIDDLE EASTERN
    {
        "id": "akkawi-levantine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Akkawi (Levantine Brine Cheese)",
        "category": "sides",
        "attribution": "Traditional Levantine cheese",
        "source_note": "Brined white cheese from the Levant, named after Acre (Akka), Palestine.",
        "description": "Mild, white brined cheese from the Levant. Soft texture with moderate saltiness, traditionally desalted before use in sweets like knafeh or eaten fresh.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "1-2 weeks aging in brine",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "for brine", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir 15 minutes, keeping temperature at 90°F."},
            {"step": 5, "text": "Drain and press lightly (5 lbs) for 2 hours."},
            {"step": 6, "text": "Cut into blocks and place in brine (1 lb salt per gallon water)."},
            {"step": 7, "text": "Age in brine 1-2 weeks refrigerated."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Must be desalted in water 6-12 hours before using in desserts",
            "Essential cheese for knafeh and other Middle Eastern sweets",
            "Named after the ancient port city of Acre"
        ],
        "tags": ["cheese", "Levantine", "Palestinian", "brined", "Middle Eastern"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "nabulsi-palestinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Nabulsi (Palestinian Boiled Cheese)",
        "category": "sides",
        "attribution": "Traditional Palestinian cheese",
        "source_note": "White brined cheese from Nablus, Palestine. Traditionally boiled with mahlab and mastic.",
        "description": "Palestinian brined cheese from Nablus, distinctively flavored with mahlab (cherry pit spice) and mastic. Boiled preparation gives unique texture and flavor profile.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "2-3 weeks aging",
        "ingredients": [
            {"item": "whole sheep or cow milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "mahlab (ground cherry pits)", "quantity": "1", "unit": "tsp"},
            {"item": "mastic gum, ground", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt for brine", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Make basic white cheese: heat milk to 90°F, add starter, ripen, add rennet."},
            {"step": 2, "text": "Cut curds, drain, and press lightly for 2 hours."},
            {"step": 3, "text": "Cut into rectangular blocks."},
            {"step": 4, "text": "Boil cheese blocks in whey with mahlab and mastic for 30 minutes."},
            {"step": 5, "text": "Cool and place in strong brine solution."},
            {"step": 6, "text": "Age in brine 2-3 weeks."}
        ],
        "temperature": "90°F (32°C) for cheesemaking",
        "notes": [
            "Mahlab adds distinctive cherry/almond flavor",
            "Mastic provides subtle pine/resin notes",
            "Boiling process creates characteristic squeaky texture"
        ],
        "tags": ["cheese", "Palestinian", "Nablus", "brined", "Middle Eastern", "boiled"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "jibneh-arabieh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Jibneh Arabieh (Arabian White Cheese)",
        "category": "sides",
        "attribution": "Traditional Arabian cheese",
        "source_note": "Soft white table cheese common throughout the Arabian Peninsula.",
        "description": "Soft, mild white cheese popular across the Arabian Peninsula. Simple preparation with clean, milky flavor - perfect for breakfast with bread, dates, and honey.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "1.5 hours",
        "total_time": "4-6 hours",
        "ingredients": [
            {"item": "whole cow or goat milk", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet diluted in water. Stir gently once."},
            {"step": 3, "text": "Let set 45-60 minutes until curd is firm."},
            {"step": 4, "text": "Cut curds into large cubes. Rest 10 minutes."},
            {"step": 5, "text": "Ladle into molds or cheesecloth. Drain 4-6 hours."},
            {"step": 6, "text": "Salt lightly. Eat fresh or store in light brine up to 2 weeks."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Simple cheese common at Gulf Arab breakfast tables",
            "Often served with date syrup (dibs) or honey",
            "Fresh version has very mild, clean flavor"
        ],
        "tags": ["cheese", "Arabian", "Gulf", "fresh", "Middle Eastern", "breakfast"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # ASIAN
    {
        "id": "rushan-chinese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rushan (Chinese Fan Cheese)",
        "category": "sides",
        "attribution": "Traditional Bai minority cheese",
        "source_note": "Stretched cheese from Yunnan Province, made by the Bai minority people.",
        "description": "Unique Chinese cheese from Yunnan's Bai people. Fresh cheese is stretched into thin sheets, dried on bamboo frames into fan shapes. Grilled or fried as street food.",
        "servings_yield": "About 4 cheese fans",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "2-3 hours + drying",
        "ingredients": [
            {"item": "fresh cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "sour whey or dilute vinegar", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 160°F (71°C)."},
            {"step": 2, "text": "Add sour whey or vinegar. Stir until curds form."},
            {"step": 3, "text": "Collect curds, knead while still warm."},
            {"step": 4, "text": "Stretch the warm curd repeatedly until smooth and elastic."},
            {"step": 5, "text": "Shape into thin sheets and drape over bamboo sticks to form fan shape."},
            {"step": 6, "text": "Dry until firm but still pliable. Grill over flame to serve."}
        ],
        "temperature": "160°F (71°C)",
        "notes": [
            "One of China's few traditional cheeses",
            "Bai minority specialty from Dali region, Yunnan",
            "Grilled rushan is popular Yunnan street food, often sweetened"
        ],
        "tags": ["cheese", "Chinese", "Yunnan", "Bai minority", "stretched", "Asian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "rubing-chinese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rubing (Yunnan Goat Cheese)",
        "category": "sides",
        "attribution": "Traditional Bai and Sani minority cheese",
        "source_note": "Firm goat milk cheese from Yunnan, made by Bai and Sani peoples.",
        "description": "Firm, mild goat cheese from Yunnan Province. Dense texture holds up to grilling or frying. Often served with chili flakes as a snack or appetizer.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "4-6 hours",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "sour whey or white vinegar", "quantity": "3/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 180°F (82°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat. Add sour whey or vinegar gradually while stirring."},
            {"step": 3, "text": "Let curds form 10-15 minutes."},
            {"step": 4, "text": "Drain curds in cheesecloth. Press in square mold with moderate weight."},
            {"step": 5, "text": "Press 2-4 hours until firm block forms."},
            {"step": 6, "text": "Unmold and salt surfaces. Ready to grill or fry."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Sani and Bai peoples have made this cheese for centuries",
            "Cut into cubes and pan-fry until golden outside, soft inside",
            "Serve with Yunnan chili flakes and mint"
        ],
        "tags": ["cheese", "Chinese", "Yunnan", "goat", "Asian", "firm"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chhurpi-himalayan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chhurpi (Himalayan Hard Cheese)",
        "category": "sides",
        "attribution": "Traditional Himalayan cheese",
        "source_note": "Rock-hard yak or cow milk cheese from Nepal, Bhutan, Tibet, and Sikkim.",
        "description": "Extremely hard Himalayan cheese, traditionally from yak milk. So hard it must be chewed for hours or softened in tea. Traditional protein source for mountain peoples.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "4-8 weeks drying",
        "ingredients": [
            {"item": "yak or cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk or yogurt", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 180°F (82°C). Add buttermilk to curdle."},
            {"step": 2, "text": "Let curds form, then drain thoroughly in cloth."},
            {"step": 3, "text": "Press curds very firmly for 24-48 hours."},
            {"step": 4, "text": "Cut into small cubes or sticks."},
            {"step": 5, "text": "Smoke over wood fire for several hours (traditional method)."},
            {"step": 6, "text": "Sun dry for 4-8 weeks until rock hard."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "So hard it's sometimes called 'Himalayan chewing gum'",
            "Traditional long-lasting protein source for herders",
            "Now popular as long-lasting dog chews internationally"
        ],
        "tags": ["cheese", "Himalayan", "Nepali", "Tibetan", "dried", "hard", "Asian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # CENTRAL ASIAN
    {
        "id": "kurut-kazakh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kurut (Kazakh Dried Cheese Balls)",
        "category": "sides",
        "attribution": "Traditional Central Asian cheese",
        "source_note": "Dried salted cheese balls from Kazakhstan and Central Asia, made from suzma (strained yogurt).",
        "description": "Central Asian dried cheese balls made from strained yogurt. Extremely salty and sour, these long-lasting provisions sustained nomadic herders. Dissolved in water for a tangy drink.",
        "servings_yield": "About 20 cheese balls",
        "prep_time": "20 min",
        "cook_time": "None",
        "total_time": "5-10 days drying",
        "ingredients": [
            {"item": "plain whole milk yogurt", "quantity": "32", "unit": "oz"},
            {"item": "salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Line strainer with cheesecloth. Add yogurt."},
            {"step": 2, "text": "Drain 24-48 hours until very thick (suzma stage)."},
            {"step": 3, "text": "Mix salt thoroughly into the thick yogurt."},
            {"step": 4, "text": "Form into small balls, about 1 inch diameter."},
            {"step": 5, "text": "Dry in sun or low oven (150°F) for 5-10 days until completely hard."},
            {"step": 6, "text": "Store indefinitely in dry place."}
        ],
        "temperature": "Sun dried or 150°F (65°C)",
        "notes": [
            "Essential travel food for Central Asian nomads",
            "Dissolve in warm water for ayran-like sour drink",
            "Called kurt, qurt, or kurut across different regions"
        ],
        "tags": ["cheese", "Kazakh", "Central Asian", "dried", "preserved", "nomadic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "irimshik-kazakh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Irimshik (Kazakh Sweet Dried Cheese)",
        "category": "sides",
        "attribution": "Traditional Kazakh cheese",
        "source_note": "Sweet dried cheese from Kazakhstan, made by slowly cooking milk until caramelized.",
        "description": "Unique Kazakh cheese made by slowly cooking milk until it caramelizes and dries. Sweet, crumbly texture with butterscotch notes - more confection than traditional cheese.",
        "servings_yield": "About 8 oz",
        "prep_time": "15 min",
        "cook_time": "4-6 hours",
        "total_time": "6-8 hours",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk or kefir", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and buttermilk in large, heavy pot."},
            {"step": 2, "text": "Bring to simmer over low heat. Curds will form."},
            {"step": 3, "text": "Continue cooking over very low heat, stirring occasionally."},
            {"step": 4, "text": "Cook 4-6 hours until most liquid evaporates and mass turns golden."},
            {"step": 5, "text": "Spread on baking sheet to cool and dry further."},
            {"step": 6, "text": "Crumble when dry. Store in airtight container."}
        ],
        "temperature": "Low simmer",
        "notes": [
            "Color ranges from golden to reddish-brown depending on cook time",
            "Naturally sweet from lactose caramelization - no sugar added",
            "Traditional Kazakh snack and dessert"
        ],
        "tags": ["cheese", "Kazakh", "Central Asian", "sweet", "dried", "caramelized"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # EASTERN EUROPEAN
    {
        "id": "urda-romanian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Urda (Romanian Whey Cheese)",
        "category": "sides",
        "attribution": "Traditional Romanian cheese",
        "source_note": "Romanian whey cheese similar to ricotta, made from sheep or cow whey.",
        "description": "Romanian fresh cheese made from heated whey, similar to Italian ricotta. Light, fluffy texture with mild, slightly sweet flavor. Essential in Romanian cuisine.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "1 hour",
        "total_time": "2-3 hours",
        "ingredients": [
            {"item": "fresh whey (from cheesemaking)", "quantity": "1", "unit": "gallon"},
            {"item": "whole milk (optional, for richer urda)", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh whey slowly to 195°F (90°C)."},
            {"step": 2, "text": "Add optional milk for richer texture."},
            {"step": 3, "text": "Hold at 195°F for 30-45 minutes. Fine curds will rise to surface."},
            {"step": 4, "text": "Skim floating curds with slotted spoon into cheesecloth."},
            {"step": 5, "text": "Drain 1-2 hours until desired consistency."},
            {"step": 6, "text": "Mix in salt. Use immediately or refrigerate up to 5 days."}
        ],
        "temperature": "195°F (90°C)",
        "notes": [
            "Traditional way to use whey from brânză or telemea production",
            "Used in Romanian pastries like plăcinte and as filling for sarmale",
            "Sheep milk whey produces the finest urda"
        ],
        "tags": ["cheese", "Romanian", "Eastern European", "whey", "fresh", "ricotta-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "branza-de-burduf",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Brânză de Burduf (Romanian Bark Cheese)",
        "category": "sides",
        "attribution": "Traditional Romanian cheese",
        "source_note": "Romanian sheep cheese aged in fir bark or sheep stomach, from Transylvania.",
        "description": "Traditional Transylvanian sheep cheese, aged in pine bark cylinders or sheep stomach. Strong, pungent flavor with slight resinous notes from the bark. A mountain shepherd specialty.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "3", "unit": "tbsp"},
            {"item": "fir or pine bark cylinder (burduf)", "quantity": "1", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Make basic sheep cheese: heat milk to 95°F, add starter, rennet, form curds."},
            {"step": 2, "text": "Drain and press curds until quite dry."},
            {"step": 3, "text": "Crumble or grate the pressed cheese finely."},
            {"step": 4, "text": "Mix thoroughly with salt."},
            {"step": 5, "text": "Pack tightly into bark cylinder or sheep stomach."},
            {"step": 6, "text": "Age in cool cellar 2-4 weeks."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Burduf means the bark container or sheep stomach casing",
            "Fir bark imparts subtle resinous, forest character",
            "Protected Traditional Specialty in Romania"
        ],
        "tags": ["cheese", "Romanian", "Transylvanian", "sheep", "aged", "bark-aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "tvarog-slavic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tvarog (Slavic Curd Cheese)",
        "category": "sides",
        "attribution": "Traditional Slavic cheese",
        "source_note": "Fresh curd cheese found throughout Eastern Europe - Russia, Poland, Czech Republic, etc.",
        "description": "Essential Eastern European fresh cheese, known as tvorog (Russia), twaróg (Poland), or tvaroh (Czech). Tangy, crumbly fresh cheese used in both sweet and savory dishes.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "10 min + overnight",
        "cook_time": "1 hour",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk or kefir", "quantity": "1", "unit": "cup"},
            {"item": "salt (optional)", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix milk with buttermilk or kefir in large pot."},
            {"step": 2, "text": "Cover and let stand at room temperature 24-48 hours until thickened/clabbered."},
            {"step": 3, "text": "Heat very slowly to 150°F (65°C) - do not stir. Curds will separate."},
            {"step": 4, "text": "Let cool in whey 30 minutes."},
            {"step": 5, "text": "Pour into cheesecloth-lined strainer. Drain 4-8 hours."},
            {"step": 6, "text": "Add salt if desired. Use in pierogies, blintzes, cheesecakes, or eat plain."}
        ],
        "temperature": "150°F (65°C)",
        "notes": [
            "Foundation of Eastern European cuisine",
            "Used in sweet dishes (syrniki, blintzes) and savory (pierogies, lazanki)",
            "Texture ranges from smooth to crumbly based on drainage time"
        ],
        "tags": ["cheese", "Slavic", "Russian", "Polish", "Czech", "fresh", "curd"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # CAUCASUS
    {
        "id": "sulguni-georgian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sulguni (Georgian Stretched Cheese)",
        "category": "sides",
        "attribution": "Traditional Georgian cheese",
        "source_note": "Georgian brined cheese with layered, stringy texture from Samegrelo region.",
        "description": "Iconic Georgian cheese with distinctive layered, stringy texture from stretching. Brined in salt water, it's mild with slight sourness. Often smoked for deeper flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "1-2 weeks aging",
        "ingredients": [
            {"item": "whole cow's or buffalo milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt for brine", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes."},
            {"step": 3, "text": "Cut curds, let acidify at room temperature 6-12 hours."},
            {"step": 4, "text": "When curds stretch smoothly in 170°F water, proceed to stretching."},
            {"step": 5, "text": "Heat curds in 170°F (77°C) water, stretch and fold repeatedly."},
            {"step": 6, "text": "Form into rounds, cool in ice water. Brine 1-2 weeks."}
        ],
        "temperature": "95°F (35°C) for curd, 170°F (77°C) for stretching",
        "notes": [
            "Similar to mozzarella but acidified longer for tangier flavor",
            "Smoked sulguni (shemtsvari) is a Megrelian specialty",
            "Essential filling for khachapuri (Georgian cheese bread)"
        ],
        "tags": ["cheese", "Georgian", "Caucasus", "stretched", "brined", "pasta filata"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chanakh-armenian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chanakh (Armenian Pot Cheese)",
        "category": "sides",
        "attribution": "Traditional Armenian cheese",
        "source_note": "Armenian brined cheese traditionally aged in clay pots.",
        "description": "Armenian white cheese traditionally aged in clay pots (chanakh). Firm, crumbly texture with sharp, tangy flavor from extended brining. Foundation of Armenian cuisine.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "1-3 months aging",
        "ingredients": [
            {"item": "sheep or cow milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt for brine", "quantity": "1 lb per gallon water", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet, let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into small cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir and heat to 100°F (38°C)."},
            {"step": 5, "text": "Drain and press at moderate weight for 6-8 hours."},
            {"step": 6, "text": "Cut into blocks, place in strong brine. Age 1-3 months in cool place."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Traditional clay pot aging develops complex flavors",
            "Modern versions often use plastic containers",
            "Essential for Armenian breakfast with lavash bread"
        ],
        "tags": ["cheese", "Armenian", "Caucasus", "brined", "aged", "pot cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # MORE ADULTERATED CHEESES
    {
        "id": "rum-washed-gouda",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rum Washed Gouda",
        "category": "sides",
        "attribution": "Caribbean-Dutch fusion artisan cheese",
        "source_note": "Dutch Gouda with Caribbean rum washes for tropical character.",
        "description": "Creamy Dutch Gouda enhanced with Caribbean rum washes during aging. Caramel, vanilla, and molasses notes from the rum complement Gouda's natural sweetness.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "aged dark rum", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard Gouda with washed-curd method."},
            {"step": 2, "text": "Brine as normal, then air dry 3-4 days."},
            {"step": 3, "text": "Begin rum washes: brush entire surface with rum every 3-4 days."},
            {"step": 4, "text": "Continue rum washes for 6 weeks."},
            {"step": 5, "text": "Age at 55°F for 3-6 months total."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Use quality aged rum for best flavor",
            "Molasses and caramel notes develop from the rum",
            "Excellent with tropical fruits and dark chocolate"
        ],
        "tags": ["cheese", "Gouda", "rum", "Caribbean", "washed", "Dutch-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "tequila-washed-queso",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tequila Washed Queso",
        "category": "sides",
        "attribution": "Mexican artisan cheese",
        "source_note": "Mexican-style cheese washed with reposado tequila.",
        "description": "Mexican semi-firm cheese enhanced with reposado tequila washes. Agave and oak notes from the tequila create a distinctly Mexican cheese with complex character.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "reposado tequila", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make semi-firm Mexican-style cheese base."},
            {"step": 2, "text": "Press, brine briefly, and air dry 3 days."},
            {"step": 3, "text": "Wash with tequila every 3-4 days for 4-6 weeks."},
            {"step": 4, "text": "Age at 55°F for 2-4 months total."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Reposado tequila adds oak and agave complexity",
            "Añejo tequila creates even deeper, woodier flavor",
            "Perfect for elevated quesadillas and Mexican dishes"
        ],
        "tags": ["cheese", "Mexican", "tequila", "washed", "agave"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "szechuan-peppercorn-jack",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Szechuan Peppercorn Jack",
        "category": "sides",
        "attribution": "Chinese-American fusion artisan cheese",
        "source_note": "Monterey Jack with Szechuan peppercorns for numbing heat.",
        "description": "Creamy Monterey Jack with Szechuan peppercorns' distinctive numbing, citrusy sensation. Unique 'ma la' effect creates tingles unlike any other cheese.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "Szechuan peppercorns, lightly crushed", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Lightly toast and crush Szechuan peppercorns - don't grind to powder."},
            {"step": 2, "text": "Make standard Monterey Jack base."},
            {"step": 3, "text": "Mix crushed peppercorns into drained curds with salt."},
            {"step": 4, "text": "Press and age as standard Jack cheese 4-8 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Szechuan peppercorns create numbing sensation, not spicy heat",
            "Citrus and floral notes complement mild Jack cheese",
            "Excellent in fusion dishes or with Asian pears"
        ],
        "tags": ["cheese", "Jack", "Szechuan", "Chinese", "peppercorn", "numbing"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dukkah-coated-chevre",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Dukkah Coated Chèvre",
        "category": "sides",
        "attribution": "Egyptian-inspired artisan cheese",
        "source_note": "Fresh goat cheese rolled in Egyptian dukkah nut-spice blend.",
        "description": "Creamy fresh goat cheese rolled in Egyptian dukkah - a blend of hazelnuts, coriander, cumin, and sesame. Crunchy coating with Middle Eastern aromatics.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "dukkah spice blend", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard fresh chèvre."},
            {"step": 2, "text": "Drain 24 hours until thick and shapeable."},
            {"step": 3, "text": "Form into log shape. Salt lightly."},
            {"step": 4, "text": "Roll log firmly in dukkah, coating completely."},
            {"step": 5, "text": "Refrigerate 24 hours for flavors to meld."},
            {"step": 6, "text": "Slice into rounds to serve."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Dukkah is Egyptian nut-spice blend with hazelnuts, coriander, cumin, sesame",
            "Crunchy coating contrasts with creamy cheese",
            "Serve with olive oil and warm flatbread"
        ],
        "tags": ["cheese", "goat", "dukkah", "Egyptian", "coated", "Middle Eastern"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "everything-bagel-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Everything Bagel Cream Cheese",
        "category": "sides",
        "attribution": "American-Jewish deli style",
        "source_note": "Cream cheese mixed with everything bagel seasoning.",
        "description": "Homemade cream cheese loaded with everything bagel seasoning - poppy seeds, sesame seeds, dried garlic, dried onion, and coarse salt. A deli classic made at home.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "everything bagel seasoning", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cream cheese base."},
            {"step": 2, "text": "Drain 12-24 hours until thick."},
            {"step": 3, "text": "Beat until smooth."},
            {"step": 4, "text": "Mix in salt and everything bagel seasoning thoroughly."},
            {"step": 5, "text": "Refrigerate to firm up before serving."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Everything seasoning includes poppy, sesame, garlic, onion, salt",
            "A New York deli staple",
            "Perfect on fresh bagels or crackers"
        ],
        "tags": ["cheese", "cream cheese", "everything bagel", "American", "Jewish deli"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "piri-piri-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Piri Piri Cream Cheese",
        "category": "sides",
        "attribution": "Portuguese-African inspired cheese",
        "source_note": "Cream cheese with African bird's eye chili (piri piri).",
        "description": "Cream cheese infused with piri piri - the African bird's eye chili used in Portuguese-African cuisine. Bright, sharp heat with citrus notes.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "piri piri sauce or paste", "quantity": "2", "unit": "tbsp"},
            {"item": "lemon zest", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cream cheese base and drain."},
            {"step": 2, "text": "Beat until smooth."},
            {"step": 3, "text": "Mix in salt, piri piri, and lemon zest."},
            {"step": 4, "text": "Adjust heat level to taste."},
            {"step": 5, "text": "Refrigerate overnight for flavors to develop."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Piri piri chili originated in Africa, adopted by Portuguese colonizers",
            "Heat level varies - adjust to taste",
            "Excellent with grilled chicken or on crusty bread"
        ],
        "tags": ["cheese", "cream cheese", "piri piri", "Portuguese", "African", "spicy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "saffron-paneer",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Saffron Paneer (Kesar Paneer)",
        "category": "sides",
        "attribution": "Indian artisan cheese",
        "source_note": "Indian fresh cheese infused with luxurious saffron.",
        "description": "Fresh Indian paneer infused with saffron, creating golden color and subtle floral, honey notes. Luxurious version of the everyday cheese, perfect for special occasions.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 min",
        "cook_time": "30 min",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "lemon juice or white vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "saffron threads", "quantity": "1/2", "unit": "tsp"},
            {"item": "warm milk (for blooming saffron)", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Bloom saffron in warm milk for 15 minutes."},
            {"step": 2, "text": "Heat gallon of milk to 190°F (88°C), just below boiling."},
            {"step": 3, "text": "Add saffron-milk mixture and lemon juice. Stir gently."},
            {"step": 4, "text": "Curds will separate from greenish whey."},
            {"step": 5, "text": "Pour into cheesecloth, drain, add salt."},
            {"step": 6, "text": "Press firmly for 2-3 hours until solid block forms."}
        ],
        "temperature": "190°F (88°C)",
        "notes": [
            "Saffron adds golden color and subtle floral-honey notes",
            "Traditional for wedding and festival dishes",
            "Pairs beautifully with pistachios and cardamom"
        ],
        "tags": ["cheese", "paneer", "saffron", "Indian", "fresh", "luxurious"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "black-garlic-brie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Black Garlic Brie",
        "category": "sides",
        "attribution": "Modern artisan cheese",
        "source_note": "Creamy Brie with caramelized black garlic for umami depth.",
        "description": "Creamy Brie-style cheese with sweet, caramelized black garlic folded throughout. Deep umami notes without raw garlic's pungency - sophisticated and complex.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum (white mold)", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "black garlic cloves, mashed", "quantity": "4-6", "unit": "cloves"}
        ],
        "instructions": [
            {"step": 1, "text": "Make Brie base: heat milk to 90°F, add cultures, ripen, add rennet."},
            {"step": 2, "text": "Cut curds, drain gently into Brie molds."},
            {"step": 3, "text": "Flip several times over 24 hours."},
            {"step": 4, "text": "Salt all surfaces. Mash black garlic and spread on top surface."},
            {"step": 5, "text": "Age at 55°F and 90%+ humidity. White bloom will develop."},
            {"step": 6, "text": "Ready when soft throughout, about 4-6 weeks."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Black garlic is sweet, mild, and umami-rich - no raw garlic bite",
            "Can also fold black garlic into center for stuffed effect",
            "Pairs with crusty bread and fig preserves"
        ],
        "tags": ["cheese", "Brie", "black garlic", "soft-ripened", "umami"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "matcha-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Matcha Green Tea Cream Cheese",
        "category": "sides",
        "attribution": "Japanese-American fusion cheese",
        "source_note": "Cream cheese with ceremonial grade matcha green tea.",
        "description": "Silky cream cheese with ceremonial grade matcha, creating earthy, vegetal notes with subtle sweetness. Vibrant green color and sophisticated umami character.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "ceremonial grade matcha powder", "quantity": "1-2", "unit": "tbsp"},
            {"item": "honey (optional)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Make standard cream cheese base and drain thoroughly."},
            {"step": 2, "text": "Sift matcha to remove lumps."},
            {"step": 3, "text": "Beat cream cheese until smooth."},
            {"step": 4, "text": "Add sifted matcha, salt, and optional honey. Mix thoroughly."},
            {"step": 5, "text": "Refrigerate overnight for color and flavor to develop."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Use ceremonial grade matcha for best color and flavor",
            "Culinary grade works but produces more bitter result",
            "Beautiful on Asian-inspired pastries or with fruit"
        ],
        "tags": ["cheese", "cream cheese", "matcha", "Japanese", "green tea"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]

def main():
    # Load existing recipes
    with open('/home/user/Allrecipes/data/recipes.json', 'r') as f:
        data = json.load(f)

    # Get existing IDs to check for duplicates
    existing_ids = {r['id'] for r in data['recipes']}

    # Filter out any duplicates
    new_recipes = []
    duplicates = []
    for recipe in NEW_RECIPES:
        if recipe['id'] in existing_ids:
            duplicates.append(recipe['id'])
        else:
            new_recipes.append(recipe)

    if duplicates:
        print(f"Skipping {len(duplicates)} duplicates: {duplicates}")

    # Add new recipes
    data['recipes'].extend(new_recipes)
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = '2026-01-22'

    # Save
    with open('/home/user/Allrecipes/data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {len(new_recipes)} new cheese recipes")
    print(f"Total recipes now: {data['meta']['total_count']}")

if __name__ == '__main__':
    main()
