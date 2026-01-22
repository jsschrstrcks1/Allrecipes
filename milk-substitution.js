/**
 * Milk Substitution Calculator for Cheese Recipes
 *
 * Provides interactive milk type switching and ingredient adjustment
 * for cheese-making recipes. Supports mixed milk ratios (e.g., 75% sheep,
 * 25% cow) with dynamic nutrition calculation.
 * Loads data from data/milk-substitution.json.
 */

// =============================================================================
// Milk Substitution Module
// =============================================================================

const MilkSubstitution = (function() {
  'use strict';

  // Module state
  let substitutionData = null;
  let isLoaded = false;
  let originalMilkType = 'cow';
  let quantityMultiplier = 1.0;

  // Mixed milk ratios (percentages, must sum to 100)
  let milkRatios = {
    cow: 100,
    goat: 0,
    sheep: 0
  };

  // Track whether we're in single or mixed mode
  let mixedMode = false;

  // Track whether we're in volume input mode
  let volumeMode = false;

  // Store volume inputs (in cups) for each milk type
  let milkVolumes = {
    cow: 0,
    goat: 0,
    sheep: 0
  };

  // Volume unit conversions to cups
  const VOLUME_TO_CUPS = {
    cups: 1,
    cup: 1,
    oz: 0.125,        // 8 oz = 1 cup
    'fl oz': 0.125,
    tbsp: 0.0625,     // 16 tbsp = 1 cup
    quart: 4,         // 1 quart = 4 cups
    quarts: 4,
    qt: 4,
    gallon: 16,       // 1 gallon = 16 cups
    gallons: 16,
    gal: 16,
    pint: 2,          // 1 pint = 2 cups
    pints: 2,
    pt: 2,
    ml: 0.00423,      // ~236ml = 1 cup
    liter: 4.227,     // 1 liter = ~4.227 cups
    liters: 4.227,
    l: 4.227
  };

  // Display names for volume units
  const VOLUME_UNITS = [
    { id: 'cups', label: 'cups' },
    { id: 'oz', label: 'fl oz' },
    { id: 'quarts', label: 'quarts' },
    { id: 'gallons', label: 'gallons' },
    { id: 'pints', label: 'pints' },
    { id: 'ml', label: 'ml' },
    { id: 'liters', label: 'liters' }
  ];

  // Ingredient keywords that should be adjusted
  const MILK_KEYWORDS = ['milk', 'whole milk', 'raw milk', 'pasteurized milk'];
  const RENNET_KEYWORDS = ['rennet', 'vegetable rennet', 'animal rennet', 'liquid rennet'];
  const CACL2_KEYWORDS = ['calcium chloride', 'cacl2', 'calcium chloride solution'];

  /**
   * Load substitution data from JSON file
   */
  async function loadData() {
    if (isLoaded && substitutionData) {
      return substitutionData;
    }

    try {
      const response = await fetch('data/milk-substitution.json');
      if (!response.ok) {
        console.warn('Milk substitution data not available');
        return null;
      }
      substitutionData = await response.json();
      isLoaded = true;
      console.log('Milk substitution data loaded');
      return substitutionData;
    } catch (error) {
      console.error('Failed to load milk substitution data:', error);
      return null;
    }
  }

  /**
   * Check if a recipe is a cheese recipe
   */
  function isCheeseRecipe(recipe) {
    if (!recipe) return false;

    // Check tags
    if (recipe.tags && recipe.tags.some(tag =>
      tag.toLowerCase().includes('cheese') ||
      tag.toLowerCase() === 'cheesemaking'
    )) {
      return true;
    }

    // Check title
    if (recipe.title && recipe.title.toLowerCase().includes('cheese')) {
      return true;
    }

    // Check category
    if (recipe.category && recipe.category.toLowerCase() === 'cheese') {
      return true;
    }

    // Check ingredients for cheese-making indicators
    if (recipe.ingredients) {
      const hasRennet = recipe.ingredients.some(ing =>
        RENNET_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
      );
      const hasMilk = recipe.ingredients.some(ing =>
        MILK_KEYWORDS.some(kw => ing.item.toLowerCase().includes(kw))
      );
      if (hasRennet && hasMilk) {
        return true;
      }
    }

    return false;
  }

  // Milk type detection keywords
  const MILK_TYPE_KEYWORDS = {
    sheep: ['sheep', "sheep's", 'ewe', 'ovine'],
    goat: ['goat', "goat's", 'caprine'],
    buffalo: ['buffalo', 'water buffalo', "buffalo's", 'bubalus'],
    camel: ['camel', "camel's", 'dromedary'],
    yak: ['yak', "yak's"],
    mare: ['mare', 'horse', "mare's", 'equine'],
    donkey: ['donkey', "donkey's", 'ass', 'jenny'],
    reindeer: ['reindeer', "reindeer's", 'caribou'],
    llama: ['llama', "llama's"],
    alpaca: ['alpaca', "alpaca's"]
  };

  /**
   * Detect the original milk type from recipe ingredients
   * Supports both common (cow, goat, sheep) and exotic milk types
   */
  function detectOriginalMilkType(recipe) {
    if (!recipe || !recipe.ingredients) return 'cow';

    for (const ing of recipe.ingredients) {
      const item = ing.item.toLowerCase();

      // Check for exotic and specific milk types first
      for (const [milkType, keywords] of Object.entries(MILK_TYPE_KEYWORDS)) {
        if (keywords.some(kw => item.includes(kw))) {
          return milkType;
        }
      }
    }

    // Default to cow if no specific type mentioned
    return 'cow';
  }

  /**
   * Check if a milk type is available (can be used as output)
   */
  function isAvailableMilkType(milkType) {
    if (!substitutionData) return milkType === 'cow' || milkType === 'goat' || milkType === 'sheep';
    return substitutionData.available_milk_types?.includes(milkType) ||
           substitutionData.milk_types?.[milkType]?.available === true;
  }

  /**
   * Get the recommended substitute for an exotic milk type
   */
  function getRecommendedSubstitute(milkType) {
    if (!substitutionData) return 'cow';
    const milkInfo = substitutionData.milk_types?.[milkType];
    return milkInfo?.best_substitute || 'cow';
  }

  /**
   * Get substitute notes for an exotic milk type
   */
  function getSubstituteNotes(milkType) {
    if (!substitutionData) return null;
    return substitutionData.milk_types?.[milkType]?.substitute_notes;
  }

  /**
   * Check if the original milk type is exotic (not commonly available)
   */
  function isExoticMilkType(milkType) {
    return !isAvailableMilkType(milkType);
  }

  /**
   * Get the dominant milk type from current ratios
   */
  function getDominantMilkType() {
    let maxRatio = 0;
    let dominant = 'cow';
    for (const [type, ratio] of Object.entries(milkRatios)) {
      if (ratio > maxRatio) {
        maxRatio = ratio;
        dominant = type;
      }
    }
    return dominant;
  }

  /**
   * Get volume conversion factor for mixed milk
   * Uses weighted average based on ratios
   */
  function getVolumeConversionFactor(fromMilk) {
    if (!substitutionData) return 1.0;

    // Calculate weighted conversion factor
    let totalFactor = 0;
    for (const [toMilk, ratio] of Object.entries(milkRatios)) {
      if (ratio > 0) {
        const key = `${fromMilk}_to_${toMilk}`;
        const factor = substitutionData.volume_conversions?.factors?.[key] || 1.0;
        totalFactor += factor * (ratio / 100);
      }
    }
    return totalFactor;
  }

  /**
   * Get rennet adjustment factor for mixed milk
   * Uses weighted average based on ratios
   */
  function getRennetFactor() {
    if (!substitutionData) return 1.0;

    let totalFactor = 0;
    for (const [milkType, ratio] of Object.entries(milkRatios)) {
      if (ratio > 0) {
        const factor = substitutionData.rennet_adjustments?.factors?.[milkType] || 1.0;
        totalFactor += factor * (ratio / 100);
      }
    }
    return totalFactor;
  }

  /**
   * Get CaCl2 recommendation for mixed milk
   */
  function getCaCl2Recommendation(isRaw = false) {
    if (!substitutionData) return null;

    // If sheep milk is 50% or more, CaCl2 is generally not needed
    if (milkRatios.sheep >= 50) {
      return 'reduced_or_none';
    }

    const processing = isRaw ? 'raw' : 'pasteurized';
    const dominant = getDominantMilkType();
    return substitutionData.calcium_chloride_guidelines?.recommendations?.[dominant]?.[processing];
  }

  /**
   * Check if CaCl2 should be omitted
   */
  function shouldOmitCaCl2() {
    // Omit if sheep milk is dominant (>=50%)
    return milkRatios.sheep >= 50;
  }

  /**
   * Parse quantity string to number
   */
  function parseQuantity(quantityStr) {
    if (!quantityStr) return null;

    const str = String(quantityStr).trim();

    // Handle fractions like "1/2", "1/4"
    if (str.includes('/')) {
      const parts = str.split('/');
      if (parts.length === 2) {
        const num = parseFloat(parts[0]);
        const denom = parseFloat(parts[1]);
        if (!isNaN(num) && !isNaN(denom) && denom !== 0) {
          return num / denom;
        }
      }
      // Handle mixed fractions like "1 1/2"
      const mixedMatch = str.match(/^(\d+)\s+(\d+)\/(\d+)$/);
      if (mixedMatch) {
        const whole = parseFloat(mixedMatch[1]);
        const num = parseFloat(mixedMatch[2]);
        const denom = parseFloat(mixedMatch[3]);
        return whole + (num / denom);
      }
    }

    // Handle ranges like "2-3" - use the first number
    if (str.includes('-')) {
      const parts = str.split('-');
      const num = parseFloat(parts[0]);
      if (!isNaN(num)) return num;
    }

    const num = parseFloat(str);
    return isNaN(num) ? null : num;
  }

  /**
   * Format quantity for display
   */
  function formatQuantity(num) {
    if (num === null || num === undefined) return '';

    // Common fractions
    const fractions = {
      0.125: '1/8',
      0.167: '1/6',
      0.25: '1/4',
      0.333: '1/3',
      0.375: '3/8',
      0.5: '1/2',
      0.625: '5/8',
      0.667: '2/3',
      0.75: '3/4',
      0.875: '7/8'
    };

    const whole = Math.floor(num);
    const decimal = num - whole;

    // Find closest fraction
    let closestFrac = '';
    let minDiff = 0.05;

    for (const [val, str] of Object.entries(fractions)) {
      const diff = Math.abs(decimal - parseFloat(val));
      if (diff < minDiff) {
        minDiff = diff;
        closestFrac = str;
      }
    }

    if (whole === 0 && closestFrac) {
      return closestFrac;
    } else if (closestFrac) {
      return `${whole} ${closestFrac}`;
    } else if (decimal < 0.05) {
      return String(whole);
    } else {
      // Round to reasonable precision
      return num.toFixed(2).replace(/\.?0+$/, '');
    }
  }

  /**
   * Get milk blend description string
   */
  function getMilkBlendDescription() {
    const parts = [];
    for (const [type, ratio] of Object.entries(milkRatios)) {
      if (ratio > 0) {
        const info = substitutionData?.milk_types?.[type];
        const name = info?.name || type;
        parts.push(`${ratio}% ${name.toLowerCase()}`);
      }
    }
    return parts.join(', ');
  }

  /**
   * Adjust an ingredient based on milk substitution
   */
  function adjustIngredient(ingredient, fromMilk, qtyMultiplier = 1.0) {
    const item = ingredient.item.toLowerCase();
    const adjusted = { ...ingredient };

    // Check if this is a milk ingredient
    const isMilk = MILK_KEYWORDS.some(kw => item.includes(kw));
    if (isMilk) {
      const volumeFactor = getVolumeConversionFactor(fromMilk);
      const originalQty = parseQuantity(ingredient.quantity);
      if (originalQty !== null) {
        const newQty = originalQty * volumeFactor * qtyMultiplier;
        adjusted.quantity = formatQuantity(newQty);
      }
      // Update item name to reflect milk blend
      const blendDesc = getMilkBlendDescription();
      adjusted.item = ingredient.item.replace(/cow('s)?|goat('s)?|sheep('s)?/gi, '')
        .replace(/milk/i, `milk (${blendDesc})`);
      adjusted._adjusted = true;
      adjusted._adjustmentNote = `Volume adjusted for milk blend: ${blendDesc}`;
      return adjusted;
    }

    // Check if this is rennet
    const isRennet = RENNET_KEYWORDS.some(kw => item.includes(kw));
    if (isRennet) {
      const fromRennetFactor = substitutionData?.rennet_adjustments?.factors?.[fromMilk] || 1.0;
      const toRennetFactor = getRennetFactor();
      const rennetRatio = toRennetFactor / fromRennetFactor;

      const originalQty = parseQuantity(ingredient.quantity);
      if (originalQty !== null) {
        const newQty = originalQty * rennetRatio * qtyMultiplier;
        adjusted.quantity = formatQuantity(newQty);
      }
      adjusted._adjusted = true;
      adjusted._adjustmentNote = `Rennet adjusted for milk blend (${Math.round(rennetRatio * 100)}% of original)`;
      return adjusted;
    }

    // Check if this is CaCl2
    const isCaCl2 = CACL2_KEYWORDS.some(kw => item.includes(kw));
    if (isCaCl2) {
      if (shouldOmitCaCl2()) {
        adjusted.quantity = '0';
        adjusted._adjusted = true;
        adjusted._adjustmentNote = 'CaCl2 reduced/omitted (sheep milk provides high natural calcium)';
        adjusted._omit = true;
      }
      return adjusted;
    }

    // Apply quantity multiplier to other ingredients
    if (qtyMultiplier !== 1.0) {
      const originalQty = parseQuantity(ingredient.quantity);
      if (originalQty !== null) {
        const newQty = originalQty * qtyMultiplier;
        adjusted.quantity = formatQuantity(newQty);
        adjusted._adjusted = true;
      }
    }

    return adjusted;
  }

  /**
   * Get all adjusted ingredients for a recipe
   */
  function getAdjustedIngredients(recipe, qtyMultiplier = 1.0) {
    if (!recipe || !recipe.ingredients) return [];

    const fromMilk = detectOriginalMilkType(recipe);

    return recipe.ingredients.map(ing =>
      adjustIngredient(ing, fromMilk, qtyMultiplier)
    ).filter(ing => !ing._omit);
  }

  /**
   * Get milk type info
   */
  function getMilkTypeInfo(milkType) {
    if (!substitutionData) return null;
    return substitutionData.milk_types?.[milkType];
  }

  /**
   * Get flavor expectations
   */
  function getFlavorExpectations(milkType) {
    if (!substitutionData) return null;
    return substitutionData.flavor_expectations?.[milkType];
  }

  /**
   * Get curd handling notes
   */
  function getCurdHandlingNotes(milkType) {
    if (!substitutionData) return null;
    return substitutionData.curd_handling_notes?.[milkType];
  }

  /**
   * Calculate blended milk info based on current ratios
   */
  function getBlendedMilkInfo() {
    if (!substitutionData) return null;

    const blended = {
      fat_percent: 0,
      protein_percent: 0,
      cheese_yield_per_gallon_lb: 0,
      coagulation_speed: 'standard',
      flavor_profile: [],
      texture_notes: []
    };

    let coagSpeeds = { standard: 0, faster: 0, fastest: 0 };

    for (const [type, ratio] of Object.entries(milkRatios)) {
      if (ratio > 0) {
        const info = substitutionData.milk_types?.[type];
        if (info) {
          const weight = ratio / 100;
          blended.fat_percent += info.fat_percent * weight;
          blended.protein_percent += info.protein_percent * weight;
          blended.cheese_yield_per_gallon_lb += info.cheese_yield_per_gallon_lb * weight;

          // Track coagulation speeds
          coagSpeeds[info.coagulation_speed] = (coagSpeeds[info.coagulation_speed] || 0) + ratio;

          // Collect unique flavor profiles
          if (ratio >= 25) {
            info.flavor_profile.forEach(fp => {
              if (!blended.flavor_profile.includes(fp)) {
                blended.flavor_profile.push(fp);
              }
            });
            blended.texture_notes.push(`${ratio}% ${info.name}: ${info.texture_notes}`);
          }
        }
      }
    }

    // Determine dominant coagulation speed
    blended.coagulation_speed = Object.entries(coagSpeeds)
      .sort((a, b) => b[1] - a[1])[0][0];

    // Round values
    blended.fat_percent = Math.round(blended.fat_percent * 10) / 10;
    blended.protein_percent = Math.round(blended.protein_percent * 10) / 10;
    blended.cheese_yield_per_gallon_lb = Math.round(blended.cheese_yield_per_gallon_lb * 100) / 100;

    return blended;
  }

  /**
   * Calculate blended nutrition per cup based on current ratios
   */
  function getBlendedNutrition() {
    if (!substitutionData || !substitutionData.nutrition_per_cup) return null;

    const blended = {
      calories: 0,
      fat_g: 0,
      saturated_fat_g: 0,
      carbs_g: 0,
      protein_g: 0,
      sodium_mg: 0,
      calcium_mg: 0,
      sugar_g: 0,
      cholesterol_mg: 0
    };

    for (const [type, ratio] of Object.entries(milkRatios)) {
      if (ratio > 0) {
        const nutrition = substitutionData.nutrition_per_cup?.[type];
        if (nutrition) {
          const weight = ratio / 100;
          blended.calories += nutrition.calories * weight;
          blended.fat_g += nutrition.fat_g * weight;
          blended.saturated_fat_g += nutrition.saturated_fat_g * weight;
          blended.carbs_g += nutrition.carbs_g * weight;
          blended.protein_g += nutrition.protein_g * weight;
          blended.sodium_mg += nutrition.sodium_mg * weight;
          blended.calcium_mg += nutrition.calcium_mg * weight;
          blended.sugar_g += nutrition.sugar_g * weight;
          blended.cholesterol_mg += nutrition.cholesterol_mg * weight;
        }
      }
    }

    // Round values appropriately
    blended.calories = Math.round(blended.calories);
    blended.fat_g = Math.round(blended.fat_g * 10) / 10;
    blended.saturated_fat_g = Math.round(blended.saturated_fat_g * 10) / 10;
    blended.carbs_g = Math.round(blended.carbs_g);
    blended.protein_g = Math.round(blended.protein_g);
    blended.sodium_mg = Math.round(blended.sodium_mg);
    blended.calcium_mg = Math.round(blended.calcium_mg);
    blended.sugar_g = Math.round(blended.sugar_g);
    blended.cholesterol_mg = Math.round(blended.cholesterol_mg);

    return blended;
  }

  /**
   * Normalize ratios to ensure they sum to 100
   */
  function normalizeRatios(changedType = null) {
    const total = Object.values(milkRatios).reduce((a, b) => a + b, 0);

    if (total === 100) return;

    if (total === 0) {
      // Reset to 100% of the changed type or cow
      milkRatios[changedType || 'cow'] = 100;
      return;
    }

    // Scale all ratios proportionally
    const scale = 100 / total;
    for (const type of Object.keys(milkRatios)) {
      milkRatios[type] = Math.round(milkRatios[type] * scale);
    }

    // Fix rounding errors
    const newTotal = Object.values(milkRatios).reduce((a, b) => a + b, 0);
    if (newTotal !== 100) {
      const diff = 100 - newTotal;
      const dominant = getDominantMilkType();
      milkRatios[dominant] += diff;
    }
  }

  /**
   * Set milk ratio and adjust others proportionally
   */
  function setMilkRatio(milkType, newRatio) {
    newRatio = Math.max(0, Math.min(100, newRatio));

    const oldRatio = milkRatios[milkType];
    const diff = newRatio - oldRatio;

    // Calculate remaining ratio to distribute
    const otherTypes = Object.keys(milkRatios).filter(t => t !== milkType);
    const otherTotal = otherTypes.reduce((sum, t) => sum + milkRatios[t], 0);

    milkRatios[milkType] = newRatio;

    if (otherTotal > 0) {
      // Distribute the difference proportionally among other types
      for (const type of otherTypes) {
        const proportion = milkRatios[type] / otherTotal;
        milkRatios[type] = Math.max(0, Math.round(milkRatios[type] - diff * proportion));
      }
    } else if (diff < 0) {
      // If other types were 0 and we're reducing, put remainder in cow (or first non-zero other)
      milkRatios[otherTypes[0]] = 100 - newRatio;
    }

    normalizeRatios(milkType);
  }

  /**
   * Convert a volume value from one unit to cups
   */
  function convertToCups(value, unit) {
    const normalizedUnit = unit.toLowerCase().trim();
    const factor = VOLUME_TO_CUPS[normalizedUnit];
    if (factor === undefined) {
      console.warn(`Unknown unit: ${unit}, defaulting to cups`);
      return value;
    }
    return value * factor;
  }

  /**
   * Convert cups to another unit
   */
  function convertFromCups(cups, unit) {
    const normalizedUnit = unit.toLowerCase().trim();
    const factor = VOLUME_TO_CUPS[normalizedUnit];
    if (factor === undefined || factor === 0) {
      return cups;
    }
    return cups / factor;
  }

  /**
   * Set milk volumes and automatically calculate ratios
   */
  function setMilkVolumes(volumes) {
    milkVolumes = { ...volumes };
    calculateRatiosFromVolumes();
  }

  /**
   * Set a single milk volume and recalculate ratios
   */
  function setMilkVolume(milkType, value, unit = 'cups') {
    const cups = convertToCups(value, unit);
    milkVolumes[milkType] = cups;
    calculateRatiosFromVolumes();
  }

  /**
   * Calculate percentages from volume inputs
   */
  function calculateRatiosFromVolumes() {
    const totalCups = Object.values(milkVolumes).reduce((a, b) => a + b, 0);

    if (totalCups === 0) {
      // Reset to default if no volumes entered
      milkRatios = { cow: 100, goat: 0, sheep: 0 };
      return;
    }

    // Calculate ratios based on volume proportions
    for (const type of Object.keys(milkRatios)) {
      milkRatios[type] = Math.round((milkVolumes[type] / totalCups) * 100);
    }

    // Fix rounding errors
    normalizeRatios();
  }

  /**
   * Get total milk volume in cups
   */
  function getTotalVolumeCups() {
    return Object.values(milkVolumes).reduce((a, b) => a + b, 0);
  }

  /**
   * Get total milk volume in a specified unit
   */
  function getTotalVolume(unit = 'cups') {
    const cups = getTotalVolumeCups();
    return convertFromCups(cups, unit);
  }

  /**
   * Get milk volumes
   */
  function getMilkVolumes() {
    return { ...milkVolumes };
  }

  /**
   * Format volume for display
   */
  function formatVolume(cups, unit = 'cups') {
    const value = convertFromCups(cups, unit);
    if (value === 0) return '0';
    if (value < 0.1) return value.toFixed(2);
    if (value < 1) return value.toFixed(1);
    if (Number.isInteger(value)) return String(value);
    return value.toFixed(1);
  }

  /**
   * Check if in volume mode
   */
  function isVolumeMode() {
    return volumeMode;
  }

  /**
   * Enter volume mode
   */
  function enterVolumeMode() {
    volumeMode = true;
    mixedMode = true;
  }

  /**
   * Set single milk mode (100% of one type)
   */
  function setSingleMilk(milkType) {
    milkRatios = {
      cow: 0,
      goat: 0,
      sheep: 0
    };
    milkRatios[milkType] = 100;
    milkVolumes = { cow: 0, goat: 0, sheep: 0 };
    mixedMode = false;
    volumeMode = false;
  }

  /**
   * Enter mixed mode with current ratios (percentage-based)
   */
  function enterMixedMode() {
    mixedMode = true;
    volumeMode = false;
  }

  /**
   * Get current milk ratios
   */
  function getMilkRatios() {
    return { ...milkRatios };
  }

  /**
   * Check if in mixed mode
   */
  function isMixedMode() {
    return mixedMode;
  }

  /**
   * Render the milk substitution UI
   */
  function renderMilkSwitcher(recipe, containerId) {
    const container = document.getElementById(containerId);
    if (!container || !substitutionData) return;

    const detectedMilk = detectOriginalMilkType(recipe);
    originalMilkType = detectedMilk;

    // Check if original milk is exotic (not available)
    const isExotic = isExoticMilkType(detectedMilk);
    const recommendedSub = isExotic ? getRecommendedSubstitute(detectedMilk) : detectedMilk;
    const subNotes = isExotic ? getSubstituteNotes(detectedMilk) : null;

    // Initialize ratios based on detected or recommended milk type
    setSingleMilk(isExotic ? recommendedSub : detectedMilk);

    // Get only available milk types for the UI
    const availableMilkTypes = substitutionData.available_milk_types ||
      Object.keys(substitutionData.milk_types).filter(t => substitutionData.milk_types[t].available !== false);

    // Build exotic milk notice with override option
    const originalMilkInfo = substitutionData.milk_types[detectedMilk];
    const exoticNotice = isExotic ? `
      <div class="exotic-milk-notice">
        <div class="exotic-milk-header">
          <strong>Original Recipe Uses ${originalMilkInfo?.name || detectedMilk}</strong>
        </div>
        <p class="exotic-milk-message">
          This milk is not commonly available. ${subNotes || `We recommend using ${substitutionData.milk_types[recommendedSub]?.name || recommendedSub} as a substitute.`}
        </p>
        <div class="exotic-milk-override">
          <span class="override-label">You can override this recommendation below using any of your available milks.</span>
        </div>
      </div>
    ` : '';

    const html = `
      <div class="milk-substitution-panel">
        <h3>Milk Substitution Calculator</h3>
        <p class="milk-sub-intro">Adjust this cheese recipe for different milk types or create a custom blend.</p>

        ${exoticNotice}

        <div class="milk-sub-controls">
          <div class="milk-sub-mode-toggle">
            <button type="button" id="single-mode-btn" class="mode-btn active" title="Select one milk type">Single Milk</button>
            <button type="button" id="mixed-mode-btn" class="mode-btn" title="Create a custom milk blend by percentages">% Blend</button>
            <button type="button" id="volume-mode-btn" class="mode-btn" title="Enter the volumes of milk you have on hand">What I Have</button>
          </div>

          <div id="single-milk-controls" class="milk-sub-row">
            <label for="milk-type-select">Milk Type:</label>
            <select id="milk-type-select" class="milk-type-select">
              ${availableMilkTypes.map(type => {
                const info = substitutionData.milk_types[type];
                const selected = type === recommendedSub ? 'selected' : '';
                return `<option value="${type}" ${selected}>${info.name}</option>`;
              }).join('')}
            </select>
          </div>

          <div id="mixed-milk-controls" class="milk-blend-controls" style="display: none;">
            ${availableMilkTypes.map(type => {
              const info = substitutionData.milk_types[type];
              const initialValue = type === recommendedSub ? 100 : 0;
              return `
                <div class="milk-ratio-row">
                  <label class="milk-ratio-label">
                    <span class="milk-type-name">${info.name}</span>
                    <span class="milk-ratio-value" id="${type}-ratio-display">${initialValue}%</span>
                  </label>
                  <input type="range"
                         id="${type}-ratio-slider"
                         class="milk-ratio-slider"
                         data-milk-type="${type}"
                         min="0"
                         max="100"
                         value="${initialValue}"
                         step="5">
                  <input type="number"
                         id="${type}-ratio-input"
                         class="milk-ratio-input"
                         data-milk-type="${type}"
                         min="0"
                         max="100"
                         value="${initialValue}"
                         step="5">
                </div>
              `;
            }).join('')}
            <div class="ratio-total-row">
              <span>Total:</span>
              <span id="ratio-total" class="ratio-total">100%</span>
            </div>
          </div>

          <div id="volume-milk-controls" class="milk-volume-controls" style="display: none;">
            <p class="volume-input-intro">Enter the amounts of milk you have available:</p>
            ${availableMilkTypes.map(type => {
              const info = substitutionData.milk_types[type];
              return `
                <div class="milk-volume-row">
                  <label class="milk-volume-label">
                    <span class="milk-type-name">${info.name}</span>
                  </label>
                  <input type="number"
                         id="${type}-volume-input"
                         class="milk-volume-input"
                         data-milk-type="${type}"
                         min="0"
                         step="0.25"
                         value="0"
                         placeholder="0">
                  <select id="${type}-volume-unit"
                          class="milk-volume-unit"
                          data-milk-type="${type}">
                    ${VOLUME_UNITS.map(u => `<option value="${u.id}"${u.id === 'cups' ? ' selected' : ''}>${u.label}</option>`).join('')}
                  </select>
                  <span class="milk-volume-percent" id="${type}-volume-percent">0%</span>
                </div>
              `;
            }).join('')}
            <div class="volume-total-row">
              <span class="volume-total-label">Total:</span>
              <span id="volume-total" class="volume-total">0 cups</span>
              <span class="volume-total-note">(Ratios calculated automatically)</span>
            </div>
          </div>

          <div class="milk-sub-row">
            <label for="quantity-multiplier">Batch Size:</label>
            <select id="quantity-multiplier" class="quantity-multiplier-select">
              <option value="0.5">Half batch (0.5x)</option>
              <option value="1" selected>Original (1x)</option>
              <option value="1.5">1.5x batch</option>
              <option value="2">Double batch (2x)</option>
              <option value="3">Triple batch (3x)</option>
            </select>
          </div>
        </div>

        <div id="milk-sub-info" class="milk-sub-info">
          ${renderMilkInfo()}
        </div>

        <div id="milk-nutrition-info" class="milk-nutrition-info">
          ${renderNutritionInfo()}
        </div>

        <div id="milk-sub-warnings" class="milk-sub-warnings"></div>
      </div>
    `;

    container.innerHTML = html;

    // Attach event listeners
    attachEventListeners(recipe);
  }

  /**
   * Attach event listeners for all controls
   */
  function attachEventListeners(recipe) {
    const singleModeBtn = document.getElementById('single-mode-btn');
    const mixedModeBtn = document.getElementById('mixed-mode-btn');
    const volumeModeBtn = document.getElementById('volume-mode-btn');
    const singleControls = document.getElementById('single-milk-controls');
    const mixedControls = document.getElementById('mixed-milk-controls');
    const volumeControls = document.getElementById('volume-milk-controls');
    const milkSelect = document.getElementById('milk-type-select');
    const qtySelect = document.getElementById('quantity-multiplier');

    // Helper to clear all mode buttons
    function clearModeButtons() {
      singleModeBtn?.classList.remove('active');
      mixedModeBtn?.classList.remove('active');
      volumeModeBtn?.classList.remove('active');
    }

    // Helper to hide all control panels
    function hideAllControls() {
      if (singleControls) singleControls.style.display = 'none';
      if (mixedControls) mixedControls.style.display = 'none';
      if (volumeControls) volumeControls.style.display = 'none';
    }

    // Mode toggle - Single Milk
    if (singleModeBtn) {
      singleModeBtn.addEventListener('click', () => {
        clearModeButtons();
        hideAllControls();
        singleModeBtn.classList.add('active');
        singleControls.style.display = '';

        // Reset to selected single milk
        const selectedMilk = milkSelect.value;
        setSingleMilk(selectedMilk);
        updateMilkSubstitution(recipe);
      });
    }

    // Mode toggle - Mixed/Percent Blend
    if (mixedModeBtn) {
      mixedModeBtn.addEventListener('click', () => {
        clearModeButtons();
        hideAllControls();
        mixedModeBtn.classList.add('active');
        mixedControls.style.display = '';

        enterMixedMode();
        updateSliderDisplays();
        updateMilkSubstitution(recipe);
      });
    }

    // Mode toggle - Volume Input ("What I Have")
    if (volumeModeBtn) {
      volumeModeBtn.addEventListener('click', () => {
        clearModeButtons();
        hideAllControls();
        volumeModeBtn.classList.add('active');
        volumeControls.style.display = '';

        enterVolumeMode();
        updateVolumeDisplays();
        updateMilkSubstitution(recipe);
      });
    }

    // Single milk select
    if (milkSelect) {
      milkSelect.addEventListener('change', (e) => {
        setSingleMilk(e.target.value);
        updateMilkSubstitution(recipe);
      });
    }

    // Batch size
    if (qtySelect) {
      qtySelect.addEventListener('change', (e) => {
        quantityMultiplier = parseFloat(e.target.value);
        updateMilkSubstitution(recipe);
      });
    }

    // Mixed mode sliders and inputs
    const milkTypes = ['cow', 'goat', 'sheep'];
    for (const type of milkTypes) {
      const slider = document.getElementById(`${type}-ratio-slider`);
      const input = document.getElementById(`${type}-ratio-input`);

      if (slider) {
        slider.addEventListener('input', (e) => {
          const newValue = parseInt(e.target.value, 10);
          setMilkRatio(type, newValue);
          updateSliderDisplays();
          updateMilkSubstitution(recipe);
        });
      }

      if (input) {
        input.addEventListener('change', (e) => {
          const newValue = parseInt(e.target.value, 10) || 0;
          setMilkRatio(type, newValue);
          updateSliderDisplays();
          updateMilkSubstitution(recipe);
        });
      }
    }

    // Volume mode inputs and unit selectors
    for (const type of milkTypes) {
      const volumeInput = document.getElementById(`${type}-volume-input`);
      const unitSelect = document.getElementById(`${type}-volume-unit`);

      if (volumeInput) {
        volumeInput.addEventListener('input', (e) => {
          const value = parseFloat(e.target.value) || 0;
          const unit = unitSelect?.value || 'cups';
          setMilkVolume(type, value, unit);
          updateVolumeDisplays();
          updateMilkSubstitution(recipe);
        });
      }

      if (unitSelect) {
        unitSelect.addEventListener('change', (e) => {
          // When unit changes, recalculate with current input value
          const value = parseFloat(volumeInput?.value) || 0;
          const unit = e.target.value;
          setMilkVolume(type, value, unit);
          updateVolumeDisplays();
          updateMilkSubstitution(recipe);
        });
      }
    }
  }

  /**
   * Update all volume displays to match current volumes
   */
  function updateVolumeDisplays() {
    const milkTypes = ['cow', 'goat', 'sheep'];
    const totalCups = getTotalVolumeCups();

    for (const type of milkTypes) {
      const percentDisplay = document.getElementById(`${type}-volume-percent`);
      if (percentDisplay) {
        const percent = totalCups > 0 ? Math.round((milkVolumes[type] / totalCups) * 100) : 0;
        percentDisplay.textContent = `${percent}%`;
      }
    }

    // Update total display
    const totalDisplay = document.getElementById('volume-total');
    if (totalDisplay) {
      if (totalCups === 0) {
        totalDisplay.textContent = '0 cups';
      } else if (totalCups >= 16) {
        // Show in gallons if >= 1 gallon
        const gallons = totalCups / 16;
        totalDisplay.textContent = `${gallons.toFixed(1)} gallons (${totalCups.toFixed(1)} cups)`;
      } else if (totalCups >= 4) {
        // Show in quarts if >= 1 quart
        const quarts = totalCups / 4;
        totalDisplay.textContent = `${quarts.toFixed(1)} quarts (${totalCups.toFixed(1)} cups)`;
      } else {
        totalDisplay.textContent = `${totalCups.toFixed(1)} cups`;
      }
    }
  }

  /**
   * Update all slider and input displays to match current ratios
   */
  function updateSliderDisplays() {
    const milkTypes = ['cow', 'goat', 'sheep'];
    let total = 0;

    for (const type of milkTypes) {
      const slider = document.getElementById(`${type}-ratio-slider`);
      const input = document.getElementById(`${type}-ratio-input`);
      const display = document.getElementById(`${type}-ratio-display`);
      const value = milkRatios[type];
      total += value;

      if (slider) slider.value = value;
      if (input) input.value = value;
      if (display) display.textContent = `${value}%`;
    }

    const totalDisplay = document.getElementById('ratio-total');
    if (totalDisplay) {
      totalDisplay.textContent = `${total}%`;
      totalDisplay.classList.toggle('ratio-error', total !== 100);
    }
  }

  /**
   * Render milk type info panel
   */
  function renderMilkInfo() {
    const blended = getBlendedMilkInfo();
    if (!blended) return '';

    const activeMilks = Object.entries(milkRatios)
      .filter(([_, ratio]) => ratio > 0)
      .map(([type, ratio]) => {
        const info = substitutionData.milk_types[type];
        return `${ratio}% ${info.name}`;
      }).join(' + ');

    return `
      <div class="milk-blend-header">
        <strong>Milk Blend:</strong> ${activeMilks || 'None selected'}
      </div>

      <div class="milk-info-grid">
        <div class="milk-info-item">
          <span class="milk-info-label">Fat Content</span>
          <span class="milk-info-value">${blended.fat_percent}%</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Protein</span>
          <span class="milk-info-value">${blended.protein_percent}%</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Yield/Gallon</span>
          <span class="milk-info-value">~${blended.cheese_yield_per_gallon_lb} lb</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Coagulation</span>
          <span class="milk-info-value">${blended.coagulation_speed}</span>
        </div>
      </div>

      ${blended.flavor_profile.length > 0 ? `
        <div class="milk-flavor-notes">
          <strong>Flavor Profile:</strong> ${blended.flavor_profile.join(', ')}
        </div>
      ` : ''}

      ${blended.texture_notes.length > 0 ? `
        <div class="milk-texture-notes">
          <strong>Texture Notes:</strong><br>
          ${blended.texture_notes.map(n => `<span class="texture-note">${n}</span>`).join('<br>')}
        </div>
      ` : ''}
    `;
  }

  /**
   * Render nutrition info panel
   */
  function renderNutritionInfo() {
    const nutrition = getBlendedNutrition();
    if (!nutrition) return '';

    return `
      <div class="milk-nutrition-header">
        <strong>Milk Nutrition</strong> <span class="nutrition-subtext">(per cup)</span>
      </div>
      <div class="milk-nutrition-grid">
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.calories}</span>
          <span class="nutrition-label-small">Cal</span>
        </div>
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.fat_g}g</span>
          <span class="nutrition-label-small">Fat</span>
        </div>
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.protein_g}g</span>
          <span class="nutrition-label-small">Protein</span>
        </div>
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.carbs_g}g</span>
          <span class="nutrition-label-small">Carbs</span>
        </div>
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.calcium_mg}mg</span>
          <span class="nutrition-label-small">Calcium</span>
        </div>
        <div class="nutrition-item-small">
          <span class="nutrition-value-small">${nutrition.cholesterol_mg}mg</span>
          <span class="nutrition-label-small">Cholest.</span>
        </div>
      </div>
    `;
  }

  /**
   * Update the recipe display with substituted ingredients
   */
  function updateMilkSubstitution(recipe) {
    // Update info panel
    const infoPanel = document.getElementById('milk-sub-info');
    if (infoPanel) {
      infoPanel.innerHTML = renderMilkInfo();
    }

    // Update nutrition panel
    const nutritionPanel = document.getElementById('milk-nutrition-info');
    if (nutritionPanel) {
      nutritionPanel.innerHTML = renderNutritionInfo();
    }

    // Update warnings
    const warningsPanel = document.getElementById('milk-sub-warnings');
    if (warningsPanel) {
      const warnings = [];

      // Check if milk blend differs from original
      const hasChange = milkRatios[originalMilkType] < 100;
      if (hasChange) {
        const originalInfo = substitutionData.milk_types[originalMilkType];
        warnings.push(`Original recipe uses ${originalInfo.name}. Your blend will affect flavor and texture.`);
      }

      // Warn about high sheep content
      if (milkRatios.sheep >= 50 && originalMilkType !== 'sheep') {
        warnings.push('High sheep milk content: CaCl2 has been reduced/omitted due to natural calcium content.');
      }

      // Warn about goat milk fragility
      if (milkRatios.goat >= 40) {
        warnings.push('Goat milk produces fragile curds. Handle gently and consider larger curd cuts.');
      }

      if (warnings.length > 0) {
        warningsPanel.innerHTML = warnings.map(w => `
          <div class="milk-sub-warning">
            <strong>Note:</strong> ${w}
          </div>
        `).join('');
      } else {
        warningsPanel.innerHTML = '';
      }
    }

    // Update ingredients list
    const adjustedIngredients = getAdjustedIngredients(recipe, quantityMultiplier);

    // Dispatch custom event for the main script to handle
    const event = new CustomEvent('milkSubstitutionChanged', {
      detail: {
        originalMilkType,
        milkRatios: getMilkRatios(),
        milkVolumes: getMilkVolumes(),
        mixedMode,
        volumeMode,
        quantityMultiplier,
        totalVolumeCups: getTotalVolumeCups(),
        adjustedIngredients,
        blendedNutrition: getBlendedNutrition(),
        blendedMilkInfo: getBlendedMilkInfo()
      }
    });
    document.dispatchEvent(event);
  }

  // Public API
  return {
    loadData,
    isCheeseRecipe,
    detectOriginalMilkType,
    getAdjustedIngredients,
    getMilkTypeInfo,
    getFlavorExpectations,
    getCurdHandlingNotes,
    renderMilkSwitcher,
    getVolumeConversionFactor,
    getRennetFactor,
    getCaCl2Recommendation,
    getMilkRatios,
    setMilkRatio,
    setSingleMilk,
    isMixedMode,
    isVolumeMode,
    enterVolumeMode,
    getMilkVolumes,
    setMilkVolume,
    setMilkVolumes,
    getTotalVolumeCups,
    getTotalVolume,
    convertToCups,
    convertFromCups,
    getBlendedMilkInfo,
    getBlendedNutrition,
    isAvailableMilkType,
    isExoticMilkType,
    getRecommendedSubstitute,
    getSubstituteNotes
  };
})();

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MilkSubstitution;
}
