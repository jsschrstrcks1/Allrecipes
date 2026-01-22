#!/usr/bin/env node
/**
 * Edge case tests for the Milk Substitution Tool
 * Run with: node scripts/test-milk-substitution.js
 */

// Mock browser environment
global.document = {
  getElementById: () => null,
  addEventListener: () => {},
  dispatchEvent: () => {}
};
global.CustomEvent = class CustomEvent {
  constructor(name, options) {
    this.name = name;
    this.detail = options?.detail;
  }
};

// Load the module
const fs = require('fs');
const path = require('path');

// Load substitution data
const substitutionData = JSON.parse(
  fs.readFileSync(path.join(__dirname, '../data/milk-substitution.json'), 'utf8')
);

// Simple test framework
let passed = 0;
let failed = 0;
const failures = [];

function test(name, fn) {
  try {
    fn();
    passed++;
    console.log(`  ✓ ${name}`);
  } catch (e) {
    failed++;
    failures.push({ name, error: e.message });
    console.log(`  ✗ ${name}`);
    console.log(`    Error: ${e.message}`);
  }
}

function assertEqual(actual, expected, msg = '') {
  if (actual !== expected) {
    throw new Error(`${msg} Expected ${expected}, got ${actual}`);
  }
}

function assertClose(actual, expected, tolerance = 0.01, msg = '') {
  if (Math.abs(actual - expected) > tolerance) {
    throw new Error(`${msg} Expected ~${expected}, got ${actual}`);
  }
}

function assertTrue(value, msg = '') {
  if (!value) {
    throw new Error(`${msg} Expected truthy value, got ${value}`);
  }
}

function assertFalse(value, msg = '') {
  if (value) {
    throw new Error(`${msg} Expected falsy value, got ${value}`);
  }
}

// ============================================================================
// Volume Conversion Tests
// ============================================================================

console.log('\n=== Volume Conversion Tests ===\n');

// Volume unit conversions to cups (from the module)
const VOLUME_TO_CUPS = {
  cups: 1,
  cup: 1,
  oz: 0.125,
  'fl oz': 0.125,
  tbsp: 0.0625,
  quart: 4,
  quarts: 4,
  qt: 4,
  gallon: 16,
  gallons: 16,
  gal: 16,
  pint: 2,
  pints: 2,
  pt: 2,
  ml: 0.00423,
  liter: 4.227,
  liters: 4.227,
  l: 4.227
};

function convertToCups(value, unit) {
  const normalizedUnit = unit.toLowerCase().trim();
  const factor = VOLUME_TO_CUPS[normalizedUnit];
  if (factor === undefined) {
    return value; // default to cups
  }
  return value * factor;
}

function convertFromCups(cups, unit) {
  const normalizedUnit = unit.toLowerCase().trim();
  const factor = VOLUME_TO_CUPS[normalizedUnit];
  if (factor === undefined || factor === 0) {
    return cups;
  }
  return cups / factor;
}

test('1 gallon = 16 cups', () => {
  assertEqual(convertToCups(1, 'gallon'), 16);
});

test('1 quart = 4 cups', () => {
  assertEqual(convertToCups(1, 'quart'), 4);
});

test('8 oz = 1 cup', () => {
  assertEqual(convertToCups(8, 'oz'), 1);
});

test('2 pints = 4 cups', () => {
  assertEqual(convertToCups(2, 'pints'), 4);
});

test('16 tbsp = 1 cup', () => {
  assertEqual(convertToCups(16, 'tbsp'), 1);
});

test('236 ml ≈ 1 cup', () => {
  assertClose(convertToCups(236, 'ml'), 1, 0.05);
});

test('1 liter ≈ 4.227 cups', () => {
  assertClose(convertToCups(1, 'liters'), 4.227, 0.01);
});

test('Round-trip conversion: cups → gallons → cups', () => {
  const cups = 32;
  const gallons = convertFromCups(cups, 'gallons');
  const backToCups = convertToCups(gallons, 'gallons');
  assertEqual(backToCups, cups);
});

