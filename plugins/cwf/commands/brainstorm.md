---
description: Quick feature exploration before creating plan
disable-model-invocation: true
argument-hint: [initial context]
---

# Brainstorm Command

Guide conversational exploration of feature requirements and design before formalizing with /write-plan.

## Context

This command is run BEFORE writing planning documents to quickly explore feature requirements and design through natural conversation. The agent first understands the repository context, then asks essential questions to uncover just enough context to create comprehensive planning documents.

## Arguments

**Input**: `$ARGUMENTS`

If arguments are provided, they contain context or initial direction for the brainstorming session. Use this context to inform your questions and exploration.

## Brainstorm workflow

If skill `claude-workflow` is not loaded, load it using the Skill tool

Read the following if not already loaded:

- `references/plan-spec.md`

**Understand repository context before asking questions:**

Before diving into questions, actively explore the codebase to understand what exists and how it's structured. This context ensures questions are relevant and informed.

**Exploration approach:**

1. Read CLAUDE.md if present for repository overview and navigation guidance
2. Examine project structure using appropriate tools (glob patterns, directory listings)
3. Search for similar or related features to understand existing patterns
4. Identify testing approach (test files, frameworks used)
5. Note architecture patterns and conventions from actual code

**What to understand:**

- Project organization (monorepo vs single package, directory structure)
- Existing implementations similar to planned feature
- Testing conventions (where tests live, what frameworks are used, how detailed)
- Key dependencies and technologies in use
- Coding patterns and architectural decisions evident in code

Once you have sufficient repository context, ask questions one at a time to uncover additional context needed for /write-plan. Adapt questions based on responses. Reference specific files and patterns you discovered during exploration.

**Essential questions** (adapt as needed):

- What does this feature do? (core functionality)
- Why this approach? (reasoning, alternatives, apply YAGNI)
- What components involved? (create vs modify, integration)
- How should it be built? (strategy, phases, risks, priorities)
- How should it be tested? (strategy, coverage)
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
