#!/usr/bin/env python3
"""Add batch 69 - More ancient French regional cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-livarot-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Livarot (Normandy's Colonel Cheese)",
        "category": "mains",
        "attribution": "French tradition from Normandy, 13th century",
        "source_note": "Modernized from traditional Norman methods, adapted for home cheesemaking",
        "description": "One of Normandy's oldest cheeses, Livarot has been made since at least the 13th century. Called 'the Colonel' for the five stripes of sedge grass wrapped around it (like a colonel's insignia), this washed-rind cheese develops an intense aroma and rich, spicy flavor.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 6-8 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "rich Norman-style if possible"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": "for orange rind"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"},
            {"item": "annatto", "quantity": "5", "unit": "drops", "prep_note": "optional, for color"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and annatto if using. Add cultures and ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 60-90 minutes until soft clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Stir gently for 20 minutes at 90°F. Curds should remain moist."},
            {"step": 5, "text": "Ladle curds into cylindrical molds (about 4 inches diameter). Do not press."},
            {"step": 6, "text": "Flip every 30 minutes for 4 hours, then let drain overnight at room temperature."},
            {"step": 7, "text": "Brine for 4-6 hours. Remove and begin aging."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity. Wash with salt brine every 2-3 days."},
            {"step": 9, "text": "Orange-red bacteria will develop. After 3 weeks, wrap with 5 strips of sedge or raffia."},
            {"step": 10, "text": "Continue aging 6-8 weeks total. Rind becomes sticky and pungent; interior becomes creamy."}
        ],
        "temperature": "90°F curd, 55°F aging",
        "notes": [
            "The five stripes traditionally are sedge grass from Norman marshes",
            "Livarot has PDO protection since 1975",
            "Known as 'the Colonel' for the stripes resembling military rank",
            "Very strong aroma but flavor is milder than the smell suggests",
            "One of Normandy's three great washed-rind cheeses (with Pont-l'Évêque and Pavé d'Auge)"
        ],
        "tags": ["cheese", "cheesemaking", "french", "norman", "livarot", "washed-rind", "pungent", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-munster-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Munster (Alsatian Monastery Cheese)",
        "category": "mains",
        "attribution": "French tradition from Alsace-Vosges, 7th century",
        "source_note": "Modernized from traditional Alsatian methods, adapted for home cheesemaking",
        "description": "One of France's oldest cheeses, Munster was created by Benedictine monks in the 7th century. Made in the Vosges mountains, this washed-rind cheese has a powerful aroma but surprisingly delicate, creamy flavor. Traditionally served with caraway seeds and boiled potatoes.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 4-6 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brine and washing"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tbsp", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and cultures. Ripen for 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set for 60-90 minutes until soft clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Rest 10 minutes, then stir gently 15 minutes."},
            {"step": 4, "text": "Drain whey. Ladle curds into round molds about 7 inches diameter."},
            {"step": 5, "text": "Let drain at room temperature, flipping every 30 minutes for 4 hours."},
            {"step": 6, "text": "Continue draining overnight. No pressing - Munster drains under its own weight."},
            {"step": 7, "text": "Rub with salt or brine briefly. Begin aging at 55°F (13°C) and 95% humidity."},
            {"step": 8, "text": "Wash rind with brine every 2-3 days. Orange bacteria will develop."},
            {"step": 9, "text": "Age for 4-6 weeks, washing regularly. Rind becomes orange-red and tacky."},
            {"step": 10, "text": "Serve with caraway seeds and hot boiled potatoes - the traditional Alsatian pairing."}
        ],
        "temperature": "90°F curd, 55°F aging",
        "notes": [
            "Munster was created by Benedictine monks in the Vosges around 660 AD",
            "Not to be confused with American 'Muenster' which is completely different",
            "Munster-Géromé has PDO protection",
            "The aroma is powerful but flavor is surprisingly mild and creamy",
            "Traditionally paired with Gewürztraminer wine"
        ],
        "tags": ["cheese", "cheesemaking", "french", "alsatian", "munster", "washed-rind", "monastery-cheese", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-pont-leveque-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pont-l'Évêque (Norman Square Cheese)",
        "category": "mains",
        "attribution": "French tradition from Normandy, 12th century",
        "source_note": "Modernized from traditional Norman methods, adapted for home cheesemaking",
        "description": "One of France's oldest cheeses, Pont-l'Évêque has been made in Normandy since the 12th century. This square washed-rind cheese is milder than its cousin Livarot, with a golden crust and creamy, buttery interior. Named after the village in the Calvados department.",
        "servings_yield": "About 12 oz cheese",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus 4-6 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "Norman-style, high-fat"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "tiny pinch", "unit": "", "prep_note": "for white bloom"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and cultures. Ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 60-90 minutes until soft clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Stir gently for 10 minutes at 90°F. Keep curds moist and intact."},
            {"step": 5, "text": "Ladle curds into small square molds (about 4 inches). No pressing."},
            {"step": 6, "text": "Flip every 30 minutes for 4 hours, then let drain overnight."},
            {"step": 7, "text": "Salt surfaces lightly. Begin aging at 55°F (13°C) and 90% humidity."},
            {"step": 8, "text": "Wash with light salt brine every 3-4 days initially, then weekly."},
            {"step": 9, "text": "A golden to light orange rind with some white bloom will develop."},
            {"step": 10, "text": "Age 4-6 weeks. Interior should be creamy but not runny. Flavor is buttery with mushroom notes."}
        ],
        "temperature": "90°F curd, 55°F aging",
        "notes": [
            "First documented in 1226, making it one of France's oldest named cheeses",
            "Milder and more approachable than Livarot or Époisses",
            "The square shape is traditional and distinctive",
            "Has PDO protection since 1996",
            "Traditional pairing is with Calvados (apple brandy) or local cider"
        ],
        "tags": ["cheese", "cheesemaking", "french", "norman", "pont-leveque", "washed-rind", "soft-ripened", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-maroilles-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Maroilles (Picardy Monastery Cheese)",
        "category": "mains",
        "attribution": "French tradition from Picardy, 10th century",
        "source_note": "Modernized from traditional Picard methods, adapted for home cheesemaking",
        "description": "Created by monks at the Abbey of Maroilles around 960 AD, this powerful cheese is one of France's most pungent. The square shape, orange rind, and overwhelming aroma made it famous across northern France. Despite the smell, the flavor is rich and complex.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 5-7 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride and cultures. Ripen 1 hour."},
            {"step": 2, "text": "Add diluted rennet. Let set 90 minutes for very soft curd."},
            {"step": 3, "text": "Cut curd into 1-inch cubes (large for soft texture). Rest 10 minutes."},
            {"step": 4, "text": "Very gently stir for 10 minutes. Keep curds large and moist."},
            {"step": 5, "text": "Ladle curds into square molds about 5 inches. Do not press at all."},
            {"step": 6, "text": "Flip every hour for 6 hours, then let drain overnight at room temperature."},
            {"step": 7, "text": "Brine for 6-8 hours. Remove and begin aging."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity. Wash with brine every 2-3 days."},
            {"step": 9, "text": "Orange-red rind develops. The aroma will become increasingly powerful."},
            {"step": 10, "text": "Age 5-7 weeks minimum. Interior becomes creamy; aroma reaches full pungency."}
        ],
        "temperature": "86°F curd, 55°F aging",
        "notes": [
            "Created at the Abbey of Maroilles in 960 AD",
            "One of France's smelliest cheeses",
            "Traditional in flamiche (Picardy leek tart with Maroilles)",
            "Has PDO protection",
            "The monks who created it may have intended to ward off demons with the smell!"
        ],
        "tags": ["cheese", "cheesemaking", "french", "picardy", "maroilles", "washed-rind", "monastery-cheese", "pungent", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cantal-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cantal (France's Oldest Cheese)",
        "category": "mains",
        "attribution": "French tradition from Auvergne, 2000+ years",
        "source_note": "Modernized from traditional Auvergnat methods, adapted for home cheesemaking",
        "description": "Cantal may be France's oldest cheese, mentioned by Pliny the Elder in Roman times. Made in the volcanic mountains of Auvergne, this pressed cheese has a distinctive 'tome' texture from double-pressing. Three ages offer different experiences: jeune, entre-deux, and vieux.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "7 hours plus 1-6 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "from grass-fed cows if possible"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and culture. Ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45-60 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Stir gently 15 minutes at 90°F."},
            {"step": 4, "text": "Slowly raise temperature to 98°F (37°C) over 20 minutes while stirring."},
            {"step": 5, "text": "Drain whey. Pack curds into mold and press with 20 lbs for 6-8 hours. This is the 'first pressing.'"},
            {"step": 6, "text": "Remove from mold. Break or mill the pressed tome into walnut-sized pieces."},
            {"step": 7, "text": "Salt the milled curds (2 tbsp). Let rest 1-2 hours for salt to distribute."},
            {"step": 8, "text": "Repack salted curds into mold. Press with 40 lbs for 24 hours. This 'second pressing' is traditional."},
            {"step": 9, "text": "Remove and rub with remaining salt. Air dry 2-3 days."},
            {"step": 10, "text": "Age at 50°F (10°C) and 85% humidity. Jeune: 1-2 months. Entre-deux: 2-6 months. Vieux: 6+ months."}
        ],
        "temperature": "90-98°F curd, 50°F aging",
        "notes": [
            "Pliny the Elder wrote about cheese from Auvergne in 1st century AD",
            "The double-pressing (pressing, breaking, salting, repressing) creates Cantal's unique texture",
            "Cantal jeune (young) is mild and supple; vieux (old) is sharp and crumbly",
            "Traditional wheels are 35-45 kg (77-99 lbs)",
            "Has PDO protection - must be made in specific communes"
        ],
        "tags": ["cheese", "cheesemaking", "french", "auvergnat", "cantal", "pressed-cheese", "aged-cheese", "ancient", "roman", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-salers-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Salers (Transhumance Mountain Cheese)",
        "category": "mains",
        "attribution": "French tradition from Auvergne, ancient transhumance",
        "source_note": "Modernized from traditional Auvergnat methods, adapted for home cheesemaking",
        "description": "A close relative of Cantal but made only during summer when cattle graze high mountain pastures (transhumance). Salers must be made from raw milk of Salers cattle and only between April and November. The wild flowers and herbs of the volcanic pastures flavor the milk.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "5 hours",
        "total_time": "7 hours plus 3-18 months aging",
        "ingredients": [
            {"item": "whole raw milk", "quantity": "2", "unit": "gallons", "prep_note": "ideally from Salers cows on pasture"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "optional with raw milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh raw milk, still warm from milking if possible. Add culture if desired and ripen 20 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45-60 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small pieces. Stir gently while raising temperature to 98°F (37°C)."},
            {"step": 4, "text": "Continue stirring at 98°F for 30 minutes until curds are firm."},
            {"step": 5, "text": "Drain whey. Pack curds into mold and press with 30 lbs for 8 hours."},
            {"step": 6, "text": "Remove and mill the pressed tome into pieces. Salt and let rest 2 hours."},
            {"step": 7, "text": "Repack and press with 50 lbs for 24-48 hours."},
            {"step": 8, "text": "Traditional Salers is pressed in a 'gerle' - a wooden barrel. Use lined mold at home."},
            {"step": 9, "text": "Remove, rub with salt, and air dry 3-5 days."},
            {"step": 10, "text": "Age at 50°F (10°C) and 90% humidity for minimum 3 months, traditionally 12-18 months."}
        ],
        "temperature": "Fresh milk to 98°F curd, 50°F aging",
        "notes": [
            "Salers can only be made April-November during mountain grazing",
            "Must use raw milk from Salers cattle - a hardy breed from Auvergne",
            "The gerle (wooden barrel) develops unique microflora over generations",
            "Salers Tradition uses ONLY milk from Salers cows; regular Salers allows other breeds",
            "Has PDO protection with strict requirements"
        ],
        "tags": ["cheese", "cheesemaking", "french", "auvergnat", "salers", "raw-milk", "mountain-cheese", "transhumance", "ancient", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-morbier-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Morbier (Two-Milking Ash Line Cheese)",
        "category": "mains",
        "attribution": "French tradition from Franche-Comté, 19th century",
        "source_note": "Modernized from traditional Comtois methods, adapted for home cheesemaking",
        "description": "Morbier's distinctive black ash line tells its story: traditionally, evening curds were covered with ash to protect them overnight, then morning curds were added on top. Today the line is decorative, but it creates Morbier's unique identity - two layers of creamy cheese divided by a dark stripe.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "2 hours",
        "cook_time": "3 hours",
        "total_time": "5 hours plus 2-3 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "divided into two batches"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "divided"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted, divided"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted, divided"},
            {"item": "vegetable ash", "quantity": "1", "unit": "tbsp", "prep_note": "food-grade"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "FIRST BATCH: Heat 1 gallon milk to 90°F (32°C). Add half the culture and calcium chloride. Ripen 30 minutes."},
            {"step": 2, "text": "Add half the diluted rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds to 1/2-inch. Stir gently while raising to 100°F (38°C) over 20 minutes."},
            {"step": 4, "text": "Drain whey. Pack curds into mold, pressing lightly."},
            {"step": 5, "text": "After 30 minutes, sprinkle vegetable ash evenly over the top surface."},
            {"step": 6, "text": "SECOND BATCH: Repeat process with second gallon of milk."},
            {"step": 7, "text": "Pack second batch curds on top of ash layer. Press with 20 lbs for 6 hours."},
            {"step": 8, "text": "Flip and press with 30 lbs overnight."},
            {"step": 9, "text": "Brine for 12 hours. Air dry 2-3 days."},
            {"step": 10, "text": "Age at 55°F (13°C) and 90% humidity for 2-3 months. Rub or wash rind weekly."}
        ],
        "temperature": "90-100°F curd, 55°F aging",
        "notes": [
            "The ash line was originally functional - protecting evening curds until morning",
            "Today the ash is purely decorative but legally required for Morbier PDO",
            "The ash has no flavor - it's food-grade vegetable ash",
            "Morbier has a mild, creamy, slightly fruity flavor",
            "Can make in single batch with ash applied mid-press for similar effect"
        ],
        "tags": ["cheese", "cheesemaking", "french", "comte", "morbier", "ash-line", "semi-soft", "aged-cheese", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-tomme-de-savoie-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tomme de Savoie (Alpine Farmhouse Cheese)",
        "category": "mains",
        "attribution": "French tradition from Savoie Alps, ancient",
        "source_note": "Modernized from traditional Savoyard methods, adapted for home cheesemaking",
        "description": "The everyday cheese of the Savoie Alps, tomme was made from skimmed milk after the cream was taken for butter. This 'poor man's cheese' has a gray, rustic rind and firm, mild interior. Every Alpine farm made its own tomme - it's the foundation of Savoyard cuisine.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 2-4 months aging",
        "ingredients": [
            {"item": "partly skimmed milk", "quantity": "2", "unit": "gallons", "prep_note": "or mix whole and skim"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and culture. Ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Stir gently while slowly raising temperature to 100°F (38°C) over 20 minutes."},
            {"step": 5, "text": "Continue stirring at 100°F for 20 more minutes until curds are firm."},
            {"step": 6, "text": "Drain whey. Pack curds into mold. Press with 15 lbs for 1 hour."},
            {"step": 7, "text": "Flip and press with 25 lbs for 6 hours, then 35 lbs overnight."},
            {"step": 8, "text": "Rub surfaces with salt or brine briefly. Air dry for 2-3 days."},
            {"step": 9, "text": "Age at 55°F (13°C) and 90% humidity for 2-4 months."},
            {"step": 10, "text": "Natural gray mold will develop on rind - this is traditional. Turn regularly."}
        ],
        "temperature": "90-100°F curd, 55°F aging",
        "notes": [
            "Tomme means 'wheel' or 'round' - a generic term for many Alpine cheeses",
            "Traditional tomme is lower in fat since made from skimmed milk",
            "The gray natural rind is characteristic - don't wash it off",
            "Tomme de Savoie has PGI protection",
            "Base cheese for raclette and tartiflette in Savoie cuisine"
        ],
        "tags": ["cheese", "cheesemaking", "french", "savoyard", "alpine", "tomme", "farmhouse-cheese", "ancient", "pgi"],
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
