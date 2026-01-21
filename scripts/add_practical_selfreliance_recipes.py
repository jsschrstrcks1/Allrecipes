#!/usr/bin/env python3
"""Add practicalselfreliance.com cheese and dairy recipes to the database."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "psr-farmers-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Farmer's Cheese",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A simple farmer's cheese that's easy to make at home without specialized equipment. Start to finish in about 30 minutes. Often called 'lazy man's ricotta' due to similar flavor.",
        "servings_yield": "About 1 lb from 1/2 gallon milk",
        "prep_time": "5 min",
        "cook_time": "25 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "whole milk", "quantity": "1/2", "unit": "gallon", "prep_note": "raw or pasteurized, not ultra-pasteurized"},
            {"item": "cultured buttermilk", "quantity": "2", "unit": "cup"},
            {"item": "lemon juice", "quantity": "4", "unit": "tbsp", "prep_note": "fresh or bottled"},
            {"item": "sea salt", "quantity": "1/2", "unit": "tsp", "prep_note": "optional, to taste"},
            {"item": "fresh herbs", "quantity": "", "unit": "to taste", "prep_note": "minced, optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 175°F over medium heat, stirring occasionally to prevent sticking."},
            {"step": 2, "text": "Remove from heat and add buttermilk and lemon juice, stirring to combine."},
            {"step": 3, "text": "Allow mixture to sit undisturbed for at least 5 minutes until curds and whey separate visibly."},
            {"step": 4, "text": "Pour curds and whey through a cheesecloth-lined colander. Drain 2-3 minutes for a texture resembling thick oatmeal (extend draining for drier cheese)."},
            {"step": 5, "text": "Stir in salt and herbs if desired, then serve."}
        ],
        "temperature": "175°F (79°C)",
        "notes": [
            "Works with both raw and pasteurized milk, but ultra-pasteurized is not recommended",
            "Less straining time gives wetter cheese closer to cottage cheese",
            "Add 1 tbsp heavy cream to crumbled cheese for texture closer to ricotta",
            "Can be used in place of ricotta or cream cheese"
        ],
        "tags": ["cheese", "homemade", "beginner", "quick", "farmer's cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-homemade-cheddar-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Homemade Cheddar Cheese",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "Homemade cheddar is rich and flavorful. Natural bandaging allows the cheese to achieve complex flavors during aging. Can be made as waxed cheddar or clothbound cheddar.",
        "servings_yield": "One cheese wheel from 4 gallons milk",
        "prep_time": "30 min",
        "cook_time": "6 hours",
        "total_time": "3-12 months (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "4", "unit": "gallon", "prep_note": "raw or pasteurized, not ultra-pasteurized"},
            {"item": "direct set mesophilic starter", "quantity": "2", "unit": "packet", "prep_note": "1 packet for raw milk"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp", "prep_note": "diluted in 1/4 cup cool, unchlorinated water"},
            {"item": "calcium chloride liquid", "quantity": "1", "unit": "tsp", "prep_note": "optional, for pasteurized milk only"},
            {"item": "cheese salt or canning salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm milk to 86°F, add starter culture, and allow 45 minutes to culture."},
            {"step": 2, "text": "Add rennet, stir, and set for 45 minutes until curds show clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes; heat slowly to 100°F over 40 minutes."},
            {"step": 4, "text": "Hold at 100°F for 30 minutes while stirring gently."},
            {"step": 5, "text": "Drain curds through cheesecloth; mat for 15 minutes."},
            {"step": 6, "text": "Stack and 'cheddar' (flip every 15 minutes) at 100°F for 2 hours."},
            {"step": 7, "text": "Break into 1/2-inch pieces; hold for 30 minutes, stirring every 10 minutes."},
            {"step": 8, "text": "Add salt and mix thoroughly."},
            {"step": 9, "text": "Press at increasing pressures: 20 lbs (30 min), 40 lbs (12 hrs), 50 lbs (24 hrs)."},
            {"step": 10, "text": "Air dry 2-5 days, flipping daily."},
            {"step": 11, "text": "Dress for aging via cloth binding, waxing, or vacuum sealing."},
            {"step": 12, "text": "Age at 50-55°F with 85% humidity for minimum 3 months (preferably 6-12 months)."}
        ],
        "temperature": "86°F (30°C) initial, 100°F (38°C) cooking",
        "notes": [
            "The cheddaring process involves stacking and flipping the curd mat",
            "Equipment needed: 5-gallon stockpot, butter muslin, slotted spoon, long knife, colander, cheese press, cheesemaking form",
            "Aging space should maintain 50-55°F and 85% humidity"
        ],
        "tags": ["cheese", "homemade", "cheddar", "aged", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-18th-century-farmhouse-cheddar",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "18th Century Farmhouse Cheddar",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "An old 18th century recipe for farmhouse cheddar that captures traditional cheesemaking techniques using simple ingredients and time-honored methods. Becomes dry and slightly salty, suitable for grating like parmesan.",
        "servings_yield": "About 2 lbs finished cheese (32 servings)",
        "prep_time": "3 hours",
        "cook_time": "24 hours pressing",
        "total_time": "About 24 days (including 60+ days aging)",
        "ingredients": [
            {"item": "milk", "quantity": "2", "unit": "gallon", "prep_note": "preferably raw"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt or canning salt", "quantity": "1", "unit": "tbsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp", "prep_note": "optional, if using pasteurized milk"},
            {"item": "cultured buttermilk", "quantity": "1", "unit": "cup", "prep_note": "optional, if using pasteurized milk"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 85-90°F."},
            {"step": 2, "text": "Dilute rennet in 1/4 cup water; add to cheese and stir for ~1 minute using figure-8 motions."},
            {"step": 3, "text": "If using pasteurized milk, add cultured buttermilk and calcium chloride."},
            {"step": 4, "text": "Allow cheese to rest undisturbed for ~90 minutes until firm curds form."},
            {"step": 5, "text": "Cut curds into 1-inch cubes, cutting completely to pot bottom."},
            {"step": 6, "text": "Let cut curds rest 60-90 minutes."},
            {"step": 7, "text": "Slowly raise temperature to 100°F, increasing no more than 2°F every 5 minutes."},
            {"step": 8, "text": "Hold at 100°F for 5-10 minutes, then strain curds through cheesecloth-lined colander."},
            {"step": 9, "text": "Add salt and break curds into small pieces while distributing salt."},
            {"step": 10, "text": "Line cheese press with cheesecloth; place curds inside."},
            {"step": 11, "text": "Press, increasing pressure every 20-30 minutes for ~2 hours, then rest under pressure for ~12 hours."},
            {"step": 12, "text": "Flip cheese and press opposite side for another ~12 hours."},
            {"step": 13, "text": "Age on salted shelf for minimum 60 days, flipping every 1-2 days."}
        ],
        "temperature": "85-90°F (29-32°C) initial, 100°F (38°C) cooking",
        "notes": [
            "Historical recipe that produces a drier, grating-style cheese",
            "Goat's milk works wonderfully in this recipe",
            "Age for minimum 60 days for food safety"
        ],
        "tags": ["cheese", "homemade", "cheddar", "historical", "aged", "farmhouse"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-fromage-blanc",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fromage Blanc",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "An easy to make French soft cheese that's ready in less than 24 hours. Strained for just a few hours it achieves a cream cheese-like texture; strained for 10-12 hours it's most similar to ricotta.",
        "servings_yield": "About 1.5 lbs from 1 gallon milk",
        "prep_time": "15 min",
        "cook_time": "12 hours setting",
        "total_time": "16-24 hours",
        "ingredients": [
            {"item": "milk", "quantity": "1", "unit": "gallon"},
            {"item": "Fromage Blanc Starter Culture", "quantity": "1", "unit": "packet"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour one gallon of milk into a saucepan or stockpot."},
            {"step": 2, "text": "Heat to 86°F (30°C)."},
            {"step": 3, "text": "Add one packet Fromage Blanc culture. Allow the culture to re-hydrate for 2 minutes, then stir to dissolve."},
            {"step": 4, "text": "Cover and let set at room temperature (65-75°F) for about 12 hours, or until thickened."},
            {"step": 5, "text": "Pour or ladle the curd into a butter muslin lined colander."},
            {"step": 6, "text": "Hang and drain 4 to 12 hours (hangtime depends on desired consistency)."},
            {"step": 7, "text": "Refrigerate and enjoy within 1-2 weeks."}
        ],
        "temperature": "86°F (30°C), then room temperature 65-75°F (18-24°C)",
        "notes": [
            "Shorter straining = creamier, cream cheese-like texture",
            "Longer straining = firmer, ricotta-like texture",
            "Great base for both sweet and savory dishes"
        ],
        "tags": ["cheese", "homemade", "french", "soft cheese", "cultured", "beginner"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-yogurt-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Yogurt Cheese (Labneh-Style)",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A simple recipe creating a creamy, tangy spread or dip from yogurt using just one ingredient. Has the texture of very thick yogurt or cream cheese, depending on how much whey is removed.",
        "servings_yield": "About 1 cup from 2 cups yogurt",
        "prep_time": "5 min",
        "cook_time": "4-24 hours draining",
        "total_time": "4-24 hours",
        "ingredients": [
            {"item": "whole or low-fat yogurt", "quantity": "2", "unit": "cup", "prep_note": "use thermophilic cultured yogurt, not mesophilic"}
        ],
        "instructions": [
            {"step": 1, "text": "Line a sieve with cheesecloth and position it over a bowl."},
            {"step": 2, "text": "In a separate bowl, whisk the yogurt until it reaches a smooth, lump-free consistency."},
            {"step": 3, "text": "Carefully pour the yogurt onto the cheesecloth in the sieve."},
            {"step": 4, "text": "Refrigerate the setup for at least 4 hours, up to 24 hours, allowing the whey to drain."},
            {"step": 5, "text": "Once reaching desired texture, transfer the cheese to a covered container and refrigerate."}
        ],
        "notes": [
            "Keeps for 1-2 weeks refrigerated",
            "Low-fat versions have slightly shorter shelf life",
            "Can partially or completely replace cream cheese in cheesecake",
            "Use standard yogurt cultures (thermophilic), avoid mesophilic room-temperature yogurts"
        ],
        "tags": ["cheese", "homemade", "yogurt", "labneh", "beginner", "no-cook"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-colby-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Colby Cheese",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A mild cheese with an open texture. Colby has more moisture than most cheddars, and that extra moisture is maintained with cheese wax during the aging process.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "4 hours",
        "total_time": "60-90 days (including aging)",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallon", "prep_note": "raw or pasteurized"},
            {"item": "direct-set mesophilic starter", "quantity": "1", "unit": "packet"},
            {"item": "rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "single strength, dissolved in 1/4 cup cool, unchlorinated water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F."},
            {"step": 2, "text": "Add starter culture, stir 1 minute, let ripen 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir 1 minute (a few minutes longer for raw milk)."},
            {"step": 4, "text": "Let sit undisturbed 30 minutes until clean break forms."},
            {"step": 5, "text": "Cut curds into 3/8-inch pieces, rest 5 minutes."},
            {"step": 6, "text": "Gradually heat curds to 102°F (raising 2 degrees every 5 minutes)."},
            {"step": 7, "text": "Maintain 102°F for 30 minutes with periodic stirring."},
            {"step": 8, "text": "Wash curds by replacing whey with cool water until reaching 80°F; maintain 15 minutes."},
            {"step": 9, "text": "Drain curds 20 minutes."},
            {"step": 10, "text": "Mix curds with salt."},
            {"step": 11, "text": "Press at progressive pressures (20, 30, 40, then 50 lbs) over several hours."},
            {"step": 12, "text": "Air dry 2-4 days until surface is dry."},
            {"step": 13, "text": "Wax and age 60-90 days at 50°F."}
        ],
        "temperature": "86°F (30°C) initial, 102°F (39°C) cooking",
        "notes": [
            "The curd washing step distinguishes Colby from cheddar",
            "Washing with cool water stops acid development and creates milder flavor",
            "Waxing helps maintain the higher moisture content"
        ],
        "tags": ["cheese", "homemade", "colby", "american", "washed curd", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-paneer",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Homemade Paneer",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A simple homemade cheese that comes together quickly with just a few ingredients. This Indian cheese can be prepared in under two hours from start to finish.",
        "servings_yield": "About 1 lb from 1 gallon milk",
        "prep_time": "30 min",
        "cook_time": "45 min",
        "total_time": "90 min",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "lemon juice", "quantity": "1/4", "unit": "cup", "prep_note": "or 1 tsp citric acid as alternative"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp", "prep_note": "optional"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat the milk: Gradually warm milk to 185-194°F, holding at temperature for 20-30 minutes, then cool to 170°F."},
            {"step": 2, "text": "Add curdling agent: Warm lemon juice to 170°F and stir into milk. Alternatively, dissolve citric acid in warm water before adding."},
            {"step": 3, "text": "Set curds: Allow mixture to sit undisturbed for 10-15 minutes until whey clears. If whey remains cloudy, add more lemon juice or citric acid."},
            {"step": 4, "text": "Strain: Pour curds and whey through cheesecloth-lined colander. Mix in salt if desired."},
            {"step": 5, "text": "Drain: Wrap cheesecloth around cheese and hang to drain for approximately 30 minutes."},
            {"step": 6, "text": "Press: Place wrapped curds between cutting boards with 8-12 pounds weight on top. Press for 15-20 minutes (longer for firmer texture)."},
            {"step": 7, "text": "Finish: Remove weight and unwrap. Cheese is ready to use immediately."}
        ],
        "temperature": "185-194°F (85-90°C), then 170°F (77°C)",
        "notes": [
            "Best consumed fresh within 2-3 days",
            "Will keep refrigerated for 1-2 weeks when tightly wrapped",
            "Similar to queso fresco in technique"
        ],
        "tags": ["cheese", "homemade", "paneer", "indian", "fresh cheese", "beginner"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-traditional-cultured-mozzarella",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cultured Mozzarella",
        "category": "sides",
        "attribution": "David Asher / Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com (from 'Milk Into Cheese' by David Asher)",
        "description": "This cheese-making method employs natural starter cultures and slow fermentation rather than quick acid-set techniques, yielding superior flavor and texture complexity.",
        "servings_yield": "About 2.25 lbs (1 kg) or 36 servings",
        "prep_time": "1 hour",
        "cook_time": "7 hours",
        "total_time": "8 hours",
        "ingredients": [
            {"item": "whole milk", "quantity": "2.5", "unit": "gallon", "prep_note": "10 liters, preferably unhomogenized"},
            {"item": "starter", "quantity": "100", "unit": "ml", "prep_note": "clabber, kefir, whey at 1:100 ratio, or mesophilic starter powder packet"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C)."},
            {"step": 2, "text": "Mix in starter thoroughly."},
            {"step": 3, "text": "Add rennet and blend completely."},
            {"step": 4, "text": "Wait 45 minutes to 1 hour for clean break; cover to retain heat."},
            {"step": 5, "text": "Cut curds into 1-inch (2.5 cm) walnut-sized pieces using vertical, crosswise, and horizontal cuts."},
            {"step": 6, "text": "Gently stir curds for 5-10 minutes."},
            {"step": 7, "text": "Ferment curds under whey at room temperature until pH reaches 5.3 (typically 6-8 hours); maintain 86°F (30°C) minimum."},
            {"step": 8, "text": "Prepare 5 quarts boiling water and 5 quarts cold water."},
            {"step": 9, "text": "Mix light salt brine: 2 quarts cold water plus 1 tablespoon salt."},
            {"step": 10, "text": "Strain curds from whey."},
            {"step": 11, "text": "Slowly pour nearly-boiling water over curds, stirring gently between additions."},
            {"step": 12, "text": "Form curds into a single mass; stretch and shape into balls."},
            {"step": 13, "text": "Plunge finished mozzarella into cold water until cooled."},
            {"step": 14, "text": "Transfer to salt brine and refrigerate."}
        ],
        "temperature": "95°F (35°C) initial",
        "notes": [
            "The key to good mozzarella is hitting the exact moment the curd is ready to stretch",
            "Test a small piece of curd in hot water every 30 minutes once fermentation begins - it should stretch smoothly without breaking",
            "For quicker make, thermophilic culture like yogurt can reduce fermentation time to around 3 hours",
            "Recipe from David Asher's 'Milk Into Cheese' (Chelsea Green Publishing, 2024)"
        ],
        "tags": ["cheese", "homemade", "mozzarella", "italian", "cultured", "pasta filata", "intermediate"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-cultured-butter",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cultured Butter",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "Cultured butter has so much more flavor than regular butter, and it's incredibly easy to make yourself. The cream is fermented before churning, creating a tangy, complex flavor.",
        "servings_yield": "About 1.25 cups butter and 3/4 cup buttermilk",
        "prep_time": "20 min",
        "cook_time": "24-72 hours culturing",
        "total_time": "About 48 hours total",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "pint", "prep_note": "preferably grass-fed Jersey or Brown Swiss"},
            {"item": "cultured buttermilk with live cultures", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Culture the Cream: Pour heavy cream into a clean jar. Add 1/8 to 1/4 cup cultured buttermilk, stirring gently to combine."},
            {"step": 2, "text": "Cover and let sit at room temperature for 24-72 hours until it reaches crème fraîche consistency with a tangy aroma."},
            {"step": 3, "text": "Churn the Cream: Pour cultured cream into a stand mixer with whisk attachment. Mix at medium-low speed (3-4 out of 10) for 15-20 minutes."},
            {"step": 4, "text": "After ~10 minutes, cream becomes whipped. Continue churning until butter clumps form and separate from liquid (about 20 minutes total)."},
            {"step": 5, "text": "Stop mixing when butter is firm and cohesive."},
            {"step": 6, "text": "Drain off buttermilk and reserve for pancakes or baking."},
            {"step": 7, "text": "Wash the Butter: Rinse under cold water with a wooden spoon until water runs clear (optional but improves shelf life)."},
            {"step": 8, "text": "Season and Store: Add salt to taste if desired. Pack into a container and refrigerate."}
        ],
        "notes": [
            "Alternatives to stand mixer include hand mixers, traditional churns, or vigorous shaking in a mason jar",
            "Skip buttermilk step for milder-flavored uncultured butter",
            "The buttermilk byproduct is true cultured buttermilk, perfect for baking",
            "Two quarts of cream yields about a quart of buttermilk and 2-ish pounds of butter"
        ],
        "tags": ["butter", "homemade", "cultured", "fermented", "dairy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-cultured-buttermilk",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cultured Buttermilk",
        "category": "beverages",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "Making cultured buttermilk at home is a simple, rewarding process that yields a tangy, creamy liquid perfect for baking, cooking, or dressings. Prized for its ability to tenderize baked goods and provide slight acidity.",
        "servings_yield": "About 1 cup buttermilk (plus 8 oz butter)",
        "prep_time": "10 min",
        "cook_time": "24-48 hours culturing",
        "total_time": "About 24 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "pint", "prep_note": "preferably grass-fed or high-quality"},
            {"item": "cultured buttermilk with live cultures", "quantity": "1/4", "unit": "cup"},
            {"item": "buttermilk starter culture", "quantity": "1", "unit": "packet", "prep_note": "optional, if cultured buttermilk unavailable"}
        ],
        "instructions": [
            {"step": 1, "text": "Culture the Cream: Pour heavy cream into a clean jar or bowl."},
            {"step": 2, "text": "Add approximately 1/8 to 1/4 cup cultured buttermilk; stir gently to combine."},
            {"step": 3, "text": "Cover loosely and let sit at room temperature for 24-48 hours until thickened with a tangy aroma."},
            {"step": 4, "text": "Churn into Butter: Pour cultured cream into stand mixer, food processor, or use hand mixer."},
            {"step": 5, "text": "Mix on medium-low speed for 15-20 minutes until butter separates from liquid."},
            {"step": 6, "text": "Stop mixing when butter clumps together."},
            {"step": 7, "text": "Strain and Store: Strain buttermilk into clean container; refrigerate for about one week."},
            {"step": 8, "text": "Optional: Wash butter in cold water to extend shelf life."}
        ],
        "notes": [
            "Traditionally, buttermilk is the liquid left behind after churning cream to make butter",
            "Use in pancakes, biscuits, dressings, marinades, cornbread, fried chicken",
            "The tangy flavor comes from beneficial bacteria in the culture"
        ],
        "tags": ["buttermilk", "homemade", "cultured", "fermented", "dairy", "baking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-creme-fraiche",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crème Fraîche",
        "category": "sides",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A thick, tangy cream that has been cultured with beneficial bacteria, similar to sour cream but with a milder flavor and smoother texture. Less prone to curdling when heated, making it perfect for sauces and soups.",
        "servings_yield": "About 2 cups (32 tbsp)",
        "prep_time": "10 min",
        "cook_time": "12-24 hours culturing",
        "total_time": "About 24 hours",
        "ingredients": [
            {"item": "heavy cream", "quantity": "1", "unit": "pint", "prep_note": "preferably grass-fed or high-quality"},
            {"item": "cultured buttermilk OR crème fraîche starter culture packet", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour heavy cream into a clean jar or bowl. Add the buttermilk or starter culture and stir gently to combine."},
            {"step": 2, "text": "Cover loosely with a lid or cloth and leave at room temperature for 12-24 hours until thickened with a mild, tangy flavor."},
            {"step": 3, "text": "Once thickened, stir again, cover tightly, and transfer to the refrigerator."},
            {"step": 4, "text": "Chill for several hours before using to allow full flavor development."}
        ],
        "notes": [
            "If your house is very cool (like in Vermont winter), you may need up to 48 hours",
            "Keep in warm spot no more than 80-90°F to avoid overheating the bacteria",
            "Quick substitute: mix sour cream with heavy cream 1:1, let sit at room temperature a few hours",
            "Alternative: mix plain Greek yogurt with heavy cream for similar results"
        ],
        "tags": ["creme fraiche", "homemade", "cultured", "french", "cream", "dairy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-swedish-filmjolk",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Swedish Filmjölk (Drinkable Yogurt)",
        "category": "beverages",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A traditional Swedish cultured dairy product that resembles kefir but offers a smooth, pleasant taste profile. Unlike thermophilic yogurts requiring incubation, this mesophilic yogurt cultures at room temperature.",
        "servings_yield": "4 cups / 4 servings",
        "prep_time": "10 min",
        "cook_time": "1-2 days fermentation",
        "total_time": "About 48 hours",
        "ingredients": [
            {"item": "milk", "quantity": "1", "unit": "quart", "prep_note": "raw or pasteurized"},
            {"item": "filmjölk starter culture", "quantity": "1/4", "unit": "cup", "prep_note": "or 1 packet freeze-dried starter culture"}
        ],
        "instructions": [
            {"step": 1, "text": "Begin with a quart of milk. If using raw milk, shake it to mix the cream back in since it naturally separates."},
            {"step": 2, "text": "Mix approximately 1/4 to 1/2 cup of existing filmjölk culture into the milk and stir thoroughly. Alternatively, add freeze-dried culture directly."},
            {"step": 3, "text": "Cover the milk and let it sit at room temperature for 1-2 days, ideally between 65-75°F. Duration depends on desired thickness and flavor intensity."},
            {"step": 4, "text": "Once thickened to your liking, you can enjoy the Filmjölk immediately or store it in the refrigerator for up to two weeks."},
            {"step": 5, "text": "Add preferred flavorings like crushed fruit, honey, or maple syrup."}
        ],
        "notes": [
            "Both pasteurized and raw milk work well",
            "Can be used in baking recipes requiring buttermilk, sour cream, or yogurt",
            "Has a rich buttery flavor from diacetyl produced by the probiotic strains",
            "Part of a family of Nordic dairy ferments including Viili and Skyr"
        ],
        "tags": ["yogurt", "homemade", "swedish", "filmjolk", "mesophilic", "fermented", "probiotic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-kefir-yogurt",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kefir Yogurt",
        "category": "beverages",
        "attribution": "David Asher / Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com (from 'The Art of Natural Cheesemaking' by David Asher)",
        "description": "A thick, creamy yogurt made at home using a kefir starter culture. The kefir offers a rich, diverse mix of beneficial microbes that create a flavorful yogurt without commercial packets.",
        "servings_yield": "About 3 quarts (12 servings)",
        "prep_time": "30 min",
        "cook_time": "30-60 min cooking + 12-36 hours culturing",
        "total_time": "About 8 hours active + culturing time",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "pasteurized or raw, preferably unhomogenized"},
            {"item": "active kefir", "quantity": "3/4", "unit": "cup", "prep_note": "180 mL, strained kefir grains, prepared the day before, or yogurt"}
        ],
        "instructions": [
            {"step": 1, "text": "Warm the milk: Slowly heat milk to 185°F (85°C) over medium heat, stirring continuously."},
            {"step": 2, "text": "Cook the milk: Maintain 185°F for 30 minutes to 1 hour with constant stirring. Extended cooking time produces thicker yogurt."},
            {"step": 3, "text": "Cool: Remove from heat and stir until temperature drops to 110°F (43°C). Wait for proper cooling before adding culture to avoid killing beneficial bacteria."},
            {"step": 4, "text": "Add culture: Incorporate 1/4 cup (60 mL) kefir into the warm milk and stir thoroughly."},
            {"step": 5, "text": "Incubate: Culture for 12 to 36 hours until desired flavor and consistency develop. Check every 12 hours as kefir culture timing varies unpredictably."}
        ],
        "temperature": "185°F (85°C) for cooking, 110°F (43°C) for culturing",
        "notes": [
            "The longer the milk is cooked at 185°F, the thicker the yogurt will be",
            "Culturing time can vary widely (12-36 hours)",
            "Uses kefir instead of commercial yogurt starter"
        ],
        "tags": ["yogurt", "homemade", "kefir", "fermented", "probiotic", "dairy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "psr-water-kefir",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Water Kefir (Natural Probiotic Soda)",
        "category": "beverages",
        "attribution": "Ashley Adamant, Practical Self Reliance",
        "source_note": "practicalselfreliance.com",
        "description": "A delightfully fizzy fermented drink that's like a probiotic homemade soda. An all-natural probiotic soda that's easy to make at home.",
        "servings_yield": "1 quart",
        "prep_time": "10 min",
        "cook_time": "12-48 hours fermentation",
        "total_time": "12-48 hours",
        "ingredients": [
            {"item": "sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "hot water", "quantity": "1/2", "unit": "cup"},
            {"item": "room-temperature water", "quantity": "3", "unit": "cup"},
            {"item": "water kefir grains", "quantity": "1", "unit": "tbsp", "prep_note": "rehydrated, or 1 packet"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sugar and hot water in a quart-size jar, stirring until sugar fully dissolves."},
            {"step": 2, "text": "Add 3 cups of room-temperature water."},
            {"step": 3, "text": "Introduce rehydrated kefir grains."},
            {"step": 4, "text": "Cover jar with breathable fabric like cloth napkin or muslin."},
            {"step": 5, "text": "Keep in a warm location (68-85°F) for 12 to 48 hours."},
            {"step": 6, "text": "Strain kefir grains from liquid, preserving both the finished beverage and grains."},
            {"step": 7, "text": "Consume immediately or bottle and refrigerate."}
        ],
        "temperature": "68-85°F (20-29°C) for fermentation",
        "notes": [
            "For extra fizz, do a second ferment: transfer to swing-top bottle and add 1/2 cup favorite fruit juice",
            "Preserve the grains for future batches",
            "Start with just a pinch of water kefir grains"
        ],
        "tags": ["kefir", "homemade", "probiotic", "fermented", "soda", "beverage", "water kefir"],
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