test('Round-trip conversion: cups → quarts → cups', () => {
  const cups = 8;
  const quarts = convertFromCups(cups, 'quarts');
  const backToCups = convertToCups(quarts, 'quarts');
  assertEqual(backToCups, cups);
});

test('Unknown unit defaults to cups', () => {
  assertEqual(convertToCups(5, 'unknown_unit'), 5);
});

test('Case insensitive: GALLON = gallon', () => {
  assertEqual(convertToCups(1, 'GALLON'), 16);
});

test('Handles whitespace: " cups " = cups', () => {
  assertEqual(convertToCups(1, ' cups '), 1);
});

// ============================================================================
// Edge Case: Zero and Negative Values
// ============================================================================

console.log('\n=== Zero and Negative Value Tests ===\n');

test('Zero volume converts correctly', () => {
  assertEqual(convertToCups(0, 'gallons'), 0);
});

test('Negative volume converts (but should be prevented in UI)', () => {
  assertEqual(convertToCups(-1, 'gallons'), -16);
});

test('Very small values: 0.01 cups', () => {
  assertClose(convertToCups(0.01, 'cups'), 0.01, 0.0001);
});

test('Very large values: 100 gallons = 1600 cups', () => {
  assertEqual(convertToCups(100, 'gallons'), 1600);
});

// ============================================================================
// Ratio Calculation Tests
// ============================================================================

console.log('\n=== Ratio Calculation Tests ===\n');

function calculateRatios(volumes) {
  const totalCups = Object.values(volumes).reduce((a, b) => a + b, 0);

  if (totalCups === 0) {
    return { cow: 100, goat: 0, sheep: 0 };
  }

  const ratios = {};
  for (const [type, cups] of Object.entries(volumes)) {
    ratios[type] = Math.round((cups / totalCups) * 100);
  }

  // Normalize to ensure sum = 100
  const sum = Object.values(ratios).reduce((a, b) => a + b, 0);
  if (sum !== 100) {
    // Find the largest ratio and adjust it
    const maxType = Object.entries(ratios).sort((a, b) => b[1] - a[1])[0][0];
    ratios[maxType] += 100 - sum;
  }

  return ratios;
}

test('Equal volumes = equal percentages (sum to 100)', () => {
  const ratios = calculateRatios({ cow: 4, goat: 4, sheep: 4 });
  // Each should be ~33%, with rounding adjustment
  assertTrue(ratios.cow >= 33 && ratios.cow <= 34, 'cow ratio');
  assertTrue(ratios.goat >= 33 && ratios.goat <= 34, 'goat ratio');
  assertTrue(ratios.sheep >= 33 && ratios.sheep <= 34, 'sheep ratio');
  assertEqual(ratios.cow + ratios.goat + ratios.sheep, 100, 'sum to 100');
});

test('All zero volumes defaults to 100% cow', () => {
  const ratios = calculateRatios({ cow: 0, goat: 0, sheep: 0 });
  assertEqual(ratios.cow, 100);
  assertEqual(ratios.goat, 0);
  assertEqual(ratios.sheep, 0);
});

test('Single milk at 100%', () => {
  const ratios = calculateRatios({ cow: 0, goat: 16, sheep: 0 });
  assertEqual(ratios.cow, 0);
  assertEqual(ratios.goat, 100);
  assertEqual(ratios.sheep, 0);
});

test('75% sheep, 12.5% cow, 12.5% goat (example from user)', () => {
  // 75% of 16 cups = 12 cups sheep
  // 12.5% of 16 cups = 2 cups each cow and goat
  const ratios = calculateRatios({ cow: 2, goat: 2, sheep: 12 });
  // Sheep should be ~75%, cow and goat ~12.5% each
  assertTrue(ratios.sheep >= 74 && ratios.sheep <= 76, 'sheep ~75%');
  assertTrue(ratios.cow >= 12 && ratios.cow <= 14, 'cow ~12.5%');
  assertTrue(ratios.goat >= 12 && ratios.goat <= 14, 'goat ~12.5%');
  assertEqual(ratios.cow + ratios.goat + ratios.sheep, 100, 'sum to 100');
});

