#!/usr/bin/env python3
"""Add batch 18 of traditional cheese recipes - English and American classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-cheddar-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional English Cheddar",
        "category": "mains",
        "attribution": "Cheddar, Somerset, England, 12th Century",
        "source_note": "Cheddar cheese originated in the village of Cheddar in Somerset, England. The caves of Cheddar Gorge provided ideal aging conditions. Documentation dates to at least 1170 when King Henry II purchased 10,240 lb of Cheddar.",
        "description": "The world's most popular cheese style, with its characteristic sharp, tangy flavor developed through the unique 'cheddaring' process.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-24 months aging",
        "total_time": "3-24 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw preferred for traditional flavor"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for orange cheddar"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk. Add annatto if using."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 30 seconds. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 102°F over 30 minutes, stirring gently."},
            {"step": 6, "text": "Hold at 102°F for 30 minutes, stirring every few minutes."},
            {"step": 7, "text": "Drain whey. Now begin 'cheddaring': Let curd mat into a slab at bottom of pot."},
            {"step": 8, "text": "Cut the matted curd into 2 slabs. Stack and flip every 15 minutes for 2 hours while maintaining 100°F. Slabs will become smooth and develop a chicken-breast texture."},
            {"step": 9, "text": "Mill the cheddared curd into finger-sized pieces."},
            {"step": 10, "text": "Toss with salt and let rest 5 minutes."},
            {"step": 11, "text": "Pack salted curds firmly into a cloth-lined mold."},
            {"step": 12, "text": "Press at 10 lbs for 15 minutes, flip. Press at 40 lbs for 12 hours."},
            {"step": 13, "text": "Air dry 2-4 days until rind forms, turning daily."},
            {"step": 14, "text": "Age at 55°F and 85% humidity. Mild: 3 months. Medium: 6-9 months. Sharp: 12+ months. Extra sharp: 24+ months."}
        ],
        "temperature": "86°F start, 102°F cook, 55°F aging",
        "notes": [
            "The 'cheddaring' process - stacking and flipping curd slabs - is unique to cheddar and develops its texture",
            "Traditional Somerset cheddar is cloth-bound and has a natural rind",
            "Block/mild cheddar is waxed or vacuum-sealed; bandaged cheddar develops more complex flavor",
            "Annatto coloring was traditionally added to suggest rich summer milk"
        ],
        "tags": ["cheese", "traditional", "english", "somerset", "cheddar", "aged-cheese", "12th-century", "cheddaring"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-edam-dutch",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Dutch Edam",
        "category": "mains",
        "attribution": "Edam, Netherlands, 14th Century",
        "source_note": "Edam cheese is named after the town of Edam in North Holland, where it was historically traded. In the 14th-18th centuries, Edam was the world's most popular cheese due to its long shelf life for sea voyages.",
        "description": "Mild, slightly nutty Dutch cheese traditionally coated in red or yellow wax, famous for its long shelf life and characteristic ball shape.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "4-10 months aging",
        "total_time": "4-10 months",
        "ingredients": [
            {"item": "part-skim milk", "quantity": "2", "unit": "gallons", "prep_note": "or mix whole milk 50/50 with skim"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "cheese wax", "quantity": "as needed", "unit": "", "prep_note": "red traditional for export, yellow for domestic"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 3/8-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Remove 1/4 of the whey. Replace with 140°F water to raise temperature to 95°F (curd washing)."},
            {"step": 6, "text": "Stir for 30 minutes while maintaining 95°F. Curds should shrink and become firmer."},
            {"step": 7, "text": "Drain whey and transfer curds to round ball-shaped molds."},
            {"step": 8, "text": "Press at 10 lbs for 30 minutes."},
            {"step": 9, "text": "Flip and press at 20 lbs for 2 hours."},
            {"step": 10, "text": "Flip and press at 30 lbs for 12 hours."},
            {"step": 11, "text": "Brine for 6-8 hours in saturated salt solution."},
            {"step": 12, "text": "Air dry for 2-3 days until surface is completely dry."},
            {"step": 13, "text": "Apply 2-3 coats of cheese wax."},
            {"step": 14, "text": "Age at 50-55°F for 4 weeks minimum; 10+ months for aged Edam."}
        ],
        "temperature": "90°F start, 95°F cook, 50-55°F aging",
        "notes": [
            "Traditional Edam uses part-skim milk, giving it lower fat content than Gouda",
            "The spherical shape and wax coating helped Edam survive long sea voyages",
            "Red wax indicates export quality; yellow wax was traditionally for Dutch domestic consumption",
            "Young Edam is mild and slightly rubbery; aged Edam develops more complex, sharper flavors"
        ],
        "tags": ["cheese", "traditional", "dutch", "washed-curd", "edam", "semi-hard", "14th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-colby-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional American Colby",
        "category": "mains",
        "attribution": "Colby, Wisconsin, 1885",
        "source_note": "Colby cheese was invented in 1885 by Joseph F. Steinwand at his father's cheese factory near Colby, Wisconsin. It was one of the first truly American cheese varieties.",
        "description": "Mild, moist American cheese similar to cheddar but softer and more open-textured due to the washed-curd process.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "1-3 months aging",
        "total_time": "1-3 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp", "prep_note": "for traditional orange color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk. Add annatto and stir well."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 3/8-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 102°F over 30 minutes, stirring gently."},
            {"step": 6, "text": "Hold at 102°F for 30 minutes, stirring frequently."},
            {"step": 7, "text": "Drain most of the whey. Replace with cold (60°F) water to bring temperature down to 80°F. This 'washed curd' step is what makes Colby different from cheddar."},
            {"step": 8, "text": "Stir curds in the cold water for 15 minutes. Drain completely."},
            {"step": 9, "text": "Toss curds with salt."},
            {"step": 10, "text": "Pack salted curds loosely into a cloth-lined mold (loose packing creates Colby's open texture)."},
            {"step": 11, "text": "Press at 20 lbs for 20 minutes."},
            {"step": 12, "text": "Flip and press at 30 lbs for 3 hours."},
            {"step": 13, "text": "Flip and press at 50 lbs for 12 hours."},
            {"step": 14, "text": "Air dry 2-3 days until surface is dry. Wax or vacuum seal."},
            {"step": 15, "text": "Age at 50-55°F for 1-3 months."}
        ],
        "temperature": "86°F start, 102°F cook, 80°F wash, 50-55°F aging",
        "notes": [
            "The cold water wash stops acid development, making Colby milder and moister than cheddar",
            "Colby does not go through the cheddaring process - it's NOT the same as cheddar despite similar appearance",
            "Traditional Colby has an open texture with small irregular holes",
            "Colby-Jack (Cojack) combines Colby and Monterey Jack curds marbled together"
        ],
        "tags": ["cheese", "traditional", "american", "wisconsin", "colby", "washed-curd", "1885"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-monterey-jack-california",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Monterey Jack",
        "category": "mains",
        "attribution": "Monterey, California, 1700s-1800s",
        "source_note": "Monterey Jack has roots in the queso blanco made by Spanish missionaries in California. David Jack of Monterey commercialized it in the 1880s, giving the cheese its current name.",
        "description": "Mild, creamy California cheese with excellent melting properties, descended from Spanish mission cheesemaking traditions.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "1-10 months aging",
        "total_time": "1-10 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 30 minutes while maintaining 88°F."},
            {"step": 6, "text": "Slowly raise temperature to 100°F over 30 minutes, stirring gently."},
            {"step": 7, "text": "Hold at 100°F for 30 minutes, stirring every few minutes."},
            {"step": 8, "text": "Drain whey. Rinse curds briefly with cool water (this helps keep Jack mild)."},
            {"step": 9, "text": "Toss curds with salt."},
            {"step": 10, "text": "Pack curds into a cloth-lined mold."},
            {"step": 11, "text": "Press at 10 lbs for 15 minutes."},
            {"step": 12, "text": "Flip and press at 20 lbs for 4 hours."},
            {"step": 13, "text": "Flip and press at 30 lbs for 12 hours."},
            {"step": 14, "text": "Air dry 2-3 days. Wax or vacuum seal for regular Jack."},
            {"step": 15, "text": "Age at 50°F for 1 month for mild Jack. For Dry Jack, age unwaxed 7-10 months, rubbing with oil/cocoa mixture."}
        ],
        "temperature": "88°F start, 100°F cook, 50°F aging",
        "notes": [
            "Regular Jack is aged about 1 month and is mild and melting",
            "Dry Jack (aged 7-10 months) becomes hard and granular, suitable for grating like Parmesan",
            "Pepper Jack is made by adding jalapeños to the curds before pressing",
            "The cool water rinse helps keep Monterey Jack's characteristic mild flavor"
        ],
        "tags": ["cheese", "traditional", "american", "california", "monterey-jack", "semi-soft", "1800s", "melting-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-brick-cheese-wisconsin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Wisconsin Brick Cheese",
        "category": "mains",
        "attribution": "Wisconsin, 1877",
        "source_note": "Brick cheese was invented by John Jossi, a Swiss immigrant cheesemaker, in Wisconsin around 1877. Named for the bricks used to press it (and its final shape), it's essential for authentic Detroit-style pizza.",
        "description": "Unique American original with a pungent aroma, tangy flavor, and superb melting qualities - the secret to Detroit-style pizza.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "optional, for aged brick"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "light brine", "quantity": "1", "unit": "cup", "prep_note": "for washing if aging longer"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture (and B. linens if using), stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 96°F over 20 minutes, stirring gently."},
            {"step": 6, "text": "Remove 1/3 of the whey. Add 96°F water to wash curds (reduces acidity)."},
            {"step": 7, "text": "Continue stirring for 30 minutes at 96°F."},
            {"step": 8, "text": "Drain whey and transfer curds to rectangular brick-shaped molds."},
            {"step": 9, "text": "Press with actual bricks or weights at 5-10 lbs for 8-12 hours, flipping several times."},
            {"step": 10, "text": "Brine for 12 hours in saturated salt solution."},
            {"step": 11, "text": "For mild brick: Air dry 2-3 days, wax, age 2-3 weeks at 50°F."},
            {"step": 12, "text": "For aged brick: Age at 55°F and 90% humidity for 2-3 months, washing with brine weekly to develop surface bacteria."}
        ],
        "temperature": "90°F start, 96°F cook, 50-55°F aging",
        "notes": [
            "Young brick cheese is mild, buttery, and perfect for melting on pizza",
            "Aged brick develops a pungent, Limburger-like aroma from surface bacteria",
            "The brick shape isn't just decorative - the high surface area aids in aging",
            "Essential for authentic Detroit-style pizza, where it's applied edge-to-edge before baking"
        ],
        "tags": ["cheese", "traditional", "american", "wisconsin", "brick-cheese", "semi-soft", "1877", "pizza-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-red-leicester-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Red Leicester (Leicestershire)",
        "category": "mains",
        "attribution": "Leicestershire, England, 17th Century",
        "source_note": "Red Leicester originated in the English county of Leicestershire, with records dating to the 1600s. The orange-red color comes from annatto, traditionally added to simulate the rich color of summer milk.",
        "description": "Distinctive English cheese with a deep russet color, crumbly texture, and slightly sweet, nutty flavor.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "6-9 months aging",
        "total_time": "6-9 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto coloring", "quantity": "1/2", "unit": "tsp", "prep_note": "essential for traditional color"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add annatto and stir thoroughly to distribute color evenly."},
            {"step": 3, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 4, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 5, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 6, "text": "Slowly raise temperature to 94°F over 40 minutes, stirring gently."},
            {"step": 7, "text": "Hold at 94°F for 45 minutes, stirring every few minutes."},
            {"step": 8, "text": "Drain whey. Perform modified cheddaring: stack curds at bottom of pot for 30 minutes, cutting and restacking once."},
            {"step": 9, "text": "Mill curds into walnut-sized pieces."},
            {"step": 10, "text": "Toss with salt and let rest 5 minutes."},
            {"step": 11, "text": "Pack into cloth-lined mold."},
            {"step": 12, "text": "Press at 20 lbs for 30 minutes, flip. Press at 40 lbs for 12 hours."},
            {"step": 13, "text": "Air dry 3-5 days. Cloth-bind with lard-soaked cloth or wax."},
            {"step": 14, "text": "Age at 55°F and 85% humidity for 6-9 months."}
        ],
        "temperature": "86°F start, 94°F cook, 55°F aging",
        "notes": [
            "Red Leicester's color should be a deep russet-orange, not bright orange",
            "The cheese is milled into larger pieces than cheddar, giving it a more crumbly texture",
            "Traditional Leicester is cloth-bound; modern versions may be waxed",
            "Pairs well with crusty bread, apples, and English ales"
        ],
        "tags": ["cheese", "traditional", "english", "leicestershire", "red-leicester", "territorial-cheese", "17th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sage-derby-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sage Derby",
        "category": "mains",
        "attribution": "Derbyshire, England, 17th Century",
        "source_note": "Derby cheese has been made in Derbyshire since at least the 1600s. Sage Derby, with its distinctive green marbling, was traditionally made at Christmas and harvest time using fresh sage leaves.",
        "description": "Festive English cheese marbled with green sage, traditionally served at Christmas with its distinctive herbal flavor and striking appearance.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "1-6 months aging",
        "total_time": "1-6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "fresh sage leaves", "quantity": "1", "unit": "cup", "prep_note": "finely chopped, or 1/4 cup dried"},
            {"item": "spinach juice", "quantity": "1/4", "unit": "cup", "prep_note": "for green color, traditional method"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare sage infusion: Blend fresh sage with spinach juice to make a bright green paste. Strain through fine cloth."},
            {"step": 2, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 4, "text": "Add diluted rennet, stir gently. Let set 45 minutes until clean break."},
            {"step": 5, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 6, "text": "Slowly raise temperature to 94°F over 30 minutes, stirring gently."},
            {"step": 7, "text": "Hold at 94°F for 30 minutes, stirring frequently."},
            {"step": 8, "text": "Drain whey. Divide curds into two portions."},
            {"step": 9, "text": "Add the sage/spinach paste to one portion and mix thoroughly. Leave the other portion plain."},
            {"step": 10, "text": "Salt both portions separately."},
            {"step": 11, "text": "Layer green and plain curds alternately in cloth-lined mold for marbled effect."},
            {"step": 12, "text": "Press at 15 lbs for 30 minutes, flip. Press at 30 lbs for 12 hours."},
            {"step": 13, "text": "Air dry 3-4 days. Wax or cloth-bind."},
            {"step": 14, "text": "Age at 55°F for 1-3 months for mild, 6+ months for stronger flavor."}
        ],
        "temperature": "86°F start, 94°F cook, 55°F aging",
        "notes": [
            "Spinach adds color intensity to the sage; without it, the green may be subtle",
            "Traditional Sage Derby was made for harvest festivals and Christmas",
            "The marbling pattern varies depending on how curds are layered",
            "Modern commercial versions often use dried sage and artificial coloring; this traditional method uses real herbs"
        ],
        "tags": ["cheese", "traditional", "english", "derbyshire", "sage-derby", "herbed-cheese", "17th-century", "christmas"],
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
