# Unfinished Tasks

| library_task_id | priority | title |
|---|---|---|
| recipe-repo-verify-entrypoint | 4 | Give each recipe repo a single runnable verification entry point (scripts/verify.sh) that shells the validators already written — link-integrity, seo-schema-audit, recipe-validation, accessibility-audit — so verification-before-completion can NAME a command instead of asking the agent to remember a posture. Verified gap: ls /home/user/Allrecipes/scripts/verify* returns nothing; the pieces exist, the entry point does not. Same shape as UL-137's finding about coding modes — a skill is instructional and can be skipped, a command is a fact. UL-175. Cheap v1 is a shell wrapper; a later version could be required by a pre-commit or pre-push guard, but that is a separate decision and should not be bundled in |

<!-- library register 2026-08-27T05:05:33.911Z -->
| audit0827-all-single-ingredient-blobs | 1 | P1 AUDIT-0827: 1,616 recipes carry <=1 ingredient entry — typically one unparsed blob (861 Stevenson Memorial + 103 Complete Book of Cheese + others), rendering as one mangled line on recipe.html. Tracked PENDING at root PENDING_TASKS.md:308-316 since registration; parse into structured ingredients. |

<!-- library register 2026-08-27T05:05:34.321Z -->
| audit0827-all-collection-sync-skill-fiction | 2 | P2 AUDIT-0827: .claude/skills/collection-sync/SKILL.md:36-52 documents aggregate_collections.py, aggregate_tips.py, analyze_duplicates.py, check-duplicates.py, build_shards.py as available in this repo — none exists here; the aggregation code and registry live in Grandmasrecipes, which is the actual hub. Rewrite the skill to point at the hub (or move the scripts) so the sync procedure is runnable as documented. |

<!-- library register 2026-08-27T05:05:34.721Z -->
| audit0827-all-ingredient-index-unconsumed | 2 | P2 AUDIT-0827: data/ingredient-index.json (4.6 MB, 13,479 ingredients) is built by TWO duplicate scripts (build-ingredient-index.py and build_ingredient_index.py) and fetched by no page — tips.html builds its ingredient block client-side from tip.related_ingredients instead. Wire an ingredient-search UI to it (the hub has one to copy) or stop building it; delete the duplicate builder either way. |

<!-- library register 2026-08-27T05:05:35.126Z -->
| audit0827-all-builder-pages-orphaned | 2 | P2 AUDIT-0827: cheese-builder.html and butter-builder.html are absent from every site-nav in this repo (they link only to each other; Grandmasrecipes' nav links Cheese Builder, nothing anywhere links Butter Builder). Add nav entries. Related dead code: script.js:408-440 updateCollectionCounts targets .collection-btn elements that exist in no Allrecipes HTML. |

<!-- library register 2026-08-27T05:05:35.519Z -->
| audit0827-all-unclear-recipes | 3 | P3 AUDIT-0827: 35 recipes still contain [UNCLEAR] markers, incl. the 2 DGF recipes blocked on the physical cookbook (dgf-peanut-butter-chocolate-chip-cookies: 6 unclear quantities; dgf-crispy-salmon: no instructions) tracked at PENDING_TASKS.md:187-201. Resolve with sources or mark permanently unavailable. |

<!-- library register 2026-08-27T05:05:35.927Z -->
| audit0827-all-dead-thumbnails | 3 | P3 AUDIT-0827: data/thumbnails/ holds 906 webp files; only 3 recipes in the corpus have image_refs (5 refs, 2 of which map to missing thumbnails) because the image-retention policy strips refs from non-handwritten recipes — ~903 thumbnails are unreachable dead weight served with the site. Prune or re-link. |

<!-- library register 2026-08-27T05:05:36.326Z -->
| audit0827-all-cheese-tracker-stalled | 4 | P4 AUDIT-0827: CHEESE_VARIETIES_TRACKER.md — 1,519 cheesemaking recipes, ~15-17% of the stated minimum goal, 2,839 unchecked markers, progress table untouched since 2026-01-21. Operator decision: resume the harvest or park the goal explicitly. |

<!-- library register 2026-08-27T05:05:36.740Z -->
| audit0827-all-pipeline-artifacts-served | 3 | P3 AUDIT-0827: ~4 MB of pipeline logs/reports/raw sources ship to the published site in data/ with no consumer (image_manifest 575 KB, processed_images 252 KB, 4 processing logs 1.9 MB, cheese-reclassification-report 231 KB, gordon_ramsay manifest + 432 images, cooking_tips.json's ~60 unreachable tips, measurement_tips.md human-authored and unrendered, 7cury10/8cury10.txt 526 KB). Decide serve-vs-archive; wire measurement_tips + cooking_tips or fold them into tips_master. |
