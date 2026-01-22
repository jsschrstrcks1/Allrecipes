#!/usr/bin/env python3
"""Add batch 52 - Asian, Central Asian, and global traditional cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-chhurpi-himalayan-yak",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chhurpi (Himalayan Yak Cheese)",
        "category": "mains",
        "attribution": "Ancient Himalayan pastoral tradition",
        "source_note": "Traditional Nepali/Tibetan cheesemaking",
        "description": "Made by Himalayan herders for centuries, Chhurpi comes in two forms: soft fresh cheese and incredibly hard dried cheese that can last for years. The hard version is one of the world's hardest cheeses, chewed for hours like gum.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "Fresh: 1-2 days; Hard: 2-4 weeks drying",
        "ingredients": [
            {"item": "yak milk", "quantity": "2", "unit": "gallons", "prep_note": "or chauri (yak-cow hybrid) milk"},
            {"item": "buttermilk or whey", "quantity": "1", "unit": "cup", "prep_note": "as acidifying agent"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional, for soft chhurpi"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat yak milk slowly to 180°F (82°C), stirring to prevent scorching."},
            {"step": 2, "text": "Add buttermilk or whey while stirring - milk will curdle."},
            {"step": 3, "text": "Continue heating and stirring until curds fully separate from whey."},
            {"step": 4, "text": "Remove from heat and let settle 10 minutes."},
            {"step": 5, "text": "Strain through cloth, collecting curds."},
            {"step": 6, "text": "FOR SOFT CHHURPI: Hang cloth to drain 4-8 hours, salt lightly, consume fresh within days."},
            {"step": 7, "text": "FOR HARD CHHURPI: After draining, knead curds thoroughly."},
            {"step": 8, "text": "Form into small blocks or strips."},
            {"step": 9, "text": "Thread string through pieces for hanging."},
            {"step": 10, "text": "Smoke gently over wood fire for 1-2 days (traditional preservation)."},
            {"step": 11, "text": "Hang in dry, airy place for 2-4 weeks until rock hard."},
            {"step": 12, "text": "Hard chhurpi stores for years and is chewed slowly to extract flavor."}
        ],
        "temperature": "180°F (82°C) for curdling",
        "notes": [
            "Yak milk has much higher fat content than cow's milk",
            "Hard chhurpi is chewed for hours - one piece can last all day",
            "Now popular as long-lasting dog chews internationally",
            "Soft chhurpi is similar to paneer, used in curries",
            "Traditional food for Himalayan mountaineers and herders"
        ],
        "tags": ["cheese", "himalayan", "nepali", "tibetan", "yak", "traditional", "dried"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-aaruul-mongolian-dried-curd",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Aaruul (Mongolian Dried Milk Curd)",
        "category": "mains",
        "attribution": "Ancient Mongolian nomadic tradition",
        "source_note": "Traditional Mongolian pastoral cheesemaking",
        "description": "The quintessential Mongolian dairy product, Aaruul has sustained nomadic herders across the steppes for millennia. Made from any milk available (mare, cow, yak, goat, sheep, camel), it's dried hard and stored for harsh winters.",
        "servings_yield": "1 lb dried curd",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "3-7 days drying",
        "ingredients": [
            {"item": "sour milk or yogurt", "quantity": "2", "unit": "quarts", "prep_note": "any animal's milk, naturally soured"},
            {"item": "fresh milk", "quantity": "1", "unit": "quart", "prep_note": "optional, to extend"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with naturally soured milk (tarag/yogurt) - essential for proper acidification."},
            {"step": 2, "text": "Heat soured milk slowly in traditional wide pot, stirring constantly."},
            {"step": 3, "text": "If adding fresh milk, add it now and continue heating."},
            {"step": 4, "text": "Bring to gentle boil, stirring to prevent sticking."},
            {"step": 5, "text": "Curds will separate as mixture boils - continue cooking until thick."},
            {"step": 6, "text": "When curds are fully separated, strain through cloth."},
            {"step": 7, "text": "Press curds in cloth to remove excess whey."},
            {"step": 8, "text": "Spread pressed curd on clean cloth or traditional frame."},
            {"step": 9, "text": "Cut into small pieces or shape into decorative forms."},
            {"step": 10, "text": "Place on ger (yurt) roof or in sunny, airy location."},
            {"step": 11, "text": "Dry for 3-7 days until completely hard."},
            {"step": 12, "text": "Store in cloth bags - keeps for months to years."}
        ],
        "temperature": "Bring to boil for curdling; sun-dry",
        "notes": [
            "Aaruul ranges from sweet to very sour depending on starting milk",
            "Shapes vary by region - some are artistic, some practical",
            "Essential winter food source for Mongolian nomads",
            "Traditionally given as gifts and offerings",
            "Can be eaten as-is, dissolved in tea, or rehydrated in soups"
        ],
        "tags": ["cheese", "mongolian", "nomadic", "traditional", "dried", "curd"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-byaslag-mongolian-pressed",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Byaslag (Mongolian Pressed Cheese)",
        "category": "mains",
        "attribution": "Traditional Mongolian nomadic cuisine",
        "source_note": "Traditional Mongolian cheesemaking",
        "description": "Byaslag is Mongolia's fresh pressed cheese, softer than aaruul and eaten sooner. Made by heating soured milk and pressing the curds, it's a staple of the nomadic diet eaten plain or in traditional dishes.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "1-2 hours",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "cow, yak, or mixed"},
            {"item": "kefir or yogurt", "quantity": "1", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix milk with kefir or yogurt starter and let sit overnight to sour."},
            {"step": 2, "text": "Heat soured milk slowly, stirring constantly."},
            {"step": 3, "text": "Bring to gentle boil until curds separate from whey."},
            {"step": 4, "text": "Continue cooking until curds are well formed."},
            {"step": 5, "text": "Strain through cloth, collecting curds."},
            {"step": 6, "text": "Add salt if desired while curds are still warm."},
            {"step": 7, "text": "Place curds in cloth-lined mold or form."},
            {"step": 8, "text": "Press with weights (traditionally heavy boards or stones)."},
            {"step": 9, "text": "Press for several hours, flipping once."},
            {"step": 10, "text": "Remove from mold when firm but still moist."},
            {"step": 11, "text": "Eat fresh within a few days, or slice and dry for longer storage."}
        ],
        "temperature": "Bring to boil for curdling",
        "notes": [
            "Softer and fresher than aaruul",
            "Traditional breakfast food with tea",
            "Can be sliced and partially dried for longer keeping",
            "Mild, slightly sour flavor",
            "Often made in decorative molds for special occasions"
        ],
        "tags": ["cheese", "mongolian", "nomadic", "traditional", "fresh", "pressed"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-rushan-chinese-fan-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Rushan (Chinese Bai Fan Cheese)",
        "category": "mains",
        "attribution": "Bai ethnic minority tradition, Yunnan",
        "source_note": "Traditional Chinese minority cheesemaking",
        "description": "A unique Chinese cheese from the Bai people of Yunnan province, Rushan ('milk fan') is stretched cheese dried in thin fan-shaped sheets. It represents rare cheesemaking tradition in a country not known for dairy.",
        "servings_yield": "8-10 sheets",
        "prep_time": "20 minutes",
        "cook_time": "1-2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "acid whey or vinegar", "quantity": "1/2", "unit": "cup", "prep_note": "papaya juice traditional"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 140°F (60°C)."},
            {"step": 2, "text": "Slowly add acid (traditionally papaya juice) while stirring."},
            {"step": 3, "text": "Continue heating and stirring as curds form."},
            {"step": 4, "text": "When curds fully separate, drain off whey."},
            {"step": 5, "text": "Knead curds while still warm until smooth and elastic."},
            {"step": 6, "text": "Using two sticks, stretch curd into thin sheet like pulling taffy."},
            {"step": 7, "text": "Wrap stretched sheet around one stick, continue pulling."},
            {"step": 8, "text": "Fan out into thin, semi-circular 'fan' shape."},
            {"step": 9, "text": "Drape over bamboo rack to dry."},
            {"step": 10, "text": "Dry until firm but still pliable (few hours to overnight)."},
            {"step": 11, "text": "Can be eaten fresh, grilled, or deep-fried."}
        ],
        "temperature": "140°F (60°C) for curdling; stretch while warm",
        "notes": [
            "Rushan means 'milk fan' describing the shape",
            "One of China's only indigenous stretched-curd cheeses",
            "Papaya enzyme (papain) was traditional coagulant",
            "Popular street food in Dali - often wrapped around sweet fillings",
            "Can be grilled until golden and slightly crispy"
        ],
        "tags": ["cheese", "chinese", "yunnan", "bai", "traditional", "stretched", "dried"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-rubing-chinese-goat-cube",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Rubing (Yunnan Goat Cheese Cubes)",
        "category": "mains",
        "attribution": "Sani people tradition, Yunnan",
        "source_note": "Traditional Chinese minority cheesemaking",
        "description": "Made by the Sani people (Yi ethnic group) in Yunnan's Stone Forest region, Rubing is fresh goat cheese pressed into dense cubes. Often grilled until golden brown, it's one of China's most distinctive traditional cheeses.",
        "servings_yield": "1 lb cheese cubes",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "2", "unit": "gallons", "prep_note": "from local Yunnan goats"},
            {"item": "acid solution", "quantity": "1/2", "unit": "cup", "prep_note": "fermented acid water or vinegar"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 175°F (80°C), stirring occasionally."},
            {"step": 2, "text": "Slowly pour in acid while stirring gently."},
            {"step": 3, "text": "Continue stirring as curds form and separate from whey."},
            {"step": 4, "text": "Remove from heat when curds are well formed."},
            {"step": 5, "text": "Strain through cloth, letting whey drain."},
            {"step": 6, "text": "While still warm, knead curds to make smooth."},
            {"step": 7, "text": "Press into square or rectangular molds."},
            {"step": 8, "text": "Press with weights for 1-2 hours until very firm."},
            {"step": 9, "text": "Unmold and cut into small cubes (about 1-inch)."},
            {"step": 10, "text": "Eat fresh, or grill/pan-fry until golden brown."}
        ],
        "temperature": "175°F (80°C) for curdling",
        "notes": [
            "Rubing means 'milk cake' in Chinese",
            "The Sani have made this cheese for generations",
            "Traditionally grilled over charcoal and eaten with salt and chili",
            "Dense, chewy texture that holds up well to grilling",
            "Best eaten very fresh - does not store long"
        ],
        "tags": ["cheese", "chinese", "yunnan", "goat", "traditional", "fresh", "grilled"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-karish-egyptian-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Karish (Ancient Egyptian Soft Cheese)",
        "category": "mains",
        "attribution": "Ancient Egyptian tradition",
        "source_note": "Traditional Egyptian cheesemaking",
        "description": "Karish is Egypt's oldest and most traditional cheese, made for millennia by simply souring milk and draining it. Archaeological evidence suggests similar cheeses were made in ancient Egypt. Today it remains a staple of the Egyptian breakfast table.",
        "servings_yield": "1 lb cheese",
        "prep_time": "10 minutes",
        "cook_time": "24-48 hours souring",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw buffalo milk", "quantity": "1", "unit": "gallon", "prep_note": "or cow's milk"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour fresh milk into clay pot or glass jar (traditional: 'ballas' earthenware pot)."},
            {"step": 2, "text": "Cover loosely and let sit at warm room temperature."},
            {"step": 3, "text": "Allow milk to naturally sour and curdle - 24-48 hours depending on temperature."},
            {"step": 4, "text": "When milk has fully curdled and whey separates, skim off cream that rises."},
            {"step": 5, "text": "Gently ladle curds into cloth-lined strainer."},
            {"step": 6, "text": "Let drain naturally for several hours - do not press."},
            {"step": 7, "text": "Transfer soft curds to serving container."},
            {"step": 8, "text": "Salt lightly if desired."},
            {"step": 9, "text": "Refrigerate and consume within 3-5 days."}
        ],
        "temperature": "Room temperature for souring; refrigerate after",
        "notes": [
            "Name may derive from 'karoish' meaning to curdle/shrivel",
            "Buffalo milk makes richer, creamier karish",
            "Traditional Egyptian breakfast: karish with honey and bread",
            "The clay pot contributes to the souring process through retained cultures",
            "One of the simplest cheeses in existence - no rennet, no heat"
        ],
        "tags": ["cheese", "egyptian", "traditional", "ancient", "fresh", "simple", "buffalo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-mish-egyptian-aged-fermented",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mish (Egyptian Fermented Cheese)",
        "category": "mains",
        "attribution": "Ancient Egyptian fermented tradition",
        "source_note": "Traditional Egyptian cheesemaking",
        "description": "Mish is Egypt's pungent, fermented cheese - essentially karish that has been salted and aged in brine until it develops powerful flavors. The strong, sharp taste is beloved in Egyptian cuisine despite (or because of) its intensity.",
        "servings_yield": "1 lb cheese",
        "prep_time": "10 minutes",
        "cook_time": "N/A",
        "total_time": "1-4 months fermentation",
        "ingredients": [
            {"item": "karish cheese", "quantity": "1", "unit": "lb", "prep_note": "homemade or purchased"},
            {"item": "salt", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "soured milk or whey", "quantity": "1", "unit": "cup", "prep_note": "for brine"},
            {"item": "dried mint", "quantity": "1", "unit": "tbsp", "prep_note": "optional, traditional"},
            {"item": "red pepper flakes", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with well-drained karish cheese."},
            {"step": 2, "text": "Mix salt thoroughly into cheese, breaking it into crumbly pieces."},
            {"step": 3, "text": "Add dried herbs and spices if using (mint and pepper are traditional)."},
            {"step": 4, "text": "Pack salted cheese tightly into clay pot or glass jar."},
            {"step": 5, "text": "Pour soured milk or whey over to barely cover."},
            {"step": 6, "text": "Cover pot - traditionally with clay lid sealed with dough."},
            {"step": 7, "text": "Store in cool, dark place for 1-4 months."},
            {"step": 8, "text": "Cheese will ferment, developing strong flavors and softer texture."},
            {"step": 9, "text": "When ready, mish will be pungent, tangy, and spreadable."},
            {"step": 10, "text": "Store refrigerated once opened; keeps for months."}
        ],
        "temperature": "Cool room temperature for fermentation; refrigerate after opening",
        "notes": [
            "Mish is an acquired taste - intensely sour and salty",
            "Traditional breakfast spread on fresh bread",
            "The fermentation was originally a preservation method",
            "Clay pots are traditional and contribute to flavor development",
            "Can be very strong - some versions ferment for over a year"
        ],
        "tags": ["cheese", "egyptian", "traditional", "ancient", "fermented", "aged", "strong"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-braided-string-cheese-oaxacan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Quesillo (Oaxacan String Cheese)",
        "category": "mains",
        "attribution": "Oaxacan mestizo tradition",
        "source_note": "Traditional Mexican pasta filata cheesemaking",
        "description": "Mexico's unique stretched-curd cheese, Quesillo originated in Oaxaca but is now beloved throughout Mexico. Unlike European pasta filata cheeses, it's traditionally stretched into long ribbons and wound into balls, creating the distinctive 'string cheese' pull.",
        "servings_yield": "1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw preferred"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or fresh whey"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add starter or fresh whey, ripen 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch pieces."},
            {"step": 5, "text": "Let curds acidify under whey for 3-4 hours until pH reaches 5.2-5.3."},
            {"step": 6, "text": "Test stretchability: small piece should stretch smoothly in hot water."},
            {"step": 7, "text": "Drain curds and cut into strips."},
            {"step": 8, "text": "Heat water to 170°F (77°C)."},
            {"step": 9, "text": "Submerge curd strips in hot water."},
            {"step": 10, "text": "When pliable, stretch into long, thin ribbons (key difference from mozzarella)."},
            {"step": 11, "text": "Salt ribbons as you stretch."},
            {"step": 12, "text": "Wind ribbons into balls, starting from center out."},
            {"step": 13, "text": "Cool in cold water briefly to set shape."},
            {"step": 14, "text": "Best eaten fresh same day; keeps refrigerated 1-2 weeks."}
        ],
        "temperature": "90°F (32°C) for curd; 170°F (77°C) for stretching",
        "notes": [
            "The key is stretching into ribbons, not kneading into ball like mozzarella",
            "Traditional balls can weigh several pounds",
            "Essential for quesadillas, tlayudas, and other Oaxacan dishes",
            "The 'string' pull comes from aligned protein strands",
            "Also called queso Oaxaca or quesillo de Oaxaca"
        ],
        "tags": ["cheese", "mexican", "oaxacan", "traditional", "pasta-filata", "string", "fresh"],
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
