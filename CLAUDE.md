# Other Family Recipes — AI Assistant Context

**Version:** 2.0 (lean hub)
**Last updated:** 2026-05-01

> **Soli Deo Gloria.** A labor of love by a Reformed Baptist family. Real
> people will eat from these recipes — **accuracy beats speed**.

This repo is a **standalone collection** holding ~9,989 reference recipes
(digital cookbooks + magazine clippings, used with permission). It is part of
the multi-repo Family Recipe Archive (Mom, Grandma, Granny, Reference).

---

## Skills

Full skill catalog (19 skills) is documented in [`SKILLS.md`](SKILLS.md) — human-facing index with activation modes, trigger keywords, and example prompts.

**Read it at session start.** The recipe-domain skills (`recipe-transcription`, `recipe-validation`, `milk-substitution`) and the standard household kit (16 skills) are all configured under `.claude/skills/`. The activation rules and the non-negotiables enforced by each skill live in SKILLS.md.

---

## Quick Start (read first)

1. **Images are FLAT** in `data/` (no subdirs). Use `data/processed/` for AI reads.
2. **2000 px API limit.** Always read processed copies for oversized originals.
3. **NEVER invent** recipe content. Mark unclear items as `[UNCLEAR]`.
4. **`category: "cheese"` is MANDATORY** for cheese-MAKING recipes — see [`CHEESE_RULES.md`](.claude/standards/CHEESE_RULES.md).
5. **Image retention:** only **handwritten** recipes keep `image_refs`. See [`IMAGE_RETENTION.md`](.claude/standards/IMAGE_RETENTION.md).
6. **Run `python scripts/validate-recipes.py`** before committing.
7. **Check [`PENDING_TASKS.md`](PENDING_TASKS.md)** at session start.

Decision priority: **accuracy → preservation → fidelity → readability**.

---

## Essential Reading

### Standards (extracted)

| File | What it covers |
|---|---|
| [`.claude/standards/CHEESE_RULES.md`](.claude/standards/CHEESE_RULES.md) | **CRITICAL** — mandatory `category: "cheese"` rule, what is / isn't cheese-making, examples, tooling impact |
| [`.claude/standards/IMAGE_RETENTION.md`](.claude/standards/IMAGE_RETENTION.md) | Handwritten-only `image_refs` policy, source-by-source retention table |
| [`.claude/standards/COMPOUND_RECIPES.md`](.claude/standards/COMPOUND_RECIPES.md) | Hybrid compound + component approach (Beef Wellington pattern) |
| [`.claude/standards/OCR_STANDARDS.md`](.claude/standards/OCR_STANDARDS.md) | OCR error patterns, measurement standardization, source classification |
| [`.claude/standards/IMAGE_WORKFLOW.md`](.claude/standards/IMAGE_WORKFLOW.md) | 2000 px limit, manifest commands, status values |
| [`.claude/standards/RECIPE_SCHEMA.md`](.claude/standards/RECIPE_SCHEMA.md) | Full recipe JSON schema with `components` / `tips` / `substitutions` |

### Operations

| File | What it covers |
|---|---|
| [`SKILLS.md`](SKILLS.md) | **Skills index — read at session start** |
| [`.claude/ONBOARDING.md`](.claude/ONBOARDING.md) | Quick start guide for new sessions |
| [`.claude/MAINTENANCE.md`](.claude/MAINTENANCE.md) | Step-by-step maintenance workflows |
| [`.claude/mcp-servers.md`](.claude/mcp-servers.md) | Optional MCP server integrations |
| [`PENDING_TASKS.md`](PENDING_TASKS.md) | Deferred work tracking — check at every session start |
| [`CAREFUL.md`](CAREFUL.md) | Integrity guardrail (technical) |
| [`README.md`](README.md) | Public-facing overview |

---

## Repository Structure

