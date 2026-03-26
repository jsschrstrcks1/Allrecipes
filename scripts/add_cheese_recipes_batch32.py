#!/usr/bin/env python3
"""Add batch 32 of traditional cheese recipes - Ancient Middle Eastern, African, and Asian cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-shanklish-syrian-aged",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Shanklish (Syrian Aged Cheese Balls)",
        "category": "mains",
        "attribution": "Syria and Lebanon / Ancient Levantine",
        "source_note": "Ancient Levantine preservation method for cheese. The balls are rolled in zaatar and Aleppo pepper, creating a complex aged cheese.",
        "description": "Syrian and Lebanese aged cheese balls coated in thyme and red pepper, developing strong pungent flavors during fermentation.",
        "servings_yield": "About 8 balls (2 oz each)",
        "prep_time": "2 days for base cheese",
        "cook_time": "2-4 weeks aging",
        "total_time": "3-5 weeks",
        "ingredients": [
            {"item": "labneh or strained yogurt", "quantity": "2", "unit": "lbs", "prep_note": "very thick"},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "zaatar", "quantity": "1/2", "unit": "cup", "prep_note": "dried thyme blend"},
            {"item": "Aleppo pepper", "quantity": "1/4", "unit": "cup", "prep_note": "or crushed red pepper"},
            {"item": "olive oil", "quantity": "1", "unit": "cup", "prep_note": "for storing"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix salt into thick labneh or strained yogurt."},
            {"step": 2, "text": "Form into balls about 1.5 inches in diameter."},
            {"step": 3, "text": "Place on a rack and let dry at room temperature for 3-5 days."},
            {"step": 4, "text": "Turn balls daily. They will develop a dry crust and begin to ferment."},
            {"step": 5, "text": "When balls are firm and slightly cracked on surface, mix zaatar and Aleppo pepper."},
            {"step": 6, "text": "Roll each ball thoroughly in the spice mixture."},
            {"step": 7, "text": "Place coated balls in a jar and cover completely with olive oil."},
            {"step": 8, "text": "Age in a cool dark place for 2-4 weeks."},
            {"step": 9, "text": "Cheese develops stronger, more pungent flavor with time."},
            {"step": 10, "text": "Serve crumbled with olive oil, tomatoes, and flatbread."}
        ],
        "temperature": "Room temperature drying and aging",
        "notes": [
            "Shanklish is one of the oldest preserved cheese traditions in the Levant",
            "The fermentation creates a strong blue cheese-like flavor",
            "Traditional versions become quite pungent with extended aging",
            "Can be stored in olive oil for many months"
        ],
        "tags": ["cheese", "traditional", "syrian", "lebanese", "aged", "spiced", "fermented", "levantine", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-jameed-jordanian-dried",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Jameed (Jordanian Dried Yogurt Cheese)",
        "category": "mains",
        "attribution": "Jordan / Bedouin Ancient",
        "source_note": "Essential ingredient in mansaf, Jordan's national dish. Bedouin innovation for preserving dairy through the desert months.",
        "description": "Rock-hard dried fermented yogurt balls from Jordanian Bedouin tradition, reconstituted to make the sauce for mansaf.",
        "servings_yield": "About 6 balls (3 oz each)",
        "prep_time": "1 week churning and straining",
        "cook_time": "2-4 weeks drying",
        "total_time": "3-5 weeks",
        "ingredients": [
            {"item": "sheep or goat yogurt", "quantity": "2", "unit": "quarts", "prep_note": "full fat"},
            {"item": "salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Churn yogurt vigorously to separate butterfat. Remove butter."},
            {"step": 2, "text": "The remaining buttermilk-like liquid is called shaneeneh."},
            {"step": 3, "text": "Heat shaneeneh while stirring until curds separate from whey."},
            {"step": 4, "text": "Strain through cloth to remove most liquid."},
            {"step": 5, "text": "Mix salt thoroughly into the thick curd."},
            {"step": 6, "text": "Form into balls or flatten into discs."},
            {"step": 7, "text": "Place on racks in hot dry location (traditional: on tent roof in desert sun)."},
            {"step": 8, "text": "Turn daily and dry for 2-4 weeks until completely hard as stone."},
            {"step": 9, "text": "Store in dry place. Will keep for years."},
            {"step": 10, "text": "To use: soak in water overnight, then blend with cooking liquid for mansaf sauce."}
        ],
        "temperature": "Hot sun drying (110-130°F)",
        "notes": [
            "Jameed is essential for authentic mansaf, Jordan's celebratory dish",
            "The stone-hard texture allows preservation in desert heat for years",
            "Flavor is intensely sour and tangy when reconstituted",
            "Still made by Bedouin families and sold in Middle Eastern markets"
        ],
        "tags": ["cheese", "traditional", "jordanian", "bedouin", "dried", "preserved", "sheep", "goat", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-kashk-persian-dried",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kashk (Persian Dried Whey)",
        "category": "mains",
        "attribution": "Persia / Ancient",
        "source_note": "Ancient Persian preservation of dairy nutrients. Essential ingredient in many Iranian dishes like kashk-e bademjan.",
        "description": "Persian dried fermented whey product with intensely savory, tangy flavor, used as a seasoning and sauce base.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 days",
        "cook_time": "1-2 weeks drying",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "whey", "quantity": "1", "unit": "gallon", "prep_note": "from cheesemaking or strained yogurt"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Collect fresh whey from cheesemaking or from straining yogurt."},
            {"step": 2, "text": "Let whey ferment at room temperature for 2-3 days until very sour."},
            {"step": 3, "text": "Slowly heat fermented whey while stirring constantly."},
            {"step": 4, "text": "Simmer for several hours, stirring often, until reduced to thick paste."},
            {"step": 5, "text": "Add salt and continue cooking until very thick."},
            {"step": 6, "text": "Pour onto flat surface or form into balls."},
            {"step": 7, "text": "Dry in sun or dehydrator until completely hard."},
            {"step": 8, "text": "Store in dry container. Keeps indefinitely."},
            {"step": 9, "text": "To use: dissolve in warm water to create creamy sauce."}
        ],
        "temperature": "Simmer, then sun dry",
        "notes": [
            "Kashk is one of the oldest dairy preservation methods from Central Asia",
            "The fermentation and drying concentrate intense umami flavors",
            "Essential for kashk-e bademjan (eggplant dip) and ash reshteh (noodle soup)",
            "Related to Turkish tarhana and Mongolian aaruul"
        ],
        "tags": ["cheese", "traditional", "persian", "iranian", "dried", "whey", "fermented", "ancient", "preserved"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-wagashi-west-african",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Wagashi (West African Fresh Cheese)",
        "category": "mains",
        "attribution": "Benin and West Africa / Ancient Fulani",
        "source_note": "Made by Fulani herders across West Africa for centuries. Uses indigenous plant coagulants like Calotropis leaves.",
        "description": "West African fresh cheese made by Fulani herders using traditional plant rennet, with a mild fresh flavor often fried or grilled.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "30 minutes",
        "total_time": "2 hours",
        "ingredients": [
            {"item": "fresh cow milk", "quantity": "1", "unit": "gallon", "prep_note": "Fulani zebu milk traditional"},
            {"item": "Calotropis leaf extract", "quantity": "1/2", "unit": "cup", "prep_note": "or lemon juice as substitute"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare Calotropis coagulant by crushing fresh leaves and soaking in water (or use lemon juice)."},
            {"step": 2, "text": "Heat fresh milk to 95-100°F."},
            {"step": 3, "text": "Add coagulant slowly while stirring."},
            {"step": 4, "text": "Let stand for 30-45 minutes until curds form."},
            {"step": 5, "text": "Cut curds and let rest 10 minutes."},
            {"step": 6, "text": "Gently ladle curds into woven basket molds."},
            {"step": 7, "text": "Press gently and let drain for 1-2 hours."},
            {"step": 8, "text": "Add salt and shape into balls or discs."},
            {"step": 9, "text": "Eat fresh, or fry in palm oil until golden for 'wagashi fried'."},
            {"step": 10, "text": "Traditional wagashi is often smoked for preservation."}
        ],
        "temperature": "95-100°F make",
        "notes": [
            "Wagashi is the primary cheese of West Africa, made by nomadic Fulani herders",
            "Traditional coagulant is sap from Calotropis procera (apple of Sodom plant)",
            "Often sold fried in markets as a protein-rich snack",
            "Also called 'woagashi' or 'wara' depending on region"
        ],
        "tags": ["cheese", "traditional", "african", "west-african", "fulani", "fresh", "fried", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-ayibe-ethiopian-cottage",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Ayibe (Ethiopian Cottage Cheese)",
        "category": "mains",
        "attribution": "Ethiopia / Ancient",
        "source_note": "Essential accompaniment to Ethiopian cuisine. Made from the buttermilk left after churning butter, traditionally from zebu cattle.",
        "description": "Ethiopian crumbly fresh cheese made from churned buttermilk, served as a cooling contrast to spicy dishes on injera.",
        "servings_yield": "About 2 cups",
        "prep_time": "30 minutes",
        "cook_time": "20 minutes",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "buttermilk", "quantity": "1", "unit": "quart", "prep_note": "from churned butter, or cultured buttermilk"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with buttermilk left from churning butter, or use cultured buttermilk."},
            {"step": 2, "text": "Heat buttermilk slowly over medium-low heat, stirring occasionally."},
            {"step": 3, "text": "As temperature rises, curds will begin to form and separate."},
            {"step": 4, "text": "Heat until curds float and whey is clear, about 160-180°F."},
            {"step": 5, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 6, "text": "Strain through cheesecloth or fine mesh."},
            {"step": 7, "text": "Gently squeeze to remove excess whey."},
            {"step": 8, "text": "Crumble into bowl and add salt if desired."},
            {"step": 9, "text": "Serve at room temperature alongside spicy Ethiopian dishes."}
        ],
        "temperature": "160-180°F make",
        "notes": [
            "Ayibe is unseasoned on its own - it absorbs flavors from accompanying dishes",
            "Traditional method uses buttermilk from zebu cattle",
            "The mild cheese provides relief from spicy berbere-seasoned dishes",
            "Often seasoned with mitmita or niter kibbeh when served"
        ],
        "tags": ["cheese", "traditional", "ethiopian", "fresh", "cottage", "buttermilk", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-domiati-egyptian-brined",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Domiati (Egyptian Brined Cheese)",
        "category": "mains",
        "attribution": "Damietta, Egypt / Ancient",
        "source_note": "Named after the city of Damietta. Unique among cheeses for adding salt directly to the milk before curdling.",
        "description": "Egyptian white brined cheese famous for its salt-first method, soft creamy texture, and tangy flavor.",
        "servings_yield": "About 2 lbs",
        "prep_time": "2 hours",
        "cook_time": "24 hours draining",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "whole buffalo or cow milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "salt", "quantity": "1/4", "unit": "cup", "prep_note": "added to milk before curdling"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "brine", "quantity": "1", "unit": "quart", "prep_note": "saturated salt solution for storage"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add salt directly to warm milk and stir to dissolve - this is unique to Domiati."},
            {"step": 3, "text": "Add diluted rennet and stir briefly."},
            {"step": 4, "text": "Let set for 2-3 hours until firm curd forms."},
            {"step": 5, "text": "Cut curds into large 2-inch cubes."},
            {"step": 6, "text": "Gently ladle curds into cloth-lined mold."},
            {"step": 7, "text": "Let drain for 24 hours at room temperature, flipping once."},
            {"step": 8, "text": "Cut into blocks and store in brine."},
            {"step": 9, "text": "Cheese can be eaten fresh or aged in brine for months."},
            {"step": 10, "text": "Aged Domiati develops sharper, more acidic flavor."}
        ],
        "temperature": "95°F make",
        "notes": [
            "Salting the milk rather than the cheese is the defining characteristic",
            "Buffalo milk is traditional and creates creamier cheese",
            "The high salt content allows natural fermentation and preservation",
            "Fresh Domiati is mild; aged can be very strong and tangy"
        ],
        "tags": ["cheese", "traditional", "egyptian", "brined", "fresh", "salt-first", "ancient", "white"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-halloumi-cypriot-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Halloumi (Ancient Cypriot Grilling Cheese)",
        "category": "mains",
        "attribution": "Cyprus / Medieval Byzantine",
        "source_note": "Made in Cyprus since Byzantine times. The original grilling cheese - unique structure allows it to be fried or grilled without melting.",
        "description": "Cypriot semi-hard cheese made from sheep and goat milk with mint, famous for its high melting point that allows grilling.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "2 hours",
        "cook_time": "1-2 weeks aging",
        "total_time": "2 weeks",
        "ingredients": [
            {"item": "sheep milk", "quantity": "1", "unit": "gallon", "prep_note": "or blend with goat milk"},
            {"item": "goat milk", "quantity": "1", "unit": "quart", "prep_note": "optional blend"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "dried mint", "quantity": "2", "unit": "tbsp", "prep_note": "crushed"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F."},
            {"step": 2, "text": "Add diluted rennet and stir briefly."},
            {"step": 3, "text": "Let set for 45-60 minutes until firm curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes."},
            {"step": 5, "text": "Let curds rest 5 minutes, then stir gently."},
            {"step": 6, "text": "Slowly raise temperature to 104°F over 15 minutes."},
            {"step": 7, "text": "Drain curds and press into basket molds at moderate pressure for 1 hour."},
            {"step": 8, "text": "Flip and press 1 more hour."},
            {"step": 9, "text": "Heat whey to 190-195°F. Poach pressed cheese in hot whey for 30-40 minutes."},
            {"step": 10, "text": "Remove cheese when it floats. Fold in half while still pliable."},
            {"step": 11, "text": "Sprinkle with salt and dried mint. Fold mint inside."},
            {"step": 12, "text": "Cool completely. Store in brine or eat fresh."}
        ],
        "temperature": "95-104°F make, 190-195°F poaching",
        "notes": [
            "The whey poaching step is essential - it creates halloumi's grilling properties",
            "Traditional fold traps dried mint inside the cheese",
            "Can be eaten fresh, grilled, fried, or aged in brine",
            "Has PDO protection - true halloumi must be made in Cyprus"
        ],
        "tags": ["cheese", "traditional", "cypriot", "grilling", "sheep", "goat", "byzantine", "medieval", "pdo"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-nor-tunisian-curdled",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Nor (Tunisian/Algerian Curdled Cheese)",
        "category": "mains",
        "attribution": "Tunisia and Algeria / Ancient Berber",
        "source_note": "Ancient Berber cheese tradition from the Maghreb. Made by desert nomads using dried thistle as coagulant.",
        "description": "North African fresh cheese made with vegetable rennet from wild artichoke thistle, with a delicate creamy texture.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "4 hours",
        "ingredients": [
            {"item": "fresh sheep or goat milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "dried wild artichoke thistle", "quantity": "2", "unit": "tbsp", "prep_note": "crushed flowers, or vegetable rennet"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Prepare vegetable rennet by soaking crushed thistle flowers in 1/4 cup warm water for 1 hour."},
            {"step": 2, "text": "Strain the thistle extract."},
            {"step": 3, "text": "Heat milk to 90°F."},
            {"step": 4, "text": "Add thistle extract and stir gently."},
            {"step": 5, "text": "Cover and let stand for 1-2 hours until soft curd forms."},
            {"step": 6, "text": "Vegetable rennet creates a more delicate curd than animal rennet."},
            {"step": 7, "text": "Gently ladle curd into small woven baskets or cheesecloth."},
            {"step": 8, "text": "Let drain for 2-3 hours."},
            {"step": 9, "text": "Salt lightly and serve fresh."},
            {"step": 10, "text": "Best eaten same day as made."}
        ],
        "temperature": "90°F make",
        "notes": [
            "Wild artichoke thistle (Cynara cardunculus) is the traditional coagulant",
            "Berber nomads have made this cheese for thousands of years",
            "The vegetable rennet creates a more delicate, less firm curd",
            "Related to Portuguese queijo de Serra which uses similar thistle"
        ],
        "tags": ["cheese", "traditional", "tunisian", "algerian", "berber", "fresh", "vegetable-rennet", "ancient"],
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
