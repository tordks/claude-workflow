# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Bootstrap

Use the SlashCommand tool to execute: `/prime-planning-commands`

Wait for it to complete, then proceed with instructions below.

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

Use the standard feature name parsing pattern from `/prime-planning-commands`.

**Special case for write-plan:** If no feature name is provided, SUGGEST a feature name based on the conversation (don't list existing plans, since this creates NEW plans):

```
Based on our conversation about adding document query functionality, I suggest
the feature name: "query-command"

This will create:
- plans/query-command-plan.md
- plans/query-command-tasklist.md

Should I proceed with "query-command" as the feature name?
```

## Instructions

Review the conversation history from plan mode and create two documents in the `plans/` directory:

### 1. Plan Document: `plans/{feature-name}-plan.md`

Formalize the discussed plan with this structure:

#### Overview
- **Purpose**: What is being built and why (from discussion)
- **Scope**: What's included and what's not
- **Success Criteria**: How we know it's complete

#### Architecture & Design

**Component Overview**: High-level description of major components and their relationships

**Project Structure**: Show a file tree with [CREATE] and [MODIFY] annotations
```
src/
├── feature/
│   ├── __init__.py          [CREATE] - Public exports
│   ├── models.py            [CREATE] - Data models
│   ├── service.py           [MODIFY] - Integration points
tests/
└── test_feature.py          [CREATE] - Tests
```

**Design Decisions**: Key architectural choices and their rationale
- List decisions with WHY (rationale), not just WHAT
- Include trade-offs that were accepted

**Data Flow**: How data moves through the system (descriptions or diagrams if discussed)

#### Technical Approach
- **Dependencies**: External libraries, system requirements, configuration changes
- **Integration Points**: How this integrates with existing codebase
- **Error Handling Strategy**: Approach to errors, validation, edge cases

#### Implementation Strategy
- **Phase Breakdown**: Brief overview of what each phase accomplishes and why they're ordered this way
- **Testing Approach**: Unit testing strategy, integration testing approach, manual testing steps
- **Migration/Deployment Notes**: Any special considerations for rolling out (if applicable)

#### Risks & Considerations
- Potential challenges or blockers
- Performance implications
- Security considerations
- Technical debt or future refactoring needs

**Note**: The plan provides architectural context and design decisions. It answers WHY and WHAT (architecture). Keep it balanced - detailed enough to guide implementation but not overly prescriptive.

### 2. Tasklist Document: `plans/{feature-name}-tasklist.md`

Convert the discussed plan into a phase-based tasklist with this structure:

#### Header Section
Include a brief usage guide at the top:
```markdown
> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `{feature-name}-plan.md` for architectural context
```

#### Phase 0: Branch Setup (always first)
- **Goal**: Create and checkout feature branch for isolated development
- **Tasks**: Single task with git command
  - Format: `- [ ] [P0.1] Create feature branch {branch-name} for {brief description}`
  - Include: `git checkout -b {suggested-branch-name}`

#### Subsequent Phases
Organize logically (e.g., Phase 1: Foundation, Phase 2: Core Implementation, Phase 3: Testing)

Each phase must have:
- **Goal**: One-sentence description of what this phase accomplishes
- **Deliverable**: Concrete outcome (e.g., "Working data models with validation passing tests")
- **Tasks**: List of granular tasks (15-30 minutes each)
  - Each task format: `- [ ] [PX.Y] {Specific atomic action} - {File/component detail}`
  - Tasks should be atomic and testable
  - When relevant, mention specific files being created/modified
  - Examples of granular tasks:
    - `- [ ] [P1.1] Create User model with Pydantic validation in models.py`
    - `- [ ] [P1.2] Add email validation logic to User model`
    - `- [ ] [P1.3] Write unit tests for User model validation`
- **Phase X Checkpoint**: Brief description of system state after phase completion

#### Requirements
- **Task granularity**: Each task should take 15-30 minutes and be a single, testable action
- **Runnable state**: Code must be in a working, runnable state after completing each phase
- **Task IDs**: Unique ID using phase numbering (e.g., `[P0.1]`, `[P1.1]`, `[P1.2]`)
- **Checkboxes**: Format `- [ ]` for tracking completion
- **Clear descriptions**: Actionable based on what was discussed, reference specific files when relevant

**Note**: The tasklist provides step-by-step execution tracking. It answers WHEN (phase order) and HOW (specific steps). It breaks down the plan into bite-sized, achievable tasks.

## Requirements

- **Branch naming**: Use standard format from `/prime-planning-commands` (e.g., `feat-query-command`)
- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Make sure completing each phase leaves the codebase in a stable state
- Break down high-level plans into granular, testable tasks (15-30 min each)
- Use clear, concise language

## Example Output

For a feature called "query-command", create `plans/query-command-plan.md` and `plans/query-command-tasklist.md`:

### Plan Document (excerpt):

```markdown
# Query Command - Implementation Plan

## Overview
- **Purpose**: Add document query functionality to search and filter documents
- **Scope**: Basic keyword search, file type filtering. NOT: full-text search, fuzzy matching
- **Success Criteria**: Users can query documents with filters and get ranked results

## Architecture & Design

### Project Structure
```
src/query/
├── __init__.py    [CREATE] - Public exports
├── models.py      [CREATE] - Query models
└── parser.py      [CREATE] - Query parser
tests/
└── test_query.py  [CREATE] - Unit tests
```

### Design Decisions
- **Query DSL**: Simple key:value syntax for UX and reduced complexity
- **Ranking**: TF-IDF for initial version, can upgrade later
...
```

### Tasklist Document (excerpt):

```markdown
# Query Command - Implementation Tasklist

> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `query-command-plan.md` for architectural context

## Phase 0: Branch Setup
**Goal**: Create feature branch for isolated development
**Tasks**:
- [ ] [P0.1] Create feature branch `feat-query-command`
  ```bash
  git checkout -b feat-query-command
  ```

## Phase 1: Foundation
**Goal**: Establish core module structure and data models
**Deliverable**: Working query models with validation passing tests
**Tasks**:
- [ ] [P1.1] Create query/ directory and __init__.py
- [ ] [P1.2] Create QueryModel class with Pydantic in models.py
- [ ] [P1.3] Add field validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
- [ ] [P1.5] Verify tests pass with pytest
**Phase 1 Checkpoint**: Core data models validated, ready for parser
...
```
