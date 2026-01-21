#!/usr/bin/env python3
"""Add batch 26 of traditional cheese recipes - Eastern European and ancient historical cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-bryndza-carpathian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bryndza (Carpathian Sheep Cheese)",
        "category": "mains",
        "attribution": "Carpathian Mountains (Slovakia/Poland), Ancient",
        "source_note": "Bryndza has been made by Vlach shepherds in the Carpathian Mountains for over a thousand years. It's the national cheese of Slovakia and essential to Polish and Slovak cuisine. Made from sheep's milk, it has a distinctively tangy, sharp flavor.",
        "description": "Ancient Carpathian sheep cheese with a sharp, tangy flavor - the national cheese of Slovakia and foundation of bryndzové halušky.",
        "servings_yield": "About 1 lb",
        "prep_time": "24 hours",
        "cook_time": "1-2 weeks ripening",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or natural clabbering"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 90°F."},
            {"step": 2, "text": "Add starter or allow to naturally sour for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Drain whey and hang curds in cloth to drain for 24 hours."},
            {"step": 6, "text": "The drained curd (called 'hrudka' or 'žinčica base') should be crumbly."},
            {"step": 7, "text": "Let the drained curd ripen at cool room temperature (55-60°F) for 1-2 weeks, breaking up and re-forming daily."},
            {"step": 8, "text": "When properly ripened, the curd will be tangy and slightly sour."},
            {"step": 9, "text": "Grind or mash the ripened curd until smooth and spreadable."},
            {"step": 10, "text": "Mix in salt to taste."},
            {"step": 11, "text": "Pack into containers. Refrigerate and use within 2-3 weeks."}
        ],
        "temperature": "90°F make, 55-60°F ripening",
        "notes": [
            "Authentic bryndza must be made from sheep's milk (at least 50% by EU regulations)",
            "The ripening process develops the characteristic sharp, tangy flavor",
            "Essential for bryndzové halušky (Slovak national dish) and pierogi fillings",
            "Slovenská bryndza has PGI protection"
        ],
        "tags": ["cheese", "traditional", "slovak", "polish", "carpathian", "sheep-cheese", "bryndza", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-oscypek-polish",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Oscypek (Polish Smoked Sheep Cheese)",
        "category": "mains",
        "attribution": "Tatra Mountains, Poland, 15th Century",
        "source_note": "Oscypek has been made by Górale (Polish highlanders) in the Tatra Mountains since at least the 15th century, likely brought by Vlach shepherds. The distinctive spindle shape and decorative patterns are carved by hand into wooden molds.",
        "description": "Decorative smoked sheep cheese from the Polish Tatras, hand-carved into traditional spindle shapes by highland shepherds.",
        "servings_yield": "About 1 lb (2-3 spindles)",
        "prep_time": "3 hours",
        "cook_time": "2-3 weeks including smoking",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "cow's milk", "quantity": "up to 40%", "unit": "", "prep_note": "optional, traditional blend"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F."},
            {"step": 2, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes."},
            {"step": 3, "text": "Cut curd finely into rice-sized grains."},
            {"step": 4, "text": "Gather curds in cloth and squeeze out whey."},
            {"step": 5, "text": "While still warm and pliable, knead the curd mass by hand."},
            {"step": 6, "text": "Form into a spindle/lens shape (traditional oscypek form)."},
            {"step": 7, "text": "Press into decorative carved wooden molds to imprint traditional patterns."},
            {"step": 8, "text": "Soak in saturated brine for 12-24 hours."},
            {"step": 9, "text": "Air dry for 1-2 days."},
            {"step": 10, "text": "Cold smoke over pine, spruce, or juniper wood for 1-2 weeks."},
            {"step": 11, "text": "The finished cheese should be golden-brown with a smoky aroma."}
        ],
        "temperature": "95°F make, cold smoking",
        "notes": [
            "The decorative patterns are unique to each shepherd's molds",
            "Authentic oscypek must be made in the Tatra region from specific sheep breeds",
            "Often grilled and served with cranberry jam",
            "PDO protected since 2008"
        ],
        "tags": ["cheese", "traditional", "polish", "tatra", "smoked-cheese", "sheep-cheese", "oscypek", "15th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-olomoucke-tvaruzky-czech",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Olomoucké Tvarůžky (Czech Stinky Cheese)",
        "category": "mains",
        "attribution": "Olomouc, Moravia, 15th Century",
        "source_note": "Olomoucké tvarůžky have been made in the Haná region of Moravia since at least the 15th century. One of the world's smelliest cheeses, it's made from soured quark and is virtually fat-free.",
        "description": "Intensely pungent Moravian cheese made from soured quark - one of the world's smelliest cheeses, fat-free and centuries old.",
        "servings_yield": "About 1 lb (many small rounds)",
        "prep_time": "2 hours",
        "cook_time": "1-6 weeks ripening",
        "total_time": "1-6 weeks",
        "ingredients": [
            {"item": "quark or farmer's cheese", "quantity": "2", "unit": "lb", "prep_note": "low-fat, well-drained"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp", "prep_note": "optional, traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with very well-drained, low-fat quark or farmer's cheese."},
            {"step": 2, "text": "Let the quark sour at room temperature for 2-3 days until it develops a sharp smell."},
            {"step": 3, "text": "Knead the soured quark with salt (and caraway if using) until smooth."},
            {"step": 4, "text": "Form into small disc shapes about 1 inch thick and 2 inches across."},
            {"step": 5, "text": "Place on a rack in a ripening container with high humidity."},
            {"step": 6, "text": "Ripen at 55-60°F and 90%+ humidity for 1-6 weeks."},
            {"step": 7, "text": "Turn daily. A golden-yellow surface bacteria will develop (Brevibacterium linens)."},
            {"step": 8, "text": "The cheese is ready when golden-yellow throughout with an intense aroma."},
            {"step": 9, "text": "Young tvarůžky (1-2 weeks) are milder; aged (6+ weeks) are extremely pungent."}
        ],
        "temperature": "Room temperature souring, 55-60°F ripening",
        "notes": [
            "This is one of the world's smelliest cheeses - the aroma is INTENSE",
            "Despite the smell, the flavor is savory, complex, and addictive",
            "Virtually fat-free, high in protein",
            "Traditionally served with bread, onions, and Czech beer",
            "PGI protected; the only Czech cheese with EU protection"
        ],
        "tags": ["cheese", "traditional", "czech", "moravian", "stinky-cheese", "tvaruzky", "quark-cheese", "15th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-branza-burduf-romanian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brânză de Burduf (Romanian Pine Bark Cheese)",
        "category": "mains",
        "attribution": "Carpathian Mountains, Romania, Ancient",
        "source_note": "Brânză de burduf is an ancient Romanian cheese traditionally aged in sheep stomach or pine bark tubes. The name means 'cheese in a bag' and it's been made by Transylvanian shepherds for millennia.",
        "description": "Ancient Transylvanian cheese aged in pine bark tubes, with an intense sheep flavor and resinous notes from the bark.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "fresh sheep cheese (telemea or brânză)", "quantity": "1.5", "unit": "lb", "prep_note": "or fresh sheep curd"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "pine bark tube", "quantity": "1", "unit": "", "prep_note": "or sheep stomach, or cloth"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh sheep cheese or well-drained sheep curd."},
            {"step": 2, "text": "Crumble or grate the cheese finely."},
            {"step": 3, "text": "Mix thoroughly with salt."},
            {"step": 4, "text": "Knead until the mixture becomes smooth and pliable."},
            {"step": 5, "text": "Traditional method: Pack the cheese tightly into a pine bark tube (coajă de brad)."},
            {"step": 6, "text": "Alternative: Pack into a clean sheep stomach or cloth bag."},
            {"step": 7, "text": "Press down firmly to remove air pockets."},
            {"step": 8, "text": "Seal the container and age at 50-55°F for 2-4 weeks."},
            {"step": 9, "text": "The pine bark imparts a subtle resinous flavor to the cheese."},
            {"step": 10, "text": "When ready, the cheese should be smooth, intensely flavored, and slightly tangy."}
        ],
        "temperature": "50-55°F aging",
        "notes": [
            "The pine bark is not just a container - it adds distinctive flavor",
            "Can also be aged in sheep stomach (original method) or dried pig bladder",
            "The cheese becomes more pungent with longer aging",
            "A specialty of the Brașov region in Transylvania"
        ],
        "tags": ["cheese", "traditional", "romanian", "transylvanian", "sheep-cheese", "branza-burduf", "pine-bark", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-telemea-romanian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Telemea (Romanian White Cheese)",
        "category": "mains",
        "attribution": "Romania, Ancient (possibly Dacian)",
        "source_note": "Telemea is Romania's most widespread traditional cheese, similar to feta but with regional variations. It may date back to the ancient Dacians. Made from sheep, goat, cow, or buffalo milk depending on the region.",
        "description": "Romania's essential white brine cheese, possibly dating to ancient Dacian times - the foundation of Romanian cuisine.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks brining",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "or cow/goat/buffalo"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 15 minutes at 90°F."},
            {"step": 6, "text": "Let curds settle, drain most whey."},
            {"step": 7, "text": "Transfer curds to a cloth-lined mold. Press lightly for 4-6 hours."},
            {"step": 8, "text": "Cut the pressed cheese into 3-4 inch blocks."},
            {"step": 9, "text": "Make brine (8-10% salt solution) and submerge cheese blocks."},
            {"step": 10, "text": "Store in brine at refrigerator temperature for 2-4 weeks minimum."},
            {"step": 11, "text": "Telemea can be stored in brine for many months."}
        ],
        "temperature": "90°F make, refrigerator storage",
        "notes": [
            "Telemea de Sibiu (sheep milk) and Telemea de Ibănești are PGI protected",
            "The type of milk dramatically affects the flavor - sheep is richest",
            "Essential for Romanian salads, mamaliga, and countless traditional dishes",
            "Similar to feta but often softer and less tangy"
        ],
        "tags": ["cheese", "traditional", "romanian", "dacian", "brine-cheese", "telemea", "white-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-urda-romanian-whey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Urda (Romanian Whey Cheese)",
        "category": "mains",
        "attribution": "Romania/Balkans, Ancient",
        "source_note": "Urda is the Romanian name for the whey cheese made throughout the Balkans (called 'urda' in Romanian, 'urda' in Serbian, 'hurda' in Turkish). It's been made by Balkan shepherds for millennia as a way to use whey left from other cheeses.",
        "description": "Ancient Balkan whey cheese, light and fresh - made by shepherds for millennia from the whey of sheep cheese production.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "fresh sheep whey", "quantity": "1", "unit": "gallon", "prep_note": "from telemea or brânză making"},
            {"item": "sheep's milk", "quantity": "1", "unit": "cup", "prep_note": "optional, for richer urda"},
            {"item": "vinegar or lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "if needed"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh whey from sheep cheese making (within hours if possible)."},
            {"step": 2, "text": "Add fresh milk if using for richer results."},
            {"step": 3, "text": "Heat slowly over medium heat, stirring occasionally."},
            {"step": 4, "text": "As temperature reaches 185-195°F, white curds will rise to the surface."},
            {"step": 5, "text": "If curds don't form well, add vinegar one tablespoon at a time."},
            {"step": 6, "text": "When curds are floating, remove from heat and rest 10 minutes."},
            {"step": 7, "text": "Gently skim curds into a cloth-lined strainer."},
            {"step": 8, "text": "Let drain for 15-30 minutes."},
            {"step": 9, "text": "Add salt if desired."},
            {"step": 10, "text": "Eat fresh (best within 2-3 days) or use in pastries."}
        ],
        "temperature": "185-195°F",
        "notes": [
            "Urda from sheep whey is richest; cow whey produces lighter urda",
            "Similar to ricotta but traditionally made from sheep whey",
            "Used in Romanian pastries, with mamaliga, or eaten with honey",
            "Must be eaten very fresh - doesn't keep well"
        ],
        "tags": ["cheese", "traditional", "romanian", "balkan", "whey-cheese", "urda", "fresh-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-liptauer-hungarian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Liptauer (Hungarian/Austrian Cheese Spread)",
        "category": "mains",
        "attribution": "Liptó County (now Slovakia), Medieval",
        "source_note": "Liptauer originated in Liptó County (now Liptov in Slovakia, then part of Hungary). This spiced cheese spread became popular throughout the Austro-Hungarian Empire and remains beloved in Hungary, Austria, and Central Europe.",
        "description": "Spiced Central European cheese spread from the old Austro-Hungarian Empire, flavored with paprika, caraway, and onions.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "None (refrigerate to meld)",
        "total_time": "2-24 hours mellowing",
        "ingredients": [
            {"item": "sheep cheese or bryndza", "quantity": "8", "unit": "oz", "prep_note": "or cream cheese/quark mix"},
            {"item": "butter", "quantity": "4", "unit": "tbsp", "prep_note": "softened"},
            {"item": "sweet Hungarian paprika", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp", "prep_note": "lightly crushed"},
            {"item": "Dijon mustard", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "onion", "quantity": "2", "unit": "tbsp", "prep_note": "very finely minced"},
            {"item": "capers", "quantity": "1", "unit": "tbsp", "prep_note": "chopped, optional"},
            {"item": "salt", "quantity": "to taste", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "If using fresh sheep cheese, let it come to room temperature and mash until smooth."},
            {"step": 2, "text": "Beat softened butter until fluffy."},
            {"step": 3, "text": "Combine cheese and butter, mixing until completely smooth."},
            {"step": 4, "text": "Add paprika, caraway seeds, mustard, and minced onion."},
            {"step": 5, "text": "Add capers if using."},
            {"step": 6, "text": "Season with salt to taste."},
            {"step": 7, "text": "Mix thoroughly until all seasonings are evenly distributed."},
            {"step": 8, "text": "Pack into a crock or bowl."},
            {"step": 9, "text": "Refrigerate for at least 2 hours (overnight is better) to allow flavors to meld."},
            {"step": 10, "text": "Serve at room temperature with dark bread or crackers."}
        ],
        "temperature": "Room temperature preparation, refrigerate",
        "notes": [
            "Traditional Liptauer uses sheep cheese (bryndza or liptói túró)",
            "The paprika should be Hungarian sweet paprika for authentic flavor",
            "Variations include adding chives, anchovies, or beer",
            "Popular in Austrian wine taverns (Heurigen) and Hungarian cuisine"
        ],
        "tags": ["cheese", "traditional", "hungarian", "austrian", "cheese-spread", "liptauer", "paprika", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-giuncata-roman",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Giuncata (Ancient Roman Rush Cheese)",
        "category": "mains",
        "attribution": "Ancient Rome, 2000+ Years",
        "source_note": "Giuncata (from 'giunco' - rush/reed) is one of the oldest Italian cheeses, dating to ancient Rome. Described by Columella and other Roman writers, it was traditionally drained in rush baskets which gave it its name.",
        "description": "Ancient Roman fresh cheese drained in rush baskets, unchanged for over 2000 years - one of the oldest cheese recipes still made.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "2-4 hours draining",
        "total_time": "3-5 hours",
        "ingredients": [
            {"item": "whole sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or mixed sheep/goat"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops", "prep_note": "diluted in 1 tbsp water"},
            {"item": "salt", "quantity": "pinch", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (no higher - this is a delicate cheese)."},
            {"step": 2, "text": "Add diluted rennet, stir very gently for 30 seconds."},
            {"step": 3, "text": "Let set undisturbed for 30-45 minutes until a soft curd forms."},
            {"step": 4, "text": "The curd should be soft and delicate, like a custard."},
            {"step": 5, "text": "Very gently ladle the soft curd into rush baskets or fine-weave molds."},
            {"step": 6, "text": "Let drain at room temperature for 2-4 hours. Do not press."},
            {"step": 7, "text": "The finished cheese should be soft, moist, and delicate."},
            {"step": 8, "text": "Eat immediately while fresh, with honey if desired."}
        ],
        "temperature": "95°F make",
        "notes": [
            "This cheese was described by Columella in 'De Re Rustica' (1st century AD)",
            "The rush basket gives distinctive texture marks and the name 'giuncata'",
            "Must be eaten within 1-2 days - it's not a cheese for keeping",
            "Traditional Roman dessert when served with honey",
            "Similar to modern junket but made with real milk and rennet"
        ],
        "tags": ["cheese", "traditional", "italian", "roman", "ancient", "giuncata", "fresh-cheese", "rush-basket"],
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
