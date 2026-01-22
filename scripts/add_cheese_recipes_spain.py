#!/usr/bin/env python3
"""Add comprehensive Spanish cheese recipes to the cheese category."""

import json

SPANISH_CHEESE_RECIPES = [
    # === CLASSIC SPANISH CHEESES ===
    {
        "id": "manchego-curado",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Manchego Curado (Aged Manchego)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "Spain's most famous cheese, PDO protected from La Mancha region.",
        "description": "The quintessential Spanish cheese made from Manchega sheep's milk. Aged 3-12 months, it develops a firm, crumbly texture with intense nutty, tangy, and slightly piquant flavors. The distinctive herringbone rind pattern comes from traditional esparto grass molds.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "sheep's milk (Manchega breed preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set for 45-60 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes - small curds are essential for Manchego's texture."},
            {"step": 4, "text": "Slowly heat to 104°F (40°C) over 30 minutes while stirring continuously."},
            {"step": 5, "text": "Maintain temperature and stir until curds shrink and feel firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and press into traditional pleita (herringbone) molds at 20 lbs for 2 hours, flip, then 40 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24 hours."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) and 85% humidity for 3-12 months. Rub with olive oil monthly."}
        ],
        "temperature": "86-104°F (30-40°C)",
        "notes": [
            "Manchego has PDO status - authentic only from La Mancha with Manchega sheep",
            "Herringbone pattern from traditional esparto grass molds (pleitas)",
            "Curado (cured) is aged 3-6 months; Viejo (old) is 6-12 months",
            "The sheep graze on wild herbs and grasses, giving distinctive terroir"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "aged", "La Mancha", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "manchego-semicurado",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Manchego Semicurado (Semi-Aged Manchego)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "Younger version of Manchego, aged 3-4 months.",
        "description": "The younger sibling of aged Manchego, with a softer, creamier texture and milder flavor. Still retains the characteristic nuttiness but with more buttery notes and less sharpness.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter culture, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes - slightly larger than for Curado."},
            {"step": 4, "text": "Heat to 102°F (39°C) over 25 minutes while stirring."},
            {"step": 5, "text": "Stir at temperature until curds firm, about 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 1 hour, flip, then 30 lbs for 12 hours."},
            {"step": 7, "text": "Brine for 18 hours."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for 3-4 months only."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Semicurado is more approachable for those new to sheep's milk cheese",
            "Lighter pressing gives softer texture",
            "Shorter aging preserves more milky sweetness",
            "Excellent introduction to Manchego before trying aged versions"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "semi-aged", "La Mancha"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cabrales-blue-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Cabrales (Asturian Blue Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO cave-aged blue cheese from Asturias, Spain's strongest blue.",
        "description": "Spain's most intense blue cheese, traditionally made from mixed milks and aged in limestone caves of the Picos de Europa mountains. Bold, spicy, and complex with extensive blue-green veining throughout.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "3-6 months cave aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "raw sheep's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "raw goat's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (coarse)", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all three milks. Heat to 82°F (28°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add rennet, let set 90 minutes for very soft, fragile curd."},
            {"step": 3, "text": "Cut curds into large 2-inch pieces. Handle very gently."},
            {"step": 4, "text": "Ladle curds into molds without pressing, layering with coarse salt."},
            {"step": 5, "text": "Drain at cool room temperature (60-65°F/15-18°C) for 3-4 days, flipping twice daily."},
            {"step": 6, "text": "Pierce cheese extensively with sterilized skewer - 50+ holes per side."},
            {"step": 7, "text": "Age in cave-like conditions: 45-50°F (7-10°C) and 95% humidity for 3-6 months."},
            {"step": 8, "text": "Blue mold should develop extensively within 4-6 weeks."}
        ],
        "temperature": "82°F (28°C)",
        "notes": [
            "Traditional Cabrales uses milk from Asturian breeds grazing mountain pastures",
            "Cave aging in natural limestone caves is essential for authentic flavor",
            "Mixed milk creates more complex flavor than single-milk blues",
            "One of the world's strongest blue cheeses - not for the faint of heart"
        ],
        "tags": ["cheese", "Spanish", "blue cheese", "cave-aged", "Asturias", "PDO", "mixed milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mahon-menorca-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Mahon-Menorca (Menorcan Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO cheese from Menorca, Balearic Islands, with distinctive square shape.",
        "description": "Distinctive square-shaped cow's milk cheese from the island of Menorca. Made by wrapping curds in cloth (fogasser) and pressing, giving rounded edges. Buttery when young, sharp and crystalline when aged.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk (Friesian or Menorcan breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "olive oil and paprika for rind", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gather curds in cheesecloth (fogasser), twist corners together, and knead to expel whey."},
            {"step": 5, "text": "Place cloth-wrapped curds in square mold, pressing the gathered corners to create the characteristic 'mamella' (nipple) on top."},
            {"step": 6, "text": "Press at 30 lbs for 24 hours."},
            {"step": 7, "text": "Brine 48 hours, turning daily."},
            {"step": 8, "text": "Age at 55°F (13°C). Rub with olive oil mixed with paprika monthly. Age 2 months (tierno), 5 months (semicurado), or 10+ months (curado)."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Square shape with rounded edges is unique to Mahon",
            "The 'mamella' bump on top comes from the gathered cloth corners",
            "Paprika and oil rubbing gives distinctive orange rind",
            "Menorca's maritime climate influences the cheese's flavor"
        ],
        "tags": ["cheese", "Spanish", "cow's milk", "Menorca", "Balearic", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "idiazabal-basque-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Idiazabal (Basque Smoked Sheep Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO smoked sheep's milk cheese from the Basque Country and Navarra.",
        "description": "Firm, pressed sheep's milk cheese from the Basque Country, traditionally smoked over cherry or beech wood. Intense, buttery flavor with smoky undertones. Made from Latxa and Carranzana sheep's milk.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-6 months aging plus smoking",
        "ingredients": [
            {"item": "sheep's milk (Latxa breed preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "cherry or beech wood chips for smoking", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 100°F (38°C) over 30 minutes while stirring constantly."},
            {"step": 5, "text": "Continue stirring until curds are firm and shrunk, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 25 lbs for 2 hours, flip, then 40 lbs for 24 hours."},
            {"step": 7, "text": "Brine 24-36 hours."},
            {"step": 8, "text": "Age at 50°F (10°C) for 2 months minimum. Cold smoke over cherry or beech wood for 10-15 days. Continue aging 2-4 more months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Smoking is traditional but not required - unsmoked Idiazabal exists",
            "Latxa sheep produce rich, fatty milk ideal for cheese",
            "Shepherds traditionally made this while grazing flocks in mountains",
            "The smoky exterior gives way to creamy, nutty interior"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "smoked", "Basque", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "tetilla-galician-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Tetilla (Galician Breast-Shaped Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO soft cheese from Galicia with distinctive conical shape.",
        "description": "Soft, creamy cow's milk cheese from Galicia, named for its distinctive breast-like conical shape. Mild, buttery, and slightly tangy with a thin, edible rind. The shape comes from the traditional mold design.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk (Galician breeds preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 82°F (28°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes at 82°F - do not heat further."},
            {"step": 5, "text": "Ladle curds into conical (tetilla) molds without pressing."},
            {"step": 6, "text": "Drain at room temperature 12-24 hours, flipping 3-4 times."},
            {"step": 7, "text": "Salt surfaces lightly."},
            {"step": 8, "text": "Age at 50°F (10°C) and 85% humidity for 2-4 weeks."}
        ],
        "temperature": "82°F (28°C)",
        "notes": [
            "Tetilla means 'small breast' - refers to the conical shape",
            "Very mild cheese, popular with children and cheese novices",
            "Galicia's humid climate is perfect for soft cheese production",
            "Often served as dessert with membrillo (quince paste)"
        ],
        "tags": ["cheese", "Spanish", "cow's milk", "soft", "Galicia", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "torta-del-casar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Torta del Casar (Extremaduran Creamy Sheep Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO soft sheep's milk cheese from Extremadura with liquid interior.",
        "description": "Luxurious soft sheep's milk cheese from Extremadura with a runny, spoonable interior when ripe. Made using vegetable rennet from cardoon thistle, giving distinctive bitter-herbaceous notes. Cut off the top and spoon out the creamy center.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "60-90 days aging",
        "ingredients": [
            {"item": "raw sheep's milk (Merino or Entrefino breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "cardoon thistle rennet (Cynara cardunculus)", "quantity": "1", "unit": "tbsp prepared extract"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw sheep's milk to 82-86°F (28-30°C). Add minimal starter for slow acidification."},
            {"step": 2, "text": "Add cardoon thistle rennet extract. Let set 60-75 minutes for very soft, fragile curd."},
            {"step": 3, "text": "Cut curds very gently into large 1.5-inch pieces."},
            {"step": 4, "text": "Ladle directly into flat, round molds without any pressing."},
            {"step": 5, "text": "Drain at room temperature 24-48 hours, flipping gently every 6-8 hours."},
            {"step": 6, "text": "Salt top and bottom surfaces."},
            {"step": 7, "text": "Age at 46-50°F (8-10°C) and 85-90% humidity for 60-90 days."},
            {"step": 8, "text": "The interior should become liquid and spoonable when fully ripe."}
        ],
        "temperature": "82-86°F (28-30°C)",
        "notes": [
            "Cardoon thistle rennet is essential - it creates the unique texture and bitter notes",
            "The cheese 'torta' has a sunken top when properly made",
            "Serve by cutting off the top and scooping with bread",
            "Similar to Portuguese Queijo da Serra but with distinct character"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "soft", "spoonable", "Extremadura", "PDO", "vegetable rennet"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-murcia-al-vino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso de Murcia al Vino (Wine-Washed Goat Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO goat cheese from Murcia, washed in red wine during aging.",
        "description": "Elegant goat cheese from the Murcia region, washed in local red wine during aging. The wine creates a distinctive burgundy-purple rind while the interior remains white and creamy. Mild goat flavor with fruity wine notes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "goat's milk (Murciana breed preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "red wine (Spanish Monastrell or similar)", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Stir until curds firm, about 20 minutes more."},
            {"step": 6, "text": "Drain and press at 15 lbs for 1 hour, flip, then 25 lbs for 8 hours."},
            {"step": 7, "text": "Brine 12 hours."},
            {"step": 8, "text": "Age at 50°F (10°C). Wash rind with red wine every 2-3 days for first month, then weekly. Total aging 2-3 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Murciana goats produce exceptionally sweet, mild milk",
            "Wine washing creates the signature purple rind",
            "Interior remains pristine white - beautiful contrast when cut",
            "The wine adds subtle fruity notes without overpowering the cheese"
        ],
        "tags": ["cheese", "Spanish", "goat's milk", "wine-washed", "Murcia", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "roncal-navarran-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Roncal (Navarran Sheep Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "Spain's first PDO cheese, from the Roncal Valley in Navarra.",
        "description": "Historic pressed sheep's milk cheese from the Pyrenean Roncal Valley. Spain's first cheese to receive PDO status. Hard, dry texture with intense, piquant flavor and notes of herbs and nuts. Made only from Rasa and Latxa sheep.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "4-12 months aging",
        "ingredients": [
            {"item": "sheep's milk (Rasa or Latxa breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into very small 1/4-inch cubes."},
            {"step": 4, "text": "Heat to 104°F (40°C) over 40 minutes while stirring constantly."},
            {"step": 5, "text": "Continue stirring until curds are very firm and dry, about 40 minutes."},
            {"step": 6, "text": "Drain and press heavily at 30 lbs for 2 hours, flip, then 50 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 48 hours."},
            {"step": 8, "text": "Age at 50°F (10°C) and 80% humidity for minimum 4 months, up to 12 months."}
        ],
        "temperature": "86-104°F (30-40°C)",
        "notes": [
            "First Spanish cheese to receive Denominacion de Origen (1981)",
            "Made only from December to July when sheep graze mountain pastures",
            "Heavy pressing creates the characteristic dense, dry texture",
            "Transhumance tradition - sheep move between mountain and valley pastures"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "hard", "aged", "Navarra", "PDO", "Pyrenees"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "zamorano-castilian-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Zamorano (Castilian Sheep Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO sheep's milk cheese from Zamora province, Castilla y Leon.",
        "description": "Firm, flavorful sheep's milk cheese from Zamora in the Castilian plains. Made from Churra and Castellana sheep, it has a grainy, crumbly texture with intense, slightly spicy flavor. Often compared to Manchego but with its own distinct character.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "sheep's milk (Churra or Castellana breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 82°F (28°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 50-60 minutes."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes."},
            {"step": 4, "text": "Heat to 102°F (39°C) over 35 minutes while stirring."},
            {"step": 5, "text": "Continue stirring until curds are firm and dry, about 35 minutes."},
            {"step": 6, "text": "Drain and press at 25 lbs for 2 hours, flip, then 45 lbs for 24 hours."},
            {"step": 7, "text": "Brine 36 hours."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for minimum 3 months, up to 12 months."}
        ],
        "temperature": "82-102°F (28-39°C)",
        "notes": [
            "Churra sheep are famous for their milk's high fat and protein content",
            "Zamora province has centuries of sheep cheese tradition",
            "Similar to Manchego but made from different sheep breeds",
            "Develops tyrosine crystals when well-aged"
        ],
        "tags": ["cheese", "Spanish", "sheep's milk", "hard", "aged", "Castilla y Leon", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "san-simon-da-costa-smoked",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "San Simon da Costa (Galician Smoked Cow Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO smoked cow's milk cheese from Galicia with distinctive teardrop shape.",
        "description": "Distinctive teardrop-shaped smoked cheese from Galicia. Smoked over birch wood, it has a glossy amber exterior and creamy, buttery interior. The unique shape and smoking tradition date back centuries.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months including smoking",
        "ingredients": [
            {"item": "whole cow's milk (Galician breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "birch wood chips for smoking", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 98°F (37°C) over 25 minutes while stirring."},
            {"step": 5, "text": "Drain and press into teardrop/pear-shaped molds at 20 lbs for 12 hours."},
            {"step": 6, "text": "Brine 12 hours."},
            {"step": 7, "text": "Age at 50°F (10°C) for 3-4 weeks, then cold smoke over birch wood for 2-3 weeks."},
            {"step": 8, "text": "Continue aging 2-4 more weeks after smoking."}
        ],
        "temperature": "86-98°F (30-37°C)",
        "notes": [
            "Teardrop shape is called 'pera' (pear) or 'bala' (bullet)",
            "Birch smoking is traditional - gives distinctive golden-brown rind",
            "Galicia's humid climate makes smoking an effective preservation method",
            "Interior stays creamy despite the firm smoked exterior"
        ],
        "tags": ["cheese", "Spanish", "cow's milk", "smoked", "Galicia", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "afuegal-pitu-asturian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Afuega'l Pitu (Asturian Spicy Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO cheese from Asturias, name means 'fire in the throat'.",
        "description": "Ancient Asturian cheese whose name means 'fire in the throat' in Asturian dialect - a testament to its dense, paste-like texture that sticks to the palate. Made in two versions: white (natural) or roxu (with paprika). Conical or gourd-shaped.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet (very small amount)", "quantity": "2", "unit": "drops"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"},
            {"item": "Spanish paprika (for roxu version)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C) - barely warm. Add starter."},
            {"step": 2, "text": "Add only 2 drops of rennet - this is primarily an acid-set cheese."},
            {"step": 3, "text": "Let set at room temperature 24-48 hours until thick, acidic curd forms."},
            {"step": 4, "text": "Hang curd in cheesecloth to drain for 24-48 hours."},
            {"step": 5, "text": "Mix salt (and paprika for roxu version) into the drained curd."},
            {"step": 6, "text": "Pack into conical (atroncau) or gourd-shaped (trapu) molds."},
            {"step": 7, "text": "Age at 50°F (10°C) for 2-8 weeks."},
            {"step": 8, "text": "Rind will develop natural molds - leave or brush as preferred."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "One of Spain's oldest cheese-making traditions",
            "Afuega'l Pitu means 'chokes the chicken' - refers to dense, sticky texture",
            "Roxu (red) version uses local paprika; blancu (white) is natural",
            "Two traditional shapes: atroncau (cone) and trapu (gourd/pumpkin)"
        ],
        "tags": ["cheese", "Spanish", "cow's milk", "acid-set", "Asturias", "PDO", "paprika"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "garrotxa-catalan-goat",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Garrotxa (Catalan Goat Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "Revived Catalan goat cheese with distinctive gray mold rind.",
        "description": "Semi-firm Catalan goat cheese with a distinctive fuzzy gray Penicillium mold rind. Nearly extinct in the 1980s, it was revived by artisan cheesemakers. Mild, nutty goat flavor with earthy undertones from the natural rind.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-8 weeks aging",
        "ingredients": [
            {"item": "goat's milk (Murciana-Granadina or Pyrenean breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium candidum (optional, will grow naturally)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 86°F (30°C). Add starter and optional P. candidum, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 95°F (35°C) over 20 minutes while stirring gently."},
            {"step": 5, "text": "Stir until curds firm slightly, about 15 minutes."},
            {"step": 6, "text": "Drain and press lightly at 10 lbs for 1 hour, flip, then 15 lbs for 6 hours."},
            {"step": 7, "text": "Salt surfaces."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) and 90% humidity for 3-8 weeks. Gray mold will develop naturally."}
        ],
        "temperature": "86-95°F (30-35°C)",
        "notes": [
            "Named for the Garrotxa region in Catalonia's Pyrenean foothills",
            "Was nearly extinct until 1981 revival by artisan cheesemakers",
            "Gray Penicillium mold rind is characteristic - don't brush it off",
            "Milder than many goat cheeses due to the mold-ripening"
        ],
        "tags": ["cheese", "Spanish", "goat's milk", "mold-ripened", "Catalonia", "artisanal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "majorero-canarian-goat",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Majorero (Canarian Goat Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO goat cheese from Fuerteventura, Canary Islands.",
        "description": "Pressed goat cheese from Fuerteventura in the Canary Islands, made from the native Majorera goat. Can be fresh, semi-cured, or aged. Traditionally rubbed with paprika, oil, or roasted corn flour (gofio). Intense goat flavor with island terroir.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "1 week to 6 months aging",
        "ingredients": [
            {"item": "goat's milk (Majorera breed)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "paprika, olive oil, or gofio for rind (optional)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 82°F (28°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 95°F (35°C) over 20 minutes while stirring."},
            {"step": 5, "text": "Drain and press into traditional palm-leaf patterned molds at 20 lbs for 12-24 hours."},
            {"step": 6, "text": "Brine 12-24 hours depending on size."},
            {"step": 7, "text": "Optionally rub rind with paprika, olive oil, or gofio (roasted corn flour)."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C): 1-2 weeks for fresh, 1-2 months semi-cured, 3-6 months for cured."}
        ],
        "temperature": "82-95°F (28-35°C)",
        "notes": [
            "Majorera goats are native to Fuerteventura, adapted to arid conditions",
            "Palm leaf mold pattern on rind is traditional",
            "Gofio coating is unique to Canarian cheese tradition",
            "Island terroir gives distinctive minerality"
        ],
        "tags": ["cheese", "Spanish", "goat's milk", "Canary Islands", "PDO", "gofio"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "arzua-ulloa-galician-soft",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Arzua-Ulloa (Galician Soft Cow Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "PDO soft cow's milk cheese from inland Galicia.",
        "description": "Soft, creamy cow's milk cheese from the Arzua and Ulloa regions of Galicia. Buttery and mild with a thin, edible rind. One of Spain's most approachable cheeses, often eaten at breakfast or as a snack.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk (Galician breeds)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 50 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Stir very gently for 15 minutes - do not heat further."},
            {"step": 5, "text": "Ladle curds into molds without pressing."},
            {"step": 6, "text": "Drain at room temperature 12-24 hours, flipping every 4-6 hours."},
            {"step": 7, "text": "Salt surfaces lightly."},
            {"step": 8, "text": "Age at 46-50°F (8-10°C) and 85-90% humidity for 2-4 weeks."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "One of Spain's mildest, most approachable cheeses",
            "Galicia's green, humid climate is ideal for soft cheese",
            "Often served with membrillo (quince paste) for dessert",
            "Similar to Tetilla but flatter disc shape"
        ],
        "tags": ["cheese", "Spanish", "cow's milk", "soft", "Galicia", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-iberico-mixed-milk",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Iberico (Spanish Mixed Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Spanish cheese",
        "source_note": "Classic Spanish blend of cow, sheep, and goat milks.",
        "description": "Traditional Spanish cheese blending cow, sheep, and goat milks in varying proportions. The combination creates a complex, balanced flavor - the creaminess of cow, richness of sheep, and tang of goat. A true taste of the Iberian Peninsula.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "sheep's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "goat's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all three milks. Heat to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Continue stirring until curds firm, about 25 minutes."},
            {"step": 6, "text": "Drain and press at 20 lbs for 2 hours, flip, then 35 lbs for 12 hours."},
            {"step": 7, "text": "Brine 24 hours."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) for 2-6 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Milk ratios can vary - some versions favor sheep, others cow",
            "Three-milk blend is traditional throughout central Spain",
            "Each milk contributes different characteristics to the final cheese",
            "The name 'Iberico' references the Iberian Peninsula"
        ],
        "tags": ["cheese", "Spanish", "mixed milk", "semi-hard", "blended"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Spanish cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in SPANISH_CHEESE_RECIPES:
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
