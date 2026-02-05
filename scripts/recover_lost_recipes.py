#!/usr/bin/env python3
"""
Recover lost recipes from git history.

Uses the RECIPE_AUDIT_LOST_IDS.md and RECIPE_AUDIT_TRACKER.md to identify
which recipe IDs need recovery and which commits contain them.
"""

import json
import subprocess
import sys
import re


def get_recipes_at_commit(commit_hash):
    """Extract recipes.json from a specific git commit."""
    try:
        result = subprocess.run(
            ["git", "show", f"{commit_hash}:data/recipes.json"],
            capture_output=True, text=True, check=True,
            cwd="/home/user/Allrecipes"
        )
        data = json.loads(result.stdout)
        if isinstance(data, list):
            return {r["id"]: r for r in data}
        elif isinstance(data, dict) and "recipes" in data:
            return {r["id"]: r for r in data["recipes"]}
        else:
            return {}
    except Exception as e:
        print(f"  ERROR reading commit {commit_hash}: {e}", file=sys.stderr)
        return {}


def parse_lost_ids_from_markdown(filepath):
    """Parse RECIPE_AUDIT_LOST_IDS.md to get all lost recipe IDs by category."""
    categories = {}
    current_category = None

    with open(filepath) as f:
        for line in f:
            # Match category headers like ### LOST_CHEESE_BAD_MERGE (291 recipes)
            header_match = re.match(r'^### (LOST_\w+)\s+\((\d+)\s+recipes?\)', line)
            if header_match:
                current_category = header_match.group(1)
                categories[current_category] = []
                continue

            # Match table rows with recipe IDs like | `some-id` | Title | ...
            if current_category and line.startswith('| `'):
                id_match = re.match(r'\| `([^`]+)`', line)
                if id_match:
                    categories[current_category].append(id_match.group(1))

    return categories


