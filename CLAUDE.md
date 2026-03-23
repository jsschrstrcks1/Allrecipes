# Allrecipes — Family Recipe Aggregator

**Soli Deo Gloria.** Recipe aggregation hub for cross-collection features.

This repository is part of the multi-repo Family Recipe Archive:
- **Grandmasrecipes** — Grandma Baker's collection
- **Grannysrecipes** — Granny Hudson's collection
- **MomsRecipes** — MomMom Baker's collection
- **Allrecipes** — This repo (aggregator)

---

## Multi-LLM Integration

This repository has access to the multi-LLM orchestrator system. External models (GPT, Gemini, Grok) serve as **consultants only** — Claude remains lead author and decision-maker.

### Available Skills

| Skill | Usage | Purpose |
|-------|-------|---------|
| `/consult` | `/consult gemini expand "cross-collection search UX"` | Quick single-model second opinion |
| `/orchestrate` | `/orchestrate recipe "generate a family favorites collection page"` | Full multi-model pipeline |
| Cognitive Memory | Automatic on session start | Cross-session knowledge persistence |

### Mode: `recipe`
- **Lead:** GPT (generation)
- **Pipeline:** Generate (GPT) → Expand (Gemini) → Safety Check (Claude) → Creative Variation (Grok)
- **Memory scope:** `/recipes/allrecipes`
- **Orchestrator:** `/home/user/ken/orchestrator/`

### Context Boundaries
- **SEND:** Recipe requirements, ingredient lists, dietary constraints
- **NEVER SEND:** Family attribution details, site analytics, personal details
