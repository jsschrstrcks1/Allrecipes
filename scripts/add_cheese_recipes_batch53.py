#!/usr/bin/env python3
"""Add batch 53 - More ancient Mediterranean and historical cheeses plus tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-whey-utilization",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Creative Whey Utilization",
        "category": "mains",
        "attribution": "Traditional zero-waste cheesemaking",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Whey is the liquid gold of cheesemaking - don't waste it! Traditional cheesemakers had dozens of uses for whey, from making ricotta to feeding livestock to baking bread. Here's how to maximize this valuable byproduct.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "fresh whey", "quantity": "", "unit": "", "prep_note": "from any cheesemaking"},
            {"item": "acid for ricotta", "quantity": "", "unit": "", "prep_note": "vinegar or citric acid"},
            {"item": "storage containers", "quantity": "", "unit": "", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "RICOTTA: Heat fresh whey to 200°F, add acid, let curds form. Skim delicate ricotta curds. Makes about 1 cup per gallon of whey."},
            {"step": 2, "text": "BREAD BAKING: Replace water or milk in bread recipes with whey. Adds protein, nutrients, and subtle tang. Excellent in sourdough."},
            {"step": 3, "text": "LACTO-FERMENTATION: Use whey as starter for lacto-fermented vegetables. 2-3 tbsp per quart of vegetables speeds fermentation."},
            {"step": 4, "text": "SOUP STOCK: Use whey as base for soups - traditional in Nordic and Alpine cooking. Particularly good with pork and beans."},
            {"step": 5, "text": "SMOOTHIES: Add whey to smoothies for protein and probiotics. Blend with fruit to mask any sour notes."},
            {"step": 6, "text": "COOKING GRAINS: Cook rice, oatmeal, or other grains in whey instead of water for added nutrition."},
            {"step": 7, "text": "ANIMAL FEED: Pigs particularly thrive on whey - traditional use on farmsteads. Chickens also benefit."},
            {"step": 8, "text": "GARDEN FERTILIZER: Diluted whey (1:4 with water) adds nutrients to soil. Acid-loving plants benefit most."},
            {"step": 9, "text": "WHEY CHEESE: Some traditions make 'second cheeses' from whey alone - Mysost (Norwegian), Gjetost, Ziger."},
            {"step": 10, "text": "MARINADES: Use whey to tenderize meat - the lactic acid breaks down proteins gently."},
            {"step": 11, "text": "STARTER CULTURE: Save acidic whey from this batch to start the next - traditional method."},
            {"step": 12, "text": "Storage: Fresh whey keeps 1-2 weeks refrigerated; acidic whey keeps longer."}
        ],
        "temperature": "N/A",
        "notes": [
            "Sweet whey (from rennet cheeses) vs acid whey (from acid-set cheeses) have different uses",
            "Don't discard whey down the drain - it's rich in lactose and can stress septic systems",
            "Commercial cheesemakers produce tons of whey - it's an industry challenge",
            "Traditional farmstead operations had complete whey utilization cycles",
            "Whey protein is now a valuable supplement - you're making it fresh!"
        ],
        "tags": ["cheese", "technique", "tip", "whey", "zero-waste", "utilization"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-halloumi-cyprus-grilling",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Halloumi (Cyprus Grilling Cheese)",
        "category": "mains",
        "attribution": "Medieval Cypriot tradition",
        "source_note": "Traditional Cypriot stretched-curd cheesemaking",
        "description": "Cyprus's gift to the world, Halloumi is a unique stretched-curd cheese that doesn't melt when heated - it grills to a perfect golden crust while staying intact. Made from sheep and goat milk since at least medieval times, it's now internationally beloved.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "Same day to 1 month aged",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1", "unit": "gallon", "prep_note": "traditional"},
            {"item": "raw goat's milk", "quantity": "1", "unit": "gallon", "prep_note": "traditional blend"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "plus more for brine"},
            {"item": "dried mint", "quantity": "2", "unit": "tbsp", "prep_note": "traditional addition"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep and goat milk (traditional ratio about 60/40)."},
            {"step": 2, "text": "Heat to 95°F (35°C)."},
            {"step": 3, "text": "Add rennet without starter culture (traditional method)."},
            {"step": 4, "text": "Let set 45-60 minutes until very firm curd."},
            {"step": 5, "text": "Cut curds into large pieces, then let rest."},
            {"step": 6, "text": "Gently heat curds in whey to 104°F (40°C), stirring occasionally."},
            {"step": 7, "text": "Drain curds and pack into molds, press lightly for 1-2 hours."},
            {"step": 8, "text": "Heat whey to 195°F (90°C)."},
            {"step": 9, "text": "Cut pressed cheese into blocks and poach in hot whey for 30-40 minutes."},
            {"step": 10, "text": "Remove when cheese floats - this is the key step that prevents melting."},
            {"step": 11, "text": "Salt poached cheese, sprinkle with dried mint, fold in half."},
            {"step": 12, "text": "Store in brine or eat fresh. Traditional halloumi ages in brine for weeks."}
        ],
        "temperature": "95-104°F (35-40°C) for curd; 195°F (90°C) for poaching",
        "notes": [
            "The whey poaching denatures proteins, preventing melting - unique technique",
            "PDO protected since 2021 - must be made in Cyprus from local milk",
            "Folding with mint inside is the traditional presentation",
            "Grills, pan-fries, or bakes without melting",
            "Fresh halloumi squeaks when you bite it - sign of quality"
        ],
        "tags": ["cheese", "cypriot", "traditional", "grilling", "non-melting", "mediterranean"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-anari-cypriot-whey-ricotta",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Anari (Cypriot Whey Cheese)",
        "category": "mains",
        "attribution": "Ancient Cypriot tradition",
        "source_note": "Traditional Cypriot whey cheesemaking",
        "description": "Made from the whey leftover from halloumi production, Anari is Cyprus's ricotta-style cheese. Fresh and creamy, it's been made alongside halloumi for centuries - nothing wasted in traditional cheesemaking.",
        "servings_yield": "8-12 oz cheese",
        "prep_time": "10 minutes",
        "cook_time": "30-45 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "fresh halloumi whey", "quantity": "1", "unit": "gallon", "prep_note": "still hot from halloumi making"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": "optional, increases yield"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "to taste"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "if curds don't form naturally"}
        ],
        "instructions": [
            {"step": 1, "text": "Use whey immediately after removing halloumi - it should still be very hot."},
            {"step": 2, "text": "If whey has cooled, heat to 185-200°F (85-93°C)."},
            {"step": 3, "text": "If desired, add small amount of fresh milk to increase yield and richness."},
            {"step": 4, "text": "Stir gently and watch for small white curds rising to surface."},
            {"step": 5, "text": "If curds don't appear naturally, add lemon juice and stir gently."},
            {"step": 6, "text": "Let curds accumulate on surface - don't stir once they start forming."},
            {"step": 7, "text": "When no more curds rise (10-15 minutes), remove from heat."},
            {"step": 8, "text": "Skim curds gently with slotted spoon into colander lined with cloth."},
            {"step": 9, "text": "Let drain 1-2 hours until desired consistency."},
            {"step": 10, "text": "Salt to taste while still warm."},
            {"step": 11, "text": "Fresh anari: soft, spreadable. Dried anari: salted and sun-dried for grating."}
        ],
        "temperature": "185-200°F (85-93°C)",
        "notes": [
            "Anari means 'without whey' - what remains after whey is exhausted",
            "Fresh anari is mild and creamy - traditional Cypriot breakfast",
            "Dried anari is salted, dried, and used for grating like aged ricotta",
            "Must be very fresh - consume within 2-3 days",
            "Traditional partner to halloumi - always made together"
        ],
        "tags": ["cheese", "cypriot", "traditional", "whey", "fresh", "ricotta-style"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-akkawi-levantine-brine",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Akkawi (Levantine Brine Cheese)",
        "category": "mains",
        "attribution": "Ancient Levantine tradition from Acre",
        "source_note": "Traditional Middle Eastern cheesemaking",
        "description": "Named for the ancient port city of Acre (Akko) in present-day Israel, Akkawi is a mild white brine cheese beloved throughout the Levant. Its ability to absorb flavors makes it perfect for desserts like knafeh, where it's soaked to remove salt.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "1-2 days brining",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "or sheep's milk"},
            {"item": "mesophilic starter", "quantity": "1/8", "unit": "tsp", "prep_note": "optional - traditional uses no starter"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add starter if using - or proceed directly with rennet (traditional)."},
            {"step": 3, "text": "Add diluted rennet, stir gently, let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Let curds rest 10 minutes, then stir gently."},
            {"step": 6, "text": "Drain whey and transfer curds to cloth-lined mold."},
            {"step": 7, "text": "Press lightly for 2-4 hours."},
            {"step": 8, "text": "Prepare brine: dissolve 1 cup salt in 1 quart water."},
            {"step": 9, "text": "Cut pressed cheese into blocks."},
            {"step": 10, "text": "Submerge in brine - cheese will absorb salt over 24-48 hours."},
            {"step": 11, "text": "Store in brine refrigerated for weeks."},
            {"step": 12, "text": "For knafeh: soak in fresh water 12-24 hours to desalt before using."}
        ],
        "temperature": "95°F (35°C) for make; store in brine refrigerated",
        "notes": [
            "Very mild, almost sweet flavor when desalted",
            "Essential for Middle Eastern dessert knafeh",
            "Also called 'Akawi' or 'Ackawi'",
            "Texture is smooth and sliceable, not crumbly",
            "Traditional table cheese throughout Lebanon, Syria, Palestine, Jordan"
        ],
        "tags": ["cheese", "levantine", "middle-eastern", "traditional", "brine", "dessert"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-nabulsi-palestinian-boiled",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Nabulsi (Palestinian Boiled White Cheese)",
        "category": "mains",
        "attribution": "Ancient Nablus tradition",
        "source_note": "Traditional Palestinian cheesemaking",
        "description": "Named for the West Bank city of Nablus, this ancient cheese is unique for being boiled in brine after forming - giving it a distinctive firm yet springy texture. Flavored with mahleb and mastic, it's essential to Palestinian cuisine.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "goat milk also traditional"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "1", "unit": "cup", "prep_note": "for boiling brine"},
            {"item": "water", "quantity": "2", "unit": "quarts", "prep_note": "for brine"},
            {"item": "mahleb", "quantity": "1/2", "unit": "tsp", "prep_note": "ground cherry pit spice"},
            {"item": "mastic", "quantity": "1/4", "unit": "tsp", "prep_note": "tree resin, ground"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet without starter (traditional method)."},
            {"step": 3, "text": "Let set 45-60 minutes until very firm."},
            {"step": 4, "text": "Cut curds into large pieces."},
            {"step": 5, "text": "Let curds rest, then drain whey."},
            {"step": 6, "text": "Pack curds into molds, press lightly for 1-2 hours."},
            {"step": 7, "text": "Cut pressed cheese into rectangular blocks."},
            {"step": 8, "text": "Prepare brine: dissolve salt in water, add mahleb and mastic."},
            {"step": 9, "text": "Bring spiced brine to boil."},
            {"step": 10, "text": "Add cheese blocks to boiling brine."},
            {"step": 11, "text": "Boil for 30-45 minutes - cheese will become firm and springy."},
            {"step": 12, "text": "Remove and cool. Store in brine. For eating, soak to desalt."}
        ],
        "temperature": "95°F (35°C) for curd; boiling for brine cooking",
        "notes": [
            "Boiling in brine gives unique firm yet elastic texture",
            "Mahleb and mastic give distinctive Middle Eastern flavor",
            "Can be stored in its brine for months",
            "Desalt by soaking in fresh water before eating",
            "Traditional in knafeh nabulsieh - the famous Nablus dessert"
        ],
        "tags": ["cheese", "palestinian", "traditional", "ancient", "boiled", "spiced"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-jibneh-arabieh-gulf-white",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jibneh Arabieh (Gulf Arab White Cheese)",
        "category": "mains",
        "attribution": "Arabian Peninsula tradition",
        "source_note": "Traditional Gulf Arab cheesemaking",
        "description": "The traditional white cheese of the Arabian Gulf states, Jibneh Arabieh is mild, soft, and stored in brine. Made from sheep, goat, or cow milk, it's a staple of Gulf breakfast tables, served with dates and Arabic coffee.",
        "servings_yield": "1.5 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "2-3 hours",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "sheep, goat, or cow"},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "salt", "quantity": "3/4", "unit": "cup", "prep_note": "for brine"},
            {"item": "water", "quantity": "1", "unit": "quart", "prep_note": "for brine"},
            {"item": "nigella seeds", "quantity": "1", "unit": "tbsp", "prep_note": "black seed - traditional addition"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet directly - no starter culture traditionally used."},
            {"step": 3, "text": "Let set 40-50 minutes until firm."},
            {"step": 4, "text": "Cut curds gently into 1-inch pieces."},
            {"step": 5, "text": "Let rest 10 minutes, then stir gently."},
            {"step": 6, "text": "Drain whey through cloth."},
            {"step": 7, "text": "Mix nigella seeds into curds if using."},
            {"step": 8, "text": "Pack curds into molds, press lightly for 2-3 hours."},
            {"step": 9, "text": "Prepare brine: dissolve salt in water (6-8% solution)."},
            {"step": 10, "text": "Cut cheese into blocks and submerge in brine."},
            {"step": 11, "text": "Refrigerate in brine - ready after 24 hours, keeps for weeks."}
        ],
        "temperature": "95°F (35°C) for curd; store in brine refrigerated",
        "notes": [
            "Jibneh means 'cheese' in Arabic, Arabieh means 'Arabic'",
            "Nigella seeds (habba sawda/black seed) are traditional in Gulf cuisine",
            "Mild, fresh flavor - not aged",
            "Often served at breakfast with dates and fresh bread",
            "Each Gulf country has slight variations"
        ],
        "tags": ["cheese", "arab", "gulf", "traditional", "brine", "white", "fresh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-labneh-strained-yogurt-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Labneh (Strained Yogurt Cheese)",
        "category": "mains",
        "attribution": "Ancient Levantine tradition",
        "source_note": "Traditional Middle Eastern strained yogurt",
        "description": "The simplest of cheeses, labneh is yogurt strained until thick and creamy - a technique used throughout the Middle East for millennia. Ranging from spreadable to firm balls preserved in oil, it's fundamental to Levantine cuisine.",
        "servings_yield": "1-2 cups labneh",
        "prep_time": "5 minutes",
        "cook_time": "N/A",
        "total_time": "12-48 hours straining",
        "ingredients": [
            {"item": "full-fat yogurt", "quantity": "1", "unit": "quart", "prep_note": "whole milk, plain, no additives"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "", "unit": "", "prep_note": "for serving or preserving"},
            {"item": "za'atar", "quantity": "", "unit": "", "prep_note": "optional, for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt into yogurt."},
            {"step": 2, "text": "Line colander or strainer with cheesecloth or clean cotton cloth."},
            {"step": 3, "text": "Pour yogurt into lined strainer."},
            {"step": 4, "text": "Place over bowl to catch whey."},
            {"step": 5, "text": "Cover and refrigerate."},
            {"step": 6, "text": "FOR SPREADABLE: Strain 12-24 hours until thick cream cheese consistency."},
            {"step": 7, "text": "FOR FIRM: Strain 24-48 hours, weighting the top, until very thick."},
            {"step": 8, "text": "FOR LABNEH BALLS: Roll extra-thick labneh into balls, store in olive oil."},
            {"step": 9, "text": "Transfer to container. Drizzle with olive oil, sprinkle with za'atar to serve."},
            {"step": 10, "text": "Refrigerate up to 2 weeks; balls in oil keep for months."}
        ],
        "temperature": "Refrigerated throughout",
        "notes": [
            "The longer you strain, the thicker the labneh",
            "Save the whey - it's full of protein and probiotics",
            "Traditional breakfast: labneh, olive oil, za'atar, and fresh bread",
            "Labneh balls in olive oil are a traditional preservation method",
            "Can season with herbs, garlic, or spices"
        ],
        "tags": ["cheese", "middle-eastern", "levantine", "traditional", "yogurt", "simple", "fresh"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-mascarpone-italian-cream",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mascarpone (Italian Cream Cheese)",
        "category": "mains",
        "attribution": "12th century Lombard tradition",
        "source_note": "Traditional Italian acid-set cream cheese",
        "description": "Mascarpone is not technically cheese but acid-coagulated cream - Italy's luxuriously rich answer to cream cheese. Originating in Lombardy around the 12th century, it's essential for tiramisu and countless Italian desserts.",
        "servings_yield": "1 lb mascarpone",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "total_time": "8-24 hours draining",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "quart", "prep_note": "not ultra-pasteurized if possible"},
            {"item": "tartaric acid", "quantity": "1/4", "unit": "tsp", "prep_note": "or 1 tbsp lemon juice"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour cream into heavy-bottomed pot or double boiler."},
            {"step": 2, "text": "Heat cream slowly to 185°F (85°C), stirring occasionally."},
            {"step": 3, "text": "Do not let cream boil."},
            {"step": 4, "text": "Remove from heat."},
            {"step": 5, "text": "Add tartaric acid (or lemon juice) and stir gently."},
            {"step": 6, "text": "Let sit 10 minutes - cream will thicken noticeably."},
            {"step": 7, "text": "Line colander with butter muslin or tight-weave cheesecloth."},
            {"step": 8, "text": "Pour thickened cream into lined colander."},
            {"step": 9, "text": "Cover and refrigerate."},
            {"step": 10, "text": "Let drain 8-24 hours until desired thickness."},
            {"step": 11, "text": "Transfer to container, refrigerate. Use within 1-2 weeks."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Use the freshest cream you can find - ultra-pasteurized doesn't set as well",
            "Tartaric acid (cream of tartar) is traditional; lemon juice works but may add flavor",
            "Consistency should be thick but spreadable, like very dense whipped cream",
            "Essential for tiramisu, cheesecake, and Italian cream sauces",
            "Can be sweetened for desserts or left plain for savory uses"
        ],
        "tags": ["cheese", "italian", "traditional", "cream", "dessert", "simple"],
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
