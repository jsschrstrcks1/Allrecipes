#!/usr/bin/env python3
"""Add batch 27 of traditional cheese recipes - Ancient Mediterranean and Nordic cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-pecorino-sardo-sardinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Sardo (Sardinian)",
        "category": "mains",
        "attribution": "Sardinia, Italy, Bronze Age",
        "source_note": "Pecorino Sardo has been made in Sardinia since the Bronze Age, possibly 4000+ years. The island's unique sheep breeds and wild herbs create distinctive flavors. Two types exist: Dolce (young) and Maturo (aged).",
        "description": "Ancient Sardinian sheep cheese dating to the Bronze Age, made from milk of indigenous sheep grazing on wild Mediterranean herbs.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "1-8 months aging",
        "total_time": "1-8 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Sardinian breeds if possible"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "lamb rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional, or liquid rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 20 minutes."},
            {"step": 3, "text": "Add rennet, stir gently. Let set 30-40 minutes until firm curd."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (small). Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 113°F over 20 minutes while stirring."},
            {"step": 6, "text": "Continue stirring for 15 minutes at 113°F."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 20 lbs for 30 minutes. Flip and press at 40 lbs for 8-12 hours."},
            {"step": 9, "text": "Dry salt or brine for 24-48 hours."},
            {"step": 10, "text": "Age at 55°F and 85% humidity. Dolce: 1-2 months. Maturo: 4-8 months."}
        ],
        "temperature": "95°F start, 113°F cook, 55°F aging",
        "notes": [
            "Pecorino Sardo Dolce is soft, mild, and milky",
            "Pecorino Sardo Maturo is hard, sharp, and excellent for grating",
            "The wild herbs of Sardinian pastures (myrtle, wild fennel) flavor the milk",
            "DOP protected; one of Italy's most ancient cheeses"
        ],
        "tags": ["cheese", "traditional", "italian", "sardinian", "pecorino", "sheep-cheese", "bronze-age", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fiore-sardo-sardinian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fiore Sardo (Smoked Sardinian Pecorino)",
        "category": "mains",
        "attribution": "Sardinia, Italy, Nuragic Era (3000+ years)",
        "source_note": "Fiore Sardo ('Sardinian Flower') is possibly the original Sardinian pecorino, predating even Pecorino Sardo. Made by shepherds in the mountainous interior and traditionally smoked over aromatic wood, it may date to the Nuragic civilization.",
        "description": "The original Sardinian cheese, smoked over aromatic wood by mountain shepherds - possibly 3000+ years old.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3-8 months aging",
        "total_time": "3-8 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "still warm from milking traditionally"},
            {"item": "lamb rennet paste", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional, or liquid rennet"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "olive oil", "quantity": "for rubbing", "unit": "", "prep_note": ""},
            {"item": "aromatic wood", "quantity": "as needed", "unit": "", "prep_note": "olive, myrtle, or local woods for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh, still-warm sheep's milk (traditional) or heat to 95°F."},
            {"step": 2, "text": "Add lamb rennet paste (no starter culture - this is a raw rennet-only cheese)."},
            {"step": 3, "text": "Let set 40-50 minutes until very firm curd."},
            {"step": 4, "text": "Cut curd into small pieces and work by hand to expel whey."},
            {"step": 5, "text": "Transfer to molds and press firmly by hand."},
            {"step": 6, "text": "Let drain overnight at room temperature."},
            {"step": 7, "text": "Brine or dry salt for 2-3 days."},
            {"step": 8, "text": "Cold smoke over olive, myrtle, or local aromatic wood for 10-15 days."},
            {"step": 9, "text": "Rub with olive oil periodically during aging."},
            {"step": 10, "text": "Age at 50-55°F for 3-8 months minimum."}
        ],
        "temperature": "95°F make, cold smoking, 50-55°F aging",
        "notes": [
            "Fiore Sardo uses NO starter culture - only lamb rennet paste",
            "The smoking over aromatic Mediterranean woods is essential",
            "The name 'Fiore' (flower) may refer to the flower-shaped molds once used",
            "DOP protected; considered the original Sardinian cheese"
        ],
        "tags": ["cheese", "traditional", "italian", "sardinian", "smoked-cheese", "fiore-sardo", "sheep-cheese", "nuragic", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-kefalotyri-greek",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Kefalotyri (Greek Hard Cheese)",
        "category": "mains",
        "attribution": "Greece, Byzantine Era",
        "source_note": "Kefalotyri (meaning 'head cheese' from its shape) has been made in Greece since at least Byzantine times. It's the traditional hard cheese of Greece, used for grating and for making saganaki (pan-fried cheese).",
        "description": "Traditional Greek hard cheese for grating and frying, made since Byzantine times - the original cheese for saganaki.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons", "prep_note": "or mixed sheep/goat"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon", "prep_note": "optional blend"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 95°F."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 40-50 minutes until very firm."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Raise temperature to 122°F over 40 minutes while stirring constantly."},
            {"step": 6, "text": "Continue stirring at 122°F for 20 minutes until curds are very firm."},
            {"step": 7, "text": "Drain whey and transfer curds to molds."},
            {"step": 8, "text": "Press at 20 lbs for 1 hour. Flip and press at 50 lbs for 24 hours."},
            {"step": 9, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 10, "text": "Age at 55°F and 85% humidity for 3-12 months, turning weekly."}
        ],
        "temperature": "95°F start, 122°F cook, 55°F aging",
        "notes": [
            "Kefalotyri should be very hard - harder than most Italian pecorinos",
            "The high cooking temperature creates the firm, dense texture",
            "Essential for saganaki - fry thick slices in olive oil until golden",
            "Young kefalotyri (3 months) for frying; aged (12+ months) for grating"
        ],
        "tags": ["cheese", "traditional", "greek", "kefalotyri", "hard-cheese", "sheep-cheese", "byzantine", "saganaki"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gamalost-norwegian-viking",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Gamalost (Norwegian Viking Cheese)",
        "category": "mains",
        "attribution": "Norway, Viking Age (1000+ years)",
        "source_note": "Gamalost ('old cheese') is one of Norway's oldest cheeses, dating back to Viking times. Made from sour skim milk and inoculated with mold, it's sharp, pungent, and was an important protein source for Vikings.",
        "description": "Sharp, pungent Norwegian cheese from the Viking Age - an important protein source for Norse seafarers over a thousand years ago.",
        "servings_yield": "About 1 lb",
        "prep_time": "48 hours souring",
        "cook_time": "4-5 weeks aging",
        "total_time": "5-6 weeks",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon", "prep_note": "traditionally soured naturally"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": "as starter"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Mix skim milk with buttermilk. Let sour at room temperature for 24-48 hours."},
            {"step": 2, "text": "Heat the soured milk very slowly to 145°F, stirring occasionally."},
            {"step": 3, "text": "The curds will separate. Continue heating gently for 30 minutes."},
            {"step": 4, "text": "Drain the curds through cheesecloth. Press firmly to remove whey."},
            {"step": 5, "text": "Crumble the pressed curd and mix with salt."},
            {"step": 6, "text": "Pack into small molds or form into balls."},
            {"step": 7, "text": "Place in a humid ripening environment (70°F, 90% humidity) for 1 week."},
            {"step": 8, "text": "Mold (traditionally Mucor species) will begin to grow on the surface."},
            {"step": 9, "text": "After 1 week, knead the moldy exterior into the cheese."},
            {"step": 10, "text": "Return to ripening for 3-4 more weeks until fully covered in mold."},
            {"step": 11, "text": "When ready, the cheese should be brown and sharp-smelling."}
        ],
        "temperature": "145°F cooking, 70°F ripening",
        "notes": [
            "Gamalost is very low in fat (made from skim milk) but high in protein",
            "The sharp, pungent flavor is an acquired taste",
            "Vikings took gamalost on sea voyages as a concentrated protein source",
            "Nearly extinct but now protected as a traditional Norwegian food"
        ],
        "tags": ["cheese", "traditional", "norwegian", "viking", "gamalost", "mold-cheese", "skim-milk", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-handkase-german",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Handkäse (German Hand Cheese)",
        "category": "mains",
        "attribution": "Hesse, Germany, 16th Century (documented)",
        "source_note": "Handkäse ('hand cheese') has been made in the Hesse region of Germany since at least the 16th century, though likely much older. Named because it was traditionally shaped by hand, it's a sour milk cheese with a distinctive pungent aroma.",
        "description": "Pungent German sour milk cheese shaped by hand, a specialty of the Frankfurt region for centuries.",
        "servings_yield": "About 1 lb (several small rounds)",
        "prep_time": "24 hours souring",
        "cook_time": "3-7 days ripening",
        "total_time": "1-2 weeks",
        "ingredients": [
            {"item": "quark or farmer's cheese", "quantity": "1", "unit": "lb", "prep_note": "well-drained, low-fat"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp", "prep_note": "optional, traditional"},
            {"item": "baking soda", "quantity": "1/4", "unit": "tsp", "prep_note": "helps develop surface culture"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with well-drained, low-fat quark or farmer's cheese."},
            {"step": 2, "text": "Let quark sour at room temperature for 24 hours until tangy."},
            {"step": 3, "text": "Mix soured quark with salt, caraway (if using), and baking soda."},
            {"step": 4, "text": "Knead until smooth and uniform."},
            {"step": 5, "text": "With wet hands, shape into small disc-shaped rounds (hence 'hand cheese')."},
            {"step": 6, "text": "Place on a rack and let dry for 24 hours."},
            {"step": 7, "text": "Transfer to a humid ripening chamber (60°F, 90% humidity)."},
            {"step": 8, "text": "Ripen for 3-7 days until a yellowish rind develops."},
            {"step": 9, "text": "The cheese is ready when the surface is golden and slightly sticky."}
        ],
        "temperature": "Room temperature souring, 60°F ripening",
        "notes": [
            "Traditional Frankfurt dish: Handkäse mit Musik (with onion-vinegar dressing)",
            "The 'music' in the name refers to... digestive effects",
            "Very low in fat, high in protein",
            "The pungent aroma is much stronger than the actual flavor"
        ],
        "tags": ["cheese", "traditional", "german", "hesse", "handkase", "sour-milk-cheese", "hand-shaped", "16th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-harzer-german",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Harzer Käse (Harz Mountain Cheese)",
        "category": "mains",
        "attribution": "Harz Mountains, Germany, Medieval",
        "source_note": "Harzer Käse originated in the Harz Mountains of central Germany, where it's been made since medieval times. Like Handkäse, it's a sour milk cheese but ripened with yellow surface mold to develop its characteristic sharp flavor.",
        "description": "Pungent German sour milk cheese from the Harz Mountains, ripened with yellow mold for a sharp, tangy flavor.",
        "servings_yield": "About 1 lb",
        "prep_time": "24 hours souring",
        "cook_time": "1-2 weeks ripening",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "skim milk quark", "quantity": "1", "unit": "lb", "prep_note": "very low-fat"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "caraway seeds", "quantity": "1/2", "unit": "tsp", "prep_note": "traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Use very low-fat quark, well-drained."},
            {"step": 2, "text": "Let sour at room temperature for 24-48 hours."},
            {"step": 3, "text": "Mix with salt and caraway seeds."},
            {"step": 4, "text": "Form into small round or roll shapes."},
            {"step": 5, "text": "Let dry at room temperature for 24 hours."},
            {"step": 6, "text": "Place in ripening environment at 55-60°F and 90% humidity."},
            {"step": 7, "text": "Turn daily. Yellow surface mold (Brevibacterium linens) will develop."},
            {"step": 8, "text": "Ripen for 1-2 weeks until fully covered with golden-yellow rind."},
            {"step": 9, "text": "The interior should remain white while the surface becomes golden and aromatic."}
        ],
        "temperature": "Room temperature souring, 55-60°F ripening",
        "notes": [
            "Harzer is one of Germany's most protein-rich foods - virtually fat-free",
            "The yellow surface bacteria create the characteristic sharp aroma",
            "Popular among athletes and dieters for its high protein, low fat content",
            "The longer it ripens, the more pungent it becomes"
        ],
        "tags": ["cheese", "traditional", "german", "harz", "harzer", "sour-milk-cheese", "surface-ripened", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mizithra-greek-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mizithra (Ancient Greek Whey Cheese)",
        "category": "mains",
        "attribution": "Greece, Ancient/Homer Era",
        "source_note": "Mizithra is one of the oldest Greek cheeses, possibly the cheese Homer described the Cyclops making in the Odyssey. Made from whey with added milk, it comes fresh (soft) or aged (hard for grating).",
        "description": "Ancient Greek whey cheese possibly described by Homer - made fresh and soft or aged hard for grating.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "30 minutes",
        "cook_time": "Fresh or 3-4 months aged",
        "total_time": "1 hour fresh; 3-4 months aged",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from sheep/goat cheese making"},
            {"item": "sheep's milk", "quantity": "1", "unit": "cup", "prep_note": "for enrichment"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "if needed"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "for aged version"}
        ],
        "instructions": [
            {"step": 1, "text": "Use fresh whey from sheep or goat cheese making."},
            {"step": 2, "text": "Add fresh sheep's milk to enrich."},
            {"step": 3, "text": "Heat slowly to 185-195°F, stirring occasionally."},
            {"step": 4, "text": "White curds will rise to surface. Add lemon juice if needed."},
            {"step": 5, "text": "Let rest 10 minutes off heat."},
            {"step": 6, "text": "Gently ladle curds into a cloth-lined strainer."},
            {"step": 7, "text": "For fresh Mizithra: Drain 2-4 hours, eat immediately or within days."},
            {"step": 8, "text": "For aged Mizithra: Salt the drained curds, form into balls."},
            {"step": 9, "text": "Hang in cloth to dry for 1 week in a cool, airy place."},
            {"step": 10, "text": "Age in a cool cellar (55°F) for 3-4 months until very hard."}
        ],
        "temperature": "185-195°F, 55°F aging",
        "notes": [
            "Fresh Mizithra is soft, sweet, and mild - often served with honey",
            "Aged Mizithra (Xinomizithra) is hard, salty, and sharp - used for grating",
            "May be the cheese described in Homer's Odyssey (8th century BC)",
            "The hard aged version is Greece's traditional pasta cheese"
        ],
        "tags": ["cheese", "traditional", "greek", "ancient", "mizithra", "whey-cheese", "homer", "odyssey"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-anthotyro-greek-ancient",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Anthotyro (Greek 'Flower Cheese')",
        "category": "mains",
        "attribution": "Greece (Crete), Ancient",
        "source_note": "Anthotyro ('flower cheese') is one of Greece's most ancient cheeses, particularly associated with Crete. The poetic name refers to its delicate, pure character. Made from whey and milk, it comes fresh or aged.",
        "description": "Delicate Greek 'flower cheese' from Crete, pure and mild when fresh, sharp and grateable when aged.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "Fresh or 2-3 months aged",
        "total_time": "1 hour fresh; 2-3 months aged",
        "ingredients": [
            {"item": "fresh whey", "quantity": "3/4", "unit": "gallon", "prep_note": "from sheep/goat cheese"},
            {"item": "sheep or goat milk", "quantity": "1/4", "unit": "gallon", "prep_note": ""},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp", "prep_note": "if needed"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": "for aged version"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey and milk."},
            {"step": 2, "text": "Heat slowly to 185°F, stirring gently."},
            {"step": 3, "text": "Fine white curds will form and rise. Add lemon juice if needed."},
            {"step": 4, "text": "Remove from heat and let rest 15 minutes."},
            {"step": 5, "text": "Skim curds gently into a fine cloth-lined strainer."},
            {"step": 6, "text": "For fresh Anthotyro: Drain 1-2 hours. Eat within 2-3 days."},
            {"step": 7, "text": "For dry Anthotyro: Salt lightly, form into small cones or balls."},
            {"step": 8, "text": "Air dry in a cool, airy place for 1-2 weeks."},
            {"step": 9, "text": "Continue aging at 55°F for 2-3 months until hard."}
        ],
        "temperature": "185°F, 55°F aging",
        "notes": [
            "Fresh Anthotyro is snow-white, mild, and slightly sweet",
            "Cretan Anthotyro is particularly prized",
            "Dry Anthotyro is hard, sharp, and used for grating over pasta",
            "The 'flower' name suggests the delicacy and purity of the fresh cheese"
        ],
        "tags": ["cheese", "traditional", "greek", "cretan", "ancient", "anthotyro", "whey-cheese", "flower-cheese"],
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
