#!/usr/bin/env python3
"""Add comprehensive Eastern European cheese recipes to the cheese category."""

import json

EASTERN_EUROPEAN_CHEESE_RECIPES = [
    # === SLOVAK/POLISH CHEESES ===
    {
        "id": "bryndza-slovak-sheep-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bryndza (Slovak/Polish Sheep Cheese Spread)",
        "category": "cheese",
        "attribution": "Traditional Slovak/Polish cheese",
        "source_note": "Slovakia's national cheese, protected by EU geographical indication since 2008.",
        "description": "Tangy, spreadable sheep's milk cheese essential for bryndzove halusky (Slovak national dish). This crumbly, pungent cheese has been made in the Carpathian Mountains for centuries by shepherd communities.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-4 weeks aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 86°F (30°C). Add starter culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Let set for 45-60 minutes until firm curd forms."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Let rest 10 minutes."},
            {"step": 4, "text": "Gently stir curds for 20 minutes, maintaining temperature."},
            {"step": 5, "text": "Drain curds and press lightly for 2 hours to form a basic cheese (this is called 'hrudka')."},
            {"step": 6, "text": "Break the pressed cheese into small pieces and salt lightly."},
            {"step": 7, "text": "Age the pieces at 55-60°F (13-15°C) for 2-4 weeks until they develop sharp flavor."},
            {"step": 8, "text": "Grind or mash the aged cheese until smooth and spreadable. Add salt to taste."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Traditional bryndza must be made from at least 50% sheep's milk",
            "The longer it ages before grinding, the sharper the flavor",
            "Essential for bryndzove halusky (potato dumplings with sheep cheese)",
            "Can be mixed with butter for smoother spreading consistency"
        ],
        "tags": ["cheese", "Eastern European", "Slovak", "Polish", "sheep's milk", "spreadable"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "oscypek-polish-smoked-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Oscypek (Polish Smoked Sheep's Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Polish highland cheese",
        "source_note": "Protected Designation of Origin cheese from the Tatra Mountain region of Poland.",
        "description": "Distinctive spindle-shaped smoked cheese made by Goral highlanders in the Tatra Mountains. The intricate decorative patterns pressed into the rind and the cold-smoking process create a unique cheese with centuries of tradition.",
        "servings_yield": "About 1 lb (2 spindles)",
        "prep_time": "1 hour",
        "cook_time": "3 hours plus smoking",
        "total_time": "3-5 days including smoking",
        "ingredients": [
            {"item": "sheep's milk (or 60% sheep, 40% cow)", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tbsp"},
            {"item": "cold smoking wood chips (beech or pine)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh milk to 95°F (35°C). Add rennet and let set 30-40 minutes."},
            {"step": 2, "text": "Cut curds finely and gather into a mass. Knead in warm whey until elastic."},
            {"step": 3, "text": "While still warm and pliable, form into traditional spindle shape (pointed at both ends)."},
            {"step": 4, "text": "Press decorative patterns into the surface using traditional carved wooden molds."},
            {"step": 5, "text": "Soak in saturated brine for 12-24 hours."},
            {"step": 6, "text": "Air dry for 24 hours until surface is no longer wet."},
            {"step": 7, "text": "Cold smoke at below 85°F (29°C) for 2-3 days using beech or pine wood."},
            {"step": 8, "text": "Age in cool, ventilated area for 2-4 weeks. Surface should be golden-brown."}
        ],
        "temperature": "95°F (35°C), smoke below 85°F (29°C)",
        "notes": [
            "Only cheese made by licensed bacas (head shepherds) in specific regions can be called Oscypek",
            "Traditional decorative patterns identify the maker",
            "Grilled oscypek with cranberry sauce is a popular Polish street food",
            "The spindle shape is achieved by hand-molding warm, elastic curd"
        ],
        "tags": ["cheese", "Eastern European", "Polish", "smoked", "sheep's milk", "Tatra Mountains"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "twarog-polish-quark",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Twarog (Polish Quark/Farmer's Cheese)",
        "category": "cheese",
        "attribution": "Traditional Polish fresh cheese",
        "source_note": "Staple of Polish cuisine, used in both sweet and savory dishes.",
        "description": "Fresh, acid-set Polish cheese similar to quark. Slightly tangy with a crumbly-creamy texture, it's essential for pierogi fillings, cheesecakes (sernik), and breakfast spreads throughout Poland.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "15 min",
        "cook_time": "1 hour",
        "total_time": "24-48 hours",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "cultured buttermilk", "quantity": "1", "unit": "cup"},
            {"item": "salt (optional)", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine milk and buttermilk in a large pot. Stir well."},
            {"step": 2, "text": "Cover and let stand at room temperature (68-72°F/20-22°C) for 24-48 hours until thick and clabbered."},
            {"step": 3, "text": "When milk has set into a solid mass with clear whey, cut into 2-inch cubes."},
            {"step": 4, "text": "Very slowly heat to 110°F (43°C) over 30-45 minutes, stirring gently."},
            {"step": 5, "text": "Hold at temperature until curds firm up and whey is clear, about 20-30 minutes."},
            {"step": 6, "text": "Pour into cheesecloth-lined colander. Drain for 1-2 hours."},
            {"step": 7, "text": "Gather cloth and hang to drain for additional 2-4 hours for drier texture."},
            {"step": 8, "text": "Transfer to container. Add salt if desired. Refrigerate immediately."}
        ],
        "temperature": "Room temperature for culturing, 110°F (43°C) for cooking",
        "notes": [
            "For creamier twarog, drain less time; for drier, drain longer",
            "Traditional for Polish sernik (cheesecake) - use full-fat for best results",
            "Mixed with sugar and vanilla for sweet pierogi filling",
            "Mixed with chives and radishes for savory breakfast spread"
        ],
        "tags": ["cheese", "Eastern European", "Polish", "fresh", "quark", "acid-set"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bundz-polish-fresh-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bundz (Polish Fresh Sheep's Milk Cheese)",
        "category": "cheese",
        "attribution": "Traditional Polish highland cheese",
        "source_note": "Fresh sheep's milk cheese from the Podhale region, precursor to oscypek.",
        "description": "Soft, fresh sheep's milk cheese made in the Tatra Mountains. This is the unsmoked, unaged form that can become oscypek if smoked. Mild, milky, and slightly tangy with a squeaky texture.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "fresh sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet diluted in cool water. Stir gently for 30 seconds."},
            {"step": 3, "text": "Let set undisturbed for 30-40 minutes until firm curd forms."},
            {"step": 4, "text": "Cut curds into 1/2-inch cubes. Let rest 5 minutes."},
            {"step": 5, "text": "Gently stir curds for 10-15 minutes while maintaining temperature."},
            {"step": 6, "text": "Drain curds and press lightly in molds for 1-2 hours."},
            {"step": 7, "text": "Salt the surface lightly."},
            {"step": 8, "text": "Eat fresh within 3-5 days, or proceed to smoke for oscypek."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Bundz is the fresh form; oscypek is bundz that has been smoked",
            "Best eaten very fresh when the texture is soft and squeaky",
            "Traditional highlander breakfast with bread and honey",
            "Can be grilled briefly for a different texture"
        ],
        "tags": ["cheese", "Eastern European", "Polish", "fresh", "sheep's milk", "highland"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === HUNGARIAN CHEESES ===
    {
        "id": "liptauer-hungarian-spread",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Liptauer (Hungarian Spiced Cheese Spread)",
        "category": "cheese",
        "attribution": "Traditional Hungarian cheese spread",
        "source_note": "Named after the Liptov region, now in Slovakia, this spread is beloved across Central Europe.",
        "description": "Vibrant orange-red spiced cheese spread made with sheep's cheese, paprika, and aromatics. This piquant spread is a fixture of Hungarian cuisine, perfect on dark bread with beer.",
        "servings_yield": "About 2 cups",
        "prep_time": "20 min",
        "cook_time": "0",
        "total_time": "20 min plus chilling",
        "ingredients": [
            {"item": "fresh sheep's cheese or quark", "quantity": "1", "unit": "lb"},
            {"item": "softened butter", "quantity": "4", "unit": "tbsp"},
            {"item": "sweet Hungarian paprika", "quantity": "2", "unit": "tbsp"},
            {"item": "caraway seeds", "quantity": "1", "unit": "tsp"},
            {"item": "Dijon mustard", "quantity": "1", "unit": "tsp"},
            {"item": "capers, minced", "quantity": "1", "unit": "tbsp"},
            {"item": "minced shallot", "quantity": "2", "unit": "tbsp"},
            {"item": "minced chives", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "to taste", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Press sheep's cheese or quark through a fine sieve for smooth texture."},
            {"step": 2, "text": "Beat softened butter until fluffy. Combine with pressed cheese."},
            {"step": 3, "text": "Add paprika, caraway seeds, and mustard. Mix thoroughly."},
            {"step": 4, "text": "Fold in capers, shallot, and chives."},
            {"step": 5, "text": "Season with salt to taste."},
            {"step": 6, "text": "Pack into a crock or bowl. Refrigerate at least 2 hours for flavors to meld."},
            {"step": 7, "text": "Serve at room temperature with dark rye bread."}
        ],
        "temperature": "Room temperature for serving",
        "notes": [
            "The iconic orange color comes from paprika, not artificial coloring",
            "Some versions add anchovy paste for extra umami",
            "Called Liptovsky Syr in Slovak, Liptauer in Austrian cuisine",
            "Traditionally served as part of a cold appetizer spread"
        ],
        "tags": ["cheese", "Eastern European", "Hungarian", "spread", "paprika", "spiced"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "trappista-hungarian-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Trappista (Hungarian Trappist Cheese)",
        "category": "cheese",
        "attribution": "Traditional Hungarian monastery cheese",
        "source_note": "Introduced by French Trappist monks to Hungary in the 19th century.",
        "description": "Semi-hard, mild Hungarian cheese with a supple texture and small eyes. Brought to Hungary by Trappist monks, it became one of the country's most popular everyday cheeses. Excellent for slicing and melting.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "4-8 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter culture and ripen for 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set for 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 100°F (38°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Remove 30% of whey and replace with same-temperature water. Continue stirring 20 minutes."},
            {"step": 6, "text": "Drain curds and press at 15 lbs for 30 minutes, flip, then 30 lbs for 8 hours."},
            {"step": 7, "text": "Brine in saturated solution for 8 hours per pound."},
            {"step": 8, "text": "Age at 55°F (13°C) and 85% humidity for 4-8 weeks. Turn weekly."}
        ],
        "temperature": "90-100°F (32-38°C)",
        "notes": [
            "Washed-curd technique gives mild, sweet flavor",
            "Hungarian Trappista is milder than French Port-Salut",
            "One of Hungary's most consumed cheeses",
            "Excellent melting properties for cooking"
        ],
        "tags": ["cheese", "Eastern European", "Hungarian", "semi-hard", "Trappist", "monastery"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "palpusztai-hungarian-washed-rind",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Palpusztai (Hungarian Washed-Rind Cheese)",
        "category": "cheese",
        "attribution": "Traditional Hungarian pungent cheese",
        "source_note": "Hungary's famous 'stinky cheese' from the Pusztai region.",
        "description": "Pungent, soft Hungarian cheese with an orange washed rind and creamy interior. Bold and assertive, this is Hungary's answer to Limburger. Not for the faint-hearted, but beloved by aficionados.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "4-6 weeks aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "Brevibacterium linens", "quantity": "1/16", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1.5", "unit": "tbsp"},
            {"item": "brine solution for washing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and B. linens, ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 60-75 minutes for soft curd."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes without stirring."},
            {"step": 4, "text": "Gently ladle curds into molds without pressing. Drain 12-18 hours, flipping every 4 hours."},
            {"step": 5, "text": "Salt all surfaces generously."},
            {"step": 6, "text": "Age at 55-60°F (13-15°C) and 95% humidity."},
            {"step": 7, "text": "Wash rind with light brine solution every 2-3 days."},
            {"step": 8, "text": "Ready in 4-6 weeks when rind is sticky, orange, and aromatic, interior is soft and creamy."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "The strong aroma comes from B. linens bacteria on the rind",
            "Interior should be runny when fully ripe",
            "Traditional pairing with onions and paprika",
            "Store separately - the aroma will transfer to other foods"
        ],
        "tags": ["cheese", "Eastern European", "Hungarian", "washed-rind", "pungent", "soft"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ROMANIAN CHEESES ===
    {
        "id": "branza-de-burduf-romanian-bark",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Branza de Burduf (Romanian Cheese in Bark)",
        "category": "cheese",
        "attribution": "Traditional Romanian aged cheese",
        "source_note": "Ancient Carpathian cheese traditionally aged in pine bark or sheep stomach.",
        "description": "Strong, tangy Romanian sheep's cheese traditionally aged in pine bark cylinders or sheep's stomach. The unique aging vessel imparts subtle resinous notes and creates a distinctive ripening environment.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 months aging",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "pine bark cylinder (optional, for traditional method)", "quantity": "1", "unit": "piece"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C). Add rennet and let set 45 minutes."},
            {"step": 2, "text": "Cut curds into 1/2-inch cubes. Stir gently for 15 minutes."},
            {"step": 3, "text": "Drain and press curds into a basic fresh cheese. Age at room temperature for 1-2 weeks until sharp."},
            {"step": 4, "text": "Break aged cheese into small pieces and knead with salt until uniform paste forms."},
            {"step": 5, "text": "Traditional: Pack tightly into cleaned pine bark cylinder or sheep stomach."},
            {"step": 6, "text": "Modern: Pack into ceramic crock or glass jar."},
            {"step": 7, "text": "Seal tightly and age at 50-55°F (10-13°C) for 2-4 months."},
            {"step": 8, "text": "Cheese is ready when very strong, tangy, and paste-like in texture."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Pine bark imparts subtle resinous, forest notes",
            "Traditional vessel was sheep's stomach (burduf)",
            "Very strong flavor - a little goes a long way",
            "Serve with mamaliga (Romanian polenta) and sour cream"
        ],
        "tags": ["cheese", "Eastern European", "Romanian", "sheep's milk", "aged", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "cas-romanian-fresh-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cas (Romanian Fresh Sheep's Cheese)",
        "category": "cheese",
        "attribution": "Traditional Romanian fresh cheese",
        "source_note": "Basic fresh cheese that forms the foundation of Romanian cheese-making.",
        "description": "Fresh, mild Romanian sheep's milk cheese - the starting point for many other Romanian cheeses. Soft and elastic when fresh, it can be eaten immediately or further processed into aged varieties.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day",
        "ingredients": [
            {"item": "fresh sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet diluted in cool water. Stir briefly."},
            {"step": 3, "text": "Let set undisturbed for 40-50 minutes until firm curd."},
            {"step": 4, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 5, "text": "Gently stir for 10 minutes while maintaining temperature."},
            {"step": 6, "text": "Drain curds and place in mold. Press very lightly for 2-3 hours."},
            {"step": 7, "text": "Salt the surface lightly."},
            {"step": 8, "text": "Eat within 3-5 days, or proceed to make telemea or burduf."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Cas is the foundation - it becomes telemea when brined, burduf when aged in bark",
            "Fresh cas has mild, milky flavor and elastic texture",
            "Can be made with cow's milk but sheep's is traditional",
            "Best eaten same day for maximum freshness"
        ],
        "tags": ["cheese", "Eastern European", "Romanian", "fresh", "sheep's milk"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "telemea-romanian-brined",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Telemea (Romanian Brined White Cheese)",
        "category": "cheese",
        "attribution": "Traditional Romanian brined cheese",
        "source_note": "Romania's most popular cheese, similar to Greek feta but with distinct character.",
        "description": "Tangy, crumbly Romanian brined cheese similar to feta. Made from sheep's or cow's milk and aged in brine, it's essential for Romanian salads, pastries, and as a table cheese.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-4 weeks in brine",
        "ingredients": [
            {"item": "sheep's milk (or cow's milk)", "quantity": "1", "unit": "gallon"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt for brine", "quantity": "1", "unit": "lb"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Let set 45-60 minutes until firm curd."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 20 minutes, maintaining temperature."},
            {"step": 5, "text": "Drain curds and ladle into molds. Press very lightly for 4-6 hours."},
            {"step": 6, "text": "Cut pressed cheese into 3-inch blocks."},
            {"step": 7, "text": "Prepare saturated brine (dissolve salt in water until no more dissolves)."},
            {"step": 8, "text": "Submerge cheese blocks in brine. Age at 50-55°F (10-13°C) for 2-4 weeks minimum."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Telemea develops more tang the longer it sits in brine",
            "Sheep's milk version is richer and more traditional",
            "Rinse briefly before eating if too salty",
            "Essential for Romanian salata de varza (cabbage salad)"
        ],
        "tags": ["cheese", "Eastern European", "Romanian", "brined", "white cheese", "feta-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "urda-romanian-whey-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Urda (Romanian Whey Cheese)",
        "category": "cheese",
        "attribution": "Traditional Romanian whey cheese",
        "source_note": "Made from whey leftover from other cheese production, similar to Italian ricotta.",
        "description": "Delicate, sweet Romanian whey cheese similar to ricotta. Made by heating whey until the remaining proteins coagulate, it's a economical way to use every part of the milk.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "1 hour",
        "total_time": "2-3 hours",
        "ingredients": [
            {"item": "fresh whey (from cheese making)", "quantity": "1", "unit": "gallon"},
            {"item": "whole milk (optional, for richer urda)", "quantity": "1", "unit": "cup"},
            {"item": "white vinegar or lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Start with fresh, still-warm whey from making cas or telemea."},
            {"step": 2, "text": "Optionally add whole milk for richer texture."},
            {"step": 3, "text": "Heat whey slowly to 195-200°F (90-93°C), stirring occasionally."},
            {"step": 4, "text": "When white foam appears on surface, add vinegar or lemon juice."},
            {"step": 5, "text": "Continue heating until white curds float to the top. Do not boil."},
            {"step": 6, "text": "Remove from heat and let rest 10 minutes."},
            {"step": 7, "text": "Skim curds from surface into cheesecloth-lined colander."},
            {"step": 8, "text": "Drain 1-2 hours. Salt lightly. Use fresh within 5 days."}
        ],
        "temperature": "195-200°F (90-93°C)",
        "notes": [
            "Must use very fresh whey - same day as cheese making",
            "Adding milk increases yield and richness",
            "Traditional Romanian breakfast with honey and sour cream",
            "Can be smoked for a different character (urda afumata)"
        ],
        "tags": ["cheese", "Eastern European", "Romanian", "whey cheese", "fresh", "ricotta-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === BULGARIAN CHEESES ===
    {
        "id": "kashkaval-bulgarian-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kashkaval (Bulgarian Yellow Cheese)",
        "category": "cheese",
        "attribution": "Traditional Bulgarian cheese",
        "source_note": "Bulgaria's most popular yellow cheese, from the Italian cascaval/caciocavallo tradition.",
        "description": "Semi-hard Bulgarian pasta filata cheese with a smooth, elastic texture and mild, slightly tangy flavor. Essential for Bulgarian cuisine, it's excellent for slicing, grilling, and baking.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "sheep's milk (or cow's milk)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 95°F (35°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 105°F (41°C) over 30 minutes while stirring."},
            {"step": 5, "text": "Drain curds and let mat together for 1-2 hours until pH drops (curd stretches when tested in hot water)."},
            {"step": 6, "text": "Cut curd into strips. Place in 170°F (77°C) water and knead until smooth and stretchy."},
            {"step": 7, "text": "Form into balls or blocks. Salt surfaces or brine for 12 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-3 months. Rub with oil if rind dries."}
        ],
        "temperature": "95-170°F (35-77°C)",
        "notes": [
            "Kashkaval means 'horse cheese' from the shape hung over horse saddles",
            "Sheep's milk version (kashkaval ot ovche mlyako) is premium",
            "Pan-fried kashkaval (kashkaval pane) is a popular appetizer",
            "Essential ingredient in Bulgarian banitsa pastry"
        ],
        "tags": ["cheese", "Eastern European", "Bulgarian", "pasta filata", "semi-hard", "yellow cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sirene-bulgarian-white-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sirene (Bulgarian White Brined Cheese)",
        "category": "cheese",
        "attribution": "Traditional Bulgarian white cheese",
        "source_note": "Bulgaria's national cheese, similar to feta but with distinct Bulgarian character.",
        "description": "Tangy, crumbly Bulgarian brined cheese that's a cornerstone of Bulgarian cuisine. Made from sheep's, goat's, or cow's milk, it's eaten at nearly every meal and essential for shopska salata.",
        "servings_yield": "About 1.5 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "3-6 weeks in brine",
        "ingredients": [
            {"item": "sheep's milk (or cow's milk)", "quantity": "1", "unit": "gallon"},
            {"item": "Bulgarian yogurt or mesophilic starter", "quantity": "2", "unit": "tbsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "lb"},
            {"item": "water for brine", "quantity": "1", "unit": "gallon"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add yogurt or starter and ripen 30 minutes."},
            {"step": 2, "text": "Add rennet diluted in water. Let set 45-60 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 15 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes at temperature."},
            {"step": 5, "text": "Ladle curds into molds lined with cheesecloth. Drain without pressing for 6-8 hours."},
            {"step": 6, "text": "Cut into blocks about 3 inches on each side."},
            {"step": 7, "text": "Make saturated brine. Submerge cheese blocks."},
            {"step": 8, "text": "Age in brine at 50°F (10°C) for minimum 3 weeks, up to several months."}
        ],
        "temperature": "90°F (32°C)",
        "notes": [
            "Using Bulgarian yogurt as starter gives authentic tang",
            "Sirene is less crumbly than Greek feta",
            "Essential for shopska salata - the Bulgarian national salad",
            "Can be aged much longer for sharper flavor"
        ],
        "tags": ["cheese", "Eastern European", "Bulgarian", "brined", "white cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SERBIAN CHEESE ===
    {
        "id": "kajmak-serbian-cream-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kajmak (Serbian Clotted Cream Cheese)",
        "category": "cheese",
        "attribution": "Traditional Serbian dairy product",
        "source_note": "Ancient Balkan clotted cream, essential for Serbian cuisine.",
        "description": "Rich, layered Serbian clotted cream cheese made by skimming cream from slowly heated milk over several days. Ranges from fresh and mild to aged and tangy, it's indispensable for cevapi and pljeskavica.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour daily",
        "total_time": "5-7 days for fresh, 2-3 months for aged",
        "ingredients": [
            {"item": "whole cow's milk (raw preferred)", "quantity": "1", "unit": "gallon"},
            {"item": "salt (for aged kajmak)", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Pour milk into wide, shallow pan. Gently heat to 185°F (85°C) without stirring."},
            {"step": 2, "text": "Remove from heat and let cool undisturbed in cool place overnight."},
            {"step": 3, "text": "Next day, carefully skim the thick cream layer that formed on top."},
            {"step": 4, "text": "Place skimmed cream in a crock, layering each day's collection."},
            {"step": 5, "text": "Repeat steps 1-4 daily for 5-7 days, layering cream each time."},
            {"step": 6, "text": "For fresh kajmak: Use immediately or refrigerate up to 1 week."},
            {"step": 7, "text": "For aged kajmak: Salt layers lightly, press down, and age at 50°F (10°C) for 2-3 months."},
            {"step": 8, "text": "Aged kajmak develops tangy, cheesy flavor while fresh is mild and buttery."}
        ],
        "temperature": "185°F (85°C) for heating",
        "notes": [
            "Raw milk produces thicker, more flavorful cream layer",
            "Fresh kajmak is like super-rich clotted cream",
            "Aged kajmak is tangy and cheese-like",
            "Essential accompaniment to cevapi (grilled meat) and Serbian pljeskavica"
        ],
        "tags": ["cheese", "Eastern European", "Serbian", "clotted cream", "fresh", "aged"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === CROATIAN CHEESE ===
    {
        "id": "paski-sir-croatian-sheep",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Paski Sir (Croatian Pag Island Sheep's Cheese)",
        "category": "cheese",
        "attribution": "Traditional Croatian sheep cheese",
        "source_note": "Protected Designation of Origin cheese from Pag Island, Croatia.",
        "description": "Hard, aromatic sheep's milk cheese from the Croatian island of Pag. The sheep graze on salt-sprayed herbs (especially sage), creating a unique, slightly salty, herbaceous cheese aged to crystalline perfection.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "5-12 months aging",
        "ingredients": [
            {"item": "sheep's milk (from Pag breed if possible)", "quantity": "2", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"},
            {"item": "olive oil for rubbing", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add rennet and let set 45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into small 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Heat slowly to 113°F (45°C) over 45 minutes while stirring."},
            {"step": 5, "text": "Continue stirring at temperature until curds are firm, about 30 minutes more."},
            {"step": 6, "text": "Drain and press at 20 lbs for 30 minutes, flip, then 40 lbs for 24 hours."},
            {"step": 7, "text": "Rub with sea salt or brine for 3-5 days."},
            {"step": 8, "text": "Age at 55°F (13°C) for minimum 5 months, up to 12+ months. Rub with olive oil monthly."}
        ],
        "temperature": "95-113°F (35-45°C)",
        "notes": [
            "Pag sheep graze on sage, rosemary, and salt-sprayed herbs",
            "The bura wind and sea salt spray flavor the milk naturally",
            "Develops crunchy amino acid crystals with long aging",
            "Often compared to aged Manchego or Pecorino"
        ],
        "tags": ["cheese", "Eastern European", "Croatian", "sheep's milk", "hard", "aged", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === SLOVENIAN CHEESE ===
    {
        "id": "tolminc-slovenian-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tolminc (Slovenian Alpine Cheese)",
        "category": "cheese",
        "attribution": "Traditional Slovenian mountain cheese",
        "source_note": "Protected Designation of Origin cheese from the Tolmin region of Slovenia.",
        "description": "Semi-hard Slovenian Alpine cheese with a smooth, supple texture and complex nutty flavor. Made from raw cow's milk in the Julian Alps, it represents centuries of Slovenian mountain dairy tradition.",
        "servings_yield": "About 2.5 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "2-6 months aging",
        "ingredients": [
            {"item": "raw cow's milk", "quantity": "3", "unit": "gallons"},
            {"item": "thermophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "3/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2.5", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat raw milk to 93°F (34°C). Add starter and ripen 30 minutes."},
            {"step": 2, "text": "Add rennet and let set 35-40 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 1/3-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 115°F (46°C) over 40 minutes while stirring constantly."},
            {"step": 5, "text": "Continue stirring at temperature until curds are firm and shrunk, about 30 minutes."},
            {"step": 6, "text": "Drain and press at 20 lbs for 30 minutes, flip, then 35 lbs for 12-24 hours."},
            {"step": 7, "text": "Brine in saturated solution for 24-36 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) and 90% humidity for 2-6 months. Turn and brush weekly."}
        ],
        "temperature": "93-115°F (34-46°C)",
        "notes": [
            "Raw milk is essential for authentic flavor",
            "Made in mountain dairy huts (planina) during summer",
            "Develops small irregular eyes during aging",
            "Pairs well with Slovenian wines from the Goriska region"
        ],
        "tags": ["cheese", "Eastern European", "Slovenian", "Alpine", "semi-hard", "raw milk", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === CZECH CHEESE ===
    {
        "id": "olomoucke-tvaruzky-czech-stinky",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Olomoucke Tvaruzky (Czech Ripened Cheese)",
        "category": "cheese",
        "attribution": "Traditional Czech pungent cheese",
        "source_note": "Czech Republic's only PDO cheese, made since the 15th century in Moravia.",
        "description": "Small, disc-shaped Czech cheese famous for its powerful aroma and sharp flavor. Made from skimmed quark and ripened until pungent, these 'stinky cheeses' are a beloved Czech delicacy, traditionally enjoyed with beer and onions.",
        "servings_yield": "About 1 lb (many small discs)",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "2-6 weeks ripening",
        "ingredients": [
            {"item": "low-fat quark or farmer's cheese", "quantity": "2", "unit": "lbs"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"},
            {"item": "Brevibacterium linens culture (optional)", "quantity": "pinch", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Start with well-drained, low-fat quark. Press to remove excess moisture if needed."},
            {"step": 2, "text": "Knead the quark with salt until smooth and uniform."},
            {"step": 3, "text": "Optionally add B. linens for more consistent ripening."},
            {"step": 4, "text": "Form into small flat discs about 1 inch diameter and 1/2 inch thick."},
            {"step": 5, "text": "Arrange discs on racks in ripening chamber at 50-55°F (10-13°C) and 90-95% humidity."},
            {"step": 6, "text": "Turn discs daily for first week."},
            {"step": 7, "text": "Surface will become sticky and develop yellow-orange color from natural bacteria."},
            {"step": 8, "text": "Ready in 2-6 weeks when fully yellowed, aromatic, and slightly soft. Longer aging = stronger flavor."}
        ],
        "temperature": "50-55°F (10-13°C)",
        "notes": [
            "The distinctive smell is from B. linens bacteria (same as Limburger)",
            "Traditional accompaniments: raw onion, rye bread, beer",
            "Only cheese in Czech Republic with Protected Designation of Origin",
            "Olomouc region has made these since 1452"
        ],
        "tags": ["cheese", "Eastern European", "Czech", "pungent", "ripened", "quark-based", "PDO"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    # === ADDITIONAL REGIONAL VARIETIES ===
    {
        "id": "gomolya-hungarian-sheep-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gomolya (Hungarian Fresh Sheep's Cheese)",
        "category": "cheese",
        "attribution": "Traditional Hungarian shepherd's cheese",
        "source_note": "Simple fresh sheep's cheese from Hungarian shepherding traditions.",
        "description": "Fresh Hungarian sheep's milk cheese shaped into small rounds. The name comes from its ball-like shape (gomoly). Mild and milky when fresh, often salted and dried for longer keeping.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "Same day to 2 weeks",
        "ingredients": [
            {"item": "sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat sheep's milk to 95°F (35°C)."},
            {"step": 2, "text": "Add rennet diluted in water. Let set 40-50 minutes."},
            {"step": 3, "text": "Cut curds into 1-inch cubes. Rest 10 minutes."},
            {"step": 4, "text": "Gently stir for 15 minutes at temperature."},
            {"step": 5, "text": "Drain curds and form into small balls about 2-3 inches diameter."},
            {"step": 6, "text": "Salt surfaces lightly."},
            {"step": 7, "text": "Eat fresh within 3-5 days, or dry on rack for 1-2 weeks for firmer texture."},
            {"step": 8, "text": "Dried gomolya can be stored longer and grated when very dry."}
        ],
        "temperature": "95°F (35°C)",
        "notes": [
            "Gomoly means 'ball' or 'lump' in Hungarian",
            "Traditional shepherd's cheese made in summer pastures",
            "Fresh version is squeaky and mild",
            "Dried version becomes crumbly and more pungent"
        ],
        "tags": ["cheese", "Eastern European", "Hungarian", "sheep's milk", "fresh", "shepherd's cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "korbaciky-slovak-string-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Korbaciky (Slovak Braided String Cheese)",
        "category": "cheese",
        "attribution": "Traditional Slovak smoked cheese",
        "source_note": "Decorative braided cheese from Slovakia, often smoked.",
        "description": "Distinctive braided Slovak string cheese, often smoked for extra flavor. The elaborate braiding technique is a point of pride, creating both a snack cheese and an edible decoration.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "Same day plus optional smoking",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "1", "unit": "tsp"},
            {"item": "smoking wood (optional)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Dissolve citric acid in 1/4 cup water. Add to cold milk."},
            {"step": 2, "text": "Heat milk to 88°F (31°C). Add rennet and stir briefly."},
            {"step": 3, "text": "Heat to 105°F (41°C). Curds will form."},
            {"step": 4, "text": "Drain curds. Let mat together 1-2 hours until stretchable."},
            {"step": 5, "text": "Heat whey or water to 170°F (77°C). Add curd and knead until smooth and stretchy."},
            {"step": 6, "text": "Pull into long thin strips about 1/4 inch thick."},
            {"step": 7, "text": "Braid strips into decorative patterns. Salt lightly."},
            {"step": 8, "text": "Optional: Cold smoke for 1-2 days for smoked korbaciky."}
        ],
        "temperature": "88-170°F (31-77°C)",
        "notes": [
            "The braiding technique takes practice to master",
            "Popular snack cheese throughout Slovakia and Czech Republic",
            "Smoked version has golden color and deeper flavor",
            "Often sold at Christmas markets and festivals"
        ],
        "tags": ["cheese", "Eastern European", "Slovak", "string cheese", "braided", "smoked"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Eastern European cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in EASTERN_EUROPEAN_CHEESE_RECIPES:
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
