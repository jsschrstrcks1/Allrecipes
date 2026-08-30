/**
 * Other Family Recipes - Client-side JavaScript
 * Handles recipe loading, search, filtering, and navigation
 */

// =============================================================================
// Security Utilities - XSS Prevention
// =============================================================================

/**
 * Escape HTML special characters to prevent XSS attacks.
 * Always use this when inserting dynamic content into innerHTML.
 * @param {*} text - The text to escape (will be converted to string)
 * @returns {string} - HTML-escaped string safe for innerHTML
 */
function escapeHtml(text) {
  if (text === null || text === undefined) return '';
  const div = document.createElement('div');
  div.textContent = String(text);
  return div.innerHTML;
}

/**
 * Sanitize URLs to prevent javascript: and data: XSS attacks.
 * Only allows relative paths, http://, and https:// URLs.
 * @param {string} url - The URL to sanitize
 * @returns {string} - Sanitized URL or '#' if unsafe
 */
function sanitizeUrl(url) {
  if (!url) return '#';
  const trimmed = String(url).trim();
  // Allow relative paths and http(s) URLs only
  if (trimmed.startsWith('/') ||
      trimmed.startsWith('./') ||
      trimmed.startsWith('../') ||
      trimmed.startsWith('http://') ||
      trimmed.startsWith('https://')) {
    return trimmed;
  }
  // Allow simple filenames and paths (no protocol)
  if (/^[a-zA-Z0-9_\-./]+$/.test(trimmed) && !trimmed.includes(':')) {
    return trimmed;
  }
  return '#';
}

/**
 * Escape a value for use in an HTML attribute.
 * @param {*} value - The value to escape
 * @returns {string} - Escaped string safe for attribute values
 */
