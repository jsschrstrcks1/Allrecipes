#!/usr/bin/env python3
"""Add comprehensive Scandinavian cheese recipes to the cheese category."""

import json

SCANDINAVIAN_CHEESE_RECIPES = [
    # === NORWEGIAN CHEESES ===
    {
        "id": "norwegian-gammelost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gammelost (Norwegian Old Cheese)",
        "category": "cheese",
        "attribution": "Traditional Norwegian cheese",
        "source_note": "Ancient Norwegian cheese dating back to Viking times, made with sour skim milk.",
        "description": "One of Norway's oldest cheeses, Gammelost ('old cheese') is a pungent, granular cheese made from soured skim milk and ripened with mold. Its sharp, intense flavor is beloved in traditional Norwegian cuisine.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "skim milk", "quantity": "2", "unit": "gallons"},
            {"item": "cultured buttermilk", "quantity": "2", "unit": "cups"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "Mucor mold culture (or wild mold)", "quantity": "1/8", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine skim milk and buttermilk. Let sour at room temperature for 24-48 hours until thickened."},
            {"step": 2, "text": "Heat soured milk to 140°F (60°C) slowly, stirring gently. Curds will form."},
            {"step": 3, "text": "Remove from heat, add rennet, and let set 30 minutes."},
            {"step": 4, "text": "Drain curds thoroughly in cheesecloth. The texture should be crumbly and dry."},
            {"step": 5, "text": "Mix salt into curds. Pack into molds without pressing."},
            {"step": 6, "text": "Dust surface with Mucor mold culture or place in humid environment for wild mold."},
            {"step": 7, "text": "Age at 55-60°F (13-16°C) and 85% humidity for 4-6 weeks."},
            {"step": 8, "text": "Turn every few days. Mold should cover entire surface by week 2."},
            {"step": 9, "text": "When ripe, interior will be golden-brown with granular texture."}
        ],
        "temperature": "140°F (60°C)",
        "notes": [
            "Viking-era cheese, one of the oldest in Scandinavia",
            "Traditionally made with naturally soured milk",
            "Very low fat due to skim milk base",
            "Intense, pungent flavor - an acquired taste",
            "Often served with flatbread and butter"
        ],
        "tags": ["cheese", "Norwegian", "aged", "mold-ripened", "skim milk", "traditional", "Viking"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "norwegian-pultost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pultost (Norwegian Soft Fermented Cheese)",
        "category": "cheese",
        "attribution": "Traditional Norwegian cheese",
        "source_note": "Traditional soft cheese from central Norway, often flavored with caraway.",
        "description": "A soft, spreadable Norwegian cheese made from soured skim milk curds. Pultost has a distinctive tangy flavor and is traditionally seasoned with caraway seeds. Popular on dark rye bread.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1.5 hours",
        "total_time": "3-5 days fermentation",
        "ingredients": [
            {"item": "skim milk", "quantity": "1", "unit": "gallon"},
            {"item": "cultured buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1.5", "unit": "tsp"},
            {"item": "cream (optional, for richness)", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine skim milk and buttermilk. Let sour at room temperature 24-36 hours."},
            {"step": 2, "text": "Heat slowly to 110°F (43°C) until curds separate from whey."},
            {"step": 3, "text": "Drain curds in cheesecloth for several hours until quite dry."},
            {"step": 4, "text": "Crumble curds into a bowl. Mix in salt and caraway seeds."},
            {"step": 5, "text": "Pack into a crock or jar. Cover loosely."},
            {"step": 6, "text": "Let ferment at room temperature 3-5 days, stirring daily."},
            {"step": 7, "text": "When soft and spreadable with tangy aroma, it's ready."},
            {"step": 8, "text": "Mix in cream if desired for smoother texture. Refrigerate to stop fermentation."}
        ],
        "temperature": "110°F (43°C)",
        "notes": [
            "Traditional farm cheese from Hedmark and Oppland regions",
            "Caraway is the classic flavoring, but cumin can substitute",
            "The longer fermentation, the stronger the flavor",
            "Best spread on Norwegian crispbread or dark rye",
            "Low-fat cheese due to skim milk base"
        ],
        "tags": ["cheese", "Norwegian", "soft", "fermented", "caraway", "spreadable", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "norwegian-nokkelost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Nokkelost (Norwegian Caraway Cheese)",
        "category": "cheese",
        "attribution": "Traditional Norwegian cheese",
        "source_note": "Classic Norwegian cheese with caraway and cloves, inspired by Dutch Leyden.",
        "description": "A semi-hard Norwegian cheese flavored with caraway seeds and cloves. Based on Dutch Leyden cheese traditions, Nokkelost ('key cheese') features distinctive spice patterns throughout.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "caraway seeds", "quantity": "2", "unit": "tbsp"},
            {"item": "whole cloves, crushed", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter culture, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Remove 1/3 whey. Add warm water to maintain temperature. Stir 20 minutes."},
            {"step": 6, "text": "Drain curds. Mix in caraway seeds, crushed cloves, and salt."},
            {"step": 7, "text": "Press at 15 lbs for 1 hour, flip, then 30 lbs for 12 hours."},
            {"step": 8, "text": "Brine 12 hours in saturated solution."},
            {"step": 9, "text": "Age at 55°F (13°C) and 80% humidity for 2-3 months."}
        ],
        "temperature": "86-100°F (30-38°C)",
        "notes": [
            "Name means 'key cheese' - traditional molds were key-shaped",
            "Inspired by Dutch Leyden cheese brought by traders",
            "Cloves add warmth that complements the caraway",
            "Often served with dark bread and aquavit",
            "Look for even spice distribution when cutting"
        ],
        "tags": ["cheese", "Norwegian", "semi-hard", "spiced", "caraway", "cloves", "Dutch-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === DANISH CHEESES ===
    {
        "id": "danish-blue-danablu",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Danish Blue (Danablu)",
        "category": "cheese",
        "attribution": "Traditional Danish cheese",
        "source_note": "Denmark's famous blue cheese, developed in the early 20th century.",
        "description": "Denmark's world-renowned blue cheese, Danablu is creamy and sharp with distinctive blue-green veining. Milder and creamier than Roquefort, it's become one of the world's most popular blue cheeses.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "8-12 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 86°F (30°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Let rest undisturbed 15 minutes."},
            {"step": 4, "text": "Gently ladle curds into molds, layering with salt. Do not press."},
            {"step": 5, "text": "Drain at room temperature 24-48 hours, flipping every 6-8 hours."},
            {"step": 6, "text": "Pierce cheese with sterilized skewer: create grid of holes on all sides (about 50 holes)."},
            {"step": 7, "text": "Age at 50°F (10°C) and 95% humidity for 8-12 weeks."},
            {"step": 8, "text": "Blue veining should appear by week 3-4 and spread throughout."},
            {"step": 9, "text": "Wrap in foil after 6 weeks to control rind development."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Developed by Marius Boel in 1927 as Danish answer to Roquefort",
            "PGI protected in EU since 2003",
            "Creamier and milder than French blue cheeses",
            "Adding cream creates the characteristic richness",
            "Excellent crumbled over salads or with fruit"
        ],
        "tags": ["cheese", "Danish", "blue cheese", "mold-ripened", "creamy", "PGI"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "danish-esrom",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Esrom (Danish Washed-Rind Cheese)",
        "category": "cheese",
        "attribution": "Traditional Danish cheese",
        "source_note": "Medieval recipe revived from Esrom monastery, with pungent washed rind.",
        "description": "A semi-soft Danish washed-rind cheese originally made by monks at Esrom Abbey. Rich, buttery interior with a pungent aroma from the washed rind. Full-flavored but approachable.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "light brine for washing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Stir at temperature 20 minutes until curds firm slightly."},
            {"step": 6, "text": "Drain and ladle into rectangular molds. Light press for 30 minutes."},
            {"step": 7, "text": "Flip and press at 10 lbs for 6-8 hours."},
            {"step": 8, "text": "Brine 8 hours, then dry 2 days."},
            {"step": 9, "text": "Age at 55°F (13°C) and 95% humidity for 6-8 weeks. Wash rind with brine every 2-3 days."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Originally made by Cistercian monks at Esrom Abbey in 12th century",
            "Recipe was lost and revived in 1951",
            "The rind smells stronger than the cheese tastes",
            "Rectangular shape is traditional",
            "Pairs well with dark Danish rye bread"
        ],
        "tags": ["cheese", "Danish", "washed-rind", "semi-soft", "monastery", "pungent"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "danish-maribo",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maribo (Danish Semi-Hard Cheese)",
        "category": "cheese",
        "attribution": "Traditional Danish cheese",
        "source_note": "Named after the town of Maribo on Lolland island, a classic Danish table cheese.",
        "description": "A semi-hard Danish cheese with irregular small holes and a mild, slightly acidic flavor. Named after the town of Maribo, it's one of Denmark's most popular everyday cheeses.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until firm."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Remove 1/3 whey. Add warm water gradually while stirring 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 minutes, flip, 25 lbs for 8-12 hours."},
            {"step": 7, "text": "Brine 12 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for 2-4 months."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Named after town on Lolland island, south of Zealand",
            "Similar to Gouda but with higher acidity",
            "The washed-curd technique gives mild flavor",
            "Small irregular holes develop naturally",
            "Popular slicing cheese for Danish smørrebrød"
        ],
        "tags": ["cheese", "Danish", "semi-hard", "washed-curd", "table cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "danish-samso",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Samso (Danish Swiss-Style Cheese)",
        "category": "cheese",
        "attribution": "Traditional Danish cheese",
        "source_note": "Denmark's national cheese, developed on Samso island in the 19th century.",
        "description": "Denmark's national cheese, originally developed by Swiss cheesemakers on Samso island. Features characteristic eyes, sweet nutty flavor, and firm texture. One of Denmark's most exported cheeses.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add thermophilic starter and P. shermanii, ripen 15 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 115°F (46°C) over 40 minutes while stirring continuously."},
            {"step": 5, "text": "Hold at temperature, stirring until curds are firm, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 20 lbs for 30 min, flip, 35 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine 24 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2 weeks, then move to 65-68°F (18-20°C) for 3 weeks for eye development, then return to 55°F for 2-3 more months."}
        ],
        "temperature": "90-115°F (32-46°C)",
        "notes": [
            "Swiss cheesemakers invited to Samso island in 1800s to develop cheese industry",
            "Denmark's national cheese, essential for traditional dishes",
            "The warm room period allows propioni bacteria to create eyes",
            "Mild, sweet flavor makes it universally appealing",
            "Used in classic Danish cheese platters"
        ],
        "tags": ["cheese", "Danish", "Swiss-style", "semi-hard", "eye cheese", "national cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SWEDISH CHEESES ===
    {
        "id": "swedish-vasterbottenost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Vasterbottenost (Swedish Aged Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swedish cheese",
        "source_note": "Prestigious Swedish cheese from Vasterbotten province, aged minimum 14 months.",
        "description": "Sweden's most prized cheese, Vasterbottenost has a complex, granular texture with distinctive bitter-sweet notes. Only produced in Vasterbotten province, it's Sweden's answer to Parmesan.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "14-24 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add both cultures, ripen 30 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "The key Vasterbotten technique: heat and cool repeatedly. Heat to 100°F, cool to 95°F, heat to 105°F, cool to 100°F, over 1 hour with constant stirring."},
            {"step": 5, "text": "Final temperature 118°F (48°C). Stir until curds are very firm."},
            {"step": 6, "text": "Drain and press at 30 lbs for 1 hour, flip, 45 lbs for 24 hours."},
            {"step": 7, "text": "Brine 48 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for minimum 14 months, up to 24 months. Turn weekly."}
        ],
        "temperature": "90-118°F (32-48°C)",
        "notes": [
            "Only authentic when made in Vasterbotten province",
            "The heating/cooling technique is the 'secret' to its flavor",
            "Minimum 14 months aging required for proper flavor development",
            "Distinctive bitter-sweet, almost truffle-like notes",
            "Essential for Swedish crayfish parties and Midsummer"
        ],
        "tags": ["cheese", "Swedish", "hard", "aged", "granular", "premium", "Vasterbotten"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "swedish-herrgardost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Herrgardsost (Swedish Manor Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swedish cheese",
        "source_note": "Swedish estate cheese with small eyes, meaning 'manor house cheese'.",
        "description": "A mild Swedish cheese with small round eyes, traditionally made on large estates. Herrgardsost ('manor cheese') has a buttery, nutty flavor and smooth texture, making it Sweden's most popular table cheese.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add mesophilic starter and P. shermanii, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 104°F (40°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Hold temperature and stir until curds firm, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 30 lbs for 12 hours."},
            {"step": 7, "text": "Brine 18-24 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 1 month, then 60-65°F (16-18°C) for 2 weeks for eyes, then return to 55°F for 2-5 more months."}
        ],
        "temperature": "88-104°F (31-40°C)",
        "notes": [
            "Name means 'manor house cheese' - made on Swedish estates",
            "Sweden's most popular cheese for everyday eating",
            "Small eyes are characteristic - like a milder Swiss",
            "Warm room period essential for proper eye development",
            "Perfect for Swedish open-faced sandwiches"
        ],
        "tags": ["cheese", "Swedish", "semi-hard", "eye cheese", "mild", "table cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "swedish-prastost",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Prastost (Swedish Priest's Cheese)",
        "category": "cheese",
        "attribution": "Traditional Swedish cheese",
        "source_note": "Historic Swedish cheese once given to clergy as tithe payment.",
        "description": "A semi-hard Swedish cheese with a complex, slightly tangy flavor. Prastost ('priest's cheese') was traditionally given to clergy as part of the tithe, representing the finest cheese a farm could produce.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "whiskey or aquavit (for washing)", "quantity": "1/4", "unit": "cup"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Stir at temperature until curds firm, about 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 25 lbs for 10-12 hours."},
            {"step": 7, "text": "Brine 12 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-3 months. Wash rind weekly with whiskey or aquavit mixed with brine."}
        ],
        "temperature": "90-100°F (38°C)",
        "notes": [
            "Historically given to clergy as part of the tithe",
            "The whiskey wash adds distinctive flavor to the rind",
            "Full, complex flavor from the washed rind technique",
            "More flavorful than Herrgardsost but not as strong as aged varieties",
            "Traditional for Swedish cheese boards and holiday tables"
        ],
        "tags": ["cheese", "Swedish", "semi-hard", "washed-rind", "historical", "priest's cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === FINNISH CHEESES ===
    {
        "id": "finnish-leipajuusto",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Leipajuusto (Finnish Bread Cheese)",
        "category": "cheese",
        "attribution": "Traditional Finnish cheese",
        "source_note": "Traditional Finnish squeaky cheese, grilled until browned, served with cloudberry jam.",
        "description": "Finland's famous 'bread cheese' gets its name from its flat, bread-like appearance and the charred spots from grilling. Fresh, mild, and slightly squeaky, it's traditionally served warm with cloudberry jam and coffee.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "30 min",
        "total_time": "1-2 hours (fresh cheese)",
        "ingredients": [
            {"item": "whole cow's milk (or traditionally reindeer milk)", "quantity": "1", "unit": "gallon"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk and cream to 95°F (35°C). Add salt."},
            {"step": 2, "text": "Add rennet diluted in 1/4 cup water. Stir for 30 seconds, then stop."},
            {"step": 3, "text": "Let set undisturbed 30-45 minutes until firm curd forms."},
            {"step": 4, "text": "Cut curd into large sections. Gently ladle into a flat, round mold (traditionally birch bark)."},
            {"step": 5, "text": "Press lightly to form a flat disc about 1-inch thick. Drain 30 minutes."},
            {"step": 6, "text": "Preheat broiler. Place cheese on oven-safe pan lined with parchment."},
            {"step": 7, "text": "Broil 4-6 inches from heat for 5-8 minutes until golden brown spots appear."},
            {"step": 8, "text": "Flip carefully and brown the other side."},
            {"step": 9, "text": "Serve warm, cut into wedges, with cloudberry jam or lingonberry preserves."}
        ],
        "temperature": "95°F (35°C) for curd, broiler for finishing",
        "notes": [
            "Also called Juustoleipa - both names mean 'bread cheese'",
            "Traditional in Lapland, originally made with reindeer milk",
            "The broiling creates characteristic dark spots and squeaky texture",
            "Can be stored frozen and reheated in oven or microwave",
            "The 'squeak' when you bite it is a sign of freshness"
        ],
        "tags": ["cheese", "Finnish", "fresh", "grilled", "bread cheese", "Lapland", "squeaky cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "finnish-aura-blue",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Aura (Finnish Blue Cheese)",
        "category": "cheese",
        "attribution": "Traditional Finnish cheese",
        "source_note": "Finland's signature blue cheese, creamier and milder than Danish Blue.",
        "description": "Finland's most famous blue cheese, Aura is creamy, mild, and approachable. Less sharp than other blue cheeses, it has a buttery texture that spreads easily and melts beautifully.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "1.5", "unit": "cups"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 86°F (30°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 15 minutes without stirring."},
            {"step": 4, "text": "Gently ladle curds into cylindrical molds. Do not press."},
            {"step": 5, "text": "Drain at room temperature 24-36 hours, flipping every 6 hours."},
            {"step": 6, "text": "Salt surfaces. Let rest 24 hours."},
            {"step": 7, "text": "Pierce with sterilized skewer: 30-40 holes per side."},
            {"step": 8, "text": "Age at 50°F (10°C) and 95% humidity for 6-8 weeks."},
            {"step": 9, "text": "Wrap in foil after 4 weeks for creamier texture."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Finland's most popular blue cheese since 1934",
            "Extra cream creates signature buttery texture",
            "Milder than Danish Blue, more approachable for newcomers",
            "Excellent melted on steaks or in cream sauces",
            "Named after word meaning 'sun plow' - a natural phenomenon in Finland"
        ],
        "tags": ["cheese", "Finnish", "blue cheese", "mold-ripened", "creamy", "mild blue"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "finnish-oltermanni",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Oltermanni (Finnish Mild Cheese)",
        "category": "cheese",
        "attribution": "Traditional Finnish cheese",
        "source_note": "Finland's most popular everyday cheese, mild and versatile.",
        "description": "Finland's best-selling cheese, Oltermanni is a mild, semi-soft cheese with a smooth, creamy texture. Its gentle flavor makes it perfect for everyday use on bread, in cooking, or for children.",
        "servings_yield": "About 2 lbs",
        "prep_time": "40 min",
        "cook_time": "2.5 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 1/3 whey. Add warm water slowly while stirring for 30 minutes."},
            {"step": 5, "text": "Target temperature 98°F (37°C) by end of stirring."},
            {"step": 6, "text": "Drain and press at 10 lbs for 30 min, flip, 20 lbs for 6-8 hours."},
            {"step": 7, "text": "Brine 8-10 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 4-6 weeks."}
        ],
        "temperature": "88-98°F (31-37°C)",
        "notes": [
            "Finland's most consumed cheese for over 30 years",
            "Washed-curd technique removes lactose for mild flavor",
            "Name is old Finnish word for 'village elder'",
            "Comes in various fat contents - 17% to 29%",
            "Perfect introduction cheese for children"
        ],
        "tags": ["cheese", "Finnish", "semi-soft", "mild", "washed-curd", "everyday cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === BONUS: ICELANDIC CHEESE ===
    {
        "id": "icelandic-skyr-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Skyr (Icelandic Cultured Dairy)",
        "category": "cheese",
        "attribution": "Traditional Icelandic cheese",
        "source_note": "Ancient Viking dairy product, technically a fresh cheese though often eaten like yogurt.",
        "description": "Iceland's national dairy product, Skyr is technically a fresh acid-set cheese though it has the consistency of thick yogurt. High in protein and tangy in flavor, it's been made in Iceland since Viking times.",
        "servings_yield": "About 3 cups",
        "prep_time": "20 min",
        "cook_time": "15 min",
        "total_time": "12-24 hours incubation",
        "ingredients": [
            {"item": "skim milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "heavy cream (optional)", "quantity": "1/4", "unit": "cup"},
            {"item": "plain skyr or Greek yogurt (as starter)", "quantity": "2", "unit": "tbsp"},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat skim milk to 185°F (85°C) and hold for 5 minutes to denature proteins."},
            {"step": 2, "text": "Cool milk to 110°F (43°C)."},
            {"step": 3, "text": "Whisk in skyr or Greek yogurt starter until smooth."},
            {"step": 4, "text": "Add 3 drops rennet diluted in 1 tbsp water. Stir briefly."},
            {"step": 5, "text": "Pour into clean container. Cover and keep at 110°F for 12-24 hours."},
            {"step": 6, "text": "When thick and tangy, line strainer with cheesecloth over bowl."},
            {"step": 7, "text": "Pour skyr into lined strainer. Drain 2-4 hours until very thick."},
            {"step": 8, "text": "Whisk until smooth. Add cream if desired for richer texture."},
            {"step": 9, "text": "Refrigerate. Serve with berries and honey, or use in recipes."}
        ],
        "temperature": "110°F (43°C) for incubation",
        "notes": [
            "Vikings brought skyr-making to Iceland around 900 AD",
            "Technically a cheese, not yogurt - uses rennet",
            "Skim milk is traditional - nearly fat-free",
            "Very high protein content compared to yogurt",
            "The whey (mysa) was traditionally used as a drink"
        ],
        "tags": ["cheese", "Icelandic", "fresh", "cultured", "Viking", "high-protein", "acid-set"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Scandinavian cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in SCANDINAVIAN_CHEESE_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"Skipping existing: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"Added: {recipe['title']}")
            added += 1

    data['recipes'] = recipes

    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Added: {added} recipes")
    print(f"Skipped (existing): {skipped}")
    print(f"Total recipes now: {len(recipes)}")


if __name__ == '__main__':
    add_recipes()
