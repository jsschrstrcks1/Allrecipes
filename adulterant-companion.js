/**
 * Adulterant Companion for Cheese Recipes
 *
 * Provides herb, spice, and adulterant guidance for cheese-making recipes.
 * Integrates with MilkSubstitution module for milk-type-aware adjustments.
 * Loads data from data/adulterants.json.
 */

// =============================================================================
// Adulterant Companion Module
// =============================================================================

const AdulterantCompanion = (function() {
  'use strict';

  // Module state
  let adulterantData = null;
  let isLoaded = false;
  let selectedAdulterants = []; // Array of {id, stage, quantity, unit}
  let currentRecipe = null;
  let currentMilkType = 'cow';

  // =============================================================================
  // Data Loading
  // =============================================================================

  /**
   * Load adulterant data from JSON file
   */
  async function loadData() {
    if (isLoaded && adulterantData) {
      return adulterantData;
    }

    try {
      const response = await fetch('data/adulterants.json');
      if (!response.ok) {
        console.warn('Adulterant data not available');
        return null;
      }
      adulterantData = await response.json();
      isLoaded = true;
      console.log('Adulterant companion data loaded:', adulterantData.meta.total_adulterants, 'adulterants');
      return adulterantData;
    } catch (error) {
      console.error('Failed to load adulterant data:', error);
      return null;
    }
  }

  /**
   * Get all adulterants
   */
  function getAllAdulterants() {
    return adulterantData?.adulterants || [];
  }

  /**
   * Get adulterant by ID
   */
  function getAdulterant(id) {
    return getAllAdulterants().find(a => a.id === id);
  }

  /**
   * Get adulterants by category
   */
  function getByCategory(categoryId) {
    return getAllAdulterants().filter(a => a.category === categoryId);
  }

  /**
   * Get all categories
   */
  function getCategories() {
    return adulterantData?.categories || [];
  }

  /**
   * Get prohibited adulterants
   */
  function getProhibited() {
    return adulterantData?.prohibited_adulterants || [];
  }

  /**
   * Get stage guidelines
   */
  function getStageGuidelines(stage) {
    return adulterantData?.stage_guidelines?.[stage] || null;
  }

  // =============================================================================
  // Compatibility & Filtering
  // =============================================================================

  /**
   * Detect cheese style from recipe
   */
  function detectCheeseStyle(recipe) {
    if (!recipe) return 'semi-hard'; // Default

    const title = (recipe.title || '').toLowerCase();
    const tags = (recipe.tags || []).map(t => t.toLowerCase());
    const category = (recipe.category || '').toLowerCase();

    // Check for style indicators
    if (tags.includes('fresh-cheese') || title.includes('ricotta') ||
        title.includes('queso fresco') || title.includes('paneer') ||
        title.includes('cottage')) {
      return 'fresh';
    }
    if (tags.includes('soft-cheese') || title.includes('brie') ||
        title.includes('camembert')) {
      return 'soft';
    }
    if (tags.includes('bloomy') || title.includes('bloomy')) {
      return 'bloomy';
    }
    if (tags.includes('blue') || title.includes('blue') ||
        title.includes('roquefort') || title.includes('gorgonzola')) {
      return 'blue';
    }
    if (tags.includes('washed-rind') || title.includes('washed')) {
      return 'washed-rind';
    }
    if (tags.includes('hard-cheese') || title.includes('parmesan') ||
        title.includes('cheddar') || title.includes('gouda')) {
      return 'hard';
    }
    if (title.includes('mozzarella') || title.includes('provolone')) {
      return 'pasta-filata';
    }
    if (title.includes('feta') || title.includes('halloumi')) {
      return 'brined';
    }

    return 'semi-hard'; // Safe default
  }

  /**
   * Get adulterants compatible with a cheese style
   */
  function getCompatibleAdulterants(cheeseStyle) {
    return getAllAdulterants().filter(a =>
      a.compatible_styles.includes(cheeseStyle)
    );
  }

  /**
   * Get adulterants compatible with current recipe
   */
  function getCompatibleForRecipe(recipe) {
    const style = detectCheeseStyle(recipe);
    return getCompatibleAdulterants(style);
  }

  /**
   * Check if an adulterant is compatible with a cheese style
   */
  function isCompatible(adulterantId, cheeseStyle) {
    const adulterant = getAdulterant(adulterantId);
    if (!adulterant) return false;
    return adulterant.compatible_styles.includes(cheeseStyle);
  }

  /**
   * Check if an adulterant is incompatible with a cheese style
   */
  function isIncompatible(adulterantId, cheeseStyle) {
    const adulterant = getAdulterant(adulterantId);
    if (!adulterant) return false;
    return adulterant.incompatible_styles.includes(cheeseStyle);
  }

  // =============================================================================
  // Quantity Calculations
  // =============================================================================

  /**
   * Get milk type adjustment factor for an adulterant
   */
  function getMilkAdjustment(adulterantId, milkType) {
    const adulterant = getAdulterant(adulterantId);
    if (!adulterant || !adulterant.milk_adjustments) return 1.0;
    return adulterant.milk_adjustments[milkType] || 1.0;
  }

  /**
   * Calculate adjusted quantity for milk type and recipe scale
   */
  function calculateAdjustedQuantity(adulterantId, milkType, milkGallons = 1) {
    const adulterant = getAdulterant(adulterantId);
    if (!adulterant) return null;

    const baseQty = adulterant.base_quantity;
    const milkFactor = getMilkAdjustment(adulterantId, milkType);

    // Calculate: base amount * milk factor * scale factor
    const adjustedAmount = baseQty.amount * milkFactor * milkGallons;

    return {
      amount: adjustedAmount,
      unit: baseQty.unit,
      per: `${milkGallons} gallon${milkGallons !== 1 ? 's' : ''}`,
      milkType: milkType,
      adjustmentFactor: milkFactor
    };
  }

  /**
   * Format quantity for display
   */
  function formatQuantity(amount, unit) {
    // Handle fractions
    if (amount < 1) {
      const fractions = {
        0.125: '1/8',
        0.25: '1/4',
        0.333: '1/3',
        0.375: '3/8',
        0.5: '1/2',
        0.625: '5/8',
        0.666: '2/3',
        0.75: '3/4',
        0.875: '7/8'
      };

      // Find closest fraction
      let closest = amount;
      let minDiff = 1;
      for (const [val, frac] of Object.entries(fractions)) {
        const diff = Math.abs(parseFloat(val) - amount);
        if (diff < minDiff) {
          minDiff = diff;
          closest = frac;
        }
      }

      if (typeof closest === 'string') {
        return `${closest} ${unit}`;
      }
    }

    // Handle mixed numbers
    if (amount > 1 && amount % 1 !== 0) {
      const whole = Math.floor(amount);
      const frac = amount - whole;
      const fracStr = formatQuantity(frac, '').trim();
      return `${whole} ${fracStr} ${unit}`.trim();
    }

    // Round to reasonable precision
    const rounded = Math.round(amount * 100) / 100;
    return `${rounded} ${unit}`;
  }

  // =============================================================================
  // Warnings System
  // =============================================================================

  /**
   * Get warnings for an adulterant selection
   */
  function getWarnings(adulterantId, quantity, unit, cheeseStyle) {
    const adulterant = getAdulterant(adulterantId);
    if (!adulterant) return [];

    const warnings = [];

    // Check quantity exceeded
    if (adulterant.max_safe_quantity) {
      const max = adulterant.max_safe_quantity;
      if (unit === max.unit && quantity > max.amount) {
        warnings.push({
          type: 'QUANTITY_EXCEEDED',
          level: 'warning',
          message: adulterant.warnings.exceeded_message
        });
      }
    }

    // Check style compatibility
    if (adulterant.incompatible_styles.includes(cheeseStyle)) {
      const styleWarning = adulterant.warnings?.style_warnings?.[cheeseStyle];
      warnings.push({
        type: 'INCOMPATIBLE_STYLE',
        level: styleWarning?.includes('PROHIBITED') ? 'danger' : 'caution',
        message: styleWarning || `${adulterant.name} is not recommended for ${cheeseStyle} cheese`
      });
    }

    // Check general warnings
    if (adulterant.warnings?.general) {
      warnings.push({
        type: 'GENERAL',
        level: 'info',
        message: adulterant.warnings.general
      });
    }

    return warnings;
  }

  /**
   * Get all warnings for current selections
   */
  function getAllWarnings(cheeseStyle) {
    const allWarnings = [];

    for (const selection of selectedAdulterants) {
      const warnings = getWarnings(selection.id, selection.quantity, selection.unit, cheeseStyle);
      allWarnings.push(...warnings.map(w => ({
        ...w,
        adulterantId: selection.id,
        adulterantName: getAdulterant(selection.id)?.name
      })));
    }

    // Check interactions between selected adulterants
    const interactionWarnings = checkInteractions();
    allWarnings.push(...interactionWarnings);

    return allWarnings;
  }

  /**
   * Check for interactions between selected adulterants
   */
  function checkInteractions() {
    const warnings = [];
    const selectedIds = selectedAdulterants.map(s => s.id);

    for (const selection of selectedAdulterants) {
      const adulterant = getAdulterant(selection.id);
      if (!adulterant?.interactions) continue;

      for (const interaction of adulterant.interactions) {
        if (selectedIds.includes(interaction.with)) {
          const other = getAdulterant(interaction.with);
          if (interaction.effect === 'problematic') {
            warnings.push({
              type: 'INTERACTION',
              level: 'warning',
              message: `${adulterant.name} + ${other?.name}: ${interaction.reason || interaction.note}`,
              adulterantId: selection.id
            });
          } else if (interaction.effect === 'complementary') {
            warnings.push({
              type: 'INTERACTION',
              level: 'info',
              message: `${adulterant.name} + ${other?.name}: ${interaction.note || 'Complementary pairing'}`,
              adulterantId: selection.id
            });
          }
        }
      }
    }

    return warnings;
  }

  // =============================================================================
  // Selection Management
  // =============================================================================

  /**
   * Add an adulterant to selection
   */
  function addAdulterant(id, stage, quantity, unit) {
    const adulterant = getAdulterant(id);
    if (!adulterant) {
      console.error('Unknown adulterant:', id);
      return false;
    }

    // Check if stage is allowed
    if (!adulterant.allowed_stages.includes(stage)) {
      console.warn(`Stage ${stage} not allowed for ${adulterant.name}`);
    }

    selectedAdulterants.push({
      id,
      stage,
      quantity,
      unit: unit || adulterant.base_quantity.unit
    });

    dispatchChangeEvent();
    return true;
  }

  /**
   * Remove an adulterant from selection
   */
  function removeAdulterant(index) {
    if (index >= 0 && index < selectedAdulterants.length) {
      selectedAdulterants.splice(index, 1);
      dispatchChangeEvent();
      return true;
    }
    return false;
  }

  /**
   * Update adulterant quantity
   */
  function updateQuantity(index, quantity) {
    if (index >= 0 && index < selectedAdulterants.length) {
      selectedAdulterants[index].quantity = quantity;
      dispatchChangeEvent();
      return true;
    }
    return false;
  }

  /**
   * Clear all selections
   */
  function clearSelections() {
    selectedAdulterants = [];
    dispatchChangeEvent();
  }

  /**
   * Get current selections
   */
  function getSelections() {
    return [...selectedAdulterants];
  }

  // =============================================================================
  // Recipe Injection
  // =============================================================================

  /**
   * Generate injection steps for selected adulterants
   */
  function generateInjectionSteps(recipe) {
    const steps = [];

    for (const selection of selectedAdulterants) {
      const adulterant = getAdulterant(selection.id);
      if (!adulterant) continue;

      const template = adulterant.injection_templates?.[selection.stage];
      if (!template) continue;

      const formattedQty = formatQuantity(selection.quantity, selection.unit);
      const instruction = template
        .replace('{quantity}', formattedQty)
        .replace('{name}', adulterant.name);

      steps.push({
        adulterantId: selection.id,
        adulterantName: adulterant.name,
        stage: selection.stage,
        quantity: formattedQty,
        instruction: instruction,
        stageOrder: getStageOrder(selection.stage)
      });
    }

    // Sort by stage order
    steps.sort((a, b) => a.stageOrder - b.stageOrder);

    return steps;
  }

  /**
   * Get numeric order for stages
   */
  function getStageOrder(stage) {
    const order = {
      'COLD_INFUSE': 1,
      'MILK_PREHEAT': 2,
      'PRE_RENNET': 3,
      'CURD_CUT': 4,
      'CURD_MILL': 5,
      'MOLD_LAYER': 6,
      'POST_PRESS': 7,
      'BRINE_ADDITION': 8,
      'RIND_RUB': 9,
      'AGING_SURFACE': 10,
      'FINISH_SERVING': 11
    };
    return order[stage] || 99;
  }

  /**
   * Get stage display name
   */
  function getStageDisplayName(stage) {
    const names = {
      'COLD_INFUSE': 'Cold Infusion (Before Heating)',
      'MILK_PREHEAT': 'During Milk Heating',
      'PRE_RENNET': 'Before Adding Rennet',
      'CURD_CUT': 'After Cutting Curds',
      'CURD_MILL': 'During Curd Milling',
      'MOLD_LAYER': 'Layering in Molds',
      'POST_PRESS': 'After Pressing',
      'BRINE_ADDITION': 'In Brine Solution',
      'RIND_RUB': 'Rind Wash/Rub',
      'AGING_SURFACE': 'During Aging',
      'FINISH_SERVING': 'Before Serving'
    };
    return names[stage] || stage;
  }

  // =============================================================================
  // Event Handling
  // =============================================================================

  /**
   * Dispatch change event
   */
  function dispatchChangeEvent() {
    const cheeseStyle = detectCheeseStyle(currentRecipe);
    const event = new CustomEvent('adulterantSelectionChanged', {
      detail: {
        selections: getSelections(),
        injectionSteps: generateInjectionSteps(currentRecipe),
        warnings: getAllWarnings(cheeseStyle),
        cheeseStyle: cheeseStyle,
        milkType: currentMilkType
      }
    });
    document.dispatchEvent(event);
  }

  /**
   * Set current recipe context
   */
  function setRecipe(recipe) {
    currentRecipe = recipe;
  }

  /**
   * Set current milk type (integrates with MilkSubstitution)
   */
  function setMilkType(milkType) {
    currentMilkType = milkType;
    dispatchChangeEvent();
  }

  // =============================================================================
  // Integration with MilkSubstitution
  // =============================================================================

  /**
   * Listen for milk substitution changes
   */
  function initMilkIntegration() {
    document.addEventListener('milkSubstitutionChanged', (e) => {
      if (e.detail && e.detail.milkRatios) {
        // Determine dominant milk type from ratios
        const ratios = e.detail.milkRatios;
        let dominant = 'cow';
        let maxRatio = 0;

        for (const [type, ratio] of Object.entries(ratios)) {
          if (ratio > maxRatio) {
            maxRatio = ratio;
            dominant = type;
          }
        }

        setMilkType(dominant);
      }
    });
  }

  // =============================================================================
  // UI Rendering
  // =============================================================================

  /**
   * Render adulterant selection panel
   */
  function renderPanel(recipe, containerId) {
    const container = document.getElementById(containerId);
    if (!container || !adulterantData) return;

    currentRecipe = recipe;
    const cheeseStyle = detectCheeseStyle(recipe);
    const compatible = getCompatibleForRecipe(recipe);

    const html = `
      <div class="adulterant-companion-panel">
        <div class="adulterant-header">
          <h3>🧂 Herb & Spice Companion</h3>
          <p class="adulterant-subtitle">Cheese Style: <strong>${cheeseStyle}</strong></p>
        </div>

        <div class="adulterant-categories">
          ${getCategories().map(cat => {
            const catAdulterants = getByCategory(cat.id).filter(a =>
              a.compatible_styles.includes(cheeseStyle)
            );
            if (catAdulterants.length === 0) return '';

            return `
              <details class="adulterant-category">
                <summary>${cat.icon} ${cat.name} (${catAdulterants.length})</summary>
                <div class="adulterant-list">
                  ${catAdulterants.map(a => `
                    <div class="adulterant-item" data-id="${a.id}">
                      <div class="adulterant-info">
                        <span class="adulterant-name">${a.name}</span>
                        <span class="adulterant-intensity intensity-${a.intensity}">${a.intensity}</span>
                      </div>
                      <div class="adulterant-flavor">${a.flavor_profile.join(', ')}</div>
                      <button class="btn-add-adulterant" data-id="${a.id}">+ Add</button>
                    </div>
                  `).join('')}
                </div>
              </details>
            `;
          }).join('')}
        </div>

        <div class="adulterant-selections">
          <h4>Selected Additions</h4>
          <div id="adulterant-selection-list">
            ${selectedAdulterants.length === 0 ?
              '<p class="no-selections">No additions selected</p>' :
              renderSelectionList()}
          </div>
        </div>

        <div class="adulterant-warnings" id="adulterant-warnings">
          ${renderWarnings(cheeseStyle)}
        </div>

        <div class="adulterant-injection-preview" id="adulterant-injection-preview">
          ${renderInjectionPreview(recipe)}
        </div>
      </div>
    `;

    container.innerHTML = html;
    attachEventListeners(container);
  }

  /**
   * Render selection list
   */
  function renderSelectionList() {
    return selectedAdulterants.map((sel, index) => {
      const adulterant = getAdulterant(sel.id);
      return `
        <div class="selection-item">
          <span class="selection-name">${adulterant?.name}</span>
          <input type="number" class="selection-qty"
                 value="${sel.quantity}"
                 step="0.125" min="0"
                 data-index="${index}">
          <span class="selection-unit">${sel.unit}</span>
          <select class="selection-stage" data-index="${index}">
            ${adulterant?.allowed_stages.map(s =>
              `<option value="${s}" ${s === sel.stage ? 'selected' : ''}>${getStageDisplayName(s)}</option>`
            ).join('')}
          </select>
          <button class="btn-remove-selection" data-index="${index}">×</button>
        </div>
      `;
    }).join('');
  }

  /**
   * Render warnings
   */
  function renderWarnings(cheeseStyle) {
    const warnings = getAllWarnings(cheeseStyle);
    if (warnings.length === 0) return '';

    return `
      <h4>⚠️ Notes & Warnings</h4>
      <ul class="warning-list">
        ${warnings.map(w => `
          <li class="warning-item warning-${w.level}">
            <span class="warning-type">${w.type}</span>
            ${w.message}
          </li>
        `).join('')}
      </ul>
    `;
  }

  /**
   * Render injection preview
   */
  function renderInjectionPreview(recipe) {
    const steps = generateInjectionSteps(recipe);
    if (steps.length === 0) return '';

    return `
      <h4>📝 Recipe Additions</h4>
      <ol class="injection-steps">
        ${steps.map(s => `
          <li class="injection-step">
            <span class="injection-stage">${getStageDisplayName(s.stage)}:</span>
            ${s.instruction}
          </li>
        `).join('')}
      </ol>
    `;
  }

  /**
   * Attach event listeners
   */
  function attachEventListeners(container) {
    // Add buttons
    container.querySelectorAll('.btn-add-adulterant').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.target.dataset.id;
        const adulterant = getAdulterant(id);
        if (adulterant) {
          const adjusted = calculateAdjustedQuantity(id, currentMilkType, 1);
          addAdulterant(id, adulterant.best_stages[0], adjusted.amount, adjusted.unit);
          updatePanelUI(container);
        }
      });
    });

    // Remove buttons
    container.querySelectorAll('.btn-remove-selection').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const index = parseInt(e.target.dataset.index);
        removeAdulterant(index);
        updatePanelUI(container);
      });
    });

    // Quantity inputs
    container.querySelectorAll('.selection-qty').forEach(input => {
      input.addEventListener('change', (e) => {
        const index = parseInt(e.target.dataset.index);
        const value = parseFloat(e.target.value);
        updateQuantity(index, value);
        updatePanelUI(container);
      });
    });

    // Stage selects
    container.querySelectorAll('.selection-stage').forEach(select => {
      select.addEventListener('change', (e) => {
        const index = parseInt(e.target.dataset.index);
        selectedAdulterants[index].stage = e.target.value;
        dispatchChangeEvent();
        updatePanelUI(container);
      });
    });
  }

  /**
   * Update panel UI after changes
   */
  function updatePanelUI(container) {
    const cheeseStyle = detectCheeseStyle(currentRecipe);

    const selectionList = container.querySelector('#adulterant-selection-list');
    if (selectionList) {
      selectionList.innerHTML = selectedAdulterants.length === 0 ?
        '<p class="no-selections">No additions selected</p>' :
        renderSelectionList();
    }

    const warningsDiv = container.querySelector('#adulterant-warnings');
    if (warningsDiv) {
      warningsDiv.innerHTML = renderWarnings(cheeseStyle);
    }

    const previewDiv = container.querySelector('#adulterant-injection-preview');
    if (previewDiv) {
      previewDiv.innerHTML = renderInjectionPreview(currentRecipe);
    }

    // Re-attach event listeners for new elements
    attachEventListeners(container);
  }

  // =============================================================================
  // Public API
  // =============================================================================

  return {
    // Data loading
    loadData,

    // Data access
    getAllAdulterants,
    getAdulterant,
    getByCategory,
    getCategories,
    getProhibited,
    getStageGuidelines,

    // Compatibility
    detectCheeseStyle,
    getCompatibleAdulterants,
    getCompatibleForRecipe,
    isCompatible,
    isIncompatible,

    // Calculations
    getMilkAdjustment,
    calculateAdjustedQuantity,
    formatQuantity,

    // Warnings
    getWarnings,
    getAllWarnings,
    checkInteractions,

    // Selection management
    addAdulterant,
    removeAdulterant,
    updateQuantity,
    clearSelections,
    getSelections,

    // Recipe integration
    generateInjectionSteps,
    getStageOrder,
    getStageDisplayName,

    // Context
    setRecipe,
    setMilkType,

    // Integration
    initMilkIntegration,

    // UI
    renderPanel
  };
})();

// Auto-initialize milk integration when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  AdulterantCompanion.initMilkIntegration();
});