function escapeAttr(value) {
  if (value === null || value === undefined) return '';
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

// =============================================================================
// Application Code
// =============================================================================

// Global state
let recipes = [];          // Index data (minimal metadata for all recipes)
let recipesFull = {};      // Full recipe data cache, keyed by id
let loadedShards = {};     // Cache of loaded shard data, keyed by category
let shardManifest = [];    // List of available shards
let tips = [];
let categories = new Set();
let allTags = new Set();
let tipCategories = new Set();
let currentFilter = { search: '', category: '', tag: '', collection: '' };
let showMetric = false; // Toggle for metric conversions
let milkSubstitutionEnabled = false; // Track if milk substitution is active
let currentRecipeForMilkSub = null; // Track current recipe for milk substitution

// DOM Ready - Auth is handled by inline script in HTML
document.addEventListener('DOMContentLoaded', init);

async function init() {
  // Load content directly - auth gate is handled by inline script in HTML
  await loadContent();
}

/**
 * Load all content
 */
async function loadContent() {
  await Promise.all([loadRecipes(), loadTips(), loadMilkSubstitutionData()]);
  setupEventListeners();
  setupMilkSubstitutionListener();
  await handleRouting();
}

/**
 * Load milk substitution data
 */
async function loadMilkSubstitutionData() {
  if (typeof MilkSubstitution !== 'undefined') {
    await MilkSubstitution.loadData();
    console.log('Milk substitution module initialized');
  }
}

/**
 * Setup listener for milk substitution changes
 */
function setupMilkSubstitutionListener() {
  document.addEventListener('milkSubstitutionChanged', (e) => {
    if (currentRecipeForMilkSub) {
      updateIngredientsWithSubstitution(e.detail);
    }
  });
}

/**
 * Update ingredients display with milk substitution
 */
function updateIngredientsWithSubstitution(detail) {
  const ingredientsList = document.querySelector('.ingredients-list');
  if (!ingredientsList || !detail.adjustedIngredients) return;

  let html = '';
  detail.adjustedIngredients.forEach(ing => {
    const adjustedClass = ing._adjusted ? 'ingredient-adjusted' : '';
    const omittedClass = ing._omit ? 'ingredient-omitted' : '';

    html += `
      <li class="${adjustedClass} ${omittedClass}">
        <span class="ingredient-quantity">${escapeHtml(ing.quantity)} ${escapeHtml(ing.unit)}</span>
        <span class="ingredient-item">
          ${escapeHtml(ing.item)}
          ${ing.prep_note ? `<span class="ingredient-prep">, ${escapeHtml(ing.prep_note)}</span>` : ''}
        </span>
      </li>
    `;
  });

  ingredientsList.innerHTML = html;
}

/**
 * Load recipe index (sharded architecture)
 * Loads minimal metadata for all recipes, full data loaded on demand
 */
async function loadRecipes() {
  try {
    // Try sharded index first, fall back to monolithic file
    let response = await fetch('data/recipes-index.json');
    if (!response.ok) {
      // Fallback to old monolithic file
      response = await fetch('data/recipes.json');
      const data = await response.json();
      recipes = data.recipes || [];
      // Populate full cache from monolithic file
      recipes.forEach(r => { recipesFull[r.id] = r; });
      console.log(`Loaded ${recipes.length} recipes (monolithic)`);
    } else {
      const data = await response.json();
      recipes = data.recipes || [];
      shardManifest = data.shards || [];
      console.log(`Loaded index with ${recipes.length} recipes (${shardManifest.length} shards available)`);
    }

    // Extract categories and tags from index
    recipes.forEach(recipe => {
      if (recipe.category) categories.add(recipe.category);
      if (recipe.tags) recipe.tags.forEach(tag => allTags.add(tag));
    });

  } catch (error) {
    console.error('Failed to load recipes:', error);
    showError('Unable to load recipes. Please refresh the page.');
  }
}

/**
 * Load a category shard (full recipe data for a category)
 * @param {string} category - The category to load
 * @returns {Promise<Array>} - Array of full recipe objects
 */
async function loadShard(category) {
  if (loadedShards[category]) {
    return loadedShards[category];
  }

  try {
    const response = await fetch(`data/recipes-${category}.json`);
    if (!response.ok) {
      console.warn(`Shard not found for category: ${category}`);
      return [];
    }
    const data = await response.json();
    const shardRecipes = data.recipes || [];

    // Cache the shard and populate full recipe cache
    loadedShards[category] = shardRecipes;
    shardRecipes.forEach(r => { recipesFull[r.id] = r; });

    console.log(`Loaded shard: ${category} (${shardRecipes.length} recipes)`);
    return shardRecipes;
  } catch (error) {
    console.error(`Failed to load shard ${category}:`, error);
    return [];
  }
}

/**
 * Get full recipe data by ID (loads shard if needed)
 * @param {string} recipeId - The recipe ID
 * @returns {Promise<Object|null>} - Full recipe object or null
 */
async function getFullRecipe(recipeId) {
  // Check cache first
  if (recipesFull[recipeId]) {
    return recipesFull[recipeId];
  }

  // Find recipe in index to get category
  const indexEntry = recipes.find(r => r.id === recipeId);
  if (!indexEntry) {
    return null;
  }

  // Load the shard for this category
  await loadShard(indexEntry.category);

  return recipesFull[recipeId] || null;
}

/**
 * Load tips from JSON file
 */
async function loadTips() {
  try {
    const response = await fetch('data/tips_master.json');
    const data = await response.json();
    tips = data.tips || [];

    // Extract tip categories
    tips.forEach(tip => {
      if (tip.category) tipCategories.add(tip.category);
    });

    console.log(`Loaded ${tips.length} tips`);
  } catch (error) {
    console.error('Failed to load tips:', error);
    // Tips are optional - don't show error to user
  }
}

// =============================================================================
// Fuzzy Search Implementation
// =============================================================================

/**
 * Calculate Levenshtein distance between two strings
 * Used for fuzzy matching
 */
function levenshteinDistance(str1, str2) {
  const m = str1.length;
  const n = str2.length;
  const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (str1[i - 1] === str2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
      }
    }
  }
  return dp[m][n];
}

/**
 * Calculate fuzzy match score (0 to 1, higher is better)
 */
function fuzzyScore(query, text) {
  query = query.toLowerCase();
  text = text.toLowerCase();

  // Exact match
  if (text.includes(query)) return 1;

  // Word-level matching
  const queryWords = query.split(/\s+/);
  const textWords = text.split(/\s+/);

  let matchedWords = 0;
  for (const qWord of queryWords) {
    for (const tWord of textWords) {
      // Check for prefix match or close match
      if (tWord.startsWith(qWord) || qWord.startsWith(tWord)) {
        matchedWords++;
        break;
      }
      // Fuzzy match with tolerance
      const maxDist = Math.floor(Math.max(qWord.length, tWord.length) * 0.3);
      if (levenshteinDistance(qWord, tWord) <= maxDist) {
        matchedWords++;
        break;
      }
    }
  }

  return matchedWords / queryWords.length;
}

/**
 * Search tips with fuzzy matching
 * @param {string} query - Search query
 * @param {number} minScore - Minimum fuzzy score (0-1)
 * @returns {Array} - Matched tips with scores
 */
function searchTips(query, minScore = 0.5) {
  if (!query || query.length < 2) return [];

  const results = [];
  for (const tip of tips) {
    // Build searchable text from tip
    const searchText = [
      tip.title,
      tip.content,
      ...(tip.search_terms || []),
      ...(tip.related_tags || [])
    ].join(' ');

    const score = fuzzyScore(query, searchText);
    if (score >= minScore) {
      results.push({ tip, score });
    }
  }

  // Sort by score descending
  results.sort((a, b) => b.score - a.score);
  return results.map(r => r.tip);
}

