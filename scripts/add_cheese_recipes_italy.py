#!/usr/bin/env python3
"""Add comprehensive Italian cheese recipes to the cheese category."""

import json

ITALIAN_CHEESE_RECIPES = [
    # === WASHED RIND CHEESES ===
    {
        "id": "ita-taleggio-lombardy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Taleggio Lombardo (Lombardy Washed Rind)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP washed-rind cheese from Lombardy's Val Taleggio.",
        "description": "Pungent, creamy washed-rind cheese from the valleys of Lombardy. The characteristic orange rind and strong aroma belie a mild, fruity interior that melts beautifully.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "6-10 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "brine solution for washing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set 45-60 minutes until soft curd forms."},
            {"step": 3, "text": "Cut curds into 2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Gently ladle curds into square molds - do NOT press. Allow to drain naturally at room temperature."},
            {"step": 5, "text": "Flip every 2-3 hours for 12-24 hours until cheese holds its shape."},
            {"step": 6, "text": "Salt surfaces lightly. Transfer to aging cave at 50°F (10°C) and 95% humidity."},
            {"step": 7, "text": "Wash rind with light brine every 2-3 days. Rind will turn orange-pink."},
            {"step": 8, "text": "Age 6-10 weeks. Interior should become creamy near the rind."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Named for Val Taleggio in the Bergamo Alps",
            "Square shape is traditional and required for DOP status",
            "Rind washing develops the characteristic pungent aroma",
            "Interior is surprisingly mild compared to its strong smell"
        ],
        "tags": ["cheese", "Italian", "washed-rind", "Lombardy", "DOP", "soft-ripened"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-puzzone-di-moena",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Puzzone di Moena (Stinky Cheese of Moena)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Famously pungent washed-rind cheese from Trentino-Alto Adige.",
        "description": "Italy's stinkiest cheese from the Dolomite town of Moena. The name means 'big stinker' but the flavor is remarkably complex - earthy, meaty, with notes of hay and Alpine meadows.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-5 months aging",
        "ingredients": [
            {"item": "raw cow's milk (preferably Alpine)", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "brine for washing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 95°F (35°C). Add thermophilic starter and B. linens, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet and let set 35-45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 115°F (46°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Drain and press at 15 lbs for 30 minutes, flip, then 25 lbs for 12 hours."},
            {"step": 6, "text": "Brine for 24 hours in saturated solution."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity. Wash rind with brine every 2 days for first month."},
            {"step": 8, "text": "Continue aging 3-5 months, reducing washing to weekly. Rind becomes sticky and orange."}
        ],
        "temperature": "95-115°F (35-46°C)",
        "notes": [
            "Puzzone means 'big stinker' in local dialect",
            "Traditional production uses milk from Rendena and Bruna cows",
            "The smell is much stronger than the taste",
            "Pairs wonderfully with polenta and speck"
        ],
        "tags": ["cheese", "Italian", "washed-rind", "Trentino", "stinky cheese", "Alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === AGED HARD CHEESES ===
    {
        "id": "ita-grana-padano-traditional",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grana Padano Tradizionale",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP hard cheese from the Po Valley, Italy's most consumed cheese.",
        "description": "Grainy-textured hard cheese from the Po Valley, aged 9-24 months. Milder than Parmigiano-Reggiano with sweet, nutty flavors. Essential for risotto and pasta.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1 hour",
        "cook_time": "5 hours",
        "total_time": "9-24 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "lysozyme (optional, for raw milk)", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Allow whole milk to sit overnight. Skim cream from surface to create part-skim milk."},
            {"step": 2, "text": "Heat to 91°F (33°C). Add starter and optional lysozyme, ripen 20 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 15-20 minutes until firm break."},
            {"step": 4, "text": "Cut curds into rice-sized grains - as small as possible."},
            {"step": 5, "text": "Heat slowly to 131°F (55°C) over 45 minutes while stirring constantly."},
            {"step": 6, "text": "Hold at 131°F for 30 minutes, stirring until curds are very firm and squeaky."},
            {"step": 7, "text": "Let curds settle 45-60 minutes under whey. Collect in cheesecloth."},
            {"step": 8, "text": "Press at 40 lbs for 2 hours, flip, 50 lbs for 24-48 hours."},
            {"step": 9, "text": "Brine in saturated solution for 20-25 days, turning daily."},
            {"step": 10, "text": "Age at 60°F (16°C) and 85% humidity for minimum 9 months, up to 24 months for Riserva."}
        ],
        "temperature": "91-131°F (33-55°C)",
        "notes": [
            "Grana means 'grainy' - referring to the texture",
            "Part-skim milk is essential for proper aging",
            "Originally created by Cistercian monks in 1135",
            "More economical than Parmigiano-Reggiano with similar uses"
        ],
        "tags": ["cheese", "Italian", "hard", "grating", "Po Valley", "DOP", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-piave-vecchio",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Piave Vecchio (Aged Piave)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP hard cheese from the Piave River valley in Veneto.",
        "description": "Dense, intensely flavored aged cheese from the Dolomite foothills. Aged 12+ months, it develops crystalline texture and complex butterscotch notes. Often called the 'poor man's Parmigiano.'",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "12-18 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 118°F (48°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Continue stirring at 118°F until curds are very firm, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 30 lbs for 1 hour, flip, 45 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 3 days."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 12-18 months. Brush and turn weekly."}
        ],
        "temperature": "95-118°F (35-48°C)",
        "notes": [
            "Named for the Piave River that flows through Belluno province",
            "Vecchio means aged 12+ months; Stravecchio is 18+ months",
            "Develops tyrosine crystals like aged Parmesan",
            "Excellent table cheese and for grating"
        ],
        "tags": ["cheese", "Italian", "hard", "Veneto", "DOP", "aged", "grating"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === FRESH AND SEMI-SOFT ASIAGO ===
    {
        "id": "ita-asiago-pressato",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Asiago Pressato (Fresh Asiago)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Fresh, mild Asiago from the Asiago Plateau in Veneto.",
        "description": "Young, mild Asiago aged only 20-40 days. Soft, springy texture with sweet, milky flavor. Quite different from the aged versions - this is a table cheese, not for grating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "40 min",
        "cook_time": "2.5 hours",
        "total_time": "20-40 days aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 20 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 25-30 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 105°F (41°C) over 20 minutes while stirring gently."},
            {"step": 5, "text": "Drain and press at 15 lbs for 30 minutes, flip, 20 lbs for 4-6 hours."},
            {"step": 6, "text": "Brine for 12 hours."},
            {"step": 7, "text": "Age at 50°F (10°C) for only 20-40 days."}
        ],
        "temperature": "95-105°F (35-41°C)",
        "notes": [
            "Pressato refers to the pressed fresh style",
            "Much different from aged Asiago d'Allevo",
            "Soft enough to slice for sandwiches",
            "Popular as a table cheese in Northern Italy"
        ],
        "tags": ["cheese", "Italian", "semi-soft", "Veneto", "fresh", "table cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-asiago-stravecchio",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Asiago Stravecchio (Extra-Aged Asiago)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Aged Asiago d'Allevo from the Veneto highlands, 15+ months old.",
        "description": "Intensely flavored aged Asiago, hard and crumbly with sharp, complex taste. Aged minimum 15 months for Stravecchio designation. Excellent for grating over pasta and risotto.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "15-24 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Skim cream from milk surface to create part-skim milk."},
            {"step": 2, "text": "Heat to 95°F (35°C). Add starter, ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 30 minutes."},
            {"step": 4, "text": "Cut curds into small 1/4-inch pieces. Rest 5 minutes."},
            {"step": 5, "text": "Heat slowly to 115°F (46°C) over 30 minutes while stirring constantly."},
            {"step": 6, "text": "Continue stirring at temperature until curds are very firm, about 30 minutes."},
            {"step": 7, "text": "Drain and press at 25 lbs for 1 hour, flip, 35 lbs for 24 hours."},
            {"step": 8, "text": "Brine for 4-5 days."},
            {"step": 9, "text": "Age at 55°F (13°C) for minimum 15 months. Turn and brush weekly."}
        ],
        "temperature": "95-115°F (35-46°C)",
        "notes": [
            "Stravecchio means 'extra old' - minimum 15 months",
            "Part-skim milk is essential for proper aging",
            "Develops sharp, slightly spicy flavor",
            "Can substitute for Parmesan in many recipes"
        ],
        "tags": ["cheese", "Italian", "hard", "Veneto", "aged", "grating"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === PROVOLONE VARIETIES ===
    {
        "id": "ita-provolone-valpadana-dop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Provolone Valpadana DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP pasta filata cheese from the Po Valley, made since the 19th century.",
        "description": "Stretched-curd cheese from Northern Italy, available in Dolce (mild, 2-3 months) or Piccante (sharp, 4+ months) styles. Traditional shapes include salami, melon, and pear.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder (for Piccante)", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F (36°C). Add starter and lipase (for Piccante style), ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 30-40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Heat to 118°F (48°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds, let mat together for 2-3 hours until pH reaches 5.2-5.3."},
            {"step": 6, "text": "Cut curd mass into strips. Place in 170-180°F (77-82°C) water."},
            {"step": 7, "text": "Knead and stretch repeatedly until smooth and elastic. Form into desired shape."},
            {"step": 8, "text": "Cool in cold water, then brine 24-48 hours depending on size."},
            {"step": 9, "text": "Hang to age at 55°F (13°C). Dolce: 2-3 months. Piccante: 4-12 months."}
        ],
        "temperature": "97-180°F (36-82°C)",
        "notes": [
            "Valpadana refers to the Po Valley (Val Padana)",
            "Traditional shapes hung by ropes for aging",
            "Lipase gives Piccante version its sharp bite",
            "Smoking is an option after initial aging"
        ],
        "tags": ["cheese", "Italian", "pasta filata", "DOP", "aged", "stretched-curd"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === FRESH CHEESES ===
    {
        "id": "ita-burrata-pugliese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Burrata Pugliese (Apulian Burrata)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Fresh cheese from Puglia - mozzarella pouch filled with stracciatella and cream.",
        "description": "Luxurious fresh cheese from Puglia: a mozzarella shell encasing creamy stracciatella (shredded mozzarella curds mixed with cream). When cut, the rich filling oozes out.",
        "servings_yield": "About 1.5 lbs (6-8 burrata)",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "heavy cream", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup cool water. Add to cold milk."},
            {"step": 2, "text": "Heat milk to 90°F (32°C) while stirring gently."},
            {"step": 3, "text": "Add rennet diluted in water. Let set 10 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1-inch cubes. Heat to 105°F (41°C)."},
            {"step": 5, "text": "Drain whey. Heat water to 175°F (80°C)."},
            {"step": 6, "text": "Add curds to hot water. Stretch until smooth and elastic."},
            {"step": 7, "text": "Reserve 1/3 of mozzarella. Shred remainder into thin strands (stracciatella)."},
            {"step": 8, "text": "Mix stracciatella with cream and pinch of salt."},
            {"step": 9, "text": "Form reserved mozzarella into thin pouches. Fill each with stracciatella mixture."},
            {"step": 10, "text": "Pinch pouches closed. Store in salted whey. Eat within 48 hours."}
        ],
        "temperature": "90-175°F (32-80°C)",
        "notes": [
            "Burrata means 'buttered' - referring to the rich filling",
            "Invented in Andria, Puglia in the 1920s",
            "Must be eaten very fresh - within 2 days ideally",
            "Traditionally wrapped in asphodel leaves"
        ],
        "tags": ["cheese", "Italian", "fresh", "Puglia", "pasta filata", "cream"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-stracciatella-filling",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Stracciatella (Burrata Filling)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Creamy filling of shredded mozzarella curds and cream from Puglia.",
        "description": "The luscious filling inside burrata - shredded mozzarella curds soaked in fresh cream. Also served on its own as a luxurious fresh cheese.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 min",
        "cook_time": "1.5 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "fresh mozzarella curds", "quantity": "12", "unit": "oz"},
            {"item": "heavy cream", "quantity": "1/2", "unit": "cup"},
            {"item": "fine sea salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with freshly made mozzarella curds, still warm from stretching."},
            {"step": 2, "text": "Tear or shred the mozzarella into thin, irregular strands while still warm."},
            {"step": 3, "text": "Place strands in a bowl. Add cream and salt."},
            {"step": 4, "text": "Gently mix to coat all strands with cream."},
            {"step": 5, "text": "Let rest 10 minutes for cream to be absorbed."},
            {"step": 6, "text": "Serve immediately or use to fill burrata pouches."},
            {"step": 7, "text": "Store in cream in refrigerator. Best within 24 hours."}
        ],
        "temperature": "Room temperature",
        "notes": [
            "Stracciatella means 'little rags' - describing the shredded texture",
            "The curds must be warm and fresh for proper texture",
            "Can be served alone drizzled with olive oil",
            "The same name as a soup and gelato - different preparations"
        ],
        "tags": ["cheese", "Italian", "fresh", "Puglia", "cream", "stracciatella"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-stracchino-crescenza",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Stracchino (Crescenza)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Ultra-creamy spreading cheese from Lombardy, also called Crescenza.",
        "description": "Extremely soft, spreadable cheese from Northern Italy. Mild, slightly tangy with a creamy, almost liquid texture when ripe. Perfect for focaccia and spreading.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-3 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 100°F (38°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Let rest 15 minutes."},
            {"step": 4, "text": "Gently ladle curds into molds - do NOT press."},
            {"step": 5, "text": "Drain at room temperature 12-24 hours, flipping every 4-6 hours."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Age at 50°F (10°C) for 1-3 weeks until very soft and spreadable."}
        ],
        "temperature": "100°F (38°C)",
        "notes": [
            "Stracchino comes from 'stracco' meaning tired - referring to tired cows returning from Alpine pastures",
            "Crescenza is another name for the same cheese",
            "Should be very soft, almost runny when ripe",
            "Essential for focaccia di Recco"
        ],
        "tags": ["cheese", "Italian", "soft", "Lombardy", "spreading cheese", "fresh"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === PASTA FILATA CHEESES ===
    {
        "id": "ita-caciocavallo-silano",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caciocavallo Silano DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Ancient pasta filata cheese from Southern Italy, DOP since 1996.",
        "description": "Pear-shaped stretched-curd cheese hung to age in pairs. The name means 'cheese on horseback' - tied in pairs that drape over a pole like saddlebags. Mild when young, sharp when aged.",
        "servings_yield": "About 2 lbs (2 small caciocavalli)",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder (optional)", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F (36°C). Add starter and optional lipase, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 115°F (46°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds, let acidify 4-8 hours until pH reaches 5.2."},
            {"step": 6, "text": "Cut curd into strips. Place in 175°F (80°C) water."},
            {"step": 7, "text": "Stretch and knead until very smooth. Form into pear shapes with small knob on top."},
            {"step": 8, "text": "Tie pairs together at the knobs with twine. Cool in cold water."},
            {"step": 9, "text": "Brine 8-12 hours. Hang over pole to age at 55°F (13°C) for 2-12 months."}
        ],
        "temperature": "97-175°F (36-80°C)",
        "notes": [
            "Ancient cheese predating mozzarella by centuries",
            "Traditional to hang in pairs over a pole",
            "Can be smoked after initial aging",
            "Excellent grilled when aged - called Caciocavallo Impiccato"
        ],
        "tags": ["cheese", "Italian", "pasta filata", "Southern Italy", "DOP", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-scamorza-affumicata",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Scamorza Affumicata (Smoked Scamorza)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Smoked pasta filata cheese from Southern Italy.",
        "description": "Stretched-curd cheese shaped like a tied pouch, then smoked over hay or wood. Golden-brown exterior with smoky aroma and firm, slightly chewy texture. Excellent for grilling.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours plus smoking",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tsp"},
            {"item": "wood chips for smoking", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup water. Add to cold milk."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add rennet, let set 5-10 minutes."},
            {"step": 3, "text": "Cut curds and heat to 105°F (41°C)."},
            {"step": 4, "text": "Drain whey. Let curds acidify 2-4 hours."},
            {"step": 5, "text": "Heat water to 175°F (80°C). Stretch curds until smooth."},
            {"step": 6, "text": "Form into pouch shapes, creating a 'neck' by pinching top. Tie with twine."},
            {"step": 7, "text": "Brine 2-4 hours. Air dry 24 hours."},
            {"step": 8, "text": "Cold smoke at 70-90°F (21-32°C) for 4-8 hours until golden."},
            {"step": 9, "text": "Age 2-4 weeks at 55°F (13°C)."}
        ],
        "temperature": "90-175°F (32-80°C)",
        "notes": [
            "Scamorza means 'beheaded' - referring to the pinched neck shape",
            "Traditional smoking uses wheat straw or beechwood",
            "Also available un-smoked (Scamorza Bianca)",
            "Excellent melted on pizza or grilled as an appetizer"
        ],
        "tags": ["cheese", "Italian", "pasta filata", "smoked", "Southern Italy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ALPINE AND SEMI-HARD CHEESES ===
    {
        "id": "ita-fontina-valdaosta",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fontina Val d'Aosta DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP Alpine cheese from the Aosta Valley since the 12th century.",
        "description": "Semi-soft Alpine cheese with earthy, nutty flavor and excellent melting properties. Made from milk of Valdostana cows grazing on Alpine meadows. Essential for fonduta (Italian fondue).",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk (preferably raw)", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F (36°C). Add both starter cultures, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 35-40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 118°F (48°C) over 40 minutes while stirring gently."},
            {"step": 5, "text": "Stir at temperature until curds firm, about 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 7, "text": "Brine for 12 hours."},
            {"step": 8, "text": "Age at 50°F (10°C) and 95% humidity for 3-4 months. Wash and turn every 2-3 days."}
        ],
        "temperature": "97-118°F (36-48°C)",
        "notes": [
            "True Fontina DOP comes only from Val d'Aosta",
            "Mixed cultures create complex flavor",
            "Rind washing develops earthy, mushroomy notes",
            "The foundation of classic Italian fonduta"
        ],
        "tags": ["cheese", "Italian", "semi-soft", "Alpine", "DOP", "fondue", "washed-rind"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-montasio-friulian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Montasio Friulano DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "DOP cheese from Friuli-Venezia Giulia, created by Benedictine monks.",
        "description": "Fruity, nutty cheese from the northeast corner of Italy. Ranges from soft and mild (2 months) to hard and sharp (12+ months). Essential ingredient for frico (crispy cheese wafers).",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-18 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Raise temperature to 95°F (35°C). Add calcium chloride, then rennet."},
            {"step": 3, "text": "Let set 25-30 minutes until firm break. Cut into 1/4-inch cubes."},
            {"step": 4, "text": "Heat slowly to 115°F (46°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Continue stirring until curds are firm, about 20 minutes more."},
            {"step": 6, "text": "Drain and press at 20 lbs for 30 min, flip, 35 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine 24-48 hours depending on size."},
            {"step": 8, "text": "Age at 55°F (13°C): Fresco (2-4 mo), Mezzano (5-10 mo), Stagionato (12+ mo)."}
        ],
        "temperature": "90-115°F (32-46°C)",
        "notes": [
            "Named for Mount Montasio in the Julian Alps",
            "Created by monks at Moggio Abbey around 1200 AD",
            "Essential for frico - crispy cheese wafers from Friuli",
            "Flavor ranges from mild and fruity to sharp and complex"
        ],
        "tags": ["cheese", "Italian", "semi-hard", "Friuli", "DOP", "Alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-toma-piemontese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Toma Piemontese DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Traditional Alpine cheese from the Piedmont region.",
        "description": "Rustic Alpine cheese from Piedmont with buttery, slightly tangy flavor. Semi-soft when young, firmer when aged. The everyday table cheese of the Piedmont mountains.",
        "servings_yield": "About 2 lbs",
        "prep_time": "40 min",
        "cook_time": "2.5 hours",
        "total_time": "1-6 months aging",
        "ingredients": [
            {"item": "whole or part-skim cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat gently to 100°F (38°C) over 20 minutes while stirring."},
            {"step": 5, "text": "Drain and press at 10 lbs for 30 min, flip, 20 lbs for 8 hours."},
            {"step": 6, "text": "Salt by rubbing surfaces or brief brining."},
            {"step": 7, "text": "Age at 55°F (13°C) for 1-6 months. Turn weekly."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Toma is a generic term for wheel-shaped Alpine cheeses",
            "Part-skim version is traditional for longer aging",
            "Rind may be rubbed with olive oil or tomato paste",
            "Each valley has its own variation"
        ],
        "tags": ["cheese", "Italian", "semi-soft", "Piedmont", "DOP", "Alpine", "table cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-bitto-storico",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bitto Storico (Historic Bitto)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Ancient Alpine cheese from the Bitto Valley in Lombardy, unchanged for centuries.",
        "description": "Rare Alpine cheese made only during summer in high mountain pastures. Mixed cow and goat milk creates complex, grassy flavors. Can be aged up to 10 years.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "70 days to 10 years aging",
        "ingredients": [
            {"item": "raw cow's milk (just milked)", "quantity": "2.5", "unit": "gallons"},
            {"item": "raw goat's milk", "quantity": "0.5", "unit": "gallon"},
            {"item": "natural whey starter (from previous batch)", "quantity": "1", "unit": "cup"},
            {"item": "traditional calf rennet paste", "quantity": "1/2", "unit": "tsp"},
            {"item": "coarse salt", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh milk immediately after milking, still warm at body temperature."},
            {"step": 2, "text": "Combine cow's and goat's milk. Add natural whey starter."},
            {"step": 3, "text": "Add rennet. Let set 30-40 minutes at 95-100°F (35-38°C)."},
            {"step": 4, "text": "Break curds into rice-sized pieces using traditional spino tool."},
            {"step": 5, "text": "Heat to 120-125°F (49-52°C) over 30 minutes while stirring constantly."},
            {"step": 6, "text": "Let curds settle. Collect in linen cloth."},
            {"step": 7, "text": "Press under increasing weight for 24 hours, flipping frequently."},
            {"step": 8, "text": "Dry salt the surface daily for one week."},
            {"step": 9, "text": "Age minimum 70 days, traditionally in stone caves. Can age 10+ years."}
        ],
        "temperature": "95-125°F (35-52°C)",
        "notes": [
            "True Bitto Storico made only in summer on mountain pastures",
            "Goat's milk percentage traditionally 10-20%",
            "Must be made within 30 minutes of milking",
            "Among the longest-aged cheeses in the world"
        ],
        "tags": ["cheese", "Italian", "Alpine", "Lombardy", "raw milk", "mixed milk", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SOFT AND SEMI-SOFT CHEESES ===
    {
        "id": "ita-robiola-piemonte",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Robiola Piemontese",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Soft, creamy cheese from Piedmont, traditionally mixed milk.",
        "description": "Delicate, creamy cheese from Piedmont made from cow, sheep, and/or goat milk. Bloomy white rind develops with aging. Spreadable when young, runny when ripe.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "goat's milk (optional, for mixed milk version)", "quantity": "1", "unit": "quart"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks if using mixed version. Heat to 72°F (22°C) - barely warm."},
            {"step": 2, "text": "Add starter and P. candidum. Ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride, then just 2 drops rennet. Stir gently."},
            {"step": 4, "text": "Cover and let set at room temperature 18-24 hours until thick curd forms."},
            {"step": 5, "text": "Gently ladle curds into small molds. Do not press."},
            {"step": 6, "text": "Drain at room temperature 24-48 hours, flipping daily."},
            {"step": 7, "text": "Salt surfaces. Age at 50-55°F (10-13°C) and 90% humidity for 1-4 weeks."},
            {"step": 8, "text": "White mold will develop on surface. Ready when soft throughout."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Traditional Robiola varies by specific valley and maker",
            "Very little rennet - mostly acid-set cheese",
            "Robiola di Roccaverano DOP is famous goat's milk version",
            "Name may derive from Latin 'ruber' (red) or 'robur' (strength)"
        ],
        "tags": ["cheese", "Italian", "soft", "Piedmont", "bloomy-rind", "spreadable"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-caciotta-alle-erbe",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caciotta alle Erbe (Herbed Caciotta)",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Rustic Italian farmhouse cheese flavored with herbs.",
        "description": "Small, mild farmhouse cheese infused with Italian herbs. Caciotta is a generic term for small wheel cheeses made throughout central Italy, often flavored with local herbs.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "35 min",
        "cook_time": "2 hours",
        "total_time": "2-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1.5", "unit": "gallons"},
            {"item": "sheep's milk (optional)", "quantity": "0.5", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "mixed Italian herbs (rosemary, thyme, oregano)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks if using mixed version. Heat to 90°F (32°C)."},
            {"step": 2, "text": "Add starter, ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 40-45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Heat gently to 100°F (38°C) over 20 minutes while stirring."},
            {"step": 6, "text": "Add chopped herbs to curds, mix gently."},
            {"step": 7, "text": "Drain and press at 10 lbs for 30 min, flip, 15 lbs for 4-6 hours."},
            {"step": 8, "text": "Salt surfaces or brine briefly."},
            {"step": 9, "text": "Age at 55°F (13°C) for 2-8 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Caciotta means 'little cheese' - typically small wheels",
            "Every region has its own version and herb combinations",
            "Tuscany is particularly known for herbed caciotta",
            "Can also be flavored with truffles, peppercorns, or chiles"
        ],
        "tags": ["cheese", "Italian", "semi-soft", "herbed", "farmhouse", "Tuscany"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === BLUE AND BLUE-VEINED CHEESES ===
    {
        "id": "ita-castelmagno-alpeggio",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Castelmagno d'Alpeggio DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Rare blue-veined cheese from mountain pastures in Piedmont.",
        "description": "Ancient crumbly cheese from Piedmont with subtle blue veining. Made in summer Alpine pastures, it develops complex, slightly spicy flavor with blue mold. Among Italy's most prized cheeses.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2.5", "unit": "gallons"},
            {"item": "sheep's milk (optional, traditional)", "quantity": "0.5", "unit": "gallon"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti (develops naturally in caves)", "quantity": "1/16", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "coarse salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter (and P. roqueforti if not relying on natural molds), ripen 30 minutes."},
            {"step": 2, "text": "Add rennet, let set 45-60 minutes until very firm curd."},
            {"step": 3, "text": "Break curds into irregular pieces. Let drain in cloth 12-24 hours."},
            {"step": 4, "text": "Break drained curd again. Mix with fresh curds from a second batch (traditional method)."},
            {"step": 5, "text": "Press mixture into molds at 15 lbs for 12 hours."},
            {"step": 6, "text": "Salt surfaces. Age in natural cave at 50°F (10°C) and high humidity."},
            {"step": 7, "text": "Blue mold develops naturally in cracks. Pierce if needed to encourage veining."},
            {"step": 8, "text": "Age 2-6 months. Older wheels develop more blue and crumbly texture."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "One of Italy's oldest cheeses, documented since 1277",
            "Traditional production mixes curds from two milkings",
            "Blue mold develops naturally in aging caves",
            "Best Castelmagno comes from summer Alpine pastures (Alpeggio)"
        ],
        "tags": ["cheese", "Italian", "blue cheese", "Piedmont", "DOP", "Alpine", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SARDINIAN AND SICILIAN CHEESES ===
    {
        "id": "ita-fiore-sardo-dop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fiore Sardo DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Ancient Sardinian sheep's milk cheese, the original Pecorino.",
        "description": "Raw sheep's milk cheese from Sardinia, smoked over aromatic woods and aged 3-12 months. Sharp, complex flavor with smoky undertones. Sardinia's original cheese, predating Pecorino Romano.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours plus smoking",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "traditional lamb rennet paste", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "aromatic wood for smoking (oak, myrtle, or arbutus)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw sheep's milk to 95°F (35°C) - no starter culture traditionally used."},
            {"step": 2, "text": "Add lamb rennet paste. Let set 40-60 minutes until firm break."},
            {"step": 3, "text": "Break curds by hand into walnut-sized pieces."},
            {"step": 4, "text": "Heat slowly to 104°F (40°C) while stirring gently."},
            {"step": 5, "text": "Drain and press into molds by hand, forming wheel shape."},
            {"step": 6, "text": "Press lightly for 6-8 hours, turning frequently."},
            {"step": 7, "text": "Brine for 48 hours. Air dry 24 hours."},
            {"step": 8, "text": "Cold smoke over aromatic woods for 10-15 days, several hours per day."},
            {"step": 9, "text": "Age at 55°F (13°C) for 3-12 months. Rub with olive oil or sheep fat monthly."}
        ],
        "temperature": "95-104°F (35-40°C)",
        "notes": [
            "Fiore means 'flower' - from the thistle flower used in traditional rennet",
            "Sardinia's original cheese, made for millennia by shepherds",
            "Smoking was originally done in shepherd huts over cooking fires",
            "Young Fiore Sardo is table cheese; aged is for grating"
        ],
        "tags": ["cheese", "Italian", "sheep's milk", "Sardinia", "DOP", "smoked", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ita-ragusano-dop",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ragusano DOP",
        "category": "cheese",
        "attribution": "Traditional Italian cheese",
        "source_note": "Ancient Sicilian pasta filata cheese, block-shaped and rope-aged.",
        "description": "Stretched-curd cheese from the Ragusa province of Sicily. Distinctive rectangular block shape, hung by ropes to age. Sweet and delicate when young, sharp and complex when aged.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "raw cow's milk (Modicana breed preferred)", "quantity": "3", "unit": "gallons"},
            {"item": "natural whey starter", "quantity": "1/2", "unit": "cup"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp"},
            {"item": "coarse sea salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 95°F (35°C). Add whey starter, ripen 30 minutes."},
            {"step": 2, "text": "Add lamb rennet paste. Let set 60-90 minutes until very firm."},
            {"step": 3, "text": "Break curds into small pieces. Let mature in warm whey 4-8 hours."},
            {"step": 4, "text": "When curd stretches smoothly, cut into strips."},
            {"step": 5, "text": "Place strips in 175°F (80°C) water. Stretch and knead extensively."},
            {"step": 6, "text": "Form into rectangular block shape, traditional for Ragusano."},
            {"step": 7, "text": "Brine for 24-48 hours."},
            {"step": 8, "text": "Tie with rope and hang to age at 55-60°F (13-16°C) for 3-12 months."},
            {"step": 9, "text": "Rub surface with olive oil and tomato paste mixture periodically."}
        ],
        "temperature": "95-175°F (35-80°C)",
        "notes": [
            "Traditional shape is a rectangular block (parallelepipedo)",
            "Modicana breed cows give distinctive flavor",
            "Surface is rubbed with olive oil and tomato paste",
            "Block shape allowed easy transport on donkeys"
        ],
        "tags": ["cheese", "Italian", "pasta filata", "Sicily", "DOP", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Italian cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in ITALIAN_CHEESE_RECIPES:
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