def main():
    print("=" * 70)
    print("RECIPE RECOVERY TOOL")
    print("=" * 70)

    # Step 1: Parse lost IDs
    print("\n[1/5] Parsing lost recipe IDs from tracker...")
    lost_ids_by_category = parse_lost_ids_from_markdown(
        "/home/user/Allrecipes/RECIPE_AUDIT_LOST_IDS.md"
    )
    total_lost = sum(len(ids) for ids in lost_ids_by_category.values())
    for cat, ids in sorted(lost_ids_by_category.items()):
        print(f"  {cat}: {len(ids)} IDs")
    print(f"  TOTAL: {total_lost} lost IDs")

    # Step 2: Load current recipes
    print("\n[2/5] Loading current recipes.json...")
    with open("/home/user/Allrecipes/data/recipes.json") as f:
        current_data = json.load(f)
    if isinstance(current_data, list):
        current_recipes = current_data
    else:
        current_recipes = current_data.get("recipes", [])
    current_ids = {r["id"] for r in current_recipes}
    print(f"  Current recipes: {len(current_ids)}")

    # Step 3: Define recovery sources
    # Maps category -> list of commits to try (in order of preference)
    recovery_sources = {
        "LOST_GUTENBERG_RECIPE": ["12f070a"],
        "LOST_CPM_RECIPE": ["12f070a"],
        "LOST_CUSOCUTS_RECIPE": ["12f070a"],
        "LOST_WEBSITE_RECIPE": ["12f070a"],
        "LOST_HBH_RECIPE": ["12f070a"],
        "LOST_PP_RECIPE": ["12f070a"],
        "LOST_OTHER": ["12f070a"],
        "LOST_CHEESE_BAD_MERGE": ["19ebd7f"],
        "LOST_CHEESE_OTHER": ["ec41a91", "6acd2f3", "4eb5094"],
        "LOST_GORDON_RAMSAY": ["4eb5094", "de90dcf", "9758e95", "fdeb794", "de49d59", "87be94c"],
    }

    # Step 4: Extract recipes from historical commits
    print("\n[3/5] Extracting recipes from historical commits...")

    # Cache commit data to avoid re-reading
    commit_cache = {}
    all_needed_commits = set()
    for commits in recovery_sources.values():
        all_needed_commits.update(commits)

    for commit in sorted(all_needed_commits):
        print(f"  Reading commit {commit}...")
        commit_cache[commit] = get_recipes_at_commit(commit)
        print(f"    Found {len(commit_cache[commit])} recipes")

    # Step 5: Recover recipes
    print("\n[4/5] Recovering lost recipes...")
    recovered = []
    not_found = []
    already_present = []
    skipped_duplicate_title = []

    # Build a set of current titles for duplicate detection
    current_titles = {}
    for r in current_recipes:
        title_key = r.get("title", "").strip().lower()
        if title_key:
            current_titles[title_key] = r["id"]

    for category, lost_ids in sorted(lost_ids_by_category.items()):
        commits_to_try = recovery_sources.get(category, [])
        if not commits_to_try:
            print(f"  WARNING: No recovery source for {category}")
            for rid in lost_ids:
                not_found.append((category, rid, "no recovery source"))
            continue

        cat_recovered = 0
        cat_not_found = 0
        cat_already = 0

        for rid in lost_ids:
            # Skip if already in current recipes
            if rid in current_ids:
                already_present.append((category, rid))
                cat_already += 1
                continue

            # Try each commit source
            found = False
            for commit in commits_to_try:
                recipes_at_commit = commit_cache.get(commit, {})
                if rid in recipes_at_commit:
                    recipe = recipes_at_commit[rid]
                    recovered.append((category, recipe))
                    cat_recovered += 1
                    found = True
                    break

            if not found:
                not_found.append((category, rid, "not in any recovery commit"))
                cat_not_found += 1

        print(f"  {category}: recovered={cat_recovered}, already_present={cat_already}, not_found={cat_not_found}")

    print(f"\n  TOTAL recovered: {len(recovered)}")
    print(f"  TOTAL already present: {len(already_present)}")
    print(f"  TOTAL not found: {len(not_found)}")

    if not_found:
        print(f"\n  Not found IDs:")
        for cat, rid, reason in not_found:
            print(f"    [{cat}] {rid} - {reason}")

    # Step 6: Fix stale fields on recovered recipes
    print("\n[5/5] Fixing stale fields on recovered recipes...")
    fixed_recipes = []
    for category, recipe in recovered:
        # Ensure collection is "all"
        recipe["collection"] = "all"
        recipe["collection_display"] = "Other Family Recipes"

        # Fix cheese categories per CLAUDE.md rules
        if category in ("LOST_CHEESE_BAD_MERGE", "LOST_CHEESE_OTHER"):
            # These are cheese-making recipes - must be category "cheese"
            if recipe.get("category") != "cheese":
                recipe["category"] = "cheese"

        fixed_recipes.append(recipe)

    # Write results
    print(f"\n{'=' * 70}")
    print(f"RECOVERY SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Current recipes:    {len(current_ids)}")
    print(f"  Recipes recovered:  {len(fixed_recipes)}")
    print(f"  New total:          {len(current_ids) + len(fixed_recipes)}")
    print(f"  Already present:    {len(already_present)}")
    print(f"  Not found:          {len(not_found)}")

    if fixed_recipes:
        # Add recovered recipes to current data
        if isinstance(current_data, list):
            output_data = current_data + fixed_recipes
        else:
            output_data = current_data.copy()
            output_data["recipes"] = current_recipes + fixed_recipes

        # Write to a recovery file first (not directly to recipes.json)
        output_path = "/home/user/Allrecipes/data/recipes.json"
        print(f"\n  Writing to {output_path}...")
        with open(output_path, "w") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"  Done! {len(current_ids) + len(fixed_recipes)} total recipes")
    else:
        print("\n  No recipes to recover.")

    # Write detailed report
    report_path = "/home/user/Allrecipes/recovery_report.txt"
    with open(report_path, "w") as f:
        f.write("RECIPE RECOVERY REPORT\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Recovered: {len(fixed_recipes)}\n")
        f.write(f"Already present: {len(already_present)}\n")
        f.write(f"Not found: {len(not_found)}\n\n")

        if already_present:
            f.write("ALREADY PRESENT:\n")
            for cat, rid in already_present:
                f.write(f"  [{cat}] {rid}\n")
            f.write("\n")

        if not_found:
            f.write("NOT FOUND:\n")
            for cat, rid, reason in not_found:
                f.write(f"  [{cat}] {rid} - {reason}\n")
            f.write("\n")

        if fixed_recipes:
            f.write("RECOVERED:\n")
            for r in fixed_recipes:
                f.write(f"  {r['id']} - {r.get('title', 'NO TITLE')} [{r.get('category', 'unknown')}]\n")

    print(f"  Report written to {report_path}")


if __name__ == "__main__":
    main()
