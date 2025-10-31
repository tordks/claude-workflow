# Plan Command

You are being asked to formalize the planning discussion from plan mode into structured documentation for the **$ARGUMENTS** feature.

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

**Arguments**: `$ARGUMENTS` captures the feature name if provided (e.g., `/write-plan query-command`).

## Instructions

Review the conversation history from plan mode and create two documents in the `plans/` directory:

### 1. Plan Document: `plans/{feature-name}-plan.md`

Formalize the discussed plan with:

- **Overview/Purpose**: What is being built and why (from discussion)
- **Technical Approach**: The strategy that was agreed upon
- **Architecture & Design**: Components, data flow, and design decisions from the discussion
- **Implementation Strategy**: The step-by-step approach that was refined through iteration
- **Dependencies**: External libraries, services, or prerequisites identified
- **Testing Approach**: How to verify the implementation works
- **Risks & Considerations**: Potential challenges or trade-offs discussed

### 2. Tasklist Document: `plans/{feature-name}-tasklist.md`

Convert the discussed plan into a phase-based tasklist with:

- **Phase 0: Branch Setup** (always first):
  - Goal: Create and checkout feature branch for isolated development
  - Task: Include brief description of suggested branch name and rationale
  - Include the git command: `git checkout -b {suggested-branch-name}`
- **Multiple phases** organized logically (e.g., Phase 1: Setup, Phase 2: Core Implementation, Phase 3: Testing)
- **Runnable state requirement**: Code must be in a working, runnable state after completing each phase
- **Task format**: Each task must have:
  - A unique ID using phase numbering (e.g., `[P0.1]` for Phase 0, `[P1.1]`, `[P1.2]` for Phase 1 tasks)
  - A checkbox `[ ]` for tracking completion
  - Clear, actionable description based on what was discussed
  - Format: `- [ ] [PX.Y] Task description`

## Requirements

- **Feature name**:
  - If `$ARGUMENTS` is provided, use that as the feature name
  - If `$ARGUMENTS` is empty, suggest a concise feature name (2-3 words) based on the plan discussion
  - Use kebab-case format (e.g., `query-command`, `user-auth`, `data-export`)
  - Present suggestion to user for confirmation before proceeding
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

Tasklist example:

````markdown
## Phase 0: Branch Setup

**Goal**: Create and checkout feature branch for isolated development

**Tasks**:
- [ ] [P0.1] Create feature branch `feat-query-command` for document query implementation
  ```bash
  git checkout -b feat-query-command
  ```

## Phase 1: Foundation

**Goal**: Establish core module structure and data models

**Tasks**:

- [ ] [P1.1] Set up basic module structure
- [ ] [P1.2] Create core data models with Pydantic
- [ ] [P1.3] Write unit tests for models

## Phase 2: Implementation

**Goal**: Implement query functionality with error handling

**Tasks**:

- [ ] [P2.1] Implement query parser
- [ ] [P2.2] Add error handling
- [ ] [P2.3] Integration testing

````