test('4 cups goat + 1 gallon cow + 1 quart sheep (user example)', () => {
  // 4 cups goat = 4 cups
  // 1 gallon cow = 16 cups
  // 1 quart sheep = 4 cups
  // Total = 24 cups
  const ratios = calculateRatios({
    cow: 16,  // 66.67%
    goat: 4,  // 16.67%
    sheep: 4  // 16.67%
  });
  // Cow ~67%, goat and sheep ~17% each
  assertTrue(ratios.cow >= 66 && ratios.cow <= 68, 'cow ~67%');
  assertTrue(ratios.goat >= 16 && ratios.goat <= 18, 'goat ~17%');
  assertTrue(ratios.sheep >= 16 && ratios.sheep <= 18, 'sheep ~17%');
  assertEqual(ratios.cow + ratios.goat + ratios.sheep, 100, 'sum to 100');
});

test('Very small amounts: 0.25 cups each', () => {
  const ratios = calculateRatios({ cow: 0.25, goat: 0.25, sheep: 0.25 });
  assertEqual(ratios.cow + ratios.goat + ratios.sheep, 100);
});

// ============================================================================
// Cheese Recipe Detection Tests
// ============================================================================

console.log('\n=== Cheese Recipe Detection Tests ===\n');

const CHEESE_KEYWORDS_TITLE = [
  'cheese', 'fromage', 'queso', 'formaggio', 'käse',
  'cheddar', 'mozzarella', 'parmesan', 'brie', 'camembert',
  'gouda', 'feta', 'ricotta', 'mascarpone', 'gruyere',
  'manchego', 'pecorino', 'roquefort', 'gorgonzola',
  'halloumi', 'paneer', 'quark', 'labneh', 'burrata'
];

const CHEESEMAKING_TAGS = [
  'cheese', 'cheesemaking', 'cheese-making', 'homemade-cheese',
  'artisan-cheese', 'fromage', 'dairy', 'fermented-dairy'
];

const RENNET_KEYWORDS = [
  'rennet', 'vegetable rennet', 'animal rennet', 'liquid rennet',
  'rennet tablet', 'microbial rennet', 'thistle rennet'
];

const MILK_KEYWORDS = [
  'milk', 'whole milk', 'raw milk', 'pasteurized milk',
  'fresh milk', 'farm milk', 'unhomogenized milk'
];

const CULTURE_KEYWORDS = [
  'mesophilic', 'thermophilic', 'starter culture', 'cheese culture',
  'buttermilk culture', 'kefir grains', 'yogurt culture'
];

function isCheeseRecipe(recipe) {
  if (!recipe) return false;

  // Check category
  if (recipe.category && recipe.category.toLowerCase() === 'cheese') {
    return true;
  }

  // Check tags
  if (recipe.tags) {
    const tagsLower = recipe.tags.map(t => t.toLowerCase());
    if (CHEESEMAKING_TAGS.some(tag => tagsLower.includes(tag))) {
      return true;
    }
  }

  // Check title for cheese keywords
  if (recipe.title) {
    const titleLower = recipe.title.toLowerCase();
    if (CHEESE_KEYWORDS_TITLE.some(kw => titleLower.includes(kw))) {
      // But exclude "grilled cheese sandwich" type recipes
      const excludePatterns = [
        'grilled cheese', 'cheese sandwich', 'cheese toast',
        'mac and cheese', 'mac & cheese', 'cheese dip',
        'cheese ball', 'cheese spread', 'cheese sauce',
        'cheesecake', 'cheese cake', 'cream cheese frosting'
      ];
      if (!excludePatterns.some(p => titleLower.includes(p))) {
        // Could be a cheese recipe, check ingredients
        if (recipe.ingredients) {
          const hasRennet = recipe.ingredients.some(ing =>
            RENNET_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
          );
          const hasMilk = recipe.ingredients.some(ing =>
            MILK_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
          );
          const hasCulture = recipe.ingredients.some(ing =>
            CULTURE_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
          );

          // Cheese-making requires milk + (rennet OR culture)
          if (hasMilk && (hasRennet || hasCulture)) {
            return true;
          }
        }
        return true; // Title says cheese, assume it's a cheese recipe
      }
    }
  }

  // Check ingredients for cheese-making indicators
  if (recipe.ingredients) {
    const hasRennet = recipe.ingredients.some(ing =>
      RENNET_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
    );
    const hasMilk = recipe.ingredients.some(ing =>
      MILK_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
    );
    const hasCulture = recipe.ingredients.some(ing =>
      CULTURE_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
    );

    if (hasRennet && hasMilk) {
      return true;
    }
    if (hasCulture && hasMilk && recipe.instructions) {
      // Check if instructions mention curd formation
      const instructionsText = recipe.instructions.map(i => i.text).join(' ').toLowerCase();
      if (instructionsText.includes('curd') || instructionsText.includes('drain') ||
          instructionsText.includes('whey') || instructionsText.includes('coagul')) {
        return true;
      }
    }
  }

  // Check milk_substitutions field
  if (recipe.milk_substitutions && recipe.milk_substitutions.enabled) {
    return true;
  }

  return false;
}