/**
 * Find tips relevant to a recipe based on its ingredients
 * @param {Object} recipe - Recipe object
 * @returns {Array} - Related tips
 */
function findTipsForRecipe(recipe) {
  if (!recipe || !recipe.ingredients || tips.length === 0) return [];

  // Extract ingredient names from recipe
  const ingredientNames = recipe.ingredients.map(ing =>
    ing.item.toLowerCase().trim()
  );

  // Also include tags if present
  const recipeTags = (recipe.tags || []).map(t => t.toLowerCase());

  const matchedTips = [];
  const seenTips = new Set();

  for (const tip of tips) {
    if (seenTips.has(tip.id)) continue;

    // Check if any tip's related ingredients match recipe ingredients
    const tipIngredients = (tip.related_ingredients || []).map(i => i.toLowerCase());
    const tipTags = (tip.related_tags || []).map(t => t.toLowerCase());

    let isMatch = false;

    // Check ingredient matches
    for (const tipIng of tipIngredients) {
      for (const recipeIng of ingredientNames) {
        // Match if either contains the other (handles "banana" matching "bananas, mashed")
        if (recipeIng.includes(tipIng) || tipIng.includes(recipeIng.split(',')[0].trim())) {
          isMatch = true;
          break;
        }
      }
      if (isMatch) break;
    }

    // Also check tag matches
    if (!isMatch) {
      for (const tipTag of tipTags) {
        if (recipeTags.includes(tipTag)) {
          isMatch = true;
          break;
        }
      }
    }

    if (isMatch) {
      matchedTips.push(tip);
      seenTips.add(tip.id);
    }
  }

  return matchedTips;
}

/**
 * Update collection filter buttons with recipe counts
 */
function updateCollectionCounts() {
  const collectionFilters = document.getElementById('collection-filters');
  if (!collectionFilters) return;

  // Count recipes by collection (excluding reference collection from individual counts)
  const counts = {
    '': recipes.length, // All recipes
    'grandma': 0,
    'mommom': 0,
    'granny': 0
  };

  recipes.forEach(recipe => {
    const collection = recipe.collection || '';
    if (counts.hasOwnProperty(collection)) {
      counts[collection]++;
    }
  });

  // Update button labels
  const labels = {
    '': 'All',
    'grandma': 'Grandma Baker',
    'mommom': 'MomMom Baker',
    'granny': 'Granny Hudson'
  };

  collectionFilters.querySelectorAll('.collection-btn').forEach(btn => {
    const collection = btn.dataset.collection;
    const label = labels[collection] || collection;
    const count = counts[collection] || 0;
    btn.textContent = `${label} (${count})`;
  });
}

/**
 * Setup event listeners
 */
function setupEventListeners() {
  // Search form
  const searchForm = document.getElementById('search-form');
  if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const query = document.getElementById('search-input').value;
      currentFilter.search = query.toLowerCase();
      renderRecipeGrid();
    });
  }

  // Search input (live search)
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', debounce((e) => {
      currentFilter.search = e.target.value.toLowerCase();
      renderRecipeGrid();
    }, 300));
  }

  // Category filter
  const categorySelect = document.getElementById('category-filter');
  if (categorySelect) {
    categorySelect.addEventListener('change', (e) => {
      currentFilter.category = e.target.value;
      renderRecipeGrid();
    });
  }

  // Print button
  const printBtn = document.getElementById('print-btn');
  if (printBtn) {
    printBtn.addEventListener('click', () => window.print());
  }

  // Tags toggle (collapsible)
  const tagsToggle = document.getElementById('tags-toggle');
  const tagFilters = document.getElementById('tag-filters');
  if (tagsToggle && tagFilters) {
    tagsToggle.addEventListener('click', () => {
      const isExpanded = tagsToggle.getAttribute('aria-expanded') === 'true';
      tagsToggle.setAttribute('aria-expanded', !isExpanded);
      tagFilters.classList.toggle('collapsed', isExpanded);
    });
  }
}

/**
 * Handle client-side routing based on URL hash
 */
async function handleRouting() {
  const path = window.location.pathname;
  const hash = window.location.hash;

  if (path.includes('recipe.html') && hash) {
    const recipeId = hash.slice(1);
    await renderRecipeDetail(recipeId);
  } else if (path.includes('index.html') || path.endsWith('/')) {
    renderHomePage();
  }
}

/**
 * Render home page with recipe grid
 */
