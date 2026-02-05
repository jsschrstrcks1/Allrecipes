#!/usr/bin/env python3
"""Add batch 11 of Sioux Chef recipes - Indigenous Partners guest chef recipes"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "scallops-three-sisters-four-medicines-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Scallops with Three Sisters Reduction and Four Medicines",
        "native_name": "",
        "category": "mains",
        "attribution": "Chef Rich Francis",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 185 (Indigenous Partners)",
        "description": "Chef Rich Francis of Atikamekw and French Canadian heritage trained at the Stratford Chefs School in Ontario and honed his skills at some of Canada's finest restaurants. He is committed to using indigenous wild ingredients and foraging. This elegant dish features seared scallops with a reduction of the three sisters (corn, beans, squash) and a garnish of the four sacred medicines.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "large sea scallops", "quantity": "8 to 12", "unit": ""},
            {"item": "coarse salt", "quantity": "", "unit": "pinch"},
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "cooked corn kernels", "quantity": "½", "unit": "cup"},
            {"item": "cooked beans", "quantity": "½", "unit": "cup"},
            {"item": "roasted squash puree", "quantity": "½", "unit": "cup"},
            {"item": "Corn or Vegetable Stock", "quantity": "½", "unit": "cup"},
            {"item": "fresh sage leaves for garnish", "quantity": "", "unit": ""},
            {"item": "fresh cedar tips for garnish", "quantity": "", "unit": ""},
            {"item": "sweetgrass for garnish (optional)", "quantity": "", "unit": ""},
            {"item": "tobacco flowers for garnish (optional)", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Pat the scallops dry and season with salt. Heat the oil in a large skillet over high heat. Sear the scallops until golden, about 2 minutes per side. Remove and set aside."},
            {"step": 2, "text": "In a blender, combine the corn, beans, squash puree, and stock. Blend until smooth. Strain through a fine-mesh sieve into a saucepan."},
            {"step": 3, "text": "Warm the reduction over medium heat. Taste and adjust the seasoning."},
            {"step": 4, "text": "Spoon the reduction onto plates. Arrange the scallops on top. Garnish with sage, cedar tips, and if available, sweetgrass and tobacco flowers."}
        ],
        "notes": [
            "The four medicines in many First Nations traditions are tobacco, cedar, sage, and sweetgrass—used in ceremony and healing."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "scallops", "three sisters", "guest chef", "elegant"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "navajo-tea-smoked-quail-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Navajo Tea-Smoked Quail with Manoomin Fritter, Pickled Cholla, and Lichii Sauce",
        "native_name": "",
        "category": "mains",
        "attribution": "Chef Karlos Baca",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 186-187 (Indigenous Partners)",
        "description": "Chef Karlos Baca is Tewa, Diné, and Nuche. He grew up on the Southern Ute reservation, learning traditional foodways from his grandmother. This dish reflects the Southwest with Navajo tea-smoked quail, wild rice fritters, pickled cholla cactus, and a sauce made from lichii (juniper berries).",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "semi-boneless quail", "quantity": "4", "unit": ""},
            {"item": "Navajo tea (greenthread/Thelesperma)", "quantity": "¼", "unit": "cup"},
            {"item": "cooked wild rice", "quantity": "1", "unit": "cup"},
            {"item": "corn flour", "quantity": "¼", "unit": "cup"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "oil for frying", "quantity": "", "unit": ""},
            {"item": "pickled cholla buds", "quantity": "¼", "unit": "cup"},
            {"item": "juniper berries", "quantity": "2", "unit": "tbsp"},
            {"item": "red chile powder", "quantity": "1", "unit": "tsp"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "½", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "For the lichii sauce: In a small saucepan, combine the juniper berries, chile powder, maple syrup, and water. Simmer until reduced by half. Strain and set aside."},
            {"step": 2, "text": "For the fritters: Mix the wild rice, corn flour, egg, and salt. Form into small patties. Fry in oil until golden on both sides. Drain and keep warm."},
            {"step": 3, "text": "For the quail: Prepare a smoker with the Navajo tea. Smoke the quail at 225°F until cooked through, about 45 minutes to 1 hour."},
            {"step": 4, "text": "To serve: Place a fritter on each plate. Top with the smoked quail. Drizzle with lichii sauce and garnish with pickled cholla buds."}
        ],
        "temperature": "225°F (107°C)",
        "notes": [
            "Navajo tea (greenthread) is a traditional Diné tea with a mild, pleasant flavor. It can be found at specialty markets or ordered online.",
            "Cholla buds are the flower buds of the cholla cactus, harvested in spring. They have a slightly tart, artichoke-like flavor."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "quail", "smoked", "navajo", "southwest", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "coriander-cured-elk-chokecherry-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Coriander-Cured Elk with Dried Chokecherry Sauce",
        "native_name": "",
        "category": "mains",
        "attribution": "Chef Lois Ellen Frank",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 188-189 (Indigenous Partners)",
        "description": "Chef Lois Ellen Frank is a culinary anthropologist, author, and photographer who has dedicated her career to Native American cuisine of the Southwest. This elegant dish features cured elk loin with a rich chokecherry sauce.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "elk loin", "quantity": "2", "unit": "pounds"},
            {"item": "coarse salt", "quantity": "¼", "unit": "cup"},
            {"item": "maple sugar", "quantity": "2", "unit": "tbsp"},
            {"item": "coriander seeds, crushed", "quantity": "2", "unit": "tbsp"},
            {"item": "juniper berries, crushed", "quantity": "1", "unit": "tbsp"},
            {"item": "dried chokecherries", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "sumac", "quantity": "1", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix the salt, maple sugar, coriander, and juniper. Rub the mixture all over the elk loin. Wrap tightly in plastic and refrigerate for 3 to 5 days, turning daily."},
            {"step": 2, "text": "For the sauce: Combine the chokecherries, water, and maple syrup in a small saucepan. Simmer until the berries are soft and the liquid is reduced by half, about 20 minutes. Strain, pressing on the solids. Stir in the sumac."},
            {"step": 3, "text": "Rinse the elk loin and pat dry. Allow to come to room temperature."},
            {"step": 4, "text": "Preheat the oven to 400°F. Sear the elk in a hot pan until browned on all sides. Transfer to the oven and roast until the internal temperature reaches 130°F for medium-rare, about 15 to 20 minutes."},
            {"step": 5, "text": "Let rest 10 minutes before slicing. Serve drizzled with the chokecherry sauce."}
        ],
        "temperature": "400°F (200°C)",
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "elk", "substitute": "venison or beef tenderloin", "note": ""}
        ],
        "tags": ["indigenous", "native american", "elk", "cured", "chokecherry", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "inca-trail-mix-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Inca Trail Mix",
        "native_name": "",
        "category": "snacks",
        "attribution": "Chef Andrea Murdoch",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 190 (Indigenous Partners)",
        "description": "Chef Andrea Murdoch, of Scottish and Incan heritage, explores the intersection of her ancestral cuisines. This trail mix combines indigenous ingredients from the Americas—quinoa, cacao, and native nuts.",
        "servings_yield": "Makes about 4 cups",
        "ingredients": [
            {"item": "puffed quinoa", "quantity": "1", "unit": "cup"},
            {"item": "roasted pumpkin seeds", "quantity": "1", "unit": "cup"},
            {"item": "cacao nibs", "quantity": "½", "unit": "cup"},
            {"item": "dried goldenberries or cranberries", "quantity": "½", "unit": "cup"},
            {"item": "toasted coconut flakes", "quantity": "½", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all ingredients in a large bowl and toss to mix well."},
            {"step": 2, "text": "Spread on a baking sheet and bake at 300°F for 10 to 15 minutes, stirring once, until lightly toasted."},
            {"step": 3, "text": "Allow to cool completely before storing in an airtight container."}
        ],
        "temperature": "300°F (150°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "trail mix", "snack", "quinoa", "cacao", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "chilchin-sumac-pudding-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "J.D. Kinlacheeny's Chilchin (Sumac) Pudding",
        "native_name": "Chilchin",
        "category": "desserts",
        "attribution": "Chef Brian Tatsukawa / J.D. Kinlacheeny",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 191 (Indigenous Partners)",
        "description": "This traditional Navajo pudding uses sumac berries to create a tangy, lemony dessert. The recipe comes from J.D. Kinlacheeny, shared by Chef Brian Tatsukawa.",
        "servings_yield": "Serves 6 to 8",
        "ingredients": [
            {"item": "sumac berries", "quantity": "2", "unit": "cups"},
            {"item": "cold water", "quantity": "4", "unit": "cups"},
            {"item": "blue cornmeal", "quantity": "½", "unit": "cup"},
            {"item": "honey or maple syrup", "quantity": "¼", "unit": "cup"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Place the sumac berries in a bowl and cover with the cold water. Let steep for 2 to 4 hours, crushing the berries occasionally."},
            {"step": 2, "text": "Strain the liquid through cheesecloth, squeezing to extract as much juice as possible. Discard the berries."},
            {"step": 3, "text": "Pour the sumac liquid into a saucepan. Whisk in the cornmeal gradually to prevent lumps."},
            {"step": 4, "text": "Set over medium heat and cook, stirring constantly, until the mixture thickens, about 10 to 15 minutes."},
            {"step": 5, "text": "Stir in the honey and salt. Pour into serving bowls."},
            {"step": 6, "text": "Serve warm or chilled."}
        ],
        "notes": [
            "Use only staghorn sumac (Rhus typhina) or smooth sumac (Rhus glabra). Never use white-berried sumac, which is poisonous."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sumac", "pudding", "navajo", "dessert", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "blue-corn-mush-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Terri Ami's Blue Corn Mush",
        "native_name": "",
        "category": "breakfast",
        "attribution": "Terri Ami",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 192 (Indigenous Partners)",
        "description": "Terri Ami shares this traditional blue corn mush, a staple in Southwestern cuisine. The blue corn gives it a distinctive color and nutty flavor.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "blue cornmeal", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "salt", "quantity": "½", "unit": "tsp"},
            {"item": "culinary ash (optional)", "quantity": "1", "unit": "tsp"},
            {"item": "maple syrup or honey for serving", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Bring the water and salt to a boil in a medium saucepan."},
            {"step": 2, "text": "Slowly whisk in the blue cornmeal, stirring constantly to prevent lumps."},
            {"step": 3, "text": "If using culinary ash, stir it in now—it will help the corn maintain its blue color."},
            {"step": 4, "text": "Reduce heat to low and cook, stirring frequently, until the mush is thick and the cornmeal is tender, about 15 to 20 minutes."},
            {"step": 5, "text": "Serve warm with maple syrup or honey drizzled on top."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "blue corn", "mush", "breakfast", "southwest", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "corn-broth-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Chef Freddie Bitsoie's Corn Broth",
        "native_name": "",
        "category": "soups",
        "attribution": "Chef Freddie Bitsoie",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 193 (Indigenous Partners)",
        "description": "Freddie Bitsoie, executive chef at the renowned Mitsitam Café at the National Museum of the American Indian in Washington, D.C., is one of the most sought-after educators and presenters, with a deep knowledge of art history and anthropology. Freddie shares his passion for Navajo (Diné) foods with wit and panache. His simple, elegant recipes are as inspiring as they are accessible. 'This broth is a workhorse in our kitchen; easy to make and more delicious as it simmers on the back of the stove,' he says. 'To make a hearty soup or stew, add smoked fish or duck. Add soaked hominy or beans for a nutritious meal. It will keep several days in the refrigerator and freezes beautifully.'",
        "servings_yield": "Makes about 2 quarts",
        "ingredients": [
            {"item": "ears fresh corn, shucked", "quantity": "6", "unit": ""},
            {"item": "water", "quantity": "4", "unit": "quarts"},
            {"item": "fresh or frozen corn kernels", "quantity": "½", "unit": "cup"},
            {"item": "stalks celery, roughly chopped", "quantity": "3", "unit": ""},
            {"item": "carrots, roughly chopped", "quantity": "3", "unit": ""},
            {"item": "cloves garlic, minced", "quantity": "3", "unit": ""},
            {"item": "sprigs fresh thyme", "quantity": "4", "unit": ""},
            {"item": "bay leaves", "quantity": "2", "unit": ""},
            {"item": "salt and pepper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine all of the ingredients, except for the salt and pepper, in a pot. Bring to a boil, then turn the heat down to a simmer."},
            {"step": 2, "text": "Simmer for about 3 hours. Strain the broth and discard the vegetables."},
            {"step": 3, "text": "Using a paper towel, strain the broth again for clarity. Pour the broth back into the pot."},
            {"step": 4, "text": "Place over medium heat and reduce it by three-fourths. Season with salt and pepper, to taste."},
            {"step": 5, "text": "Check the seasoning before serving. Serve warm or hot."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "corn", "broth", "soup", "navajo", "guest chef"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "two-fruit-jam-scattered-seeds-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Felicia Cocotzin Ruiz's Two-Fruit Jam Scattered with Seeds",
        "native_name": "",
        "category": "sides",
        "attribution": "Felicia Cocotzin Ruiz",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 194 (Indigenous Partners)",
        "description": "Chef Felicia is an inspiration. Her Facebook and Instagram posts showcase her thoughtful, authentic plant-based recipes, all rooted in the history and culture of the Southwest. They reflect the bold flavors of this deeply spiritual place. This jam is great on mesquite crackers, on blue corn pancakes, or in amaranth porridge.",
        "servings_yield": "Makes about 1 pint",
        "ingredients": [
            {"item": "tomatillos, husked, washed, and chopped", "quantity": "1", "unit": "pound"},
            {"item": "xoconostle (nopal cactus fruit), cut in half, seeds removed with a spoon, peeled", "quantity": "1", "unit": "pound"},
            {"item": "honey", "quantity": "¾ to 1", "unit": "cup"},
            {"item": "water", "quantity": "1", "unit": "cup"},
            {"item": "sea salt", "quantity": "½", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Put all of the ingredients in a large saucepan and bring to a boil. Reduce the heat to simmer, stir well, and cook for about 45 minutes, until mixture has the consistency of jam."},
            {"step": 2, "text": "The jam will thicken even more once cooled and will keep for about 6 months refrigerated in a tightly covered container."}
        ],
        "notes": [
            "*Xoconostle is the fruit of the nopal cactus."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "jam", "tomatillo", "cactus", "southwest", "guest chef", "plant-based"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "wild-berries-amaranth-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Valerie Segrest's Wild Berries with Amaranth",
        "native_name": "",
        "category": "breakfast",
        "attribution": "Valerie Segrest",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 195 (Indigenous Partners)",
        "description": "A native nutrition educator who focuses on local, traditional foods, Valerie Segrest is a member of the Muckleshoot tribe. She serves her community as the coordinator of the Muckleshoot Food Sovereignty Project and as the Traditional Foods and Medicines Program Manager. She is coauthor with Elise Krohn of Feeding the People, Feeding the Spirit: Revitalizing Northwest Coastal Indian Food Culture. Huckleberries grow throughout the Pacific Northwest. 'Some are bright red with a bitter punch; others are as big as grapes and royal purple,' Valerie and her coauthor write. 'Ceremonies, spiritual journeys, harvesting and honor songs, careful ecological managements all celebrate the huckleberries' noble role in our culture.' This dish makes a delicious breakfast. It's good with any wild berries you might wish to use.",
        "servings_yield": "Serves 2",
        "ingredients": [
            {"item": "amaranth", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "huckleberries or any wild berries", "quantity": "1", "unit": "cup"},
            {"item": "maple syrup", "quantity": "1", "unit": "tbsp"},
            {"item": "balsamic vinegar", "quantity": "2", "unit": "tsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the amaranth in a bowl, add enough water to cover by 1 inch, and set aside to soak overnight. Drain in a colander and rinse under cold running water."},
            {"step": 2, "text": "Add the amaranth to a pot with enough water to cover and add a pinch of salt. Bring to a boil and then reduce the heat to a simmer. Cover and cook for about 8 to 10 minutes; drain off any unabsorbed water."},
            {"step": 3, "text": "Put the berries, just enough water to cover the bottom of the pot, syrup, and vinegar into a small saucepan. Set over low heat and gently simmer until the berries soften and begin to burst, about 2 to 5 minutes."},
            {"step": 4, "text": "Spoon the berries over the amaranth and serve warm or at room temperature."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "amaranth", "berries", "breakfast", "huckleberry", "guest chef", "pacific northwest"],
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

    print(f"Successfully added {len(new_recipes)} Sioux Chef recipes (batch 11 - Indigenous Partners)")
    print(f"Total recipes: {data['meta']['total_count']}")
    return True

if __name__ == '__main__':
    main()
