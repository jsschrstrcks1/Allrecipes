#!/usr/bin/env python3
"""Add batch 64 - Ancient African and Pre-Columbian American cheeses."""

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
        "attribution": "Ancient Ethiopian tradition",
        "source_note": "Modernized from traditional Ethiopian methods, adapted for home cheesemaking",
        "description": "Ethiopia's traditional fresh cheese, ayib is made from the buttermilk left after churning butter. Mild and crumbly, it's the cooling counterpart to spicy Ethiopian dishes, served alongside injera and wots. This ancient dairy tradition has been passed down for millennia in the Ethiopian highlands.",
        "servings_yield": "About 2 cups ayib",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes plus draining",
        "ingredients": [
            {"item": "buttermilk", "quantity": "1/2", "unit": "gallon", "prep_note": "cultured or from butter-making"},
            {"item": "whole milk", "quantity": "2", "unit": "cups", "prep_note": "optional, for richer version"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "or to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "If making from butter-churning, use the buttermilk directly. Otherwise, use cultured buttermilk."},
            {"step": 2, "text": "Pour buttermilk (and milk if using) into pot. Heat slowly over medium-low heat."},
            {"step": 3, "text": "Stir occasionally as the mixture heats. Curds will begin forming around 160°F (71°C)."},
            {"step": 4, "text": "Continue heating until curds fully separate from whey, about 180°F (82°C). Do not boil."},
            {"step": 5, "text": "Remove from heat. Let sit 10 minutes for curds to consolidate."},
            {"step": 6, "text": "Line colander with fine cheesecloth. Pour in mixture and let drain."},
            {"step": 7, "text": "Let drain 30 minutes to 2 hours depending on desired consistency."},
            {"step": 8, "text": "Transfer to bowl, break up curds with fork. Season with salt."},
            {"step": 9, "text": "Serve alongside spicy Ethiopian stews (wots) to cool the palate."},
            {"step": 10, "text": "Store refrigerated up to 1 week. Best eaten fresh within 3 days."}
        ],
        "temperature": "Heat to 180°F (82°C)",
        "notes": [
            "Traditional ayib uses buttermilk from making niter kibbeh (spiced clarified butter)",
            "The mild, cooling flavor balances Ethiopia's spicy cuisine",
            "Often mixed with collard greens (gomen) for the dish gomen be ayib",
            "Ethiopian Orthodox fasting rules prohibit dairy, so ayib is celebratory food",
            "Similar to cottage cheese or quark in texture"
        ],
        "tags": ["cheese", "cheesemaking", "ethiopian", "african", "fresh-cheese", "ancient", "buttermilk-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-wagashi-west-african",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Wagashi (West African Fried Cheese)",
        "category": "mains",
        "attribution": "Fulani herding tradition, West Africa",
        "source_note": "Modernized from traditional Fulani methods, adapted for home cheesemaking",
        "description": "Made by the Fulani people who have herded cattle across West Africa for centuries, wagashi (also called wara in Nigeria) is one of Africa's few traditional cheeses. Fresh curds are shaped and fried until golden, then sold in markets from Benin to Nigeria. The Soumbala leaf used for coagulation gives it a distinctive flavor.",
        "servings_yield": "About 8 cheese patties",
        "prep_time": "1 hour",
        "cook_time": "30 minutes",
        "total_time": "1.5 hours",
        "ingredients": [
            {"item": "whole cow milk", "quantity": "1/2", "unit": "gallon", "prep_note": "fresh and full-fat"},
            {"item": "lemon juice", "quantity": "1/4", "unit": "cup", "prep_note": "or papaya juice (traditional)"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "vegetable oil", "quantity": "1/2", "unit": "cup", "prep_note": "for frying"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185°F (85°C) over medium heat, stirring occasionally."},
            {"step": 2, "text": "Traditional coagulant: In West Africa, Soumbala (Calotropis) leaves or papaya leaf juice is used. Lemon juice is an accessible substitute."},
            {"step": 3, "text": "Remove from heat and add lemon juice gradually while stirring. Curds will form and separate from whey."},
            {"step": 4, "text": "Let sit 15 minutes. The curds should be well-formed."},
            {"step": 5, "text": "Drain through cloth-lined colander. Let drip for 20 minutes."},
            {"step": 6, "text": "Salt the curds and knead briefly. Divide into 8 portions."},
            {"step": 7, "text": "Shape each portion into a small patty or disc about 1/2 inch thick."},
            {"step": 8, "text": "Heat oil in pan over medium-high heat. Fry patties until golden brown, 2-3 minutes per side."},
            {"step": 9, "text": "Drain on paper and serve warm. Traditional accompaniments include hot pepper sauce."},
            {"step": 10, "text": "Best eaten same day. Can also be stored in water and refried."}
        ],
        "temperature": "185°F (85°C) for milk",
        "notes": [
            "The Fulani are traditionally nomadic cattle herders across the Sahel",
            "Wagashi is sold by Fulani women in markets from Benin to Nigeria to Cameroon",
            "Traditional coagulants include Soumbala (Calotropis procera) and papaya",
            "Sometimes the cheese is colored with local vegetables",
            "Similar to paneer but always fried before eating"
        ],
        "tags": ["cheese", "cheesemaking", "african", "west-african", "fulani", "nigerian", "fried-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-klila-north-african",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Klila (North African Dried Buttermilk Cheese)",
        "category": "mains",
        "attribution": "Berber/North African tradition",
        "source_note": "Modernized from traditional Berber/Maghreb methods, adapted for home cheesemaking",
        "description": "A traditional Berber cheese from across the Maghreb, klila is made from dried buttermilk curds. After churning butter from fermented milk, the remaining buttermilk is heated, drained, and dried in the sun. The hard nuggets keep for months and are reconstituted in water for cooking.",
        "servings_yield": "About 1 cup dried klila",
        "prep_time": "45 minutes",
        "cook_time": "1 hour",
        "total_time": "2 hours plus days of drying",
        "ingredients": [
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "gallon", "prep_note": "or lben (fermented milk)"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Traditional method starts with lben (fermented milk) after butter is churned out."},
            {"step": 2, "text": "Pour buttermilk into pot. Heat slowly over medium-low heat, stirring occasionally."},
            {"step": 3, "text": "As temperature rises, curds will form and separate from the thin whey."},
            {"step": 4, "text": "Continue heating to about 180°F (82°C). Curds should be clearly separated."},
            {"step": 5, "text": "Pour through cheesecloth-lined colander. Let drain thoroughly, at least 1 hour."},
            {"step": 6, "text": "Gather cloth and squeeze to remove as much moisture as possible."},
            {"step": 7, "text": "Break the pressed curds into small nuggets or balls. Salt if desired."},
            {"step": 8, "text": "Spread on clean cloth in direct sun. In North Africa, hot sun dries them in 2-3 days."},
            {"step": 9, "text": "In less sunny climates, use dehydrator at 115°F (46°C) for 24-48 hours."},
            {"step": 10, "text": "Store dry klila in cloth bags for months. Rehydrate in water or milk for couscous dishes."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Klila is traditional across Morocco, Algeria, and Tunisia",
            "The dried nuggets are added to couscous, tajines, and soups",
            "Berber nomads made klila for long desert journeys",
            "Sometimes formed into large balls and smoked for preservation",
            "The tangy flavor mellows when rehydrated in cooking"
        ],
        "tags": ["cheese", "cheesemaking", "north-african", "berber", "moroccan", "algerian", "dried-cheese", "ancient", "preservation"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-jameed-jordanian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jameed (Jordanian Dried Yogurt Cheese)",
        "category": "mains",
        "attribution": "Bedouin/Jordanian tradition",
        "source_note": "Modernized from traditional Jordanian Bedouin methods, adapted for home cheesemaking",
        "description": "The essential ingredient in Jordan's national dish mansaf, jameed is rock-hard dried yogurt made from sheep or goat milk. Bedouin herders developed this preservation method to store precious dairy for lean seasons. When reconstituted, it becomes the tangy sauce that defines mansaf.",
        "servings_yield": "About 8-10 jameed balls",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours active plus 1-2 weeks drying",
        "ingredients": [
            {"item": "goat or sheep milk yogurt", "quantity": "2", "unit": "quarts", "prep_note": "full-fat"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cheesecloth", "quantity": "1", "unit": "yard", "prep_note": "for draining"}
        ],
        "instructions": [
            {"step": 1, "text": "Place yogurt in cheesecloth-lined colander. Gather edges and hang over bowl."},
            {"step": 2, "text": "Drain for 24-48 hours until very thick, like cream cheese consistency."},
            {"step": 3, "text": "Transfer drained yogurt to pot. Add salt and cook over low heat, stirring constantly."},
            {"step": 4, "text": "Cook for 1-2 hours until mixture is thick and pulls away from sides of pot."},
            {"step": 5, "text": "The mixture should be very thick and almost paste-like when ready."},
            {"step": 6, "text": "While still warm, form into balls about 2-3 inches in diameter."},
            {"step": 7, "text": "Place balls on a drying rack in hot, dry location. Turn daily."},
            {"step": 8, "text": "Dry for 1-2 weeks until completely rock-hard. They should be very hard and light in weight."},
            {"step": 9, "text": "Store in cool, dry place for months or years."},
            {"step": 10, "text": "To use for mansaf: soak overnight in water, then blend until smooth to make the sauce."}
        ],
        "temperature": "Low cooking heat, ambient drying",
        "notes": [
            "Traditional jameed is made from sheep or goat milk, never cow",
            "The hard balls can be stored for years without refrigeration",
            "Jameed from Karak region is considered the finest in Jordan",
            "The reconstituted sauce has a distinctive tangy, fermented flavor",
            "Mansaf (lamb in jameed sauce over rice) is Jordan's national dish"
        ],
        "tags": ["cheese", "cheesemaking", "jordanian", "bedouin", "middle-eastern", "dried-cheese", "yogurt-cheese", "ancient", "preservation"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-qarish-egyptian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Qarish (Egyptian Skimmed Milk Cheese)",
        "category": "mains",
        "attribution": "Ancient Egyptian tradition",
        "source_note": "Modernized from traditional Egyptian village methods, adapted for home cheesemaking",
        "description": "One of Egypt's most ancient cheeses, qarish is made from skimmed sour milk in the Egyptian countryside. After cream is skimmed for butter, the remaining milk is left to naturally sour, then heated to form curds. The resulting low-fat cheese is tangy and crumbly.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "15 minutes active",
        "cook_time": "30 minutes",
        "total_time": "45 minutes plus 24-48 hours souring",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or whole milk with cream skimmed off"},
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine skim milk with buttermilk in a jar or crock. Cover loosely."},
            {"step": 2, "text": "Leave at room temperature for 24-48 hours until naturally thickened and soured."},
            {"step": 3, "text": "The milk should be thick like yogurt and smell pleasantly tangy."},
            {"step": 4, "text": "Pour soured milk into pot. Heat gently over low-medium heat."},
            {"step": 5, "text": "Stir occasionally as curds begin to form and separate from whey."},
            {"step": 6, "text": "Heat to about 175°F (80°C). Curds should be clearly separated."},
            {"step": 7, "text": "Pour through cheesecloth-lined colander. Let drain 30 minutes."},
            {"step": 8, "text": "Gather cloth and squeeze gently. Salt the curds to taste."},
            {"step": 9, "text": "Press lightly in mold or shape by hand. Refrigerate."},
            {"step": 10, "text": "Eat fresh within a week. Traditional accompaniments are bread and honey."}
        ],
        "temperature": "175°F (80°C)",
        "notes": [
            "Qarish is the poor farmer's cheese - made from leftover skimmed milk",
            "The low fat content makes it very tangy and crumbly",
            "Can be dried further into a harder aged version",
            "Often eaten at breakfast with bread, honey, and mint",
            "The souring process uses natural milk bacteria - no added acid"
        ],
        "tags": ["cheese", "cheesemaking", "egyptian", "ancient", "fresh-cheese", "low-fat", "soured-milk"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queso-blanco-ancient-style",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Blanco (Central American White Cheese)",
        "category": "mains",
        "attribution": "Central American tradition (post-Columbian)",
        "source_note": "Modernized from traditional Central American methods, adapted for home cheesemaking",
        "description": "While cattle came to the Americas with Spanish colonizers, queso blanco quickly became embedded in Central American cuisine. This simple acid-set cheese is essential in pupusas, baleadas, and countless other dishes. The technique likely blended Spanish cheesemaking with indigenous cooking traditions.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "30 minutes",
        "total_time": "50 minutes plus draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "full-fat"},
            {"item": "white vinegar or lime juice", "quantity": "1/4", "unit": "cup", "prep_note": "lime is traditional"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in a large pot over medium heat to 180°F (82°C), stirring occasionally."},
            {"step": 2, "text": "Remove from heat. Add lime juice or vinegar slowly while stirring gently."},
            {"step": 3, "text": "Curds will form immediately. Let sit 10 minutes."},
            {"step": 4, "text": "Line colander with cheesecloth. Pour in curds and whey."},
            {"step": 5, "text": "Let drain 15 minutes. Rinse curds briefly with cool water."},
            {"step": 6, "text": "Gather cloth corners and squeeze to remove excess moisture."},
            {"step": 7, "text": "Transfer curds to bowl. Add salt and mix well."},
            {"step": 8, "text": "Pack into mold or shape into a round. Press lightly for 1-2 hours."},
            {"step": 9, "text": "Use immediately for pupusas, enchiladas, or slice for sandwiches."},
            {"step": 10, "text": "Store refrigerated up to 2 weeks. Does not melt - perfect for frying."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Queso blanco does not melt - it softens but holds shape when heated",
            "Essential in Salvadoran pupusas, Honduran baleadas, and Mexican dishes",
            "Lime juice gives a slightly different flavor than vinegar",
            "Can be crumbled fresh or sliced for grilling",
            "The technique is essentially the same as paneer but with Latin American seasoning"
        ],
        "tags": ["cheese", "cheesemaking", "central-american", "mexican", "salvadoran", "queso-blanco", "fresh-cheese", "frying-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queso-oaxaca-stretched",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Oaxaca (Mexican String Cheese)",
        "category": "mains",
        "attribution": "Oaxacan tradition, Mexico (post-Columbian)",
        "source_note": "Modernized from traditional Oaxacan methods, adapted for home cheesemaking",
        "description": "Mexico's beloved string cheese from Oaxaca, made using pasta filata (stretched curd) technique that arrived with Spanish colonizers. The cheese is stretched into long ribbons and wound into balls. It melts beautifully, making it essential for quesadillas and tlayudas.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "1 hour",
        "cook_time": "3-4 hours",
        "total_time": "5 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or 1/4 cup cultured buttermilk"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "non-iodized salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add calcium chloride and stir. Add culture and ripen 45 minutes."},
            {"step": 2, "text": "Add diluted rennet. Stir gently for 30 seconds. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly raise temperature to 100°F (38°C) while stirring gently. Hold 30 minutes."},
            {"step": 5, "text": "Drain whey. Place curds in warm whey at 100°F to acidify 2-4 hours until stretching test passes."},
            {"step": 6, "text": "Test: place small piece in 170°F water. If it stretches smooth without breaking, curds are ready."},
            {"step": 7, "text": "Heat water to 170°F (77°C). Cut curd into strips and submerge."},
            {"step": 8, "text": "Work the curd, stretching and folding until smooth and shiny. Stretch into long ribbons."},
            {"step": 9, "text": "Wind the ribbons into balls while still warm and pliable. Drop into ice water to set shape."},
            {"step": 10, "text": "Salt by rubbing or brief brine. Store refrigerated up to 2 weeks."}
        ],
        "temperature": "90-100°F curd, 170°F stretching",
        "notes": [
            "Queso Oaxaca is Mexico's most popular melting cheese",
            "The technique came from Spain/Italy but was adapted to local tastes",
            "Properly made Oaxaca cheese pulls into long strings when melted",
            "Essential for quesadillas, tlayudas, and stuffed peppers",
            "Called quesillo in Oaxaca; elsewhere in Mexico it's queso Oaxaca"
        ],
        "tags": ["cheese", "cheesemaking", "mexican", "oaxacan", "pasta-filata", "stretched-curd", "string-cheese", "melting-cheese"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-queso-fresco-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Fresco (Mexican Fresh Farmer's Cheese)",
        "category": "mains",
        "attribution": "Mexican tradition (post-Columbian)",
        "source_note": "Modernized from traditional Mexican methods, adapted for home cheesemaking",
        "description": "The essential crumbling cheese of Mexican cuisine, queso fresco is found on everything from tacos to elotes to enchiladas. Fresh, mild, and slightly tangy, it doesn't melt but softens beautifully. Every region of Mexico has its own variation of this versatile cheese.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "1.5 hours plus pressing",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "full-fat"},
            {"item": "white vinegar or lime juice", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "1.5", "unit": "tsp", "prep_note": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk in large pot over medium heat to 180°F (82°C), stirring to prevent scorching."},
            {"step": 2, "text": "Remove from heat. Add vinegar or lime juice while stirring gently. Curds form immediately."},
            {"step": 3, "text": "Let sit 10-15 minutes for curds to fully develop."},
            {"step": 4, "text": "Line colander with cheesecloth. Gently pour in curds and whey."},
            {"step": 5, "text": "Let drain for 15 minutes. Rinse briefly with cool water to remove acid taste."},
            {"step": 6, "text": "Gather cloth and squeeze gently to remove more whey."},
            {"step": 7, "text": "Transfer curds to bowl. Add salt and mix thoroughly."},
            {"step": 8, "text": "Pack into mold. Press with moderate weight for 2-4 hours or overnight for firmer cheese."},
            {"step": 9, "text": "Unmold and use immediately or wrap and refrigerate."},
            {"step": 10, "text": "Crumble over tacos, salads, beans, or elotes. Store refrigerated up to 2 weeks."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Queso fresco means 'fresh cheese' - it's meant to be eaten within days",
            "Does not melt - it softens and becomes creamy when heated",
            "Perfect for sprinkling on hot dishes as it won't puddle",
            "Regional variations include añejo (aged), cotija (salty), and panela (smooth)",
            "Mexican cheese traditions blended Spanish techniques with indigenous foods"
        ],
        "tags": ["cheese", "cheesemaking", "mexican", "queso-fresco", "fresh-cheese", "crumbling-cheese", "taco-cheese"],
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
