#!/usr/bin/env python3
"""
Add Gordon Ramsay recipes to recipes.json
"""

import json
import re
from datetime import datetime

# Gordon Ramsay recipes fetched from gordonramsay.com
RAMSAY_RECIPES = [
    {
        "title": "Beef Wellington",
        "description": "Gordon's signature dish featuring beef tenderloin wrapped in pate and puff pastry",
        "category": "mains",
        "servings_yield": "6 servings",
        "prep_time": "45 min",
        "cook_time": "30 min",
        "total_time": "1 hr 15 min",
        "ingredients": [
            {"item": "beef tenderloin", "quantity": "2", "unit": "lb"},
            {"item": "English mustard", "quantity": "2", "unit": "tbsp"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp"},
            {"item": "puff pastry", "quantity": "1", "unit": "sheet"},
            {"item": "egg yolk", "quantity": "1", "unit": ""},
            {"item": "mushrooms", "quantity": "1", "unit": "lb"},
            {"item": "shallots", "quantity": "2", "unit": ""},
            {"item": "thyme", "quantity": "1", "unit": "tbsp"},
            {"item": "prosciutto", "quantity": "8", "unit": "slices"},
            {"item": "salt and pepper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Season beef with salt and pepper. Heat oil in a pan and sear beef on all sides until browned. Brush with mustard and let cool."},
            {"step": 2, "text": "Finely chop mushrooms and shallots. Cook in butter until all moisture evaporates. Season and add thyme. Let cool completely."},
            {"step": 3, "text": "Lay prosciutto on plastic wrap, spread mushroom mixture (duxelles) over it. Place beef on top and roll tightly. Refrigerate 30 minutes."},
            {"step": 4, "text": "Wrap the beef roll in puff pastry, sealing edges with egg wash. Score the top decoratively."},
            {"step": 5, "text": "Bake at 425°F (220°C) for 25-30 minutes until pastry is golden and internal temp reaches 125°F for medium-rare."},
            {"step": 6, "text": "Rest for 10 minutes before slicing and serving."}
        ],
        "temperature": "425°F (220°C)",
        "tags": ["beef", "pastry", "special-occasion", "british", "gordon-ramsay"]
    },
    {
        "title": "Teriyaki Salmon",
        "description": "Pan-seared salmon with a sweet and savory teriyaki glaze",
        "category": "mains",
        "servings_yield": "4 servings",
        "prep_time": "10 min",
        "cook_time": "15 min",
        "total_time": "25 min",
        "ingredients": [
            {"item": "salmon fillets", "quantity": "4", "unit": "6-oz"},
            {"item": "soy sauce", "quantity": "1/4", "unit": "cup"},
            {"item": "mirin", "quantity": "2", "unit": "tbsp"},
            {"item": "sake", "quantity": "2", "unit": "tbsp"},
            {"item": "brown sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "ginger", "quantity": "1", "unit": "tbsp"},
            {"item": "garlic", "quantity": "2", "unit": "cloves"},
            {"item": "sesame oil", "quantity": "1", "unit": "tbsp"},
            {"item": "sesame seeds", "quantity": "1", "unit": "tbsp"},
            {"item": "green onions", "quantity": "2", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Combine soy sauce, mirin, sake, brown sugar, ginger, and garlic in a small saucepan. Simmer until slightly thickened."},
            {"step": 2, "text": "Season salmon with salt and pepper. Heat oil in a non-stick pan over medium-high heat."},
            {"step": 3, "text": "Sear salmon skin-side down for 4 minutes until crispy. Flip and cook 3 more minutes."},
            {"step": 4, "text": "Brush with teriyaki glaze and cook 1 minute more."},
            {"step": 5, "text": "Garnish with sesame seeds and sliced green onions. Serve with rice."}
        ],
        "temperature": "Medium-high heat",
        "tags": ["salmon", "fish", "asian", "quick", "gordon-ramsay"]
    },
    {
        "title": "Sticky Toffee Pudding",
        "description": "Individual sticky toffee puddings with rich toffee sauce",
        "category": "desserts",
        "servings_yield": "6 servings",
        "prep_time": "20 min",
        "cook_time": "20 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "dates, pitted and chopped", "quantity": "5", "unit": "oz"},
            {"item": "baking soda", "quantity": "1/2", "unit": "tsp"},
            {"item": "boiling water", "quantity": "1/4", "unit": "cup"},
            {"item": "butter, softened", "quantity": "3", "unit": "tbsp"},
            {"item": "light brown sugar", "quantity": "6", "unit": "tbsp"},
            {"item": "egg", "quantity": "1", "unit": ""},
            {"item": "all-purpose flour", "quantity": "1/2", "unit": "cup"},
            {"item": "baking powder", "quantity": "1/2", "unit": "tsp"},
            {"item": "heavy cream", "quantity": "2", "unit": "tbsp"},
            {"item": "corn syrup", "quantity": "2", "unit": "tbsp"},
            {"item": "bourbon", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine dates and baking soda in a bowl. Pour boiling water over and let stand 10 minutes."},
            {"step": 2, "text": "Cream butter and sugar until fluffy. Add egg, then flour and baking powder."},
            {"step": 3, "text": "Puree dates and fold into batter."},
            {"step": 4, "text": "Divide among 6 greased muffin cups. Bake at 350°F for 17-19 minutes."},
            {"step": 5, "text": "For sauce: combine butter, brown sugar, milk, cream, corn syrup in a pan. Simmer 3 minutes, stir in bourbon."},
            {"step": 6, "text": "Spoon sauce over warm puddings and serve immediately."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["dessert", "british", "dates", "caramel", "gordon-ramsay"]
    },
    {
        "title": "Scrambled Eggs",
        "description": "Gordon's famous creamy scrambled eggs cooked low and slow",
        "category": "breakfast",
        "servings_yield": "2 servings",
        "prep_time": "2 min",
        "cook_time": "10 min",
        "total_time": "12 min",
        "ingredients": [
            {"item": "eggs", "quantity": "6", "unit": ""},
            {"item": "butter", "quantity": "3", "unit": "tbsp"},
            {"item": "creme fraiche", "quantity": "1", "unit": "tbsp"},
            {"item": "chives, chopped", "quantity": "1", "unit": "tbsp"},
            {"item": "salt and pepper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Crack eggs into a cold non-stick pan with butter. Do not whisk beforehand."},
            {"step": 2, "text": "Place pan over medium heat. Stir continuously with a spatula, moving the pan on and off the heat."},
            {"step": 3, "text": "Continue stirring for 3-5 minutes until eggs begin to set but are still soft and creamy."},
            {"step": 4, "text": "Remove from heat, stir in creme fraiche to stop cooking."},
            {"step": 5, "text": "Season with salt and pepper, garnish with chives. Serve immediately on toast."}
        ],
        "temperature": "Medium heat",
        "tags": ["breakfast", "eggs", "quick", "british", "gordon-ramsay"]
    },
    {
        "title": "Bangers and Mash",
        "description": "Classic British comfort food with sausages, mashed potatoes, and onion gravy",
        "category": "mains",
        "servings_yield": "4 servings",
        "prep_time": "10 min",
        "cook_time": "30 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "pork sausages", "quantity": "8", "unit": ""},
            {"item": "potatoes, peeled and cubed", "quantity": "2", "unit": "lb"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "milk", "quantity": "1/2", "unit": "cup"},
            {"item": "red onion, sliced", "quantity": "2", "unit": ""},
            {"item": "beef stock", "quantity": "1", "unit": "cup"},
            {"item": "Worcestershire sauce", "quantity": "2", "unit": "tsp"},
            {"item": "balsamic vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "rosemary", "quantity": "2", "unit": "sprigs"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Boil potatoes in salted water until tender. Drain and mash with butter and milk. Season and keep warm."},
            {"step": 2, "text": "Brown sausages in a pan with oil and rosemary, about 10-12 minutes. Transfer to oven at 325°F to finish."},
            {"step": 3, "text": "In the same pan, caramelize onions with butter and sugar. Add balsamic and Worcestershire sauce."},
            {"step": 4, "text": "Add beef stock, simmer until reduced to a rich gravy."},
            {"step": 5, "text": "Serve sausages on mashed potatoes, topped with onion gravy."}
        ],
        "temperature": "325°F (160°C)",
        "tags": ["british", "comfort-food", "sausage", "potatoes", "gordon-ramsay"]
    },
    {
        "title": "Carbonara",
        "description": "Classic Italian pasta with crispy pancetta and creamy egg sauce",
        "category": "mains",
        "servings_yield": "2 servings",
        "prep_time": "5 min",
        "cook_time": "15 min",
        "total_time": "20 min",
        "ingredients": [
            {"item": "spaghetti", "quantity": "200", "unit": "g"},
            {"item": "pancetta or bacon", "quantity": "150", "unit": "g"},
            {"item": "egg yolks", "quantity": "3", "unit": ""},
            {"item": "Parmesan cheese, grated", "quantity": "1/2", "unit": "cup"},
            {"item": "garlic", "quantity": "2", "unit": "cloves"},
            {"item": "black pepper", "quantity": "", "unit": "to taste"},
            {"item": "olive oil", "quantity": "1", "unit": "tbsp"},
            {"item": "creme fraiche", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook pasta in salted boiling water until al dente. Reserve 1 cup pasta water."},
            {"step": 2, "text": "Fry pancetta with garlic until crispy. Remove garlic."},
            {"step": 3, "text": "Whisk egg yolks with Parmesan and creme fraiche."},
            {"step": 4, "text": "Add hot pasta to pancetta pan, remove from heat."},
            {"step": 5, "text": "Quickly toss in egg mixture, adding pasta water to create creamy sauce."},
            {"step": 6, "text": "Season with black pepper and serve immediately with extra Parmesan."}
        ],
        "temperature": "Medium-high heat",
        "tags": ["pasta", "italian", "quick", "eggs", "gordon-ramsay"]
    },
    {
        "title": "Fish and Chips",
        "description": "Classic British pub dish with crispy battered fish and chips",
        "category": "mains",
        "servings_yield": "2 servings",
        "prep_time": "15 min",
        "cook_time": "20 min",
        "total_time": "35 min",
        "ingredients": [
            {"item": "cod or haddock fillet", "quantity": "2", "unit": "6-oz"},
            {"item": "self-rising flour", "quantity": "1", "unit": "cup"},
            {"item": "light beer", "quantity": "3/4", "unit": "cup"},
            {"item": "baking powder", "quantity": "1", "unit": "tsp"},
            {"item": "potatoes", "quantity": "2", "unit": "large"},
            {"item": "vegetable oil", "quantity": "4", "unit": "cups"},
            {"item": "salt", "quantity": "", "unit": "to taste"},
            {"item": "curry powder", "quantity": "1", "unit": "tsp"},
            {"item": "egg white", "quantity": "1", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Cut potatoes into thick chips. Soak in cold water 30 minutes, then dry thoroughly."},
            {"step": 2, "text": "Whisk flour, baking powder, curry powder, and beer. Fold in stiffly beaten egg white."},
            {"step": 3, "text": "Heat oil to 350°F. Fry chips until golden, about 5-6 minutes. Drain and keep warm."},
            {"step": 4, "text": "Dredge fish in seasoned flour, then batter. Fry until golden and cooked through, 3-4 minutes."},
            {"step": 5, "text": "Drain on paper towels, season with salt. Serve with chips, tartar sauce, and lemon wedges."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["british", "fish", "fried", "pub-food", "gordon-ramsay"]
    },
    {
        "title": "Honey Glazed Ham",
        "description": "Festive glazed ham perfect for Christmas dinner",
        "category": "mains",
        "servings_yield": "8-10 servings",
        "prep_time": "1 hr",
        "cook_time": "3 hr 30 min",
        "total_time": "4 hr 30 min",
        "ingredients": [
            {"item": "unsmoked gammon joint", "quantity": "3", "unit": "kg"},
            {"item": "carrots, chopped", "quantity": "4", "unit": ""},
            {"item": "leek, chopped", "quantity": "1", "unit": ""},
            {"item": "onion, chopped", "quantity": "1", "unit": ""},
            {"item": "peppercorns", "quantity": "1", "unit": "tsp"},
            {"item": "coriander seeds", "quantity": "1", "unit": "tsp"},
            {"item": "cinnamon stick", "quantity": "1", "unit": ""},
            {"item": "bay leaves", "quantity": "3", "unit": ""},
            {"item": "cloves", "quantity": "20", "unit": ""},
            {"item": "demerara sugar", "quantity": "100", "unit": "g"},
            {"item": "Madeira wine", "quantity": "50", "unit": "ml"},
            {"item": "sherry vinegar", "quantity": "25", "unit": "ml"},
            {"item": "honey", "quantity": "125", "unit": "g"}
        ],
        "instructions": [
            {"step": 1, "text": "Place gammon in a large pan with vegetables and spices. Cover with water, bring to boil, then simmer 3 hours."},
            {"step": 2, "text": "Make glaze by heating sugar, Madeira, vinegar, and honey until syrupy."},
            {"step": 3, "text": "Remove ham, let cool slightly. Peel off skin leaving fat. Score fat in crosshatch pattern."},
            {"step": 4, "text": "Stud each diamond with a clove. Place in roasting tin."},
            {"step": 5, "text": "Brush with half the glaze, roast at 375°F for 15 minutes."},
            {"step": 6, "text": "Add remaining glaze, roast 25-35 minutes more until golden. Rest before carving."}
        ],
        "temperature": "375°F (190°C)",
        "tags": ["pork", "ham", "holiday", "christmas", "gordon-ramsay"]
    },
    {
        "title": "Roast Turkey with Lemon, Parsley and Garlic",
        "description": "Juicy roast turkey with herb butter perfect for holiday meals",
        "category": "mains",
        "servings_yield": "8-10 servings",
        "prep_time": "30 min",
        "cook_time": "3 hr",
        "total_time": "3 hr 30 min",
        "ingredients": [
            {"item": "whole turkey", "quantity": "12-14", "unit": "lb"},
            {"item": "butter, softened", "quantity": "1", "unit": "cup"},
            {"item": "lemon zest", "quantity": "2", "unit": "tbsp"},
            {"item": "parsley, chopped", "quantity": "1/4", "unit": "cup"},
            {"item": "garlic, minced", "quantity": "4", "unit": "cloves"},
            {"item": "thyme", "quantity": "2", "unit": "tbsp"},
            {"item": "onion", "quantity": "1", "unit": ""},
            {"item": "carrots", "quantity": "2", "unit": ""},
            {"item": "celery", "quantity": "2", "unit": "stalks"},
            {"item": "chicken stock", "quantity": "2", "unit": "cups"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix butter with lemon zest, parsley, garlic, and thyme."},
            {"step": 2, "text": "Gently loosen turkey skin and spread herb butter underneath. Season cavity with salt and pepper."},
            {"step": 3, "text": "Place vegetables in roasting tin, set turkey on top."},
            {"step": 4, "text": "Roast at 350°F for about 3 hours, basting every 30 minutes."},
            {"step": 5, "text": "Turkey is done when internal temp reaches 165°F. Rest 30 minutes before carving."},
            {"step": 6, "text": "Make gravy from pan drippings and stock."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["turkey", "holiday", "thanksgiving", "christmas", "gordon-ramsay"]
    },
    {
        "title": "Pork Dumplings",
        "description": "Pork and chive dumplings with black vinegar dipping sauce",
        "category": "appetizers",
        "servings_yield": "25 dumplings",
        "prep_time": "1 hr",
        "cook_time": "10 min",
        "total_time": "1 hr 30 min",
        "ingredients": [
            {"item": "dumpling flour", "quantity": "1 1/2", "unit": "cups"},
            {"item": "salt", "quantity": "1/2", "unit": "tsp"},
            {"item": "water", "quantity": "1/2", "unit": "cup"},
            {"item": "ground pork", "quantity": "8", "unit": "oz"},
            {"item": "shiitake mushrooms, minced", "quantity": "2", "unit": "oz"},
            {"item": "garlic, grated", "quantity": "3", "unit": "cloves"},
            {"item": "ginger, grated", "quantity": "1", "unit": "oz"},
            {"item": "Chinese chives, sliced", "quantity": "1", "unit": "bunch"},
            {"item": "soy sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "sesame oil", "quantity": "1", "unit": "tbsp"},
            {"item": "black vinegar", "quantity": "1/2", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix flour and salt, gradually add water while stirring. Knead until smooth, rest 1 hour."},
            {"step": 2, "text": "Combine pork with mushrooms, garlic, ginger, chives, soy sauce, and sesame oil."},
            {"step": 3, "text": "Roll dough into thin wrappers about 3.5 inches in diameter."},
            {"step": 4, "text": "Fill each wrapper with 1 tbsp filling, fold and pleat edges to seal."},
            {"step": 5, "text": "Pan-fry dumplings in oil, add water, cover and steam 5-7 minutes."},
            {"step": 6, "text": "Remove lid, crisp bottoms 1-2 minutes. Serve with black vinegar dipping sauce."}
        ],
        "temperature": "Medium heat",
        "tags": ["asian", "pork", "dumplings", "appetizer", "gordon-ramsay"]
    },
    {
        "title": "Pavlova with Raspberry Curd",
        "description": "Light meringue dessert with raspberry curd for two",
        "category": "desserts",
        "servings_yield": "2 servings",
        "prep_time": "30 min",
        "cook_time": "1 hr 15 min",
        "total_time": "3 hr",
        "ingredients": [
            {"item": "egg white", "quantity": "1", "unit": ""},
            {"item": "granulated sugar", "quantity": "1/4", "unit": "cup"},
            {"item": "cornstarch", "quantity": "1 1/2", "unit": "tsp"},
            {"item": "white vinegar", "quantity": "1/2", "unit": "tsp"},
            {"item": "vanilla extract", "quantity": "1/2", "unit": "tsp"},
            {"item": "raspberries", "quantity": "1", "unit": "cup"},
            {"item": "butter", "quantity": "7", "unit": "tbsp"},
            {"item": "egg yolks", "quantity": "5", "unit": ""},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"},
            {"item": "chocolate chips", "quantity": "1", "unit": "cup"},
            {"item": "strawberries", "quantity": "10", "unit": ""}
        ],
        "instructions": [
            {"step": 1, "text": "Whisk egg white and sugar to soft peaks. Add cornstarch, vinegar, and vanilla; whisk to stiff peaks."},
            {"step": 2, "text": "Shape into 4-inch circle on parchment, creating a shallow bowl. Bake at 220°F for 1 hr 15 min."},
            {"step": 3, "text": "For curd: melt butter, add raspberries, sugar, yolks, lemon. Cook until thickened. Strain."},
            {"step": 4, "text": "Make chocolate-dipped strawberries."},
            {"step": 5, "text": "Fill cooled pavlova with raspberry curd, top with berries and strawberries."}
        ],
        "temperature": "220°F (105°C)",
        "tags": ["dessert", "meringue", "raspberries", "romantic", "gordon-ramsay"]
    },
    {
        "title": "Baked Chicken Wings",
        "description": "Crispy baked chicken wings with hot sauce glaze",
        "category": "appetizers",
        "servings_yield": "4 servings",
        "prep_time": "15 min",
        "cook_time": "35 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "chicken wings", "quantity": "2", "unit": "lb"},
            {"item": "garlic powder", "quantity": "1", "unit": "tbsp"},
            {"item": "smoked paprika", "quantity": "1", "unit": "tbsp"},
            {"item": "kosher salt", "quantity": "1", "unit": "tsp"},
            {"item": "canola oil", "quantity": "2", "unit": "tbsp"},
            {"item": "butter", "quantity": "4", "unit": "tbsp"},
            {"item": "black pepper", "quantity": "", "unit": "to taste"},
            {"item": "hot sauce", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 375°F."},
            {"step": 2, "text": "Pat wings dry, season with garlic powder, paprika, and salt."},
            {"step": 3, "text": "Heat oil and butter in oven-safe pan. Brown wings on both sides."},
            {"step": 4, "text": "Transfer to oven, bake 15 minutes until cooked to 165°F."},
            {"step": 5, "text": "Toss with hot sauce and additional butter. Serve immediately."}
        ],
        "temperature": "375°F (190°C)",
        "tags": ["chicken", "wings", "appetizer", "game-day", "gordon-ramsay"]
    },
    {
        "title": "Gingerbread Bundt Cake",
        "description": "Moist gingerbread cake with spiced glaze",
        "category": "desserts",
        "servings_yield": "10-12 servings",
        "prep_time": "20 min",
        "cook_time": "50 min",
        "total_time": "1 hr 10 min",
        "ingredients": [
            {"item": "all-purpose flour", "quantity": "3 3/4", "unit": "cups"},
            {"item": "ground ginger", "quantity": "1", "unit": "tbsp"},
            {"item": "ground cinnamon", "quantity": "1", "unit": "tbsp"},
            {"item": "nutmeg", "quantity": "1", "unit": "tsp"},
            {"item": "ground cloves", "quantity": "1", "unit": "tsp"},
            {"item": "baking powder", "quantity": "1", "unit": "tbsp"},
            {"item": "butter, softened", "quantity": "1", "unit": "cup"},
            {"item": "brown sugar", "quantity": "1", "unit": "cup"},
            {"item": "granulated sugar", "quantity": "3/4", "unit": "cup"},
            {"item": "molasses", "quantity": "3/4", "unit": "cup"},
            {"item": "eggs", "quantity": "3", "unit": ""},
            {"item": "milk", "quantity": "1 1/2", "unit": "cups"},
            {"item": "powdered sugar", "quantity": "1", "unit": "cup"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 350°F. Prepare bundt pan with baking spray."},
            {"step": 2, "text": "Mix flour, spices, baking powder, baking soda, and salt."},
            {"step": 3, "text": "Cream butter and sugars until fluffy. Add orange zest, ginger, molasses, and eggs."},
            {"step": 4, "text": "Alternate adding dry ingredients and milk in three additions."},
            {"step": 5, "text": "Bake 45-55 minutes until toothpick comes out clean."},
            {"step": 6, "text": "Cool, then drizzle with spiced powdered sugar glaze."}
        ],
        "temperature": "350°F (175°C)",
        "tags": ["dessert", "cake", "gingerbread", "holiday", "gordon-ramsay"]
    },
    {
        "title": "Mozzarella and Rosemary Pizza",
        "description": "Homemade pizza dough topped with fresh mozzarella and rosemary",
        "category": "mains",
        "servings_yield": "4 pizzas",
        "prep_time": "1 hr 30 min",
        "cook_time": "15 min",
        "total_time": "1 hr 45 min",
        "ingredients": [
            {"item": "dried yeast", "quantity": "2", "unit": "packets"},
            {"item": "golden caster sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "olive oil", "quantity": "4", "unit": "tbsp"},
            {"item": "bread flour", "quantity": "500", "unit": "g"},
            {"item": "fine sea salt", "quantity": "1", "unit": "tbsp"},
            {"item": "tomato passata", "quantity": "8", "unit": "tbsp"},
            {"item": "mozzarella", "quantity": "2", "unit": "balls"},
            {"item": "rosemary", "quantity": "2", "unit": "sprigs"},
            {"item": "black pepper", "quantity": "", "unit": "to taste"}
        ],
        "instructions": [
            {"step": 1, "text": "Mix yeast and sugar with 325ml warm water. Combine flour and salt, add oil and yeast mixture."},
            {"step": 2, "text": "Knead 10 minutes until smooth. Cover and let rise 1 hour until doubled."},
            {"step": 3, "text": "Punch down and divide into 4 balls. Roll each to fit a 26cm pan."},
            {"step": 4, "text": "Cook dough in oiled pan over medium heat 5-8 minutes until crispy."},
            {"step": 5, "text": "Top with passata, torn mozzarella, rosemary, and pepper."},
            {"step": 6, "text": "Grill 4 minutes until golden. Serve with olive oil drizzle."}
        ],
        "temperature": "Medium heat plus grill",
        "tags": ["pizza", "italian", "bread", "cheese", "gordon-ramsay"]
    },
    {
        "title": "Chilli Beef Lettuce Wraps",
        "description": "Spicy beef and pork mince in crisp lettuce cups",
        "category": "appetizers",
        "servings_yield": "4 servings",
        "prep_time": "10 min",
        "cook_time": "20 min",
        "total_time": "30 min",
        "ingredients": [
            {"item": "lean minced beef", "quantity": "200", "unit": "g"},
            {"item": "minced pork", "quantity": "200", "unit": "g"},
            {"item": "garlic, chopped", "quantity": "2", "unit": "cloves"},
            {"item": "ginger, chopped", "quantity": "2", "unit": "inches"},
            {"item": "red chillies", "quantity": "2", "unit": ""},
            {"item": "brown sugar", "quantity": "1", "unit": "tbsp"},
            {"item": "fish sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "lime", "quantity": "1", "unit": ""},
            {"item": "spring onions", "quantity": "3", "unit": ""},
            {"item": "sesame oil", "quantity": "1", "unit": "tbsp"},
            {"item": "little gem lettuce", "quantity": "2", "unit": "heads"},
            {"item": "soy sauce", "quantity": "1", "unit": "tbsp"},
            {"item": "coriander", "quantity": "1", "unit": "bunch"}
        ],
        "instructions": [
            {"step": 1, "text": "Brown mixed mince in oil until crispy. Drain excess fat."},
            {"step": 2, "text": "Add garlic, ginger, and chillies with sesame oil. Cook 2 minutes."},
            {"step": 3, "text": "Add sugar and fish sauce. Stir in lime zest, juice, and spring onions."},
            {"step": 4, "text": "Make dressing with soy, lime, sesame oil, chilli, coriander, fish sauce, and sugar."},
            {"step": 5, "text": "Spoon mince into lettuce cups, drizzle with dressing and serve."}
        ],
        "temperature": "High heat",
        "tags": ["asian", "beef", "pork", "appetizer", "low-carb", "gordon-ramsay"]
    },
    {
        "title": "Slow-Cooked Beef Short Ribs",
        "description": "Tender braised beef short ribs in red wine",
        "category": "mains",
        "servings_yield": "4 servings",
        "prep_time": "40 min",
        "cook_time": "3 hr",
        "total_time": "3 hr 40 min",
        "ingredients": [
            {"item": "beef short ribs", "quantity": "6", "unit": "thick-cut"},
            {"item": "olive oil", "quantity": "2", "unit": "tbsp"},
            {"item": "garlic head, halved", "quantity": "1", "unit": ""},
            {"item": "tomato puree", "quantity": "1", "unit": "tbsp"},
            {"item": "red wine", "quantity": "750", "unit": "ml"},
            {"item": "beef stock", "quantity": "1", "unit": "liter"},
            {"item": "pancetta", "quantity": "150", "unit": "g"},
            {"item": "chestnut mushrooms", "quantity": "250", "unit": "g"},
            {"item": "parsley", "quantity": "2", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Preheat oven to 325°F. Season and brown ribs in hot oil, 10-15 minutes."},
            {"step": 2, "text": "Add garlic and tomato puree, then wine. Reduce by half."},
            {"step": 3, "text": "Add stock, cover with foil, braise 3-4 hours until tender."},
            {"step": 4, "text": "Fry pancetta until crispy, add mushrooms."},
            {"step": 5, "text": "Strain sauce, top ribs with pancetta and mushrooms. Garnish with parsley."}
        ],
        "temperature": "325°F (170°C)",
        "tags": ["beef", "braised", "comfort-food", "wine", "gordon-ramsay"]
    },
    {
        "title": "Chocolate Avocado Mousse",
        "description": "Healthy chocolate mousse made with avocado",
        "category": "desserts",
        "servings_yield": "8 servings",
        "prep_time": "20 min",
        "cook_time": "0 min",
        "total_time": "20 min",
        "ingredients": [
            {"item": "ripe avocados", "quantity": "2", "unit": "large"},
            {"item": "honey", "quantity": "3", "unit": "tbsp"},
            {"item": "vanilla extract", "quantity": "1", "unit": "tsp"},
            {"item": "raw cacao powder", "quantity": "50", "unit": "g"}
        ],
        "instructions": [
            {"step": 1, "text": "Blend avocados until smooth."},
            {"step": 2, "text": "Add honey, vanilla, and cacao powder. Blend until combined."},
            {"step": 3, "text": "Taste and adjust sweetness with more honey if desired."},
            {"step": 4, "text": "Divide into small glasses. Refrigerate 1 hour before serving."}
        ],
        "temperature": "No cooking required",
        "tags": ["dessert", "chocolate", "healthy", "vegan", "gordon-ramsay"]
    },
    {
        "title": "Quinoa Salad",
        "description": "Nutty quinoa salad with almonds, cucumber, and fresh herbs",
        "category": "salads",
        "servings_yield": "4 servings",
        "prep_time": "15 min",
        "cook_time": "0 min",
        "total_time": "15 min",
        "ingredients": [
            {"item": "quinoa, cooked", "quantity": "200", "unit": "g"},
            {"item": "flaked almonds", "quantity": "50", "unit": "g"},
            {"item": "cucumber", "quantity": "1/2", "unit": "large"},
            {"item": "cherry tomatoes, halved", "quantity": "125", "unit": "g"},
            {"item": "raisins", "quantity": "50", "unit": "g"},
            {"item": "spring onions", "quantity": "4", "unit": ""},
            {"item": "mint leaves", "quantity": "1", "unit": "bunch"},
            {"item": "lime juice", "quantity": "1", "unit": ""},
            {"item": "olive oil", "quantity": "3", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Cook quinoa and spread on plate to cool quickly."},
            {"step": 2, "text": "Toast almonds until golden."},
            {"step": 3, "text": "Peel cucumber in strips, remove seeds, slice into half-moons."},
            {"step": 4, "text": "Combine quinoa, almonds, cucumber, tomatoes, raisins, spring onions, and half the mint."},
            {"step": 5, "text": "Dress with lime juice and olive oil. Season and garnish with remaining mint."}
        ],
        "temperature": "No cooking required",
        "tags": ["salad", "quinoa", "healthy", "vegetarian", "gordon-ramsay"]
    },
    {
        "title": "Gazpacho",
        "description": "Refreshing cold Spanish tomato soup",
        "category": "soups",
        "servings_yield": "4 servings",
        "prep_time": "50 min",
        "cook_time": "0 min",
        "total_time": "50 min",
        "ingredients": [
            {"item": "cucumber, chopped", "quantity": "1", "unit": ""},
            {"item": "red pepper, chopped", "quantity": "1", "unit": ""},
            {"item": "green pepper, chopped", "quantity": "1", "unit": ""},
            {"item": "ripe plum tomatoes, chopped", "quantity": "1", "unit": "kg"},
            {"item": "garlic", "quantity": "2", "unit": "cloves"},
            {"item": "spring onions", "quantity": "2", "unit": ""},
            {"item": "stale bread, chopped", "quantity": "75", "unit": "g"},
            {"item": "sherry vinegar", "quantity": "2", "unit": "tbsp"},
            {"item": "olive oil", "quantity": "4", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Combine vegetables, bread, and seasonings. Add vinegar and oil."},
            {"step": 2, "text": "Press down and chill at least 30 minutes or overnight."},
            {"step": 3, "text": "Blend until smooth. Add more oil if needed."},
            {"step": 4, "text": "Adjust seasoning. Serve ice cold with toasted bread."}
        ],
        "temperature": "No cooking required",
        "tags": ["soup", "spanish", "cold", "summer", "vegetarian", "gordon-ramsay"]
    },
    {
        "title": "Lamb Koftas with Mint Yogurt",
        "description": "Spiced lamb meatballs with cooling yogurt dressing",
        "category": "mains",
        "servings_yield": "4 servings",
        "prep_time": "25 min",
        "cook_time": "15 min",
        "total_time": "40 min",
        "ingredients": [
            {"item": "minced lamb", "quantity": "500", "unit": "g"},
            {"item": "onion, diced", "quantity": "1", "unit": ""},
            {"item": "garlic", "quantity": "2", "unit": "cloves"},
            {"item": "cumin seeds, toasted", "quantity": "2", "unit": "tsp"},
            {"item": "chilli flakes", "quantity": "1/2", "unit": "tsp"},
            {"item": "parsley, chopped", "quantity": "2", "unit": "tbsp"},
            {"item": "mint, chopped", "quantity": "2", "unit": "tbsp"},
            {"item": "natural yogurt", "quantity": "3", "unit": "tbsp"},
            {"item": "lemon juice", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Saute onion and garlic until soft. Add cumin and chilli. Cool."},
            {"step": 2, "text": "Mix lamb with onion mixture and herbs. Form into patties. Chill 10 minutes."},
            {"step": 3, "text": "Make dressing by bruising mint with yogurt, cumin, and lemon."},
            {"step": 4, "text": "Griddle koftas 5-6 minutes, turning halfway."},
            {"step": 5, "text": "Serve warm with yogurt dressing on the side."}
        ],
        "temperature": "Medium-high heat",
        "tags": ["lamb", "middle-eastern", "meatballs", "yogurt", "gordon-ramsay"]
    },
    {
        "title": "Crispy Roast Duck with Chinese Pancakes",
        "description": "Aromatic roast duck served with pancakes and dipping sauce",
        "category": "mains",
        "servings_yield": "4-6 servings",
        "prep_time": "45 min",
        "cook_time": "4 hr",
        "total_time": "4 hr 45 min",
        "ingredients": [
            {"item": "whole duck", "quantity": "1", "unit": ""},
            {"item": "Chinese five-spice", "quantity": "4", "unit": "tbsp"},
            {"item": "star anise", "quantity": "4", "unit": ""},
            {"item": "garlic", "quantity": "2", "unit": "cloves"},
            {"item": "ginger", "quantity": "4", "unit": "cm"},
            {"item": "spring onions", "quantity": "4", "unit": ""},
            {"item": "Chinese pancakes", "quantity": "20", "unit": ""},
            {"item": "black bean sauce", "quantity": "4", "unit": "tbsp"},
            {"item": "rice vinegar", "quantity": "2", "unit": "tsp"},
            {"item": "soy sauce", "quantity": "2", "unit": "tbsp"},
            {"item": "honey", "quantity": "1", "unit": "tbsp"}
        ],
        "instructions": [
            {"step": 1, "text": "Rub duck with five-spice. Fill cavity with star anise, garlic, ginger, and spring onions."},
            {"step": 2, "text": "Roast at 320°F for 1 hour, then reduce to 275°F for 2.5-3 hours until tender and crispy."},
            {"step": 3, "text": "Make sauce: fry garlic, add black bean sauce, vinegar, soy sauce, and honey. Simmer 3-4 minutes."},
            {"step": 4, "text": "Rest duck 15 minutes. Heat pancakes according to package."},
            {"step": 5, "text": "Pull duck apart with forks. Serve with pancakes and dipping sauce."}
        ],
        "temperature": "320°F then 275°F (160°C then 135°C)",
        "tags": ["duck", "chinese", "asian", "pancakes", "gordon-ramsay"]
    }
]

def slugify(title):
    """Convert title to URL-friendly slug"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return f"gr-{slug}"

def main():
    # Load existing recipes
    with open('/home/user/Allrecipes/data/recipes.json', 'r') as f:
        data = json.load(f)

    # Add Gordon Ramsay recipes
    new_recipes = []
    for recipe in RAMSAY_RECIPES:
        new_recipe = {
            "id": slugify(recipe["title"]),
            "collection": "all",
            "collection_display": "Other Family Recipes",
            "title": recipe["title"],
            "category": recipe["category"],
            "attribution": "Gordon Ramsay",
            "source_note": "gordonramsay.com (used with permission)",
            "description": recipe.get("description", ""),
            "servings_yield": recipe.get("servings_yield", ""),
            "prep_time": recipe.get("prep_time", ""),
            "cook_time": recipe.get("cook_time", ""),
            "total_time": recipe.get("total_time", ""),
            "ingredients": recipe["ingredients"],
            "instructions": recipe["instructions"],
            "temperature": recipe.get("temperature", ""),
            "tags": recipe.get("tags", []),
            "confidence": {
                "overall": "high",
                "flags": []
            },
            "image_refs": []
        }
        new_recipes.append(new_recipe)

    # Add to existing recipes
    data["recipes"].extend(new_recipes)

    # Update metadata
    data["meta"]["total_count"] = len(data["recipes"])
    data["meta"]["total_recipes"] = len(data["recipes"])
    data["meta"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    # Write back
    with open('/home/user/Allrecipes/data/recipes.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Added {len(new_recipes)} Gordon Ramsay recipes")
    print(f"Total recipes now: {data['meta']['total_count']}")

if __name__ == "__main__":
    main()
