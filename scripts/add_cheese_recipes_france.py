#!/usr/bin/env python3
"""Add comprehensive French cheese recipes to the cheese category."""

import json

FRENCH_CHEESE_RECIPES = [
    # === ALPINE MOUNTAIN CHEESES ===
    {
        "id": "artisan-french-comte",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Comté (Aged Alpine Cheese)",
        "category": "cheese",
        "attribution": "Traditional French Alpine cheese",
        "source_note": "AOC/AOP cheese from the Jura mountains, France's most consumed cheese.",
        "description": "Noble Alpine cheese with extraordinary complexity - fruity, nutty, and caramel notes that develop over long aging. Made in large wheels from raw milk of Montbéliarde cows grazing on mountain pastures.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1 hour",
        "cook_time": "5 hours",
        "total_time": "8-24 months aging",
        "ingredients": [
            {"item": "whole raw cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/2", "unit": "tsp"},
            {"item": "Propionibacterium shermanii (for eye development)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add thermophilic starter and P. shermanii, stir thoroughly."},
            {"step": 2, "text": "Ripen for 30 minutes. Temperature should remain stable."},
            {"step": 3, "text": "Add calcium chloride if using pasteurized milk. Add rennet diluted in cool water."},
            {"step": 4, "text": "Let set 30-40 minutes until clean break forms."},
            {"step": 5, "text": "Cut curds into tiny rice-sized pieces - this is critical for Comté's dense texture."},
            {"step": 6, "text": "Begin stirring gently and slowly raise temperature to 130°F (55°C) over 45 minutes."},
            {"step": 7, "text": "Hold at 130°F while stirring until curds are firm and squeaky, about 30 more minutes."},
            {"step": 8, "text": "Drain curds into large cloth-lined mold. Press at 25 lbs for 30 minutes."},
            {"step": 9, "text": "Flip and press at 40 lbs for 12 hours, then 50 lbs for another 12 hours."},
            {"step": 10, "text": "Brine in saturated salt solution for 48 hours, flipping daily."},
            {"step": 11, "text": "Age at 55°F (13°C) and 90% humidity for first month, rubbing with salt weekly."},
            {"step": 12, "text": "Continue aging 8-24 months. Longer aging develops more intense flavor and crystalline texture."}
        ],
        "temperature": "90-130°F (32-55°C)",
        "notes": [
            "Traditional Comté is made from raw milk of Montbéliarde or Simmental cows",
            "Fruité (fruity) designation: 4+ months; Extra: 12+ months",
            "Small eyes develop from propionic fermentation during warm aging",
            "Wheels traditionally weigh 80-100 lbs - scale recipe as needed",
            "Crystals that form during long aging are tyrosine amino acid clusters"
        ],
        "tags": ["cheese", "French", "Alpine", "hard", "aged", "AOP", "Jura"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-reblochon",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Reblochon (Semi-Soft Alpine Cheese)",
        "category": "cheese",
        "attribution": "Traditional French Savoie cheese",
        "source_note": "AOP cheese from Haute-Savoie, essential for tartiflette.",
        "description": "Buttery, nutty washed-rind cheese with an ivory paste that becomes increasingly supple as it ripens. The name comes from 'reblocher' - to milk again - referring to the richer second milking.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk (high fat content ideal)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "Brevibacterium linens (for rind)", "quantity": "1/32", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter, P. candidum, and B. linens. Mix well."},
            {"step": 2, "text": "Ripen for 30 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet diluted in water. Stir gently for 30 seconds."},
            {"step": 4, "text": "Let set undisturbed for 45 minutes until soft curd forms."},
            {"step": 5, "text": "Cut curds into 3/4-inch cubes. Let rest 10 minutes."},
            {"step": 6, "text": "Gently stir for 20 minutes - do NOT heat further. Curds should remain soft."},
            {"step": 7, "text": "Drain whey and ladle curds into small disc-shaped molds (traditional size ~5 inches diameter)."},
            {"step": 8, "text": "Allow to drain without pressing for 6-8 hours, flipping every 2 hours."},
            {"step": 9, "text": "Salt all surfaces. Let rest overnight at room temperature."},
            {"step": 10, "text": "Age at 55°F (13°C) and 95% humidity. Wash rind with light brine every 2-3 days."},
            {"step": 11, "text": "Ready in 4-6 weeks when rind is orange-pink and interior is supple."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Traditional Reblochon is made from raw milk of Abondance, Tarine, or Montbéliarde cows",
            "The 'second milking' was historically richer in fat - use highest fat milk available",
            "Fermier (farmstead) has green casein stamp; laitier (dairy) has red",
            "Essential for authentic tartiflette - sliced over potatoes, lardons, and onions",
            "Should smell like mushrooms and hazelnuts when properly aged"
        ],
        "tags": ["cheese", "French", "Alpine", "semi-soft", "washed-rind", "AOP", "Savoie", "tartiflette"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-tomme-de-savoie",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tomme de Savoie (Rustic Mountain Cheese)",
        "category": "cheese",
        "attribution": "Traditional French Alpine cheese",
        "source_note": "Rustic mountain cheese from the French Alps, traditionally made from skimmed milk.",
        "description": "Humble yet complex Alpine tomme with a thick gray-brown rind covered in yellow and orange mold patches. Semi-firm paste with nutty, grassy, earthy flavors and a slight tanginess.",
        "servings_yield": "About 3 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "part-skim cow's milk (or skim evening + whole morning milk)", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter culture and mix well."},
            {"step": 2, "text": "Ripen for 45 minutes, maintaining temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet diluted in water. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Slowly raise temperature to 100°F (38°C) over 30 minutes while stirring gently."},
            {"step": 6, "text": "Continue stirring at 100°F until curds shrink and firm slightly, about 20 minutes."},
            {"step": 7, "text": "Drain curds and press at 10 lbs for 30 minutes."},
            {"step": 8, "text": "Flip, press at 20 lbs for 6 hours, flip again, press at 20 lbs for 12 hours."},
            {"step": 9, "text": "Dry salt all surfaces or brine for 12 hours."},
            {"step": 10, "text": "Age at 55°F (13°C) and 90% humidity for 2-4 months."},
            {"step": 11, "text": "Let natural rind develop - brush off excessive mold if needed but allow gray/brown coat to form."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Historically made from leftover skimmed milk after cream was taken for butter",
            "Lower fat content allows rustic rind to develop character",
            "Natural rind should be left alone - it protects the cheese",
            "Each wheel is unique due to wild ambient molds",
            "Look for PGI label for authentic Tomme de Savoie"
        ],
        "tags": ["cheese", "French", "Alpine", "semi-firm", "natural rind", "PGI", "Savoie", "tomme"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === WASHED RIND CHEESES ===
    {
        "id": "artisan-french-epoisses",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Époisses (Washed Rind Cheese)",
        "category": "cheese",
        "attribution": "Traditional Burgundian cheese",
        "source_note": "AOP cheese from Burgundy, washed with Marc de Bourgogne brandy.",
        "description": "The 'King of Cheeses' according to Brillat-Savarin. Intensely aromatic washed-rind cheese with a sunset-orange rind and spoonable creamy interior when perfectly ripe.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "Marc de Bourgogne or brandy (for wash)", "quantity": "1/2", "unit": "cup"},
            {"item": "water (for wash)", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and B. linens, mix thoroughly."},
            {"step": 2, "text": "Ripen for 1 hour at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet diluted in water. Stir briefly."},
            {"step": 4, "text": "Let set undisturbed for 90 minutes until very soft curd forms."},
            {"step": 5, "text": "Very gently ladle curds into small disc molds - do not break curds."},
            {"step": 6, "text": "Drain naturally at room temperature for 48 hours, flipping 4-5 times."},
            {"step": 7, "text": "Salt all surfaces. Rest at room temperature overnight."},
            {"step": 8, "text": "Transfer to aging space at 55°F (13°C) and 95% humidity."},
            {"step": 9, "text": "Mix Marc/brandy with water for wash. Wash rind every 2-3 days with this solution."},
            {"step": 10, "text": "Continue washing and aging for 6-8 weeks until rind is deep orange and sticky."},
            {"step": 11, "text": "When gently pressed, center should feel liquid. Ready when aroma is powerful but not ammonia."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Brillat-Savarin called Époisses 'le roi des fromages' - the king of cheeses",
            "Traditional wash is Marc de Bourgogne - grape pomace brandy",
            "Banned on Paris Metro due to its powerful aroma",
            "Best enjoyed at room temperature with Burgundy red wine",
            "The orange color comes from B. linens bacteria, enhanced by the alcohol wash"
        ],
        "tags": ["cheese", "French", "washed-rind", "soft", "AOP", "Burgundy", "stinky cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-munster",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Munster (Alsatian Washed Rind)",
        "category": "cheese",
        "attribution": "Traditional Alsatian cheese",
        "source_note": "AOP cheese from Alsace and Lorraine, traditionally served with cumin.",
        "description": "Powerful Alsatian washed-rind cheese with orange-red sticky rind and supple, creamy interior. Strong barnyard aroma belies a surprisingly mild, earthy flavor.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "cumin seeds (traditional accompaniment)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, stir well."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet diluted in water."},
            {"step": 4, "text": "Let set 60-90 minutes until soft curd forms."},
            {"step": 5, "text": "Cut curds into 1-inch cubes. Let rest 15 minutes."},
            {"step": 6, "text": "Gently ladle curds into round molds (traditional size ~6 inches diameter)."},
            {"step": 7, "text": "Drain naturally 24-48 hours, flipping every 6-8 hours."},
            {"step": 8, "text": "Salt all surfaces liberally."},
            {"step": 9, "text": "Age at 55-60°F (13-16°C) and 95% humidity."},
            {"step": 10, "text": "Wash rind with light salt brine every 2 days for first 2 weeks, then twice weekly."},
            {"step": 11, "text": "Ready in 5-8 weeks when rind is orange-red and sticky. Serve with cumin seeds."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Munster (French) vs Münster (German) - different spelling, same cheese tradition",
            "Vosges mountain monks created this cheese in the 7th century",
            "Traditionally served with boiled potatoes and cumin seeds",
            "Smaller version called Géromé is also AOP",
            "Aroma is much stronger than flavor - give it a chance!"
        ],
        "tags": ["cheese", "French", "washed-rind", "soft", "AOP", "Alsace", "monastic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-pont-leveque",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Pont-l'Évêque (Washed Rind Norman)",
        "category": "cheese",
        "attribution": "Traditional Norman cheese",
        "source_note": "AOP cheese from Normandy, one of France's oldest cheeses.",
        "description": "Square-shaped Norman washed-rind cheese with a golden-orange rind and soft, slightly springy interior. Milder than Livarot, with buttery, slightly tangy flavors.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/32", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, B. linens, and P. candidum."},
            {"step": 2, "text": "Ripen for 45 minutes, maintaining temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 60 minutes for soft curd."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently stir for 15 minutes without heating."},
            {"step": 6, "text": "Ladle curds into square molds (traditional shape). Drain 24 hours, flipping frequently."},
            {"step": 7, "text": "Salt all surfaces, including edges."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90-95% humidity."},
            {"step": 9, "text": "Wash rind with light brine every 3-4 days."},
            {"step": 10, "text": "Ready in 4-6 weeks when rind is golden-orange and interior springs back when pressed."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Possibly France's oldest Norman cheese, mentioned in 13th century texts",
            "Square shape distinguishes it from other Norman washed-rind cheeses",
            "Milder than its stronger cousin, Livarot",
            "The white P. candidum bloom should show through the orange wash",
            "Best paired with Normandy cider or Calvados"
        ],
        "tags": ["cheese", "French", "washed-rind", "soft", "AOP", "Normandy", "Norman"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-livarot",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Livarot (The Colonel)",
        "category": "cheese",
        "attribution": "Traditional Norman cheese",
        "source_note": "AOP cheese from Normandy, nicknamed 'The Colonel' for its stripes.",
        "description": "Powerfully aromatic Norman washed-rind cheese wrapped with sedge grass bands. Deep orange rind encases a golden, oozy paste with meaty, complex flavors.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "6-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "sedge grass or raffia strips (for wrapping)", "quantity": "5", "unit": "strips"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and B. linens."},
            {"step": 2, "text": "Ripen for 1 hour at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 4, "text": "Very gently ladle curds into cylindrical molds without cutting."},
            {"step": 5, "text": "Drain naturally 48 hours, flipping every 8-12 hours."},
            {"step": 6, "text": "Salt all surfaces liberally."},
            {"step": 7, "text": "After 1 week, wrap with 5 strips of sedge grass or raffia around circumference."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity. Wash with salt brine every 2 days."},
            {"step": 9, "text": "Continue washing and aging 6-8 weeks total."},
            {"step": 10, "text": "Ready when rind is deep orange-red and center feels liquid when pressed."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Nicknamed 'Le Colonel' for its five stripes resembling military rank",
            "Stripes originally helped the soft cheese hold its shape",
            "Traditional sedge grass (laîche) comes from Norman marshes",
            "One of the strongest-smelling French cheeses",
            "Historically food of the poor, now a protected delicacy"
        ],
        "tags": ["cheese", "French", "washed-rind", "soft", "AOP", "Normandy", "stinky cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-langres",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Langres (Washed Rind with Fontaine)",
        "category": "cheese",
        "attribution": "Traditional Champagne cheese",
        "source_note": "AOP cheese from Champagne with characteristic concave top.",
        "description": "Unique washed-rind cheese with a 'fontaine' (well) in the top, traditionally filled with Champagne or Marc. Orange-red wrinkled rind surrounds a creamy, intense paste.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "Marc de Champagne or Champagne (for finishing)", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and B. linens, mix well."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 75 minutes for soft curd."},
            {"step": 4, "text": "Very gently ladle curds into cylindrical molds without stirring or cutting."},
            {"step": 5, "text": "Drain naturally 36-48 hours, flipping every 8 hours. Do NOT flip after 48 hours."},
            {"step": 6, "text": "Salt all surfaces except top - this creates the signature concave 'fontaine'."},
            {"step": 7, "text": "Age at 55°F (13°C) and 95% humidity."},
            {"step": 8, "text": "Wash sides and bottom with brine every 2-3 days. Never flip - top naturally sinks."},
            {"step": 9, "text": "Age 5-8 weeks. The top depression should deepen as cheese ripens from outside in."},
            {"step": 10, "text": "To serve traditionally, pour Marc de Champagne into the fontaine."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "The 'fontaine' (well) forms because the cheese is never flipped after molding",
            "Traditional to fill the well with Marc de Champagne before serving",
            "Wrinkled rind is characteristic - don't smooth it out",
            "Related to Époisses but distinct AOP with different shape and process",
            "The depression catches the alcohol and lets it seep into the paste"
        ],
        "tags": ["cheese", "French", "washed-rind", "soft", "AOP", "Champagne", "fontaine"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SEMI-HARD AND HARD CHEESES ===
    {
        "id": "artisan-french-morbier",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Morbier (Ash Line Cheese)",
        "category": "cheese",
        "attribution": "Traditional Jura cheese",
        "source_note": "AOP cheese from Franche-Comté with distinctive ash line through center.",
        "description": "Semi-soft Jura cheese with a signature horizontal ash line through its center. Creamy, springy paste with fruity, slightly smoky flavor and an edible washed rind.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "food-grade vegetable ash", "quantity": "1", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add both starters, mix well."},
            {"step": 2, "text": "Ripen for 30 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly raise to 100°F (38°C) over 20 minutes while stirring gently."},
            {"step": 6, "text": "Drain half the curds into mold and press lightly."},
            {"step": 7, "text": "Sprinkle vegetable ash evenly over surface of pressed curds."},
            {"step": 8, "text": "Add remaining curds on top. Press at 15 lbs for 6 hours, flip, 15 lbs for 12 hours."},
            {"step": 9, "text": "Brine for 24 hours in saturated solution."},
            {"step": 10, "text": "Age at 55°F (13°C) and 90% humidity for 2-3 months."},
            {"step": 11, "text": "Rub rind with salt water weekly to develop thin washed rind."}
        ],
        "temperature": "95-100°F (35-38°C)",
        "notes": [
            "Ash line originally from wood ash protecting morning curd until evening milking",
            "Today's ash is food-grade vegetable ash (vegetable carbon)",
            "Mixed cultures give more complex flavor than single culture",
            "The ash has no flavor - purely visual and traditional",
            "Semi-soft paste should spring back when pressed"
        ],
        "tags": ["cheese", "French", "Jura", "semi-soft", "AOP", "ash line", "washed-rind"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-saint-nectaire",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Saint-Nectaire (Rustic Auvergne Cheese)",
        "category": "cheese",
        "attribution": "Traditional Auvergne cheese",
        "source_note": "AOP cheese from volcanic Auvergne region with distinctive rustic rind.",
        "description": "Rustic semi-soft cheese from Auvergne's volcanic soil, with a thick gray rind dotted with red, yellow, and white molds. Earthy, mushroomy paste with subtle hazelnut notes.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "5-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter, mix thoroughly."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 50 minutes."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Gently stir for 15 minutes without heating."},
            {"step": 6, "text": "Press curds in mold: 10 lbs for 1 hour, flip, 15 lbs for 3 hours, flip, 20 lbs overnight."},
            {"step": 7, "text": "Dry salt all surfaces or brine 6 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) and 95% humidity on rye straw mats if available."},
            {"step": 9, "text": "Turn daily for first week, then every 2-3 days."},
            {"step": 10, "text": "Let natural molds develop - don't brush off. Ready in 5-8 weeks."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Traditional aging on rye straw gives distinctive flavor and rind",
            "Fermier version has oval green casein stamp; laitier has square",
            "Volcanic soil of Auvergne gives milk unique mineral character",
            "Multi-colored mold rind is desirable - shows proper cave aging",
            "Named after Marshal of France who introduced it to Louis XIV"
        ],
        "tags": ["cheese", "French", "Auvergne", "semi-soft", "AOP", "natural rind", "rustic"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-cantal",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cantal (Ancient Auvergne Cheese)",
        "category": "cheese",
        "attribution": "Traditional Auvergne cheese",
        "source_note": "AOP cheese from Auvergne, possibly France's oldest cheese.",
        "description": "Ancient hard cheese from Auvergne with a distinctive two-day curd process. Firm, slightly crumbly paste with buttery tang that intensifies with age.",
        "servings_yield": "About 4 lbs",
        "prep_time": "1 hour (over 2 days)",
        "cook_time": "4 hours",
        "total_time": "1-6 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "4", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "DAY 1: Heat milk to 90°F (32°C). Add starter, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Stir gently for 30 minutes, maintaining 90°F."},
            {"step": 5, "text": "Drain whey. Press curds at 10 lbs for 8 hours."},
            {"step": 6, "text": "DAY 2: Break up pressed curd mass into walnut-sized pieces - this is 'tome fraîche'."},
            {"step": 7, "text": "Mix salt thoroughly into broken curds. Let rest 1 hour."},
            {"step": 8, "text": "Pack salted curds firmly into large cylindrical mold."},
            {"step": 9, "text": "Press at 25 lbs for 24 hours, flipping every 6 hours."},
            {"step": 10, "text": "Age at 50°F (10°C) and 95% humidity. Brush rind with salt water weekly."},
            {"step": 11, "text": "Cantal Jeune: 1-2 months. Entre-Deux: 3-7 months. Vieux: 8+ months."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Two-day process with 'tome fraîche' stage is unique to Cantal family",
            "Tome fraîche is used fresh in aligot - mashed potatoes stretched with cheese",
            "Three age designations: Jeune (mild), Entre-Deux (medium), Vieux (strong)",
            "Pliny the Elder mentioned cheese from Auvergne in Roman times",
            "Salers is closely related but made only from raw Salers cow milk"
        ],
        "tags": ["cheese", "French", "Auvergne", "hard", "AOP", "ancient", "tome fraîche"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SHEEP MILK CHEESES ===
    {
        "id": "artisan-french-ossau-iraty",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ossau-Iraty (Basque Sheep Cheese)",
        "category": "cheese",
        "attribution": "Traditional French Basque cheese",
        "source_note": "AOP sheep's milk cheese from the French Basque Country and Béarn.",
        "description": "Firm sheep's milk cheese from the Pyrenees with nutty, slightly sweet flavor and hints of lanolin and grass. Dense, slightly crumbly paste with a natural brushed rind.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet (lamb rennet traditional)", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter, mix well."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet (lamb rennet traditional). Let set 45 minutes."},
            {"step": 4, "text": "Cut curds into 1/4-inch cubes - small for firm texture."},
            {"step": 5, "text": "Slowly heat to 105°F (41°C) over 30 minutes while stirring."},
            {"step": 6, "text": "Continue stirring at temperature until curds shrink and firm, about 20 minutes."},
            {"step": 7, "text": "Drain and press at 15 lbs for 1 hour, flip, 25 lbs for 12 hours."},
            {"step": 8, "text": "Brine for 24-48 hours in saturated solution."},
            {"step": 9, "text": "Age at 55°F (13°C) and 85% humidity for 3-6 months."},
            {"step": 10, "text": "Brush rind regularly to develop firm, natural coat."}
        ],
        "temperature": "86-105°F (30-41°C)",
        "notes": [
            "Made from Manech and Basco-Béarnaise sheep breeds",
            "Name combines Ossau valley (Béarn) and Iraty forest (Basque)",
            "Traditional with black cherry jam (cerises noires d'Itxassou)",
            "Transhumance - seasonal mountain grazing - gives summer milk special character",
            "Sheep's milk has higher fat and protein than cow's milk"
        ],
        "tags": ["cheese", "French", "Basque", "sheep milk", "hard", "AOP", "Pyrenees"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === BLUE CHEESES ===
    {
        "id": "artisan-french-bleu-dauvergne",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bleu d'Auvergne",
        "category": "cheese",
        "attribution": "Traditional Auvergne blue cheese",
        "source_note": "AOP blue cheese from the volcanic Auvergne region.",
        "description": "Creamy, powerful blue cheese with ivory paste streaked with blue-green veins. Spicy, assertive flavor with mushroom and grassy notes from volcanic terroir.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt (flaky)", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and P. roqueforti, mix thoroughly."},
            {"step": 2, "text": "Ripen for 1 hour at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes. Let rest 15 minutes."},
            {"step": 5, "text": "Very gently ladle curds into molds without pressing, layering salt between additions."},
            {"step": 6, "text": "Drain naturally at room temperature for 3-4 days, flipping twice daily."},
            {"step": 7, "text": "When firm enough, pierce with sterilized needle: 30-40 holes per side."},
            {"step": 8, "text": "Age at 48-50°F (9-10°C) and 95% humidity."},
            {"step": 9, "text": "Blue veins should develop within 2-3 weeks."},
            {"step": 10, "text": "Ready in 4-8 weeks when extensively veined and creamy."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Created in 1850s by Antoine Roussel using rye bread mold",
            "Volcanic soil of Auvergne gives distinctive mineral notes",
            "More assertive than Fourme d'Ambert, its milder cousin",
            "Piercing is critical - creates air channels for mold growth",
            "Pairs wonderfully with sweet wines like Sauternes"
        ],
        "tags": ["cheese", "French", "blue cheese", "Auvergne", "AOP", "P. roqueforti"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-fourme-dambert",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fourme d'Ambert (Gentle Blue)",
        "category": "cheese",
        "attribution": "Traditional Auvergne blue cheese",
        "source_note": "AOP blue cheese from Auvergne, one of France's mildest blues.",
        "description": "Tall cylindrical blue cheese with a dry gray rind and creamy ivory paste laced with delicate blue veins. Gentler than most blues with buttery, slightly sweet character.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium roqueforti (mild strain)", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and P. roqueforti."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 75 minutes."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently ladle curds into tall cylindrical molds without pressing."},
            {"step": 6, "text": "Drain naturally 2-3 days, flipping several times daily."},
            {"step": 7, "text": "Dry salt all surfaces liberally."},
            {"step": 8, "text": "Pierce with needle after 1 week: 20-30 holes per side."},
            {"step": 9, "text": "Age at 48-50°F (9-10°C) and 90% humidity for 4-8 weeks."},
            {"step": 10, "text": "Let gray natural rind develop. Interior should be creamy with delicate veining."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "One of France's oldest cheeses - possibly 2000+ years old",
            "Milder than Bleu d'Auvergne due to less P. roqueforti and fewer piercings",
            "Tall shape gives higher paste-to-rind ratio than flat wheels",
            "Gray rind is characteristic - don't mistake for contamination",
            "Excellent entry-level blue for those new to the style"
        ],
        "tags": ["cheese", "French", "blue cheese", "Auvergne", "AOP", "mild blue"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === TRIPLE CREAM CHEESES ===
    {
        "id": "artisan-french-brillat-savarin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Brillat-Savarin (Triple Cream)",
        "category": "cheese",
        "attribution": "Traditional French triple cream",
        "source_note": "Named after the famous gastronome Jean Anthelme Brillat-Savarin.",
        "description": "Luxuriously rich triple-cream cheese with 75% butterfat and a bloomy white rind. Buttery, tangy, and impossibly smooth - the ultimate indulgence.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "heavy cream", "quantity": "1", "unit": "quart"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and cream. Heat to 72°F (22°C) - barely warm."},
            {"step": 2, "text": "Add starter and P. candidum, stir gently."},
            {"step": 3, "text": "Ripen for 30 minutes."},
            {"step": 4, "text": "Add calcium chloride, then just 4 drops rennet diluted in water."},
            {"step": 5, "text": "Let set at room temperature 18-24 hours until very thick curd forms."},
            {"step": 6, "text": "Very gently ladle curds into molds - do NOT break curds."},
            {"step": 7, "text": "Drain naturally 24-48 hours at room temperature, flipping gently 2-3 times."},
            {"step": 8, "text": "Salt all surfaces very lightly."},
            {"step": 9, "text": "Age at 55°F (13°C) and 90% humidity for 2-3 weeks."},
            {"step": 10, "text": "White P. candidum bloom should fully cover surface when ready."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Named after the author of 'The Physiology of Taste'",
            "Triple cream = at least 75% butterfat in dry matter",
            "Minimal rennet - mostly acid set for delicate texture",
            "Best at room temperature when paste is spoonable",
            "Created in the 1930s by Henri Androuët"
        ],
        "tags": ["cheese", "French", "triple cream", "soft", "bloomy rind", "rich"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === BLOOMY RIND CHEESES ===
    {
        "id": "artisan-french-chaource",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chaource (Bloomy Rind)",
        "category": "cheese",
        "attribution": "Traditional Champagne cheese",
        "source_note": "AOP cheese from Champagne with thick bloomy rind.",
        "description": "Tall cylindrical bloomy-rind cheese with a thick white P. candidum coat and a chalky-to-creamy interior. Mushroomy, slightly sour, with dense texture.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and P. candidum."},
            {"step": 2, "text": "Ripen for 45 minutes at stable temperature."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 90 minutes for very soft curd."},
            {"step": 4, "text": "Very gently ladle curds into tall cylindrical molds without cutting."},
            {"step": 5, "text": "Drain naturally at room temperature 24-36 hours, flipping every 6-8 hours."},
            {"step": 6, "text": "Salt all surfaces evenly."},
            {"step": 7, "text": "Age at 55°F (13°C) and 90% humidity for 2-4 weeks."},
            {"step": 8, "text": "Thick white bloom should develop within first week."},
            {"step": 9, "text": "Young Chaource has chalky center; aged has fully creamy paste."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "From the town of Chaource in the Champagne region",
            "Thicker and taller than Camembert with denser texture",
            "Traditionally eaten young with chalky center still present",
            "Pairs excellently with Champagne or Chablis",
            "The thick rind is edible and flavorful"
        ],
        "tags": ["cheese", "French", "bloomy rind", "soft", "AOP", "Champagne"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-saint-marcellin",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Saint-Marcellin",
        "category": "cheese",
        "attribution": "Traditional Dauphiné cheese",
        "source_note": "IGP cheese from Dauphiné, traditionally served in small terracotta crocks.",
        "description": "Small, delicate cheese that transforms from fresh and tangy to runny and complex. At peak ripeness, it becomes liquid gold that must be eaten with a spoon.",
        "servings_yield": "About 3 small cheeses",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C). Add starter, P. candidum, and G. candidum."},
            {"step": 2, "text": "Ripen for 30 minutes."},
            {"step": 3, "text": "Add just 3 drops rennet diluted in water. Stir briefly."},
            {"step": 4, "text": "Let set at room temperature 24-36 hours until very thick."},
            {"step": 5, "text": "Gently ladle into small (3-inch) molds without breaking curd."},
            {"step": 6, "text": "Drain naturally 24-48 hours, flipping gently."},
            {"step": 7, "text": "Salt very lightly all surfaces."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90% humidity."},
            {"step": 9, "text": "When rind is wrinkled and cream-colored with blue-gray patches, cheese is ripening."},
            {"step": 10, "text": "Eat from fresh to very ripe - flavor intensifies dramatically with age."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Originally made with goat's milk, now typically cow's milk",
            "Legend: saved Louis XI from a bear attack, became his favorite cheese",
            "Traditionally sold in small terracotta crocks (coupelles)",
            "At peak ripeness, entire interior becomes liquid",
            "The wrinkled rind is normal and desirable"
        ],
        "tags": ["cheese", "French", "Dauphiné", "soft", "IGP", "bloomy rind", "runny"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === GOAT CHEESES ===
    {
        "id": "artisan-french-valencay",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Valençay (Ash-Covered Pyramid)",
        "category": "cheese",
        "attribution": "Traditional Loire Valley cheese",
        "source_note": "AOP goat cheese with truncated pyramid shape covered in ash.",
        "description": "Striking truncated pyramid-shaped goat cheese covered in blue-gray vegetable ash. Firm, slightly crumbly paste with citrusy tang that develops complexity with age.",
        "servings_yield": "About 4 small cheeses",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-5 weeks aging",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "food-grade vegetable ash", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 72°F (22°C). Add starter and P. candidum."},
            {"step": 2, "text": "Ripen for 1 hour."},
            {"step": 3, "text": "Add just 4 drops rennet diluted in water."},
            {"step": 4, "text": "Let set at room temperature 18-24 hours until very thick curd."},
            {"step": 5, "text": "Very gently ladle curds into truncated pyramid molds."},
            {"step": 6, "text": "Drain naturally 36-48 hours until firm enough to unmold."},
            {"step": 7, "text": "Salt all surfaces lightly."},
            {"step": 8, "text": "Coat thoroughly with vegetable ash on all surfaces."},
            {"step": 9, "text": "Age at 55°F (13°C) and 85% humidity for 2-5 weeks."},
            {"step": 10, "text": "White mold will grow through ash, creating distinctive blue-gray appearance."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Legend: Napoleon sliced top off full pyramid after Egyptian campaign defeat",
            "More likely: flat top allows stacking during aging",
            "Ash protects surface and neutralizes acidity for mold growth",
            "Young: fresh and tangy; Aged: dense, nutty, complex",
            "Loire Valley produces many famous ash-coated chèvres"
        ],
        "tags": ["cheese", "French", "Loire Valley", "goat", "AOP", "ash-covered", "pyramid"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-crottin-de-chavignol",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crottin de Chavignol (Aged Goat)",
        "category": "cheese",
        "attribution": "Traditional Sancerre goat cheese",
        "source_note": "AOP goat cheese from Sancerre wine region, transforms dramatically with age.",
        "description": "Small barrel-shaped goat cheese that transforms from fresh and mild to hard and intensely goaty. The name means 'little dropping' - don't let that stop you!",
        "servings_yield": "About 6 small cheeses",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-10 weeks aging",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Penicillium candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 70°F (21°C). Add starter, P. candidum, and G. candidum."},
            {"step": 2, "text": "Ripen for 1 hour at stable temperature."},
            {"step": 3, "text": "Add just 3 drops rennet diluted in water."},
            {"step": 4, "text": "Let set at room temperature 24 hours until thick curd."},
            {"step": 5, "text": "Gently ladle curds into small barrel-shaped molds (2-inch diameter)."},
            {"step": 6, "text": "Drain naturally 24-48 hours, flipping occasionally."},
            {"step": 7, "text": "Salt all surfaces lightly."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity."},
            {"step": 9, "text": "Track development: fresh (1 week), mi-sec (2-3 weeks), sec (5-6 weeks), très sec (10+ weeks)."}
        ],
        "temperature": "70°F (21°C)",
        "notes": [
            "Name comes from oil lamp ('crot') shape - or possibly less savory origins",
            "Four stages: fresh (white), mi-sec (some mold), sec (hard), très sec (rock hard)",
            "Pairs perfectly with Sancerre wine from same region",
            "Aged versions can be grated like Parmesan",
            "Warmed crottin on salad is classic French bistro dish"
        ],
        "tags": ["cheese", "French", "Loire Valley", "goat", "AOP", "Sancerre", "aged goat"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-rocamadour",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rocamadour (Tiny Goat Medallion)",
        "category": "cheese",
        "attribution": "Traditional Quercy goat cheese",
        "source_note": "AOP goat cheese from Quercy, one of France's smallest cheeses.",
        "description": "Tiny disc of goat cheese, just 1.5 oz, with intense flavor packed into a small package. Creamy when young, develops wrinkled rind and concentrated tang with age.",
        "servings_yield": "About 8-10 tiny cheeses",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1-3 weeks aging",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "Geotrichum candidum", "quantity": "1/32", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3", "unit": "drops"},
            {"item": "cheese salt", "quantity": "3/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 68-72°F (20-22°C). Add starter and G. candidum."},
            {"step": 2, "text": "Ripen for 1 hour."},
            {"step": 3, "text": "Add just 3 drops rennet diluted in water."},
            {"step": 4, "text": "Let set at room temperature 24-36 hours for very thick, acidic curd."},
            {"step": 5, "text": "Gently ladle curds into tiny (2-inch diameter, 1/2-inch tall) molds."},
            {"step": 6, "text": "Drain naturally 24-36 hours. These tiny cheeses drain quickly."},
            {"step": 7, "text": "Salt very lightly - tiny size means salt penetrates quickly."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for 1-3 weeks."},
            {"step": 9, "text": "Wrinkled cream-colored rind develops as it ages."}
        ],
        "temperature": "68-72°F (20-22°C)",
        "notes": [
            "Named after the pilgrimage town of Rocamadour in Quercy",
            "Traditionally weighs only 35g (1.2 oz)",
            "Served as appetizer or dessert - often grilled on salad",
            "High surface area to volume ratio = fast ripening",
            "Produces 'Cabécou' style - small goat disc"
        ],
        "tags": ["cheese", "French", "Quercy", "goat", "AOP", "tiny", "cabécou"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "artisan-french-banon",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Banon (Chestnut Leaf Wrapped)",
        "category": "cheese",
        "attribution": "Traditional Provence cheese",
        "source_note": "AOP cheese from Provence wrapped in chestnut leaves.",
        "description": "Unique Provençal cheese wrapped in chestnut leaves and tied with raffia. The leaves impart tannins that help ripen the interior to a runny, complex state.",
        "servings_yield": "About 4 small cheeses",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "goat's milk (or cow's milk)", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "4", "unit": "drops"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "dried chestnut leaves", "quantity": "16-20", "unit": "leaves"},
            {"item": "raffia or kitchen twine", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 72°F (22°C). Add starter, mix well."},
            {"step": 2, "text": "Ripen for 1 hour."},
            {"step": 3, "text": "Add 4 drops rennet diluted in water."},
            {"step": 4, "text": "Let set at room temperature 24 hours until thick curd."},
            {"step": 5, "text": "Gently ladle into small round molds (3-inch diameter)."},
            {"step": 6, "text": "Drain naturally 24-48 hours until firm but still moist."},
            {"step": 7, "text": "Salt lightly all surfaces."},
            {"step": 8, "text": "Soak dried chestnut leaves in warm water or white wine/eau de vie until pliable."},
            {"step": 9, "text": "Wrap each cheese in 4-5 overlapping leaves, tie with raffia in a cross pattern."},
            {"step": 10, "text": "Age at 55°F (13°C) and 90% humidity for 2-4 weeks."},
            {"step": 11, "text": "Leaves will brown; interior will become runny and complex."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Chestnut leaves contribute tannins that transform the cheese",
            "Traditional to dip leaves in eau de vie (brandy) before wrapping",
            "Originally goat's milk, now cow's or mixed milk allowed for AOP",
            "When opened, should be runny and aromatic",
            "Autumn leaves harvested and stored for year-round production"
        ],
        "tags": ["cheese", "French", "Provence", "goat", "AOP", "leaf-wrapped", "unique"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add French cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in FRENCH_CHEESE_RECIPES:
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
