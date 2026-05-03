#!/usr/bin/env python3
"""
Hand-merge artifact for PR #120 (multi-llm-integration-plan).

Surgically applies the new functionality from the multi-llm PR onto current
main: imports the new skill directories, drops in supporting files, and
backs up + replaces the modified config files. Does NOT touch CLAUDE.md.

WHY THIS EXISTS:
PR #120 was opened against an older main and conflicts with merges that
followed (cognitive-memory, claude-mem-eval, README trim). The bulk of the
PR is *clean adds* — new skill directories that don't exist on main.
GitHub's auto-merge gave up because of overlap on .claude/settings.json
and the two .claude/hooks/*.sh files. Doing it surgically avoids that.

WHAT THIS APPLIES (Allrecipes):
  New skills (11) — only those NOT already on main:
    - careful-not-clever      (integrity guardrail)
    - collection-sync         (cross-collection data sync)
    - consult                 (quick multi-LLM second opinion)
    - ebook-builder           (print PDF pipeline)
    - icp-2                   (ICP-2 SEO/AEO standard)
    - ingredient-substitution (recipe-specific)
    - nutrition-estimator     (recipe-specific)
    - orchestra               (fan-out + deliberation)
    - orchestrate             (linear multi-LLM pipeline)
    - recipe-story            (recipe narrative voice)
    - seo-schema-audit        (JSON-LD / OG validator)

  Skipped — already on main:
    - cognitive-memory
    - session-checkpoint

  Supporting files (clean adds):
    - bootstrap-env.sh                 (orchestrator dep installer)
    - new-skills-proposal.md           (curation doc)
    - skills-audit.md                  (audit doc)

  Modified config (with .bak backup, then PR head version applied):
    - .claude/settings.json
    - .claude/hooks/image-safety-check.sh
    - .claude/hooks/post-write-validate.sh

NOT TOUCHED:
  - CLAUDE.md — Allrecipes' multi-llm PR doesn't modify it; the README trim
    that landed already restructured the surrounding docs. Add references
    to the new skills under your CLAUDE.md "Essential Reading" or wherever
    you list available skills, when convenient.

REQUIREMENTS:
  - Run from inside the Allrecipes repo on current main
  - PR #120 branch fetched: `git fetch origin claude/multi-llm-integration-plan-MZxEu`

HOW TO APPLY:
  cd <Allrecipes repo>
  git fetch origin claude/multi-llm-integration-plan-MZxEu
  python3 scripts/_merge_artifacts/apply_multi_llm_merge.py --dry-run
  python3 scripts/_merge_artifacts/apply_multi_llm_merge.py
  git status   # review what changed
  git add .claude/ bootstrap-env.sh new-skills-proposal.md skills-audit.md
  git commit -m "Merge PR #120: multi-llm orchestrator skills + integrity guardrail"
  # Then close PR #120 with comment linking to this commit.
"""

import shutil
import subprocess
import sys
from pathlib import Path

PR_HEAD_SHA = 'a53de8918e5a3d9ecf4d9729cc59cc63b845182d'
PR_BRANCH = 'claude/multi-llm-integration-plan-MZxEu'

NEW_SKILLS = [
    'careful-not-clever', 'collection-sync', 'consult',
    'ebook-builder', 'icp-2', 'ingredient-substitution',
    'nutrition-estimator', 'orchestra', 'orchestrate',
    'recipe-story', 'seo-schema-audit',
]

SUPPORTING_FILES = [
    'bootstrap-env.sh',
    'new-skills-proposal.md',
    'skills-audit.md',
]

MODIFIED_CONFIG = [
    '.claude/settings.json',
    '.claude/hooks/image-safety-check.sh',
    '.claude/hooks/post-write-validate.sh',
]


def git_path_exists_in_ref(ref: str, path: str) -> bool:
    return subprocess.run(
        ['git', 'cat-file', '-e', f'{ref}:{path}'],
        capture_output=True,
    ).returncode == 0


