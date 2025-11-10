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

Review the conversation history from plan mode and create two documents in the `plans/` directory.

### Document Structure

**Plan (`plans/{feature-name}-plan.md`):**
- Overview: purpose, scope, success criteria
- Architecture & Design: component overview, project structure (file tree with [CREATE]/[MODIFY]), design decisions (with WHY rationale), data flow
- Technical Approach: dependencies, integration points, error handling
- Implementation Strategy: phase breakdown, testing approach, deployment notes
- Risks & Considerations: challenges, performance, security, technical debt

**Tasklist (`plans/{feature-name}-tasklist.md`):**
- Usage header (see prime-planning-commands.md for format)
- Phase 0: Branch setup with git command
- Phase 1+: Each phase has goal, deliverable, tasks (with [PX.Y] IDs), checkpoint
- Tasks: 15-30 min each, atomic, testable, reference specific files

See prime-planning-commands.md for standard formats and task ID conventions. See Example Output below for concrete structure.

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
