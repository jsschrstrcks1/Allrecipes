# Skills — Allrecipes

> The reference shelf. Recipe-transcription and recipe-validation skills are the bread-and-butter; the standard household kit handles everything else.

This document is the human-facing index of all Claude Code skills configured in this repository. The agent-facing pointer lives in [`CLAUDE.md`](CLAUDE.md). Skills follow the agent-skills-spec format and live under `.claude/skills/`.

**Total skills configured: 19.** Of those, 16 are the standard household kit and 3 are recipe-domain specific.

---

## Quick reference

| Skill | Activation | Default | Domain |
|---|---|---|---|
| [`recipe-transcription`](#recipe-transcription) | automatic on image+recipe context | on | Recipe ingestion |
| [`recipe-validation`](#recipe-validation) | automatic before commit | on | Recipe integrity |
| [`milk-substitution`](#milk-substitution) | explicit | on | Cooking conversion |
| Standard household kit (16 skills) | mixed | on | See [section below](#standard-household-kit) |

---

## How invocation works

Claude Code skills can fire three ways:

**1. Automatic activation.** Each skill's YAML frontmatter declares `keywords:`. When those keywords appear in your prompt, in surrounding context (file paths, recent tool output), or in the operation Claude is about to perform, the skill auto-activates without being asked.

**2. Explicit invocation.** Name the skill directly:

```
"Use the recipe-transcription skill to extract this Cook's Illustrated béarnaise."
/skill recipe-transcription
```

**3. Implicit invocation by task shape.** Skills also fire on certain operations regardless of keywords — image reads of recipe sources trigger `recipe-transcription`, recipe JSON edits trigger `recipe-validation`, completion claims trigger `verification-before-completion`, etc.

**Disabling for a session:** "For this session, do not apply the X skill." Skills respect explicit user override.

---

## Recipe-domain skills

### `recipe-transcription`

**Path:** `.claude/skills/recipe-transcription/SKILL.md`

Extracts structured recipe data from images (Kindle screenshots, magazine scans, handwritten cards, typed cards). Outputs JSON conforming to the Allrecipes schema (`id`, `collection`, `title`, `category`, `attribution`, `source_note`, `ingredients[]`, `instructions[]`, `confidence`, `image_refs`).

**Activation:** automatic when image-source-of-recipe context is detected (e.g., reading a `.PNG` from `data/processed/`, or a prompt mentioning "transcribe this recipe"). Also explicitly invokable.

**Non-negotiables enforced by this skill:**
- Never invent ingredients, steps, temperatures, times, or yields
- Mark unclear text `[UNCLEAR]` — never guess
- Verify source license / permission before processing
- `image_refs` is reserved for **handwritten** sources only
- Always read from `data/processed/`, never raw oversized images

**Example prompts that should trigger:**

| Prompt | Expected behavior |
|---|---|
| "Transcribe `data/processed/IMG_004.PNG`" | Reads processed copy, extracts to schema, marks `[UNCLEAR]` for ambiguous OCR |
| "Add this Betty Crocker pound cake from the magazine clipping" | Verifies source license; transcribes; sets `category: 'desserts'` |
| "Process the Kindle cookbook screenshots in `data/`" | Refuses raw read; calls `process_images.py` first |

### `recipe-validation`

**Path:** `.claude/skills/recipe-validation/SKILL.md`

Validates `data/recipes.json` against the schema. Checks required fields, slug uniqueness, image references, category vocabulary (cheese-MAKING vs recipes-using-cheese), confidence-flag consistency.

**Activation:** automatic before commit (paired with `verification-before-completion`); also explicit.

**Validation rules enforced:**

- Every recipe has `id`, `title`, `attribution`, `source_note`, `ingredients[]`, `instructions[]`
- `category: "cheese"` is reserved for cheese-MAKING (not mac-and-cheese)
- `image_refs` empty unless source is handwritten
- `confidence.overall` set; `flags` populated when `low`
- Slug uniqueness across the corpus

**Manual invocation:**

```
python scripts/validate-recipes.py
python scripts/validate-recipes.py --strict   # warnings become errors
```

### `milk-substitution`

**Path:** `.claude/skills/milk-substitution/SKILL.md`

Maps dairy milks to plant-based alternatives accounting for fat content and sweetness. Same engine as `Grandmasrecipes` (lives there as `.js`); this repo carries the skill version so the reference site works offline.

**Activation:** explicit. Invoked when a user asks for a milk substitution suggestion or when generating substitution notes for a recipe.

**Refusal patterns:**
- Refuses substitutions where the conversion would fundamentally change the recipe (e.g., milk-only sauces where dairy proteins matter for emulsification)
- Returns `[UNSAFE]` flag with explanation rather than producing a plausible-but-wrong answer

---

## Standard household kit

Common to every sister repo. Canonical versions live in `ken/.claude/skills/`.

| Skill | Activation | One-line |
|---|---|---|
| `brainstorming` | automatic on creative work | Pre-implementation creative exploration. |
| `cognitive-memory` | automatic on session start | Cross-session knowledge persistence. Memory scope: `/Allrecipes`. |
| `executing-plans` | explicit | Use when executing a written plan in a separate session. |
| `finishing-a-development-branch` | explicit | Use when implementation is complete; decide merge / PR / cleanup. |
| `prompt-optimizer` | automatic on prompt-improvement requests | Optimizes raw prompts. Advisory only. |
| `receiving-code-review` | explicit | Use when receiving review feedback. |
| `requesting-code-review` | explicit | Use when completing tasks before merging. |
| `safety-guard` | automatic on destructive ops | Prevents destructive operations on production / autonomous runs. |
| `security-review` | automatic on auth/secrets/payment | Security checklist + patterns. |
| `security-scan` | explicit | Scans `.claude/` config via AgentShield. |
| `session-checkpoint` | automatic + explicit | Atomic commits, checkpoint summaries, rate-limit recovery. |
| `subagent-driven-development` | explicit | Use when executing implementation plans with independent tasks. |
| `systematic-debugging` | automatic on bug/test-failure | Use before proposing fixes. |
| `using-git-worktrees` | explicit | Isolate feature work in worktrees. |
| `verification-before-completion` | automatic on completion claims | Refuses "complete/fixed/passing" without observed output. |
| `writing-plans` | explicit | Use when you have a spec for a multi-step task. |

---

## Repo-specific guardrails (not yet packaged as skills)

[`CAREFUL.md`](CAREFUL.md) is the human-readable integrity guardrail for this repo — "careful, not clever." It enforces read-before-edit, grep-before-rename, and refuses unrequested "improvements." The pattern is published as a public-domain skill at [`open-claw-stuff/skills/careful-not-clever`](https://github.com/jsschrstrcks1/open-claw-stuff/tree/main/skills/careful-not-clever).

---

## Multi-LLM orchestrator

This repo defaults to **`recipe` mode** in the multi-LLM orchestrator hosted in [ken](https://github.com/jsschrstrcks1/ken).

| Slash command | Usage |
|---|---|
| `/consult` | `/consult gpt structure "review this extracted recipe"` |
| `/orchestrate recipe "<task>"` | Full pipeline: transcribe → validate → integrate (lead: GPT) |

First-time setup per session:

```bash
pip3 install -q -r /home/user/ken/orchestrator/requirements.txt
```

---

## See also

- [`CLAUDE.md`](CLAUDE.md) — agent context
- [`README.md`](README.md) — public-facing overview
- [`CAREFUL.md`](CAREFUL.md) — integrity guardrail (human-readable)
- [`.claude/standards/`](.claude/standards/) — extracted reference standards (CHEESE_RULES, IMAGE_RETENTION, COMPOUND_RECIPES, OCR_STANDARDS, IMAGE_WORKFLOW, RECIPE_SCHEMA)
- `ken` — hosts the orchestrator; canonical versions of the standard household kit