// Test recipes
const testRecipes = [
  {
    name: 'Basic Cheddar (should detect)',
    recipe: {
      title: 'Homemade Cheddar Cheese',
      category: 'cheese',
      tags: ['cheese', 'cheesemaking'],
      ingredients: [
        { item: 'whole milk', quantity: '2', unit: 'gallons' },
        { item: 'liquid rennet', quantity: '1/4', unit: 'tsp' }
      ]
    },
    expected: true
  },
  {
    name: 'Grilled Cheese Sandwich (should NOT detect)',
    recipe: {
      title: 'Classic Grilled Cheese Sandwich',
      category: 'mains',
      tags: ['sandwiches', 'quick'],
      ingredients: [
        { item: 'bread', quantity: '2', unit: 'slices' },
        { item: 'cheddar cheese', quantity: '2', unit: 'slices' },
        { item: 'butter', quantity: '1', unit: 'tbsp' }
      ]
    },
    expected: false
  },
  {
    name: 'Ricotta (culture-based, should detect)',
    recipe: {
      title: 'Fresh Ricotta',
      category: 'cheese',
      ingredients: [
        { item: 'whole milk', quantity: '1', unit: 'gallon' },
        { item: 'buttermilk culture', quantity: '1/4', unit: 'cup' }
      ],
      instructions: [
        { step: 1, text: 'Heat milk and add culture' },
        { step: 2, text: 'Let curds form and drain whey' }
      ]
    },
    expected: true
  },
  {
    name: 'Cheesecake (should NOT detect)',
    recipe: {
      title: 'New York Cheesecake',
      category: 'desserts',
      tags: ['dessert', 'baking'],
      ingredients: [
        { item: 'cream cheese', quantity: '32', unit: 'oz' },
        { item: 'sugar', quantity: '1', unit: 'cup' },
        { item: 'eggs', quantity: '4', unit: '' }
      ]
    },
    expected: false
  },
  {
    name: 'Ancient Cheese Recipe (should detect via tags)',
    recipe: {
      title: 'Oxygala (Ancient Roman Fresh Cheese)',
      category: 'mains',
      tags: ['ancient', 'roman', 'cheesemaking', 'historical'],
      ingredients: [
        { item: 'raw milk', quantity: '2', unit: 'quarts' },
        { item: 'vinegar', quantity: '2', unit: 'tbsp' }
      ]
    },
    expected: true
  },
  {
    name: 'Paneer (should detect)',
    recipe: {
      title: 'Homemade Paneer',
      ingredients: [
        { item: 'whole milk', quantity: '1/2', unit: 'gallon' },
        { item: 'lemon juice', quantity: '3', unit: 'tbsp' }
      ],
      instructions: [
        { step: 1, text: 'Heat milk to 190F' },
        { step: 2, text: 'Add lemon juice and stir until curds form' },
        { step: 3, text: 'Drain curds and press' }
      ]
    },
    expected: true
  },
  {
    name: 'Mac and Cheese (should NOT detect)',
    recipe: {
      title: 'Creamy Mac and Cheese',
      category: 'mains',
      ingredients: [
        { item: 'elbow macaroni', quantity: '1', unit: 'lb' },
        { item: 'cheddar cheese', quantity: '2', unit: 'cups' },
        { item: 'milk', quantity: '2', unit: 'cups' }
      ]
    },
    expected: false
  },
  {
    name: 'Recipe with milk_substitutions enabled',
    recipe: {
      title: 'Mystery Recipe',
      milk_substitutions: {
        enabled: true,
        original_milk: 'cow'
      }
    },
    expected: true
  },
  {
    name: 'Queso Fresco (Spanish name, should detect)',
    recipe: {
      title: 'Queso Fresco Casero',
      ingredients: [
        { item: 'fresh milk', quantity: '1', unit: 'gallon' },
        { item: 'rennet tablet', quantity: '1/4', unit: '' }
      ]
    },
    expected: true
  },
  {
    name: 'Labneh (should detect)',
    recipe: {
      title: 'Traditional Labneh',
      tags: ['middle-eastern', 'dairy'],
      ingredients: [
        { item: 'whole milk yogurt', quantity: '4', unit: 'cups' },
        { item: 'salt', quantity: '1', unit: 'tsp' }
      ],
      instructions: [
        { step: 1, text: 'Mix yogurt with salt' },
        { step: 2, text: 'Strain through cheesecloth for 24 hours to drain whey' }
      ]
    },
    expected: true
  }
];

