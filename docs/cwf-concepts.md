# CWF Concepts

This document explains CWF's core concepts and workflow. For the general skills/commands/agents pattern, see [concepts.md](concepts.md). For detailed command usage, see [workflow-guide.md](workflow-guide.md).

## Overview

Claude Workflow (CWF) is a plan-driven development workflow for Claude Code. It uses the skills/commands/agents pattern to separate knowledge, orchestration, and execution:


## Core Concepts

### Plans and Tasklists

CWF uses two complementary documents that work together to guide feature implementation:

#### Plan Document: `plans/{feature-name}-plan.md`

**Purpose:** WHY and WHAT

**Content:**
- **Overview:** Purpose, scope, success criteria
- **Architecture & Design:** Component overview, project structure, design decisions with rationale, data flow
- **Technical Approach:** Dependencies, integration points, error handling
- **Implementation Strategy:** Phase breakdown, testing approach, deployment notes
- **Risks & Considerations:** Technical challenges, performance implications, security concerns, technical debt

**When to Read:** First, before starting implementation, to understand the overall design and architectural context

**Key Characteristics:**
- Explains rationale behind decisions
- Documents alternatives considered
- Provides architectural context
- Focuses on understanding over execution

#### Tasklist Document: `plans/{feature-name}-tasklist.md`

**Purpose:** WHEN and HOW

**Content:**
- **Usage Header:** Quick guide to using the tasklist
- **Phase 0:** Branch setup (always first)
- **Phase 1+:** Implementation phases with:
  - Goal: What this phase accomplishes
  - Deliverable: Concrete outcome
  - Tasks: Specific actions with IDs
  - Checkpoint: System state after completion

**When to Read:** During implementation, for step-by-step execution guidance

**Key Characteristics:**
- Actionable, specific tasks
- Sequential execution order
- Progress tracking via checkboxes
- Testable deliverables at each phase

#### How They Work Together

Plans and tasklists are created using `/write-plan` and updated using `/amend-plan`. During implementation, read the plan first for context, then follow the tasklist for execution steps. Refer back to the plan when task details need clarification.

**Example Relationship:**

**Plan says:** "Use TF-IDF ranking for query results (Design Decision: Simple, well-understood algorithm; can upgrade to neural ranking in v2 if needed)"

**Tasklist says:**
- `[P2.1] Implement TF-IDF scoring in ranker.py`
- `[P2.2] Add tests for TF-IDF ranking with sample documents`

**When implementing P2.1:** If unclear about TF-IDF parameters, check plan's "Technical Approach" section for specifics.

### Phases and Tasks

#### Phases

**Definition:** Major milestone in feature implementation with clear goal and deliverable

**Structure:**
```markdown
## Phase X: Descriptive Name

**Goal:** One-sentence description of what this phase accomplishes

**Deliverable:** Concrete outcome (e.g., "Working data models with validation passing tests")

**Tasks:**
- [ ] [PX.1] Specific atomic action
- [ ] [PX.2] Another specific action
- [ ] [PX.3] Write tests for functionality
- [ ] [PX.4] Verify tests pass

**Phase X Checkpoint:** Brief description of system state after phase completion
```

**Requirements:**
- Code must be in runnable state after each phase
- Each phase should take 1-3 hours total
- Clear deliverable that can be tested
- Checkpoint documents what's been accomplished

**Phase 0 (Always):**
- Reserved for branch setup
- Single task: Create feature branch
- Must complete before implementation phases

**Implementation Phases (1+):**
- Numbered sequentially: Phase 1, Phase 2, Phase 3, etc.
- Each builds on previous phases
- Tasks within phase are ordered logically
- Phase ends when all tasks complete and tests pass

#### Tasks

**Definition:** Atomic, testable unit of work

**Format:** `- [ ] [PX.Y] Task description with specific file/component details`

**Components:**
- `[ ]` or `[x]`: Checkbox for completion tracking
- `[PX.Y]`: Unique task ID
  - P: "Phase" prefix
  - X: Phase number
  - Y: Task number within phase
- Description: Clear, actionable statement of what to do

