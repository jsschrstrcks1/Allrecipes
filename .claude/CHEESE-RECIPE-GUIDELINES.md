# Cheese Recipe Guidelines

> Guidelines for adding cheesemaking recipes to ensure automatic detection by the Milk Substitution Tool.

## Overview

The Milk Substitution Tool automatically detects cheesemaking recipes and enables milk type switching (cow, goat, sheep) with automatic ingredient adjustments. For the tool to detect your recipe, follow these guidelines.

---

## Detection Criteria

The tool uses multiple methods to identify cheesemaking recipes. **At least one** of these must be satisfied:

### 1. Explicit Marker (Recommended)
Add the `milk_substitutions` field to your recipe:

```json
{
  "milk_substitutions": {
    "enabled": true,
    "original_milk": "cow",
    "supported_types": ["cow", "goat", "sheep"]
  }
}
```

**Fields:**
- `enabled` (required): Set to `true` to enable the tool
- `original_milk` (optional): The milk type the recipe was designed for. Options: `cow`, `goat`, `sheep`, `buffalo`, `camel`, `yak`, `mare`, `donkey`, `reindeer`, `llama`, `alpaca`
- `supported_types` (optional): Array of milk types that work with this recipe

### 2. Category
Set `category` to `"cheese"`:

```json
{
  "category": "cheese"
}
```

### 3. Cheesemaking Tags
Include at least one of these tags:

```json
{
  "tags": ["cheese", "cheesemaking", "cheese-making", "homemade-cheese",
           "artisan-cheese", "fromage", "dairy", "fermented-dairy",
           "curds", "whey", "aged-cheese", "fresh-cheese"]
}
```

### 4. Cheese Keyword in Title
Titles containing cheese-related keywords are detected:

**Detected keywords:**
- Generic: cheese, fromage, queso, formaggio, käse, ost
- Specific varieties: cheddar, mozzarella, parmesan, brie, camembert, gouda, feta, ricotta, mascarpone, gruyère, manchego, pecorino, roquefort, gorgonzola, stilton, halloumi, paneer, quark, labneh, burrata, stracciatella
- Regional: cottage cheese, cream cheese, farmer cheese, pot cheese, chhurpi, byaslag, juustoleipa

**Excluded patterns** (recipes that USE cheese, not make it):
- grilled cheese, cheese sandwich, mac and cheese, cheese dip, cheese ball, cheesecake, cheese pizza, cheese quesadilla, cheese omelet

### 5. Ingredient Detection
Recipes with milk + rennet or milk + starter culture are detected:

**Milk keywords:**
- milk, whole milk, raw milk, pasteurized milk, fresh milk, farm milk, unhomogenized milk

**Rennet keywords:**
- rennet, vegetable rennet, animal rennet, liquid rennet, rennet tablet, microbial rennet, thistle rennet

**Culture keywords:**
- mesophilic, thermophilic, starter culture, cheese culture, buttermilk culture, kefir grains, yogurt culture, mother culture

---

## Milk Type Detection

The tool automatically detects exotic milk types from ingredient names. Include the milk type in the ingredient item:

| Milk Type | Keywords Detected |
|-----------|-------------------|
| Sheep | sheep, sheep's, ewe, ovine, pecora, brebis, oveja, schaf |
| Goat | goat, goat's, caprine, chèvre, cabra, ziege, capra |
| Buffalo | buffalo, water buffalo, bufala, búfala |
| Camel | camel, camel's, dromedary, chameau, camello |
| Yak | yak, yak's, dri |
| Reindeer | reindeer, caribou, renne, reno |
| Llama | llama, llama's |
| Alpaca | alpaca, alpaca's |
| Mare | mare, horse, mare's, equine, jument |
| Donkey | donkey, donkey's, âne, burro |

**Examples:**
```json
{"item": "sheep's milk", "quantity": "2", "unit": "gallons"}
{"item": "fresh goat milk", "quantity": "1", "unit": "gallon"}
{"item": "water buffalo milk", "quantity": "3", "unit": "liters"}
```

If no specific milk type is mentioned (just "milk" or "whole milk"), the tool defaults to **cow milk**.