function renderHomePage() {
  renderCategoryFilter();
  renderTagFilters();
  renderRecipeGrid();
}

/**
 * Render category filter dropdown
 */
function renderCategoryFilter() {
  const select = document.getElementById('category-filter');
  if (!select) return;

  const sortedCategories = Array.from(categories).sort();
  let html = '<option value="">All Categories</option>';

  sortedCategories.forEach(cat => {
    html += `<option value="${escapeAttr(cat)}">${escapeHtml(capitalizeFirst(cat))}</option>`;
  });

  select.innerHTML = html;
}

/**
 * Render tag filter buttons
 */
function renderTagFilters() {
  const container = document.getElementById('tag-filters');
  if (!container) return;

  const sortedTags = Array.from(allTags).sort();
  let html = '';

  sortedTags.forEach(tag => {
    html += `<span class="filter-tag" data-tag="${escapeAttr(tag)}">${escapeHtml(tag)}</span>`;
  });

  container.innerHTML = html;

  // Add click handlers
  container.querySelectorAll('.filter-tag').forEach(el => {
    el.addEventListener('click', () => {
      const tag = el.dataset.tag;
      if (currentFilter.tag === tag) {
        currentFilter.tag = '';
        el.classList.remove('active');
      } else {
        container.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
        currentFilter.tag = tag;
        el.classList.add('active');
      }
      renderRecipeGrid();
    });
  });
}

/**
 * Render recipe grid with current filters
 */
