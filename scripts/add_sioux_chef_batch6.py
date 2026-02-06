#!/usr/bin/env python3
"""Add sixth batch of Sioux Chef recipes - Fields and Gardens completion + Prairies and Lakes"""

import json
from datetime import datetime

new_recipes = [
    {
        "id": "amaranth-crackers-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Amaranth Crackers",
        "native_name": "Wahpé Ská Aǧúyapi",
        "category": "snacks",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 60",
        "description": "These rich and nutty crackers are terrific with the Smoked Whitefish and White Bean Spread, page 44, and pair beautifully with duck pâté.",
        "servings_yield": "Makes about 2 dozen crackers",
        "ingredients": [
            {"item": "amaranth flour", "quantity": "1", "unit": "cup"},
            {"item": "sunflower seeds, toasted and ground", "quantity": "1/2", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "generous pinch"},
            {"item": "warm water", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "In a medium bowl, mix together the flour, sunflower seeds, oil, and salt. Stir in the water to make a stiff dough."},
            {"step": 2, "text": "Turn onto a floured work surface and knead until smooth."},
            {"step": 3, "text": "Preheat the oven to 350°F."},
            {"step": 4, "text": "Divide the dough in half. Roll each portion paper-thin and cut into 2-inch squares."},
            {"step": 5, "text": "Set the crackers on baking sheets and bake until golden brown, about 15 to 20 minutes."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "crackers", "amaranth", "snack"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "wild-rice-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Cakes",
        "native_name": "Psíŋ Aǧúyapi Saksáka",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 63",
        "description": "These hearty cakes may be seared, baked, or griddled. Delicious on their own with a drizzle of Wojape, they make an excellent base for smoked fish or game.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "cooked Real Wild Rice, page 81", "quantity": "2", "unit": "cups"},
            {"item": "chopped wild onion or shallot", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1 to 2", "unit": "tsp"},
            {"item": "duck egg, beaten", "quantity": "1", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "wild rice flour, page 167, or finely ground cornmeal, plus a tablespoon for dusting the cakes", "quantity": "1/4", "unit": "cup"},
            {"item": "sunflower oil", "quantity": "3 to 4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 250°F."},
            {"step": 2, "text": "In a food processor fitted with a steel blade, pulse together all of the ingredients to make a rough dough."},
            {"step": 3, "text": "Using moistened hands, form the mixture into patties about 1/2 inch thick. Dust the patties with flour and set aside."},
            {"step": 4, "text": "Film a skillet with the oil and set over medium heat. Working in batches, fry the patties until golden brown on each side, about 5 to 7 minutes per side."},
            {"step": 5, "text": "Transfer to a baking sheet and put in the oven to keep warm."}
        ],
        "temperature": "250°F (120°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "cakes", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "sorrel-sauce-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Sorrel Sauce",
        "native_name": "Pȟežíȟota Iyúlthuŋ",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 64",
        "description": "This bright, tangy sauce is wonderful drizzled over fish or stirred into soups.",
        "servings_yield": "Makes about 1/2 cup",
        "ingredients": [
            {"item": "sorrel leaves, stems removed", "quantity": "2", "unit": "cups"},
            {"item": "sunflower oil", "quantity": "1/4", "unit": "cup"},
            {"item": "maple vinegar or apple cider vinegar", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "pinch"},
            {"item": "maple sugar", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the sorrel and oil into a blender or food processor and puree until smooth."},
            {"step": 2, "text": "Add the vinegar and season to taste with salt and maple sugar."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "sauce", "sorrel", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "summers-vegetable-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Summer's Vegetable Soup with Wild Greens",
        "native_name": "Blokétu Wathótho Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 65",
        "description": "As summer vegetables start to ripen, we like to make a big batch of this simple soup. It's delicious warm, at room temperature, or chilled.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "small summer squash, cut into 1-inch chunks", "quantity": "2", "unit": ""},
            {"item": "sweet corn kernels", "quantity": "2", "unit": "cups"},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "chopped wild greens such as watercress, purslane, or sorrel", "quantity": "2", "unit": "cups"},
            {"item": "chopped mint", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the squash and corn and continue cooking, stirring often, until the squash is tender, about 5 to 7 minutes."},
            {"step": 3, "text": "Add the stock and bring to a simmer."},
            {"step": 4, "text": "Stir in the greens and mint and cook just until the greens are wilted."},
            {"step": 5, "text": "Season with salt to taste."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "summer", "vegetables"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "missouri-river-pozole-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Missouri River Pozole",
        "native_name": "Mníšoše Makhóčhe Pasláyapi Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 66",
        "description": "This hearty soup is our take on the traditional Mexican pozole. Depending on the season, we flavor it with wild greens, mushrooms, or smoked fish.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "cooked hominy, page 31", "quantity": "2", "unit": "cups"},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1", "unit": "cup"},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "smoked salt", "quantity": "", "unit": "to taste"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"},
            {"item": "sliced radishes for garnish", "quantity": "", "unit": ""},
            {"item": "chopped wild greens for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the hominy, beans, and stock and bring to a simmer."},
            {"step": 3, "text": "Stir in the sage and cook for about 10 minutes."},
            {"step": 4, "text": "Season with the smoked salt and juniper."},
            {"step": 5, "text": "Serve garnished with the radishes and wild greens."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "pozole", "hominy"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "hearty-mushroom-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Hearty Mushroom, Sweet Potato, and Bean Soup",
        "native_name": "Čhaŋnákpa na Bló Skúya na Omníča Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 67",
        "description": "This warming, earthy soup is perfect for cool autumn evenings. It's hearty enough to serve as a main course.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "fresh mushrooms, sliced", "quantity": "2", "unit": "cups"},
            {"item": "medium sweet potato, peeled and cut into 1-inch chunks", "quantity": "1", "unit": ""},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1", "unit": "cup"},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the mushrooms and continue cooking until they release their liquid, about 5 minutes."},
            {"step": 3, "text": "Add the sweet potato, beans, and stock and bring to a simmer."},
            {"step": 4, "text": "Cook until the sweet potato is tender, about 20 to 25 minutes."},
            {"step": 5, "text": "Stir in the sage and season with salt and juniper."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "mushrooms", "sweet potato"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "fish-head-wild-rice-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Fish Head and Wild Rice Soup",
        "native_name": "Hoǧáŋ Phá na Psíŋ Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 69",
        "description": "This soup is a celebration of nose-to-tail cooking. The fish head adds incredible depth of flavor to the broth.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "large fish head from walleye, whitefish, or other freshwater fish", "quantity": "1", "unit": ""},
            {"item": "water", "quantity": "6", "unit": "cups"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "cooked Real Wild Rice, page 81", "quantity": "1", "unit": "cup"},
            {"item": "chopped wild greens", "quantity": "1", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the fish head and water into a large pot and bring to a boil. Reduce the heat and simmer until the broth is flavorful, about 30 to 40 minutes."},
            {"step": 2, "text": "Remove the fish head and pick off any meat, discarding the bones. Return the meat to the pot."},
            {"step": 3, "text": "Add the onion, wild rice, and sage and simmer for 10 minutes."},
            {"step": 4, "text": "Stir in the greens and cook just until wilted."},
            {"step": 5, "text": "Season with salt to taste."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "fish", "wild rice"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "white-bean-winter-squash-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "White Bean and Winter Squash Soup",
        "native_name": "Omníča Ská na Wagmú Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 70",
        "description": "This creamy, comforting soup is perfect for cold winter days. The sweetness of the squash balances beautifully with the earthy beans.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "small winter squash, peeled, seeded, and cut into 1-inch chunks", "quantity": "1", "unit": ""},
            {"item": "Cedar-Braised Beans (white beans), page 36", "quantity": "2", "unit": "cups"},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "maple syrup", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the squash, beans, and stock and bring to a simmer."},
            {"step": 3, "text": "Cook until the squash is very tender, about 25 to 30 minutes."},
            {"step": 4, "text": "Puree about half of the soup in a blender and return to the pot."},
            {"step": 5, "text": "Stir in the sage and maple syrup and season with salt."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "beans", "squash", "winter"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "smoked-turkey-acorn-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Turkey and Acorn Soup",
        "native_name": "Waglékšuŋ Asótkaziyapi na Úta Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 71",
        "description": "Smoked turkey adds depth to this warming autumn soup. The acorn flour gives it a subtle, nutty sweetness.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "shredded Smoked Turkey, page 110, or smoked turkey from the deli", "quantity": "2", "unit": "cups"},
            {"item": "Corn or Turkey Stock, page 170", "quantity": "4", "unit": "cups"},
            {"item": "acorn flour or hazelnut flour", "quantity": "2", "unit": "tbsp"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the turkey and stock and bring to a simmer."},
            {"step": 3, "text": "Whisk in the acorn flour and cook, stirring, until the soup thickens slightly, about 10 minutes."},
            {"step": 4, "text": "Stir in the sage and season with salt."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "turkey", "smoked", "acorn"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "squash-apple-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Squash and Apple Soup with Fresh Cranberry Sauce",
        "native_name": "Wagmú na Tȟaspáŋ Waháŋpi nakúŋ Wathókeča T'áǧa Yužápi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 72-73",
        "description": "The sweetness of the squash and apples in this velvety soup is balanced by the bright, tart cranberry sauce.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "medium winter squash, peeled, seeded, and cut into chunks", "quantity": "1", "unit": ""},
            {"item": "tart apples, cored and cut into chunks", "quantity": "2", "unit": ""},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "Fresh Cranberry Sauce for garnish", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the squash, apples, and stock and bring to a simmer."},
            {"step": 3, "text": "Cook until the squash and apples are very tender, about 25 to 30 minutes."},
            {"step": 4, "text": "Puree the soup in a blender until smooth."},
            {"step": 5, "text": "Stir in the maple syrup and season with salt."},
            {"step": 6, "text": "Serve garnished with a swirl of Fresh Cranberry Sauce."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "squash", "apple", "cranberry"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "black-bean-yucca-soup-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Black Bean and Yucca Soup with Warming Spices",
        "native_name": "Omníča Sápa na Hupȟéstola Hutkȟáŋ Waháŋpi",
        "category": "soups",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 74",
        "description": "This hearty soup is warming and satisfying. The yucca adds a starchy, comforting element.",
        "servings_yield": "Serves 4 to 5",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "Cedar-Braised Beans (black beans), page 36", "quantity": "2", "unit": "cups"},
            {"item": "yucca, peeled and cut into 1-inch chunks", "quantity": "1", "unit": "cup"},
            {"item": "Corn Stock, page 170, or water", "quantity": "4", "unit": "cups"},
            {"item": "crushed juniper", "quantity": "1/2", "unit": "tsp"},
            {"item": "sumac", "quantity": "1/2", "unit": "tsp"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a soup pot with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the beans, yucca, and stock and bring to a simmer."},
            {"step": 3, "text": "Cook until the yucca is tender, about 20 to 25 minutes."},
            {"step": 4, "text": "Stir in the juniper, sumac, and sage and season with salt."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "soup", "black beans", "yucca"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "real-wild-rice-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Real Wild Rice",
        "native_name": "Psíŋ Ikčéka",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 81",
        "description": "True wild rice is not cultivated but harvested from canoes using traditional methods. It cooks up fluffy with a distinctive nutty flavor. Properly stored, it will keep for years.",
        "servings_yield": "Serves about 8",
        "ingredients": [
            {"item": "wild rice, rinsed", "quantity": "1", "unit": "cup"},
            {"item": "water", "quantity": "3", "unit": "cups"},
            {"item": "salt", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the rice and water into a medium saucepan and bring to a boil."},
            {"step": 2, "text": "Reduce the heat to a simmer, cover, and cook until the rice is tender and most of the grains have split open, about 45 minutes to 1 hour."},
            {"step": 3, "text": "Drain any excess water (reserve for Wild Rice Stock, page 170)."},
            {"step": 4, "text": "Season with salt to taste."}
        ],
        "notes": [
            "True wild rice is hand-harvested from lakes in Minnesota, Wisconsin, and Canada. It cooks differently than cultivated 'wild rice' and has a more complex, nutty flavor.",
            "Save the cooking water for Wild Rice Stock."
        ],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "side dish", "component"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": []
    },
    {
        "id": "tatanka-truck-fried-wild-rice-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tatanka Truck Fried Wild Rice Bowl",
        "native_name": "Wakšíča Psíŋ Čheúŋpapi Ožúla",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 83",
        "description": "This is one of our most popular dishes at the food truck. It's a one-bowl meal that's satisfying, healthy, and delicious.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "3", "unit": "tbsp"},
            {"item": "duck egg, beaten", "quantity": "1", "unit": ""},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "cooked Real Wild Rice, page 81", "quantity": "3", "unit": "cups"},
            {"item": "sweet corn kernels", "quantity": "1", "unit": "cup"},
            {"item": "chopped wild greens", "quantity": "1", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "smoked salt", "quantity": "", "unit": "to taste"},
            {"item": "Wojape, page 173, for serving", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Heat 1 tablespoon of the oil in a large skillet over high heat. Add the egg and scramble until just set. Remove and set aside."},
            {"step": 2, "text": "Add the remaining oil to the skillet and sauté the onion until tender, about 2 to 3 minutes."},
            {"step": 3, "text": "Add the wild rice and corn and cook, stirring occasionally, until the rice is lightly browned, about 5 to 7 minutes."},
            {"step": 4, "text": "Stir in the greens and sage and cook until the greens are wilted."},
            {"step": 5, "text": "Return the egg to the pan and toss to combine."},
            {"step": 6, "text": "Season with smoked salt and serve drizzled with Wojape."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "bowl", "tatanka truck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "wild-rice-pilaf-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice Pilaf with Wild Mushrooms, Roasted Chestnuts, and Dried Cranberries",
        "native_name": "Psíŋ na Čhaŋnákpa na Úma Čheúŋpapi na Wathókeča T'áǧa",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 84-85",
        "description": "This festive pilaf is perfect for holiday gatherings. The combination of wild rice, mushrooms, chestnuts, and cranberries is both earthy and celebratory.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "sunflower oil", "quantity": "2", "unit": "tbsp"},
            {"item": "wild onion or large shallot, chopped", "quantity": "1", "unit": ""},
            {"item": "fresh wild mushrooms, sliced", "quantity": "2", "unit": "cups"},
            {"item": "cooked Real Wild Rice, page 81", "quantity": "3", "unit": "cups"},
            {"item": "roasted chestnuts, roughly chopped", "quantity": "1/2", "unit": "cup"},
            {"item": "dried cranberries", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch"}
        ],
        "instructions": [
            {"step": 1, "text": "Film a large skillet with the oil and set over medium heat. Sauté the onion until tender, about 3 to 5 minutes."},
            {"step": 2, "text": "Add the mushrooms and cook until they release their liquid and begin to brown, about 7 to 10 minutes."},
            {"step": 3, "text": "Add the wild rice, chestnuts, and cranberries and cook, stirring, until heated through, about 5 minutes."},
            {"step": 4, "text": "Stir in the sage and season with salt and juniper."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "wild rice", "pilaf", "mushrooms", "chestnuts"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "timpsula-cakes-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Timpsula Cakes with Cedar-Braised Beans",
        "native_name": "Tȟíŋpsila Aǧúyapi Sáka na Omníča Lolóbyapi",
        "category": "sides",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 86-87",
        "description": "Timpsula, or prairie turnip, was a staple food for the Plains tribes. These cakes are earthy and satisfying, perfect topped with beans and greens.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "timpsula, cut into chunks, or medium turnips plus 1 small butternut squash, peeled, seeded, all cut into chunks", "quantity": "6 or 4", "unit": ""},
            {"item": "water to cover", "quantity": "", "unit": ""},
            {"item": "small sprig cedar", "quantity": "1", "unit": ""},
            {"item": "salt", "quantity": "", "unit": "pinch, to taste"},
            {"item": "crushed juniper", "quantity": "", "unit": "pinch, to taste"},
            {"item": "hazelnut or sunflower oil or Rendered Duck Fat, page 105, plus extra for greasing the pan", "quantity": "2 to 3", "unit": "tbsp"},
            {"item": "Cedar-Braised Beans, page 36", "quantity": "1", "unit": "cup"},
            {"item": "Griddled Maple Squash, page 33", "quantity": "1", "unit": "cup"},
            {"item": "toasted sunflower seeds, page 158", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Put the timpsula (or turnip and squash) and cedar in a large pot and add water to just cover. Set over high heat, bring to a boil, reduce to a simmer, and cook until the vegetables are very tender, about 15 to 20 minutes."},
            {"step": 2, "text": "Drain off any excess water and place in a bowl. Mash with the oil and season with the salt and juniper."},
            {"step": 3, "text": "When the mash has cooled a little, form patties about 4 inches in diameter and 2 inches thick."},
            {"step": 4, "text": "Film a large skillet with the remaining oil and set over medium-high heat. Sear the patties until lightly browned and crisped on both sides, about 5 minutes per side."},
            {"step": 5, "text": "Serve topped with Cedar-Braised Beans, Griddled Maple Squash, and sunflower seeds."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [
            {"original": "timpsula", "substitute": "4 medium turnips plus 1 small butternut squash", "note": "Peel and cut all into chunks"}
        ],
        "tags": ["indigenous", "native american", "timpsula", "prairie turnip", "cakes"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "smoked-whitefish-trout-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Smoked Whitefish or Trout",
        "native_name": "Hoǧáŋ Asótkaziyapi",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 89",
        "description": "In the old days, smoking fish fresh was a group effort. We are using a more modern technique with brining as the first step. Be sure the fish is thoroughly cleaned before you begin.",
        "servings_yield": "Serves 4 to 6 (or more as an appetizer)",
        "ingredients": [
            {"item": "coarse salt", "quantity": "1/2", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "water", "quantity": "1", "unit": "quart"},
            {"item": "trout, whitefish, or walleye fillets, 3 to 5 ounces each, pin bones removed and skin on", "quantity": "2", "unit": "lb"}
        ],
        "instructions": [
            {"step": 1, "text": "In a 4-quart container, stir together the salt, maple syrup, and water until the salt is thoroughly dissolved."},
            {"step": 2, "text": "Add the fillets; they should be submerged. Cover and refrigerate for about 3 hours."},
            {"step": 3, "text": "Remove the fillets from the brine, rinse thoroughly, pat dry, place, skin side down, on a cooling rack (set over a sheet pan to catch any drips). Continue to dry the fish in the refrigerator for at least 24 hours, or until the skin is tacky to the touch."},
            {"step": 4, "text": "Bring a smoker to 160°F. Put the fish onto the smoking racks, skin side down, about 1/2 inch apart. Smoke until the fish is cooked through and has darkened in color, about 2 1/2 to 3 hours."},
            {"step": 5, "text": "The fish can be stored in an airtight container for up to a week."}
        ],
        "temperature": "160°F (70°C)",
        "notes": [],
        "tips": [
            "Save the skins of the smoked fish. They are delicious when griddled and cut into strips for garnishing a soup. They can also be topped with smoked fish, griddled vegetables, greens, and berries."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "fish", "smoked", "whitefish", "trout"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": True,
        "component_of": ["smoked-whitefish-white-bean-spread-sioux-chef"]
    },
    {
        "id": "wild-rice-crusted-walleye-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Wild Rice-Crusted Walleye",
        "native_name": "Hoǧáŋ",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, pages 90-91",
        "description": "The Red Lake Nation is an Ojibwe community in northern Minnesota, home of our ethnobotanist Tashia, who shares her knowledge with our team. We source all of our fish—the walleye, northerns, and whitefish—from the Red Lake Nation Fishery.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "walleye or trout fillets, or butterflied fish", "quantity": "4 to 6", "unit": ""},
            {"item": "Wild Rice Flour, page 167, or finely ground cornmeal", "quantity": "1/2", "unit": "cup"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "crushed juniper berries", "quantity": "", "unit": "pinch"},
            {"item": "sunflower oil, or more as needed", "quantity": "1/4", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse the fillets, remove any pin bones, and pat dry."},
            {"step": 2, "text": "Pour the wild rice flour onto a flat plate and stir in the smoked salt and juniper."},
            {"step": 3, "text": "Dredge both sides of the fillets in the seasoned flour to thoroughly coat."},
            {"step": 4, "text": "Heat the oil in a large skillet over a high flame. Without crowding the pan, fry one or two of the fillets in the oil for about 2 to 4 minutes per side until nicely crisped and cooked through."},
            {"step": 5, "text": "Drain on paper towels and serve immediately."}
        ],
        "notes": [],
        "tips": [
            "For an impressive presentation, butterfly the fish (so that it's filleted but whole and served head on). Garnish with fresh cranberries, chopped apple, or berries lightly tossed into the pan, right before serving.",
            "This recipe works nicely with trout, too."
        ],
        "substitutions": [],
        "tags": ["indigenous", "native american", "fish", "walleye", "wild rice", "fried"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "herb-roasted-fish-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Herb-Roasted Fish",
        "native_name": "Hoǧáŋ Čheúŋpapi",
        "category": "mains",
        "attribution": "Chef Brian Yazzie (Navajo Nation)",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 92",
        "description": "Chef Brian Yazzie shares this recipe from his family's traditions. The original recipe calls for the bluehead sucker fish, a rare fish specific to the Southwest, but any small or large firm fish works nicely. The fish is traditionally cooked in a pit filled with hot wood coals, covered with sand so that it steam-roasts.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "large whitefish, about 4 to 5 pounds", "quantity": "1", "unit": ""},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "sumac", "quantity": "", "unit": ""},
            {"item": "sprigs sage", "quantity": "3 to 4", "unit": ""},
            {"item": "wild onions or shallots cut into quarters", "quantity": "4 to 5", "unit": ""},
            {"item": "corn husks, soaked, for the traditional pit method", "quantity": "3", "unit": "dozen"}
        ],
        "instructions": [
            {"step": 1, "text": "Generously sprinkle the outside and the cavities of the fish with the salt and sumac. Stuff the cavities of the fish with the sage and the onions."},
            {"step": 2, "text": "If using the traditional pit method, wrap the fish in enough of the soaked corn husks to completely cover the fish."},
            {"step": 3, "text": "To cook the fish in a traditional pit: Cover the bottom of a 1-foot-deep pit (2 feet in diameter) with hot wood coals. Set the corn husk-wrapped fish on the coals. Fill the pit with sand to cover the fish. Steam/cook the fish for 45 minutes to 1 hour. Dig away the sand. Remove the fish from the pit. Set on a platter. Serve the fish whole, family style."},
            {"step": 4, "text": "To cook the fish in a clay pot: Soak the pot in water for a good hour. Place the fish in the clay pot. Cover and place in a 250°F oven and cook the fish for about 1 hour or until it is tender. Remove the clay pot from the oven. Remove the fish and serve family style."}
        ],
        "temperature": "250°F (120°C) for clay pot method",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "navajo", "fish", "roasted", "herb"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "sunflower-crusted-trout-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Tatanka Truck Sunflower-Crusted Trout",
        "native_name": "",
        "category": "mains",
        "attribution": "Chef Vern DeFoe (Red Cliff Band of Lake Superior Chippewa)",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 93",
        "description": "This crispy trout with a sunflower crust is one of chef Vern DeFoe's recipes and a Tatanka Truck favorite. Vern, a member of the Red Cliff Band of Lake Superior Chippewa, serves the trout with roe on wild rice flatbread, garnished with dried apple slices.",
        "servings_yield": "Serves 4 to 6",
        "ingredients": [
            {"item": "trout fillets", "quantity": "4 to 6", "unit": ""},
            {"item": "ground untoasted sunflower seeds", "quantity": "1/4", "unit": "cup"},
            {"item": "ground sumac", "quantity": "1 to 2", "unit": "tbsp"},
            {"item": "smoked salt", "quantity": "", "unit": "pinch"},
            {"item": "sunflower oil", "quantity": "2 to 3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Rinse the fillets, remove any pin bones, and pat dry."},
            {"step": 2, "text": "On a flat plate, mix together the sunflower seeds, sumac, and smoked salt."},
            {"step": 3, "text": "Dredge both sides of the fillets in the seasoned mixture to thoroughly coat."},
            {"step": 4, "text": "Heat the oil in a large skillet over a high flame. Without crowding the pan, fry one or two of the fillets in the oil for about 2 to 4 minutes per side, until nicely crisped and cooked through."},
            {"step": 5, "text": "Drain on paper towels and serve immediately."}
        ],
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "fish", "trout", "sunflower", "tatanka truck"],
        "confidence": {"overall": "high", "flags": []},
        "image_refs": [],
        "is_component": False
    },
    {
        "id": "grouse-cranberry-sage-sioux-chef",
        "collection": "all",
        "collection_display": "Other Family Recipes",
        "title": "Grouse with Cranberry and Sage",
        "native_name": "Čháŋšiyo nakúŋ Gmá na Phežíȟota Iyúlthuŋ",
        "category": "mains",
        "attribution": "Sean Sherman",
        "source_note": "The Sioux Chef's Indigenous Kitchen, page 95",
        "description": "Grouse, such as partridge, feed on wild berries, nuts, and seeds. Near the cranberry regions of southern Wisconsin, the wild berries turn the bird's meat bright pink. In this recipe, the rendered duck fat, cranberries, and sage baste the meat while it roasts to become tender and flavorful. This is great on our Wild Rice Pilaf, page 84.",
        "servings_yield": "Serves 4",
        "ingredients": [
            {"item": "dressed grouse, about 1 pound each", "quantity": "2", "unit": ""},
            {"item": "coarse salt", "quantity": "", "unit": ""},
            {"item": "tart apple", "quantity": "1", "unit": ""},
            {"item": "sprigs sage", "quantity": "8", "unit": ""},
            {"item": "cranberries", "quantity": "1/4", "unit": "cup"},
            {"item": "maple syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "walnuts, toasted", "quantity": "1/4", "unit": "cup"},
            {"item": "Rendered Duck Fat, page 105, or sunflower oil", "quantity": "1/4", "unit": "cup"},
            {"item": "chopped sage", "quantity": "1", "unit": "tbsp"},
            {"item": "wild onion or shallot, minced", "quantity": "1", "unit": ""},
            {"item": "water or cider as needed", "quantity": "", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat the oven to 350°F. Rinse the birds and pat dry with paper towels. Sprinkle them inside and out with the salt."},
            {"step": 2, "text": "Core the apple and cut into quarters. Place 2 quarters of apple and 4 sprigs of sage into each bird's cavity."},
            {"step": 3, "text": "In a small saucepan, cook the cranberries with the maple syrup over low heat until the cranberries pop, about 3 minutes."},
            {"step": 4, "text": "Put the berries, walnuts, duck fat, sage, and onion into a food processor fitted with a steel blade and process until combined."},
            {"step": 5, "text": "Tuck some of the mixture under the breast skin of the birds and rub the remaining mixture over the birds."},
            {"step": 6, "text": "Set breast side up on a roasting rack set over a roasting pan. Add about 2 inches of cider or water into the pan."},
            {"step": 7, "text": "Roast the grouse, basting frequently with the pan juices, until the birds are nicely browned, the juices run clear, and a meat thermometer inserted into the thigh registers 155°F. Remove and allow to stand at least 10 minutes."},
            {"step": 8, "text": "Carve and serve with the pan juices drizzled over all."}
        ],
        "temperature": "350°F (175°C)",
        "notes": [],
        "tips": [],
        "substitutions": [],
        "tags": ["indigenous", "native american", "grouse", "game bird", "cranberry", "roasted"],
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
