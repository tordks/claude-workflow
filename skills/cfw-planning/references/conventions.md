# CWF Planning Conventions

Shared naming and structure conventions for the CWF planning workflow.

## Feature Names

**Format:** kebab-case (lowercase with hyphens)
- **Length:** 2-3 words, concise and descriptive
- **Characters:** lowercase letters, numbers, hyphens only
- **Examples:** `query-command`, `user-auth`, `data-export`

**Used in:**
- Plan: `plans/{feature-name}-plan.md`
- Tasklist: `plans/{feature-name}-tasklist.md`
- Branch: `{prefix}-{feature-name}`

---

## File Structure

```
plans/
├── {feature-name}-plan.md       # Architectural plan (WHY/WHAT)
└── {feature-name}-tasklist.md   # Execution tasklist (WHEN/HOW)
```

**Discovery pattern:**
```bash
ls *-plan.md | sed 's|.*/||; s/-plan\.md$//'
```

---

## Branch Naming

**Format:** `{prefix}-{feature-name}`

**Valid prefixes:**
- `feat` - New features (default)
- `fix` - Bug fixes
- `refactor` - Code refactoring
- `docs` - Documentation only
- `test` - Test additions/changes
- `chore` - Maintenance tasks
- `perf` - Performance improvements

**Examples:**
- `feat-query-command`
- `fix-auth-token-refresh`
- `perf-cache-optimization`

---

## Consistency Rule

Feature names must match across all artifacts:

| Artifact | Format |
|----------|--------|
| Plan file | `plans/query-command-plan.md` |
| Tasklist file | `plans/query-command-tasklist.md` |
| Git branch | `feat-query-command` |
| Document references | "query-command feature" |

This consistency enables easy discovery and clear association between plan, tasklist, and branch.
