#!/usr/bin/env python3
"""Add batch 29 of traditional cheese recipes - More ancient and regional cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-kefalograviera-greek",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kefalograviera (Greek)",
        "category": "mains",
        "attribution": "Greece, Traditional",
        "source_note": "Kefalograviera is a Greek cheese that combines characteristics of both Kefalotyri and Graviera. It's a versatile hard cheese excellent for both table use and frying for saganaki.",
        "description": "Greek hard cheese combining the best of Kefalotyri and Graviera - firm, tangy, and perfect for saganaki.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-6 months aging",
        "total_time": "3-6 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": ""},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon", "prep_note": "optional blend"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F. Add calcium chloride if using pasteurized."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 35-45 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Raise temperature to 118°F over 40 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at 118°F for 20 minutes until curds are firm."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 20 lbs for 1 hour. Flip and press at 45 lbs for 24 hours."},
            {"step": 9, "text": "Brine for 24-36 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 55°F and 85% humidity for 3-6 months."}
        ],
        "temperature": "95°F start, 118°F cook, 55°F aging",
        "notes": [
            "Kefalograviera is firmer than Graviera but milder than Kefalotyri",
            "Excellent for saganaki - fry thick slices until golden",
            "Also good as table cheese or grated over pasta",
            "PDO protected in certain Greek regions"
        ],
        "tags": ["cheese", "traditional", "greek", "kefalograviera", "hard-cheese", "sheep-cheese", "saganaki"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-manouri-greek",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Manouri (Greek Whey Cheese)",
        "category": "mains",
        "attribution": "Macedonia/Thessaly, Greece, Ancient",
        "source_note": "Manouri is an ancient Greek whey cheese from Macedonia and Thessaly, richer than mizithra because cream or milk is added. It's been made for centuries and is PDO protected.",
        "description": "Rich Greek whey cheese, creamier than mizithra - an ancient delicacy from Macedonia and Thessaly.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "30 minutes",
        "cook_time": "Fresh or 1 week dried",
        "total_time": "1-2 hours fresh",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from sheep/goat cheese making"},
            {"item": "sheep's milk", "quantity": "2", "unit": "cups", "prep_note": "for enrichment"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for richness"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey, milk, and cream in a large pot."},
            {"step": 2, "text": "Heat slowly to 185-190°F, stirring occasionally."},
            {"step": 3, "text": "Rich white curds will rise to the surface."},
            {"step": 4, "text": "Remove from heat and let rest 15 minutes."},
            {"step": 5, "text": "Gently ladle curds into cloth-lined molds or baskets."},
            {"step": 6, "text": "Let drain for 4-6 hours at room temperature."},
            {"step": 7, "text": "Salt lightly if desired."},
            {"step": 8, "text": "Fresh manouri is ready to eat. Can be aged briefly for firmer texture."}
        ],
        "temperature": "185-190°F",
        "notes": [
            "Manouri is richer than mizithra due to added cream",
            "The texture is smooth and creamy, similar to fresh chevre",
            "Often served drizzled with honey or in savory dishes",
            "PDO protected; traditional to Macedonia and Thessaly"
        ],
        "tags": ["cheese", "traditional", "greek", "macedonian", "manouri", "whey-cheese", "fresh-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-kopanisti-greek",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kopanisti (Greek Spicy Cheese)",
        "category": "mains",
        "attribution": "Cyclades Islands, Greece, Ancient",
        "source_note": "Kopanisti is an ancient, intensely flavored cheese from the Cyclades islands, particularly Mykonos. Made by repeatedly kneading and aging soft cheese, it develops a sharp, spicy, blue-veined character.",
        "description": "Intensely pungent Greek island cheese, kneaded and aged until sharp and spicy - a bold Cycladic specialty.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes initial",
        "cook_time": "1-3 months repeated kneading/aging",
        "total_time": "1-3 months",
        "ingredients": [
            {"item": "fresh soft cheese (mizithra or similar)", "quantity": "1", "unit": "lb", "prep_note": ""},
            {"item": "salt", "quantity": "2", "unit": "tsp", "prep_note": ""},
            {"item": "pepper", "quantity": "1/2", "unit": "tsp", "prep_note": "optional, some versions"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh, soft sheep or goat cheese."},
            {"step": 2, "text": "Mix cheese with salt and knead thoroughly."},
            {"step": 3, "text": "Place in a covered crock and store at cool room temperature (60-65°F)."},
            {"step": 4, "text": "Every 2-3 days, remove the cheese and knead it vigorously again."},
            {"step": 5, "text": "Return to the crock and continue aging."},
            {"step": 6, "text": "Over time, natural molds will develop and the flavor intensifies."},
            {"step": 7, "text": "Continue the kneading process for 1-3 months."},
            {"step": 8, "text": "The finished cheese should be creamy, very sharp, and spicy."}
        ],
        "temperature": "60-65°F aging",
        "notes": [
            "Kopanisti means 'beaten' or 'pounded' - referring to the kneading process",
            "The repeated kneading incorporates wild molds that develop naturally",
            "The flavor is intensely sharp, peppery, and pungent",
            "Often spread on bread or used as a meze with ouzo",
            "PDO protected; specialty of Mykonos and the Cyclades"
        ],
        "tags": ["cheese", "traditional", "greek", "cyclades", "mykonos", "kopanisti", "spicy-cheese", "blue-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tyrosyr-icelandic",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Skyr (Icelandic Cultured Dairy)",
        "category": "mains",
        "attribution": "Iceland, Viking Age (1100+ years)",
        "source_note": "Skyr has been made in Iceland since the Viking settlement over 1100 years ago. Technically a fresh cheese (not yogurt), it's made by culturing skim milk and straining extensively for a thick, protein-rich product.",
        "description": "Ancient Viking-age Icelandic cultured cheese, thick and tangy - brought to Iceland by Norse settlers over 1100 years ago.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "12-24 hours culturing",
        "total_time": "24-36 hours",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": ""},
            {"item": "skyr or Greek yogurt", "quantity": "2", "unit": "tbsp", "prep_note": "as starter"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted in 1 tbsp water"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat skim milk to 185°F to pasteurize. Hold for 5 minutes."},
            {"step": 2, "text": "Cool milk to 110°F."},
            {"step": 3, "text": "Whisk in the skyr or yogurt starter until smooth."},
            {"step": 4, "text": "Add the diluted rennet and stir gently."},
            {"step": 5, "text": "Cover and keep warm (100-110°F) for 12-24 hours until thick and tangy."},
            {"step": 6, "text": "Line a strainer with fine cloth and pour in the cultured milk."},
            {"step": 7, "text": "Drain for 12-24 hours until very thick - thicker than Greek yogurt."},
            {"step": 8, "text": "Whisk until smooth. Traditionally served with cream and sugar."}
        ],
        "temperature": "185°F pasteurizing, 100-110°F culturing",
        "notes": [
            "Skyr is technically a fresh cheese, not yogurt, due to the rennet",
            "Traditional skyr is made from skim milk and is very high in protein",
            "Icelandic tradition: serve with cream drizzled on top and sugar",
            "Vikings brought the technique from Norway; it survived only in Iceland"
        ],
        "tags": ["cheese", "traditional", "icelandic", "viking", "skyr", "fresh-cheese", "cultured", "norse"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pule-serbian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pule (Serbian Donkey Cheese)",
        "category": "mains",
        "attribution": "Zasavica, Serbia, Traditional",
        "source_note": "Pule is made from donkey milk at the Zasavica Special Nature Reserve in Serbia. It's one of the world's rarest and most expensive cheeses because donkeys produce very little milk and it takes 25 liters to make 1 kg of cheese.",
        "description": "Extremely rare Serbian cheese from donkey milk - one of the world's most expensive cheeses due to its scarcity.",
        "servings_yield": "About 8 oz (very small yield)",
        "prep_time": "1 hour",
        "cook_time": "Fresh",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "donkey milk", "quantity": "1", "unit": "gallon", "prep_note": "extremely rare - goat milk can substitute"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp", "prep_note": ""},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat donkey milk very gently to 95°F - donkey milk is delicate."},
            {"step": 2, "text": "Add lemon juice gradually, stirring gently."},
            {"step": 3, "text": "The milk will slowly curdle into very fine, soft curds."},
            {"step": 4, "text": "Let rest for 30 minutes."},
            {"step": 5, "text": "Very gently ladle curds into a fine cloth-lined mold."},
            {"step": 6, "text": "Let drain for several hours - the curds are very delicate."},
            {"step": 7, "text": "Salt lightly and serve fresh."},
            {"step": 8, "text": "Pule must be eaten fresh - it does not age well."}
        ],
        "temperature": "95°F",
        "notes": [
            "Donkey milk has very little casein, making cheese extremely difficult",
            "It takes about 25 liters of donkey milk to make 1 kg of pule",
            "The flavor is mild, slightly sweet, and very delicate",
            "One of the world's most expensive cheeses due to rarity",
            "If donkey milk is unavailable, this method works with goat milk for a similar texture"
        ],
        "tags": ["cheese", "traditional", "serbian", "pule", "donkey-milk", "rare-cheese", "fresh-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-brunost-norwegian-farm",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Farm Brunost (Norwegian Brown Cheese)",
        "category": "mains",
        "attribution": "Norway, 19th Century (farm tradition older)",
        "source_note": "While Gjetost/Brunost was commercialized in the 1860s, Norwegian farmers had been making similar whey-based products for centuries. This farm-style version uses traditional methods with mixed milk whey.",
        "description": "Traditional Norwegian farm-style brown cheese, caramelized whey with a sweet, fudgy character.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "3-4 hours",
        "total_time": "4-5 hours",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from goat or cow cheese making"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": ""},
            {"item": "cream", "quantity": "1/2", "unit": "cup", "prep_note": "for richer brunost"},
            {"item": "brown sugar", "quantity": "2", "unit": "tbsp", "prep_note": "optional, for deeper color"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine whey, milk, and cream in a large, heavy-bottomed pot."},
            {"step": 2, "text": "Bring to a boil over medium-high heat, stirring frequently."},
            {"step": 3, "text": "Reduce heat to maintain a steady boil. Stir regularly to prevent scorching."},
            {"step": 4, "text": "Boil for 2-3 hours as the liquid reduces significantly."},
            {"step": 5, "text": "The mixture will turn tan, then progressively brown as sugars caramelize."},
            {"step": 6, "text": "Add brown sugar in the last 30 minutes if using."},
            {"step": 7, "text": "When very thick and pulling from the sides, remove from heat."},
            {"step": 8, "text": "Beat vigorously for 10-15 minutes until smooth."},
            {"step": 9, "text": "Pour into a buttered mold and cool completely."}
        ],
        "temperature": "Boiling throughout",
        "notes": [
            "The key is patience - slow reduction caramelizes the lactose",
            "Constant stirring in the final stages prevents burning",
            "The vigorous beating prevents a grainy texture",
            "Goat whey produces more traditional gjetost; cow whey makes brunost"
        ],
        "tags": ["cheese", "traditional", "norwegian", "brunost", "farm-cheese", "whey-cheese", "caramelized"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-vieux-boulogne-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Vieux-Boulogne (French Washed-Rind)",
        "category": "mains",
        "attribution": "Boulogne-sur-Mer, France, 1980s (based on older traditions)",
        "source_note": "Vieux-Boulogne was created in the 1980s but based on traditional Pas-de-Calais cheesemaking. Washed with beer, it's been scientifically measured as one of the world's smelliest cheeses.",
        "description": "Legendarily pungent French cheese washed with beer - scientifically proven to be one of the world's smelliest cheeses.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "3 hours",
        "cook_time": "7-9 weeks aging",
        "total_time": "7-9 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "beer", "quantity": "2", "unit": "cups", "prep_note": "local ale or strong beer for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add starter and B. linens, ripen 1 hour."},
            {"step": 2, "text": "Add diluted rennet, stir gently. Let set 1 hour until soft curd."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Stir gently for 30 minutes at 90°F."},
            {"step": 5, "text": "Drain whey and ladle curds into square molds."},
            {"step": 6, "text": "Let drain at room temperature for 24-48 hours, flipping every 6-8 hours."},
            {"step": 7, "text": "Salt all surfaces and let dry for 24 hours."},
            {"step": 8, "text": "Transfer to aging cave at 55°F and 95% humidity."},
            {"step": 9, "text": "Wash with beer every 2-3 days for 7-9 weeks."},
            {"step": 10, "text": "The rind should become sticky, orange-red, and extremely pungent."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "Scientifically tested as one of the world's smelliest cheeses",
            "The beer wash intensifies the pungency",
            "Despite the smell, the flavor is rich and complex, not as strong as the aroma",
            "Best enjoyed with crusty bread and the same beer used for washing"
        ],
        "tags": ["cheese", "traditional", "french", "washed-rind", "vieux-boulogne", "pungent", "beer-washed"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-casu-axedu-sardinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Casu Axedu (Sardinian Sour Cheese)",
        "category": "mains",
        "attribution": "Sardinia, Italy, Ancient",
        "source_note": "Casu Axedu (also called Fiscidu or Casu Agedu) is an ancient Sardinian cheese made by souring milk naturally without rennet. The name means 'sour cheese' in Sardinian. It's one of the simplest and oldest cheese methods.",
        "description": "Ancient Sardinian sour cheese made without rennet - one of the most primitive cheesemaking methods still practiced.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 minutes",
        "cook_time": "24-48 hours souring",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "must be raw for natural souring"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pour fresh raw sheep's milk into a clean container."},
            {"step": 2, "text": "Cover loosely and leave at warm room temperature (70-75°F)."},
            {"step": 3, "text": "Let the milk sour naturally for 24-48 hours until thickened and tangy."},
            {"step": 4, "text": "The natural bacteria in raw milk will curdle it without rennet."},
            {"step": 5, "text": "Once thickened, gently heat to 100-110°F to help curds firm slightly."},
            {"step": 6, "text": "Ladle the soft curds into a cloth-lined strainer."},
            {"step": 7, "text": "Drain for several hours until desired consistency."},
            {"step": 8, "text": "Salt lightly and eat fresh, or age briefly in a cool place."}
        ],
        "temperature": "Room temperature souring, 100-110°F gentle heating",
        "notes": [
            "This is one of the most ancient cheesemaking methods - no rennet required",
            "Must use raw milk - pasteurized milk won't sour properly",
            "The flavor is tangy and acidic, similar to fresh chevre",
            "Can be eaten fresh or aged for a few days for firmer texture"
        ],
        "tags": ["cheese", "traditional", "sardinian", "italian", "casu-axedu", "sour-cheese", "no-rennet", "ancient", "primitive"],
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
