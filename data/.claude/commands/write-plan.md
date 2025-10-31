# Plan Command

You are being asked to formalize the planning discussion from plan mode into structured documentation.

## Context

This command is run AFTER iterating with Claude in plan mode. The user has
already discussed and refined the approach with you. Your job is to capture and
formalize what was discussed.

Assume that the engineer that shall use the plan has zero context for our
codebase and questionable taste. document everything they need to know. which
files to touch for each task, code, testing, docs they might need to check. how
to test it.

Assume they are a skilled developer, but know almost nothing about our toolset
or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

From the arguments above, identify the feature name. The feature name is typically:
- A kebab-case identifier (e.g., `query-command`, `user-auth`)
- The first clear token in the arguments
- May be accompanied by additional instructions or context

If the feature name is clear from the arguments, extract it and use it as `{feature-name}` throughout this command.

If no feature name is provided or it's unclear:
- Suggest a concise feature name (2-3 words) based on the plan discussion
- Use kebab-case format (e.g., `query-command`, `user-auth`, `data-export`)
- Present suggestion to user for confirmation before proceeding

**Example usage:**
- `/write-plan query-command` → feature-name: `query-command`
- `/write-plan user-auth add OAuth support` → feature-name: `user-auth`, context: "add OAuth support"
- `/write-plan` (no args) → suggest feature name based on conversation

**Example when no feature name provided:**
```
Input: $ARGUMENTS is empty

Based on our conversation about adding document query functionality, I suggest
the feature name: "query-command"

This will create:
- plans/query-command-plan.md
- plans/query-command-tasklist.md

Should I proceed with "query-command" as the feature name?
```

**Example with context but no clear feature name:**
```
Input: $ARGUMENTS = "add caching support with Redis"

I see you want to add caching support with Redis, but I need to know which
feature this applies to.

Scanning plans/ directory...

Found the following features:
1. query-command - Document query and search functionality
2. user-auth - User authentication system
3. data-export - Data export capabilities

Which feature should I add caching support to? (1-3, or type the feature name)

Context to include: "add caching support with Redis"
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

- **Generate branch name**: Create a suggested branch name using format `{prefix}-{feature-name}`:
  - Use kebab-case (lowercase with hyphens only)
  - Choose appropriate prefix: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`
  - Default to `feat` unless context suggests otherwise
  - Example: `feat-query-command`, `refactor-module-structure`
- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Make sure completing each phase leaves the codebase in a stable state
- Break down high-level plans into granular, testable tasks
- Use clear, concise language

## Example Format

For a feature called "query", create:

- `plans/query-plan.md`
- `plans/query-tasklist.md`

### Plan Document Example (excerpt):

````markdown
# Query Command - Implementation Plan

## Overview
- **Purpose**: Add document query functionality to search and filter documents
- **Scope**: Basic keyword search, file type filtering, date range queries. NOT including: full-text search, fuzzy matching
- **Success Criteria**: Users can query documents with filters and get ranked results

## Architecture & Design

### Project Structure
```
src/
├── query/
│   ├── __init__.py          [CREATE] - Public exports
│   ├── models.py            [CREATE] - Query models
│   ├── parser.py            [CREATE] - Query parser
│   ├── engine.py            [CREATE] - Search engine
│   └── ranking.py           [CREATE] - Result ranking
tests/
├── unit/
│   └── test_query.py        [CREATE] - Unit tests
└── integration/
    └── test_query_e2e.py    [CREATE] - E2E tests
```

### Design Decisions
- **Query DSL**: Using simple key:value syntax instead of complex grammar to reduce complexity and improve UX
- **Ranking**: TF-IDF for initial version, can upgrade to ML-based later if needed
...
````

### Tasklist Document Example:

````markdown
# Query Command - Implementation Tasklist

> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `query-plan.md` for architectural context

## Phase 0: Branch Setup

**Goal**: Create and checkout feature branch for isolated development

**Tasks**:
- [ ] [P0.1] Create feature branch `feat-query-command` for document query implementation
  ```bash
  git checkout -b feat-query-command
  ```

## Phase 1: Foundation

**Goal**: Establish core module structure and data models

**Deliverable**: Working query models with validation passing tests

**Tasks**:
- [ ] [P1.1] Create query/ directory and __init__.py with module exports
- [ ] [P1.2] Create QueryModel class with Pydantic in models.py
- [ ] [P1.3] Add keyword field validation to QueryModel
- [ ] [P1.4] Add filter fields (file_type, date_range) to QueryModel
- [ ] [P1.5] Write unit tests for QueryModel validation
- [ ] [P1.6] Verify tests pass with pytest

**Phase 1 Checkpoint**: Core data models validated and tested, ready for parser implementation

## Phase 2: Query Parser

**Goal**: Implement query string parsing

**Deliverable**: Working parser that converts strings to QueryModel instances

**Tasks**:
- [ ] [P2.1] Create parser.py with basic parse() function
- [ ] [P2.2] Implement keyword extraction logic
- [ ] [P2.3] Implement key:value filter parsing
- [ ] [P2.4] Add parse error handling and validation
- [ ] [P2.5] Write parser unit tests for valid queries
- [ ] [P2.6] Write parser unit tests for invalid queries
- [ ] [P2.7] Verify all tests pass

**Phase 2 Checkpoint**: Query parser complete with comprehensive error handling

````
