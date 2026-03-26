#!/usr/bin/env python3
"""Add traditional cheese making recipes to the database (batch 14) - European soft cheeses and more heritage recipes."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-camembert",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Camembert",
        "category": "mains",
        "attribution": "French / Marie Harel (1791)",
        "source_note": "Camembert was created in 1791 by Marie Harel in Normandy, France, reportedly with advice from a priest she sheltered during the French Revolution. The small round wooden box became iconic. A bloomy rind cheese that ripens from the outside in.",
        "description": "The famous soft French cheese with a bloomy white rind and creamy interior. Created in Normandy in 1791, it ripens in just 4-6 weeks. The white Penicillium candidum mold creates the edible rind and transforms the interior to a luscious paste.",
        "servings_yield": "2 small wheels (about 8 oz each)",
        "prep_time": "3 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "optional, for richer cheese"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "white mold powder"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk (and cream if using) to 90°F (32°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Stir well."},
            {"step": 3, "text": "Sprinkle mesophilic culture and Penicillium candidum over surface. Wait 2 minutes to rehydrate, then stir gently."},
            {"step": 4, "text": "Cover and ripen for 90 minutes at 90°F."},
            {"step": 5, "text": "Add diluted rennet, stirring gently in up-and-down motions for 30 strokes."},
            {"step": 6, "text": "Cover and let set for 60-90 minutes until curd gives a clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes."},
            {"step": 8, "text": "Let curds rest for 15 minutes."},
            {"step": 9, "text": "Gently ladle curds into Camembert molds (4-inch diameter). Do not press - let gravity drain."},
            {"step": 10, "text": "Let drain at room temperature (72°F) for 24 hours, flipping every 4-6 hours."},
            {"step": 11, "text": "Remove from molds. Salt all surfaces lightly."},
            {"step": 12, "text": "Place on a drying mat in a well-ventilated area for 1-2 days until surface is dry to touch."},
            {"step": 13, "text": "Move to aging environment: 50-55°F, 85-90% humidity."},
            {"step": 14, "text": "Flip daily. White mold should appear in 5-7 days."},
            {"step": 15, "text": "When fully covered in white mold (10-14 days), wrap in cheese paper."},
            {"step": 16, "text": "Continue aging until cheese feels soft when gently pressed, about 4-6 weeks total."}
        ],
        "temperature": "90°F make, 50-55°F aging",
        "notes": [
            "Created by Marie Harel in Normandy, France, in 1791",
            "The white bloomy rind is edible Penicillium candidum mold",
            "Ripe when it feels like the soft flesh between thumb and index finger",
            "Younger cheese is firmer and milder; aged cheese is runnier and stronger",
            "The wooden box was invented in 1890 for shipping",
            "Humidity control is critical - too dry and rind won't develop"
        ],
        "tags": ["cheese", "Camembert", "French", "soft cheese", "bloomy rind", "Penicillium", "Normandy", "1791"],
        "confidence": {"overall": "high", "flags": ["Requires aging environment with humidity control"]},
        "image_refs": []
    },
    {
        "id": "traditional-brie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Brie",
        "category": "mains",
        "attribution": "French / Île-de-France (7th-8th Century)",
        "source_note": "Brie dates back to the 7th-8th centuries near Paris. Often called 'The King of Cheeses,' it was reportedly Charlemagne's favorite. Larger and flatter than Camembert, with a milder, buttery flavor.",
        "description": "The 'King of Cheeses' dating back 1,200+ years to the Île-de-France region. Larger and milder than Camembert, with a luxuriously creamy interior beneath its white bloomy rind. Charlemagne himself reportedly loved this cheese.",
        "servings_yield": "1 wheel (about 2 lbs)",
        "prep_time": "3 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "3", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "2", "unit": "cups", "prep_note": "for double cream Brie"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/8", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "optional, for wrinkled rind"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk and cream to 90°F (32°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture, P. candidum, and Geotrichum (if using) over surface. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 90 minutes at 90°F."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 90 minutes until firm curd with clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 8, "text": "Gently stir curds for 20 minutes at 90°F."},
            {"step": 9, "text": "Ladle curds into large Brie mold (8-10 inch diameter). Do not press."},
            {"step": 10, "text": "Drain at room temperature for 24-48 hours, flipping every 6-8 hours."},
            {"step": 11, "text": "Remove from mold. Salt top and sides, flip, salt bottom."},
            {"step": 12, "text": "Air dry 2-3 days at 60-65°F until surface is dry."},
            {"step": 13, "text": "Move to aging at 50-55°F, 90% humidity."},
            {"step": 14, "text": "Turn daily. White mold appears in 7-10 days."},
            {"step": 15, "text": "When fully covered (2-3 weeks), wrap in cheese paper."},
            {"step": 16, "text": "Age 6-8 weeks total until center is soft and creamy."}
        ],
        "temperature": "90°F make, 50-55°F aging",
        "notes": [
            "Dating to the 7th-8th centuries, one of the world's oldest cheeses",
            "Charlemagne reportedly discovered Brie in 774 AD and loved it",
            "Larger and flatter than Camembert, with a milder flavor",
            "Adding cream creates 'double cream' or 'triple cream' Brie",
            "The rind should be white and velvety, not gray or slimy",
            "Ready when the center yields to gentle pressure"
        ],
        "tags": ["cheese", "Brie", "French", "soft cheese", "bloomy rind", "King of Cheeses", "medieval"],
        "confidence": {"overall": "high", "flags": ["Requires aging environment with humidity control"]},
        "image_refs": []
    },
    {
        "id": "creole-cream-cheese-1901",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Creole Cream Cheese (1901 New Orleans)",
        "category": "mains",
        "attribution": "New Orleans Creole / The Picayune's Creole Cook Book (1901)",
        "source_note": "From 'The Picayune's Creole Cook Book' (1901): 'Cream cheese is always made from clabbered milk.' Traditional New Orleans cream cheese was made from naturally clabbered raw milk, drained in muslin bags hung from tree limbs overnight.",
        "description": "The original New Orleans cream cheese from 1901 - made from naturally clabbered milk, drained overnight in muslin bags. A tangy, fresh cheese served with sweet cream poured over. A treasured Creole tradition nearly lost to history.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "15 min (plus 24-48 hours clabbering)",
        "cook_time": "12 hours draining",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "raw milk traditional, or use cultured"},
            {"item": "buttermilk", "quantity": "1/2", "unit": "cup", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops", "prep_note": "diluted in 2 tbsp water"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "for serving"}
        ],
        "instructions": [
            {"step": 1, "text": "TRADITIONAL METHOD (raw milk): Let raw milk sit at room temperature 24-48 hours until naturally clabbered (thickened like yogurt)."},
            {"step": 2, "text": "MODERN METHOD: Heat pasteurized milk to 72°F. Stir in buttermilk and diluted rennet."},
            {"step": 3, "text": "Cover and let sit at room temperature for 12-24 hours until a soft curd forms."},
            {"step": 4, "text": "Line a colander with butter muslin or a clean flour sack towel."},
            {"step": 5, "text": "Gently pour clabbered milk into the cloth."},
            {"step": 6, "text": "Gather corners of cloth and tie into a bag."},
            {"step": 7, "text": "Hang the bag to drain overnight (traditionally from a tree limb or porch hook in a cool place)."},
            {"step": 8, "text": "When curds stop dripping and reach desired consistency (8-12 hours), remove from bag."},
            {"step": 9, "text": "Beat the cheese until light and smooth."},
            {"step": 10, "text": "Pack into small molds or ramekins."},
            {"step": 11, "text": "To serve: Unmold onto a dish and pour sweet cream over the top."},
            {"step": 12, "text": "Traditionally eaten for breakfast with fruit or sugar."}
        ],
        "temperature": "Room temperature (68-72°F)",
        "notes": [
            "From 'The Picayune's Creole Cook Book' published in 1901",
            "Traditional method used raw milk that clabbered naturally",
            "The cloth bag was hung from tree limbs overnight to drain",
            "Served with sweet cream poured over - a New Orleans breakfast tradition",
            "Nearly disappeared until local dairies revived it in the 2000s",
            "The tangy-sweet combination is uniquely Creole"
        ],
        "tags": ["cheese", "cream cheese", "Creole", "New Orleans", "1901", "clabber", "traditional", "Louisiana"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-neufchatel",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Neufchâtel",
        "category": "mains",
        "attribution": "French / Normandy (1035 AD)",
        "source_note": "One of France's oldest cheeses, dating to 1035 AD in Normandy. The heart shape was traditionally made by young women for their suitors. American 'Neufchatel' is different - the French original has a bloomy rind.",
        "description": "One of France's oldest cheeses, documented since 1035 AD. This Normandy cheese has a white bloomy rind and soft, slightly grainy interior. Traditionally molded into heart shapes by young women for their sweethearts.",
        "servings_yield": "4-6 small hearts or 2 rounds",
        "prep_time": "2 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C) - cooler than most cheeses."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture and P. candidum over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 5, "text": "Cover and let set at room temperature for 18-24 hours until curd is firm."},
            {"step": 6, "text": "The long set time develops the characteristic slightly grainy texture."},
            {"step": 7, "text": "Ladle curds into cheesecloth-lined molds (heart-shaped is traditional)."},
            {"step": 8, "text": "Drain for 12-24 hours at room temperature, flipping once."},
            {"step": 9, "text": "Remove from molds. Salt all surfaces."},
            {"step": 10, "text": "Air dry 1-2 days at 60°F until surface is dry."},
            {"step": 11, "text": "Age at 50-55°F, 85% humidity for 2-4 weeks."},
            {"step": 12, "text": "White mold should cover surface. Cheese is ready when slightly soft."}
        ],
        "temperature": "72°F make, 50-55°F aging",
        "notes": [
            "Documented since 1035 AD - one of France's oldest cheeses",
            "Young women traditionally made heart-shaped cheeses for suitors",
            "The long 18-24 hour set creates the characteristic texture",
            "French Neufchâtel has a bloomy rind - different from American 'Neufchatel'",
            "American Neufchatel is an unaged cream cheese without the rind",
            "This is what cream cheese evolved from in America"
        ],
        "tags": ["cheese", "Neufchatel", "French", "Normandy", "1035", "heart-shaped", "bloomy rind", "medieval"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-labneh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Labneh (Middle Eastern Yogurt Cheese)",
        "category": "mains",
        "attribution": "Traditional Middle Eastern / Levantine",
        "source_note": "Labneh (also labne, labni, or lebni) has been made throughout the Middle East and Mediterranean for thousands of years. Simply strained yogurt transformed into a creamy, tangy cheese. Essential in Lebanese, Syrian, and Palestinian cuisines.",
        "description": "The simplest cheese - just strained yogurt. Made throughout the Middle East for millennia, labneh is creamy, tangy, and infinitely versatile. Serve drizzled with olive oil and za'atar, or roll into balls and preserve in oil.",
        "servings_yield": "About 2 cups labneh from 4 cups yogurt",
        "prep_time": "5 min",
        "cook_time": "12-24 hours straining",
        "total_time": "12-24 hours",
        "ingredients": [
            {"item": "full-fat plain yogurt", "quantity": "4", "unit": "cups", "prep_note": "no gelatin or thickeners"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for serving"},
            {"item": "za'atar", "quantity": "1", "unit": "tsp", "prep_note": "for serving, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Stir salt into yogurt until combined."},
            {"step": 2, "text": "Line a fine-mesh strainer with cheesecloth or a clean kitchen towel."},
            {"step": 3, "text": "Set strainer over a deep bowl to catch the whey."},
            {"step": 4, "text": "Spoon yogurt into the lined strainer."},
            {"step": 5, "text": "Cover loosely and refrigerate."},
            {"step": 6, "text": "For spreadable labneh: strain 12-18 hours."},
            {"step": 7, "text": "For thick labneh (ball-forming consistency): strain 24-48 hours."},
            {"step": 8, "text": "Transfer strained labneh to a container."},
            {"step": 9, "text": "To serve: Spread on a plate, drizzle with olive oil, sprinkle with za'atar."},
            {"step": 10, "text": "For preserved labneh balls: Roll thick labneh into 1-inch balls, place in jar, cover with olive oil."}
        ],
        "temperature": "Refrigerator temperature",
        "notes": [
            "Made throughout the Middle East for thousands of years",
            "Use full-fat yogurt without gelatin or thickeners",
            "Greek yogurt is already strained - use regular yogurt for best results",
            "The whey can be used in baking or smoothies",
            "Preserved in olive oil, labneh balls keep for months",
            "Essential in Lebanese, Syrian, Palestinian, and Jordanian cuisines"
        ],
        "tags": ["cheese", "labneh", "yogurt cheese", "Middle Eastern", "Lebanese", "strained yogurt", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-feta-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Greek Feta Cheese",
        "category": "mains",
        "attribution": "Greek / Ancient Mediterranean",
        "source_note": "Feta is mentioned in Homer's Odyssey (8th century BC) when Cyclops Polyphemus made cheese from sheep's milk. True feta is brined white cheese from Greece, traditionally made with sheep's milk or a sheep-goat blend.",
        "description": "The ancient Greek cheese mentioned in Homer's Odyssey. Tangy, crumbly, and brined for preservation. Traditional feta uses sheep's milk (or sheep-goat blend) and ages in brine for at least 2 months. A 3,000+ year-old recipe.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "3 hours",
        "cook_time": "2+ months brining",
        "total_time": "2+ months",
        "ingredients": [
            {"item": "sheep's milk or goat's milk", "quantity": "1", "unit": "gallon", "prep_note": "or cow's milk"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/8", "unit": "tsp", "prep_note": "optional, for tangier flavor"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1/4", "unit": "cup", "prep_note": "for dry salting"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "cup", "prep_note": "per quart water for brine"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture (and lipase if using) over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 60 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 45-60 minutes until clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 8, "text": "Gently stir curds for 20 minutes."},
            {"step": 9, "text": "Let curds settle 5 minutes. Drain off whey."},
            {"step": 10, "text": "Ladle curds into a cheesecloth-lined mold. Let drain 4-6 hours, flipping once."},
            {"step": 11, "text": "Remove from mold. Cut into 2-3 inch blocks."},
            {"step": 12, "text": "Salt all surfaces of blocks. Let drain on a rack 2-3 days, flipping and re-salting daily."},
            {"step": 13, "text": "Make brine: Dissolve 1/2 cup salt per quart of water."},
            {"step": 14, "text": "Place salted blocks in brine. Refrigerate for at least 2 months."},
            {"step": 15, "text": "Feta keeps in brine for up to a year."}
        ],
        "temperature": "86°F (30°C) for make",
        "notes": [
            "Mentioned in Homer's Odyssey (8th century BC)",
            "True Greek feta is made from sheep's milk or sheep-goat blend",
            "EU law protects 'feta' designation for Greek cheese only",
            "Lipase adds the characteristic tangy 'sheepy' flavor",
            "Must be brined for at least 2 months by Greek standards",
            "The brine preserves the cheese for up to a year"
        ],
        "tags": ["cheese", "feta", "Greek", "brined", "sheep milk", "ancient", "Homer", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-manchego",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Spanish Manchego",
        "category": "mains",
        "attribution": "Spanish / La Mancha (Ancient)",
        "source_note": "Manchego comes from Spain's La Mancha region, made exclusively from Manchega sheep's milk. Archaeological evidence shows cheese making here since the Bronze Age. The distinctive crosshatch pattern comes from traditional esparto grass molds.",
        "description": "Spain's most famous cheese, from the land of Don Quixote. Made from Manchega sheep's milk with a distinctive crosshatch rind pattern. Nutty, buttery, and slightly tangy. Traditionally aged 2 months to 2 years.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "4 hours",
        "cook_time": "2-12 months aging",
        "total_time": "2-12 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "cow's milk can substitute"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp", "prep_note": "for rind, traditional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle thermophilic culture over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 45 minutes."},
            {"step": 5, "text": "Raise temperature to 90°F. Add diluted rennet. Stir 1 minute."},
            {"step": 6, "text": "Cover and let set for 30-45 minutes until firm clean break."},
            {"step": 7, "text": "Cut curd into 1/4-inch cubes (small for Manchego)."},
            {"step": 8, "text": "Slowly raise temperature to 104°F over 30 minutes, stirring gently."},
            {"step": 9, "text": "Hold at 104°F for 30 minutes, stirring. Curds should be firm."},
            {"step": 10, "text": "Drain whey. Pack curds firmly into a traditional Manchego mold with crosshatch pattern (or use a basket weave mat)."},
            {"step": 11, "text": "Press at 10 lbs for 30 min, 25 lbs for 2 hours, 50 lbs overnight."},
            {"step": 12, "text": "Remove from mold. Float in saturated brine for 12 hours per pound."},
            {"step": 13, "text": "Air dry 2-3 days at 55°F until rind forms."},
            {"step": 14, "text": "Rub rind with olive oil (traditional) or wax."},
            {"step": 15, "text": "Age at 55°F, 85% humidity: 2 months (semi-curado), 6 months (curado), 12+ months (viejo)."}
        ],
        "temperature": "86-104°F make, 55°F aging",
        "notes": [
            "From La Mancha, Spain - Don Quixote's homeland",
            "Traditional Manchego uses only Manchega sheep's milk",
            "The crosshatch pattern is from esparto grass molds",
            "Bronze Age archaeological evidence of cheese making in this region",
            "Aging classifications: fresco (fresh), semi-curado (2 mo), curado (6 mo), viejo (12+ mo)",
            "Traditionally rubbed with olive oil, not waxed"
        ],
        "tags": ["cheese", "Manchego", "Spanish", "sheep milk", "aged", "La Mancha", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-limburger",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Limburger Cheese",
        "category": "mains",
        "attribution": "Belgian/German / Limburg Region (19th Century)",
        "source_note": "Limburger originated in the Duchy of Limburg (now Belgium/Netherlands/Germany) and became famous in 19th century America via German immigrants. Its strong smell comes from Brevibacterium linens - the same bacteria on human skin.",
        "description": "The famously pungent washed-rind cheese beloved by German immigrants. The strong smell comes from the same bacteria found on human skin. Despite the aroma, the flavor is surprisingly mild and creamy. An acquired taste and a cultural icon.",
        "servings_yield": "About 1 lb",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "red/orange rind bacteria"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": "for brine wash"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 30 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 30-45 minutes until clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 8, "text": "Gently stir curds for 15 minutes at 90°F."},
            {"step": 9, "text": "Drain whey. Ladle curds into rectangular Limburger molds."},
            {"step": 10, "text": "Let drain 24 hours at room temperature, flipping every 4-6 hours."},
            {"step": 11, "text": "Remove from mold. Salt all surfaces. Let rest 2 days at 60°F."},
            {"step": 12, "text": "Make brine wash: 1 tbsp salt in 1 cup water, add pinch of B. linens."},
            {"step": 13, "text": "Wash cheese with brine solution every 2-3 days."},
            {"step": 14, "text": "Age at 55-60°F, 90%+ humidity for 2-3 months."},
            {"step": 15, "text": "The rind will turn orange-red and develop the characteristic smell."},
            {"step": 16, "text": "Ready when rind is fully developed and interior is soft."}
        ],
        "temperature": "90°F make, 55-60°F aging",
        "notes": [
            "The smell comes from Brevibacterium linens - same bacteria on human feet",
            "The flavor is much milder than the smell suggests",
            "German immigrants made it famous in Wisconsin in the 1800s",
            "Traditionally eaten on rye bread with raw onion",
            "Monroe, Wisconsin was once the 'Limburger Capital of America'",
            "Requires high humidity aging - a 'smear-ripened' or 'washed-rind' cheese"
        ],
        "tags": ["cheese", "Limburger", "German", "Belgian", "washed rind", "pungent", "traditional", "Wisconsin"],
        "confidence": {"overall": "high", "flags": ["Strong smell - age in well-ventilated area away from other foods"]},
        "image_refs": []
    }
]

def main():
    # Load existing recipes
    with open(RECIPES_FILE, 'r') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}

    # Add new recipes
    added = 0
    skipped = 0
    for recipe in new_recipes:
        if recipe['id'] not in existing_ids:
            data['recipes'].append(recipe)
            added += 1
            print(f"Added: {recipe['title']}")
        else:
            skipped += 1
            print(f"Skipped (exists): {recipe['title']}")

    # Update metadata
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = str(date.today())

    # Save
    with open(RECIPES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone! Added {added} recipes, skipped {skipped}")
    print(f"Total recipes: {data['meta']['total_count']}")

if __name__ == "__main__":
    main()
