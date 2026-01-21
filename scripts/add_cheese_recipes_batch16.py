#!/usr/bin/env python3
"""Add batch 16 of traditional cheese recipes - fresh and soft cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-cottage-cheese-1800s",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cottage Cheese (1800s American Farmhouse)",
        "category": "mains",
        "attribution": "American Farmhouse Tradition, 1800s",
        "source_note": "Cottage cheese was a staple of American farmhouse kitchens in the 1800s, made from naturally soured milk. The name comes from the cottages where it was commonly made.",
        "description": "Simple fresh cheese made from clabbered milk, a farmhouse staple that requires no special equipment or cultures.",
        "servings_yield": "About 1 lb",
        "prep_time": "24-48 hours",
        "cook_time": "30 minutes",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "raw milk", "quantity": "1", "unit": "gallon", "prep_note": "or pasteurized non-homogenized"},
            {"item": "buttermilk", "quantity": "1/4", "unit": "cup", "prep_note": "as starter if using pasteurized milk"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp", "prep_note": ""},
            {"item": "cream", "quantity": "2-4", "unit": "tbsp", "prep_note": "optional, for creaming"}
        ],
        "instructions": [
            {"step": 1, "text": "If using raw milk, leave covered at room temperature for 24-48 hours until it clabbers (thickens and slightly sours). If using pasteurized milk, add buttermilk starter and let sit 24 hours."},
            {"step": 2, "text": "Once milk has thickened and shows clear whey separation, cut the curd into 1/2-inch cubes using a long knife."},
            {"step": 3, "text": "Very slowly heat the curds to 110°F over 30-40 minutes, stirring gently every few minutes to prevent matting."},
            {"step": 4, "text": "Hold at 110°F for 20-30 minutes until curds are firm but still tender when squeezed."},
            {"step": 5, "text": "Pour into a colander lined with butter muslin. Let drain for 5 minutes."},
            {"step": 6, "text": "Rinse curds with cold water to stop cooking and remove excess acid. Drain well."},
            {"step": 7, "text": "Toss with salt. For creamed cottage cheese, fold in cream to desired consistency."},
            {"step": 8, "text": "Refrigerate and use within 1 week."}
        ],
        "temperature": "110°F cooking",
        "notes": [
            "The slower you heat the curds, the more tender the final cheese",
            "Small curd cottage cheese uses smaller cuts; large curd uses bigger cuts",
            "Adding cream makes it 'creamed cottage cheese' - adjust amount to taste"
        ],
        "tags": ["cheese", "traditional", "american", "farmhouse", "fresh-cheese", "cottage-cheese", "1800s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-ricotta-italian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Italian Ricotta",
        "category": "mains",
        "attribution": "Italian Tradition, Ancient",
        "source_note": "Ricotta means 're-cooked' in Italian - it was traditionally made from whey left over from other cheese making, heated again to extract remaining proteins. References date to Roman times.",
        "description": "Classic Italian whey cheese, light and creamy, made by re-cooking whey with a splash of fresh milk for better yield.",
        "servings_yield": "About 2 cups",
        "prep_time": "15 minutes",
        "cook_time": "30 minutes",
        "total_time": "1 hour including draining",
        "ingredients": [
            {"item": "fresh whey", "quantity": "1", "unit": "gallon", "prep_note": "from mozzarella or other cheese making"},
            {"item": "whole milk", "quantity": "1", "unit": "cup", "prep_note": "for better yield"},
            {"item": "white vinegar or lemon juice", "quantity": "2", "unit": "tbsp", "prep_note": "if whey is not acidic enough"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey and milk in a large non-reactive pot."},
            {"step": 2, "text": "Heat slowly over medium heat, stirring occasionally to prevent scorching."},
            {"step": 3, "text": "As temperature approaches 185-195°F, white fluffy curds will begin to rise to the surface."},
            {"step": 4, "text": "If curds don't form by 190°F, add vinegar or lemon juice one tablespoon at a time."},
            {"step": 5, "text": "Once curds have formed and are floating on top, remove from heat and let rest 10 minutes."},
            {"step": 6, "text": "Gently ladle curds into a fine-mesh strainer or butter muslin-lined colander."},
            {"step": 7, "text": "Let drain for 15-30 minutes depending on desired consistency."},
            {"step": 8, "text": "Salt lightly if desired. Use immediately or refrigerate up to 5 days."}
        ],
        "temperature": "185-195°F",
        "notes": [
            "The fresher the whey, the better the ricotta - use within hours of cheese making",
            "Whey from acid-set cheeses won't produce ricotta as well as rennet-set whey",
            "For whole milk ricotta without whey, use 1/2 gallon milk heated to 200°F with 3 tbsp lemon juice"
        ],
        "tags": ["cheese", "traditional", "italian", "whey-cheese", "ricotta", "fresh-cheese", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-mascarpone-lombard",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Mascarpone (Lombard Method)",
        "category": "mains",
        "attribution": "Lombardy, Italy, 16th Century",
        "source_note": "Mascarpone originated in the Lombardy region of Italy, possibly named from 'mascarpa' (ricotta in Lombard dialect) or 'mas que bueno' (better than good). First documented in the late 1500s.",
        "description": "Ultra-rich Italian cream cheese with a buttery, slightly sweet flavor, essential for tiramisu and other Italian desserts.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 minutes",
        "cook_time": "20 minutes",
        "total_time": "12-24 hours including draining",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "quart", "prep_note": "not ultra-pasteurized if possible"},
            {"item": "tartaric acid", "quantity": "1/4", "unit": "tsp", "prep_note": "dissolved in 1 tbsp water"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp", "prep_note": "alternative to tartaric acid"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour cream into a double boiler or heavy-bottomed pot set over simmering water."},
            {"step": 2, "text": "Heat cream slowly to 185°F, stirring occasionally to prevent skin formation."},
            {"step": 3, "text": "Add dissolved tartaric acid (or lemon juice) and stir gently for 5 minutes while maintaining temperature."},
            {"step": 4, "text": "The cream will thicken slightly and coat the back of a spoon - it won't form distinct curds like other cheeses."},
            {"step": 5, "text": "Remove from heat and let cool to room temperature."},
            {"step": 6, "text": "Pour into a fine-mesh strainer lined with several layers of butter muslin set over a bowl."},
            {"step": 7, "text": "Cover and refrigerate for 12-24 hours until desired thickness is reached."},
            {"step": 8, "text": "Transfer to a container and refrigerate. Use within 1 week."}
        ],
        "temperature": "185°F",
        "notes": [
            "Tartaric acid produces the most authentic flavor; lemon juice adds a slight citrus note",
            "Do not use ultra-pasteurized cream - it won't set properly",
            "The longer you drain, the thicker the mascarpone becomes",
            "For sweeter mascarpone, you can add 1 tbsp powdered sugar after draining"
        ],
        "tags": ["cheese", "traditional", "italian", "lombard", "cream-cheese", "mascarpone", "16th-century", "dessert-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-halloumi-cypriot",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cypriot Halloumi",
        "category": "mains",
        "attribution": "Cyprus, Medieval Period",
        "source_note": "Halloumi has been made in Cyprus since at least the Medieval Byzantine period. The name may derive from Egyptian Arabic 'hallum'. Traditional halloumi uses a mix of sheep and goat milk.",
        "description": "Distinctive squeaky grilling cheese from Cyprus that holds its shape when cooked, traditionally made from sheep and goat milk.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "sheep milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or goat milk"},
            {"item": "goat milk", "quantity": "1/2", "unit": "gallon", "prep_note": "or use all sheep or cow milk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup cool water"},
            {"item": "salt", "quantity": "2", "unit": "tbsp", "prep_note": "for brining"},
            {"item": "dried mint", "quantity": "2", "unit": "tbsp", "prep_note": "traditional filling"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat mixed milks to 90°F in a large pot."},
            {"step": 2, "text": "Add diluted rennet, stir gently for 30 seconds, then let sit undisturbed for 45-60 minutes until a clean break is achieved."},
            {"step": 3, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly raise temperature to 104°F over 30 minutes, stirring gently."},
            {"step": 5, "text": "Pour curds into cheese molds and press lightly for 1 hour, flipping every 20 minutes."},
            {"step": 6, "text": "Reserve the whey and heat to 195°F. Add pressed cheese to hot whey."},
            {"step": 7, "text": "Poach cheese in whey for 30-60 minutes until it floats and is firm throughout."},
            {"step": 8, "text": "Remove cheese, fold in half while warm, tucking dried mint in the fold if desired."},
            {"step": 9, "text": "Make brine with reserved whey and salt. Submerge folded cheese and store refrigerated."},
            {"step": 10, "text": "Halloumi can be eaten fresh or stored in brine for several months."}
        ],
        "temperature": "90°F make, 195°F poach",
        "notes": [
            "The hot whey poaching step is what gives halloumi its unique high melting point",
            "Traditional halloumi is always folded with mint inside",
            "Can be made with cow's milk, but sheep/goat blend is more authentic",
            "To grill: slice 1/2-inch thick and cook on high heat until golden on each side"
        ],
        "tags": ["cheese", "traditional", "cypriot", "grilling-cheese", "halloumi", "mediterranean", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-burrata-puglia",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Burrata (Puglia Style)",
        "category": "mains",
        "attribution": "Puglia, Italy, 1920s",
        "source_note": "Burrata was invented in the 1920s in Andria, Puglia, as a way to use up mozzarella scraps. The name means 'buttered' in Italian, referring to its rich creamy interior.",
        "description": "Fresh Italian cheese with a mozzarella shell encasing a creamy stracciatella filling, the crown jewel of fresh cheeses.",
        "servings_yield": "4 burrata balls",
        "prep_time": "1 hour",
        "cook_time": "30 minutes",
        "total_time": "2-3 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "not ultra-pasteurized"},
            {"item": "citric acid", "quantity": "1 1/2", "unit": "tsp", "prep_note": "dissolved in 1/2 cup cool water"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup cool water"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "heavy cream", "quantity": "1/2", "unit": "cup", "prep_note": "for stracciatella filling"}
        ],
        "instructions": [
            {"step": 1, "text": "Add citric acid solution to cold milk in pot, stir well. Heat to 90°F."},
            {"step": 2, "text": "Remove from heat, add rennet solution, stir gently for 30 seconds. Let sit 5-10 minutes until clean break."},
            {"step": 3, "text": "Cut curd into 1-inch cubes. Let rest 5 minutes, then slowly heat to 105°F while stirring."},
            {"step": 4, "text": "Drain curds and let mat for 15-20 minutes until they become stretchy."},
            {"step": 5, "text": "Heat water to 170-180°F with salt. Test a small piece of curd - if it stretches smoothly, it's ready."},
            {"step": 6, "text": "Working in batches, submerge curd in hot water and stretch until smooth and shiny, forming a thin sheet."},
            {"step": 7, "text": "Set aside 1/4 of the stretched mozzarella. Tear remaining mozzarella into small shreds (stracciatella)."},
            {"step": 8, "text": "Mix shredded mozzarella with heavy cream and a pinch of salt."},
            {"step": 9, "text": "Form the reserved mozzarella into small pouches. Fill each with 2-3 tbsp of stracciatella mixture."},
            {"step": 10, "text": "Pinch closed and twist to seal. Store in lightly salted water. Best eaten within 24-48 hours."}
        ],
        "temperature": "90°F curd, 170-180°F stretching",
        "notes": [
            "Burrata must be eaten very fresh - it's best the day it's made",
            "The key to good burrata is a thin, stretchy shell with a creamy, oozy center",
            "Serve at room temperature with good olive oil, salt, and crusty bread",
            "The stracciatella filling should be loose and creamy, not dense"
        ],
        "tags": ["cheese", "traditional", "italian", "puglia", "fresh-cheese", "burrata", "mozzarella", "1920s"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-taleggio-lombardy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Taleggio (Lombardy Washed-Rind)",
        "category": "mains",
        "attribution": "Val Taleggio, Lombardy, Italy, 10th Century",
        "source_note": "Taleggio is one of the oldest soft cheeses, named after the Val Taleggio caves in the Bergamo Alps where it was traditionally aged. Documentation dates to the 10th century.",
        "description": "Pungent Italian washed-rind cheese with a thin rosy crust and soft, tangy interior - one of Italy's most ancient cheeses.",
        "servings_yield": "About 2 lb",
        "prep_time": "2 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "raw or pasteurized"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "salt brine", "quantity": "1", "unit": "quart", "prep_note": "saturated salt solution for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk. Add starter culture and B. linens, stir well."},
            {"step": 2, "text": "Let ripen for 30 minutes at 90°F."},
            {"step": 3, "text": "Add diluted rennet, stir gently for 30 seconds. Let set for 45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 3/4-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Stir gently for 20 minutes, maintaining 90°F temperature."},
            {"step": 6, "text": "Drain whey and ladle curds into square molds (traditionally 8x8 inches)."},
            {"step": 7, "text": "Let drain at room temperature for 8-12 hours, flipping every 2-3 hours."},
            {"step": 8, "text": "Unmold and salt all surfaces. Let rest 24 hours."},
            {"step": 9, "text": "Move to aging cave at 50°F and 90% humidity."},
            {"step": 10, "text": "Wash with light brine solution every 2-3 days for the first 3 weeks, then weekly."},
            {"step": 11, "text": "Age for 6-8 weeks until rind is rosy-orange and interior is soft and bulging."}
        ],
        "temperature": "90°F make, 50°F aging",
        "notes": [
            "The characteristic pink-orange rind comes from the B. linens bacteria activated by washing",
            "Traditional aging caves had natural humidity and temperature - a cheese cave or wine fridge works",
            "Ripe Taleggio should bulge slightly when pressed and have a pungent, fruity aroma",
            "If blue mold appears, wipe with brine more frequently"
        ],
        "tags": ["cheese", "traditional", "italian", "lombardy", "washed-rind", "taleggio", "aged-cheese", "10th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-fontina-valdaosta",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fontina (Val d'Aosta)",
        "category": "mains",
        "attribution": "Val d'Aosta, Italy, 12th Century",
        "source_note": "Fontina has been made in the Aosta Valley of the Italian Alps since at least the 12th century. The name may derive from the village of Fontinaz or the Italian 'fondere' (to melt).",
        "description": "Buttery semi-soft Alpine cheese from Italy's Aosta Valley, prized for its superior melting qualities and earthy, nutty flavor.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "3 months aging",
        "total_time": "3 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from single milking if possible"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 96°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add thermophilic starter, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently, and let set for 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 118°F over 45 minutes while stirring continuously."},
            {"step": 6, "text": "Continue stirring at 118°F for 30 minutes until curds are firm and springy."},
            {"step": 7, "text": "Drain whey and transfer curds to a cloth-lined mold. Press at 10 lbs for 30 minutes."},
            {"step": 8, "text": "Flip and press at 20 lbs for 8-12 hours."},
            {"step": 9, "text": "Unmold and float in saturated brine for 8-12 hours (1 hour per pound)."},
            {"step": 10, "text": "Air dry at room temperature for 2-3 days until surface is dry to touch."},
            {"step": 11, "text": "Age at 50-55°F and 90% humidity for 3 months minimum, flipping weekly and wiping with dry cloth."}
        ],
        "temperature": "96°F start, 118°F cook, 50-55°F aging",
        "notes": [
            "Traditional Fontina uses milk from a single milking for best flavor",
            "The natural rind should develop a light brown color during aging",
            "Perfect for fondue - it melts smoothly without becoming stringy",
            "Authentic Fontina from Val d'Aosta is DOP protected; this is a traditional-style recipe"
        ],
        "tags": ["cheese", "traditional", "italian", "alpine", "fontina", "semi-soft", "12th-century", "melting-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-muenster-alsatian",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Munster (Alsatian)",
        "category": "mains",
        "attribution": "Alsace-Lorraine/Vosges Region, 7th Century",
        "source_note": "Munster cheese originated in the Vosges mountains, named after the town of Munster (from Latin 'monasterium' - monastery) where monks began making it in the 7th century. Not to be confused with American Muenster.",
        "description": "Pungent Alsatian washed-rind cheese with a sticky orange rind and creamy, intensely flavored interior - traditional monastic cheese.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "5-8 weeks aging",
        "total_time": "5-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "raw or pasteurized"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "light brine", "quantity": "2", "unit": "cups", "prep_note": "2 tbsp salt per cup water"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture and B. linens, stir well. Let ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir for 30 seconds. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 30 minutes at 90°F. Curds should shrink slightly and become firmer."},
            {"step": 6, "text": "Drain most of the whey and ladle curds into round molds."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, flipping every 4-6 hours."},
            {"step": 8, "text": "Unmold and rub all surfaces with salt. Let rest 24 hours."},
            {"step": 9, "text": "Transfer to aging environment at 55°F and 95% humidity."},
            {"step": 10, "text": "Wash every 2 days with light brine for the first 2 weeks, then every 3-4 days."},
            {"step": 11, "text": "Age for 5-8 weeks until rind is sticky and orange, and cheese gives when pressed."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "Traditional Munster is much stronger than American Muenster, which is a mild imitation",
            "The sticky orange rind is essential - it's where much of the flavor develops",
            "Often served with cumin seeds (Munster au Cumin) or alongside Gewürztraminer wine",
            "The aroma is powerful, but the flavor is rich, meaty, and complex",
            "If white mold appears, wash more frequently with slightly stronger brine"
        ],
        "tags": ["cheese", "traditional", "french", "alsatian", "washed-rind", "munster", "monastery-cheese", "7th-century"],
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
