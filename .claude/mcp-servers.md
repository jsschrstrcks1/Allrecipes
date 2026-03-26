# MCP Servers for Recipe Archive

*Optional enhancements for AI-assisted recipe work*

This guide outlines Model Context Protocol (MCP) servers that can enhance recipe transcription and data enrichment. **These are optional** - the archive is fully functional without them.

---

## Recommended Servers

### 1. OpenNutrition MCP (Priority: High)

**Purpose:** Nutritional data lookup for recipe enrichment

**Features:**
- Access to 300,000+ food items with complete nutritional profiles
- Works offline after initial setup
- USDA and international food databases

**Use Cases:**
- Adding nutrition facts to recipes
- Verifying nutritional calculations
- Looking up ingredient nutritional values

**Installation:** See [OpenNutrition MCP documentation](https://github.com/open-nutrition/mcp-server)

---

### 2. Kitchen MCP (Priority: Medium)

**Purpose:** Ingredient queries and substitutions

**Features:**
- Ingredient substitution recommendations
- Measurement conversions
- Diet preference filtering

**Use Cases:**
- Suggesting ingredient alternatives
- Converting between metric and imperial
- Identifying allergen-free substitutions

---

### 3. Spoonacular MCP (Priority: Medium)

**Purpose:** Comprehensive recipe and food API

**Features:**
- Recipe search by ingredients
- Nutritional analysis
- Substitution suggestions
- Requires API key (free tier available)

**Use Cases:**
- Cross-referencing transcribed recipes
- Verifying ingredient combinations
- Nutritional enrichment

---

### 4. MealDB MCP (Priority: Low)

**Purpose:** Recipe cross-reference database

**Features:**
- Access to TheMealDB recipe database
- No authentication required
- Basic recipe verification

**Use Cases:**
- Verifying recipe authenticity
- Checking standard ingredient ratios
- Cross-referencing cooking methods

---

## Integration Patterns

### Pattern 1: Ingredient Substitution

When transcribing a recipe with hard-to-find ingredients:

1. Query Kitchen MCP for substitution options
2. Add substitution notes to recipe `notes` field
3. Preserve original ingredient in main list

### Pattern 2: Nutritional Enrichment

When adding nutrition data to recipes:

1. Look up each ingredient in OpenNutrition MCP
2. Calculate per-serving values based on `servings_yield`
3. Document assumptions in `nutrition.assumptions`
4. Set `nutrition.status` to "complete", "partial", or "insufficient_data"

### Pattern 3: Recipe Verification

When transcribing and uncertain about ratios:

1. Search Spoonacular/MealDB for similar recipes
2. Compare ingredient ratios
3. Flag significant discrepancies for review
4. **Never auto-correct** - only flag for human review

---

## Installation Priority

1. **OpenNutrition MCP** - Most useful for nutrition data pass
2. **Kitchen MCP** - Helpful for substitutions
3. **Spoonacular MCP** - Good for verification
4. **MealDB MCP** - Supplementary

---

## Important Notes

- MCP servers are **optional enhancements**
- The archive works fully without them
- **Never use MCP data to invent recipe content**
- MCP data should inform, not override, original sources
- Always document when MCP-sourced data is used

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."*
— Proverbs 31:27
