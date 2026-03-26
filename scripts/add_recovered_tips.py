#!/usr/bin/env python3
"""
Add recovered tips, nutrition data, and editorial comments to recipes_master.json

This script processes all the overlooked content found during the comprehensive
image audit and adds it to the appropriate recipes.
"""

import json
from pathlib import Path
from datetime import datetime

RECIPES_FILE = Path(__file__).parent.parent / "all" / "recipes_master.json"

# Comprehensive list of recovered tips and updates
# Format: recipe_title -> {updates}
RECOVERED_CONTENT = {
    # === BATCH 1-50 ===

    "Crunchy Chocolate Malt Cupcakes": {
        "tips": [
            "Can be made up to 2 days ahead.",
            "Frosting can be stored 4 hours or overnight.",
            "Refrigerate until ready to serve, then sprinkle with the cereal."
        ]
    },

    "Mint Patty Cakes": {
        "tips": [
            "Refrigerate until set, at least 20 minutes.",
            "Serve cold."
        ]
    },

    "Bob's Oatmeal-Crusted Trout": {
        "tips": [
            "You can also try this recipe with salmon. - Bob Tuschman",
            "I was inspired by Irish recipes, which often use oats for breading fish."
        ],
        "attribution": "Bob Tuschman"
    },

    "Claudia's Turkish Dumplings": {
        "tips": [
            "I love manti, Turkish dumplings, with chili oil and yogurt. I thought it would be fun to try them with oatmeal! - Claudia Sidoti"
        ],
        "attribution": "Claudia Sidoti"
    },

    "Melissa D'Arabian's White Chili with Quick-Roasted Garlic": {
        "tips": [
            "Melissa's secret weapon: Quick-roasted garlic gives the chili deep flavor in minimal time."
        ],
        "attribution": "Melissa D'Arabian"
    },

    "Almost-Famous Broccoli-Cheddar Soup": {
        "tips": [
            "Panera Bread sells over 50 million cups of this soup annually.",
            "Or puree the soup in the pot with an immersion blender.",
            "Add up to 3/4 cup water if the soup is too thick."
        ]
    },

    "Aaron McCargo Jr.'s Steak Fajita Chili": {
        "tips": [
            "Aaron's secret weapon: Short ribs for extra richness.",
            "Ladle into bowls and garnish with guacamole, sour cream, cheese and fried tortilla strips for a little extra crunch."
        ],
        "attribution": "Aaron McCargo Jr."
    },

    "Tortilla Soup": {
        "tips": [
            "Citrus tricks your taste buds into craving less sodium.",
            "Stir 1/4 cup lime juice into the soup for brightness."
        ],
        "nutrition": {
            "calories": 270,
            "fat_g": 12,
            "cholesterol_mg": 20,
            "sodium_mg": 560,
            "carbs_g": 30,
            "fiber_g": 6,
            "protein_g": 13
        }
    },

    "Hawaiian Fish Lettuce Wraps": {
        "tips": [
            "Using lettuce instead of bread cuts calories significantly.",
            "You can do this for any sandwich to keep calories down."
        ],
        "nutrition": {
            "calories": 310,
            "fat_g": 14,
            "saturated_fat_g": 5,
            "cholesterol_mg": 30,
            "sodium_mg": 800,
            "carbs_g": 35,
            "fiber_g": 3,
            "protein_g": 14
        }
    },

    "Asian Chicken Salad": {
        "tips": [
            "The makeover cuts the fat by 80 percent while keeping the Colonel's secret herbs and spices."
        ],
        "nutrition": {
            "calories": 220,
            "fat_g": 8,
            "saturated_fat_g": 2,
            "cholesterol_mg": 30,
            "sodium_mg": 430,
            "carbs_g": 24,
            "fiber_g": 2,
            "protein_g": 14
        }
    },

    "Sloppy Joes": {
        "tips": [
            "The beans add lean protein.",
            "Fat per serving drops from 29 grams to just 13.",
            "Spread among four plates to control portions."
        ],
        "nutrition": {
            "calories": 310,
            "fat_g": 13,
            "saturated_fat_g": 3,
            "cholesterol_mg": 20,
            "sodium_mg": 520,
            "carbs_g": 37,
            "fiber_g": 5,
            "protein_g": 12
        }
    },

    "Daisy Potato Skins": {
        "tips": [
            "Save cooked potato for mashed potatoes or hash browns.",
            "Brush inside and outside of skins with steak seasoning and Parmesan."
        ]
    },

    "Warm and Creamy Bacon Dip": {
        "tips": [
            "Dip may also be placed in hollowed round sourdough loaf, wrapped in foil and heated in 400°F oven for 30 minutes.",
            "Serve with sliced French bread, crackers and/or chips."
        ]
    },

    "French Onion Burgers": {
        "tips": [
            "Top burgers with cheese and cook until cheese is melted.",
            "Serve burgers on buns with soup mixture for dipping."
        ]
    },

    "Very Strawberry Shortcake": {
        "tips": [
            "Turn out onto a lightly floured surface and knead 3 or 4 times. Pat dough to 1/2-inch thickness.",
            "Serve warm with sliced strawberries."
        ],
        "nutrition": {
            "calories": 130,
            "fat_g": 1.5,
            "saturated_fat_g": 0,
            "cholesterol_mg": 0,
            "sodium_mg": 350,
            "carbs_g": 25,
            "fiber_g": 1,
            "protein_g": 4
        }
    },

    "Zinfandel-Braised Leg of Lamb": {
        "tips": [
            "Broccoli rabe's bitterness is a pleasant foil to the sweet spices in the lamb dish.",
            "Pour the same wine you used for the lamb.",
            "You can make the cookies a couple of days in advance."
        ]
    },

    "Garlicky Broccoli Rabe": {
        "tips": [
            "Serve with lemon wedges.",
            "Drain and plunge into ice water to stop cooking and preserve bright green color."
        ]
    },

    "Broccoli and Chicken Noodle Soup": {
        "tips": [
            "If the broccoli florets are large, break into smaller pieces at the stalk instead of chopping them; they'll cook more quickly.",
            "Count on having dinner on the table in about 40 minutes.",
            "Serve this soup the moment it's done for the best results. In fact, if you wait, you'll find it gets thicker with time.",
            "If you have leftovers, you will want to thin the soup with a little chicken broth or milk to the desired consistency."
        ],
        "nutrition": {
            "calories": 317,
            "fat_g": 12.3,
            "saturated_fat_g": 6.8,
            "cholesterol_mg": 74,
            "sodium_mg": 723,
            "carbs_g": 23.8,
            "fiber_g": 1.9,
            "protein_g": 27.5,
            "mono_fat_g": 2.9,
            "poly_fat_g": 0.9,
            "iron_mg": 1.6,
            "calcium_mg": 179
        }
    },

    # === BATCH 51-100 ===

    "How to Make Fresh Tomato Sauce": {
        "tips": [
            "To peel tomatoes, core and cut a small X through the skin on the bottom with a sharp knife. Place in boiling water for about 30 seconds or just until skins begin to peel back. Quickly remove and plunge into ice water.",
            "Add garlic, and cook just until it begins to brown lightly, taking care not to burn it.",
            "Add enough of the pasta cooking water to the sauce to give the dish a creamy texture and marry the sauce to the pasta.",
            "Learn about common pasta shapes and how to pair them with the proper sauce at CookingLight.com/features"
        ]
    },

    "Ravioli with Herbed Ricotta Filling": {
        "tips": [
            "You can shape the pasta and freeze it up to a month before cooking.",
            "Use a sharp knife or a pasta wheel to cut the sheets crosswise into ravioli.",
            "Serve with a delicate sauce, and allow the pasta to be the star."
        ],
        "nutrition": {
            "calories": 394,
            "fat_g": 20.1,
            "saturated_fat_g": 8.3,
            "cholesterol_mg": 193,
            "sodium_mg": 733,
            "carbs_g": 33,
            "fiber_g": 0.4,
            "protein_g": 19,
            "mono_fat_g": 9.1,
            "poly_fat_g": 1.6,
            "iron_mg": 1.6,
            "calcium_mg": 263
        }
    },

    "Halibut with Coconut-Red Curry Sauce": {
        "tips": [
            "Prepare salad up to a day ahead (it's great for lunch). Sprinkle nuts on just before serving.",
            "A bed of seasoned rice with bok choy soaks up the sauce."
        ],
        "nutrition": {
            "calories": 278,
            "fat_g": 13.9,
            "saturated_fat_g": 8.6,
            "cholesterol_mg": 54,
            "sodium_mg": 475,
            "carbs_g": 10.9,
            "fiber_g": 1.2,
            "protein_g": 37,
            "mono_fat_g": 2.7,
            "poly_fat_g": 0.9,
            "iron_mg": 2,
            "calcium_mg": 102
        }
    },

    "Spicy Asian Noodles with Chicken": {
        "tips": [
            "Add a snow pea sauté to complete the meal.",
            "Sprinkle with peanuts just before serving."
        ],
        "nutrition": {
            "calories": 381,
            "fat_g": 8.1,
            "saturated_fat_g": 1.5,
            "cholesterol_mg": 60,
            "sodium_mg": 640,
            "carbs_g": 48.4,
            "fiber_g": 4.7,
            "protein_g": 27.1,
            "mono_fat_g": 3.2,
            "poly_fat_g": 2.7,
            "iron_mg": 3,
            "calcium_mg": 51
        }
    },

    "Tomato-Ricotta Spaghetti": {
        "tips": [
            "Get the most flavor: Use cooking techniques that intensify the taste of foods.",
            "Roasting tomatoes intensifies their sweetness.",
            "We also tested this recipe with grated Parmigiano-Reggiano—it's a splurge that makes the difference.",
            "Serve immediately."
        ],
        "nutrition": {
            "calories": 314,
            "fat_g": 8.4,
            "saturated_fat_g": 1.8,
            "cholesterol_mg": 4.6,
            "sodium_mg": 331,
            "carbs_g": 50.3,
            "fiber_g": 3.6,
            "protein_g": 10.5,
            "mono_fat_g": 4.7,
            "poly_fat_g": 1.4,
            "iron_mg": 2.7,
            "calcium_mg": 66
        }
    },

    "Stay Safe - Slow Cooker Tips": {
        "tips": [
            "Don't add frozen food to the slow cooker or use the cooker to defrost food—always defrost in the refrigerator or microwave.",
            "In a cooker, thawing food will linger too long between 40° and 140°, leaving it vulnerable to bacterial contamination.",
            "For the same reason, don't reheat food in the cooker."
        ]
    },

    "Borlotti Minestrone": {
        "tips": [
            "Borlotti beans—the Italian variety of cranberry beans—can be ordered from www.ranchogordo.com, among other online retailers.",
            "Runner beans tend to be buttery. Christmas limas have a distinct chestnut taste, and the bean broth is beefy.",
            "They've been saved from extinction because they taste good."
        ],
        "nutrition": {
            "calories": 224,
            "fat_g": 5.7,
            "saturated_fat_g": 2.4,
            "cholesterol_mg": 9,
            "sodium_mg": 662,
            "carbs_g": 31.6,
            "fiber_g": 10.7,
            "protein_g": 14.9,
            "mono_fat_g": 2.3,
            "poly_fat_g": 0.4,
            "iron_mg": 3,
            "calcium_mg": 199
        }
    },

    "Barley and Beef Soup": {
        "tips": [
            "Make this soup the night before to allow time for its flavors to develop.",
            "Pour hot servings into a thermos to take for lunch, or reheat individual portions in the microwave as needed.",
            "Serve the soup with crusty bread, crackers, or Spicy Whole-Wheat Pita Chips.",
            "Make dishes ahead when possible—like many soups and stews, this improves with time.",
            "Keep it separate: To prevent soggy sandwiches, pack separate zip-top bags of tomato slices, lettuce, and bread, then assemble just before serving.",
            "Don't dress leafy salads until you are ready to eat. Salt will draw moisture out of watery ingredients.",
            "Put leftovers to good use. Consider applying extras from dinner to the next day's lunch.",
            "Stay safe: Keep cold food cold (below 40°) and hot food hot (above 140°) as it travels.",
            "Use insulated lunch bags, coolers, thermoses, ice bags, and frozen gel packs.",
            "If re-heating items in a microwave, the USDA recommends they reach 165° and are served steaming hot."
        ],
        "nutrition": {
            "calories": 275,
            "fat_g": 5,
            "saturated_fat_g": 1.6,
            "cholesterol_mg": 43,
            "sodium_mg": 649,
            "carbs_g": 36,
            "fiber_g": 8,
            "protein_g": 21.8,
            "mono_fat_g": 2.3,
            "poly_fat_g": 0.3,
            "iron_mg": 3.1,
            "calcium_mg": 57
        }
    },

    "Yale College Punch": {
        "tips": [
            "Punch is back in style. Retro cocktails get all the attention these days, but punch predates individual mixed drinks by at least two centuries.",
            "From 'Punch: The Delights (and Dangers) of the Flowing Bowl' by drinks historian David Wondrich.",
            "Includes historically accurate recipes dating back as far as 1668.",
            "This recipe from 1867 is the 19th-century version of that college favorite 'jungle juice.'"
        ]
    },

    "Reduced-Sugar Banana Bread": {
        "tips": [
            "Lightly fold the banana mixture into the dry ingredients until just combined.",
            "The batter will be thick and chunky. Don't overmix or your loaf will be small and tough."
        ]
    },

    "Chocolate Crepes": {
        "tips": [
            "Place batter in fridge for 1 hour to allow flour to absorb liquid.",
            "Stack crepes with wax paper between each layer to prevent sticking.",
            "Serving Suggestion: Place several rows of fresh or frozen raspberries down the center of the crepe and fold in half. Dust with chocolate shavings and powdered sugar."
        ]
    },

    "Grape Turkey Chili": {
        "tips": [
            "An Antioxidant Punch: The deeper and darker the color of the produce, the higher the antioxidant power.",
            "Heart Healthy: Welch's 100% Grape Juice made from Concord grapes helps protect cardiovascular health.",
            "Good for the Mind: Emerging research suggests that what is good for the heart may also be good for the mind.",
            "Serve over warm polenta or rice, in taco shells, or in tortillas.",
            "Serve hot topped with red onion, cilantro, low-fat sour cream."
        ],
        "nutrition": {
            "calories": 250,
            "fat_g": 6,
            "saturated_fat_g": 1,
            "protein_g": 27,
            "cholesterol_mg": 0.8,
            "sodium_mg": 608
        }
    },

    "Raisin Fudge Pecan Pie": {
        "tips": [
            "Cool completely. Store in refrigerator.",
            "Top with whipped cream and sprinkle with cocoa, if desired."
        ]
    },

    "Applesauce Bread Pudding": {
        "tips": [
            "Pour mixture over bread cubes and let stand 25 minutes.",
            "Let cool 15 to 20 minutes and serve."
        ]
    },

    # === BATCH 101-152 ===

    "Meringue Swirls": {
        "tips": [
            "Store in an airtight container up to 1 week.",
            "Bake 1 hour, then turn off the oven and let the meringues stand in the oven until dry, about 2 hours."
        ]
    },

    "Golden Sesame Roll-Ups": {
        "tips": [
            "Wrap in the parchment paper and freeze until firm, about 30 minutes.",
            "Store in an airtight container up to 1 week."
        ]
    },

    "Double Chocolate Crackles": {
        "tips": [
            "Cover with plastic wrap and chill until firm, about 1 hour.",
            "Store in an airtight container up to 1 week.",
            "Host a cookie swap with a theme: all chocolate, maybe?"
        ]
    },

    "Mexican Chocolate Shortbread": {
        "tips": [
            "You can cover the dough with plastic wrap and use the bottom of a measuring cup to even it out.",
            "Refrigerate until the dough is firm, about 10 minutes.",
            "Store in an airtight container up to 1 week."
        ]
    },

    "Chocolate Mousse Torte": {
        "tips": [
            "Refrigerate 3 hours.",
            "Meanwhile, shave remaining chocolate square into curls.",
            "Top torte with remaining COOL WHIP, berries and chocolate curls."
        ]
    },

    "Gingerbread Cupcakes with Caramelized Mango Buttercream": {
        "tips": [
            "Cook until the sugar has melted and the mixture thickens slightly, about 2 minutes. Remove from the heat and let infuse for 30 minutes. Strain the syrup before using.",
            "Cook without stirring until the syrup reaches the soft-ball stage, 238° to 242° on a candy thermometer, immediately pour the syrup into the measuring cup to halt the cooking."
        ]
    },

    "Swedish Meatballs": {
        "tips": [
            "After you shape and bread the meatballs, you can freeze them for up to 2 weeks. To cook, fry for 5 to 6 minutes (do not thaw).",
            "Refrigerate at least 4 hours or overnight.",
            "Let stand 10 minutes after frying."
        ]
    },

    "McCormick Molten Spiced Chocolate Cabernet Cakes": {
        "tips": [
            "BAKE at preheated 425°F 14 to 15 minutes or until sides are firm but centers are soft.",
            "Let stand 1 minute. Carefully loosen edges with knife; Invert onto serving plates.",
            "Sprinkle with additional confectioners' sugar. Serve immediately."
        ]
    },

    "Herb-and-Mustard Sirloin with Baked Potatoes": {
        "tips": [
            "Let rest at least 5 minutes before slicing.",
            "Thinly slice the steak on the bias."
        ],
        "nutrition": {
            "calories": 478,
            "fat_g": 20,
            "saturated_fat_g": 11,
            "cholesterol_mg": 99,
            "sodium_mg": 217,
            "carbs_g": 31,
            "fiber_g": 3,
            "protein_g": 42
        }
    },

    "Lemon-Garlic Shrimp and Grits": {
        "tips": [
            "Done in 20 minutes.",
            "Cover to keep warm.",
            "Serve with lemon wedges."
        ],
        "nutrition": {
            "calories": 367,
            "fat_g": 12,
            "saturated_fat_g": 7,
            "cholesterol_mg": 309,
            "sodium_mg": 904,
            "carbs_g": 26,
            "fiber_g": 1,
            "protein_g": 34
        }
    },

    "Cheese Omelet with Roasted Tomatoes and Onions": {
        "nutrition": {
            "calories": 507,
            "fat_g": 35,
            "saturated_fat_g": 13,
            "cholesterol_mg": 579,
            "sodium_mg": 310,
            "carbs_g": 19,
            "fiber_g": 2,
            "protein_g": 27
        }
    },

    "Low-Fat Scalloped Potatoes": {
        "tips": [
            "We slimmed down the ultimate cold-weather side dish.",
            "Cook, stirring, until the paste puffs slightly, about 1 minute.",
            "Let rest 10 minutes before serving.",
            "Secret Ingredient - Milk: Instead of cream, we used low-fat and whole milk and saved 13g fat per serving."
        ],
        "nutrition": {
            "calories": 290,
            "fat_g": 7,
            "saturated_fat_g": 4,
            "cholesterol_mg": 22,
            "sodium_mg": 546,
            "carbs_g": 46,
            "fiber_g": 3,
            "protein_g": 10
        }
    },

    "Duff Goldman's Slightly Adapted Mamo's Potato Pancakes": {
        "tips": [
            "Duff's secret weapon: The large onion gives extra flavor.",
            "Let the potatoes settle, then pour out as much water as possible, leaving the starch in the bowl.",
            "Thin pancakes yield crispy ones.",
            "Fry until golden, 3 to 4 minutes per side. Drain on paper towels.",
            "Family serving suggestions: with poached pears, tart chunky homemade applesauce, cold sour cream and caviar, confectioner's sugar, or plain. Ronnie loves his with ketchup."
        ],
        "attribution": "Duff Goldman"
    },

    "Eggo Waffles with Spiced Apple Compote": {
        "tips": [
            "Chill, if desired.",
            "Serve warm with apple mixture on side."
        ]
    },

    "Rice Krispies Nutty Butterscotch Squares": {
        "tips": [
            "Refrigerate for 30 minutes. Cut into squares.",
            "Best if served the same day.",
            "Note: For best results, use fresh marshmallows."
        ]
    }
}


