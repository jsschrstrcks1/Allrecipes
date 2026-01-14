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

    # =========================================================================
    # SUGARS & SWEETENERS
    # =========================================================================
    "sugar": {"cup": {"cal": 774, "fat": 0, "carbs": 200, "protein": 0, "sodium": 2, "fiber": 0, "sugar": 200},
             "tbsp": {"cal": 48, "fat": 0, "carbs": 12.5, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 12.5},
             "tsp": {"cal": 16, "fat": 0, "carbs": 4, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 4}},
    "brown sugar": {"cup": {"cal": 836, "fat": 0, "carbs": 216, "protein": 0, "sodium": 57, "fiber": 0, "sugar": 213},
                   "tbsp": {"cal": 52, "fat": 0, "carbs": 13.5, "protein": 0, "sodium": 4, "fiber": 0, "sugar": 13}},
    "powdered sugar": {"cup": {"cal": 467, "fat": 0, "carbs": 120, "protein": 0, "sodium": 1, "fiber": 0, "sugar": 117}},
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
            "tbsp": {"cal": 9, "fat": 0.5, "carbs": 0.75, "protein": 0.5, "sodium": 7, "fiber": 0, "sugar": 0.75}},
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
              "tsp": {"cal": 34, "fat": 4, "carbs": 0, "protein": 0, "sodium": 26, "fiber": 0, "sugar": 0}},
    "margarine": {"tbsp": {"cal": 100, "fat": 11, "carbs": 0, "protein": 0, "sodium": 90, "fiber": 0, "sugar": 0}},
    "vegetable oil": {"cup": {"cal": 1927, "fat": 218, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0},
                     "tbsp": {"cal": 120, "fat": 14, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}},
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
    "clams": {"cup": {"cal": 168, "fat": 2, "carbs": 6, "protein": 29, "sodium": 127, "fiber": 0, "sugar": 0}},
    "lobster": {"cup": {"cal": 142, "fat": 1, "carbs": 2, "protein": 30, "sodium": 705, "fiber": 0, "sugar": 0}},
    "anchovies": {"can": {"cal": 94, "fat": 4, "carbs": 0, "protein": 13, "sodium": 1651, "fiber": 0, "sugar": 0}},

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
              "tsp": {"cal": 4, "fat": 0, "carbs": 1, "protein": 0.2, "sodium": 1, "fiber": 0.1, "sugar": 0}},
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
            "to taste": {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 300, "fiber": 0, "sugar": 0}},
    "pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0},
              "to taste": {"cal": 1, "fat": 0, "carbs": 0.3, "protein": 0, "sodium": 0, "fiber": 0.1, "sugar": 0}},
    "black pepper": {"tsp": {"cal": 6, "fat": 0.1, "carbs": 1.5, "protein": 0.2, "sodium": 0, "fiber": 0.6, "sugar": 0}},
    "garlic powder": {"tsp": {"cal": 10, "fat": 0, "carbs": 2, "protein": 0.5, "sodium": 2, "fiber": 0.3, "sugar": 0}},
    "onion powder": {"tsp": {"cal": 8, "fat": 0, "carbs": 2, "protein": 0.2, "sodium": 2, "fiber": 0.2, "sugar": 0.4}},
    "cumin": {"tsp": {"cal": 8, "fat": 0.5, "carbs": 1, "protein": 0.4, "sodium": 4, "fiber": 0.2, "sugar": 0},
             "tbsp": {"cal": 22, "fat": 1.3, "carbs": 3, "protein": 1, "sodium": 10, "fiber": 0.6, "sugar": 0.1}},
    "paprika": {"tsp": {"cal": 6, "fat": 0.3, "carbs": 1.2, "protein": 0.3, "sodium": 2, "fiber": 0.8, "sugar": 0.5}},
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
    "bay leaf": {"": {"cal": 2, "fat": 0.1, "carbs": 0.5, "protein": 0, "sodium": 0, "fiber": 0.2, "sugar": 0}},
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

    # Remove prep notes after comma
    if "," in item:
        item = item.split(",")[0].strip()

    # Remove parenthetical notes
    item = re.sub(r'\s*\([^)]*\)', '', item)

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

    # Brand name normalization
    brand_map = {
        "grandma's molasses": "molasses",
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
# NUTRITION CALCULATION
# =============================================================================

def get_nutrition_for_ingredient(ingredient):
    """Calculate nutrition for a single ingredient entry."""
    item = normalize_ingredient(ingredient.get("item", ""))
    quantity = parse_quantity(ingredient.get("quantity", "1"))
    unit = normalize_unit(ingredient.get("unit", ""))

    # Handle compound units like "5-oz" or "6-inch" -> extract multiplier
    compound_match = re.match(r'^(\d+(?:\.\d+)?)-?(\w+)$', unit)
    if compound_match:
        unit_multiplier = float(compound_match.group(1))
        unit = compound_match.group(2)
        quantity = quantity * unit_multiplier

    # Handle "to taste" - minimal impact
    if "to taste" in str(ingredient.get("unit", "")).lower() or "to taste" in str(ingredient.get("item", "")).lower():
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
    servings = parse_servings(recipe.get("servings_yield", ""), default_servings)

    total = {"cal": 0, "fat": 0, "carbs": 0, "protein": 0, "sodium": 0, "fiber": 0, "sugar": 0}
    missing = []

    for ing in ingredients:
        nutr = get_nutrition_for_ingredient(ing)
        if nutr:
            for key in total:
                total[key] += nutr.get(key, 0)
        else:
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

    # Determine status
    total_ingredients = len(ingredients)
    missing_count = len(missing)

    if missing_count == 0:
        status = "complete"
    elif missing_count <= 2 or (total_ingredients > 0 and missing_count / total_ingredients <= 0.2):
        status = "partial"
    else:
        status = "insufficient_data"

    assumptions = [f"Calculated for {servings} servings"]
    if servings == default_servings and not recipe.get("servings_yield"):
        assumptions.append(f"Default serving size assumed ({default_servings})")

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
