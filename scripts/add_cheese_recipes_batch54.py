#!/usr/bin/env python3
"""Add batch 54 - Fresh cheeses, American heritage cheeses, and advanced tips."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-tip-starter-culture-guide",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Tip: Complete Starter Culture Guide",
        "category": "mains",
        "attribution": "Scientific cheesemaking knowledge",
        "source_note": "Artisan cheesemaking techniques compilation",
        "description": "Starter cultures are the heart of cheesemaking, determining flavor, texture, and safety. Understanding different cultures and when to use them is essential for any serious cheesemaker.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "mesophilic cultures", "quantity": "", "unit": "", "prep_note": "for cheeses made below 102°F"},
            {"item": "thermophilic cultures", "quantity": "", "unit": "", "prep_note": "for cheeses made above 102°F"},
            {"item": "specialty cultures", "quantity": "", "unit": "", "prep_note": "propionic, brevibacterium, penicillium"}
        ],
        "instructions": [
            {"step": 1, "text": "MESOPHILIC ('middle-loving'): Works best at 70-102°F. Use for cheddar, Gouda, feta, brie, blue cheese, most soft and semi-hard cheeses."},
            {"step": 2, "text": "Common mesophilic: Lactococcus lactis (acidification), Lactococcus cremoris (flavor/texture), Leuconostoc (CO2 for eyes)."},
            {"step": 3, "text": "THERMOPHILIC ('heat-loving'): Works best at 100-130°F. Use for Swiss, Parmesan, provolone, mozzarella, other Italian styles."},
            {"step": 4, "text": "Common thermophilic: Streptococcus thermophilus (fast acid), Lactobacillus helveticus (nutty flavor), Lactobacillus delbrueckii."},
            {"step": 5, "text": "PROPIONIC BACTERIA: Added to Swiss-style for eye formation. Creates CO2 that forms holes and sweet/nutty flavor."},
            {"step": 6, "text": "BREVIBACTERIUM LINENS: Surface culture for washed-rind cheeses. Creates orange color and pungent aroma."},
            {"step": 7, "text": "PENICILLIUM CANDIDUM: White mold for bloomy-rind cheeses like Brie and Camembert."},
            {"step": 8, "text": "PENICILLIUM ROQUEFORTI: Blue mold for blue cheeses. Creates characteristic blue veins and sharp flavor."},
            {"step": 9, "text": "GEOTRICHUM CANDIDUM: Yeast-like mold that helps other molds establish. Used with P. candidum for wrinkled rinds."},
            {"step": 10, "text": "DOSING: Follow package instructions. Typically 1/8-1/4 tsp per 2 gallons. Under-dosing slows fermentation; over-dosing can cause bitterness."},
            {"step": 11, "text": "STORAGE: Keep cultures frozen (-10°F) for years, or refrigerated for weeks. Never let them warm up repeatedly."},
            {"step": 12, "text": "NATURAL STARTERS: Whey from previous batch, cultured buttermilk, or clabbered milk. Traditional but less predictable."}
        ],
        "temperature": "Varies by culture type",
        "notes": [
            "Direct-set cultures are added directly to milk; bulk cultures are propagated first",
            "Some makers develop their own 'house cultures' from raw milk over years",
            "Temperature determines which bacteria dominate - that's why it matters",
            "Blended cultures combine multiple strains for complex flavor development",
            "Fresh, properly stored cultures make consistently better cheese"
        ],
        "tags": ["cheese", "technique", "tip", "cultures", "starter", "science"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-quark-german-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Quark (German Fresh Cheese)",
        "category": "mains",
        "attribution": "Central European staple tradition",
        "source_note": "Traditional German/Austrian cheesemaking",
        "description": "Germany's most consumed dairy product, Quark is a fresh acid-set cheese somewhere between yogurt and cream cheese. Made throughout Central and Eastern Europe for centuries, it's used in everything from cheesecakes to savory dishes.",
        "servings_yield": "1 lb quark",
        "prep_time": "10 minutes",
        "cook_time": "N/A",
        "total_time": "12-24 hours culturing + draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "pasteurized fine"},
            {"item": "buttermilk", "quantity": "1", "unit": "cup", "prep_note": "cultured, active"},
            {"item": "rennet", "quantity": "1", "unit": "drop", "prep_note": "optional, tiny amount for firmer curd"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Stir in cultured buttermilk thoroughly."},
            {"step": 3, "text": "If using rennet, add just 1-2 drops diluted in water - this is very little."},
            {"step": 4, "text": "Cover and let sit at room temperature (70-75°F) for 12-24 hours."},
            {"step": 5, "text": "Milk will thicken and gel like yogurt."},
            {"step": 6, "text": "When fully set, cut gently into 1-inch cubes (optional - helps draining)."},
            {"step": 7, "text": "Line colander with butter muslin or tight cheesecloth."},
            {"step": 8, "text": "Gently ladle curd into lined colander."},
            {"step": 9, "text": "Let drain 4-8 hours until desired consistency."},
            {"step": 10, "text": "For smooth quark, blend briefly or pass through fine sieve."},
            {"step": 11, "text": "Refrigerate. Use within 1-2 weeks."}
        ],
        "temperature": "86°F (30°C) to start; room temperature to culture",
        "notes": [
            "German 'Magerquark' is fat-free; 'Sahnequark' is creamy - adjust with milk fat content",
            "Essential for German cheesecake (Käsekuchen)",
            "Also called 'tvorog' in Russia, 'tvaroh' in Czech",
            "Consistency ranges from pourable to spreadable depending on draining",
            "Naturally tangy - sweeten for desserts or use savory in dips"
        ],
        "tags": ["cheese", "german", "traditional", "fresh", "acid-set", "simple"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-fromage-blanc-french-fresh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Fromage Blanc (French Fresh White Cheese)",
        "category": "mains",
        "attribution": "Ancient French farmhouse tradition",
        "source_note": "Traditional French fresh cheesemaking",
        "description": "Fromage blanc (white cheese) is France's answer to quark - a simple, fresh, tangy cheese made on farms for millennia. Lighter than cream cheese, it's eaten with fruit, honey, or herbs, and used in cooking.",
        "servings_yield": "1 lb cheese",
        "prep_time": "10 minutes",
        "cook_time": "N/A",
        "total_time": "12-18 hours culturing + draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "fromage blanc culture", "quantity": "1", "unit": "packet", "prep_note": "or crème fraîche as starter"},
            {"item": "rennet", "quantity": "2", "unit": "drops", "prep_note": "very small amount"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72-75°F (22-24°C) - just slightly warm."},
            {"step": 2, "text": "Add fromage blanc culture (or 2 tbsp crème fraîche as starter)."},
            {"step": 3, "text": "Add 1-2 drops of rennet diluted in 1/4 cup cool water."},
            {"step": 4, "text": "Stir gently for 1 minute."},
            {"step": 5, "text": "Cover and let sit at room temperature for 12-18 hours."},
            {"step": 6, "text": "Curd should be set like thick yogurt - spoon will leave mark."},
            {"step": 7, "text": "Line colander with butter muslin."},
            {"step": 8, "text": "Gently spoon curd into cloth without breaking too much."},
            {"step": 9, "text": "Let drain 6-12 hours until desired consistency."},
            {"step": 10, "text": "Transfer to container. Add salt, herbs, or sweetener as desired."},
            {"step": 11, "text": "Refrigerate. Best within 1-2 weeks."}
        ],
        "temperature": "72-75°F (22-24°C) to start; room temperature to culture",
        "notes": [
            "Lighter and more delicate than American cream cheese",
            "Traditional French breakfast: fromage blanc with berries and honey",
            "Can be made richer by using part cream",
            "Very versatile - sweet with fruit or savory with herbs",
            "Similar to quark but typically lighter texture"
        ],
        "tags": ["cheese", "french", "traditional", "fresh", "simple", "breakfast"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cream-cheese-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cream Cheese (American Style)",
        "category": "mains",
        "attribution": "19th century American invention",
        "source_note": "Traditional American fresh cheesemaking",
        "description": "American cream cheese was invented in 1872 by William Lawrence in New York, attempting to recreate Neufchâtel. The result was richer and denser - now a uniquely American creation essential for cheesecake and bagels.",
        "servings_yield": "1 lb cream cheese",
        "prep_time": "20 minutes",
        "cook_time": "N/A",
        "total_time": "12-24 hours culturing + draining",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "quart", "prep_note": ""},
            {"item": "heavy cream", "quantity": "1", "unit": "quart", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream in pot. Heat to 75°F (24°C)."},
            {"step": 2, "text": "Add mesophilic culture, stir well."},
            {"step": 3, "text": "Add rennet diluted in 1/4 cup water, stir gently for 1 minute."},
            {"step": 4, "text": "Cover and let sit at room temperature for 12-24 hours."},
            {"step": 5, "text": "Curd should be firm with clear whey separation."},
            {"step": 6, "text": "Line colander with butter muslin."},
            {"step": 7, "text": "Gently ladle curd into cloth."},
            {"step": 8, "text": "Tie cloth and hang to drain for 12-24 hours until very thick."},
            {"step": 9, "text": "Transfer drained curd to bowl."},
            {"step": 10, "text": "Add salt and beat with mixer until smooth and spreadable."},
            {"step": 11, "text": "Pack into container, refrigerate. Keeps 2-3 weeks."}
        ],
        "temperature": "75°F (24°C) to start; room temperature to culture",
        "notes": [
            "The cream makes it richer and denser than French fromage blanc",
            "Essential for New York cheesecake",
            "Beating at the end creates the smooth, spreadable texture",
            "Philadelphia-style is the benchmark for American cream cheese",
            "Can add herbs, garlic, or other flavors for spread variations"
        ],
        "tags": ["cheese", "american", "traditional", "fresh", "cream", "bagel"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-farmers-cheese-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Farmer's Cheese (American Dry Curd)",
        "category": "mains",
        "attribution": "European immigrant tradition in America",
        "source_note": "Traditional American farmhouse cheesemaking",
        "description": "Brought to America by European immigrants, farmer's cheese is dry cottage cheese pressed into blocks. Common in Jewish, German, and Eastern European communities, it's used for blintzes, pierogies, and baking.",
        "servings_yield": "1 lb cheese",
        "prep_time": "20 minutes",
        "cook_time": "1-2 hours",
        "total_time": "4-6 hours total",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "cultured"},
            {"item": "white vinegar", "quantity": "1/4", "unit": "cup", "prep_note": "or lemon juice"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and buttermilk in large pot."},
            {"step": 2, "text": "Heat slowly to 180°F (82°C), stirring occasionally."},
            {"step": 3, "text": "Add vinegar gradually while stirring gently."},
            {"step": 4, "text": "Curds will separate from whey. If not, add more acid."},
            {"step": 5, "text": "Remove from heat, let sit 10 minutes."},
            {"step": 6, "text": "Line colander with cheesecloth, drain curds."},
            {"step": 7, "text": "Rinse curds with cool water to remove acid taste."},
            {"step": 8, "text": "Add salt to drained curds, mix well."},
            {"step": 9, "text": "Wrap in cloth and press in mold or shape by hand."},
            {"step": 10, "text": "Press 2-4 hours with moderate weight."},
            {"step": 11, "text": "Unwrap and refrigerate. Keeps 1-2 weeks."}
        ],
        "temperature": "180°F (82°C)",
        "notes": [
            "Similar to queso fresco, paneer, and quark in concept",
            "Dry curds make it ideal for stuffing blintzes and pierogies",
            "Jewish delis traditionally offer farmer's cheese",
            "Can be eaten fresh or used in cooking and baking",
            "Rinsing is important to remove sharp acid flavor"
        ],
        "tags": ["cheese", "american", "traditional", "fresh", "immigrant", "baking"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-cottage-cheese-american",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cottage Cheese (American Curds and Cream)",
        "category": "mains",
        "attribution": "Colonial American tradition",
        "source_note": "Traditional American farmhouse cheesemaking",
        "description": "America's most popular fresh cheese, cottage cheese was made in colonial home kitchens using naturally soured milk. The name comes from making it in rural cottages. Large or small curd, it remains a protein-rich staple.",
        "servings_yield": "1 lb cottage cheese",
        "prep_time": "20 minutes",
        "cook_time": "2-3 hours",
        "total_time": "4-6 hours total",
        "ingredients": [
            {"item": "skim milk", "quantity": "1", "unit": "gallon", "prep_note": "traditionally skimmed"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted, optional"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "cream", "quantity": "1/2", "unit": "cup", "prep_note": "for creaming"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat skim milk to 72°F (22°C)."},
            {"step": 2, "text": "Add mesophilic culture, stir well."},
            {"step": 3, "text": "Add rennet if using (creates firmer curd)."},
            {"step": 4, "text": "Cover and let sit at room temperature 12-16 hours until firmly set."},
            {"step": 5, "text": "Cut curd into 1/2-inch cubes (small curd) or 1-inch cubes (large curd)."},
            {"step": 6, "text": "Let rest 10 minutes, then stir very gently."},
            {"step": 7, "text": "Heat slowly to 115°F (46°C) over 1-2 hours, stirring occasionally."},
            {"step": 8, "text": "When curds are firm and slightly squeaky, drain whey."},
            {"step": 9, "text": "Rinse curds with cold water to stop cooking and remove acid."},
            {"step": 10, "text": "Drain well, add salt, mix gently."},
            {"step": 11, "text": "Add cream to reach desired creaminess. Refrigerate."}
        ],
        "temperature": "72°F (22°C) to culture; heat to 115°F (46°C)",
        "notes": [
            "Small curd: cut smaller, heat higher. Large curd: cut larger, lower heat",
            "The cream adds richness - adjust or omit for dietary preferences",
            "Colonial housewives made this from naturally soured milk",
            "Rinsing removes the tangy acid taste, making it milder",
            "High protein, low fat when made with skim and minimal cream"
        ],
        "tags": ["cheese", "american", "traditional", "fresh", "curds", "cottage"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-colby-wisconsin-original",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Colby (Wisconsin Original)",
        "category": "mains",
        "attribution": "1885 Wisconsin invention",
        "source_note": "Traditional American cheesemaking",
        "description": "Invented in 1885 by Joseph Steinwand in Colby, Wisconsin, this is one of America's few original cheese styles. By washing the curds with cold water, he created a milder, moister cheese than cheddar - distinctly American.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "5-6 hours",
        "total_time": "1-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto", "quantity": "4", "unit": "drops", "prep_note": "for traditional orange color"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""},
            {"item": "cold water", "quantity": "1", "unit": "gallon", "prep_note": "for washing curds"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add annatto for orange color if desired."},
            {"step": 3, "text": "Add mesophilic culture, ripen 45 minutes."},
            {"step": 4, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 5, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 6, "text": "Stir gently and raise temperature to 102°F (39°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are moderately firm."},
            {"step": 8, "text": "Drain about half the whey."},
            {"step": 9, "text": "KEY STEP: Add cold water to curds, stirring gently. This 'washes' out lactose and acid."},
            {"step": 10, "text": "Continue stirring in cold water bath until curds are at 80°F (27°C)."},
            {"step": 11, "text": "Drain water, salt curds."},
            {"step": 12, "text": "Pack into molds, press at 30 lbs for 1 hour, then 50 lbs overnight."},
            {"step": 13, "text": "Wax and age at 55°F for 1-3 months."}
        ],
        "temperature": "86-102°F (30-39°C) for curd; cold water wash; 55°F (13°C) for aging",
        "notes": [
            "The cold water wash is the defining step - removes lactose, creates mild sweet flavor",
            "Does not go through cheddaring process - no matting or milling",
            "Moister and more open texture than cheddar",
            "Best aged 1-3 months - doesn't improve much beyond that",
            "Colby-Jack combines Colby and Monterey Jack curds"
        ],
        "tags": ["cheese", "american", "wisconsin", "traditional", "washed-curd", "original"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-monterey-jack-california",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Monterey Jack (California Mission Cheese)",
        "category": "mains",
        "attribution": "Spanish mission tradition, 18th century",
        "source_note": "Traditional California cheesemaking",
        "description": "Originating at California's Spanish missions in the 1700s, this cheese was commercialized by David Jacks of Monterey in the 1880s. Mild, semi-soft, and excellent for melting, it became California's signature cheese.",
        "servings_yield": "2 lb wheel",
        "prep_time": "30 minutes",
        "cook_time": "4-5 hours",
        "total_time": "1-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "animal rennet", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C)."},
            {"step": 2, "text": "Add mesophilic culture, ripen 30-45 minutes."},
            {"step": 3, "text": "Add diluted rennet, let set 30-40 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes."},
            {"step": 5, "text": "Stir gently for 15 minutes without raising temperature."},
            {"step": 6, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes."},
            {"step": 7, "text": "Continue stirring until curds are moderately firm but still moist."},
            {"step": 8, "text": "Drain most whey."},
            {"step": 9, "text": "Stir curds gently to prevent matting - Monterey Jack is NOT cheddared."},
            {"step": 10, "text": "Salt curds and mix well."},
            {"step": 11, "text": "Pack into molds, press at 20 lbs for 1 hour, then 40 lbs overnight."},
            {"step": 12, "text": "Wax or vacuum seal."},
            {"step": 13, "text": "Age at 50°F: 1-2 weeks for fresh Jack, 1-6 months for aged (Dry Jack)."}
        ],
        "temperature": "88-100°F (31-38°C) for make; 50°F (10°C) for aging",
        "notes": [
            "Fresh Jack is mild and melts beautifully - perfect for quesadillas",
            "Dry Jack (aged 7+ months) becomes hard, sharp, and grateable",
            "Pepper Jack adds jalapeños to the curds",
            "Franciscan missionaries likely adapted Spanish cheese techniques",
            "David Jacks branded it as 'Jack's Cheese' which became Monterey Jack"
        ],
        "tags": ["cheese", "american", "california", "traditional", "mission", "melting"],
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
