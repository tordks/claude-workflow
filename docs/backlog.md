# CWF Backlog

## Feature-Based Directory Organization

Organize plans in feature-specific subdirectories (`plans/feature-name/`) instead of flat `plans/` directory. This opens up for opens for adding complementary documents without increasing clutter.

 Complementary files could be:
- Architecture diagrams
- Draft UI/wireframe mockups
- API specifications
- Data model schemas

---

## Pre-defined Implementation Strategies

Introduce recognized implementation patterns (like Tracer Bullets) that agents can apply during `/write-plan`. Tracer Bullets creates minimal end-to-end working examples before full layer implementations, enabling early testing and reducing integration risk.

---

## Amendment Enhancements

Add changelog section to amended plans tracking what changed, when, and why. Amended plans currently lack historical record, making it difficult to understand requirement evolution. Use strikethrough formatting for replaced content to maintain visible history.

---

## Constitution File Reorganization

Move plugin's default constitution files to plugin-internal location (e.g., `.constitution-examples/`), reserving `.constitution/` exclusively for project-specific overrides. Currently `.constitution/` in plugin mixes CWF defaults with examples, creating confusion between plugin-shipped standards and project conventions.

---

## Phase Checkpoint Hooks

Implement CWF-specific event hooks (cwf:pre-phase, cwf:post-phase, cwf:pre-checkpoint, cwf:post-checkpoint) integrated with Claude Code's hook system. Automate quality checks, linting, and complexity analysis at phase boundaries instead of relying on agent. This will also potentially save token usage. 

---

## Code Quality Analysis Skill

Dedicated skills integrating Ruff (linting) and Radon (complexity/maintainability metrics) for systematic code quality analysis.

---

## PM-Subagent Coordination Mode

PM agent orchestrates CWF workflow by delegating task/phase implementation to subagents, enabling parallel execution while maintaining plan adherence. Requires mechanism to identify parallel-eligible tasks/phases (either during plan generation or post-plan analysis). Preserves current workflow by reusing skills in both commands and subagents.

---

## Constitution Frontmatter and Selective Loading

Add YAML frontmatter with tags to constitution files for context-based selective loading. Loading all constitution files wastes tokens on irrelevant standards (e.g., Python conventions during planning). Commands load only relevant files based on context.

Strongly consider replacig constitution reading with skill loading, that already is loaded dynamically.

Example frontmatter:
```yaml
---
tags: [planning, architecture]
description: Architectural design principles
---
```

---

## Beads Integration for Task Management

Explore integrating Beads (git-backed graph issue tracker) to replace markdown tasklists with queryable task graphs. Markdown tasklists are "write-only memory" for agents - dependencies exist only in prose, making it hard to query for ready work or dynamically file discovered issues during implementation. Beads provides graph-based dependencies, ready-work detection (`bd ready --json`), and dynamic task discovery where agents can file new issues mid-implementation.

Beads does have a concept of Epic, Story, Feature and Task, which could represent both the plan and tasklist.

**Potential integration approaches:**
1. Beads replaces tasklist while plan.md remains living document with phase context. One Feature, Phase->Epic, Task->Task
2. plan.md initializes Beads then gets archived with all context migrated to Beads. Uncertain how well the plan document can be represented.


