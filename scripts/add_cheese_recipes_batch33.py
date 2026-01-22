#!/usr/bin/env python3
"""Add batch 33 of traditional cheese recipes - Balkan, Caucasus, and Central Asian ancient cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-sulguni-georgian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sulguni (Georgian Stretched Cheese)",
        "category": "mains",
        "attribution": "Samegrelo, Georgia / Ancient",
        "source_note": "From the Samegrelo region of Georgia, where cheesemaking traditions date back thousands of years. Related to Italian pasta filata.",
        "description": "Georgian brine-soaked stretched cheese with a layered structure and mild salty flavor, often smoked or filled with other cheeses.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "3 hours",
        "cook_time": "1-2 days",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "fresh cow milk", "quantity": "1", "unit": "gallon", "prep_note": "or buffalo milk"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or matsoni as starter"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add culture and let ripen 30 minutes."},
            {"step": 3, "text": "Add rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Drain whey and let curds acidify at room temperature for 6-12 hours."},
            {"step": 6, "text": "Test curd by stretching a piece in hot water - when it stretches smoothly, it's ready."},
            {"step": 7, "text": "Heat water to 170-180°F. Cut curd into strips."},
            {"step": 8, "text": "Submerge strips in hot water and stretch, folding repeatedly."},
            {"step": 9, "text": "Form into round flat discs about 1 inch thick."},
            {"step": 10, "text": "Place in cold water briefly to set shape."},
            {"step": 11, "text": "Make brine and soak cheese for 12-24 hours."},
            {"step": 12, "text": "Store in brine. Optionally smoke for smoked sulguni."}
        ],
        "temperature": "90°F make, 170-180°F stretching",
        "notes": [
            "Sulguni is essential for Georgian khachapuri bread",
            "The layered stretched structure is visible when sliced",
            "Can be filled with fresh curd cheese (gadazelili sulguni)",
            "Smoked sulguni is popular throughout the Caucasus"
        ],
        "tags": ["cheese", "traditional", "georgian", "stretched", "brined", "caucasus", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-imeruli-georgian-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Imeruli (Georgian Fresh Cheese)",
        "category": "mains",
        "attribution": "Imereti, Georgia / Ancient",
        "source_note": "From the Imereti region. The classic filling cheese for Imeretian khachapuri, made fresh and used immediately.",
        "description": "Georgian fresh cheese with a crumbly texture and mild salty flavor, the essential filling for Imeretian-style cheese bread.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "2 hours",
        "cook_time": "24 hours draining",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "fresh cow milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "matsoni or yogurt", "quantity": "1/4", "unit": "cup", "prep_note": "as starter"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add matsoni and stir gently."},
            {"step": 3, "text": "Add diluted rennet and stir briefly."},
            {"step": 4, "text": "Let set for 1 hour until firm curd forms."},
            {"step": 5, "text": "Cut curds into large chunks."},
            {"step": 6, "text": "Gently stir and let rest 10 minutes."},
            {"step": 7, "text": "Ladle curds into cloth-lined basket."},
            {"step": 8, "text": "Sprinkle salt between layers of curd."},
            {"step": 9, "text": "Let drain at room temperature for 12-24 hours."},
            {"step": 10, "text": "Cheese is ready when firm but still moist."},
            {"step": 11, "text": "Use fresh for khachapuri or store in light brine."}
        ],
        "temperature": "95°F make",
        "notes": [
            "Imeruli should be crumbly and moist, not dry",
            "Traditional starter is matsoni (Georgian yogurt)",
            "Must be fresh for best results in khachapuri",
            "Less salty than sulguni, with milder flavor"
        ],
        "tags": ["cheese", "traditional", "georgian", "fresh", "imereti", "caucasus", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-chechil-armenian-string",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chechil (Armenian String Cheese)",
        "category": "mains",
        "attribution": "Armenia / Ancient",
        "source_note": "Armenian stretched cheese made into thin strings and braided. Ancient tradition shared across the Caucasus.",
        "description": "Armenian string cheese stretched into thin strands and braided or twisted, often smoked, with a salty tangy flavor.",
        "servings_yield": "About 1 lb braided",
        "prep_time": "3 hours",
        "cook_time": "1-2 days",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "fresh sheep or cow milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "yogurt or matsoni", "quantity": "1/4", "unit": "cup", "prep_note": "as starter"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add yogurt starter and ripen 30 minutes."},
            {"step": 3, "text": "Add rennet and let set for 45 minutes."},
            {"step": 4, "text": "Cut curds and drain whey."},
            {"step": 5, "text": "Let curds acidify at room temperature for 6-12 hours until stretchy."},
            {"step": 6, "text": "Test by stretching in hot water - should pull into smooth strings."},
            {"step": 7, "text": "Heat water to 175°F."},
            {"step": 8, "text": "Pull small pieces of curd and stretch into very thin strings."},
            {"step": 9, "text": "Continue stretching until strings are pencil-thin or thinner."},
            {"step": 10, "text": "Braid or twist strings together while still warm."},
            {"step": 11, "text": "Soak in brine for 12-24 hours."},
            {"step": 12, "text": "Optionally smoke for 4-8 hours with fruit wood."}
        ],
        "temperature": "90°F make, 175°F stretching",
        "notes": [
            "The thinner the strings, the more traditional the chechil",
            "Skilled cheesemakers pull strings thin as thread",
            "Often sold braided or in twisted bundles",
            "Smoked chechil is popular across the Caucasus"
        ],
        "tags": ["cheese", "traditional", "armenian", "string", "braided", "stretched", "smoked", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-kurut-central-asian-dried",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kurut (Central Asian Dried Cheese Balls)",
        "category": "mains",
        "attribution": "Central Asia / Ancient Nomadic",
        "source_note": "Made by nomads across Central Asia for thousands of years. Essential protein source for long migrations on the Silk Road.",
        "description": "Rock-hard dried cheese balls from Central Asian nomadic tradition, intensely salty and sour, eaten as a snack or dissolved in soups.",
        "servings_yield": "About 20 small balls",
        "prep_time": "2 days",
        "cook_time": "1-2 weeks drying",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "yogurt", "quantity": "1", "unit": "quart", "prep_note": "full fat, preferably from sheep or goat"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Line a colander with cheesecloth."},
            {"step": 2, "text": "Pour yogurt into cloth and let drain for 24-48 hours until very thick."},
            {"step": 3, "text": "Mix salt thoroughly into the thick strained yogurt."},
            {"step": 4, "text": "Roll into small balls about 1 inch diameter."},
            {"step": 5, "text": "Place balls on a drying rack in a hot, dry, well-ventilated area."},
            {"step": 6, "text": "Traditional method: dry in yurt or on tent roof in sun."},
            {"step": 7, "text": "Turn balls daily for even drying."},
            {"step": 8, "text": "Dry for 1-2 weeks until completely hard as stone."},
            {"step": 9, "text": "Store in dry container. Will keep for years."},
            {"step": 10, "text": "Eat as a snack or dissolve in hot soup or tea."}
        ],
        "temperature": "Sun drying or 100-120°F dehydrator",
        "notes": [
            "Kurut is one of the oldest preserved dairy foods in the world",
            "Essential provision for Silk Road travelers and nomadic herders",
            "Known by many names: qurt, kurut, kashk, aaruul",
            "The intense flavor develops from fermentation and concentration"
        ],
        "tags": ["cheese", "traditional", "central-asian", "dried", "nomadic", "preserved", "ancient", "silk-road"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-kajmak-serbian-clotted-cream",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kajmak (Serbian Clotted Cream Cheese)",
        "category": "mains",
        "attribution": "Serbia and Balkans / Ottoman Era",
        "source_note": "Rich clotted cream from the Balkans, layered and aged. Essential accompaniment to ćevapi and traditional Serbian cuisine.",
        "description": "Balkan clotted cream cheese made by skimming and layering cream over several days, with rich buttery flavor and spreadable texture.",
        "servings_yield": "About 1 lb",
        "prep_time": "3-5 days",
        "cook_time": "2 weeks aging",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "raw milk traditional, non-homogenized"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour fresh milk into wide shallow pan."},
            {"step": 2, "text": "Heat slowly until small bubbles appear around edges (160-180°F)."},
            {"step": 3, "text": "Remove from heat and let cool undisturbed for 12 hours."},
            {"step": 4, "text": "A thick layer of cream will form on surface."},
            {"step": 5, "text": "Carefully skim this cream layer into a crock."},
            {"step": 6, "text": "Sprinkle lightly with salt."},
            {"step": 7, "text": "Repeat process daily with fresh milk, layering cream on cream."},
            {"step": 8, "text": "Continue for 3-5 days until crock is full of layered cream."},
            {"step": 9, "text": "Cover and age at cool temperature for 1-2 weeks."},
            {"step": 10, "text": "Kajmak develops tangy, fermented flavor as it ages."},
            {"step": 11, "text": "Serve spread on bread or with grilled meats."}
        ],
        "temperature": "160-180°F heating, cool aging",
        "notes": [
            "Fresh kajmak (mladi kajmak) is sweet and buttery",
            "Aged kajmak (stari kajmak) develops stronger tangy flavor",
            "Essential with ćevapi, pljeskavica, and Serbian grilled meats",
            "Each daily layer creates distinct strata visible when sliced"
        ],
        "tags": ["cheese", "traditional", "serbian", "balkan", "clotted-cream", "aged", "ottoman", "layered"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-katiki-domokou-greek-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Katiki Domokou (Greek Fresh Cheese)",
        "category": "mains",
        "attribution": "Domokos, Greece / Ancient",
        "source_note": "PDO protected fresh cheese from Domokos in central Greece. Made from goat and sheep milk, naturally drained.",
        "description": "Greek fresh spreadable cheese from Domokos with a creamy texture, slightly tangy flavor, and no rennet - purely acid-set.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "24-48 hours draining",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "goat milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "sheep milk", "quantity": "1", "unit": "quart", "prep_note": "fresh, optional blend"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and let stand at warm room temperature."},
            {"step": 2, "text": "Allow to naturally sour and curdle over 24-48 hours."},
            {"step": 3, "text": "No culture or rennet is added - this is purely natural acidification."},
            {"step": 4, "text": "When milk has thickened and separated, gently ladle into cheesecloth."},
            {"step": 5, "text": "Hang or drain for 24-48 hours until thick but still spreadable."},
            {"step": 6, "text": "Add salt and mix gently."},
            {"step": 7, "text": "Pack into containers."},
            {"step": 8, "text": "Refrigerate and use within 1 week."}
        ],
        "temperature": "Room temperature natural souring",
        "notes": [
            "True Katiki uses no rennet - it relies on natural souring",
            "PDO protected - must be made in Domokos area",
            "Spreadable texture, similar to cream cheese but tangier",
            "Traditional breakfast food spread on bread"
        ],
        "tags": ["cheese", "traditional", "greek", "fresh", "spreadable", "pdo", "no-rennet", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-circassian-cheese-adyghe",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Adyghe Cheese (Circassian Fresh Cheese)",
        "category": "mains",
        "attribution": "Circassia/Adygea / Ancient",
        "source_note": "Made by Circassian peoples of the North Caucasus for millennia. Now protected GI as Adygean cheese in Russia.",
        "description": "Circassian fresh cheese with a mild milky flavor and springy texture, traditionally made from sheep milk and coagulated with whey.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "2 hours",
        "cook_time": "2-3 hours",
        "total_time": "4-5 hours",
        "ingredients": [
            {"item": "whole cow or sheep milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "sour whey", "quantity": "1", "unit": "cup", "prep_note": "or buttermilk, or yogurt whey"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 195-200°F, stirring occasionally to prevent scorching."},
            {"step": 2, "text": "When milk reaches temperature, remove from heat."},
            {"step": 3, "text": "Slowly add sour whey while stirring gently."},
            {"step": 4, "text": "Curds will form and separate from whey."},
            {"step": 5, "text": "Let rest 10 minutes until curds consolidate."},
            {"step": 6, "text": "Gently ladle curds into basket molds or colander."},
            {"step": 7, "text": "Press lightly and let drain for 1-2 hours."},
            {"step": 8, "text": "Add salt, mixing gently or sprinkling on surface."},
            {"step": 9, "text": "Let rest 1 more hour to firm up."},
            {"step": 10, "text": "Eat fresh or store in light brine for up to 2 weeks."}
        ],
        "temperature": "195-200°F make",
        "notes": [
            "The high-heat, whey-acid method is distinctly Circassian",
            "Results in springy, slightly rubbery texture",
            "Traditional round shape with basket-weave pattern from molds",
            "Essential in Circassian cuisine, served at every meal"
        ],
        "tags": ["cheese", "traditional", "circassian", "adyghe", "fresh", "caucasus", "ancient", "whey-coagulated"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-lor-turkish-whey-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Lor (Turkish Whey Cheese)",
        "category": "mains",
        "attribution": "Turkey / Ancient Anatolian",
        "source_note": "Traditional Turkish whey cheese made after producing kaşar or other hard cheeses. Similar to ricotta but with distinct Turkish character.",
        "description": "Turkish fresh whey cheese with delicate creamy texture, made from the whey of other cheeses with added milk.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "3 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from making other cheese"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": "fresh"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh warm whey immediately after making another cheese."},
            {"step": 2, "text": "Add fresh milk to the whey."},
            {"step": 3, "text": "Heat slowly, stirring gently, until temperature reaches 185-195°F."},
            {"step": 4, "text": "Curds will begin to form and float to surface."},
            {"step": 5, "text": "Stop stirring when curds appear and let rest 10 minutes."},
            {"step": 6, "text": "Gently skim floating curds into cheesecloth-lined strainer."},
            {"step": 7, "text": "Let drain for 1-2 hours."},
            {"step": 8, "text": "Add salt and mix gently."},
            {"step": 9, "text": "Use fresh or within 3-4 days."}
        ],
        "temperature": "185-195°F make",
        "notes": [
            "Lor is traditionally made alongside kaşar production",
            "Adding fresh milk enriches the whey and improves yield",
            "Delicate and mild - often used in börek and pastries",
            "Similar to Italian ricotta and Corsican brocciu"
        ],
        "tags": ["cheese", "traditional", "turkish", "whey", "fresh", "anatolian", "ancient"],
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