**Requirements:**
- Each task should take 15-30 minutes
- Must be atomic (complete in one go)
- Must be testable (can verify it's done)
- Should reference specific files or components
- Must be in logical order (dependencies come first)

**Task ID Rules:**
- IDs are immutable once created
- Never reuse or skip IDs
- Sequential numbering within phases (no gaps)
- Start at .1 for each phase

**Examples:**

Good tasks:
- `[P1.1] Create query/ directory and __init__.py`
- `[P1.2] Create QueryModel class with Pydantic in models.py`
- `[P1.3] Add field validation to QueryModel (required fields, type checks)`
- `[P1.4] Write unit tests for QueryModel validation`

Too vague:
- `[P1.1] Set up module`
- `[P1.2] Add query stuff`

Too large:
- `[P1.1] Implement entire query system with models, parser, and ranking`

#### Checkpoints

**Definition:** Statement of system state after phase completion

**Purpose:**
- Document what's been accomplished
- Verify phase goals met
- Provide context for next phase
- Enable safe stopping points

**Format:** 1-2 sentences describing system capabilities and state

**Examples:**
- "Core data models validated, ready for parser implementation"
- "Query parser complete with DSL support, validated against test cases"
- "End-to-end query flow working with TF-IDF ranking, ready for optimization"

### Amendments

**Definition:** Changes to existing plan and tasklist documents

**When to Amend:**
- Discovered new requirements during implementation
- Need to add tasks to incomplete phases
- Want to create new phases
- Need to clarify or expand plan sections
- Realized better approach mid-implementation

**What NOT to Amend:**
- Completed tasks (immutable)
- Completed phases (all tasks marked [x])
- Historical decisions (document instead in plan)

#### Amendment Types

**Add Tasks to Incomplete Phase:**
- Insert after last existing task in phase
- Use next sequential task ID
- New tasks start unchecked [ ]
- Preserve phase goal and deliverable

**Add New Phase:**
- Add after highest existing phase number
- Follow standard phase structure
- All tasks start unchecked
- Tasks numbered from .1

**Modify Incomplete Task Descriptions:**
- Only tasks marked [ ] (not [x])
- Keep task ID unchanged
- Update description text
- Maintain checkbox format

**Update Plan Sections:**
- Add new subsections
- Clarify existing content
- Add examples or details
- Document why amendment was made

#### Safety Rules

**NEVER:**
- Modify completed tasks (marked [x])
- Change task IDs
- Add tasks to completed phases
- Delete completed work
- Modify historical decisions

**ALWAYS:**
- Confirm proposed changes with user
- Explain why modifications aren't allowed
- Suggest alternatives for blocked operations
- Document amendment rationale in plan

**WHY:**
- Completed work represents implemented code
- Changing history breaks implementation tracking
- Task IDs provide stable references
- Immutability ensures reliable progress tracking

### File and Branch Naming

#### Branch Naming

**Format:** `{prefix}-{feature-name}`

**Valid Prefixes:**
- `feat` - New features (default)
- `fix` - Bug fixes
- `refactor` - Code refactoring
- `docs` - Documentation only
- `test` - Test additions/changes
- `chore` - Maintenance tasks
- `perf` - Performance improvements

**Requirements:**
- Use kebab-case (lowercase with hyphens)
- No special characters except hyphens
- Keep concise and descriptive
- Match feature name from plan files

**Examples:**
- `feat-query-command`
- `feat-user-authentication`
- `fix-search-performance`
- `refactor-api-structure`

#### File Naming

**Feature Name:**
- Format: kebab-case
- Length: 2-3 words
- Characters: lowercase letters, numbers, hyphens only
- Examples: `query-command`, `user-auth`, `data-export`

**Plan Files:**
- Pattern: `plans/{feature-name}-plan.md`
- Example: `plans/query-command-plan.md`

**Tasklist Files:**
- Pattern: `plans/{feature-name}-tasklist.md`
- Example: `plans/query-command-tasklist.md`

**Consistency:**
- Feature name must match across all files
- Branch name derived from feature name
- All references use same feature name

## CWF Workflow

### Skills Overview

CWF includes two core skills that provide specialized knowledge:

**cfw-planning:**
- implementation-essentials.md - Minimal implementation guide (load first for implementation)
- validation.md - Validation checklist for plans and tasklists
- amendment.md - Amendment rules and safety guidelines
- plan-structure.md - Plan document structure and requirements
- tasklist-structure.md - Tasklist document structure and task guidelines
- document-synergy.md - How plan and tasklist work together
- conventions.md - Feature naming, file structure, branch naming
- Used by: `/write-plan`, `/implement-plan`, `/amend-plan`
- For complete reference, see `skills/cfw-planning/SKILL.md`

**read-constitution:**
- Loads coding principles from `.constitution/` files
- Software engineering fundamentals, testing philosophy, Python standards
- Used by: `/implement-plan` (automatic), `/read-constitution` (manual)


### Commands Overview

CWF provides three main commands that orchestrate the workflow:

**/write-plan {feature-name}:**
- Create plan and tasklist from planning discussion
- Loads `cfw-planning` skill
- Analyzes conversation and structures documents

**/implement-plan {feature-name}:**
- Execute implementation phase-by-phase
- Loads `read-constitution` and `cfw-planning` skills
- Follows tasklist, marks tasks complete, stops at phase boundaries

**/amend-plan {feature-name}:**
- Update existing plan and tasklist
- Loads `cfw-planning` skill
- Safely adds tasks/phases without modifying completed work

For detailed usage, see [workflow-guide.md](workflow-guide.md). For complete command reference, see [commands-reference.md](commands-reference.md).

### Workflow States

**Planning:**
- Plan mode conversation active
- No files created yet
- Discussing approach and architecture

**Documented:**
- Plan and tasklist files created via `/write-plan`
- Ready for implementation
- May still be refined before starting

**In Progress:**
- Implementation started via `/implement-plan`
- Some tasks/phases completed
- Tasklist shows progress via checkboxes

**Phase Complete:**
- All tasks in current phase marked [x]
- Checkpoint reached
- Waiting for user approval to continue

**Feature Complete:**
- All phases complete
- All tasks marked [x]
- Ready for final review and merge

**Amended:**
- Original plan modified via `/amend-plan`
- New tasks or phases added
- May return to "In Progress" state

### Progress Tracking

**Checkbox States:**
- `[ ]` - Task not started
- `[x]` - Task completed

**Phase States:**
- Not Started: No tasks marked [x]
- In Progress: Some tasks marked [x]
- Complete: All tasks marked [x]

**Feature States:**
- Not Started: Phase 0 not complete
- In Progress: Phase 0+ complete, some phases incomplete
- Complete: All phases complete

**Tracking in Tasklist:**
- Edit file to mark tasks complete
- Use Edit tool: change `[ ]` to `[x]`
- Atomic updates (one task at a time)
- Done immediately after completing task

**Tracking in Commits:**
- One commit per phase completion
- Commit message references phase
- Includes phase checkpoint in body
- Shows which tasks were completed


## Design Decisions

### Why Two Documents (Plan + Tasklist)?

**Separation of WHY/WHAT vs WHEN/HOW:**
- Plan documents architectural context and rationale
- Tasklist provides step-by-step execution guidance
- Implementation engineer reads plan first for understanding, then follows tasklist

### Why Skills Instead of Inline Knowledge?

**Benefits of skills-first approach:**
- Planning conventions centralized in `cfw-planning` skill
- All three commands use same knowledge
- Update conventions in one place, all commands benefit
- Easier to maintain and extend

### Why Phase-Based Implementation?

**Reviewable checkpoints:**
- Code must be runnable after each phase
- Stop for user review between phases
- Enables incremental progress and atomic commits
- Reduces risk of large, untested changes

## References

- **General Pattern:** See [concepts.md](concepts.md) for skills/commands/agents explanation
- **Command Usage:** See [workflow-guide.md](workflow-guide.md) for step-by-step guide
- **Command Reference:** See [commands-reference.md](commands-reference.md) for complete API reference
- **Future Plans:** See [future-phases.md](future-phases.md) for roadmap

