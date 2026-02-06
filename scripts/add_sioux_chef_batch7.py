#!/usr/bin/env python3
"""Add seventh batch of Sioux Chef recipes - game birds, duck, bison"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "maple-juniper-roast-pheasant-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple-Juniper Roast Pheasant",
        "native_name": "Čhaŋháŋpi Tiktíča na Haŋté úŋ Šiyóša Čheúŋpapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 97",
        "description": "When I was growing up on the Pine Ridge Reservation, we stocked our freezers with pheasant and grouse. We'd see them darting across the dirt roads into the dry brush. They were as common as the red-winged blackbirds perched on the fence posts. Overnight dry brining seasons and helps this especially lean bird to become tender and succulent. The technique also works with grouse and guinea hens.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "small pheasants", "quantity": "2", "unit": ""},
            {"item": "coarse salt", "quantity": "1", "unit": "tbsp"},
            {"item": "maple sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "sumac", "quantity": "1", "unit": "tsp"},
            {"item": "crushed juniper", "quantity": "1", "unit": "tsp"},
            {"item": "Rendered Duck Fat, page 105, or sunflower oil", "quantity": "1/4", "unit": "cup"},
            {"item": "fresh cranberries", "quantity": "1", "unit": "cup"},
            {"item": "Corn or Turkey Stock, page 170, or vegetable stock", "quantity": "1/2", "unit": "cup"},
            {"item": "maple vinegar", "quantity": "3", "unit": "tbsp"},
            {"item": "griddled apple halves for garnish (optional)", "quantity": "2", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "The day before, rinse the pheasants and pat dry with paper towels. To dry-brine, generously season with the salt, maple sugar, sumac, and juniper. Place on a roasting pan or deep plate in the refrigerator, uncovered, overnight."},
            {"step": 2, "text": "Preheat the oven to 500°F. Place the pheasants breast side up in a medium roasting pan. Rub a generous amount of the duck fat under the skin of the birds and over the outside of the skin. Put half the cranberries into the cavity of the pheasants and spread the rest in the pan."},
            {"step": 3, "text": "Pour the stock and vinegar into the roasting pan. Roast for 15 minutes. Reduce the heat to 350°F and baste the pheasants with the pan juices."},
            {"step": 4, "text": "Continue roasting until the skin is crisp, the juices run clear, and a meat thermometer inserted in the thigh reaches 155°F, about 30 to 45 more minutes."},
            {"step": 5, "text": "Allow to stand at least 10 minutes before carving."},
            {"step": 6, "text": "Carve and drizzle with the pan juices before serving with the griddled apples."}
        ],
        "temperature": "500°F (260°C) then 350°F (175°C)",
        "notes": [],
        "tips": [
            "Substitute 2 tablespoons cider vinegar and 1 tablespoon maple syrup for the maple vinegar.",
            "For the griddled apples, slice the apples in half horizontally, brush with a little sunflower or walnut oil, and griddle cut side down in a hot skillet or frying pan until lightly browned, about 3 to 5 minutes."
        ],
        "substitutions": [
            {"original": "maple vinegar", "substitute": "2 tbsp cider vinegar + 1 tbsp maple syrup", "note": ""}
        ],
        "tags": ["indigenous", "native american", "pheasant", "game bird", "roasted", "maple", "juniper"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sweet-sour-roast-goose-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sweet and Sour Roast Goose with Autumn Squash and Cranberries",
        "native_name": "Čhaŋháŋpi Tiktíča úŋ Maǧá Čheúŋpapi nakúŋ Wagmú na Wathókeča T'áǧa",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 98",
        "description": "This slow-roasted goose will emerge from the oven golden brown and tender. The sauce was inspired by an older recipe using 'sour sap,' a vinegar made from the maple syrup's last run blended with the maple syrup. Save the fat that collects at the bottom of the roasting pan for cooking vegetables, frying corn cakes, or sautéing other meats. This recipe works equally well with duck if you adjust the cooking time accordingly.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "whole goose, about 10 pounds", "quantity": "1", "unit": ""},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "large butternut squash, about 4 pounds, peeled, seeded, and cut into 2-inch chunks", "quantity": "1", "unit": ""},
            {"item": "cranberries", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "1/4", "unit": "cup"},
            {"item": "maple vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "coarse mustard", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse and dry the goose with paper towels. Rub it inside and out with the salt and refrigerate, uncovered, for at least 6 hours or overnight. Then pat it dry with paper towels, set it on a rack, and allow it to come to room temperature, about an hour."},
            {"step": 2, "text": "Trim any excess fat from the goose and reserve for another use. Using the tip of a sharp knife, lightly score the breast and leg skin in a crosshatch pattern. This helps to render the fat more quickly during roasting."},
            {"step": 3, "text": "Preheat the oven to 325°F. Season the goose with a little more salt and the ground juniper. Place the goose on a rack in a deep roasting pan and roast for about an hour."},
            {"step": 4, "text": "Every 30 minutes or so, baste the bird with the pan juices; then pour off the fat through a sieve into a large heatproof bowl (and reserve it for later use). Reduce the heat to 275°F, add the cubed squash and cranberries to the roasting pan, and return the goose to the oven."},
            {"step": 5, "text": "Continue roasting until a thermometer registers 165°F at the center of the breast, about 1 1/2 to 2 hours. Total roasting time is about 3 hours."},
            {"step": 6, "text": "In a small dish, whisk together the maple syrup, vinegar, and mustard to make a glaze. Brush the goose with the glaze several minutes before removing it from the oven."},
            {"step": 7, "text": "When it is done, place the goose on a carving board and allow to rest for 20 to 30 minutes before carving. Serve the goose with the squash and cranberries drizzled with the pan juices."}
        ],
        "temperature": "325°F (165°C) then 275°F (135°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "goose", "game bird", "roasted", "squash", "cranberry"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sage-rosehip-roasted-duck-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sage and Rose-Hip Roasted Duck",
        "native_name": "Phežíȟota na Uŋžíŋžiŋtka úŋ Maǧáksica Čheúŋpapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 99",
        "description": "The ducks we bagged when I was growing up were wild ducks; some were puddle ducks, others were diving ducks that varied in size. Their flavor depends on where the duck had been feeding. Shallow-water ducks that feed on local grains tend to be succulent, while diving ducks that eat fish can taste, well, fishy. We've found that an overnight soak in brine benefits any duck, wild or domestic. This simple recipe yields a duck with supercrisp skin and juicy meat. The sage and rose-hip sauce is tangy, woodsy, and mildly sweet. Serve over wild rice.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "5- to 6-pound duck", "quantity": "1", "unit": ""},
            {"item": "coarse salt", "quantity": "1", "unit": "tbsp"},
            {"item": "crushed juniper", "quantity": "1", "unit": "tbsp"},
            {"item": "large sprig sage", "quantity": "1", "unit": ""},
            {"item": "dried rose hips", "quantity": "1/2", "unit": "cup"},
            {"item": "water to cover", "quantity": "", "unit": ""},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "honey", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 425°F. Cut off the wing tips of the duck with poultry shears or a sharp knife. Remove any excess fat from the neck and body cavity. Rinse inside and out and pat dry with a paper towel or a clean dishcloth."},
            {"step": 2, "text": "Prick the outer layer of fat with a sharp fork or knife. Sprinkle the salt and juniper over the duck, outside and inside the cavity. Put the sprig of sage inside the cavity of the duck."},
            {"step": 3, "text": "Place the duck in a roasting pan and roast, breast side up, for 45 minutes, then remove from the oven and flip it over so that the back is up."},
            {"step": 4, "text": "Return to the oven and continue roasting another 45 minutes. Remove and turn it over so the breast side is up once more."},
            {"step": 5, "text": "Continue roasting until the duck is fully cooked and an instant-read thermometer inserted into the thigh registers 165°F, another 35 to 50 minutes. Allow the duck to rest before carving."},
            {"step": 6, "text": "To make the sauce: Put the rose hips into a small saucepan and add just enough water to cover. Set over medium heat, bring to a simmer, and cook until the rose hips are plump and soft."},
            {"step": 7, "text": "Strain off and discard the rose hips, retaining the cooking liquid, and return to the stove. Add the chopped sage and season with the honey, to taste."},
            {"step": 8, "text": "Drizzle the sage and rose-hip sauce over the cooked duck and serve."}
        ],
        "temperature": "425°F (220°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "roasted", "sage", "rose hip"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "seared-duck-breast-cider-glaze-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Seared Duck Breast with Cider Glaze",
        "native_name": "Maǧáksica Tȟaspáŋhaŋpi Akáštaŋpi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 100-101",
        "description": "In this recipe, the duck breast is barely cooked, seared under a maple glaze, and served over a griddled corn cake with wild mushrooms and a wild pesto. It's a simple plate that makes a stunning entrée. Unless you hunt or know someone who does, find duck breasts in the freezer section of most grocery stores. The sear on high heats gets the skin nice and crispy. Serve on Corn Cakes, page 51, or Wild Rice Pilaf, page 84.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "coarse mineral salt", "quantity": "1", "unit": "tsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "duck breasts, skin on", "quantity": "2 to 3", "unit": "lb"},
            {"item": "sunflower or hazelnut oil", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "cider", "quantity": "1", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "maple vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "maple syrup, or to taste", "quantity": "1", "unit": "tbsp"},
            {"item": "Wojape for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In a large, self-sealing plastic bag, shake the salt, sumac, and juniper together, then add the duck breasts and shake to coat with the mix. Seal and refrigerate at least 1 hour or overnight."},
            {"step": 2, "text": "Preheat the oven to 400°F. In a large ovenproof sauté pan, add enough oil to generously cover the pan and set over medium-high heat until shimmering."},
            {"step": 3, "text": "Working in batches so not to crowd the pan, sear the duck breasts, skin side down, for about 5 minutes. Turn and sear the other side for 5 minutes."},
            {"step": 4, "text": "Place the pan in the oven and roast for about 5 to 7 minutes for medium rare. Transfer the breasts to a plate and tent to keep warm."},
            {"step": 5, "text": "Pour all but about 1 teaspoon of fat from the pan and reserve for another use. Return the pan to medium heat, add the cider, and scrape up the browned bits from the bottom of the pan."},
            {"step": 6, "text": "Stir in the sage. Simmer the cider to reduce by half. Add the vinegar and cook to reduce for several more minutes. Season with the maple syrup."},
            {"step": 7, "text": "Cut the duck breasts into 1-inch-thick diagonal slices and serve drizzled with the Wojape sauce."}
        ],
        "temperature": "400°F (200°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "seared", "cider", "glaze"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "rendered-duck-goose-fat-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rendered Duck or Goose Fat",
        "native_name": "",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 101/105",
        "description": "Rendering the fat from duck or goose is easy and the rendered fat is the best cooking medium for just about any fried food. It's incredibly tasty with a silky mouth-feel and yields a bonus—little fritters or cracklings. Be warned, though, the freshly crisped morsels are addictive! They're terrific sprinkled on salads, over corn cakes, and on top of wild rice.",
        "servings_yield": "Variable",
        "ingredients": [
            {"item": "duck or goose skin and fat", "quantity": "", "unit": "from 1 bird"},
            {"item": "water", "quantity": "3/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "To render fat from a duck or goose: Carefully remove all the skin and fat from the duck, cutting close to but not touching the meat."},
            {"step": 2, "text": "Cut the skin and fat into inch-size chunks and place in a heavy-bottomed stockpot or Dutch oven. Add 3/4 cup water."},
            {"step": 3, "text": "Set over medium-low heat and bring to a simmer, turning the bits of skin occasionally, until the water has evaporated and the skin has fully crisped and released the fat, about 1 hour."},
            {"step": 4, "text": "Remove the cracklings with a slotted spoon and drain on paper towels."},
            {"step": 5, "text": "Store in an airtight container at room temperature for up to 3 days or freeze."},
            {"step": 6, "text": "Allow the fat to cool slightly, then strain through a fine-mesh sieve lined with cheesecloth into clean containers with lids."},
            {"step": 7, "text": "The fat may be stored, covered, up to 6 months in the refrigerator or frozen."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck fat", "goose fat", "rendered", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "crispy-duck-legs-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Crispy Duck Legs",
        "native_name": "Maǧáksica Hú Gaǧáyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 102",
        "description": "This recipe is an easier, quicker, and less fussy method of making 'confit.' The legs are cured for 24 hours and then cooked for about 4 hours in their own rendered fat. Serve these on a bed of Real Wild Rice, page 81, Maple-Sage Roasted Vegetables, page 46, or Three Sisters Mash, page 43.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "coarse salt", "quantity": "1 to 2", "unit": "tsp"},
            {"item": "crushed juniper", "quantity": "1/2", "unit": "tsp"},
            {"item": "ground sage", "quantity": "1/2", "unit": "tsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "duck legs, depending on size, rinsed and patted dry but not trimmed", "quantity": "4 to 8", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In a small bowl, combine the salt, juniper, sage, and sumac and sprinkle the duck legs generously with the mix."},
            {"step": 2, "text": "Place the duck legs in a pan, cover tightly with plastic, and refrigerate for 24 hours."},
            {"step": 3, "text": "Preheat the oven to 325°F. Place the duck legs fat side down in a large oven-proof skillet, with the legs fitting snugly together, or use two skillets."},
            {"step": 4, "text": "Set the skillet over medium-high heat and cook until the fat begins to render, about 20 minutes."},
            {"step": 5, "text": "Turn the legs over, cover the pan with foil, and place in the oven."},
            {"step": 6, "text": "Roast for 2 hours, remove the foil, and continue roasting until the duck is golden, 1 more hour."},
            {"step": 7, "text": "Remove the duck and reserve the fat."},
            {"step": 8, "text": "Serve the duck legs warm over cooked wild rice, roasted vegetables, or Three Sisters Mash, page 43."}
        ],
        "temperature": "325°F (165°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "confit", "crispy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "duck-pate-dried-apple-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Duck Pâté with Dried Apple",
        "native_name": "Maǧáksica Yulopapi nakun Tȟapanhaŋpi Tȟaspanpi Pusyapi",
        "category": "appetizers",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 103",
        "description": "Delicious served by itself, and on Corn Cakes, page 51, or with Amaranth Crackers, page 60.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "Rendered Duck Fat, page 105", "quantity": "3", "unit": "tbsp"},
            {"item": "wild onion or shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "duck liver, cut into 1-inch pieces", "quantity": "1", "unit": ""},
            {"item": "chopped sage", "quantity": "1/2", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": "generous pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "cider", "quantity": "1/4", "unit": "cup"},
            {"item": "slices fresh or Dried Apple, page 177, for garnish", "quantity": "4 to 6", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Place the duck fat in a skillet and set over medium-high heat to melt, about 4 to 5 minutes."},
            {"step": 2, "text": "Add the onion or shallot and cook for 30 seconds, stirring occasionally."},
            {"step": 3, "text": "Add the liver, sage, salt, and juniper. Cook, stirring occasionally, until the liver is cooked through and no longer pink, about 5 minutes."},
            {"step": 4, "text": "Add the cider and continue cooking to reduce to a glaze, about 3 minutes."},
            {"step": 5, "text": "Transfer to a food processor fitted with a steel blade and process into a rough pâté."},
            {"step": 6, "text": "Place in a bowl and allow to cool. Store, covered in the refrigerator, until ready to use."},
            {"step": 7, "text": "Serve garnished with the apple slices."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "pate", "appetizer", "liver"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "duck-wild-rice-pemmican-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Duck and Wild Rice Pemmican",
        "native_name": "Maǧáksica na Psíŋ Wasná",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 104-105",
        "description": "Pemmican, like the wasna I grew up with, is an ancient staple of dried meat, tallow, berries, and other seasonings. Our take on this dish using flavor-intense duck speaks of culture and history in a bite. This duck appetizer is rich, satisfying, and surprisingly easy. Although it takes a little time and patience for the duck to dry in either a dehydrator or in a very low temperature oven, the recipe comes together in a snap. Serve as finger food, on a bed of greens, or even with dried vegetable chips for a starter or light meal.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "duck breasts, skin on", "quantity": "2", "unit": ""},
            {"item": "maple sugar", "quantity": "4", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"},
            {"item": "uncooked wild rice, page 79", "quantity": "1/3", "unit": "cup"},
            {"item": "dried blueberries", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Carefully remove all the skin and fat from the duck breasts, cutting close to, but not touching, the meat. Once the fat and skin are removed, cut into 1-inch chunks."},
            {"step": 2, "text": "Place the skin, with its fat, into a heavy-bottomed skillet or Dutch oven. Set the pan over low heat and slowly cook, stirring occasionally, until the skin has crisped and its fat has changed to liquid, about 45 minutes."},
            {"step": 3, "text": "With a slotted spoon, remove the crisped skin (cracklings) and drain them in a bowl lined with paper towels. Allow the liquid fat to cool to room temperature, then strain through a fine-mesh sieve lined with cheesecloth into a bowl or a clean glass jar."},
            {"step": 4, "text": "In a small bowl, mix together the sugar and salt."},
            {"step": 5, "text": "Slice the duck breast into thin, long strips along the grain. Rub both sides of the duck strips with the sugar and salt. If you have a food dehydrator, follow the instructions for making jerky."},
            {"step": 6, "text": "To dry the duck in the oven: Preheat the oven to the lowest setting. Lay the strips on a wire rack over a rimmed baking sheet and put into the oven. Leave the meat until it is dried out but still pliable, about 6 to 8 hours."},
            {"step": 7, "text": "In a medium skillet, heat 1 tablespoon of the rendered duck fat, or more as needed, over low and add the wild rice. Shake the pan until the rice begins to 'pop' and 'puff.' Spread the rice out on a paper towel. Reserve 1 tablespoon of the puffed rice for garnish."},
            {"step": 8, "text": "Put the cracklings, dried duck, puffed wild rice (except for the reserved amount), dried blueberries, and any leftover duck oil into a food processor fitted with a steel blade. Pulse to chop fine."},
            {"step": 9, "text": "Put the mixture in a bowl and, using 2 tablespoons or 1/8 cup, form the mixture into small bites."},
            {"step": 10, "text": "Serve garnished with the puffed wild rice."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "pemmican", "wild rice", "jerky"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "smoked-duck-pheasant-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Duck or Pheasant",
        "native_name": "Maǧáksica naiŋš Šiyóša Asótkaziyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 106",
        "description": "Pheasant and duck are wonderful smoked. Brining helps make them more juicy and tender, and the smoking process adds the flavor of an open flame. Brining does two things: it seasons meat and, through osmosis, helps infuse moisture to keep it juicy. We leave the skin on the birds to help keep them from drying out. (Many markets now sell pheasant, often frozen.) Shred the smoked pheasant or duck and serve over Corn Cakes, page 51, or Timpsula Cakes, page 86, with a drizzle of Wojape. Plan on a 12-hour brine followed by a 5-hour smoke.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "3-pound pheasants or 1 5- to 6-pound duck", "quantity": "2", "unit": ""},
            {"item": "salt", "quantity": "1/4", "unit": "cup"},
            {"item": "maple sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup, boiled down to 1 cup", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse and thoroughly clean the pheasants or duck. In a large container, stir together the salt, sugar, and water until dissolved."},
            {"step": 2, "text": "Immerse the birds in the container and brine in the refrigerator for at least 12 and up to 18 hours."},
            {"step": 3, "text": "Remove and pat dry; allow them to sit for 1 to 3 hours, until the skin is dry to the touch."},
            {"step": 4, "text": "Smoke the birds over hard wood (hickory) for at least 3 hours at 200° to 250°F."},
            {"step": 5, "text": "After 1 hour, baste with the maple syrup every 30 minutes. The cooking time will vary greatly depending on the size and type of bird."},
            {"step": 6, "text": "Use an instant-read thermometer to check for doneness. It should read 160°F when the birds are ready."},
            {"step": 7, "text": "Remove to a cooling rack, baste one more time, and cool."}
        ],
        "temperature": "200-250°F (95-120°C)",
        "notes": [],
        "tips": [
            "The smoked duck or pheasant makes a fine stuffing for Tamales, page 57, and in any soups."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "duck", "pheasant", "smoked", "game bird"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["smoked-turkey-acorn-soup-sioux-chef"]
    },
    {
        "id": "roast-turkey-wild-onions-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Roast Turkey, Wild Onions, Maple Squash, and Cranberry Sauce",
        "native_name": "Waglékšuŋ, Psíŋ, Wagmú, nakúŋ Wathókeča T'áǧa Yužápi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 107",
        "description": "Hands down, this is the best way to roast turkey. We serve it and the vegetables over wild rice. Save the turkey bones for stock, page 170.",
        "servings_yield": "Serves 8",
        "ingredients": [
            {"item": "small (10- to 12-pound) turkey, rinsed well and patted dry", "quantity": "1", "unit": ""},
            {"item": "hazelnut oil", "quantity": "1/2", "unit": "cup"},
            {"item": "chopped sage", "quantity": "2", "unit": "tbsp"},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "crushed juniper", "quantity": "", "unit": ""},
            {"item": "Corn, Wild Rice, or Turkey Stock, page 170", "quantity": "2", "unit": "cups"},
            {"item": "wild onions or 2 large onions, quartered", "quantity": "4", "unit": ""},
            {"item": "wild mushrooms, chopped", "quantity": "1", "unit": "cup"},
            {"item": "cubed winter squash", "quantity": "2", "unit": "cups"},
            {"item": "maple syrup", "quantity": "1/2", "unit": "cup"},
            {"item": "Cranberry Sauce, page 108", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "One hour before roasting, remove the turkey from the refrigerator and bring to room temperature."},
            {"step": 2, "text": "In a blender, puree the hazelnut oil and sage and rub over the turkey. Season with salt and juniper."},
            {"step": 3, "text": "Preheat the oven to 450°F. Place the turkey into a roasting pan, add the stock, and put into the oven."},
            {"step": 4, "text": "Roast until the turkey is light golden brown, about 45 minutes."},
            {"step": 5, "text": "Reduce the oven temperature to 350°F and continue roasting."},
            {"step": 6, "text": "After about 1 1/2 hours, scatter the onions, mushrooms, and squash into the roasting pan and baste the turkey and the vegetables occasionally with the pan juices."},
            {"step": 7, "text": "Continue cooking until an instant-read thermometer inserted into the thigh registers 160°F, about 30 minutes to 1 hour longer."},
            {"step": 8, "text": "Brush the turkey with the maple syrup."},
            {"step": 9, "text": "Remove the turkey from the oven and transfer to a cutting board. Arrange the vegetables on a platter."},
            {"step": 10, "text": "Carve the turkey and arrange over the vegetables. Drizzle the pan juices over all. Serve with wild rice and Cranberry Sauce."}
        ],
        "temperature": "450°F (230°C) then 350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "turkey", "roasted", "thanksgiving", "holiday"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "bison-ribs-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bison Ribs",
        "native_name": "Tȟathúčhuhu",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 118",
        "description": "Finger-licking, rib-sucking, and tasty, these ribs are lean, crispy, and tender.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "ground juniper", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "1", "unit": "tbsp"},
            {"item": "ground sage", "quantity": "1", "unit": "tsp"},
            {"item": "bison ribs", "quantity": "4 to 6", "unit": "lb"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "Wojape, page 173", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the broiler or grill to high. In a small bowl, combine the juniper, salt, and sage and rub over the ribs to season."},
            {"step": 2, "text": "Grill both sides of the ribs under the broiler or on the grill until a firm crust forms, about 2 to 3 minutes per side."},
            {"step": 3, "text": "Reduce oven temperature to 250°F."},
            {"step": 4, "text": "Place the ribs bone side down on a rack and set in a roasting pan; alternatively, set the rack on a deep baking sheet."},
            {"step": 5, "text": "Add a cup of water to the pan. Cover or wrap tightly with foil and roast for 2 hours."},
            {"step": 6, "text": "Turn the ribs over, cover, and continue roasting until the meat is very tender, about 45 minutes to 1 hour."},
            {"step": 7, "text": "Remove the ribs and scoop out the Wojape. Brush the ribs with Wojape to glaze the meat, about 3 to 5 minutes."},
            {"step": 8, "text": "Remove and cut into pieces for serving."}
        ],
        "temperature": "High broil, then 250°F (120°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "bison", "ribs", "grilled", "wojape"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    }
]

def main():
    with open('data/recipes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_ids = {r['id'] for r in data['recipes']}
    for recipe in new_recipes:
        if recipe['id'] in existing_ids:
            print(f"ERROR: Recipe ID '{recipe['id']}' already exists!")
            return False

    data['recipes'].extend(new_recipes)
    data['meta']['total_count'] = len(data['recipes'])
    data['meta']['total_recipes'] = len(data['recipes'])
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    with open('data/recipes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