---

## Recipe Schema Example

Complete example for a cheese recipe:

```json
{
  "id": "homemade-mozzarella",
  "collection": "all",
  "title": "Fresh Homemade Mozzarella",
  "category": "cheese",
  "tags": ["cheese", "cheesemaking", "fresh-cheese", "italian"],
  "description": "Soft, stretchy mozzarella made from scratch",
  "servings_yield": "1 pound",
  "prep_time": "15 minutes",
  "cook_time": "30 minutes",
  "total_time": "45 minutes",
  "ingredients": [
    {"item": "whole milk", "quantity": "1", "unit": "gallon", "prep_note": "not ultra-pasteurized"},
    {"item": "citric acid", "quantity": "1 1/2", "unit": "tsp", "prep_note": "dissolved in 1/4 cup water"},
    {"item": "liquid rennet", "quantity": "1/4", "unit": "tsp", "prep_note": "diluted in 1/4 cup water"},
    {"item": "salt", "quantity": "1", "unit": "tsp"}
  ],
  "instructions": [
    {"step": 1, "text": "Heat milk to 55°F (13°C) and add citric acid solution while stirring."},
    {"step": 2, "text": "Heat to 90°F (32°C), remove from heat, and add rennet. Stir gently for 30 seconds."},
    {"step": 3, "text": "Let sit for 5 minutes until curds form a clean break."},
    {"step": 4, "text": "Cut curds into 1-inch cubes and heat to 105°F (40°C) while stirring gently."},
    {"step": 5, "text": "Drain whey and microwave curds in 30-second intervals, kneading between each."},
    {"step": 6, "text": "When stretchy and smooth, add salt, form into ball, and place in ice water."}
  ],
  "temperature": "90-105°F (32-40°C)",
  "notes": ["Use raw or pasteurized milk, never ultra-pasteurized", "Work quickly once curds are ready"],
  "milk_substitutions": {
    "enabled": true,
    "original_milk": "cow",
    "supported_types": ["cow", "goat", "sheep"]
  },
  "confidence": {
    "overall": "high",
    "flags": []
  }
}
```

---

## Ancient & Historical Recipes

For ancient or historical cheese recipes, ensure detection by:

1. Adding `"cheesemaking"` or `"cheese"` to tags
2. Setting `category` to `"cheese"`
3. Including the `milk_substitutions` field

Example for an ancient recipe:
```json
{
  "id": "oxygala-ancient-roman-cheese",
  "title": "Oxygala (Ancient Roman Fresh Cheese)",
  "category": "cheese",
  "tags": ["ancient", "roman", "cheesemaking", "historical", "fresh-cheese"],
  "milk_substitutions": {
    "enabled": true,
    "original_milk": "sheep",
    "supported_types": ["cow", "goat", "sheep"]
  }
}
```

---

## Testing Detection

After adding a cheese recipe, verify detection:

1. Run the test script:
   ```bash
   node scripts/test-milk-substitution.js
   ```

2. Check the browser console when viewing the recipe - you should see "Milk substitution data loaded"

3. The Milk Substitution Calculator panel should appear on the recipe page

---

## Troubleshooting

**Tool not appearing on recipe page:**
- Verify the recipe has `category: "cheese"` or relevant tags
- Check that ingredients include milk + rennet/culture
- Add explicit `milk_substitutions.enabled: true`

**Wrong milk type detected:**
- Add specific milk type to ingredient name (e.g., "goat milk" not just "milk")
- Set `original_milk` in `milk_substitutions`

**Recipe incorrectly detected as cheese:**
- Ensure title doesn't contain cheese variety names
- Check that recipe doesn't have `milk_substitutions.enabled: true`
- Review tags for accidental cheesemaking tags

---

## Summary Checklist

For guaranteed detection, ensure your cheese recipe has:

- [ ] `category: "cheese"` OR
- [ ] `tags` includes "cheesemaking" or "cheese" OR
- [ ] `milk_substitutions.enabled: true` (recommended)
- [ ] Milk ingredient with recognizable name
- [ ] Rennet or culture ingredient (if applicable)
- [ ] Original milk type specified (if not cow)
