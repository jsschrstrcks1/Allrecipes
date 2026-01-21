#!/usr/bin/env python3
"""Add batch 19 of traditional cheese recipes - British territorial and French classics."""

import json
from datetime import date

RECIPES_FILE = "data/recipes.json"

new_recipes = [
    {
        "id": "traditional-cheshire-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cheshire Cheese",
        "category": "mains",
        "attribution": "Cheshire, England, Roman Era",
        "source_note": "Cheshire is possibly the oldest named British cheese, with references dating to Roman times. The salty pastures of the Cheshire Plain give this cheese its distinctive minerally flavor.",
        "description": "England's oldest named cheese, crumbly and tangy with a salty minerally finish from the salt marshes of Cheshire.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "annatto coloring", "quantity": "1/4", "unit": "tsp", "prep_note": "optional, for red Cheshire"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2 1/2", "unit": "tbsp", "prep_note": "slightly more than other cheeses"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk. Add annatto if making Red Cheshire."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 45 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 45-60 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (smaller than most cheeses). Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 15 minutes while maintaining 90°F."},
            {"step": 6, "text": "Allow curds to settle for 5 minutes, then drain off most whey."},
            {"step": 7, "text": "Keep curds at 90°F and stir occasionally for 1 hour, developing acid."},
            {"step": 8, "text": "Mill curds into small pieces (Cheshire has a crumbly texture)."},
            {"step": 9, "text": "Add salt (Cheshire uses more salt than other English cheeses) and mix well."},
            {"step": 10, "text": "Pack into cloth-lined mold. Press at 10 lbs for 30 minutes."},
            {"step": 11, "text": "Flip and press at 30 lbs for 12 hours."},
            {"step": 12, "text": "Flip and press at 50 lbs for 24 hours."},
            {"step": 13, "text": "Air dry 5-7 days. Cloth-bind with lard or butter-soaked cloth."},
            {"step": 14, "text": "Age at 55°F and 85% humidity for 2-6 months."}
        ],
        "temperature": "90°F throughout make, 55°F aging",
        "notes": [
            "Traditional Cheshire is more acidic than cheddar, giving it its characteristic tang",
            "Red Cheshire uses annatto; White Cheshire is the natural color",
            "The crumbly texture comes from the fine curd cut and high salt content",
            "Blue Cheshire occurs when Penicillium roqueforti naturally colonizes cracks during aging"
        ],
        "tags": ["cheese", "traditional", "english", "cheshire", "territorial-cheese", "roman-era", "crumbly"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-caerphilly-welsh",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Welsh Caerphilly",
        "category": "mains",
        "attribution": "Caerphilly, Wales, 1830s",
        "source_note": "Caerphilly was developed in the 1830s near the town of Caerphilly in South Wales. It was the traditional lunch cheese for Welsh coal miners, providing salt and moisture replenishment.",
        "description": "Fresh, lemony Welsh cheese with a moist, crumbly interior - the traditional miners' lunch cheese.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-8 weeks aging",
        "total_time": "2-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 1 hour (longer ripening for more acid)."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 40-45 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Gently stir for 10 minutes while maintaining 90°F."},
            {"step": 6, "text": "Raise temperature to 92°F over 30 minutes, stirring gently."},
            {"step": 7, "text": "Drain whey. Let curds mat slightly for 15 minutes."},
            {"step": 8, "text": "Cut matted curd into 2-inch strips. Stack for 15 minutes (brief cheddaring)."},
            {"step": 9, "text": "Mill curds into thumb-sized pieces."},
            {"step": 10, "text": "Add salt and mix gently."},
            {"step": 11, "text": "Pack into cloth-lined mold. Press at 10 lbs for 30 minutes."},
            {"step": 12, "text": "Flip and press at 20 lbs for 6 hours."},
            {"step": 13, "text": "Flip and press at 30 lbs for 12 hours."},
            {"step": 14, "text": "Brine for 12-24 hours or dry salt the surface."},
            {"step": 15, "text": "Age at 55°F and 90% humidity for 2-8 weeks. Traditional Caerphilly develops a natural gray-white rind."}
        ],
        "temperature": "90-92°F make, 55°F aging",
        "notes": [
            "Caerphilly is meant to be eaten young - it becomes too dry if aged too long",
            "The natural rind should be gray-white and slightly wrinkled",
            "Traditional Caerphilly was made quickly to provide income while cheddar aged",
            "The acidic, lemony tang made it refreshing for coal miners working in hot conditions"
        ],
        "tags": ["cheese", "traditional", "welsh", "caerphilly", "territorial-cheese", "1830s", "miners-cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-pont-leveque-normandy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Pont-l'Évêque (Normandy)",
        "category": "mains",
        "attribution": "Normandy, France, 12th Century",
        "source_note": "Pont-l'Évêque is one of the oldest Norman cheeses, possibly dating to the 12th century. It was originally called 'Angelot' and is named after the market town where it was sold.",
        "description": "Classic Norman washed-rind cheese with a golden crust and creamy, pungent interior - one of France's oldest cheeses.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "Norman breeds preferred"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp", "prep_note": "for white surface mold"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "light brine", "quantity": "1", "unit": "cup", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter, P. candidum, and B. linens. Stir well and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1 hour until firm curd forms."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Gently ladle curds into square molds (traditional shape is square)."},
            {"step": 6, "text": "Let drain at room temperature for 24 hours, flipping every 4-6 hours."},
            {"step": 7, "text": "Unmold and salt all surfaces. Let dry for 24 hours."},
            {"step": 8, "text": "Transfer to aging space at 55°F and 95% humidity."},
            {"step": 9, "text": "Allow white mold to develop for 1 week."},
            {"step": 10, "text": "Begin washing with light brine every 2-3 days. The rind will turn golden-orange."},
            {"step": 11, "text": "Continue aging and washing for 4-6 weeks until interior is soft and bulging."}
        ],
        "temperature": "90°F make, 55°F aging",
        "notes": [
            "The square shape is traditional and distinguishes it from round Norman cheeses",
            "Ripe Pont-l'Évêque should bulge slightly and feel soft throughout",
            "The rind is edible but very pungent; many prefer to remove it",
            "Traditional pairing is with Calvados (Norman apple brandy) and crusty bread"
        ],
        "tags": ["cheese", "traditional", "french", "normandy", "washed-rind", "pont-leveque", "12th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-reblochon-savoie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Reblochon (Savoie)",
        "category": "mains",
        "attribution": "Savoie, France, 13th Century",
        "source_note": "Reblochon originated in the Aravis Mountains of Savoie. The name comes from 're-blocher' (to milk again), as farmers would partially milk cows for the landlord's inspection, then fully milk them later to make this rich cheese from the creamier second milking.",
        "description": "Buttery French Alpine cheese with a washed rind and supple texture, essential for Tartiflette - born from 13th-century tax evasion.",
        "servings_yield": "About 1 lb",
        "prep_time": "2 hours",
        "cook_time": "4-6 weeks aging",
        "total_time": "4-6 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "high-fat milk preferred"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup", "prep_note": "to simulate rich 'second milking'"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp", "prep_note": "for washed rind"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "light brine", "quantity": "1", "unit": "cup", "prep_note": "for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 96°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and B. linens. Stir well and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-40 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Stir gently for 10 minutes while maintaining 96°F."},
            {"step": 6, "text": "Drain whey and ladle curds into small round molds (traditional diameter is about 5 inches)."},
            {"step": 7, "text": "Let drain at room temperature for 6-8 hours, flipping every 2 hours."},
            {"step": 8, "text": "Unmold and rub with salt. Let dry for 24 hours."},
            {"step": 9, "text": "Transfer to aging cave at 55°F and 95% humidity."},
            {"step": 10, "text": "Wash with light brine every 2-3 days for 4-6 weeks."},
            {"step": 11, "text": "The rind should develop a pinkish-orange color. Interior should be supple but not runny."}
        ],
        "temperature": "96°F make, 55°F aging",
        "notes": [
            "Traditional Reblochon uses very fresh, still-warm milk from the second milking",
            "The casein disk on top identifies authentic Reblochon (green = farmhouse, red = dairy)",
            "Essential for Tartiflette - a Savoyard potato gratin with Reblochon and lardons",
            "Properly aged Reblochon is supple throughout with no runny center"
        ],
        "tags": ["cheese", "traditional", "french", "savoie", "alpine", "washed-rind", "reblochon", "13th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-epoisses-burgundy",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Époisses (Burgundy)",
        "category": "mains",
        "attribution": "Époisses, Burgundy, France, 16th Century",
        "source_note": "Époisses was developed by Cistercian monks in the village of Époisses in Burgundy around the 16th century. It was revived in the 1950s after nearly disappearing. Napoleon reportedly called it 'the king of cheeses.'",
        "description": "Legendarily pungent Burgundian cheese washed with Marc de Bourgogne, with a sticky orange rind and spoonable, intensely flavored interior.",
        "servings_yield": "About 12 oz",
        "prep_time": "2 hours",
        "cook_time": "6-8 weeks aging",
        "total_time": "6-8 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon", "prep_note": ""},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "Brevibacterium linens", "quantity": "1/8", "unit": "tsp", "prep_note": "for the signature orange rind"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp", "prep_note": ""},
            {"item": "Marc de Bourgogne or brandy", "quantity": "1/2", "unit": "cup", "prep_note": "for washing"},
            {"item": "light brine", "quantity": "1", "unit": "cup", "prep_note": "mixed with Marc for washing"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter and B. linens. Stir well and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1.5-2 hours until very soft curd forms."},
            {"step": 4, "text": "Do NOT cut the curd. Gently ladle large curds into round molds."},
            {"step": 5, "text": "Let drain at room temperature for 48 hours, flipping gently every 8-12 hours."},
            {"step": 6, "text": "Unmold and salt the surface lightly. Let dry for 24 hours."},
            {"step": 7, "text": "Transfer to humid aging space (55°F, 95%+ humidity)."},
            {"step": 8, "text": "Mix brine with Marc de Bourgogne (about 50/50)."},
            {"step": 9, "text": "Wash the cheese with the Marc/brine mixture every day for first week, then every 2 days."},
            {"step": 10, "text": "Gradually increase the proportion of Marc in the wash as aging progresses."},
            {"step": 11, "text": "Age for 6-8 weeks until rind is sticky, bright orange, and cheese is soft throughout."}
        ],
        "temperature": "86°F make, 55°F aging",
        "notes": [
            "Époisses is so pungent it's banned on French public transport",
            "The Marc de Bourgogne (grape brandy) wash is essential for authentic flavor",
            "Ripe Époisses should be almost spoonable - serve in its wooden box",
            "The frequent washing develops the characteristic sticky orange rind",
            "If Marc is unavailable, substitute another grape brandy or even white wine"
        ],
        "tags": ["cheese", "traditional", "french", "burgundy", "washed-rind", "epoisses", "16th-century", "pungent"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-comte-jura",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Comté (Franche-Comté)",
        "category": "mains",
        "attribution": "Franche-Comté, France, 12th Century",
        "source_note": "Comté has been made in the Jura Mountains of eastern France since at least the 12th century. It was traditionally made in 'fruitières' (cooperative dairies) because the large wheels required milk from multiple farms.",
        "description": "France's favorite cheese - a complex, nutty Alpine wheel with notes of butter, fruit, and hazelnut that develop over long aging.",
        "servings_yield": "About 2 lb",
        "prep_time": "4 hours",
        "cook_time": "4-24 months aging",
        "total_time": "4-24 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "from Montbéliarde or Simmental cows traditionally"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp", "prep_note": ""},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "if using pasteurized milk"},
            {"item": "cheese salt", "quantity": "as needed", "unit": "", "prep_note": "for brining"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 93°F. Add calcium chloride if using pasteurized milk."},
            {"step": 2, "text": "Add starter culture, stir well, and ripen for 30 minutes."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 30-35 minutes until clean break."},
            {"step": 4, "text": "Cut curd into 1/4-inch cubes (very small). Let rest 5 minutes."},
            {"step": 5, "text": "Stir while slowly raising temperature to 130°F over 30-40 minutes."},
            {"step": 6, "text": "Hold at 130°F for 30-45 minutes, stirring constantly, until curds are very small and firm."},
            {"step": 7, "text": "Transfer curds to a large cloth-lined mold under the whey (traditional method)."},
            {"step": 8, "text": "Press immediately at 20 lbs, increasing to 50 lbs over 24 hours with several flips."},
            {"step": 9, "text": "Brine for 24-48 hours in saturated salt solution."},
            {"step": 10, "text": "Transfer to cool cellar at 55°F and 95% humidity."},
            {"step": 11, "text": "Rub with brine and turn daily for first month, then weekly."},
            {"step": 12, "text": "Age minimum 4 months; 12-24 months for full flavor development."}
        ],
        "temperature": "93°F start, 130°F cook, 55°F aging",
        "notes": [
            "Traditional Comté wheels weigh 80-100 lbs - scale up significantly for authentic results",
            "The high cooking temperature and small curd cut create Comté's dense, smooth texture",
            "Summer Comté tends to be fruitier; winter Comté more nutty",
            "Look for tyrosine crystals in well-aged wheels - a sign of proper aging"
        ],
        "tags": ["cheese", "traditional", "french", "jura", "alpine", "comte", "aged-cheese", "12th-century"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-cabrales-spanish-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Cabrales (Asturian Blue)",
        "category": "mains",
        "attribution": "Asturias, Spain, Ancient",
        "source_note": "Cabrales has been made in the Picos de Europa mountains of Asturias for centuries. It's traditionally aged in natural limestone caves where wild Penicillium strains create its intense blue veining.",
        "description": "Spain's most famous blue cheese, intensely pungent and creamy, traditionally aged in mountain caves with wild molds.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 hours",
        "cook_time": "2-6 months aging",
        "total_time": "2-6 months",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "1", "unit": "gallon", "prep_note": "or mixed milk"},
            {"item": "raw goat's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional, traditional"},
            {"item": "raw sheep's milk", "quantity": "1/2", "unit": "gallon", "prep_note": "optional, traditional"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": ""},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp", "prep_note": "for blue veining"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix milks (any combination - traditional uses all three). Heat to 86°F."},
            {"step": 2, "text": "Add starter and P. roqueforti. Stir well and ripen for 1 hour."},
            {"step": 3, "text": "Add diluted rennet, stir gently. Let set 1-1.5 hours until soft but firm curd."},
            {"step": 4, "text": "Cut curd into 1-inch cubes (larger than most blue cheeses). Let rest 10 minutes."},
            {"step": 5, "text": "Gently stir curds for 30 minutes at 86°F. Curds should remain large and soft."},
            {"step": 6, "text": "Drain whey and ladle curds into cylindrical molds. Do not press."},
            {"step": 7, "text": "Let drain at room temperature for 24-48 hours, flipping every 6-8 hours."},
            {"step": 8, "text": "Unmold and rub all surfaces with salt. Repeat salting over 3-4 days."},
            {"step": 9, "text": "Transfer to cool, humid cave or aging space (45-50°F, 90%+ humidity)."},
            {"step": 10, "text": "After 2 weeks, pierce the cheese with thick needles to allow air penetration for blue development."},
            {"step": 11, "text": "Age for 2-6 months. The rind should develop wild molds; the interior should be heavily veined with blue."}
        ],
        "temperature": "86°F make, 45-50°F aging",
        "notes": [
            "Traditional Cabrales uses a mix of cow, goat, and sheep milk - proportions vary by season",
            "The cool, humid limestone caves of Asturias provide wild Penicillium strains",
            "Cabrales is wrapped in maple or sycamore leaves traditionally; now often foil-wrapped",
            "The flavor is intensely sharp, salty, and pungent - not for the faint of heart",
            "Pairs traditionally with Asturian cider"
        ],
        "tags": ["cheese", "traditional", "spanish", "asturian", "blue-cheese", "cabrales", "cave-aged", "ancient"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "traditional-lancashire-english",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Traditional Lancashire Cheese",
        "category": "mains",
        "attribution": "Lancashire, England, 13th Century",
        "source_note": "Lancashire cheese has been made in the English county of Lancashire since at least the 13th century. Unique among English cheeses, it's traditionally made from curds from two or three consecutive days' milkings.",
        "description": "Buttery, crumbly English cheese made from mixed-day curds, with a fresh, tangy flavor that's perfect for toasting.",
        "servings_yield": "About 2 lb",
        "prep_time": "3 days (multi-day curd)",
        "cook_time": "1-6 months aging",
        "total_time": "1-6 months",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons", "prep_note": "for each day, need 3 days total"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp", "prep_note": "per day"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp", "prep_note": "per day, diluted"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp", "prep_note": "per day if using pasteurized"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp", "prep_note": "non-iodized"}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Heat milk to 86°F. Add calcium chloride if needed. Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes. Cut curd into 1/2-inch cubes."},
            {"step": 3, "text": "Stir gently, raise to 92°F over 30 minutes. Drain and press curds lightly overnight at 70°F."},
            {"step": 4, "text": "DAY 2: Repeat steps 1-3 with fresh milk, creating a second batch of curds."},
            {"step": 5, "text": "Mill Day 1 curds into small pieces. Add some salt. Store wrapped in cloth."},
            {"step": 6, "text": "DAY 3: Repeat steps 1-3 with fresh milk, creating a third batch of curds."},
            {"step": 7, "text": "Mill Day 2 curds. Now combine all three days' curds: Day 1, Day 2, and Day 3 (fresh)."},
            {"step": 8, "text": "Add remaining salt and mix all curds thoroughly."},
            {"step": 9, "text": "Pack mixed curds firmly into cloth-lined mold."},
            {"step": 10, "text": "Press at 20 lbs for 6 hours. Flip and press at 40 lbs for 24 hours."},
            {"step": 11, "text": "Air dry 4-5 days. Cloth-bind with butter or lard."},
            {"step": 12, "text": "Age at 55°F: 'Creamy' Lancashire 4-8 weeks; 'Tasty' Lancashire 4-6 months."}
        ],
        "temperature": "86-92°F make, 55°F aging",
        "notes": [
            "The multi-day curd process is unique to Lancashire and creates its distinctive texture",
            "Young 'Creamy' Lancashire is soft, buttery, and mild",
            "Aged 'Tasty' Lancashire is firmer, crumblier, with a stronger flavor",
            "Lancashire is the best cheese for Welsh Rarebit due to its melting properties",
            "Modern 'New Lancashire' uses single-day curds and lacks traditional character"
        ],
        "tags": ["cheese", "traditional", "english", "lancashire", "territorial-cheese", "13th-century", "multi-day-curd"],
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
