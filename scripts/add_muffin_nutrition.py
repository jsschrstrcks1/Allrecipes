#!/usr/bin/env python3
"""
Add nutrition data to muffin recipes in the reference collection.
Uses USDA standard nutrition values for common baking ingredients.
"""

import json
import re
from fractions import Fraction
from pathlib import Path

# USDA nutrition values per standard unit
# Format: {ingredient: {unit: {calories, fat_g, carbs_g, protein_g, sodium_mg, fiber_g, sugar_g}}}
NUTRITION_DB = {
    # Flours
    "all-purpose flour": {"cup": {"cal": 440, "fat": 1.2, "carbs": 92, "protein": 12.5, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
                         "tbsp": {"cal": 28, "fat": 0.1, "carbs": 5.8, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "flour": {"cup": {"cal": 440, "fat": 1.2, "carbs": 92, "protein": 12.5, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
             "tbsp": {"cal": 28, "fat": 0.1, "carbs": 5.8, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "whole wheat flour": {"cup": {"cal": 408, "fat": 2.2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0.4}},
    "cake flour": {"cup": {"cal": 400, "fat": 1, "carbs": 88, "protein": 9, "sodium": 2, "fiber": 2, "sugar": 0.3}},
    "self-rising flour": {"cup": {"cal": 440, "fat": 1.2, "carbs": 92, "protein": 12, "sodium": 1520, "fiber": 3, "sugar": 0.3}},
    "oat flour": {"cup": {"cal": 420, "fat": 9, "carbs": 68, "protein": 15, "sodium": 3, "fiber": 7, "sugar": 1}},
    "almond flour": {"cup": {"cal": 640, "fat": 56, "carbs": 24, "protein": 24, "sodium": 0, "fiber": 12, "sugar": 4}},

    # Sugars
    "granulated white sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "brown sugar": {"cup": {"cal": 836, "fat": 0, "carbs": 216, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 213}},
    "powdered sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 120, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117}},
    "honey": {"cup": {"cal": 1031, "fat": 0, "carbs": 279, "protein": 1, "sodium": 14, "fiber": 0, "sugar": 278}},
    "maple syrup": {"cup": {"cal": 840, "fat": 0.2, "carbs": 216, "protein": 0, "sodium": 27, "fiber": 0, "sugar": 192}},
    "molasses": {"cup": {"cal": 977, "fat": 0, "carbs": 252, "protein": 0, "sodium": 121, "fiber": 0, "sugar": 183}},

    # Dairy
    "milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "buttermilk": {"cup": {"cal": 99, "fat": 2.2, "carbs": 12, "protein": 8, "sodium": 257, "fiber": 0, "sugar": 12}},
    "heavy cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "sour cream": {"cup": {"cal": 444, "fat": 45, "carbs": 8, "protein": 5, "sodium": 108, "fiber": 0, "sugar": 5}},
    "cream cheese": {"cup": {"cal": 793, "fat": 79, "carbs": 8, "protein": 14, "sodium": 691, "fiber": 0, "sugar": 6}},
    "yogurt": {"cup": {"cal": 149, "fat": 8, "carbs": 11, "protein": 9, "sodium": 113, "fiber": 0, "sugar": 11}},
    "greek yogurt": {"cup": {"cal": 190, "fat": 10, "carbs": 8, "protein": 18, "sodium": 65, "fiber": 0, "sugar": 7}},

    # Fats
    "butter": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 1246, "fiber": 0, "sugar": 0},
               "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0}},
    "vegetable oil": {"cup": {"cal": 1927, "fat": 218, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coconut oil": {"cup": {"cal": 1879, "fat": 218, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                   "tbsp": {"cal": 117, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "olive oil": {"tbsp": {"cal": 119, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Eggs
    "large egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "eggs": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg white": {"": {"cal": 17, "fat": 0, "carbs": 0.2, "protein": 4, "sodium": 55, "fiber": 0, "sugar": 0.2}},
    "egg yolk": {"": {"cal": 55, "fat": 5, "carbs": 0.6, "protein": 3, "sodium": 8, "fiber": 0, "sugar": 0.1}},

    # Leavening
    "baking powder": {"tbsp": {"cal": 5, "fat": 0, "carbs": 2, "protein": 0, "sodium": 400, "fiber": 0, "sugar": 0},
                     "tsp": {"cal": 2, "fat": 0, "carbs": 0.7, "protein": 0, "sodium": 133, "fiber": 0, "sugar": 0}},
    "baking soda": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1260, "fiber": 0, "sugar": 0},
                   "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 3780, "fiber": 0, "sugar": 0}},

    # Extracts/Flavorings (minimal calories)
    "vanilla extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.5}},
    "almond extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lemon extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Spices (minimal per typical amount)
    "cinnamon": {"tsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 1, "sugar": 0}},
    "nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0}},
    "ginger": {"tsp": {"cal": 6, "fat": 0, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0},
              "tbsp": {"cal": 18, "fat": 0, "carbs": 4, "protein": 0.5, "sodium": 3, "fiber": 0.6, "sugar": 0.5}},
    "fresh ginger": {"tsp": {"cal": 6, "fat": 0, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0},
                    "tbsp": {"cal": 18, "fat": 0, "carbs": 4, "protein": 0.5, "sodium": 3, "fiber": 0.6, "sugar": 0.5}},
    "allspice": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1.4, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "cloves": {"tsp": {"cal": 7, "fat": 0.4, "carbs": 1.3, "protein": 0.1, "sodium": 5, "fiber": 0.7, "sugar": 0}},
    "pumpkin pie spice": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1.2, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},

    # Salt
    "salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 2325, "fiber": 0, "sugar": 0},
            "pinch": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0},
            "dash": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0},
            "": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0}},

    # Fruits
    "fresh peaches": {"cup": {"cal": 60, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 12}},
    "blueberries": {"cup": {"cal": 84, "fat": 0.5, "carbs": 21, "protein": 1, "sodium": 1, "fiber": 3.6, "sugar": 15}},
    "raspberries": {"cup": {"cal": 64, "fat": 0.8, "carbs": 15, "protein": 1.5, "sodium": 1, "fiber": 8, "sugar": 5}},
    "strawberries": {"cup": {"cal": 49, "fat": 0.5, "carbs": 12, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 7}},
    "banana": {"": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3, "sugar": 14}},
    "bananas": {"cup": {"cal": 134, "fat": 0.5, "carbs": 34, "protein": 1.6, "sodium": 2, "fiber": 4, "sugar": 18}},
    "mashed banana": {"cup": {"cal": 200, "fat": 0.7, "carbs": 51, "protein": 2.5, "sodium": 2, "fiber": 6, "sugar": 28}},
    "ripe bananas": {"": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3, "sugar": 14}},
    "apple": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13}},
    "apples": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13}},
    "diced apple": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13}},
    "applesauce": {"cup": {"cal": 167, "fat": 0.4, "carbs": 43, "protein": 0.4, "sodium": 5, "fiber": 2.7, "sugar": 36}},
    "cranberries": {"cup": {"cal": 46, "fat": 0.1, "carbs": 12, "protein": 0.4, "sodium": 2, "fiber": 5, "sugar": 4}},
    "dried cranberries": {"cup": {"cal": 308, "fat": 1.1, "carbs": 82, "protein": 0.2, "sodium": 3, "fiber": 6, "sugar": 65}},
    "raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 5.4, "sugar": 86}},
    "dates": {"cup": {"cal": 415, "fat": 0.4, "carbs": 110, "protein": 3.6, "sodium": 3, "fiber": 12, "sugar": 93}},
    "orange zest": {"tbsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 1, "sugar": 1}},
    "lemon zest": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0.5, "sugar": 0.3},
                  "": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0.5, "sugar": 0.3}},
    "lemon lemon zest": {"": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0.5, "sugar": 0.3}},
    "lemon juice": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.4}},
    "orange juice": {"cup": {"cal": 112, "fat": 0.5, "carbs": 26, "protein": 2, "sodium": 2, "fiber": 0.5, "sugar": 21}},
    "pumpkin puree": {"cup": {"cal": 83, "fat": 0.7, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 7, "sugar": 8}},
    "canned pumpkin": {"cup": {"cal": 83, "fat": 0.7, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 7, "sugar": 8}},
    "mashed sweet potato": {"cup": {"cal": 249, "fat": 0.5, "carbs": 58, "protein": 4.5, "sodium": 90, "fiber": 8.2, "sugar": 24}},
    "grated carrot": {"cup": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 1, "sodium": 76, "fiber": 3, "sugar": 5}},
    "carrots": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1.2, "sodium": 88, "fiber": 3.6, "sugar": 6}},
    "grated zucchini": {"cup": {"cal": 19, "fat": 0.2, "carbs": 4, "protein": 1.4, "sodium": 12, "fiber": 1.2, "sugar": 3}},
    "zucchini": {"cup": {"cal": 19, "fat": 0.2, "carbs": 4, "protein": 1.4, "sodium": 12, "fiber": 1.2, "sugar": 3}},

    # Nuts & Seeds
    "walnuts": {"cup": {"cal": 765, "fat": 76, "carbs": 16, "protein": 18, "sodium": 2, "fiber": 8, "sugar": 3}},
    "chopped walnuts": {"cup": {"cal": 765, "fat": 76, "carbs": 16, "protein": 18, "sodium": 2, "fiber": 8, "sugar": 3}},
    "pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "chopped pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "almonds": {"cup": {"cal": 828, "fat": 72, "carbs": 28, "protein": 30, "sodium": 1, "fiber": 17, "sugar": 6}},
    "sliced almonds": {"cup": {"cal": 529, "fat": 46, "carbs": 18, "protein": 19, "sodium": 1, "fiber": 11, "sugar": 4}},
    "hazelnuts": {"cup": {"cal": 848, "fat": 82, "carbs": 23, "protein": 20, "sodium": 0, "fiber": 13, "sugar": 6}},
    "macadamia nuts": {"cup": {"cal": 962, "fat": 102, "carbs": 19, "protein": 11, "sodium": 7, "fiber": 12, "sugar": 6}},
    "peanuts": {"cup": {"cal": 828, "fat": 72, "carbs": 24, "protein": 38, "sodium": 26, "fiber": 12, "sugar": 6}},
    "peanut butter": {"cup": {"cal": 1517, "fat": 130, "carbs": 50, "protein": 64, "sodium": 1010, "fiber": 12, "sugar": 24},
                     "tbsp": {"cal": 95, "fat": 8, "carbs": 3, "protein": 4, "sodium": 63, "fiber": 0.8, "sugar": 1.5}},
    "poppy seeds": {"tbsp": {"cal": 46, "fat": 4, "carbs": 2, "protein": 2, "sodium": 2, "fiber": 2, "sugar": 0}},
    "sunflower seeds": {"cup": {"cal": 818, "fat": 71, "carbs": 28, "protein": 29, "sodium": 4, "fiber": 12, "sugar": 4}},
    "flax seeds": {"tbsp": {"cal": 37, "fat": 3, "carbs": 2, "protein": 1.3, "sodium": 2, "fiber": 2, "sugar": 0}},
    "chia seeds": {"tbsp": {"cal": 58, "fat": 4, "carbs": 5, "protein": 2, "sodium": 2, "fiber": 4, "sugar": 0}},
    "shredded coconut": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},
    "coconut flakes": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},

    # Chocolate
    "chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "semi-sweet chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "white chocolate chips": {"cup": {"cal": 916, "fat": 55, "carbs": 101, "protein": 10, "sodium": 153, "fiber": 0, "sugar": 101}},
    "cocoa powder": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1},
                    "tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "unsweetened cocoa powder": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "nutella": {"tbsp": {"cal": 100, "fat": 6, "carbs": 11, "protein": 1, "sodium": 15, "fiber": 0.5, "sugar": 10}},
    "chocolate-hazelnut spread": {"tbsp": {"cal": 100, "fat": 6, "carbs": 11, "protein": 1, "sodium": 15, "fiber": 0.5, "sugar": 10}},

    # Cheese
    "cream cheese": {"oz": {"cal": 99, "fat": 10, "carbs": 1, "protein": 2, "sodium": 86, "fiber": 0, "sugar": 0.8},
                    "cup": {"cal": 793, "fat": 79, "carbs": 8, "protein": 14, "sodium": 691, "fiber": 0, "sugar": 6}},
    "nutella": {"cup": {"cal": 1600, "fat": 96, "carbs": 176, "protein": 16, "sodium": 240, "fiber": 8, "sugar": 160},
               "tbsp": {"cal": 100, "fat": 6, "carbs": 11, "protein": 1, "sodium": 15, "fiber": 0.5, "sugar": 10}},
    "cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1, "protein": 28, "sodium": 702, "fiber": 0, "sugar": 0.5}},
    "shredded cheddar": {"cup": {"cal": 455, "fat": 37, "carbs": 1, "protein": 28, "sodium": 702, "fiber": 0, "sugar": 0.5}},
    "shredded cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1, "protein": 28, "sodium": 702, "fiber": 0, "sugar": 0.5}},
    "parmesan cheese": {"cup": {"cal": 431, "fat": 29, "carbs": 4, "protein": 38, "sodium": 1529, "fiber": 0, "sugar": 1}},
    "ricotta cheese": {"cup": {"cal": 428, "fat": 32, "carbs": 7, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.5}},
    "cottage cheese": {"cup": {"cal": 220, "fat": 10, "carbs": 8, "protein": 25, "sodium": 819, "fiber": 0, "sugar": 5}},

    # Oats & Grains
    "old-fashioned oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "rolled oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "quick oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "wheat bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "oat bran": {"cup": {"cal": 231, "fat": 7, "carbs": 62, "protein": 16, "sodium": 4, "fiber": 15, "sugar": 1}},
    "cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 43, "fiber": 9, "sugar": 1}},
    "yellow cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 43, "fiber": 9, "sugar": 1}},
    "wheat germ": {"tbsp": {"cal": 26, "fat": 0.7, "carbs": 4, "protein": 2, "sodium": 0, "fiber": 1, "sugar": 0}},

    # Jams & Preserves
    "jam": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "jelly": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 10}},
    "preserves": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "marmalade": {"tbsp": {"cal": 49, "fat": 0, "carbs": 13, "protein": 0, "sodium": 11, "fiber": 0, "sugar": 10}},

    # Misc
    "corn": {"cup": {"cal": 132, "fat": 2, "carbs": 29, "protein": 5, "sodium": 1, "fiber": 4, "sugar": 5}},
    "corn kernels": {"cup": {"cal": 132, "fat": 2, "carbs": 29, "protein": 5, "sodium": 1, "fiber": 4, "sugar": 5}},
    "bacon": {"slice": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "cup": {"cal": 344, "fat": 27, "carbs": 0, "protein": 24, "sodium": 1096, "fiber": 0, "sugar": 0}},
    "cooked bacon": {"slice": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
                    "cup": {"cal": 344, "fat": 27, "carbs": 0, "protein": 24, "sodium": 1096, "fiber": 0, "sugar": 0}},
    "ham": {"cup": {"cal": 207, "fat": 11, "carbs": 2, "protein": 24, "sodium": 1684, "fiber": 0, "sugar": 0}},
    "sausage": {"link": {"cal": 82, "fat": 7, "carbs": 0.5, "protein": 4, "sodium": 192, "fiber": 0, "sugar": 0}},
    "amaretto liqueur": {"tbsp": {"cal": 44, "fat": 0, "carbs": 5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 5}},
    "amaretto": {"tbsp": {"cal": 44, "fat": 0, "carbs": 5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 5},
                "cup": {"cal": 704, "fat": 0, "carbs": 80, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 80}},
    "amaretto liqueur": {"tbsp": {"cal": 44, "fat": 0, "carbs": 5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 5},
                        "cup": {"cal": 704, "fat": 0, "carbs": 80, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 80}},
    "green apple": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13}},
    "unsweetened cocoa": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1},
                         "tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "raspberry jam": {"cup": {"cal": 896, "fat": 0, "carbs": 224, "protein": 0, "sodium": 96, "fiber": 3, "sugar": 160},
                     "tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "thick raspberry jam": {"cup": {"cal": 896, "fat": 0, "carbs": 224, "protein": 0, "sodium": 96, "fiber": 3, "sugar": 160},
                          "tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "grape jelly": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 10}},
    "pineapple": {"cup": {"cal": 82, "fat": 0.2, "carbs": 22, "protein": 0.9, "sodium": 2, "fiber": 2.3, "sugar": 16}},
    "crushed pineapple": {"cup": {"cal": 82, "fat": 0.2, "carbs": 22, "protein": 0.9, "sodium": 2, "fiber": 2.3, "sugar": 16}},
    "maraschino cherries": {"cup": {"cal": 165, "fat": 0.2, "carbs": 42, "protein": 0.3, "sodium": 10, "fiber": 2, "sugar": 36}},
    "cherries": {"cup": {"cal": 97, "fat": 0.3, "carbs": 25, "protein": 2, "sodium": 0, "fiber": 3, "sugar": 20}},
    "mini chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "mini semi-sweet chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "mini marshmallows": {"cup": {"cal": 159, "fat": 0, "carbs": 41, "protein": 1, "sodium": 22, "fiber": 0, "sugar": 29}},
    "peppermint extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "crushed peppermint candy": {"cup": {"cal": 396, "fat": 0, "carbs": 99, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 99}},
    "candy canes": {"": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 13}},
    "eggnog": {"cup": {"cal": 343, "fat": 19, "carbs": 34, "protein": 10, "sodium": 137, "fiber": 0, "sugar": 21}},
    "lavender": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "dried lavender": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "chai tea": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "instant espresso powder": {"tsp": {"cal": 4, "fat": 0, "carbs": 0.8, "protein": 0.2, "sodium": 0, "fiber": 0, "sugar": 0}},
    "instant coffee": {"tsp": {"cal": 4, "fat": 0, "carbs": 0.8, "protein": 0.2, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "brewed coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "strong brewed coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "pomegranate seeds": {"cup": {"cal": 144, "fat": 2, "carbs": 33, "protein": 3, "sodium": 5, "fiber": 7, "sugar": 24}},
    "truvia": {"tsp": {"cal": 0, "fat": 0, "carbs": 3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
              "tbsp": {"cal": 0, "fat": 0, "carbs": 9, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "russet potatoes": {"": {"cal": 168, "fat": 0.2, "carbs": 38, "protein": 5, "sodium": 24, "fiber": 3, "sugar": 1}},
    "potatoes": {"": {"cal": 168, "fat": 0.2, "carbs": 38, "protein": 5, "sodium": 24, "fiber": 3, "sugar": 1}},
    "stevia": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "caramel sauce": {"tbsp": {"cal": 60, "fat": 1, "carbs": 13, "protein": 0, "sodium": 65, "fiber": 0, "sugar": 11}},
    "caramel": {"tbsp": {"cal": 60, "fat": 1, "carbs": 13, "protein": 0, "sodium": 65, "fiber": 0, "sugar": 11}},
    "blackberries": {"cup": {"cal": 62, "fat": 0.7, "carbs": 14, "protein": 2, "sodium": 1, "fiber": 8, "sugar": 7}},
    "lemon juice": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.4},
                   "": {"cal": 17, "fat": 0, "carbs": 5, "protein": 0.4, "sodium": 1, "fiber": 0, "sugar": 1.5}},  # per whole lemon
    "orange juice": {"cup": {"cal": 112, "fat": 0.5, "carbs": 26, "protein": 2, "sodium": 2, "fiber": 0.5, "sugar": 21},
                    "": {"cal": 62, "fat": 0.2, "carbs": 15, "protein": 1.2, "sodium": 0, "fiber": 3, "sugar": 12}},  # per medium orange
    "scallions": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.4, "sugar": 0.4}},
    "dill": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "paprika": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5}},
    "taco seasoning": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.2, "protein": 0.2, "sodium": 300, "fiber": 0.3, "sugar": 0.3}},
    "culinary lavender": {"tbsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "liquid egg substitute": {"cup": {"cal": 211, "fat": 8, "carbs": 2, "protein": 30, "sodium": 419, "fiber": 0, "sugar": 2}},
    "vanilla pudding": {"cup": {"cal": 280, "fat": 6, "carbs": 51, "protein": 5, "sodium": 320, "fiber": 0, "sugar": 35}},
    "cook and serve vanilla pudding": {"": {"cal": 100, "fat": 0, "carbs": 25, "protein": 0, "sodium": 200, "fiber": 0, "sugar": 18}},  # per box prepared
    "caramel squares": {"": {"cal": 40, "fat": 1, "carbs": 8, "protein": 0.3, "sodium": 25, "fiber": 0, "sugar": 6}},
    "peaches": {"cup": {"cal": 60, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 12}},
    "whipped cream": {"tbsp": {"cal": 15, "fat": 1.4, "carbs": 0.4, "protein": 0.2, "sodium": 4, "fiber": 0, "sugar": 0.4},
                     "cup": {"cal": 240, "fat": 22, "carbs": 7, "protein": 3, "sodium": 60, "fiber": 0, "sugar": 7},
                     "": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},  # for serving - optional
    "for serving whipped cream": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "to taste salt and pepper": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 100, "fiber": 0, "sugar": 0}},
}

