#!/usr/bin/env python3
"""Add batch 66 - Ancient British Isles and Celtic cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-caerphilly-welsh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caerphilly (Welsh Miners' Cheese)",
        "category": "mains",
        "attribution": "Welsh tradition, named after Caerphilly town",
        "source_note": "Modernized from traditional Welsh methods, adapted for home cheesemaking",
        "description": "A crumbly, moist cheese that was traditionally the staple of Welsh coal miners - it could be eaten in the pit with bare, coal-dusty hands without dirtying the cheese. Made quickly and eaten young, it was Wales's answer to the miners' need for portable, nutritious food.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 2-3 weeks aging",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and stir. Add culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set for 45 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes, then gently stir for 10 minutes."},
            {"step": 4, "text": "Slowly raise temperature to 92°F (33°C) over 20 minutes. This is only slightly warmed."},
            {"step": 5, "text": "Continue stirring for 30 minutes as curds firm. The lower temperature keeps moisture in."},
            {"step": 6, "text": "Drain most whey. Pile curds at side of pot and let them mat together for 30 minutes."},
            {"step": 7, "text": "Cut matted curds into blocks and stack. Flip every 15 minutes for 1 hour (cheddaring)."},
            {"step": 8, "text": "Mill curds into small pieces. Salt with 1 tbsp and mix well."},
            {"step": 9, "text": "Pack into mold and press with 20 lbs for 1 hour, flip, then 40 lbs overnight."},
            {"step": 10, "text": "Brine for 12 hours. Age at 55°F (13°C) and 90% humidity for only 2-3 weeks. Eat young and fresh."}
        ],
        "temperature": "90-92°F curd, 55°F aging",
        "notes": [
            "Traditional Caerphilly is eaten very young - just 2-3 weeks old",
            "The crumbly, moist texture was ideal for eating without utensils",
            "Miners needed high-salt, high-moisture cheese to replace minerals lost sweating",
            "Now mostly made in Somerset, England rather than Wales",
            "Modern versions sometimes age longer with a wrinkly, natural rind"
        ],
        "tags": ["cheese", "cheesemaking", "welsh", "british", "caerphilly", "miners-cheese", "crumbly-cheese", "young-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-lancashire-british",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Lancashire (Two-Day Curd Cheese)",
        "category": "mains",
        "attribution": "English tradition from Lancashire county",
        "source_note": "Modernized from traditional Lancashire methods, adapted for home cheesemaking",
        "description": "A unique English cheese made by combining curds from two or three days' milkings - an ancient farmhouse technique that created a cheese with complex texture and buttery flavor. This 'two-day curd' method produces Lancashire's characteristic creamy yet crumbly texture.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1 hour per day",
        "cook_time": "3 hours",
        "total_time": "2 days of curd-making plus 4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "day 1"},
            {"item": "whole cow milk", "quantity": "1", "unit": "gallon", "prep_note": "day 2"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "per day"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "per day, diluted"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "per day, diluted"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Heat 1 gallon milk to 86°F (30°C). Add calcium chloride and culture. Ripen 45 minutes."},
            {"step": 2, "text": "Add rennet and let set 1 hour. Cut into 1/2-inch cubes. Stir gently 30 minutes at 86°F."},
            {"step": 3, "text": "Drain whey from day 1 curds. Salt lightly and refrigerate overnight."},
            {"step": 4, "text": "DAY 2: Repeat with second gallon of milk - heat, culture, rennet, cut, stir, drain."},
            {"step": 5, "text": "Break up day 1 curds (they will be more acidic now). Combine with fresh day 2 curds."},
            {"step": 6, "text": "Mix both days' curds together thoroughly. Add remaining salt."},
            {"step": 7, "text": "Pack combined curds into mold. Press with 30 lbs for 24 hours, flipping every 6 hours."},
            {"step": 8, "text": "Remove from mold. The mixed-age curds create Lancashire's unique texture."},
            {"step": 9, "text": "Bandage with cheesecloth and lard, or develop natural rind."},
            {"step": 10, "text": "Age at 55°F (13°C) for 4-8 weeks. Creamy Lancashire is younger; Tasty Lancashire ages longer."}
        ],
        "temperature": "86°F curd, 55°F aging",
        "notes": [
            "The two-day curd method is unique to Lancashire cheesemaking",
            "Different acid levels in the curds create complex texture",
            "Creamy Lancashire (young) is buttery and spreadable",
            "Tasty Lancashire (aged) is more crumbly with sharper flavor",
            "Excellent melting cheese - traditional on toast or in pies"
        ],
        "tags": ["cheese", "cheesemaking", "english", "british", "lancashire", "two-day-curd", "crumbly-cheese", "farmhouse"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-wensleydale-british",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Wensleydale (Yorkshire Monastery Cheese)",
        "category": "mains",
        "attribution": "English tradition from Wensleydale, Yorkshire",
        "source_note": "Modernized from traditional Yorkshire methods dating to 12th century, adapted for home cheesemaking",
        "description": "Brought to Yorkshire by Cistercian monks from France in 1150, Wensleydale was originally made from sheep's milk. The monks' blue-veined cheese evolved over centuries into today's crumbly white cheese. Now famous paired with Christmas cake and made even more popular by Wallace and Gromit.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 3-4 weeks aging",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep's milk for traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride if using pasteurized. Add culture and ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set for 45 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly stir for 30 minutes while raising temperature very gently to 90°F (32°C)."},
            {"step": 5, "text": "Let curds settle. Drain off whey to level of curds."},
            {"step": 6, "text": "Pile curds at side of pot. Let them mat for 15 minutes, then cut and stack (brief cheddaring)."},
            {"step": 7, "text": "Mill curds into walnut-sized pieces. Add salt and mix gently."},
            {"step": 8, "text": "Pack into mold loosely - don't compress too much. Press lightly (10 lbs) for 6 hours."},
            {"step": 9, "text": "Flip and press with 20 lbs overnight. The light pressing keeps the open texture."},
            {"step": 10, "text": "Age at 52°F (11°C) and high humidity for 3-4 weeks. Wensleydale is eaten young and moist."}
        ],
        "temperature": "86-90°F curd, 52°F aging",
        "notes": [
            "Cistercian monks brought cheesemaking to Wensleydale in 1150",
            "Originally made from sheep's milk and naturally blued",
            "Modern Wensleydale is cow's milk and not blued (usually)",
            "Traditionally eaten with fruitcake at Christmas",
            "Wallace and Gromit made 'Wensleydale, Gromit!' famous"
        ],
        "tags": ["cheese", "cheesemaking", "english", "british", "yorkshire", "wensleydale", "monastery-cheese", "crumbly-cheese", "medieval"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-dunlop-scottish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Dunlop (Scottish Farmhouse Cheese)",
        "category": "mains",
        "attribution": "Scottish tradition from Ayrshire",
        "source_note": "Modernized from traditional Scottish methods, adapted for home cheesemaking",
        "description": "Scotland's oldest native cheese, Dunlop was developed in the 17th century by Barbara Gilmour, who learned cheesemaking in Ireland and brought the technique to Ayrshire. Made from Ayrshire cow milk, it's milder than cheddar with a close, buttery texture.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "5 hours plus 2-6 months aging",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "Ayrshire if available"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "1.5", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add calcium chloride and culture. Ripen for 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set for 45-60 minutes until firm clean break."},
            {"step": 3, "text": "Cut curd into 3/8-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Stir gently while slowly raising temperature to 100°F (38°C) over 40 minutes."},
            {"step": 5, "text": "Continue stirring at 100°F for 30 minutes until curds are firm."},
            {"step": 6, "text": "Drain whey. Pile curds and let mat for 20 minutes."},
            {"step": 7, "text": "Cut and stack curd blocks (cheddaring) for 1.5 hours, flipping every 15-20 minutes."},
            {"step": 8, "text": "Mill curds and add salt. Mix well."},
            {"step": 9, "text": "Pack into mold. Press with 30 lbs for 1 hour, then 50 lbs for 24 hours."},
            {"step": 10, "text": "Bandage with cloth and age at 55°F (13°C) for 2-6 months."}
        ],
        "temperature": "88-100°F curd, 55°F aging",
        "notes": [
            "Barbara Gilmour (c. 1650) is credited with creating Dunlop cheese",
            "Milder and moister than cheddar due to lower cooking temperature",
            "Ayrshire cows produce especially rich milk for cheese",
            "Almost disappeared in the 20th century, now being revived",
            "The close texture made it ideal for slicing for sandwiches"
        ],
        "tags": ["cheese", "cheesemaking", "scottish", "british", "dunlop", "farmhouse-cheese", "ayrshire"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-caboc-scottish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caboc (Scottish Highland Double Cream Cheese)",
        "category": "mains",
        "attribution": "Ancient Scottish Highland tradition",
        "source_note": "Modernized from traditional Highland methods, adapted for home cheesemaking",
        "description": "One of Scotland's oldest cheeses, caboc was said to be created by Mariota de Ile, daughter of a 15th-century MacDonald chieftain. This rich double-cream cheese is rolled in toasted pinhead oatmeal, giving it a uniquely Scottish character. The recipe was passed down through the MacDonald clan.",
        "servings_yield": "About 12 oz cheese",
        "prep_time": "20 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour plus overnight draining",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "quart", "prep_note": "full-fat"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "buttermilk", "quantity": "2", "unit": "tbsp", "prep_note": "as culture"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "pinhead oatmeal", "quantity": "1/2", "unit": "cup", "prep_note": "toasted, for coating"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cream and milk in pot. Heat gently to 75°F (24°C) - barely warm."},
            {"step": 2, "text": "Stir in buttermilk. Cover and leave at room temperature for 24-48 hours."},
            {"step": 3, "text": "The mixture will thicken to a cream-cheese consistency."},
            {"step": 4, "text": "Line a colander with fine cheesecloth. Pour thickened cream into cloth."},
            {"step": 5, "text": "Gather edges and hang over bowl. Drain for 8-12 hours until thick."},
            {"step": 6, "text": "Toast pinhead oatmeal in dry pan until fragrant and golden."},
            {"step": 7, "text": "Transfer drained cheese to bowl. Add salt and mix well."},
            {"step": 8, "text": "Form cheese into a log shape about 2 inches in diameter."},
            {"step": 9, "text": "Roll the log in toasted oatmeal, pressing gently so oats adhere."},
            {"step": 10, "text": "Wrap in paper and refrigerate. Best eaten within 1 week."}
        ],
        "temperature": "75°F ripening, room temperature",
        "notes": [
            "Legend says Mariota de Ile created caboc in the 15th century",
            "The recipe was preserved by her descendants for over 500 years",
            "Susannah Stone revived commercial production in the 1960s",
            "The oatmeal coating is distinctively Scottish",
            "Very rich (69% butterfat) - a little goes a long way"
        ],
        "tags": ["cheese", "cheesemaking", "scottish", "highland", "caboc", "cream-cheese", "oatmeal", "ancient", "clan-recipe"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-crowdie-scottish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Crowdie (Scottish Cottage Cheese)",
        "category": "mains",
        "attribution": "Ancient Scottish/Celtic tradition",
        "source_note": "Modernized from traditional Scottish methods, adapted for home cheesemaking",
        "description": "Scotland's ancient fresh cheese, crowdie dates back over 1,000 years to Viking times or earlier. Made by simply souring milk and draining the curds, it's the foundation of Scottish dairy culture. Traditionally eaten with oatcakes, it's tangy, light, and low in fat.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes plus souring time",
        "ingredients": [
            {"item": "whole or skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1/4", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "cream", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for richness"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk with buttermilk in a pot or jar. Cover loosely."},
            {"step": 2, "text": "Leave at room temperature for 24-48 hours until milk thickens and sours."},
            {"step": 3, "text": "The milk should be thick like yogurt and smell pleasantly tangy."},
            {"step": 4, "text": "Heat very gently to 110°F (43°C), just until curds begin to separate from whey."},
            {"step": 5, "text": "Do not overheat - crowdie is a delicate, fresh cheese."},
            {"step": 6, "text": "Pour through cheesecloth-lined colander. Let drain for 30 minutes."},
            {"step": 7, "text": "Gather cloth and squeeze gently - don't press too dry."},
            {"step": 8, "text": "Transfer to bowl. Break up curds with fork and add salt."},
            {"step": 9, "text": "For richer version, stir in a little cream."},
            {"step": 10, "text": "Eat fresh with oatcakes or use in traditional Scottish dishes."}
        ],
        "temperature": "110°F (43°C) maximum",
        "notes": [
            "Crowdie may be Scotland's oldest cheese, predating Viking era",
            "Traditionally made from the skimmed milk left after cream was taken for butter",
            "Similar to cottage cheese but tangier from natural souring",
            "Can be flavored with herbs, wild garlic, or pepper",
            "Gruth dhu is crowdie mixed with cream and rolled in oatmeal"
        ],
        "tags": ["cheese", "cheesemaking", "scottish", "celtic", "crowdie", "fresh-cheese", "cottage-cheese", "ancient", "viking"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-irish-cais",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Irish Cáis (Ancient Celtic Cheese)",
        "category": "mains",
        "attribution": "Ancient Irish/Celtic tradition",
        "source_note": "Reconstructed from historical references, adapted for home cheesemaking",
        "description": "Ancient Ireland had a rich cheese culture - 'cáis' was so important it appears in Brehon law and monastery records. This reconstruction of ancient Irish cheese uses simple techniques available in early Celtic times: natural souring and gentle heating. The result is a tangy fresh cheese.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes plus 24-48 hours souring",
        "ingredients": [
            {"item": "whole raw milk", "quantity": "1/2", "unit": "gallon", "prep_note": "raw if possible, or add buttermilk"},
            {"item": "buttermilk", "quantity": "1/4", "unit": "cup", "prep_note": "if using pasteurized milk"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour raw milk into a crock or jar. If using pasteurized, add buttermilk."},
            {"step": 2, "text": "Cover loosely and leave at room temperature 24-48 hours to naturally sour."},
            {"step": 3, "text": "The milk will thicken and become pleasantly tangy (like clabber or thick buttermilk)."},
            {"step": 4, "text": "Pour soured milk into pot. Heat very slowly and gently."},
            {"step": 5, "text": "As it warms, curds will separate from whey. Heat only to about 100°F (38°C)."},
            {"step": 6, "text": "Remove from heat when curds are clearly separated and floating in clear whey."},
            {"step": 7, "text": "Line colander with cloth. Gently ladle curds into cloth."},
            {"step": 8, "text": "Let drain for several hours. Don't squeeze - let gravity do the work."},
            {"step": 9, "text": "Salt the curds lightly and shape into a round."},
            {"step": 10, "text": "Eat fresh within a few days, or press and salt more heavily for longer keeping."}
        ],
        "temperature": "100°F (38°C) maximum",
        "notes": [
            "Ancient Irish Brehon law specified fines payable in cheese",
            "Monasteries were major cheesemaking centers in medieval Ireland",
            "Cáis was typically made from cow's milk, unlike Scottish crowdie which used sheep",
            "The tradition largely died out but is being revived by artisan makers",
            "Similar technique to clabber cheese or Scandinavian fresh cheeses"
        ],
        "tags": ["cheese", "cheesemaking", "irish", "celtic", "ancient", "fresh-cheese", "historical", "monastery"],
        "confidence": {"overall": "medium", "flags": ["Reconstructed historical recipe"]}
    },
    {
        "id": "traditional-gubbeen-inspired-irish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Irish Washed-Rind Cheese (Gubbeen Style)",
        "category": "mains",
        "attribution": "Modern Irish farmhouse tradition inspired by ancient methods",
        "source_note": "Modernized farmhouse recipe in traditional style, adapted for home cheesemaking",
        "description": "While specific washed-rind recipes may be modern, the tradition of washing cheese with brine or whey to develop flavor is ancient. This recipe creates a semi-soft washed-rind cheese with the pungent, meaty character found in Irish farmhouse cheeses like Gubbeen, Milleens, and Ardrahan.",
        "servings_yield": "About 1.5 lbs cheese",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4 hours plus 6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh, high-quality"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": "for orange rind"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brine and washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride, then cultures including B. linens. Ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Stir gently for 30 minutes, maintaining 90°F. Curds should remain moist."},
            {"step": 5, "text": "Drain whey. Pack curds gently into molds - do not press hard."},
            {"step": 6, "text": "Flip every 30 minutes for 2 hours, then let drain overnight at room temperature."},
            {"step": 7, "text": "Brine for 6-8 hours. Remove and place in aging environment."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity. This high humidity is essential."},
            {"step": 9, "text": "Wash rind with salt brine (3% salt solution) every 2-3 days. Orange bacteria will develop."},
            {"step": 10, "text": "Age 6-8 weeks, washing regularly. Rind becomes orange-pink; interior becomes creamy and pungent."}
        ],
        "temperature": "90°F curd, 55°F aging",
        "notes": [
            "Irish washed-rind cheeses have won world championships",
            "High humidity is crucial for B. linens to develop properly",
            "The pungent smell is normal - the taste is milder",
            "Cork and West Cork are centers of Irish artisan cheese revival",
            "These cheeses pair beautifully with Irish whiskey or cider"
        ],
        "tags": ["cheese", "cheesemaking", "irish", "washed-rind", "farmhouse-cheese", "semi-soft", "pungent"],
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
