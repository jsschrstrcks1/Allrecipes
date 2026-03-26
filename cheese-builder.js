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
 *
 * Features:
 * - Matches against 1800+ cheese-making recipes
 * - Suggests adjacent cheeses with technique variations
 * - Pulls tips from recipe notes
 * - Provides general cheese-making guidance
 */

const CheeseBuilder = (function() {
    'use strict';

    // ============ State ============
    let templatesData = null;
    let recipesData = null;
    let milkSubData = null;
    let adulterantsData = null;
    let cheeseRecipesCache = null; // Cached cheese-making recipes

    // ============ Cheese Adjacency Data ============
    // Defines relationships between cheeses and what changes transform one into another
    const CHEESE_ADJACENCIES = {
        // Fresh cheeses
        'ricotta': {
            family: 'fresh',
            adjacent: [
                { cheese: 'mascarpone', change: 'Use cream instead of milk, drain less' },
                { cheese: 'queso fresco', change: 'Press the curds, add more salt' },
                { cheese: 'paneer', change: 'Press firmly, use lemon juice instead of vinegar' },
                { cheese: 'fromage blanc', change: 'Add culture, drain longer for tangier flavor' }
            ]
        },
        'paneer': {
            family: 'fresh',
            adjacent: [
                { cheese: 'halloumi', change: 'Add rennet, poach in whey, brine' },
                { cheese: 'queso blanco', change: 'Use vinegar instead of lemon, less pressing' },
                { cheese: 'ricotta', change: 'Skip pressing, use whey from other cheese' }
            ]
        },
        'cream cheese': {
            family: 'fresh',
            adjacent: [
                { cheese: 'neufchâtel', change: 'Use less cream for lower fat version' },
                { cheese: 'mascarpone', change: 'Use only cream, add tartaric acid' },
                { cheese: 'boursin', change: 'Add garlic and herbs before final mixing' },
                { cheese: 'labneh', change: 'Start with yogurt instead of cultured cream' }
            ]
        },
        'mozzarella': {
            family: 'pasta-filata',
            adjacent: [
                { cheese: 'burrata', change: 'Form pouch, fill with stracciatella and cream' },
                { cheese: 'scamorza', change: 'Air dry the formed cheese, optionally smoke' },
                { cheese: 'provolone', change: 'Age 2-12 months, use lipase for sharper flavor' },
                { cheese: 'oaxaca', change: 'Pull into long ropes, wind into ball shape' },
                { cheese: 'string cheese', change: 'Pull into thin ropes, don\'t ball up' }
            ]
        },
        'cheddar': {
            family: 'cheddared',
            adjacent: [
                { cheese: 'colby', change: 'Wash curds with water, skip cheddaring' },
                { cheese: 'monterey jack', change: 'Higher moisture, shorter aging, milder culture' },
                { cheese: 'leicester', change: 'Add annatto for orange color, crumblier texture' },
                { cheese: 'gloucester', change: 'Use evening milk + morning cream, age 4+ months' },
                { cheese: 'derby', change: 'Moister curd, add sage leaves for Sage Derby' },
                { cheese: 'dunlop', change: 'Scottish variant - use full-fat milk, milder culture' },
                { cheese: 'caerphilly', change: 'Higher acid, shorter aging (2-8 weeks), crumbly' }
            ]
        },
        'gouda': {
            family: 'washed-curd',
            adjacent: [
                { cheese: 'edam', change: 'Lower fat milk, smaller wheels, age shorter' },
                { cheese: 'leyden', change: 'Add cumin and caraway seeds to curds' },
                { cheese: 'maasdam', change: 'Add propionic bacteria for eyes (holes)' },
                { cheese: 'fontina', change: 'Raw milk, washed rind, cave aging' },
                { cheese: 'havarti', change: 'Higher moisture, more washing, cream addition' }
            ]
        },
        'swiss': {
            family: 'alpine',
            adjacent: [
                { cheese: 'gruyère', change: 'Smaller/fewer eyes, longer aging, nuttier' },
                { cheese: 'emmental', change: 'Larger wheels, more propionic for bigger eyes' },
                { cheese: 'jarlsberg', change: 'Norwegian variant - sweeter, milder' },
                { cheese: 'appenzeller', change: 'Wash rind with herbed brine' },
                { cheese: 'comté', change: 'French variant - raw milk, longer aging' },
                { cheese: 'beaufort', change: 'Concave wheel shape, no eyes, alpine pastures' }
            ]
        },
        'brie': {
            family: 'bloomy',
            adjacent: [
                { cheese: 'camembert', change: 'Smaller wheel, stronger flavor, thicker rind' },
                { cheese: 'coulommiers', change: 'Thicker wheel, creamier center' },
                { cheese: 'triple cream', change: 'Add cream for 75%+ butterfat' },
                { cheese: 'saint-andré', change: 'Triple cream with thicker rind' }
            ]
        },
        'feta': {
            family: 'brined',
            adjacent: [
                { cheese: 'halloumi', change: 'Add mint, poach in whey, higher salt brine' },
                { cheese: 'sirene', change: 'Bulgarian variant - cow milk, less tangy' },
                { cheese: 'beyaz peynir', change: 'Turkish variant - milder, cubed' },
                { cheese: 'queso fresco', change: 'Skip brining, eat fresh, milder' }
            ]
        },
        'blue cheese': {
            family: 'blue',
            adjacent: [
                { cheese: 'roquefort', change: 'Use sheep milk, cave age' },
                { cheese: 'gorgonzola', change: 'Italian - creamier, milder (dolce) or firmer (piccante)' },
                { cheese: 'stilton', change: 'English - crumbly, pierced later, longer aging' },
                { cheese: 'danish blue', change: 'Higher moisture, creamier, sharper' },
                { cheese: 'cambozola', change: 'Combine blue mold with bloomy rind' }
            ]
        },
        'parmesan': {
            family: 'grana',
            adjacent: [
                { cheese: 'grana padano', change: 'Shorter aging (9-24mo), milder flavor' },
                { cheese: 'pecorino romano', change: 'Use sheep milk, saltier, sharper' },
                { cheese: 'asiago', change: 'Shorter aging, softer when young' },
                { cheese: 'piave', change: 'Northeastern Italian, sweeter, less granular' }
            ]
        },
        'chevre': {
            family: 'fresh-goat',
            adjacent: [
                { cheese: 'crottin', change: 'Form into small rounds, age with bloomy rind' },
                { cheese: 'valencay', change: 'Pyramid shape, ash coating' },
                { cheese: 'bucheron', change: 'Log shape, age for soft center' },
                { cheese: 'humboldt fog', change: 'Ash layer in middle, bloomy rind' }
            ]
        },
        'washed rind': {
            family: 'washed',
            adjacent: [
                { cheese: 'taleggio', change: 'Italian - square, mild, washed with brine' },
                { cheese: 'époisses', change: 'French - wash with marc de Bourgogne' },
                { cheese: 'limburger', change: 'German - stronger, smaller, brick shape' },
                { cheese: 'munster', change: 'Alsatian - wash with brine, milder than limburger' },
                { cheese: 'reblochon', change: 'French alpine - wash gently, use raw milk' }
            ]
        }
    };

    // General cheese-making tips organized by topic
    const GENERAL_TIPS = {
        milk: [
            'Never use ultra-pasteurized (UHT) milk - it won\'t form proper curds',
            'Raw milk makes the best cheese but requires extra food safety care',
            'Pasteurized milk may need calcium chloride to help curds set',
            'Homogenized milk works fine but may produce slightly softer curds',
            'Goat milk curds are more fragile - handle gently',
            'Sheep milk produces 50-80% more cheese per gallon than cow milk'
        ],
        temperature: [
            'Use a reliable thermometer - temperature control is crucial',
            'Heat milk slowly and stir frequently to prevent scorching',
            'Most cheeses ripen at 86-102°F (30-39°C)',
            'Thermophilic cultures need higher temps (104-113°F)',
            'Mesophilic cultures work at moderate temps (68-102°F)',
            'Even 2°F difference can affect your final cheese'
        ],
        rennet: [
            'Less rennet = softer cheese, more rennet = firmer cheese',
            'Dilute rennet in cool non-chlorinated water before adding',
            'Stir rennet in gently for only 30-60 seconds',
            'Don\'t disturb the milk while rennet is working',
            'Goat and sheep milk need 30-40% less rennet than cow milk',
            'Check for "clean break" before cutting curds'
        ],
        curds: [
            'Cut curds uniformly for even moisture content',
            'Smaller curds = drier cheese, larger curds = moister cheese',
            'Stir gently to avoid smashing curds',
            'Stacking/cheddaring curds develops tangy flavor',
            'Heating curds expels more whey = firmer cheese',
            'Fresh curds squeak against your teeth when ready'
        ],
        salt: [
            'Salt controls moisture and slows bacterial growth',
            'Brine concentration affects rind development',
            'Dry salting pulls more moisture than brining',
            'Under-salted cheese spoils; over-salted is harsh',
            'Flake salt dissolves faster and distributes more evenly',
            'Iodized salt can inhibit cultures - use cheese salt or kosher'
        ],
        aging: [
            'Higher humidity = softer rind, lower humidity = harder rind',
            'Turn cheese regularly to prevent moisture pooling',
            'Cave temperature (50-55°F) is ideal for most aging',
            'A dedicated cheese fridge maintains consistent conditions',
            'Vacuum sealing prevents mold on hard cheeses',
            'Waxing protects cheese while allowing some gas exchange'
        ],
        troubleshooting: [
            'Weak curds? Add calcium chloride next time',
            'Bitter cheese? May be over-renneted or contaminated',
            'No curds forming? Check rennet freshness and milk quality',
            'Spongy texture? Too much whey trapped in curds',
            'Off flavors? Check for contamination or old cultures',
            'Cracks in rind? Humidity too low during aging'
        ]
    };

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

    // List of cheese names for detection
    const CHEESE_NAMES = [
        'ricotta', 'mozzarella', 'cheddar', 'gouda', 'feta', 'brie', 'camembert',
        'parmesan', 'pecorino', 'manchego', 'gruyere', 'gruyère', 'swiss', 'havarti',
        'muenster', 'münster', 'colby', 'jack', 'provolone', 'asiago', 'fontina',
        'halloumi', 'paneer', 'queso', 'chevre', 'chèvre', 'boursin', 'mascarpone',
        'cream cheese', 'cottage cheese', 'farmer', 'fromage', 'stilton', 'roquefort',
        'gorgonzola', 'blue cheese', 'taleggio', 'limburger', 'edam', 'emmental',
        'jarlsberg', 'raclette', 'comté', 'comte', 'reblochon', 'epoisses', 'époisses',
        'tomme', 'caciocavallo', 'scamorza', 'burrata', 'oaxaca', 'cotija', 'labneh',
        'quark', 'skyr', 'tvorog', 'kashkaval', 'sirene', 'appenzeller', 'beaufort',
        'caerphilly', 'gloucester', 'leicester', 'derby', 'dunlop', 'wensleydale',
        'lancashire', 'cheshire', 'crottin', 'valencay', 'valençay', 'bucheron',
        'neufchâtel', 'neufchatel', 'coulommiers', 'pont', 'langres', 'maroilles',
        'munster', 'brick', 'limburger', 'tilsit', 'port salut', 'saint-nectaire',
        'morbier', 'raclette', 'idiazabal', 'idiazábal', 'mahon', 'mahón', 'tetilla',
        'manchego', 'zamorano', 'graviera', 'kefalograviera', 'kasseri', 'kefalotyri',
        'panir', 'chhena', 'kalari', 'bandel', 'sulguni', 'imeruli', 'chechil'
    ];

    /**
     * Detect if a recipe is for MAKING cheese (not just using it)
     */
    function isCheeseMAKINGRecipe(recipe) {
        const title = (recipe.title || '').toLowerCase();
        const desc = (recipe.description || '').toLowerCase();
        const tags = (recipe.tags || []).join(' ').toLowerCase();

        // Already categorized as cheese
        if (recipe.category === 'cheese') return true;

        // Check ingredients for definitive making indicators
        let ingredientsText = '';
        for (const ing of (recipe.ingredients || [])) {
            ingredientsText += ' ' + (ing.item || '').toLowerCase();
        }

        // Must have rennet OR culture in ingredients (definitive cheese-making)
        const hasRennet = ingredientsText.includes('rennet');
        const hasCulture = ['mesophilic', 'thermophilic', 'culture', 'starter'].some(c => ingredientsText.includes(c));
        const hasCitric = ingredientsText.includes('citric acid') && ingredientsText.includes('milk');

        // If has definitive making ingredients, it's a cheese recipe
        if (hasRennet || hasCulture) return true;
        if (hasCitric) return true;

        // Named cheese in title with making indicators
        const isNamedCheese = CHEESE_NAMES.some(cn => title.includes(cn));
        const titleSuggestsMaking = ['homemade', 'make ', 'making', 'recipe', 'style', 'traditional', 'authentic', 'artisan'].some(w => title.includes(w));

        if (isNamedCheese && titleSuggestsMaking && ingredientsText.includes('milk')) {
            return true;
        }

        // Named cheese as entire title (e.g., "Gouda Cheese", "Brie")
        if (isNamedCheese && ingredientsText.includes('milk') && !title.includes('with ') && !title.includes('and ')) {
            return true;
        }

        return false;
    }

    /**
     * Get all cheese-making recipes (cached for performance)
     */
    function getCheeseRecipes() {
        if (cheeseRecipesCache) return cheeseRecipesCache;
        if (!recipesData) return [];

        cheeseRecipesCache = recipesData.filter(isCheeseMAKINGRecipe);
        console.log(`Cheese recipes cached: ${cheeseRecipesCache.length}`);
        return cheeseRecipesCache;
    }

    /**
     * Detect which style family a recipe belongs to based on its name
     */
    function detectRecipeStyle(recipe) {
        const title = (recipe.title || '').toLowerCase();

        const stylePatterns = {
            'fresh': ['ricotta', 'paneer', 'queso fresco', 'queso blanco', 'cream cheese', 'mascarpone',
                      'cottage', 'farmer', 'fromage blanc', 'labneh', 'quark', 'tvorog', 'chhena', 'fresh'],
            'soft': ['brie', 'camembert', 'chevre', 'chèvre', 'boursin', 'neufchâtel', 'neufchatel'],
            'semi-soft': ['mozzarella', 'halloumi', 'feta', 'havarti', 'muenster', 'münster', 'fontina',
                          'colby', 'oaxaca', 'scamorza', 'burrata', 'provolone', 'string', 'jack'],
            'semi-hard': ['cheddar', 'gouda', 'edam', 'gruyere', 'gruyère', 'swiss', 'emmental',
                          'jarlsberg', 'raclette', 'comté', 'comte', 'tomme', 'caciocavallo',
                          'kashkaval', 'beaufort', 'appenzeller', 'leicester', 'gloucester',
                          'derby', 'dunlop', 'caerphilly', 'lancashire', 'wensleydale'],
            'hard': ['parmesan', 'parmigiano', 'pecorino', 'asiago', 'grana', 'romano', 'manchego',
                     'aged', 'stravecchio', 'piave', 'sbrinz', 'idiazabal', 'idiazábal'],
            'bloomy': ['brie', 'camembert', 'coulommiers', 'triple cream', 'saint-andré',
                       'brillat-savarin', 'robiola'],
            'washed': ['taleggio', 'limburger', 'epoisses', 'époisses', 'munster', 'münster',
                       'langres', 'pont', 'reblochon', 'maroilles', 'washed'],
            'blue': ['stilton', 'roquefort', 'gorgonzola', 'blue', 'danish blue', 'cambozola',
                     'cabrales', 'valdeon', 'valdeón']
        };

        for (const [style, patterns] of Object.entries(stylePatterns)) {
            if (patterns.some(p => title.includes(p))) {
                return style;
            }
        }

        return 'other';
    }

    function findMatchingRecipes() {
        if (!recipesData || !wizardState.style) return [];

        const style = wizardState.style;
        const flavorProfile = wizardState.flavorProfile;
        const milkType = wizardState.milk?.type;
        const keywords = templatesData?.recipe_matching?.style_keywords[style] || [];
        const flavorKeywords = flavorProfile ?
            (templatesData?.recipe_matching?.flavor_keywords[flavorProfile] || []) : [];

        // Get all cheese-making recipes (expanded matching)
        const cheeseRecipes = getCheeseRecipes();

        // Score each recipe
        const scored = cheeseRecipes.map(recipe => {
            let score = 0;
            const title = (recipe.title || '').toLowerCase();
            const tags = (recipe.tags || []).map(t => t.toLowerCase());
            const detectedStyle = detectRecipeStyle(recipe);

            // Style matching - big boost for same style
            if (detectedStyle === style) {
                score += 20;
            } else if (detectedStyle === 'other') {
                score += 2; // Small boost for uncategorized
            }

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

            // Milk type matching
            if (milkType === 'goat' && (title.includes('goat') || title.includes('chevre') || title.includes('chèvre'))) {
                score += 15;
            }
            if (milkType === 'sheep' && (title.includes('sheep') || title.includes('pecorino') || title.includes('manchego') || title.includes('roquefort'))) {
                score += 15;
            }

            // Boost recipes with milk_substitutions enabled
            if (recipe.milk_substitutions?.enabled) score += 3;

            // Boost recipes with notes (they have tips!)
            if (recipe.notes && recipe.notes.length > 2) score += 2;

            // Adulterant matching
            const adulterantNames = wizardState.adulterants.map(a => (a.name || a.id || '').toLowerCase());
            adulterantNames.forEach(aName => {
                const shortName = aName.replace(' powder', '').replace(' dried', '').replace(' ground', '');
                if (title.includes(shortName)) score += 12;
            });

            return { recipe, score, detectedStyle };
        });

        // Sort by score and return top matches
        return scored
            .filter(s => s.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 20) // Return more matches for variety
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
        const { milk, style, flavorProfile, adulterants, selectedRecipe, matchedRecipes } = wizardState;

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

        // Get matched recipes for tips extraction
        const matches = matchedRecipes.length > 0 ? matchedRecipes : findMatchingRecipes();

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
            adjacentCheeses: getAdjacentCheeses(recipe.data, style),
            recipeTips: getTipsFromRecipeNotes(matches),
            generalTips: getGeneralEducationalTips(style, milk.type),
            didYouKnow: getDidYouKnowFacts().slice(0, 3), // Random 3 facts
            yield: estimateYield(milk, milkInfo),
            matchedRecipeCount: getCheeseRecipes().length,
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

        // Milk-specific tips
        if (milkInfo?.notes) {
            tips.push({ category: 'milk', text: milkInfo.notes });
        }

        if (milk.type === 'goat') {
            tips.push({ category: 'milk', text: 'Goat milk curds are fragile - handle very gently and cut larger.' });
            tips.push({ category: 'milk', text: 'Goat milk is naturally homogenized - no cream line means smooth texture.' });
        }
        if (milk.type === 'sheep') {
            tips.push({ category: 'milk', text: 'Sheep milk produces 50-80% more cheese per gallon - adjust your recipe accordingly.' });
            tips.push({ category: 'milk', text: 'Sheep milk has more calcium - skip the calcium chloride even with pasteurized.' });
        }
        if (milk.processing === 'pasteurized') {
            tips.push({ category: 'milk', text: 'Pasteurized milk may benefit from 1/4 tsp calcium chloride per gallon.' });
        }

        // Style-specific tips
        const styleInfo = getStyleInfo(style);
        if (styleInfo?.notes) {
            tips.push({ category: 'style', text: styleInfo.notes });
        }

        // Add general tips relevant to the style
        if (style === 'fresh') {
            tips.push({ category: 'technique', text: 'Fresh cheese should be eaten within 5-7 days for best flavor.' });
            tips.push({ category: 'technique', text: 'Drain longer for firmer cheese, less for creamier.' });
        }
        if (style === 'semi-hard' || style === 'hard') {
            tips.push({ category: 'aging', text: 'Flip your cheese daily for the first week, then weekly during aging.' });
            tips.push({ category: 'aging', text: 'Maintain 80-85% humidity during aging to prevent cracking.' });
        }
        if (style === 'bloomy') {
            tips.push({ category: 'technique', text: 'White mold needs air circulation - don\'t wrap tightly.' });
            tips.push({ category: 'aging', text: 'Ripen at 50-55°F until the rind is fully developed.' });
        }
        if (style === 'washed') {
            tips.push({ category: 'technique', text: 'Wash rind every 2-3 days with brine or alcohol.' });
            tips.push({ category: 'technique', text: 'The orange color comes from B. linens bacteria - it\'s supposed to smell strong!' });
        }
        if (style === 'blue') {
            tips.push({ category: 'technique', text: 'Pierce the cheese with sterile needles to allow oxygen for blue mold growth.' });
            tips.push({ category: 'aging', text: 'Blue cheeses need higher humidity (90-95%) than other styles.' });
        }

        // Adulterant tips
        if (adulterants.length > 0) {
            tips.push({ category: 'adulterant', text: 'Add adulterants after salting to preserve their flavor.' });
        }
        if (adulterants.length > 2) {
            tips.push({ category: 'adulterant', text: 'With multiple additions, start with half quantities and adjust to taste.' });
        }

        // Add relevant general tips
        const relevantGeneralTips = getRelevantGeneralTips(style, milk);
        relevantGeneralTips.forEach(tip => {
            tips.push({ category: 'general', text: tip });
        });

        return tips;
    }

    /**
     * Get general tips relevant to the current cheese style and milk
     */
    function getRelevantGeneralTips(style, milk) {
        const relevant = [];

        // Always include some temperature tips
        relevant.push(GENERAL_TIPS.temperature[Math.floor(Math.random() * 2)]);

        // Style-specific general tips
        if (['semi-hard', 'hard'].includes(style)) {
            relevant.push(GENERAL_TIPS.aging[Math.floor(Math.random() * GENERAL_TIPS.aging.length)]);
            relevant.push(GENERAL_TIPS.curds[Math.floor(Math.random() * GENERAL_TIPS.curds.length)]);
        }
        if (['fresh', 'soft'].includes(style)) {
            relevant.push(GENERAL_TIPS.curds[0]); // Cut uniformly
        }
        if (milk.processing === 'pasteurized') {
            relevant.push(GENERAL_TIPS.milk[2]); // CaCl2 tip
        }

        // Always add a salt tip
        relevant.push(GENERAL_TIPS.salt[Math.floor(Math.random() * GENERAL_TIPS.salt.length)]);

        // Include a troubleshooting tip
        relevant.push(GENERAL_TIPS.troubleshooting[Math.floor(Math.random() * GENERAL_TIPS.troubleshooting.length)]);

        return relevant.slice(0, 4); // Limit to 4 general tips
    }

    /**
     * Get adjacent cheeses - what other cheeses can be made with small technique changes
     */
    function getAdjacentCheeses(recipe, style) {
        const adjacent = [];
        const title = (recipe?.title || recipe?.name || '').toLowerCase();

        // Find which cheese family this belongs to
        for (const [cheeseName, data] of Object.entries(CHEESE_ADJACENCIES)) {
            if (title.includes(cheeseName) || data.family === style) {
                // Add adjacent cheeses with their transformation tips
                data.adjacent.forEach(adj => {
                    adjacent.push({
                        cheese: adj.cheese,
                        change: adj.change,
                        family: data.family
                    });
                });
                break; // Found the family, stop looking
            }
        }

        // If no specific match, suggest based on style
        if (adjacent.length === 0) {
            const styleAdjacencies = {
                'fresh': [
                    { cheese: 'ricotta', change: 'Use whey from other cheese, heat to 200°F' },
                    { cheese: 'paneer', change: 'Press firmly for 30+ minutes' },
                    { cheese: 'queso fresco', change: 'Add more salt, press lightly' }
                ],
                'semi-soft': [
                    { cheese: 'mozzarella', change: 'Stretch curds in hot water until smooth' },
                    { cheese: 'halloumi', change: 'Poach in whey, add mint, brine' },
                    { cheese: 'feta', change: 'Cube and brine for 5+ days' }
                ],
                'semi-hard': [
                    { cheese: 'cheddar', change: 'Stack and flip curds (cheddaring) for 2 hours' },
                    { cheese: 'gouda', change: 'Wash curds with warm water before pressing' },
                    { cheese: 'colby', change: 'Wash curds, skip cheddaring, press' }
                ],
                'hard': [
                    { cheese: 'parmesan', change: 'Use partial skim, age 12+ months' },
                    { cheese: 'pecorino', change: 'Use sheep milk, age 8+ months' },
                    { cheese: 'asiago', change: 'Age 4-6 months for table cheese' }
                ],
                'bloomy': [
                    { cheese: 'brie', change: 'Spray with P. candidum, ripen 4-6 weeks' },
                    { cheese: 'camembert', change: 'Smaller molds, thicker rind, stronger flavor' }
                ],
                'washed': [
                    { cheese: 'taleggio', change: 'Wash with brine every 2-3 days' },
                    { cheese: 'munster', change: 'Wash with salt brine, milder than limburger' }
                ],
                'blue': [
                    { cheese: 'stilton', change: 'Pierce at 4 weeks, age 9+ weeks' },
                    { cheese: 'gorgonzola', change: 'Italian style - creamier, milder' }
                ]
            };

            if (styleAdjacencies[style]) {
                styleAdjacencies[style].forEach(adj => {
                    adjacent.push({ ...adj, family: style });
                });
            }
        }

        return adjacent.slice(0, 5); // Return top 5 suggestions
    }

    /**
     * Extract tips from matched recipe notes
     */
    function getTipsFromRecipeNotes(matchedRecipes) {
        const tips = [];

        matchedRecipes.slice(0, 5).forEach(recipe => {
            const notes = recipe.notes || [];
            notes.forEach(note => {
                // Filter for actual tips (not just metadata)
                if (note.length > 20 && note.length < 200) {
                    if (!note.toLowerCase().includes('source:') &&
                        !note.toLowerCase().includes('adapted from') &&
                        !note.toLowerCase().includes('original recipe')) {
                        tips.push({
                            text: note,
                            source: recipe.title
                        });
                    }
                }
            });
        });

        return tips.slice(0, 6); // Limit to 6 recipe tips
    }

    /**
     * Get general educational tips from all cheese recipes in database
     * These are technique tips that apply broadly
     */
    function getGeneralEducationalTips(style, milkType) {
        const allTips = [];
        const cheeseRecipes = getCheeseRecipes();

        // Keywords that indicate educational/technique content
        const educationalKeywords = [
            'technique', 'method', 'traditional', 'tip', 'important', 'crucial',
            'must', 'should', 'always', 'never', 'careful', 'ensure', 'prevent',
            'avoid', 'helps', 'creates', 'develops', 'produces', 'results in'
        ];

        // Style-related keywords for filtering
        const styleKeywords = {
            'fresh': ['drain', 'press', 'whey', 'curd', 'acid', 'temperature'],
            'soft': ['mold', 'rind', 'ripen', 'bloom', 'culture', 'age'],
            'semi-soft': ['stretch', 'brine', 'salt', 'press', 'curd'],
            'semi-hard': ['press', 'age', 'flip', 'wax', 'cheddar', 'curd', 'salt'],
            'hard': ['age', 'press', 'crystal', 'granular', 'long', 'months'],
            'bloomy': ['penicillium', 'candidum', 'white', 'rind', 'ripen', 'mold'],
            'washed': ['wash', 'brine', 'linens', 'orange', 'rind', 'pungent'],
            'blue': ['pierce', 'roqueforti', 'blue', 'vein', 'mold', 'humidity']
        };

        const relevantKeywords = styleKeywords[style] || [];

        // Collect educational notes from recipes
        cheeseRecipes.forEach(recipe => {
            const notes = recipe.notes || [];
            notes.forEach(note => {
                const lower = note.toLowerCase();

                // Skip metadata
                if (lower.includes('source:') || lower.includes('adapted from') ||
                    lower.includes('calories') || lower.includes('protein') ||
                    note.length < 30 || note.length > 200) {
                    return;
                }

                // Check if it's educational
                const isEducational = educationalKeywords.some(kw => lower.includes(kw));
                const isRelevantToStyle = relevantKeywords.some(kw => lower.includes(kw));

                if (isEducational || isRelevantToStyle) {
                    allTips.push({
                        text: note,
                        source: recipe.title,
                        relevance: (isEducational ? 1 : 0) + (isRelevantToStyle ? 2 : 0)
                    });
                }
            });
        });

        // Sort by relevance and deduplicate similar tips
        const sorted = allTips
            .sort((a, b) => b.relevance - a.relevance)
            .filter((tip, index, self) => {
                // Remove very similar tips
                const firstWords = tip.text.split(' ').slice(0, 4).join(' ').toLowerCase();
                return index === self.findIndex(t =>
                    t.text.split(' ').slice(0, 4).join(' ').toLowerCase() === firstWords
                );
            });

        // Return a good mix
        return sorted.slice(0, 8);
    }

    /**
     * Get "Did You Know" facts about cheese-making
     */
    function getDidYouKnowFacts() {
        return [
            { text: 'Cheese has been made for over 7,000 years - it\'s one of humanity\'s oldest foods.', category: 'history' },
            { text: 'It takes about 10 pounds of milk to make 1 pound of hard cheese.', category: 'yield' },
            { text: 'The holes in Swiss cheese are caused by bacteria releasing carbon dioxide.', category: 'science' },
            { text: 'Blue cheese mold (P. roqueforti) is related to the mold that makes penicillin.', category: 'science' },
            { text: 'Cheddar isn\'t naturally orange - the color comes from annatto dye.', category: 'history' },
            { text: 'Parmesan must be aged at least 12 months; some age for 36+ months.', category: 'aging' },
            { text: 'Rennet was traditionally made from calf stomach - now vegetable rennet is common.', category: 'history' },
            { text: 'The curd "squeaks" when fresh mozzarella is properly made.', category: 'technique' },
            { text: 'Cheese caves maintain natural temperature (50-55°F) and humidity perfect for aging.', category: 'aging' },
            { text: 'Washed rind cheeses get their orange color from B. linens bacteria, not dye.', category: 'science' },
            { text: 'Sheep milk has nearly twice the fat of cow milk, making richer cheese.', category: 'milk' },
            { text: 'Halloumi\'s high melting point comes from being cooked in whey.', category: 'technique' },
            { text: 'The word "cheese" comes from Latin "caseus" meaning "to ferment."', category: 'history' },
            { text: 'Brie was called "the king of cheeses" by French diplomat Talleyrand in 1815.', category: 'history' },
            { text: 'Fresh cheese has the shortest shelf life; hard aged cheese can last years.', category: 'storage' }
        ];
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

        // Group tips by category
        const tipsByCategory = {};
        (generated.tips || []).forEach(tip => {
            const cat = tip.category || 'general';
            if (!tipsByCategory[cat]) tipsByCategory[cat] = [];
            tipsByCategory[cat].push(tip.text || tip);
        });

        const categoryLabels = {
            milk: 'Milk Tips',
            style: 'Style Tips',
            technique: 'Technique Tips',
            aging: 'Aging Tips',
            adulterant: 'Adulterant Tips',
            general: 'General Tips'
        };

        return `
            <div class="step-recipe">
                <div class="recipe-header">
                    <h2>${generated.title}</h2>
                    <p class="recipe-meta">
                        <span class="style">${generated.styleInfo?.name}</span>
                        <span class="yield">Yield: ${generated.yield.formatted}</span>
                        <span class="milk">${generated.milk.typeName}</span>
                    </p>
                    <p class="recipe-stats">
                        Matched from ${generated.matchedRecipeCount?.toLocaleString() || '1,800+'} cheese-making recipes
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

                ${generated.adjacentCheeses && generated.adjacentCheeses.length > 0 ? `
                    <div class="recipe-section adjacent-cheeses">
                        <h3>Try These Variations</h3>
                        <p class="section-intro">With small technique changes, you can also make:</p>
                        <div class="adjacent-grid">
                            ${generated.adjacentCheeses.map(adj => `
                                <div class="adjacent-card">
                                    <h4>${adj.cheese.charAt(0).toUpperCase() + adj.cheese.slice(1)}</h4>
                                    <p class="change-tip">${adj.change}</p>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${Object.keys(tipsByCategory).length > 0 ? `
                    <div class="recipe-section tips">
                        <h3>Tips & Guidance</h3>
                        ${Object.entries(tipsByCategory).map(([cat, tips]) => `
                            <div class="tip-category">
                                <h4>${categoryLabels[cat] || cat}</h4>
                                <ul>
                                    ${tips.map(tip => `<li>${tip}</li>`).join('')}
                                </ul>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}

                ${generated.recipeTips && generated.recipeTips.length > 0 ? `
                    <div class="recipe-section recipe-notes">
                        <h3>From Our Recipe Collection</h3>
                        <p class="section-intro">Tips from similar recipes in the database:</p>
                        <ul class="recipe-tip-list">
                            ${generated.recipeTips.map(tip => `
                                <li>
                                    <span class="tip-text">${tip.text}</span>
                                    <span class="tip-source">— ${tip.source}</span>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                ` : ''}

                ${generated.generalTips && generated.generalTips.length > 0 ? `
                    <div class="recipe-section general-tips-section">
                        <h3>General Cheese-Making Tips</h3>
                        <p class="section-intro">Wisdom from our collection of ${generated.matchedRecipeCount?.toLocaleString() || '1,800+'} cheese recipes:</p>
                        <div class="general-tips-grid">
                            ${generated.generalTips.map(tip => `
                                <div class="general-tip-card">
                                    <p class="tip-text">${tip.text}</p>
                                    <span class="tip-source">— ${tip.source}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                ` : ''}

                ${generated.didYouKnow && generated.didYouKnow.length > 0 ? `
                    <div class="recipe-section did-you-know">
                        <h3>Did You Know?</h3>
                        <div class="facts-list">
                            ${generated.didYouKnow.map(fact => `
                                <div class="fact-item">
                                    <span class="fact-icon">💡</span>
                                    <span class="fact-text">${fact.text}</span>
                                </div>
                            `).join('')}
                        </div>
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