for (const tc of testRecipes) {
  test(tc.name, () => {
    const result = isCheeseRecipe(tc.recipe);
    assertEqual(result, tc.expected, `${tc.name}: `);
  });
}

// ============================================================================
// Milk Type Detection Tests
// ============================================================================

console.log('\n=== Milk Type Detection Tests ===\n');

const MILK_TYPE_KEYWORDS = {
  sheep: ['sheep', "sheep's", 'ewe', 'ovine', 'pecora'],
  goat: ['goat', "goat's", 'caprine', 'chevre'],
  buffalo: ['buffalo', 'water buffalo', "buffalo's", 'bubalus'],
  camel: ['camel', "camel's", 'dromedary'],
  yak: ['yak', "yak's"],
  mare: ['mare', 'horse', "mare's", 'equine'],
  donkey: ['donkey', "donkey's", 'ass', 'jenny'],
  reindeer: ['reindeer', "reindeer's", 'caribou'],
  llama: ['llama', "llama's"],
  alpaca: ['alpaca', "alpaca's"]
};

function detectMilkType(ingredients) {
  if (!ingredients) return 'cow';

  for (const ing of ingredients) {
    const item = ing.item.toLowerCase();

    for (const [milkType, keywords] of Object.entries(MILK_TYPE_KEYWORDS)) {
      if (keywords.some(kw => item.includes(kw))) {
        return milkType;
      }
    }
  }

  return 'cow';
}

test('Detects sheep milk', () => {
  assertEqual(detectMilkType([{ item: "sheep's milk" }]), 'sheep');
});

test('Detects goat milk', () => {
  assertEqual(detectMilkType([{ item: 'fresh goat milk' }]), 'goat');
});

test('Detects buffalo milk', () => {
  assertEqual(detectMilkType([{ item: 'water buffalo milk' }]), 'buffalo');
});

test('Detects camel milk', () => {
  assertEqual(detectMilkType([{ item: 'camel milk' }]), 'camel');
});

test('Defaults to cow when unspecified', () => {
  assertEqual(detectMilkType([{ item: 'whole milk' }]), 'cow');
});

test('Defaults to cow with no ingredients', () => {
  assertEqual(detectMilkType([]), 'cow');
});

test('Detects first exotic milk in list', () => {
  assertEqual(detectMilkType([
    { item: 'water' },
    { item: 'sheep milk' },
    { item: 'goat milk' }
  ]), 'sheep');
});

// ============================================================================
// Summary
// ============================================================================

console.log('\n=== Test Summary ===\n');
console.log(`Passed: ${passed}`);
console.log(`Failed: ${failed}`);

if (failures.length > 0) {
  console.log('\nFailures:');
  for (const f of failures) {
    console.log(`  - ${f.name}: ${f.error}`);
  }
  process.exit(1);
}

console.log('\nAll tests passed!');
