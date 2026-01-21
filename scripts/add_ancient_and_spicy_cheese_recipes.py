#!/usr/bin/env python3
"""Add ancient Roman and super-hot pepper cheese recipes to recipes.json"""

import json

# Load existing recipes
with open('data/recipes.json', 'r') as f:
    data = json.load(f)

new_recipes = [
    {
        "id": "columella-roman-cheese-65ce",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Columella's Roman Cheese (65 CE)",
        "category": "sides",
        "attribution": "Lucius Junius Moderatus Columella, De Re Rustica",
        "source_note": "Ancient Roman recipe from Columella's agricultural treatise 'De Re Rustica' (65 CE). Reconstructed from Tavola Mediterranea.",
        "description": "An authentic ancient Roman cheese recipe using fig-sap rennet as described by Columella in the 1st century CE. This simple fresh cheese was a staple of Roman cuisine.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Overnight plus 3 hours active",
        "ingredients": [
            {"item": "whole goat's or cow's milk", "quantity": "4", "unit": "liters", "prep_note": "not ultra-pasteurized"},
            {"item": "fig-sap rennet", "quantity": "2", "unit": "tbsp", "prep_note": "or vegetable rennet, vinegar, or lemon juice"},
            {"item": "salt", "quantity": "35", "unit": "g", "prep_note": "per liter of brine water"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to boiling while whisking continuously to prevent scorching."},
            {"step": 2, "text": "Remove from heat and add your coagulant (fig rennet, vinegar, or lemon juice)."},
            {"step": 3, "text": "Let the milk curdle undisturbed for 30 minutes."},
            {"step": 4, "text": "Strain curds through cheesecloth and drain for 1 hour."},
            {"step": 5, "text": "Bundle the curds in cheesecloth and weight them for another hour to press out more whey."},
            {"step": 6, "text": "Prepare a brine with 35g salt per liter of water (3.5% salinity)."},
            {"step": 7, "text": "Simmer the pressed curds in the salted brine for one hour."},
            {"step": 8, "text": "Remove from brine and chill overnight in the refrigerator."},
            {"step": 9, "text": "Serve with walnuts, figs, olives, or honey as the Romans did."}
        ],
        "temperature": "212°F (100°C) for initial boil",
        "notes": [
            "Fig-sap rennet was the traditional Roman coagulant - collected from fig branches",
            "Columella wrote 12 books on agriculture including detailed cheese-making instructions",
            "This cheese does not age well - consume within a few days",
            "The Romans often paired fresh cheese with honey, nuts, and dried fruits"
        ],
        "tags": ["cheese", "ancient", "Roman", "historical", "fresh cheese", "fig rennet"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "caseus-fumosus-velabrensis",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Caseus Fumosus Velabrensis (Ancient Roman Smoked Cheese)",
        "category": "sides",
        "attribution": "Ancient Roman tradition",
        "source_note": "Ancient Roman smoked cheese from the Velabrum district of Rome. Reconstructed from historical sources by Tavola Mediterranea.",
        "description": "A smoked cheese from ancient Rome, named after the Velabrum marketplace district where it was sold. The smoking process preserved the cheese and added distinctive flavor prized by Romans.",
        "servings_yield": "About 1 lb",
        "prep_time": "1 hour",
        "cook_time": "10 hours (including smoking)",
        "total_time": "24 hours",
        "ingredients": [
            {"item": "raw goat or cow milk", "quantity": "4", "unit": "liters"},
            {"item": "salt", "quantity": "35+", "unit": "g", "prep_note": "for brine"},
            {"item": "rennet or fig sap", "quantity": "2", "unit": "tbsp"},
            {"item": "applewood chips", "quantity": "2", "unit": "cups", "prep_note": "for smoking"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to boiling while whisking continuously."},
            {"step": 2, "text": "Add rennet or fig sap coagulant and let the curds separate for 30 minutes."},
            {"step": 3, "text": "Transfer curds to cheesecloth and press for 4-8 hours with weights."},
            {"step": 4, "text": "Prepare brine with 35g salt per liter of water."},
            {"step": 5, "text": "Wrap the pressed cheese in cheesecloth and simmer in brine for 1 hour."},
            {"step": 6, "text": "Allow your oven or smoker to cool below 90°F (32°C)."},
            {"step": 7, "text": "Add applewood chips to generate smoke without excessive heat."},
            {"step": 8, "text": "Place cheese on a rack in the smoker and cold smoke for 8-10 hours."},
            {"step": 9, "text": "Rest the cheese for 24 hours before serving to allow smoke flavor to mellow."}
        ],
        "temperature": "Below 90°F (32°C) for smoking",
        "notes": [
            "The Velabrum was a busy marketplace district in ancient Rome",
            "Cold smoking is essential - temperatures above 90°F will melt the cheese",
            "Romans prized smoked cheeses for their extended shelf life",
            "Applewood provides a mild, slightly sweet smoke similar to ancient fruit woods"
        ],
        "tags": ["cheese", "ancient", "Roman", "historical", "smoked", "cold smoked"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "ghost-pepper-camembert",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ghost Pepper Camembert",
        "category": "sides",
        "attribution": "Modern artisan cheesemaking",
        "source_note": "Spicy bloomy rind cheese combining traditional Camembert technique with bhut jolokia (ghost pepper). From The Hot Pepper Forum community.",
        "description": "A fiery twist on classic Camembert, infused with ghost pepper (bhut jolokia) for extreme heat lovers. The creamy, bloomy rind tempers the intense spice.",
        "servings_yield": "Two 4-inch wheels",
        "prep_time": "2 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "white mold culture"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "ghost pepper", "quantity": "1", "unit": "small", "prep_note": "finely chopped, seeds removed for less heat"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "SAFETY: Wear gloves when handling ghost peppers. Their oils cause severe skin and eye irritation."},
            {"step": 2, "text": "Heat milk to 90°F (32°C). Add mesophilic culture and P. candidum, stir gently."},
            {"step": 3, "text": "Add finely chopped ghost pepper to the milk and stir to distribute."},
            {"step": 4, "text": "Ripen for 30 minutes, maintaining temperature."},
            {"step": 5, "text": "Add calcium chloride if using, then rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Let set for 90 minutes until you achieve a clean break."},
            {"step": 7, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 8, "text": "Gently ladle curds into Camembert molds. Do not press - let drain naturally."},
            {"step": 9, "text": "Flip every few hours for 24 hours as cheese drains."},
            {"step": 10, "text": "Unmold and salt all surfaces. Air dry at room temperature for 24 hours."},
            {"step": 11, "text": "Age at 50-55°F (10-13°C) and 90-95% humidity for 4-6 weeks."},
            {"step": 12, "text": "Turn daily for first 2 weeks. White bloom should fully cover by week 2."}
        ],
        "temperature": "90°F (32°C) for make, 50-55°F (10-13°C) for aging",
        "notes": [
            "Ghost peppers are 855,000-1,041,427 Scoville units - extremely hot",
            "Start with half a pepper if unsure of heat tolerance",
            "Bloomy rind cheeses are among the easiest ripened cheeses - no press needed",
            "The creamy paste helps temper the pepper heat somewhat",
            "Refrigerate when ripe to slow further aging"
        ],
        "tags": ["cheese", "Camembert", "ghost pepper", "bhut jolokia", "spicy", "super-hot", "bloomy rind"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "carolina-reaper-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Carolina Reaper Cheddar",
        "category": "sides",
        "attribution": "Modern artisan cheesemaking",
        "source_note": "Extreme heat cheddar using the world's hottest pepper. Adapted from Chili Craze techniques.",
        "description": "For the ultimate heat seekers - a sharp cheddar infused with Carolina Reaper, the world's hottest pepper at 1.4-2.2 million Scoville units. Intense, fruity heat with a delayed burn.",
        "servings_yield": "About 2 lbs",
        "prep_time": "3 hours",
        "cook_time": "3+ months aging",
        "total_time": "3+ months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "Carolina Reaper peppers", "quantity": "2", "unit": "dried", "prep_note": "ground to fine powder"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "CRITICAL SAFETY: Wear gloves, eye protection, and work in ventilated area. Reaper powder is extremely irritating."},
            {"step": 2, "text": "Grind dried Carolina Reapers into fine powder. A dedicated spice grinder is recommended."},
            {"step": 3, "text": "Heat milk to 90°F (32°C). Add mesophilic culture and ripen 45 minutes."},
            {"step": 4, "text": "Add calcium chloride if using, then rennet. Stir gently."},
            {"step": 5, "text": "Let set 45-60 minutes until clean break achieved."},
            {"step": 6, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 7, "text": "Slowly raise temperature to 102°F (39°C) over 30 minutes, stirring gently."},
            {"step": 8, "text": "Maintain 102°F for 30 minutes, stirring every 5 minutes."},
            {"step": 9, "text": "Drain whey. Mill curds into walnut-sized pieces."},
            {"step": 10, "text": "Add salt and Reaper powder to milled curds. Mix thoroughly with gloved hands."},
            {"step": 11, "text": "Pack curds into cheese mold. Press at 10 lbs for 15 minutes."},
            {"step": 12, "text": "Flip, press at 20 lbs for 12 hours. Flip and press another 12 hours."},
            {"step": 13, "text": "Air dry at room temperature for 2-3 days until rind forms."},
            {"step": 14, "text": "Wax or vacuum seal. Age at 55°F (13°C) for minimum 3 months."},
            {"step": 15, "text": "Longer aging (6+ months) allows heat to meld with cheese flavor."}
        ],
        "temperature": "90-102°F (32-39°C) for make, 55°F (13°C) for aging",
        "notes": [
            "Carolina Reaper is 1,400,000-2,200,000 Scoville units - world's hottest pepper",
            "Start with ONE pepper for first batch - you can always add more next time",
            "Aging allows pepper oils to permeate throughout the cheese",
            "The delayed heat of Reapers intensifies over 30+ seconds",
            "Pair with crackers and cold beer - dairy helps with capsaicin burn"
        ],
        "tags": ["cheese", "cheddar", "Carolina Reaper", "spicy", "super-hot", "extreme heat", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "chipotle-infused-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chipotle-Infused Farmhouse Cheese",
        "category": "sides",
        "attribution": "Little Green Cheese",
        "source_note": "Smoky-spicy cheese using chipotle peppers (smoked jalapeños). From Little Green Cheese herb and spice techniques.",
        "description": "A medium-aged farmhouse cheese infused with chipotle peppers, providing both smokiness and moderate heat in one ingredient. Perfect balance of smoke and spice.",
        "servings_yield": "About 2 lbs",
        "prep_time": "2 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "not ultra-pasteurized"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "chipotle flakes", "quantity": "1", "unit": "tbsp"},
            {"item": "water", "quantity": "1/2", "unit": "cup", "prep_note": "for steeping chipotles"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Simmer chipotle flakes in 1/2 cup water for 15 minutes to rehydrate and release oils."},
            {"step": 2, "text": "Strain and reserve both the liquid and the softened flakes. Cool to room temperature."},
            {"step": 3, "text": "Heat milk to 90°F (32°C). Add the cooled chipotle liquid and stir."},
            {"step": 4, "text": "Add mesophilic culture and ripen for 45 minutes."},
            {"step": 5, "text": "Add calcium chloride if using, then rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Let set 45-60 minutes until clean break."},
            {"step": 7, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 8, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes, stirring gently."},
            {"step": 9, "text": "Maintain temperature for 30 minutes, stirring regularly."},
            {"step": 10, "text": "Drain whey. Add salt and reserved chipotle flakes to curds. Mix well."},
            {"step": 11, "text": "Pack into mold. Press at 10 lbs for 15 minutes."},
            {"step": 12, "text": "Flip and press at 20 lbs for 12 hours."},
            {"step": 13, "text": "Air dry for 2-3 days. Wax or vacuum seal."},
            {"step": 14, "text": "Age at 55°F (13°C) for 2-3 months. Smoke flavor melds beautifully with aging."}
        ],
        "temperature": "90-100°F (32-38°C) for make, 55°F (13°C) for aging",
        "notes": [
            "Chipotles are smoked jalapeños - they provide both smoke and heat",
            "Heat level is moderate (2,500-8,000 Scoville) compared to habanero or ghost pepper",
            "Steeping extracts oils for even distribution throughout the cheese",
            "Can increase to 2 tbsp chipotle for more intense flavor",
            "Pairs excellently with Mexican dishes and grilled meats"
        ],
        "tags": ["cheese", "chipotle", "smoked", "spicy", "farmhouse", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]

# Check for duplicates
existing_ids = {r['id'] for r in data['recipes']}
recipes_to_add = [r for r in new_recipes if r['id'] not in existing_ids]
skipped = [r['id'] for r in new_recipes if r['id'] in existing_ids]

if skipped:
    print(f"Skipping {len(skipped)} duplicate(s): {skipped}")

# Add new recipes
data['recipes'].extend(recipes_to_add)
print(f"Added {len(recipes_to_add)} new recipes")

# Save
with open('data/recipes.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Total recipes now: {len(data['recipes'])}")
