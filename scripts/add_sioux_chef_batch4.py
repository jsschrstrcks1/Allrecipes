#!/usr/bin/env python3
"""Add fourth batch of Sioux Chef recipes to recipes.json"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "simple-corn-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Simple Corn Cakes with Assorted Toppings",
        "native_name": "Wagmíza Aǧúyabskuyela",
        "category": "breads",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 51",
        "description": "When we were designing the menu for the Tatanka Truck, we wanted something lighthearted, unpretentious, healthy, and fun. So, we re-created the Indian taco with authentic ingredients—the indigenous taco. The base is a griddled corn cake, like a griddled polenta cake, topped with local foods such as walleye, smoked turkey, cedar-braised bison, and roasted squash. This Simple Corn Cake is made of cornmeal, cooled, formed into a patty, cooked on a hot flat surface—flat rocks, a home griddle—just as many Native communities have been doing for centuries.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "salt", "quantity": "", "unit": "generous pinch"},
            {"item": "polenta or coarse cornmeal", "quantity": "1", "unit": "cup"},
            {"item": "sunflower or nut oil", "quantity": "1 to 2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "In a large pot set over high heat, bring the water and salt to a boil and whisk in the cornmeal in a slow, steady stream."},
            {"step": 2, "text": "Continue stirring to be sure there are no lumps. Reduce the heat and simmer, stirring occasionally, until the mixture is thick and the flavor is rich and corny, about 30 to 40 minutes."},
            {"step": 3, "text": "Set aside until cool enough to handle."},
            {"step": 4, "text": "Shape the cooked cornmeal into patties, about 4 inches round by an inch thick."},
            {"step": 5, "text": "Film a skillet with the oil and set over medium-high heat. Sear the patties until nicely browned on one side, about 5 to 10 minutes, then flip and sear the other side, making sure they are cooked through."},
            {"step": 6, "text": "Place on a baking sheet and keep in a warm oven until ready to serve."}
        ],
        "notes": [
            "The variations on these easy, simple cakes are endless. Stir in fresh corn, herbs, dried meat, berries, maple, seeds, nuts, and mushrooms.",
            "The base of cooked cornmeal may be stored in the refrigerator for at least a week, ready to shape into cakes for breakfast, lunch, appetizers, and snacks."
        ],
        "tips": [
            "Serve with Wild Greens Pesto, page 24",
            "Serve with Cedar-Braised Bison, page 120",
            "Serve with Smoked Whitefish or Trout, page 89",
            "Serve with Dried Rabbit, page 115"
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "corn", "cakes", "breads", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "hominy-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hominy Cakes",
        "native_name": "Pasláyapi Aǧúyabskuyela",
        "category": "breads",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 53",
        "description": "We sometimes make corn cakes with hominy instead of cornmeal. Because it's been nixtamalized, it has a slightly different flavor associated with corn tortillas. These cakes make great use of leftover hominy corn or cornmeal mush.",
        "servings_yield": "Serves 4–6",
        "ingredients": [
            {"item": "cooked hominy or cornmeal mush", "quantity": "2", "unit": "cups"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Use leftover cornmeal mush or Southern grits instead of the cornmeal."},
            {"step": 2, "text": "Shape into patties and fry as directed for Simple Corn Cakes."}
        ],
        "notes": [],
        "tips": [
            "They are delicious topped with shredded Smoked Duck or Pheasant (page 106) and Wojape (page 173)."
        ],
        "substitutions": [
            {"original": "hominy", "substitute": "leftover cornmeal mush or Southern grits", "note": ""}
        ],
        "tags": ["indigenous", "native american", "corn", "hominy", "cakes", "breads"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "kneel-down-bread-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Kneel Down Bread",
        "native_name": "Čhaŋkpémakȟagle Aǧúyapi",
        "category": "breads",
        "attribution": "Chef Brian Yazzie (Navajo Nation)",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 55-56",
        "description": "This recipe comes from Chef Brian Yazzie, a member of the Navajo Nation. Kneel Down Bread is a family tradition. Simple, nourishing, and beautiful, it's like a tamale but made with fresh field corn and traditionally cooked in an earth oven or over hot coals. The name comes from the posture of Navajo women who used to kneel on the ground to grind the corn into a thick batter. It is traditionally baked in a wood-fired pit oven where corn husks are laid over red embers and then covered with clay to hold the heat as it bakes through the night.",
        "servings_yield": "Makes 12 breads",
        "ingredients": [
            {"item": "ears fresh or flint corn", "quantity": "12", "unit": ""},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Husk the corn, reserving the husks for wrapping. Using a sharp knife, cut the kernels from the cob."},
            {"step": 2, "text": "Then, setting each cob in a large bowl, scrape down the cob with the dull side of a knife to release the corn milk into the bowl."},
            {"step": 3, "text": "Place the kernels and milk into a food processor fitted with a steel blade and grind into a mush. Add the oil, and if the dough is too stiff, add water, 1 tablespoon at a time, and process into a stiff dough."},
            {"step": 4, "text": "Divide the mixture into twelve portions. Lay the husks rounded side down, then spoon the corn dough into each of the husks. Using strips of husks, tie both ends to enclose the filling."},
            {"step": 5, "text": "Gently fold the filled husk in half and tie the two ends together. Then tie another strip around the middle."},
            {"step": 6, "text": "Place on a baking sheet and bake until the package is firm to the touch, about 1 hour. Serve hot."},
            {"step": 7, "text": "These will store in the refrigerator up to five days. Reheat before serving."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [
            "Fresh field corn can be sourced directly from organic farmers. If it's not available, use rehydrated dried field corn, available in many natural food co-ops or online."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "navajo", "corn", "bread", "tamale"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sioux-chef-tamales",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sioux Chef Tamales",
        "native_name": "Wagmíza Čhoǧíŋ Opémníšpaŋ",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 57",
        "description": "Often associated with Mexico, tamales are found in every corn-growing region throughout the Americas. We fill them with smoked game and fish, as well as braised bison and assorted beans. They freeze well, so make a few extra to have on hand.",
        "servings_yield": "Makes about 12",
        "ingredients": [
            {"item": "dried corn husks", "quantity": "12 to 16", "unit": ""},
            {"item": "masa or corn flour", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "1/2 to 1", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "shredded Cedar-Braised Bison, page 120, or Smoked Duck, page 106", "quantity": "2", "unit": "cups"},
            {"item": "dried bergamot or oregano", "quantity": "", "unit": "generous pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "To soften the dried husks, place them in a bowl and cover with water. Place a plate on top to keep the husks submerged and let stand until soft, about 4 hours to one day."},
            {"step": 2, "text": "In a medium bowl, beat together the corn flour, water, and oil to make a tender but firm dough."},
            {"step": 3, "text": "Fill the bottom of a pot with a steamer insert and add about 2 inches of water to the pot. Line the bottom of the insert with a few of the softened corn husks."},
            {"step": 4, "text": "Open 2 large husks on a work surface and spread 1/4 cup of dough in the center of each, leaving a 2- to 3-inch border at the narrow end of the husk. Spoon the shredded meat down the center of the dough."},
            {"step": 5, "text": "Fold up the narrow end of the husk. Tie the folded portion with a strip of husk, but leave the wide end of the tamale open. Stand the tamales in a steamer basket, open side up. Repeat, filling the husks."},
            {"step": 6, "text": "Set the pot over high heat and bring the water to a boil. Reduce the heat to a simmer and steam the tamales until the dough is firm to the touch and separates easily from the husk, adding more water to the pot if necessary, about 45 minutes to an hour."},
            {"step": 7, "text": "Serve hot."}
        ],
        "notes": [],
        "tips": [
            "Find corn husks at natural food co-ops, Mexican mercados, and specialty grocery stores."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "tamales", "corn", "bison", "mains"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "old-fashioned-cornmeal-mush-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Old-Fashioned Cornmeal Mush with Poached Eggs",
        "native_name": "Wagmíza Yužápi na Witka Lolóbyapi",
        "category": "breakfast",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 59",
        "description": "This dish is especially soft and creamy, bright tasting, and corny. Top it with blueberries, fresh or dried, maple syrup, or even better, a poached duck egg. For this recipe, you'll want a heavy-bottomed saucepan and a sturdy whisk. Leftovers are fabulous made into cakes and fried.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "cornmeal or grits", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "4", "unit": "cups"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "duck eggs", "quantity": "4", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Put the cornmeal and water in a heavy-bottomed medium saucepan and set over medium heat."},
            {"step": 2, "text": "Bring to a simmer, whisking constantly, about 5 minutes."},
            {"step": 3, "text": "Reduce the heat to a simmer and cook, whisking occasionally as the mush thickens, about 40 to 45 more minutes. The mush should be thick enough to drop heavily from a spoon, but still fluid and not sludgy."},
            {"step": 4, "text": "Whisk in the salt. Remove from the heat."},
            {"step": 5, "text": "Serve in individual bowls topped with a poached egg or drizzle with maple syrup or honey."}
        ],
        "notes": [
            "Duck eggs are ideal for this recipe, as their assertive flavor works beautifully with the creamy golden mush. But if they are not available, substitute free-range jumbo chicken eggs."
        ],
        "tips": [
            "To poach duck eggs, bring a small pan of water to a gentle simmer. Stir the simmering water vigorously to create a vortex, then carefully crack two of the duck eggs into the water. Poach for 2 to 3 minutes, or until the eggs are cooked to your liking, then carefully remove from the pan using a slotted spoon and set on the individual bowls of porridge. Repeat the process with the two remaining eggs. Serve immediately."
        ],
        "substitutions": [
            {"original": "duck eggs", "substitute": "free-range jumbo chicken eggs", "note": ""}
        ],
        "tags": ["indigenous", "native american", "breakfast", "cornmeal", "porridge", "eggs"],
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