def parse_quantity(qty_str):
    """Parse quantity string to float, handling fractions."""
    if not qty_str or qty_str.strip() == "":
        return 1.0

    qty_str = qty_str.strip()

    # Handle mixed numbers like "1 1/2"
    parts = qty_str.split()
    total = 0
    for part in parts:
        try:
            if '/' in part:
                total += float(Fraction(part))
            else:
                total += float(part)
        except (ValueError, ZeroDivisionError):
            return 1.0

    return total if total > 0 else 1.0

def normalize_ingredient(item):
    """Normalize ingredient name for lookup."""
    item = item.lower().strip()

    # Remove prep notes in parentheses or after comma
    if "," in item:
        item = item.split(",")[0].strip()

    # Handle "fresh or frozen X" pattern FIRST (before removing prefixes)
    if "fresh or frozen " in item:
        item = item.replace("fresh or frozen ", "")

    # Remove common prefixes
    prefixes = ["fresh ", "frozen ", "dried ", "chopped ", "diced ", "grated ", "mashed ",
                "sliced ", "cooked ", "melted ", "softened ", "ripe ", "peeled ", "pitted ",
                "toasted ", "crushed ", "crumbled ", "sifted ", "packed ", "firmly packed ",
                "lightly packed ", "cubed ", "shredded ", "minced "]
    for prefix in prefixes:
        if item.startswith(prefix):
            item = item[len(prefix):]

    # Common substitutions
    substitutions = {
        "all purpose flour": "all-purpose flour",
        "cake flour": "all-purpose flour",  # close enough nutritionally
        "whole wheat pastry flour": "whole wheat flour",
        "whole wheat flour": "whole wheat flour",
        "old fashioned oats": "old-fashioned oats",
        "rolled oats": "old-fashioned oats",
        "quick cooking oats": "quick oats",
        "skim milk": "milk",  # slightly less cal but close
        "low fat milk": "milk",
        "whole milk": "milk",
        "nonfat milk": "milk",
        "2% milk": "milk",
        "beaten egg": "large egg",
        "egg": "large egg",
        "eggs": "large egg",
        "large eggs": "large egg",
        "ripe bananas": "banana",
        "bananas": "banana",
        "granny smith apples": "apple",
        "granny smith apple": "apple",
        "apples": "apple",
        "green apple": "apple",
        "baking cocoa": "unsweetened cocoa powder",
        "unsweetened baking cocoa": "unsweetened cocoa powder",
        "dark chocolate chips": "chocolate chips",
        "semi-sweet chocolate chips": "chocolate chips",
        "mint chocolate chips": "chocolate chips",
        "california raisins": "raisins",
        "golden raisins": "raisins",
        "pure vanilla extract": "vanilla extract",
        "vanilla": "vanilla extract",
        "pure peppermint extract": "peppermint extract",
        "pure almond extract": "almond extract",
        "sharp cheddar cheese": "cheddar cheese",
        "cheddar cheese": "shredded cheddar cheese",
        "ground cinnamon": "cinnamon",
        "ground nutmeg": "nutmeg",
        "ground ginger": "ginger",
        "ground cloves": "cloves",
        "ground allspice": "allspice",
        "white sugar": "sugar",
        "white granulated sugar": "sugar",
        "granulated sugar": "sugar",
        "dark brown sugar": "brown sugar",
        "light brown sugar": "brown sugar",
        "canola oil": "vegetable oil",
        "corn oil": "vegetable oil",
        "cooking oil": "vegetable oil",
        "creamy peanut butter": "peanut butter",
        "smooth peanut butter": "peanut butter",
        "crunchy peanut butter": "peanut butter",
        "lemon": "lemon juice",  # assuming juice/zest use
        "lemons": "lemon juice",
        "orange": "orange juice",
        "oranges": "orange juice",
        "blueberries": "blueberries",
        "raspberries": "raspberries",
        "strawberries": "strawberries",
        "carrots": "grated carrot",
        "carrot": "grated carrot",
        "vanilla yogurt": "yogurt",
        "nonfat vanilla yogurt": "greek yogurt",
        "non fat vanilla yogurt": "greek yogurt",
        "vanilla non-fat yogurt": "greek yogurt",
        "plain yogurt": "yogurt",
        "corn meal": "cornmeal",
        "canned corn": "corn",
        "pure maple syrup": "maple syrup",
        "russet potatoes": "russet potatoes",
        "fresh ginger": "ginger",
        "butter or shortening": "butter",
        "unsalted butter": "butter",
        "salted butter": "butter",
        "cold butter": "butter",
        "fresh or frozen blueberries": "blueberries",
        "frozen blueberries": "blueberries",
        "unsweetened applesauce": "applesauce",
        "baking cocoa": "cocoa powder",
        "unsweetened baking cocoa": "cocoa powder",
        "cream cheese": "cream cheese",
        "fully cooked ham": "ham",
        "cooked ham": "ham",
        "truvia natural sweetener spoonable": "truvia",
        "truvia natural sweetener": "truvia",
    }

    # Handle "X, peeled" pattern (already handled above in comma split)
    # This catches cases where comma wasn't split
    if ", peeled" in item:
        item = item.replace(", peeled", "")

    if item in substitutions:
        item = substitutions[item]

    return item

