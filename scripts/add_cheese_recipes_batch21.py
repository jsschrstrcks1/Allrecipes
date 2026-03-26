#!/usr/bin/env python3
"""Add batch 21 of traditional cheese recipes - Scandinavian and European specialties."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-gjetost-norwegian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gjetost/Brunost (Norwegian Brown Cheese)",
        "category": "mains",
        "attribution": "Norway, 1860s (popularized)",
        "source_note": "Brunost (brown cheese) has been made in Norway since at least the 1800s. Anne Hov of Gudbrandsdalen is credited with adding cream in the 1860s, creating the sweeter modern version that became a Norwegian national treasure.",
        "description": "Unique Norwegian sweet brown cheese made from caramelized whey - not technically cheese but a beloved Scandinavian breakfast staple.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "4-5 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from goat cheese making (gjetost) or cow (brunost)"},
            {"item": "goat milk", "quantity": "2", "unit": "cups", "prep_note": "for authentic gjetost"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richness"},
            {"item": "salt", "quantity": "pinch", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine whey, milk, and cream in a large, heavy-bottomed pot."},
            {"step": 2, "text": "Bring to a boil over medium-high heat, stirring frequently."},
            {"step": 3, "text": "Reduce heat to maintain a steady boil. Stir frequently to prevent scorching."},
            {"step": 4, "text": "Continue boiling for 2-3 hours as liquid reduces. The mixture will gradually thicken and turn tan, then brown."},
            {"step": 5, "text": "As it thickens, stir constantly. The color will deepen to caramel brown and the mixture will become very thick."},
            {"step": 6, "text": "When the mixture pulls away from the sides and has a fudge-like consistency, remove from heat."},
            {"step": 7, "text": "Beat vigorously with a wooden spoon for 10-15 minutes until smooth (this prevents graininess)."},
            {"step": 8, "text": "Pour into a buttered mold or loaf pan."},
            {"step": 9, "text": "Let cool completely, then refrigerate."},
            {"step": 10, "text": "Slice thinly with a cheese plane and serve on bread or crackers."}
        ],
        "temperature": "Boiling throughout",
        "notes": [
            "True gjetost uses goat whey; brunost can be any whey. Ekte Geitost is 100% goat milk",
            "The brown color and sweet flavor come from caramelization of milk sugars (lactose)",
            "Beat vigorously after cooking to prevent a grainy texture",
            "Store wrapped tightly as it absorbs odors and dries out quickly",
            "Traditionally served on waffles or bread for breakfast"
        ],
        "tags": ["cheese", "traditional", "norwegian", "whey-cheese", "gjetost", "brunost", "caramelized", "1860s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-jarlsberg-norwegian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jarlsberg (Norwegian Swiss-Style)",
        "category": "mains",
        "attribution": "Norway, 1956 (modern), 1820s (original)",
        "source_note": "Jarlsberg was developed in the 1950s at the Agricultural University of Norway, based on a cheese made in the Jarlsberg region in the 1820s. It combines Swiss-style eye formation with a milder, nuttier flavor.",
        "description": "Norwegian Swiss-style cheese with large eyes, sweet nutty flavor, and excellent melting properties - Norway's most famous cheese export.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Propionibacterium shermanii", "quantity": "1/16", "unit": "tsp", "prep_note": "for eye formation"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add both starter cultures and propionic bacteria. Stir well and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 102°F over 30 minutes while stirring."},
            {"step": 6, "text": "Remove 1/3 of whey. Replace with 102°F water (curd washing for sweeter flavor)."},
            {"step": 7, "text": "Raise temperature to 108°F over 15 minutes while stirring."},
            {"step": 8, "text": "Let curds settle, drain whey, and transfer to mold."},
            {"step": 9, "text": "Press at 10 lbs for 30 minutes. Flip and press at 30 lbs for 6 hours."},
            {"step": 10, "text": "Flip and press at 50 lbs for 12 hours."},
            {"step": 11, "text": "Brine for 18-24 hours in saturated salt solution."},
            {"step": 12, "text": "Age at 55°F for 2 weeks, then move to 'warm room' at 68-70°F for 4-6 weeks for eye development."},
            {"step": 13, "text": "Return to 55°F and age for 3-12 months total."}
        ],
        "temperature": "90°F start, 108°F cook, 68-70°F warm room, 55°F aging",
        "notes": [
            "The combination of mesophilic and thermophilic starters is key to Jarlsberg's unique flavor",
            "The warm room phase develops the characteristic large eyes (holes)",
            "Jarlsberg is sweeter and milder than Swiss Emmental due to curd washing",
            "Eyes should be round, smooth, and evenly distributed"
        ],
        "tags": ["cheese", "traditional", "norwegian", "swiss-style", "jarlsberg", "eye-formation", "1950s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-danish-blue-danablu",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Danablu (Danish Blue)",
        "category": "mains",
        "attribution": "Denmark, 1920s",
        "source_note": "Danish Blue was developed in the early 1920s by Marius Boel as a Danish alternative to Roquefort. It quickly became Denmark's most famous blue cheese, known for its creamy texture and sharp, tangy flavor.",
        "description": "Creamy, sharp Danish blue cheese developed as a Roquefort alternative - now beloved worldwide for its bold flavor and smooth texture.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "8-12 weeks aging",
        "total_time": "8-12 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "homogenized for creamier texture"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richness"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and P. roqueforti. Stir well and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1-1.5 hours until soft curd forms."},
            {"step": 4, "text": "Cut curd into 1-inch cubes (larger for open texture). Let rest 10 minutes."},
            {"step": 5, "text": "Gently stir curds for 30 minutes at 86°F. Curds should remain soft."},
            {"step": 6, "text": "Drain whey and ladle curds into cylindrical molds. Do not press."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, flipping every 6-8 hours."},
            {"step": 8, "text": "Unmold and salt all surfaces heavily. Repeat salting over 3-4 days."},
            {"step": 9, "text": "Transfer to aging cave at 50°F and 95% humidity."},
            {"step": 10, "text": "After 1 week, pierce the cheese thoroughly with sterilized needles."},
            {"step": 11, "text": "Age for 8-12 weeks, turning weekly. Blue veins should develop within 3-4 weeks of piercing."}
        ],
        "temperature": "86°F make, 50°F aging",
        "notes": [
            "Danish Blue is creamier than Roquefort because it uses cow's milk plus cream",
            "Homogenized milk produces a creamier, more spreadable cheese",
            "Heavy salting is traditional and contributes to the sharp flavor",
            "The piercing allows air to reach the interior for blue mold growth"
        ],
        "tags": ["cheese", "traditional", "danish", "blue-cheese", "danablu", "1920s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cantal-auvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cantal (Auvergne)",
        "category": "mains",
        "attribution": "Auvergne, France, 2000+ Years",
        "source_note": "Cantal is one of the oldest French cheeses, mentioned by Pliny the Elder in the 1st century AD. Made in the volcanic Auvergne region, it may be the ancestor of many European cheeses including English cheddar.",
        "description": "Ancient French cheese from the volcanic Auvergne, possibly the ancestor of cheddar - with a complex, buttery flavor that deepens with age.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "1-8 months aging",
        "total_time": "1-8 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Salers cattle traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 95°F over 30 minutes while stirring gently."},
            {"step": 6, "text": "Drain whey. Press curds lightly in mold for 1 hour."},
            {"step": 7, "text": "Remove and break up the pressed curd. Let rest covered for 8-12 hours (the 'tome' stage)."},
            {"step": 8, "text": "Break the tome into walnut-sized pieces. This double-handling is unique to Cantal."},
            {"step": 9, "text": "Mix in salt thoroughly."},
            {"step": 10, "text": "Pack salted curds into mold. Press at 30 lbs for 2 hours."},
            {"step": 11, "text": "Flip and press at 50 lbs for 24 hours."},
            {"step": 12, "text": "Age at 50°F and 95% humidity. Cantal Jeune: 1-2 months; Entre-Deux: 3-6 months; Vieux: 8+ months."}
        ],
        "temperature": "90-95°F make, 50°F aging",
        "notes": [
            "The 'tome' stage (resting broken curds) is unique to Cantal and gives it distinctive texture",
            "Traditional Cantal wheels weigh 80-100 lbs",
            "Cantal Jeune (young) is mild and supple; Vieux (old) is firm, crumbly, and intense",
            "Some historians believe Cantal is the ancestor of English cheddar"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "cantal", "ancient-cheese", "territorial"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-morbier-jura",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Morbier (Jura)",
        "category": "mains",
        "attribution": "Jura, France, 19th Century",
        "source_note": "Morbier originated in Franche-Comté when farmers making Comté would protect leftover evening curd with ash, then add morning curd on top. The ash line became its signature, even though it's now purely decorative.",
        "description": "French cheese with a distinctive black ash line, originally a frugal farmhouse creation using leftover Comté curds.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "vegetable ash", "quantity": "2", "unit": "tbsp", "prep_note": "food-grade, for the line"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100°F over 30 minutes while stirring."},
            {"step": 6, "text": "Hold at 100°F for 20 minutes, stirring gently."},
            {"step": 7, "text": "Drain whey and divide curds in half."},
            {"step": 8, "text": "Press the first half of curds lightly into the mold."},
            {"step": 9, "text": "Sprinkle vegetable ash evenly over the surface of the pressed curds."},
            {"step": 10, "text": "Add the remaining curds on top of the ash layer."},
            {"step": 11, "text": "Press at 10 lbs for 30 minutes. Flip and press at 20 lbs for 8 hours."},
            {"step": 12, "text": "Salt the surface and let dry for 24 hours."},
            {"step": 13, "text": "Age at 55°F and 90% humidity for 2-3 months, turning weekly and wiping with brine if needed."}
        ],
        "temperature": "90°F start, 100°F cook, 55°F aging",
        "notes": [
            "The ash line was originally functional (protecting overnight curds) but is now decorative",
            "Traditional Morbier used soot from the wooden vat; modern versions use vegetable ash",
            "The cheese should be semi-soft with a fruity, slightly bitter flavor",
            "The rind develops a gray-brown color naturally during aging"
        ],
        "tags": ["cheese", "traditional", "french", "jura", "morbier", "ash-line", "19th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-saint-nectaire-auvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Saint-Nectaire (Auvergne)",
        "category": "mains",
        "attribution": "Auvergne, France, 17th Century",
        "source_note": "Saint-Nectaire has been made in the volcanic highlands of Auvergne since at least the 17th century. Named after Marshal Henri de la Ferté-Senneterre who introduced it to Louis XIV's court, it's prized for its rich, earthy flavor.",
        "description": "Earthy Auvergnat cheese with a complex, mushroomy rind and creamy interior - a favorite of Louis XIV.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Salers cattle traditionally"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 10 minutes while maintaining 90°F."},
            {"step": 6, "text": "Raise temperature slowly to 95°F over 20 minutes while stirring."},
            {"step": 7, "text": "Drain whey and transfer curds to flat round molds."},
            {"step": 8, "text": "Press lightly at 5 lbs for 2 hours, flipping several times."},
            {"step": 9, "text": "Press at 15 lbs for 8-12 hours."},
            {"step": 10, "text": "Salt all surfaces and let dry for 24 hours."},
            {"step": 11, "text": "Age on rye straw (traditional) at 50°F and 95% humidity for 4-8 weeks."},
            {"step": 12, "text": "Turn daily and wipe with brine as needed. A fuzzy gray-brown rind with orange patches should develop."}
        ],
        "temperature": "90-95°F make, 50°F aging",
        "notes": [
            "Traditional Saint-Nectaire is aged on rye straw, which contributes to the flavor and rind development",
            "The rind should be fuzzy with gray, brown, and orange molds - this is normal",
            "Fermier (farmhouse) Saint-Nectaire has an oval green casein mark; laitier (dairy) has a square mark",
            "The paste should be creamy and slightly bulging when ripe"
        ],
        "tags": ["cheese", "traditional", "french", "auvergne", "saint-nectaire", "washed-rind", "17th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-crowdie-scottish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Scottish Crowdie",
        "category": "mains",
        "attribution": "Scottish Highlands, Ancient/Medieval",
        "source_note": "Crowdie is one of Scotland's oldest cheeses, made in the Highlands for centuries. A simple acid-set fresh cheese, it was a staple of Highland crofters and is experiencing a modern revival.",
        "description": "Ancient Scottish fresh cheese, tangy and crumbly - a Highland crofter's staple now enjoying a renaissance.",
        "servings_yield": "About 1 lb",
        "prep_time": "10 minutes",
        "cook_time": "24-48 hours culturing",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw or pasteurized milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1/4", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "cream", "quantity": "2-4", "unit": "tbsp", "prep_note": "optional, for richness"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to lukewarm (about 72°F)."},
            {"step": 2, "text": "Stir in buttermilk thoroughly."},
            {"step": 3, "text": "Cover and leave at room temperature (65-72°F) for 24-48 hours until thickened and slightly separated."},
            {"step": 4, "text": "The milk should be thick like yogurt with visible whey separation."},
            {"step": 5, "text": "Line a colander with butter muslin and gently pour in the thickened milk."},
            {"step": 6, "text": "Tie up the corners and hang to drain for 6-12 hours until desired consistency."},
            {"step": 7, "text": "Turn the drained curd into a bowl."},
            {"step": 8, "text": "Add salt to taste and mix well."},
            {"step": 9, "text": "For a richer Crowdie, fold in a little cream."},
            {"step": 10, "text": "Use immediately or refrigerate for up to 1 week."}
        ],
        "temperature": "72°F culturing, room temperature",
        "notes": [
            "Traditional Crowdie is very simple - just soured milk, drained and salted",
            "Highland crofters made it from whatever milk was available",
            "Crowdie has a tangy, fresh flavor similar to fromage blanc or quark",
            "Traditionally spread on oatcakes or used in Scottish dishes like Cranachan"
        ],
        "tags": ["cheese", "traditional", "scottish", "highlands", "fresh-cheese", "crowdie", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-stracchino-lombardy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Stracchino/Crescenza (Lombardy)",
        "category": "mains",
        "attribution": "Lombardy, Italy, Medieval",
        "source_note": "Stracchino (also called Crescenza) has been made in Lombardy since at least the Middle Ages. The name comes from 'stracca' (tired) - referring to tired cows descending from Alpine pastures whose milk made the best cheese.",
        "description": "Soft, spreadable Italian cheese with a mild, milky flavor - named for the 'tired' cows whose rich autumn milk made the best wheels.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "1-3 weeks aging",
        "total_time": "1-3 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops", "prep_note": "diluted in 2 tbsp water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 100°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet (very small amount), stir gently. Let set 30-45 minutes until soft curd."},
            {"step": 4, "text": "Cut curd into 1-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Very gently stir curds for 10 minutes while maintaining 100°F."},
            {"step": 6, "text": "Drain whey gently and ladle curds into square molds without pressing."},
            {"step": 7, "text": "Let drain at room temperature for 8-12 hours, flipping every 2-3 hours."},
            {"step": 8, "text": "Unmold and salt lightly all surfaces."},
            {"step": 9, "text": "Refrigerate immediately. Stracchino is ready to eat in 1-3 days."},
            {"step": 10, "text": "Use within 1-2 weeks; it does not age well."}
        ],
        "temperature": "100°F make, refrigerator aging",
        "notes": [
            "Stracchino is meant to be eaten very fresh - it's not an aged cheese",
            "The texture should be soft and spreadable, like a thickened cream cheese",
            "Traditional in northern Italian focaccia (focaccia di Recco) and as a spread",
            "Crescenza is the same cheese with slightly more acid development"
        ],
        "tags": ["cheese", "traditional", "italian", "lombardy", "fresh-cheese", "stracchino", "crescenza", "medieval"],
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
