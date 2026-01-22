#!/usr/bin/env python3
"""Add batch 30 of traditional cheese recipes - Ancient and historical cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-crottin-de-chavignol-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Crottin de Chavignol (French Goat Cheese)",
        "category": "mains",
        "attribution": "Loire Valley, France / 16th Century",
        "source_note": "AOC protected since 1976, made in Chavignol since the 1500s. Name means 'little dropping' referring to its small round shape.",
        "description": "Small round French goat cheese from the Loire Valley with a wrinkled rind that develops from young and mild to aged and piquant over time.",
        "servings_yield": "About 4 small cheeses (2 oz each)",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh, at room temperature"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "MM100 or similar"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "for wrinkled rind"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "optional, for white coating"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops", "prep_note": "diluted in water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat milk to 72°F in a large pot."},
            {"step": 2, "text": "Add mesophilic culture, Geotrichum candidum, and Penicillium candidum. Stir gently to distribute."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk. Stir gently."},
            {"step": 4, "text": "Add diluted rennet and stir with up-and-down motions for 30 seconds."},
            {"step": 5, "text": "Cover and let set at 72°F for 18-24 hours until curd shows clean break."},
            {"step": 6, "text": "Gently ladle curds into small Crottin molds (about 2.5 inches diameter)."},
            {"step": 7, "text": "Let drain at room temperature for 24 hours, flipping several times."},
            {"step": 8, "text": "When firm enough to handle, unmold and salt all surfaces lightly."},
            {"step": 9, "text": "Place on drying mat in ripening box at 55°F, 85% humidity."},
            {"step": 10, "text": "Turn daily. Wrinkled Geotrichum rind develops within 5-7 days."},
            {"step": 11, "text": "Age for 2 weeks for mild, 4 weeks for stronger flavor, or longer for très sec."}
        ],
        "temperature": "72°F make, 55°F aging",
        "notes": [
            "Traditional Crottin uses very slow acidification over 18-24 hours",
            "The wrinkled 'brain-like' rind is characteristic of proper Geotrichum development",
            "Young (mi-sec) is creamy, aged (sec) is drier, very aged (très sec) is hard and sharp",
            "Chavignol is a small village near Sancerre - the wines pair perfectly with this cheese"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "aged", "loire-valley", "aoc", "16th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-valençay-french-goat",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Valençay (French Pyramid Goat Cheese)",
        "category": "mains",
        "attribution": "Indre, France / Medieval Origins",
        "source_note": "Legend says Napoleon sliced off the top of the pyramid shape after his Egyptian defeat. AOC protected cheese from the Berry region.",
        "description": "Truncated pyramid-shaped French goat cheese coated in vegetable ash, with a creamy interior and distinctive tangy flavor.",
        "servings_yield": "About 2 pyramids (7 oz each)",
        "prep_time": "2 hours",
        "cook_time": "3-5 weeks aging",
        "total_time": "3-5 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted"},
            {"item": "vegetable ash", "quantity": "2", "unit": "tbsp", "prep_note": "food-grade activated charcoal"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm goat milk to 68-72°F."},
            {"step": 2, "text": "Add cultures (mesophilic, P. candidum, G. candidum) and stir gently."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and stir briefly."},
            {"step": 5, "text": "Cover and let set for 18-24 hours at 68-72°F until firm curd forms."},
            {"step": 6, "text": "Carefully ladle curds into truncated pyramid molds, filling to top."},
            {"step": 7, "text": "Let drain at room temperature for 48 hours, flipping twice daily as curds compact."},
            {"step": 8, "text": "Unmold carefully and salt all surfaces."},
            {"step": 9, "text": "Let dry for 24 hours, then dust entire surface with vegetable ash."},
            {"step": 10, "text": "Place in ripening area at 52-55°F with 90% humidity."},
            {"step": 11, "text": "Turn every other day. White mold will grow through the ash in 1-2 weeks."},
            {"step": 12, "text": "Age for 3-5 weeks until rind is established and interior is creamy."}
        ],
        "temperature": "68-72°F make, 52-55°F aging",
        "notes": [
            "The ash coating helps neutralize acidity on the surface, encouraging mold growth",
            "Authentic shape is a truncated pyramid - flat top, wider base",
            "Interior should be chalky near the rind with a creamy center when properly aged",
            "Pairs wonderfully with Sancerre and other Loire Valley wines"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "ash-coated", "pyramid", "berry-region", "aoc"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pouligny-saint-pierre-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pouligny-Saint-Pierre (French 'Eiffel Tower' Cheese)",
        "category": "mains",
        "attribution": "Indre, France / Ancient Origins",
        "source_note": "Called 'the Eiffel Tower' or 'the pyramid' for its distinctive tall pointed shape. One of the oldest AOC goat cheeses in France.",
        "description": "Tall pyramid-shaped French goat cheese with a natural rind, featuring a fine, dense texture and pronounced goaty flavor.",
        "servings_yield": "About 2 pyramids (9 oz each)",
        "prep_time": "2 hours",
        "cook_time": "4-5 weeks aging",
        "total_time": "4-5 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh from Alpine or Saanen goats"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "6", "unit": "drops", "prep_note": "very small amount"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": "fine, non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm goat milk to 70°F - no higher for this delicate cheese."},
            {"step": 2, "text": "Add mesophilic culture and Penicillium candidum. Stir gently."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add just 6 drops of rennet - this cheese relies primarily on acid coagulation."},
            {"step": 5, "text": "Cover and let acidify for 24-36 hours at 68-70°F until curd is firm."},
            {"step": 6, "text": "Gently ladle curd into tall pyramid molds (about 5 inches tall with pointed top)."},
            {"step": 7, "text": "Drain for 48 hours at room temperature, turning twice daily."},
            {"step": 8, "text": "Unmold and salt all surfaces moderately."},
            {"step": 9, "text": "Dry at room temperature for 24 hours."},
            {"step": 10, "text": "Transfer to cave or ripening area at 50-55°F, 85-90% humidity."},
            {"step": 11, "text": "Turn every other day. Natural blue-gray molds will develop on rind."},
            {"step": 12, "text": "Age minimum 4 weeks, longer for stronger flavor."}
        ],
        "temperature": "70°F make, 50-55°F aging",
        "notes": [
            "The tall pointed pyramid shape is unique to this cheese",
            "Very low rennet and long acidification gives distinctive fine texture",
            "Natural rind develops blue-gray molds - this is characteristic",
            "Interior should be slightly chalky with clean, tangy goat flavor"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "pyramid", "aoc", "berry-region", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-sainte-maure-de-touraine-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Sainte-Maure de Touraine (French Log Cheese)",
        "category": "mains",
        "attribution": "Touraine, France / 8th Century",
        "source_note": "One of the oldest French goat cheeses, traditionally made since the Arab invasions brought goats to France. The straw through the center is its trademark.",
        "description": "Log-shaped French goat cheese with a distinctive straw running through its center, ash-coated exterior, and creamy tangy interior.",
        "servings_yield": "About 2 logs (9 oz each)",
        "prep_time": "2 hours",
        "cook_time": "3-4 weeks aging",
        "total_time": "3-4 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": "very small amount"},
            {"item": "rye straw", "quantity": "2", "unit": "pieces", "prep_note": "sterilized, 6 inches long"},
            {"item": "vegetable ash", "quantity": "2", "unit": "tbsp", "prep_note": "food-grade"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Warm goat milk to 68-70°F."},
            {"step": 2, "text": "Add all cultures and stir gently to distribute."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add small amount of diluted rennet."},
            {"step": 5, "text": "Cover and let acidify for 18-24 hours until curd is firm."},
            {"step": 6, "text": "Place sterilized rye straw lengthwise in log-shaped molds."},
            {"step": 7, "text": "Carefully ladle curd into molds around the straw."},
            {"step": 8, "text": "Drain for 24-48 hours, turning carefully to avoid disturbing straw."},
            {"step": 9, "text": "Unmold gently - straw should remain centered in the log."},
            {"step": 10, "text": "Salt all surfaces, then coat with vegetable ash."},
            {"step": 11, "text": "Age at 52-55°F, 85-90% humidity, turning every other day."},
            {"step": 12, "text": "Ready in 3-4 weeks when rind is established and paste is creamy."}
        ],
        "temperature": "68-70°F make, 52-55°F aging",
        "notes": [
            "The straw serves dual purpose: structural support during aging and proof of authenticity",
            "Traditional straw is rye, burned with the producer's ID for AOC cheeses",
            "Arabs brought goats to the Loire Valley in the 8th century after the Battle of Poitiers",
            "Interior texture changes from chalky to creamy as it ripens from outside in"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "ash-coated", "log", "aoc", "8th-century", "touraine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-selles-sur-cher-french",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Selles-sur-Cher (French Ash-Rind Goat)",
        "category": "mains",
        "attribution": "Loir-et-Cher, France / 19th Century",
        "source_note": "Named after the town of Selles-sur-Cher. The ash was originally used to protect the cheese from flies in farm cellars.",
        "description": "Small disc-shaped French goat cheese with a distinctive blue-gray ash rind, mild creamy interior, and delicate nutty flavor.",
        "servings_yield": "About 4 small discs (5 oz each)",
        "prep_time": "2 hours",
        "cook_time": "2-3 weeks aging",
        "total_time": "2-3 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "2", "unit": "gallons", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "poplar wood ash", "quantity": "3", "unit": "tbsp", "prep_note": "or food-grade vegetable ash"},
            {"item": "sea salt", "quantity": "1", "unit": "tbsp", "prep_note": "fine"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm goat milk to 68-72°F."},
            {"step": 2, "text": "Add all cultures and stir gently."},
            {"step": 3, "text": "Add calcium chloride if needed, then diluted rennet."},
            {"step": 4, "text": "Let set for 18-24 hours at room temperature until firm."},
            {"step": 5, "text": "Ladle curds gently into flat disc molds (about 3.5 inches diameter, 1 inch deep)."},
            {"step": 6, "text": "Drain for 24-48 hours, flipping several times as curds compact."},
            {"step": 7, "text": "Unmold and salt all surfaces lightly."},
            {"step": 8, "text": "Let dry for several hours, then coat completely with ash."},
            {"step": 9, "text": "Place in ripening area at 52-55°F, 85-90% humidity."},
            {"step": 10, "text": "Turn every other day. Blue-gray mold grows through ash in 7-10 days."},
            {"step": 11, "text": "Age for 2-3 weeks minimum until paste is creamy near rind."}
        ],
        "temperature": "68-72°F make, 52-55°F aging",
        "notes": [
            "Traditional ash is from poplar wood, mixed with salt",
            "The ash creates the distinctive blue-gray appearance as mold grows through it",
            "Milder than many French goat cheeses - good introduction to chèvre",
            "Best eaten young to medium aged - doesn't benefit from extended aging"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "ash-coated", "disc", "aoc", "loire-valley"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cabécou-french-goat",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cabécou (French Occitan Goat Cheese)",
        "category": "mains",
        "attribution": "Périgord/Quercy, France / Ancient Origins",
        "source_note": "Name comes from Occitan 'cabra' meaning goat. Made for centuries in southwest France, possibly since Roman times.",
        "description": "Tiny round French goat cheese from the Dordogne region, traditionally eaten fresh or wrapped in leaves and aged.",
        "servings_yield": "About 8 small rounds (1.5 oz each)",
        "prep_time": "1.5 hours",
        "cook_time": "Fresh or 2-4 weeks aged",
        "total_time": "1 day to 4 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "1", "unit": "gallon", "prep_note": "fresh"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "very small amount"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "chestnut or grape leaves", "quantity": "8", "unit": "leaves", "prep_note": "optional, for wrapping aged versions"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm goat milk to 70-72°F."},
            {"step": 2, "text": "Add mesophilic culture and stir gently."},
            {"step": 3, "text": "Add just 2 drops of rennet - cabécou relies mostly on acid coagulation."},
            {"step": 4, "text": "Cover and let set for 20-24 hours at room temperature."},
            {"step": 5, "text": "Ladle delicate curd into tiny round molds (about 2 inches diameter)."},
            {"step": 6, "text": "Drain for 24 hours at room temperature, turning once."},
            {"step": 7, "text": "Unmold and sprinkle lightly with salt."},
            {"step": 8, "text": "For fresh cabécou: eat within 3-5 days, soft and mild."},
            {"step": 9, "text": "For aged: wrap in chestnut or grape leaves soaked in eau-de-vie."},
            {"step": 10, "text": "Age wrapped cheeses at 52-55°F for 2-4 weeks until firmer and more piquant."}
        ],
        "temperature": "70-72°F make, 52-55°F aging",
        "notes": [
            "Cabécou is one of the smallest French cheeses - about 1.5 oz each",
            "Fresh version is mild and creamy, aged version wrapped in leaves is sharper",
            "Traditionally wrapped in chestnut, walnut, or grape leaves soaked in plum brandy",
            "Rocamadour is a famous AOC type of cabécou"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "tiny", "occitan", "périgord", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-banon-french-wrapped",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Banon (French Chestnut Leaf Wrapped)",
        "category": "mains",
        "attribution": "Provence, France / Roman Era",
        "source_note": "Evidence of this cheese dates to Roman Gaul. The chestnut leaf wrapping preserves it and imparts subtle tannins.",
        "description": "Small round Provençal cheese wrapped in chestnut leaves and tied with raffia, developing a creamy runny interior with earthy flavors.",
        "servings_yield": "About 4 small rounds (3 oz each)",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "raw goat milk", "quantity": "1", "unit": "gallon", "prep_note": "or mixed goat/cow milk"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": ""},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if pasteurized"},
            {"item": "liquid rennet", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp", "prep_note": ""},
            {"item": "dried chestnut leaves", "quantity": "16", "unit": "leaves", "prep_note": "soaked in water or white wine"},
            {"item": "natural raffia", "quantity": "4", "unit": "strips", "prep_note": "for tying"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to 68-72°F."},
            {"step": 2, "text": "Add mesophilic culture and Geotrichum candidum. Stir gently."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Add diluted rennet and stir briefly."},
            {"step": 5, "text": "Let set for 18-24 hours until curd is firm."},
            {"step": 6, "text": "Ladle curds into small round molds (about 3 inches diameter)."},
            {"step": 7, "text": "Drain for 24-48 hours, flipping several times."},
            {"step": 8, "text": "Unmold and salt all surfaces. Let dry for 1-2 days."},
            {"step": 9, "text": "Soak dried chestnut leaves in water or white wine until pliable."},
            {"step": 10, "text": "Wrap each cheese in 4 overlapping chestnut leaves, brown side out."},
            {"step": 11, "text": "Tie securely with raffia in a cross pattern."},
            {"step": 12, "text": "Age at 50-55°F, 90% humidity for 2-4 weeks until paste softens and runs."}
        ],
        "temperature": "68-72°F make, 50-55°F aging",
        "notes": [
            "Banon has been made since Roman times in Haute-Provence",
            "The chestnut leaves add tannins and protect while allowing controlled ripening",
            "When properly aged, the interior should be creamy to runny",
            "Traditional versions dip leaves in eau-de-vie before wrapping"
        ],
        "tags": ["cheese", "traditional", "french", "goat", "wrapped", "provence", "roman-era", "aoc", "chestnut-leaf"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-brocciu-corsican-whey",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Brocciu (Corsican Whey Cheese)",
        "category": "mains",
        "attribution": "Corsica, France / Ancient Origins",
        "source_note": "Corsica's only AOC cheese, made from sheep or goat whey. Essential to Corsican cuisine since ancient times.",
        "description": "Fresh Corsican whey cheese similar to ricotta but tangier, made by heating whey with fresh milk and traditionally eaten very fresh.",
        "servings_yield": "About 1.5 lb",
        "prep_time": "30 minutes",
        "cook_time": "1 hour",
        "total_time": "3-4 hours with draining",
        "ingredients": [
            {"item": "fresh sheep or goat whey", "quantity": "1", "unit": "gallon", "prep_note": "from cheesemaking, still warm"},
            {"item": "whole sheep or goat milk", "quantity": "2", "unit": "cups", "prep_note": "fresh"},
            {"item": "sea salt", "quantity": "1", "unit": "tsp", "prep_note": "Corsican grey salt traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh warm whey immediately after making another cheese."},
            {"step": 2, "text": "Add fresh milk to the whey - this provides protein for the brocciu."},
            {"step": 3, "text": "Heat slowly while stirring gently, bringing to 175-185°F."},
            {"step": 4, "text": "As temperature rises, proteins will begin to coagulate and rise."},
            {"step": 5, "text": "When curds float to surface, stop stirring and let rest 5 minutes."},
            {"step": 6, "text": "Skim the floating curds carefully into traditional woven rush baskets or ricotta molds."},
            {"step": 7, "text": "Sprinkle with sea salt while still warm."},
            {"step": 8, "text": "Drain for 2-3 hours until firm enough to hold shape."},
            {"step": 9, "text": "Eat fresh within 3-4 days, or salt more heavily for passu (aged) version."}
        ],
        "temperature": "175-185°F cooking",
        "notes": [
            "Must use whey from sheep or goat milk for authentic brocciu",
            "Adding fresh milk is essential - provides the protein that creates the curds",
            "Traditional Corsican baskets give characteristic ridged pattern",
            "Used in fiadone (Corsican cheesecake) and many traditional dishes",
            "Passu is the aged version, salted and dried for several weeks"
        ],
        "tags": ["cheese", "traditional", "french", "corsican", "whey", "fresh", "sheep", "goat", "aoc", "ancient"],
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
