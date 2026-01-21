# Guard Rails for Productive Claude Sessions

This document defines patterns to prevent unproductive token burn in AI-assisted development.

## The Problem: Token-Burning Anti-Patterns

Sessions can waste tokens when:
1. **Circular debugging** - Repeatedly trying the same fix
2. **Scope creep** - Expanding tasks without completing original goal
3. **Over-research** - Reading endlessly without producing output
4. **Perfectionism loops** - Rewriting working code for marginal improvements
5. **Blocked without asking** - Spinning on missing information instead of asking

## Guard Rail Rules

### Rule 1: The Three-Strike Rule
If the same approach fails 3 times:
- **STOP** attempting that approach
- **ASK** the user for clarification or alternative direction
- **DOCUMENT** what was tried and what failed

### Rule 2: Commit Early, Commit Often
- Make an initial commit within the first meaningful change
- Commit after each completed feature/fix
- Never end a session with uncommitted working code
- If no commits after 10+ file operations, something is wrong

### Rule 3: Output-Oriented Progress
Every 5 minutes of work should produce ONE of:
- A new or modified file
- A commit
- A concrete answer to a question
- A documented decision

If none of the above: STOP and reassess.

### Rule 4: Scope Lock
- Define the task clearly before starting
- Do NOT expand scope mid-task without explicit approval
- If a "better" approach emerges, finish current approach first OR ask to pivot

### Rule 5: Missing Information Protocol
When blocked by missing information:
```
1. Identify exactly what is missing
2. Check if it can be reasonably inferred (if yes, proceed)
3. If no, ASK IMMEDIATELY - do not speculate
4. Do not attempt workarounds that might be wrong
```

### Rule 6: The Rewrite Limit
- No file should be rewritten more than 2x without user approval
- If rewriting again, explain WHY previous versions were insufficient
- Consider if the task requirements are unclear

## Session Productivity Checklist

At any point, the session should pass this checklist:

- [ ] Current task is clearly defined
- [ ] Progress is being made toward completion
- [ ] Recent work produced tangible output (file/commit)
- [ ] Not repeating the same operation multiple times
- [ ] No blocking questions remain unanswered

## Red Flags to Watch For

| Red Flag | Action |
|----------|--------|
| Same error 3+ times | Stop, ask user |
| No commits in 15+ minutes of coding | Commit what works |
| Task scope keeps growing | Pause, redefine scope |
| Searching for same thing repeatedly | Ask where it is |
| Rewriting completed work | Ask if changes are needed |
| User seems confused | Clarify before proceeding |

## Recovery Protocol

If a session has become unproductive:

1. **Pause** - Stop the current approach
2. **Summarize** - State what was attempted and results
3. **Commit** - Save any working progress
4. **Ask** - Get user input on direction
5. **Reset** - Start fresh with new approach

## Metrics for This Project

For the Allrecipes project specifically:

**Minimum viable session output:**
- At least 1 complete recipe OR
- At least 1 meaningful improvement to existing content OR
- Clear documentation of a blocker

**Target metrics:**
- 1 commit per recipe added/modified
- Clear recipe structure (ingredients, steps, tips)
- No partially-written recipes left in repo
