#!/usr/bin/env python3
"""Add batch 63 - Ancient Central Asian and Asian cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-kurt-central-asian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kurt/Qurt (Central Asian Dried Cheese Balls)",
        "category": "mains",
        "attribution": "Ancient Turkic/Mongolian nomadic tradition",
        "source_note": "Modernized from traditional Central Asian nomadic methods, adapted for home cheesemaking",
        "description": "An ingenious preservation cheese from the Central Asian steppes, kurt (also qurt, kurut) are rock-hard dried cheese balls that kept for months without refrigeration. Essential for nomadic herders, they were reconstituted in water for soup or gnawed as trail snacks. Still popular across Kazakhstan, Kyrgyzstan, and Mongolia.",
        "servings_yield": "About 30 cheese balls",
        "prep_time": "1 hour",
        "cook_time": "None",
        "total_time": "1 hour active plus 5-10 days drying",
        "ingredients": [
            {"item": "plain yogurt", "quantity": "2", "unit": "quarts", "prep_note": "full-fat, or drained whey from cheese"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "to taste"},
            {"item": "cheesecloth", "quantity": "1", "unit": "yard", "prep_note": "for straining"}
        ],
        "instructions": [
            {"step": 1, "text": "Place yogurt in cheesecloth-lined colander. Hang over bowl and drain for 24-48 hours until very thick."},
            {"step": 2, "text": "Alternatively, use the strained solids left from making other cheeses mixed with yogurt."},
            {"step": 3, "text": "Mix drained yogurt with salt. The mixture should be quite dry and moldable."},
            {"step": 4, "text": "Roll mixture into small balls about 1 inch in diameter. Traditional kurt are sometimes flattened or shaped differently by region."},
            {"step": 5, "text": "Place balls on a drying rack or screen in a well-ventilated area. Hot, dry climate is ideal."},
            {"step": 6, "text": "Dry for 5-10 days, turning occasionally, until completely hard - they should be rock-like."},
            {"step": 7, "text": "In humid climates, use a food dehydrator at 115°F (46°C) for 24-48 hours, or a very low oven."},
            {"step": 8, "text": "Properly dried kurt will sound hollow when tapped together and be very hard."},
            {"step": 9, "text": "Store in a breathable cloth bag at room temperature. Will keep for months or even years."},
            {"step": 10, "text": "To use: dissolve in hot water for soup base, soak to soften, or gnaw slowly as a salty snack."}
        ],
        "temperature": "Dry at room temperature or 115°F in dehydrator",
        "notes": [
            "Mongolian and Turkic nomads carried kurt for months on horseback",
            "The intense drying allows storage without refrigeration for very long periods",
            "Flavor ranges from mildly tangy to intensely sour depending on base ingredient",
            "Modern Central Asian stores sell machine-made kurt, but traditional is still made",
            "Can be made from any dairy culture: sheep, goat, cow, mare, even camel milk"
        ],
        "tags": ["cheese", "cheesemaking", "central-asian", "mongolian", "kazakh", "kyrgyz", "dried-cheese", "nomadic", "ancient", "preservation"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-aaruul-mongolian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Aaruul (Mongolian Dried Curd Cheese)",
        "category": "mains",
        "attribution": "Ancient Mongolian nomadic tradition",
        "source_note": "Modernized from traditional Mongolian methods, adapted for home cheesemaking",
        "description": "Mongolia's most important dairy preservation, aaruul are dried curds that can be made from any milk - cow, yak, sheep, goat, or the prized mare's milk. The distinctive shapes (pressed in carved molds) were traditionally unique to each family. Aaruul was the food that fueled Genghis Khan's armies.",
        "servings_yield": "About 20-30 pieces",
        "prep_time": "1 hour",
        "cook_time": "3 hours initial",
        "total_time": "4 hours active plus 3-7 days drying",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "any type, or use cultured buttermilk"},
            {"item": "plain yogurt or kefir", "quantity": "1", "unit": "cup", "prep_note": "as starter"},
            {"item": "sugar", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for sweet aaruul"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk with yogurt or kefir. Cover and leave at room temperature 24-48 hours to ferment and thicken."},
            {"step": 2, "text": "Pour fermented milk into heavy pot. Heat over low flame, stirring, until curds separate from whey."},
            {"step": 3, "text": "Continue cooking gently for 1-2 hours until curds become thick and paste-like. Stir frequently to prevent burning."},
            {"step": 4, "text": "The mixture will reduce significantly and become a thick, spreadable mass."},
            {"step": 5, "text": "For sweet aaruul, add sugar and mix well. Traditional aaruul is unsweetened but modern versions often add sugar."},
            {"step": 6, "text": "Spread the hot curd onto a flat surface or into molds. Traditional molds have carved patterns."},
            {"step": 7, "text": "Cut into pieces or shapes while still warm and pliable."},
            {"step": 8, "text": "Dry in sun or well-ventilated area for 3-7 days. In Mongolian summers, the sun and wind dry aaruul quickly."},
            {"step": 9, "text": "Finished aaruul should be hard and completely dry. Soft spots indicate more drying needed."},
            {"step": 10, "text": "Store in cloth bags. Will keep for years. Eat as-is or soften in tea."}
        ],
        "temperature": "Low simmer for cooking, ambient drying",
        "notes": [
            "Mongolian families traditionally have carved wooden molds passed down generations",
            "Genghis Khan's soldiers carried aaruul mixed into water pouches - it would dissolve into an energy drink",
            "Yak milk aaruul is creamier; mare's milk version (considered finest) is tangier",
            "Modern commercial aaruul often contains sugar; traditional is purely sour",
            "The small pieces are designed to be held in cheek and slowly dissolved"
        ],
        "tags": ["cheese", "cheesemaking", "mongolian", "dried-cheese", "nomadic", "ancient", "preservation", "yak-milk"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-byaslag-mongolian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Byaslag (Mongolian Fresh Pressed Cheese)",
        "category": "mains",
        "attribution": "Traditional Mongolian cheese",
        "source_note": "Modernized from traditional Mongolian methods, adapted for home cheesemaking",
        "description": "Unlike the dried aaruul, byaslag is a fresh cheese eaten within days. Pressed into rectangular blocks and sliced for eating, it's mild, dense, and slightly chewy. This fresh cheese tradition exists alongside the dried varieties, typically made when milk is abundant in summer.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "2 hours plus pressing time",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "cow, yak, or sheep"},
            {"item": "yogurt or kefir", "quantity": "1", "unit": "cup", "prep_note": "as acid source"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in a large pot to 185°F (85°C), stirring occasionally to prevent scorching."},
            {"step": 2, "text": "Remove from heat. Stir in yogurt or kefir. The milk will curdle and separate."},
            {"step": 3, "text": "Let stand 10-15 minutes for curds to fully form and consolidate."},
            {"step": 4, "text": "Line a colander with cheesecloth. Ladle curds into cloth, letting whey drain."},
            {"step": 5, "text": "Gather cloth corners and squeeze gently to remove more whey."},
            {"step": 6, "text": "Transfer curds to a rectangular mold or shape by hand into a block."},
            {"step": 7, "text": "Press with moderate weight (5-10 lbs) for 2-4 hours or overnight."},
            {"step": 8, "text": "Remove from mold. Salt surface lightly if desired."},
            {"step": 9, "text": "Slice and serve fresh with tea and bread. Traditional Mongolian meals include byaslag."},
            {"step": 10, "text": "Store refrigerated for up to 1 week. Does not keep long - meant to be eaten fresh."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Byaslag is the fresh cheese counterpart to dried aaruul in Mongolian cuisine",
            "Made in summer when milk production peaks and there's no time to dry everything",
            "Can be lightly smoked for longer preservation",
            "The texture is similar to farmer's cheese or paneer",
            "Mongolian herders traditionally make both fresh and dried cheeses from same batch"
        ],
        "tags": ["cheese", "cheesemaking", "mongolian", "fresh-cheese", "pressed-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-chhurpi-himalayan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chhurpi (Himalayan Yak Cheese)",
        "category": "mains",
        "attribution": "Ancient Himalayan tradition (Tibet, Nepal, Bhutan)",
        "source_note": "Modernized from traditional Himalayan methods, adapted for home cheesemaking",
        "description": "The legendary hard cheese of the Himalayas, chhurpi is dried yak cheese that becomes so hard it takes hours to chew a small piece. Used as a long-lasting snack by mountain dwellers, it's now marketed globally as a long-lasting dog chew! The soft version (fresh chhurpi) is a delicacy eaten with rice.",
        "servings_yield": "About 1 lb hard chhurpi or 1.5 lbs soft",
        "prep_time": "2 hours",
        "cook_time": "Variable",
        "total_time": "3 hours active plus weeks of drying for hard version",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "yak milk traditional, cow milk acceptable"},
            {"item": "lemon juice or vinegar", "quantity": "1/3", "unit": "cup", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185°F (85°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat and add lemon juice or vinegar. Stir gently as curds form."},
            {"step": 3, "text": "Let sit 15 minutes for complete separation."},
            {"step": 4, "text": "Drain through cheesecloth-lined colander. Squeeze out excess whey."},
            {"step": 5, "text": "For SOFT CHHURPI: Mix with salt, press lightly, and refrigerate. Eat within a week with rice or vegetables."},
            {"step": 6, "text": "For HARD CHHURPI: Press firmly overnight to remove all moisture."},
            {"step": 7, "text": "Cut pressed cheese into 1-inch cubes or small blocks."},
            {"step": 8, "text": "String pieces on cord or place on rack. Dry over smoky fire or in well-ventilated area."},
            {"step": 9, "text": "Continue drying for 3-6 weeks until rock-hard. Traditional chhurpi is smoked during drying."},
            {"step": 10, "text": "Hard chhurpi is gnawed slowly over hours, or soaked in liquid to soften. Stores indefinitely."}
        ],
        "temperature": "185°F (85°C) for curdling",
        "notes": [
            "Real yak milk chhurpi is extremely hard - takes hours to chew through one piece",
            "Now marketed as 'Himalayan dog chews' in Western countries",
            "Soft chhurpi has a texture like ricotta and is a prized fresh delicacy",
            "Traditional drying over juniper smoke adds distinctive flavor",
            "Sherpa and Tibetan herders have made chhurpi for centuries"
        ],
        "tags": ["cheese", "cheesemaking", "himalayan", "tibetan", "nepali", "yak-cheese", "dried-cheese", "ancient", "preservation"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-chhena-indian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Chhena/Chhana (Indian Fresh Acid-Set Curd)",
        "category": "mains",
        "attribution": "Ancient Indian subcontinent tradition",
        "source_note": "Modernized from traditional Indian methods, adapted for home cheesemaking",
        "description": "Chhena is the fresh curd that becomes the base for countless Indian sweets like rasgulla, sandesh, and cham cham. Unlike paneer (which is pressed), chhena remains soft and malleable. The technique of acid-curdling milk is ancient in India, with records going back over 2,000 years.",
        "servings_yield": "About 1.5 cups chhena",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes plus draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "full-fat, not ultra-pasteurized"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "or white vinegar"},
            {"item": "water", "quantity": "1", "unit": "cup", "prep_note": "cold, for stopping cooking"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in heavy-bottomed pot over medium heat, stirring frequently to prevent scorching."},
            {"step": 2, "text": "Watch carefully as milk approaches boiling. When it rises in the pot and small bubbles form, remove from heat."},
            {"step": 3, "text": "Immediately add lemon juice, stirring gently. Curds will form and separate from greenish whey."},
            {"step": 4, "text": "Add cold water to stop the cooking process. This keeps chhena soft and prevents graininess."},
            {"step": 5, "text": "Let sit 5 minutes for curds to fully separate."},
            {"step": 6, "text": "Pour through muslin or fine cheesecloth. Rinse briefly with cold water to remove acid taste."},
            {"step": 7, "text": "Gather cloth and hang for 30-45 minutes. Do not press - chhena should remain moist."},
            {"step": 8, "text": "Transfer to bowl and knead briefly with heel of palm until smooth. The texture should be like soft dough."},
            {"step": 9, "text": "Use immediately for sweets, or refrigerate up to 2 days (texture degrades quickly)."},
            {"step": 10, "text": "For best results in sweets, chhena should be fresh, soft, and slightly moist - never dry or crumbly."}
        ],
        "temperature": "Bring to just below boiling, about 200°F (93°C)",
        "notes": [
            "Chhena and paneer start the same way - the difference is pressing and kneading",
            "The quality of chhena determines the quality of Bengali sweets",
            "Too much acid makes grainy chhena; too little won't separate curds properly",
            "The cold water wash is crucial for smooth texture",
            "Buffalo milk makes richer chhena but cow milk is more common"
        ],
        "tags": ["cheese", "cheesemaking", "indian", "chhena", "fresh-cheese", "acid-set", "ancient", "sweets-base", "bengali"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-rushan-chinese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Rushan (Chinese Bai Minority Fan-Shaped Cheese)",
        "category": "mains",
        "attribution": "Bai ethnic minority, Yunnan Province, China",
        "source_note": "Modernized from traditional Bai minority methods, adapted for home cheesemaking",
        "description": "One of China's rare traditional cheeses, rushan (meaning 'milk fan') is made by the Bai minority in Yunnan Province. The stretchy curd is wrapped around bamboo sticks and dried into fan-like shapes. When fried and dusted with sugar, it becomes a beloved Yunnan street snack.",
        "servings_yield": "About 12 rushan fans",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus drying time",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "cow or goat"},
            {"item": "acidic whey", "quantity": "2", "unit": "cups", "prep_note": "or 1/4 cup white vinegar mixed with water"},
            {"item": "bamboo sticks or chopsticks", "quantity": "12", "unit": "", "prep_note": "for wrapping"},
            {"item": "sugar", "quantity": "as needed", "unit": "", "prep_note": "for serving"},
            {"item": "oil", "quantity": "as needed", "unit": "", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 150°F (65°C) in a large wok or wide pan. The shallow shape is traditional."},
            {"step": 2, "text": "Slowly add acidic whey or diluted vinegar while stirring. Curds will form and stretch."},
            {"step": 3, "text": "Keep stirring over heat as the curds become stretchy like mozzarella. This takes 15-20 minutes."},
            {"step": 4, "text": "When curd forms a stretchy mass, use chopsticks to lift and stretch it repeatedly."},
            {"step": 5, "text": "Take a portion of the stretched curd and wrap it around a bamboo stick in overlapping layers."},
            {"step": 6, "text": "Spread and flatten the wrapped curd into a thin, fan-like shape on the stick."},
            {"step": 7, "text": "Repeat with remaining curd. Place sticks in sun or well-ventilated area to dry for 2-3 days."},
            {"step": 8, "text": "Dried rushan becomes stiff and can be stored for months."},
            {"step": 9, "text": "To serve: heat oil and fry dried rushan until puffed and golden. Dust with sugar while hot."},
            {"step": 10, "text": "Can also be grilled over charcoal, which is the street food method in Dali, Yunnan."}
        ],
        "temperature": "150°F (65°C) for curdling",
        "notes": [
            "Rushan is one of very few indigenous Chinese cheese traditions",
            "The Bai people of Dali have made this for generations using water buffalo milk",
            "Fresh rushan (before drying) is also eaten, similar to mozzarella",
            "Street vendors in Dali grill rushan over charcoal and add various toppings",
            "The cheese-making tradition likely came via ancient trade routes"
        ],
        "tags": ["cheese", "cheesemaking", "chinese", "yunnan", "bai-minority", "stretched-curd", "ancient", "street-food"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-rubing-chinese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Rubing (Chinese Goat Cheese Cubes)",
        "category": "mains",
        "attribution": "Sani people, Yunnan Province, China",
        "source_note": "Modernized from traditional Sani Yi minority methods, adapted for home cheesemaking",
        "description": "Another of China's rare indigenous cheeses, rubing comes from the Sani subgroup of the Yi minority in Yunnan's Stone Forest region. Made from goat milk, it's formed into small cubes and pan-fried until golden. The mild, squeaky texture is similar to halloumi.",
        "servings_yield": "About 20 cubes",
        "prep_time": "30 minutes",
        "cook_time": "1.5 hours",
        "total_time": "2 hours plus pressing",
        "ingredients": [
            {"item": "goat milk", "quantity": "1/2", "unit": "gallon", "prep_note": "cow milk works but goat is traditional"},
            {"item": "acid whey", "quantity": "1/2", "unit": "cup", "prep_note": "or 2 tbsp white vinegar"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "oil", "quantity": "2", "unit": "tbsp", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 185°F (85°C), stirring occasionally."},
            {"step": 2, "text": "Remove from heat. Add acid whey or vinegar while stirring gently. Curds will form immediately."},
            {"step": 3, "text": "Let sit 10 minutes for curds to consolidate."},
            {"step": 4, "text": "Pour through cheesecloth-lined colander. Let drain 10 minutes."},
            {"step": 5, "text": "Gather cloth and squeeze to remove more whey. Mix in salt."},
            {"step": 6, "text": "Press cheese in small square mold or shape by hand into a block."},
            {"step": 7, "text": "Press with moderate weight for 2 hours or until quite firm."},
            {"step": 8, "text": "Cut block into 1-inch cubes. These can be stored refrigerated for a few days."},
            {"step": 9, "text": "To serve: pan-fry cubes in a little oil over medium heat until golden on all sides."},
            {"step": 10, "text": "Serve hot with dipping sauce or as part of Yunnan-style hot pot."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Rubing is specifically a Sani Yi minority cheese from Shilin (Stone Forest) area",
            "The texture is squeaky like halloumi or fresh cheese curds",
            "Must be eaten fried - not typically eaten raw",
            "Often served with a spicy dipping sauce in Yunnan restaurants",
            "The Sani have made this cheese for generations alongside their goat herding"
        ],
        "tags": ["cheese", "cheesemaking", "chinese", "yunnan", "yi-minority", "sani", "goat-cheese", "fried-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-airag-cheese-mongolian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Airag Cheese (Mongolian Fermented Mare's Milk Curds)",
        "category": "mains",
        "attribution": "Ancient Mongolian nomadic tradition",
        "source_note": "Modernized interpretation using available ingredients, inspired by traditional methods",
        "description": "Airag (fermented mare's milk, also called kumis) is the legendary drink of the Mongol steppes. The curds that form during fermentation are collected and dried into a distinctive tangy cheese. Since mare's milk is unavailable to most, this recipe adapts the technique using kefir-fermented milk.",
        "servings_yield": "About 1 cup dried curds",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "2 hours active plus 2 weeks fermentation and drying",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "raw if possible"},
            {"item": "kefir grains", "quantity": "2", "unit": "tbsp", "prep_note": "or 1 cup active kefir"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk with kefir grains or active kefir in a jar. Cover loosely."},
            {"step": 2, "text": "Keep at room temperature, stirring vigorously twice daily. The stirring is traditional and important."},
            {"step": 3, "text": "Continue fermenting 5-7 days until very sour, slightly effervescent, and thickened."},
            {"step": 4, "text": "The mixture will separate somewhat. The thicker curds that form are what we're after."},
            {"step": 5, "text": "Strain through fine cheesecloth. The liquid is a drinkable probiotic (airag-style beverage)."},
            {"step": 6, "text": "The curds collected in the cloth are the cheese base. Salt lightly if desired."},
            {"step": 7, "text": "Roll curds into small balls or spread thin on a mat."},
            {"step": 8, "text": "Dry in sun or dehydrator until completely hard, 5-10 days."},
            {"step": 9, "text": "These dried curds have a distinctive tangy, fermented flavor unlike other cheeses."},
            {"step": 10, "text": "Store in breathable container. Eat as snack or dissolve in hot water for traditional beverage."}
        ],
        "temperature": "Room temperature fermentation",
        "notes": [
            "True airag requires mare's milk, which is very low in fat and high in lactose",
            "The vigorous daily stirring mimics the constant agitation of milk in saddlebags on horseback",
            "This adaptation captures the tangy, fermented character if not the exact flavor",
            "Airag was sacred to Mongols - offered to guests and used in ceremonies",
            "The alcohol content of true airag is low (2-3%) due to lactose fermentation"
        ],
        "tags": ["cheese", "cheesemaking", "mongolian", "fermented", "airag", "kumis", "mare-milk", "ancient", "nomadic", "kefir"],
        "confidence": {"overall": "medium", "flags": ["Adapted recipe - true airag requires mare's milk"]}
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
