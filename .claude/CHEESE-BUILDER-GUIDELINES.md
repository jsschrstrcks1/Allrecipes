# Cheese Recipe Builder Guidelines

> Documentation for the interactive Cheese Recipe Builder wizard.

## Overview

The Cheese Recipe Builder is an interactive wizard that guides users through creating custom cheese recipes based on:

- **Available milk type** - Cow, goat, sheep, or exotic milks
- **Desired cheese style** - Fresh, soft, semi-soft, semi-hard, hard, bloomy, washed, blue
- **Flavor profile** - Herbed, spicy, smoky, garlicky, etc.
- **Adulterant selections** - Herbs, spices, peppers, and other additions

The builder integrates with the **Milk Substitution Tool** and **Adulterant Companion** to provide accurate ingredient adjustments and quantity recommendations.

---

## Files

| File | Purpose |
|------|---------|
| `cheese-builder.js` | Core JavaScript module with wizard logic |
| `cheese-builder.html` | Wizard page with UI |
| `data/cheese-templates.json` | Cheese style definitions, flavor profiles, base recipes |
| `styles.css` | Wizard UI styles (appended to main stylesheet) |

---

## Wizard Flow

### Step 1: Welcome

Introduction to the builder with overview of the process.

### Step 2: Milk Selection

- **Type**: Cow, goat, or sheep (expandable to exotic milks)
- **Quantity**: Amount available (gallons or liters)
- **Processing**: Raw, pasteurized, or ultra-pasteurized

The milk type selection affects:
- Recipe recommendations (styles best suited for each milk)
- Ingredient adjustments (rennet, calcium chloride)
- Yield estimates
- Adulterant quantity adjustments

### Step 3: Style Selection

Choose from cheese styles:

| Style | Difficulty | Aging | Examples |
|-------|------------|-------|----------|
| Fresh | Beginner | None | Ricotta, paneer, queso fresco |
| Soft | Intermediate | 1-4 weeks | Brie, chevre, boursin |
| Semi-Soft | Intermediate | 2-8 weeks | Mozzarella, halloumi, feta |
| Semi-Hard | Intermediate | 2-12 months | Cheddar, gouda, jack |
| Hard | Advanced | 6-24+ months | Parmesan, pecorino |
| Bloomy | Advanced | 2-6 weeks | Brie, camembert |
| Washed | Advanced | 4-12 weeks | Taleggio, epoisses |
| Blue | Advanced | 2-6 months | Roquefort, stilton |

Styles are marked as "recommended" based on the selected milk type.

### Step 4: Flavor Profile

Choose a flavor direction:

- **Mild & Creamy** - Subtle, approachable
- **Herbed & Garden Fresh** - Mediterranean herbs
- **Garlic & Allium Forward** - Bold garlic/onion
- **Spicy & Hot** - Pepper heat
- **Smoky & BBQ** - Smoke and char notes
- **Warm Spices** - Cumin, caraway, coriander
- **Indian Spiced** - Cumin, turmeric, garam masala
- **Mediterranean** - Sun-dried tomato, olives, za'atar
- **Sweet & Fruity** - Honey, dried fruits
- **Nutty & Earthy** - Nuts, seeds, truffle
- **Alcohol Washed** - Beer, wine, spirits
- **Plain / Classic** - No additions

The flavor profile pre-selects compatible adulterants for the next step.

### Step 5: Adulterant Selection

- Shows adulterants compatible with the selected cheese style
- Grouped by category (peppers, herbs, spices, etc.)
- Pre-populated based on flavor profile
- Users can add/remove selections
- Intensity indicators help gauge strength

### Step 6: Review

Summary of all selections:
- Milk type and quantity
- Cheese style
- Flavor profile
- Selected adulterants
- Matched recipes from database
- Estimated yield

Users can select a specific matched recipe or proceed with the default template.

### Step 7: Recipe