def checkout_from_ref(ref: str, path: str, repo_root: Path) -> bool:
    """git checkout <ref> -- <path>. Returns True on success."""
    r = subprocess.run(
        ['git', 'checkout', ref, '--', path],
        cwd=repo_root, capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(f'  ERROR checking out {path}: {r.stderr.strip()}', file=sys.stderr)
        return False
    return True


def main():
    dry = '--dry-run' in sys.argv
    repo_root = Path(__file__).resolve().parents[2]

    if not git_path_exists_in_ref(PR_HEAD_SHA, 'bootstrap-env.sh'):
        print(
            f'ERROR: PR head ({PR_HEAD_SHA[:8]}) not reachable.\n'
            f'  Did you fetch? git fetch origin {PR_BRANCH}',
            file=sys.stderr,
        )
        sys.exit(1)

    print(f'=== Importing skills from {PR_HEAD_SHA[:8]} ===')
    skills_added = []
    skills_skipped = []
    for skill in NEW_SKILLS:
        target = repo_root / '.claude' / 'skills' / skill
        if target.exists():
            print(f'  SKIP {skill} (already on main)')
            skills_skipped.append(skill)
        elif dry:
            print(f'  [DRY] would import .claude/skills/{skill}/')
        else:
            if checkout_from_ref(PR_HEAD_SHA, f'.claude/skills/{skill}', repo_root):
                print(f'  + .claude/skills/{skill}')
                skills_added.append(skill)

    print(f'\n=== Supporting files ===')
    files_added = []
    files_skipped = []
    for f in SUPPORTING_FILES:
        target = repo_root / f
        if target.exists():
            print(f'  SKIP {f} (already on main)')
            files_skipped.append(f)
        elif dry:
            print(f'  [DRY] would import {f}')
        else:
            if checkout_from_ref(PR_HEAD_SHA, f, repo_root):
                print(f'  + {f}')
                files_added.append(f)

    print(f'\n=== Modified config (backup + replace) ===')
    config_replaced = []
    config_skipped = []
    for f in MODIFIED_CONFIG:
        target = repo_root / f
        if not git_path_exists_in_ref(PR_HEAD_SHA, f):
            print(f'  SKIP {f} (not in PR head)')
            config_skipped.append(f)
            continue
        backup = target.with_suffix(target.suffix + '.bak')
        if dry:
            print(f'  [DRY] would back up {f} -> {backup.name} and apply PR version')
        else:
            if target.exists() and not backup.exists():
                shutil.copy2(target, backup)
                print(f'  backup: {f} -> {backup.name}')
            if checkout_from_ref(PR_HEAD_SHA, f, repo_root):
                print(f'  ~ {f} (PR head version applied)')
                config_replaced.append(f)

    print(f'\n=== Summary ===')
    print(f'Skills added:      {len(skills_added)} {skills_added}')
    print(f'Skills skipped:    {len(skills_skipped)} {skills_skipped}')
    print(f'Files added:       {len(files_added)} {files_added}')
    print(f'Files skipped:     {len(files_skipped)} {files_skipped}')
    print(f'Configs replaced:  {len(config_replaced)} {config_replaced}')
    print(f'Configs skipped:   {len(config_skipped)} {config_skipped}')

    if dry:
        print('\n[DRY RUN] No changes made. Re-run without --dry-run to apply.')
        return

    print(f'\n=== Next steps ===')
    print('  git status                                         # review')
    print('  git diff --stat HEAD                               # summary')
    print('  git add .claude/ bootstrap-env.sh new-skills-proposal.md skills-audit.md')
    print('  git commit -m "Merge PR #120: multi-llm skills + integrity guardrail"')
    print('  # Close PR #120 with link to this commit.')
    print()
    print('  TIP: Review .claude/settings.json.bak to confirm the new settings')
    print('  do not unintentionally drop a hook or permission you wanted.')


if __name__ == '__main__':
    main()
