#!/usr/bin/env python3
"""Add batch 59 - Ancient and historic cheeses from around the world."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-casu-marzu-sardinian-living",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Casu Marzu (Sardinian Living Cheese) - Historical Reference",
        "category": "mains",
        "attribution": "Ancient Sardinian tradition",
        "source_note": "Traditional Sardinian fermented cheesemaking - historical documentation",
        "description": "One of the world's most controversial cheeses, Casu Marzu is Pecorino that has been colonized by cheese fly larvae. The larvae break down the cheese fats, creating an intensely pungent, soft cheese. Documented here for historical purposes.",
        "servings_yield": "Historical reference only",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "aged pecorino sardo", "quantity": "1", "unit": "wheel", "prep_note": "starting cheese"},
            {"item": "cheese fly exposure", "quantity": "", "unit": "", "prep_note": "Piophila casei - occurs naturally"}
        ],
        "instructions": [
            {"step": 1, "text": "HISTORICAL PROCESS - NOT FOR RECREATION: This describes traditional practice."},
            {"step": 2, "text": "Start with a wheel of Pecorino Sardo that has aged 2-3 months."},
            {"step": 3, "text": "Cut the top rind to allow cheese flies (Piophila casei) access."},
            {"step": 4, "text": "Leave in location where cheese flies are present."},
            {"step": 5, "text": "Flies lay eggs in the cheese; larvae hatch and begin consuming the cheese."},
            {"step": 6, "text": "Larval digestion breaks down fats, creating soft, spreadable texture."},
            {"step": 7, "text": "Process continues for 3-6 months."},
            {"step": 8, "text": "Traditionally eaten with larvae still alive and active."},
            {"step": 9, "text": "When larvae die, cheese is considered too fermented to eat."},
            {"step": 10, "text": "This cheese is banned for sale under EU food hygiene regulations."}
        ],
        "temperature": "Ambient outdoor temperature",
        "notes": [
            "THIS IS HISTORICAL DOCUMENTATION - not recommended for recreation",
            "Banned under EU regulations but still made illegally in Sardinia",
            "Name means 'rotten cheese' in Sardinian",
            "Larvae can jump up to 6 inches when disturbed",
            "Represents extreme end of traditional fermentation practices",
            "Similar insect-fermented cheeses exist in other Mediterranean regions"
        ],
        "tags": ["cheese", "sardinian", "historical", "ancient", "fermented", "reference-only"],
        "confidence": {"overall": "high", "flags": ["historical reference only"]}
    },
    {
        "id": "traditional-oscypek-polish-smoked-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Oscypek (Polish Tatra Mountain Smoked Cheese)",
        "category": "mains",
        "attribution": "15th century Vlach shepherd tradition",
        "source_note": "Traditional Polish highland cheesemaking",
        "description": "Brought to the Polish Tatras by Vlach shepherds in the 15th century, Oscypek is a smoked sheep's milk cheese with distinctive spindle shape and decorative patterns. Made only in summer mountain pastures, it's protected by EU PDO.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "2-3 weeks including smoking",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Polish Mountain Sheep"},
            {"item": "cow's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "up to 40% allowed by PDO"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "cold-smoking wood", "quantity": "", "unit": "", "prep_note": "traditionally pine"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep's milk with up to 40% cow's milk."},
            {"step": 2, "text": "Heat to 95°F (35°C)."},
            {"step": 3, "text": "Add rennet without starter culture (traditional method)."},
            {"step": 4, "text": "Let set 30-40 minutes until firm."},
            {"step": 5, "text": "Break curds by hand and gather into mass."},
            {"step": 6, "text": "Knead curds in warm whey until smooth and elastic."},
            {"step": 7, "text": "Form into traditional spindle/lens shape (pointed at both ends)."},
            {"step": 8, "text": "Press decorative patterns using carved wooden molds."},
            {"step": 9, "text": "Brine for 12-24 hours."},
            {"step": 10, "text": "Cold smoke over pine wood for 1-2 weeks."},
            {"step": 11, "text": "Cheese develops golden-brown rind from smoking."},
            {"step": 12, "text": "Can be eaten fresh or aged up to several months."}
        ],
        "temperature": "95°F (35°C) for curd; cold smoking",
        "notes": [
            "PDO protected since 2008 - made only in Polish Tatra region",
            "Vlach shepherds brought the technique from the Balkans",
            "Each shepherd has unique decorative mold patterns",
            "Must weigh 600-800g and have characteristic spindle shape",
            "Traditionally made May-September in mountain huts (bacówka)"
        ],
        "tags": ["cheese", "polish", "tatra", "traditional", "smoked", "sheep", "decorated"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-bryndza-slovak-sheep-spread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bryndza (Slovak Sheep Cheese Spread)",
        "category": "mains",
        "attribution": "Ancient Carpathian shepherd tradition",
        "source_note": "Traditional Slovak sheep cheesemaking",
        "description": "Slovakia's national cheese, Bryndza is a creamy, tangy spread made from sheep's milk cheese that's been crumbled and mixed. Essential for bryndzové halušky (Slovakia's national dish), it has ancient Carpathian origins.",
        "servings_yield": "1 lb spread",
        "prep_time": "20 minutes",
        "cook_time": "3-4 hours for base cheese",
        "total_time": "1-2 weeks for fermentation",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Valachian or Tsigai sheep"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "sheep's milk or cream", "quantity": "1/4", "unit": "cup", "prep_note": "for mixing"}
        ],
        "instructions": [
            {"step": 1, "text": "First make base cheese: heat sheep's milk to 90°F (32°C)."},
            {"step": 2, "text": "Add rennet, let set 30-45 minutes."},
            {"step": 3, "text": "Cut curds coarsely, drain, and form into small cheeses."},
            {"step": 4, "text": "Let base cheeses age and ferment 1-2 weeks until tangy."},
            {"step": 5, "text": "Crumble aged cheeses into mixing bowl."},
            {"step": 6, "text": "Add salt and small amount of sheep's milk or cream."},
            {"step": 7, "text": "Knead and mix vigorously until smooth, spreadable paste forms."},
            {"step": 8, "text": "Traditional method: mix in wooden tubs with wooden paddles."},
            {"step": 9, "text": "Taste and adjust salt."},
            {"step": 10, "text": "Pack into containers. Refrigerate."},
            {"step": 11, "text": "Best within 2 weeks. Flavor intensifies over time."}
        ],
        "temperature": "90°F (32°C) for base cheese; room temperature for mixing",
        "notes": [
            "PGI protected since 2008",
            "Essential for bryndzové halušky - Slovak potato dumplings",
            "Must contain at least 50% sheep's milk",
            "Tangy, salty, slightly sharp flavor",
            "Similar cheeses: Polish bundz, Romanian brânză"
        ],
        "tags": ["cheese", "slovak", "carpathian", "traditional", "sheep", "spread", "fermented"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-urda-romanian-whey-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Urdă (Romanian Whey Cheese)",
        "category": "mains",
        "attribution": "Ancient Dacian-Romanian tradition",
        "source_note": "Traditional Romanian whey cheesemaking",
        "description": "Romania's ricotta-style cheese, Urdă has been made by Carpathian shepherds for millennia. Made from the whey left after making brânză or cașcaval, it's traditionally eaten fresh with mămăligă (polenta).",
        "servings_yield": "8-12 oz cheese",
        "prep_time": "10 minutes",
        "cook_time": "30-45 minutes",
        "total_time": "1-2 hours",
        "ingredients": [
            {"item": "fresh sheep's milk whey", "quantity": "1", "unit": "gallon", "prep_note": "from cheesemaking"},
            {"item": "sheep's milk", "quantity": "1", "unit": "cup", "prep_note": "optional, for richer urdă"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "vinegar or lemon", "quantity": "1", "unit": "tbsp", "prep_note": "if curds don't form naturally"}
        ],
        "instructions": [
            {"step": 1, "text": "Use whey immediately after making sheep cheese while still hot."},
            {"step": 2, "text": "If whey has cooled, heat to 185-195°F (85-90°C)."},
            {"step": 3, "text": "Add fresh sheep's milk if richer urdă is desired."},
            {"step": 4, "text": "Stir gently and watch for fine white curds rising to surface."},
            {"step": 5, "text": "If curds don't appear, add small amount of acid."},
            {"step": 6, "text": "Let curds accumulate on surface for 10-15 minutes."},
            {"step": 7, "text": "Skim curds carefully with slotted spoon."},
            {"step": 8, "text": "Transfer to cloth-lined mold or colander."},
            {"step": 9, "text": "Drain 1-2 hours until desired consistency."},
            {"step": 10, "text": "Salt to taste while still warm."},
            {"step": 11, "text": "Eat fresh within 2-3 days."}
        ],
        "temperature": "185-195°F (85-90°C)",
        "notes": [
            "Must be made from fresh whey - aged whey doesn't work well",
            "Similar to Italian ricotta but traditionally from sheep's milk",
            "Essential accompaniment to Romanian mămăligă",
            "Can be smoked (urdă afumată) for longer preservation",
            "Dacian origins - made in these mountains for 2000+ years"
        ],
        "tags": ["cheese", "romanian", "carpathian", "traditional", "whey", "fresh", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-kashk-persian-dried-whey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kashk (Persian Dried Whey Cheese)",
        "category": "mains",
        "attribution": "Ancient Persian tradition",
        "source_note": "Traditional Persian preserved dairy",
        "description": "An ancient Persian preparation, Kashk is dried, fermented whey that's been concentrated into hard balls or paste. Used throughout the Middle East for millennia, it adds intense umami and tang to dishes like kashk-e bademjan.",
        "servings_yield": "1 lb dried kashk",
        "prep_time": "30 minutes",
        "cook_time": "Several hours",
        "total_time": "1-2 weeks including drying",
        "ingredients": [
            {"item": "whey or sour milk", "quantity": "1", "unit": "gallon", "prep_note": "from yogurt or cheesemaking"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": "for preservation"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with whey from cheesemaking or strained yogurt."},
            {"step": 2, "text": "Pour whey into wide pot and heat gently."},
            {"step": 3, "text": "Simmer slowly, stirring frequently to prevent sticking."},
            {"step": 4, "text": "Continue simmering for several hours as liquid evaporates."},
            {"step": 5, "text": "Stir more frequently as mixture thickens."},
            {"step": 6, "text": "Add salt when mixture becomes paste-like."},
            {"step": 7, "text": "Continue cooking until very thick and pulls away from pot."},
            {"step": 8, "text": "For liquid kashk: stop here, jar while warm."},
            {"step": 9, "text": "For dried kashk: form thick paste into balls."},
            {"step": 10, "text": "Dry balls in sun or dehydrator for 1-2 weeks."},
            {"step": 11, "text": "Dried kashk keeps for months. Reconstitute in water to use."}
        ],
        "temperature": "Low simmer for concentration",
        "notes": [
            "Ancient Persian preservation technique for surplus whey",
            "Similar products: Turkish kurut, Central Asian qurt",
            "Essential for kashk-e bademjan (eggplant dip)",
            "Provides intense umami flavor - fermented and concentrated",
            "Dried kashk was valuable trade good on Silk Road"
        ],
        "tags": ["cheese", "persian", "iranian", "traditional", "ancient", "dried", "preserved", "whey"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-circassian-cheese-adyghe",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Circassian Cheese (Adyghe Cheese)",
        "category": "mains",
        "attribution": "Ancient Circassian Caucasus tradition",
        "source_note": "Traditional Caucasian cheesemaking",
        "description": "Made by the Circassian people of the Northwest Caucasus for thousands of years, Adyghe cheese is a mild, soft, fresh cheese. It has PGI protection in Russia and represents one of the oldest continuous cheesemaking traditions.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "1-2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or sheep/goat"},
            {"item": "kefir or buttermilk", "quantity": "1", "unit": "cup", "prep_note": "for acidification"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185-195°F (85-90°C)."},
            {"step": 2, "text": "Add kefir or buttermilk while stirring gently."},
            {"step": 3, "text": "Curds will form and separate from whey."},
            {"step": 4, "text": "Continue heating gently until curds are well formed."},
            {"step": 5, "text": "Remove from heat, let rest 10 minutes."},
            {"step": 6, "text": "Strain curds through cloth-lined colander."},
            {"step": 7, "text": "Rinse briefly with cool water if desired."},
            {"step": 8, "text": "Salt curds while still warm."},
            {"step": 9, "text": "Pack into molds or form by hand."},
            {"step": 10, "text": "Press lightly or let drain naturally for 1-2 hours."},
            {"step": 11, "text": "Eat fresh. Keeps refrigerated 1-2 weeks."}
        ],
        "temperature": "185-195°F (85-90°C)",
        "notes": [
            "PGI protected in Russia since 2005",
            "Circassian people have made this cheese for millennia",
            "Mild, slightly tangy, soft and springy texture",
            "Used in Circassian cuisine - often with herbs or walnuts",
            "Similar to paneer but traditionally uses acidified milk, not just acid"
        ],
        "tags": ["cheese", "circassian", "caucasian", "russian", "traditional", "ancient", "fresh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-sulguni-georgian-stretched",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sulguni (Georgian Stretched Cheese)",
        "category": "mains",
        "attribution": "Ancient Georgian Samegrelo tradition",
        "source_note": "Traditional Georgian pasta filata cheesemaking",
        "description": "Georgia's most famous cheese, Sulguni is a stretched-curd cheese from the Samegrelo region. Similar to mozzarella but traditionally stored in brine, it can be fresh, smoked, or braided. Essential to Georgian cuisine.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "Same day to weeks (brined)",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "or buffalo milk"},
            {"item": "mesophilic starter", "quantity": "1/8", "unit": "tsp", "prep_note": "or kefir"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "3/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add starter or kefir, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch pieces."},
            {"step": 5, "text": "Let curds acidify under whey for 3-5 hours until pH 5.2-5.3."},
            {"step": 6, "text": "Test: small piece should stretch in hot water."},
            {"step": 7, "text": "Heat water to 170-175°F (77-80°C)."},
            {"step": 8, "text": "Cut curd into strips, submerge in hot water."},
            {"step": 9, "text": "Knead and stretch until smooth and elastic."},
            {"step": 10, "text": "Form into flat disc shape (traditional) or braid."},
            {"step": 11, "text": "Cool in cold water, then transfer to brine."},
            {"step": 12, "text": "Store in brine refrigerated. Can be smoked for extra flavor."}
        ],
        "temperature": "95°F (35°C) for curd; 170-175°F (77-80°C) for stretching",
        "notes": [
            "PGI protected from Georgia's Samegrelo region",
            "Can be fresh, brined, smoked, or braided",
            "Smoked Sulguni has distinctive golden-brown surface",
            "Essential for khachapuri (Georgian cheese bread)",
            "Stretchy texture but firmer than Italian mozzarella"
        ],
        "tags": ["cheese", "georgian", "caucasian", "traditional", "pasta-filata", "brined", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-tulum-turkish-goatskin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Tulum (Turkish Goatskin-Aged Cheese)",
        "category": "mains",
        "attribution": "Ancient Anatolian nomadic tradition",
        "source_note": "Traditional Turkish pastoral cheesemaking",
        "description": "Named for the goatskin bag in which it's aged, Tulum has been made by Turkish shepherds for millennia. The goatskin imparts distinctive earthy, animal flavors while allowing the cheese to breathe during aging.",
        "servings_yield": "2 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "raw goat's milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep's milk"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "goatskin bag", "quantity": "1", "unit": "", "prep_note": "or modern alternative - food-safe bag"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 90°F (32°C)."},
            {"step": 2, "text": "Add rennet without starter (traditional method)."},
            {"step": 3, "text": "Let set 45-60 minutes until firm."},
            {"step": 4, "text": "Break curds by hand, let rest in whey."},
            {"step": 5, "text": "Drain curds and hang in cloth to drain further."},
            {"step": 6, "text": "Crumble drained curds, salt generously."},
            {"step": 7, "text": "If using goatskin: prepare by cleaning, salting, and drying skin."},
            {"step": 8, "text": "Pack salted curds tightly into goatskin, pressing out air."},
            {"step": 9, "text": "Tie skin closed tightly."},
            {"step": 10, "text": "Age in cool cave or cellar for 3-6 months."},
            {"step": 11, "text": "Modern alternative: pack in food-grade bags, age in cool conditions."},
            {"step": 12, "text": "Cheese develops crumbly texture and sharp, earthy flavor."}
        ],
        "temperature": "90°F (32°C) for curd; 50-55°F for aging",
        "notes": [
            "Traditional goatskin aging is rare today - food safety concerns",
            "Erzincan Tulum is the most famous variety",
            "The goatskin contributes unique flavor compounds",
            "Modern versions use plastic or cloth bags",
            "Crumbly texture similar to aged feta but earthier flavor"
        ],
        "tags": ["cheese", "turkish", "anatolian", "traditional", "ancient", "goatskin", "aged"],
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