def find_recipe_by_title(recipes, title):
    """Find a recipe by title (case-insensitive, partial match)."""
    title_lower = title.lower()
    for recipe in recipes:
        if title_lower in recipe.get('title', '').lower():
            return recipe
        # Also check for exact match
        if recipe.get('title', '').lower() == title_lower:
            return recipe
    return None


def update_recipe(recipe, updates):
    """Update a recipe with recovered content."""
    modified = False

    # Add tips to notes
    if 'tips' in updates:
        existing_notes = recipe.get('notes', [])
        for tip in updates['tips']:
            # Check if tip already exists (avoid duplicates)
            if tip not in existing_notes:
                existing_notes.append(tip)
                modified = True
        recipe['notes'] = existing_notes

    # Update attribution if provided
    if 'attribution' in updates and not recipe.get('attribution'):
        recipe['attribution'] = updates['attribution']
        modified = True

    # Update nutrition data
    if 'nutrition' in updates:
        if 'nutrition' not in recipe:
            recipe['nutrition'] = {
                "status": "partial",
                "per_serving": {},
                "missing_inputs": [],
                "assumptions": ["Data extracted from magazine clipping"]
            }

        nutrition = updates['nutrition']
        per_serving = recipe['nutrition'].get('per_serving', {})

        # Map our keys to the schema keys
        key_mapping = {
            'calories': 'calories',
            'fat_g': 'fat_g',
            'saturated_fat_g': 'saturated_fat_g',
            'carbs_g': 'carbs_g',
            'protein_g': 'protein_g',
            'sodium_mg': 'sodium_mg',
            'fiber_g': 'fiber_g',
            'sugar_g': 'sugar_g',
            'cholesterol_mg': 'cholesterol_mg',
            'mono_fat_g': 'mono_fat_g',
            'poly_fat_g': 'poly_fat_g',
            'iron_mg': 'iron_mg',
            'calcium_mg': 'calcium_mg'
        }

        for our_key, schema_key in key_mapping.items():
            if our_key in nutrition:
                per_serving[schema_key] = nutrition[our_key]
                modified = True

        recipe['nutrition']['per_serving'] = per_serving

        # Update status based on completeness
        required_fields = ['calories', 'fat_g', 'carbs_g', 'protein_g']
        has_required = all(per_serving.get(f) is not None for f in required_fields)
        recipe['nutrition']['status'] = 'complete' if has_required else 'partial'

    return modified


def main():
    print("Loading recipes_master.json...")
    with open(RECIPES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    recipes = data.get('recipes', [])
    print(f"Found {len(recipes)} recipes")

    updated_count = 0
    not_found = []

    for title, updates in RECOVERED_CONTENT.items():
        recipe = find_recipe_by_title(recipes, title)
        if recipe:
            if update_recipe(recipe, updates):
                updated_count += 1
                print(f"  ✓ Updated: {recipe['title']}")
        else:
            not_found.append(title)

    # Update metadata
    data['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    # Write back
    print(f"\nWriting {updated_count} updates to recipes_master.json...")
    with open(RECIPES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Updated {updated_count} recipes with recovered tips and nutrition data")

    if not_found:
        print(f"\n⚠ Could not find {len(not_found)} recipes (may need manual review):")
        for title in not_found:
            print(f"  - {title}")

    return updated_count


if __name__ == '__main__':
    main()
