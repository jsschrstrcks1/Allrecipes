#!/usr/bin/env python3
"""Add batch 67 - Ancient and Traditional Scandinavian cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-gamalost-norwegian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gamalost (Norwegian Ancient Cheese)",
        "category": "mains",
        "attribution": "Ancient Norwegian tradition, dating to Viking era",
        "source_note": "Modernized from traditional Norwegian methods, adapted for home cheesemaking",
        "description": "One of Norway's oldest cheeses, gamalost (meaning 'old cheese') was being made before the Viking age. This pungent, protein-rich cheese is made from sour skimmed milk and develops a brown, moldly rind. Vikings likely carried it on long voyages - it's nearly pure protein with minimal fat.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus 4-6 weeks aging",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine skim milk with buttermilk. Leave at room temperature for 24-48 hours until fully soured and thickened."},
            {"step": 2, "text": "Pour soured milk into pot. Heat slowly to 145°F (63°C), stirring occasionally."},
            {"step": 3, "text": "Curds will form and separate from whey. Continue heating until curds are clearly separated."},
            {"step": 4, "text": "Pour through cheesecloth-lined colander. Let drain thoroughly, at least 2 hours."},
            {"step": 5, "text": "Gather cloth and press curds into a compact mass. Press with weight overnight."},
            {"step": 6, "text": "The cheese will be very firm due to low fat content."},
            {"step": 7, "text": "Salt the surface. Place in a warm, humid location (70°F/21°C)."},
            {"step": 8, "text": "Natural molds (including internal blue-green) will develop over 1-2 weeks. Turn daily."},
            {"step": 9, "text": "After mold develops, move to cooler aging (55°F/13°C) for 4-6 weeks."},
            {"step": 10, "text": "Aged gamalost becomes very pungent and crumbly. An acquired taste, intensely flavored."}
        ],
        "temperature": "145°F curd, 70°F initial aging, 55°F final aging",
        "notes": [
            "Gamalost has been made in Norway for over 1,000 years",
            "Nearly 50% protein, very low fat - a survival food",
            "Vikings likely carried gamalost on voyages for its nutrition and keeping qualities",
            "The strong flavor and aroma is not for everyone - very much an acquired taste",
            "Production nearly died out in 20th century, now being preserved by artisans"
        ],
        "tags": ["cheese", "cheesemaking", "norwegian", "scandinavian", "viking", "ancient", "blue-cheese", "aged-cheese", "low-fat"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-pultost-norwegian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pultost (Norwegian Caraway Curd Cheese)",
        "category": "mains",
        "attribution": "Ancient Norwegian tradition",
        "source_note": "Modernized from traditional Norwegian methods, adapted for home cheesemaking",
        "description": "A spreadable sour milk cheese from Norway, pultost is made from soured buttermilk curds mixed with caraway seeds. The texture is soft and spreadable, the flavor tangy and earthy from the caraway. This simple farm cheese has sustained Norwegian families for generations.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "1.5 hours plus overnight draining",
        "ingredients": [
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "gallon", "prep_note": "or soured milk"},
            {"item": "caraway seeds", "quantity": "2", "unit": "tbsp", "prep_note": "crushed slightly"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "to taste"},
            {"item": "cream", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for richness"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour buttermilk into heavy pot. Heat slowly over low heat."},
            {"step": 2, "text": "As temperature rises, curds will form. Heat to 160°F (71°C) but do not boil."},
            {"step": 3, "text": "When curds clearly separate from thin whey, remove from heat."},
            {"step": 4, "text": "Pour through fine cheesecloth-lined colander. Let drain 1-2 hours."},
            {"step": 5, "text": "Transfer drained curds to bowl. The texture should be like thick cottage cheese."},
            {"step": 6, "text": "Add caraway seeds and salt. Mix well."},
            {"step": 7, "text": "For creamier texture, mix in a little cream."},
            {"step": 8, "text": "Pack into small crock or jar. Press down to remove air pockets."},
            {"step": 9, "text": "Cover and refrigerate. The flavor develops over 1-2 days."},
            {"step": 10, "text": "Spread on Norwegian flatbread (flatbrød) or crackers. Keeps refrigerated 2 weeks."}
        ],
        "temperature": "160°F (71°C)",
        "notes": [
            "Caraway is traditional in many Scandinavian cheeses",
            "Pultost is a farmhouse cheese - every farm had its own variation",
            "Similar to German quark or American cottage cheese",
            "Can be aged further to develop stronger flavors",
            "Often eaten for breakfast with coffee"
        ],
        "tags": ["cheese", "cheesemaking", "norwegian", "scandinavian", "pultost", "caraway", "fresh-cheese", "spreadable"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-brunost-norwegian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brunost (Norwegian Brown Whey Cheese)",
        "category": "mains",
        "attribution": "Traditional Norwegian/Scandinavian",
        "source_note": "Modernized from traditional Norwegian methods, adapted for home cheesemaking",
        "description": "Norway's iconic brown cheese is not a true cheese but a caramelized whey product. The long cooking concentrates whey sugars (lactose) into a sweet, fudgy spread with a distinctive brown color. Essential on Norwegian breakfast tables, it's made from the whey left over from cheesemaking.",
        "servings_yield": "About 8 oz",
        "prep_time": "15 minutes",
        "cook_time": "2-3 hours",
        "total_time": "3 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1/2", "unit": "gallon", "prep_note": "from cheesemaking"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richness"},
            {"item": "goat milk", "quantity": "1", "unit": "cup", "prep_note": "optional, for traditional flavor"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine whey with cream (and goat milk if using) in a large, heavy pot."},
            {"step": 2, "text": "Bring to a simmer over medium heat, stirring occasionally."},
            {"step": 3, "text": "Reduce heat and simmer, stirring frequently, for 2-3 hours."},
            {"step": 4, "text": "The mixture will reduce dramatically - watch carefully and stir more often as it thickens."},
            {"step": 5, "text": "As liquid evaporates, the sugars will begin to caramelize, turning mixture tan, then brown."},
            {"step": 6, "text": "When very thick and mahogany brown (will coat spoon thickly), test by dropping a bit in cold water."},
            {"step": 7, "text": "If it forms a soft ball in cold water, it's ready. Remove from heat immediately."},
            {"step": 8, "text": "Beat vigorously with wooden spoon as it cools to prevent crystallization. This creates smooth texture."},
            {"step": 9, "text": "Pour into mold or container while still pourable. It will set as it cools."},
            {"step": 10, "text": "Slice thin with cheese plane and eat on bread or waffles. Store refrigerated."}
        ],
        "temperature": "Simmer until thick (approx 220°F when done)",
        "notes": [
            "Brunost is not technically cheese - it's caramelized whey",
            "Gjetost (goat whey version) has stronger, more complex flavor",
            "Invented as a way to use whey by-product from cheesemaking",
            "Norwegians consider it a breakfast staple - especially with waffles",
            "Be very careful of burning as it thickens - stir constantly at the end"
        ],
        "tags": ["cheese", "cheesemaking", "norwegian", "scandinavian", "brunost", "gjetost", "whey-cheese", "caramelized", "sweet"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-gammelost-faroese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Faroese Skerpikjøt-style Cheese (Aged Fermented)",
        "category": "mains",
        "attribution": "Faroe Islands tradition",
        "source_note": "Modernized from traditional Faroese methods, adapted for home cheesemaking",
        "description": "The Faroe Islands have a tradition of fermenting and air-drying foods in the cold, windy climate. This cheese uses similar principles - made from sour milk, it's dried in the harsh sea air until intensely flavored. The result is similar to Norwegian gamalost but with Faroese character.",
        "servings_yield": "About 12 oz",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus weeks of drying",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or low-fat milk"},
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix milk with buttermilk. Leave at room temperature 48 hours until fully soured."},
            {"step": 2, "text": "Heat soured milk gently to 140°F (60°C). Curds will separate."},
            {"step": 3, "text": "Drain through cloth. Let drip for 2 hours."},
            {"step": 4, "text": "Squeeze cloth firmly to remove as much moisture as possible."},
            {"step": 5, "text": "Salt the curds well and pack into small molds or shape into balls."},
            {"step": 6, "text": "Press firmly overnight. Remove from mold."},
            {"step": 7, "text": "Place in a cold, well-ventilated area with high humidity - traditional Faroese hjallur (drying house)."},
            {"step": 8, "text": "For home production: hang in cool basement or refrigerator with door cracked, or use wine fridge."},
            {"step": 9, "text": "Dry for 4-8 weeks. Natural molds may develop - this is traditional."},
            {"step": 10, "text": "Cheese becomes very hard and intensely flavored. Shave thin or grate over dishes."}
        ],
        "temperature": "140°F curd, cold windy drying",
        "notes": [
            "Faroese food culture relies heavily on wind-drying and fermentation",
            "The harsh North Atlantic climate provides natural refrigeration and drying",
            "Similar in concept to skerpikjøt (wind-dried mutton)",
            "The strong flavor reflects the Faroese taste for fermented foods",
            "Very much an acquired taste for those not raised with it"
        ],
        "tags": ["cheese", "cheesemaking", "faroese", "scandinavian", "fermented", "air-dried", "ancient", "wind-dried"],
        "confidence": {"overall": "medium", "flags": ["Reconstructed traditional recipe"]}
    },
    {
        "id": "traditional-danish-blue-style",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Danish Blue Style Cheese (Danablu)",
        "category": "mains",
        "attribution": "Danish tradition, early 20th century",
        "source_note": "Modernized from traditional Danish methods, adapted for home cheesemaking",
        "description": "While Danish Blue was developed in the early 1900s as Denmark's answer to Roquefort, it has become a classic in its own right. Made from cow's milk rather than sheep's, it has a creamier texture and milder blue flavor. This home version captures its essential character.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 3-4 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richness"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "blue mold"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 90°F (32°C). Add calcium chloride."},
            {"step": 2, "text": "Add mesophilic culture and Penicillium roqueforti. Stir well. Ripen 1 hour."},
            {"step": 3, "text": "Add diluted rennet. Let set 1-1.5 hours until clean break (soft set for blue)."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir very gently for 30 minutes at 90°F. Curds should remain large and moist."},
            {"step": 6, "text": "Drain whey. Gently ladle curds into tall cylindrical mold (no pressing)."},
            {"step": 7, "text": "Flip every 30 minutes for 4 hours, then let drain overnight at room temperature."},
            {"step": 8, "text": "Remove from mold. Rub salt on all surfaces. Rest 24 hours. Repeat salting."},
            {"step": 9, "text": "After 5 days, pierce cheese through with knitting needle or skewer in grid pattern."},
            {"step": 10, "text": "Age at 50°F (10°C) and 95% humidity for 3-4 months. Blue veins develop in piercings."}
        ],
        "temperature": "90°F curd, 50°F aging",
        "notes": [
            "Danish Blue was created by Marius Boel in the early 1900s",
            "The added cream creates a creamier, milder blue than Roquefort",
            "Piercing allows air into the cheese for mold to grow",
            "High humidity is crucial - blue molds need moisture",
            "Milder than Roquefort, sharper than Gorgonzola"
        ],
        "tags": ["cheese", "cheesemaking", "danish", "scandinavian", "blue-cheese", "danablu", "aged-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-havarti-danish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Havarti (Danish Washed-Curd Cheese)",
        "category": "mains",
        "attribution": "Danish tradition, 19th century",
        "source_note": "Modernized from traditional Danish methods, adapted for home cheesemaking",
        "description": "Created by Hanne Nielsen in the 1800s, Havarti is Denmark's most famous cheese export. The washed-curd technique removes lactose, creating a buttery, mild cheese with small irregular holes. Creamy and versatile, it's become a worldwide favorite for sandwiches and snacking.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 2-3 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "flora danica ideal"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride. Add culture and ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Stir gently for 10 minutes at 86°F."},
            {"step": 5, "text": "CURD WASHING: Drain off 1/3 of the whey. Replace with same amount of 86°F water."},
            {"step": 6, "text": "This washing removes lactose and creates Havarti's sweet, mild flavor."},
            {"step": 7, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 8, "text": "Drain whey. Pack curds loosely into molds. Press lightly (15 lbs) for 30 minutes."},
            {"step": 9, "text": "Flip and press with 30 lbs for 4 hours, then 50 lbs overnight."},
            {"step": 10, "text": "Brine for 12 hours. Age at 55°F (13°C) and 85% humidity for 2-3 months."}
        ],
        "temperature": "86-100°F curd, 55°F aging",
        "notes": [
            "Hanne Nielsen developed Havarti at her farm in the 1800s",
            "Curd washing is the key technique - it removes lactose, reducing sharpness",
            "The irregular holes are from the loose packing, not added gas",
            "Can be made with added dill, caraway, or other flavors",
            "Cream Havarti has added cream for extra richness"
        ],
        "tags": ["cheese", "cheesemaking", "danish", "scandinavian", "havarti", "washed-curd", "buttery", "mild"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-adelost-swedish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ädelost (Swedish Noble Blue Cheese)",
        "category": "mains",
        "attribution": "Swedish tradition, 20th century",
        "source_note": "Modernized from traditional Swedish methods, adapted for home cheesemaking",
        "description": "Sweden's answer to French blue cheese, ädelost (noble cheese) was developed in the early 20th century. Made from pasteurized cow's milk with added cream, it's milder and creamier than Roquefort but still has good blue character. It has become an essential cheese on Swedish holiday tables.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 3 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "heavy cream", "quantity": "2", "unit": "cups", "prep_note": "for richness"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 88°F (31°C). Add calcium chloride."},
            {"step": 2, "text": "Add mesophilic culture and Penicillium roqueforti. Stir well. Ripen 45 minutes."},
            {"step": 3, "text": "Add diluted rennet. Let set 1 hour until soft clean break."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Large curds retain moisture for creamy texture."},
            {"step": 5, "text": "Stir very gently for 20 minutes at 88°F. Keep curds large and moist."},
            {"step": 6, "text": "Drain whey. Gently ladle curds into molds without pressing."},
            {"step": 7, "text": "Flip every 30 minutes for 4 hours. Leave at room temperature overnight."},
            {"step": 8, "text": "Dry salt all surfaces. Rest 24 hours, then salt again. Repeat for 5 days."},
            {"step": 9, "text": "Pierce thoroughly with skewer in rows. Age at 46-50°F (8-10°C) and 95% humidity."},
            {"step": 10, "text": "Turn twice weekly. Blue develops in 4-6 weeks. Full flavor at 3 months."}
        ],
        "temperature": "88°F curd, 46-50°F aging",
        "notes": [
            "Ädelost means 'noble cheese' in Swedish",
            "The extra cream creates a milder, more approachable blue",
            "Traditional on Swedish Christmas smörgåsbord",
            "Pairs well with Swedish crispbread and fruit",
            "Swedish blue is generally milder than Danish Blue"
        ],
        "tags": ["cheese", "cheesemaking", "swedish", "scandinavian", "blue-cheese", "adelost", "noble-cheese", "aged-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-juustoleipa-finnish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Juustoleipä (Finnish Squeaky Cheese)",
        "category": "mains",
        "attribution": "Ancient Finnish/Scandinavian tradition",
        "source_note": "Modernized from traditional Finnish methods, adapted for home cheesemaking",
        "description": "Also called 'bread cheese' or leipäjuusto, this unique Finnish cheese is traditionally made from the rich colostrum of cows that have just calved. The fresh cheese is baked until golden-spotted, creating a squeaky texture when bitten. Traditionally served warm with cloudberry jam.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "1.5 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "or colostrum if available"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "to mimic colostrum richness"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 100°F (38°C)."},
            {"step": 2, "text": "Add salt and stir. Add diluted rennet and stir gently for 30 seconds."},
            {"step": 3, "text": "Let set for 30-45 minutes until clean break achieved."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Stir gently for 5 minutes."},
            {"step": 5, "text": "Pour into cheesecloth-lined colander. Drain for 10 minutes."},
            {"step": 6, "text": "Transfer curds to a wide, shallow pan (traditionally a wooden form). Press flat."},
            {"step": 7, "text": "Traditionally, place near fire; modernly, broil in oven."},
            {"step": 8, "text": "Broil 4-6 inches from heat until top is spotted golden-brown, 5-10 minutes."},
            {"step": 9, "text": "Flip and brown the other side."},
            {"step": 10, "text": "Serve warm with cloudberry jam or lingonberry. Also delicious dipped in coffee."}
        ],
        "temperature": "100°F curd, broil to finish",
        "notes": [
            "Traditionally made from colostrum, the first milk after a cow gives birth",
            "The high protein in colostrum creates the squeaky texture",
            "Called 'squeaky cheese' because it squeaks against teeth",
            "Originated in northern Finland and Sweden (Lapland region)",
            "Now commercially made from regular milk with similar technique"
        ],
        "tags": ["cheese", "cheesemaking", "finnish", "scandinavian", "juustoleipa", "bread-cheese", "squeaky-cheese", "baked-cheese", "ancient"],
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
