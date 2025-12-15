---
description: Quick feature exploration before creating plan
---

# Brainstorm Command

Guide conversational exploration of feature requirements and design before formalizing with /write-plan.

## Context

This command is run BEFORE writing planning documents to quickly explore feature requirements and design through natural conversation. The agent first understands the repository context, then asks essential questions to uncover just enough context to create comprehensive planning documents.

## Arguments

**Input**: `$ARGUMENTS`

If arguments are provided, they contain context or initial direction for the brainstorming session. Use this context to inform your questions and exploration.

## Brainstorm workflow

If skill `claude-workflow` is not loaded, load it

Read the following if not already loaded:

- `references/plan-spec.md`

**Gain quick repository understanding:**

- Scan project structure (directories, modules, organization)
- Identify architecture patterns (how things are currently built)
- Note key dependencies and constraints (libraries, APIs, integrations)
- Survey existing features (what's already implemented)

Ask questions one at a time to uncover context for /write-plan. Adapt based on responses. Explore relevant code when discussing components/architecture.

**Essential questions** (adapt as needed):

- What does this feature do? (core functionality)
- Why this approach? (reasoning, alternatives, apply YAGNI)
- What components involved? (create vs modify, integration)
- How should it be built? (strategy, phases, risks, priorities)
- How tested? (strategy, coverage)
- Other context? (dependencies, constraints, performance, security)

**Stop when you have:**

- Clear problem/solution
- Architecture understanding
- Key design decisions and rationale
- Implementation strategy
- Testing approach

**Transition:** When sufficient context gathered, ask: "Ready to run /write-plan?" If yes, confirm they should run `/write-plan [feature-name]`.

**Guidelines:**

- 1-3 question at a time, natural conversation
- Challenge complexity (YAGNI, DRY, orthogonality)
- Adapt to user's preferred depth