Generated recipe with:
- Custom title based on selections
- Adjusted ingredients for milk type and quantity
- Injected adulterant steps at appropriate stages
- Warnings for style/adulterant conflicts
- Tips for the specific milk and style
- Print and save options

---

## Data Structures

### Cheese Templates (`data/cheese-templates.json`)

```json
{
  "meta": { "version": "1.0.0" },
  "cheese_styles": {
    "fresh": {
      "id": "fresh",
      "name": "Fresh Cheese",
      "description": "...",
      "examples": ["ricotta", "paneer"],
      "difficulty": "beginner",
      "time_to_eat": "immediate",
      "aging_required": false,
      "equipment": ["pot", "thermometer"],
      "best_milk_types": ["cow", "goat", "sheep"],
      "adulterant_timing": ["CURD_MILL", "FINISH_SERVING"],
      "suggested_adulterants": ["garlic-powder", "dill-dried"]
    }
  },
  "flavor_profiles": {
    "spicy": {
      "id": "spicy",
      "name": "Spicy & Hot",
      "compatible_styles": ["semi-soft", "semi-hard", "hard"],
      "suggested_adulterants": ["cayenne-pepper", "jalapeno-powder"],
      "intensity_max": "E6"
    }
  },
  "base_recipes": {
    "basic-ricotta": {
      "id": "basic-ricotta",
      "name": "Basic Ricotta",
      "style": "fresh",
      "ingredients": [...],
      "steps": [...],
      "adulterant_injection_point": 5
    }
  }
}
```

---

## API Reference

### Data Loading

```javascript
// Load all required data files
await CheeseBuilder.loadData();
```

### State Management

```javascript
// Get current wizard state
const state = CheeseBuilder.getState();

// Reset wizard to initial state
CheeseBuilder.resetWizard();
```

### Navigation

```javascript
// Get current step name
CheeseBuilder.getCurrentStep(); // 'milk', 'style', etc.

// Navigate
CheeseBuilder.nextStep();
CheeseBuilder.prevStep();
CheeseBuilder.goToStep('adulterants');
```

### Milk Selection

```javascript
// Get available milk types
const milks = CheeseBuilder.getMilkTypes();

// Set milk selection
CheeseBuilder.setMilk('goat', 2, 'gallon', 'pasteurized');

// Get info for a milk type
const info = CheeseBuilder.getMilkInfo('sheep');
```

### Style Selection

```javascript
// Get all styles
const styles = CheeseBuilder.getCheeseStyles();

// Get styles recommended for a milk type
const recommended = CheeseBuilder.getStylesForMilk('goat');

// Set style
CheeseBuilder.setStyle('semi-soft');
```

### Flavor Profiles

```javascript
// Get profiles compatible with current style
const flavors = CheeseBuilder.getFlavorProfilesForStyle('semi-hard');

// Set flavor profile (auto-populates adulterants)
CheeseBuilder.setFlavorProfile('spicy');
```

### Adulterants

```javascript
// Get compatible adulterants for style
const adulterants = CheeseBuilder.getCompatibleAdulterants('semi-hard');

// Add/remove adulterant
CheeseBuilder.addAdulterant('cayenne-pepper');
CheeseBuilder.removeAdulterant('cayenne-pepper');

// Get current selections
const selected = CheeseBuilder.getSelectedAdulterants();

// Clear all
CheeseBuilder.clearAdulterants();
```

### Recipe Generation

```javascript
// Find matching recipes from database
const matches = CheeseBuilder.findMatchingRecipes();

// Select a specific recipe
CheeseBuilder.selectRecipe('basic-cheddar');

// Generate final recipe with all adjustments
const recipe = CheeseBuilder.generateRecipe();
```

### Rendering

```javascript
// Render wizard to container
CheeseBuilder.renderWizard('container-id');

// Attach event listeners (required after render)
CheeseBuilder.attachEventListeners('container-id');
```

---

## Events

### `cheeseRecipeGenerated`

Dispatched when user clicks "Save to Collection":

