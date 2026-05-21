# Recipe Schema — Other Family Recipes

```json
{
  "id": "stable-slug-like-recipe-name",
  "collection": "all",
  "collection_display": "Other Family Recipes",
  "title": "",
  "category": "desserts",
  "attribution": "",
  "source_note": "e.g., Kindle cookbook, magazine clipping",
  "description": "1-2 sentences",
  "servings_yield": "",
  "prep_time": "",
  "cook_time": "",
  "total_time": "",
  "ingredients": [
    {"item": "", "quantity": "", "unit": "", "prep_note": ""}
  ],
  "instructions": [
    {"step": 1, "text": ""}
  ],
  "temperature": "",
  "pan_size": "",
  "notes": [""],
  "tips": ["Chef tips, technique notes"],
  "substitutions": [{"original": "", "substitute": "", "note": ""}],
  "tags": ["dessert", "holiday", "bread", "casserole"],
  "confidence": {
    "overall": "high|medium|low",
    "flags": []
  },
  "image_refs": ["IMG_001.PNG"],   // HANDWRITTEN images only
  "page_continuation": {"continues_from": "", "continues_to": ""},
  "components": ["recipe-id-of-sub-recipe"],
  "component_of": ["recipe-id-of-parent"],
  "is_component": false,
  "conversions": {
    "has_conversions": true,
    "conversion_assumptions": [],
    "ingredients_metric": [],
    "temperature_c": ""
  },
  "nutrition": {
    "status": "complete|partial|insufficient_data",
    "per_serving": {},
    "missing_inputs": [],
    "assumptions": []
  }
}
```

## Quality Checklist

- [ ] Cross-check ingredient quantities against instructions.
- [ ] Flag implausible amounts (e.g., "4 cups salt" is probably an OCR error).
- [ ] Preserve original voice where possible.
- [ ] Verify temperatures are reasonable (most baking: 300–425°F).
- [ ] Check liquid-to-dry ratios make sense.
- [ ] Ensure baking times align with temperatures and pan sizes.

## Categories

```
appetizers, beverages, breads, breakfast, cheese, desserts,
mains, salads, sides, soups, snacks
```

**Cheese-making recipes MUST use `category: "cheese"`** — see
[`CHEESE_RULES.md`](CHEESE_RULES.md).
