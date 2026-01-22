# Adulterant Companion Guidelines

> Guidelines for the Herb & Spice Companion tool for cheese-making recipes.

## Overview

The Adulterant Companion provides interactive guidance for adding herbs, spices, peppers, and other adulterants to cheese recipes. It integrates with the Milk Substitution Tool to automatically adjust quantities based on milk type.

---

## Quick Start

### Loading the Module

```html
<!-- Include after milk-substitution.js -->
<script src="milk-substitution.js"></script>
<script src="adulterant-companion.js"></script>
```

### Initialize and Render

```javascript
// Load data
await AdulterantCompanion.loadData();

// Render panel for a recipe
AdulterantCompanion.renderPanel(recipe, 'adulterant-container');
```

---

## Data Structure

### Adulterant Entry Schema

```json
{
  "id": "ghost-pepper-powder",
  "name": "Ghost Pepper (Bhut Jolokia) Powder",
  "category": "pepper",
  "subcategory": "superhot",
  "scoville_min": 855000,
  "scoville_max": 1041427,
  "forms": ["powder"],
  "flavor_profile": ["SPICY", "FRUITY", "SMOKY"],
  "intensity": "E6",
  "compatible_styles": ["hard", "semi-hard"],
  "incompatible_styles": ["fresh", "soft", "bloomy", "blue"],
  "best_stages": ["RIND_RUB", "AGING_SURFACE"],
  "allowed_stages": ["COLD_INFUSE", "CURD_MILL", "RIND_RUB", "AGING_SURFACE"],
  "base_quantity": {"amount": 0.125, "unit": "tsp", "per": "gallon"},
  "milk_adjustments": {"cow": 1.0, "goat": 0.8, "sheep": 1.3, "buffalo": 1.2},
  "max_safe_quantity": {"amount": 0.5, "unit": "tsp", "per": "gallon"},
  "warnings": {
    "exceeded_message": "Ghost pepper >1/2 tsp/gallon creates dangerously intense heat",
    "style_warnings": {
      "fresh": "Extreme heat won't mellow - fresh cheese will be inedible",
      "bloomy": "May inhibit Penicillium development"
    },
    "general": "Wear gloves when handling. Wash hands thoroughly."
  },
  "injection_templates": {
    "COLD_INFUSE": "Carefully steep {quantity} {name} in cold milk for 1-2 hours.",
    "CURD_MILL": "Wearing gloves, carefully dust {quantity} {name} over curds.",
    "RIND_RUB": "Mix {quantity} {name} with salt. Apply thin layer using gloves."
  },
  "interactions": [
    {"with": "honey", "effect": "complementary", "note": "Sweetness balances heat"}
  ],
  "notes": "One of the world's hottest peppers. Use extreme caution."
}
```

---

## Categories

| Category | ID | Description |
|----------|-----|-------------|
| Hot Peppers | `pepper` | Mild to superhot pepper powders and flakes |
| Dried Herbs | `herb` | Mediterranean and culinary herbs |
| Spices | `spice` | Seeds, bark, and root spices |
| Indian Spices | `indian` | Traditional Indian/South Asian spices |
| Alliums | `allium` | Garlic, onion, and related |
| Alcohol | `alcohol` | Wine, beer, spirits for washing |
| Dried Fruits | `fruit` | Cranberries, apricots, etc. |
| Nuts & Seeds | `nut` | Walnuts, sesame, etc. |
| Other | `other` | Truffle, honey, ash, smoke, etc. |

---

## Intensity Scale

| Code | Level | Description | Typical Dose |
|------|-------|-------------|--------------|
| M1 | Very Mild | Background note | 1/8-1/4 tsp/gal |
| M2 | Mild | Noticeable but subtle | 1/4-1/2 tsp/gal |
| M3 | Medium | Distinct flavor | 1/2-1 tsp/gal |
| H4 | Hot | Noticeable heat | 1/4-1/2 tsp/gal |
| H5 | Very Hot | Strong heat | 1/8-1/4 tsp/gal |
| E6 | Extreme | Use with caution | 1/16-1/8 tsp/gal |

---

## Addition Stages

