#!/usr/bin/env python3
"""Add batch 70 - Comprehensive cheesemaking technique guides."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "cheesemaking-guide-milk-selection",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Guide: Milk Selection and Preparation",
        "category": "mains",
        "attribution": "Home cheesemaking reference",
        "source_note": "Comprehensive guide for home cheesemakers",
        "description": "The foundation of great cheese is great milk. Understanding milk types, fat content, pasteurization effects, and preparation techniques is essential for consistent results. This guide covers everything from supermarket milk to farm-fresh raw milk.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Whole milk", "quantity": "", "unit": "", "prep_note": "3.25-4% fat, most versatile"},
            {"item": "Raw milk", "quantity": "", "unit": "", "prep_note": "Unpasteurized, farm-fresh"},
            {"item": "HTST pasteurized milk", "quantity": "", "unit": "", "prep_note": "161°F for 15 seconds"},
            {"item": "Ultra-pasteurized (UHT)", "quantity": "", "unit": "", "prep_note": "280°F briefly - AVOID"},
            {"item": "Goat milk", "quantity": "", "unit": "", "prep_note": "Lower fat, smaller fat globules"},
            {"item": "Sheep milk", "quantity": "", "unit": "", "prep_note": "Highest fat and protein"}
        ],
        "instructions": [
            {"step": 1, "text": "MILK TYPES: Raw milk makes the best cheese - it has intact proteins and natural beneficial bacteria. However, it's not available everywhere and has safety considerations. HTST pasteurized is a good alternative. NEVER use ultra-pasteurized (UHT) - the proteins are denatured and won't form proper curds."},
            {"step": 2, "text": "FAT CONTENT: Whole milk (3.25%+ fat) is standard for most cheeses. Cream can be added for richer cheese. Skim milk makes lower-fat cheese but with weaker curd and different texture. For specific cheese styles, match the milk type to tradition."},
            {"step": 3, "text": "HOMOGENIZATION: Homogenized milk has fat globules broken up so cream doesn't separate. It makes cheese but with slightly different texture. Non-homogenized ('cream-line') milk is preferred by many cheesemakers. The cream layer adds extra richness."},
            {"step": 4, "text": "CALCIUM CHLORIDE: Pasteurization reduces calcium availability, weakening curd formation. Add calcium chloride (typically 1/4-1/2 tsp per gallon, diluted in water) to pasteurized milk to restore proper curdling. Not needed for raw milk."},
            {"step": 5, "text": "MILK FRESHNESS: Use the freshest milk possible. Older milk has higher bacteria counts and more developed acidity, which can affect flavor and texture. Ideally, use milk within 2-3 days of purchase."},
            {"step": 6, "text": "GOAT MILK: Naturally homogenized with smaller fat globules. Makes tangier cheese due to different fatty acid profile. Set is often softer; may need more rennet or different cultures. Excellent for chèvre, feta-style, and aged chevres."},
            {"step": 7, "text": "SHEEP MILK: Richest in fat (6-9%) and protein, producing highest cheese yield per gallon. Traditional for Roquefort, Pecorino, Manchego. More expensive and harder to find. Makes incredibly rich, complex cheese."},
            {"step": 8, "text": "TEMPERATURE HISTORY: Milk should be kept cold (under 40°F) until use. If milk has been frozen, it may not set properly. Let refrigerated milk come to target temperature gradually - don't shock it with rapid heating."},
            {"step": 9, "text": "LIPASE: For cheeses traditionally made from raw milk, adding lipase powder recreates the sharp, piquant flavors that develop from natural milk enzymes. Common in Italian cheeses like Provolone and Pecorino. Use sparingly - it's powerful."},
            {"step": 10, "text": "TROUBLESHOOTING: Weak or no curd? Check for ultra-pasteurized milk, old rennet, or chlorinated water. Rubbery curd? Too much rennet or culture. Off flavors? May be milk past prime or contamination. When in doubt, start with fresh, whole milk from a reputable dairy."}
        ],
        "temperature": "Store at 38-40°F, warm to recipe temperature",
        "notes": [
            "The quality of your cheese is directly linked to the quality of your milk",
            "Never use ultra-pasteurized milk - it cannot form proper curds",
            "Raw milk requires extra care regarding sanitation and temperature control",
            "Different milks (cow, goat, sheep, buffalo) create distinctly different cheeses",
            "When possible, source milk from grass-fed animals for better flavor"
        ],
        "tags": ["cheese", "cheesemaking", "guide", "milk", "reference", "technique", "basics"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "cheesemaking-guide-aging-environments",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Guide: Creating Proper Aging Environments",
        "category": "mains",
        "attribution": "Home cheesemaking reference",
        "source_note": "Comprehensive guide for home cheesemakers",
        "description": "Proper aging is as important as proper cheesemaking. This guide covers creating aging environments in home settings, from simple refrigerator solutions to dedicated cheese caves. Temperature, humidity, and air circulation all affect how your cheese develops.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Wine refrigerator", "quantity": "", "unit": "", "prep_note": "Ideal 50-55°F aging"},
            {"item": "Standard refrigerator", "quantity": "", "unit": "", "prep_note": "Too cold (35-40°F) for most aging"},
            {"item": "Plastic containers with lids", "quantity": "", "unit": "", "prep_note": "For humidity control"},
            {"item": "Cheese mats/bamboo mats", "quantity": "", "unit": "", "prep_note": "For air circulation"},
            {"item": "Hygrometer", "quantity": "", "unit": "", "prep_note": "To monitor humidity"},
            {"item": "Damp cloth or salt water", "quantity": "", "unit": "", "prep_note": "To maintain humidity"}
        ],
        "instructions": [
            {"step": 1, "text": "TEMPERATURE REQUIREMENTS: Most aged cheeses want 50-57°F (10-14°C). Fresh cheeses store at regular refrigerator temp (38-40°F). Blue cheeses often prefer cooler caves (45-50°F). Washed rinds like warmer initial aging (60-65°F) then cooler (50-55°F)."},
            {"step": 2, "text": "WINE REFRIGERATOR: The easiest solution for home cheese aging. Most wine fridges hold 50-55°F perfectly. Choose one with humidity control or add water containers. Glass door lets you monitor cheese without opening."},
            {"step": 3, "text": "STANDARD REFRIGERATOR: Too cold for most aging but can work for short-term. Use the warmest spot (often top shelf or crisper). A closed container with damp cloth maintains humidity. Open container lets cheese dry out."},
            {"step": 4, "text": "HUMIDITY REQUIREMENTS: Most cheeses want 80-95% humidity during aging. Too dry = cracked rind and case hardening. Too wet = excessive mold and sliminess. Washed rinds need highest humidity (90-95%). Natural rinds can tolerate lower (75-85%)."},
            {"step": 5, "text": "CREATING HUMIDITY: In containers, place damp (not wet) cloth or small dish of salt water. Salt water releases humidity more slowly and consistently than plain water. Replace or rewet regularly."},
            {"step": 6, "text": "AIR CIRCULATION: Cheese needs to breathe but shouldn't dry out. Cheese mats elevate cheese from sitting in moisture. Flip cheese regularly for even drying. Never seal cheese in airtight container during aging (except waxed cheese)."},
            {"step": 7, "text": "BASEMENT CAVES: If you have a basement at 50-60°F, you may have a natural cheese cave. Monitor temperature seasonally. Increase humidity with wet towels or humidifier. Watch for mold on walls indicating good humidity."},
            {"step": 8, "text": "DEDICATED CHEESE CAVES: For serious hobbyists, convert a small refrigerator or purchase purpose-built cheese cave. These maintain precise temperature and humidity with minimal intervention."},
            {"step": 9, "text": "MONITORING: Check cheese at least weekly. Record temperature, humidity, and cheese condition. Note any mold development (normal for many cheeses). Adjust environment based on how cheese is developing."},
            {"step": 10, "text": "COMMON PROBLEMS: Cheese drying too fast? Increase humidity. Slimy surface? Decrease humidity, improve air circulation. Unwanted mold? Check for contamination, wipe with brine. Cheese not aging? Check temperature isn't too cold."}
        ],
        "temperature": "50-57°F for most aged cheese, 80-95% humidity",
        "notes": [
            "A wine refrigerator is the best investment for home cheese aging",
            "Humidity is just as important as temperature",
            "Different cheese styles require different conditions",
            "Monitoring and adjusting is an ongoing process",
            "Natural caves maintain ideal conditions without electricity"
        ],
        "tags": ["cheese", "cheesemaking", "guide", "aging", "cave", "reference", "technique"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "cheesemaking-guide-cultures-explained",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Guide: Understanding Starter Cultures",
        "category": "mains",
        "attribution": "Home cheesemaking reference",
        "source_note": "Comprehensive guide for home cheesemakers",
        "description": "Starter cultures are the living heart of cheesemaking - bacteria that acidify milk and develop flavor. Understanding the difference between mesophilic and thermophilic cultures, and when to use each, is fundamental to making great cheese.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Mesophilic culture", "quantity": "", "unit": "", "prep_note": "Moderate temperatures, 70-102°F"},
            {"item": "Thermophilic culture", "quantity": "", "unit": "", "prep_note": "Higher temperatures, 104-130°F"},
            {"item": "Penicillium candidum", "quantity": "", "unit": "", "prep_note": "White bloomy rinds (Brie, Camembert)"},
            {"item": "Penicillium roqueforti", "quantity": "", "unit": "", "prep_note": "Blue veins (Roquefort, Stilton)"},
            {"item": "Brevibacterium linens", "quantity": "", "unit": "", "prep_note": "Orange washed rinds (Époisses, Munster)"},
            {"item": "Propionibacterium", "quantity": "", "unit": "", "prep_note": "Eye formation (Swiss, Emmentaler)"}
        ],
        "instructions": [
            {"step": 1, "text": "MESOPHILIC CULTURES: Work at moderate temperatures (70-102°F). Used for most cheeses that don't involve high cooking: cheddar, Gouda, Brie, Camembert, blue cheese, feta, chèvre. Common strains: Lactococcus lactis, Lactococcus cremoris. Die at temperatures above 102°F."},
            {"step": 2, "text": "THERMOPHILIC CULTURES: Thrive at higher temperatures (104-130°F). Essential for 'cooked curd' cheeses: Parmesan, Swiss, Mozzarella, Provolone. Common strains: Streptococcus thermophilus, Lactobacillus helveticus, Lactobacillus delbrueckii. Work with high-temperature cooking."},
            {"step": 3, "text": "DIRECT-SET (DVI) CULTURES: Freeze-dried cultures added directly to milk. Convenient and consistent. One packet per specified milk volume. No preparation needed. Most common for home cheesemakers. Store frozen."},
            {"step": 4, "text": "BULK CULTURES (Mother Cultures): Cultures propagated by the cheesemaker in milk. More traditional, potentially more complex flavor. Requires maintenance (daily/weekly transfers). Risk of contamination. Used by experienced cheesemakers."},
            {"step": 5, "text": "RIPENING CULTURES: Added for surface development. Penicillium candidum creates white fuzzy rinds on Brie/Camembert. Penicillium roqueforti creates blue veins. Brevibacterium linens creates orange washed rinds. Usually added with starter culture."},
            {"step": 6, "text": "PROPIONIC CULTURES: Propionibacterium shermanii creates 'eyes' (holes) in Swiss-style cheese. Produces CO2 gas that forms bubbles in the paste. Also contributes sweet, nutty flavor. Requires specific aging conditions."},
            {"step": 7, "text": "DOSAGE: Follow manufacturer's guidelines. Typical DVI: 1/8 to 1/4 tsp per 2 gallons milk. Too much culture = overly acidic cheese. Too little = weak flavor development. Adjust based on experience with your specific conditions."},
            {"step": 8, "text": "STORAGE: Freeze-dried cultures should be stored in freezer (-4°F or colder). They lose potency over time even frozen. Buy fresh annually. Don't let them thaw and refreeze repeatedly."},
            {"step": 9, "text": "RIPENING TIME: Cultures need time to acidify milk before rennet is added. This 'ripening' period (30-90 minutes typically) allows bacteria to begin working. Longer ripening = more acidity = different cheese character."},
            {"step": 10, "text": "COMBINING CULTURES: Many cheeses use multiple cultures. Example: Mozzarella uses thermophilic starter + add citric acid for quick acidification. Washed rinds use mesophilic + B. linens. Understanding combinations is advanced cheesemaking."}
        ],
        "temperature": "Mesophilic: 70-102°F, Thermophilic: 104-130°F",
        "notes": [
            "Cultures are living organisms - treat them carefully",
            "Match culture type to cheese style and cooking temperature",
            "Fresh, properly stored cultures are essential for success",
            "Ripening time affects acidity and final cheese character",
            "Traditional cheeses often relied on natural milk bacteria"
        ],
        "tags": ["cheese", "cheesemaking", "guide", "cultures", "starter", "reference", "technique", "bacteria"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "cheesemaking-guide-troubleshooting",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cheesemaking Guide: Troubleshooting Common Problems",
        "category": "mains",
        "attribution": "Home cheesemaking reference",
        "source_note": "Comprehensive guide for home cheesemakers",
        "description": "Every cheesemaker encounters problems. This guide helps diagnose and fix common issues from weak curds to off-flavors to rind problems. Understanding what went wrong helps prevent future mistakes and salvage current batches when possible.",
        "servings_yield": "Reference guide",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "ingredients": [
            {"item": "Fresh milk", "quantity": "", "unit": "", "prep_note": "Avoid ultra-pasteurized"},
            {"item": "Fresh rennet", "quantity": "", "unit": "", "prep_note": "Check expiration"},
            {"item": "Active cultures", "quantity": "", "unit": "", "prep_note": "Store frozen"},
            {"item": "Non-chlorinated water", "quantity": "", "unit": "", "prep_note": "For diluting rennet"},
            {"item": "Clean equipment", "quantity": "", "unit": "", "prep_note": "Sanitize properly"}
        ],
        "instructions": [
            {"step": 1, "text": "WEAK OR NO CURD: Causes - ultra-pasteurized milk (most common), old rennet, chlorinated water deactivating rennet, milk too cold, too little rennet. Solutions - use HTST pasteurized milk, fresh rennet, filtered water, proper temperature. If no curd in 90 min, try adding more rennet."},
            {"step": 2, "text": "RUBBERY/TOUGH CURD: Causes - too much rennet, curd set too long, cooked too hot, too much acid. Solutions - reduce rennet, cut curd sooner, lower cooking temp, reduce ripening time. Rubbery cheese is still edible but texture won't improve with aging."},
            {"step": 3, "text": "SOFT/MUSHY CHEESE: Causes - too little rennet, weak culture, not enough pressing, too much moisture. Solutions - increase rennet, use fresh culture, press longer/harder, drain more whey. Soft cheese can be aged longer or used as fresh cheese."},
            {"step": 4, "text": "BITTER FLAVOR: Causes - too much rennet, vegetable/microbial rennet in long-aged cheese, contamination, too much lipase, protein breakdown issues. Solutions - reduce rennet, switch rennet type for aged cheese, improve sanitation, reduce lipase."},
            {"step": 5, "text": "SOUR/ACIDIC CHEESE: Causes - too much culture, too long ripening, too long draining, milk was already acidic. Solutions - reduce culture, shorten ripening time, don't overwork curds, use fresher milk. Some acidity mellows with aging."},
            {"step": 6, "text": "UNWANTED MOLD: Causes - contamination, too much humidity, insufficient salt, poor air circulation. Blue/green mold - if not a blue cheese, scrub with brine and improve conditions. Black mold - usually discard affected area. Pink/orange - often harmless but investigate."},
            {"step": 7, "text": "CRACKED RIND: Causes - aging too dry, temperature fluctuations, cheese dried too fast, insufficient fat in milk. Solutions - increase humidity, stabilize temperature, slow initial drying, use whole milk. Cracks can be sealed with butter or lard."},
            {"step": 8, "text": "CHEESE WON'T AGE: Causes - too cold (refrigerator is too cold for most aging), too much salt inhibiting bacteria, insufficient moisture, dead cultures. Solutions - use wine fridge or cheese cave, reduce salt, maintain proper humidity, use fresh cultures."},
            {"step": 9, "text": "OFF-FLAVORS/SMELLS: Ammonia smell (especially in bloomy rinds) - overripe, eat soon or discard. Barnyard/funky (in washed rinds) - often normal. Truly rotten smell - contamination, discard. Soapy flavor - rancid fat, discard."},
            {"step": 10, "text": "GENERAL PREVENTION: Keep detailed notes on every batch. Sanitize everything that touches milk or curd. Use fresh ingredients. Control temperature precisely. Maintain proper aging conditions. Learn from each batch and adjust."}
        ],
        "temperature": "Varies by issue",
        "notes": [
            "Most problems come from milk quality, culture/rennet freshness, or temperature control",
            "Keep detailed notes to identify patterns in problems",
            "Many issues can still produce edible cheese, just different from intended",
            "When in doubt about safety (off smells, weird colors), discard",
            "Experience and note-taking are the best teachers"
        ],
        "tags": ["cheese", "cheesemaking", "guide", "troubleshooting", "reference", "technique", "problems"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-reblochon-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Reblochon (Savoyard Farmer's Secret Cheese)",
        "category": "mains",
        "attribution": "French tradition from Savoie, 13th century",
        "source_note": "Modernized from traditional Savoyard methods, adapted for home cheesemaking",
        "description": "Born of peasant tax evasion in the 13th century, Reblochon was made from the 'second milking' - after the tax collector had measured the herd's output, farmers would milk again. This rich, creamy, second-milk cheese became the heart of tartiflette. The name comes from 'reblocher' (to pinch again).",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "1 hour",
        "cook_time": "2 hours",
        "total_time": "3 hours plus 3-4 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "richest available"},
            {"item": "heavy cream", "quantity": "1/2", "unit": "cup", "prep_note": "to mimic second milking richness"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "1.5", "unit": "tsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 95°F (35°C). Add calcium chloride and culture. Ripen 30 minutes."},
            {"step": 2, "text": "Add diluted rennet. Let set 30-40 minutes until soft clean break."},
            {"step": 3, "text": "Cut curd into 1-inch cubes (larger curds for creamy texture). Let rest 10 minutes."},
            {"step": 4, "text": "Very gently stir for 10 minutes at 95°F. Keep curds large and moist."},
            {"step": 5, "text": "Drain whey. Ladle curds into small round molds (about 3-4 inches). Do not press."},
            {"step": 6, "text": "Flip every 30 minutes for 3 hours. Let drain overnight at room temperature."},
            {"step": 7, "text": "Salt surfaces lightly. Begin aging at 55°F (13°C) and 95% humidity."},
            {"step": 8, "text": "Wash gently with brine every 2-3 days. A yellowish-pink rind will develop."},
            {"step": 9, "text": "Age 3-4 weeks. Interior becomes creamy and slightly runny near rind."},
            {"step": 10, "text": "Essential ingredient in tartiflette - baked with potatoes, bacon, and onions."}
        ],
        "temperature": "95°F curd, 55°F aging",
        "notes": [
            "Invented by farmers hiding milk production from tax collectors",
            "Second milking was richer because less volume, more fat",
            "Has PDO protection - must be made in specific Savoie areas",
            "Fermier Reblochon (farm-made) is distinguished by green casein mark",
            "Tartiflette was invented in 1980s to promote Reblochon sales"
        ],
        "tags": ["cheese", "cheesemaking", "french", "savoyard", "reblochon", "washed-rind", "soft-cheese", "medieval", "pdo"],
        "confidence": {"overall": "high", "flags": []}
    },
    {
        "id": "traditional-bleu-dauvergne-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Bleu d'Auvergne (Volcanic Blue Cheese)",
        "category": "mains",
        "attribution": "French tradition from Auvergne, 19th century",
        "source_note": "Modernized from traditional Auvergnat methods, adapted for home cheesemaking",
        "description": "Created in the mid-1800s by Antoine Roussel, Bleu d'Auvergne was an attempt to replicate Roquefort in the volcanic mountains of Auvergne. Made from cow's milk rather than sheep's, it developed its own character - creamy, pungent, with bold blue veins. It's become one of France's most popular blues.",
        "servings_yield": "About 2 lbs cheese",
        "prep_time": "1.5 hours",
        "cook_time": "4 hours",
        "total_time": "6 hours plus 4-8 weeks aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted"},
            {"item": "non-iodized salt", "quantity": "3", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add calcium chloride, mesophilic culture, and P. roqueforti. Ripen 1 hour."},
            {"step": 2, "text": "Add diluted rennet. Let set 1-1.5 hours until soft clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Stir very gently for 30 minutes at 86°F. Keep curds moist."},
            {"step": 5, "text": "Drain whey. Ladle curds into tall cylindrical molds without pressing."},
            {"step": 6, "text": "Flip every hour for 6 hours, then let drain overnight at room temperature."},
            {"step": 7, "text": "Dry salt all surfaces generously. Repeat salting daily for 5 days."},
            {"step": 8, "text": "Pierce cheese through with skewer in grid pattern to allow air for blue development."},
            {"step": 9, "text": "Age at 46-50°F (8-10°C) and 95% humidity for 4-8 weeks."},
            {"step": 10, "text": "Blue veins develop in the pierced channels. Flavor is bold and creamy."}
        ],
        "temperature": "86°F curd, 46-50°F aging",
        "notes": [
            "Antoine Roussel developed this cheese around 1854 using rye bread mold",
            "Unlike Roquefort (sheep), Bleu d'Auvergne is cow's milk",
            "Has PDO protection since 1975",
            "Volcanic caves of Auvergne provide natural aging conditions",
            "More accessible flavor than Roquefort for blue cheese beginners"
        ],
        "tags": ["cheese", "cheesemaking", "french", "auvergnat", "bleu-dauvergne", "blue-cheese", "aged-cheese", "pdo"],
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