def get_nutrition_for_ingredient(ingredient):
    """Calculate nutrition for a single ingredient."""
    item = normalize_ingredient(ingredient.get("item", ""))
    quantity = parse_quantity(ingredient.get("quantity", "1"))
    unit = ingredient.get("unit", "").lower().strip()

    # Normalize unit (handle plurals)
    unit_map = {
        "cups": "cup",
        "tablespoons": "tbsp",
        "tablespoon": "tbsp",
        "teaspoons": "tsp",
        "teaspoon": "tsp",
        "ounces": "oz",
        "ounce": "oz",
        "slices": "slice",
        "links": "link",
    }
    unit = unit_map.get(unit, unit)

    # Try exact match first
    if item in NUTRITION_DB:
        db_entry = NUTRITION_DB[item]
        if unit in db_entry:
            base = db_entry[unit]
            return {k: v * quantity for k, v in base.items()}
        elif "" in db_entry:  # Unit-less items like eggs
            base = db_entry[""]
            return {k: v * quantity for k, v in base.items()}

    # Try with original item name (before normalization)
    orig_item = ingredient.get("item", "").lower().strip()
    if orig_item in NUTRITION_DB:
        db_entry = NUTRITION_DB[orig_item]
        if unit in db_entry:
            base = db_entry[unit]
            return {k: v * quantity for k, v in base.items()}

    # Handle unit conversions
    if unit == "tbsp" and item in NUTRITION_DB and "cup" in NUTRITION_DB[item]:
        base = NUTRITION_DB[item]["cup"]
        return {k: v * quantity / 16 for k, v in base.items()}
    elif unit == "tsp" and item in NUTRITION_DB and "cup" in NUTRITION_DB[item]:
        base = NUTRITION_DB[item]["cup"]
        return {k: v * quantity / 48 for k, v in base.items()}
    elif unit == "tsp" and item in NUTRITION_DB and "tbsp" in NUTRITION_DB[item]:
        base = NUTRITION_DB[item]["tbsp"]
        return {k: v * quantity / 3 for k, v in base.items()}

    # Return None if ingredient not found
    return None

