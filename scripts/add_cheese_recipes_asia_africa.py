#!/usr/bin/env python3
"""Add Asian, African, and Oceania cheese recipes to the cheese category."""

import json

ASIA_AFRICA_OCEANIA_CHEESE_RECIPES = [
    # === ASIAN CHEESES ===
    {
        "id": "chhena-indian-fresh-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chhena (Indian Fresh Cheese for Sweets)",
        "category": "cheese",
        "attribution": "Traditional Indian cheese",
        "source_note": "Essential base for Bengali sweets like rasgulla and sandesh.",
        "description": "Soft, crumbly Indian fresh cheese made by curdling milk with acid. Unlike paneer which is pressed firm, chhena remains soft and malleable - the essential base for iconic Bengali sweets.",
        "servings_yield": "About 1 lb",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "1 hour",
        "ingredients": [
            {"item": "whole milk", "quantity": "1", "unit": "gallon"},
            {"item": "lemon juice or white vinegar", "quantity": "3", "unit": "tbsp"},
            {"item": "water", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Bring milk to a rolling boil in a heavy-bottomed pot, stirring frequently to prevent scorching."},
            {"step": 2, "text": "Reduce heat to low. Add lemon juice diluted in water, one tablespoon at a time, stirring gently."},
            {"step": 3, "text": "As soon as curds separate from greenish whey, stop adding acid. Remove from heat immediately."},
            {"step": 4, "text": "Let rest 5 minutes - do not over-acidify or chhena will become grainy."},
            {"step": 5, "text": "Strain through muslin cloth. Rinse curds under cold water to remove acidic taste."},
            {"step": 6, "text": "Gather cloth and squeeze gently - leave more moisture than for paneer."},
            {"step": 7, "text": "Knead the warm chhena on a clean surface until smooth and free of lumps, about 8-10 minutes."},
            {"step": 8, "text": "Use immediately for sweets, or refrigerate up to 2 days."}
        ],
        "temperature": "212°F (100°C)",
        "notes": [
            "Fresh chhena must be soft and pliable, never crumbly",
            "The kneading step is crucial - develops smooth texture needed for rasgulla",
            "Use full-fat milk for best results - low-fat produces dry, grainy chhena",
            "Called 'chenna' in some regions - same product, different spelling"
        ],
        "tags": ["cheese", "Indian", "Bengali", "fresh", "acid-set", "sweets base"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "kalari-kashmiri-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kalari (Kashmiri Fried Cheese)",
        "category": "cheese",
        "attribution": "Traditional Kashmiri cheese",
        "source_note": "Ancient cheese from the Gujjar and Bakerwal herding communities of Kashmir.",
        "description": "Dense, chewy Kashmiri cheese traditionally made from raw buffalo or cow milk. When fried, it develops a crispy golden exterior while becoming molten inside - Kashmir's answer to halloumi.",
        "servings_yield": "About 12 oz",
        "prep_time": "30 min",
        "cook_time": "3 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "raw whole milk (cow or buffalo)", "quantity": "1", "unit": "gallon"},
            {"item": "soured buttermilk or yogurt whey", "quantity": "1", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 185°F (85°C) in a heavy pot, stirring occasionally."},
            {"step": 2, "text": "Remove from heat and add soured buttermilk gradually while stirring."},
            {"step": 3, "text": "Let stand 15-20 minutes until curds form and separate from whey."},
            {"step": 4, "text": "Strain through muslin, collecting curds. Save whey for next batch."},
            {"step": 5, "text": "While still warm, knead curds with salt until smooth and pliable."},
            {"step": 6, "text": "Shape into flat disc or dome shape, about 1 inch thick."},
            {"step": 7, "text": "Air dry in cool place for 2-3 days until firm and slightly leathery on outside."},
            {"step": 8, "text": "To serve: Slice thick pieces and fry in ghee until golden brown on both sides."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Traditional Kalari is smoke-dried over wood fires for preservation",
            "Buffalo milk produces denser, richer kalari than cow milk",
            "Fried kalari is often served with bread or in kulcha sandwiches",
            "The Gujjar nomads make this while moving with their herds"
        ],
        "tags": ["cheese", "Indian", "Kashmiri", "frying cheese", "buffalo milk", "traditional"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "bandel-bengali-smoked-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bandel Cheese (Bengali Smoked Cheese)",
        "category": "cheese",
        "attribution": "Traditional Bengali cheese",
        "source_note": "Portuguese-influenced smoked cheese from Bandel, West Bengal.",
        "description": "Unique smoked cheese from the former Portuguese settlement of Bandel near Kolkata. Made from cow's milk and smoked over rice husk fires, it comes in both fresh and aged varieties.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "4 hours",
        "total_time": "3-5 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1", "unit": "gallon"},
            {"item": "lemon juice", "quantity": "3", "unit": "tbsp"},
            {"item": "salt", "quantity": "2", "unit": "tsp"},
            {"item": "rice husks or paddy straw (for smoking)", "quantity": "as needed", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to boiling in a heavy pot, stirring to prevent scorching."},
            {"step": 2, "text": "Reduce heat and add lemon juice slowly until curds separate from whey."},
            {"step": 3, "text": "Strain through muslin. Rinse curds with cold water."},
            {"step": 4, "text": "Mix salt into curds while still warm. Knead until smooth."},
            {"step": 5, "text": "Shape into small balls or flat discs, about 2-3 inches diameter."},
            {"step": 6, "text": "Press gently to remove excess moisture. Let drain overnight."},
            {"step": 7, "text": "Set up smoker with rice husks or paddy straw. Cold smoke cheese for 6-8 hours."},
            {"step": 8, "text": "Age at room temperature 2-3 days for fresh style, or 2-3 weeks for aged version."}
        ],
        "temperature": "212°F (100°C) for curdling, cold smoke",
        "notes": [
            "Portuguese settlers introduced cheesemaking to Bandel in 16th century",
            "Rice husk smoke gives distinctive earthy, slightly sweet flavor",
            "Fresh Bandel is soft and mild; aged version is hard and pungent",
            "Nearly extinct - only a few families still make traditional Bandel"
        ],
        "tags": ["cheese", "Indian", "Bengali", "smoked", "Portuguese-influenced", "heritage"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "rushan-yunnan-fan-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rushan (Yunnan Fan-Shaped Cheese)",
        "category": "cheese",
        "attribution": "Traditional Bai ethnic minority cheese",
        "source_note": "Unique stretched cheese from the Bai people of Yunnan, China.",
        "description": "Distinctive Chinese cheese made by the Bai ethnic group near Dali. Fresh milk curds are stretched into thin sheets and dried on bamboo frames, resembling decorative fans. Served grilled or fried.",
        "servings_yield": "About 8 pieces",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "1 day",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "soured whey or rice vinegar", "quantity": "1/2", "unit": "cup"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 160°F (71°C) in a wide, shallow pan."},
            {"step": 2, "text": "Add soured whey or diluted rice vinegar slowly while stirring."},
            {"step": 3, "text": "As curds form, use chopsticks or paddle to gather them together."},
            {"step": 4, "text": "When curds are cohesive, remove from whey and knead while still hot."},
            {"step": 5, "text": "Working quickly, stretch the cheese mass like pulling taffy."},
            {"step": 6, "text": "Wrap stretched cheese around bamboo sticks, spreading thin like a fan."},
            {"step": 7, "text": "Sprinkle with salt. Dry in sun or warm area for 12-24 hours until leathery."},
            {"step": 8, "text": "To serve: Grill over charcoal until puffed and golden, or deep-fry."}
        ],
        "temperature": "160°F (71°C)",
        "notes": [
            "Rushan means 'milk fan' - describes the traditional shape",
            "Street vendors in Dali grill rushan and drizzle with rose syrup",
            "The Bai people are one of few Chinese ethnic groups with dairy tradition",
            "Best eaten hot when the cheese is stretchy and slightly caramelized"
        ],
        "tags": ["cheese", "Chinese", "Yunnan", "Bai", "stretched", "grilled"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "rubing-yunnan-grilled-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rubing (Yunnan Grilled Goat Cheese)",
        "category": "cheese",
        "attribution": "Traditional Sani ethnic minority cheese",
        "source_note": "Fresh goat cheese from the Sani people of Yunnan's Stone Forest region.",
        "description": "Fresh, firm goat cheese blocks from Yunnan Province, made by the Sani branch of the Yi ethnic group. Mild when raw, it transforms when grilled into a squeaky, savory treat with crispy edges.",
        "servings_yield": "About 1 lb",
        "prep_time": "20 min",
        "cook_time": "2 hours",
        "total_time": "4-6 hours",
        "ingredients": [
            {"item": "fresh goat's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "soured goat milk or vinegar", "quantity": "1/4", "unit": "cup"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat goat's milk to 175°F (80°C), stirring occasionally."},
            {"step": 2, "text": "Remove from heat and add acidic whey or diluted vinegar gradually."},
            {"step": 3, "text": "Stir gently until curds form and separate from whey."},
            {"step": 4, "text": "Let rest 10 minutes, then strain through cheesecloth."},
            {"step": 5, "text": "While warm, add salt and knead curds into a smooth mass."},
            {"step": 6, "text": "Press into rectangular molds or shape by hand into thick blocks."},
            {"step": 7, "text": "Weight down and press for 2-4 hours until firm."},
            {"step": 8, "text": "To serve: Slice into 1/2-inch pieces and grill or pan-fry until golden spots appear."}
        ],
        "temperature": "175°F (80°C)",
        "notes": [
            "Rubing means 'milk cake' in Chinese",
            "Traditional accompaniment to Yunnan mint and chili dishes",
            "The Sani people have raised goats for cheese for centuries",
            "Fresh rubing is very mild - grilling brings out nutty flavors"
        ],
        "tags": ["cheese", "Chinese", "Yunnan", "goat cheese", "fresh", "grilling"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "sakura-cheese-japanese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sakura Cheese (Japanese Cherry Blossom Cheese)",
        "category": "cheese",
        "attribution": "Modern Japanese artisan cheese",
        "source_note": "Award-winning Japanese cheese featuring preserved cherry blossoms.",
        "description": "Elegant Japanese cream cheese decorated with preserved cherry blossoms and cherry leaves. A modern artisan creation that has won international awards, it embodies Japanese aesthetics and seasonal appreciation.",
        "servings_yield": "About 1 lb",
        "prep_time": "45 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "heavy cream", "quantity": "1", "unit": "cup"},
            {"item": "mesophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "2", "unit": "drops"},
            {"item": "salt-preserved cherry blossoms (sakura)", "quantity": "2", "unit": "tbsp"},
            {"item": "salt-preserved cherry leaves", "quantity": "4-6", "unit": "leaves"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Soak preserved cherry blossoms and leaves in water for 30 minutes to remove excess salt. Pat dry."},
            {"step": 2, "text": "Combine milk and cream. Heat to 72°F (22°C)."},
            {"step": 3, "text": "Add starter culture, stir, and let ripen 1 hour."},
            {"step": 4, "text": "Add rennet diluted in water. Stir briefly, then let set 12-18 hours at room temperature."},
            {"step": 5, "text": "When curd is thick and pulls away from sides, ladle into cheesecloth-lined molds."},
            {"step": 6, "text": "Drain 24 hours at cool room temperature, flipping once."},
            {"step": 7, "text": "Unmold and gently mix in salt. Press cherry blossoms into top surface decoratively."},
            {"step": 8, "text": "Wrap bottom and sides in cherry leaves. Age 1-2 days refrigerated before serving."}
        ],
        "temperature": "72°F (22°C)",
        "notes": [
            "Hokkaido's dairy farms produce most Japanese artisan cheese",
            "Cherry blossoms impart subtle floral, slightly salty flavor",
            "Won gold at World Cheese Awards - put Japanese cheese on global map",
            "Best enjoyed in spring during cherry blossom season (hanami)"
        ],
        "tags": ["cheese", "Japanese", "artisan", "cream cheese", "cherry blossom", "seasonal"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # === AFRICAN CHEESES ===
    {
        "id": "ayib-ethiopian-cottage-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Ayib (Ethiopian Cottage Cheese)",
        "category": "cheese",
        "attribution": "Traditional Ethiopian cheese",
        "source_note": "Mild, crumbly cheese served with berbere-spiced dishes.",
        "description": "Soft, mild Ethiopian cottage cheese traditionally made from buttermilk left over from butter-making. Its cool, creamy texture provides essential contrast to spicy Ethiopian stews and is often served atop injera.",
        "servings_yield": "About 1 cup",
        "prep_time": "15 min",
        "cook_time": "30 min",
        "total_time": "2-3 hours",
        "ingredients": [
            {"item": "whole milk or buttermilk", "quantity": "1/2", "unit": "gallon"},
            {"item": "lemon juice or niter kibbeh whey", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1/4", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "If using whole milk, heat to 180°F (82°C). If using buttermilk, heat gently to 100°F (38°C)."},
            {"step": 2, "text": "For whole milk: add lemon juice and stir until curds form. For buttermilk: curds form naturally as it warms."},
            {"step": 3, "text": "Let stand 15-20 minutes until curds fully separate."},
            {"step": 4, "text": "Strain through cheesecloth, allowing whey to drain completely (1-2 hours)."},
            {"step": 5, "text": "Transfer curds to bowl. Add salt and mix gently, keeping texture crumbly."},
            {"step": 6, "text": "Do not press - ayib should remain loose and cottage cheese-like."},
            {"step": 7, "text": "Refrigerate and use within 3-4 days."},
            {"step": 8, "text": "Serve as cooling accompaniment to doro wat, kitfo, or other spicy dishes."}
        ],
        "temperature": "180°F (82°C) for milk, 100°F (38°C) for buttermilk",
        "notes": [
            "Traditionally made from ergo (Ethiopian fermented milk) byproduct",
            "Essential component of Ethiopian fasting dishes during Orthodox Lent",
            "The mild flavor deliberately contrasts with berbere-spiced foods",
            "Often mixed with mitmita spice or served plain"
        ],
        "tags": ["cheese", "Ethiopian", "African", "cottage cheese", "fresh", "acid-set"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wagashi-west-african-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wagashi (West African Fulani Cheese)",
        "category": "cheese",
        "attribution": "Traditional Fulani cheese",
        "source_note": "Fresh cheese made by Fulani herders across West Africa.",
        "description": "Soft, mild white cheese made by Fulani (Peul) pastoral communities across West Africa. Curdled with natural plant coagulants, it's sold fresh in markets and often fried for added flavor.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "fresh whole cow's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "Calotropis procera leaf extract (or lemon juice)", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat fresh milk to 185°F (85°C), stirring occasionally."},
            {"step": 2, "text": "Remove from heat. Add plant coagulant extract (traditionally from Sodom apple leaves) or lemon juice."},
            {"step": 3, "text": "Stir gently and let stand until curds form and separate, about 20 minutes."},
            {"step": 4, "text": "Line a woven basket or colander with clean cloth. Ladle in curds."},
            {"step": 5, "text": "Sprinkle salt over curds and fold cloth over top."},
            {"step": 6, "text": "Press lightly and drain for 2-3 hours until firm enough to slice."},
            {"step": 7, "text": "Cut into cubes or rounds."},
            {"step": 8, "text": "Eat fresh, or fry in palm oil until golden for preserved version (awara)."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Fulani women are traditionally the cheese-makers and sellers",
            "Plant-based coagulants include Calotropis procera (Sodom apple) and papaya latex",
            "Fried wagashi can last several days without refrigeration",
            "Common in Benin, Nigeria, Niger, and other Sahel countries"
        ],
        "tags": ["cheese", "African", "West African", "Fulani", "fresh", "plant-coagulated"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "wara-nigerian-soft-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wara (Nigerian Soft Cheese)",
        "category": "cheese",
        "attribution": "Traditional Yoruba and Nigerian cheese",
        "source_note": "West African soft cheese similar to wagashi, popular in Nigerian cuisine.",
        "description": "Soft, unaged Nigerian cheese traditionally made by Fulani herders and popular throughout Yorubaland. Similar to wagashi but often prepared with slight regional variations. Eaten fresh or fried as a protein-rich snack.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "1 hour",
        "total_time": "3-4 hours",
        "ingredients": [
            {"item": "fresh cow's milk", "quantity": "1/2", "unit": "gallon"},
            {"item": "Calotropis procera sap, papaya leaves, or lemon juice", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tsp"},
            {"item": "palm oil (for frying, optional)", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "If using papaya leaves, crush and soak in small amount of water to extract coagulant."},
            {"step": 2, "text": "Heat milk to 185°F (85°C) in a heavy pot."},
            {"step": 3, "text": "Remove from heat and add coagulant, stirring gently."},
            {"step": 4, "text": "Allow curds to form and settle, about 15-20 minutes."},
            {"step": 5, "text": "Strain through woven basket or cloth-lined colander."},
            {"step": 6, "text": "Add salt and press gently for 2-3 hours until firm."},
            {"step": 7, "text": "Cut into cubes. Serve fresh or proceed to frying."},
            {"step": 8, "text": "To fry: Heat palm oil and fry wara pieces until golden on all sides."}
        ],
        "temperature": "185°F (85°C)",
        "notes": [
            "Called 'tofu of Africa' for its versatility and protein content",
            "Fried wara is called 'wara elede' and is a popular street food",
            "Papaya leaves contain papain enzyme that curdles milk",
            "Often served with pepper sauce or in stews"
        ],
        "tags": ["cheese", "African", "Nigerian", "Yoruba", "fresh", "soft cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "gibna-bayda-sudanese-white-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Gibna Bayda (Sudanese White Cheese)",
        "category": "cheese",
        "attribution": "Traditional Sudanese cheese",
        "source_note": "Brined white cheese essential to Sudanese breakfast and cuisine.",
        "description": "Salty, firm white cheese that is a staple of Sudanese cuisine. Similar to feta, it's preserved in brine and served at nearly every Sudanese breakfast alongside ful medames and fresh bread.",
        "servings_yield": "About 1 lb",
        "prep_time": "30 min",
        "cook_time": "2 hours",
        "total_time": "2-3 days",
        "ingredients": [
            {"item": "whole cow's or sheep's milk", "quantity": "1", "unit": "gallon"},
            {"item": "plain yogurt with active cultures", "quantity": "1/4", "unit": "cup"},
            {"item": "liquid rennet or junket tablet", "quantity": "1/4", "unit": "tsp"},
            {"item": "salt", "quantity": "2", "unit": "tbsp"},
            {"item": "salt for brine", "quantity": "1/2", "unit": "cup"},
            {"item": "water for brine", "quantity": "4", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Stir in yogurt and let ripen 1 hour."},
            {"step": 2, "text": "Dissolve rennet in small amount of cool water. Add to milk and stir gently."},
            {"step": 3, "text": "Cover and let set undisturbed for 45-60 minutes until firm curd forms."},
            {"step": 4, "text": "Cut curd into 1-inch cubes. Let rest 10 minutes."},
            {"step": 5, "text": "Gently stir curds for 15 minutes, then let settle."},
            {"step": 6, "text": "Drain whey and transfer curds to cheesecloth-lined mold. Sprinkle salt between layers."},
            {"step": 7, "text": "Press with light weight for 6-8 hours, flipping once."},
            {"step": 8, "text": "Dissolve 1/2 cup salt in 4 cups water for brine. Submerge cheese and store refrigerated. Ready in 2-3 days."}
        ],
        "temperature": "86°F (30°C)",
        "notes": [
            "Gibna bayda means 'white cheese' in Arabic",
            "The brine preservation allows cheese to last for months",
            "Essential accompaniment to ful medames (fava bean stew)",
            "Sheep's milk version is richer and more traditional"
        ],
        "tags": ["cheese", "African", "Sudanese", "brined", "white cheese", "breakfast cheese"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "boerekaas-south-african-farmhouse",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Boerekaas (South African Farmhouse Cheese)",
        "category": "cheese",
        "attribution": "Traditional South African cheese",
        "source_note": "Farmhouse cheese tradition from Afrikaner farming communities.",
        "description": "Traditional South African farmhouse cheese made on Afrikaner farms for generations. Semi-hard with a mild, buttery flavor, it reflects the Dutch cheesemaking heritage adapted to African conditions.",
        "servings_yield": "About 2 lbs",
        "prep_time": "45 min",
        "cook_time": "3 hours",
        "total_time": "2-3 months aging",
        "ingredients": [
            {"item": "raw or pasteurized cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride (if using pasteurized)", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add starter culture and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride if using pasteurized milk, then rennet. Let set 45 minutes."},
            {"step": 3, "text": "Cut curds into 1/2-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 30 minutes while stirring gently."},
            {"step": 5, "text": "Continue stirring at temperature until curds shrink and firm, about 30 minutes more."},
            {"step": 6, "text": "Drain curds and press at 15 lbs for 30 minutes, flip, then 25 lbs for 8-12 hours."},
            {"step": 7, "text": "Rub all surfaces with salt or brine for 12 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) for 2-3 months, turning weekly and wiping with brine if mold appears."}
        ],
        "temperature": "90-102°F (32-39°C)",
        "notes": [
            "Boerekaas means 'farmer's cheese' in Afrikaans",
            "Dutch settlers brought Gouda-making traditions to South Africa",
            "Farm-made versions vary by region and family tradition",
            "Now experiencing artisanal revival with craft cheesemakers"
        ],
        "tags": ["cheese", "South African", "African", "farmhouse", "semi-hard", "Dutch-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },

    # === OCEANIA CHEESES ===
    {
        "id": "australian-cheddar-traditional",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Australian Cheddar (Traditional Style)",
        "category": "cheese",
        "attribution": "Traditional Australian cheese",
        "source_note": "Classic Australian cheddar following British traditions established in the 1800s.",
        "description": "Traditional Australian cheddar made following methods brought by British settlers. Australian cheddars tend to be slightly milder and less crumbly than English originals, adapted to local milk and climate conditions.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "3-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 86°F (30°C). Add starter and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45-60 minutes until clean break."},
            {"step": 3, "text": "Cut curds into 1/4-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 102°F (39°C) over 40 minutes, stirring gently."},
            {"step": 5, "text": "Maintain temperature and stir until curds are firm and squeaky, about 30 minutes."},
            {"step": 6, "text": "Drain whey, let curds mat together. Cut into slabs and stack (cheddaring) for 2 hours, flipping every 15 minutes."},
            {"step": 7, "text": "Mill curds into small pieces, add salt, mix well. Press at 20 lbs for 30 min, then 50 lbs for 24 hours."},
            {"step": 8, "text": "Age at 55°F (13°C) for minimum 3 months. For vintage cheddar, age 12+ months."}
        ],
        "temperature": "86-102°F (30-39°C)",
        "notes": [
            "Australian cheddar production began in Tasmania in the 1820s",
            "Cloth-bound versions are traditional; waxed versions are common",
            "Hot climate historically made aging challenging - cave aging is prized",
            "Australian vintage cheddars now compete with world's best"
        ],
        "tags": ["cheese", "Australian", "Oceania", "cheddar", "hard", "British-style"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    },
    {
        "id": "kapiti-new-zealand-aged-cheese",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kapiti-Style Aged Cheese (New Zealand)",
        "category": "cheese",
        "attribution": "New Zealand artisan cheese tradition",
        "source_note": "Premium aged cheese in the style of New Zealand's renowned Kapiti region.",
        "description": "Rich, complex aged cheese in the style of New Zealand's celebrated Kapiti cheesemakers. New Zealand's pristine pastures and year-round grazing produce exceptional milk for artisan cheese with deep, nuanced flavors.",
        "servings_yield": "About 2 lbs",
        "prep_time": "1 hour",
        "cook_time": "4 hours",
        "total_time": "6-12 months aging",
        "ingredients": [
            {"item": "whole cow's milk (grass-fed preferred)", "quantity": "2", "unit": "gallons"},
            {"item": "mesophilic starter culture", "quantity": "1/4", "unit": "tsp"},
            {"item": "thermophilic starter culture", "quantity": "1/8", "unit": "tsp"},
            {"item": "calcium chloride", "quantity": "1/4", "unit": "tsp"},
            {"item": "liquid rennet", "quantity": "1/2", "unit": "tsp"},
            {"item": "cheese salt", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Heat milk to 90°F (32°C). Add both starter cultures and ripen 45 minutes."},
            {"step": 2, "text": "Add calcium chloride, then rennet. Let set 45 minutes until firm break."},
            {"step": 3, "text": "Cut curds into 3/8-inch cubes. Rest 5 minutes."},
            {"step": 4, "text": "Slowly heat to 104°F (40°C) over 40 minutes, stirring gently."},
            {"step": 5, "text": "Hold temperature and stir until curds are well-shrunk and firm, about 45 minutes."},
            {"step": 6, "text": "Drain whey. Press curds at 15 lbs for 30 min, flip, 35 lbs for 12 hours."},
            {"step": 7, "text": "Brine in saturated solution for 12 hours per pound of cheese."},
            {"step": 8, "text": "Age at 50-55°F (10-13°C) and 85% humidity for 6-12 months. Turn weekly and brush off any mold."}
        ],
        "temperature": "90-104°F (32-40°C)",
        "notes": [
            "New Zealand's grass-fed cows produce distinctively rich, golden milk",
            "Kapiti Coast region is famous for artisan cheesemaking",
            "Mixed cultures create complex flavor profile during long aging",
            "New Zealand cheeses have won numerous international awards"
        ],
        "tags": ["cheese", "New Zealand", "Oceania", "aged", "artisan", "grass-fed"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": []
    }
]


def add_recipes():
    """Add Asian, African, and Oceania cheese recipes to the collection."""
    with open('data/recipes.json', 'r') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    existing_ids = {r['id'] for r in recipes if isinstance(r, dict)}

    added = 0
    skipped = 0

    for recipe in ASIA_AFRICA_OCEANIA_CHEESE_RECIPES:
        if recipe['id'] in existing_ids:
            print(f"Skipping existing: {recipe['id']}")
            skipped += 1
        else:
            recipes.append(recipe)
            existing_ids.add(recipe['id'])
            print(f"Added: {recipe['title']}")
            added += 1

    data['recipes'] = recipes

    # Update meta counts
    if 'meta' in data:
        data['meta']['total_count'] = len(recipes)
        data['meta']['total_recipes'] = len(recipes)

    with open('data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Added: {added} recipes")
    print(f"Skipped (existing): {skipped}")
    print(f"Total recipes now: {len(recipes)}")

    print(f"\n=== Recipes by Region ===")
    print(f"Asian cheeses: 6 (Chhena, Kalari, Bandel, Rushan, Rubing, Sakura)")
    print(f"African cheeses: 5 (Ayib, Wagashi, Wara, Gibna Bayda, Boerekaas)")
    print(f"Oceania cheeses: 2 (Australian Cheddar, Kapiti-style)")


if __name__ == '__main__':
    add_recipes()
