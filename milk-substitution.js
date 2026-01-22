/**
 * Milk Substitution Calculator for Cheese Recipes
 *
 * Provides interactive milk type switching and ingredient adjustment
 * for cheese-making recipes. Loads data from data/milk-substitution.json.
 */

// =============================================================================
// Milk Substitution Module
// =============================================================================

const MilkSubstitution = (function() {
  'use strict';

  // Module state
  let substitutionData = null;
  let isLoaded = false;
  let currentMilkType = 'cow';
  let originalMilkType = 'cow';
  let quantityMultiplier = 1.0;

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

  /**
   * Detect the original milk type from recipe ingredients
   */
  function detectOriginalMilkType(recipe) {
    if (!recipe || !recipe.ingredients) return 'cow';

    for (const ing of recipe.ingredients) {
      const item = ing.item.toLowerCase();
      if (item.includes('sheep') || item.includes("sheep's") || item.includes('ewe')) {
        return 'sheep';
      }
      if (item.includes('goat') || item.includes("goat's")) {
        return 'goat';
      }
    }

    // Default to cow if no specific type mentioned
    return 'cow';
  }

  /**
   * Get volume conversion factor
   */
  function getVolumeConversionFactor(fromMilk, toMilk) {
    if (!substitutionData || fromMilk === toMilk) return 1.0;

    const key = `${fromMilk}_to_${toMilk}`;
    return substitutionData.volume_conversions?.factors?.[key] || 1.0;
  }

  /**
   * Get rennet adjustment factor
   */
  function getRennetFactor(milkType) {
    if (!substitutionData) return 1.0;
    return substitutionData.rennet_adjustments?.factors?.[milkType] || 1.0;
  }

  /**
   * Get CaCl2 recommendation
   */
  function getCaCl2Recommendation(milkType, isRaw = false) {
    if (!substitutionData) return null;

    const processing = isRaw ? 'raw' : 'pasteurized';
    return substitutionData.calcium_chloride_guidelines?.recommendations?.[milkType]?.[processing];
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
   * Adjust an ingredient based on milk substitution
   */
  function adjustIngredient(ingredient, fromMilk, toMilk, qtyMultiplier = 1.0) {
    const item = ingredient.item.toLowerCase();
    const adjusted = { ...ingredient };

    // Check if this is a milk ingredient
    const isMilk = MILK_KEYWORDS.some(kw => item.includes(kw));
    if (isMilk) {
      const volumeFactor = getVolumeConversionFactor(fromMilk, toMilk);
      const originalQty = parseQuantity(ingredient.quantity);
      if (originalQty !== null) {
        const newQty = originalQty * volumeFactor * qtyMultiplier;
        adjusted.quantity = formatQuantity(newQty);
      }
      // Update item name to reflect milk type
      adjusted.item = ingredient.item.replace(/cow('s)?|goat('s)?|sheep('s)?/gi, '')
        .replace(/milk/i, `${toMilk} milk`);
      adjusted._adjusted = true;
      adjusted._adjustmentNote = `Volume adjusted for ${toMilk} milk`;
      return adjusted;
    }

    // Check if this is rennet
    const isRennet = RENNET_KEYWORDS.some(kw => item.includes(kw));
    if (isRennet) {
      const fromRennetFactor = getRennetFactor(fromMilk);
      const toRennetFactor = getRennetFactor(toMilk);
      const rennetRatio = toRennetFactor / fromRennetFactor;

      const originalQty = parseQuantity(ingredient.quantity);
      if (originalQty !== null) {
        const newQty = originalQty * rennetRatio * qtyMultiplier;
        adjusted.quantity = formatQuantity(newQty);
      }
      adjusted._adjusted = true;
      adjusted._adjustmentNote = `Rennet adjusted for ${toMilk} milk (${Math.round(rennetRatio * 100)}% of original)`;
      return adjusted;
    }

    // Check if this is CaCl2
    const isCaCl2 = CACL2_KEYWORDS.some(kw => item.includes(kw));
    if (isCaCl2) {
      if (toMilk === 'sheep') {
        adjusted.quantity = '0';
        adjusted._adjusted = true;
        adjusted._adjustmentNote = 'CaCl2 not needed for sheep milk (high natural calcium)';
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
  function getAdjustedIngredients(recipe, toMilk, qtyMultiplier = 1.0) {
    if (!recipe || !recipe.ingredients) return [];

    const fromMilk = detectOriginalMilkType(recipe);

    return recipe.ingredients.map(ing =>
      adjustIngredient(ing, fromMilk, toMilk, qtyMultiplier)
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
   * Render the milk substitution UI
   */
  function renderMilkSwitcher(recipe, containerId) {
    const container = document.getElementById(containerId);
    if (!container || !substitutionData) return;

    const detectedMilk = detectOriginalMilkType(recipe);
    originalMilkType = detectedMilk;
    currentMilkType = detectedMilk;

    const milkTypes = Object.keys(substitutionData.milk_types);

    const html = `
      <div class="milk-substitution-panel">
        <h3>Milk Substitution Calculator</h3>
        <p class="milk-sub-intro">Adjust this cheese recipe for different milk types.</p>

        <div class="milk-sub-controls">
          <div class="milk-sub-row">
            <label for="milk-type-select">Milk Type:</label>
            <select id="milk-type-select" class="milk-type-select">
              ${milkTypes.map(type => {
                const info = substitutionData.milk_types[type];
                const selected = type === detectedMilk ? 'selected' : '';
                return `<option value="${type}" ${selected}>${info.name}</option>`;
              }).join('')}
            </select>
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
          ${renderMilkInfo(detectedMilk)}
        </div>

        <div id="milk-sub-warnings" class="milk-sub-warnings"></div>
      </div>
    `;

    container.innerHTML = html;

    // Attach event listeners
    const milkSelect = document.getElementById('milk-type-select');
    const qtySelect = document.getElementById('quantity-multiplier');

    if (milkSelect) {
      milkSelect.addEventListener('change', (e) => {
        currentMilkType = e.target.value;
        updateMilkSubstitution(recipe);
      });
    }

    if (qtySelect) {
      qtySelect.addEventListener('change', (e) => {
        quantityMultiplier = parseFloat(e.target.value);
        updateMilkSubstitution(recipe);
      });
    }
  }

  /**
   * Render milk type info panel
   */
  function renderMilkInfo(milkType) {
    const info = getMilkTypeInfo(milkType);
    const flavor = getFlavorExpectations(milkType);
    const curd = getCurdHandlingNotes(milkType);

    if (!info) return '';

    return `
      <div class="milk-info-grid">
        <div class="milk-info-item">
          <span class="milk-info-label">Fat Content</span>
          <span class="milk-info-value">${info.fat_percent}%</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Protein</span>
          <span class="milk-info-value">${info.protein_percent}%</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Yield/Gallon</span>
          <span class="milk-info-value">~${info.cheese_yield_per_gallon_lb} lb</span>
        </div>
        <div class="milk-info-item">
          <span class="milk-info-label">Coagulation</span>
          <span class="milk-info-value">${info.coagulation_speed}</span>
        </div>
      </div>

      <div class="milk-flavor-notes">
        <strong>Flavor Profile:</strong> ${info.flavor_profile.join(', ')}
      </div>

      <div class="milk-texture-notes">
        <strong>Texture:</strong> ${info.texture_notes}
      </div>

      ${curd ? `
        <div class="milk-curd-notes">
          <strong>Curd Handling:</strong> ${curd.notes}
        </div>
      ` : ''}
    `;
  }

  /**
   * Update the recipe display with substituted ingredients
   */
  function updateMilkSubstitution(recipe) {
    // Update info panel
    const infoPanel = document.getElementById('milk-sub-info');
    if (infoPanel) {
      infoPanel.innerHTML = renderMilkInfo(currentMilkType);
    }

    // Update warnings
    const warningsPanel = document.getElementById('milk-sub-warnings');
    if (warningsPanel && currentMilkType !== originalMilkType) {
      warningsPanel.innerHTML = `
        <div class="milk-sub-warning">
          <strong>Note:</strong> Substituting ${substitutionData.milk_types[originalMilkType].name}
          with ${substitutionData.milk_types[currentMilkType].name} will affect flavor and texture.
        </div>
      `;
    } else if (warningsPanel) {
      warningsPanel.innerHTML = '';
    }

    // Update ingredients list
    const adjustedIngredients = getAdjustedIngredients(recipe, currentMilkType, quantityMultiplier);

    // Dispatch custom event for the main script to handle
    const event = new CustomEvent('milkSubstitutionChanged', {
      detail: {
        originalMilkType,
        currentMilkType,
        quantityMultiplier,
        adjustedIngredients
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
    getCaCl2Recommendation
  };
})();

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MilkSubstitution;
}
