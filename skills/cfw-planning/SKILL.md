# Claude Workflow Planning

This skill provides comprehensive guidance for creating and managing plans and tasklists in Claude Workflow. It covers planning conventions, document structures, and how plans and tasklists work together.

---

## Part 1: Plan Document Structure (WHY/WHAT - Strategic)

Plans provide architectural context and design rationale. They explain WHY decisions were made and WHAT the feature accomplishes.

### Plan Document: `plans/{feature-name}-plan.md`

**Purpose:** WHY and WHAT
- Architectural context and design rationale
- Component overview and relationships
- Design decisions with trade-offs
- Technical approach and dependencies
- Risks and considerations

**When to read:** First, to understand overall design

### File Structure Conventions

#### Directory Layout
```
plans/
├── {feature-name}-plan.md       # Architectural plan
└── {feature-name}-tasklist.md   # Execution tasklist
```

#### Naming Rules
- Feature name must match between both files
- Use kebab-case consistently
- Plan: `{feature-name}-plan.md`
- Tasklist: `{feature-name}-tasklist.md`

#### Discovery
- List plans: Find `*-plan.md` in `plans/` directory
- Extract feature name: Remove `-plan.md` suffix
- Verify tasklist exists: Check for matching `*-tasklist.md`

### Required Plan Sections

Every plan document should include these sections:

#### 1. Overview
- **Purpose:** One-sentence description of what feature does
- **Scope:** What's included and explicitly NOT included
- **Success Criteria:** Testable conditions for "done"

#### 2. Architecture & Design
- **Component Overview:** High-level system parts
- **Project Structure:** File tree with [CREATE] and [MODIFY] markers
- **Design Decisions:** Decision + WHY rationale format
- **Data Flow:** How information moves through system (if applicable)

#### 3. Technical Approach
- **Dependencies:** External libraries, tools, services
- **Integration Points:** How feature connects to existing code
- **Error Handling:** Strategy for managing failures

#### 4. Implementation Strategy
- **Phase Breakdown:** Overview of phases and their goals
- **Testing Approach:** How feature will be validated
- **Deployment Notes:** Any special deployment considerations

#### 5. Risks & Considerations
- **Technical Challenges:** What could go wrong
- **Performance Considerations:** Scalability, speed concerns
- **Security Considerations:** Vulnerabilities, mitigations
- **Technical Debt:** Known limitations or shortcuts

### File Tree Conventions

Use code blocks with file paths to show project structure:
- Mark new files: `[CREATE]`
- Mark modified files: `[MODIFY]`

**Example:**
```
src/auth/
├── __init__.py    [CREATE]
├── models.py      [CREATE]
└── login.py       [MODIFY]
```

### Design Decision Format

Document decisions with rationale:

```markdown
### Design Decisions

**1. Decision Name**
- **Decision:** What was chosen
- **Rationale:** WHY this choice was made (trade-offs, constraints, benefits)
- **Alternatives Considered:** What else was evaluated
- **Impact:** How this affects architecture
```

---

## Part 2: Tasklist Document Structure (WHEN/HOW - Tactical)

Tasklists provide phased execution steps. They explain WHEN tasks happen and HOW to implement them.

### Tasklist Document: `plans/{feature-name}-tasklist.md`

**Purpose:** WHEN and HOW
- Phased execution with sequential tasks
- Specific implementation steps
- Task IDs for tracking
- Phase goals and deliverables
- Checkpoints for progress validation

**When to read:** During implementation, for step-by-step guidance

### Feature Name Requirements

All planning commands accept a feature name as their first argument.

#### Format Requirements
- **Pattern:** kebab-case (e.g., `query-command`, `user-auth`)
- **Length:** 2-3 words, concise and descriptive
- **Characters:** lowercase letters, numbers, hyphens only

#### Standard Parsing Pattern

**Input:** `$ARGUMENTS`

1. **If feature name is clear:** Extract from first token and use as `{feature-name}`
2. **If unclear or missing:**
   - Scan `plans/` directory for `*-plan.md` files
   - Extract feature names from filenames (e.g., `query-plan.md` → `query`)
   - Present numbered list with brief descriptions
   - Ask user to select by number or type feature name
   - Use selected name for rest of command

#### Example Response When Missing

```
Input: $ARGUMENTS is empty or does not contain a clear feature name.

Scanning plans/ directory...

Found the following features:
1. query-command - Document query and search functionality
2. user-auth - User authentication system
3. data-export - Data export capabilities

Which feature would you like to work with? (1-3, or type the feature name)
```

### Task ID Format

#### Structure: `[PX.Y]`
- **P:** Prefix indicating "Phase"
- **X:** Phase number (0, 1, 2, 3...)
- **Y:** Task number within phase (1, 2, 3...)

