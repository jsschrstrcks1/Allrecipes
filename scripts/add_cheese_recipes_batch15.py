#!/usr/bin/env python3
"""Add traditional cheese making recipes to the database (batch 15) - Italian, French, and more aged cheeses."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-parmesan-style",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Parmesan-Style Cheese",
        "category": "mains",
        "attribution": "Italian / Emilia-Romagna (Medieval)",
        "source_note": "Inspired by Parmigiano-Reggiano, which dates to the Middle Ages when Benedictine and Cistercian monks created it for long storage. True Parmigiano-Reggiano can only come from specific Italian provinces. This is an authentic-style homemade version.",
        "description": "A hard, granular aged cheese inspired by Italian Parmigiano-Reggiano. Requires patience - at least 10-12 months aging - but the nutty, crystalline result is worth the wait. The 'King of Cheeses' in your own cheese cave.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "4 hours",
        "cook_time": "10-24 months aging",
        "total_time": "10-24 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "3", "unit": "gallons"},
            {"item": "skim milk", "quantity": "1", "unit": "gallon", "prep_note": "or let cream rise off 1 gallon overnight"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for sharper flavor"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "3", "unit": "lbs", "prep_note": "for saturated brine"}
        ],
        "instructions": [
            {"step": 1, "text": "TRADITIONAL: Let evening milk sit overnight to allow cream to rise. Skim cream and combine with fresh morning milk."},
            {"step": 2, "text": "MODERN: Combine whole and skim milk. Heat to 90°F (32°C)."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Sprinkle thermophilic culture (and lipase if using) over milk. Rehydrate 2 minutes, then stir."},
            {"step": 5, "text": "Cover and ripen for 45 minutes."},
            {"step": 6, "text": "Raise temperature to 95°F. Add diluted rennet. Stir 1 minute."},
            {"step": 7, "text": "Cover and let set for 30-45 minutes until firm clean break."},
            {"step": 8, "text": "Cut curd into VERY SMALL pieces (rice-grain size) - this is critical for Parmesan texture."},
            {"step": 9, "text": "Slowly raise temperature to 131°F (55°C) over 45 minutes, stirring constantly."},
            {"step": 10, "text": "Hold at 131°F for 30 minutes, stirring. Curds should be very firm."},
            {"step": 11, "text": "Let curds settle. Drain whey."},
            {"step": 12, "text": "Pack curds firmly into a large wheel mold."},
            {"step": 13, "text": "Press at 10 lbs for 15 min, 20 lbs for 30 min, 40 lbs for 2 hours, 50 lbs for 24 hours."},
            {"step": 14, "text": "Make saturated brine (3 lbs salt per gallon water). Brine cheese for 24 hours per pound."},
            {"step": 15, "text": "Air dry 3-5 days at 55°F until rind forms."},
            {"step": 16, "text": "Age at 55°F, 80% humidity for minimum 10-12 months (24 months preferred)."},
            {"step": 17, "text": "Turn weekly. Oil rind if cracking occurs."}
        ],
        "temperature": "90-131°F make, 55°F aging",
        "notes": [
            "True Parmigiano-Reggiano can only come from specific Italian provinces",
            "The tiny curd size and high cook temperature are essential",
            "Minimum 10-12 months aging; 24 months for best flavor",
            "White crystals that form are tyrosine amino acids, not salt",
            "Medieval monks created this for long-term storage",
            "One of the most challenging home cheeses - worth the effort"
        ],
        "tags": ["cheese", "Parmesan", "Italian", "aged", "hard cheese", "grating cheese", "medieval", "traditional"],
        "confidence": {"overall": "high", "flags": ["Advanced - requires long aging and temperature control"]},
        "image_refs": []
    },
    {
        "id": "traditional-asiago",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Italian Asiago",
        "category": "mains",
        "attribution": "Italian / Veneto Region (1000+ years)",
        "source_note": "Asiago comes from the Asiago plateau in the Veneto and Trentino regions of Italy. Originally made from sheep's milk over 1,000 years ago, it transitioned to cow's milk around 1500. Comes in fresh (Pressato) and aged (d'Allevo) varieties.",
        "description": "An Italian cheese with over 1,000 years of history. Fresh Asiago (Pressato) is mild and smooth; aged Asiago (d'Allevo) is sharp and crumbly. This recipe makes the aged version, perfect for grating.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "3-12 months aging",
        "total_time": "3-12 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle thermophilic culture over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 30 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 45 minutes until firm clean break."},
            {"step": 7, "text": "Cut curd into 1/4-inch cubes."},
            {"step": 8, "text": "Let rest 5 minutes."},
            {"step": 9, "text": "Slowly raise temperature to 118°F (48°C) over 45 minutes, stirring gently."},
            {"step": 10, "text": "Hold at 118°F for 30 minutes, stirring occasionally."},
            {"step": 11, "text": "Let curds settle. Drain whey."},
            {"step": 12, "text": "Pack curds into a wheel mold lined with cheesecloth."},
            {"step": 13, "text": "Press at 10 lbs for 30 min, 20 lbs for 2 hours, 40 lbs for 12 hours."},
            {"step": 14, "text": "Remove from mold. Rub salt on all surfaces."},
            {"step": 15, "text": "Salt daily for 3-4 days, turning each time."},
            {"step": 16, "text": "Air dry at 55°F until rind forms (about 1 week)."},
            {"step": 17, "text": "Age at 55°F, 85% humidity: 3 months (mezzano), 9 months (vecchio), 12+ months (stravecchio)."}
        ],
        "temperature": "95-118°F make, 55°F aging",
        "notes": [
            "Over 1,000 years of history on the Asiago plateau",
            "Originally sheep's milk, transitioned to cow's milk around 1500",
            "Fresh Asiago (Pressato) is only aged 20-40 days",
            "Aged Asiago (d'Allevo) is aged 3-12+ months",
            "Mezzano (3-5 mo), Vecchio (9-12 mo), Stravecchio (15-24 mo)",
            "The longer it ages, the sharper and more crumbly it becomes"
        ],
        "tags": ["cheese", "Asiago", "Italian", "aged", "Veneto", "traditional", "1000 years"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pecorino-romano",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pecorino Romano",
        "category": "mains",
        "attribution": "Italian / Roman Empire (2000+ years)",
        "source_note": "One of the oldest cheeses in the world, Pecorino Romano was a staple ration for Roman legionnaires. 'Pecorino' means sheep in Italian. Still made with sheep's milk in Lazio, Sardinia, and Tuscany using ancient methods.",
        "description": "A 2,000-year-old cheese that fueled the Roman legions. Made from sheep's milk with a sharp, salty, tangy flavor. Essential for authentic Cacio e Pepe, Carbonara, and Amatriciana. Aged 5-12 months.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "5-12 months aging",
        "total_time": "5-12 months",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons", "prep_note": "cow's milk can substitute"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/4", "unit": "tsp", "prep_note": "essential for authentic flavor"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "lamb rennet traditional"},
            {"item": "coarse sea salt", "quantity": "1/4", "unit": "cup", "prep_note": "for dry salting"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 100°F (38°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle thermophilic culture and lipase over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 30 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir 1 minute."},
            {"step": 6, "text": "Cover and let set for 30-40 minutes until firm clean break."},
            {"step": 7, "text": "Cut curd into very small pieces (rice-grain size)."},
            {"step": 8, "text": "Raise temperature to 116°F (47°C) over 30 minutes, stirring constantly."},
            {"step": 9, "text": "Hold at 116°F for 20 minutes. Curds should be very firm and squeaky."},
            {"step": 10, "text": "Drain whey. Pack curds very firmly into a wheel mold."},
            {"step": 11, "text": "Press at 25 lbs for 30 min, 50 lbs for 12 hours."},
            {"step": 12, "text": "Remove from mold. Rub coarse sea salt generously on all surfaces."},
            {"step": 13, "text": "Salt and turn daily for 30 days. This extended salting is traditional."},
            {"step": 14, "text": "After salting period, scrape off excess salt."},
            {"step": 15, "text": "Age at 55°F, 85% humidity for minimum 5 months (8-12 months preferred)."},
            {"step": 16, "text": "The rind will develop naturally. Turn weekly during aging."}
        ],
        "temperature": "100-116°F make, 55°F aging",
        "notes": [
            "Fed Roman legionnaires - 27 grams daily ration for each soldier",
            "'Pecorino' means made from sheep (pecora) milk",
            "Lipase is essential for the authentic sharp, tangy flavor",
            "The 30-day salting period is traditional and creates the salty character",
            "True Pecorino Romano comes only from Lazio, Sardinia, and parts of Tuscany",
            "Essential for authentic Cacio e Pepe, Carbonara, and Amatriciana"
        ],
        "tags": ["cheese", "Pecorino Romano", "Italian", "sheep milk", "Roman", "ancient", "grating cheese", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-gorgonzola",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Italian Gorgonzola",
        "category": "mains",
        "attribution": "Italian / Lombardy (879 AD)",
        "source_note": "Named after the town of Gorgonzola near Milan, first documented in 879 AD. One of the world's oldest blue cheeses. Comes in two varieties: Dolce (sweet/mild, aged 2-3 months) and Piccante (sharp, aged 3-6 months).",
        "description": "One of the world's oldest blue cheeses, from the town of Gorgonzola near Milan since 879 AD. Creamy and spreadable with characteristic blue-green veining. Milder than Roquefort, with a sweet, buttery undertone.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "blue mold culture"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture and P. roqueforti over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 60 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 60 minutes until soft curd forms."},
            {"step": 7, "text": "Cut curd into 1-inch cubes (larger than most cheeses)."},
            {"step": 8, "text": "Let rest 10 minutes. Gently stir for 20 minutes at 86°F."},
            {"step": 9, "text": "Ladle curds into tall cylindrical molds. Do not press - let gravity drain."},
            {"step": 10, "text": "Drain at room temperature for 24 hours, flipping every 4-6 hours."},
            {"step": 11, "text": "Remove from mold. Salt all surfaces generously."},
            {"step": 12, "text": "Place on draining mat at 60°F. Turn and re-salt daily for 1 week."},
            {"step": 13, "text": "Move to aging at 45-50°F, 95% humidity."},
            {"step": 14, "text": "At 3-4 weeks, pierce cheese with stainless steel skewer (about 25 holes per side)."},
            {"step": 15, "text": "Age 2-3 months for Dolce (mild), 3-6 months for Piccante (sharp)."},
            {"step": 16, "text": "Blue veins should develop throughout. Wrap in foil when fully developed."}
        ],
        "temperature": "86°F make, 45-50°F aging",
        "notes": [
            "First documented in the town of Gorgonzola in 879 AD",
            "One of the world's oldest blue cheeses",
            "Dolce (sweet) is aged 2-3 months - creamy and mild",
            "Piccante (sharp) is aged 3-6 months - firmer and stronger",
            "Requires very high humidity (95%) for proper aging",
            "The large curd size creates the characteristic creamy texture"
        ],
        "tags": ["cheese", "Gorgonzola", "Italian", "blue cheese", "879 AD", "Lombardy", "traditional"],
        "confidence": {"overall": "high", "flags": ["Requires high humidity aging environment"]},
        "image_refs": []
    },
    {
        "id": "traditional-roquefort",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Roquefort",
        "category": "mains",
        "attribution": "French / Roquefort-sur-Soulzon (79 AD)",
        "source_note": "Pliny the Elder mentioned Roquefort in 79 AD. Made exclusively from raw sheep's milk and aged in the natural caves of Roquefort-sur-Soulzon. Legend says a shepherd left his lunch in a cave and returned to find it transformed.",
        "description": "The 'King of Cheeses' according to the French, made from raw sheep's milk and aged in limestone caves since Roman times. Sharp, tangy, and crumbly with bold blue veining. The original blue cheese.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "3-5 months aging",
        "total_time": "3-5 months",
        "ingredients": [
            {"item": "raw sheep's milk", "quantity": "3", "unit": "gallons", "prep_note": "cow's milk can substitute"},
            {"item": "mesophilic culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "authentic Roquefort strain if possible"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "coarse sea salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Traditional Roquefort uses raw milk."},
            {"step": 2, "text": "Add calcium chloride only if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle mesophilic culture and P. roqueforti over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 60 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 90 minutes until soft curd forms (longer than Gorgonzola)."},
            {"step": 7, "text": "Cut curd into 3/4-inch cubes."},
            {"step": 8, "text": "Let rest 10 minutes without stirring."},
            {"step": 9, "text": "Gently transfer curds to a cheesecloth-lined mold. Do not press."},
            {"step": 10, "text": "Drain at 68-72°F for 2-3 days, flipping every 6-8 hours."},
            {"step": 11, "text": "Remove from mold. Rub coarse salt on all surfaces."},
            {"step": 12, "text": "Place in aging cave at 46-48°F, 95% humidity."},
            {"step": 13, "text": "At 2-3 weeks, pierce cheese with 40+ holes using a skewer."},
            {"step": 14, "text": "Continue aging 3-5 months. Blue mold should develop extensively."},
            {"step": 15, "text": "When properly veined, wrap in foil to slow further development."},
            {"step": 16, "text": "Ready when interior is creamy and heavily veined throughout."}
        ],
        "temperature": "86°F make, 46-48°F cave aging",
        "notes": [
            "Pliny the Elder mentioned this cheese in 79 AD",
            "True Roquefort is aged in the limestone caves of Roquefort-sur-Soulzon",
            "Legend: a shepherd forgot his lunch in a cave and discovered blue cheese",
            "Must be made from raw sheep's milk for authentic designation",
            "The cool, humid caves have natural Penicillium roqueforti spores",
            "Charles VI of France granted Roquefort a monopoly in 1411"
        ],
        "tags": ["cheese", "Roquefort", "French", "blue cheese", "sheep milk", "cave aged", "79 AD", "ancient"],
        "confidence": {"overall": "high", "flags": ["Requires cave-like aging conditions"]},
        "image_refs": []
    },
    {
        "id": "traditional-raclette",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Swiss Raclette",
        "category": "mains",
        "attribution": "Swiss / Valais (Medieval)",
        "source_note": "Raclette comes from the French 'racler' (to scrape). Medieval Swiss shepherds melted cheese by the fire and scraped it onto bread and potatoes. A quintessential Alpine melting cheese with a creamy, nutty flavor.",
        "description": "The ultimate melting cheese from the Swiss Alps. Medieval shepherds held wheels by the fire and scraped the melted cheese onto bread. Rich, creamy, and nutty with excellent melting properties. Perfect for the traditional raclette meal.",
        "servings_yield": "About 2 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "2-3 months aging",
        "total_time": "2-3 months",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C)."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 3, "text": "Sprinkle thermophilic culture over milk. Rehydrate 2 minutes, then stir."},
            {"step": 4, "text": "Cover and ripen for 30 minutes."},
            {"step": 5, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 6, "text": "Cover and let set for 30-40 minutes until clean break."},
            {"step": 7, "text": "Cut curd into 1/4-inch cubes."},
            {"step": 8, "text": "Let rest 5 minutes."},
            {"step": 9, "text": "Slowly raise temperature to 104°F (40°C) over 30 minutes, stirring gently."},
            {"step": 10, "text": "Hold at 104°F for 30 minutes, stirring occasionally."},
            {"step": 11, "text": "Drain whey. Pack curds firmly into a wheel mold."},
            {"step": 12, "text": "Press at 10 lbs for 30 min, 20 lbs for 2 hours, 30 lbs overnight."},
            {"step": 13, "text": "Remove from mold. Float in saturated brine for 8-12 hours."},
            {"step": 14, "text": "Air dry at 55°F for 2-3 days until rind forms."},
            {"step": 15, "text": "Age at 55°F, 90% humidity for 2-3 months."},
            {"step": 16, "text": "Wash rind with light brine weekly to develop characteristic flavor."}
        ],
        "temperature": "90-104°F make, 55°F aging",
        "notes": [
            "'Raclette' comes from French 'racler' - to scrape",
            "Medieval shepherds melted cheese by the fire and scraped it onto food",
            "The traditional meal: melted raclette over potatoes with pickles and onions",
            "Washing the rind develops the distinctive flavor",
            "Best melting properties at 2-3 months age",
            "From the Valais canton of Switzerland"
        ],
        "tags": ["cheese", "Raclette", "Swiss", "melting cheese", "Alps", "medieval", "washed rind"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-tomme",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional French Tomme (Farmhouse Wheel)",
        "category": "mains",
        "attribution": "French / Alpine Regions (Ancient)",
        "source_note": "'Tomme' simply means 'round of cheese' and refers to many traditional farmhouse cheeses made in the French Alps and surrounding regions. Typically made from skimmed milk left over after making butter - true farmhouse thrift.",
        "description": "A rustic French farmhouse cheese traditionally made from the skim milk left after butter making. Semi-firm with a gray-brown natural rind and earthy, nutty flavor. The embodiment of Alpine cheese making tradition.",
        "servings_yield": "About 1.5 lb wheel",
        "prep_time": "3 hours",
        "cook_time": "2-4 months aging",
        "total_time": "2-4 months",
        "ingredients": [
            {"item": "part-skim milk", "quantity": "2", "unit": "gallons", "prep_note": "or whole milk with cream skimmed"},
            {"item": "mesophilic culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "1 1/2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "TRADITIONAL: Skim the cream from milk (used for butter). Use the remaining part-skim milk."},
            {"step": 2, "text": "Heat milk to 90°F (32°C)."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk."},
            {"step": 4, "text": "Sprinkle mesophilic culture over milk. Rehydrate 2 minutes, then stir."},
            {"step": 5, "text": "Cover and ripen for 45 minutes."},
            {"step": 6, "text": "Add diluted rennet. Stir gently for 1 minute."},
            {"step": 7, "text": "Cover and let set for 45-60 minutes until clean break."},
            {"step": 8, "text": "Cut curd into 1/2-inch cubes."},
            {"step": 9, "text": "Let rest 10 minutes."},
            {"step": 10, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes, stirring gently."},
            {"step": 11, "text": "Hold at 100°F for 20 minutes, stirring."},
            {"step": 12, "text": "Drain whey. Pack curds into a tomme mold."},
            {"step": 13, "text": "Press at 5 lbs for 15 min, 10 lbs for 1 hour, 15 lbs for 6 hours."},
            {"step": 14, "text": "Remove from mold. Salt all surfaces."},
            {"step": 15, "text": "Air dry at 55°F for 1 week, turning daily. A natural gray rind will form."},
            {"step": 16, "text": "Age at 50-55°F, 85% humidity for 2-4 months."},
            {"step": 17, "text": "Let the natural rind develop - it should become gray-brown and slightly fuzzy."}
        ],
        "temperature": "90-100°F make, 50-55°F aging",
        "notes": [
            "'Tomme' simply means 'wheel of cheese' in Alpine dialects",
            "Traditionally made from skim milk left after butter making",
            "True farmhouse thrift - nothing wasted",
            "The natural rind should be allowed to develop naturally",
            "Many varieties: Tomme de Savoie, Tomme de Chèvre, etc.",
            "Semi-firm texture with earthy, mushroomy flavor from natural rind"
        ],
        "tags": ["cheese", "Tomme", "French", "farmhouse", "Alpine", "natural rind", "traditional", "skim milk"],
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
