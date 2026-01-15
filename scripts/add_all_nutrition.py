#!/usr/bin/env python3
"""
Add nutrition data to ALL recipes lacking it.
Expands on add_muffin_nutrition.py with comprehensive ingredient database.
"""

import json
import re
import glob
from fractions import Fraction
from pathlib import Path

# =============================================================================
# COMPREHENSIVE NUTRITION DATABASE (USDA values)
# Format: {ingredient: {unit: {cal, fat, carbs, protein, sodium, fiber, sugar}}}
# =============================================================================

NUTRITION_DB = {
    # =========================================================================
    # WATER & LIQUIDS (0 or minimal calories)
    # =========================================================================
    "water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
              "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "ice": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # FLOURS & STARCHES
    # =========================================================================
    "all-purpose flour": {"cup": {"cal": 455, "fat": 1.2, "carbs": 95, "protein": 13, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
                         "tbsp": {"cal": 28, "fat": 0.1, "carbs": 6, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "flour": {"cup": {"cal": 455, "fat": 1.2, "carbs": 95, "protein": 13, "sodium": 2, "fiber": 3.4, "sugar": 0.3},
             "tbsp": {"cal": 28, "fat": 0.1, "carbs": 6, "protein": 0.8, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "whole wheat flour": {"cup": {"cal": 408, "fat": 2.2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0.4}},
    "bread flour": {"cup": {"cal": 495, "fat": 1.5, "carbs": 99, "protein": 16, "sodium": 2, "fiber": 3.4, "sugar": 0.3}},
    "cake flour": {"cup": {"cal": 400, "fat": 1, "carbs": 88, "protein": 9, "sodium": 2, "fiber": 2, "sugar": 0.3}},
    "self-rising flour": {"cup": {"cal": 443, "fat": 1.2, "carbs": 93, "protein": 12, "sodium": 1520, "fiber": 3, "sugar": 0.3}},
    "almond flour": {"cup": {"cal": 640, "fat": 56, "carbs": 24, "protein": 24, "sodium": 0, "fiber": 12, "sugar": 4}},
    "coconut flour": {"cup": {"cal": 480, "fat": 16, "carbs": 64, "protein": 16, "sodium": 64, "fiber": 40, "sugar": 8}},
    "cornstarch": {"cup": {"cal": 488, "fat": 0.1, "carbs": 117, "protein": 0.3, "sodium": 12, "fiber": 1, "sugar": 0},
                  "tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "tapioca": {"cup": {"cal": 544, "fat": 0, "carbs": 135, "protein": 0, "sodium": 2, "fiber": 1, "sugar": 5},
               "tbsp": {"cal": 34, "fat": 0, "carbs": 8, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 43, "fiber": 9, "sugar": 1}},
    "masa harina": {"cup": {"cal": 416, "fat": 4, "carbs": 87, "protein": 11, "sodium": 6, "fiber": 7, "sugar": 1}},
    "chickpea flour": {"cup": {"cal": 356, "fat": 6, "carbs": 53, "protein": 21, "sodium": 59, "fiber": 10, "sugar": 10},
                      "oz": {"cal": 100, "fat": 1.7, "carbs": 15, "protein": 6, "sodium": 17, "fiber": 3, "sugar": 3}},
    "garbanzo bean flour": {"cup": {"cal": 356, "fat": 6, "carbs": 53, "protein": 21, "sodium": 59, "fiber": 10, "sugar": 10}},
    "semolina": {"cup": {"cal": 601, "fat": 1.8, "carbs": 122, "protein": 21, "sodium": 2, "fiber": 6.5, "sugar": 0},
                "oz": {"cal": 106, "fat": 0.3, "carbs": 22, "protein": 4, "sodium": 0, "fiber": 1, "sugar": 0}},
    "semolina flour": {"cup": {"cal": 601, "fat": 1.8, "carbs": 122, "protein": 21, "sodium": 2, "fiber": 6.5, "sugar": 0}},
    "rye flour": {"cup": {"cal": 361, "fat": 2, "carbs": 75, "protein": 11, "sodium": 2, "fiber": 15, "sugar": 1}},
    "whole wheat flour": {"cup": {"cal": 408, "fat": 2.2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0.4},
                         "oz": {"cal": 96, "fat": 0.5, "carbs": 20, "protein": 4, "sodium": 1, "fiber": 3.5, "sugar": 0.1}},

    # =========================================================================
    # SUGARS & SWEETENERS
    # =========================================================================
    "sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200},
             "tbsp": {"cal": 48, "fat": 0, "carbs": 12.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 12.5},
             "tsp": {"cal": 16, "fat": 0, "carbs": 4, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 4}},
    "brown sugar": {"cup": {"cal": 836, "fat": 0, "carbs": 216, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 213},
                   "tbsp": {"cal": 52, "fat": 0, "carbs": 13.5, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 13}},
    "powdered sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 120, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117},
                       "tbsp": {"cal": 29, "fat": 0, "carbs": 7.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7.3},
                       "": {"cal": 29, "fat": 0, "carbs": 7.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7.3}},
    "honey": {"cup": {"cal": 1031, "fat": 0, "carbs": 279, "protein": 1, "sodium": 14, "fiber": 0, "sugar": 278},
             "tbsp": {"cal": 64, "fat": 0, "carbs": 17, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 17}},
    "maple syrup": {"cup": {"cal": 840, "fat": 0.2, "carbs": 216, "protein": 0, "sodium": 27, "fiber": 0, "sugar": 192},
                   "tbsp": {"cal": 52, "fat": 0, "carbs": 13, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 12}},
    "molasses": {"cup": {"cal": 977, "fat": 0, "carbs": 252, "protein": 0, "sodium": 121, "fiber": 0, "sugar": 183},
                "tbsp": {"cal": 58, "fat": 0, "carbs": 15, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 11}},
    "corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 395, "fiber": 0, "sugar": 155},
                  "tbsp": {"cal": 57, "fat": 0, "carbs": 15.5, "protein": 0, "sodium": 24, "fiber": 0, "sugar": 9.5}},
    "agave": {"tbsp": {"cal": 60, "fat": 0, "carbs": 16, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 15}},
    "stevia": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "splenda": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # DAIRY
    # =========================================================================
    "milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12},
            "tbsp": {"cal": 9, "fat": 0.5, "carbs": 0.75, "protein": 0.5, "sodium": 7, "fiber": 0, "sugar": 0.75},
            "pint": {"cal": 298, "fat": 16, "carbs": 24, "protein": 16, "sodium": 210, "fiber": 0, "sugar": 24},
            "quart": {"cal": 596, "fat": 32, "carbs": 48, "protein": 32, "sodium": 420, "fiber": 0, "sugar": 48},
            "ml": {"cal": 0.63, "fat": 0.03, "carbs": 0.05, "protein": 0.03, "sodium": 0.44, "fiber": 0, "sugar": 0.05}},
    "skim milk": {"cup": {"cal": 83, "fat": 0.2, "carbs": 12, "protein": 8, "sodium": 103, "fiber": 0, "sugar": 12}},
    "evaporated milk": {"cup": {"cal": 338, "fat": 19, "carbs": 25, "protein": 17, "sodium": 267, "fiber": 0, "sugar": 25}},
    "sweetened condensed milk": {"cup": {"cal": 982, "fat": 27, "carbs": 166, "protein": 24, "sodium": 389, "fiber": 0, "sugar": 166}},
    "buttermilk": {"cup": {"cal": 99, "fat": 2.2, "carbs": 12, "protein": 8, "sodium": 257, "fiber": 0, "sugar": 12}},
    "heavy cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7},
                   "tbsp": {"cal": 51, "fat": 5.5, "carbs": 0.4, "protein": 0.3, "sodium": 6, "fiber": 0, "sugar": 0.4}},
    "half and half": {"cup": {"cal": 315, "fat": 28, "carbs": 10, "protein": 7, "sodium": 98, "fiber": 0, "sugar": 10},
                     "tbsp": {"cal": 20, "fat": 1.7, "carbs": 0.6, "protein": 0.4, "sodium": 6, "fiber": 0, "sugar": 0.6}},
    "sour cream": {"cup": {"cal": 444, "fat": 45, "carbs": 8, "protein": 5, "sodium": 108, "fiber": 0, "sugar": 5},
                  "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.5, "protein": 0.3, "sodium": 7, "fiber": 0, "sugar": 0.3}},
    "cream cheese": {"cup": {"cal": 793, "fat": 79, "carbs": 8, "protein": 14, "sodium": 691, "fiber": 0, "sugar": 6},
                    "oz": {"cal": 99, "fat": 10, "carbs": 1, "protein": 2, "sodium": 86, "fiber": 0, "sugar": 0.8},
                    "tbsp": {"cal": 50, "fat": 5, "carbs": 0.5, "protein": 1, "sodium": 43, "fiber": 0, "sugar": 0.4}},
    "yogurt": {"cup": {"cal": 149, "fat": 8, "carbs": 11, "protein": 9, "sodium": 113, "fiber": 0, "sugar": 11}},
    "greek yogurt": {"cup": {"cal": 190, "fat": 10, "carbs": 8, "protein": 18, "sodium": 65, "fiber": 0, "sugar": 7}},
    "cottage cheese": {"cup": {"cal": 220, "fat": 10, "carbs": 8, "protein": 25, "sodium": 819, "fiber": 0, "sugar": 5}},
    "ricotta cheese": {"cup": {"cal": 428, "fat": 32, "carbs": 7, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.5}},
    "cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1, "protein": 28, "sodium": 702, "fiber": 0, "sugar": 0.5},
                      "oz": {"cal": 113, "fat": 9, "carbs": 0.3, "protein": 7, "sodium": 175, "fiber": 0, "sugar": 0.1}},
    "parmesan cheese": {"cup": {"cal": 431, "fat": 29, "carbs": 4, "protein": 38, "sodium": 1529, "fiber": 0, "sugar": 1},
                       "tbsp": {"cal": 22, "fat": 1.4, "carbs": 0.2, "protein": 2, "sodium": 76, "fiber": 0, "sugar": 0}},
    "mozzarella cheese": {"cup": {"cal": 336, "fat": 25, "carbs": 2, "protein": 25, "sodium": 627, "fiber": 0, "sugar": 1},
                         "oz": {"cal": 84, "fat": 6, "carbs": 0.6, "protein": 6, "sodium": 157, "fiber": 0, "sugar": 0.2}},
    "swiss cheese": {"cup": {"cal": 420, "fat": 31, "carbs": 6, "protein": 30, "sodium": 228, "fiber": 0, "sugar": 2},
                    "oz": {"cal": 106, "fat": 8, "carbs": 1.5, "protein": 8, "sodium": 54, "fiber": 0, "sugar": 0.4}},
    "american cheese": {"slice": {"cal": 94, "fat": 7, "carbs": 2, "protein": 5, "sodium": 274, "fiber": 0, "sugar": 1}},
    "velveeta": {"oz": {"cal": 80, "fat": 6, "carbs": 3, "protein": 4, "sodium": 410, "fiber": 0, "sugar": 2}},
    "whipped cream": {"cup": {"cal": 240, "fat": 22, "carbs": 7, "protein": 3, "sodium": 60, "fiber": 0, "sugar": 7},
                     "tbsp": {"cal": 15, "fat": 1.4, "carbs": 0.4, "protein": 0.2, "sodium": 4, "fiber": 0, "sugar": 0.4}},

    # =========================================================================
    # FATS & OILS
    # =========================================================================
    "butter": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 1246, "fiber": 0, "sugar": 0},
              "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0},
              "tsp": {"cal": 34, "fat": 4, "carbs": 0, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 0},
              "": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0}},
    "margarine": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0},
                  "stick": {"cal": 810, "fat": 91, "carbs": 1, "protein": 1, "sodium": 800, "fiber": 0, "sugar": 0},
                  "": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "oleo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0},
             "stick": {"cal": 810, "fat": 91, "carbs": 1, "protein": 1, "sodium": 800, "fiber": 0, "sugar": 0},
             "": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "vegetable oil": {"cup": {"cal": 1927, "fat": 218, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "olive oil": {"cup": {"cal": 1909, "fat": 216, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                 "tbsp": {"cal": 119, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coconut oil": {"tbsp": {"cal": 117, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "shortening": {"cup": {"cal": 1812, "fat": 205, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                  "tbsp": {"cal": 113, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lard": {"cup": {"cal": 1849, "fat": 205, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "mayonnaise": {"cup": {"cal": 1440, "fat": 160, "carbs": 0, "protein": 2, "sodium": 1250, "fiber": 0, "sugar": 0},
                  "tbsp": {"cal": 90, "fat": 10, "carbs": 0, "protein": 0.1, "sodium": 78, "fiber": 0, "sugar": 0}},
    "bacon grease": {"tbsp": {"cal": 116, "fat": 13, "carbs": 0, "protein": 0, "sodium": 19, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # EGGS
    # =========================================================================
    "egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "large egg": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "eggs": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg white": {"": {"cal": 17, "fat": 0, "carbs": 0.2, "protein": 4, "sodium": 55, "fiber": 0, "sugar": 0.2}},
    "egg yolk": {"": {"cal": 55, "fat": 5, "carbs": 0.6, "protein": 3, "sodium": 8, "fiber": 0, "sugar": 0.1}},

    # =========================================================================
    # MEATS - POULTRY
    # =========================================================================
    "chicken breast": {"lb": {"cal": 748, "fat": 16, "carbs": 0, "protein": 140, "sodium": 340, "fiber": 0, "sugar": 0},
                      "": {"cal": 187, "fat": 4, "carbs": 0, "protein": 35, "sodium": 85, "fiber": 0, "sugar": 0}},
    "chicken thigh": {"lb": {"cal": 980, "fat": 54, "carbs": 0, "protein": 115, "sodium": 422, "fiber": 0, "sugar": 0},
                     "": {"cal": 206, "fat": 11, "carbs": 0, "protein": 24, "sodium": 88, "fiber": 0, "sugar": 0}},
    "chicken": {"lb": {"cal": 880, "fat": 40, "carbs": 0, "protein": 120, "sodium": 380, "fiber": 0, "sugar": 0},
               "cup": {"cal": 231, "fat": 10, "carbs": 0, "protein": 32, "sodium": 100, "fiber": 0, "sugar": 0}},
    "ground chicken": {"lb": {"cal": 748, "fat": 36, "carbs": 0, "protein": 100, "sodium": 340, "fiber": 0, "sugar": 0}},
    "turkey": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 104, "sodium": 300, "fiber": 0, "sugar": 0},
              "cup": {"cal": 190, "fat": 8, "carbs": 0, "protein": 27, "sodium": 79, "fiber": 0, "sugar": 0}},
    "ground turkey": {"lb": {"cal": 752, "fat": 36, "carbs": 0, "protein": 100, "sodium": 340, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # MEATS - BEEF
    # =========================================================================
    "ground beef": {"lb": {"cal": 1152, "fat": 88, "carbs": 0, "protein": 80, "sodium": 304, "fiber": 0, "sugar": 0}},
    "lean ground beef": {"lb": {"cal": 816, "fat": 48, "carbs": 0, "protein": 92, "sodium": 320, "fiber": 0, "sugar": 0}},
    "beef": {"lb": {"cal": 1000, "fat": 68, "carbs": 0, "protein": 92, "sodium": 280, "fiber": 0, "sugar": 0},
            "cup": {"cal": 263, "fat": 18, "carbs": 0, "protein": 24, "sodium": 74, "fiber": 0, "sugar": 0}},
    "steak": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0},
             "oz": {"cal": 55, "fat": 3.3, "carbs": 0, "protein": 6, "sodium": 16, "fiber": 0, "sugar": 0}},
    "roast beef": {"lb": {"cal": 800, "fat": 40, "carbs": 0, "protein": 108, "sodium": 272, "fiber": 0, "sugar": 0}},
    "beef stew meat": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 108, "sodium": 280, "fiber": 0, "sugar": 0}},
    "corned beef": {"lb": {"cal": 880, "fat": 56, "carbs": 2, "protein": 88, "sodium": 3840, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # MEATS - PORK
    # =========================================================================
    "pork": {"lb": {"cal": 1016, "fat": 60, "carbs": 0, "protein": 112, "sodium": 260, "fiber": 0, "sugar": 0}},
    "pork chop": {"": {"cal": 231, "fat": 13, "carbs": 0, "protein": 26, "sodium": 62, "fiber": 0, "sugar": 0}},
    "pork loin": {"lb": {"cal": 680, "fat": 24, "carbs": 0, "protein": 116, "sodium": 280, "fiber": 0, "sugar": 0}},
    "pork tenderloin": {"lb": {"cal": 544, "fat": 12, "carbs": 0, "protein": 104, "sodium": 240, "fiber": 0, "sugar": 0}},
    "bacon": {"slice": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "strip": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "strips": {"cal": 43, "fat": 3, "carbs": 0, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0},
             "lb": {"cal": 2420, "fat": 232, "carbs": 0, "protein": 60, "sodium": 3040, "fiber": 0, "sugar": 0}},
    "ham": {"cup": {"cal": 207, "fat": 11, "carbs": 2, "protein": 24, "sodium": 1684, "fiber": 0, "sugar": 0},
           "lb": {"cal": 620, "fat": 32, "carbs": 4, "protein": 80, "sodium": 5050, "fiber": 0, "sugar": 0}},
    "sausage": {"link": {"cal": 82, "fat": 7, "carbs": 0.5, "protein": 4, "sodium": 192, "fiber": 0, "sugar": 0},
               "lb": {"cal": 1148, "fat": 100, "carbs": 4, "protein": 56, "sodium": 2840, "fiber": 0, "sugar": 0}},
    "italian sausage": {"link": {"cal": 125, "fat": 10, "carbs": 1, "protein": 8, "sodium": 380, "fiber": 0, "sugar": 0}},
    "ground pork": {"lb": {"cal": 1200, "fat": 92, "carbs": 0, "protein": 80, "sodium": 280, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # SEAFOOD
    # =========================================================================
    "shrimp": {"lb": {"cal": 480, "fat": 8, "carbs": 4, "protein": 92, "sodium": 800, "fiber": 0, "sugar": 0},
              "cup": {"cal": 120, "fat": 2, "carbs": 1, "protein": 23, "sodium": 200, "fiber": 0, "sugar": 0}},
    "salmon": {"lb": {"cal": 936, "fat": 56, "carbs": 0, "protein": 104, "sodium": 260, "fiber": 0, "sugar": 0},
              "oz": {"cal": 59, "fat": 3.5, "carbs": 0, "protein": 6.5, "sodium": 16, "fiber": 0, "sugar": 0}},
    "trout": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 104, "sodium": 260, "fiber": 0, "sugar": 0},
              "oz": {"cal": 43, "fat": 1.8, "carbs": 0, "protein": 6.5, "sodium": 16, "fiber": 0, "sugar": 0},
              "fillet": {"cal": 215, "fat": 9, "carbs": 0, "protein": 33, "sodium": 81, "fiber": 0, "sugar": 0},
              "fillets": {"cal": 215, "fat": 9, "carbs": 0, "protein": 33, "sodium": 81, "fiber": 0, "sugar": 0}},
    "tuna": {"can": {"cal": 179, "fat": 1, "carbs": 0, "protein": 40, "sodium": 558, "fiber": 0, "sugar": 0},
            "cup": {"cal": 179, "fat": 1, "carbs": 0, "protein": 40, "sodium": 558, "fiber": 0, "sugar": 0}},
    "cod": {"lb": {"cal": 372, "fat": 4, "carbs": 0, "protein": 80, "sodium": 280, "fiber": 0, "sugar": 0}},
    "tilapia": {"lb": {"cal": 436, "fat": 8, "carbs": 0, "protein": 92, "sodium": 232, "fiber": 0, "sugar": 0}},
    "crab": {"cup": {"cal": 97, "fat": 2, "carbs": 0, "protein": 19, "sodium": 911, "fiber": 0, "sugar": 0}},
    "crabmeat": {"oz": {"cal": 25, "fat": 0.4, "carbs": 0, "protein": 5, "sodium": 95, "fiber": 0, "sugar": 0}},
    "clams": {"cup": {"cal": 168, "fat": 2, "carbs": 6, "protein": 29, "sodium": 127, "fiber": 0, "sugar": 0}},
    "lobster": {"cup": {"cal": 142, "fat": 1, "carbs": 2, "protein": 30, "sodium": 705, "fiber": 0, "sugar": 0}},
    "anchovies": {"can": {"cal": 94, "fat": 4, "carbs": 0, "protein": 13, "sodium": 1651, "fiber": 0, "sugar": 0}},
    "swordfish": {"oz": {"cal": 41, "fat": 1.4, "carbs": 0, "protein": 6.7, "sodium": 30, "fiber": 0, "sugar": 0}},
    "red snapper": {"oz": {"cal": 28, "fat": 0.4, "carbs": 0, "protein": 5.8, "sodium": 18, "fiber": 0, "sugar": 0}},
    "cornish hen": {"": {"cal": 500, "fat": 28, "carbs": 0, "protein": 60, "sodium": 200, "fiber": 0, "sugar": 0}},
    "corned beef": {"oz": {"cal": 71, "fat": 5.4, "carbs": 0.4, "protein": 5, "sodium": 285, "fiber": 0, "sugar": 0}},
    "sirloin": {"lb": {"cal": 880, "fat": 48, "carbs": 0, "protein": 104, "sodium": 280, "fiber": 0, "sugar": 0}},
    "round steak": {"lb": {"cal": 720, "fat": 24, "carbs": 0, "protein": 120, "sodium": 240, "fiber": 0, "sugar": 0}},
    "pot roast": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 280, "fiber": 0, "sugar": 0}},
    "stew meat": {"lb": {"cal": 880, "fat": 52, "carbs": 0, "protein": 100, "sodium": 280, "fiber": 0, "sugar": 0}},
    "salami": {"oz": {"cal": 119, "fat": 10, "carbs": 0.5, "protein": 6, "sodium": 529, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # CANNED GOODS & PREPARED FOODS
    # =========================================================================
    "cream of chicken soup": {"can": {"cal": 225, "fat": 14, "carbs": 18, "protein": 6, "sodium": 1800, "fiber": 0, "sugar": 2}},
    "cream of mushroom soup": {"can": {"cal": 200, "fat": 13, "carbs": 15, "protein": 4, "sodium": 1700, "fiber": 1, "sugar": 2}},
    "cream of celery soup": {"can": {"cal": 180, "fat": 11, "carbs": 17, "protein": 3, "sodium": 1650, "fiber": 1, "sugar": 2}},
    "tomato soup": {"can": {"cal": 161, "fat": 4, "carbs": 28, "protein": 4, "sodium": 1410, "fiber": 3, "sugar": 19}},
    "chicken broth": {"cup": {"cal": 15, "fat": 0.5, "carbs": 1, "protein": 2, "sodium": 860, "fiber": 0, "sugar": 0},
                     "can": {"cal": 30, "fat": 1, "carbs": 2, "protein": 4, "sodium": 1720, "fiber": 0, "sugar": 0}},
    "beef broth": {"cup": {"cal": 17, "fat": 0.5, "carbs": 1, "protein": 3, "sodium": 890, "fiber": 0, "sugar": 0},
                  "can": {"cal": 34, "fat": 1, "carbs": 2, "protein": 6, "sodium": 1780, "fiber": 0, "sugar": 0}},
    "vegetable broth": {"cup": {"cal": 12, "fat": 0, "carbs": 3, "protein": 0, "sodium": 700, "fiber": 0, "sugar": 1}},
    "bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "chicken bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "beef bouillon cube": {"": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "bouillon": {"cube": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},
    "tomato paste": {"can": {"cal": 139, "fat": 1, "carbs": 32, "protein": 7, "sodium": 170, "fiber": 7, "sugar": 21},
                    "tbsp": {"cal": 13, "fat": 0.1, "carbs": 3, "protein": 0.7, "sodium": 16, "fiber": 0.7, "sugar": 2}},
    "tomato sauce": {"cup": {"cal": 59, "fat": 0.4, "carbs": 13, "protein": 3, "sodium": 1116, "fiber": 4, "sugar": 8},
                    "can": {"cal": 89, "fat": 0.6, "carbs": 20, "protein": 4, "sodium": 1674, "fiber": 6, "sugar": 12}},
    "diced tomatoes": {"can": {"cal": 66, "fat": 0.4, "carbs": 16, "protein": 3, "sodium": 564, "fiber": 4, "sugar": 9}},
    "crushed tomatoes": {"can": {"cal": 70, "fat": 0.5, "carbs": 16, "protein": 3, "sodium": 600, "fiber": 4, "sugar": 10}},
    "canned tomatoes": {"can": {"cal": 66, "fat": 0.4, "carbs": 16, "protein": 3, "sodium": 564, "fiber": 4, "sugar": 9}},
    "salsa": {"cup": {"cal": 70, "fat": 0.3, "carbs": 15, "protein": 3, "sodium": 1990, "fiber": 4, "sugar": 8}},
    "enchilada sauce": {"cup": {"cal": 60, "fat": 1, "carbs": 11, "protein": 2, "sodium": 1160, "fiber": 2, "sugar": 4}},
    "black beans": {"can": {"cal": 339, "fat": 1, "carbs": 61, "protein": 22, "sodium": 660, "fiber": 15, "sugar": 1},
                   "cup": {"cal": 227, "fat": 0.9, "carbs": 41, "protein": 15, "sodium": 440, "fiber": 10, "sugar": 0.5}},
    "kidney beans": {"can": {"cal": 330, "fat": 1, "carbs": 58, "protein": 23, "sodium": 880, "fiber": 16, "sugar": 3}},
    "pinto beans": {"can": {"cal": 320, "fat": 1, "carbs": 56, "protein": 20, "sodium": 620, "fiber": 15, "sugar": 1}},
    "refried beans": {"cup": {"cal": 237, "fat": 3, "carbs": 39, "protein": 14, "sodium": 1069, "fiber": 11, "sugar": 1}},
    "baked beans": {"cup": {"cal": 266, "fat": 1, "carbs": 52, "protein": 12, "sodium": 928, "fiber": 10, "sugar": 22}},
    "green beans": {"can": {"cal": 44, "fat": 0.3, "carbs": 10, "protein": 2, "sodium": 620, "fiber": 4, "sugar": 2},
                   "cup": {"cal": 31, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 6, "fiber": 3, "sugar": 3}},
    "corn": {"can": {"cal": 210, "fat": 2, "carbs": 50, "protein": 6, "sodium": 600, "fiber": 4, "sugar": 12},
            "cup": {"cal": 132, "fat": 2, "carbs": 29, "protein": 5, "sodium": 1, "fiber": 4, "sugar": 5}},
    "peas": {"cup": {"cal": 117, "fat": 0.6, "carbs": 21, "protein": 8, "sodium": 7, "fiber": 7, "sugar": 8},
            "can": {"cal": 175, "fat": 0.9, "carbs": 31, "protein": 12, "sodium": 800, "fiber": 10, "sugar": 12}},
    "mushrooms": {"can": {"cal": 39, "fat": 0.5, "carbs": 8, "protein": 3, "sodium": 660, "fiber": 4, "sugar": 2},
                 "cup": {"cal": 15, "fat": 0.2, "carbs": 2, "protein": 2, "sodium": 4, "fiber": 0.7, "sugar": 1}},
    "olives": {"cup": {"cal": 155, "fat": 14, "carbs": 8, "protein": 1, "sodium": 1556, "fiber": 3, "sugar": 0}},
    "coconut milk": {"cup": {"cal": 445, "fat": 48, "carbs": 6, "protein": 5, "sodium": 29, "fiber": 0, "sugar": 6}},
    "pumpkin puree": {"cup": {"cal": 83, "fat": 0.7, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 7, "sugar": 8}},
    "green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3},
                    "cup": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},
    "diced green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},
    "chopped green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 400, "fiber": 2, "sugar": 3}},

    # =========================================================================
    # VEGETABLES
    # =========================================================================
    "onion": {"cup": {"cal": 64, "fat": 0.2, "carbs": 15, "protein": 2, "sodium": 6, "fiber": 3, "sugar": 7},
             "medium": {"cal": 44, "fat": 0.1, "carbs": 10, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 5},
             "small": {"cal": 28, "fat": 0.1, "carbs": 7, "protein": 0.8, "sodium": 3, "fiber": 1, "sugar": 3},
             "large": {"cal": 60, "fat": 0.2, "carbs": 14, "protein": 1.5, "sodium": 5, "fiber": 2.5, "sugar": 6},
             "": {"cal": 44, "fat": 0.1, "carbs": 10, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 5}},
    "green onion": {"cup": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 16, "fiber": 3, "sugar": 2},
                   "": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.4, "sugar": 0.4}},
    "garlic": {"clove": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "cloves": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "tbsp": {"cal": 13, "fat": 0, "carbs": 3, "protein": 0.6, "sodium": 2, "fiber": 0.2, "sugar": 0},
              "tsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0},
              "": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0}},
    "celery": {"cup": {"cal": 16, "fat": 0.2, "carbs": 3, "protein": 0.7, "sodium": 80, "fiber": 2, "sugar": 1},
              "stalk": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.5}},
    "carrot": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1, "sodium": 88, "fiber": 4, "sugar": 6},
              "medium": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 2, "sugar": 3},
              "": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 2, "sugar": 3}},
    "bell pepper": {"cup": {"cal": 30, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 4},
                   "medium": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3},
                   "": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3}},
    "green pepper": {"cup": {"cal": 30, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 4},
                    "": {"cal": 24, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 3, "fiber": 1.5, "sugar": 3}},
    "red pepper": {"cup": {"cal": 39, "fat": 0.4, "carbs": 9, "protein": 1, "sodium": 5, "fiber": 3, "sugar": 6}},
    "jalapeno": {"": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.5}},
    "tomato": {"cup": {"cal": 32, "fat": 0.4, "carbs": 7, "protein": 2, "sodium": 9, "fiber": 2, "sugar": 5},
              "medium": {"cal": 22, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 6, "fiber": 1.5, "sugar": 3},
              "": {"cal": 22, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 6, "fiber": 1.5, "sugar": 3}},
    "potato": {"medium": {"cal": 163, "fat": 0.2, "carbs": 37, "protein": 4, "sodium": 13, "fiber": 4, "sugar": 2},
              "cup": {"cal": 116, "fat": 0.1, "carbs": 26, "protein": 3, "sodium": 9, "fiber": 3, "sugar": 1},
              "lb": {"cal": 354, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 28, "fiber": 9, "sugar": 4},
              "": {"cal": 163, "fat": 0.2, "carbs": 37, "protein": 4, "sodium": 13, "fiber": 4, "sugar": 2}},
    "sweet potato": {"cup": {"cal": 114, "fat": 0.1, "carbs": 27, "protein": 2, "sodium": 73, "fiber": 4, "sugar": 6},
                    "medium": {"cal": 103, "fat": 0.1, "carbs": 24, "protein": 2, "sodium": 41, "fiber": 4, "sugar": 7},
                    "": {"cal": 103, "fat": 0.1, "carbs": 24, "protein": 2, "sodium": 41, "fiber": 4, "sugar": 7}},
    "broccoli": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 3, "sodium": 30, "fiber": 2, "sugar": 2}},
    "cauliflower": {"cup": {"cal": 27, "fat": 0.3, "carbs": 5, "protein": 2, "sodium": 32, "fiber": 2, "sugar": 2}},
    "spinach": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 24, "fiber": 0.7, "sugar": 0.1}},
    "lettuce": {"cup": {"cal": 5, "fat": 0.1, "carbs": 1, "protein": 0.5, "sodium": 5, "fiber": 0.5, "sugar": 0.5}},
    "cabbage": {"cup": {"cal": 22, "fat": 0.1, "carbs": 5, "protein": 1, "sodium": 16, "fiber": 2, "sugar": 3}},
    "zucchini": {"cup": {"cal": 19, "fat": 0.2, "carbs": 4, "protein": 1, "sodium": 12, "fiber": 1, "sugar": 3},
                "medium": {"cal": 33, "fat": 0.4, "carbs": 6, "protein": 2, "sodium": 20, "fiber": 2, "sugar": 5}},
    "squash": {"cup": {"cal": 21, "fat": 0.2, "carbs": 5, "protein": 1, "sodium": 2, "fiber": 1, "sugar": 3}},
    "eggplant": {"cup": {"cal": 20, "fat": 0.2, "carbs": 5, "protein": 0.8, "sodium": 2, "fiber": 3, "sugar": 3}},
    "cucumber": {"cup": {"cal": 16, "fat": 0.1, "carbs": 4, "protein": 0.7, "sodium": 2, "fiber": 0.5, "sugar": 2}},
    "asparagus": {"cup": {"cal": 27, "fat": 0.2, "carbs": 5, "protein": 3, "sodium": 3, "fiber": 3, "sugar": 2}},
    "brussels sprouts": {"cup": {"cal": 56, "fat": 0.4, "carbs": 12, "protein": 4, "sodium": 28, "fiber": 4, "sugar": 3}},
    "kale": {"cup": {"cal": 33, "fat": 0.5, "carbs": 6, "protein": 2, "sodium": 25, "fiber": 1, "sugar": 1}},
    "avocado": {"": {"cal": 234, "fat": 21, "carbs": 12, "protein": 3, "sodium": 10, "fiber": 10, "sugar": 1},
               "cup": {"cal": 234, "fat": 21, "carbs": 12, "protein": 3, "sodium": 10, "fiber": 10, "sugar": 1}},
    "artichoke": {"": {"cal": 60, "fat": 0.2, "carbs": 13, "protein": 4, "sodium": 120, "fiber": 7, "sugar": 1}},
    "leek": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3},
             "": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3}},
    "leeks": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3},
              "": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 18, "fiber": 2, "sugar": 3}},
    "parsley": {"cup": {"cal": 22, "fat": 0.5, "carbs": 4, "protein": 2, "sodium": 34, "fiber": 2, "sugar": 0.5},
                "tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "cilantro": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 3, "fiber": 0.2, "sugar": 0},
                 "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "basil": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.2, "sodium": 0, "fiber": 0.1, "sugar": 0},
              "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "chives": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "dill": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "mint": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "rosemary": {"tbsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0, "sodium": 1, "fiber": 0.2, "sugar": 0}},
    "thyme": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "sage": {"tbsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # =========================================================================
    # FRUITS
    # =========================================================================
    "apple": {"cup": {"cal": 65, "fat": 0.2, "carbs": 17, "protein": 0.3, "sodium": 1, "fiber": 3, "sugar": 13},
             "medium": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4, "sugar": 19},
             "": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4, "sugar": 19}},
    "banana": {"": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1, "sodium": 1, "fiber": 3, "sugar": 14},
              "cup": {"cal": 134, "fat": 0.5, "carbs": 34, "protein": 1.6, "sodium": 2, "fiber": 4, "sugar": 18}},
    "orange": {"": {"cal": 62, "fat": 0.2, "carbs": 15, "protein": 1, "sodium": 0, "fiber": 3, "sugar": 12},
              "cup": {"cal": 85, "fat": 0.2, "carbs": 21, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "lemon": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 2, "sugar": 1.5}},
    "lime": {"": {"cal": 20, "fat": 0.1, "carbs": 7, "protein": 0.5, "sodium": 1, "fiber": 2, "sugar": 1}},
    "lemon juice": {"cup": {"cal": 54, "fat": 0.6, "carbs": 17, "protein": 1, "sodium": 4, "fiber": 1, "sugar": 6},
                   "tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.4}},
    "lime juice": {"cup": {"cal": 60, "fat": 0.2, "carbs": 20, "protein": 1, "sodium": 4, "fiber": 1, "sugar": 4},
                  "tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.3}},
    "orange juice": {"cup": {"cal": 112, "fat": 0.5, "carbs": 26, "protein": 2, "sodium": 2, "fiber": 0.5, "sugar": 21}},
    "blueberries": {"cup": {"cal": 84, "fat": 0.5, "carbs": 21, "protein": 1, "sodium": 1, "fiber": 4, "sugar": 15}},
    "strawberries": {"cup": {"cal": 49, "fat": 0.5, "carbs": 12, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 7}},
    "raspberries": {"cup": {"cal": 64, "fat": 0.8, "carbs": 15, "protein": 1.5, "sodium": 1, "fiber": 8, "sugar": 5}},
    "blackberries": {"cup": {"cal": 62, "fat": 0.7, "carbs": 14, "protein": 2, "sodium": 1, "fiber": 8, "sugar": 7}},
    "cranberries": {"cup": {"cal": 46, "fat": 0.1, "carbs": 12, "protein": 0.4, "sodium": 2, "fiber": 5, "sugar": 4}},
    "grapes": {"cup": {"cal": 104, "fat": 0.2, "carbs": 27, "protein": 1, "sodium": 3, "fiber": 1, "sugar": 23}},
    "peach": {"cup": {"cal": 60, "fat": 0.4, "carbs": 14, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 12},
             "": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 13}},
    "pear": {"": {"cal": 102, "fat": 0.2, "carbs": 27, "protein": 0.6, "sodium": 2, "fiber": 6, "sugar": 17}},
    "plum": {"": {"cal": 30, "fat": 0.2, "carbs": 8, "protein": 0.5, "sodium": 0, "fiber": 1, "sugar": 7}},
    "mango": {"cup": {"cal": 99, "fat": 0.6, "carbs": 25, "protein": 1, "sodium": 2, "fiber": 3, "sugar": 23}},
    "pineapple": {"cup": {"cal": 82, "fat": 0.2, "carbs": 22, "protein": 1, "sodium": 2, "fiber": 2, "sugar": 16}},
    "watermelon": {"cup": {"cal": 46, "fat": 0.2, "carbs": 12, "protein": 1, "sodium": 2, "fiber": 0.6, "sugar": 9}},
    "cantaloupe": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1, "sodium": 26, "fiber": 1, "sugar": 12}},
    "cherries": {"cup": {"cal": 97, "fat": 0.3, "carbs": 25, "protein": 2, "sodium": 0, "fiber": 3, "sugar": 20}},
    "raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 5, "sugar": 86}},
    "dates": {"cup": {"cal": 415, "fat": 0.4, "carbs": 110, "protein": 4, "sodium": 3, "fiber": 12, "sugar": 93}},
    "dried cranberries": {"cup": {"cal": 308, "fat": 1, "carbs": 82, "protein": 0.2, "sodium": 3, "fiber": 6, "sugar": 65}},
    "applesauce": {"cup": {"cal": 167, "fat": 0.4, "carbs": 43, "protein": 0.4, "sodium": 5, "fiber": 3, "sugar": 36}},

    # =========================================================================
    # NUTS & SEEDS
    # =========================================================================
    "almonds": {"cup": {"cal": 828, "fat": 72, "carbs": 28, "protein": 30, "sodium": 1, "fiber": 17, "sugar": 6},
               "oz": {"cal": 164, "fat": 14, "carbs": 6, "protein": 6, "sodium": 0, "fiber": 3.5, "sugar": 1}},
    "walnuts": {"cup": {"cal": 765, "fat": 76, "carbs": 16, "protein": 18, "sodium": 2, "fiber": 8, "sugar": 3}},
    "pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "peanuts": {"cup": {"cal": 828, "fat": 72, "carbs": 24, "protein": 38, "sodium": 26, "fiber": 12, "sugar": 6}},
    "peanut butter": {"cup": {"cal": 1517, "fat": 130, "carbs": 50, "protein": 64, "sodium": 1010, "fiber": 12, "sugar": 24},
                     "tbsp": {"cal": 95, "fat": 8, "carbs": 3, "protein": 4, "sodium": 63, "fiber": 0.8, "sugar": 1.5}},
    "cashews": {"cup": {"cal": 786, "fat": 64, "carbs": 44, "protein": 25, "sodium": 22, "fiber": 4, "sugar": 8}},
    "sunflower seeds": {"cup": {"cal": 818, "fat": 71, "carbs": 28, "protein": 29, "sodium": 4, "fiber": 12, "sugar": 4}},
    "pumpkin seeds": {"cup": {"cal": 677, "fat": 55, "carbs": 25, "protein": 34, "sodium": 25, "fiber": 12, "sugar": 2}},
    "sesame seeds": {"cup": {"cal": 825, "fat": 72, "carbs": 34, "protein": 25, "sodium": 16, "fiber": 17, "sugar": 0},
                    "tbsp": {"cal": 52, "fat": 4.5, "carbs": 2, "protein": 1.6, "sodium": 1, "fiber": 1, "sugar": 0}},
    "flax seeds": {"tbsp": {"cal": 37, "fat": 3, "carbs": 2, "protein": 1.3, "sodium": 2, "fiber": 2, "sugar": 0}},
    "chia seeds": {"tbsp": {"cal": 58, "fat": 4, "carbs": 5, "protein": 2, "sodium": 2, "fiber": 4, "sugar": 0}},
    "coconut": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},

    # =========================================================================
    # GRAINS & PASTA
    # =========================================================================
    "rice": {"cup": {"cal": 206, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "brown rice": {"cup": {"cal": 216, "fat": 1.8, "carbs": 45, "protein": 5, "sodium": 10, "fiber": 4, "sugar": 0}},
    "pasta": {"cup": {"cal": 220, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 3, "sugar": 0.8},
             "lb": {"cal": 756, "fat": 4.5, "carbs": 148, "protein": 27, "sodium": 3, "fiber": 10, "sugar": 3}},
    "egg noodles": {"cup": {"cal": 221, "fat": 3.3, "carbs": 40, "protein": 7, "sodium": 8, "fiber": 2, "sugar": 0.5}},
    "oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "instant oatmeal": {"packet": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "packets": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "oz": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "1-oz": {"cal": 100, "fat": 2, "carbs": 19, "protein": 4, "sodium": 75, "fiber": 3, "sugar": 1},
                        "cup": {"cal": 150, "fat": 3, "carbs": 28, "protein": 6, "sodium": 113, "fiber": 4, "sugar": 1}},
    "quinoa": {"cup": {"cal": 222, "fat": 3.6, "carbs": 39, "protein": 8, "sodium": 13, "fiber": 5, "sugar": 2}},
    "couscous": {"cup": {"cal": 176, "fat": 0.3, "carbs": 36, "protein": 6, "sodium": 8, "fiber": 2, "sugar": 0}},
    "breadcrumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 791, "fiber": 5, "sugar": 6}},
    "croutons": {"cup": {"cal": 122, "fat": 2, "carbs": 22, "protein": 4, "sodium": 209, "fiber": 2, "sugar": 2}},

    # =========================================================================
    # BREADS & TORTILLAS
    # =========================================================================
    "bread": {"slice": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 0.6, "sugar": 1.5}},
    "white bread": {"slice": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 0.6, "sugar": 1.5}},
    "whole wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 14, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1.4}},
    "tortilla": {"": {"cal": 94, "fat": 2, "carbs": 16, "protein": 2, "sodium": 191, "fiber": 1, "sugar": 0.4},
                "large": {"cal": 140, "fat": 3.5, "carbs": 24, "protein": 4, "sodium": 290, "fiber": 1.5, "sugar": 0.6}},
    "flour tortilla": {"": {"cal": 94, "fat": 2, "carbs": 16, "protein": 2, "sodium": 191, "fiber": 1, "sugar": 0.4},
                      "large": {"cal": 140, "fat": 3.5, "carbs": 24, "protein": 4, "sodium": 290, "fiber": 1.5, "sugar": 0.6}},
    "corn tortilla": {"": {"cal": 52, "fat": 0.7, "carbs": 11, "protein": 1, "sodium": 11, "fiber": 1.5, "sugar": 0.2}},
    "pita bread": {"": {"cal": 165, "fat": 0.7, "carbs": 34, "protein": 5, "sodium": 322, "fiber": 1, "sugar": 0.5}},
    "hamburger bun": {"": {"cal": 120, "fat": 2, "carbs": 21, "protein": 4, "sodium": 206, "fiber": 0.9, "sugar": 3}},
    "hot dog bun": {"": {"cal": 100, "fat": 1.5, "carbs": 18, "protein": 3, "sodium": 180, "fiber": 0.7, "sugar": 2}},
    "pie crust": {"": {"cal": 648, "fat": 40, "carbs": 63, "protein": 7, "sodium": 520, "fiber": 2, "sugar": 2}},
    "pizza dough": {"lb": {"cal": 680, "fat": 8, "carbs": 130, "protein": 22, "sodium": 1200, "fiber": 5, "sugar": 4}},
    "biscuit": {"": {"cal": 127, "fat": 6, "carbs": 17, "protein": 2, "sodium": 368, "fiber": 0.5, "sugar": 2}},

    # =========================================================================
    # CHOCOLATE & BAKING
    # =========================================================================
    "chocolate chips": {"cup": {"cal": 805, "fat": 50, "carbs": 100, "protein": 7, "sodium": 23, "fiber": 10, "sugar": 81}},
    "cocoa powder": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1},
                    "tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "baking chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 4, "sugar": 0}},
    "white chocolate": {"cup": {"cal": 916, "fat": 55, "carbs": 101, "protein": 10, "sodium": 153, "fiber": 0, "sugar": 101}},
    "nutella": {"tbsp": {"cal": 100, "fat": 6, "carbs": 11, "protein": 1, "sodium": 15, "fiber": 0.5, "sugar": 10}},
    "gelatin": {"tbsp": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0},
               "packet": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0},
               "envelope": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0}},
    "vanilla extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.5}},
    "almond extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # LEAVENING & BAKING STAPLES
    # =========================================================================
    "baking powder": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.7, "protein": 0, "sodium": 133, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 5, "fat": 0, "carbs": 2, "protein": 0, "sodium": 400, "fiber": 0, "sugar": 0}},
    "baking soda": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1260, "fiber": 0, "sugar": 0}},
    "yeast": {"packet": {"cal": 21, "fat": 0.3, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 2, "sugar": 0},
             "tbsp": {"cal": 23, "fat": 0.4, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 2, "sugar": 0},
             "tsp": {"cal": 8, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 1, "fiber": 0.6, "sugar": 0}},
    "cream of tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # SPICES & SEASONINGS
    # =========================================================================
    "salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 2325, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 6975, "fiber": 0, "sugar": 0},
            "pinch": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0},
            "to taste": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0},
            "": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0}},
    "pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0},
              "to taste": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0},
              "": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "black pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "garlic powder": {"tsp": {"cal": 10, "fat": 0, "carbs": 2, "protein": 0.5, "sodium": 2, "fiber": 0.3, "sugar": 0}},
    "onion powder": {"tsp": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 2, "fiber": 0.2, "sugar": 0.4}},
    "cumin": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 1, "protein": 0.4, "sodium": 4, "fiber": 0.2, "sugar": 0},
             "tbsp": {"cal": 22, "fat": 1.3, "carbs": 3, "protein": 1, "sodium": 10, "fiber": 0.6, "sugar": 0.1}},
    "paprika": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5},
               "": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5}},
    "chili powder": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.4, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.3},
                    "tbsp": {"cal": 24, "fat": 1.3, "carbs": 4, "protein": 1, "sodium": 77, "fiber": 2.7, "sugar": 0.9}},
    "cayenne pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "oregano": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "basil": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "thyme": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "rosemary": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0, "sodium": 1, "fiber": 0.2, "sugar": 0}},
    "sage": {"tsp": {"cal": 2, "fat": 0.1, "carbs": 0.4, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},
    "parsley": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0},
               "cup": {"cal": 22, "fat": 0.5, "carbs": 4, "protein": 2, "sodium": 34, "fiber": 2, "sugar": 0.5}},
    "cilantro": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 3, "fiber": 0.2, "sugar": 0}},
    "dill": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0},
            "tbsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.2, "sodium": 5, "fiber": 0.2, "sugar": 0}},
    "cinnamon": {"tsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 1, "sugar": 0}},
    "nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0}},
    "ginger": {"tsp": {"cal": 6, "fat": 0, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0},
              "tbsp": {"cal": 18, "fat": 0, "carbs": 4, "protein": 0.5, "sodium": 3, "fiber": 0.6, "sugar": 0.5}},
    "allspice": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1.4, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "cloves": {"tsp": {"cal": 7, "fat": 0.4, "carbs": 1.3, "protein": 0.1, "sodium": 5, "fiber": 0.7, "sugar": 0}},
    "mustard": {"tsp": {"cal": 3, "fat": 0.2, "carbs": 0.3, "protein": 0.2, "sodium": 57, "fiber": 0.1, "sugar": 0.1},
               "tbsp": {"cal": 10, "fat": 0.7, "carbs": 0.8, "protein": 0.7, "sodium": 171, "fiber": 0.4, "sugar": 0.3}},
    "dry mustard": {"tsp": {"cal": 9, "fat": 0.5, "carbs": 0.5, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "curry powder": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 1, "fiber": 0.7, "sugar": 0.1},
                    "tbsp": {"cal": 20, "fat": 0.9, "carbs": 3.7, "protein": 0.8, "sodium": 3, "fiber": 2, "sugar": 0.2}},
    "bay leaf": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "bay leaves": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "italian seasoning": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "taco seasoning": {"packet": {"cal": 30, "fat": 0.5, "carbs": 6, "protein": 1, "sodium": 1400, "fiber": 1, "sugar": 1},
                      "tbsp": {"cal": 15, "fat": 0.3, "carbs": 3, "protein": 0.5, "sodium": 700, "fiber": 0.5, "sugar": 0.5}},
    "ranch seasoning": {"packet": {"cal": 45, "fat": 0, "carbs": 10, "protein": 1, "sodium": 1200, "fiber": 0, "sugar": 2}},
    "worcestershire sauce": {"tbsp": {"cal": 13, "fat": 0, "carbs": 3, "protein": 0, "sodium": 167, "fiber": 0, "sugar": 2}},
    "soy sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 1, "protein": 1, "sodium": 879, "fiber": 0, "sugar": 0}},
    "hot sauce": {"tsp": {"cal": 1, "fat": 0, "carbs": 0, "protein": 0, "sodium": 124, "fiber": 0, "sugar": 0}},
    "bbq sauce": {"tbsp": {"cal": 29, "fat": 0.1, "carbs": 7, "protein": 0.1, "sodium": 175, "fiber": 0.2, "sugar": 5}},
    "ketchup": {"tbsp": {"cal": 19, "fat": 0, "carbs": 5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 4}},

    # =========================================================================
    # VINEGARS & ACIDS
    # =========================================================================
    "vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
               "cup": {"cal": 43, "fat": 0, "carbs": 0.9, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0.4}},
    "apple cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "balsamic vinegar": {"tbsp": {"cal": 14, "fat": 0, "carbs": 3, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 2}},
    "red wine vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0},
                         "cup": {"cal": 45, "fat": 0, "carbs": 0, "protein": 0, "sodium": 12, "fiber": 0, "sugar": 0}},
    "white wine vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0}},
    "rice vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # WINES & ALCOHOL (for cooking)
    # =========================================================================
    "white wine": {"cup": {"cal": 194, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 10, "fiber": 0, "sugar": 1.4}},
    "red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 10, "fiber": 0, "sugar": 0.9}},
    "cooking wine": {"cup": {"cal": 190, "fat": 0, "carbs": 8, "protein": 0, "sodium": 1000, "fiber": 0, "sugar": 4}},
    "beer": {"cup": {"cal": 103, "fat": 0, "carbs": 6, "protein": 1, "sodium": 14, "fiber": 0, "sugar": 0}},
    "rum": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bourbon": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vodka": {"tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # MISCELLANEOUS
    # =========================================================================
    "coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "tea": {"cup": {"cal": 2, "fat": 0, "carbs": 1, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 0}},
    "cocoa": {"cup": {"cal": 196, "fat": 12, "carbs": 47, "protein": 17, "sodium": 18, "fiber": 29, "sugar": 1}},
    "jam": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0.2, "sugar": 10}},
    "jelly": {"tbsp": {"cal": 56, "fat": 0, "carbs": 14, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 10}},
    "marshmallows": {"cup": {"cal": 159, "fat": 0, "carbs": 41, "protein": 1, "sodium": 22, "fiber": 0, "sugar": 29}},
    "graham cracker": {"sheet": {"cal": 59, "fat": 1.4, "carbs": 11, "protein": 1, "sodium": 67, "fiber": 0.4, "sugar": 4}},
    "crackers": {"cup": {"cal": 484, "fat": 15, "carbs": 78, "protein": 10, "sodium": 1080, "fiber": 3, "sugar": 6}},
    "tortilla chips": {"cup": {"cal": 267, "fat": 14, "carbs": 33, "protein": 3, "sodium": 179, "fiber": 2, "sugar": 0}},
    "potato chips": {"cup": {"cal": 274, "fat": 19, "carbs": 25, "protein": 3, "sodium": 303, "fiber": 2, "sugar": 1}},
    "french fried onions": {"cup": {"cal": 320, "fat": 24, "carbs": 24, "protein": 4, "sodium": 520, "fiber": 2, "sugar": 4}},

    # Cooking sprays & zests
    "cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "nonstick spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lemon zest": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0.1},
                   "tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.2}},
    "orange zest": {"tsp": {"cal": 2, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0.2},
                    "tbsp": {"cal": 6, "fat": 0, "carbs": 1.5, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 0.4}},
    "lime zest": {"tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0.1},
                  "tbsp": {"cal": 3, "fat": 0, "carbs": 0.9, "protein": 0, "sodium": 0, "fiber": 0.3, "sugar": 0.2}},
    "onion juice": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0.4},
                    "tsp": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.1}},
    "grated onion": {"tbsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.4}},

    # Cream and creamed soups
    "cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "whipped topping": {"cup": {"cal": 239, "fat": 19, "carbs": 17, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 14}},
    "cool whip": {"cup": {"cal": 239, "fat": 19, "carbs": 17, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 14}},
    "cream of chicken soup": {"can": {"cal": 226, "fat": 14, "carbs": 18, "protein": 6, "sodium": 1764, "fiber": 1, "sugar": 2}},
    "cream of mushroom soup": {"can": {"cal": 260, "fat": 18, "carbs": 18, "protein": 4, "sodium": 1740, "fiber": 2, "sugar": 4}},
    "cream of celery soup": {"can": {"cal": 180, "fat": 10, "carbs": 18, "protein": 2, "sodium": 1760, "fiber": 2, "sugar": 4}},
    "tomato soup": {"can": {"cal": 160, "fat": 2, "carbs": 34, "protein": 4, "sodium": 1400, "fiber": 2, "sugar": 20}},

    # Pinch/dash for minimal seasonings
    "pinch": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 0}},
    "dash": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 0}},

    # Baked goods & prepared items (from GrannysRecipes)
    "croissant": {"": {"cal": 230, "fat": 12, "carbs": 26, "protein": 5, "sodium": 310, "fiber": 1, "sugar": 6}},
    "crescent rolls": {"": {"cal": 100, "fat": 5, "carbs": 11, "protein": 2, "sodium": 220, "fiber": 0, "sugar": 2}},
    "puff pastry": {"sheet": {"cal": 900, "fat": 60, "carbs": 72, "protein": 12, "sodium": 360, "fiber": 2, "sugar": 2}},
    "english muffin": {"": {"cal": 134, "fat": 1, "carbs": 26, "protein": 4, "sodium": 264, "fiber": 2, "sugar": 2}},
    "angel food cake": {"slice": {"cal": 72, "fat": 0.2, "carbs": 16, "protein": 2, "sodium": 210, "fiber": 0, "sugar": 12}},
    "crepe": {"": {"cal": 90, "fat": 4, "carbs": 11, "protein": 3, "sodium": 100, "fiber": 0, "sugar": 2}},
    "crepes": {"": {"cal": 90, "fat": 4, "carbs": 11, "protein": 3, "sodium": 100, "fiber": 0, "sugar": 2}},
    "pound cake": {"slice": {"cal": 220, "fat": 10, "carbs": 28, "protein": 3, "sodium": 180, "fiber": 0.5, "sugar": 18}},

    # Convenience foods
    "cake mix": {"package": {"cal": 1600, "fat": 32, "carbs": 312, "protein": 16, "sodium": 2800, "fiber": 4, "sugar": 168}},
    "pudding mix": {"package": {"cal": 140, "fat": 0, "carbs": 35, "protein": 0, "sodium": 340, "fiber": 0, "sugar": 28}},
    "jello": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "pie filling": {"can": {"cal": 840, "fat": 0, "carbs": 210, "protein": 0, "sodium": 100, "fiber": 4, "sugar": 180}},
    "tater tots": {"cup": {"cal": 200, "fat": 10, "carbs": 24, "protein": 2, "sodium": 400, "fiber": 2, "sugar": 0}},
    "bouillon cube": {"": {"cal": 5, "fat": 0.1, "carbs": 0.6, "protein": 0.5, "sodium": 900, "fiber": 0, "sugar": 0}},

    # Additional vegetables/fruits
    "beets": {"cup": {"cal": 58, "fat": 0.2, "carbs": 13, "protein": 2, "sodium": 106, "fiber": 4, "sugar": 9}},
    "cherry": {"cup": {"cal": 87, "fat": 0.3, "carbs": 22, "protein": 1.5, "sodium": 0, "fiber": 3, "sugar": 18}},
    "cherries": {"cup": {"cal": 87, "fat": 0.3, "carbs": 22, "protein": 1.5, "sodium": 0, "fiber": 3, "sugar": 18}},
    "mandarin oranges": {"cup": {"cal": 72, "fat": 0.2, "carbs": 18, "protein": 1, "sodium": 10, "fiber": 2, "sugar": 14}},
    "prunes": {"cup": {"cal": 418, "fat": 0.7, "carbs": 111, "protein": 4, "sodium": 4, "fiber": 12, "sugar": 66}},
    "barley": {"cup": {"cal": 651, "fat": 2.3, "carbs": 135, "protein": 23, "sodium": 22, "fiber": 32, "sugar": 1}},

    # Condiments & misc
    "horseradish": {"tbsp": {"cal": 7, "fat": 0.1, "carbs": 2, "protein": 0.2, "sodium": 47, "fiber": 0.5, "sugar": 1}},
    "chili sauce": {"tbsp": {"cal": 20, "fat": 0.1, "carbs": 5, "protein": 0.3, "sodium": 200, "fiber": 0.2, "sugar": 3},
                   "cup": {"cal": 320, "fat": 1.6, "carbs": 80, "protein": 4.8, "sodium": 3200, "fiber": 3.2, "sugar": 48}},
    "pickles": {"cup": {"cal": 17, "fat": 0.2, "carbs": 3.7, "protein": 0.4, "sodium": 1208, "fiber": 1, "sugar": 2}},
    "pickle": {"": {"cal": 12, "fat": 0.1, "carbs": 2.7, "protein": 0.3, "sodium": 870, "fiber": 0.8, "sugar": 1}},

    # =========================================================================
    # ADDITIONAL FROM MomsRecipes DATABASE
    # =========================================================================

    # Meat variants & poultry
    "chicken thighs": {"lb": {"cal": 900, "fat": 56, "carbs": 0, "protein": 80, "sodium": 340, "fiber": 0, "sugar": 0}},
    "extra-lean ground beef": {"lb": {"cal": 800, "fat": 48, "carbs": 0, "protein": 88, "sodium": 300, "fiber": 0, "sugar": 0}},
    "pork chops": {"oz": {"cal": 52, "fat": 2.5, "carbs": 0, "protein": 7, "sodium": 18, "fiber": 0, "sugar": 0},
                   "": {"cal": 231, "fat": 13, "carbs": 0, "protein": 26, "sodium": 62, "fiber": 0, "sugar": 0}},
    "spareribs": {"lb": {"cal": 1200, "fat": 96, "carbs": 0, "protein": 80, "sodium": 400, "fiber": 0, "sugar": 0}},
    "lamb": {"lb": {"cal": 1100, "fat": 80, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "ground lamb": {"lb": {"cal": 1100, "fat": 80, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "lamb chops": {"lb": {"cal": 880, "fat": 60, "carbs": 0, "protein": 84, "sodium": 260, "fiber": 0, "sugar": 0}},
    "guanciale": {"oz": {"cal": 155, "fat": 14, "carbs": 0, "protein": 6, "sodium": 480, "fiber": 0, "sugar": 0}},
    "pancetta": {"oz": {"cal": 145, "fat": 13, "carbs": 0, "protein": 7, "sodium": 500, "fiber": 0, "sugar": 0}},
    "andouille sausage": {"oz": {"cal": 90, "fat": 8, "carbs": 1, "protein": 4, "sodium": 300, "fiber": 0, "sugar": 0}},
    "tofu": {"oz": {"cal": 22, "fat": 1.3, "carbs": 0.5, "protein": 2, "sodium": 2, "fiber": 0, "sugar": 0},
             "cup": {"cal": 176, "fat": 10, "carbs": 4, "protein": 16, "sodium": 16, "fiber": 0, "sugar": 0}},
    "fish": {"oz": {"cal": 35, "fat": 0.8, "carbs": 0, "protein": 7, "sodium": 45, "fiber": 0, "sugar": 0},
             "lb": {"cal": 560, "fat": 13, "carbs": 0, "protein": 112, "sodium": 720, "fiber": 0, "sugar": 0}},

    # Dairy aliases & variants
    "unsalted butter": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 12, "fiber": 0, "sugar": 0},
                        "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "butter or margarine": {"cup": {"cal": 1628, "fat": 184, "carbs": 0, "protein": 2, "sodium": 1284, "fiber": 0, "sugar": 0},
                            "tbsp": {"cal": 102, "fat": 11.5, "carbs": 0, "protein": 0.1, "sodium": 80, "fiber": 0, "sugar": 0}},
    "oleo (margarine)": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "whipping cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "half-and-half": {"cup": {"cal": 315, "fat": 28, "carbs": 10, "protein": 7, "sodium": 98, "fiber": 0, "sugar": 10},
                      "tbsp": {"cal": 20, "fat": 1.7, "carbs": 0.6, "protein": 0.4, "sodium": 6, "fiber": 0, "sugar": 0.6}},
    "shredded cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.5, "protein": 28, "sodium": 700, "fiber": 0, "sugar": 0}},
    "grated parmesan cheese": {"tbsp": {"cal": 22, "fat": 1.4, "carbs": 0.2, "protein": 2, "sodium": 76, "fiber": 0, "sugar": 0},
                               "cup": {"cal": 352, "fat": 22, "carbs": 3, "protein": 32, "sodium": 1216, "fiber": 0, "sugar": 0}},
    "cheese": {"cup": {"cal": 400, "fat": 32, "carbs": 2, "protein": 24, "sodium": 650, "fiber": 0, "sugar": 0},
               "oz": {"cal": 100, "fat": 8, "carbs": 0.5, "protein": 6, "sodium": 162, "fiber": 0, "sugar": 0}},
    "large eggs": {"": {"cal": 72, "fat": 5, "carbs": 0.4, "protein": 6, "sodium": 71, "fiber": 0, "sugar": 0.4}},
    "egg whites": {"": {"cal": 17, "fat": 0, "carbs": 0.2, "protein": 3.6, "sodium": 55, "fiber": 0, "sugar": 0}},
    "egg yolks": {"": {"cal": 55, "fat": 4.5, "carbs": 0.6, "protein": 2.7, "sodium": 8, "fiber": 0, "sugar": 0}},

    # Grains & starches
    "quick oats": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "oatmeal": {"cup": {"cal": 307, "fat": 5, "carbs": 55, "protein": 11, "sodium": 5, "fiber": 8, "sugar": 1}},
    "noodles": {"cup": {"cal": 220, "fat": 2, "carbs": 40, "protein": 8, "sodium": 10, "fiber": 2, "sugar": 0}},
    "linguine": {"oz": {"cal": 100, "fat": 0.5, "carbs": 20, "protein": 3.5, "sodium": 1, "fiber": 1, "sugar": 0}},
    "elbow macaroni": {"cup": {"cal": 200, "fat": 1, "carbs": 41, "protein": 7, "sodium": 2, "fiber": 2, "sugar": 1}},
    "rotini": {"cup": {"cal": 200, "fat": 1, "carbs": 41, "protein": 7, "sodium": 2, "fiber": 2, "sugar": 1}},
    "fresh chinese noodles": {"oz": {"cal": 100, "fat": 1, "carbs": 20, "protein": 3, "sodium": 150, "fiber": 1, "sugar": 0}},
    "bread crumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 930, "fiber": 3, "sugar": 6}},
    "bread slices": {"": {"cal": 79, "fat": 1, "carbs": 15, "protein": 3, "sodium": 147, "fiber": 1, "sugar": 1}},
    "kashi pilaf": {"cup": {"cal": 170, "fat": 1, "carbs": 34, "protein": 6, "sodium": 0, "fiber": 6, "sugar": 0}},
    "biscuit mix": {"cup": {"cal": 480, "fat": 16, "carbs": 72, "protein": 8, "sodium": 1360, "fiber": 2, "sugar": 8}},
    "bisquick": {"cup": {"cal": 480, "fat": 16, "carbs": 72, "protein": 8, "sodium": 1360, "fiber": 2, "sugar": 8}},
    "graham crackers": {"cup": {"cal": 440, "fat": 10, "carbs": 80, "protein": 6, "sodium": 520, "fiber": 2, "sugar": 24}},
    "graham cracker crust": {"": {"cal": 800, "fat": 36, "carbs": 112, "protein": 8, "sodium": 600, "fiber": 2, "sugar": 40}},

    # Sugar aliases
    "granulated sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200},
                         "tbsp": {"cal": 48, "fat": 0, "carbs": 12.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 12.5}},
    "white sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "light brown sugar": {"cup": {"cal": 829, "fat": 0, "carbs": 214, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 212}},
    "packed brown sugar": {"cup": {"cal": 829, "fat": 0, "carbs": 214, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 212}},
    "confectioners' sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 119, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117}},

    # Oils
    "oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
            "cup": {"cal": 1920, "fat": 224, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "sesame oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Vegetables
    "onions": {"cup": {"cal": 64, "fat": 0.2, "carbs": 15, "protein": 1.8, "sodium": 6, "fiber": 3, "sugar": 7}},
    "green onions": {"cup": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 1.8, "sodium": 16, "fiber": 2.6, "sugar": 2.3},
                     "bunch": {"cal": 32, "fat": 0.2, "carbs": 7, "protein": 1.8, "sodium": 16, "fiber": 2.6, "sugar": 2.3}},
    "carrots": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1.2, "sodium": 88, "fiber": 3.6, "sugar": 6}},
    "tomatoes": {"can": {"cal": 80, "fat": 0.4, "carbs": 16, "protein": 4, "sodium": 600, "fiber": 4, "sugar": 10},
                 "cup": {"cal": 32, "fat": 0.4, "carbs": 7, "protein": 1.6, "sodium": 9, "fiber": 2, "sugar": 5}},
    "potatoes": {"lb": {"cal": 350, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 28, "fiber": 9, "sugar": 4}},
    "rhubarb": {"cup": {"cal": 26, "fat": 0.2, "carbs": 6, "protein": 1.1, "sodium": 5, "fiber": 2, "sugar": 1.3}},
    "pumpkin": {"cup": {"cal": 83, "fat": 0.3, "carbs": 20, "protein": 3, "sodium": 12, "fiber": 3, "sugar": 8}},
    "okra": {"cup": {"cal": 33, "fat": 0.2, "carbs": 7, "protein": 2, "sodium": 7, "fiber": 3, "sugar": 1}},
    "sauerkraut": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1.3, "sodium": 939, "fiber": 4, "sugar": 3}},
    "green chilies": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 550, "fiber": 2, "sugar": 3}},
    "chopped green chilies": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 550, "fiber": 2, "sugar": 3}},
    "frozen mixed vegetables": {"cup": {"cal": 82, "fat": 0.5, "carbs": 16, "protein": 4, "sodium": 64, "fiber": 5, "sugar": 4}},
    "mixed vegetables": {"cup": {"cal": 82, "fat": 0.5, "carbs": 16, "protein": 4, "sodium": 64, "fiber": 5, "sugar": 4}},
    "beans": {"cup": {"cal": 225, "fat": 1, "carbs": 40, "protein": 15, "sodium": 400, "fiber": 12, "sugar": 1}},

    # Fruits
    "calamondin": {"": {"cal": 12, "fat": 0.1, "carbs": 3, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 1.5}},
    "calamondins": {"cup": {"cal": 60, "fat": 0.5, "carbs": 15, "protein": 1, "sodium": 5, "fiber": 2.5, "sugar": 7.5}},
    "crushed pineapple": {"can": {"cal": 280, "fat": 0.4, "carbs": 68, "protein": 2, "sodium": 4, "fiber": 4, "sugar": 60}},
    "apricots": {"cup": {"cal": 79, "fat": 0.6, "carbs": 18, "protein": 2.3, "sodium": 2, "fiber": 3, "sugar": 15}},
    "dried apricots": {"cup": {"cal": 313, "fat": 0.7, "carbs": 81, "protein": 4.4, "sodium": 13, "fiber": 9.5, "sugar": 69}},
    "lemons": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 1.6, "sugar": 1.5}},
    "lemon": {"": {"cal": 17, "fat": 0.2, "carbs": 5, "protein": 0.6, "sodium": 1, "fiber": 1.6, "sugar": 1.5}},
    "cranberry juice": {"cup": {"cal": 116, "fat": 0.3, "carbs": 31, "protein": 0, "sodium": 5, "fiber": 0.3, "sugar": 31}},

    # Nuts
    "chopped pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "pecan halves": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "chopped nuts": {"cup": {"cal": 800, "fat": 72, "carbs": 24, "protein": 20, "sodium": 5, "fiber": 8, "sugar": 4}},
    "nuts": {"cup": {"cal": 800, "fat": 72, "carbs": 24, "protein": 20, "sodium": 5, "fiber": 8, "sugar": 4}},
    "wheat germ": {"tbsp": {"cal": 26, "fat": 0.7, "carbs": 3.7, "protein": 2, "sodium": 0, "fiber": 1, "sugar": 0},
                   "cup": {"cal": 414, "fat": 11, "carbs": 60, "protein": 27, "sodium": 4, "fiber": 15, "sugar": 0}},

    # Baking & chocolate
    "chocolate": {"oz": {"cal": 155, "fat": 9, "carbs": 17, "protein": 1.4, "sodium": 7, "fiber": 2, "sugar": 14}},
    "unsweetened cocoa": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 1, "fiber": 2, "sugar": 0}},
    "vanilla": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.5}},
    "lemon extract": {"tsp": {"cal": 10, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0.3}},
    "active dry yeast": {"packet": {"cal": 21, "fat": 0.3, "carbs": 3, "protein": 3, "sodium": 4, "fiber": 1, "sugar": 0}},
    "yellow cake mix": {"package": {"cal": 1600, "fat": 32, "carbs": 312, "protein": 16, "sodium": 2800, "fiber": 4, "sugar": 168}},
    "brownie mix": {"package": {"cal": 1600, "fat": 32, "carbs": 280, "protein": 16, "sodium": 800, "fiber": 4, "sugar": 160}},
    "liquid pectin": {"pouch": {"cal": 10, "fat": 0, "carbs": 3, "protein": 0, "sodium": 5, "fiber": 1, "sugar": 0}},

    # Pie shells
    "pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},
    "baked pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},
    "unbaked pie shell": {"": {"cal": 650, "fat": 40, "carbs": 64, "protein": 8, "sodium": 400, "fiber": 2, "sugar": 2}},

    # Herbs & spices - dried variants
    "ground cinnamon": {"tsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1, "sugar": 0}},
    "ground nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1.1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0}},
    "ground ginger": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 1, "fiber": 0.2, "sugar": 0.1}},
    "ground cumin": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 0.9, "protein": 0.4, "sodium": 4, "fiber": 0.2, "sugar": 0}},
    "fresh ginger": {"tbsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.1, "sugar": 0.1}},
    "fresh parsley": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "fresh dill": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 2, "fiber": 0, "sugar": 0}},
    "dried dill": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.5, "protein": 0.2, "sodium": 2, "fiber": 0.1, "sugar": 0}},
    "dried oregano": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "dried thyme": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.6, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "dried parsley": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "dried parsley flakes": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "parsley flakes": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 0.6, "protein": 0.3, "sodium": 6, "fiber": 0.2, "sugar": 0.1}},
    "turmeric": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "poultry seasoning": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "white pepper": {"tsp": {"cal": 7, "fat": 0.1, "carbs": 1.6, "protein": 0.3, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "salt and pepper": {"tsp": {"cal": 3, "fat": 0, "carbs": 0.7, "protein": 0.1, "sodium": 1163, "fiber": 0.3, "sugar": 0}},
    "seasoned salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1360, "fiber": 0, "sugar": 0}},
    "garlic salt": {"tsp": {"cal": 3, "fat": 0, "carbs": 0.7, "protein": 0.1, "sodium": 1480, "fiber": 0, "sugar": 0}},

    # Condiments & sauces
    "oyster sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 437, "fiber": 0, "sugar": 1}},
    "white vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tabasco sauce": {"tsp": {"cal": 1, "fat": 0, "carbs": 0, "protein": 0, "sodium": 124, "fiber": 0, "sugar": 0}},
    "marinara sauce": {"cup": {"cal": 80, "fat": 2, "carbs": 12, "protein": 2, "sodium": 560, "fiber": 2, "sugar": 8}},

    # Alcohol
    "wine": {"cup": {"cal": 200, "fat": 0, "carbs": 5, "protein": 0.2, "sodium": 12, "fiber": 0, "sugar": 2}},
    "chinese cooking wine": {"tbsp": {"cal": 15, "fat": 0, "carbs": 2, "protein": 0, "sodium": 180, "fiber": 0, "sugar": 1}},
    "sherry": {"oz": {"cal": 45, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 3, "fiber": 0, "sugar": 1},
               "tbsp": {"cal": 22, "fat": 0, "carbs": 1, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0.5}},
    "brandy": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
               "tbsp": {"cal": 32, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Water variants
    "warm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "hot water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cold water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "boiling water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Miscellaneous
    "miniature marshmallows": {"cup": {"cal": 159, "fat": 0.1, "carbs": 41, "protein": 1.4, "sodium": 22, "fiber": 0, "sugar": 29}},
    "pretzels": {"cup": {"cal": 229, "fat": 2, "carbs": 48, "protein": 5, "sodium": 814, "fiber": 2, "sugar": 1}},
    "chex cereal": {"cup": {"cal": 110, "fat": 0.5, "carbs": 25, "protein": 2, "sodium": 220, "fiber": 1, "sugar": 2}},
    "lemon rind": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "grated lemon rind": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "grated lemon peel": {"tbsp": {"cal": 3, "fat": 0, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0.4}},
    "orange peel": {"tbsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 1}},
    "grated orange peel": {"tbsp": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 0.6, "sugar": 1}},
    "food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "green food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "red food coloring": {"drop": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vegetable cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "nonstick cooking spray": {"": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # ADDITIONAL FROM MomsRecipes DATABASE - ROUND 2
    # =========================================================================

    # Beverages
    "cola": {"cup": {"cal": 97, "fat": 0, "carbs": 26, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 26}},
    "soda": {"cup": {"cal": 97, "fat": 0, "carbs": 26, "protein": 0, "sodium": 7, "fiber": 0, "sugar": 26}},
    "ginger ale": {"cup": {"cal": 83, "fat": 0, "carbs": 21, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 21}},
    "apple juice": {"cup": {"cal": 114, "fat": 0.3, "carbs": 28, "protein": 0.2, "sodium": 10, "fiber": 0.2, "sugar": 24}},
    "grape juice": {"cup": {"cal": 152, "fat": 0.2, "carbs": 37, "protein": 1, "sodium": 13, "fiber": 0.3, "sugar": 36}},
    "limeade": {"cup": {"cal": 104, "fat": 0, "carbs": 27, "protein": 0.1, "sodium": 5, "fiber": 0, "sugar": 26}},
    "lemonade": {"cup": {"cal": 99, "fat": 0.1, "carbs": 26, "protein": 0.2, "sodium": 7, "fiber": 0.2, "sugar": 25}},
    "cranberry juice": {"cup": {"cal": 116, "fat": 0.3, "carbs": 31, "protein": 0, "sodium": 5, "fiber": 0.3, "sugar": 31}},
    "tomato juice": {"cup": {"cal": 41, "fat": 0.1, "carbs": 10, "protein": 1.8, "sodium": 654, "fiber": 1, "sugar": 8}},
    "v8 juice": {"cup": {"cal": 46, "fat": 0.1, "carbs": 10, "protein": 1.5, "sodium": 480, "fiber": 1.5, "sugar": 7}},
    "prune juice": {"cup": {"cal": 182, "fat": 0.1, "carbs": 45, "protein": 1.6, "sodium": 10, "fiber": 2.6, "sugar": 42}},

    # Proteins - meats & poultry
    "veal": {"lb": {"cal": 800, "fat": 32, "carbs": 0, "protein": 120, "sodium": 340, "fiber": 0, "sugar": 0}},
    "duck": {"lb": {"cal": 1300, "fat": 100, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},
    "liver": {"lb": {"cal": 600, "fat": 16, "carbs": 16, "protein": 92, "sodium": 300, "fiber": 0, "sugar": 0}},
    "chicken liver": {"lb": {"cal": 600, "fat": 16, "carbs": 3, "protein": 84, "sodium": 320, "fiber": 0, "sugar": 0}},
    "hot dog": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "hot dogs": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "frankfurter": {"each": {"cal": 151, "fat": 13, "carbs": 2, "protein": 5, "sodium": 567, "fiber": 0, "sugar": 1}},
    "pepperoni": {"oz": {"cal": 138, "fat": 12, "carbs": 0.9, "protein": 6, "sodium": 463, "fiber": 0, "sugar": 0}},
    "salami": {"oz": {"cal": 119, "fat": 10, "carbs": 0.5, "protein": 6, "sodium": 529, "fiber": 0, "sugar": 0}},
    "prosciutto": {"oz": {"cal": 55, "fat": 3, "carbs": 0.3, "protein": 7, "sodium": 520, "fiber": 0, "sugar": 0}},
    "corned beef": {"lb": {"cal": 800, "fat": 48, "carbs": 2, "protein": 88, "sodium": 3200, "fiber": 0, "sugar": 0}},

    # Proteins - seafood
    "halibut": {"lb": {"cal": 500, "fat": 10, "carbs": 0, "protein": 96, "sodium": 260, "fiber": 0, "sugar": 0}},
    "catfish": {"lb": {"cal": 544, "fat": 24, "carbs": 0, "protein": 80, "sodium": 200, "fiber": 0, "sugar": 0}},
    "scallops": {"lb": {"cal": 400, "fat": 4, "carbs": 8, "protein": 76, "sodium": 700, "fiber": 0, "sugar": 0}},
    "sea scallops": {"lb": {"cal": 400, "fat": 4, "carbs": 8, "protein": 76, "sodium": 700, "fiber": 0, "sugar": 0}},
    "oysters": {"cup": {"cal": 169, "fat": 6, "carbs": 10, "protein": 17, "sodium": 521, "fiber": 0, "sugar": 0}},
    "mussels": {"lb": {"cal": 350, "fat": 8, "carbs": 16, "protein": 48, "sodium": 1200, "fiber": 0, "sugar": 0}},
    "sardines": {"can": {"cal": 191, "fat": 11, "carbs": 0, "protein": 23, "sodium": 465, "fiber": 0, "sugar": 0}},
    "anchovies": {"can": {"cal": 95, "fat": 4, "carbs": 0, "protein": 13, "sodium": 1650, "fiber": 0, "sugar": 0}},
    "anchovy fillets": {"each": {"cal": 8, "fat": 0.4, "carbs": 0, "protein": 1, "sodium": 147, "fiber": 0, "sugar": 0}},
    "cod": {"lb": {"cal": 372, "fat": 3, "carbs": 0, "protein": 80, "sodium": 220, "fiber": 0, "sugar": 0}},
    "sole": {"lb": {"cal": 360, "fat": 4, "carbs": 0, "protein": 76, "sodium": 360, "fiber": 0, "sugar": 0}},
    "flounder": {"lb": {"cal": 360, "fat": 4, "carbs": 0, "protein": 76, "sodium": 360, "fiber": 0, "sugar": 0}},
    "perch": {"lb": {"cal": 420, "fat": 4, "carbs": 0, "protein": 88, "sodium": 300, "fiber": 0, "sugar": 0}},
    "trout": {"lb": {"cal": 600, "fat": 24, "carbs": 0, "protein": 92, "sodium": 220, "fiber": 0, "sugar": 0}},
    "swordfish": {"lb": {"cal": 548, "fat": 16, "carbs": 0, "protein": 92, "sodium": 420, "fiber": 0, "sugar": 0}},
    "mahi mahi": {"lb": {"cal": 384, "fat": 4, "carbs": 0, "protein": 84, "sodium": 400, "fiber": 0, "sugar": 0}},

    # Legumes
    "navy beans": {"cup": {"cal": 255, "fat": 1, "carbs": 47, "protein": 15, "sodium": 0, "fiber": 19, "sugar": 0}},
    "lima beans": {"cup": {"cal": 216, "fat": 0.7, "carbs": 39, "protein": 15, "sodium": 29, "fiber": 13, "sugar": 6}},
    "chickpeas": {"cup": {"cal": 269, "fat": 4, "carbs": 45, "protein": 15, "sodium": 11, "fiber": 12.5, "sugar": 8}},
    "garbanzo beans": {"cup": {"cal": 269, "fat": 4, "carbs": 45, "protein": 15, "sodium": 11, "fiber": 12.5, "sugar": 8}},
    "lentils": {"cup": {"cal": 230, "fat": 0.8, "carbs": 40, "protein": 18, "sodium": 4, "fiber": 16, "sugar": 4}},
    "split peas": {"cup": {"cal": 231, "fat": 0.8, "carbs": 41, "protein": 16, "sodium": 4, "fiber": 16, "sugar": 6}},
    "hummus": {"cup": {"cal": 435, "fat": 21, "carbs": 50, "protein": 20, "sodium": 960, "fiber": 15, "sugar": 0}},

    # Dairy
    "ricotta cheese": {"cup": {"cal": 428, "fat": 32, "carbs": 7.5, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.6}},
    "ricotta": {"cup": {"cal": 428, "fat": 32, "carbs": 7.5, "protein": 28, "sodium": 307, "fiber": 0, "sugar": 0.6}},
    "blue cheese": {"oz": {"cal": 100, "fat": 8, "carbs": 0.7, "protein": 6, "sodium": 325, "fiber": 0, "sugar": 0.1}},
    "feta cheese": {"oz": {"cal": 75, "fat": 6, "carbs": 1, "protein": 4, "sodium": 316, "fiber": 0, "sugar": 1}},
    "feta": {"oz": {"cal": 75, "fat": 6, "carbs": 1, "protein": 4, "sodium": 316, "fiber": 0, "sugar": 1}},
    "goat cheese": {"oz": {"cal": 76, "fat": 6, "carbs": 0, "protein": 5, "sodium": 104, "fiber": 0, "sugar": 0}},
    "gorgonzola": {"oz": {"cal": 100, "fat": 9, "carbs": 1, "protein": 6, "sodium": 375, "fiber": 0, "sugar": 0}},
    "gorgonzola cheese": {"oz": {"cal": 100, "fat": 9, "carbs": 1, "protein": 6, "sodium": 375, "fiber": 0, "sugar": 0}},
    "string cheese": {"each": {"cal": 80, "fat": 6, "carbs": 1, "protein": 7, "sodium": 200, "fiber": 0, "sugar": 0}},
    "mozzarella string cheese": {"each": {"cal": 80, "fat": 6, "carbs": 1, "protein": 7, "sodium": 200, "fiber": 0, "sugar": 0}},
    "crème fraîche": {"cup": {"cal": 450, "fat": 45, "carbs": 3, "protein": 3, "sodium": 40, "fiber": 0, "sugar": 3},
                     "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.2, "protein": 0.2, "sodium": 2, "fiber": 0, "sugar": 0.2}},
    "creme fraiche": {"cup": {"cal": 450, "fat": 45, "carbs": 3, "protein": 3, "sodium": 40, "fiber": 0, "sugar": 3},
                     "tbsp": {"cal": 28, "fat": 2.8, "carbs": 0.2, "protein": 0.2, "sodium": 2, "fiber": 0, "sugar": 0.2}},
    "ice cream": {"cup": {"cal": 273, "fat": 15, "carbs": 31, "protein": 5, "sodium": 100, "fiber": 0.7, "sugar": 28}},
    "vanilla ice cream": {"cup": {"cal": 273, "fat": 15, "carbs": 31, "protein": 5, "sodium": 100, "fiber": 0.7, "sugar": 28}},
    "sweetened condensed milk": {"can": {"cal": 982, "fat": 27, "carbs": 166, "protein": 24, "sodium": 389, "fiber": 0, "sugar": 166}},
    "mascarpone": {"cup": {"cal": 920, "fat": 96, "carbs": 4, "protein": 8, "sodium": 80, "fiber": 0, "sugar": 4}},
    "queso fresco": {"oz": {"cal": 80, "fat": 6, "carbs": 1, "protein": 5, "sodium": 180, "fiber": 0, "sugar": 0}},

    # Produce - vegetables
    "artichoke": {"each": {"cal": 60, "fat": 0.2, "carbs": 13, "protein": 4, "sodium": 120, "fiber": 6.5, "sugar": 1}},
    "artichoke hearts": {"cup": {"cal": 90, "fat": 0.3, "carbs": 20, "protein": 6, "sodium": 180, "fiber": 9, "sugar": 2}},
    "parsnips": {"cup": {"cal": 100, "fat": 0.4, "carbs": 24, "protein": 1.6, "sodium": 13, "fiber": 6.5, "sugar": 6}},
    "parsnip": {"cup": {"cal": 100, "fat": 0.4, "carbs": 24, "protein": 1.6, "sodium": 13, "fiber": 6.5, "sugar": 6}},
    "radish": {"cup": {"cal": 19, "fat": 0.1, "carbs": 4, "protein": 0.8, "sodium": 45, "fiber": 1.9, "sugar": 2}},
    "radishes": {"cup": {"cal": 19, "fat": 0.1, "carbs": 4, "protein": 0.8, "sodium": 45, "fiber": 1.9, "sugar": 2}},
    "turnip": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 1, "sodium": 87, "fiber": 2.3, "sugar": 5}},
    "turnips": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 1, "sodium": 87, "fiber": 2.3, "sugar": 5}},
    "watercress": {"cup": {"cal": 4, "fat": 0, "carbs": 0.4, "protein": 0.8, "sodium": 14, "fiber": 0.2, "sugar": 0.1}},
    "shallot": {"tbsp": {"cal": 7, "fat": 0, "carbs": 2, "protein": 0.3, "sodium": 1, "fiber": 0, "sugar": 0.8},
               "": {"cal": 28, "fat": 0, "carbs": 7, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 3}},
    "shallots": {"tbsp": {"cal": 7, "fat": 0, "carbs": 2, "protein": 0.3, "sodium": 1, "fiber": 0, "sugar": 0.8},
                "": {"cal": 28, "fat": 0, "carbs": 7, "protein": 1, "sodium": 5, "fiber": 0, "sugar": 3}},
    "leek": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "leeks": {"cup": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "fennel": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 45, "fiber": 3, "sugar": 3}},
    "fennel bulb": {"cup": {"cal": 27, "fat": 0.2, "carbs": 6, "protein": 1, "sodium": 45, "fiber": 3, "sugar": 3}},
    "rutabaga": {"cup": {"cal": 52, "fat": 0.3, "carbs": 12, "protein": 1.5, "sodium": 28, "fiber": 3, "sugar": 7}},
    "kohlrabi": {"cup": {"cal": 36, "fat": 0.1, "carbs": 8, "protein": 2, "sodium": 27, "fiber": 5, "sugar": 4}},
    "jicama": {"cup": {"cal": 46, "fat": 0.1, "carbs": 11, "protein": 0.9, "sodium": 5, "fiber": 6, "sugar": 2}},
    "bok choy": {"cup": {"cal": 9, "fat": 0.1, "carbs": 1.5, "protein": 1, "sodium": 46, "fiber": 0.7, "sugar": 0.8}},
    "swiss chard": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1.4, "protein": 0.6, "sodium": 77, "fiber": 0.6, "sugar": 0.4}},
    "collard greens": {"cup": {"cal": 11, "fat": 0.2, "carbs": 2, "protein": 1, "sodium": 6, "fiber": 1.4, "sugar": 0.2}},
    "mustard greens": {"cup": {"cal": 15, "fat": 0.2, "carbs": 3, "protein": 1.5, "sodium": 14, "fiber": 2, "sugar": 0.8}},

    # Produce - fruits
    "blackberries": {"cup": {"cal": 62, "fat": 0.7, "carbs": 14, "protein": 2, "sodium": 1, "fiber": 7.6, "sugar": 7}},
    "cantaloupe": {"cup": {"cal": 53, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 25, "fiber": 1.4, "sugar": 12}},
    "figs": {"each": {"cal": 37, "fat": 0.2, "carbs": 10, "protein": 0.4, "sodium": 1, "fiber": 1.5, "sugar": 8}},
    "dried figs": {"cup": {"cal": 371, "fat": 1.4, "carbs": 95, "protein": 5, "sodium": 14, "fiber": 14.6, "sugar": 71}},
    "honeydew": {"cup": {"cal": 61, "fat": 0.2, "carbs": 15, "protein": 0.9, "sodium": 30, "fiber": 1.4, "sugar": 14}},
    "honeydew melon": {"cup": {"cal": 61, "fat": 0.2, "carbs": 15, "protein": 0.9, "sodium": 30, "fiber": 1.4, "sugar": 14}},
    "kiwi": {"each": {"cal": 42, "fat": 0.4, "carbs": 10, "protein": 0.8, "sodium": 2, "fiber": 2.1, "sugar": 6}},
    "kiwi fruit": {"each": {"cal": 42, "fat": 0.4, "carbs": 10, "protein": 0.8, "sodium": 2, "fiber": 2.1, "sugar": 6}},
    "mango": {"each": {"cal": 202, "fat": 1.3, "carbs": 50, "protein": 2.8, "sodium": 3, "fiber": 5.4, "sugar": 45}},
    "papaya": {"cup": {"cal": 55, "fat": 0.2, "carbs": 14, "protein": 0.8, "sodium": 4, "fiber": 2.5, "sugar": 8}},
    "passion fruit": {"each": {"cal": 17, "fat": 0.1, "carbs": 4, "protein": 0.4, "sodium": 5, "fiber": 1.9, "sugar": 2}},
    "pomegranate": {"each": {"cal": 234, "fat": 3.3, "carbs": 53, "protein": 4.7, "sodium": 8, "fiber": 11, "sugar": 39}},
    "pomegranate seeds": {"cup": {"cal": 144, "fat": 2, "carbs": 33, "protein": 3, "sodium": 5, "fiber": 7, "sugar": 24}},
    "persimmon": {"each": {"cal": 118, "fat": 0.3, "carbs": 31, "protein": 1, "sodium": 2, "fiber": 6, "sugar": 21}},
    "guava": {"each": {"cal": 37, "fat": 0.5, "carbs": 8, "protein": 1.4, "sodium": 1, "fiber": 3, "sugar": 5}},
    "star fruit": {"each": {"cal": 28, "fat": 0.3, "carbs": 6, "protein": 1, "sodium": 2, "fiber": 2.5, "sugar": 4}},
    "tangerine": {"each": {"cal": 47, "fat": 0.3, "carbs": 12, "protein": 0.7, "sodium": 2, "fiber": 1.6, "sugar": 9}},
    "clementine": {"each": {"cal": 35, "fat": 0.1, "carbs": 9, "protein": 0.6, "sodium": 1, "fiber": 1.3, "sugar": 7}},
    "nectarine": {"each": {"cal": 63, "fat": 0.5, "carbs": 15, "protein": 1.5, "sodium": 0, "fiber": 2.4, "sugar": 11}},
    "plantain": {"each": {"cal": 218, "fat": 0.5, "carbs": 57, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 27}},

    # Grains
    "stuffing mix": {"cup": {"cal": 356, "fat": 17, "carbs": 44, "protein": 6, "sodium": 1086, "fiber": 3, "sugar": 4}},
    "corn flakes": {"cup": {"cal": 101, "fat": 0.2, "carbs": 24, "protein": 2, "sodium": 203, "fiber": 0.7, "sugar": 3}},
    "bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "wheat bran": {"cup": {"cal": 125, "fat": 2.5, "carbs": 37, "protein": 9, "sodium": 1, "fiber": 25, "sugar": 0}},
    "oat bran": {"cup": {"cal": 231, "fat": 6.5, "carbs": 62, "protein": 16, "sodium": 4, "fiber": 14.5, "sugar": 1}},
    "wild rice": {"cup": {"cal": 166, "fat": 0.6, "carbs": 35, "protein": 6.5, "sodium": 5, "fiber": 3, "sugar": 1}},
    "grits": {"cup": {"cal": 143, "fat": 0.5, "carbs": 31, "protein": 3, "sodium": 5, "fiber": 1, "sugar": 0}},
    "polenta": {"cup": {"cal": 143, "fat": 0.5, "carbs": 31, "protein": 3, "sodium": 5, "fiber": 1, "sugar": 0}},
    "couscous": {"cup": {"cal": 176, "fat": 0.3, "carbs": 36, "protein": 6, "sodium": 8, "fiber": 2.2, "sugar": 0}},
    "quinoa": {"cup": {"cal": 222, "fat": 4, "carbs": 39, "protein": 8, "sodium": 13, "fiber": 5, "sugar": 0}},
    "bulgur": {"cup": {"cal": 151, "fat": 0.4, "carbs": 34, "protein": 6, "sodium": 9, "fiber": 8, "sugar": 0}},
    "farro": {"cup": {"cal": 200, "fat": 1.5, "carbs": 40, "protein": 8, "sodium": 0, "fiber": 5, "sugar": 0}},
    "barley": {"cup": {"cal": 193, "fat": 0.7, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 6, "sugar": 0.4}},
    "pearl barley": {"cup": {"cal": 193, "fat": 0.7, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 6, "sugar": 0.4}},
    "millet": {"cup": {"cal": 207, "fat": 1.7, "carbs": 41, "protein": 6, "sodium": 3, "fiber": 2.3, "sugar": 0}},
    "buckwheat": {"cup": {"cal": 155, "fat": 1, "carbs": 34, "protein": 6, "sodium": 7, "fiber": 4.5, "sugar": 0}},
    "orzo": {"cup": {"cal": 200, "fat": 0.9, "carbs": 42, "protein": 7, "sodium": 0, "fiber": 2, "sugar": 0}},

    # Nuts & seeds
    "macadamia nuts": {"cup": {"cal": 962, "fat": 102, "carbs": 18, "protein": 10, "sodium": 6, "fiber": 11, "sugar": 6}},
    "macadamias": {"cup": {"cal": 962, "fat": 102, "carbs": 18, "protein": 10, "sodium": 6, "fiber": 11, "sugar": 6}},
    "pine nuts": {"cup": {"cal": 909, "fat": 92, "carbs": 18, "protein": 18, "sodium": 3, "fiber": 5, "sugar": 5}},
    "pignoli": {"cup": {"cal": 909, "fat": 92, "carbs": 18, "protein": 18, "sodium": 3, "fiber": 5, "sugar": 5}},
    "hazelnuts": {"cup": {"cal": 848, "fat": 82, "carbs": 23, "protein": 20, "sodium": 0, "fiber": 13, "sugar": 6}},
    "filberts": {"cup": {"cal": 848, "fat": 82, "carbs": 23, "protein": 20, "sodium": 0, "fiber": 13, "sugar": 6}},
    "pistachios": {"cup": {"cal": 685, "fat": 55, "carbs": 34, "protein": 25, "sodium": 1, "fiber": 13, "sugar": 9}},
    "poppy seeds": {"tbsp": {"cal": 46, "fat": 4, "carbs": 2, "protein": 1.6, "sodium": 2, "fiber": 0.5, "sugar": 0.3}},
    "tahini": {"tbsp": {"cal": 89, "fat": 8, "carbs": 3, "protein": 2.6, "sodium": 17, "fiber": 0.7, "sugar": 0}},
    "sesame paste": {"tbsp": {"cal": 89, "fat": 8, "carbs": 3, "protein": 2.6, "sodium": 17, "fiber": 0.7, "sugar": 0}},
    "pumpkin seeds": {"cup": {"cal": 285, "fat": 12, "carbs": 34, "protein": 12, "sodium": 12, "fiber": 12, "sugar": 0}},
    "pepitas": {"cup": {"cal": 285, "fat": 12, "carbs": 34, "protein": 12, "sodium": 12, "fiber": 12, "sugar": 0}},
    "chia seeds": {"tbsp": {"cal": 58, "fat": 4, "carbs": 5, "protein": 2, "sodium": 2, "fiber": 4, "sugar": 0}},
    "hemp seeds": {"tbsp": {"cal": 57, "fat": 4, "carbs": 1, "protein": 3, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # Canned goods
    "rotel": {"can": {"cal": 50, "fat": 0, "carbs": 10, "protein": 2, "sodium": 890, "fiber": 2, "sugar": 6}},
    "bamboo shoots": {"cup": {"cal": 25, "fat": 0.5, "carbs": 4, "protein": 2.5, "sodium": 9, "fiber": 2, "sugar": 3}},
    "water chestnuts": {"cup": {"cal": 60, "fat": 0.1, "carbs": 15, "protein": 1, "sodium": 9, "fiber": 2, "sugar": 3}},
    "fruit cocktail": {"cup": {"cal": 110, "fat": 0, "carbs": 28, "protein": 0.5, "sodium": 10, "fiber": 2.5, "sugar": 26}},
    "mandarin oranges": {"cup": {"cal": 72, "fat": 0.1, "carbs": 19, "protein": 1, "sodium": 12, "fiber": 1.8, "sugar": 16}},
    "crushed pineapple": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "pineapple chunks": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "pineapple tidbits": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "sliced pineapple": {"cup": {"cal": 109, "fat": 0.2, "carbs": 28, "protein": 0.8, "sodium": 2, "fiber": 2, "sugar": 25}},
    "hearts of palm": {"cup": {"cal": 41, "fat": 0.9, "carbs": 7, "protein": 4, "sodium": 622, "fiber": 3.5, "sugar": 0}},
    "palm hearts": {"cup": {"cal": 41, "fat": 0.9, "carbs": 7, "protein": 4, "sodium": 622, "fiber": 3.5, "sugar": 0}},

    # Sauces & condiments
    "pesto": {"tbsp": {"cal": 80, "fat": 8, "carbs": 1, "protein": 2, "sodium": 125, "fiber": 0, "sugar": 0}},
    "basil pesto": {"tbsp": {"cal": 80, "fat": 8, "carbs": 1, "protein": 2, "sodium": 125, "fiber": 0, "sugar": 0}},
    "sun-dried tomato pesto": {"tbsp": {"cal": 70, "fat": 6, "carbs": 3, "protein": 1, "sodium": 160, "fiber": 0.5, "sugar": 2}},
    "aioli": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0.5, "protein": 0.3, "sodium": 110, "fiber": 0, "sugar": 0}},
    "chipotle mayo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0.5, "protein": 0.1, "sodium": 140, "fiber": 0, "sugar": 0}},
    "sriracha mayo": {"tbsp": {"cal": 100, "fat": 11, "carbs": 1, "protein": 0.1, "sodium": 160, "fiber": 0, "sugar": 0.5}},
    "tartar sauce": {"tbsp": {"cal": 74, "fat": 8, "carbs": 1, "protein": 0.2, "sodium": 107, "fiber": 0, "sugar": 1}},
    "cocktail sauce": {"tbsp": {"cal": 20, "fat": 0, "carbs": 5, "protein": 0.3, "sodium": 270, "fiber": 0, "sugar": 4}},
    "hoisin sauce": {"tbsp": {"cal": 35, "fat": 0.5, "carbs": 7, "protein": 0.5, "sodium": 258, "fiber": 0.4, "sugar": 5}},
    "fish sauce": {"tbsp": {"cal": 6, "fat": 0, "carbs": 0.7, "protein": 0.9, "sodium": 1413, "fiber": 0, "sugar": 0}},
    "oyster sauce": {"tbsp": {"cal": 9, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 492, "fiber": 0, "sugar": 1}},
    "miso paste": {"tbsp": {"cal": 34, "fat": 1, "carbs": 4.5, "protein": 2, "sodium": 634, "fiber": 0.9, "sugar": 1}},
    "white miso": {"tbsp": {"cal": 34, "fat": 1, "carbs": 4.5, "protein": 2, "sodium": 634, "fiber": 0.9, "sugar": 1}},
    "red miso": {"tbsp": {"cal": 35, "fat": 1, "carbs": 5, "protein": 2, "sodium": 750, "fiber": 1, "sugar": 1}},
    "sambal oelek": {"tbsp": {"cal": 15, "fat": 0, "carbs": 3, "protein": 0.5, "sodium": 600, "fiber": 1, "sugar": 1}},
    "gochujang": {"tbsp": {"cal": 40, "fat": 1, "carbs": 8, "protein": 1, "sodium": 410, "fiber": 1, "sugar": 4}},
    "harissa": {"tbsp": {"cal": 15, "fat": 0.5, "carbs": 2.5, "protein": 0.5, "sodium": 95, "fiber": 0.5, "sugar": 1}},
    "chili garlic sauce": {"tbsp": {"cal": 20, "fat": 0.5, "carbs": 4, "protein": 0.5, "sodium": 450, "fiber": 0.5, "sugar": 2}},
    "duck sauce": {"tbsp": {"cal": 60, "fat": 0, "carbs": 15, "protein": 0, "sodium": 75, "fiber": 0, "sugar": 13}},
    "plum sauce": {"tbsp": {"cal": 35, "fat": 0, "carbs": 8, "protein": 0.2, "sodium": 180, "fiber": 0.2, "sugar": 6}},
    "sweet chili sauce": {"tbsp": {"cal": 40, "fat": 0, "carbs": 10, "protein": 0.1, "sodium": 220, "fiber": 0, "sugar": 9}},
    "ponzu": {"tbsp": {"cal": 10, "fat": 0, "carbs": 2, "protein": 0.5, "sodium": 600, "fiber": 0, "sugar": 1}},

    # Prepared foods
    "pizza dough": {"lb": {"cal": 1100, "fat": 6, "carbs": 220, "protein": 32, "sodium": 1600, "fiber": 8, "sugar": 4}},
    "pie crust": {"each": {"cal": 620, "fat": 39, "carbs": 60, "protein": 7, "sodium": 420, "fiber": 2, "sugar": 2}},
    "puff pastry": {"sheet": {"cal": 850, "fat": 56, "carbs": 72, "protein": 11, "sodium": 420, "fiber": 2, "sugar": 1}},
    "phyllo dough": {"sheet": {"cal": 57, "fat": 1, "carbs": 10, "protein": 1.4, "sodium": 92, "fiber": 0.4, "sugar": 0}},
    "wonton wrappers": {"each": {"cal": 23, "fat": 0.4, "carbs": 4.6, "protein": 0.8, "sodium": 46, "fiber": 0.2, "sugar": 0}},
    "egg roll wrappers": {"each": {"cal": 93, "fat": 1.6, "carbs": 18, "protein": 3, "sodium": 183, "fiber": 0.6, "sugar": 0}},
    "tortilla chips": {"cup": {"cal": 200, "fat": 10, "carbs": 24, "protein": 2.5, "sodium": 170, "fiber": 2, "sugar": 0.5}},
    "croutons": {"cup": {"cal": 122, "fat": 2, "carbs": 22, "protein": 4, "sodium": 210, "fiber": 1.5, "sugar": 1}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 3 (most common missing ingredients)
    # =========================================================================

    # Syrups & sweeteners
    "light corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 395, "fiber": 0, "sugar": 251}},
    "dark corn syrup": {"cup": {"cal": 925, "fat": 0, "carbs": 251, "protein": 0, "sodium": 210, "fiber": 0, "sugar": 251}},
    "superfine sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "caster sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "raw sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "turbinado sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "demerara sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},
    "muscovado sugar": {"cup": {"cal": 760, "fat": 0, "carbs": 196, "protein": 0, "sodium": 6, "fiber": 0, "sugar": 196}},

    # Dried fruits
    "currants": {"cup": {"cal": 408, "fat": 0.4, "carbs": 107, "protein": 6, "sodium": 12, "fiber": 10, "sugar": 93}},
    "dried currants": {"cup": {"cal": 408, "fat": 0.4, "carbs": 107, "protein": 6, "sodium": 12, "fiber": 10, "sugar": 93}},
    "citron": {"cup": {"cal": 320, "fat": 0.3, "carbs": 82, "protein": 0.5, "sodium": 290, "fiber": 5, "sugar": 73}},
    "candied citron": {"cup": {"cal": 320, "fat": 0.3, "carbs": 82, "protein": 0.5, "sodium": 290, "fiber": 5, "sugar": 73}},
    "maraschino cherries": {"each": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 2}},
    "candied cherries": {"cup": {"cal": 160, "fat": 0, "carbs": 40, "protein": 0, "sodium": 30, "fiber": 0, "sugar": 36}},

    # Condiments & sauces
    "catsup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "ketchup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "dijon mustard": {"tbsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 1, "sodium": 360, "fiber": 0.5, "sugar": 0}},
    "prepared mustard": {"tbsp": {"cal": 10, "fat": 0.6, "carbs": 0.8, "protein": 0.6, "sodium": 168, "fiber": 0.4, "sugar": 0.3}},
    "yellow mustard": {"tbsp": {"cal": 10, "fat": 0.6, "carbs": 0.8, "protein": 0.6, "sodium": 168, "fiber": 0.4, "sugar": 0.3}},
    "stone ground mustard": {"tbsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 1, "sodium": 200, "fiber": 0.5, "sugar": 0}},
    "salad dressing": {"tbsp": {"cal": 60, "fat": 5, "carbs": 3, "protein": 0, "sodium": 160, "fiber": 0, "sugar": 2}},
    "thousand island dressing": {"tbsp": {"cal": 59, "fat": 5.6, "carbs": 2.4, "protein": 0.1, "sodium": 138, "fiber": 0, "sugar": 2}},
    "ranch dressing": {"tbsp": {"cal": 73, "fat": 7.7, "carbs": 0.5, "protein": 0.1, "sodium": 122, "fiber": 0, "sugar": 0.4}},
    "blue cheese dressing": {"tbsp": {"cal": 77, "fat": 8, "carbs": 0.6, "protein": 0.4, "sodium": 167, "fiber": 0, "sugar": 0.5}},
    "italian dressing": {"tbsp": {"cal": 35, "fat": 3, "carbs": 1.5, "protein": 0, "sodium": 146, "fiber": 0, "sugar": 1}},
    "sweet pickle": {"each": {"cal": 32, "fat": 0, "carbs": 9, "protein": 0.1, "sodium": 160, "fiber": 0.3, "sugar": 7}},
    "sweet pickle relish": {"tbsp": {"cal": 20, "fat": 0.1, "carbs": 5, "protein": 0.1, "sodium": 122, "fiber": 0.2, "sugar": 4}},
    "dill pickle relish": {"tbsp": {"cal": 4, "fat": 0.1, "carbs": 1, "protein": 0, "sodium": 210, "fiber": 0.2, "sugar": 0.5}},

    # Vegetables
    "pimiento": {"oz": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8}},
    "pimentos": {"oz": {"cal": 6, "fat": 0.1, "carbs": 1.3, "protein": 0.2, "sodium": 4, "fiber": 0.4, "sugar": 0.8}},
    "green peppers": {"cup": {"cal": 30, "fat": 0.3, "carbs": 7, "protein": 1.3, "sodium": 4, "fiber": 2.5, "sugar": 4}},
    "red peppers": {"cup": {"cal": 39, "fat": 0.4, "carbs": 9, "protein": 1.5, "sodium": 6, "fiber": 3, "sugar": 6}},
    "apples": {"each": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4.4, "sugar": 19}},
    "apple": {"each": {"cal": 95, "fat": 0.3, "carbs": 25, "protein": 0.5, "sodium": 2, "fiber": 4.4, "sugar": 19}},
    "bananas": {"each": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3.1, "sugar": 14}},
    "banana": {"each": {"cal": 105, "fat": 0.4, "carbs": 27, "protein": 1.3, "sodium": 1, "fiber": 3.1, "sugar": 14}},
    "peaches": {"each": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 13}},
    "peach": {"each": {"cal": 59, "fat": 0.4, "carbs": 14, "protein": 1.4, "sodium": 0, "fiber": 2.3, "sugar": 13}},

    # Dairy & cream
    "light cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "coffee cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "table cream": {"cup": {"cal": 468, "fat": 46, "carbs": 9, "protein": 6, "sodium": 95, "fiber": 0, "sugar": 9}},
    "sour milk": {"cup": {"cal": 98, "fat": 2.4, "carbs": 12, "protein": 8, "sodium": 257, "fiber": 0, "sugar": 12}},
    "buttermilk powder": {"tbsp": {"cal": 25, "fat": 0.4, "carbs": 3, "protein": 2, "sodium": 34, "fiber": 0, "sugar": 3}},
    "rich milk": {"cup": {"cal": 150, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "plain yogurt": {"cup": {"cal": 149, "fat": 8, "carbs": 11, "protein": 9, "sodium": 113, "fiber": 0, "sugar": 11}},
    "greek yogurt": {"cup": {"cal": 190, "fat": 10, "carbs": 8, "protein": 18, "sodium": 65, "fiber": 0, "sugar": 7}},

    # Cheese variations
    "sharp cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},
    "mild cheddar cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 621, "fiber": 0, "sugar": 0.5}},
    "monterey jack cheese": {"cup": {"cal": 421, "fat": 34, "carbs": 0.7, "protein": 28, "sodium": 603, "fiber": 0, "sugar": 0.5}},
    "pepper jack cheese": {"cup": {"cal": 421, "fat": 34, "carbs": 0.7, "protein": 28, "sodium": 650, "fiber": 0, "sugar": 0.5}},
    "colby cheese": {"cup": {"cal": 445, "fat": 36, "carbs": 2.9, "protein": 27, "sodium": 684, "fiber": 0, "sugar": 0.5}},
    "american cheese": {"slice": {"cal": 104, "fat": 9, "carbs": 0.5, "protein": 5, "sodium": 406, "fiber": 0, "sugar": 0.3}},
    "velveeta": {"oz": {"cal": 80, "fat": 6, "carbs": 3, "protein": 4, "sodium": 410, "fiber": 0, "sugar": 2}},

    # Spices & seasonings
    "cayenne": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "cayenne pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "mace": {"tsp": {"cal": 8, "fat": 0.6, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "ground mace": {"tsp": {"cal": 8, "fat": 0.6, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 0}},
    "whole cloves": {"tsp": {"cal": 7, "fat": 0.4, "carbs": 1.3, "protein": 0.1, "sodium": 5, "fiber": 0.7, "sugar": 0.5}},
    "celery seed": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 0.8, "protein": 0.4, "sodium": 3, "fiber": 0.2, "sugar": 0}},
    "celery salt": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 0.6, "protein": 0.3, "sodium": 1280, "fiber": 0.2, "sugar": 0}},
    "cinnamon stick": {"each": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1.4, "sugar": 0}},
    "cinnamon sticks": {"each": {"cal": 6, "fat": 0, "carbs": 2, "protein": 0.1, "sodium": 0, "fiber": 1.4, "sugar": 0}},
    "red pepper flakes": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.5, "sugar": 0.2}},
    "crushed red pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0.5, "sugar": 0.2}},
    "ground coriander": {"tsp": {"cal": 5, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.8, "sugar": 0}},
    "freshly grated nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0.1}},
    "cream tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 1.8, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},
    "cream of tartar": {"tsp": {"cal": 8, "fat": 0, "carbs": 1.8, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Flavorings
    "rose water": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "rose-water": {"tbsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "orange extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "lemon extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "almond extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "peppermint extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "rum extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "maple extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "coconut extract": {"tsp": {"cal": 12, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Flours & starches
    "pastry flour": {"cup": {"cal": 400, "fat": 1, "carbs": 84, "protein": 9, "sodium": 2, "fiber": 2, "sugar": 0}},
    "whole wheat pastry flour": {"cup": {"cal": 400, "fat": 2, "carbs": 80, "protein": 12, "sodium": 2, "fiber": 12, "sugar": 0}},
    "cake flour": {"cup": {"cal": 400, "fat": 1, "carbs": 85, "protein": 8, "sodium": 2, "fiber": 2, "sugar": 0}},
    "bread flour": {"cup": {"cal": 495, "fat": 1.5, "carbs": 99, "protein": 16, "sodium": 2, "fiber": 3, "sugar": 0}},
    "self-rising flour": {"cup": {"cal": 443, "fat": 1.2, "carbs": 93, "protein": 12, "sodium": 1588, "fiber": 3, "sugar": 0}},
    "yellow cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "white cornmeal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "corn meal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "indian meal": {"cup": {"cal": 442, "fat": 4, "carbs": 94, "protein": 10, "sodium": 4, "fiber": 9, "sugar": 1}},
    "corn starch": {"tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tapioca starch": {"tbsp": {"cal": 30, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "arrowroot": {"tbsp": {"cal": 29, "fat": 0, "carbs": 7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "dry bread crumbs": {"cup": {"cal": 427, "fat": 6, "carbs": 78, "protein": 14, "sodium": 791, "fiber": 5, "sugar": 6}},
    "panko": {"cup": {"cal": 220, "fat": 2, "carbs": 44, "protein": 6, "sodium": 300, "fiber": 2, "sugar": 2}},
    "panko bread crumbs": {"cup": {"cal": 220, "fat": 2, "carbs": 44, "protein": 6, "sodium": 300, "fiber": 2, "sugar": 2}},

    # Fats & oils
    "salad oil": {"tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "drippings": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bacon drippings": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bacon grease": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "fat": {"tbsp": {"cal": 115, "fat": 13, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "salt pork": {"oz": {"cal": 212, "fat": 23, "carbs": 0, "protein": 1.4, "sodium": 404, "fiber": 0, "sugar": 0}},
    "fatback": {"oz": {"cal": 212, "fat": 23, "carbs": 0, "protein": 1.4, "sodium": 404, "fiber": 0, "sugar": 0}},
    "suet": {"oz": {"cal": 242, "fat": 27, "carbs": 0, "protein": 0.4, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Meats
    "chicken wings": {"lb": {"cal": 960, "fat": 68, "carbs": 0, "protein": 80, "sodium": 360, "fiber": 0, "sugar": 0}},
    "chicken wing": {"each": {"cal": 43, "fat": 3, "carbs": 0, "protein": 4, "sodium": 16, "fiber": 0, "sugar": 0}},
    "ground italian sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 4, "protein": 68, "sodium": 1500, "fiber": 0, "sugar": 0}},
    "italian sausage links": {"each": {"cal": 286, "fat": 23, "carbs": 1, "protein": 16, "sodium": 756, "fiber": 0, "sugar": 0}},
    "breakfast sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 0, "protein": 64, "sodium": 1400, "fiber": 0, "sugar": 0}},
    "polish sausage": {"lb": {"cal": 1280, "fat": 104, "carbs": 8, "protein": 68, "sodium": 2800, "fiber": 0, "sugar": 0}},
    "kielbasa": {"lb": {"cal": 1280, "fat": 104, "carbs": 8, "protein": 68, "sodium": 2800, "fiber": 0, "sugar": 0}},
    "andouille sausage": {"lb": {"cal": 1200, "fat": 96, "carbs": 8, "protein": 68, "sodium": 3200, "fiber": 0, "sugar": 0}},
    "chorizo": {"lb": {"cal": 1550, "fat": 132, "carbs": 8, "protein": 72, "sodium": 2700, "fiber": 0, "sugar": 0}},

    # Rice & grains
    "instant rice": {"cup": {"cal": 190, "fat": 0.4, "carbs": 42, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "minute rice": {"cup": {"cal": 190, "fat": 0.4, "carbs": 42, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "converted rice": {"cup": {"cal": 200, "fat": 0.5, "carbs": 44, "protein": 4, "sodium": 5, "fiber": 1, "sugar": 0}},
    "arborio rice": {"cup": {"cal": 200, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 0, "fiber": 1, "sugar": 0}},
    "jasmine rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "basmati rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "sushi rice": {"cup": {"cal": 200, "fat": 0.4, "carbs": 44, "protein": 4, "sodium": 0, "fiber": 0.6, "sugar": 0}},

    # Canned goods
    "tomato sauce": {"cup": {"cal": 59, "fat": 0.5, "carbs": 13, "protein": 2.6, "sodium": 1116, "fiber": 3, "sugar": 9}},
    "mushrooms": {"cup": {"cal": 15, "fat": 0.2, "carbs": 2.3, "protein": 2.2, "sodium": 4, "fiber": 0.7, "sugar": 1}},
    "canned mushrooms": {"cup": {"cal": 33, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 561, "fiber": 2, "sugar": 2}},

    # Wine & alcohol
    "dry white wine": {"cup": {"cal": 194, "fat": 0, "carbs": 5, "protein": 0, "sodium": 10, "fiber": 0, "sugar": 1}},
    "dry sherry": {"cup": {"cal": 255, "fat": 0, "carbs": 10, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 2}},
    "cooking sherry": {"cup": {"cal": 225, "fat": 0, "carbs": 8, "protein": 0, "sodium": 1100, "fiber": 0, "sugar": 4}},
    "marsala wine": {"cup": {"cal": 320, "fat": 0, "carbs": 28, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 18}},
    "port wine": {"cup": {"cal": 370, "fat": 0, "carbs": 36, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 30}},
    "madeira wine": {"cup": {"cal": 330, "fat": 0, "carbs": 32, "protein": 0, "sodium": 20, "fiber": 0, "sugar": 20}},
    "sake": {"cup": {"cal": 195, "fat": 0, "carbs": 7.5, "protein": 0.7, "sodium": 3, "fiber": 0, "sugar": 0}},

    # Chocolate & cocoa
    "semisweet chocolate": {"oz": {"cal": 136, "fat": 9, "carbs": 15, "protein": 1.2, "sodium": 2, "fiber": 1.8, "sugar": 13}},
    "bittersweet chocolate": {"oz": {"cal": 136, "fat": 9, "carbs": 13, "protein": 1.4, "sodium": 4, "fiber": 2, "sugar": 10}},
    "unsweetened chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},
    "baking chocolate": {"oz": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},
    "white chocolate": {"oz": {"cal": 153, "fat": 9, "carbs": 17, "protein": 1.5, "sodium": 25, "fiber": 0, "sugar": 17}},
    "german chocolate": {"oz": {"cal": 140, "fat": 8, "carbs": 16, "protein": 1, "sodium": 5, "fiber": 1.5, "sugar": 14}},
    "dutch-process cocoa powder": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 0}},
    "natural cocoa powder": {"tbsp": {"cal": 12, "fat": 0.7, "carbs": 3, "protein": 1, "sodium": 0, "fiber": 2, "sugar": 0}},

    # Miscellaneous
    "pistachio nuts": {"cup": {"cal": 685, "fat": 55, "carbs": 34, "protein": 25, "sodium": 1, "fiber": 13, "sugar": 9}},
    "slivered almonds": {"cup": {"cal": 624, "fat": 54, "carbs": 22, "protein": 23, "sodium": 1, "fiber": 12, "sugar": 5}},
    "sliced almonds": {"cup": {"cal": 530, "fat": 46, "carbs": 18, "protein": 20, "sodium": 1, "fiber": 10, "sugar": 4}},
    "almond meal": {"cup": {"cal": 640, "fat": 56, "carbs": 24, "protein": 24, "sodium": 0, "fiber": 14, "sugar": 5}},
    "lukewarm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "warm water": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0.1}},
    "apple cider vinegar": {"tbsp": {"cal": 3, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 0.1}},
    "kitchen bouquet": {"tsp": {"cal": 15, "fat": 0, "carbs": 4, "protein": 0, "sodium": 10, "fiber": 0, "sugar": 3}},
    "truvia": {"packet": {"cal": 0, "fat": 0, "carbs": 3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "truvia natural sweetener": {"packet": {"cal": 0, "fat": 0, "carbs": 3, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "truvia natural sweetener spoonable": {"tsp": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "splenda": {"packet": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "stevia": {"packet": {"cal": 0, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 4 (remaining missing ingredients)
    # =========================================================================

    # Vegetables
    "sweet potatoes": {"lb": {"cal": 390, "fat": 0.4, "carbs": 90, "protein": 7, "sodium": 250, "fiber": 14, "sugar": 18}},
    "sweet potato": {"each": {"cal": 112, "fat": 0.1, "carbs": 26, "protein": 2, "sodium": 72, "fiber": 4, "sugar": 5}},
    "acorn squash": {"cup": {"cal": 56, "fat": 0.1, "carbs": 15, "protein": 1, "sodium": 4, "fiber": 2, "sugar": 0}},
    "butternut squash": {"cup": {"cal": 63, "fat": 0.1, "carbs": 16, "protein": 1.4, "sodium": 6, "fiber": 2.8, "sugar": 3}},
    "spaghetti squash": {"cup": {"cal": 31, "fat": 0.6, "carbs": 7, "protein": 0.6, "sodium": 17, "fiber": 1.5, "sugar": 2.5}},
    "button mushrooms": {"cup": {"cal": 15, "fat": 0.2, "carbs": 2.3, "protein": 2.2, "sodium": 4, "fiber": 0.7, "sugar": 1}},
    "black olives": {"cup": {"cal": 142, "fat": 13, "carbs": 8, "protein": 1, "sodium": 735, "fiber": 3, "sugar": 0}},
    "green olives": {"cup": {"cal": 145, "fat": 15, "carbs": 4, "protein": 1, "sodium": 1556, "fiber": 3, "sugar": 0}},
    "kalamata olives": {"cup": {"cal": 196, "fat": 17, "carbs": 10, "protein": 2, "sodium": 1840, "fiber": 3, "sugar": 0}},
    "plum tomato": {"each": {"cal": 11, "fat": 0.1, "carbs": 2.4, "protein": 0.5, "sodium": 3, "fiber": 0.7, "sugar": 1.6}},
    "stalk celery": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "celery stalks": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},

    # Nuts & seeds
    "blanched almonds": {"cup": {"cal": 624, "fat": 54, "carbs": 22, "protein": 23, "sodium": 1, "fiber": 12, "sugar": 5}},
    "nut meats": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "walnut meats": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "fennel seeds": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0}},
    "mustard seeds": {"tsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 0.8, "sodium": 0, "fiber": 0.4, "sugar": 0}},

    # Proteins
    "cooked chicken": {"cup": {"cal": 231, "fat": 5, "carbs": 0, "protein": 43, "sodium": 104, "fiber": 0, "sugar": 0}},
    "frying chicken": {"lb": {"cal": 960, "fat": 68, "carbs": 0, "protein": 80, "sodium": 360, "fiber": 0, "sugar": 0}},
    "smoked salmon": {"oz": {"cal": 33, "fat": 1.2, "carbs": 0, "protein": 5, "sodium": 222, "fiber": 0, "sugar": 0}},

    # Juices
    "pineapple juice": {"cup": {"cal": 132, "fat": 0.3, "carbs": 32, "protein": 0.9, "sodium": 5, "fiber": 0.5, "sugar": 25}},

    # Sauces
    "white sauce": {"cup": {"cal": 368, "fat": 27, "carbs": 23, "protein": 10, "sodium": 797, "fiber": 0.5, "sugar": 12}},
    "cream sauce": {"cup": {"cal": 368, "fat": 27, "carbs": 23, "protein": 10, "sodium": 797, "fiber": 0.5, "sugar": 12}},
    "cheese sauce": {"cup": {"cal": 470, "fat": 36, "carbs": 14, "protein": 24, "sodium": 1360, "fiber": 0.5, "sugar": 6}},
    "mushroom soup": {"cup": {"cal": 129, "fat": 9, "carbs": 9, "protein": 2.3, "sodium": 871, "fiber": 0.5, "sugar": 1.6}},

    # Breads & doughs
    "whole ciabatta": {"each": {"cal": 600, "fat": 4, "carbs": 120, "protein": 20, "sodium": 1200, "fiber": 4, "sugar": 4}},
    "pancake mix": {"cup": {"cal": 420, "fat": 4, "carbs": 84, "protein": 12, "sodium": 1400, "fiber": 3, "sugar": 12}},
    "macaroons": {"each": {"cal": 97, "fat": 4, "carbs": 14, "protein": 1, "sodium": 30, "fiber": 0.5, "sugar": 13}},

    # Flours
    "whole-wheat flour": {"cup": {"cal": 407, "fat": 2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0}},
    "unsifted whole-wheat flour": {"cup": {"cal": 407, "fat": 2, "carbs": 87, "protein": 16, "sodium": 6, "fiber": 15, "sugar": 0}},

    # Dairy
    "sweet cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "sweet milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "sharp cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},

    # Wine
    "dry red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 6, "protein": 0, "sodium": 8, "fiber": 0, "sugar": 1}},
    "red wine": {"cup": {"cal": 199, "fat": 0, "carbs": 6, "protein": 0, "sodium": 8, "fiber": 0, "sugar": 1}},

    # Miscellaneous
    "basil leaves": {"cup": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.2, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "tortillas": {"each": {"cal": 150, "fat": 4, "carbs": 26, "protein": 4, "sodium": 340, "fiber": 2, "sugar": 1}},
    "unsweetened applesauce": {"cup": {"cal": 102, "fat": 0.2, "carbs": 28, "protein": 0.4, "sodium": 5, "fiber": 2.7, "sugar": 23}},
    "applesauce": {"cup": {"cal": 167, "fat": 0.4, "carbs": 43, "protein": 0.4, "sodium": 5, "fiber": 2.7, "sugar": 37}},
    "creamy peanut butter": {"tbsp": {"cal": 94, "fat": 8, "carbs": 3, "protein": 4, "sodium": 73, "fiber": 1, "sugar": 1.5}},
    "chunky peanut butter": {"tbsp": {"cal": 94, "fat": 8, "carbs": 3.5, "protein": 4, "sodium": 78, "fiber": 1, "sugar": 1}},
    "mustard powder": {"tsp": {"cal": 9, "fat": 0.6, "carbs": 0.6, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "dry mustard": {"tsp": {"cal": 9, "fat": 0.6, "carbs": 0.6, "protein": 0.5, "sodium": 0, "fiber": 0.2, "sugar": 0}},
    "golden raisins": {"cup": {"cal": 434, "fat": 0.7, "carbs": 115, "protein": 5, "sodium": 17, "fiber": 5, "sugar": 86}},
    "apricot preserves": {"tbsp": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 8, "fiber": 0.2, "sugar": 11}},
    "apricot jam": {"tbsp": {"cal": 50, "fat": 0, "carbs": 13, "protein": 0, "sodium": 8, "fiber": 0.2, "sugar": 11}},
    "malted milk powder": {"tbsp": {"cal": 40, "fat": 0.5, "carbs": 7, "protein": 1.5, "sodium": 40, "fiber": 0, "sugar": 5}},
    "grated nutmeg": {"tsp": {"cal": 12, "fat": 0.8, "carbs": 1, "protein": 0.1, "sodium": 0, "fiber": 0.5, "sugar": 0.1}},
    "tomato catsup": {"tbsp": {"cal": 17, "fat": 0, "carbs": 4.5, "protein": 0.2, "sodium": 154, "fiber": 0, "sugar": 3.5}},
    "gelatine": {"envelope": {"cal": 23, "fat": 0, "carbs": 0, "protein": 6, "sodium": 14, "fiber": 0, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 5 (remaining missing ingredients)
    # =========================================================================

    # Vegetables
    "avocados": {"each": {"cal": 322, "fat": 29, "carbs": 17, "protein": 4, "sodium": 14, "fiber": 13, "sugar": 1}},
    "avocado": {"each": {"cal": 322, "fat": 29, "carbs": 17, "protein": 4, "sodium": 14, "fiber": 13, "sugar": 1}},
    "broccoli florets": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 30, "fiber": 2.4, "sugar": 1.5}},
    "broccoli": {"cup": {"cal": 31, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 30, "fiber": 2.4, "sugar": 1.5}},
    "cucumbers": {"each": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 2, "sodium": 6, "fiber": 1.5, "sugar": 5}},
    "cucumber": {"each": {"cal": 45, "fat": 0.3, "carbs": 11, "protein": 2, "sodium": 6, "fiber": 1.5, "sugar": 5}},
    "baby spinach": {"cup": {"cal": 7, "fat": 0.1, "carbs": 1.1, "protein": 0.9, "sodium": 24, "fiber": 0.7, "sugar": 0.1}},
    "spring onions": {"each": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.3, "sodium": 2, "fiber": 0.4, "sugar": 0.4}},
    "rocket": {"cup": {"cal": 5, "fat": 0.1, "carbs": 0.7, "protein": 0.5, "sodium": 5, "fiber": 0.3, "sugar": 0.4}},
    "arugula": {"cup": {"cal": 5, "fat": 0.1, "carbs": 0.7, "protein": 0.5, "sodium": 5, "fiber": 0.3, "sugar": 0.4}},
    "mashed potatoes": {"cup": {"cal": 237, "fat": 9, "carbs": 35, "protein": 4, "sodium": 699, "fiber": 3, "sugar": 3}},
    "new potatoes": {"lb": {"cal": 350, "fat": 0.4, "carbs": 80, "protein": 9, "sodium": 25, "fiber": 8, "sugar": 4}},
    "small potatoes": {"each": {"cal": 130, "fat": 0.1, "carbs": 30, "protein": 3.5, "sodium": 8, "fiber": 3, "sugar": 1}},

    # Beans & legumes
    "cannellini beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 4, "fiber": 11, "sugar": 0.6}},
    "white beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 4, "fiber": 11, "sugar": 0.6}},
    "great northern beans": {"cup": {"cal": 209, "fat": 0.8, "carbs": 37, "protein": 15, "sodium": 4, "fiber": 12, "sugar": 0.6}},
    "pork & beans": {"cup": {"cal": 268, "fat": 4, "carbs": 51, "protein": 13, "sodium": 1047, "fiber": 14, "sugar": 16}},
    "soybeans": {"cup": {"cal": 298, "fat": 15, "carbs": 17, "protein": 29, "sodium": 1, "fiber": 10, "sugar": 6}},
    "edamame": {"cup": {"cal": 188, "fat": 8, "carbs": 14, "protein": 18, "sodium": 9, "fiber": 8, "sugar": 3}},

    # Meats
    "flank steak": {"lb": {"cal": 720, "fat": 32, "carbs": 0, "protein": 104, "sodium": 280, "fiber": 0, "sugar": 0}},
    "round beef": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0}},
    "streaky bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "bacon strips": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "slices bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "strips bacon": {"slice": {"cal": 43, "fat": 3.3, "carbs": 0.1, "protein": 3, "sodium": 137, "fiber": 0, "sugar": 0}},
    "chopped cooked ham": {"cup": {"cal": 203, "fat": 8, "carbs": 2, "protein": 30, "sodium": 1684, "fiber": 0, "sugar": 0}},
    "chicken breast halves": {"each": {"cal": 284, "fat": 6, "carbs": 0, "protein": 53, "sodium": 104, "fiber": 0, "sugar": 0}},

    # Grains & pasta
    "white rice": {"cup": {"cal": 205, "fat": 0.4, "carbs": 45, "protein": 4, "sodium": 2, "fiber": 0.6, "sugar": 0}},
    "macaroni": {"cup": {"cal": 221, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 2.5, "sugar": 1}},
    "elbow macaroni": {"cup": {"cal": 221, "fat": 1.3, "carbs": 43, "protein": 8, "sodium": 1, "fiber": 2.5, "sugar": 1}},
    "soft bread crumbs": {"cup": {"cal": 120, "fat": 2, "carbs": 22, "protein": 4, "sodium": 200, "fiber": 1, "sugar": 2}},
    "wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 15, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1}},
    "slices wheat bread": {"slice": {"cal": 81, "fat": 1, "carbs": 15, "protein": 4, "sodium": 146, "fiber": 2, "sugar": 1}},
    "ciabatta": {"each": {"cal": 200, "fat": 1.3, "carbs": 40, "protein": 7, "sodium": 400, "fiber": 1.5, "sugar": 1}},
    "muesli": {"cup": {"cal": 289, "fat": 4, "carbs": 66, "protein": 8, "sodium": 14, "fiber": 6, "sugar": 26}},
    "cornflakes": {"cup": {"cal": 101, "fat": 0.2, "carbs": 24, "protein": 2, "sodium": 203, "fiber": 0.7, "sugar": 3}},

    # Cheese
    "longhorn cheese": {"cup": {"cal": 455, "fat": 37, "carbs": 1.4, "protein": 28, "sodium": 701, "fiber": 0, "sugar": 0.5}},
    "muenster cheese": {"oz": {"cal": 104, "fat": 8.5, "carbs": 0.3, "protein": 7, "sodium": 178, "fiber": 0, "sugar": 0.3}},
    "sieved cottage cheese": {"cup": {"cal": 163, "fat": 2.3, "carbs": 6, "protein": 28, "sodium": 918, "fiber": 0, "sugar": 5}},

    # Condiments & sauces
    "chunky salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1200, "fiber": 4, "sugar": 8}},
    "salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1200, "fiber": 4, "sugar": 8}},
    "seasoning salt": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 1600, "fiber": 0, "sugar": 0}},
    "low-sodium soy sauce": {"tbsp": {"cal": 10, "fat": 0, "carbs": 1, "protein": 1, "sodium": 533, "fiber": 0, "sugar": 0}},
    "bottled minced garlic": {"tsp": {"cal": 5, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Spices
    "whole allspice": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1.4, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "pumpkin pie spice": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1.2, "protein": 0.1, "sodium": 1, "fiber": 0.4, "sugar": 0}},
    "greek seasoning": {"tsp": {"cal": 5, "fat": 0.2, "carbs": 1, "protein": 0.2, "sodium": 5, "fiber": 0.3, "sugar": 0}},
    "sage leaves": {"each": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Alcohol
    "gin": {"oz": {"cal": 73, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "vodka": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "tequila": {"oz": {"cal": 64, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "whiskey": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "bourbon": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "scotch": {"oz": {"cal": 70, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "cognac": {"oz": {"cal": 69, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "brandy": {"oz": {"cal": 69, "fat": 0, "carbs": 1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "triple sec": {"oz": {"cal": 103, "fat": 0, "carbs": 11, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 11}},
    "kahlua": {"oz": {"cal": 91, "fat": 0, "carbs": 14, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 14}},
    "amaretto": {"oz": {"cal": 110, "fat": 0, "carbs": 17, "protein": 0, "sodium": 3, "fiber": 0, "sugar": 17}},
    "grand marnier": {"oz": {"cal": 76, "fat": 0, "carbs": 7, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 7}},

    # Gelatin flavors
    "lemon-flavored gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "strawberry gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "lime gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "orange gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},
    "cherry gelatin": {"package": {"cal": 80, "fat": 0, "carbs": 19, "protein": 2, "sodium": 120, "fiber": 0, "sugar": 19}},

    # Fruits
    "grapefruits": {"each": {"cal": 103, "fat": 0.3, "carbs": 26, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "grapefruit": {"each": {"cal": 103, "fat": 0.3, "carbs": 26, "protein": 2, "sodium": 0, "fiber": 4, "sugar": 17}},
    "large apple": {"each": {"cal": 116, "fat": 0.4, "carbs": 31, "protein": 0.6, "sodium": 2, "fiber": 5.4, "sugar": 23}},
    "large bananas": {"each": {"cal": 121, "fat": 0.4, "carbs": 31, "protein": 1.5, "sodium": 1, "fiber": 3.5, "sugar": 17}},
    "large mangos": {"each": {"cal": 202, "fat": 1.3, "carbs": 50, "protein": 2.8, "sodium": 3, "fiber": 5.4, "sugar": 45}},
    "mixed berries": {"cup": {"cal": 70, "fat": 0.5, "carbs": 17, "protein": 1, "sodium": 1, "fiber": 4, "sugar": 10}},

    # Yogurt flavors
    "plain nonfat yoghurt": {"cup": {"cal": 137, "fat": 0.4, "carbs": 19, "protein": 14, "sodium": 189, "fiber": 0, "sugar": 19}},
    "banana-flavored yogurt": {"cup": {"cal": 193, "fat": 2.8, "carbs": 36, "protein": 11, "sodium": 148, "fiber": 0, "sugar": 33}},
    "mango flavored yogurt": {"cup": {"cal": 193, "fat": 2.8, "carbs": 36, "protein": 11, "sodium": 148, "fiber": 0, "sugar": 33}},

    # Chiles & peppers
    "whole green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},
    "green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},
    "diced green chiles": {"can": {"cal": 30, "fat": 0, "carbs": 6, "protein": 1, "sodium": 680, "fiber": 2, "sugar": 3}},

    # Seeds
    "linseeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},
    "flaxseeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},
    "flax seeds": {"tbsp": {"cal": 55, "fat": 4.3, "carbs": 3, "protein": 2, "sodium": 3, "fiber": 2.8, "sugar": 0.2}},

    # Historical/vintage ingredients (for old cookbooks)
    "pearl ash": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "saleratus": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 629, "fiber": 0, "sugar": 0}},
    "emptins": {"cup": {"cal": 30, "fat": 1, "carbs": 4, "protein": 2, "sodium": 10, "fiber": 1, "sugar": 0}},

    # Misc
    "thick cream": {"cup": {"cal": 821, "fat": 88, "carbs": 7, "protein": 5, "sodium": 89, "fiber": 0, "sugar": 7}},
    "truffles": {"oz": {"cal": 84, "fat": 9, "carbs": 2, "protein": 1, "sodium": 15, "fiber": 0, "sugar": 0}},
    "minced parsley": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.2, "protein": 0.1, "sodium": 2, "fiber": 0.1, "sugar": 0}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 6 (final pass)
    # =========================================================================

    # Meats & sausages
    "pork sausage": {"lb": {"cal": 1360, "fat": 112, "carbs": 0, "protein": 64, "sodium": 1400, "fiber": 0, "sugar": 0}},
    "pork sausage links": {"each": {"cal": 80, "fat": 7, "carbs": 0, "protein": 4, "sodium": 200, "fiber": 0, "sugar": 0}},
    "stewing beef": {"lb": {"cal": 800, "fat": 48, "carbs": 0, "protein": 88, "sodium": 280, "fiber": 0, "sugar": 0}},

    # Chocolate & chips
    "milk chocolate": {"oz": {"cal": 153, "fat": 8, "carbs": 17, "protein": 2, "sodium": 23, "fiber": 0.8, "sugar": 15}},
    "milk chocolate chips": {"cup": {"cal": 840, "fat": 48, "carbs": 92, "protein": 10, "sodium": 128, "fiber": 4, "sugar": 84}},
    "peanut butter chips": {"cup": {"cal": 800, "fat": 48, "carbs": 80, "protein": 16, "sodium": 320, "fiber": 2, "sugar": 72}},
    "butterscotch chips": {"cup": {"cal": 800, "fat": 40, "carbs": 100, "protein": 2, "sodium": 300, "fiber": 0, "sugar": 92}},
    "squares unsweetened chocolate": {"each": {"cal": 145, "fat": 15, "carbs": 8, "protein": 3, "sodium": 4, "fiber": 5, "sugar": 0}},

    # Nuts
    "black walnuts": {"cup": {"cal": 760, "fat": 71, "carbs": 12, "protein": 30, "sodium": 2, "fiber": 6, "sugar": 1}},
    "chopped walnuts": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},
    "broken pecans": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "cut-up nuts": {"cup": {"cal": 785, "fat": 79, "carbs": 16, "protein": 18, "sodium": 1, "fiber": 8, "sugar": 3}},

    # Dried fruits
    "cut-up raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 6, "sugar": 86}},
    "cut-up dates": {"cup": {"cal": 415, "fat": 0.6, "carbs": 110, "protein": 4, "sodium": 3, "fiber": 12, "sugar": 93}},
    "eeded raisins": {"cup": {"cal": 434, "fat": 0.5, "carbs": 115, "protein": 5, "sodium": 18, "fiber": 6, "sugar": 86}},

    # Coconut variants
    "sweetened shredded coconut": {"cup": {"cal": 466, "fat": 33, "carbs": 44, "protein": 3, "sodium": 244, "fiber": 4, "sugar": 40}},
    "cocoanut": {"cup": {"cal": 283, "fat": 27, "carbs": 12, "protein": 3, "sodium": 16, "fiber": 7, "sugar": 5}},

    # Spreads & condiments
    "apple butter": {"tbsp": {"cal": 29, "fat": 0.1, "carbs": 7, "protein": 0.1, "sodium": 1, "fiber": 0.3, "sugar": 6}},
    "spicy salsa": {"cup": {"cal": 70, "fat": 0.4, "carbs": 14, "protein": 3, "sodium": 1400, "fiber": 4, "sugar": 8}},

    # Seeds & spices
    "mustard seed": {"tsp": {"cal": 15, "fat": 1, "carbs": 1, "protein": 0.8, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "caraway seeds": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.4, "sodium": 0, "fiber": 0.8, "sugar": 0}},
    "caraway seed": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1, "protein": 0.4, "sodium": 0, "fiber": 0.8, "sugar": 0}},
    "coriander seed": {"tsp": {"cal": 5, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.8, "sugar": 0}},
    "spice": {"tsp": {"cal": 6, "fat": 0.2, "carbs": 1, "protein": 0.1, "sodium": 1, "fiber": 0.5, "sugar": 0}},
    "mild chili powder": {"tsp": {"cal": 8, "fat": 0.4, "carbs": 1.4, "protein": 0.3, "sodium": 26, "fiber": 0.9, "sugar": 0.2}},

    # Dairy
    "eggnog": {"cup": {"cal": 343, "fat": 19, "carbs": 34, "protein": 10, "sodium": 137, "fiber": 0, "sugar": 34}},
    "coconut custard": {"cup": {"cal": 280, "fat": 14, "carbs": 32, "protein": 8, "sodium": 180, "fiber": 1, "sugar": 28}},
    "milk or cream": {"cup": {"cal": 150, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "lukewarm milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},

    # Flour variants
    "buckwheat flour": {"cup": {"cal": 402, "fat": 4, "carbs": 85, "protein": 15, "sodium": 13, "fiber": 12, "sugar": 3}},

    # Apples
    "tart apples": {"each": {"cal": 80, "fat": 0.3, "carbs": 21, "protein": 0.4, "sodium": 1, "fiber": 4, "sugar": 15}},
    "tart cooking apples": {"each": {"cal": 80, "fat": 0.3, "carbs": 21, "protein": 0.4, "sodium": 1, "fiber": 4, "sugar": 15}},

    # Yeast variants
    "yeast cake": {"each": {"cal": 10, "fat": 0.1, "carbs": 1.5, "protein": 1.3, "sodium": 4, "fiber": 0.8, "sugar": 0}},
    "cake yeast": {"each": {"cal": 10, "fat": 0.1, "carbs": 1.5, "protein": 1.3, "sodium": 4, "fiber": 0.8, "sugar": 0}},
    "granulated yeast": {"tsp": {"cal": 8, "fat": 0.1, "carbs": 1, "protein": 1, "sodium": 2, "fiber": 0.5, "sugar": 0}},

    # Canned goods
    "can tomato soup": {"can": {"cal": 161, "fat": 2.4, "carbs": 33, "protein": 4, "sodium": 1710, "fiber": 1.6, "sugar": 20}},
    "strained tomato": {"cup": {"cal": 41, "fat": 0.3, "carbs": 9, "protein": 2, "sodium": 800, "fiber": 2, "sugar": 7}},

    # Cereals
    "kellogg's rice krispies cereal": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 2, "sodium": 190, "fiber": 0.3, "sugar": 3}},
    "rice krispies": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 2, "sodium": 190, "fiber": 0.3, "sugar": 3}},

    # Vegetables
    "shelled peas": {"cup": {"cal": 117, "fat": 0.6, "carbs": 21, "protein": 8, "sodium": 7, "fiber": 7, "sugar": 8}},
    "one carrot": {"each": {"cal": 25, "fat": 0.1, "carbs": 6, "protein": 0.6, "sodium": 42, "fiber": 1.7, "sugar": 3}},

    # Misc prepared
    "stove top stuffing": {"cup": {"cal": 177, "fat": 9, "carbs": 21, "protein": 4, "sodium": 522, "fiber": 1, "sugar": 3}},
    "fine sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200}},

    # =========================================================================
    # GAP ANALYSIS - ROUND 7 (final cleanup)
    # =========================================================================

    # Herbs & leaves
    "mint leaves": {"tbsp": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0.1, "sodium": 1, "fiber": 0, "sugar": 0}},
    "oregano leaves": {"tsp": {"cal": 3, "fat": 0.1, "carbs": 0.7, "protein": 0.1, "sodium": 0, "fiber": 0.4, "sugar": 0}},
    "thyme sprigs": {"each": {"cal": 1, "fat": 0, "carbs": 0.1, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
    "fresh oregano": {"tbsp": {"cal": 3, "fat": 0.1, "carbs": 0.5, "protein": 0.1, "sodium": 0, "fiber": 0.3, "sugar": 0}},

    # Spices & seasonings
    "ground red pepper": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.5, "sugar": 0.2}},
    "garam masala": {"tsp": {"cal": 7, "fat": 0.3, "carbs": 1.3, "protein": 0.2, "sodium": 2, "fiber": 0.5, "sugar": 0.1}},
    "turmeric powder": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "turmeric": {"tsp": {"cal": 8, "fat": 0.2, "carbs": 1.4, "protein": 0.3, "sodium": 1, "fiber": 0.5, "sugar": 0.1}},
    "powdered thyme": {"tsp": {"cal": 4, "fat": 0.1, "carbs": 0.9, "protein": 0.1, "sodium": 1, "fiber": 0.5, "sugar": 0}},
    "black peppercorns": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "peppercorns": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.4, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "alum": {"tsp": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 0}},

    # Nuts & seeds
    "pecan meats": {"cup": {"cal": 753, "fat": 78, "carbs": 15, "protein": 10, "sodium": 0, "fiber": 10, "sugar": 4}},
    "cashew nuts": {"cup": {"cal": 786, "fat": 63, "carbs": 45, "protein": 21, "sodium": 16, "fiber": 4, "sugar": 6}},
    "cashews": {"cup": {"cal": 786, "fat": 63, "carbs": 45, "protein": 21, "sodium": 16, "fiber": 4, "sugar": 6}},

    # Peppers
    "serrano chile": {"each": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0.1, "sodium": 1, "fiber": 0.2, "sugar": 0.2}},
    "poblano pepper": {"each": {"cal": 48, "fat": 0.5, "carbs": 9, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 5}},
    "poblano": {"each": {"cal": 48, "fat": 0.5, "carbs": 9, "protein": 2, "sodium": 6, "fiber": 4, "sugar": 5}},

    # Vegetables
    "yellow squash": {"cup": {"cal": 18, "fat": 0.2, "carbs": 4, "protein": 1, "sodium": 2, "fiber": 1, "sugar": 2}},
    "sliced cucumber": {"cup": {"cal": 14, "fat": 0.1, "carbs": 3, "protein": 0.6, "sodium": 2, "fiber": 0.5, "sugar": 1.5}},
    "corn kernels": {"cup": {"cal": 132, "fat": 1.8, "carbs": 29, "protein": 5, "sodium": 23, "fiber": 4, "sugar": 5}},
    "one leek": {"each": {"cal": 54, "fat": 0.3, "carbs": 13, "protein": 1.3, "sodium": 18, "fiber": 1.6, "sugar": 3.5}},
    "celery stalk": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "stalks celery": {"each": {"cal": 6, "fat": 0.1, "carbs": 1, "protein": 0.3, "sodium": 32, "fiber": 0.6, "sugar": 0.6}},
    "capers": {"tbsp": {"cal": 2, "fat": 0, "carbs": 0.4, "protein": 0.2, "sodium": 255, "fiber": 0.3, "sugar": 0}},
    "guacamole": {"cup": {"cal": 368, "fat": 32, "carbs": 20, "protein": 4, "sodium": 700, "fiber": 14, "sugar": 2}},

    # Beans
    "red kidney beans": {"cup": {"cal": 225, "fat": 0.9, "carbs": 40, "protein": 15, "sodium": 2, "fiber": 11, "sugar": 0.6}},
    "chili beans": {"cup": {"cal": 286, "fat": 2.6, "carbs": 52, "protein": 17, "sodium": 920, "fiber": 18, "sugar": 6}},

    # Cheese
    "asiago cheese": {"oz": {"cal": 111, "fat": 9, "carbs": 1, "protein": 7, "sodium": 340, "fiber": 0, "sugar": 0.5}},
    "parmigiano-reggiano cheese": {"oz": {"cal": 111, "fat": 7, "carbs": 1, "protein": 10, "sodium": 330, "fiber": 0, "sugar": 0}},
    "mozzarella": {"cup": {"cal": 318, "fat": 22, "carbs": 3, "protein": 26, "sodium": 627, "fiber": 0, "sugar": 1}},
    "cheese slices": {"slice": {"cal": 104, "fat": 9, "carbs": 0.5, "protein": 5, "sodium": 406, "fiber": 0, "sugar": 0.3}},

    # Dairy
    "crème fraîche": {"cup": {"cal": 440, "fat": 46, "carbs": 3, "protein": 4, "sodium": 40, "fiber": 0, "sugar": 3}},
    "creme fraiche": {"cup": {"cal": 440, "fat": 46, "carbs": 3, "protein": 4, "sodium": 40, "fiber": 0, "sugar": 3}},
    "full cream milk": {"cup": {"cal": 149, "fat": 8, "carbs": 12, "protein": 8, "sodium": 105, "fiber": 0, "sugar": 12}},
    "ice cubes": {"cup": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Meats
    "ground turkey breast": {"lb": {"cal": 544, "fat": 8, "carbs": 0, "protein": 112, "sodium": 320, "fiber": 0, "sugar": 0}},
    "lean beef": {"lb": {"cal": 680, "fat": 28, "carbs": 0, "protein": 100, "sodium": 260, "fiber": 0, "sugar": 0}},
    "ham fat": {"oz": {"cal": 170, "fat": 18, "carbs": 0, "protein": 1.5, "sodium": 320, "fiber": 0, "sugar": 0}},

    # Juices & beverages
    "grapefruit juice": {"cup": {"cal": 96, "fat": 0.3, "carbs": 23, "protein": 1.2, "sodium": 2, "fiber": 0.2, "sugar": 20}},
    "strong hot coffee": {"cup": {"cal": 2, "fat": 0, "carbs": 0, "protein": 0.3, "sodium": 5, "fiber": 0, "sugar": 0}},
    "apricot nectar": {"cup": {"cal": 140, "fat": 0.2, "carbs": 36, "protein": 0.9, "sodium": 8, "fiber": 1.5, "sugar": 33}},
    "apple juice or cider": {"cup": {"cal": 114, "fat": 0.3, "carbs": 28, "protein": 0.2, "sodium": 10, "fiber": 0.2, "sugar": 24}},

    # Breads
    "baguette": {"each": {"cal": 680, "fat": 2, "carbs": 140, "protein": 24, "sodium": 1400, "fiber": 6, "sugar": 2}},

    # Oils
    "peanut oil": {"tbsp": {"cal": 119, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Condiments & canned
    "jellied cranberry sauce": {"cup": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87}},
    "cranberry sauce": {"cup": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87},
                       "can": {"cal": 418, "fat": 0.4, "carbs": 108, "protein": 0.5, "sodium": 80, "fiber": 3, "sugar": 87}},
    "tzatziki": {"cup": {"cal": 150, "fat": 10, "carbs": 10, "protein": 6, "sodium": 400, "fiber": 0.5, "sugar": 6}},
    "tzatziki sauce": {"cup": {"cal": 150, "fat": 10, "carbs": 10, "protein": 6, "sodium": 400, "fiber": 0.5, "sugar": 6}},
    "onion soup": {"can": {"cal": 140, "fat": 4, "carbs": 18, "protein": 5, "sodium": 2440, "fiber": 2, "sugar": 5}},
    "condensed french onion soup": {"can": {"cal": 140, "fat": 4, "carbs": 18, "protein": 5, "sodium": 2440, "fiber": 2, "sugar": 5}},
    "mushrooms canned": {"cup": {"cal": 33, "fat": 0.3, "carbs": 6, "protein": 2.5, "sodium": 561, "fiber": 2, "sugar": 2}},

    # Sweeteners
    "swerve sweetener": {"cup": {"cal": 0, "fat": 0, "carbs": 96, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},

    # Misc
    "large banana": {"each": {"cal": 121, "fat": 0.4, "carbs": 31, "protein": 1.5, "sodium": 1, "fiber": 3.5, "sugar": 17}},
    "frozen strawberries": {"cup": {"cal": 77, "fat": 0.2, "carbs": 20, "protein": 1, "sodium": 3, "fiber": 3.3, "sugar": 13}},
}

# =============================================================================
# STANDARD CAN & JAR SIZES
# =============================================================================

STANDARD_CAN_SIZES = {
    # Size name: ounces
    "small": 8,
    "regular": 14.5,
    "standard": 14.5,
    "large": 28,
    "family": 28,
    "#10": 106,  # Restaurant size
    "#300": 14,
    "#303": 16,
    "#2": 20,
    "#2.5": 28,
    "#3": 46,
}

STANDARD_JAR_SIZES = {
    # Size name: ounces
    "small": 8,
    "regular": 16,
    "standard": 16,
    "large": 24,
    "family": 32,
}

# =============================================================================
# INGREDIENT NORMALIZATION
# =============================================================================

def parse_quantity(qty_str):
    """Parse quantity string to float, handling fractions and ranges."""
    if not qty_str or qty_str.strip() == "":
        return 1.0

    qty_str = str(qty_str).strip().lower()

    # Handle ranges like "1-2" or "6-8" - take midpoint
    if '-' in qty_str and not qty_str.startswith('-'):
        parts = qty_str.split('-')
        if len(parts) == 2:
            try:
                low = parse_quantity(parts[0])
                high = parse_quantity(parts[1])
                return (low + high) / 2
            except:
                pass

    # Handle "to" ranges like "6 to 8"
    if ' to ' in qty_str:
        parts = qty_str.split(' to ')
        if len(parts) == 2:
            try:
                low = parse_quantity(parts[0])
                high = parse_quantity(parts[1])
                return (low + high) / 2
            except:
                pass

    # Handle mixed numbers like "1 1/2"
    parts = qty_str.split()
    total = 0
    for part in parts:
        try:
            if '/' in part:
                total += float(Fraction(part))
            else:
                # Remove any trailing punctuation
                part = part.rstrip('.,;:')
                total += float(part)
        except (ValueError, ZeroDivisionError):
            continue

    return total if total > 0 else 1.0


def normalize_unit(unit):
    """Normalize unit names to standard forms."""
    unit = str(unit).lower().strip().rstrip('.')

    unit_map = {
        # Volume
        "cups": "cup", "c": "cup", "c.": "cup",
        "tablespoons": "tbsp", "tablespoon": "tbsp", "tbsps": "tbsp", "t": "tbsp", "tbs": "tbsp", "tbl": "tbsp",
        "teaspoons": "tsp", "teaspoon": "tsp", "tsps": "tsp", "t.": "tsp",
        "ounces": "oz", "ounce": "oz", "ozs": "oz",
        "pounds": "lb", "pound": "lb", "lbs": "lb",
        "pints": "pint", "pt": "pint",
        "quarts": "quart", "qt": "quart",
        "gallons": "gallon", "gal": "gallon",
        # Count
        "slices": "slice",
        "links": "link",
        "cloves": "clove",
        "cans": "can",
        "packages": "packet", "pkg": "packet", "pkgs": "packet", "packets": "packet",
        "envelopes": "envelope",
        "stalks": "stalk",
        "sprigs": "sprig",
        "bunches": "bunch",
        "heads": "head",
        "loaves": "loaf",
        "pieces": "piece", "pc": "piece", "pcs": "piece",
        # Size-based
        "small": "small", "sm": "small",
        "medium": "medium", "med": "medium",
        "large": "large", "lg": "large",
    }

    return unit_map.get(unit, unit)


def normalize_ingredient(item):
    """Normalize ingredient name for database lookup."""
    if not item:
        return ""

    item = str(item).lower().strip()

    # Fix unicode fractions
    unicode_fractions = {
        '½': '1/2', '¼': '1/4', '¾': '3/4', '⅓': '1/3', '⅔': '2/3',
        '⅛': '1/8', '⅜': '3/8', '⅝': '5/8', '⅞': '7/8'
    }
    for uf, replacement in unicode_fractions.items():
        item = item.replace(uf, replacement)

    # Normalize curly quotes and special characters
    item = item.replace('\u2019', "'")   # Right single curly quote '
    item = item.replace('\u2018', "'")   # Left single curly quote '
    item = item.replace('\u201c', '"')   # Left double curly quote "
    item = item.replace('\u201d', '"')   # Right double curly quote "
    item = item.replace('ﬂ', 'fl')  # fi/fl ligature
    item = item.replace('ﬁ', 'fi')  # fi ligature

    # Fix common OCR quirks in ingredient text
    ocr_fixes = [
        (r'^ful[s]?\s+of\s*', ''),           # item starts with "ful of" (OCR artifact)
        (r'^ful[s]?\s+', ''),                # item starts with "ful " (OCR artifact)
        (r'\btsp\s*ful\s*of\b', ''),         # "tsp ful of" -> ""
        (r'\btbsp\s*ful[s]?\s*of\b', ''),    # "tbsp fuls of" -> ""
        (r'\btsp\s*ful\b', ''),              # "tsp ful" -> ""
        (r'\btbsp\s*ful[s]?\b', ''),         # "tbsp fuls" -> ""
        (r'\btblsp\.?\b', ''),               # "tblsp" -> ""
        (r'\blevel\s+tablespoonful[s]?\s+of\b', ''),  # "level tablespoonfuls of"
        (r'\blevel\s+teaspoonful[s]?\s+of\b', ''),    # "level teaspoonfuls of"
        (r'\bsaltspoonful\s+of\b', ''),      # "saltspoonful of" -> ""
        (r'\bfew\s+grains\b', ''),           # "few grains" -> ""
        (r'\bdash\s+of\b', ''),              # "dash of" -> ""
        (r'\bdash\s+', ''),                  # "dash " embedded in item
        (r'\bpinch\s+', ''),                 # "pinch " embedded in item
        (r'\btsp\.?\s+', ''),                # "tsp " or "tsp. " embedded in item
        (r'\btbsp\.?\s+', ''),               # "tbsp " embedded in item
        (r'^t\s+', ''),                      # "t " at start (abbreviation for tsp)
        (r'^c\s+', ''),                      # "c " at start (abbreviation for cup)
        (r'^T\s+', ''),                      # "T " at start (abbreviation for tbsp)
        (r'\b1/2\s+cups?\s+', ''),           # "1/2 cup(s) " embedded
        (r'\b1/4\s+cups?\s+', ''),           # "1/4 cup(s) " embedded
        (r'\b3/4\s+cups?\s+', ''),           # "3/4 cup(s) " embedded
        (r'\b1/2\s+tsp\.?\s+', ''),          # "1/2 tsp " embedded
        (r'\b1/4\s+tsp\.?\s+', ''),          # "1/4 tsp " embedded
        (r'\b1/2\s+tbsp\.?\s+', ''),         # "1/2 tbsp " embedded
        (r'\bcup[s]?\s+', ''),               # "cup " embedded in item
        (r'\bpint[s]?\s+', ''),              # "pint " embedded in item
        (r'\bquart[s]?\s+', ''),             # "quart " embedded in item
        (r'\bpound[s]?\s+', ''),             # "pound " embedded in item
        (r'\s+of\s+', ' '),                  # " of " -> " "
        (r'\s*\.\s*$', ''),                  # trailing period
        (r'\s*\.\s+', ' '),                  # period in middle
        (r'-\s+', ' '),                      # hyphen with trailing space (OCR line-break)
        (r'\s+-', ' '),                      # space before hyphen
        (r',\s*$', ''),                      # trailing comma
        (r'\s{2,}', ' '),                    # multiple spaces
    ]
    for pattern, replacement in ocr_fixes:
        item = re.sub(pattern, replacement, item)

    # Remove prep notes after comma
    if "," in item:
        item = item.split(",")[0].strip()

    # Remove parenthetical notes (including leading ones like "(4 oz)")
    item = re.sub(r'^\([^)]*\)\s*', '', item)  # Leading parenthetical
    item = re.sub(r'\s*\([^)]*\)', '', item)   # Embedded parenthetical

    # Remove leading numbers/quantities that got mixed in
    item = re.sub(r'^\d+[\s/\d]*\s*', '', item)

    # Common prefixes to remove
    prefixes = [
        "fresh ", "frozen ", "dried ", "canned ", "cooked ", "raw ",
        "chopped ", "diced ", "minced ", "sliced ", "cubed ",
        "grated ", "shredded ", "mashed ", "crushed ", "crumbled ",
        "melted ", "softened ", "room temperature ", "cold ", "warm ", "hot ",
        "ripe ", "peeled ", "pitted ", "seeded ", "cored ",
        "toasted ", "roasted ", "sauteed ",
        "sifted ", "packed ", "firmly packed ", "lightly packed ",
        "finely ", "coarsely ", "roughly ", "thinly ",
        "boneless ", "skinless ",
        "low-fat ", "lowfat ", "low fat ", "nonfat ", "non-fat ", "fat-free ",
        "unsalted ", "salted ",
        "pure ", "organic ", "natural ",
        "about ", "approximately ", "approx ",
    ]

    for prefix in prefixes:
        if item.startswith(prefix):
            item = item[len(prefix):]

    # Brand name normalization (use straight quotes since curly quotes are normalized earlier)
    brand_map = {
        "grandma's molasses": "molasses",
        "grandmas molasses": "molasses",
        "carnation milk": "evaporated milk",
        "gold medal flour": "flour",
        "pillsbury flour": "flour",
        "crisco": "shortening",
        "pam": "cooking spray",
        "kraft": "",
        "heinz": "",
        "hellmann's": "mayonnaise",
        "best foods": "mayonnaise",
        "philadelphia": "cream cheese",
        "jell-o": "gelatin",
        "knox": "gelatin",
        "bisquick": "biscuit mix",
        "jiffy": "corn muffin mix",
        "shedd's spread country crock calcium plus vitamin d": "margarine",
        "shedd's spread country crock": "margarine",
        "shedd's spread": "margarine",
        "country crock": "margarine",
        "i can't believe it's not butter": "margarine",
        "campbell's": "",
        "swanson": "",
        "progresso": "",
        "lipton": "",
        "mccormick": "",
    }

    for brand, replacement in brand_map.items():
        if brand in item:
            if replacement:
                item = replacement
            else:
                item = item.replace(brand, "").strip()

    # Common ingredient synonyms
    synonyms = {
        # Flour
        "all purpose flour": "flour",
        "all-purpose flour": "flour",
        "ap flour": "flour",
        "plain flour": "flour",
        "unbleached flour": "flour",
        "enriched flour": "flour",

        # Sugar
        "granulated sugar": "sugar",
        "white sugar": "sugar",
        "cane sugar": "sugar",
        "light brown sugar": "brown sugar",
        "dark brown sugar": "brown sugar",
        "confectioners sugar": "powdered sugar",
        "confectioner's sugar": "powdered sugar",
        "icing sugar": "powdered sugar",
        "10x sugar": "powdered sugar",

        # Eggs
        "large eggs": "egg",
        "eggs": "egg",
        "whole egg": "egg",
        "beaten egg": "egg",
        "egg whites": "egg white",
        "egg yolks": "egg yolk",

        # Dairy
        "whole milk": "milk",
        "2% milk": "milk",
        "1% milk": "skim milk",
        "fat free milk": "skim milk",
        "heavy whipping cream": "heavy cream",
        "whipping cream": "heavy cream",

        # Butter
        "unsalted butter": "butter",
        "salted butter": "butter",
        "stick butter": "butter",
        "butter or margarine": "butter",

        # Oil
        "canola oil": "vegetable oil",
        "corn oil": "vegetable oil",
        "safflower oil": "vegetable oil",
        "cooking oil": "vegetable oil",
        "extra virgin olive oil": "olive oil",
        "extra-virgin olive oil": "olive oil",
        "evoo": "olive oil",

        # Chicken
        "chicken breasts": "chicken breast",
        "boneless skinless chicken breasts": "chicken breast",
        "boneless skinless chicken breast": "chicken breast",
        "whole chicken breasts": "chicken breast",
        "chicken thighs": "chicken thigh",
        "boneless skinless chicken thighs": "chicken thigh",

        # Ground meats
        "lean ground beef": "ground beef",
        "ground chuck": "ground beef",
        "hamburger": "ground beef",
        "hamburger meat": "ground beef",

        # Onion/garlic
        "yellow onion": "onion",
        "white onion": "onion",
        "red onion": "onion",
        "sweet onion": "onion",
        "vidalia onion": "onion",
        "garlic cloves": "garlic",
        "cloves garlic": "garlic",
        "garlic clove": "garlic",
        "green onions": "green onion",
        "scallions": "green onion",

        # Peppers
        "green bell pepper": "green pepper",
        "red bell pepper": "red pepper",
        "bell pepper": "bell pepper",
        "jalapeno pepper": "jalapeno",
        "jalapeño": "jalapeno",
        "serrano pepper": "jalapeno",

        # Tomatoes
        "roma tomatoes": "tomato",
        "plum tomatoes": "tomato",
        "cherry tomatoes": "tomato",
        "grape tomatoes": "tomato",
        "tomatoes": "tomato",

        # Potatoes
        "russet potato": "potato",
        "russet potatoes": "potato",
        "yukon gold potato": "potato",
        "red potato": "potato",
        "baking potato": "potato",
        "idaho potato": "potato",

        # Spices
        "ground cumin": "cumin",
        "ground cinnamon": "cinnamon",
        "ground ginger": "ginger",
        "ground nutmeg": "nutmeg",
        "ground cloves": "cloves",
        "ground allspice": "allspice",
        "ground black pepper": "black pepper",
        "freshly ground black pepper": "black pepper",
        "freshly ground pepper": "pepper",
        "kosher salt": "salt",
        "sea salt": "salt",
        "table salt": "salt",
        "salt and pepper": "salt",
        "salt & pepper": "salt",

        # Vanilla
        "pure vanilla extract": "vanilla extract",
        "vanilla": "vanilla extract",
        "pure vanilla": "vanilla extract",

        # Oatmeal
        "instant oatmeal packets": "instant oatmeal",
        "instant oatmeal packets plain": "instant oatmeal",
        "oatmeal packets": "instant oatmeal",
        "quaker instant oatmeal": "instant oatmeal",
        "quaker oats instant oatmeal": "instant oatmeal",
        "quick oats": "oats",
        "rolled oats": "oats",
        "old fashioned oats": "oats",

        # Baking
        "baking cocoa": "cocoa powder",
        "unsweetened cocoa": "cocoa powder",
        "unsweetened cocoa powder": "cocoa powder",
        "dutch process cocoa": "cocoa powder",
        "semisweet chocolate chips": "chocolate chips",
        "semi-sweet chocolate chips": "chocolate chips",
        "dark chocolate chips": "chocolate chips",
        "milk chocolate chips": "chocolate chips",
        "active dry yeast": "yeast",
        "instant yeast": "yeast",
        "rapid rise yeast": "yeast",
        "unflavored gelatin": "gelatin",

        # Broth
        "low sodium chicken broth": "chicken broth",
        "reduced sodium chicken broth": "chicken broth",
        "low sodium beef broth": "beef broth",
        "stock": "chicken broth",
        "chicken stock": "chicken broth",
        "beef stock": "beef broth",

        # Canned goods
        "condensed cream of chicken soup": "cream of chicken soup",
        "condensed cream of mushroom soup": "cream of mushroom soup",
        "condensed cream of celery soup": "cream of celery soup",
        "condensed tomato soup": "tomato soup",
        "petite diced tomatoes": "diced tomatoes",
        "fire roasted diced tomatoes": "diced tomatoes",
        "stewed tomatoes": "canned tomatoes",
        "whole tomatoes": "canned tomatoes",

        # Herbs
        "fresh parsley": "parsley",
        "flat-leaf parsley": "parsley",
        "italian parsley": "parsley",
        "fresh cilantro": "cilantro",
        "fresh basil": "basil",
        "fresh dill": "dill",
        "fresh thyme": "thyme",
        "fresh rosemary": "rosemary",
        "fresh mint": "mint",
        "fresh sage": "sage",

        # Fish
        "trout fillets": "trout",
        "trout fillet": "trout",
        "salmon fillets": "salmon",
        "salmon fillet": "salmon",
        "skinless trout": "trout",
        "skinless salmon": "salmon",

        # Leavening
        "soda": "baking soda",
        "bicarbonate of soda": "baking soda",
        "bicarb": "baking soda",
        "dry active yeast": "yeast",
        "dry yeast": "yeast",

        # Citrus zest
        "lemon rind": "lemon zest",
        "grated lemon rind": "lemon zest",
        "lemon peel": "lemon zest",
        "orange rind": "orange zest",
        "grated orange rind": "orange zest",
        "orange peel": "orange zest",
        "lime rind": "lime zest",
        "grated lime rind": "lime zest",

        # Salt & pepper
        "salt and pepper": "salt",
        "salt & pepper": "salt",
        "kosher salt and pepper": "salt",
        "kosher salt and freshly ground pepper": "salt",
        "salt and freshly ground pepper": "salt",
        "salt and freshly ground black pepper": "salt",
        "salt to taste": "salt",
        "pepper to taste": "pepper",
        "paprika": "paprika",

        # Misc
        "fresh lemon juice": "lemon juice",
        "fresh lime juice": "lime juice",
        "worcestershire": "worcestershire sauce",
        "sour cream": "sour cream",
        "plain greek yogurt": "greek yogurt",
        "non-fat greek yogurt": "greek yogurt",
        "thick-cut bacon": "bacon",
        "thick cut bacon": "bacon",
        "turkey bacon": "bacon",
        "center-cut bacon": "bacon",

        # Cooking spray
        "cooking spray": "cooking spray",
        "nonstick cooking spray": "cooking spray",
        "non-stick cooking spray": "cooking spray",
        "vegetable cooking spray": "cooking spray",
        "butter flavored cooking spray": "cooking spray",

        # Pie crust
        "savory deep dish pie crust": "pie crust",
        "deep dish pie crust": "pie crust",
        "9-inch pie crust": "pie crust",
        "unbaked pie crust": "pie crust",
        "prepared pie crust": "pie crust",
        "refrigerated pie crust": "pie crust",

        # Creamed soups
        "cream chicken soup": "cream of chicken soup",
        "cream mushroom soup": "cream of mushroom soup",
        "cream celery soup": "cream of celery soup",

        # Tortillas
        "large flour tortillas": "flour tortilla",
        "flour tortillas": "flour tortilla",
        "corn tortillas": "corn tortilla",
        "10-inch flour tortillas": "flour tortilla",
        "8-inch flour tortillas": "flour tortilla",

        # Lemons/citrus
        "lemons": "lemon",
        "limes": "lime",
        "oranges": "orange",

        # Gelatin
        "envelope unflavored gelatin": "gelatin",
        "packet unflavored gelatin": "gelatin",
        "unflavored gelatine": "gelatin",

        # Additional gap analysis mappings
        "soft shortening": "shortening",
        "soft butter": "butter",
        "creamed butter": "butter",
        "sweet butter": "butter",
        "butter substitute": "butter",
        "chilled butter": "butter",
        "clove garlic": "garlic",
        "small onion": "onion",
        "medium onion": "onion",
        "large onion": "onion",
        "chopped onion": "onion",
        "one onion": "onion",
        "two onions": "onion",
        "cut onion": "onion",
        "cutonion": "onion",
        "one egg": "egg",
        "eggwhites": "egg white",

        # OCR artifact fixes - space-corrupted words
        "mayonnais e": "mayonnaise",
        "eg g yolks": "egg yolk",
        "eg g": "egg",
        "unsalt ed butter": "butter",
        "lemo n peel": "lemon zest",
        "lemo n": "lemon",
        "m iniature marshmallows": "miniature marshmallows",
        "bouillon c ube": "bouillon cube",
        "unsweet ened pineapple juice": "pineapple juice",
        "s. hard pears": "pear",
        "s. sugar": "sugar",
        "all-purpose ﬂour": "flour",
        "ﬂour": "flour",  # Wrong fl character
        "confectioners' sugar": "powdered sugar",
        "cutparsley": "parsley",
        "teaspoon salt": "salt",
        "teaspoons salt": "salt",
        "t salt": "salt",
        "of salt": "salt",
        "two teaspoons ofsalt": "salt",
        "two teaspoons ofbaking powder": "baking powder",
        "three offlour": "flour",
        "four tablespoons ofshortening": "shortening",

        # Unit embedded in item cleanup
        "c sugar": "sugar",
        "c flour": "flour",
        "c butter": "butter",
        "c water": "water",
        "c milk": "milk",
        "qts water": "water",

        # Additional cheese
        "sharp cheddar": "sharp cheddar cheese",
        "mild cheddar": "mild cheddar cheese",
        "monterey jack": "monterey jack cheese",
        "pepper jack": "pepper jack cheese",
        "extra sharp cheddar": "sharp cheddar cheese",

        # Additional common mappings
        "boneless": "chicken breast",
        "skinless": "chicken breast",
        "low-sodium chicken broth": "chicken broth",
        "reduced sodium chicken broth": "chicken broth",
        "fat-free": "skim milk",

        # Corn syrup
        "corn syrup": "light corn syrup",
        "karo syrup": "light corn syrup",
        "karo": "light corn syrup",

        # More synonyms from gap analysis
        "large ripe banana": "banana",
        "ripe banana": "banana",
        "ripe mango": "mango",
        "t water": "water",
        "t milk": "milk",
        "t sugar": "sugar",
        "t cornstarch": "cornstarch",
        "c celery": "celery",
        "c powdered sugar": "powdered sugar",
        "c powdere d sugar": "powdered sugar",
        "lb butter": "butter",
        "teaspoon nutmeg": "nutmeg",
        "teaspoon cinnamon": "cinnamon",
        "teaspoons cinnamon": "cinnamon",
        "can tomato sauce": "tomato sauce",
        "can mushrooms": "mushrooms",
        "jar apricot preserves": "apricot preserves",
        "mel ted butter": "butter",
        "parsl ey": "parsley",
        "chili flakes": "red pepper flakes",
        "% milk": "milk",
        "spices": "allspice",
        "flavoring": "vanilla extract",

        # Round 5 gap analysis synonyms
        "c walnuts": "walnuts",
        "c salad oil": "salad oil",
        "c lemo n juice": "lemon juice",
        "tbs flour": "flour",
        "mozzarella chees e": "mozzarella cheese",
        "d onion": "onion",
        "cutgreen peppers": "green pepper",
        "pulverized sugar": "powdered sugar",
        "teaspoon pepper": "pepper",
        "of pepper": "pepper",
        "t cold water": "water",
        "glass white wine": "dry white wine",
        "olive or vegetable oil": "olive oil",
        "margarine or butter": "butter",
        "cereals or muesli": "muesli",
        "two tablespoons ofbutter": "butter",
        "two tablespoonfuls ofsugar": "sugar",
        "four branches ofparsley": "parsley",
        "three tablespoons offinely minced parsley": "parsley",
        "two teaspoonfuls ofsalt": "salt",
        "one teaspoonful ofsalt": "salt",
        "two level tablespoons ofbaking powder": "baking powder",
        "three cupsofflour": "flour",
        "ofmilk": "milk",

        # Historical cookbook OCR artifacts
        "double-acting or 11/2 teaspoons cream tartar baking powder": "baking powder",
        "double-acting or 11/4 teaspoons cream tartar baking powder": "baking powder",
        "double-acting or 3 teaspoons cream tartar baking powder": "baking powder",
        "pastry for 2-crust": "pie crust",
        "cooked": "chicken",
        "meal": "cornmeal",

        # Round 6 synonyms
        "confectioners' sugar": "powdered sugar",
        "ugar": "sugar",
        "ugar;": "sugar",
        "cheddar": "cheddar cheese",
        "tablespoons butter": "butter",
        "vinegar or lemon juice": "vinegar",
        "c brown sugar": "brown sugar",
        "two ofsugar": "sugar",
        "and a half sugar": "sugar",
        "butter with two sugar": "butter",
        "three teaspoonfuls baking powder": "baking powder",
        "three tablespoons ofbaking powder": "baking powder",
        "four cupsofsifted flour": "flour",
        "two tablespoons ofshortening": "shortening",
        "to 4 flour": "flour",
        "juice 1 lemon": "lemon juice",
        "black molasses": "molasses",
        "no 2 can crushed pineapple": "crushed pineapple",
        "one 9-inch pie shell": "pie crust",
        "pastry for 9\" shell": "pie crust",
        "s stewing beef": "stewing beef",
        "miniature marshmallows or 20 regular marshmallows": "miniature marshmallows",
        "orange zest strips": "orange zest",
        "stove top stuffi ng": "stove top stuffing",

        # Round 8 synonyms - OCR artifacts
        "tblsp. flour": "flour",
        "tblsp. sugar": "sugar",
        "tblsp. vinegar": "vinegar",
        "tblsp flour": "flour",
        "tblsp sugar": "sugar",
        "t vanilla": "vanilla extract",
        "t. vanilla": "vanilla extract",
        "tsp. vanilla": "vanilla extract",
        "level tablespoonfuls of flour": "flour",
        "level tablespoons of flour": "flour",
        "level tablespoonfuls flour": "flour",
        "tablespoonfuls of flour": "flour",
        "tablespoons of flour": "flour",
        "tablespoons flour": "flour",
        "½ cups sugar": "sugar",
        "½ cups flour": "flour",
        "½ cup sugar": "sugar",
        "½ cup shortening": "shortening",
        "½ cup milk": "milk",
        "½ tsp. baking powder": "baking powder",
        "½ tsp. cloves": "cloves",
        "½ tsp baking powder": "baking powder",
        "¾ cup sugar": "sugar",

        # Rose water variants
        "rose-water": "rose water",
        "rosewater": "rose water",

        # Catsup/ketchup
        "catsup": "ketchup",

        # Corn variants
        "kernel corn": "corn",
        "corn kernels": "corn",
        "whole kernel corn": "corn",

        # Pimiento/pimento
        "pimento": "pimiento",
        "chopped pimiento": "pimiento",
        "chopped pimento": "pimiento",

        # Green items
        "green peppers": "green pepper",
        "green chiles, chopped": "green chiles",
        "(4 oz) green chiles, chopped": "green chiles",
        "green chiles chopped": "green chiles",
        "chopped green chiles": "green chiles",

        # Whole spices
        "whole cloves": "cloves",
        "whole allspice": "allspice",

        # Common plurals and variants
        "potatoes": "potato",
        "onions": "onion",
        "carrots": "carrot",
        "apples": "apple",
        "avocados": "avocado",
        "raisins": "raisins",
        "bread crumbs": "breadcrumbs",

        # Cream variants
        "cream": "heavy cream",

        # Gelatin
        "envelope unflavored gelatin": "gelatin",
        "envelopes unflavored gelatin": "gelatin",
        "packet gelatin": "gelatin",

        # Wine
        "wine": "dry white wine",
        "white wine": "dry white wine",
        "red wine": "dry red wine",

        # Soy sauce
        "soy sauce": "soy sauce",

        # Mace
        "mace": "nutmeg",  # Similar flavor profile

        # Sliced variants
        "slices bacon": "bacon",
        "bacon slices": "bacon",

        # Water variants
        "boiling water": "water",
        "cold water": "water",
        "qts. water": "water",

        # Spice synonyms
        "white peppercorns": "peppercorns",
        "black peppercorns": "peppercorns",
        "coriander seeds": "coriander seed",
        "ground fennel seeds": "fennel seeds",
        "fennel seeds, crushed": "fennel seeds",
        "ground cayenne pepper": "cayenne",
        "ground cayenne": "cayenne",
        "pinch cayenne": "cayenne",
        "red pepper flakes": "crushed red pepper",
        "seasoning salt": "salt",

        # Panko/breadcrumbs
        "panko crumbs": "panko",
        "panko breadcrumbs": "panko",

        # Cheese synonyms
        "crumbled feta cheese": "feta cheese",
        "crumbled gorgonzola cheese": "gorgonzola",
        "crumbled feta": "feta cheese",
        "crumbled gorgonzola": "gorgonzola",
        "romano cheese": "parmesan cheese",
        "parmigiano-reggiano cheese": "parmesan cheese",
        "parmigiano-reggiano": "parmesan cheese",

        # Pasta synonyms
        "penne pasta": "pasta",
        "bucatini": "pasta",
        "uncooked penne pasta": "pasta",
        "uncooked bucatini": "pasta",

        # Brand name cleanup
        "campbell's condensed french onion soup": "onion soup",
        "pepperidge farm classic sandwich buns": "hamburger bun",
        "ocean spray jellied cranberry sauce": "cranberry sauce",
        "heinz chili sauce": "chili sauce",
        "bird's eye": "",
    }

    # Check for exact match first
    if item in synonyms:
        item = synonyms[item]
    else:
        # Try partial matches
        for old, new in synonyms.items():
            if old in item:
                item = new
                break

    return item.strip()


# =============================================================================
# EQUIPMENT FILTER - Items that are not food
# =============================================================================

EQUIPMENT_WORDS = {
    # Kitchen equipment
    "mixing-bowl", "mixing bowl", "bowl", "mixing-spoon", "spoon", "fork",
    "dover beater", "beater", "double-boiler", "double boiler", "saucepan",
    "flour sifter", "sifter", "vegetable-knife", "knife", "grater",
    "egg mixing-bowl", "butter mixing-bowl", "ugar mixing-spoon",
    "milk dover beater", "milk double-boiler",
    # Meta instructions
    "for the cake:", "for the frosting:", "for the filling:",
    "mrs.wilson's cookbook", "-inch", "-sized",
    # Non-food items
    "each", "s", "d 227", "egg .03",
}

def is_equipment(item):
    """Check if an item is equipment/non-food rather than an ingredient."""
    item_lower = item.lower().strip()

    # Direct matches
    if item_lower in EQUIPMENT_WORDS:
        return True

    # Partial matches for equipment patterns
    equipment_patterns = [
        "mixing-bowl", "mixing bowl", "double-boiler", "double boiler",
        "dover beater", "vegetable-knife", "flour sifter",
        "for the ", "cookbook", "-inch", "-sized potatoes vegetable",
        "for topping", "for serving", "for dipping", "for garnish",
        "for dusting", "(optional)", "optional",
    ]
    for pattern in equipment_patterns:
        if pattern in item_lower:
            return True

    # Very short items that are likely OCR garbage
    if len(item_lower) <= 2 and not item_lower.isdigit():
        return True

    return False


# =============================================================================
# SERVING INFERENCE - Smart defaults based on category
# =============================================================================

def infer_servings(recipe):
    """Infer serving size based on recipe characteristics."""
    # Check if we have explicit servings
    servings_yield = recipe.get("servings_yield", "")
    if servings_yield:
        parsed = parse_servings(servings_yield)
        if parsed:
            return parsed

    category = recipe.get("category", "").lower()
    title = recipe.get("title", "").lower()
    ingredients = recipe.get("ingredients", [])

    # Count key ingredients to estimate yield
    flour_cups = 0
    meat_lbs = 0
    egg_count = 0

    for ing in ingredients:
        item = ing.get("item", "").lower()
        unit = ing.get("unit", "").lower()
        try:
            qty = float(ing.get("quantity", 0) or 0)
        except:
            qty = 1

        if "flour" in item and "cup" in unit:
            flour_cups += qty
        elif any(m in item for m in ["beef", "chicken", "pork", "turkey", "lamb"]) and "lb" in unit:
            meat_lbs += qty
        elif "egg" in item and unit in ("", "each", "large"):
            egg_count += qty

    # Category-based defaults
    if category == "beverages":
        return 4
    elif category == "appetizers":
        return 8  # Appetizers usually serve more
    elif category == "desserts":
        if "cookie" in title or "bar" in title:
            return 24  # Cookies/bars make many
        elif "cake" in title:
            return 12
        elif "pie" in title:
            return 8
        elif flour_cups >= 3:
            return 16  # Large batch
        else:
            return 8
    elif category == "breads":
        if "muffin" in title:
            return 12
        elif "roll" in title or "biscuit" in title:
            return 12
        elif "loaf" in title or "bread" in title:
            return 12  # One loaf = ~12 slices
        else:
            return 8
    elif category == "breakfast":
        if "pancake" in title or "waffle" in title:
            return 4
        else:
            return 4
    elif category == "mains":
        if meat_lbs >= 2:
            return 8
        elif meat_lbs >= 1:
            return 6
        else:
            return 4
    elif category == "soups":
        return 6
    elif category == "salads":
        return 6
    elif category == "sides":
        return 6

    # Fallback based on ingredient volume
    if flour_cups >= 4:
        return 16
    elif flour_cups >= 2:
        return 8
    elif meat_lbs >= 2:
        return 8

    return 4  # Default


# =============================================================================
# NUTRITION CALCULATION
# =============================================================================

def get_nutrition_for_ingredient(ingredient):
    """Calculate nutrition for a single ingredient entry."""
    item = normalize_ingredient(ingredient.get("item", ""))

    # Skip equipment and non-food items
    if is_equipment(item):
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0, "_skipped": True}

    quantity = parse_quantity(ingredient.get("quantity", "1"))
    unit = normalize_unit(ingredient.get("unit", ""))

    # Handle compound units like "5-oz" or "6-inch" -> extract multiplier
    compound_match = re.match(r'^(\d+(?:\.\d+)?)-?(\w+)$', unit)
    if compound_match:
        unit_multiplier = float(compound_match.group(1))
        unit = compound_match.group(2)
        quantity = quantity * unit_multiplier

    # Handle "to taste" / "to sweeten" - minimal impact (check unit, item, and prep_note)
    to_taste_fields = [
        str(ingredient.get("unit", "")).lower(),
        str(ingredient.get("item", "")).lower(),
        str(ingredient.get("prep_note", "")).lower()
    ]
    if any("to taste" in f or "to sweeten" in f for f in to_taste_fields):
        if "salt" in item or "pepper" in item:
            return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 150, "fiber": 0, "sugar": 0}
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}

    # Handle water
    if "water" in item and item not in NUTRITION_DB:
        return {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}

    # Try exact match
    if item in NUTRITION_DB:
        db_entry = NUTRITION_DB[item]
        if unit in db_entry:
            base = db_entry[unit]
            return {k: v * quantity for k, v in base.items()}
        elif "" in db_entry:  # Unit-less items
            base = db_entry[""]
            return {k: v * quantity for k, v in base.items()}
        # Try unit conversions
        elif unit == "tbsp" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 16 for k, v in base.items()}
        elif unit == "tsp" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 48 for k, v in base.items()}
        elif unit == "tsp" and "tbsp" in db_entry:
            base = db_entry["tbsp"]
            return {k: v * quantity / 3 for k, v in base.items()}
        elif unit == "tbsp" and "tsp" in db_entry:
            base = db_entry["tsp"]
            return {k: v * quantity * 3 for k, v in base.items()}
        # Pint/quart to cup conversions
        elif unit == "pint" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 2 for k, v in base.items()}  # 1 pint = 2 cups
        elif unit == "quart" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 4 for k, v in base.items()}  # 1 quart = 4 cups
        elif unit == "gallon" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity * 16 for k, v in base.items()}  # 1 gallon = 16 cups
        # ML to cup conversion
        elif unit == "ml" and "cup" in db_entry:
            base = db_entry["cup"]
            return {k: v * quantity / 237 for k, v in base.items()}  # ~237 ml per cup

    # Try without unit for counted items
    if item in NUTRITION_DB and "" in NUTRITION_DB[item]:
        base = NUTRITION_DB[item][""]
        return {k: v * quantity for k, v in base.items()}

    return None


def parse_servings(servings_str, default=4):
    """Parse servings from yield string. Default to 4 if not specified."""
    if not servings_str:
        return default

    servings_str = str(servings_str).lower()

    # Handle range like "6-8 servings" - take midpoint
    range_match = re.search(r'(\d+)\s*[-–to]+\s*(\d+)', servings_str)
    if range_match:
        low = int(range_match.group(1))
        high = int(range_match.group(2))
        return (low + high) // 2

    # Handle simple number
    match = re.search(r'(\d+)', servings_str)
    if match:
        return int(match.group(1))

    # Handle word-based
    word_map = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "twelve": 12, "dozen": 12, "several": 4
    }
    for word, num in word_map.items():
        if word in servings_str:
            return num

    return default


def calculate_recipe_nutrition(recipe, default_servings=4):
    """Calculate complete nutrition for a recipe."""
    ingredients = recipe.get("ingredients", [])

    # Use smart serving inference
    servings = infer_servings(recipe)
    serving_inferred = not recipe.get("servings_yield")

    total = {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}
    missing = []
    skipped_equipment = 0
    actual_ingredients = 0

    for ing in ingredients:
        nutr = get_nutrition_for_ingredient(ing)
        if nutr:
            # Check if it was skipped equipment
            if nutr.get("_skipped"):
                skipped_equipment += 1
            else:
                actual_ingredients += 1
                for key in total:
                    total[key] += nutr.get(key, 0)
        else:
            # Check if it's equipment before adding to missing
            item = normalize_ingredient(ing.get("item", ""))
            if not is_equipment(item):
                actual_ingredients += 1
                ing_str = f"{ing.get('quantity', '')} {ing.get('unit', '')} {ing.get('item', '')}".strip()
                if ing_str:
                    missing.append(ing_str)

    # Calculate per-serving values
    per_serving = {
        "calories": round(total["cal"] / servings),
        "fat_g": round(total["fat"] / servings, 1),
        "carbs_g": round(total["carbs"] / servings, 1),
        "protein_g": round(total["protein"] / servings, 1),
        "sodium_mg": round(total["sodium"] / servings),
        "fiber_g": round(total["fiber"] / servings, 1),
        "sugar_g": round(total["sugar"] / servings, 1)
    }

    # Determine status (based on actual food ingredients, not equipment)
    total_food_ingredients = actual_ingredients
    missing_count = len(missing)

    if missing_count == 0:
        status = "complete"
    elif missing_count <= 2 or (total_food_ingredients > 0 and missing_count / total_food_ingredients <= 0.2):
        status = "partial"
    else:
        status = "insufficient_data"

    assumptions = [f"Calculated for {servings} servings"]
    if serving_inferred:
        category = recipe.get("category", "unknown")
        assumptions.append(f"Serving size inferred from {category} category")

    return {
        "status": status,
        "per_serving": per_serving,
        "missing_inputs": missing[:10] if len(missing) > 10 else missing,  # Limit to 10
        "assumptions": assumptions
    }


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def process_all_recipes():
    """Process all recipe shards and add nutrition data."""
    shard_files = sorted(glob.glob('data/recipes-*.json'))

    total_processed = 0
    total_complete = 0
    total_partial = 0
    total_insufficient = 0

    for shard_file in shard_files:
        if 'index' in shard_file:
            continue

        print(f"\nProcessing {shard_file}...")

        with open(shard_file, 'r') as f:
            data = json.load(f)

        recipes = data.get('recipes', [])
        updated = 0

        for recipe in recipes:
            # Skip if already has complete nutrition
            existing = recipe.get('nutrition', {})
            if existing.get('status') == 'complete':
                total_complete += 1
                continue

            # Calculate nutrition
            nutrition = calculate_recipe_nutrition(recipe, default_servings=4)
            recipe['nutrition'] = nutrition
            updated += 1
            total_processed += 1

            if nutrition['status'] == 'complete':
                total_complete += 1
            elif nutrition['status'] == 'partial':
                total_partial += 1
            else:
                total_insufficient += 1

        # Save updated shard
        with open(shard_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"  Updated {updated} recipes")

    print(f"\n{'='*60}")
    print(f"NUTRITION PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"Total processed: {total_processed}")
    print(f"Complete: {total_complete}")
    print(f"Partial: {total_partial}")
    print(f"Insufficient data: {total_insufficient}")

    return total_processed, total_complete, total_partial, total_insufficient


if __name__ == "__main__":
    process_all_recipes()
