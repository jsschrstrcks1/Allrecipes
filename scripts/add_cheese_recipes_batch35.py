#!/usr/bin/env python3
"""Add batch 35 of traditional cheese recipes - Scottish, Irish, Dutch, and more ancient cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-caboc-scottish-cream",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Caboc (Scottish Cream Cheese)",
        "category": "mains",
        "attribution": "Scottish Highlands / 15th Century",
        "source_note": "Scotland's oldest cheese, dating to the 15th century. Created by Mariota de Ile, daughter of a MacDonald clan chief.",
        "description": "Ancient Scottish cream cheese rolled in toasted oatmeal, with a rich buttery texture and distinctive nutty coating.",
        "servings_yield": "About 8 oz logs",
        "prep_time": "30 minutes",
        "cook_time": "24-48 hours draining",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "heavy cream", "quantity": "2", "unit": "cups", "prep_note": "full fat"},
            {"item": "buttermilk", "quantity": "2", "unit": "cups", "prep_note": "cultured"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "pinhead oatmeal", "quantity": "1/2", "unit": "cup", "prep_note": "toasted"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine cream and buttermilk in a pot."},
            {"step": 2, "text": "Heat gently to 75-80°F and hold for 12 hours to culture."},
            {"step": 3, "text": "Heat slowly to 170°F, stirring occasionally, until curds form."},
            {"step": 4, "text": "Line colander with cheesecloth and ladle in curds."},
            {"step": 5, "text": "Drain for 24-48 hours until thick and spreadable."},
            {"step": 6, "text": "Add salt and mix thoroughly."},
            {"step": 7, "text": "Toast pinhead oatmeal in dry pan until golden and fragrant."},
            {"step": 8, "text": "Form cheese into log shapes."},
            {"step": 9, "text": "Roll logs thoroughly in toasted oatmeal to coat."},
            {"step": 10, "text": "Refrigerate and serve within 1 week."}
        ],
        "temperature": "75-80°F culture, 170°F curdle",
        "notes": [
            "Caboc is Scotland's oldest documented cheese recipe",
            "The oatmeal coating is distinctly Scottish",
            "Best served at room temperature with oatcakes",
            "The recipe was revived in the 1960s by Susannah Stone"
        ],
        "tags": ["cheese", "traditional", "scottish", "cream", "oatmeal-coated", "15th-century", "highland"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-dunlop-scottish-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Dunlop (Scottish Cheddar-Style)",
        "category": "mains",
        "attribution": "Dunlop, Ayrshire, Scotland / 17th Century",
        "source_note": "Created by Barbara Gilmour in the 1680s after returning from Ireland. Scotland's answer to Cheddar.",
        "description": "Scottish cheddar-style cheese with a milder, creamier texture than English cheddar, made in Ayrshire since the 17th century.",
        "servings_yield": "About 2 lbs",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "Ayrshire cattle traditional"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Slowly raise temperature to 100°F over 40 minutes, stirring."},
            {"step": 7, "text": "Hold at 100°F, stirring, until curds are firm."},
            {"step": 8, "text": "Drain whey and mill curds (break into walnut-sized pieces)."},
            {"step": 9, "text": "Salt curds and mix well."},
            {"step": 10, "text": "Pack into mold and press at 40 lbs for 24 hours."},
            {"step": 11, "text": "Air dry for 3-5 days until rind forms."},
            {"step": 12, "text": "Age at 55°F, 85% humidity for 3-6 months."}
        ],
        "temperature": "86-100°F make, 55°F aging",
        "notes": [
            "Barbara Gilmour learned cheesemaking while in Ireland during Covenanter troubles",
            "Dunlop is milder and moister than English cheddar",
            "Traditional Ayrshire cattle produce ideal milk for this cheese",
            "Young Dunlop is very mild; aged develops more character"
        ],
        "tags": ["cheese", "traditional", "scottish", "cheddar-style", "ayrshire", "17th-century", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-irish-porter-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Irish Porter Cheese",
        "category": "mains",
        "attribution": "Ireland / Modern Traditional",
        "source_note": "Irish cheddar infused with Irish porter or stout, combining two beloved Irish traditions.",
        "description": "Irish cheddar marbled with dark porter or stout, creating ribbons of beer flavor throughout the cheese.",
        "servings_yield": "About 2 lbs",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": "Irish dairy preferred"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "Irish porter or stout", "quantity": "1", "unit": "cup", "prep_note": "reduced by half"}
        ],
        "instructions": [
            {"step": 1, "text": "Reduce porter to 1/2 cup over medium heat. Cool completely."},
            {"step": 2, "text": "Heat milk to 88°F."},
            {"step": 3, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 7, "text": "Raise temperature to 102°F over 40 minutes, stirring gently."},
            {"step": 8, "text": "Drain whey and mill curds."},
            {"step": 9, "text": "Salt curds and mix."},
            {"step": 10, "text": "Add half the curds to mold, drizzle with reduced porter."},
            {"step": 11, "text": "Add remaining curds, creating marbled layers."},
            {"step": 12, "text": "Press at 40 lbs for 24 hours."},
            {"step": 13, "text": "Age at 55°F for 3-6 months."}
        ],
        "temperature": "88-102°F make, 55°F aging",
        "notes": [
            "The reduced porter concentrates the malty, chocolate notes",
            "Creates distinctive dark veins running through the cheese",
            "Best paired with crusty bread and more porter",
            "Combines Ireland's dairy and brewing traditions"
        ],
        "tags": ["cheese", "traditional", "irish", "porter", "stout", "marbled", "cheddar-style", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-leyden-dutch-cumin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Leyden (Dutch Cumin Cheese)",
        "category": "mains",
        "attribution": "Leiden, Netherlands / 16th Century",
        "source_note": "Named after the city of Leiden. The cumin seeds were originally added for medicinal purposes.",
        "description": "Dutch spiced cheese with cumin and sometimes caraway seeds, featuring the crossed keys of Leiden imprinted on the rind.",
        "servings_yield": "About 3 lbs",
        "prep_time": "4 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": "for part-skim version"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": ""},
            {"item": "cumin seeds", "quantity": "3", "unit": "tbsp", "prep_note": "whole"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tbsp", "prep_note": "optional"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "annatto", "quantity": "1/4", "unit": "tsp", "prep_note": "for orange color, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 45 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Remove 1/3 of whey and add back warm water (washed curd technique)."},
            {"step": 7, "text": "Heat to 100°F over 30 minutes."},
            {"step": 8, "text": "Drain curds."},
            {"step": 9, "text": "Mix in cumin seeds, caraway if using, salt, and annatto."},
            {"step": 10, "text": "Pack into round mold and press at 40 lbs for 24 hours."},
            {"step": 11, "text": "Brine for 24 hours."},
            {"step": 12, "text": "Age at 55°F, 85% humidity for 3-12 months."},
            {"step": 13, "text": "Rub rind with oil and traditional crossed-keys stamp."}
        ],
        "temperature": "90-100°F make, 55°F aging",
        "notes": [
            "Traditional Leyden is partially skimmed for firmer texture",
            "The crossed keys of Leiden are imprinted on authentic wheels",
            "Originally made from buttermilk left from butter production",
            "Cumin was believed to aid digestion"
        ],
        "tags": ["cheese", "traditional", "dutch", "spiced", "cumin", "leiden", "16th-century", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mimolette-french-orange",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mimolette (French Orange Cheese)",
        "category": "mains",
        "attribution": "Flanders/Lille, France / 17th Century",
        "source_note": "Created in the 17th century as a French alternative to Dutch Edam. The cratered rind is created by cheese mites.",
        "description": "French orange-colored cheese with a distinctive pitted grey rind, aged to develop intense caramel and butterscotch flavors.",
        "servings_yield": "About 4 lbs ball",
        "prep_time": "4 hours",
        "cook_time": "6-24 months aging",
        "total_time": "6-24 months",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "3", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "3/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "annatto", "quantity": "1/2", "unit": "tsp", "prep_note": "for orange color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add annatto to color the milk bright orange."},
            {"step": 3, "text": "Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 5, "text": "Let set for 45 minutes."},
            {"step": 6, "text": "Cut curds into 1/4-inch pieces."},
            {"step": 7, "text": "Stir gently while raising temperature to 100°F over 30 minutes."},
            {"step": 8, "text": "Drain curds and pack into ball-shaped mold."},
            {"step": 9, "text": "Press at 30 lbs for 30 minutes, 50 lbs for 12 hours."},
            {"step": 10, "text": "Soak in saturated brine for 24 hours."},
            {"step": 11, "text": "Age at 55°F, 85% humidity for 6-24 months."},
            {"step": 12, "text": "Traditional aging introduces cheese mites which create the pitted rind."},
            {"step": 13, "text": "Brush rind regularly to control mite activity."}
        ],
        "temperature": "86-100°F make, 55°F aging",
        "notes": [
            "Louis XIV commissioned this cheese as a French alternative to Dutch Edam",
            "The bright orange color distinguishes it from foreign imports",
            "Cheese mites (Acarus siro) create the distinctive moonscape rind",
            "Aged Mimolette has intense butterscotch and hazelnut flavors"
        ],
        "tags": ["cheese", "traditional", "french", "flanders", "orange", "aged", "17th-century", "hard"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fromage-de-meaux-brie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brie de Meaux (French King of Cheeses)",
        "category": "mains",
        "attribution": "Meaux, Île-de-France / 8th Century",
        "source_note": "Called the 'King of Cheeses' by Talleyrand at the Congress of Vienna in 1815. Made near Paris since Charlemagne's time.",
        "description": "Classic French soft-ripened cheese with a bloomy white rind, creamy interior, and complex earthy, mushroom flavors.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "4-8 weeks aging",
        "total_time": "4-8 weeks",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh, full fat"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp", "prep_note": "for white rind"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "small amount"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add mesophilic culture, P. candidum, and G. candidum. Stir and ripen 1 hour."},
            {"step": 3, "text": "Add calcium chloride if needed."},
            {"step": 4, "text": "Add diluted rennet - use less than for firm cheeses."},
            {"step": 5, "text": "Let set for 1.5-2 hours until soft curd forms."},
            {"step": 6, "text": "Ladle curds very gently into large shallow molds - do not break up."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, flipping several times."},
            {"step": 8, "text": "Unmold and salt all surfaces."},
            {"step": 9, "text": "Age at 52-55°F, 90-95% humidity."},
            {"step": 10, "text": "Turn daily for first week, then every other day."},
            {"step": 11, "text": "White mold develops in 7-10 days."},
            {"step": 12, "text": "Ripen 4-8 weeks until interior is creamy from edge to center."}
        ],
        "temperature": "90°F make, 52-55°F aging",
        "notes": [
            "Traditional wheels are large (14 inches) and require enormous skill to age properly",
            "At the 1815 Congress of Vienna, Brie de Meaux was crowned King of Cheeses",
            "Interior ripens from outside in - look for cream line under rind",
            "AOC/PDO protected - must be made in specific region"
        ],
        "tags": ["cheese", "traditional", "french", "brie", "soft-ripened", "bloomy-rind", "8th-century", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-graukäse-tyrolean-grey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Graukäse (Tyrolean Grey Cheese)",
        "category": "mains",
        "attribution": "Tyrol, Austria / Medieval",
        "source_note": "Ancient farmers' cheese from the Austrian Alps, made from soured skimmed milk with no rennet added.",
        "description": "Austrian grey-molded cheese made from skimmed milk without rennet, developing a distinctive grey rind and pungent flavor.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "skimmed milk", "quantity": "1", "unit": "gallon", "prep_note": "cream removed"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Let skimmed milk sour naturally at room temperature for 2-3 days."},
            {"step": 2, "text": "Or add buttermilk and let sour for 24 hours."},
            {"step": 3, "text": "Heat soured milk slowly to 100-110°F."},
            {"step": 4, "text": "Curds will form from acid alone - no rennet needed."},
            {"step": 5, "text": "Strain curds through cheesecloth."},
            {"step": 6, "text": "Mix in salt."},
            {"step": 7, "text": "Press into small round molds."},
            {"step": 8, "text": "Let drain for 24 hours."},
            {"step": 9, "text": "Age at 55-60°F in humid conditions."},
            {"step": 10, "text": "Grey mold develops naturally on surface over 2-4 weeks."},
            {"step": 11, "text": "The cheese becomes very pungent with age."}
        ],
        "temperature": "100-110°F make, 55-60°F aging",
        "notes": [
            "No rennet is used - this is purely an acid-set cheese",
            "The grey mold is natural and expected",
            "Very low fat due to skimmed milk - a peasant cheese",
            "Becomes extremely pungent when fully aged",
            "Protected traditional specialty in Austria"
        ],
        "tags": ["cheese", "traditional", "austrian", "tyrolean", "grey", "skimmed", "no-rennet", "medieval", "alpine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-raclette-swiss-alpine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Raclette (Swiss Melting Cheese)",
        "category": "mains",
        "attribution": "Valais, Switzerland / Medieval",
        "source_note": "The word 'raclette' comes from 'racler' meaning to scrape. Alpine herders melted this cheese by the fire for centuries.",
        "description": "Swiss alpine cheese made for melting and scraping onto potatoes and pickles, with a smooth creamy texture and nutty flavor.",
        "servings_yield": "About 6 lbs wheel",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "raw cow milk", "quantity": "5", "unit": "gallons", "prep_note": "alpine pasture milk ideal"},
            {"item": "thermophilic culture", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1.5", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1.5", "unit": "lbs", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add thermophilic culture and ripen 30 minutes."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 35 minutes until firm."},
            {"step": 5, "text": "Cut curds to corn kernel size."},
            {"step": 6, "text": "Stir gently while heating to 104°F over 30 minutes."},
            {"step": 7, "text": "Continue stirring at 104°F for 30 more minutes."},
            {"step": 8, "text": "Drain curds and transfer to large round mold."},
            {"step": 9, "text": "Press at 25 lbs for 30 minutes, flip, 40 lbs for 12 hours."},
            {"step": 10, "text": "Soak in saturated brine for 48 hours."},
            {"step": 11, "text": "Age at 55°F, 95% humidity."},
            {"step": 12, "text": "Wash rind with brine every few days during aging."},
            {"step": 13, "text": "Age 3-6 months until paste is supple and aromatic."}
        ],
        "temperature": "90-104°F make, 55°F aging",
        "notes": [
            "Traditional raclette is made on alpine pastures during summer",
            "The washed rind creates the characteristic aroma",
            "When heated, it melts smoothly without becoming stringy",
            "Served by melting against a fire and scraping onto plates"
        ],
        "tags": ["cheese", "traditional", "swiss", "alpine", "melting", "washed-rind", "valais", "medieval"],
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
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nAdded {added} recipes, skipped {skipped} duplicates")
    print(f"Total recipes in database: {len(data['recipes'])}")

if __name__ == "__main__":
    main()
