#!/usr/bin/env python3
"""Add batch 17 of traditional cheese recipes - European classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-provolone-southern-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Provolone (Southern Italian)",
        "category": "mains",
        "attribution": "Southern Italy, 19th Century",
        "source_note": "Provolone is a pasta filata (stretched curd) cheese that originated in southern Italy, particularly Campania and Basilicata. The name comes from the Neapolitan word 'prova' meaning ball-shaped.",
        "description": "Classic Italian stretched-curd cheese, made in the southern tradition with a smooth, golden exterior and tangy, slightly sharp flavor.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-12 months aging",
        "total_time": "2-12 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "lipase powder", "quantity": "1/8", "unit": "tsp", "prep_note": "for traditional sharp flavor"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Dissolve lipase in 1/4 cup cool water, let sit 20 minutes. Add to milk and stir."},
            {"step": 3, "text": "Add starter culture, stir well, and ripen for 45 minutes at 97°F."},
            {"step": 4, "text": "Add diluted rennet, stir gently for 30 seconds. Let set 30-45 minutes until clean break."},
            {"step": 5, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 6, "text": "Slowly raise temperature to 118°F over 45 minutes while stirring."},
            {"step": 7, "text": "Drain curds and let mat at 100°F for 2-3 hours, flipping every 30 minutes, until pH reaches 5.2-5.3 and curd stretches smoothly in hot water."},
            {"step": 8, "text": "Cut matted curd into strips. Heat water to 170-180°F with salt."},
            {"step": 9, "text": "Working in batches, stretch curd in hot water until smooth and elastic, folding onto itself repeatedly."},
            {"step": 10, "text": "Form into pear or sausage shape, tying off the top with string if desired."},
            {"step": 11, "text": "Brine for 6-8 hours in saturated salt solution."},
            {"step": 12, "text": "Hang to dry for 2-3 days, then age at 55°F and 85% humidity. Coat with olive oil monthly."},
            {"step": 13, "text": "Age 2-3 months for mild (Provolone Dolce) or 6-12 months for sharp (Provolone Piccante)."}
        ],
        "temperature": "97°F make, 170°F stretch, 55°F aging",
        "notes": [
            "Lipase adds the characteristic tangy, sharp flavor - more lipase = sharper cheese",
            "The curd must reach proper acidity (pH 5.2) before stretching or it won't stretch properly",
            "Traditional provolone is hung by string and develops a golden rind",
            "Provolone can be smoked after brining for additional flavor"
        ],
        "tags": ["cheese", "traditional", "italian", "pasta-filata", "provolone", "aged-cheese", "19th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gouda-dutch",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Dutch Gouda",
        "category": "mains",
        "attribution": "Gouda, Netherlands, 12th Century",
        "source_note": "Gouda is named after the city in the Netherlands where it was historically traded (not necessarily made). Records of Gouda cheese date to 1184, making it one of the world's oldest recorded cheeses still made today.",
        "description": "Classic Dutch washed-curd cheese with its characteristic sweet, nutty flavor and smooth, dense paste - the world's most popular cheese style.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2 months to 5 years aging",
        "total_time": "2 months to 5 years",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "cheese wax", "quantity": "as needed", "unit": "", "prep_note": "red or yellow traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 10 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 30 seconds. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Remove 1/3 of the whey. Replace with 175°F water to raise temperature to 92°F. This is the 'washing' that gives Gouda its sweet flavor."},
            {"step": 6, "text": "Stir for 20 minutes while slowly raising temperature to 100°F."},
            {"step": 7, "text": "Let curds settle for 5 minutes, then drain remaining whey."},
            {"step": 8, "text": "Transfer curds to a cloth-lined mold. Press at 10 lbs for 30 minutes."},
            {"step": 9, "text": "Flip, redress, and press at 30 lbs for 6-8 hours or overnight."},
            {"step": 10, "text": "Brine for 8-12 hours in saturated salt solution (1 hour per pound)."},
            {"step": 11, "text": "Air dry at room temperature for 2-3 days until surface is dry."},
            {"step": 12, "text": "Wax with two coats of cheese wax or age naturally at 55°F and 85% humidity."},
            {"step": 13, "text": "Age minimum 2 months; 1-2 years for medium aged; 5+ years for old Gouda."}
        ],
        "temperature": "90°F start, 100°F cook, 55°F aging",
        "notes": [
            "The curd washing step removes lactose, preventing acid development and creating Gouda's characteristic sweetness",
            "Aged Gouda (2+ years) develops crunchy calcium lactate crystals and deep caramel flavors",
            "Traditional Gouda wheels are flattened spheres; baby Goudas are smaller cylinders",
            "Waxing is optional - natural rind Gouda is also traditional"
        ],
        "tags": ["cheese", "traditional", "dutch", "washed-curd", "gouda", "aged-cheese", "12th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-emmental-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Emmental (Swiss)",
        "category": "mains",
        "attribution": "Emme Valley, Switzerland, 13th Century",
        "source_note": "Emmental (often called 'Swiss cheese' in America) originated in the Emme Valley of the canton of Bern. The characteristic holes ('eyes') are formed by propionibacteria producing CO2 during aging.",
        "description": "The original 'Swiss cheese' with its distinctive large holes, mild nutty flavor, and slightly sweet taste - a masterpiece of Alpine cheesemaking.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "4-6 months aging",
        "total_time": "4-6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw preferred"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium shermanii", "quantity": "1/16", "unit": "tsp", "prep_note": "for eye formation"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add thermophilic starter and propionic bacteria. Stir well and ripen for 10 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 30 seconds. Let set 30 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (smaller than most cheeses). Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently while raising temperature to 120°F over 45 minutes."},
            {"step": 6, "text": "Continue stirring at 120°F for 30-45 minutes until curds are very firm and shrunk."},
            {"step": 7, "text": "Drain whey and transfer curds to a large cloth-lined mold (traditional Emmental is large)."},
            {"step": 8, "text": "Press at 10 lbs for 30 minutes, flip. Press at 25 lbs for 6 hours, flip."},
            {"step": 9, "text": "Press at 50 lbs for 12-24 hours."},
            {"step": 10, "text": "Brine for 24 hours in saturated salt solution."},
            {"step": 11, "text": "Age at 55°F and 85% humidity for 2-3 weeks."},
            {"step": 12, "text": "Move to 'warm room' at 68-74°F for 3-5 weeks. This is when eyes form."},
            {"step": 13, "text": "Return to cool aging at 55°F for 3-4 more months minimum."}
        ],
        "temperature": "90°F start, 120°F cook, 68-74°F warm room, 55°F aging",
        "notes": [
            "The warm room phase is critical for eye formation - propionic bacteria produce CO2 at warmer temperatures",
            "Traditional Emmental wheels weigh 150-220 lbs; scale the recipe up for more authentic results",
            "Eyes should be cherry to walnut sized and evenly distributed",
            "A 'blind' Emmental (no eyes) indicates something went wrong with the propionic culture"
        ],
        "tags": ["cheese", "traditional", "swiss", "alpine", "emmental", "swiss-cheese", "13th-century", "eye-formation"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gruyere-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gruyère (Swiss)",
        "category": "mains",
        "attribution": "Gruyères, Switzerland, 12th Century",
        "source_note": "Gruyère takes its name from the town of Gruyères in the canton of Fribourg. First mentioned in 1115 AD, it's a cornerstone of Swiss cuisine, essential for fondue and French onion soup.",
        "description": "Prestigious Swiss Alpine cheese with complex nutty, slightly sweet flavor and small irregular eyes - the king of fondue cheeses.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "5-12 months aging",
        "total_time": "5-12 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw preferred"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium shermanii", "quantity": "1/32", "unit": "tsp", "prep_note": "less than Emmental"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining and rubbing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 93°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add thermophilic starter and a very small amount of propionic bacteria. Ripen for 15 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 35-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently while raising temperature to 130°F over 45 minutes."},
            {"step": 6, "text": "Continue stirring at 130°F for 45 minutes until curds are very firm."},
            {"step": 7, "text": "Drain whey and transfer to cloth-lined mold. Press immediately at 15 lbs."},
            {"step": 8, "text": "Flip every 15 minutes for first hour, then press at 30 lbs for 12 hours."},
            {"step": 9, "text": "Brine for 18-24 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 55°F and 95% humidity for 2-3 months, washing with brine weekly."},
            {"step": 11, "text": "Optional: warm room phase at 65°F for 2-3 weeks for small eye development."},
            {"step": 12, "text": "Continue aging at 55°F for 5-12 months total, turning weekly."}
        ],
        "temperature": "93°F start, 130°F cook, 55°F aging",
        "notes": [
            "Gruyère uses less propionic bacteria than Emmental, resulting in smaller, fewer eyes",
            "The higher cooking temperature contributes to Gruyère's denser, more complex flavor",
            "Traditional Gruyère is rubbed with brine during aging to develop the rind",
            "Reserve (12+ months) Gruyère develops crystalline texture and intense flavor"
        ],
        "tags": ["cheese", "traditional", "swiss", "alpine", "gruyere", "fondue-cheese", "12th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-havarti-danish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Danish Havarti",
        "category": "mains",
        "attribution": "Denmark, 1800s (Hanne Nielsen)",
        "source_note": "Havarti was developed by Hanne Nielsen in the mid-1800s at her farm Havarthigaard north of Copenhagen. She traveled Europe learning cheesemaking techniques and created this washed-curd cheese upon her return.",
        "description": "Creamy Danish table cheese with small irregular holes, buttery flavor, and smooth meltability - a modern classic from a pioneering cheesemaker.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3 months aging",
        "total_time": "3 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "cheese wax", "quantity": "as needed", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 30 seconds. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Remove 1/3 of the whey. Replace with 145°F water to raise temperature to 98°F (curd washing step)."},
            {"step": 6, "text": "Stir gently for 15 minutes at 98°F."},
            {"step": 7, "text": "Drain whey to level of curds. Let curds settle and mat for 5 minutes."},
            {"step": 8, "text": "Transfer curds loosely to a cloth-lined mold - do not pack tightly (this creates the irregular holes)."},
            {"step": 9, "text": "Press very lightly at 5 lbs for 30 minutes."},
            {"step": 10, "text": "Flip and press at 10 lbs for 6-8 hours or overnight."},
            {"step": 11, "text": "Brine for 6-8 hours in saturated salt solution."},
            {"step": 12, "text": "Air dry 2-3 days until surface is dry."},
            {"step": 13, "text": "Age at 50°F and 80% humidity for 3 months, turning weekly. Wax after 2 weeks if desired."}
        ],
        "temperature": "86°F start, 98°F after wash, 50°F aging",
        "notes": [
            "The light pressing and loose packing create Havarti's signature small irregular holes",
            "Curd washing gives Havarti its mild, buttery flavor",
            "Flavored Havarti (dill, caraway) can be made by adding herbs after draining",
            "Creamy Havarti is aged less (6-8 weeks); aged Havarti develops more complex flavor"
        ],
        "tags": ["cheese", "traditional", "danish", "washed-curd", "havarti", "semi-soft", "19th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-paneer-indian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Indian Paneer",
        "category": "mains",
        "attribution": "South Asia, Ancient",
        "source_note": "Paneer is a fresh acid-set cheese central to South Asian cuisine. Its origins may trace to the Persian influence during the Mughal Empire, though similar fresh cheeses have ancient roots in the region.",
        "description": "Simple fresh Indian cheese that holds its shape when cooked, essential for dishes like palak paneer and matar paneer.",
        "servings_yield": "About 12 oz",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "2 hours including pressing",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": "or white vinegar"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in a heavy-bottomed pot over medium-high heat until it reaches a full rolling boil, stirring frequently to prevent scorching."},
            {"step": 2, "text": "Reduce heat to low. Add lemon juice one tablespoon at a time, stirring gently after each addition."},
            {"step": 3, "text": "The curds will separate from the greenish whey almost immediately. If not fully separated, add a bit more acid."},
            {"step": 4, "text": "Turn off heat and let sit for 5 minutes."},
            {"step": 5, "text": "Line a colander with butter muslin and set over a bowl. Pour curds and whey into the lined colander."},
            {"step": 6, "text": "Rinse curds gently with cool water to remove the acidic taste."},
            {"step": 7, "text": "Gather the cloth corners and squeeze gently to remove excess whey."},
            {"step": 8, "text": "Twist the cloth tight and place the wrapped cheese on a flat surface. Set a heavy pot or weight on top."},
            {"step": 9, "text": "Press for 1-2 hours depending on desired firmness."},
            {"step": 10, "text": "Unwrap and use immediately, or refrigerate in water for up to 1 week."}
        ],
        "temperature": "212°F (boiling)",
        "notes": [
            "Fresh paneer is soft and crumbly; pressed paneer is firm enough to cube and fry",
            "The whey can be used in bread making or added to soups for protein",
            "For softer paneer, press for less time; for firm grilling paneer, press longer",
            "Salt is optional - traditional paneer is often unsalted as it absorbs flavor from dishes"
        ],
        "tags": ["cheese", "traditional", "indian", "fresh-cheese", "paneer", "acid-set", "ancient", "vegetarian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-quark-german",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional German Quark",
        "category": "mains",
        "attribution": "Central Europe, Medieval",
        "source_note": "Quark has been made in German-speaking countries since at least the 14th century. The name derives from a Slavic word for 'curd.' It's a staple of German, Austrian, and Eastern European cuisines.",
        "description": "Smooth, creamy fresh cheese similar to yogurt but milder, essential for German cheesecake (Käsekuchen) and many Central European dishes.",
        "servings_yield": "About 1 lb",
        "prep_time": "10 minutes",
        "cook_time": "12-24 hours culturing",
        "total_time": "24-36 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as mesophilic starter"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted in 2 tbsp water"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72-76°F (barely warm room temperature)."},
            {"step": 2, "text": "Stir in buttermilk thoroughly."},
            {"step": 3, "text": "Add diluted rennet and stir gently for 30 seconds."},
            {"step": 4, "text": "Cover and let sit at room temperature (68-72°F) for 12-24 hours until thickened to a yogurt-like consistency."},
            {"step": 5, "text": "The curd is ready when it pulls away from the sides of the pot and shows clear whey on top."},
            {"step": 6, "text": "Line a colander with butter muslin set over a bowl."},
            {"step": 7, "text": "Gently pour the curd into the lined colander without breaking it up too much."},
            {"step": 8, "text": "Let drain for 6-12 hours until desired consistency is reached. For a thick quark, drain longer; for a spreadable quark, drain less."},
            {"step": 9, "text": "Transfer to a container. For smoother texture, whisk or blend briefly."},
            {"step": 10, "text": "Refrigerate and use within 1-2 weeks."}
        ],
        "temperature": "72-76°F culturing, room temperature",
        "notes": [
            "Quark is somewhere between yogurt and cream cheese in texture",
            "Traditional quark has no salt - add if desired for savory applications",
            "Low-fat quark can be made with skim milk",
            "The longer you drain, the thicker and more cheese-like it becomes",
            "Use in cheesecake, as a spread, with fruit, or in savory dips"
        ],
        "tags": ["cheese", "traditional", "german", "fresh-cheese", "quark", "central-european", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fromage-blanc-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Fromage Blanc",
        "category": "mains",
        "attribution": "France, Ancient",
        "source_note": "Fromage blanc ('white cheese') is one of the simplest and oldest French fresh cheeses. It has been made in French farmhouses for centuries as a way to use fresh milk.",
        "description": "Simple French fresh cheese with a tangy, creamy flavor - served as dessert with honey and fruit or used in savory applications.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "12-24 hours culturing",
        "total_time": "24-36 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richer fromage blanc"},
            {"item": "fromage blanc culture", "quantity": "1", "unit": "packet", "prep_note": "or 1/4 cup cultured buttermilk"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop", "prep_note": "diluted in 2 tbsp water"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream in a pot. Heat to 86°F."},
            {"step": 2, "text": "Add fromage blanc culture (or buttermilk), stir well."},
            {"step": 3, "text": "Add the single drop of diluted rennet and stir gently."},
            {"step": 4, "text": "Cover and let culture at 72-75°F for 12-18 hours until set like a thick yogurt."},
            {"step": 5, "text": "The curd is ready when it holds a knife mark and shows clear whey."},
            {"step": 6, "text": "Line a colander with butter muslin. Gently ladle the curd into the cloth."},
            {"step": 7, "text": "Let drain for 6-12 hours at room temperature, or in the refrigerator for milder flavor."},
            {"step": 8, "text": "When desired consistency is reached, transfer to a container."},
            {"step": 9, "text": "Whisk until smooth if a creamier texture is desired."},
            {"step": 10, "text": "Refrigerate and use within 1-2 weeks."}
        ],
        "temperature": "86°F start, 72-75°F culturing",
        "notes": [
            "Fromage blanc is similar to quark but traditionally richer due to added cream",
            "The French serve it as dessert with sugar, honey, jam, or fresh fruit",
            "It can also be salted and served with herbs as an appetizer",
            "The very small amount of rennet gives structure without making it rubbery",
            "For a lighter version, omit the cream and use all milk"
        ],
        "tags": ["cheese", "traditional", "french", "fresh-cheese", "fromage-blanc", "dessert-cheese", "ancient"],
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
