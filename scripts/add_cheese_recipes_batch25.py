#!/usr/bin/env python3
"""Add batch 25 of traditional cheese recipes - Portuguese, Latin American, and miscellaneous traditional."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-queijo-serra-portuguese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queijo da Serra (Portuguese Mountain Cheese)",
        "category": "mains",
        "attribution": "Serra da Estrela, Portugal, 12th Century",
        "source_note": "Queijo da Serra da Estrela is Portugal's most famous cheese, made in the highest mountain range in continental Portugal since at least the 12th century. Uniquely, it uses thistle rennet instead of animal rennet.",
        "description": "Portugal's most prestigious cheese, made with thistle rennet and sheep's milk, with a rich, runny interior when perfectly ripe.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "30-45 days aging",
        "total_time": "30-45 days",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": "from Bordaleira breed traditionally"},
            {"item": "cardoon thistle", "quantity": "1/4", "unit": "cup", "prep_note": "dried flowers, for vegetarian rennet"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare thistle rennet: Steep dried cardoon flowers in 1/2 cup warm water for 2-3 hours or overnight."},
            {"step": 2, "text": "Strain the thistle infusion through fine cloth. This is your rennet."},
            {"step": 3, "text": "Heat sheep's milk to 86-90°F."},
            {"step": 4, "text": "Add thistle rennet (about 1/4 cup per gallon). Stir gently."},
            {"step": 5, "text": "Let set for 1-2 hours until a soft curd forms (thistle rennet works slower than animal rennet)."},
            {"step": 6, "text": "Gently cut curd into large pieces and ladle into cloth-lined molds."},
            {"step": 7, "text": "Let drain at room temperature for 24-48 hours, flipping several times."},
            {"step": 8, "text": "Salt the surface and let dry for 24 hours."},
            {"step": 9, "text": "Age at 50-55°F and 90% humidity for 30-45 days minimum."},
            {"step": 10, "text": "When ripe, the rind should be firm but the interior should be soft and almost runny."}
        ],
        "temperature": "86-90°F make, 50-55°F aging",
        "notes": [
            "Thistle (cardoon) rennet is essential for authentic Serra cheese and makes it vegetarian",
            "When perfectly ripe, cut off the top and eat the creamy interior with a spoon",
            "The texture should be semi-liquid ('amanteigado') when at room temperature",
            "DOP protected; only cheese made in the Serra da Estrela region can use this name"
        ],
        "tags": ["cheese", "traditional", "portuguese", "sheep-cheese", "thistle-rennet", "queijo-da-serra", "12th-century", "vegetarian-rennet"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sao-jorge-azores",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional São Jorge (Azorean)",
        "category": "mains",
        "attribution": "São Jorge Island, Azores, 15th Century",
        "source_note": "São Jorge cheese has been made on the Azorean island of São Jorge since the 15th century, introduced by Flemish settlers. The volcanic island's pastures and oceanic climate create a unique terroir for this hard, sharp cheese.",
        "description": "Sharp, tangy cheese from the Azores, introduced by Flemish settlers and perfected over centuries of island tradition.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-7 months aging",
        "total_time": "3-7 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100°F over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring for 30 minutes at 100°F."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 20 lbs for 2 hours. Flip and press at 40 lbs for 24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours or dry salt over several days."},
            {"step": 10, "text": "Age at 55°F and 85% humidity for 3-7 months, turning weekly."}
        ],
        "temperature": "90°F start, 100°F cook, 55°F aging",
        "notes": [
            "The Azores' volcanic soil and humid climate give São Jorge its distinctive flavor",
            "Young São Jorge (3 months) is semi-hard and tangy",
            "Aged São Jorge (7+ months) is hard, sharp, and excellent for grating",
            "DOP protected; only cheese made on São Jorge island can bear this name"
        ],
        "tags": ["cheese", "traditional", "portuguese", "azorean", "sao-jorge", "hard-cheese", "15th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-chihuahua-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Chihuahua (Mexican Menonita)",
        "category": "mains",
        "attribution": "Chihuahua, Mexico, 1920s (Mennonite Settlement)",
        "source_note": "Queso Chihuahua, also called Queso Menonita, was introduced by German-speaking Mennonite settlers who arrived in Chihuahua, Mexico in the 1920s. Their Dutch/German cheesemaking traditions adapted to Mexican tastes.",
        "description": "Mild, buttery Mexican cheese introduced by Mennonite settlers, now essential for queso fundido and Mexican cuisine.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 102°F over 30 minutes while stirring."},
            {"step": 6, "text": "Remove about 1/3 of whey. Replace with warm water to wash curds (this creates the mild flavor)."},
            {"step": 7, "text": "Continue stirring for 20 minutes at 102°F."},
            {"step": 8, "text": "Drain whey and add salt to curds."},
            {"step": 9, "text": "Transfer to molds. Press at 15 lbs for 30 minutes. Flip and press at 30 lbs for 8-12 hours."},
            {"step": 10, "text": "Air dry for 1-2 days, then wax or vacuum seal."},
            {"step": 11, "text": "Age at 55°F for 2-4 weeks."}
        ],
        "temperature": "86°F start, 102°F cook, 55°F aging",
        "notes": [
            "The curd washing creates the characteristic mild, buttery flavor",
            "Excellent melting cheese for queso fundido and quesadillas",
            "Similar to Gouda in technique due to Mennonite origins",
            "Also sold as 'Queso Menonita' or just 'Chihuahua'"
        ],
        "tags": ["cheese", "traditional", "mexican", "mennonite", "queso-chihuahua", "melting-cheese", "1920s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-oaxaca-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso Oaxaca (String Cheese)",
        "category": "mains",
        "attribution": "Oaxaca, Mexico, 16th Century",
        "source_note": "Queso Oaxaca is a pasta filata cheese developed in Oaxaca, Mexico, combining indigenous cheesemaking traditions with Spanish techniques. It's traditionally formed into long ropes wound into balls.",
        "description": "Mexican string cheese formed into distinctive balls of wound ribbons, essential for quesadillas and melting over Mexican dishes.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "Fresh (no aging)",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1.5", "unit": "gallons", "prep_note": ""},
            {"item": "citric acid", "quantity": "1", "unit": "tsp", "prep_note": "dissolved in 1/4 cup water"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Add citric acid solution to cold milk, stir well. Heat to 90°F."},
            {"step": 2, "text": "Remove from heat, add diluted rennet, stir gently. Let set 15-20 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 105°F while stirring gently."},
            {"step": 5, "text": "Drain curds and let mat at 100°F for 1-2 hours until pH reaches 5.2-5.3."},
            {"step": 6, "text": "Cut matted curd into strips. Heat water to 170°F with salt."},
            {"step": 7, "text": "Stretch curd in hot water until smooth and elastic."},
            {"step": 8, "text": "Pull the stretched curd into long ribbons about 1/2 inch wide."},
            {"step": 9, "text": "Wind the ribbons into a ball, tucking the end underneath."},
            {"step": 10, "text": "Cool in ice water for 15 minutes to set shape."},
            {"step": 11, "text": "Store in light brine or eat fresh within 1 week."}
        ],
        "temperature": "90°F curd, 170°F stretching",
        "notes": [
            "The distinctive ball of wound ribbons is traditional to Oaxaca",
            "Pull apart the ribbons ('strings') for eating or melting",
            "Similar to mozzarella in technique but formed differently",
            "Essential for authentic quesadillas and tlayudas"
        ],
        "tags": ["cheese", "traditional", "mexican", "oaxacan", "pasta-filata", "queso-oaxaca", "string-cheese", "fresh-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cotija-mexican",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cotija (Mexican Aged Cheese)",
        "category": "mains",
        "attribution": "Cotija, Michoacán, Mexico, Pre-Hispanic (evolved)",
        "source_note": "Cotija is named after the town of Cotija de la Paz in Michoacán. While Mexican cheesemaking evolved after Spanish contact, Cotija developed into a distinctly Mexican aged cheese, essential for finishing tacos, elotes, and many Mexican dishes.",
        "description": "Salty, crumbly Mexican aged cheese named for a Michoacán town - the 'Mexican Parmesan' essential for finishing dishes.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp", "prep_note": "Cotija is heavily salted"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Raise temperature to 100°F over 20 minutes while stirring."},
            {"step": 6, "text": "Continue stirring for 30 minutes at 100°F until curds are firm."},
            {"step": 7, "text": "Drain whey. Add salt (more than most cheeses - Cotija is salty)."},
            {"step": 8, "text": "Transfer to cylindrical molds. Press at 20 lbs for 2 hours."},
            {"step": 9, "text": "Flip and press at 40 lbs for 24 hours."},
            {"step": 10, "text": "Air dry for 3-5 days until surface is dry."},
            {"step": 11, "text": "Age at 55°F and 80% humidity for 3-12 months. Turn weekly."}
        ],
        "temperature": "90°F start, 100°F cook, 55°F aging",
        "notes": [
            "Cotija is saltier than most cheeses - this aids preservation in hot climates",
            "Young Cotija (3 months) is crumbly like feta",
            "Aged Cotija (añejo, 12+ months) is hard and grateable like Parmesan",
            "Essential for elotes (Mexican street corn), enchiladas, and tacos"
        ],
        "tags": ["cheese", "traditional", "mexican", "cotija", "aged-cheese", "crumbly-cheese", "michoacan"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-de-mano-venezuelan",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Queso de Mano (Venezuelan)",
        "category": "mains",
        "attribution": "Llanos Region, Venezuela, Colonial Era",
        "source_note": "Queso de Mano ('hand cheese') has been made in the Venezuelan llanos (plains) since colonial times. Named for the hand-kneading process that gives it its smooth, elastic texture, it's essential for Venezuelan cuisine.",
        "description": "Venezuelan stretched-curd cheese kneaded by hand, with a smooth, elastic texture essential for arepas and cachapas.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "Fresh",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1.5", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F."},
            {"step": 2, "text": "Add starter culture, stir, and ripen for 20 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100°F while stirring."},
            {"step": 6, "text": "Drain curds and let mat at warm room temperature for 2-3 hours."},
            {"step": 7, "text": "Test for stretch in hot water (170°F). When ready, curds will stretch smoothly."},
            {"step": 8, "text": "Knead the curd by hand (hence 'de mano') in hot water until smooth and elastic."},
            {"step": 9, "text": "Work in salt while kneading."},
            {"step": 10, "text": "Form into flat rounds or balls."},
            {"step": 11, "text": "Store in light brine or use fresh within 1 week."}
        ],
        "temperature": "90°F curd, 170°F stretching",
        "notes": [
            "The hand-kneading gives Queso de Mano its characteristic smooth texture",
            "Similar to mozzarella but with a firmer, denser texture",
            "Essential for Venezuelan arepas and cachapas (corn pancakes)",
            "Best eaten fresh when still warm and stretchy"
        ],
        "tags": ["cheese", "traditional", "venezuelan", "pasta-filata", "queso-de-mano", "fresh-cheese", "llanos"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cuajada-latin-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cuajada (Latin American Fresh Curd)",
        "category": "mains",
        "attribution": "Latin America/Spain, Ancient",
        "source_note": "Cuajada (from 'cuajar,' to curdle) is one of the simplest and most ancient fresh cheeses, made throughout Latin America and Spain. It's essentially fresh curds, eaten immediately with honey or sugar.",
        "description": "Simple Latin American fresh curd cheese, often eaten as dessert with honey - the most basic form of cheese, enjoyed for millennia.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "45 minutes",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "goat, sheep, or cow"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops", "prep_note": "diluted in 1 tbsp water"},
            {"item": "honey", "quantity": "as needed", "unit": "", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (barely warm)."},
            {"step": 2, "text": "Add diluted rennet and stir gently for 30 seconds."},
            {"step": 3, "text": "Let sit undisturbed for 30-45 minutes until set like a soft junket."},
            {"step": 4, "text": "The curd should be very soft and delicate, barely holding its shape."},
            {"step": 5, "text": "Carefully spoon the soft curd into serving bowls."},
            {"step": 6, "text": "Drizzle with honey, sprinkle with cinnamon, or add sugar to taste."},
            {"step": 7, "text": "Serve immediately while still warm."}
        ],
        "temperature": "95°F",
        "notes": [
            "Cuajada is meant to be eaten immediately - it's not a cheese to store",
            "The texture should be like a soft custard or junket",
            "Traditional Spanish cuajada uses sheep's milk",
            "In Latin America, often eaten as a simple breakfast or dessert",
            "This is cheese in its most elemental form"
        ],
        "tags": ["cheese", "traditional", "latin-american", "spanish", "fresh-cheese", "cuajada", "dessert", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-requeson-latin-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Requesón (Latin American Ricotta)",
        "category": "mains",
        "attribution": "Spain/Latin America, Ancient",
        "source_note": "Requesón is the Spanish and Latin American equivalent of ricotta, made from the whey left over from other cheesemaking. The name means 're-curdled,' similar to ricotta meaning 're-cooked.'",
        "description": "Latin American whey cheese, the Spanish cousin of ricotta - light, fresh, and essential for both sweet and savory dishes.",
        "servings_yield": "About 1 cup",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour including draining",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from cheese making"},
            {"item": "whole milk", "quantity": "1/2", "unit": "cup", "prep_note": "optional, for better yield"},
            {"item": "lemon juice or vinegar", "quantity": "2", "unit": "tbsp", "prep_note": "if needed"},
            {"item": "salt", "quantity": "pinch", "unit": "", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh whey from cheese making (rennet-set whey works best)."},
            {"step": 2, "text": "Add milk if using. Heat slowly over medium heat."},
            {"step": 3, "text": "As temperature approaches 185-195°F, white curds will begin to rise."},
            {"step": 4, "text": "If curds don't form, add lemon juice one tablespoon at a time."},
            {"step": 5, "text": "When curds are floating on top, remove from heat. Let rest 10 minutes."},
            {"step": 6, "text": "Gently skim the curds with a slotted spoon into a fine strainer."},
            {"step": 7, "text": "Let drain for 15-30 minutes."},
            {"step": 8, "text": "Add salt if desired. Use immediately or refrigerate up to 5 days."}
        ],
        "temperature": "185-195°F",
        "notes": [
            "The fresher the whey, the better the requesón",
            "Acid-set cheese whey doesn't work as well as rennet-set whey",
            "Used in Mexican enchiladas, with honey as dessert, or in pastries",
            "Very light and low in fat since most fat stays in the original cheese"
        ],
        "tags": ["cheese", "traditional", "latin-american", "spanish", "whey-cheese", "requeson", "fresh-cheese", "ancient"],
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
