# Cheese-Making Recipes — MANDATORY Rules

**This is the most-easily-broken rule in the whole repo.** The Cheese Builder,
Adulterant Companion, and Milk Substitution tools all search for
`category: "cheese"`. If a cheese-making recipe is mis-categorized, **the tool
will not find it**.

---

## When `category: "cheese"` is REQUIRED

A recipe belongs in the `cheese` category if it **creates cheese as the
primary output**. Indicators:

| Indicator | Examples |
|---|---|
| **Contains rennet** | Animal, vegetable, or microbial rennet |
| **Uses cheese cultures** | Mesophilic, thermophilic, Flora Danica, etc. |
| **Cheese-making additives** | Calcium chloride, lipase, annatto |
| **Cheese molds** | Penicillium candidum, P. roqueforti, Brevibacterium, Geotrichum |
| **Citric acid + milk pattern** | Quick cheeses: mozzarella, paneer, ricotta |
| **Cheese-making process phrases** | "cut the curd", "drain the whey", "press the cheese", "age the cheese" |

## When it is NOT cheese-making

Recipes that **use** cheese as an ingredient belong elsewhere:

| Category | Examples |
|---|---|
| `desserts` | Cheesecake, cheese danish, cheese frosting |
| `appetizers` | Fondue, cheese dip, fried cheese curds, cheese ball |
| `mains` | Mac and cheese, quesadillas, grilled cheese, pizza |
| `sides` | Cheese sauce, au gratin, cheese bread |
| `snacks` | Cheese crackers, cheese straws, nachos |

## Examples

```json
// ✅ CORRECT — this MAKES mozzarella
{
  "id": "30-minute-mozzarella",
  "title": "30-Minute Mozzarella",
  "category": "cheese",          // REQUIRED
  "ingredients": [
    {"item": "whole milk", "quantity": "1", "unit": "gallon"},
    {"item": "citric acid", "quantity": "1.5", "unit": "tsp"},
    {"item": "rennet", "quantity": "1/4", "unit": "tablet"}
  ]
}

// ✅ CORRECT — this USES mozzarella, doesn't make it
{
  "id": "caprese-salad",
  "title": "Caprese Salad",
  "category": "salads",          // NOT cheese
  "ingredients": [
    {"item": "fresh mozzarella", "quantity": "8", "unit": "oz"},
    {"item": "tomatoes", "quantity": "2", "unit": "large"}
  ]
}
```

## Cheese-making Tools

| Tool | File | Purpose |
|---|---|---|
| **Cheese Builder** | `cheese-builder.html` | Interactive wizard to find / customize cheese recipes |
| **Adulterant Companion** | `adulterant-companion.js` | Flavor additions (herbs, spices, washes) |
| **Milk Substitution** | `milk-substitution.js` | Convert between milk types |

All three tools search for `category: "cheese"` recipes. **Wrong categorization
= invisible recipe.**
