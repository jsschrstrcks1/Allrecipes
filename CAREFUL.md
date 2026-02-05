# Careful, Not Clever

**Version**: 1.0.0
**Created**: 2026-02-05
**Purpose**: Guardrail to enforce careful, methodical work over clever shortcuts
**Priority**: CRITICAL — This skill overrides the impulse to optimize, batch, or shortcut

---

## The Rule

> **Be careful, not clever.**
> Careful means: verified, documented, reversible, honest.
> Clever means: fast, creative, batched, assumed.
> When in doubt, be careful.

---

## Before Modifying Any File

1. **Read it first.** Never edit a file you haven't read in this session.
2. **Understand what's there.** Don't assume you know the structure. Check.
3. **Check for conflicts.** If adding a recipe, verify the ID doesn't exist. If editing, grep for all references. If deleting, confirm zero dependencies.
4. **State your assumptions.** Before a bulk operation, list what you're assuming and verify each one.

## During Modifications

5. **One logical change at a time.** Don't combine unrelated changes in a single pass.
6. **Document as you go.** Update PENDING_TASKS.md alongside the work, not after.
7. **Spot-check after bulk operations.** After changing N recipes, read 2-3 of them to verify the change landed correctly.
8. **Leave things alone when risk outweighs benefit.** If a change could break something and the benefit is marginal, skip it. Say why you skipped it.

## After Modifications

9. **Verify, then report.** Don't say "done" until you've confirmed the result.
10. **Run validation.** Always run `python scripts/validate-recipes.py` before committing recipe changes.
11. **Commit with honest messages.** Describe what was done AND what was intentionally left alone.
12. **Update all cross-references.** If a metric changed, update it everywhere — PENDING_TASKS.md, CLAUDE.md, any relevant docs.

---

## Recipe-Specific Careful Practices

### Before Extracting Recipes

- **Check image dimensions** before reading. Use `python scripts/image_safeguards.py status` first.
- **Use processed versions** for oversized images (>2000px). Never read raw Kindle screenshots directly.
- **Verify source type** (handwritten, Kindle, magazine) — this determines `image_refs` handling.
- **Check for completeness** — title, ingredients, AND instructions must all be present.

### When Adding Recipes

- **Verify unique ID** — grep `data/recipes.json` before using a new recipe ID.
- **Cross-check quantities** — does "4 cups salt" make sense? Flag implausible OCR.
- **Check category rules** — cheese-MAKING recipes use `category: "cheese"`, not dishes that contain cheese.
- **Mark unclear content** — use `[UNCLEAR]` rather than guessing. Guessing is clever; marking is careful.

### For Image References

- **Handwritten only** — `image_refs` is reserved for handwritten recipe images.
- **Non-handwritten sources** — Kindle, magazine, typed cards get empty `image_refs: []`.
- **Multi-page handwritten** — include ALL image refs: `["IMG_001.jpeg", "IMG_002.jpeg"]`.

---

## What "Careful" Looks Like

- Reading a file before editing it
- Running `validate-recipes.py` after every recipe change
- Checking that a recipe ID doesn't already exist before creating it
- Updating PENDING_TASKS.md in the same session you complete the task
- Saying "I left X alone because Y" instead of silently skipping it
- Committing after each logical unit of work, not batching everything at the end
- Admitting when OCR is unclear rather than guessing
- Using `[UNCLEAR]` for ambiguous measurements instead of inventing values

## What "Clever" Looks Like (Avoid)

- Editing files based on assumed structure without reading them
- Batching dozens of unrelated recipe changes into one mega-commit
- Assuming a recipe ID is unique without checking
- Saying "I updated all tracking files" without actually doing it
- Optimizing for speed when the user asked for accuracy
- Making "improvements" the user didn't ask for
- Silently skipping problems instead of reporting them
- Guessing that "1 tsp" is actually "1 tbsp" based on context

---

## The Integrity Test

Before every commit, ask yourself:

1. **Is every claim in my commit message verifiable?** If I said "updated 124 recipes," can I prove it?
2. **Did I document this work in the tracking files?** Not "I'll do it later" — now.
3. **Would the user trust this work if they checked every recipe?** Not just the ones I mentioned.
4. **Did I leave anything silently broken?** If I'm not sure, run validation.
5. **Did I invent any content?** If any ingredient, quantity, or instruction was guessed rather than read, flag it.

---

## When This Skill Activates

This skill loads into context on EVERY file modification (Edit, Write). It serves as a persistent reminder that careful, verified, well-documented work is always preferred over fast, clever, undocumented work.

**This is not optional.** This guardrail exists because the project owner values integrity over speed.

---

**Soli Deo Gloria** — Excellence as worship means getting it right, not getting it fast.
