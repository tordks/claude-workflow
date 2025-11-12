# CWF Planning Conventions

Shared naming and structure conventions used across CWF planning workflow.

## Feature Names

### Format Requirements
- **Pattern:** kebab-case (lowercase with hyphens)
- **Length:** 2-3 words, concise and descriptive
- **Characters:** lowercase letters, numbers, hyphens only
- **Examples:** `query-command`, `user-auth`, `data-export`

### Purpose
Feature names serve as the common identifier across all planning artifacts:
- Plan filename: `{feature-name}-plan.md`
- Tasklist filename: `{feature-name}-tasklist.md`
- Branch name: `{prefix}-{feature-name}`

---

## File Structure

### Directory Layout
```
plans/
├── {feature-name}-plan.md       # Architectural plan
└── {feature-name}-tasklist.md   # Execution tasklist
```

### Naming Rules
- Feature name must match between both files
- Use kebab-case consistently
- Plan: `{feature-name}-plan.md`
- Tasklist: `{feature-name}-tasklist.md`

### Discovery Patterns
To find existing plans:
- List files: `*-plan.md` in `plans/` directory
- Extract feature name: Remove `-plan.md` suffix
- Verify tasklist: Check for matching `*-tasklist.md`

---

## Branch Naming

### Format
`{prefix}-{feature-name}`

### Valid Prefixes
| Prefix | Purpose |
|--------|---------|
| `feat` | New features (default) |
| `fix` | Bug fixes |
| `refactor` | Code refactoring |
| `docs` | Documentation only |
| `test` | Test additions/changes |
| `chore` | Maintenance tasks |
| `perf` | Performance improvements |

### Requirements
- Use kebab-case (lowercase with hyphens)
- No special characters except hyphens
- Keep concise and descriptive
- Must match feature name from plan/tasklist files

### Examples
- `feat-query-command`
- `fix-auth-token-refresh`
- `refactor-module-structure`
- `perf-cache-optimization`

---

## Consistency Rules

Feature names must be consistent across all artifacts:

**File naming:**
- `plans/query-command-plan.md`
- `plans/query-command-tasklist.md`

**Branch naming:**
- `feat-query-command`

**Document references:**
- Plan refers to "query-command feature"
- Tasklist refers to "query-command feature"
- All internal references use same name

This consistency enables:
- Easy discovery of related artifacts
- Clear association between plan, tasklist, and branch
- Simple automation and tooling