function renderRecipeGrid() {
  const container = document.getElementById('recipe-grid');
  if (!container) return;

  // Filter recipes
  let filtered = recipes.filter(recipe => {
    // Exclude variants from main grid (show canonical only)
    if (recipe.variant_of && recipe.variant_of !== recipe.id) {
      return false;
    }

    // Search filter
    if (currentFilter.search) {
      const searchText = [
        recipe.title,
        recipe.description,
        recipe.attribution,
        ...recipe.tags || []
      ].join(' ').toLowerCase();

      if (!searchText.includes(currentFilter.search)) return false;
    }

    // Category filter
    if (currentFilter.category && recipe.category !== currentFilter.category) {
      return false;
    }

    // Tag filter
    if (currentFilter.tag && (!recipe.tags || !recipe.tags.includes(currentFilter.tag))) {
      return false;
    }

    return true;
  });

  // Sort by title
  filtered.sort((a, b) => a.title.localeCompare(b.title));

  // Render
  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="text-center text-muted" style="grid-column: 1/-1; padding: 2rem;">
        <p>No recipes found matching your criteria.</p>
        <button class="btn btn-secondary" onclick="clearFilters()">Clear Filters</button>
      </div>
    `;
    return;
  }

  let html = '';
  filtered.forEach(recipe => {
    html += renderRecipeCard(recipe);
  });

  container.innerHTML = html;
}

/**
 * Get thumbnail path for a recipe
 * @param {Object} recipe - Recipe object with image_refs
 * @returns {string|null} - Path to webp thumbnail or null
 */
function getRecipeThumbnail(recipe) {
  if (!recipe.image_refs || recipe.image_refs.length === 0) return null;

  // Get first image ref and convert to thumbnail path
  let ref = recipe.image_refs[0];
  // Remove extension if present and add .webp
  const baseName = ref.replace(/\.(jpeg|jpg|png|PNG)$/i, '');
  return `data/thumbnails/${baseName}.webp`;
}

/**
 * Render a single recipe card
 */
function renderRecipeCard(recipe) {
  const categoryIcon = getCategoryIcon(recipe.category);
  const timeInfo = recipe.total_time || recipe.cook_time || '';
  const thumbnail = getRecipeThumbnail(recipe);

  return `
    <article class="recipe-card category-${escapeAttr(recipe.category)}">
      <div class="recipe-card-image">
        ${thumbnail
          ? `<img src="${escapeAttr(thumbnail)}" alt="" class="recipe-thumb" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='block'"><span style="display:none">${categoryIcon}</span>`
          : categoryIcon
        }
      </div>
      <div class="recipe-card-content">
        <span class="category">${escapeHtml(recipe.category) || 'Uncategorized'}</span>
        <h3><a href="recipe.html#${escapeAttr(recipe.id)}">${escapeHtml(recipe.title)}</a></h3>
        <p class="description">${escapeHtml(recipe.description)}</p>
        <div class="meta">
          ${recipe.servings_yield ? `<span>${escapeHtml(recipe.servings_yield)}</span>` : ''}
          ${timeInfo ? `<span>${escapeHtml(timeInfo)}</span>` : ''}
        </div>
      </div>
    </article>
  `;
}

/**
 * Render full recipe detail page
 * Loads full recipe data from shard if needed
 */
async function renderRecipeDetail(recipeId) {
  const container = document.getElementById('recipe-content');
  if (!container) return;

  // Show loading state
  container.innerHTML = `
    <div class="text-center" style="padding: 2rem;">
      <p>Loading recipe...</p>
    </div>
  `;

  // Get full recipe data (may load shard)
  const recipe = await getFullRecipe(recipeId);

  if (!recipe) {
    container.innerHTML = `
      <div class="text-center">
        <h2>Recipe Not Found</h2>
        <p>Sorry, we couldn't find that recipe.</p>
        <a href="index.html" class="btn btn-primary">Back to Recipes</a>
      </div>
    `;
    return;
  }

  // Find variants of this recipe
  const variants = findVariants(recipe);

  // Update page title
  document.title = `${recipe.title} - Other Family Recipes`;

  // Check if this is a cheese recipe for milk substitution
  const isCheeseRecipe = typeof MilkSubstitution !== 'undefined' && MilkSubstitution.isCheeseRecipe(recipe);
  currentRecipeForMilkSub = isCheeseRecipe ? recipe : null;

  let html = `
    <article class="recipe-detail">
      <header class="recipe-header">
        <h1>${escapeHtml(recipe.title)}</h1>
        ${recipe.attribution ? `<p class="recipe-attribution">From: ${escapeHtml(recipe.attribution)}</p>` : ''}
        ${recipe.source_note ? `<p class="recipe-source">${escapeHtml(recipe.source_note)}</p>` : ''}
        ${recipe.description ? `<p>${escapeHtml(recipe.description)}</p>` : ''}

        <div class="header-controls">
          <div class="confidence-indicator confidence-${escapeAttr(recipe.confidence?.overall || 'high')}">
            Confidence: ${escapeHtml(capitalizeFirst(recipe.confidence?.overall || 'high'))}
          </div>

          ${variants.length > 0 ? renderVariantTabs(recipe, variants) : ''}
        </div>

        <div class="action-buttons" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <button id="print-btn" class="btn btn-secondary btn-print">Print Recipe</button>
          ${recipe.conversions?.has_conversions ? `
            <button id="metric-toggle" class="btn btn-secondary">
              ${showMetric ? 'Show US Units' : 'Show Metric'}
            </button>
          ` : ''}
        </div>
      </header>

      ${renderQuickFacts(recipe)}

      ${isCheeseRecipe ? '<div id="milk-substitution-container"></div>' : ''}

      <section class="ingredients-section">
        <h2>Ingredients ${showMetric && recipe.conversions?.has_conversions ? '<span class="unit-badge">Metric (approx.)</span>' : ''}</h2>
        ${renderIngredientsList(recipe)}
      </section>

      <section class="instructions-section">
        <h2>Instructions</h2>
        <ol class="instructions-list">
          ${recipe.instructions.map(inst => {
            const isInferred = inst.text.includes('[INFERRED]');
            const text = inst.text.replace('[INFERRED] ', '');
            return `<li class="${isInferred ? 'inferred' : ''}">${escapeHtml(text)}</li>`;
          }).join('')}
        </ol>
      </section>

      ${recipe.oven_directions ? renderOvenDirections(recipe.oven_directions) : ''}
      ${recipe.frosting ? renderFrosting(recipe.frosting) : ''}
      ${recipe.nutrition ? renderNutrition(recipe.nutrition, recipe.servings_yield) : ''}
      ${recipe.notes && recipe.notes.length > 0 ? renderNotes(recipe.notes) : ''}
      ${recipe.conversions?.conversion_assumptions?.length > 0 && showMetric ? renderConversionNotes(recipe.conversions) : ''}
      ${renderTags(recipe.tags)}
      ${renderRelatedTips(recipe)}
      ${renderConfidenceFlags(recipe.confidence?.flags)}
      ${renderOriginalScan(recipe.image_refs, recipe.collection)}
    </article>
  `;

  container.innerHTML = html;

  // Re-attach event listeners
  const printBtn = document.getElementById('print-btn');
  if (printBtn) {
    printBtn.addEventListener('click', () => window.print());
  }

  const metricToggle = document.getElementById('metric-toggle');
  if (metricToggle) {
    metricToggle.addEventListener('click', () => {
      showMetric = !showMetric;
      renderRecipeDetail(recipeId);
    });
  }

  // Variant tab handler — the active tab is inert; the rest navigate
  document.querySelectorAll('.variant-tab[data-vid]').forEach(tab => {
    if (tab.dataset.vid === recipe.id) return;
    tab.addEventListener('click', () => {
      window.location.hash = tab.dataset.vid;
      renderRecipeDetail(tab.dataset.vid);
    });
  });

  // Initialize milk substitution panel for cheese recipes
  if (isCheeseRecipe && typeof MilkSubstitution !== 'undefined') {
    MilkSubstitution.renderMilkSwitcher(recipe, 'milk-substitution-container');
  }
}

/**
 * Find all variants of a recipe (or recipes this is a variant of)
 */
function findVariants(recipe) {
  const variants = [];
  const canonicalId = recipe.canonical_id || recipe.id;

  recipes.forEach(r => {
    if (r.id === recipe.id) return; // Skip self

    // Check if this recipe is a variant of the current one
    if (r.variant_of === recipe.id || r.variant_of === canonicalId) {
      variants.push(r);
    }
    // Check if current recipe is a variant and find siblings
    if (recipe.variant_of && (r.id === recipe.variant_of || r.variant_of === recipe.variant_of)) {
      if (r.id !== recipe.id) variants.push(r);
    }
    // Check canonical grouping
    if (r.canonical_id === canonicalId && r.id !== recipe.id) {
      variants.push(r);
    }
  });

  return variants;
}

/**
 * Render variant tabs — one dish, one page; the versions sit as tabs, each labeled
 * by its provenance (attribution first), canonical version first. Replaces the old
 * dropdown so a reader can SEE the versions instead of discovering a select.
 */
function renderVariantTabs(currentRecipe, variants) {
  const canonicalId = currentRecipe.variant_of || currentRecipe.canonical_id || currentRecipe.id;
  const family = new Map();
  family.set(currentRecipe.id, currentRecipe);
  variants.forEach(v => { if (!family.has(v.id)) family.set(v.id, v); });
  const members = [...family.values()].sort((a, b) =>
    (a.id === canonicalId ? -1 : b.id === canonicalId ? 1 : 0) ||
    String(a.title).localeCompare(String(b.title)) || String(a.id).localeCompare(String(b.id)));
  if (members.length < 2) return '';
  const label = (m) => m.attribution ||
    (m.source_note ? m.source_note.substring(0, 40) : '') || m.title;
  return `
    <div class="variant-tabs" role="tablist" aria-label="Recipe versions">
      ${members.map(m => `
        <button class="variant-tab${m.id === currentRecipe.id ? ' on' : ''}" role="tab"
          aria-selected="${m.id === currentRecipe.id}" data-vid="${escapeAttr(m.id)}"
          title="${escapeAttr(m.title)}${m.variant_notes ? ' — ' + escapeAttr(m.variant_notes) : ''}">
          ${escapeHtml(label(m))}
        </button>
      `).join('')}
    </div>
  `;
}

/**
 * Render ingredients list (with metric toggle support)
 */
function renderIngredientsList(recipe) {
  const ingredients = showMetric && recipe.conversions?.ingredients_metric?.length > 0
    ? recipe.conversions.ingredients_metric
    : recipe.ingredients;

  return `
    <ul class="ingredients-list">
      ${ingredients.map(ing => `
        <li>
          <span class="ingredient-quantity">${escapeHtml(ing.quantity)} ${escapeHtml(ing.unit)}</span>
          <span class="ingredient-item">
            ${escapeHtml(ing.item)}
            ${ing.prep_note ? `<span class="ingredient-prep">, ${escapeHtml(ing.prep_note)}</span>` : ''}
          </span>
        </li>
      `).join('')}
    </ul>
  `;
}

/**
 * Render nutrition information
 */
function renderNutrition(nutrition, servings) {
  if (!nutrition || nutrition.status === 'insufficient_data') {
    if (nutrition?.missing_inputs?.length > 0) {
      return `
        <section class="nutrition-section nutrition-incomplete">
          <h3>Nutrition Information</h3>
          <p class="text-muted">Nutrition data incomplete. Missing: ${escapeHtml(nutrition.missing_inputs.join(', '))}</p>
        </section>
      `;
    }
    return '';
  }

  const n = nutrition.per_serving;
  if (!n) return '';

  return `
    <section class="nutrition-section">
      <h3>Nutrition Information ${servings ? `<span class="text-muted">(per serving)</span>` : ''}</h3>
      <div class="nutrition-grid">
        ${n.calories !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.calories)}</span><span class="nutrition-label">Calories</span></div>` : ''}
        ${n.fat_g !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.fat_g)}g</span><span class="nutrition-label">Fat</span></div>` : ''}
        ${n.carbs_g !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.carbs_g)}g</span><span class="nutrition-label">Carbs</span></div>` : ''}
        ${n.protein_g !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.protein_g)}g</span><span class="nutrition-label">Protein</span></div>` : ''}
        ${n.sodium_mg !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.sodium_mg)}mg</span><span class="nutrition-label">Sodium</span></div>` : ''}
        ${n.fiber_g !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.fiber_g)}g</span><span class="nutrition-label">Fiber</span></div>` : ''}
        ${n.sugar_g !== null ? `<div class="nutrition-item"><span class="nutrition-value">${escapeHtml(n.sugar_g)}g</span><span class="nutrition-label">Sugar</span></div>` : ''}
      </div>
      ${nutrition.assumptions?.length > 0 ? `
        <p class="nutrition-assumptions text-muted">
          <small>Assumptions: ${escapeHtml(nutrition.assumptions.join('; '))}</small>
        </p>
      ` : ''}
    </section>
  `;
}

/**
 * Render conversion notes
 */
function renderConversionNotes(conversions) {
  if (!conversions?.conversion_assumptions?.length) return '';

  return `
    <section class="notes-section conversion-notes" style="border-left-color: #6c757d;">
      <h3>Conversion Notes</h3>
      <p class="text-muted"><small>Metric conversions are approximate. Assumptions used:</small></p>
      <ul>
        ${conversions.conversion_assumptions.map(a => `<li><small>${escapeHtml(a)}</small></li>`).join('')}
      </ul>
    </section>
  `;
}

/**
 * Render quick facts section
 */
function renderQuickFacts(recipe) {
  const facts = [];

  if (recipe.servings_yield) facts.push({ label: 'Yield', value: recipe.servings_yield });
  if (recipe.prep_time) facts.push({ label: 'Prep', value: recipe.prep_time });
  if (recipe.cook_time) facts.push({ label: 'Cook', value: recipe.cook_time });
  if (recipe.total_time) facts.push({ label: 'Total', value: recipe.total_time });
  if (recipe.temperature) facts.push({ label: 'Temp', value: recipe.temperature });

  if (facts.length === 0) return '';

  return `
    <div class="recipe-quick-facts">
      ${facts.map(f => `
        <div class="quick-fact">
          <span class="quick-fact-label">${escapeHtml(f.label)}</span>
          <span class="quick-fact-value">${escapeHtml(f.value)}</span>
        </div>
      `).join('')}
    </div>
  `;
}

/**
 * Render oven directions (alternative method)
 */
function renderOvenDirections(directions) {
  return `
    <section class="sub-recipe">
      <h3>Oven Directions (Alternative)</h3>
      <ol class="instructions-list">
        ${directions.map(d => `<li>${escapeHtml(d.text)}</li>`).join('')}
      </ol>
    </section>
  `;
}

/**
 * Render frosting/sub-recipe section
 */
function renderFrosting(frosting) {
  return `
    <section class="sub-recipe">
      <h3>${escapeHtml(frosting.name)}</h3>
      <h4>Ingredients:</h4>
      <ul class="ingredients-list">
        ${frosting.ingredients.map(ing => `
          <li>
            <span class="ingredient-quantity">${escapeHtml(ing.quantity)} ${escapeHtml(ing.unit)}</span>
            <span class="ingredient-item">${escapeHtml(ing.item)}</span>
          </li>
        `).join('')}
      </ul>
      <h4>Instructions:</h4>
      <p>${escapeHtml(frosting.instructions)}</p>
    </section>
  `;
}

/**
 * Render notes section
 */
function renderNotes(notes) {
  return `
    <section class="notes-section">
      <h3>Notes</h3>
      <ul>
        ${notes.map(note => `<li>${escapeHtml(note)}</li>`).join('')}
      </ul>
    </section>
  `;
}

/**
 * Render tags
 */
function renderTags(tags) {
  if (!tags || tags.length === 0) return '';

  return `
    <div class="recipe-tags">
      ${tags.map(tag => `<span class="recipe-tag">${escapeHtml(tag)}</span>`).join('')}
    </div>
  `;
}

/**
 * Render related tips for a recipe
 */
function renderRelatedTips(recipe) {
  const relatedTips = findTipsForRecipe(recipe);
  if (relatedTips.length === 0) return '';

  const categoryLabels = {
    selection: 'Selecting',
    storage: 'Storage',
    preparation: 'Prep Tips',
    cooking: 'Cooking',
    substitution: 'Substitutions',
    technique: 'Technique',
    equipment: 'Equipment',
    safety: 'Safety',
    serving: 'Serving'
  };

  return `
    <section class="tips-section">
      <h3>Related Tips</h3>
      <div class="tips-list">
        ${relatedTips.map(tip => `
          <div class="tip-card" data-tip-id="${escapeAttr(tip.id)}">
            <div class="tip-header">
              <span class="tip-category">${escapeHtml(categoryLabels[tip.category] || tip.category)}</span>
              <h4 class="tip-title">${escapeHtml(tip.title)}</h4>
            </div>
            <p class="tip-content">${escapeHtml(tip.content)}</p>
            ${tip.related_ingredients && tip.related_ingredients.length > 0 ? `
              <div class="tip-ingredients">
                <small>Related: ${tip.related_ingredients.map(i => escapeHtml(i)).join(', ')}</small>
              </div>
            ` : ''}
          </div>
        `).join('')}
      </div>
    </section>
  `;
}

/**
 * Render a single tip card (for tips page)
 */
function renderTipCard(tip) {
  const categoryLabels = {
    selection: 'Selecting',
    storage: 'Storage',
    preparation: 'Prep Tips',
    cooking: 'Cooking',
    substitution: 'Substitutions',
    technique: 'Technique',
    equipment: 'Equipment',
    safety: 'Safety',
    serving: 'Serving'
  };

  return `
    <div class="tip-card" data-tip-id="${escapeAttr(tip.id)}">
      <div class="tip-header">
        <span class="tip-category">${escapeHtml(categoryLabels[tip.category] || tip.category)}</span>
        <h4 class="tip-title">${escapeHtml(tip.title)}</h4>
      </div>
      <p class="tip-content">${escapeHtml(tip.content)}</p>
      ${tip.related_ingredients && tip.related_ingredients.length > 0 ? `
        <div class="tip-ingredients">
          <small>Applies to: ${tip.related_ingredients.map(i => escapeHtml(i)).join(', ')}</small>
        </div>
      ` : ''}
      ${tip.related_tags && tip.related_tags.length > 0 ? `
        <div class="tip-tags">
          ${tip.related_tags.map(tag => `<span class="tip-tag">${escapeHtml(tag)}</span>`).join('')}
        </div>
      ` : ''}
    </div>
  `;
}

/**
 * Render confidence flags if any
 */
function renderConfidenceFlags(flags) {
  if (!flags || flags.length === 0) return '';

  return `
    <section class="notes-section" style="border-left-color: #f0ad4e;">
      <h3>Transcription Notes</h3>
      <ul>
        ${flags.map(flag => `
          <li>
            <strong>${escapeHtml(flag.field)}:</strong> ${escapeHtml(flag.issue)}
            ${flag.candidates && flag.candidates.length > 0 ?
              `<br><em>Possible values: ${escapeHtml(flag.candidates.join(', '))}</em>` : ''}
          </li>
        `).join('')}
      </ul>
    </section>
  `;
}

/**
 * Get the folder path for a collection's images
 */
function getCollectionImagePath(collection) {
  // Single collection - all images are in data/
  return 'data/';
}

/**
 * Render original scan thumbnail
 */
function renderOriginalScan(imageRefs, collection) {
  if (!imageRefs || imageRefs.length === 0) return '';

  const basePath = getCollectionImagePath(collection);

  return `
    <section class="original-scan">
      <h3>Original Scan</h3>
      ${imageRefs.map(ref => {
        const safePath = sanitizeUrl(basePath + ref);
        return `
        <a href="${escapeAttr(safePath)}" target="_blank">
          <img src="${escapeAttr(safePath)}" alt="Original recipe scan" class="scan-thumbnail"
               style="max-width: 200px; max-height: 150px; object-fit: cover;">
        </a>
      `;}).join('')}
    </section>
  `;
}

/**
 * Get category icon (emoji)
 */
function getCategoryIcon(category) {
  const icons = {
    appetizers: '🥗',
    beverages: '🍹',
    breads: '🍞',
    breakfast: '🍳',
    desserts: '🍪',
    mains: '🍽️',
    salads: '🥬',
    sides: '🥕',
    soups: '🍲',
    snacks: '🍿'
  };
  return icons[category] || '📖';
}

/**
 * Clear all filters
 */
function clearFilters() {
  currentFilter = { search: '', category: '', tag: '' };

  const searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.value = '';

  const categorySelect = document.getElementById('category-filter');
  if (categorySelect) categorySelect.value = '';

  document.querySelectorAll('.filter-tag').forEach(el => el.classList.remove('active'));

  renderRecipeGrid();
}

// Make clearFilters available globally
window.clearFilters = clearFilters;

/**
 * Utility: Capitalize first letter
 */
function capitalizeFirst(str) {
  if (!str) return '';
  return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Utility: Debounce function
 */
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/**
 * Show error message
 */
function showError(message) {
  const container = document.getElementById('recipe-grid') || document.getElementById('recipe-content');
  if (container) {
    container.innerHTML = `
      <div class="text-center" style="padding: 2rem; color: #721c24; background: #f8d7da; border-radius: 8px;">
        <p>${escapeHtml(message)}</p>
      </div>
    `;
  }
}