```
Allrecipes/
├── SKILLS.md                 # Skills index (NEW)
├── CLAUDE.md                 # This hub
├── PENDING_TASKS.md          # Deferred work tracking
├── CAREFUL.md                # Integrity guardrail
├── README.md                 # Public-facing overview
├── index.html / recipe.html # Static site
├── styles.css / script.js   # Site bundle
├── butter-builder.{html,js} # Butter builder UI
├── cheese-builder.{html,js} # Cheese builder UI (depends on category="cheese")
├── adulterant-companion.js  # Adulterant identification
├── milk-substitution.js     # Milk substitution
├── .claude/
│   ├── settings.json        # Permissions + hooks
│   ├── skill-rules.json     # Skill auto-activation
│   ├── ONBOARDING.md        # New-session quick start
│   ├── MAINTENANCE.md       # Detailed workflows
│   ├── mcp-servers.md       # MCP integrations
│   ├── standards/           # Extracted reference files
│   ├── hooks/
│   │   ├── post-write-validate.sh
│   │   └── image-safety-check.sh
│   └── skills/              # 19 skills (see SKILLS.md)
├── data/
│   ├── *.jpeg               # Magazine scans (FLAT)
│   ├── *.PNG                # Kindle screenshots (OVERSIZED!)
│   ├── processed/           # AI-friendly ≤2000 px copies
│   ├── recipes.json         # All recipes
│   ├── collections.json     # Collection metadata
│   ├── processed_images.json # Scan processing log
│   └── image_manifest.json  # Image validation status
├── scripts/
│   ├── validate-recipes.py
│   ├── process_images.py
│   ├── image_safeguards.py
│   └── optimize_images.py
└── ebook/                   # Print generation
```

---

## Collection Configuration

```json
{
  "collections": {
    "all": {
      "id": "all",
      "display_name": "Other Family Recipes",
      "folder": "data/",
      "description": "Digital cookbook recipes and magazine clippings (used with permission)"
    }
  }
}
```

---

## Categories

```
appetizers, beverages, breads, breakfast, cheese, desserts,
mains, salads, sides, soups, snacks
```

**`cheese` is for cheese-MAKING recipes only.** A recipe that *uses* cheese
(mac and cheese, cheesecake, fondue) belongs elsewhere. See
[`CHEESE_RULES.md`](.claude/standards/CHEESE_RULES.md) for the full criteria.

---

## Non-Negotiable Rules

1. Do NOT invent ingredients, steps, temperatures, times, or yields.
2. Mark unreadable / ambiguous text as `[UNCLEAR]` with best guesses.
3. Preserve original intent; normalize spelling and formatting.
4. **Verify copyright / permission** before processing commercial cookbook images.
5. **Only link handwritten images** — `image_refs` is reserved for handwritten
   sources; non-handwritten (Kindle, magazine, typed) leave `image_refs: []`.
6. Never read oversized images (>2000 px) directly — use `data/processed/`.
7. Always run `python scripts/validate-recipes.py` before committing.
8. Check `PENDING_TASKS.md` for deferred work at session start.
9. **Cheese-making recipes MUST use `category: "cheese"`** — the Cheese Builder
   tool depends on this categorization to find recipes.

---

## Validation

```bash
# Schema + JSON syntax
python scripts/validate-recipes.py

# Strict mode (warnings become errors)
python scripts/validate-recipes.py --strict
```

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 2.1 | 2026-05-10 | Added `SKILLS.md` skill index. CLAUDE.md references it. |
| 2.0 | 2026-05-01 | Lean hub restructure. Extracted cheese / image-retention / compound / OCR / image / schema subfiles into `.claude/standards/`. CLAUDE.md cut from ~519 lines to ~155. |
| 1.3 | Feb 2026 | Added handwritten-only image retention policy. |
| 1.2 | Jan 2026 | Added `category: "cheese"` requirement and tool linkage. |
| 1.1 | Jan 2026 | Added `.claude/` config, Quick Start, Priority Framework. |
| 1.0 | Original | Initial CLAUDE.md. |

---

*"She looketh well to the ways of her household, and eateth not the bread of idleness."* — Proverbs 31:27

---

## Cognitive Memory — Slice 6 Observation Capture

To enable always-on cognitive memory observation capture in this repo, register the canonical hook (lives in `ken`) in `.claude/settings.json`:

```json
"env": {
  "MEMORY_OBSERVATIONS_ENABLED": "true",
  "MEMORY_AUTO_OBSERVE_ENABLED": "true"
},
"hooks": {
  "PostToolUse": [
    {
      "matcher": "*",
      "hooks": [
        {"type": "command",
         "command": "/home/user/ken/.claude/hooks/observe-tool-use.sh"}
      ]
    }
  ]
}
```

Hook is **fail-closed**: any error → exit 0, never blocks the tool call. Args SHA256-hashed via `_compute_args_hash` before disk; raw values never persisted. Errors → `/tmp/observe-hook.err`. Surface candidates: call `memory_ops.extract_candidates_from_observations(session_id)` after a session.

Setup memory: id `5a9c8ae1` (recall via `python3 /home/user/ken/orchestrator/memory_ops.py recall "Slice 6 always-on cognitive memory observation capture"`). Currently active in `ken/.claude/settings.json` (commit `ca78cad`); per-repo activation is opt-in via the absolute-path reference above.
