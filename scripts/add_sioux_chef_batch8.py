#!/usr/bin/env python3
"""Add batch 8 of Sioux Chef recipes - meats, game, rabbit, bison"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "cranberry-sauce-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cranberry Sauce",
        "native_name": "Wathókeča T'áǧa Yužápi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 108",
        "description": "Use this to drizzle over roasted squash or turkey, on Wild Rice Cakes, page 63, or for a dessert sauce.",
        "servings_yield": "Makes 1½ cups",
        "ingredients": [
            {"item": "cranberries, fresh or frozen", "quantity": "1½", "unit": "cups"},
            {"item": "cider", "quantity": "¼", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "crushed juniper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put all the ingredients into a saucepan and set over medium heat. Bring to a simmer, stirring occasionally, and cook until the cranberries have popped and the mixture is thick."},
            {"step": 2, "text": "Remove from the heat and put into a fine-mesh sieve set over a bowl. Press the mixture firmly with the back of a spoon and scrape the underside of the sieve to capture all of the fruit pulp."},
            {"step": 3, "text": "Taste and adjust the seasoning. Serve warm or cool."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "cranberry", "sauce", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["maple-squash-sorbet-cranberry-sioux-chef", "roast-turkey-wild-onions-sioux-chef"]
    },
    {
        "id": "cider-braised-turkey-thighs-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cider-Braised Turkey Thighs",
        "native_name": "Tȟaspáŋhaŋpi na Phežíȟota úŋ Waglékšuŋ Lolóbyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 109",
        "description": "With dark, rich meat and a coarse texture, turkey thighs are reminiscent of game birds. This recipe makes a nice weeknight dinner served with smashed sweet potatoes or maple squash, corn cakes, or wild rice.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "turkey thighs, skin removed", "quantity": "2 to 3", "unit": "pounds"},
            {"item": "chopped wild onion", "quantity": "1", "unit": "cup"},
            {"item": "Corn, Wild Rice, or Game Stock, page 170", "quantity": "1", "unit": "cup"},
            {"item": "cider", "quantity": "½", "unit": "cup"},
            {"item": "maple or apple cider vinegar", "quantity": "¼", "unit": "cup"},
            {"item": "whole juniper berries", "quantity": "2", "unit": ""},
            {"item": "sage leaves", "quantity": "4", "unit": ""},
            {"item": "large apple, cored, seeded, and diced", "quantity": "1", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat the oil over medium-high heat in a Dutch oven or heavy pot. Brown the thighs on all sides, about 3 minutes per side. Remove the thighs and set aside."},
            {"step": 2, "text": "Reduce the heat and add the onion and cook until softened, about 3 to 5 minutes."},
            {"step": 3, "text": "Add the stock and cider, increase the heat, and bring to a boil, scraping any browned bits from the bottom of the pan. Stir in the remaining ingredients and return the thighs to the pot. Reduce the heat to a simmer."},
            {"step": 4, "text": "Cover the pot and cook the turkey, turning occasionally, adding more stock if the liquid becomes low, until the turkey is very tender, about 45 minutes."},
            {"step": 5, "text": "Remove the turkey from the pot and set aside, covered to keep it warm. Skim the fat from the surface of the liquid in the pot, raise the heat to bring to a boil, and reduce the liquid by half. Taste and adjust the seasoning."},
            {"step": 6, "text": "Serve the thighs with the sauce drizzled on top."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "turkey", "braised", "cider", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "maple-brined-smoked-turkey-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Maple-Brined Smoked Turkey",
        "native_name": "Waglékšuŋ Ašótkaziyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 110",
        "description": "The traditional American Thanksgiving meal showcases the bounty of indigenous foods and the influence Native Americans have had on U.S. cuisine. This recipe ensures a terrific, tender, juicy turkey for dinner, and leftover turkey meat is delicious on Corn Cakes, page 51, and added to the Smoked Turkey and Acorn Soup, page 71.",
        "servings_yield": "Serves 10 to 12",
        "ingredients": [
            {"item": "turkey with giblets removed", "quantity": "10", "unit": "pound"},
            {"item": "water", "quantity": "4", "unit": "quarts"},
            {"item": "coarse salt", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"},
            {"item": "whole juniper berries", "quantity": "2", "unit": "tbsp"},
            {"item": "large sprig sage", "quantity": "1", "unit": ""},
            {"item": "wood chips (hickory, apple, or hazelnut)", "quantity": "4 to 6", "unit": "cups"},
            {"item": "sunflower oil for rubbing the turkey", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Place the turkey in a large container (a food-safe bucket or big pot). In a saucepan, heat about 1 quart of the water with the salt until it dissolves. Cool. Then add the salt water, the remaining water, maple syrup, juniper berries, and sage to the turkey. Make sure the turkey is fully submerged."},
            {"step": 2, "text": "Cover (weigh the turkey down, if necessary) and refrigerate for 12 to 24 hours. Soak the wood chips in cold water for at least 4 hours or overnight. Remove the turkey and pat dry."},
            {"step": 3, "text": "Prepare a charcoal grill or smoker for indirect heat, at about 275°F. Sprinkle in enough of the soaked wood chips to cover the coals and allow them to char."},
            {"step": 4, "text": "Place the turkey in a roasting pan fitted with a rack. Brush the turkey with the sunflower oil. Place the turkey in the grill or smoker and cook until the internal temperature of the thigh registers 165°F, about 3½ to 4½ hours. Remove and allow to rest for at least 20 minutes before carving."}
        ],
        "temperature": "275°F (135°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "turkey", "smoked", "maple", "thanksgiving", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "old-fashioned-rabbit-stew-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Rabbit Stew",
        "native_name": "Eháŋni Iyéčhel Maštíŋča Waháŋpi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 113",
        "description": "Serve this over golden Corn Mush, page 59, for a comforting winter meal. The long, slow cooking time is especially good for a wild rabbit. If rabbit is not available, substitute turkey thighs.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "corn flour", "quantity": "3", "unit": "tbsp"},
            {"item": "dried oregano or bergamot", "quantity": "2", "unit": "tsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "large rabbit, about 3 pounds, cut into 8 pieces", "quantity": "1", "unit": ""},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "wild onions or 2 large onions, coarsely chopped", "quantity": "3", "unit": ""},
            {"item": "Corn, Rabbit, or Turkey Stock, page 170", "quantity": "3", "unit": "cups"},
            {"item": "soaked hominy", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the flour, oregano, and a generous pinch of sumac and smoked salt in a large freezer bag. Add the rabbit portions to the bag, a few at a time, and shake well until evenly coated in the seasoned flour. Transfer to a plate."},
            {"step": 2, "text": "Heat the oil in a large, heavy pot set over medium heat. Fry the rabbit a few pieces at a time, until golden brown all over. Put the pieces into a baking dish."},
            {"step": 3, "text": "Add the onions to the pot and sauté until lightly browned and beginning to soften, about 5 minutes. Pour 1 cup of the stock into the cooking pot and stir vigorously to deglaze any of the browned bits at the bottom of the pot. Simmer for a few seconds then add the remaining stock and the hominy."},
            {"step": 4, "text": "Return the rabbit to the pot, partially cover, and set over medium heat. Bring to a boil, reduce the heat, and simmer, turning the rabbit pieces occasionally, until the meat is very tender, about 2 to 2½ hours. Skim off and discard any fat that rises to the top as the rabbit cooks."},
            {"step": 5, "text": "Serve the rabbit stew over corn mush or wild rice."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "rabbit", "substitute": "turkey thighs", "note": "If rabbit is not available"}
        ],
        "tags": ["indigenous", "native american", "rabbit", "stew", "main dish", "comfort food"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "rabbit-braised-apples-mint-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Rabbit Braised with Apples and Mint",
        "native_name": "Tȟaspáŋ na Čheyáka nakúŋ Maštíŋča Lolóbyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 115",
        "description": "This simple skillet meal is delicious served over wild rice, corn cakes, or cooked hominy. If rabbit is not available, substitute turkey or chicken thighs.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "large rabbit, about 3 pounds, cut into pieces", "quantity": "1", "unit": ""},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "sunflower or vegetable oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onions, ramps, or large shallots", "quantity": "2", "unit": ""},
            {"item": "sage leaves, chopped", "quantity": "3", "unit": ""},
            {"item": "mint leaves, chopped", "quantity": "4", "unit": ""},
            {"item": "cider", "quantity": "½", "unit": "cup"},
            {"item": "Corn or Rabbit Stock, page 170", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "maple vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "large apple, cored and sliced", "quantity": "1", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Season the rabbit with the salt. Heat the oil in a large skillet over medium heat. Cook the rabbit until browned on all sides, about 6 minutes per side. Transfer the rabbit to a plate."},
            {"step": 2, "text": "Add the onions, sage, and mint and cook until tender, about 3 to 5 minutes. Add the cider and stock and scrape up any dark bits sticking to the bottom of the pan."},
            {"step": 3, "text": "Return the rabbit to the pan; add the maple syrup and vinegar. Cover the pan and braise until tender, about 45 minutes to 1 hour, turning the pieces occasionally."},
            {"step": 4, "text": "Uncover, add the apples, and continue cooking, basting the rabbit until the sauce is thickened. Adjust the seasoning."}
        ],
        "notes": [],
        "tips": [
            "Dried rabbit: Dry leftover braised or stewed rabbit in a food dehydrator until all of the moisture has been removed. Or place the rabbit on a large screen over a baking sheet, and dry in the oven on the lowest setting. Turn the rabbit occasionally, until the meat is very dry. Shred and then store in a covered container for a week."
        ],
        "substitutions": [
            {"original": "rabbit", "substitute": "turkey or chicken thighs", "note": "If rabbit is not available"}
        ],
        "tags": ["indigenous", "native american", "rabbit", "braised", "apples", "mint", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "bison-tartare-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bison Tartare",
        "native_name": "Pté Tȟaló Spáŋšniyaŋ",
        "category": "appetizers",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 117",
        "description": "Bison is the cleanest-tasting red meat, milder and a little sweeter than beef. Tartare showcases this clean taste. Here it's seasoned with juniper and mint and gets a tangy kick from sumac.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "boneless bison, trimmed of fat and silver skin, finely chopped", "quantity": "8", "unit": "oz"},
            {"item": "crushed juniper", "quantity": "1", "unit": "tbsp"},
            {"item": "chopped mint", "quantity": "1", "unit": "tbsp"},
            {"item": "maple sugar", "quantity": "2", "unit": "tsp"},
            {"item": "finely chopped wild onion or shallots", "quantity": "1", "unit": "tbsp"},
            {"item": "sumac", "quantity": "1", "unit": "tbsp"},
            {"item": "sunflower oil", "quantity": "1", "unit": "tsp"},
            {"item": "salt", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "In a medium bowl, combine the chopped bison, juniper, mint, maple sugar, onion, sumac, and oil."},
            {"step": 2, "text": "Season with the salt. Form into patties and serve topped with a duck egg yolk and cracker of your choice."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "bison", "tartare", "appetizer", "raw"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "cedar-braised-bison-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Cedar-Braised Bison",
        "native_name": "Haŋté úŋ Pté Lolóbyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 120-121",
        "description": "This makes a simple and hearty one-pot meal. The meat becomes fork tender and the stock simmers down to a rich sauce. Leftovers are terrific served over corn cakes.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "bison or beef chuck roast", "quantity": "2 to 3", "unit": "pounds"},
            {"item": "coarse salt", "quantity": "1", "unit": "tbsp"},
            {"item": "maple sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "Wild Rice or Corn Stock, page 170", "quantity": "2 to 4", "unit": "cups"},
            {"item": "sprigs sage", "quantity": "several", "unit": ""},
            {"item": "sprig cedar", "quantity": "1", "unit": ""},
            {"item": "dried hominy, soaked overnight and drained", "quantity": "2", "unit": "cups"},
            {"item": "sumac", "quantity": "1", "unit": "tbsp"},
            {"item": "maple syrup", "quantity": "½", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 250°F. Season the bison with the salt and maple sugar."},
            {"step": 2, "text": "Film a Dutch oven or large flame-proof baking dish with the oil and set over high heat. Sear the bison on all sides until dark and crusty, about 10 minutes. Remove the bison and set aside."},
            {"step": 3, "text": "Stir in the stock and sage, scraping up any of the crusty bits that form on the bottom of the baking dish. Add the hominy, sumac, and maple syrup and return the meat to the baking dish."},
            {"step": 4, "text": "Cover the Dutch oven or the baking dish tightly. (Use aluminum foil, if necessary.) Place the bison in the oven and cook until so tender it falls from the bone, about 3 hours."},
            {"step": 5, "text": "Remove from the oven. Tent the meat with foil to keep warm. Strain the remaining stock into a saucepan and reserve the hominy."},
            {"step": 6, "text": "Set the stock over high heat, bring to a boil, and reduce the liquid by half. Taste and adjust the seasoning. Carve the bison and serve over the hominy with the sauce drizzled over the meat."}
        ],
        "temperature": "250°F (120°C)",
        "notes": [
            "When braising meat, we always add a handful of the ingredients we intend to serve alongside—such as hominy, wild rice, and dried berries. You need to soak the dried hominy overnight before adding, so be sure to plan ahead."
        ],
        "tips": [
            "Braising meat in a flavorful stock over low heat for a long time is our preferred way of cooking large game because it's so lean and dries out easily. The cooking liquids along with the herbs and spices infuse the meat with flavor. Once it's fork tender, we brown the meat under the broiler or over a flame. We then simmer the cooking liquid to reduce it into a lush, thick sauce.",
            "We always add the ingredients for the side dish to the braising liquid. We may add wild rice, soaked hominy, or squash to the Cedar-Braised Bison. They add subtle flavors that bring together the final dish."
        ],
        "substitutions": [
            {"original": "bison", "substitute": "beef chuck roast", "note": ""}
        ],
        "tags": ["indigenous", "native american", "bison", "braised", "cedar", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "indigenous-tacos-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Indigenous Tacos",
        "native_name": "Ikčé Wičháša Aǧúyapi Oštéka",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 122",
        "description": "When we launched the Tatanka Truck, we took the idea of the fast food—Indian Tacos—and slowed it down with authentic ingredients. This is a delicious and superhealthy alternative to the fry bread and commodity hamburger version. Use leftover Cedar-Braised Bison, page 120, or Cedar-Braised Beans, page 36, or Griddled Maple Squash, page 33, in lieu of the ground bison in this recipe. The recipe is easily expanded to feed a crowd.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "ground bison", "quantity": "2 to 3", "unit": "pounds"},
            {"item": "salt", "quantity": "", "unit": "generous pinch"},
            {"item": "juniper", "quantity": "", "unit": "generous pinch"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onions or 2 medium onions, chopped", "quantity": "4", "unit": ""},
            {"item": "chopped sage leaves", "quantity": "1", "unit": "tbsp"},
            {"item": "Corn or Wild Rice Stock, page 170", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup to taste", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "Corn Cakes, page 51", "quantity": "", "unit": ""},
            {"item": "Wojape, page 173", "quantity": "", "unit": ""},
            {"item": "Corn Nuts, page 176", "quantity": "", "unit": ""},
            {"item": "chopped sorrel for garnish (optional)", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Season the bison with the salt and juniper."},
            {"step": 2, "text": "Heat the sunflower oil in a large Dutch oven over high heat and add the onions. Cook until softened and lightly browned, about 3 to 4 minutes."},
            {"step": 3, "text": "Add the bison and sage, and cook until browned, about 3 to 4 minutes, stirring occasionally to break up the meat."},
            {"step": 4, "text": "Add the stock, bring to a simmer, and cook until the liquid is reduced to a glaze, about 3 minutes. Season with the maple syrup."},
            {"step": 5, "text": "Serve over the corn cakes and drizzle with Wojape. Garnish with sorrel and top with corn nuts for a nice crunch."}
        ],
        "notes": [
            "Chef's Note: For vegetarian and vegan tacos, replace the bison with Cedar-Braised Beans, page 36."
        ],
        "tips": [],
        "substitutions": [
            {"original": "ground bison", "substitute": "Cedar-Braised Beans, page 36", "note": "For vegetarian/vegan version"},
            {"original": "ground bison", "substitute": "Cedar-Braised Bison, page 120", "note": "Use leftovers"},
            {"original": "ground bison", "substitute": "Griddled Maple Squash, page 33", "note": ""}
        ],
        "tags": ["indigenous", "native american", "bison", "tacos", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["corn-cakes-sioux-chef", "wojape-sioux-chef", "corn-nuts-sioux-chef"],
        "is_component": False
    },
    {
        "id": "bison-wasna-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Bison Wasna",
        "native_name": "Pté Wasná",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 125",
        "description": "Wasna, or dried meats, are as delicious and versatile as they are ancient, and they are exceptionally easy to make. We use wasna in salads, on top of wild rice and hominy cakes as an appetizer, and in soups and stews, for they have an extraordinary flavor. Wasna is sometimes called pemmican—the mix of dried meat and berries. It's rough, sweet, and immensely nutritious and satisfying—loaded with protein, low in sugar and carbs—the original good-for-you snack food.",
        "servings_yield": "Makes about 10 to 12 ounces",
        "ingredients": [
            {"item": "bison, flank, rump, or round", "quantity": "2", "unit": "pounds"},
            {"item": "crushed juniper", "quantity": "2", "unit": "tsp"},
            {"item": "dried cranberries", "quantity": "½", "unit": "cup"},
            {"item": "coarse salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Trim the meat of fat, place in a freezer bag, and put into the freezer for about an hour or until very firm (this makes it much easier to slice)."},
            {"step": 2, "text": "Remove the meat and slice thinly with the grain into long strips. Put the strips, along with the remaining ingredients, back into the freezer bag and refrigerate at least 3 hours or overnight."},
            {"step": 3, "text": "Preheat the oven to 150°F. Or prepare a dehydrator. Remove the meat from the bag and pat dry. Arrange the strips on a food dehydrator or a screen or drying rack placed over a baking sheet to catch any drips."},
            {"step": 4, "text": "If using a screen, place in the oven. Allow the meat to dry until it is leathery, at least 4 hours or overnight. Remove, cool, and cut into bite-sized pieces."},
            {"step": 5, "text": "Put the meat and the cranberries into a food processor fitted with a steel blade. Pulse and season with the salt. Remove and shape into small cakes."}
        ],
        "temperature": "150°F (65°C)",
        "notes": [
            "Serve the wasna cakes on a 'charcuterie' board with Smoked Pheasant, page 106, dried berries, toasted hazelnuts, seeds, greens, and a little crock of Wojape, page 173."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "bison", "wasna", "pemmican", "dried meat", "snack", "preserved"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "hunters-stew-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hunter's Stew",
        "native_name": "Wóle Wičháša Waháŋpi Tȟáwa",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 126",
        "description": "Bear remains a traditional Native food, especially in the Northern Heartland, where these animals are abundant. They're known to raid summer cabins and park dumpsters, and to snatch small pets. Hunting bear for food is one of the best ways to control the expanding population. Moose, elk, and antelope are also great choices for this recipe because the slow cooking helps to turn the meat tender and flavorful. If these are not available, substitute bison or lamb. Serve it over Corn Cakes, page 51, or Cornmeal Mush, page 59, or with Kneel Down Bread, page 55. Like most hearty stews, it will taste better the day after it's made.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "dried wild mushrooms, such as chanterelles, trumpet, or morels", "quantity": "1", "unit": "oz"},
            {"item": "boiling water", "quantity": "1", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "bear, lamb, or bison, cut into 2-inch cubes", "quantity": "2½ to 3", "unit": "pounds"},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "crushed juniper", "quantity": "", "unit": ""},
            {"item": "wild onions or 1 large leek, white part, trimmed", "quantity": "3", "unit": ""},
            {"item": "fresh mushrooms, coarsely chopped", "quantity": "8", "unit": "oz"},
            {"item": "minced fresh oregano", "quantity": "1", "unit": "tbsp"},
            {"item": "sumac to taste", "quantity": "2", "unit": "tsp"},
            {"item": "Corn or Bison Stock, page 170", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the dried mushrooms in a small bowl and pour the boiling water over them. Soak about 20 minutes until softened. Drain and reserve the soaking liquid. Chop the mushrooms and set aside."},
            {"step": 2, "text": "In a large, heavy pot, heat the sunflower oil over medium-high heat and brown the meat pieces in batches, seasoning with salt and juniper. Be careful not to crowd the pan. Cook each batch about 10 to 15 minutes. Remove the browned meat to a platter."},
            {"step": 3, "text": "Reduce the heat and add the onions, mushrooms, oregano, and sumac, and sauté until the onion is soft and the mushrooms release some of their liquid, about 3 to 5 minutes."},
            {"step": 4, "text": "Stir in the chopped, reconstituted wild mushrooms and the soaking liquid and the stock, stirring to dislodge any brown bits that stick to the pan."},
            {"step": 5, "text": "Return the meat to the pot, bring to a simmer, and cook, partially covered, until the meat is fork tender, about 2 hours. Taste and adjust the seasonings. Remove from the heat and let sit a few minutes before serving."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "bear", "substitute": "bison or lamb", "note": "If bear is not available"},
            {"original": "bear", "substitute": "moose, elk, or antelope", "note": "Also great choices"}
        ],
        "tags": ["indigenous", "native american", "stew", "game", "bear", "bison", "mushrooms", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "grilled-bison-skewers-wojape-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grilled Bison Skewers with Wojape",
        "native_name": "",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 128",
        "description": "Everyone loves these kebobs, the recipe of Mikee Willard and his son Darius Willard of the Northern Cheyenne tribe in Montana, and members of the Tatanka Truck team. They skewer chunks of fresh sweet corn (on the cob), turnips, summer squash, or partially roasted winter squash in between the bison. The skewers are then garnished with Wojape, page 173, or a sauce of stewed wild plums.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "bison sirloin, cut into 1- to 2-inch cubes", "quantity": "1 to 1½", "unit": "pounds"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "sumac", "quantity": "", "unit": "pinch"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "ears of sweet corn, shucked and cut into 2-inch chunks", "quantity": "2 to 3", "unit": ""},
            {"item": "young turnips, cut into 2-inch chunks", "quantity": "2 to 4", "unit": ""},
            {"item": "summer squash, cut into 2-inch chunks", "quantity": "3", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat coals or a gas grill for direct heat."},
            {"step": 2, "text": "Brush the bison with 1 tablespoon of the sunflower oil and sprinkle with the sumac and smoked salt. Brush the corn, turnips, and squash with the remaining oil."},
            {"step": 3, "text": "Thread the meat, sweet corn, turnips, and squash alternately on 4 to 6 skewers. Sprinkle the meat and vegetables with additional sumac and smoked salt."},
            {"step": 4, "text": "Grill the skewers about 4 to 6 inches from the heat, turning frequently, until the bison is no longer pink in the center, about 15 to 20 minutes."},
            {"step": 5, "text": "Serve drizzled with the Wojape, page 173."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "bison", "skewers", "grilled", "kebabs", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "components": ["wojape-sioux-chef"],
        "is_component": False
    },
    {
        "id": "lamb-sausage-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Lamb Sausage",
        "native_name": "Tȟáčhiŋčala Tȟašúpa",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 129",
        "description": "Brian Yazzie, Sioux Chef chef de cuisine, shared his method for creating a traditional Diné lamb sausage. Churro lamb, introduced to the continent by Spanish explorers in the 1600s, has become a mainstay throughout the Southwest. It's an especially hardy animal, requiring less water and forage than other sheep, with long legs, a narrow body, and fine bones. Navajo-Churro sheep provide lean meat with a distinctive, sweet flavor and beautiful dual-fiber fleece, prized for its array of natural colors and woven into Navajo tapestries and blankets. Because the traditional recipe for Churro lamb sausage is the kind of food best learned at the side of an elder, we've modified it, using more readily available ingredients. (The original recipe for this traditional blood sausage is similar to British black pudding, French boudin, and Estonian Christmas pudding—all truly delicious.)",
        "servings_yield": "Makes about 3 pounds",
        "ingredients": [
            {"item": "boneless lamb shoulder, or combination of cuts, cut into 1-inch cubes", "quantity": "3", "unit": "pounds"},
            {"item": "water", "quantity": "¼", "unit": "cup"},
            {"item": "maple vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "coarse salt", "quantity": "2", "unit": "tsp"},
            {"item": "chopped sage", "quantity": "2", "unit": "tsp"},
            {"item": "chopped oregano", "quantity": "2", "unit": "tsp"},
            {"item": "sumac", "quantity": "", "unit": "generous pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "generous pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the lamb on a rimmed baking sheet, transfer to the freezer, and chill until it's stiff but not frozen."},
            {"step": 2, "text": "Grind the meat through the small die of a meat grinder into a bowl. Work the water, vinegar, salt, sage, oregano, sumac, and juniper into the meat."},
            {"step": 3, "text": "To check the flavor of the sausage, cook a little of it in a lightly greased skillet set over medium-high heat until lightly browned; then taste and adjust the seasonings."},
            {"step": 4, "text": "Store the sausage covered in the refrigerator or freeze."}
        ],
        "notes": [
            "Brown this off to serve in our Indigenous Tacos, page 122, or in a Fried Wild Rice Bowl, page 83. Shape into patties for the grill."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "lamb", "sausage", "churro", "navajo", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "venison-chops-apples-cranberries-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Venison Chops with Apples and Cranberries",
        "native_name": "Tȟáȟča nakúŋ Tȟaspáŋ na Wathókeča T'áǧa",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 130",
        "description": "Here the venison chops are cooked quickly over high heat to be especially tender and juicy.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "tart apples", "quantity": "2", "unit": "", "prep_note": "*"},
            {"item": "cider", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "cranberries", "quantity": "4", "unit": "cups"},
            {"item": "3- to 4-ounce venison rib chops or rack of venison cut into 8 chops", "quantity": "8", "unit": "", "prep_note": "**"},
            {"item": "salt", "quantity": "", "unit": ""},
            {"item": "crushed juniper", "quantity": "", "unit": ""},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the apples, cider, maple syrup, and cranberries into a small, heavy saucepan. Set over high heat and bring to a boil. Reduce the heat and simmer until the liquid is reduced to ¼ cup, about 10 to 12 minutes. Remove and set aside."},
            {"step": 2, "text": "Preheat the oven to 500°F. Rinse and pat the chops dry and season with the salt and juniper."},
            {"step": 3, "text": "Heat the sunflower oil in a heavy skillet and set over moderate to high heat. Sauté the chops in batches, turning once, until well browned, about 2 minutes per side, 4 minutes total."},
            {"step": 4, "text": "Transfer the chops to a shallow baking pan and roast in the preheated oven until medium rare, about 3 minutes."},
            {"step": 5, "text": "Serve the chops with the cooked apples and cranberries."}
        ],
        "temperature": "500°F (260°C)",
        "notes": [
            "*We prefer using wild crabapples for their tartness, but if those are unavailable, substitute tart, domestic apples such as greening, Haralson, or Keepsake.",
            "**If venison isn't available, pork may be substituted."
        ],
        "tips": [],
        "substitutions": [
            {"original": "wild crabapples", "substitute": "tart domestic apples (greening, Haralson, or Keepsake)", "note": "If crabapples unavailable"},
            {"original": "venison", "substitute": "pork", "note": "If venison isn't available"}
        ],
        "tags": ["indigenous", "native american", "venison", "chops", "apples", "cranberries", "main dish"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "venison-elk-stew-hominy-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Venison or Elk Stew with Hominy",
        "native_name": "Tȟáȟča naiŋš Heȟáka na Pašláyapi Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 131",
        "description": "Venison shoulder is perfect for this recipe. The meat is lean and the muscles break down to become silky and tender during the slow braise. If you can't find shoulder, use shanks. They'll need to cook a little longer but are equally delicious. This is great served with hominy, over Old-fashioned Cornmeal Mush, page 59, or roasted squash.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "4-pound venison or elk shoulder", "quantity": "1", "unit": "", "prep_note": "*"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onions or small shallots, diced", "quantity": "2", "unit": ""},
            {"item": "wild mushrooms (chanterelle, oyster, porcini, or cremini), sliced", "quantity": "1", "unit": "pound"},
            {"item": "corn flour", "quantity": "¼", "unit": "cup"},
            {"item": "Corn Stock, page 170, or vegetable stock", "quantity": "3", "unit": "cups"},
            {"item": "cider, hard or not sweet", "quantity": "1", "unit": "cup"},
            {"item": "sprig sage", "quantity": "1", "unit": ""},
            {"item": "maple vinegar to taste", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "maple sugar", "quantity": "", "unit": "dash"}
        ],
        "instructions": [
            {"step": 1, "text": "Generously season all sides of the venison with the salt and juniper."},
            {"step": 2, "text": "Film a cast-iron pot with the oil and set over high heat. Add the venison and sear well on all sides until golden brown, about 4 minutes per side. Remove the venison and set aside."},
            {"step": 3, "text": "Reduce the heat and add the onions and mushrooms to the pot and cook, stirring until they brown, about 3 to 4 minutes. Stir in the flour until dissolved; then stir in the stock, cider, and sage and bring the mixture to a boil."},
            {"step": 4, "text": "Reduce the heat to a low simmer. Cover and cook until the meat pulls away easily from the bone, about 1½ to 2 hours. Taste and season with the vinegar and sugar."},
            {"step": 5, "text": "Transfer the venison to a cutting board and remove the bone. Slice the meat into chunks and return to the pot. Discard the sprig of sage."},
            {"step": 6, "text": "Serve in shallow bowls over wild rice, corn cakes, hominy, or roasted squash."}
        ],
        "notes": [
            "*If venison is not available, substitute lamb or goat in this recipe."
        ],
        "tips": [],
        "substitutions": [
            {"original": "venison", "substitute": "lamb or goat", "note": "If venison is not available"}
        ],
        "tags": ["indigenous", "native american", "venison", "elk", "stew", "hominy", "main dish"],
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

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes (batch 8 - meats/game)")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
