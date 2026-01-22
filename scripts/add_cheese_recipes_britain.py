#!/usr/bin/env python3
"""Add comprehensive British cheese recipes to the cheese category."""

import json

BRITISH_CHEESE_RECIPES = [
    # === CLASSIC BRITISH TERRITORIAL CHEESES ===
    {
        "id": "british-stilton-blue-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Stilton Blue (King of English Cheeses)",
        "category": "cheese",
        "attribution": "Traditional English blue cheese",
        "source_note": "PDO protected - can only be made in Derbyshire, Leicestershire, or Nottinghamshire.",
        "description": "The 'King of English Cheeses' - a rich, creamy blue with characteristic veining. Dating to the 18th century, Stilton has a crumbly yet creamy texture and complex flavor that pairs perfectly with Port wine.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "9-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and P. roqueforti, ripen 90 minutes for good acid development."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes until very soft curd forms."},
            {"step": 3, "text": "Cut curds into 1-inch cubes very gently. Let rest 15 minutes."},
            {"step": 4, "text": "Ladle curds carefully into a colander lined with cheesecloth. Do NOT stir or break curds."},
            {"step": 5, "text": "Drain for 24 hours at room temperature, turning the mass gently every few hours."},
            {"step": 6, "text": "Break drained curd into walnut-sized pieces. Mix in salt thoroughly."},
            {"step": 7, "text": "Pack loosely into tall cylindrical Stilton molds - never press. The open texture is essential."},
            {"step": 8, "text": "Turn daily for 5-7 days until cheese firms enough to unmold."},
            {"step": 9, "text": "Age at 50-55°F (10-13°C) and 85-90% humidity. Rub exterior daily to smooth the rind."},
            {"step": 10, "text": "At 5-6 weeks, pierce with stainless steel needles in a grid pattern to allow oxygen for blue development."},
            {"step": 11, "text": "Continue aging until 9-12 weeks. Blue veins should be well-developed throughout."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Never press Stilton - the open texture is essential for blue mold development",
            "Named after the village where it was sold, not where it was made",
            "Traditional Christmas cheese in England, paired with Port",
            "The brown crusty rind is natural but not typically eaten"
        ],
        "tags": ["cheese", "British", "English", "blue cheese", "Stilton", "PDO", "Christmas"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-red-leicester-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Red Leicester (Leicestershire Cheese)",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "From Leicestershire, England. The deep orange-red color comes from annatto.",
        "description": "Distinctive English cheese with deep russet color, mellow nutty flavor, and slightly crumbly texture. Milder and moister than Cheddar, it's excellent for both eating and melting.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "annatto coloring", "quantity": "3/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto and stir well to distribute color evenly."},
            {"step": 2, "text": "Add starter culture, ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 94°F (34°C) over 40 minutes while stirring gently."},
            {"step": 6, "text": "Maintain temperature and stir until curds shrink and firm, about 30 minutes more."},
            {"step": 7, "text": "Drain whey. Mill curds into larger pieces than Cheddar (walnut-sized)."},
            {"step": 8, "text": "Add salt and mix thoroughly."},
            {"step": 9, "text": "Press at 20 lbs for 1 hour, flip, then 40 lbs for 12-24 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) and 80% humidity for 3-6 months. Traditional cloth-binding optional."}
        ],
        "temperature": "86-94°F (30-34°C)",
        "notes": [
            "The deep red-orange color is distinctive - more annatto than other colored cheeses",
            "Milled into larger pieces than Cheddar for slightly more open texture",
            "Flaky texture makes it excellent for crumbling",
            "Pairs well with crusty bread, apples, and English ales"
        ],
        "tags": ["cheese", "British", "English", "Leicester", "colored", "territorial"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-double-gloucester-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Double Gloucester (Gloucestershire Cheese)",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "From Gloucestershire. 'Double' refers to using full-cream milk from two milkings.",
        "description": "Rich, buttery English cheese with smooth, close texture and deep golden-orange color. Milder than Cheddar with a creamy, mellow flavor. Famous for the Cooper's Hill cheese rolling event.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "annatto coloring", "quantity": "1/2", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto and stir thoroughly."},
            {"step": 2, "text": "Add starter culture, ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 100°F (38°C) over 40 minutes while stirring gently."},
            {"step": 6, "text": "Continue stirring at temperature until curds are firm, about 30 minutes."},
            {"step": 7, "text": "Drain whey. Let curds mat for 15 minutes."},
            {"step": 8, "text": "Cut curd mass into blocks, stack and turn (cheddaring) for 1 hour until smooth."},
            {"step": 9, "text": "Mill into small pieces, add salt, mix well."},
            {"step": 10, "text": "Press at 20 lbs for 1 hour, flip, 40 lbs for 24 hours."},
            {"step": 11, "text": "Age at 55°F (13°C) for 3-4 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "'Double' refers to using whole milk from two milkings, not skim from one",
            "Single Gloucester uses part-skim milk and ages less",
            "Famous for the annual cheese rolling race at Cooper's Hill",
            "Smooth, close texture with no holes - unlike Cheddar"
        ],
        "tags": ["cheese", "British", "English", "Gloucester", "territorial", "cheddaring"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-cheshire-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheshire Cheese (England's Oldest)",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "Possibly the oldest named British cheese, with references dating to Roman times.",
        "description": "England's oldest named cheese - crumbly, salty, and tangy with a distinctive dense texture. The salty soil of Cheshire gives the milk (and cheese) unique mineral character.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "annatto coloring (for Red Cheshire)", "quantity": "1/8", "unit": "tsp", "prep_note": "optional"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto if making Red Cheshire."},
            {"step": 2, "text": "Add starter, ripen 60 minutes - longer than most cheeses for acid development."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 94°F (34°C) over 40 minutes while stirring."},
            {"step": 6, "text": "Continue stirring until curds are quite firm, about 45 minutes."},
            {"step": 7, "text": "Drain whey completely. Mill curds into small pieces."},
            {"step": 8, "text": "Add salt - Cheshire uses more salt than most English cheeses."},
            {"step": 9, "text": "Press at 15 lbs for 30 min, flip, 30 lbs for 24 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) for 2-6 months. Young Cheshire is mild; aged is sharp."}
        ],
        "temperature": "86-94°F (30-34°C)",
        "notes": [
            "Cheshire salt deposits give the milk unique minerality",
            "Crumblier than Cheddar due to higher acid and different curd handling",
            "Red Cheshire uses annatto; White Cheshire is natural color; Blue Cheshire has mold",
            "Higher salt content contributes to characteristic tang"
        ],
        "tags": ["cheese", "British", "English", "Cheshire", "territorial", "ancient", "crumbly"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-lancashire-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lancashire Cheese (Two-Day Curd)",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "Unique method combining curds from multiple days of cheesemaking.",
        "description": "Traditional English white cheese with buttery, slightly tangy flavor and unique open texture. The two-day curd method creates its characteristic crumbly-yet-creamy texture, perfect for toasting.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min over 2 days",
        "cook_time": "3 hours per day",
        "total_time": "4-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "per day, 2 days"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "per batch"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "per batch"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "per batch"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Heat milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Slowly stir while maintaining 86°F for 45 minutes."},
            {"step": 4, "text": "Drain curds and refrigerate overnight."},
            {"step": 5, "text": "DAY 2: Repeat steps 1-4 with fresh milk."},
            {"step": 6, "text": "Combine Day 1 and Day 2 curds. Break into small pieces and mix thoroughly."},
            {"step": 7, "text": "Add salt and mix well."},
            {"step": 8, "text": "Pack into mold and press lightly - 10 lbs for 30 min, flip, 20 lbs for 12 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) for 4-12 weeks. Creamy Lancashire is younger; Tasty Lancashire is aged longer."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Traditional Lancashire combines curds from 2-3 days of cheesemaking",
            "This multi-day method creates unique open, buttery texture",
            "Excellent melting cheese - perfect for Welsh rarebit",
            "Creamy Lancashire: 4-12 weeks. Tasty Lancashire: 4-24 months"
        ],
        "tags": ["cheese", "British", "English", "Lancashire", "territorial", "two-day curd", "melting"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-sage-derby-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sage Derby (Herbed Derby Cheese)",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "From Derbyshire, traditionally made for Christmas and harvest festivals.",
        "description": "Festive English cheese marbled with green sage, traditionally served at Christmas. The mild Derby base pairs beautifully with the aromatic herb, creating a striking appearance and herbal flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "fresh sage leaves", "quantity": "1/2", "unit": "cup", "prep_note": "chopped fine"},
            {"item": "fresh spinach", "quantity": "1/2", "unit": "cup", "prep_note": "for color"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Blanch sage and spinach briefly, then blend to a smooth paste. Strain through cheesecloth to extract green juice."},
            {"step": 2, "text": "Heat milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 95°F (35°C) over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at temperature until curds firm, about 30 minutes."},
            {"step": 7, "text": "Drain curds. Divide into two portions."},
            {"step": 8, "text": "Mix green sage juice into one portion of curds."},
            {"step": 9, "text": "Layer green and white curds alternately in mold for marbled effect."},
            {"step": 10, "text": "Press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 11, "text": "Age at 55°F (13°C) for 6-8 weeks."}
        ],
        "temperature": "86-95°F (30-35°C)",
        "notes": [
            "Traditional Sage Derby was made for harvest festivals and Christmas",
            "Spinach intensifies the green color - sage alone gives subtle green",
            "The marbling pattern varies depending on how curds are layered",
            "Derby base is mild and buttery, letting sage flavor shine"
        ],
        "tags": ["cheese", "British", "English", "Derby", "herbed", "Christmas", "marbled"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-cornish-yarg-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cornish Yarg (Nettle-Wrapped Cheese)",
        "category": "cheese",
        "attribution": "Traditional Cornish cheese",
        "source_note": "Revived 1980s recipe. 'Yarg' is the makers' name (Gray) spelled backwards.",
        "description": "Unique Cornish cheese wrapped in stinging nettle leaves, creating a distinctive appearance and subtle earthy flavor. The nettle rind allows the cheese to breathe while adding mushroomy notes.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "stinging nettle leaves", "quantity": "30-40", "unit": "leaves", "prep_note": "blanched, dried"}
        ],
        "instructions": [
            {"step": 1, "text": "Blanch nettle leaves briefly to remove sting. Pat dry and set aside."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 98°F (37°C) over 30 minutes while stirring gently."},
            {"step": 6, "text": "Continue stirring until curds firm, about 30 minutes."},
            {"step": 7, "text": "Drain and salt curds."},
            {"step": 8, "text": "Press at 10 lbs for 30 min, flip, 20 lbs for 8-12 hours."},
            {"step": 9, "text": "When cheese is firm, carefully press blanched nettle leaves onto entire surface, overlapping slightly."},
            {"step": 10, "text": "Age at 50-55°F (10-13°C) and 90% humidity for 4-6 weeks. The nettles will turn darker as cheese ages."}
        ],
        "temperature": "90-98°F (32-37°C)",
        "notes": [
            "'Yarg' is 'Gray' spelled backwards - the family who revived the recipe",
            "Wild garlic leaves can substitute for nettle for 'Wild Garlic Yarg' variant",
            "The nettle coating allows cheese to breathe and adds earthy, mushroomy notes",
            "Blanching removes the sting from nettles"
        ],
        "tags": ["cheese", "British", "English", "Cornish", "nettle-wrapped", "leaf-wrapped"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-stinking-bishop-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Stinking Bishop (Perry-Washed Cheese)",
        "category": "cheese",
        "attribution": "Gloucestershire washed-rind cheese",
        "source_note": "Named after the Stinking Bishop pear variety used to wash the rind.",
        "description": "Pungent, soft washed-rind cheese from Gloucestershire. Despite its powerful aroma, the flavor is surprisingly mild and creamy. Famous from Wallace and Gromit's 'Curse of the Were-Rabbit.'",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "perry (pear cider)", "quantity": "1", "unit": "cup", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 20 minutes, maintaining 90°F."},
            {"step": 5, "text": "Ladle curds into molds without pressing. Drain 12-24 hours, flipping frequently."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity. Wash rind with perry every 2-3 days."},
            {"step": 8, "text": "Continue washing and aging for 6-8 weeks. Rind will become orange and pungent."},
            {"step": 9, "text": "Cheese is ready when very soft and rind is sticky orange."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Named after the Stinking Bishop pear variety, not the cheese's aroma",
            "The smell is much stronger than the taste",
            "Featured in Wallace and Gromit: The Curse of the Were-Rabbit",
            "Perry (pear cider) is essential for authentic flavor - apple cider can substitute"
        ],
        "tags": ["cheese", "British", "English", "Gloucestershire", "washed-rind", "pungent", "soft"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-shropshire-blue-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Shropshire Blue (Orange Blue Cheese)",
        "category": "cheese",
        "attribution": "British blue cheese",
        "source_note": "Despite the name, invented in Scotland in 1970s. Orange-colored blue cheese.",
        "description": "Striking orange-colored blue cheese similar to Stilton. The deep orange from annatto contrasts beautifully with blue veining. Creamier and slightly sharper than Stilton.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "10-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/4", "unit": "tsp"},
            {"item": "annatto coloring", "quantity": "1", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add annatto and stir well for even color."},
            {"step": 2, "text": "Add starter and P. roqueforti, ripen 90 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 90 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes. Let rest 15 minutes."},
            {"step": 5, "text": "Ladle curds into colander. Drain 24 hours at room temperature, turning occasionally."},
            {"step": 6, "text": "Break curd into pieces, mix in salt."},
            {"step": 7, "text": "Pack loosely into tall cylindrical molds. Do not press."},
            {"step": 8, "text": "Turn daily for 5-7 days until firm enough to unmold."},
            {"step": 9, "text": "Age at 50-55°F (10-13°C) and 90% humidity. At 6 weeks, pierce with needles for blue development."},
            {"step": 10, "text": "Continue aging to 10-12 weeks total."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Invented in Scotland in 1970s, now made in England despite the name",
            "The orange-and-blue combination is visually striking",
            "Similar process to Stilton but with annatto coloring",
            "Slightly creamier and sharper than traditional Stilton"
        ],
        "tags": ["cheese", "British", "English", "blue cheese", "colored", "Stilton-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-colston-bassett-stilton",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Colston Bassett Stilton (Artisan Style)",
        "category": "cheese",
        "attribution": "Nottinghamshire artisan Stilton",
        "source_note": "Based on methods of the renowned Colston Bassett Dairy, est. 1913.",
        "description": "Premium artisan-style Stilton following the methods of the famous Colston Bassett Dairy. Hand-ladled curds and traditional techniques create an exceptionally creamy, rich blue.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "12-16 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for extra richness"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "3.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 86°F (30°C)."},
            {"step": 2, "text": "Add starter and P. roqueforti, ripen 2 hours for excellent acid development."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 2 hours until very soft curd."},
            {"step": 4, "text": "Hand-ladle curds very gently into colander. This preserves curd structure for creamier texture."},
            {"step": 5, "text": "Drain 24-36 hours at room temperature, turning gently every few hours."},
            {"step": 6, "text": "Break curd by hand into walnut-sized pieces. Mix in salt by hand."},
            {"step": 7, "text": "Hand-pack loosely into tall Stilton molds. Never press."},
            {"step": 8, "text": "Turn daily for 7 days. Smooth exterior with hands while turning."},
            {"step": 9, "text": "Age at 50-52°F (10-11°C) and 90% humidity. Lower temp than standard Stilton for slower development."},
            {"step": 10, "text": "Pierce at 7-8 weeks with stainless needles."},
            {"step": 11, "text": "Continue aging to 12-16 weeks for premium quality."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Colston Bassett is considered one of the finest Stilton producers",
            "Hand-ladling rather than cutting curds creates exceptional creaminess",
            "Longer aging develops more complex flavors",
            "The cream addition creates an extra-rich paste"
        ],
        "tags": ["cheese", "British", "English", "Stilton", "artisan", "blue cheese", "premium"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-montgomerys-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Montgomery's Cheddar (Clothbound Artisan)",
        "category": "cheese",
        "attribution": "Somerset artisan Cheddar",
        "source_note": "Based on methods of Montgomery's, one of only three remaining clothbound Cheddar makers in Somerset.",
        "description": "Traditional clothbound Somerset Cheddar in the style of Montgomery's - one of Britain's finest. Raw milk, animal rennet, and cloth binding create complex, earthy, intensely savory cheese.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1 hour",
        "cook_time": "5 hours",
        "total_time": "12-18 months aging",
        "ingredients": [
            {"item": "raw whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "animal rennet (traditional)", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"},
            {"item": "lard", "quantity": "1/4", "unit": "cup", "prep_note": "for cloth binding"},
            {"item": "cheesecloth/muslin", "quantity": "1", "unit": "yard"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 86°F (30°C). Add starter, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then animal rennet. Let set 45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 40 minutes while stirring ('scalding')."},
            {"step": 5, "text": "Continue stirring until curds are very firm and squeak, about 45 minutes more."},
            {"step": 6, "text": "Drain whey. Let curd mat for 15 minutes."},
            {"step": 7, "text": "Cut mat into blocks. Stack and turn blocks repeatedly (cheddaring) for 2 hours until slabs are smooth, shiny, and chicken-breast textured."},
            {"step": 8, "text": "Mill into finger-sized pieces. Add salt and mix thoroughly."},
            {"step": 9, "text": "Press at 20 lbs for 1 hour, flip, 40 lbs for 24 hours, flip, 50 lbs for 24 more hours."},
            {"step": 10, "text": "Rub exterior with lard and wrap in muslin cloth, pressing cloth firmly to cheese."},
            {"step": 11, "text": "Age at 55°F (13°C) and 85% humidity for 12-18 months. Turn weekly and brush off any mold."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Only three farms still make traditional clothbound Cheddar in Somerset",
            "Cloth binding allows the cheese to breathe and develop complex rind",
            "Raw milk and animal rennet are traditional for this style",
            "Extended aging develops intense, savory, earthy flavors"
        ],
        "tags": ["cheese", "British", "English", "Cheddar", "clothbound", "artisan", "Somerset", "raw milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-kirkhams-lancashire",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kirkham's Lancashire (Raw Milk Artisan)",
        "category": "cheese",
        "attribution": "Lancashire artisan cheese",
        "source_note": "Based on methods of Kirkham's, the last farmhouse Lancashire maker using raw milk and butter muslin.",
        "description": "Traditional raw milk Lancashire in the style of Kirkham's - the last remaining farmhouse maker. Three-day curd method, butter muslin wrapping, and raw milk create extraordinary depth and buttery richness.",
        "servings_yield": "About 3 lbs",
        "prep_time": "45 min over 3 days",
        "cook_time": "3 hours per day",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "raw whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "per day, 3 days"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "per batch"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "per batch"},
            {"item": "animal rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "per batch"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"},
            {"item": "butter", "quantity": "2", "unit": "tbsp", "prep_note": "softened, for cloth"},
            {"item": "butter muslin", "quantity": "1", "unit": "yard"}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Heat raw milk to 86°F (30°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Stir gently at 86°F for 45 minutes."},
            {"step": 4, "text": "Drain curds and refrigerate."},
            {"step": 5, "text": "DAYS 2 and 3: Repeat steps 1-4 with fresh milk each day."},
            {"step": 6, "text": "Combine all three days' curds. Break into small pieces and mix thoroughly."},
            {"step": 7, "text": "Add salt and mix well - the three different stages of curd create unique texture."},
            {"step": 8, "text": "Line mold with butter-rubbed muslin. Pack in curds."},
            {"step": 9, "text": "Press lightly - 10 lbs for 30 min, flip, 20 lbs for 24 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) and 85% humidity for 2-6 months. Turn and re-butter cloth weekly."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Kirkham's is the last farmhouse Lancashire using raw milk and butter muslin",
            "Three-day curd method creates unique lactic complexity",
            "Butter muslin gives characteristic wrinkled rind",
            "Young Lancashire is creamy; aged 'Tasty' Lancashire is more crumbly"
        ],
        "tags": ["cheese", "British", "English", "Lancashire", "artisan", "raw milk", "three-day curd"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-stichelton-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Stichelton (Raw Milk Blue)",
        "category": "cheese",
        "attribution": "Nottinghamshire raw milk blue",
        "source_note": "Stilton-style made with raw milk. 'Stichelton' is the medieval name for Stilton.",
        "description": "Raw milk blue cheese made in the Stilton style but legally distinct (PDO Stilton requires pasteurization). Exceptionally creamy and complex with sweet, savory, and spicy notes. Uses the medieval spelling 'Stichelton.'",
        "servings_yield": "About 4 lbs",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "12-16 weeks aging",
        "ingredients": [
            {"item": "raw whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/4", "unit": "tsp"},
            {"item": "animal rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "3.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 86°F (30°C). Add starter and P. roqueforti, ripen 90 minutes."},
            {"step": 2, "text": "Add animal rennet. Let set 90-120 minutes until very soft curd."},
            {"step": 3, "text": "Hand-ladle curds very gently into colander - preserve curd structure."},
            {"step": 4, "text": "Drain 24-36 hours at room temperature, turning gently every few hours."},
            {"step": 5, "text": "Break curd by hand into walnut-sized pieces."},
            {"step": 6, "text": "Mix in salt by hand - raw milk cheeses need careful salting."},
            {"step": 7, "text": "Pack loosely into tall cylindrical molds. Never press."},
            {"step": 8, "text": "Turn daily for 7-10 days until firm."},
            {"step": 9, "text": "Age at 50-52°F (10-11°C) and 90% humidity."},
            {"step": 10, "text": "Pierce at 8 weeks for blue development."},
            {"step": 11, "text": "Continue aging to 12-16 weeks. Raw milk creates exceptional complexity."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Cannot legally be called 'Stilton' because PDO requires pasteurized milk",
            "'Stichelton' is the medieval name for Stilton village",
            "Raw milk creates more complex, nuanced flavor than pasteurized",
            "Hand-ladling preserves curd structure for creamier texture"
        ],
        "tags": ["cheese", "British", "English", "blue cheese", "raw milk", "Stilton-style", "artisan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-dunlop-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Dunlop (Scottish Cheddar)",
        "category": "cheese",
        "attribution": "Traditional Scottish cheese",
        "source_note": "From Dunlop, Ayrshire, Scotland. The original Scottish Cheddar.",
        "description": "Scotland's answer to Cheddar - milder and moister with a nutty, buttery flavor. Named after the village of Dunlop in Ayrshire where it originated in the 17th century.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 95°F (35°C) - lower than English Cheddar - over 30 minutes."},
            {"step": 5, "text": "Continue stirring until curds firm, about 30 minutes more."},
            {"step": 6, "text": "Drain whey. Let curd mat briefly."},
            {"step": 7, "text": "Cheddar lightly - less than English Cheddar for moister texture."},
            {"step": 8, "text": "Mill and salt."},
            {"step": 9, "text": "Press at 20 lbs for 1 hour, flip, 40 lbs for 12-24 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) for 2-6 months."}
        ],
        "temperature": "86-95°F (30-35°C)",
        "notes": [
            "Originated in 17th century Ayrshire, Scotland",
            "Lower scalding temperature than English Cheddar creates moister cheese",
            "Less cheddaring gives milder, sweeter flavor",
            "Traditional Scottish cheese experiencing a revival"
        ],
        "tags": ["cheese", "British", "Scottish", "Cheddar-style", "Ayrshire", "mild"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-crowdie-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crowdie (Scottish Fresh Cheese)",
        "category": "cheese",
        "attribution": "Traditional Scottish Highland cheese",
        "source_note": "Ancient Highland cheese, simple acid-set fresh cheese.",
        "description": "Scotland's oldest cheese - a simple, tangy fresh cheese made by Highland crofters for centuries. Light and crumbly with a fresh, lemony flavor. The foundation of many Scottish dishes.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "heavy cream (optional)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C) - barely above room temperature."},
            {"step": 2, "text": "Add buttermilk and stir gently. Cover and leave at room temperature 24-48 hours until thickly clabbered."},
            {"step": 3, "text": "Gently heat the clabbered milk to 100°F (38°C) to encourage curd separation. Do not stir."},
            {"step": 4, "text": "Line a colander with cheesecloth. Gently ladle curds into cloth."},
            {"step": 5, "text": "Drain 2-4 hours until desired consistency."},
            {"step": 6, "text": "Transfer to bowl. Add salt and mix gently."},
            {"step": 7, "text": "For richer Crowdie, fold in cream."},
            {"step": 8, "text": "Refrigerate and use within 5-7 days."}
        ],
        "temperature": "72-100°F (22-38°C)",
        "notes": [
            "One of the simplest and oldest cheeses - no rennet needed",
            "Highland crofters made this from whatever milk was available",
            "Traditional on oatcakes or in Cranachan dessert",
            "Similar to fromage blanc or quark"
        ],
        "tags": ["cheese", "British", "Scottish", "Highland", "fresh cheese", "acid-set", "simple"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-caboc-classic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caboc (Oatmeal-Rolled Scottish Cream Cheese)",
        "category": "cheese",
        "attribution": "Traditional Scottish Highland cheese",
        "source_note": "Ancient Highland chieftain's cheese, rolled in toasted oatmeal.",
        "description": "Scotland's oldest 'cream cheese' - rich double-cream cheese rolled in toasted pinhead oatmeal. Legend says the recipe was created for a Highland chieftain's daughter in the 15th century.",
        "servings_yield": "About 12 oz",
        "prep_time": "20 min",
        "cook_time": "30 min",
        "total_time": "24-36 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups"},
            {"item": "whole milk", "quantity": "1", "unit": "cup"},
            {"item": "buttermilk", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"},
            {"item": "pinhead oatmeal", "quantity": "1/2", "unit": "cup", "prep_note": "toasted"}
        ],
        "instructions": [
            {"step": 1, "text": "Toast pinhead oatmeal in dry pan until golden and fragrant. Set aside to cool."},
            {"step": 2, "text": "Combine cream, milk, and buttermilk. Heat to 75°F (24°C)."},
            {"step": 3, "text": "Cover and leave at room temperature 24-36 hours until thickened."},
            {"step": 4, "text": "Line a sieve with cheesecloth. Pour in thickened cream mixture."},
            {"step": 5, "text": "Drain 6-12 hours until thick and spreadable."},
            {"step": 6, "text": "Transfer to bowl. Mix in salt."},
            {"step": 7, "text": "Form into a log or round shape."},
            {"step": 8, "text": "Roll completely in toasted oatmeal, pressing gently to adhere."},
            {"step": 9, "text": "Wrap in parchment and refrigerate. Best within 1-2 weeks."}
        ],
        "temperature": "75°F (24°C)",
        "notes": [
            "Reputedly created in 15th century for a Highland chieftain's daughter",
            "The oatmeal coating is traditional and adds nutty flavor",
            "Very rich - serve small portions with oatcakes",
            "Can be shaped into logs, rounds, or small drums"
        ],
        "tags": ["cheese", "British", "Scottish", "Highland", "cream cheese", "oatmeal", "double-cream"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ADDITIONAL BRITISH REGIONAL CHEESES ===
    {
        "id": "british-white-stilton",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "White Stilton",
        "category": "cheese",
        "attribution": "Traditional English cheese",
        "source_note": "Stilton without the blue mold - fresh, crumbly, and mild.",
        "description": "The non-blue version of Stilton - fresh, crumbly, and mildly tangy. Often used as a base for fruit-flavored varieties. PDO protected like its blue cousin.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter only (no blue mold), ripen 60 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Ladle curds into colander. Drain 24 hours, turning occasionally."},
            {"step": 5, "text": "Break curd into pieces. Mix in salt."},
            {"step": 6, "text": "Pack loosely into molds. Do not press."},
            {"step": 7, "text": "Turn daily for 4-5 days."},
            {"step": 8, "text": "Age at 55°F (13°C) for 4-6 weeks only. White Stilton is meant to be young."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Same PDO protection as Blue Stilton",
            "Base for many fruit-flavored varieties (apricot, cranberry, etc.)",
            "Younger and milder than blue Stilton",
            "Crumbly texture, tangy fresh flavor"
        ],
        "tags": ["cheese", "British", "English", "Stilton", "white", "fresh", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-single-gloucester",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Single Gloucester",
        "category": "cheese",
        "attribution": "Traditional Gloucestershire cheese",
        "source_note": "PDO protected. Uses part-skim milk, unlike Double Gloucester.",
        "description": "The lighter cousin of Double Gloucester - made with part-skim milk for a lower-fat, more delicate cheese. Smoother and milder than Double, with a shorter aging time.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp", "prep_note": "less than Double"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat part-skim milk to 86°F (30°C). Add annatto and stir."},
            {"step": 2, "text": "Add starter, ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 96°F (36°C) - lower than Double Gloucester."},
            {"step": 6, "text": "Stir until curds are firm, about 30 minutes."},
            {"step": 7, "text": "Drain. Light cheddaring for 30 minutes."},
            {"step": 8, "text": "Mill and salt."},
            {"step": 9, "text": "Press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) for only 6-8 weeks - shorter than Double."}
        ],
        "temperature": "86-96°F (30-36°C)",
        "notes": [
            "PDO protected - must be made in Gloucestershire",
            "Part-skim milk creates lighter, more delicate cheese",
            "Shorter aging than Double Gloucester",
            "Less annatto creates paler orange color"
        ],
        "tags": ["cheese", "British", "English", "Gloucester", "PDO", "part-skim", "mild"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-dorset-blue-vinny",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Dorset Blue Vinny",
        "category": "cheese",
        "attribution": "Traditional Dorset cheese",
        "source_note": "PGI protected. Made from hand-skimmed milk, traditionally blue-veined.",
        "description": "Historic Dorset blue cheese made from hand-skimmed milk. Drier and more crumbly than Stilton with irregular blue veining. Nearly extinct in the 20th century, now revived.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "hand-skimmed traditional"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Use hand-skimmed milk (skim off cream from top). Heat to 86°F (30°C)."},
            {"step": 2, "text": "Add starter and P. roqueforti, ripen 60 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 60 minutes."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently stir for 30 minutes, maintaining temperature."},
            {"step": 6, "text": "Drain curds. Pack loosely into molds."},
            {"step": 7, "text": "Turn frequently for 3-4 days. Do not press."},
            {"step": 8, "text": "Salt exterior and pierce for blue development."},
            {"step": 9, "text": "Age at 50°F (10°C) and high humidity for 3-4 months."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "'Vinny' is old Dorset dialect for 'vinew' meaning mold",
            "Nearly extinct by 1970s, now revived with PGI protection",
            "Skimmed milk creates drier, crumblier texture than Stilton",
            "Irregular blue veining is characteristic"
        ],
        "tags": ["cheese", "British", "English", "Dorset", "blue cheese", "PGI", "skimmed milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "british-y-fenni",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Y Fenni (Welsh Mustard Cheese)",
        "category": "cheese",
        "attribution": "Traditional Welsh cheese",
        "source_note": "From Abergavenny, Wales. Cheddar-style with mustard seeds and ale.",
        "description": "Welsh cheese flavored with wholegrain mustard and ale, creating a spicy, savory cheese. 'Y Fenni' is the Welsh name for Abergavenny where it originated.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "wholegrain mustard", "quantity": "2", "unit": "tbsp"},
            {"item": "Welsh ale", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Continue stirring until curds firm, about 30 minutes."},
            {"step": 6, "text": "Drain and cheddar for 1 hour."},
            {"step": 7, "text": "Mill curds. Mix in salt, mustard, and ale thoroughly."},
            {"step": 8, "text": "Press at 20 lbs for 1 hour, flip, 40 lbs for 24 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) for 2-3 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "'Y Fenni' is Welsh for Abergavenny",
            "Mustard seeds distribute throughout for spicy bites",
            "The ale adds complexity and helps integrate flavors",
            "Excellent with crusty bread and pickles"
        ],
        "tags": ["cheese", "British", "Welsh", "flavored", "mustard", "ale"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add British cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in BRITISH_CHEESE_RECIPES:
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
