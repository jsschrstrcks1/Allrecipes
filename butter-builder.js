/**
 * Butter Recipe Builder - Interactive Wizard
 *
 * Guides users through making homemade butter:
 * - Choose cream source (cow, goat, sheep, buffalo, yak)
 * - Select butter style (sweet cream, cultured, ghee, compound, etc.)
 * - Pick flavor additions for compound butters
 * - Get a complete recipe with tips and adjacencies
 *
 * Follows same IIFE pattern as CheeseBuilder for consistency.
 */

const ButterBuilder = (function() {
    'use strict';

    // ============ State ============
    let templateData = null;

    // Wizard state
    let currentStep = 0;
    let wizardState = {
        cream: {
            type: 'cow',
            quantity: 2,
            unit: 'cups'
        },
        style: null,
        flavorCategory: null,
        flavorChoice: null,
        selectedRecipe: null
    };

    const WIZARD_STEPS = [
        'welcome',
        'cream',
        'style',
        'flavor',
        'recipe'
    ];

    // ============ Data Loading ============

    async function loadData() {
        try {
            const response = await fetch('data/butter-templates.json');
            templateData = await response.json();
            console.log('Butter Builder data loaded:', {
                cream_sources: Object.keys(templateData.cream_sources).length,
                styles: Object.keys(templateData.butter_styles).length,
                recipes: Object.keys(templateData.base_recipes).length
            });
            return true;
        } catch (error) {
            console.error('Failed to load butter builder data:', error);
            return false;
        }
    }

    // ============ Wizard Navigation ============

    function getCurrentStep() {
        return WIZARD_STEPS[currentStep];
    }

    function nextStep() {
        // Skip flavor step if style doesn't use it
        if (getCurrentStep() === 'style' && wizardState.style && wizardState.style !== 'compound') {
            currentStep = WIZARD_STEPS.indexOf('recipe');
            return getCurrentStep();
        }
        if (currentStep < WIZARD_STEPS.length - 1) {
            currentStep++;
            return getCurrentStep();
        }
        return null;
    }

    function prevStep() {
        // Skip flavor step going backwards if not compound
        if (getCurrentStep() === 'recipe' && wizardState.style && wizardState.style !== 'compound') {
            currentStep = WIZARD_STEPS.indexOf('style');
            return getCurrentStep();
        }
        if (currentStep > 0) {
            currentStep--;
            return getCurrentStep();
        }
        return null;
    }

    function resetWizard() {
        currentStep = 0;
        wizardState = {
            cream: { type: 'cow', quantity: 2, unit: 'cups' },
            style: null,
            flavorCategory: null,
            flavorChoice: null,
            selectedRecipe: null
        };
    }

    // ============ Save Step State ============

    function saveCurrentStepState(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const step = getCurrentStep();

        if (step === 'cream') {
            const selected = container.querySelector('.cream-card.selected');
            if (selected) wizardState.cream.type = selected.dataset.creamType;

            const qtyInput = container.querySelector('#cream-quantity');
            if (qtyInput) wizardState.cream.quantity = parseFloat(qtyInput.value) || 2;

            const unitSelect = container.querySelector('#cream-unit');
            if (unitSelect) wizardState.cream.unit = unitSelect.value;
        }

        if (step === 'style') {
            const selected = container.querySelector('.style-card.selected');
            if (selected) wizardState.style = selected.dataset.styleId;
        }

        if (step === 'flavor') {
            const selected = container.querySelector('.flavor-item.selected');
            if (selected) {
                wizardState.flavorCategory = selected.dataset.category;
                wizardState.flavorChoice = selected.dataset.flavor;
            }
        }
    }

    // ============ Recipe Generation ============

    function generateRecipe() {
        const style = wizardState.style || 'sweet_cream';
        const styleInfo = templateData.butter_styles[style];
        const creamInfo = templateData.cream_sources[wizardState.cream.type];

        // Find base recipe
        let baseRecipe = null;
        for (const [key, recipe] of Object.entries(templateData.base_recipes)) {
            if (recipe.style === style) {
                baseRecipe = recipe;
                break;
            }
        }

        if (!baseRecipe) {
            baseRecipe = templateData.base_recipes['basic_sweet_cream'];
        }

        // Build adapted recipe
        const recipe = JSON.parse(JSON.stringify(baseRecipe));

        // Adapt cream type
        if (wizardState.cream.type !== 'cow') {
            recipe.title = recipe.title + ` (${creamInfo.name})`;
            recipe.notes = recipe.notes || [];
            recipe.notes.push(`Adapted for ${creamInfo.name}: ${creamInfo.notes}`);
            if (creamInfo.yield_notes) {
                recipe.notes.push(`Yield note: ${creamInfo.yield_notes}`);
            }
        }

        // Adapt quantity
        if (wizardState.cream.quantity !== 2 || wizardState.cream.unit !== 'cups') {
            recipe.ingredients[0].quantity = String(wizardState.cream.quantity);
            recipe.ingredients[0].unit = wizardState.cream.unit;
        }

        // Add compound flavoring
        if (style === 'compound' && wizardState.flavorChoice) {
            const category = templateData.flavor_additions[wizardState.flavorCategory];
            if (category) {
                const flavor = category.items.find(f => f.name === wizardState.flavorChoice);
                if (flavor) {
                    recipe.title = `${flavor.name} Compound Butter`;
                    recipe.notes = recipe.notes || [];
                    recipe.notes.push(`Flavor additions: ${flavor.ingredients.join(', ')}`);
                    recipe.notes.push(`Best paired with: ${flavor.pairs_with}`);

                    // Add flavor ingredients to recipe
                    flavor.ingredients.forEach(ing => {
                        recipe.ingredients.push({
                            item: ing,
                            quantity: '',
                            unit: 'to taste'
                        });
                    });
                }
            }
        }

        return { recipe, styleInfo, creamInfo };
    }

    // ============ Adjacency Logic ============

    function getAdjacentStyles() {
        const style = wizardState.style || 'sweet_cream';
        const adj = templateData.adjacencies[style];
        if (!adj) return [];
        return adj.adjacent.map(a => ({
            style: a.style,
            name: templateData.butter_styles[a.style]?.name || a.style,
            change: a.change
        }));
    }

    // ============ Tips ============

    function getRelevantTips() {
        const style = wizardState.style || 'sweet_cream';
        const tips = [];

        // Always include churning tips for butter-from-scratch styles
        if (['sweet_cream', 'cultured'].includes(style)) {
            tips.push({ topic: 'Churning', items: templateData.tips_by_topic.churning || [] });
            tips.push({ topic: 'Washing', items: templateData.tips_by_topic.washing || [] });
        }

        // Style-specific tips
        const styleInfo = templateData.butter_styles[style];
        if (styleInfo && styleInfo.tips) {
            tips.push({ topic: styleInfo.name + ' Tips', items: styleInfo.tips });
        }

        // Always include storage and troubleshooting
        tips.push({ topic: 'Storage', items: templateData.tips_by_topic.storage || [] });
        tips.push({ topic: 'Troubleshooting', items: templateData.tips_by_topic.troubleshooting || [] });

        return tips;
    }

    function getDidYouKnowFacts() {
        return templateData.tips_by_topic.history || [];
    }

    // ============ Rendering ============

    function renderProgressBar() {
        const div = document.createElement('div');
        div.className = 'butter-progress-bar';

        const visibleSteps = WIZARD_STEPS.filter(s => {
            if (s === 'flavor' && wizardState.style && wizardState.style !== 'compound') return false;
            return true;
        });

        const stepLabels = {
            welcome: 'Start',
            cream: 'Cream',
            style: 'Style',
            flavor: 'Flavors',
            recipe: 'Recipe'
        };

        const currentIdx = visibleSteps.indexOf(getCurrentStep());

        div.innerHTML = visibleSteps.map((step, i) => {
            let cls = 'progress-step';
            if (i < currentIdx) cls += ' completed';
            if (i === currentIdx) cls += ' active';
            return `<div class="${cls}">
                <div class="step-dot">${i < currentIdx ? '&#10003;' : i + 1}</div>
                <div class="step-label">${stepLabels[step]}</div>
            </div>`;
        }).join('<div class="step-connector"></div>');

        return div;
    }

    function renderCurrentStep() {
        const div = document.createElement('div');
        div.className = 'wizard-step-content';

        switch (getCurrentStep()) {
            case 'welcome': div.innerHTML = renderWelcomeStep(); break;
            case 'cream': div.innerHTML = renderCreamStep(); break;
            case 'style': div.innerHTML = renderStyleStep(); break;
            case 'flavor': div.innerHTML = renderFlavorStep(); break;
            case 'recipe': div.innerHTML = renderRecipeStep(); break;
        }

        return div;
    }

    function renderNavigation() {
        const div = document.createElement('div');
        div.className = 'wizard-navigation';
        const step = getCurrentStep();
        const isFirst = step === 'welcome';
        const isLast = step === 'recipe';

        div.innerHTML = `
            ${!isFirst ? '<button class="btn btn-secondary btn-prev">&#8592; Back</button>' : '<div></div>'}
            ${!isLast ? '<button class="btn btn-primary btn-next">Next &#8594;</button>' : '<button class="btn btn-primary btn-restart">Start Over</button>'}
        `;

        return div;
    }

    // ============ Step Renderers ============

    function renderWelcomeStep() {
        return `
            <div class="welcome-step">
                <h2>Butter Builder</h2>
                <p class="welcome-subtitle">Make your own homemade butter from any kind of milk</p>
                <div class="welcome-features">
                    <div class="feature-card">
                        <div class="feature-icon">&#129490;</div>
                        <h3>Choose Your Cream</h3>
                        <p>Cow, goat, sheep, buffalo, or yak</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">&#127908;</div>
                        <h3>Pick a Style</h3>
                        <p>Sweet cream, cultured, ghee, compound, smen, and more</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">&#127860;</div>
                        <h3>Add Flavors</h3>
                        <p>Herbs, spices, honey, garlic, truffle, miso...</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">&#128220;</div>
                        <h3>Get Your Recipe</h3>
                        <p>Complete instructions, tips, and variation ideas</p>
                    </div>
                </div>
            </div>
        `;
    }

    function renderCreamStep() {
        const sources = templateData.cream_sources;
        return `
            <div class="cream-step">
                <h2>Choose Your Cream Source</h2>
                <p class="step-description">Different milks produce different flavored butters. Each has unique character.</p>

                <div class="cream-grid">
                    ${Object.values(sources).map(s => `
                        <div class="cream-card ${wizardState.cream.type === s.id ? 'selected' : ''}" data-cream-type="${s.id}">
                            <h3>${s.name}</h3>
                            <div class="cream-fat">Fat: ${s.fat_content}</div>
                            <div class="cream-flavor">${s.flavor_profile.join(', ')}</div>
                            <div class="cream-yield">${s.yield_notes}</div>
                            <div class="cream-best">Best for: ${s.best_for.join(', ')}</div>
                        </div>
                    `).join('')}
                </div>

                <div class="quantity-row">
                    <label for="cream-quantity">How much cream?</label>
                    <input type="number" id="cream-quantity" value="${wizardState.cream.quantity}" min="0.5" max="16" step="0.5">
                    <select id="cream-unit">
                        <option value="cups" ${wizardState.cream.unit === 'cups' ? 'selected' : ''}>cups</option>
                        <option value="pints" ${wizardState.cream.unit === 'pints' ? 'selected' : ''}>pints</option>
                        <option value="quarts" ${wizardState.cream.unit === 'quarts' ? 'selected' : ''}>quarts</option>
                        <option value="gallons" ${wizardState.cream.unit === 'gallons' ? 'selected' : ''}>gallons</option>
                    </select>
                </div>
            </div>
        `;
    }

    function renderStyleStep() {
        const styles = templateData.butter_styles;
        const creamType = wizardState.cream.type;

        return `
            <div class="style-step">
                <h2>Choose Your Butter Style</h2>
                <p class="step-description">From simple sweet cream to aged Moroccan smen - pick your adventure.</p>

                <div class="style-grid">
                    ${Object.values(styles).map(s => {
                        const compatible = s.compatible_milks.includes(creamType);
                        return `
                            <div class="style-card ${wizardState.style === s.id ? 'selected' : ''} ${!compatible ? 'incompatible' : ''}" data-style-id="${s.id}" ${!compatible ? 'title="Not recommended with ' + creamType + ' cream"' : ''}>
                                <div class="style-header">
                                    <h3>${s.name}</h3>
                                    <span class="difficulty-badge difficulty-${s.difficulty}">${s.difficulty}</span>
                                </div>
                                <p class="style-desc">${s.description}</p>
                                <div class="style-meta">
                                    <span class="style-time">${s.time}</span>
                                    <span class="style-shelf">${s.shelf_life}</span>
                                </div>
                                ${!compatible ? '<div class="compat-warning">Not typical with ' + templateData.cream_sources[creamType].name + '</div>' : ''}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;
    }

    function renderFlavorStep() {
        const additions = templateData.flavor_additions;
        return `
            <div class="flavor-step">
                <h2>Choose Your Flavor</h2>
                <p class="step-description">Pick a flavor combination for your compound butter, or skip for plain.</p>

                ${Object.entries(additions).map(([catId, cat]) => `
                    <div class="flavor-category">
                        <h3>${cat.name}</h3>
                        <div class="flavor-grid">
                            ${cat.items.map(item => `
                                <div class="flavor-item ${wizardState.flavorChoice === item.name ? 'selected' : ''}" data-category="${catId}" data-flavor="${item.name}">
                                    <div class="flavor-name">${item.name}</div>
                                    <div class="flavor-ingredients">${item.ingredients.join(', ')}</div>
                                    <div class="flavor-pairs">Pairs with: ${item.pairs_with}</div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    function renderRecipeStep() {
        const { recipe, styleInfo, creamInfo } = generateRecipe();
        const adjacentStyles = getAdjacentStyles();
        const tips = getRelevantTips();
        const facts = getDidYouKnowFacts();

        return `
            <div class="recipe-step">
                <div class="recipe-header-card">
                    <h2>${recipe.title}</h2>
                    <div class="recipe-meta-bar">
                        <span class="meta-item"><strong>Cream:</strong> ${creamInfo.name}</span>
                        <span class="meta-item"><strong>Style:</strong> ${styleInfo.name}</span>
                        <span class="meta-item"><strong>Difficulty:</strong> ${styleInfo.difficulty}</span>
                        <span class="meta-item"><strong>Time:</strong> ${styleInfo.time}</span>
                        <span class="meta-item"><strong>Shelf Life:</strong> ${styleInfo.shelf_life}</span>
                    </div>
                    ${recipe.yield ? `<div class="recipe-yield"><strong>Yield:</strong> ${recipe.yield}</div>` : ''}
                </div>

                <div class="recipe-section">
                    <h3>Ingredients</h3>
                    <ul class="ingredient-list">
                        ${recipe.ingredients.map(ing => `
                            <li>${ing.quantity ? ing.quantity + ' ' : ''}${ing.unit ? ing.unit + ' ' : ''}${ing.item}</li>
                        `).join('')}
                    </ul>
                </div>

                <div class="recipe-section">
                    <h3>Instructions</h3>
                    <ol class="instruction-list">
                        ${recipe.instructions.map(inst => `
                            <li>${inst.text}</li>
                        `).join('')}
                    </ol>
                </div>

                ${recipe.notes && recipe.notes.length > 0 ? `
                    <div class="recipe-section notes-section">
                        <h3>Notes</h3>
                        <ul class="notes-list">
                            ${recipe.notes.map(n => `<li>${n}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}

                ${adjacentStyles.length > 0 ? `
                    <div class="recipe-section adjacent-section">
                        <h3>Want to Try Something Different?</h3>
                        <p class="section-intro">Small changes to your technique can create a whole different butter:</p>
                        <div class="adjacent-grid">
                            ${adjacentStyles.map(a => `
                                <div class="adjacent-card">
                                    <div class="adjacent-name">${a.name}</div>
                                    <div class="adjacent-change">${a.change}</div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${tips.length > 0 ? `
                    <div class="recipe-section tips-section">
                        <h3>Tips &amp; Techniques</h3>
                        ${tips.map(t => `
                            <div class="tip-group">
                                <h4>${t.topic}</h4>
                                <ul class="tip-list">
                                    ${t.items.map(tip => `<li>${tip}</li>`).join('')}
                                </ul>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}

                ${facts.length > 0 ? `
                    <div class="recipe-section facts-section">
                        <h3>Did You Know?</h3>
                        <ul class="facts-list">
                            ${facts.map(f => `<li>${f}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
            </div>
        `;
    }

    // ============ Rendering Orchestration ============

    function renderWizard(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        container.innerHTML = '';
        container.className = 'butter-builder-wizard';

        container.appendChild(renderProgressBar());
        container.appendChild(renderCurrentStep());
        container.appendChild(renderNavigation());
    }

    // ============ Event Listeners ============

    function attachEventListeners(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        // Navigation
        container.addEventListener('click', function handler(e) {
            if (e.target.classList.contains('btn-next')) {
                saveCurrentStepState(containerId);
                nextStep();
                renderWizard(containerId);
                attachEventListeners(containerId);
            } else if (e.target.classList.contains('btn-prev')) {
                saveCurrentStepState(containerId);
                prevStep();
                renderWizard(containerId);
                attachEventListeners(containerId);
            } else if (e.target.classList.contains('btn-restart')) {
                resetWizard();
                renderWizard(containerId);
                attachEventListeners(containerId);
            }
        }, { once: true });

        // Cream card selection
        container.querySelectorAll('.cream-card').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.cream-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                wizardState.cream.type = card.dataset.creamType;
            });
        });

        // Style card selection
        container.querySelectorAll('.style-card:not(.incompatible)').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.style-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                wizardState.style = card.dataset.styleId;
            });
        });

        // Flavor item selection
        container.querySelectorAll('.flavor-item').forEach(item => {
            item.addEventListener('click', () => {
                container.querySelectorAll('.flavor-item').forEach(i => i.classList.remove('selected'));
                item.classList.add('selected');
                wizardState.flavorCategory = item.dataset.category;
                wizardState.flavorChoice = item.dataset.flavor;
            });
        });

        // Quantity input
        const qtyInput = container.querySelector('#cream-quantity');
        if (qtyInput) {
            qtyInput.addEventListener('change', () => {
                wizardState.cream.quantity = parseFloat(qtyInput.value) || 2;
            });
        }

        // Unit select
        const unitSelect = container.querySelector('#cream-unit');
        if (unitSelect) {
            unitSelect.addEventListener('change', () => {
                wizardState.cream.unit = unitSelect.value;
            });
        }
    }

    // ============ Public API ============

    return {
        loadData,
        renderWizard,
        attachEventListeners,
        resetWizard,
        getState: function() { return wizardState; }
    };
})();