```javascript
document.addEventListener('cheeseRecipeGenerated', (e) => {
  const { recipe, wizardState } = e.detail;

  // recipe contains the generated recipe object
  // wizardState contains all user selections
});
```

---

## Integration Points

### Milk Substitution Tool

The builder uses `data/milk-substitution.json` for:
- Milk type properties (fat%, protein%, yield)
- Rennet adjustment factors
- Calcium chloride guidelines
- Curd handling notes

### Adulterant Companion

The builder uses `data/adulterants.json` for:
- Compatible adulterants by cheese style
- Quantity recommendations
- Milk-type adjustments
- Warning messages
- Addition stages

---

## Adding New Base Recipes

1. Edit `data/cheese-templates.json`
2. Add entry to `base_recipes`:

```json
{
  "my-new-cheese": {
    "id": "my-new-cheese",
    "name": "My New Cheese",
    "style": "semi-soft",
    "difficulty": "beginner",
    "time_total": "2 hours",
    "yield": "1 lb",
    "milk_quantity": {"amount": 1, "unit": "gallon"},
    "ingredients": [
      {"item": "whole milk", "quantity": "1", "unit": "gallon"}
    ],
    "steps": [
      {"step": 1, "text": "Heat milk..."}
    ],
    "adulterant_injection_point": 5,
    "variations": ["Add herbs", "Smoke before serving"]
  }
}
```

The `adulterant_injection_point` indicates which step number to insert adulterant additions after.

---

## Adding New Cheese Styles

1. Edit `data/cheese-templates.json`
2. Add entry to `cheese_styles`:

```json
{
  "my-style": {
    "id": "my-style",
    "name": "My Style",
    "description": "Description here",
    "examples": ["example1", "example2"],
    "difficulty": "intermediate",
    "time_to_eat": "2-4 weeks",
    "aging_required": true,
    "equipment": ["pot", "molds", "press"],
    "milk_volume_typical_gal": 2,
    "yield_estimate": "1 lb per gallon",
    "flavor_descriptors": ["buttery", "mild"],
    "best_milk_types": ["cow", "goat"],
    "adulterant_timing": ["CURD_MILL", "RIND_RUB"],
    "suggested_adulterants": ["herb-id-1", "spice-id-2"]
  }
}
```

---

## Adding New Flavor Profiles

1. Edit `data/cheese-templates.json`
2. Add entry to `flavor_profiles`:

```json
{
  "my-flavor": {
    "id": "my-flavor",
    "name": "My Flavor Profile",
    "description": "Description here",
    "compatible_styles": ["fresh", "soft", "semi-soft"],
    "suggested_adulterants": ["adulterant-id-1", "adulterant-id-2"],
    "intensity_max": "M3"
  }
}
```

---

## Maintenance Checklist

- [ ] Verify `cheese-templates.json` is valid JSON
- [ ] Test wizard navigation (all steps)
- [ ] Test milk type selection and adjustments
- [ ] Test style recommendations for each milk type
- [ ] Test flavor profile population
- [ ] Test adulterant selection UI
- [ ] Verify recipe generation produces valid output
- [ ] Check print layout renders correctly
- [ ] Test responsive design on mobile
- [ ] Verify integration with existing cheese recipes

---

## Troubleshooting

### Wizard not loading

- Check browser console for errors
- Verify all data files exist and are valid JSON
- Ensure `cheese-builder.js` is loaded after dependencies

### No recipes matching

- Verify cheese recipes have `category: "cheese"`
- Check that style keywords match recipe titles/tags
- Try selecting a different style

### Adulterant adjustments wrong

- Verify adulterant has `milk_adjustments` for the selected milk type
- Check that `base_quantity` is defined
- Review the adulterant's `compatible_styles`

### Print layout issues

- Check that `@media print` styles are applied
- Verify wizard navigation is hidden in print

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-22 | Initial release with wizard, 10 base recipes, 8 styles, 11 flavor profiles |
