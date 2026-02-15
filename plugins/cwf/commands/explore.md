---
description: Explore feature design through iterative discovery before planning
disable-model-invocation: true
argument-hint: [initial context]
---

# Explore Command

Guide iterative exploration of feature requirements and design before formalizing with /write-plan.

## Context

This command is run BEFORE writing planning documents to explore feature requirements and converge on a design through natural conversation. The agent first understands the repository context, then asks targeted questions, proposes approaches, and incrementally builds a design summary that the user validates before transitioning to `/write-plan`.

## Arguments

**Input**: `$ARGUMENTS`

If arguments are provided, they contain context or initial direction for the exploration session. Use this context to inform your questions and exploration.

## Explore workflow

If skill `claude-workflow` is not loaded, load it using the Skill tool

Read the following if not already loaded:

- `references/plan-spec.md`

### 1. Quick Repository Scan

Get a high-level understanding of the project — just enough to ask informed questions. Do NOT read deeply into the codebase at this stage.

**Do:**

- List the top-level directory structure
- Read project README, CLAUDE.md, or equivalent entrypoint docs if they exist
- Note the language, framework, and rough architecture

**Do NOT:**

- Read source files, tests, or configs beyond the entrypoint docs
- Try to understand every module or convention upfront
- Read files unrelated to what the user wants to explore

Deeper codebase reading happens in step 2, targeted by the feature direction.

### 2. Understand the Idea and Explore Approaches

Start by understanding what the user wants to build, then explore the codebase **as needed** to inform your questions and proposals. Read source files only when they are relevant to the feature being discussed.

Ask 1-3 questions at a time, allowing for natural conversation and exploration. Use the following principles to guide your questioning and proposal of approaches:

- Group related questions together to minimize context switching and allow for deeper exploration of specific areas before moving on
- Make informed guesses based on repo context rather than asking endless questions — present what you infer and ask the user to confirm or correct
- Present structured clarifications with options and implications rather than open-ended questions (e.g., "I see two approaches: A does X (simpler, less flexible) or B does Y (more complex, extensible). Which fits better?")
- As understanding develops, propose alternative approaches with trade-offs — lead with your recommendation and reasoning
- Challenge complexity and follow best practices (YAGNI, DRY, orthogonality, etc.) — ask questions that surface unnecessary complexity or coupling
- Reference specific files and patterns you discovered during exploration

**Stop when you have:**

- Core problem and solution clearly understood
- Key architectural decisions identified, with alternatives considered
- An approach selected by the user
- Testing approach established
- Development approach established (e.g., TDD, vertical slice, etc.)

### 3. Design Summary

Synthesize the conversation into a design summary covering:

1. **Problem, purpose, and scope** — what problem this solves, what's IN scope and OUT of scope
2. **Key design decisions** — decisions made during exploration with rationale
3. **Alternatives considered** — approaches explored and why they were rejected
4. **Technical architecture** — components, files affected, dependencies
5. **Testing approach** — how to verify the implementation

These sections align with what `/write-plan` expects to extract from conversation. Present the full summary, then ask if any sections need revision. If so, revise the specific sections and re-present.

### 4. UI Feature Detection

Assess whether the feature involves UI/frontend work:

- Does the feature modify or create visual components?
- Are there layout, styling, or user interaction considerations?
- Would a visual mockup help verify understanding before planning?

If UI work detected, ask: "This feature involves UI work. Would an HTML mockup help verify the layout and component structure before we proceed to `/write-plan`?"

If user agrees, note that mockup should be created during `/write-plan`.

### 5. Approval Gate

Require explicit user confirmation of the design summary before suggesting `/write-plan`.

On approval: confirm the user should run `/write-plan [feature-name]`.

## Guidelines

- Make informed guesses over interrogation — use repo context to infer and confirm rather than ask from scratch
- Synthesize before validating — present the full design, then refine based on feedback
- Adapt depth to user preference — some users want detailed exploration, others want to move fast
- Challenge complexity — apply YAGNI, DRY, orthogonality throughout
- 1-3 questions at a time, natural conversation