#### Rules
- Phase 0 is always setup
- Task numbering starts at 1 within each phase
- Sequential numbering within phases (no gaps)
- IDs are immutable once created
- Never reuse or skip IDs

#### Checkbox Format
```markdown
- [ ] [P2.3] Incomplete task description
- [x] [P2.3] Completed task description
```

#### Example Sequence
```markdown
## Phase 0: Branch Setup
- [ ] [P0.1] Create feature branch feat-query-command

## Phase 1: Foundation
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic
- [ ] [P1.3] Add validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
```

### Branch Naming Convention

#### Format: `{prefix}-{feature-name}`

#### Valid Prefixes
| Prefix | Purpose |
|--------|---------|
| `feat` | New features (default) |
| `fix` | Bug fixes |
| `refactor` | Code refactoring |
| `docs` | Documentation only |
| `test` | Test additions/changes |
| `chore` | Maintenance tasks |
| `perf` | Performance improvements |

#### Requirements
- Use kebab-case (lowercase with hyphens)
- No special characters except hyphens
- Keep concise and descriptive

#### Examples
- `feat-query-command`
- `fix-auth-token-refresh`
- `refactor-module-structure`
- `perf-cache-optimization`

### Standard Phase Structure

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

#### Phase Requirements
- Code must be in runnable state after each phase
- Each task should be atomic and testable (15-30 minutes)
- Clear goal and deliverable defined upfront
- Checkpoint describes what's been accomplished
- Tasks ordered logically (setup → implementation → testing → validation)

### Task Granularity Guidelines

- Each task should be 15-30 minutes
- Tasks should be atomic (one clear action)
- Tasks should be testable (verifiable completion)
- Tasks should reference specific files or components

### Status Tracking

- `- [ ]` Pending (not started)
- `- [x]` Complete (finished and verified)

### Task Ordering Principles

Within each phase, order tasks:
1. Setup/preparation tasks (create directories, models)
2. Implementation tasks (add functionality, business logic)
3. Testing tasks (write tests, run tests)
4. Validation tasks (verify phase complete, check quality)
5. Documentation tasks (update docs, add comments)

Dependencies always come before dependents.

### Phase 0 Special Case

Phase 0 is always branch setup:
- Typically has 1-2 tasks: create branch, initialize structure

**Example:**
```markdown
## Phase 0: Branch Setup
**Goal:** Create feature branch for isolated development
**Tasks:**
- [ ] [P0.1] Create feature branch `feat-{feature-name}`
  ```bash
  git checkout -b feat-{feature-name}
  ```
```

### Tasklist Header

Include this at the top of every tasklist:

```markdown
> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `{feature-name}-plan.md` for architectural context
```

---

## Part 3: Document Synergy (Relationship)

Plans and tasklists are complementary documents that work together throughout implementation.

### How They Work Together

Planning creates two complementary documents:

**Plan Document: `plans/{feature-name}-plan.md`**
- **Purpose:** WHY and WHAT
- Architectural context and design rationale
- Component overview and relationships
- Design decisions with trade-offs
- Technical approach and dependencies
- Risks and considerations
- **When to read:** First, to understand overall design

**Tasklist Document: `plans/{feature-name}-tasklist.md`**
- **Purpose:** WHEN and HOW
- Phased execution with sequential tasks
- Specific implementation steps
- Task IDs for tracking
- Phase goals and deliverables
- Checkpoints for progress validation
- **When to read:** During implementation, for step-by-step guidance

### Working Together

1. Read plan first to understand architecture and rationale
2. Follow tasklist for implementation
3. Refer back to plan when task details need clarification

### Consistency Rules

- Feature name must match between both files
- Phase breakdown in plan should align with phases in tasklist
- Success criteria in plan should align with final phase deliverable in tasklist
- File references in plan should match files created/modified in tasklist

### When to Update Each

- **Update plan when:** Architecture changes, design decisions change, new risks identified
- **Update tasklist when:** Tasks need to be added/removed/reordered, phase structure changes
- **Update both when:** Scope changes, requirements change, implementation approach pivots

### Plan Provides Context for Tasklist

- Why decisions were made → Informs how to implement tasks
- What components exist → Clarifies which files to modify
- What risks to consider → Guides error handling in tasks
- What testing approach → Informs which tests to write

### Tasklist Operationalizes Plan

- Phases break down implementation strategy
- Tasks make architecture concrete
- Checkpoints validate plan assumptions
- Status tracking shows progress toward success criteria

---

## Summary

**Plans** explain WHY and WHAT (strategic, architectural)
**Tasklists** explain WHEN and HOW (tactical, execution)
**Together** they provide complete guidance from concept to implementation
