#!/usr/bin/env python3
"""Add batch 22 of traditional cheese recipes - more French and specialty cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-vacherin-mont-dor",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vacherin Mont d'Or (Swiss/French)",
        "category": "mains",
        "attribution": "Jura Mountains (Swiss/French Border), 18th Century",
        "source_note": "Vacherin Mont d'Or has been made in the Jura Mountains since at least the 18th century. It's a seasonal cheese, produced only from late August to March when there isn't enough milk for Gruyère production.",
        "description": "Luxurious seasonal cheese wrapped in spruce bark, so soft it's eaten with a spoon - a winter delicacy from the Jura Mountains.",
        "servings_yield": "About 1 lb",
        "prep_time": "3 hours",
        "cook_time": "3-4 weeks aging",
        "total_time": "3-4 weeks",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "from hay-fed cows"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "spruce bark strip", "quantity": "1", "unit": "", "prep_note": "soaked in water, for wrapping"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add starter culture and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until soft curd."},
            {"step": 4, "text": "Cut curd into 3/4-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 86°F."},
            {"step": 6, "text": "Drain whey and ladle curds into round molds."},
            {"step": 7, "text": "Let drain at room temperature for 12-24 hours, flipping every 4-6 hours."},
            {"step": 8, "text": "Salt all surfaces and let dry for 24 hours."},
            {"step": 9, "text": "Wrap the cheese with soaked spruce bark, securing with a wooden band."},
            {"step": 10, "text": "Place in a spruce wood box slightly larger than the cheese."},
            {"step": 11, "text": "Age at 55°F and 95% humidity for 3-4 weeks, turning daily and wiping with brine."},
            {"step": 12, "text": "When ripe, the cheese should bulge slightly and feel liquid under the rind."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "The spruce bark is essential - it gives Vacherin its distinctive resinous aroma",
            "When perfectly ripe, cut off the top rind and eat the cheese with a spoon",
            "Traditional to bake in oven (350°F for 20 minutes) and dip bread and potatoes",
            "Both Swiss and French versions exist; Swiss is slightly larger"
        ],
        "tags": ["cheese", "traditional", "swiss", "french", "jura", "vacherin", "seasonal", "18th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-livarot-normandy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Livarot (Normandy)",
        "category": "mains",
        "attribution": "Livarot, Normandy, France, Medieval",
        "source_note": "Livarot has been made in the Pays d'Auge region of Normandy since at least the 13th century. Called 'The Colonel' due to the five strips of reed or paper wrapped around it (resembling military stripes), it's one of Normandy's great washed-rind cheeses.",
        "description": "Pungent Norman cheese nicknamed 'The Colonel' for its distinctive reed bands - one of France's oldest and most flavorful washed-rind cheeses.",
        "servings_yield": "About 1 lb",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "partially skimmed traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "annatto", "quantity": "1/8", "unit": "tsp", "prep_note": "for traditional color"},
            {"item": "reed or paper strips", "quantity": "5", "unit": "", "prep_note": "for wrapping (laîches)"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk. Add annatto for color."},
            {"step": 2, "text": "Add starter and B. linens. Ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1 hour until soft curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 90°F."},
            {"step": 6, "text": "Drain whey and ladle curds into cylindrical molds."},
            {"step": 7, "text": "Let drain at room temperature for 24-36 hours, flipping every 6-8 hours."},
            {"step": 8, "text": "Unmold and salt all surfaces. Let dry for 24 hours."},
            {"step": 9, "text": "Transfer to aging cave at 55°F and 95% humidity."},
            {"step": 10, "text": "Wash with brine (sometimes with annatto added for color) 3 times per week for 6-8 weeks."},
            {"step": 11, "text": "After 3-4 weeks, wrap with 5 bands of reed or paper around the circumference."},
            {"step": 12, "text": "Continue aging until rind is sticky orange-red and interior is soft."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "The five bands (laîches) give Livarot its 'Colonel' nickname",
            "Traditional Livarot was made from partially skimmed milk after cream was taken for butter",
            "The orange-red rind comes from annatto added to the wash",
            "Extremely pungent when ripe - one of the strongest Norman cheeses"
        ],
        "tags": ["cheese", "traditional", "french", "normandy", "washed-rind", "livarot", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-maroilles-picardy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Maroilles (Picardy)",
        "category": "mains",
        "attribution": "Maroilles Abbey, Picardy, France, 10th Century",
        "source_note": "Maroilles was created at the Maroilles Abbey in northern France around 962 AD by Benedictine monks. It's one of France's oldest and most pungent washed-rind cheeses.",
        "description": "Ancient monastic cheese with an intensely pungent washed rind - created by Benedictine monks over a thousand years ago.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "2-4 months aging",
        "total_time": "2-4 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "beer or hard cider", "quantity": "1/2", "unit": "cup", "prep_note": "traditional for wash"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and B. linens. Ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1-1.5 hours until soft curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 15 minutes."},
            {"step": 5, "text": "Stir gently for 30 minutes at 86°F."},
            {"step": 6, "text": "Drain whey and ladle curds into square molds (traditional shape)."},
            {"step": 7, "text": "Let drain at room temperature for 48 hours, flipping every 8-12 hours."},
            {"step": 8, "text": "Unmold and salt heavily. Let dry for 48 hours."},
            {"step": 9, "text": "Transfer to humid cave at 55°F and 95% humidity."},
            {"step": 10, "text": "Wash with beer or cider mixed with brine every 2-3 days for 2-4 months."},
            {"step": 11, "text": "The rind should develop a shiny, sticky, brick-red surface."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "Maroilles is traditionally square - make sure to use square molds",
            "The beer/cider wash is traditional in this region and adds to the complexity",
            "One of the strongest-smelling cheeses in France - but the flavor is milder than the aroma",
            "Essential ingredient in Flamiche au Maroilles (Belgian/French cheese tart)"
        ],
        "tags": ["cheese", "traditional", "french", "picardy", "washed-rind", "maroilles", "monastery-cheese", "10th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-bleu-dauvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bleu d'Auvergne",
        "category": "mains",
        "attribution": "Auvergne, France, 1850s",
        "source_note": "Bleu d'Auvergne was invented around 1854 by Antoine Roussel, a farmer who experimented with introducing rye bread mold into his cheese. It quickly became popular and received AOC protection in 1975.",
        "description": "Creamy French blue cheese from volcanic Auvergne, created by a curious farmer's experiment with rye bread mold.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and P. roqueforti. Stir well and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1-1.5 hours until soft curd."},
            {"step": 4, "text": "Cut curd into 1-inch cubes (large for blue cheese). Let rest 15 minutes."},
            {"step": 5, "text": "Stir gently for 30 minutes at 86°F."},
            {"step": 6, "text": "Drain whey and ladle curds loosely into cylindrical molds. Do not press."},
            {"step": 7, "text": "Let drain at room temperature for 24-48 hours, flipping every 8-12 hours."},
            {"step": 8, "text": "Unmold and salt all surfaces heavily over 3-4 days."},
            {"step": 9, "text": "Transfer to aging cave at 45-50°F and 95% humidity."},
            {"step": 10, "text": "After 10 days, pierce the cheese with sterilized skewers (20-30 holes)."},
            {"step": 11, "text": "Age for 4-8 weeks, turning weekly. Blue veins should develop within 2-3 weeks of piercing."}
        ],
        "temperature": "86°F make, 45-50°F aging",
        "notes": [
            "Bleu d'Auvergne is creamier and milder than Roquefort",
            "The piercing allows oxygen to reach the interior for blue mold growth",
            "Traditional aging was in the natural caves of the Auvergne volcanic region",
            "Pairs well with sweet wines like Sauternes"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "blue-cheese", "bleu-dauvergne", "1850s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fourme-dambert",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fourme d'Ambert",
        "category": "mains",
        "attribution": "Ambert, Auvergne, France, Ancient",
        "source_note": "Fourme d'Ambert is one of France's oldest blue cheeses, possibly dating to Roman times. The tall cylindrical shape ('fourme') is traditional to the Auvergne region. It's milder than other blues, making it a good introduction to blue cheese.",
        "description": "Ancient Auvergnat blue in a distinctive tall cylinder, milder and creamier than most blues - possibly dating to Roman times.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and P. roqueforti. Stir well and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1 hour until soft curd."},
            {"step": 4, "text": "Cut curd into 1-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 90°F."},
            {"step": 6, "text": "Drain most whey. Ladle curds into tall cylindrical molds (the distinctive 'fourme' shape)."},
            {"step": 7, "text": "Let drain at room temperature for 24-48 hours, flipping every 8-12 hours."},
            {"step": 8, "text": "Unmold and dry salt over 3-4 days."},
            {"step": 9, "text": "Transfer to aging cave at 50°F and 95% humidity."},
            {"step": 10, "text": "After 1 week, pierce with needles horizontally (the tall shape requires horizontal piercing)."},
            {"step": 11, "text": "Age for 4-8 weeks until blue-green veins develop throughout."}
        ],
        "temperature": "90°F make, 50°F aging",
        "notes": [
            "The tall cylindrical shape is traditional - use appropriate molds",
            "Fourme d'Ambert is one of the mildest French blue cheeses",
            "The gray rind is natural and edible but can be removed if desired",
            "Often paired with pears, walnuts, and sweet wines"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "blue-cheese", "fourme-dambert", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-banon-provence",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Banon (Provençal Leaf-Wrapped)",
        "category": "mains",
        "attribution": "Banon, Provence, France, Ancient",
        "source_note": "Banon cheese has been made in the hills of Haute-Provence for centuries, traditionally wrapped in chestnut leaves tied with raffia. The Roman emperor Antoninus Pius allegedly died from eating too much at a banquet featuring a cheese from this region.",
        "description": "Provençal cheese wrapped in chestnut leaves, developing complex flavors as it ages in its leafy cocoon.",
        "servings_yield": "About 8 oz (2 small cheeses)",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "raw goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or mixed goat/cow"},
            {"item": "mesophilic starter culture", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted in 1 tbsp water"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "chestnut leaves", "quantity": "8-10", "unit": "", "prep_note": "dried and soaked in brandy or eau-de-vie"},
            {"item": "raffia or string", "quantity": "as needed", "unit": "", "prep_note": "for tying"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 68-72°F (cool room temperature - Banon uses very little heat)."},
            {"step": 2, "text": "Add starter and stir well. Ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set for 12-24 hours until a soft, delicate curd forms."},
            {"step": 4, "text": "Very gently ladle the fragile curd into small round molds."},
            {"step": 5, "text": "Let drain at room temperature for 24-48 hours, flipping gently."},
            {"step": 6, "text": "Unmold and salt lightly. Let dry for 1-2 days until surface is slightly firm."},
            {"step": 7, "text": "Soak dried chestnut leaves in brandy or eau-de-vie until pliable."},
            {"step": 8, "text": "Wrap each cheese in overlapping chestnut leaves, then tie securely with raffia."},
            {"step": 9, "text": "Age at 55°F and 85% humidity for 2-4 weeks."},
            {"step": 10, "text": "The cheese will soften and develop complex flavors from the leaves."}
        ],
        "temperature": "68-72°F make (very cool), 55°F aging",
        "notes": [
            "Traditional Banon uses raw goat's milk, but some versions include sheep or cow",
            "The chestnut leaves are traditionally dipped in marc de Provence (grape brandy)",
            "Young Banon is mild and chalky; aged Banon becomes creamy with earthy, boozy notes",
            "If chestnut leaves are unavailable, grape leaves can substitute"
        ],
        "tags": ["cheese", "traditional", "french", "provence", "goat-cheese", "leaf-wrapped", "banon", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tetilla-galicia",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tetilla (Galician)",
        "category": "mains",
        "attribution": "Galicia, Spain, Medieval",
        "source_note": "Tetilla has been made in Galicia for centuries. Its distinctive pear or breast shape (the name means 'small breast') is traditional to the region. It's a mild, creamy cheese that pairs perfectly with Galician cuisine.",
        "description": "Distinctive pear-shaped Galician cheese with a mild, creamy flavor - its shape has been traditional for centuries.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Galician blonde cattle traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 15 minutes while maintaining 86°F."},
            {"step": 6, "text": "Raise temperature slowly to 95°F over 20 minutes while stirring."},
            {"step": 7, "text": "Drain whey and transfer curds to tetilla-shaped molds (pear/cone shape with nipple on top)."},
            {"step": 8, "text": "Press lightly at 5 lbs for 2 hours, flipping once."},
            {"step": 9, "text": "Press at 15 lbs for 8-12 hours."},
            {"step": 10, "text": "Brine for 8-12 hours in saturated salt solution."},
            {"step": 11, "text": "Air dry for 2-3 days."},
            {"step": 12, "text": "Age at 50°F and 85% humidity for 2-4 weeks, turning regularly."}
        ],
        "temperature": "86°F start, 95°F cook, 50°F aging",
        "notes": [
            "The distinctive pear/breast shape is essential to authentic Tetilla",
            "Traditional molds have a small nipple point at the top",
            "Tetilla is mild, slightly tangy, and becomes more flavorful with age",
            "Classic pairing with Galician empanadas and Albariño wine"
        ],
        "tags": ["cheese", "traditional", "spanish", "galicia", "tetilla", "semi-soft", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-murcia-al-vino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso de Murcia al Vino (Wine-Washed)",
        "category": "mains",
        "attribution": "Murcia, Spain, Ancient",
        "source_note": "Queso de Murcia has been made from Murciano-Granadina goat milk in southeastern Spain for centuries. The 'al vino' version is washed with local red wine, giving it a distinctive purple rind.",
        "description": "Spanish goat cheese washed with red wine, developing a striking purple rind and complex, fruity flavors.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "pasteurized goat's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Murciano-Granadina goats traditionally"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "red wine", "quantity": "2", "unit": "cups", "prep_note": "Spanish Monastrell or similar"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 90°F. Add calcium chloride."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 104°F over 30 minutes while stirring."},
            {"step": 6, "text": "Hold at 104°F for 30 minutes, stirring frequently."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 15 lbs for 1 hour. Flip and press at 30 lbs for 8-12 hours."},
            {"step": 9, "text": "Brine for 12-24 hours in saturated salt solution."},
            {"step": 10, "text": "Air dry for 2-3 days."},
            {"step": 11, "text": "Submerge the cheese in red wine for 48-72 hours, turning occasionally."},
            {"step": 12, "text": "Age at 50°F and 85% humidity for 2-3 months, washing with wine weekly."}
        ],
        "temperature": "90°F start, 104°F cook, 50°F aging",
        "notes": [
            "The wine wash gives the rind its distinctive purple-red color",
            "Traditional uses Monastrell (Mourvèdre) wine from the Jumilla region",
            "The interior is white and firm with a clean, tangy goat flavor",
            "The wine adds fruity notes to the rind while the paste remains pure goat"
        ],
        "tags": ["cheese", "traditional", "spanish", "murcia", "goat-cheese", "wine-washed", "ancient"],
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
        json.dump(data, f, indent=2)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
