# Image Retention Policy — Other Family Recipes

**Only handwritten recipe images are saved and linked in `image_refs`.**

After extracting a recipe from an image:

| Source type | Image retention | `image_refs` |
|---|---|---|
| **Handwritten** (pen/pencil on paper) | **Keep** — irreplaceable originals | Populate with filename(s) |
| **Kindle screenshots** | **Do not link** — recipe data is the deliverable | `[]` |
| **Magazine clippings** | **Do not link** | `[]` |
| **Typed cards** | **Do not link** | `[]` |
| **Cookbook pages** | **Do not link** | `[]` |

## Rationale

Handwritten recipes carry personal, irreplaceable character that JSON cannot
fully capture. Printed / digital sources are fully represented by the
extracted recipe data — the original image adds nothing once the recipe is
transcribed.

## Multi-Page Recipes

For recipes spanning multiple images (5–6 photos):

- **Handwritten** multi-page: store ALL refs —
  `"image_refs": ["IMG_7510.jpeg", "IMG_7511.jpeg", ...]`.
- **Non-handwritten** multi-page: extract all content but leave
  `image_refs: []`.
- Use `page_continuation` if splitting across entries.
- Merge into a single complete recipe when possible.

## Source Classification

| Source | Indicators | Action | Keep image? |
|---|---|---|---|
| Kindle screenshots | "Location X of Y", e-reader UI | Check copyright | **No** — clear `image_refs` |
| Magazine clippings | Printed text, magazine layout | Process normally | **No** — clear `image_refs` |
| Typed cards | Typewriter font | Process normally | **No** — clear `image_refs` |
| Handwritten | Pen/pencil on paper | Process carefully | **Yes** — keep refs |
| Cookbook pages | Professional layout, copyright notices | **Verify permission** | **No** — clear `image_refs` |
