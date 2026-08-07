# Unfinished Tasks

| library_task_id | priority | title |
|---|---|---|
| recipe-repo-verify-entrypoint | 4 | Give each recipe repo a single runnable verification entry point (scripts/verify.sh) that shells the validators already written — link-integrity, seo-schema-audit, recipe-validation, accessibility-audit — so verification-before-completion can NAME a command instead of asking the agent to remember a posture. Verified gap: ls /home/user/Allrecipes/scripts/verify* returns nothing; the pieces exist, the entry point does not. Same shape as UL-137's finding about coding modes — a skill is instructional and can be skipped, a command is a fact. UL-175. Cheap v1 is a shell wrapper; a later version could be required by a pre-commit or pre-push guard, but that is a separate decision and should not be bundled in |
