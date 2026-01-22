#!/usr/bin/env python3
"""Add comprehensive Greek cheese recipes to the cheese category."""

import json

GREEK_CHEESE_RECIPES = [
    # === PASTA FILATA CHEESES ===
    {
        "id": "kasseri-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kasseri (Greek Pasta Filata Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "Greece's signature stretched-curd cheese, similar to Italian provolone.",
        "description": "A pale yellow, medium-hard Greek cheese with a slightly tangy flavor. Made using the pasta filata (stretched curd) method, it melts beautifully and is essential for saganaki.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk. Add rennet and let set for 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 115°F (46°C) over 40 minutes while stirring gently."},
            {"step": 5, "text": "Drain curds and let mat together for 30 minutes at room temperature."},
            {"step": 6, "text": "Cut curd mass into strips. Place in 170°F (77°C) water until stretchy."},
            {"step": 7, "text": "Knead and stretch until smooth and elastic. Form into balls or blocks."},
            {"step": 8, "text": "Brine in saturated solution for 12-24 hours."},
            {"step": 9, "text": "Age at 55°F (13°C) and 85% humidity for 2-4 months, rubbing with olive oil weekly."}
        ],
        "temperature": "95-170°F (35-77°C)",
        "notes": [
            "Kasseri means 'cheese' in Turkish, reflecting Ottoman influence",
            "Traditional kasseri is made with sheep's milk or a sheep/goat blend",
            "The stretching technique is key to its characteristic texture",
            "Perfect for saganaki - fried cheese appetizer"
        ],
        "tags": ["cheese", "Greek", "pasta filata", "sheep's milk", "aged", "saganaki"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === HARD GRATING CHEESES ===
    {
        "id": "kefalotyri-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kefalotyri (Greek Hard Grating Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "Greece's answer to Parmesan, a hard sheep's milk cheese for grating.",
        "description": "A hard, salty Greek cheese made from sheep's or goat's milk. Pale yellow with a sharp, tangy flavor, it's the traditional cheese for grating over pasta and for making saganaki.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "sheep's milk (or goat's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and ripen for 1 hour."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes until very firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes."},
            {"step": 4, "text": "Slowly heat to 120°F (49°C) over 45 minutes while stirring continuously."},
            {"step": 5, "text": "Continue stirring at temperature until curds are very firm and squeak, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 30 lbs for 2 hours, flip, then 50 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 2-3 days, turning daily."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for minimum 3 months, up to 1 year. Turn weekly."}
        ],
        "temperature": "90-120°F (32-49°C)",
        "notes": [
            "Kefalotyri means 'head cheese' referring to its round shape",
            "Younger cheese is milder; aged version is sharp and crumbly",
            "Essential for authentic Greek pasta dishes",
            "Can substitute for Pecorino Romano in recipes"
        ],
        "tags": ["cheese", "Greek", "hard", "grating", "sheep's milk", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === REGIONAL HARD CHEESES ===
    {
        "id": "graviera-crete-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Graviera Kritis (Cretan Graviera)",
        "category": "cheese",
        "attribution": "Traditional Cretan cheese",
        "source_note": "PDO cheese from Crete, Greece's most popular table cheese.",
        "description": "A hard, pale yellow cheese from Crete with a sweet, nutty flavor reminiscent of Gruyère. Made primarily from sheep's milk with some goat's milk, it's aged in the island's unique climate.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "5-12 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2.5", "unit": "gallons"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/2", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep's and goat's milk. Heat to 95°F (35°C)."},
            {"step": 2, "text": "Add starter culture and ripen for 30 minutes."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 4, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 5, "text": "Slowly heat to 122°F (50°C) over 45 minutes while stirring continuously."},
            {"step": 6, "text": "Hold temperature and stir until curds are firm and shrunk, about 30 minutes."},
            {"step": 7, "text": "Drain and press at 25 lbs for 1 hour, flip, then 45 lbs for 24 hours."},
            {"step": 8, "text": "Brine in saturated solution for 2-3 days."},
            {"step": 9, "text": "Age at 55°F (13°C) and 85% humidity for 5-12 months. Rub with olive oil monthly."}
        ],
        "temperature": "95-122°F (35-50°C)",
        "notes": [
            "Graviera is derived from Gruyère, brought to Greece by Swiss cheesemakers",
            "Cretan version has PDO (Protected Designation of Origin) status",
            "Sweet, fruity flavor with hints of burnt caramel",
            "Greece's second most popular cheese after feta"
        ],
        "tags": ["cheese", "Greek", "Cretan", "hard", "PDO", "sheep's milk", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === WHEY CHEESES ===
    {
        "id": "manouri-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Manouri (Greek Whey Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "PDO whey cheese from Macedonia and Thessaly, Greece.",
        "description": "A soft, creamy Greek whey cheese made by adding milk or cream to the whey left over from feta production. Rich, buttery, and slightly sweet, it's often served with honey for dessert.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 min",
        "cook_time": "2 hours",
        "total_time": "1-2 days",
        "ingredients": [
            {"item": "fresh whey (from feta or other cheese)", "quantity": "1", "unit": "gallon"},
            {"item": "whole sheep's milk", "quantity": "1", "unit": "quart"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "white vinegar or lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey, sheep's milk, and cream in a large pot."},
            {"step": 2, "text": "Heat slowly to 195°F (90°C), stirring occasionally."},
            {"step": 3, "text": "Add vinegar or lemon juice and stir gently."},
            {"step": 4, "text": "When curds form and rise to surface, remove from heat."},
            {"step": 5, "text": "Let rest 15 minutes for curds to consolidate."},
            {"step": 6, "text": "Gently ladle curds into cheesecloth-lined molds."},
            {"step": 7, "text": "Drain at room temperature for 24-48 hours without pressing."},
            {"step": 8, "text": "Salt lightly and refrigerate. Best consumed within 1 week."}
        ],
        "temperature": "195°F (90°C)",
        "notes": [
            "Manouri is a byproduct of feta production - uses the leftover whey",
            "Adding cream makes it richer than traditional whey cheeses",
            "PDO protected - authentic manouri comes from Macedonia and Thessaly",
            "Traditional dessert served with honey and walnuts"
        ],
        "tags": ["cheese", "Greek", "whey cheese", "fresh", "PDO", "dessert cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "mizithra-fresh-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Mizithra (Fresh Greek Whey Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "Ancient Greek whey cheese, made fresh or aged.",
        "description": "A traditional Greek whey cheese available in two forms: fresh (soft and creamy) or aged (hard and salty for grating). The fresh version is sweet and ricotta-like, perfect for pastries.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "1.5 hours",
        "total_time": "24 hours for fresh; 3-4 months for aged",
        "ingredients": [
            {"item": "fresh whey (from feta or other sheep's milk cheese)", "quantity": "1", "unit": "gallon"},
            {"item": "whole sheep's milk", "quantity": "2", "unit": "cups"},
            {"item": "white vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "cheese salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey and sheep's milk in a pot."},
            {"step": 2, "text": "Heat slowly to 190°F (88°C), stirring occasionally."},
            {"step": 3, "text": "Add vinegar and stir gently once."},
            {"step": 4, "text": "When white curds form and float to surface, remove from heat."},
            {"step": 5, "text": "Let rest 10 minutes."},
            {"step": 6, "text": "Skim curds into cheesecloth-lined colander."},
            {"step": 7, "text": "Hang cheesecloth bundle to drain for 12-24 hours."},
            {"step": 8, "text": "For fresh mizithra: Salt lightly and refrigerate. Use within 1 week."},
            {"step": 9, "text": "For aged mizithra: Form into balls, salt heavily, and age at 55°F for 3-4 months until hard."}
        ],
        "temperature": "190°F (88°C)",
        "notes": [
            "One of the oldest Greek cheeses, mentioned in Homer's Odyssey",
            "Fresh version is like Italian ricotta",
            "Aged version (xinomizithra) is hard and used for grating",
            "Essential for Greek pastries like kalitsounia"
        ],
        "tags": ["cheese", "Greek", "whey cheese", "fresh", "aged", "sheep's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "anthotyros-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Anthotyros (Fresh Greek Flower Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "Delicate fresh whey cheese, named 'flower of cheese' for its lightness.",
        "description": "A fresh, soft Greek whey cheese with a delicate, slightly sweet flavor. The name means 'flower cheese' referring to its fine, light texture. Used in both savory dishes and desserts.",
        "servings_yield": "About 12 oz",
        "prep_time": "15 min",
        "cook_time": "1.5 hours",
        "total_time": "24 hours",
        "ingredients": [
            {"item": "fresh whey (from sheep's or goat's cheese)", "quantity": "1", "unit": "gallon"},
            {"item": "whole milk (sheep's, goat's, or cow's)", "quantity": "1", "unit": "cup"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "fine sea salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine fresh whey and milk in a large pot."},
            {"step": 2, "text": "Heat slowly to 185°F (85°C), stirring occasionally."},
            {"step": 3, "text": "Add lemon juice and stir once gently."},
            {"step": 4, "text": "Continue heating to 195°F (90°C) until fine curds form."},
            {"step": 5, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 6, "text": "Carefully skim delicate curds with slotted spoon into cheesecloth."},
            {"step": 7, "text": "Tie cheesecloth and hang to drain 12-24 hours."},
            {"step": 8, "text": "Salt very lightly. Refrigerate and use within 5 days."}
        ],
        "temperature": "185-195°F (85-90°C)",
        "notes": [
            "Anthos means 'flower' - the finest part of the whey",
            "Lighter and more delicate than mizithra",
            "Can be made dry (xero anthotyros) for longer storage",
            "Cretan version is particularly prized"
        ],
        "tags": ["cheese", "Greek", "whey cheese", "fresh", "delicate", "dessert cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === FERMENTED/SPREADABLE CHEESES ===
    {
        "id": "kopanisti-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kopanisti (Cycladic Spicy Fermented Cheese)",
        "category": "cheese",
        "attribution": "Traditional Cycladic cheese",
        "source_note": "PDO spicy fermented cheese from the Cyclades islands, especially Mykonos.",
        "description": "A soft, pungent, spicy cheese from the Cyclades islands. Fermented for weeks until creamy and spreadable, it develops a distinctive sharp, peppery flavor. A beloved Greek meze.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours initial",
        "total_time": "1-3 months fermentation",
        "ingredients": [
            {"item": "sheep's milk feta (or fresh sheep's cheese)", "quantity": "2", "unit": "lbs"},
            {"item": "plain yogurt (sheep's milk preferred)", "quantity": "1/2", "unit": "cup"},
            {"item": "olive oil", "quantity": "1/4", "unit": "cup"},
            {"item": "hot paprika or dried chili", "quantity": "1", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Crumble feta or fresh cheese into a bowl."},
            {"step": 2, "text": "Mix in yogurt and half the olive oil until well combined."},
            {"step": 3, "text": "Add salt and paprika, mix thoroughly."},
            {"step": 4, "text": "Pack mixture tightly into a clay pot or jar."},
            {"step": 5, "text": "Top with remaining olive oil to seal."},
            {"step": 6, "text": "Cover and store at room temperature for 2-3 days."},
            {"step": 7, "text": "Move to cool cellar or refrigerator. Ferment for 1-3 months."},
            {"step": 8, "text": "Check weekly - mash and mix, adding olive oil as needed."},
            {"step": 9, "text": "Ready when creamy, pungent, and spicy throughout."}
        ],
        "temperature": "Room temperature initially, then 50-55°F (10-13°C)",
        "notes": [
            "Kopanisti means 'beaten' from the repeated mashing",
            "Mykonos version is most famous, has PDO protection",
            "The longer fermentation, the spicier and more pungent",
            "Serve as meze with bread or add to salads"
        ],
        "tags": ["cheese", "Greek", "Cycladic", "fermented", "spicy", "spreadable", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "katiki-domokou-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Katiki Domokou (Creamy Spreadable Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "PDO fresh spreadable cheese from Domokos in Thessaly, Greece.",
        "description": "A soft, creamy, spreadable cheese from Thessaly with a tangy, refreshing flavor. Made from goat's or sheep's milk, it has a texture between yogurt and cream cheese. Perfect for spreading on bread.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "goat's milk (or sheep's milk)", "quantity": "1", "unit": "gallon"},
            {"item": "plain goat's milk yogurt", "quantity": "1/2", "unit": "cup"},
            {"item": "lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "fine sea salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 185°F (85°C)."},
            {"step": 2, "text": "Cool to 110°F (43°C). Stir in yogurt."},
            {"step": 3, "text": "Cover and let ferment at warm room temperature for 12-24 hours until thick."},
            {"step": 4, "text": "Add lemon juice and stir gently."},
            {"step": 5, "text": "Line colander with fine cheesecloth. Pour in mixture."},
            {"step": 6, "text": "Drain at room temperature for 24-48 hours until creamy but spreadable."},
            {"step": 7, "text": "Mix in salt. Transfer to container."},
            {"step": 8, "text": "Refrigerate and use within 1 week."}
        ],
        "temperature": "185°F (85°C) then 110°F (43°C)",
        "notes": [
            "Katiki has PDO protection since 1996",
            "Texture should be creamy and spoonable, not firm",
            "Traditional accompaniment to Greek salads",
            "The tangy flavor comes from natural fermentation"
        ],
        "tags": ["cheese", "Greek", "fresh", "spreadable", "PDO", "goat's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === OIL-PRESERVED CHEESES ===
    {
        "id": "ladotyri-mytilinis-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ladotyri Mytilinis (Lesbos Oil-Preserved Cheese)",
        "category": "cheese",
        "attribution": "Traditional cheese from Lesbos",
        "source_note": "PDO cheese from Lesbos (Mytilini), preserved in olive oil.",
        "description": "A hard, piquant cheese from the island of Lesbos, aged and preserved in olive oil. The oil gives it a unique smooth texture and rich flavor. One of Greece's most distinctive regional cheeses.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-6 months aging in oil",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "3", "unit": "tbsp"},
            {"item": "extra virgin olive oil (for preserving)", "quantity": "4-6", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 110°F (43°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain and press at 20 lbs for 1 hour, flip, then 35 lbs for 12 hours."},
            {"step": 6, "text": "Rub cheese generously with salt. Repeat daily for 1 week."},
            {"step": 7, "text": "Air-dry at 55°F (13°C) for 2-3 weeks until rind forms."},
            {"step": 8, "text": "Submerge cheese completely in olive oil in a crock or jar."},
            {"step": 9, "text": "Age in oil at cool room temperature for 3-6 months."}
        ],
        "temperature": "95-110°F (35-43°C)",
        "notes": [
            "Ladotyri means 'oil cheese' - named for its preservation method",
            "The olive oil both preserves and flavors the cheese",
            "PDO protected - authentic version only from Lesbos",
            "Oil becomes flavored and can be used for cooking"
        ],
        "tags": ["cheese", "Greek", "Lesbos", "oil-preserved", "hard", "PDO", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === MOUNTAIN CHEESES ===
    {
        "id": "formaella-parnassou-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Formaella Arachovas Parnassou (Parnassus Mountain Cheese)",
        "category": "cheese",
        "attribution": "Traditional mountain cheese",
        "source_note": "PDO cheese from Arachova on Mount Parnassus, Greece.",
        "description": "A semi-hard cheese from the village of Arachova on Mount Parnassus. Made from sheep's or goat's milk, it has a mild, slightly sweet flavor. Named for its small cylindrical 'formella' (mold) shape.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "sheep's milk (or goat's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Gently heat to 100°F (38°C) over 20 minutes while stirring."},
            {"step": 5, "text": "Drain and ladle curds into small cylindrical molds (about 4 inches diameter)."},
            {"step": 6, "text": "Press lightly at 10 lbs for 2 hours, flip, then 15 lbs for 8 hours."},
            {"step": 7, "text": "Brine for 12-24 hours depending on size."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 2-3 months."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Formaella is a diminutive of 'forma' (mold/form)",
            "PDO protected since 1996",
            "Traditionally made by shepherds on Mount Parnassus",
            "Mild enough for everyday eating, firm enough for grilling"
        ],
        "tags": ["cheese", "Greek", "mountain", "PDO", "semi-hard", "sheep's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sfela-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sfela (Peloponnese Spicy Brined Cheese)",
        "category": "cheese",
        "attribution": "Traditional Peloponnese cheese",
        "source_note": "PDO cheese from Messinia and Lakonia in the Peloponnese, Greece.",
        "description": "A semi-hard, brined cheese from the southern Peloponnese with a distinctive spicy, peppery flavor. Often called 'the fire of Mani' for its sharp, aggressive taste. Made from sheep's and goat's milk.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "3 hours",
        "total_time": "3+ months aging in brine",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "salt for brine", "quantity": "1", "unit": "lb per gallon water"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine sheep's and goat's milk. Heat to 90°F (32°C)."},
            {"step": 2, "text": "Add starter and ripen for 1 hour."},
            {"step": 3, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes."},
            {"step": 4, "text": "Cut curds into 3/4-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently stir curds for 30 minutes at 90°F (32°C)."},
            {"step": 6, "text": "Drain and press at 15 lbs for 2 hours, flip, then 25 lbs for 12 hours."},
            {"step": 7, "text": "Cut cheese into thick slabs. Prepare heavy brine (7% salt minimum)."},
            {"step": 8, "text": "Submerge cheese slabs in brine. Store at 55°F (13°C)."},
            {"step": 9, "text": "Age in brine for minimum 3 months. Flavor intensifies with time."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Sfela develops its spicy flavor from the aging process, not added spices",
            "The sheep/goat milk blend is traditional to the Mani peninsula",
            "PDO protected - only from Messinia and Lakonia regions",
            "Much sharper and spicier than feta"
        ],
        "tags": ["cheese", "Greek", "Peloponnese", "brined", "spicy", "PDO", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SMOKED CHEESES ===
    {
        "id": "metsovone-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Metsovone (Greek Smoked Cheese)",
        "category": "cheese",
        "attribution": "Traditional Epirus cheese",
        "source_note": "PDO smoked pasta filata cheese from Metsovo in the Pindus Mountains.",
        "description": "A smoked, semi-hard cheese from the mountain village of Metsovo in Epirus. Made using the pasta filata method, then naturally smoked, giving it a distinctive smoky-sweet flavor unique among Greek cheeses.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours plus smoking",
        "total_time": "3-4 months aging",
        "ingredients": [
            {"item": "cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "sheep's milk (optional, for tradition)", "quantity": "1", "unit": "quart"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "aromatic hardwood for smoking (beech, oak)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks. Heat to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat to 115°F (46°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds and let mat together for 2 hours until pH drops."},
            {"step": 6, "text": "Cut curd mass into strips. Stretch in 170°F (77°C) water until elastic."},
            {"step": 7, "text": "Form into oblong or cylindrical shapes. Brine 24 hours."},
            {"step": 8, "text": "Dry surface for 2-3 days at 55°F (13°C)."},
            {"step": 9, "text": "Cold-smoke at under 90°F (32°C) for 2-4 days using aromatic hardwood."},
            {"step": 10, "text": "Age at 55°F (13°C) for 3-4 months."}
        ],
        "temperature": "95-170°F (35-77°C) for cheese; under 90°F (32°C) for smoking",
        "notes": [
            "Metsovo is a Vlach village known for its cheese tradition",
            "PDO protected - only authentic if made in Metsovo region",
            "The smoking uses aromatic mountain woods, traditionally beech",
            "Greece's only widely-produced smoked cheese"
        ],
        "tags": ["cheese", "Greek", "Epirus", "smoked", "pasta filata", "PDO", "mountain"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ADDITIONAL AGED CHEESES ===
    {
        "id": "san-michali-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "San Michali (Syros Island Aged Cheese)",
        "category": "cheese",
        "attribution": "Traditional Cycladic cheese",
        "source_note": "PDO hard cheese from the island of Syros, only Greek cheese from cow's milk with PDO.",
        "description": "A hard, aged cheese from the island of Syros, unique as Greece's only PDO cheese made exclusively from cow's milk. Sharp, granular, and perfect for grating, it reflects the island's Venetian heritage.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "8-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat cow's milk to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 50 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes."},
            {"step": 4, "text": "Heat slowly to 118°F (48°C) over 45 minutes while stirring continuously."},
            {"step": 5, "text": "Hold temperature and stir until curds are very firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and press at 30 lbs for 2 hours, flip, then 45 lbs for 24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 2-3 days."},
            {"step": 8, "text": "Age at 55°F (13°C) and 80% humidity for 8-12 months, turning weekly."}
        ],
        "temperature": "95-118°F (35-48°C)",
        "notes": [
            "Named after the patron saint of the village where it originated",
            "Reflects Venetian and Italian influence on Syros island",
            "Only Greek PDO cheese made exclusively from cow's milk",
            "Similar in use to Parmesan or aged Pecorino"
        ],
        "tags": ["cheese", "Greek", "Cycladic", "hard", "PDO", "cow's milk", "aged", "grating"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "kefalograviera-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kefalograviera (Hybrid Greek Hard Cheese)",
        "category": "cheese",
        "attribution": "Traditional Greek cheese",
        "source_note": "A modern Greek cheese combining characteristics of kefalotyri and graviera.",
        "description": "A hard Greek cheese that combines the sharpness of kefalotyri with the sweetness of graviera. Light yellow with small holes, it's versatile for both table use and cooking, especially frying for saganaki.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-8 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1.5", "unit": "gallons"},
            {"item": "goat's milk", "quantity": "0.5", "unit": "gallon"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milks and heat to 92°F (33°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-50 minutes."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 118°F (48°C) over 45 minutes while stirring."},
            {"step": 5, "text": "Continue stirring until curds are firm, about 25 minutes more."},
            {"step": 6, "text": "Drain and press at 25 lbs for 1 hour, flip, then 40 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine for 24-48 hours in saturated solution."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 3-8 months."}
        ],
        "temperature": "92-118°F (33-48°C)",
        "notes": [
            "A 20th century creation combining two classic Greek cheeses",
            "The name literally combines kefalo- and -graviera",
            "More approachable than pure kefalotyri, more complex than graviera",
            "Excellent for saganaki due to high melting point"
        ],
        "tags": ["cheese", "Greek", "hard", "table cheese", "saganaki", "sheep's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Greek cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in GREEK_CHEESE_RECIPES:
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
