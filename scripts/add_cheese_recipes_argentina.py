#!/usr/bin/env python3
"""Add comprehensive Argentine cheese recipes to the cheese category."""

import json

ARGENTINE_CHEESE_RECIPES = [
    # === CLASSIC ARGENTINE CHEESES ===
    {
        "id": "queso-cremoso-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Cremoso Argentino (Argentine Creamy Cheese)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentina's most popular table cheese, similar to Italian Crescenza.",
        "description": "Ultra-creamy, mild Argentine cheese that's spreadable when young and sliceable when aged slightly. The quintessential cheese for Argentine sandwiches and picadas.",
        "servings_yield": "About 2 lbs",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "1-3 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 86°F (30°C). Add starter culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set for 60-90 minutes until very soft curd forms."},
            {"step": 3, "text": "Cut curds into 1-inch cubes very gently. Let rest 15 minutes without stirring."},
            {"step": 4, "text": "Gently ladle curds into molds - do NOT press. Allow to drain naturally at room temperature."},
            {"step": 5, "text": "Flip every 2-3 hours for 12-24 hours until cheese holds its shape."},
            {"step": 6, "text": "Salt both surfaces lightly. Refrigerate."},
            {"step": 7, "text": "Age 1-3 weeks at 50-55°F (10-13°C) for slicing texture, or eat immediately for spreading."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Cremoso means 'creamy' - the name describes the texture perfectly",
            "Adding cream increases the fat content for extra richness",
            "Most popular cheese in Argentina, found in every home",
            "Perfect for picadas (Argentine cheese boards)"
        ],
        "tags": ["cheese", "Argentine", "soft", "creamy", "table cheese", "spreading cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-sardo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Sardo Argentino (Argentine Sardinian-Style)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine adaptation of Italian Pecorino Sardo, made with cow's milk.",
        "description": "Hard, sharp Argentine cheese inspired by Sardinian Pecorino. Made with cow's milk instead of sheep's, it's aged longer for a strong, granular texture perfect for grating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "6-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder (optional, for tang)", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and optional lipase, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 118°F (48°C) over 45 minutes, stirring continuously. This is key for hard cheese texture."},
            {"step": 5, "text": "Maintain temperature and stir until curds shrink and become firm, about 30-45 minutes more."},
            {"step": 6, "text": "Drain and press at 20 lbs for 1 hour, flip, then 40 lbs for 12 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for minimum 6 months, up to 2 years. Rub with olive oil monthly."}
        ],
        "temperature": "95-118°F (35-48°C)",
        "notes": [
            "Sardo means 'from Sardinia' - brought by Italian immigrants",
            "Cow's milk gives different flavor than original sheep's milk version",
            "Lipase adds characteristic 'piccante' sharpness",
            "Traditional for grating over pasta in Argentine-Italian households"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "hard", "grating", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-reggianito",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Reggianito (Argentine Parmesan)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of Parmigiano-Reggiano, smaller wheels aged less time.",
        "description": "Argentina's answer to Parmesan, made in smaller wheels with shorter aging. Granular, sharp, and perfect for grating, it's been produced since Italian immigration in the late 1800s.",
        "servings_yield": "About 3 lbs",
        "prep_time": "1 hour",
        "cook_time": "5 hours",
        "total_time": "6-18 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat part-skim milk to 95°F (35°C). Add starter and lipase, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into rice-sized pieces (as small as possible). Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 125°F (52°C) over 45 minutes while stirring constantly."},
            {"step": 5, "text": "Hold at 125°F and stir until curds squeak when pressed together, about 30 minutes more."},
            {"step": 6, "text": "Drain and press immediately at 40 lbs for 2 hours, flip, then 50 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 3 days, turning daily."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for 6-18 months. Brush and turn weekly."}
        ],
        "temperature": "95-125°F (35-52°C)",
        "notes": [
            "Reggianito is diminutive of Reggiano - 'little Reggiano'",
            "Smaller wheel size means faster aging than Italian original",
            "Part-skim milk is traditional for this style",
            "Argentina is one of world's largest producers of Parmesan-style cheese"
        ],
        "tags": ["cheese", "Argentine", "Parmesan-style", "hard", "grating", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-provolone-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Provolone Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine provolone for grilling, essential for asado.",
        "description": "Argentine provolone specifically made for grilling. When heated, it develops a crispy exterior while staying stretchy inside. No Argentine barbecue (asado) is complete without provoleta.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "lipase powder", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "dried oregano (for provoleta)", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 97°F (36°C). Add starter and lipase, ripen 45 minutes."},
            {"step": 2, "text": "Add rennet, let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Heat to 118°F (48°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds, let mat together for 15 minutes."},
            {"step": 6, "text": "Cut curd mass into strips. Place in 170°F (77°C) water until stretchy."},
            {"step": 7, "text": "Knead and stretch like mozzarella. Form into thick discs about 1-inch thick."},
            {"step": 8, "text": "Brine for 12 hours. Age at 55°F (13°C) for 2-3 months minimum."},
            {"step": 9, "text": "For provoleta: Slice into thick rounds, top with oregano, grill until golden and bubbly."}
        ],
        "temperature": "97-170°F (36-77°C)",
        "notes": [
            "Provoleta is provolone cut into rounds and grilled during asado",
            "The lipase gives the characteristic sharp flavor",
            "Must be thick enough to develop crispy crust while staying stretchy",
            "Oregano topping is traditional for grilling"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "pasta filata", "grilling", "asado"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-tybo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Tybo Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of Danish Samsø, popular for sandwiches.",
        "description": "Mild, semi-hard Argentine cheese based on Danish Samsø/Tilsit. Elastic texture with small irregular eyes, it's excellent for sandwiches and everyday eating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 30% of whey. Add warm water to bring temp to 100°F (38°C)."},
            {"step": 5, "text": "Stir gently for 30 minutes at 100°F."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 minutes, flip, 30 lbs for 6 hours."},
            {"step": 7, "text": "Brine 8 hours per pound in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 2-3 months."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Tybo derives from Tilsit by way of Danish cheesemaking traditions",
            "Washed-curd technique gives milder flavor",
            "Small eyes develop naturally from the culture",
            "One of Argentina's most consumed cheeses for everyday use"
        ],
        "tags": ["cheese", "Argentine", "Danish-style", "semi-hard", "washed-curd"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-fontina-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Fontina Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine adaptation of Italian Fontina Val d'Aosta.",
        "description": "Semi-soft Argentine cheese based on Italian Fontina. Excellent melting properties make it ideal for fondues and cooking. Mild, buttery flavor with earthy undertones.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 96°F (36°C). Add both starters, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 110°F (43°C) over 40 minutes while stirring gently."},
            {"step": 5, "text": "Continue stirring at 110°F until curds shrink and firm up, about 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 25 lbs for 8-12 hours."},
            {"step": 7, "text": "Brine for 12 hours in saturated solution."},
            {"step": 8, "text": "Age at 50°F (10°C) and 95% humidity for 3-4 months. Wash rind weekly with brine."}
        ],
        "temperature": "96-110°F (36-43°C)",
        "notes": [
            "Mixed cultures create complex flavor profile",
            "Washed rind develops earthy, mushroomy notes",
            "Excellent melting cheese - essential for fondue",
            "Keep humidity high during aging to prevent cracking"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "semi-soft", "washed-rind", "fondue"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-azul-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Azul Argentino (Argentine Blue Cheese)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine blue cheese inspired by Roquefort and Gorgonzola traditions.",
        "description": "Creamy Argentine blue cheese with distinctive veining. Less pungent than European blues, it's approachable for newcomers while satisfying aficionados. Perfect with Argentine Malbec.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Very gently ladle into molds without pressing."},
            {"step": 4, "text": "Drain naturally at room temperature, flipping every few hours for 24 hours."},
            {"step": 5, "text": "Salt all surfaces liberally. Let rest 24 hours."},
            {"step": 6, "text": "Pierce cheese with sterilized skewer in a grid pattern to allow air for blue mold development."},
            {"step": 7, "text": "Age at 50-55°F (10-13°C) and 95% humidity. Blue veins should appear within 2-3 weeks."},
            {"step": 8, "text": "Continue aging 2-3 months total, turning weekly."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Piercing allows oxygen to reach the interior for mold growth",
            "High humidity is critical - blue mold needs moisture",
            "Less salt than European blues gives milder flavor profile",
            "Pairs beautifully with Mendoza wines"
        ],
        "tags": ["cheese", "Argentine", "blue cheese", "mold-ripened", "cow's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-port-salut-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Port Salut Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of French Port-Salut, brought by Trappist monks.",
        "description": "Soft, creamy Argentine washed-rind cheese inspired by French Port-Salut. Mild and buttery with characteristic orange rind, it's one of Argentina's most refined table cheeses.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "2.5 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "light brine solution for washing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and B. linens, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Stir gently for 30 minutes, maintaining 86°F."},
            {"step": 5, "text": "Drain and ladle into molds without pressing. Drain 8-12 hours, flipping frequently."},
            {"step": 6, "text": "Lightly salt surfaces."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity. Wash rind with light brine every 2-3 days."},
            {"step": 8, "text": "Ready in 4-6 weeks when rind is orange and interior is creamy."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Trappist monks brought Port-Salut tradition to Argentina",
            "Regular rind washing develops flavor and orange color",
            "Very mild compared to stronger washed-rind cheeses",
            "Serve at room temperature for best flavor"
        ],
        "tags": ["cheese", "Argentine", "French-style", "washed-rind", "soft", "Trappist"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-gruyerette-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Gruyerette Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of Swiss Gruyère, made in smaller wheels.",
        "description": "Argentine Gruyère-style cheese with sweet, nutty flavor and small eyes. Smaller than Swiss originals, it ages faster while maintaining the characteristic complexity.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "4-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii (for eyes)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add thermophilic starter and P. shermanii, ripen 15 minutes."},
            {"step": 2, "text": "Raise temperature to 95°F (35°C). Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes - very small for this style."},
            {"step": 4, "text": "Slowly heat to 125°F (52°C) over 45 minutes while stirring constantly."},
            {"step": 5, "text": "Hold at 125°F, stirring until curds are very firm and shrunk, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 25 lbs for 30 min, flip, 40 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24-36 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) for first month, then move to 65°F (18°C) for 2 weeks (for eye development), then back to 55°F for remaining 3-5 months."}
        ],
        "temperature": "90-125°F (32-52°C)",
        "notes": [
            "Gruyerette is diminutive - 'little Gruyère'",
            "The warm room period allows propioni bacteria to create eyes",
            "Smaller wheel means shorter total aging time",
            "Excellent for fondue and gratins"
        ],
        "tags": ["cheese", "Argentine", "Swiss-style", "hard", "Alpine", "eye cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-pategrillo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Pategrillo (Young Pategras)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Younger version of Pategras, ready in weeks instead of months.",
        "description": "The young sibling of Pategras, aged only 3-4 weeks. Softer and milder than aged Pategras, it's Argentina's everyday slicing cheese for sandwiches and casual snacking.",
        "servings_yield": "About 2 lbs",
        "prep_time": "40 min",
        "cook_time": "2.5 hours",
        "total_time": "3-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly raise to 100°F (38°C) over 25 minutes while stirring."},
            {"step": 5, "text": "Remove 30% whey, add same-temp water. Stir 15 minutes."},
            {"step": 6, "text": "Drain and press at 10 lbs for 30 min, flip, 15 lbs for 4 hours."},
            {"step": 7, "text": "Brine 6 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) for only 3-4 weeks."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Pategrillo means 'little Pategras'",
            "Lighter pressing gives softer texture than aged version",
            "Perfect for when you can't wait 2-3 months",
            "Most popular everyday cheese in Buenos Aires"
        ],
        "tags": ["cheese", "Argentine", "Dutch-style", "semi-soft", "young cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-de-cabra-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso de Cabra Argentino (Argentine Goat Cheese)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine goat cheese from the Patagonian and Cuyo regions.",
        "description": "Fresh Argentine goat cheese from the mountain regions. Tangy, bright, and spreadable, it showcases the unique terroir of Argentine goat herds grazing on wild herbs.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days to 2 weeks",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 72°F (22°C) - barely warm."},
            {"step": 2, "text": "Add starter culture, let ripen 1 hour."},
            {"step": 3, "text": "Add just 2 drops rennet diluted in water. Stir gently."},
            {"step": 4, "text": "Cover and let set at room temperature 12-24 hours until thick curd forms."},
            {"step": 5, "text": "Gently ladle curds into cheesecloth-lined molds. Do not press."},
            {"step": 6, "text": "Drain at room temperature 24 hours, flipping occasionally."},
            {"step": 7, "text": "Salt surfaces lightly."},
            {"step": 8, "text": "Eat fresh within 2-3 days, or age at 50°F for up to 2 weeks."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Very little rennet - almost entirely acid-set",
            "Patagonian goat's milk has distinctive herbaceous notes",
            "Traditional in northern Argentine mountain communities",
            "Excellent crumbled over salads or spread on crusty bread"
        ],
        "tags": ["cheese", "Argentine", "goat cheese", "fresh", "chèvre-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-de-oveja-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso de Oveja Argentino (Argentine Sheep's Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Sheep's milk cheese from Patagonian sheep ranches.",
        "description": "Rich, complex Argentine sheep's milk cheese from Patagonia. The sheep graze on wild grasses and herbs, giving the cheese distinctive lanolin sweetness and buttery depth.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Stir at temperature until curds firm, about 20 minutes more."},
            {"step": 6, "text": "Drain and press at 10 lbs for 30 min, flip, 20 lbs for 8 hours."},
            {"step": 7, "text": "Brine 8 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-4 months. Rub with olive oil monthly."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Sheep's milk has higher fat and protein than cow's milk",
            "Patagonian terroir gives unique flavor profile",
            "Less common than cow's milk cheeses in Argentina",
            "Rich enough to pair with bold Malbec wines"
        ],
        "tags": ["cheese", "Argentine", "sheep's milk", "aged", "Patagonian"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-dambo-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Dambo Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine version of Danish Danbo cheese.",
        "description": "Mild, semi-soft Argentine cheese based on Danish Danbo. Buttery and smooth with small irregular eyes, it's a versatile table cheese popular throughout Argentina.",
        "servings_yield": "About 2 lbs",
        "prep_time": "40 min",
        "cook_time": "2.5 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 88°F (31°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 40 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Remove 30% whey. Add 95°F (35°C) water gradually while stirring for 30 minutes."},
            {"step": 5, "text": "Final temperature should reach 98°F (37°C)."},
            {"step": 6, "text": "Drain and press at 10 lbs for 30 min, flip, 20 lbs for 6 hours."},
            {"step": 7, "text": "Brine 6-8 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) for 5-8 weeks."}
        ],
        "temperature": "88-98°F (31-37°C)",
        "notes": [
            "Danish immigrants brought Danbo tradition to Argentina",
            "Washed-curd technique gives mild, sweet flavor",
            "Small eyes develop naturally during aging",
            "Popular for sandwiches and children's snacks"
        ],
        "tags": ["cheese", "Argentine", "Danish-style", "semi-soft", "washed-curd"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-colonia-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Colonia Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Swiss-style cheese from Swiss-German colonies in Entre Ríos.",
        "description": "Argentine Swiss-style cheese from the Swiss-German colonies of Entre Ríos province. Features characteristic large eyes and sweet, nutty flavor. Named for the colonial settlements that perfected it.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-5 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Propionibacterium shermanii", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add thermophilic starter and P. shermanii, ripen 20 minutes."},
            {"step": 2, "text": "Raise to 95°F (35°C). Add calcium chloride, then rennet. Let set 35 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 120°F (49°C) over 40 minutes while stirring."},
            {"step": 5, "text": "Hold at 120°F and stir until curds are firm, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 20 lbs for 30 min, flip, 35 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine 24 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2 weeks, then move to warm room 68-72°F (20-22°C) for 2-3 weeks for eye formation, then return to 55°F for 2-4 more months."}
        ],
        "temperature": "90-120°F (32-49°C)",
        "notes": [
            "Named for Swiss-German colonies of Entre Ríos province",
            "Warm room period crucial for signature large eyes",
            "One of Argentina's premium domestic cheeses",
            "Excellent for fondue and raclette-style dishes"
        ],
        "tags": ["cheese", "Argentine", "Swiss-style", "Alpine", "eye cheese", "colonial"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-mozzarella-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Mozzarella Argentino",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine mozzarella - essential for empanadas and pizza.",
        "description": "Argentine-style mozzarella, slightly drier than Italian original to better suit empanadas and fugazza pizza. The stretch is essential - no Argentine kitchen is without it.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup cool water. Add to cold milk, stir well."},
            {"step": 2, "text": "Heat milk to 90°F (32°C) while stirring gently."},
            {"step": 3, "text": "Add rennet diluted in 1/4 cup water. Stir for 30 seconds, then stop."},
            {"step": 4, "text": "Let set without disturbing for 5-10 minutes until clean break."},
            {"step": 5, "text": "Cut curds into 1-inch cubes. Let rest 5 minutes."},
            {"step": 6, "text": "Slowly heat to 105°F (41°C) while stirring gently."},
            {"step": 7, "text": "Drain whey. Heat water or whey to 175°F (80°C)."},
            {"step": 8, "text": "Add curds to hot water. Stretch and fold repeatedly until smooth and elastic, adding salt while kneading."},
            {"step": 9, "text": "Form into balls or blocks. Cool in ice water bath 15 minutes. Use fresh or refrigerate."}
        ],
        "temperature": "90-175°F (32-80°C)",
        "notes": [
            "Drier than Italian mozzarella for better melting on empanadas",
            "Citric acid method is faster than traditional culture method",
            "The stretch test: should pull into long strands without breaking",
            "Essential for Argentine pizza, which has more cheese than Italian style"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "pasta filata", "fresh", "pizza cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-roquefort-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Roquefort Argentino (Argentine Roquefort-Style)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Argentine blue cheese inspired by French Roquefort, using cow's milk.",
        "description": "Argentine interpretation of Roquefort using cow's milk instead of sheep's. Creamy, tangy, and boldly veined, it's aged in humidity-controlled caves in the Tandil region.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and P. roqueforti, ripen 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 90 minutes until very soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Very gently ladle into molds, layering salt between ladlefuls."},
            {"step": 4, "text": "Do not press. Drain at room temperature 3-4 days, flipping twice daily."},
            {"step": 5, "text": "When firm enough to handle, pierce with sterilized skewer: 40-50 holes per side."},
            {"step": 6, "text": "Age at 50°F (10°C) and 95% humidity for 3-4 months."},
            {"step": 7, "text": "Blue veining should be extensive by 6 weeks."},
            {"step": 8, "text": "Wrap in foil after 2 months to slow rind development while interior continues maturing."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Tandil region has natural caves ideal for blue cheese aging",
            "Cow's milk version is creamier than sheep's milk original",
            "Multiple piercings essential for extensive veining",
            "Traditional Argentine blue cheese since 1920s"
        ],
        "tags": ["cheese", "Argentine", "blue cheese", "Roquefort-style", "cave-aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-quartirolo-tandilense",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Quartirolo Tandilense",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Regional Italian-style cheese from Tandil, Buenos Aires province.",
        "description": "Soft, rindless cheese from the Tandil region, inspired by Italian Quartirolo. Fresh and tangy when young, it develops complexity with brief aging. Essential for Argentine pasta dishes.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "25 min",
        "cook_time": "2 hours",
        "total_time": "Fresh to 2 weeks",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, ripen 30 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Let set 40 minutes until soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently ladle curds into square molds without pressing."},
            {"step": 5, "text": "Drain at room temperature 12-24 hours, flipping every 4-6 hours."},
            {"step": 6, "text": "Salt all surfaces liberally."},
            {"step": 7, "text": "Eat fresh within 3-4 days, or age at 50°F (10°C) for up to 2 weeks."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Tandil is Argentina's artisanal cheese capital",
            "Square shape is traditional for this style",
            "Fresh version is soft and spreadable",
            "Aged version firms up and develops tang"
        ],
        "tags": ["cheese", "Argentine", "Italian-style", "soft", "fresh", "Tandil"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "queso-semi-duro-argentino",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso Semi-Duro Argentino (Semi-Hard Table Cheese)",
        "category": "cheese",
        "attribution": "Traditional Argentine cheese",
        "source_note": "Generic semi-hard cheese - the workhorse of Argentine dairy.",
        "description": "The everyday semi-hard cheese found in every Argentine home. Mild, sliceable, and versatile, it's the default cheese for sandwiches, cooking, and casual eating.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Continue stirring at temperature until curds firm, about 20 minutes."},
            {"step": 6, "text": "Drain and press at 15 lbs for 30 min, flip, 25 lbs for 8 hours."},
            {"step": 7, "text": "Brine 8 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) for 4-8 weeks."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "The generic Argentine cheese - no specific regional or ethnic origin",
            "Every dairy in Argentina makes their own version",
            "Mild enough for kids, versatile enough for cooking",
            "The cheese you buy when you just need 'cheese'"
        ],
        "tags": ["cheese", "Argentine", "semi-hard", "table cheese", "everyday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "dulce-de-leche-cheese-spread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Queso con Dulce (Cheese with Dulce de Leche)",
        "category": "cheese",
        "attribution": "Traditional Argentine combination",
        "source_note": "Classic Argentine pairing - fresh cheese with dulce de leche.",
        "description": "Not a cheese per se, but the quintessential Argentine cheese preparation. Fresh, mild cheese paired with dulce de leche creates the beloved 'vigilante' or 'queso y dulce' dessert.",
        "servings_yield": "4-6 servings",
        "prep_time": "15 min",
        "cook_time": "0",
        "total_time": "15 min plus cheese-making time",
        "ingredients": [
            {"item": "fresh queso fresco or cremoso", "quantity": "8", "unit": "oz"},
            {"item": "dulce de leche", "quantity": "1/2", "unit": "cup"},
            {"item": "walnuts (optional)", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Slice fresh cheese into 1/4-inch thick slices."},
            {"step": 2, "text": "Arrange cheese slices on serving plate."},
            {"step": 3, "text": "Top each slice with a generous spoonful of dulce de leche."},
            {"step": 4, "text": "Optionally garnish with chopped walnuts."},
            {"step": 5, "text": "Serve immediately as dessert or merienda (afternoon snack)."}
        ],
        "temperature": "Room temperature",
        "notes": [
            "Called 'vigilante' or 'Martín Fierro' after the gaucho epic poem",
            "Sweet-savory combination is beloved throughout Argentina",
            "Best with mild, creamy fresh cheese - not aged varieties",
            "Traditional ending to any Argentine asado (barbecue)"
        ],
        "tags": ["cheese", "Argentine", "dessert", "dulce de leche", "traditional pairing"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Argentine cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in ARGENTINE_CHEESE_RECIPES:
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
