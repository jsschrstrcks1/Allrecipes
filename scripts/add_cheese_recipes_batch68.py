#!/usr/bin/env python3
"""Add batch 68 - Ancient Eastern European and Alpine cheeses plus a cheesemaking guide."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-liptauer-hungarian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Liptauer (Hungarian Spiced Cheese Spread)",
        "category": "mains",
        "attribution": "Hungarian/Austrian tradition from Liptov region",
        "source_note": "Modernized from traditional Hungarian methods, adapted for home cheesemaking",
        "description": "A vibrant orange-red cheese spread from the Liptov region (now Slovakia), Liptauer combines fresh sheep cheese with paprika, caraway, and other spices. The base cheese, bryndza, is mixed with butter and seasoned liberally. A staple of Hungarian and Austrian cuisine for centuries.",
        "servings_yield": "About 2 cups spread",
        "prep_time": "30 minutes",
        "cook_time": "None",
        "total_time": "30 minutes plus overnight to meld flavors",
        "ingredients": [
            {"item": "fresh farmer's cheese or quark", "quantity": "1", "unit": "lb", "prep_note": "or bryndza if available"},
            {"item": "butter", "quantity": "1/2", "unit": "cup", "prep_note": "softened"},
            {"item": "sweet Hungarian paprika", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp", "prep_note": "lightly crushed"},
            {"item": "Dijon mustard", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "capers", "quantity": "1", "unit": "tbsp", "prep_note": "drained and chopped"},
            {"item": "small onion", "quantity": "1", "unit": "", "prep_note": "very finely minced"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "chives", "quantity": "2", "unit": "tbsp", "prep_note": "minced, for garnish"}
        ],
        "instructions": [
            {"step": 1, "text": "If using farmer's cheese, press in cheesecloth for 1 hour to remove excess moisture."},
            {"step": 2, "text": "In a large bowl, combine softened butter and drained cheese. Mix until smooth."},
            {"step": 3, "text": "Add paprika, caraway seeds, mustard, and salt. Mix thoroughly."},
            {"step": 4, "text": "Fold in capers and minced onion."},
            {"step": 5, "text": "Taste and adjust seasoning. Traditional Liptauer is boldly flavored."},
            {"step": 6, "text": "Pack into a crock or bowl. Smooth the top."},
            {"step": 7, "text": "Cover and refrigerate overnight to allow flavors to meld."},
            {"step": 8, "text": "Before serving, bring to room temperature for best spreadability."},
            {"step": 9, "text": "Garnish with chives and extra paprika."},
            {"step": 10, "text": "Serve with rye bread, radishes, and beer or wine. Stores refrigerated for 1 week."}
        ],
        "temperature": "Served at room temperature",
        "notes": [
            "The base should be sheep milk cheese (bryndza) for authenticity",
            "Liptauer is called 'Liptói túró' in Hungarian",
            "Some versions add anchovies or anchovy paste",
            "The orange-red color comes from paprika",
            "A classic beer garden and wine tavern spread"
        ],
        "tags": ["cheese", "cheesemaking", "hungarian", "austrian", "slovak", "liptauer", "cheese-spread", "paprika", "traditional"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-tvaroh-czech",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tvaroh (Czech Quark-Style Fresh Cheese)",
        "category": "mains",
        "attribution": "Traditional Czech and Central European",
        "source_note": "Modernized from traditional Czech methods, adapted for home cheesemaking",
        "description": "Central Europe's essential fresh cheese, tvaroh (twaróg in Polish, topfen in German) is the base for countless dishes from cheesecakes to dumplings. Tangy and fresh, it's made by simply souring milk and gently heating to separate curds. Every Czech grandmother has her own method.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "15 minutes",
        "cook_time": "45 minutes",
        "total_time": "1 hour plus 24-48 hours souring",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and buttermilk in a large jar or pot. Cover loosely."},
            {"step": 2, "text": "Leave at room temperature for 24-48 hours until fully thickened and soured."},
            {"step": 3, "text": "The milk should be thick like yogurt and taste pleasantly tangy."},
            {"step": 4, "text": "Pour soured milk into a pot. Heat very gently over low heat."},
            {"step": 5, "text": "Slowly raise temperature to 110-120°F (43-49°C). Curds will begin separating."},
            {"step": 6, "text": "Do not stir vigorously - just gently move the mass occasionally."},
            {"step": 7, "text": "When curds have clearly separated from yellowish whey, remove from heat."},
            {"step": 8, "text": "Pour into cheesecloth-lined colander. Drain for 2-4 hours."},
            {"step": 9, "text": "The longer you drain, the drier the tvaroh. For baking, drain until quite dry."},
            {"step": 10, "text": "Add salt if desired. Use in koláče (sweet rolls), buchty, dumplings, or eat fresh."}
        ],
        "temperature": "110-120°F (43-49°C)",
        "notes": [
            "Tvaroh is essential for Czech sweet baking - koláče, buchty, tvarohové knedlíky",
            "Different moisture levels suit different recipes",
            "Can be sweetened for dessert or kept plain for savory dishes",
            "Very similar to German quark and Polish twaróg",
            "Some recipes add a bit of rennet for firmer curds"
        ],
        "tags": ["cheese", "cheesemaking", "czech", "central-european", "tvaroh", "quark", "fresh-cheese", "baking-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-sirene-bulgarian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sirene (Bulgarian White Brine Cheese)",
        "category": "mains",
        "attribution": "Ancient Bulgarian/Balkan tradition",
        "source_note": "Modernized from traditional Bulgarian methods, adapted for home cheesemaking",
        "description": "Bulgaria's national cheese, sirene has been made in the Balkans for millennia. Similar to feta but typically made from cow's milk (or mixed), it's stored in brine and has a tangy, salty character. Essential in shopska salata and Bulgarian breakfast.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus overnight pressing and brining",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "cow, sheep, or mixed"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "or Bulgarian yogurt"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "1", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride if using pasteurized."},
            {"step": 2, "text": "Add culture (Bulgarian yogurt works well for authentic flavor). Ripen 45 minutes."},
            {"step": 3, "text": "Add diluted rennet. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes at 86°F. Curds should remain moist."},
            {"step": 6, "text": "Line colander with cheesecloth. Ladle curds into cloth."},
            {"step": 7, "text": "Tie corners and hang to drain for 4-6 hours or overnight."},
            {"step": 8, "text": "Transfer to mold and press lightly (10 lbs) for 4-6 hours, flipping once."},
            {"step": 9, "text": "Make brine: dissolve 1 cup salt in 1 gallon water. Submerge cheese."},
            {"step": 10, "text": "Store in brine refrigerated. Ready to eat in 2-3 days. Keeps for months in brine."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Sirene is crumblier than feta due to different culture and process",
            "Sheep milk sirene is prized; cow milk is more common",
            "Essential in Bulgarian shopska salata - tomatoes, cucumber, peppers, sirene",
            "Bulgarian yogurt as culture gives authentic tang",
            "Often eaten for breakfast with honey and bread"
        ],
        "tags": ["cheese", "cheesemaking", "bulgarian", "balkan", "sirene", "brine-cheese", "white-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-telemea-romanian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Telemea (Romanian White Brine Cheese)",
        "category": "mains",
        "attribution": "Traditional Romanian/Balkan",
        "source_note": "Modernized from traditional Romanian methods, adapted for home cheesemaking",
        "description": "Romania's beloved white brine cheese, telemea is made from sheep, cow, or goat milk and stored in brine. It's similar to feta but has its own character, especially when made from Romanian sheep breeds. Essential in mămăligă cu brânză (polenta with cheese).",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus overnight draining",
        "ingredients": [
            {"item": "whole sheep milk", "quantity": "2", "unit": "gallons", "prep_note": "or cow milk"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "1", "unit": "cup", "prep_note": "for brine and dry salting"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and culture. Ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45-60 minutes until firm clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Stir gently for 15 minutes at 90°F."},
            {"step": 5, "text": "Pour curds and whey into cheesecloth-lined colander."},
            {"step": 6, "text": "Gather cloth and hang to drain for 6-8 hours or overnight."},
            {"step": 7, "text": "Cut the drained mass into 2-3 inch blocks."},
            {"step": 8, "text": "Dry salt blocks on all sides. Let rest 2-3 hours for salt to penetrate."},
            {"step": 9, "text": "Make brine: dissolve 1 cup salt in 1 gallon water. Place cheese blocks in brine."},
            {"step": 10, "text": "Refrigerate in brine. Ready in 1 week; keeps for months. Flavor intensifies with age."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Sheep milk telemea is traditional and most prized",
            "PDO Telemea de Ibănești is made only from sheep milk",
            "Often cubed and added to salads or crumbled over mămăligă",
            "Romanian shepherds have made telemea in mountain pastures for centuries",
            "The texture is slightly creamier than Greek feta"
        ],
        "tags": ["cheese", "cheesemaking", "romanian", "balkan", "telemea", "brine-cheese", "sheep-milk", "traditional"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-olomoucke-tvaruzky-czech",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Olomoucké Tvarůžky (Czech Ripened Cheese)",
        "category": "mains",
        "attribution": "Czech tradition from Olomouc region, since 15th century",
        "source_note": "Modernized from traditional Czech methods, adapted for home cheesemaking",
        "description": "One of the world's smelliest cheeses, Olomoucké tvarůžky (Olomouc curd cheese) has been made in Moravia since at least the 15th century. Made from skimmed milk quark, the small discs are ripened until pungent. Despite the powerful aroma, the taste is surprisingly mild.",
        "servings_yield": "About 20 small cheeses",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus 1-2 weeks ripening",
        "ingredients": [
            {"item": "skim milk tvaroh/quark", "quantity": "1", "unit": "lb", "prep_note": "well-drained and sour"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp", "prep_note": "optional, crushed"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with well-drained, sour tvaroh. Let it sit at room temperature 2-3 days to develop more acidity."},
            {"step": 2, "text": "The quark should be quite acidic and beginning to smell strong."},
            {"step": 3, "text": "Knead the acidified quark with salt (and caraway if using) until smooth."},
            {"step": 4, "text": "Form into small flat discs about 1.5 inches across and 1/2 inch thick."},
            {"step": 5, "text": "Place discs on a rack in a warm, humid location (70-75°F, high humidity)."},
            {"step": 6, "text": "Turn daily. A yellow-orange bacterial smear will develop on the surface."},
            {"step": 7, "text": "After about 1 week, the cheeses will be softening and developing strong aroma."},
            {"step": 8, "text": "Move to refrigerator to slow ripening when desired ripeness is reached."},
            {"step": 9, "text": "Young tvarůžky (1 week) are milder; older (2+ weeks) are stronger."},
            {"step": 10, "text": "Serve with bread, onions, and beer. The smell is stronger than the taste!"}
        ],
        "temperature": "70-75°F ripening, then refrigerate",
        "notes": [
            "The strong smell comes from surface bacteria, not mold",
            "Has PGI protection as a traditional Czech product",
            "First documented in Olomouc in 1452",
            "Very low in fat since made from skimmed milk",
            "Traditional pairing is with beer, bread, and raw onion"
        ],
        "tags": ["cheese", "cheesemaking", "czech", "moravian", "tvaruzky", "smelly-cheese", "ripened-cheese", "ancient", "pungent"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-bergkase-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bergkäse (Austrian Alpine Mountain Cheese)",
        "category": "mains",
        "attribution": "Ancient Austrian Alpine tradition",
        "source_note": "Modernized from traditional Austrian Alpine methods, adapted for home cheesemaking",
        "description": "Bergkäse (mountain cheese) is the generic term for hard alpine cheeses made in Austrian mountain huts during summer pasturing. Made from the rich milk of cows grazing alpine meadows, it has a smooth, dense texture and complex flavor. Every valley has its own variation.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 4-12 months aging",
        "ingredients": [
            {"item": "whole raw milk", "quantity": "3", "unit": "gallons", "prep_note": "ideally from grass-fed cows"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "omit if using raw milk"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add culture and ripen for 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 30-40 minutes until firm clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch pieces (rice-sized for hard cheese)."},
            {"step": 4, "text": "Stir while slowly raising temperature to 120-125°F (49-52°C) over 45 minutes."},
            {"step": 5, "text": "Hold at this temperature, stirring, for another 30-45 minutes until curds are very firm."},
            {"step": 6, "text": "Drain whey quickly. Pack hot curds into mold and press immediately."},
            {"step": 7, "text": "Press with 40-50 lbs for 24 hours, flipping every few hours."},
            {"step": 8, "text": "Brine in saturated salt solution for 24-48 hours."},
            {"step": 9, "text": "Air dry for 2-3 days until rind begins to form."},
            {"step": 10, "text": "Age at 55°F (13°C) and 85% humidity for 4-12 months. Rub with brine or oil weekly."}
        ],
        "temperature": "90-125°F curd, 55°F aging",
        "notes": [
            "True bergkäse is made only in summer when cows graze high alpine pastures",
            "The alpine herbs and flowers flavor the milk and cheese",
            "Vorarlberger Bergkäse has PDO protection in Austria",
            "Longer aging develops more complex, nutty flavors",
            "Traditional wheels are 30-40 kg (66-88 lbs)"
        ],
        "tags": ["cheese", "cheesemaking", "austrian", "alpine", "bergkase", "mountain-cheese", "hard-cheese", "aged-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-appenzeller-swiss",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Appenzeller (Swiss Herbal Brine-Washed Cheese)",
        "category": "mains",
        "attribution": "Swiss tradition from Appenzell, 700+ years",
        "source_note": "Modernized from traditional Swiss methods, adapted for home cheesemaking",
        "description": "One of Switzerland's oldest cheeses, Appenzeller has been made for over 700 years. Its distinctive character comes from regular washings with a secret herbal brine containing wine, herbs, and spices. The recipe for the brine is known only to a few people.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 3-6 months aging",
        "ingredients": [
            {"item": "whole raw milk", "quantity": "3", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "1/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "white wine", "quantity": "1", "unit": "cup", "prep_note": "for herbal wash"},
            {"item": "dried herbs", "quantity": "2", "unit": "tbsp", "prep_note": "thyme, savory, pepper - mix"},
            {"item": "cider vinegar", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add culture and ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 30-35 minutes until firm break."},
            {"step": 3, "text": "Cut curds to 1/4-inch. Stir while raising temperature to 118°F (48°C) over 40 minutes."},
            {"step": 4, "text": "Hold at 118°F, stirring, for 30-40 minutes until curds are firm and squeaky."},
            {"step": 5, "text": "Drain whey. Pack curds into mold and press with 40 lbs for 24 hours."},
            {"step": 6, "text": "Brine for 24 hours in saturated salt solution."},
            {"step": 7, "text": "Make herbal wash: simmer wine, vinegar, herbs, and 2 tbsp salt. Cool and strain."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90% humidity. Wash rind with herbal brine every 2-3 days."},
            {"step": 9, "text": "Continue washing and aging for 3-6 months. Rind becomes golden-brown."},
            {"step": 10, "text": "The herbal wash gives Appenzeller its distinctive aroma and flavor."}
        ],
        "temperature": "90-118°F curd, 55°F aging",
        "notes": [
            "The exact recipe for traditional Sulz (herbal brine) is a closely guarded secret",
            "Three grades: Classic (3 months), Surchoix (4-5 months), Extra (6+ months)",
            "Appenzeller is pungent - the herbal wash develops strong flavors",
            "Made in the Appenzell region of northeast Switzerland since medieval times",
            "The herbal recipe in this version is an approximation"
        ],
        "tags": ["cheese", "cheesemaking", "swiss", "appenzeller", "washed-rind", "herbal", "alpine", "aged-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": ["Herbal brine is approximation of secret recipe"]}
    },
    {
        "id": "cheesemaking-guide-rennet-types",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Guide: Understanding Rennet Types and Usage",
        "category": "mains",
        "attribution": "Home cheesemaking reference",
        "source_note": "Comprehensive guide for home cheesemakers",
        "description": "Rennet is the enzyme that coagulates milk into curds. Understanding the different types and how to use them is essential for successful cheesemaking. This guide covers animal rennet, vegetable rennet, microbial rennet, and fermentation-produced chymosin.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Animal rennet (liquid)", "quantity": "", "unit": "", "prep_note": "Traditional, from calf stomach"},
            {"item": "Animal rennet (tablet)", "quantity": "", "unit": "", "prep_note": "Convenient dry form"},
            {"item": "Vegetable rennet", "quantity": "", "unit": "", "prep_note": "From thistle, cardoon, fig, or nettle"},
            {"item": "Microbial rennet", "quantity": "", "unit": "", "prep_note": "From Rhizomucor miehei mold"},
            {"item": "FPC (fermentation-produced chymosin)", "quantity": "", "unit": "", "prep_note": "Bioengineered, identical to calf rennet"}
        ],
        "instructions": [
            {"step": 1, "text": "ANIMAL RENNET: The traditional choice, extracted from the fourth stomach of calves. Produces excellent curd and is best for long-aged cheeses. Liquid form: typically 1/4 to 1/2 tsp per gallon. Tablet form: 1/4 tablet per gallon. NOT vegetarian."},
            {"step": 2, "text": "VEGETABLE RENNET: Plant-based coagulants from thistle (cardoon), fig latex, or nettle. Thistle rennet is traditional in Portuguese and Spanish cheeses (Serra da Estrela, Torta del Casar). May impart bitter notes in long-aged cheeses. Best for fresh to medium-aged cheeses."},
            {"step": 3, "text": "MICROBIAL RENNET: Produced by certain molds (Rhizomucor miehei). Vegetarian but may cause bitter flavors in cheeses aged over 6 months. Good for fresh and short-aged cheeses. Widely available and inexpensive."},
            {"step": 4, "text": "FPC (Fermentation-Produced Chymosin): Identical to calf chymosin but produced by bioengineered microbes. Vegetarian (no animal harm), performs like animal rennet even in long aging. The most common rennet in commercial cheesemaking. Excellent choice for home use."},
            {"step": 5, "text": "DILUTION: Always dilute rennet in cool, non-chlorinated water before adding to milk. Use about 1/4 cup water per 1/4 tsp rennet. Never add undiluted rennet directly to milk."},
            {"step": 6, "text": "WATER QUALITY: Chlorine in tap water can deactivate rennet. Use bottled, filtered, or boiled-and-cooled water."},
            {"step": 7, "text": "STORAGE: Liquid rennet loses potency over time. Store in refrigerator. Use within 1 year of opening. Tablets last longer - store cool and dry."},
            {"step": 8, "text": "DOSAGE ADJUSTMENT: If your rennet is old or your milk is particularly cold, you may need more. If milk is high in protein (sheep, goat), you may need less. Always test set before cutting."},
            {"step": 9, "text": "SET TIME: Normal set is 30-60 minutes. If not set in 90 minutes, rennet may be weak or milk may have issues. A 'clean break' means the curd splits cleanly when cut with knife."},
            {"step": 10, "text": "TROUBLESHOOTING: Weak set - try more rennet, warmer milk, or longer ripening. Ultra-pasteurized milk won't set properly - avoid it. High-acid milk sets faster; adjust timing accordingly."}
        ],
        "temperature": "Add rennet at 86-95°F depending on recipe",
        "notes": [
            "For kosher/halal cheese: FPC and vegetable rennet are acceptable",
            "For vegetarian cheese: FPC, microbial, or vegetable rennet",
            "Traditional European PDO cheeses often require animal rennet",
            "Thistle rennet creates unique flavors prized in Iberian cheeses",
            "FPC accounts for over 90% of commercial cheese production worldwide"
        ],
        "tags": ["cheese", "cheesemaking", "guide", "rennet", "reference", "vegetarian", "technique"],
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