def calculate_recipe_nutrition(recipe):
    """Calculate total nutrition for a recipe."""
    ingredients = recipe.get("ingredients", [])
    servings_str = recipe.get("servings_yield", "12 muffins")

    # Parse servings (default to 12 for muffins)
    servings = 12
    match = re.search(r'(\d+)', servings_str)
    if match:
        servings = int(match.group(1))

    total = {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}
    missing = []

    for ing in ingredients:
        nutr = get_nutrition_for_ingredient(ing)
        if nutr:
            for key in total:
                total[key] += nutr.get(key, 0)
        else:
            missing.append(f"{ing.get('quantity', '')} {ing.get('unit', '')} {ing.get('item', '')}".strip())

    # Calculate per-serving
    per_serving = {
        "calories": round(total["cal"] / servings),
        "fat_g": round(total["fat"] / servings, 1),
        "carbs_g": round(total["carbs"] / servings, 1),
        "protein_g": round(total["protein"] / servings, 1),
        "sodium_mg": round(total["sodium"] / servings),
        "fiber_g": round(total["fiber"] / servings, 1),
        "sugar_g": round(total["sugar"] / servings, 1)
    }

    # Determine status
    if not missing:
        status = "complete"
    elif len(missing) <= 2:
        status = "partial"
    else:
        status = "partial"

    return {
        "status": status,
        "per_serving": per_serving,
        "missing_inputs": missing,
        "assumptions": [
            "Whole milk used where milk type unspecified",
            "Unsalted butter used",
            f"Servings calculated as {servings} based on recipe yield"
        ]
    }

def main():
    # Load recipes
    recipes_path = Path(__file__).parent.parent / "all" / "recipes_master.json"
    with open(recipes_path, 'r') as f:
        data = json.load(f)

    # Find muffin recipes
    updated = 0
    for recipe in data["recipes"]:
        if recipe.get("collection") == "reference":
            tags = recipe.get("tags", [])
            if tags and "muffins" in tags:
                # Check if already has complete nutrition
                existing = recipe.get("nutrition", {})
                if existing.get("status") == "complete" and existing.get("per_serving", {}).get("calories"):
                    continue

                # Calculate nutrition
                nutrition = calculate_recipe_nutrition(recipe)
                recipe["nutrition"] = nutrition
                updated += 1
                print(f"Updated: {recipe['title']} - {nutrition['per_serving']['calories']} cal/serving")

    # Save updated recipes
    with open(recipes_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nTotal updated: {updated} muffin recipes")

if __name__ == "__main__":
    main()