| Stage | When | Best For |
|-------|------|----------|
| `COLD_INFUSE` | Before heating milk | Saffron, mild spices, cold-infused peppers |
| `MILK_PREHEAT` | During initial heating | Turmeric (for color), gentle spices |
| `PRE_RENNET` | Just before rennet | Very mild, non-acidic only |
| `CURD_CUT` | After cutting curds | Finely ground spices only |
| `CURD_MILL` | While milling curds | Most herbs, spices, peppers |
| `MOLD_LAYER` | Filling molds | Ash, fruits, visible herbs |
| `POST_PRESS` | After pressing | Crusts, coatings, nuts |
| `BRINE_ADDITION` | In brine solution | Wine, beer, liquid smoke |
| `RIND_RUB` | Aging wash/rub | Alcohol washes, spice rubs |
| `AGING_SURFACE` | During aging | Superhot peppers, strong spices |
| `FINISH_SERVING` | Before serving | Fresh garnishes, honey, truffle oil |

---

## Cheese Style Compatibility

### Fresh Cheese
- **Good:** Mild herbs (dill, chives), garlic, mild peppers, dried fruits
- **Avoid:** Strong spices, superhot peppers, alcohol, smoke

### Soft/Semi-Soft Cheese
- **Good:** Most herbs, medium peppers, alliums, mild spices
- **Avoid:** Extreme peppers, long-aged additions

### Hard/Semi-Hard Cheese
- **Good:** Bold spices, hot peppers, caraway, cumin, alcohol washes
- **Avoid:** Delicate herbs that won't survive aging

### Bloomy Rind
- **Good:** Minimal additions, ash for visual
- **Avoid:** Most adulterants (interfere with Penicillium)

### Blue Cheese
- **Good:** Minimal (blue mold provides flavor)
- **Avoid:** Strong spices that compete with blue

### Washed Rind
- **Good:** Alcohol washes (beer, wine, calvados)
- **Avoid:** Delicate flavors overwhelmed by funk

---

## Milk Type Adjustments

Higher-yield milks need more adulterant for equivalent flavor:

| Milk Type | Adjustment Factor | Notes |
|-----------|-------------------|-------|
| Cow | 1.0x | Baseline |
| Goat | 0.85-1.0x | Tangy flavor may compete |
| Sheep | 1.3-1.4x | Higher yield = more adulterant needed |
| Buffalo | 1.2-1.3x | High fat masks some flavors |

---

## Warning System

### Warning Types

| Type | Level | Meaning |
|------|-------|---------|
| `QUANTITY_EXCEEDED` | warning | Above recommended maximum |
| `INCOMPATIBLE_STYLE` | caution/danger | Not recommended for cheese style |
| `INTERACTION` | info/warning | Reaction with another selection |
| `GENERAL` | info | Safety or handling note |

### Example Warnings

```javascript
// Quantity warning
{
  type: 'QUANTITY_EXCEEDED',
  level: 'warning',
  message: 'Garlic powder >1.5 tsp/gallon may develop sulfur off-flavors'
}

// Style warning
{
  type: 'INCOMPATIBLE_STYLE',
  level: 'danger',
  message: 'PROHIBITED: Fresh cilantro loses flavor and turns bitter'
}

// Interaction info
{
  type: 'INTERACTION',
  level: 'info',
  message: 'Smoked paprika + garlic: Classic combination'
}
```

---

## Prohibited Adulterants

These should **never** be used:

| Adulterant | Reason | Alternative |
|------------|--------|-------------|
| Fresh garlic | Botulism risk, moisture | Garlic powder |
| Fresh onion | Moisture causes spoilage | Onion powder |
| Fresh herbs | Moisture, unpredictable aging | Dried equivalents |
| Fresh cilantro | Turns bitter | Ground coriander |
| Oil-based pastes | Bacterial risk | Dry spices |
| Hot sauce | Weak curds, pH issues | Pepper powders |
| Asafoetida | Overwhelming sulfur | None |

---

## API Reference

### Data Loading

```javascript
// Load adulterant database
await AdulterantCompanion.loadData();

// Get all adulterants
const all = AdulterantCompanion.getAllAdulterants();

// Get by ID
const ghost = AdulterantCompanion.getAdulterant('ghost-pepper-powder');

// Get by category
const peppers = AdulterantCompanion.getByCategory('pepper');
```

