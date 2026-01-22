/**
 * Cheese Recipe Builder - Interactive Wizard
 *
 * Guides users through creating custom cheese recipes based on:
 * - Available milk type and quantity
 * - Desired cheese style
 * - Flavor profile preferences
 * - Adulterant/herb/spice selections
 *
 * Integrates with:
 * - milk-substitution.js for milk type adjustments
 * - adulterant-companion.js for herb/spice recommendations
 */

const CheeseBuilder = (function() {
    'use strict';

    // ============ State ============
    let templatesData = null;
    let recipesData = null;
    let milkSubData = null;
    let adulterantsData = null;

    // Wizard state
    let currentStep = 0;
    let wizardState = {
        milk: {
            type: 'cow',
            quantity: 1,
            unit: 'gallon',
            processing: 'pasteurized'
        },
        style: null,
        flavorProfile: null,
        adulterants: [],
        matchedRecipes: [],
        selectedRecipe: null,
        customizations: {}
    };

    const WIZARD_STEPS = [
        'welcome',
        'milk',
        'style',
        'flavor',
        'adulterants',
        'review',
        'recipe'
    ];

    // ============ Data Loading ============

    async function loadData() {
        try {
            const [templates, recipes, milkSub, adulterants] = await Promise.all([
                fetch('data/cheese-templates.json').then(r => r.json()),
                fetch('data/recipes.json').then(r => r.json()),
                fetch('data/milk-substitution.json').then(r => r.json()),
                fetch('data/adulterants.json').then(r => r.json())
            ]);

            templatesData = templates;
            recipesData = recipes.recipes || recipes;
            milkSubData = milkSub;
            adulterantsData = adulterants;

            console.log('Cheese Builder data loaded:', {
                templates: Object.keys(templatesData.base_recipes).length,
                recipes: recipesData.length,
                adulterants: adulterantsData.adulterants.length
            });

            return true;
        } catch (error) {
            console.error('Failed to load cheese builder data:', error);
            return false;
        }
    }

    // ============ Wizard Navigation ============

    function getCurrentStep() {
        return WIZARD_STEPS[currentStep];
    }

    function goToStep(stepName) {
        const index = WIZARD_STEPS.indexOf(stepName);
        if (index >= 0) {
            currentStep = index;
            return true;
        }
        return false;
    }

    function nextStep() {
        if (currentStep < WIZARD_STEPS.length - 1) {
            currentStep++;
            return getCurrentStep();
        }
        return null;
    }

    function prevStep() {
        if (currentStep > 0) {
            currentStep--;
            return getCurrentStep();
        }
        return null;
    }

    function resetWizard() {
        currentStep = 0;
        wizardState = {
            milk: {
                type: 'cow',
                quantity: 1,
                unit: 'gallon',
                processing: 'pasteurized'
            },
            style: null,
            flavorProfile: null,
            adulterants: [],
            matchedRecipes: [],
            selectedRecipe: null,
            customizations: {}
        };
    }

    // ============ Milk Selection ============

    function getMilkTypes() {
        if (!milkSubData) return [];
        return Object.values(milkSubData.milk_types).map(m => ({
            id: m.id,
            name: m.name,
            flavor: m.flavor_profile.join(', '),
            yield: m.cheese_yield_per_gallon_lb,
            notes: m.notes
        }));
    }

    function setMilk(type, quantity, unit = 'gallon', processing = 'pasteurized') {
        wizardState.milk = { type, quantity, unit, processing };
    }

    function getMilkInfo(type) {
        return milkSubData?.milk_types[type] || null;
    }

    // ============ Style Selection ============

    function getCheeseStyles() {
        if (!templatesData) return [];
        return Object.values(templatesData.cheese_styles).map(s => ({
            id: s.id,
            name: s.name,
            description: s.description,
            examples: s.examples,
            difficulty: s.difficulty,
            timeToEat: s.time_to_eat,
            agingRequired: s.aging_required,
            equipment: s.equipment
        }));
    }

    function setStyle(styleId) {
        wizardState.style = styleId;
        // Update matched recipes when style changes
        wizardState.matchedRecipes = findMatchingRecipes();
    }

    function getStyleInfo(styleId) {
        return templatesData?.cheese_styles[styleId] || null;
    }

    function getStylesForMilk(milkType) {
        if (!templatesData) return [];
        return Object.values(templatesData.cheese_styles)
            .filter(s => s.best_milk_types.includes(milkType))
            .map(s => ({
                id: s.id,
                name: s.name,
                description: s.description,
                recommended: true
            }));
    }

    // ============ Flavor Profile ============

    function getFlavorProfiles() {
        if (!templatesData) return [];
        return Object.values(templatesData.flavor_profiles).map(f => ({
            id: f.id,
            name: f.name,
            description: f.description,
            compatibleStyles: f.compatible_styles,
            suggestedAdulterants: f.suggested_adulterants
        }));
    }

    function getFlavorProfilesForStyle(styleId) {
        if (!templatesData) return [];
        return Object.values(templatesData.flavor_profiles)
            .filter(f => f.compatible_styles.includes(styleId))
            .map(f => ({
                id: f.id,
                name: f.name,
                description: f.description
            }));
    }

    function setFlavorProfile(profileId) {
        wizardState.flavorProfile = profileId;

        // Auto-suggest adulterants based on flavor profile
        const profile = templatesData?.flavor_profiles[profileId];
        if (profile && profile.suggested_adulterants) {
            wizardState.adulterants = profile.suggested_adulterants
                .slice(0, 3)
                .map(id => ({
                    id: id,
                    quantity: null, // Will be calculated
                    stage: null // Will be determined by recipe
                }));
        }
    }

    // ============ Adulterant Selection ============

    function getCompatibleAdulterants(styleId) {
        if (!adulterantsData || !styleId) return [];

        return adulterantsData.adulterants.filter(a => {
            // Check if compatible with cheese style
            if (a.incompatible_styles && a.incompatible_styles.includes(styleId)) {
                return false;
            }
            if (a.compatible_styles && !a.compatible_styles.includes(styleId)) {
                return false;
            }
            return true;
        }).map(a => ({
            id: a.id,
            name: a.name,
            category: a.category,
            intensity: a.intensity,
            flavorProfile: a.flavor_profile,
            bestStages: a.best_stages,
            baseQuantity: a.base_quantity
        }));
    }

    function getAdulterantsByCategory(category, styleId) {
        return getCompatibleAdulterants(styleId)
            .filter(a => a.category === category);
    }

    function addAdulterant(adulterantId, quantity = null, stage = null) {
        const adulterant = adulterantsData?.adulterants.find(a => a.id === adulterantId);
        if (!adulterant) return false;

        // Remove if already selected
        wizardState.adulterants = wizardState.adulterants.filter(a => a.id !== adulterantId);

        wizardState.adulterants.push({
            id: adulterantId,
            name: adulterant.name,
            quantity: quantity || adulterant.base_quantity,
            stage: stage || adulterant.best_stages[0],
            data: adulterant
        });

        return true;
    }

    function removeAdulterant(adulterantId) {
        wizardState.adulterants = wizardState.adulterants.filter(a => a.id !== adulterantId);
    }

    function getSelectedAdulterants() {
        return wizardState.adulterants;
    }

    function clearAdulterants() {
        wizardState.adulterants = [];
    }

    // ============ Recipe Matching ============

    function findMatchingRecipes() {
        if (!recipesData || !wizardState.style) return [];

        const style = wizardState.style;
        const flavorProfile = wizardState.flavorProfile;
        const keywords = templatesData?.recipe_matching?.style_keywords[style] || [];
        const flavorKeywords = flavorProfile ?
            (templatesData?.recipe_matching?.flavor_keywords[flavorProfile] || []) : [];

        // Filter cheese recipes
        let matches = recipesData.filter(r => r.category === 'cheese');

        // Score each recipe
        const scored = matches.map(recipe => {
            let score = 0;
            const title = (recipe.title || '').toLowerCase();
            const tags = (recipe.tags || []).map(t => t.toLowerCase());

            // Style keyword matching
            keywords.forEach(kw => {
                if (title.includes(kw.toLowerCase())) score += 10;
                if (tags.some(t => t.includes(kw.toLowerCase()))) score += 5;
            });

            // Flavor keyword matching
            flavorKeywords.forEach(kw => {
                if (title.includes(kw.toLowerCase())) score += 8;
                if (tags.some(t => t.includes(kw.toLowerCase()))) score += 4;
            });

            // Boost recipes with milk_substitutions enabled
            if (recipe.milk_substitutions?.enabled) score += 3;

            return { recipe, score };
        });

        // Sort by score and return top matches
        return scored
            .filter(s => s.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 10)
            .map(s => s.recipe);
    }

    function getBaseRecipeForStyle(styleId) {
        if (!templatesData) return null;

        // Find a base recipe that matches the style
        const baseRecipes = templatesData.base_recipes;
        for (const [id, recipe] of Object.entries(baseRecipes)) {
            if (recipe.style === styleId) {
                return { ...recipe, id };
            }
        }
        return null;
    }

    function selectRecipe(recipeId) {
        // Check if it's a base recipe
        if (templatesData?.base_recipes[recipeId]) {
            wizardState.selectedRecipe = {
                type: 'template',
                data: templatesData.base_recipes[recipeId]
            };
            return true;
        }

        // Check if it's from the recipe database
        const dbRecipe = recipesData?.find(r => r.id === recipeId);
        if (dbRecipe) {
            wizardState.selectedRecipe = {
                type: 'database',
                data: dbRecipe
            };
            return true;
        }

        return false;
    }

    // ============ Recipe Generation ============

    function generateRecipe() {
        const { milk, style, flavorProfile, adulterants, selectedRecipe } = wizardState;

        if (!selectedRecipe) {
            // Use base recipe for style
            const base = getBaseRecipeForStyle(style);
            if (base) {
                wizardState.selectedRecipe = { type: 'template', data: base };
            } else {
                return null;
            }
        }

        const recipe = wizardState.selectedRecipe;
        const milkInfo = getMilkInfo(milk.type);

        // Build the generated recipe
        const generated = {
            title: buildRecipeTitle(recipe.data, flavorProfile, adulterants),
            style: style,
            styleInfo: getStyleInfo(style),
            milk: {
                type: milk.type,
                typeName: milkInfo?.name || milk.type,
                quantity: milk.quantity,
                unit: milk.unit,
                processing: milk.processing,
                info: milkInfo
            },
            flavorProfile: flavorProfile,
            ingredients: adjustIngredients(recipe.data, milk, milkInfo),
            steps: injectAdulterantSteps(recipe.data, adulterants, milk),
            adulterants: calculateAdulterantQuantities(adulterants, milk),
            warnings: generateWarnings(style, adulterants, milk),
            tips: generateTips(style, milk, adulterants),
            yield: estimateYield(milk, milkInfo),
            sourceRecipe: recipe.data.title || recipe.data.name || recipe.data.id,
            generatedAt: new Date().toISOString()
        };

        return generated;
    }

    function buildRecipeTitle(baseRecipe, flavorProfile, adulterants) {
        const baseName = baseRecipe.title || baseRecipe.name || 'Cheese';
        const parts = [];

        // Add primary adulterant flavor
        if (adulterants.length > 0) {
            const primary = adulterants[0];
            if (primary.name) {
                // Simplify adulterant name for title
                const shortName = primary.name
                    .replace(' Powder', '')
                    .replace(' Ground', '')
                    .replace(' Dried', '')
                    .replace(' Flakes', '');
                parts.push(shortName);
            }
        }

        // Add flavor profile indicator
        if (flavorProfile === 'spicy') parts.push('Spicy');
        else if (flavorProfile === 'smoky') parts.push('Smoky');
        else if (flavorProfile === 'herbed') parts.push('Herbed');

        if (parts.length > 0) {
            return parts.join(' ') + ' ' + baseName;
        }
        return baseName;
    }

    function adjustIngredients(recipe, milk, milkInfo) {
        const ingredients = recipe.ingredients || [];
        const adjusted = [];

        const milkQuantity = milk.quantity;
        const baseQuantity = recipe.milk_quantity?.amount || 1;
        const scaleFactor = milkQuantity / baseQuantity;

        // Get rennet factor for milk type
        const rennetFactor = milkSubData?.rennet_adjustments?.factors[milk.type] || 1.0;

        ingredients.forEach(ing => {
            const item = { ...ing };
            const itemLower = (item.item || '').toLowerCase();

            // Adjust milk
            if (itemLower.includes('milk')) {
                item.quantity = String(milkQuantity);
                item.item = milkInfo?.name || milk.type + ' milk';
            }
            // Adjust rennet
            else if (itemLower.includes('rennet')) {
                const origQty = parseFloat(item.quantity) || 0.25;
                item.quantity = formatQuantity(origQty * scaleFactor * rennetFactor);
                item.notes = item.notes ? item.notes + ` (adjusted for ${milk.type} milk)` : `adjusted for ${milk.type} milk`;
            }
            // Adjust calcium chloride
            else if (itemLower.includes('calcium chloride') || itemLower.includes('cacl2')) {
                const cacl2 = milkSubData?.calcium_chloride_guidelines?.recommendations[milk.type];
                if (cacl2) {
                    if (cacl2[milk.processing] === 'not_needed' || cacl2[milk.processing] === 'never_needed') {
                        item.quantity = '0';
                        item.notes = `not needed for ${milk.type} ${milk.processing} milk`;
                    }
                }
            }
            // Scale other ingredients
            else if (scaleFactor !== 1) {
                const origQty = parseFloat(item.quantity);
                if (!isNaN(origQty)) {
                    item.quantity = formatQuantity(origQty * scaleFactor);
                }
            }

            adjusted.push(item);
        });

        return adjusted;
    }

    function injectAdulterantSteps(recipe, adulterants, milk) {
        if (!adulterants || adulterants.length === 0) {
            return recipe.steps || [];
        }

        const steps = [...(recipe.steps || [])];
        const injectionPoint = recipe.adulterant_injection_point || steps.length;

        // Group adulterants by stage
        const byStage = {};
        adulterants.forEach(a => {
            const stage = a.stage || 'CURD_MILL';
            if (!byStage[stage]) byStage[stage] = [];
            byStage[stage].push(a);
        });

        // Build injection steps
        const injectionSteps = [];
        Object.entries(byStage).forEach(([stage, ads]) => {
            const quantities = ads.map(a => {
                const qty = calculateSingleAdulterantQuantity(a, milk);
                return `${qty.formatted} ${a.name || a.id}`;
            });

            const stageName = getStageDisplayName(stage);
            injectionSteps.push({
                text: `${stageName}: Add ${quantities.join(', ')} and mix thoroughly.`,
                isAdulterant: true,
                stage: stage
            });
        });

        // Insert injection steps
        steps.splice(injectionPoint, 0, ...injectionSteps);

        // Renumber steps
        return steps.map((step, i) => ({
            ...step,
            step: i + 1
        }));
    }

    function calculateAdulterantQuantities(adulterants, milk) {
        if (!adulterants) return [];

        return adulterants.map(a => calculateSingleAdulterantQuantity(a, milk));
    }

    function calculateSingleAdulterantQuantity(adulterant, milk) {
        const base = adulterant.quantity || adulterant.data?.base_quantity || { amount: 0.5, unit: 'tsp', per: 'gallon' };
        const milkAdjustment = adulterant.data?.milk_adjustments?.[milk.type] || 1.0;

        const scaledAmount = base.amount * milk.quantity * milkAdjustment;

        return {
            id: adulterant.id,
            name: adulterant.name || adulterant.id,
            amount: scaledAmount,
            unit: base.unit,
            milkAdjustment: milkAdjustment,
            formatted: formatQuantity(scaledAmount) + ' ' + base.unit,
            stage: adulterant.stage
        };
    }

    function generateWarnings(style, adulterants, milk) {
        const warnings = [];

        // Style-specific warnings
        if (style === 'blue') {
            if (adulterants.length > 0) {
                warnings.push({
                    level: 'caution',
                    message: 'Blue cheese typically needs no adulterants - the mold provides all the flavor.'
                });
            }
        }

        if (style === 'bloomy') {
            const hasStrong = adulterants.some(a => {
                const intensity = a.data?.intensity || '';
                return intensity.startsWith('H') || intensity.startsWith('E');
            });
            if (hasStrong) {
                warnings.push({
                    level: 'warning',
                    message: 'Strong spices may inhibit Penicillium development on bloomy rinds.'
                });
            }
        }

        // Milk-specific warnings
        if (milk.processing === 'ultra_pasteurized') {
            warnings.push({
                level: 'danger',
                message: 'Ultra-pasteurized milk is not suitable for cheese making.'
            });
        }

        // Adulterant-specific warnings
        adulterants.forEach(a => {
            if (a.data?.warnings?.general) {
                warnings.push({
                    level: 'info',
                    message: a.data.warnings.general,
                    adulterant: a.name
                });
            }

            if (a.data?.warnings?.style_warnings?.[style]) {
                warnings.push({
                    level: 'warning',
                    message: a.data.warnings.style_warnings[style],
                    adulterant: a.name
                });
            }
        });

        return warnings;
    }

    function generateTips(style, milk, adulterants) {
        const tips = [];
        const milkInfo = getMilkInfo(milk.type);

        // Milk tips
        if (milkInfo?.notes) {
            tips.push(milkInfo.notes);
        }

        if (milk.type === 'goat') {
            tips.push('Goat milk curds are fragile - handle very gently.');
        }
        if (milk.type === 'sheep') {
            tips.push('Sheep milk produces higher yield - expect 50-80% more cheese.');
        }

        // Style tips
        const styleInfo = getStyleInfo(style);
        if (styleInfo?.notes) {
            tips.push(styleInfo.notes);
        }

        // Adulterant tips
        if (adulterants.length > 2) {
            tips.push('With multiple adulterants, start with smaller quantities and adjust to taste.');
        }

        return tips;
    }

    function estimateYield(milk, milkInfo) {
        const yieldPerGallon = milkInfo?.cheese_yield_per_gallon_lb || 1;
        const estimated = milk.quantity * yieldPerGallon;

        return {
            amount: estimated,
            unit: 'lb',
            formatted: `${estimated.toFixed(1)}-${(estimated * 1.2).toFixed(1)} lbs`
        };
    }

    // ============ Utility Functions ============

    function formatQuantity(num) {
        if (num === 0) return '0';
        if (num >= 1) return num.toFixed(num % 1 === 0 ? 0 : 1);

        // Convert to fractions for small amounts
        const fractions = [
            { val: 0.125, str: '1/8' },
            { val: 0.167, str: '1/6' },
            { val: 0.25, str: '1/4' },
            { val: 0.333, str: '1/3' },
            { val: 0.375, str: '3/8' },
            { val: 0.5, str: '1/2' },
            { val: 0.625, str: '5/8' },
            { val: 0.667, str: '2/3' },
            { val: 0.75, str: '3/4' },
            { val: 0.875, str: '7/8' }
        ];

        // Find closest fraction
        let closest = fractions[0];
        let minDiff = Math.abs(num - fractions[0].val);

        fractions.forEach(f => {
            const diff = Math.abs(num - f.val);
            if (diff < minDiff) {
                minDiff = diff;
                closest = f;
            }
        });

        if (minDiff < 0.05) return closest.str;
        return num.toFixed(2);
    }

    function getStageDisplayName(stage) {
        const names = {
            'COLD_INFUSE': 'Cold infusion',
            'MILK_PREHEAT': 'During milk heating',
            'PRE_RENNET': 'Before adding rennet',
            'CURD_CUT': 'After cutting curds',
            'CURD_MILL': 'While milling curds',
            'MOLD_LAYER': 'When filling molds',
            'POST_PRESS': 'After pressing',
            'BRINE_ADDITION': 'In the brine',
            'RIND_RUB': 'Rind rub/wash',
            'AGING_SURFACE': 'During aging',
            'FINISH_SERVING': 'Before serving'
        };
        return names[stage] || stage;
    }

    // ============ UI Rendering ============

    function renderWizard(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        container.innerHTML = '';
        container.className = 'cheese-builder-wizard';

        // Render progress bar
        const progress = renderProgressBar();
        container.appendChild(progress);

        // Render current step
        const stepContent = renderCurrentStep();
        container.appendChild(stepContent);

        // Render navigation
        const nav = renderNavigation();
        container.appendChild(nav);
    }

    function renderProgressBar() {
        const div = document.createElement('div');
        div.className = 'wizard-progress';

        WIZARD_STEPS.forEach((step, i) => {
            const stepEl = document.createElement('div');
            stepEl.className = 'progress-step';
            if (i < currentStep) stepEl.classList.add('completed');
            if (i === currentStep) stepEl.classList.add('active');

            const names = {
                'welcome': 'Start',
                'milk': 'Milk',
                'style': 'Style',
                'flavor': 'Flavor',
                'adulterants': 'Additions',
                'review': 'Review',
                'recipe': 'Recipe'
            };

            stepEl.innerHTML = `
                <span class="step-number">${i + 1}</span>
                <span class="step-name">${names[step] || step}</span>
            `;

            div.appendChild(stepEl);
        });

        return div;
    }

    function renderCurrentStep() {
        const div = document.createElement('div');
        div.className = 'wizard-step-content';

        const step = getCurrentStep();

        switch (step) {
            case 'welcome':
                div.innerHTML = renderWelcomeStep();
                break;
            case 'milk':
                div.innerHTML = renderMilkStep();
                break;
            case 'style':
                div.innerHTML = renderStyleStep();
                break;
            case 'flavor':
                div.innerHTML = renderFlavorStep();
                break;
            case 'adulterants':
                div.innerHTML = renderAdulterantsStep();
                break;
            case 'review':
                div.innerHTML = renderReviewStep();
                break;
            case 'recipe':
                div.innerHTML = renderRecipeStep();
                break;
        }

        return div;
    }

    function renderWelcomeStep() {
        return `
            <div class="step-welcome">
                <h2>Cheese Recipe Builder</h2>
                <p class="lead">Let's create your perfect homemade cheese!</p>
                <p>This wizard will guide you through:</p>
                <ul>
                    <li><strong>Selecting your milk</strong> - What you have on hand</li>
                    <li><strong>Choosing a cheese style</strong> - Fresh, aged, or specialty</li>
                    <li><strong>Picking flavors</strong> - Herbs, spices, and more</li>
                    <li><strong>Generating your recipe</strong> - Customized just for you</li>
                </ul>
                <p class="tip">Ready to make something delicious?</p>
            </div>
        `;
    }

    function renderMilkStep() {
        const milkTypes = getMilkTypes();
        const selected = wizardState.milk;

        return `
            <div class="step-milk">
                <h2>What milk do you have?</h2>

                <div class="form-group">
                    <label>Milk Type</label>
                    <div class="milk-type-grid">
                        ${milkTypes.map(m => `
                            <div class="milk-type-card ${selected.type === m.id ? 'selected' : ''}"
                                 data-milk-type="${m.id}">
                                <h4>${m.name}</h4>
                                <p class="flavor">${m.flavor}</p>
                                <p class="yield">~${m.yield} lb/gal yield</p>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <div class="form-group">
                    <label>Quantity Available</label>
                    <div class="quantity-input">
                        <input type="number" id="milk-quantity" value="${selected.quantity}"
                               min="0.5" max="10" step="0.5">
                        <select id="milk-unit">
                            <option value="gallon" ${selected.unit === 'gallon' ? 'selected' : ''}>Gallons</option>
                            <option value="liter" ${selected.unit === 'liter' ? 'selected' : ''}>Liters</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label>Processing</label>
                    <div class="processing-options">
                        <label class="radio-option">
                            <input type="radio" name="processing" value="raw"
                                   ${selected.processing === 'raw' ? 'checked' : ''}>
                            <span>Raw (unpasteurized)</span>
                        </label>
                        <label class="radio-option">
                            <input type="radio" name="processing" value="pasteurized"
                                   ${selected.processing === 'pasteurized' ? 'checked' : ''}>
                            <span>Pasteurized</span>
                        </label>
                        <label class="radio-option warning">
                            <input type="radio" name="processing" value="ultra_pasteurized"
                                   ${selected.processing === 'ultra_pasteurized' ? 'checked' : ''}>
                            <span>Ultra-pasteurized (not recommended)</span>
                        </label>
                    </div>
                </div>
            </div>
        `;
    }

    function renderStyleStep() {
        const styles = getCheeseStyles();
        const recommended = getStylesForMilk(wizardState.milk.type);
        const recommendedIds = recommended.map(r => r.id);

        return `
            <div class="step-style">
                <h2>What style of cheese?</h2>
                <p>Based on your ${wizardState.milk.type} milk, we recommend the highlighted styles.</p>

                <div class="style-grid">
                    ${styles.map(s => `
                        <div class="style-card ${wizardState.style === s.id ? 'selected' : ''}
                                    ${recommendedIds.includes(s.id) ? 'recommended' : ''}"
                             data-style="${s.id}">
                            <div class="style-header">
                                <h4>${s.name}</h4>
                                <span class="difficulty ${s.difficulty}">${s.difficulty}</span>
                            </div>
                            <p class="description">${s.description}</p>
                            <p class="examples">${s.examples.slice(0, 3).join(', ')}</p>
                            <p class="time-to-eat">${s.agingRequired ? s.timeToEat + ' aging' : 'Ready immediately'}</p>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    function renderFlavorStep() {
        const profiles = getFlavorProfilesForStyle(wizardState.style);

        return `
            <div class="step-flavor">
                <h2>What flavor profile?</h2>
                <p>Choose the direction you want to take your cheese.</p>

                <div class="flavor-grid">
                    ${profiles.map(f => `
                        <div class="flavor-card ${wizardState.flavorProfile === f.id ? 'selected' : ''}"
                             data-flavor="${f.id}">
                            <h4>${f.name}</h4>
                            <p>${f.description}</p>
                        </div>
                    `).join('')}

                    <div class="flavor-card ${!wizardState.flavorProfile ? 'selected' : ''}"
                         data-flavor="">
                        <h4>Plain / Classic</h4>
                        <p>No additional flavors - let the cheese shine</p>
                    </div>
                </div>
            </div>
        `;
    }

    function renderAdulterantsStep() {
        const compatible = getCompatibleAdulterants(wizardState.style);
        const selected = wizardState.adulterants;
        const selectedIds = selected.map(a => a.id);

        // Group by category
        const categories = {};
        compatible.forEach(a => {
            if (!categories[a.category]) categories[a.category] = [];
            categories[a.category].push(a);
        });

        const categoryNames = {
            'pepper': 'Hot Peppers',
            'herb': 'Dried Herbs',
            'spice': 'Spices',
            'indian': 'Indian Spices',
            'allium': 'Garlic & Onion',
            'alcohol': 'Alcohol Washes',
            'fruit': 'Dried Fruits',
            'nut': 'Nuts & Seeds',
            'other': 'Other'
        };

        return `
            <div class="step-adulterants">
                <h2>Add some extras?</h2>
                <p>Select herbs, spices, or other additions for your cheese.</p>

                <div class="selected-adulterants">
                    <h4>Selected (${selected.length})</h4>
                    ${selected.length === 0 ? '<p class="empty">None selected - this will be a plain cheese</p>' : ''}
                    <div class="selected-list">
                        ${selected.map(a => `
                            <span class="selected-tag" data-remove="${a.id}">
                                ${a.name || a.id}
                                <button class="remove-btn">&times;</button>
                            </span>
                        `).join('')}
                    </div>
                </div>

                <div class="adulterant-categories">
                    ${Object.entries(categories).map(([cat, items]) => `
                        <div class="category-section">
                            <h4>${categoryNames[cat] || cat}</h4>
                            <div class="adulterant-grid">
                                ${items.slice(0, 8).map(a => `
                                    <div class="adulterant-chip ${selectedIds.includes(a.id) ? 'selected' : ''}"
                                         data-adulterant="${a.id}">
                                        <span class="name">${a.name}</span>
                                        <span class="intensity intensity-${a.intensity}">${a.intensity}</span>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    function renderReviewStep() {
        const { milk, style, flavorProfile, adulterants } = wizardState;
        const styleInfo = getStyleInfo(style);
        const milkInfo = getMilkInfo(milk.type);
        const matchedRecipes = findMatchingRecipes();

        return `
            <div class="step-review">
                <h2>Review Your Choices</h2>

                <div class="review-summary">
                    <div class="review-item">
                        <h4>Milk</h4>
                        <p>${milkInfo?.name || milk.type}, ${milk.quantity} ${milk.unit}(s)</p>
                        <p class="detail">${milk.processing}</p>
                    </div>

                    <div class="review-item">
                        <h4>Style</h4>
                        <p>${styleInfo?.name || style}</p>
                        <p class="detail">${styleInfo?.time_to_eat || ''}</p>
                    </div>

                    <div class="review-item">
                        <h4>Flavor Profile</h4>
                        <p>${flavorProfile || 'Plain / Classic'}</p>
                    </div>

                    <div class="review-item">
                        <h4>Additions</h4>
                        <p>${adulterants.length > 0 ? adulterants.map(a => a.name || a.id).join(', ') : 'None'}</p>
                    </div>
                </div>

                <div class="recipe-matches">
                    <h3>Matching Recipes</h3>
                    ${matchedRecipes.length > 0 ? `
                        <p>We found ${matchedRecipes.length} recipes that match your preferences:</p>
                        <div class="recipe-match-list">
                            ${matchedRecipes.slice(0, 5).map(r => `
                                <div class="recipe-match-card ${wizardState.selectedRecipe?.data?.id === r.id ? 'selected' : ''}"
                                     data-recipe="${r.id}">
                                    <h4>${r.title}</h4>
                                    <p>${r.description || ''}</p>
                                </div>
                            `).join('')}
                        </div>
                    ` : `
                        <p>No exact matches found. We'll create a custom recipe using our base template.</p>
                    `}
                </div>

                <div class="estimated-yield">
                    <h4>Estimated Yield</h4>
                    <p>${estimateYield(milk, milkInfo).formatted}</p>
                </div>
            </div>
        `;
    }

    function renderRecipeStep() {
        const generated = generateRecipe();

        if (!generated) {
            return `
                <div class="step-recipe error">
                    <h2>Recipe Generation Failed</h2>
                    <p>We couldn't generate a recipe with your selections. Please go back and try different options.</p>
                </div>
            `;
        }

        return `
            <div class="step-recipe">
                <div class="recipe-header">
                    <h2>${generated.title}</h2>
                    <p class="recipe-meta">
                        <span class="style">${generated.styleInfo?.name}</span>
                        <span class="yield">Yield: ${generated.yield.formatted}</span>
                        <span class="milk">${generated.milk.typeName}</span>
                    </p>
                </div>

                ${generated.warnings.length > 0 ? `
                    <div class="recipe-warnings">
                        ${generated.warnings.map(w => `
                            <div class="warning warning-${w.level}">
                                <span class="icon">${w.level === 'danger' ? '⚠️' : w.level === 'warning' ? '⚡' : 'ℹ️'}</span>
                                <span class="message">${w.message}</span>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}

                <div class="recipe-section ingredients">
                    <h3>Ingredients</h3>
                    <ul>
                        ${generated.ingredients.map(ing => `
                            <li>
                                <span class="qty">${ing.quantity} ${ing.unit || ''}</span>
                                <span class="item">${ing.item}</span>
                                ${ing.notes ? `<span class="notes">(${ing.notes})</span>` : ''}
                            </li>
                        `).join('')}
                    </ul>

                    ${generated.adulterants.length > 0 ? `
                        <h4>Adulterant Additions</h4>
                        <ul class="adulterant-list">
                            ${generated.adulterants.map(a => `
                                <li>
                                    <span class="qty">${a.formatted}</span>
                                    <span class="item">${a.name}</span>
                                    <span class="stage">(add ${getStageDisplayName(a.stage).toLowerCase()})</span>
                                </li>
                            `).join('')}
                        </ul>
                    ` : ''}
                </div>

                <div class="recipe-section instructions">
                    <h3>Instructions</h3>
                    <ol>
                        ${generated.steps.map(step => `
                            <li class="${step.isAdulterant ? 'adulterant-step' : ''}">
                                ${step.text}
                            </li>
                        `).join('')}
                    </ol>
                </div>

                ${generated.tips.length > 0 ? `
                    <div class="recipe-section tips">
                        <h3>Tips</h3>
                        <ul>
                            ${generated.tips.map(tip => `<li>${tip}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}

                <div class="recipe-actions">
                    <button class="btn-print" onclick="window.print()">Print Recipe</button>
                    <button class="btn-save" onclick="CheeseBuilder.saveRecipe()">Save to Collection</button>
                    <button class="btn-restart" onclick="CheeseBuilder.resetAndRender()">Start Over</button>
                </div>

                <p class="source-note">
                    Based on: ${generated.sourceRecipe}<br>
                    Generated: ${new Date(generated.generatedAt).toLocaleDateString()}
                </p>
            </div>
        `;
    }

    function renderNavigation() {
        const div = document.createElement('div');
        div.className = 'wizard-navigation';

        const step = getCurrentStep();
        const isFirst = currentStep === 0;
        const isLast = currentStep === WIZARD_STEPS.length - 1;

        div.innerHTML = `
            <button class="btn-prev" ${isFirst ? 'disabled' : ''}>
                ← Back
            </button>
            <button class="btn-next" ${isLast ? 'style="display:none"' : ''}>
                ${step === 'review' ? 'Generate Recipe →' : 'Next →'}
            </button>
        `;

        return div;
    }

    function attachEventListeners(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        // Navigation buttons
        container.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-next')) {
                saveCurrentStepState();
                nextStep();
                renderWizard(containerId);
                attachEventListeners(containerId);
            }
            if (e.target.classList.contains('btn-prev')) {
                prevStep();
                renderWizard(containerId);
                attachEventListeners(containerId);
            }
        });

        // Milk type selection
        container.querySelectorAll('.milk-type-card').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.milk-type-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                wizardState.milk.type = card.dataset.milkType;
            });
        });

        // Milk quantity and unit
        const qtyInput = container.querySelector('#milk-quantity');
        const unitSelect = container.querySelector('#milk-unit');
        if (qtyInput) {
            qtyInput.addEventListener('change', () => {
                wizardState.milk.quantity = parseFloat(qtyInput.value) || 1;
            });
        }
        if (unitSelect) {
            unitSelect.addEventListener('change', () => {
                wizardState.milk.unit = unitSelect.value;
            });
        }

        // Processing radio buttons
        container.querySelectorAll('input[name="processing"]').forEach(radio => {
            radio.addEventListener('change', () => {
                wizardState.milk.processing = radio.value;
            });
        });

        // Style selection
        container.querySelectorAll('.style-card').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.style-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                setStyle(card.dataset.style);
            });
        });

        // Flavor selection
        container.querySelectorAll('.flavor-card').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.flavor-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                const flavor = card.dataset.flavor;
                if (flavor) {
                    setFlavorProfile(flavor);
                } else {
                    wizardState.flavorProfile = null;
                    wizardState.adulterants = [];
                }
            });
        });

        // Adulterant selection
        container.querySelectorAll('.adulterant-chip').forEach(chip => {
            chip.addEventListener('click', () => {
                const id = chip.dataset.adulterant;
                if (chip.classList.contains('selected')) {
                    removeAdulterant(id);
                    chip.classList.remove('selected');
                } else {
                    addAdulterant(id);
                    chip.classList.add('selected');
                }
                // Re-render selected list
                updateSelectedAdulterantsList(container);
            });
        });

        // Remove adulterant from selected list
        container.querySelectorAll('.selected-tag').forEach(tag => {
            tag.addEventListener('click', () => {
                const id = tag.dataset.remove;
                removeAdulterant(id);
                renderWizard(containerId);
                attachEventListeners(containerId);
            });
        });

        // Recipe selection
        container.querySelectorAll('.recipe-match-card').forEach(card => {
            card.addEventListener('click', () => {
                container.querySelectorAll('.recipe-match-card').forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                selectRecipe(card.dataset.recipe);
            });
        });
    }

    function updateSelectedAdulterantsList(container) {
        const listEl = container.querySelector('.selected-list');
        const emptyEl = container.querySelector('.selected-adulterants .empty');
        const countEl = container.querySelector('.selected-adulterants h4');

        const selected = wizardState.adulterants;

        if (countEl) countEl.textContent = `Selected (${selected.length})`;

        if (selected.length === 0) {
            if (emptyEl) emptyEl.style.display = '';
            if (listEl) listEl.innerHTML = '';
        } else {
            if (emptyEl) emptyEl.style.display = 'none';
            if (listEl) {
                listEl.innerHTML = selected.map(a => `
                    <span class="selected-tag" data-remove="${a.id}">
                        ${a.name || a.id}
                        <button class="remove-btn">&times;</button>
                    </span>
                `).join('');
            }
        }
    }

    function saveCurrentStepState() {
        // State is saved in real-time via event listeners
        // This is a hook for any final validation before navigation
    }

    // ============ Recipe Saving ============

    function saveRecipe() {
        const generated = generateRecipe();
        if (!generated) {
            alert('No recipe to save');
            return;
        }

        // Dispatch event for parent page to handle
        document.dispatchEvent(new CustomEvent('cheeseRecipeGenerated', {
            detail: {
                recipe: generated,
                wizardState: { ...wizardState }
            }
        }));

        alert('Recipe ready to save! Check the console for the full recipe data.');
        console.log('Generated cheese recipe:', generated);
    }

    function resetAndRender() {
        resetWizard();
        const container = document.querySelector('.cheese-builder-wizard');
        if (container) {
            renderWizard(container.id);
            attachEventListeners(container.id);
        }
    }

    // ============ Public API ============

    return {
        // Data
        loadData,

        // Navigation
        getCurrentStep,
        goToStep,
        nextStep,
        prevStep,
        resetWizard,

        // State getters
        getState: () => ({ ...wizardState }),

        // Milk
        getMilkTypes,
        setMilk,
        getMilkInfo,

        // Styles
        getCheeseStyles,
        setStyle,
        getStyleInfo,
        getStylesForMilk,

        // Flavors
        getFlavorProfiles,
        getFlavorProfilesForStyle,
        setFlavorProfile,

        // Adulterants
        getCompatibleAdulterants,
        getAdulterantsByCategory,
        addAdulterant,
        removeAdulterant,
        getSelectedAdulterants,
        clearAdulterants,

        // Recipes
        findMatchingRecipes,
        getBaseRecipeForStyle,
        selectRecipe,
        generateRecipe,

        // Rendering
        renderWizard,
        attachEventListeners,

        // Actions
        saveRecipe,
        resetAndRender,

        // Utils
        formatQuantity,
        getStageDisplayName
    };
})();

// Export for Node.js (testing)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CheeseBuilder;
}
