# Milk Substitution Skill

## Purpose

Provide guidance for substituting different milk types (cow, goat, sheep) in cheese-making recipes, including volume adjustments, rennet modifications, and flavor/texture expectations.

## Activation Triggers

- Keywords: sheep milk, goat milk, cow milk, substitute, conversion, cheese
- Working with cheese recipes
- Questions about milk properties for cheese-making

## Data Reference

All substitution data is stored in `data/milk-substitution.json` for both AI guidance and front-end calculator use.

---

## Quick Reference: Substitution Factors

### Volume Conversion (for equivalent cheese yield)

| From | To | Multiply Volume By |
|------|----|--------------------|
| Cow | Sheep | 0.625 (use 62.5% as much) |
| Cow | Goat | 1.0 (same volume) |
| Sheep | Cow | 1.6 (use 60% more) |
| Sheep | Goat | 1.6 (use 60% more) |
| Goat | Cow | 1.0 (same volume) |
| Goat | Sheep | 0.625 (use 62.5% as much) |

### Rennet Adjustment

| Milk Type | Rennet Factor | Notes |
|-----------|---------------|-------|
| Cow | 1.0x (baseline) | Standard recipe amount |
| Goat | 0.6-0.75x | Use 25-40% less rennet |
| Sheep | 0.6-0.7x | Use 30-40% less rennet |

### Calcium Chloride (CaCl2) Guidelines

| Milk Type | Raw | Pasteurized | Ultra-Pasteurized |
|-----------|-----|-------------|-------------------|
| Cow | Not needed | 1/4 tsp/gal | NOT SUITABLE |
| Goat | Not needed | 1/4 tsp/gal | NOT SUITABLE |
| Sheep | Never needed | Not needed | NOT SUITABLE |

**Critical:** Ultra-pasteurized/UHT milk cannot be used for cheese making.

---

## Milk Composition Comparison

| Property | Cow | Goat | Sheep |
|----------|-----|------|-------|
| Fat % | 3.5 | 3.8 | 7.0 |
| Protein % | 3.2 | 3.1 | 5.6 |
| Total Solids % | 12 | 12 | 18 |
| Calcium | Standard | Standard | High |
| Fat Globules | Large | Small | Smallest |

---

## Cheese Yield Comparison

| Milk Type | Yield per Gallon | To Make 1 lb Cheese |
|-----------|------------------|---------------------|
| Cow | ~0.2 lb | 5 quarts (~10 lbs milk) |
| Goat | ~0.2 lb | 5 quarts (~10 lbs milk) |
| Sheep | ~0.75 lb | ~6 lbs milk |

**Key Insight:** Sheep milk produces 3-4x more cheese per gallon than cow or goat milk.

---

## Coagulation Properties

### Speed

1. **Sheep** - Fastest (high calcium, high casein)
2. **Goat** - Faster than cow
3. **Cow** - Standard baseline

### Curd Firmness

1. **Sheep** - Firmest curds
2. **Cow** - Firm curds
3. **Goat** - Soft, fragile curds (low alpha-s1 casein)

### Whey Expulsion (Syneresis)

1. **Goat** - Most pronounced (drains quickly)
2. **Cow** - Standard
3. **Sheep** - Slowest (allow extra draining time)

---

## Flavor Profiles

### Cow Milk Cheese
- **Young:** Mild, creamy, grassy
- **Aged:** Nutty, caramel, complex
- **Character:** Most neutral, highlights aging and cultures

### Goat Milk Cheese
- **Young:** Fresh, tangy, bright
- **Aged:** Peppery, earthy, pronounced
- **Character:** Distinctive tang from capric/caprylic fatty acids

### Sheep Milk Cheese
- **Young:** Rich, buttery, slightly gamy
- **Aged:** Nutty, caramel, robust, complex
- **Character:** Highest richness, famous for Roquefort, Pecorino, Manchego

---

## Temperature Guidelines

| Cheese Type | Temperature Range |
|-------------|-------------------|
| Soft/Fresh | 86-90°F (30-32°C) |
| Semi-Soft | 88-96°F (31-36°C) |
| Hard/Aged | 90-104°F (32-40°C) |
| Swiss/Parmesan | 104-127°F (40-53°C) |

**Important:** Sheep milk should not exceed 104°F (40°C) for most cheeses.

---

## Curd Handling by Milk Type

### Cow Milk
- Standard cut size
- Gentle to moderate stirring
- Baseline handling applies

### Goat Milk
- **Cut larger** than cow
- **Very gentle** stirring required
- Fragile curds - handle delicately
- Pronounced syneresis (drains quickly)

### Sheep Milk
- Standard to smaller cut size
- Gentle stirring
- Firm curds tolerate handling well
- **Slow whey expulsion** - allow extra draining time

---

## Substitution Workflow

### Step 1: Identify Original Milk Type
Check the recipe's intended milk (usually cow if unspecified).

### Step 2: Calculate Volume Adjustment
Use the volume conversion factors above.

**Example:** Recipe calls for 2 gallons cow milk, substituting sheep:
- 2 × 0.625 = 1.25 gallons sheep milk

### Step 3: Adjust Rennet
Apply the rennet factor.

**Example:** Recipe calls for 1/4 tsp rennet (cow), substituting sheep:
- 0.25 × 0.65 = ~0.16 tsp (roughly 1/6 tsp)

### Step 4: Adjust CaCl2
- Sheep milk: Remove CaCl2 entirely
- Goat/Cow pasteurized: Keep CaCl2 as specified
- Raw milk: Remove CaCl2

### Step 5: Note Expected Differences
Document that flavor and texture will differ from the original.

---

## Guardrails

### MUST

- Use data from `data/milk-substitution.json`
- Document all substitution assumptions
- Note flavor/texture differences in recipe notes
- Warn about ultra-pasteurized milk unsuitability

### MUST NOT

- Invent conversion ratios without research basis
- Ignore pH and acidity differences
- Promise identical results when substituting
- Recommend ultra-pasteurized milk for cheese

---

## Famous Cheeses by Milk Type

### Cow Milk
Cheddar, Gouda, Brie, Camembert, Parmesan, Swiss, Mozzarella

### Goat Milk
Chevre, Bucheron, Crottin, Valencay, Humboldt Fog

### Sheep Milk
Roquefort, Pecorino Romano, Manchego, Feta, Ossau-Iraty

---

## Front-End Integration

The milk substitution calculator on the recipe page uses `data/milk-substitution.json` to:
- Allow users to select milk type
- Adjust displayed ingredient quantities
- Show flavor and texture expectations
- Display helpful warnings and notes

See `milk-substitution.js` for implementation details.

---

## Sources

- [Cheese Science Toolkit - Coagulation](https://www.cheesescience.org/coagulation.html)
- [ScienceDirect - Sheep Milk](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/sheep-milk)
- [Cheesemaking.com - Rennet FAQ](https://cheesemaking.com/blogs/learn/faq-rennet-for-cheese-making)
- [New England Cheesemaking - Goat Milk FAQ](https://help.cheesemaking.com/article/24-raw-goats-milk-faqs)
- [Cultures for Health - Raw vs Pasteurized](https://culturesforhealth.com/blogs/learn/cheese-choosing-milk-cheese-making-raw-pasteurized)
- [Tetra Pak Dairy Handbook - Cheese](https://dairyprocessinghandbook.tetrapak.com/chapter/cheese)

---

*Accuracy is more important than speed.*
