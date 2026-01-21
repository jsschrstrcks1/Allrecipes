#!/usr/bin/env python3
"""Add traditional cheese making recipes to the database (batch 13) - heritage and old-world cheese methods."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-clabber-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Clabber Cheese (Grandmother's Method)",
        "category": "mains",
        "attribution": "Traditional Farmhouse / Pre-1900s Method",
        "source_note": "The original way cheese was made before commercial cultures existed. Raw milk is allowed to naturally sour (clabber) using wild bacteria, then gently heated to form curds. Grandmothers kept a jar of clabber on the counter for generations.",
        "description": "The oldest method of cheese making - letting raw milk naturally sour and thicken with wild bacteria, then gently heating to form soft curds. This is how your great-grandmother made cottage cheese, long before store-bought cultures existed.",
        "servings_yield": "About 1 quart cheese from 1 gallon milk",
        "prep_time": "10 min active (2-3 days fermentation)",
        "cook_time": "30 min",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw milk", "quantity": "1", "unit": "gallon", "prep_note": "must be raw, not pasteurized"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "to taste"},
            {"item": "heavy cream", "quantity": "2-4", "unit": "tbsp", "prep_note": "optional, for creaming"}
        ],
        "instructions": [
            {"step": 1, "text": "TO START CLABBER: Pour raw milk into a clean glass jar. Cover loosely with cloth and rubber band."},
            {"step": 2, "text": "Let sit at room temperature (68-72°F) for 2-3 days until milk thickens and solidifies like yogurt."},
            {"step": 3, "text": "The clabber is ready when it pulls away from the jar sides and has a pleasant sour smell."},
            {"step": 4, "text": "TO MAKE CHEESE: Pour clabbered milk into a large pot."},
            {"step": 5, "text": "Heat VERY slowly over low heat, stirring gently, until temperature reaches 100-110°F."},
            {"step": 6, "text": "Do NOT exceed 110°F or the curds will become rubbery and beneficial bacteria will die."},
            {"step": 7, "text": "When curds separate clearly from the yellowish whey, remove from heat."},
            {"step": 8, "text": "Line a colander with butter muslin or cheesecloth. Pour in curds and whey."},
            {"step": 9, "text": "Let drain for 1-2 hours, or hang the cloth to drip until desired consistency."},
            {"step": 10, "text": "Transfer curds to a bowl. Add salt to taste."},
            {"step": 11, "text": "For creamed cottage cheese, stir in heavy cream."},
            {"step": 12, "text": "Refrigerate and use within 1 week."}
        ],
        "temperature": "100-110°F (38-43°C) - do not exceed",
        "notes": [
            "MUST use raw milk - pasteurized milk will spoil, not clabber",
            "Clabber was kept on grandmother's counter and used like sourdough starter",
            "Save 1/2 cup of clabber to start your next batch (like a starter)",
            "This is how cottage cheese was made for centuries before commercial cultures",
            "The slow, low heat is critical - too hot makes rubbery cheese",
            "Learned from Amish and old farmhouse traditions"
        ],
        "tags": ["cheese", "clabber", "raw milk", "cottage cheese", "traditional", "grandmother", "farmhouse", "fermented"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "pennsylvania-dutch-cup-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pennsylvania Dutch Cup Cheese",
        "category": "mains",
        "attribution": "Amish & Mennonite / Pre-Revolutionary America",
        "source_note": "A traditional Pennsylvania Dutch cheese made by Amish and Mennonites since before the American Revolution. Named because it was traditionally molded in cups. A mild, spreadable cheese that's a Lancaster County staple.",
        "description": "A traditional Amish cheese dating back to pre-Revolutionary America. Mild curds are pressed into cups, creating a spreadable cheese perfect on bread or crackers. A Lancaster County, Pennsylvania, heritage recipe.",
        "servings_yield": "About 1 lb cheese",
        "prep_time": "30 min",
        "cook_time": "12 hours setting + 12 hours draining",
        "total_time": "24+ hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "cultured buttermilk", "quantity": "1/2", "unit": "cup"},
            {"item": "liquid rennet", "quantity": "1", "unit": "drop", "prep_note": "diluted in 1/4 cup cool water"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "baking soda", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for smoothness"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to 72°F (room temperature)."},
            {"step": 2, "text": "Stir in buttermilk thoroughly."},
            {"step": 3, "text": "Add diluted rennet and stir gently for 1 minute."},
            {"step": 4, "text": "Cover pot and let stand at room temperature for 12 hours or until a soft curd forms."},
            {"step": 5, "text": "Cut the curd into 1/2-inch cubes using a long knife."},
            {"step": 6, "text": "Let curds rest for 10 minutes."},
            {"step": 7, "text": "Slowly warm curds to 115°F, stirring very gently."},
            {"step": 8, "text": "Ladle warm curds into a cheesecloth-lined colander."},
            {"step": 9, "text": "Allow to drain for 12 hours or overnight."},
            {"step": 10, "text": "Transfer drained curds to a bowl. Work in salt (and baking soda if using)."},
            {"step": 11, "text": "Pack firmly into small cups or molds."},
            {"step": 12, "text": "Refrigerate for at least 24 hours before eating. Keeps 2 weeks refrigerated."}
        ],
        "temperature": "72°F initial, warm to 115°F",
        "notes": [
            "Traditional Amish and Mennonite recipe from before the American Revolution",
            "Named 'cup cheese' because it was molded in cups",
            "The baking soda makes a smoother, spreadable texture",
            "A Lancaster County, Pennsylvania, heritage food",
            "Mild flavor - meant to be eaten fresh, not aged",
            "Traditionally served on bread with apple butter"
        ],
        "tags": ["cheese", "cup cheese", "Pennsylvania Dutch", "Amish", "Mennonite", "traditional", "Lancaster County"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-blanco",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Blanco (Traditional Latin White Cheese)",
        "category": "mains",
        "attribution": "Traditional Latin American / Mexican",
        "source_note": "Queso Blanco means 'white cheese' in Spanish. This is the simplest acid-set cheese, made throughout Latin America for centuries. Uses vinegar or lemon juice to curdle milk - no special cultures or rennet needed.",
        "description": "The simplest cheese you can make - just milk and acid. Heat milk, add vinegar, and curds form instantly. A fresh, mild cheese used throughout Mexico and Latin America for generations. Ready in 30 minutes.",
        "servings_yield": "About 10-12 oz cheese from 1 gallon milk",
        "prep_time": "5 min",
        "cook_time": "25 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "not ultra-pasteurized"},
            {"item": "white vinegar", "quantity": "1/4", "unit": "cup", "prep_note": "or lemon/lime juice"},
            {"item": "salt", "quantity": "1", "unit": "tsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour milk into a large heavy-bottomed pot."},
            {"step": 2, "text": "Heat slowly over medium heat, stirring occasionally, until it reaches 185-190°F."},
            {"step": 3, "text": "Remove from heat."},
            {"step": 4, "text": "Slowly stir in vinegar, one tablespoon at a time."},
            {"step": 5, "text": "Curds will begin to form and separate from the yellowish whey almost immediately."},
            {"step": 6, "text": "Let sit undisturbed for 10-15 minutes."},
            {"step": 7, "text": "Line a colander with butter muslin or several layers of cheesecloth."},
            {"step": 8, "text": "Gently pour curds and whey into the lined colander."},
            {"step": 9, "text": "Let drain for 15-30 minutes, or until desired moisture level."},
            {"step": 10, "text": "Transfer curds to a bowl. Mix in salt."},
            {"step": 11, "text": "Use immediately or press into a form. Refrigerate up to 1 week."}
        ],
        "temperature": "185-190°F (85-88°C)",
        "notes": [
            "The simplest cheese - no cultures or rennet needed",
            "Do NOT use ultra-pasteurized milk - it won't form proper curds",
            "Lemon or lime juice gives a slightly different flavor than vinegar",
            "This cheese does NOT melt - it softens but holds its shape",
            "Perfect crumbled over tacos, enchiladas, beans, and salads",
            "Traditional throughout Mexico and Central/South America"
        ],
        "tags": ["cheese", "queso blanco", "Mexican", "Latin American", "fresh cheese", "acid-set", "beginner"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-queso-fresco",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Fresco (Mexican Fresh Cheese with Rennet)",
        "category": "mains",
        "attribution": "Traditional Mexican",
        "source_note": "Queso Fresco means 'fresh cheese' in Spanish. Unlike acid-set Queso Blanco, traditional Queso Fresco uses rennet for a slightly different texture. A staple of Mexican cuisine for centuries.",
        "description": "The traditional Mexican fresh cheese made with rennet rather than acid. Slightly firmer and less tangy than Queso Blanco, it crumbles beautifully over hot dishes without melting. Essential for authentic Mexican cooking.",
        "servings_yield": "About 1 lb cheese from 1 gallon milk",
        "prep_time": "15 min",
        "cook_time": "2 hours",
        "total_time": "2-3 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp", "prep_note": "or 2 tbsp plain yogurt"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup cool water"},
            {"item": "salt", "quantity": "1", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, if using pasteurized milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "If using pasteurized milk, add calcium chloride and stir."},
            {"step": 3, "text": "Sprinkle culture over milk surface. Let rehydrate 2 minutes, then stir in."},
            {"step": 4, "text": "Cover and let ripen for 30-45 minutes at 90°F."},
            {"step": 5, "text": "Add diluted rennet, stirring gently in up-and-down motions for 1 minute."},
            {"step": 6, "text": "Cover and let set for 45-60 minutes until curd gives a clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes."},
            {"step": 8, "text": "Let curds rest for 5 minutes."},
            {"step": 9, "text": "Gently stir curds for 30 minutes, maintaining 90°F."},
            {"step": 10, "text": "Line a colander with cheesecloth. Ladle curds into cloth."},
            {"step": 11, "text": "Sprinkle salt over curds and mix gently."},
            {"step": 12, "text": "Drain for 30 minutes to 2 hours depending on desired firmness."},
            {"step": 13, "text": "Press lightly in a mold if desired. Refrigerate and use within 2 weeks."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Traditional Queso Fresco uses rennet, unlike acid-set Queso Blanco",
            "Does not melt - softens and becomes creamy but holds shape",
            "Essential for tacos, enchiladas, elote, tostadas",
            "Can substitute 2 tbsp plain yogurt for mesophilic culture",
            "Calcium chloride helps pasteurized milk form better curds",
            "Best eaten within 1-2 weeks - this is a fresh cheese"
        ],
        "tags": ["cheese", "queso fresco", "Mexican", "fresh cheese", "rennet", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "amish-buttermilk-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Amish Buttermilk Cheese",
        "category": "mains",
        "attribution": "Traditional Amish",
        "source_note": "A simple Amish cheese made from cultured buttermilk. The baking soda creates a smooth, spreadable texture similar to cream cheese. A thrifty way to use up buttermilk and make cheese without rennet.",
        "description": "A creamy, spreadable cheese made simply from buttermilk - no rennet needed. The Amish trick of adding baking soda creates an incredibly smooth texture. Ready in under an hour with just two ingredients.",
        "servings_yield": "About 8 oz cheese from 1 quart buttermilk",
        "prep_time": "5 min",
        "cook_time": "30 min",
        "total_time": "35 min (plus draining)",
        "ingredients": [
            {"item": "cultured buttermilk", "quantity": "1", "unit": "quart", "prep_note": "full-fat preferred"},
            {"item": "baking soda", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": "to taste"},
            {"item": "herbs", "quantity": "", "unit": "", "prep_note": "optional: chives, dill, garlic"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour buttermilk into a heavy-bottomed pot."},
            {"step": 2, "text": "Heat slowly over medium-low heat (about 2°F per minute)."},
            {"step": 3, "text": "Stir gently and occasionally - don't stir too much."},
            {"step": 4, "text": "Continue heating until temperature reaches 160°F."},
            {"step": 5, "text": "The buttermilk will separate into curds and whey."},
            {"step": 6, "text": "Remove from heat when you see clear separation."},
            {"step": 7, "text": "Line a colander with butter muslin. Pour in curds and whey."},
            {"step": 8, "text": "Let drain until curds stop dripping, about 30 minutes to 1 hour."},
            {"step": 9, "text": "Transfer curds to a bowl."},
            {"step": 10, "text": "Work in the baking soda with a fork. Let sit 10 minutes."},
            {"step": 11, "text": "Add salt and any desired herbs. Mix well."},
            {"step": 12, "text": "Refrigerate in an airtight container for up to 2 weeks."}
        ],
        "temperature": "160°F (71°C)",
        "notes": [
            "The baking soda creates the smooth, spreadable texture",
            "Use full-fat cultured buttermilk for best results",
            "No rennet needed - the acid in buttermilk curdles naturally",
            "Add chives and garlic for an herb cheese spread",
            "Traditional Amish thrift - uses up buttermilk",
            "Texture is similar to cream cheese when done right"
        ],
        "tags": ["cheese", "buttermilk", "Amish", "spread", "no rennet", "traditional", "easy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-stilton-blue-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional English Stilton Blue Cheese",
        "category": "mains",
        "attribution": "English / 18th Century Midlands",
        "source_note": "Stilton has been made in the English Midlands since the early 1700s. This 'King of English Cheeses' requires Penicillium roqueforti mold and careful aging. A challenging but rewarding project for experienced cheese makers.",
        "description": "The 'King of English Cheeses' - a creamy, crumbly blue cheese with characteristic blue-green veining. Dating to the 1700s, Stilton requires mold culture and careful aging. An advanced cheese making project.",
        "servings_yield": "About 2-3 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "12+ weeks aging",
        "total_time": "3+ months",
        "ingredients": [
            {"item": "whole milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic culture (MM100 or similar)", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/16", "unit": "tsp", "prep_note": "blue mold culture"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Rehydrate Penicillium roqueforti in 1/4 cup cool water 2 hours before starting."},
            {"step": 2, "text": "Heat milk to 86°F (30°C)."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk. Stir well."},
            {"step": 4, "text": "Sprinkle mesophilic culture over milk. Let rehydrate 2 minutes, then stir."},
            {"step": 5, "text": "Add rehydrated P. roqueforti. Stir gently."},
            {"step": 6, "text": "Cover and ripen for 60-90 minutes at 86°F."},
            {"step": 7, "text": "Add diluted rennet, stirring gently for 1 minute."},
            {"step": 8, "text": "Cover and let set for 90 minutes until firm curd forms with clean break."},
            {"step": 9, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 10, "text": "Gently stir curds for 30 minutes, maintaining 86°F."},
            {"step": 11, "text": "Line a tall Stilton mold with cheesecloth. Ladle curds loosely into mold."},
            {"step": 12, "text": "Let drain at 70°F, turning every few hours for 3-5 days."},
            {"step": 13, "text": "Remove from mold. Rub with salt. Wrap in cloth for 5 more days at 70°F."},
            {"step": 14, "text": "Move to aging cave at 54-60°F, 85% humidity."},
            {"step": 15, "text": "At 5 weeks, pierce cheese with stainless steel needle (40+ holes) to allow air for blue mold."},
            {"step": 16, "text": "Pierce again at 6 weeks. Age until 12 weeks total."}
        ],
        "temperature": "86°F (30°C) for make, 54-60°F for aging",
        "notes": [
            "Advanced cheese - requires experience and proper aging conditions",
            "Piercing at 5-6 weeks is essential for blue vein development",
            "Named after the village of Stilton though never made there",
            "The 'King of English Cheeses' since the 1700s",
            "Requires 85% humidity aging environment",
            "Based on recipes from 'Practical Cheese Making' (1917)"
        ],
        "tags": ["cheese", "Stilton", "blue cheese", "English", "aged", "Penicillium", "advanced", "traditional"],
        "confidence": {"overall": "high", "flags": ["Advanced recipe - requires cheese making experience"]},
        "image_refs": []
    },
    {
        "id": "18th-century-farmhouse-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "18th Century Farmhouse Cheddar",
        "category": "mains",
        "attribution": "Traditional English/American Farmhouse (1700s-1800s)",
        "source_note": "Based on 18th century farmhouse methods documented in historical cookbooks and the 1934 USDA bulletin 'Making American Cheese on the Farm.' This was how farm families preserved summer milk for winter use.",
        "description": "A true farmhouse cheddar using traditional methods from the 1700s. Simpler than modern cheddar, it uses basic cultures and can age for several months. How American farm families made cheese before refrigeration.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "4 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons", "prep_note": "raw milk preferred"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp", "prep_note": "or 1/2 cup cultured buttermilk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for pasteurized milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86-90°F."},
            {"step": 2, "text": "Add culture (or buttermilk). Stir well. Ripen for 45-60 minutes."},
            {"step": 3, "text": "Add diluted rennet. Stir gently in figure-8 pattern for 1 minute."},
            {"step": 4, "text": "Cover and let set 60-90 minutes until curd gives clean break."},
            {"step": 5, "text": "Cut curd into 1/2-inch cubes."},
            {"step": 6, "text": "Let curds rest 5 minutes."},
            {"step": 7, "text": "Slowly raise temperature to 100°F over 30 minutes, stirring gently."},
            {"step": 8, "text": "Maintain at 100°F for 30 more minutes, stirring occasionally."},
            {"step": 9, "text": "Drain off whey, keeping curds warm."},
            {"step": 10, "text": "CHEDDARING: Stack curds and let them mat together. Flip the slab every 15-20 minutes for 1-2 hours."},
            {"step": 11, "text": "Mill (break apart) the cheddared curd into walnut-sized pieces."},
            {"step": 12, "text": "Mix in salt thoroughly."},
            {"step": 13, "text": "Pack salted curds firmly into cheesecloth-lined mold."},
            {"step": 14, "text": "Press at 10 lbs for 15 min, 20 lbs for 30 min, 50 lbs for 12-24 hours."},
            {"step": 15, "text": "Remove from mold. Air dry 2-3 days until rind forms."},
            {"step": 16, "text": "Wax or bandage wrap. Age at 55°F for 2-6 months."}
        ],
        "temperature": "86-90°F make, 100°F cook, 55°F aging",
        "notes": [
            "Based on methods from 1700s-1800s American farmhouses",
            "The 1934 USDA bulletin documented this traditional method",
            "Cheddaring is the key step - it develops the texture",
            "Raw milk was traditional but pasteurized works with calcium chloride",
            "Bandage wrapping was used before cheese wax was available",
            "A milk cow produced 3 gallons/day - cheese preserved the surplus"
        ],
        "tags": ["cheese", "cheddar", "farmhouse", "18th century", "traditional", "aged", "American", "USDA"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-yorkshire-wensleydale",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Yorkshire Wensleydale Cheese",
        "category": "mains",
        "attribution": "English / Yorkshire Dales (Medieval origins)",
        "source_note": "Wensleydale cheese was first made by Cistercian monks in the 12th century in the Yorkshire Dales. Originally made from sheep's milk, it evolved to cow's milk over centuries. The crumbly texture and honey notes are distinctive.",
        "description": "A traditional English cheese from the Yorkshire Dales, dating back to 12th century Cistercian monks. Crumbly, moist, and slightly sweet with honey undertones. Often paired with fruitcake or apple pie in Yorkshire.",
        "servings_yield": "About 1.5 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "2-4 weeks aging",
        "total_time": "2-4 weeks",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1 1/2", "unit": "tbsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 84°F (29°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle culture over milk. Let rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 45 minutes at 84°F."},
            {"step": 5, "text": "Add diluted rennet, stirring gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 45-60 minutes until clean break."},
            {"step": 7, "text": "Cut curd into 1/2-inch cubes."},
            {"step": 8, "text": "Let rest 5 minutes."},
            {"step": 9, "text": "Slowly raise temperature to 90°F over 30 minutes, stirring gently."},
            {"step": 10, "text": "Hold at 90°F for 30 minutes, stirring occasionally."},
            {"step": 11, "text": "Drain whey. Pile curds and let mat for 30 minutes."},
            {"step": 12, "text": "Break up matted curds. Mix in salt."},
            {"step": 13, "text": "Pack into cheesecloth-lined mold."},
            {"step": 14, "text": "Press lightly (5 lbs) for 15 minutes. Flip and press at 10 lbs overnight."},
            {"step": 15, "text": "Remove from mold. Air dry 2-3 days, flipping daily."},
            {"step": 16, "text": "Age at 55°F and 80% humidity for 2-4 weeks."}
        ],
        "temperature": "84°F make, 90°F cook, 55°F aging",
        "notes": [
            "First made by Cistercian monks in 12th century Yorkshire",
            "Originally sheep's milk, now usually cow's milk",
            "Traditionally paired with fruitcake or apple pie",
            "The crumbly, moist texture is characteristic",
            "Early rennet was called 'prezzur' from French 'présure' (monks' influence)",
            "Hundreds of Yorkshire farms made this in the early 1900s"
        ],
        "tags": ["cheese", "Wensleydale", "Yorkshire", "English", "monks", "medieval", "traditional", "crumbly"],
        "confidence": {"overall": "high", "flags": []},
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