### Compatibility

```javascript
// Detect cheese style from recipe
const style = AdulterantCompanion.detectCheeseStyle(recipe);

// Get compatible adulterants for a style
const compatible = AdulterantCompanion.getCompatibleAdulterants('hard');

// Check compatibility
const ok = AdulterantCompanion.isCompatible('cayenne-pepper', 'semi-soft');
```

### Calculations

```javascript
// Get milk-adjusted quantity
const adjusted = AdulterantCompanion.calculateAdjustedQuantity(
  'garlic-powder',  // adulterant ID
  'sheep',          // milk type
  2                 // gallons
);
// Returns: {amount: 0.65, unit: 'tsp', per: '2 gallons', milkType: 'sheep'}

// Format for display
const display = AdulterantCompanion.formatQuantity(0.5, 'tsp');
// Returns: "1/2 tsp"
```

### Selection Management

```javascript
// Add an adulterant
AdulterantCompanion.addAdulterant('oregano-dried', 'CURD_MILL', 0.5, 'tsp');

// Update quantity
AdulterantCompanion.updateQuantity(0, 0.75);

// Remove
AdulterantCompanion.removeAdulterant(0);

// Get all selections
const selections = AdulterantCompanion.getSelections();

// Clear all
AdulterantCompanion.clearSelections();
```

### Warnings

```javascript
// Get warnings for a selection
const warnings = AdulterantCompanion.getWarnings(
  'ghost-pepper-powder',
  0.75,    // quantity
  'tsp',   // unit
  'fresh'  // cheese style
);

// Get all warnings for current selections
const allWarnings = AdulterantCompanion.getAllWarnings('semi-hard');
```

### Recipe Integration

```javascript
// Generate injection steps
const steps = AdulterantCompanion.generateInjectionSteps(recipe);
// Returns array of {stage, instruction, adulterantName, quantity}

// Get stage display name
AdulterantCompanion.getStageDisplayName('CURD_MILL');
// Returns: "During Curd Milling"
```

---

## Event Handling

### Listen for Changes

```javascript
document.addEventListener('adulterantSelectionChanged', (e) => {
  const {
    selections,       // Current selections array
    injectionSteps,   // Ready-to-display instructions
    warnings,         // All applicable warnings
    cheeseStyle,      // Detected cheese style
    milkType          // Current milk type
  } = e.detail;

  // Update your UI
  updateInstructions(injectionSteps);
  showWarnings(warnings);
});
```

### Milk Substitution Integration

The module automatically listens for `milkSubstitutionChanged` events and adjusts quantities when the user changes milk types:

```javascript
// Automatic - no code needed
// When milk changes, adulterant quantities recalculate
```

---

## UI Rendering

### Basic Panel

```javascript
// Render full interactive panel
AdulterantCompanion.renderPanel(recipe, 'adulterant-container');
```

### HTML Container

```html
<div id="adulterant-container"></div>
```

The panel includes:
- Category accordion with compatible adulterants
- Selection list with quantity/stage controls
- Warnings display
- Injection step preview

---

## Best Practices

1. **Start conservative** - Use base quantities, increase gradually
2. **Consider aging** - Flavors concentrate during aging
3. **Match intensity to style** - Fresh cheese = mild; aged = bold
4. **Check interactions** - Some combinations are classic, others clash
5. **Adjust for milk** - Sheep needs ~40% more adulterant than cow
6. **Heed warnings** - Especially for superhot peppers and style conflicts

---

## Integration with FamilyRecipeHub

Copy these files to the aggregator:

```
Allrecipes/
├── adulterant-companion.js
├── data/adulterants.json
└── styles.css (adulterant section)
```

Initialize alongside MilkSubstitution:

```javascript
async function init() {
  await MilkSubstitution.loadData();
  await AdulterantCompanion.loadData();

  // Render for cheese recipes
  if (MilkSubstitution.isCheeseRecipe(recipe)) {
    MilkSubstitution.renderMilkSwitcher(recipe, 'milk-container');
    AdulterantCompanion.renderPanel(recipe, 'adulterant-container');
  }
}
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-22 | Initial release with 156 adulterants |
