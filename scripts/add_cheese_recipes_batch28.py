#!/usr/bin/env python3
"""Add batch 28 of traditional cheese recipes - Global ancient and traditional cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-ayib-ethiopian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ayib (Ethiopian Fresh Cheese)",
        "category": "mains",
        "attribution": "Ethiopia, Ancient",
        "source_note": "Ayib has been made in Ethiopia for millennia, traditionally from buttermilk left after making butter (qibe). This simple fresh cheese is essential to Ethiopian cuisine, often served with injera and berbere spiced dishes.",
        "description": "Ancient Ethiopian fresh cheese made from buttermilk, mild and crumbly - essential alongside injera and spicy Ethiopian stews.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "buttermilk", "quantity": "1/2", "unit": "gallon", "prep_note": "or soured whole milk"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour buttermilk into a heavy pot."},
            {"step": 2, "text": "Heat slowly over medium-low heat, stirring occasionally."},
            {"step": 3, "text": "As it heats, curds will begin to form and separate from the whey."},
            {"step": 4, "text": "Continue heating until temperature reaches 180°F and curds are well separated."},
            {"step": 5, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 6, "text": "Line a strainer with fine cloth and pour in the curds and whey."},
            {"step": 7, "text": "Let drain for 30-60 minutes."},
            {"step": 8, "text": "Add salt if desired and mix gently."},
            {"step": 9, "text": "Serve fresh or refrigerate for up to 1 week."}
        ],
        "temperature": "180°F",
        "notes": [
            "Traditional ayib uses the buttermilk leftover from churning Ethiopian butter",
            "The texture is soft and crumbly, similar to cottage cheese or fresh farmer's cheese",
            "Often mixed with mitmita (spice blend) or served plain alongside stews",
            "Essential for balancing the heat of berbere-spiced Ethiopian dishes"
        ],
        "tags": ["cheese", "traditional", "ethiopian", "african", "ayib", "fresh-cheese", "buttermilk-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-rubing-yunnan-chinese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Rubing (Yunnan Goat Cheese)",
        "category": "mains",
        "attribution": "Yunnan Province, China (Bai People), Ancient",
        "source_note": "Rubing ('milk cake') is a traditional cheese of the Bai and other ethnic minorities of Yunnan Province, China. It's one of the few traditional Chinese cheeses and has been made for centuries, typically from goat's milk.",
        "description": "Rare traditional Chinese cheese from Yunnan, made by the Bai people - firm and mild, typically grilled or fried.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "fresh"},
            {"item": "sour liquid", "quantity": "1/4", "unit": "cup", "prep_note": "traditionally from previous batch, or vinegar/lemon juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to a rolling boil in a large pot."},
            {"step": 2, "text": "Reduce heat to maintain a simmer."},
            {"step": 3, "text": "Slowly add the sour liquid (traditional method uses whey from previous batch)."},
            {"step": 4, "text": "Stir gently as curds form and separate from the whey."},
            {"step": 5, "text": "Continue simmering until curds are well-formed."},
            {"step": 6, "text": "Drain curds through a cloth-lined strainer."},
            {"step": 7, "text": "While still warm and pliable, press curds firmly into a block or round shape."},
            {"step": 8, "text": "Weight down and press for 1-2 hours until firm."},
            {"step": 9, "text": "Cut into squares or rectangles for cooking."},
            {"step": 10, "text": "Store refrigerated; eat within 1 week."}
        ],
        "temperature": "Boiling",
        "notes": [
            "Rubing is unusual - it's one of the few traditional Chinese cheeses",
            "Typically pan-fried, grilled, or stir-fried rather than eaten raw",
            "The texture is firm and doesn't melt, similar to paneer or halloumi",
            "Often served with salt and chili, or in stir-fries"
        ],
        "tags": ["cheese", "traditional", "chinese", "yunnan", "bai", "rubing", "goat-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-chhurpi-himalayan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chhurpi (Himalayan Yak Cheese)",
        "category": "mains",
        "attribution": "Himalaya (Nepal, Tibet, Bhutan), Ancient",
        "source_note": "Chhurpi has been made by Himalayan peoples for centuries from yak or chauri (yak-cattle hybrid) milk. The hard version is one of the world's hardest cheeses, traditionally chewed for hours as a trekking snack.",
        "description": "Ancient Himalayan cheese from yak milk, dried until rock-hard - traditionally chewed for hours by Sherpa trekkers.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "Weeks to months drying",
        "total_time": "Several weeks",
        "ingredients": [
            {"item": "yak milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or whole cow's milk as substitute"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": "or buttermilk for souring"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat yak milk to boiling."},
            {"step": 2, "text": "Reduce heat, add lemon juice or soured buttermilk."},
            {"step": 3, "text": "Stir as curds separate from whey."},
            {"step": 4, "text": "Drain curds through cloth. Press firmly to remove moisture."},
            {"step": 5, "text": "For soft chhurpi: Use fresh within a few days."},
            {"step": 6, "text": "For hard chhurpi: Cut pressed curd into small blocks or nuggets."},
            {"step": 7, "text": "Thread onto string and hang in a dry, airy, smoke-filled area."},
            {"step": 8, "text": "Dry for several weeks to months until rock-hard."},
            {"step": 9, "text": "Traditional hard chhurpi is so hard it must be chewed for hours."}
        ],
        "temperature": "Boiling, then air-drying",
        "notes": [
            "Hard chhurpi is one of the world's hardest cheeses - it can take hours to chew",
            "Traditionally smoked during drying over yak dung fires",
            "An essential high-protein, long-lasting food for Himalayan peoples",
            "Soft chhurpi is used in cooking; hard chhurpi is a snack/trail food"
        ],
        "tags": ["cheese", "traditional", "himalayan", "nepali", "tibetan", "chhurpi", "yak-cheese", "dried-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-aaruul-mongolian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Aaruul (Mongolian Dried Curd)",
        "category": "mains",
        "attribution": "Mongolia, Ancient (Nomadic Era)",
        "source_note": "Aaruul has been made by Mongolian nomads for thousands of years as a way to preserve milk. Dried on yurt roofs, it can last for years and was essential food for warriors on campaigns, including Genghis Khan's armies.",
        "description": "Ancient Mongolian dried curd, preserved on yurt roofs - the trail food that sustained Mongol warriors for thousands of years.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "Days to weeks drying",
        "total_time": "1-2 weeks",
        "ingredients": [
            {"item": "aarts or kefir", "quantity": "1/2", "unit": "gallon", "prep_note": "fermented milk, or thick yogurt"},
            {"item": "sugar", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for sweet version"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fermented milk (aarts) or thick, strained yogurt."},
            {"step": 2, "text": "Heat the fermented milk slowly until curds separate."},
            {"step": 3, "text": "Drain through cloth, pressing out whey."},
            {"step": 4, "text": "Mix in sugar if making sweet aaruul (common for children)."},
            {"step": 5, "text": "Form the curd into small shapes - traditionally discs, strips, or molded forms."},
            {"step": 6, "text": "Place on a rack or board in the sun and wind to dry."},
            {"step": 7, "text": "Traditional method: dry on yurt roof in the Mongolian sun and wind."},
            {"step": 8, "text": "Dry for 1-2 weeks until completely hard."},
            {"step": 9, "text": "Store in cloth bags. Properly dried aaruul lasts for years."}
        ],
        "temperature": "Sun and wind drying",
        "notes": [
            "Aaruul can be made from any milk: cow, yak, mare, camel, goat, sheep",
            "When properly dried, it lasts for years without refrigeration",
            "Mongol warriors carried aaruul as essential campaign rations",
            "Rehydrate in tea or chew slowly as a snack"
        ],
        "tags": ["cheese", "traditional", "mongolian", "nomadic", "aaruul", "dried-curd", "preserved", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-byaslag-mongolian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Byaslag (Mongolian Fresh Cheese)",
        "category": "mains",
        "attribution": "Mongolia, Ancient (Nomadic Era)",
        "source_note": "Byaslag is the Mongolian fresh cheese, softer than the dried aaruul. Made in every ger (yurt) when milk is abundant, it's eaten fresh or used in cooking. The simplest form is pressed between two boards.",
        "description": "Fresh Mongolian cheese pressed between boards in the ger - simpler than aaruul, eaten fresh when milk is plentiful.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "2-4 hours pressing",
        "total_time": "3-5 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "any type - cow, yak, mare"},
            {"item": "kefir or yogurt", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk until just simmering."},
            {"step": 2, "text": "Add kefir or yogurt and stir gently."},
            {"step": 3, "text": "Continue heating gently until curds form and separate."},
            {"step": 4, "text": "Drain curds through cloth."},
            {"step": 5, "text": "Add salt if using."},
            {"step": 6, "text": "Traditional method: Place curds in cloth between two flat boards."},
            {"step": 7, "text": "Weight down the top board and press for 2-4 hours."},
            {"step": 8, "text": "Remove from press and cut into slices."},
            {"step": 9, "text": "Eat fresh or use in Mongolian dishes."}
        ],
        "temperature": "Simmering",
        "notes": [
            "Byaslag is softer and fresher than dried aaruul",
            "The board-pressing technique is simple and traditional to the ger",
            "Can be made from any available milk",
            "Used in Mongolian dumplings (buuz) and noodle soups"
        ],
        "tags": ["cheese", "traditional", "mongolian", "nomadic", "byaslag", "fresh-cheese", "pressed", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pecorino-toscano",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Toscano (Tuscan)",
        "category": "mains",
        "attribution": "Tuscany, Italy, Etruscan Era (2500+ years)",
        "source_note": "Pecorino Toscano has been made in Tuscany since at least Etruscan times, over 2500 years ago. Milder than Pecorino Romano, it's aged for less time and has a softer, more delicate flavor that complements Tuscan cuisine.",
        "description": "Ancient Tuscan sheep cheese dating to the Etruscans, milder and softer than Roman pecorino - the table cheese of Tuscany.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "20 days - 4 months aging",
        "total_time": "20 days - 4 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F."},
            {"step": 2, "text": "Add starter culture, stir, and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 25-35 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes (larger than Romano). Let rest 10 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 108°F over 20 minutes while stirring."},
            {"step": 6, "text": "Drain whey and transfer curds to molds."},
            {"step": 7, "text": "Press at 15 lbs for 30 minutes. Flip and press at 30 lbs for 6-8 hours."},
            {"step": 8, "text": "Dry salt or brine for 12-24 hours."},
            {"step": 9, "text": "Age at 55°F and 85% humidity. Fresco: 20 days. Stagionato: 4+ months."}
        ],
        "temperature": "95°F start, 108°F cook, 55°F aging",
        "notes": [
            "Pecorino Toscano is milder and less salty than Pecorino Romano",
            "Fresco (young) is soft and mild, perfect as table cheese",
            "Stagionato (aged) is firmer with more complex flavor",
            "DOP protected; essential to Tuscan cuisine"
        ],
        "tags": ["cheese", "traditional", "italian", "tuscan", "pecorino", "sheep-cheese", "etruscan", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pecorino-romano-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Romano (Ancient Roman)",
        "category": "mains",
        "attribution": "Lazio, Italy (Rome), 2000+ Years",
        "source_note": "Pecorino Romano was part of the daily ration for Roman legions over 2000 years ago. Made in the countryside around Rome (now mostly in Sardinia), it's a hard, salty sheep cheese essential for pasta dishes like cacio e pepe.",
        "description": "The cheese of Roman legions, sharp and salty - essential for cacio e pepe and carbonara, unchanged for over 2000 years.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "5-8 months aging",
        "total_time": "5-8 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional, or liquid rennet"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": "Romano is saltier than other pecorinos"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 100°F (higher than Toscano)."},
            {"step": 2, "text": "Add starter, stir, and ripen for 15 minutes."},
            {"step": 3, "text": "Add lamb rennet paste (traditional) or liquid rennet. Let set 20-25 minutes."},
            {"step": 4, "text": "Cut curd into rice-sized grains (very small). Let rest 5 minutes."},
            {"step": 5, "text": "Raise temperature to 118°F over 30 minutes while stirring constantly."},
            {"step": 6, "text": "Continue stirring at 118°F for 20 minutes until curds are very firm."},
            {"step": 7, "text": "Drain whey and transfer to molds. Press immediately."},
            {"step": 8, "text": "Press at 25 lbs for 1 hour. Flip and press at 50 lbs for 24 hours."},
            {"step": 9, "text": "Dry salt heavily over 2-3 weeks, or brine for several days."},
            {"step": 10, "text": "Age at 55°F and 85% humidity for 5-8 months minimum."}
        ],
        "temperature": "100°F start, 118°F cook, 55°F aging",
        "notes": [
            "Pecorino Romano is saltier and sharper than other pecorinos",
            "The small curd cut and high cooking temperature create the hard texture",
            "Originally from Lazio, now mostly made in Sardinia",
            "Essential for authentic cacio e pepe, carbonara, and amatriciana"
        ],
        "tags": ["cheese", "traditional", "italian", "roman", "pecorino-romano", "sheep-cheese", "legionary", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-anari-cypriot",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Anari (Cypriot Whey Cheese)",
        "category": "mains",
        "attribution": "Cyprus, Ancient",
        "source_note": "Anari has been made in Cyprus since ancient times from the whey left after making halloumi. Fresh anari is soft and mild; dried anari becomes hard and is used for grating. It's Cyprus's ricotta equivalent.",
        "description": "Ancient Cypriot whey cheese, the natural companion to halloumi - soft when fresh, hard when dried for grating.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes fresh; weeks for dried",
        "total_time": "1 hour fresh; 2-3 weeks dried",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from halloumi or other cheese making"},
            {"item": "sheep or goat milk", "quantity": "1", "unit": "cup", "prep_note": "for enrichment"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "for dried version"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh whey from halloumi production (same day)."},
            {"step": 2, "text": "Add fresh milk to enrich the whey."},
            {"step": 3, "text": "Heat slowly, stirring occasionally, until temperature reaches 190°F."},
            {"step": 4, "text": "White curds will rise to the surface."},
            {"step": 5, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 6, "text": "Skim curds gently into a cloth-lined strainer or small baskets."},
            {"step": 7, "text": "For fresh anari: Drain 1-2 hours. Eat within 2-3 days."},
            {"step": 8, "text": "For dried anari: Salt lightly, form into balls or cones."},
            {"step": 9, "text": "Air dry in a cool, airy place for 2-3 weeks until very hard."}
        ],
        "temperature": "190°F",
        "notes": [
            "Fresh anari is traditionally eaten for breakfast with honey or carob syrup",
            "Dried anari (anari xeri) is hard and used for grating over pasta",
            "Always made alongside halloumi - they're traditional partners",
            "The texture of fresh anari is softer and creamier than Italian ricotta"
        ],
        "tags": ["cheese", "traditional", "cypriot", "anari", "whey-cheese", "fresh-cheese", "ancient"],
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
