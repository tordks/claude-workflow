# Prime Planning Commands

Load common patterns and conventions for planning commands into context.

This command should be invoked at the start of `/write-plan`, `/implement-plan`, and `/amend-plan` commands to establish shared understanding of patterns, formats, and conventions.

---

## Feature Name Parsing

All planning commands accept a feature name as their first argument.

### Format Requirements
- **Pattern:** kebab-case (e.g., `query-command`, `user-auth`)
- **Length:** 2-3 words, concise and descriptive
- **Characters:** lowercase letters, numbers, hyphens only

### Standard Parsing Pattern

**Input:** `$ARGUMENTS`

1. **If feature name is clear:** Extract from first token and use as `{feature-name}`
2. **If unclear or missing:**
   - Scan `plans/` directory for `*-plan.md` files
   - Extract feature names from filenames (e.g., `query-plan.md` → `query`)
   - Present numbered list with brief descriptions
   - Ask user to select by number or type feature name
   - Use selected name for rest of command

### Example Response When Missing

```
Input: $ARGUMENTS is empty

Scanning plans/ directory...

Found the following features:
1. query-command - Document query and search functionality
2. user-auth - User authentication system
3. data-export - Data export capabilities

Which feature would you like to work with? (1-3, or type the feature name)
```

---

## Plan and Tasklist Relationship

Planning creates two complementary documents:

### Plan Document: `plans/{feature-name}-plan.md`
**Purpose:** WHY and WHAT
- Architectural context and design rationale
- Component overview and relationships
- Design decisions with trade-offs
- Technical approach and dependencies
- Risks and considerations

**When to read:** First, to understand overall design

### Tasklist Document: `plans/{feature-name}-tasklist.md`
**Purpose:** WHEN and HOW
- Phased execution with sequential tasks
- Specific implementation steps
- Task IDs for tracking
- Phase goals and deliverables
- Checkpoints for progress validation

**When to read:** During implementation, for step-by-step guidance

**Working Together:**
1. Read plan first to understand architecture and rationale
2. Follow tasklist for implementation
3. Refer back to plan when task details need clarification

---

## File Structure Conventions

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

### Discovery
- List plans: Find `*-plan.md` in `plans/` directory
- Extract feature name: Remove `-plan.md` suffix
- Verify tasklist exists: Check for matching `*-tasklist.md`

---

## Task ID Format

### Structure: `[PX.Y]`
- **P:** Prefix indicating "Phase"
- **X:** Phase number (0, 1, 2, 3...)
- **Y:** Task number within phase (1, 2, 3...)

### Rules
- Phase 0 is always branch setup
- Task numbering starts at 1 within each phase
- Sequential numbering within phases (no gaps)
- IDs are immutable once created
- Never reuse or skip IDs

### Checkbox Format
```markdown
- [ ] [P2.3] Incomplete task description
- [x] [P2.3] Completed task description
```

### Example Sequence
```markdown
## Phase 0: Branch Setup
- [ ] [P0.1] Create feature branch feat-query-command

## Phase 1: Foundation
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic
- [ ] [P1.3] Add validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
```

---

## Branch Naming Convention

### Format: `{prefix}-{feature-name}`

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

### Examples
- `feat-query-command`
- `fix-auth-token-refresh`
- `refactor-module-structure`
- `perf-cache-optimization`

---

## Standard Phase Structure

Every phase in a tasklist follows this structure:

```markdown
## Phase X: Descriptive Name

**Goal:** One-sentence description of what this phase accomplishes

**Deliverable:** Concrete outcome (e.g., "Working data models with validation passing tests")

**Tasks:**
- [ ] [PX.1] Specific atomic action - file/component detail
- [ ] [PX.2] Another specific action with clear scope
- [ ] [PX.3] Write tests for implemented functionality
- [ ] [PX.4] Verify tests pass and code quality checks succeed

**Phase X Checkpoint:** Brief description of system state after phase completion
```

### Phase Requirements
- Code must be in runnable state after each phase
- Each task should be atomic and testable (15-30 minutes)
- Clear goal and deliverable defined upfront
- Checkpoint describes what's been accomplished
- Tasks ordered logically (setup → implementation → testing → validation)

---

## Tasklist Header

Include this at the top of every tasklist:

```markdown
> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `{feature-name}-plan.md` for architectural context
```

---

**Priming complete.** Common patterns loaded into context. You can now proceed with your command-specific instructions.
