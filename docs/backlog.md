# CWF Backlog

## Optimize implement-plan Context Loading

**What:** Reduce context consumption by making implement-plan infer structure from planning documents rather than loading full cfw-planning skill

**Why Needed:** Currently implement-plan loads extensive skill documentation. Plans should be as self-contained as possible with needed context embedded.

**Features:**
- Write-plan embeds essential structure info into plan document
- Implement-plan reads structure from plan itself
- Reduces token usage during implementation
- Makes plans more portable and self-documenting

---

## Feature-Based Directory Organization

**What:** Organize plan documents in feature-specific subdirectories instead of flat `plans/` directory

**Why Needed:** Plans directory becomes cluttered as project grows, making navigation difficult

**Features:**
- Create `plans/feature-name/` subdirectories
- Store plan.md and tasklist.md in feature directory
- Group related artifacts (diagrams, specs) with feature
- Maintain cleaner project structure

---

## Checkpoint Validation System

**What:** Automated validation and quality checks at phase boundaries

**Why Needed:** Ensure code quality, completeness, and architectural integrity before proceeding to next phase

**Features:**
- Post-phase validation: verify all tasks complete
- Code quality checks: linting, formatting
- Complexity analysis: detect refactoring needs using Radon
- Dynamic checkpoint adjustment based on complexity metrics

- Split complex phases, combine simple ones
- Balance implementation effort


---

## Tracer Bullets Implementation Strategy

**What:** Optional workflow mode that creates minimal working examples before full implementation

**Why Needed:** Full layer/feature implementations in Phase 1 make it hard for users to test and understand incremental progress

**Features:**
- Create end-to-end minimal working example first
- Build incrementally on working foundation
- Enable early testing and feedback
- Reduce integration risk

---


## Amendment Enhancements

**What:** Changelog tracking and strikethrough formatting for amended content

**Why Needed:** Maintain historical record of changes and why they were made

**Features:**
- Changelog section in amended documents
- Strikethrough for replaced content
- Amendment timestamps
- Rationale documentation

---

## Plan Settings / Front Matter

**What:** YAML front matter in plan documents for configuration

**Why Needed:** Allow plans to specify preferences like testing framework, language version, architectural style

**Example:**
```yaml
---
testing_framework: pytest
python_version: "3.11"
architecture: layered
implementation-strategy: tracer bullet
---
```

---

## Constitution File Reorganization

**What:** Move constitution files from `.constitution/` to plugin-specific location

**Why Needed:** Separate project-specific coding standards from CWF plugin defaults

**Features:**
- Move plugin constitution to plugin directory
- Support project-local constitution overrides
- Clear separation of plugin vs project standards
- Enable per-project coding conventions


---


## Ambiguity Detection System

**What:** Automated detection of ambiguous requirements in planning discussions

**Why Needed:** Help identify unclear specifications before implementation begins

**Features:**
- Scan conversation for vague terms
- Flag missing technical details
- Prompt for clarification
- Suggest specific questions


---

## Hooks System for Event-Driven Automation

**What:** Event hooks for automated actions during workflow

**Why Needed:** Automate repetitive tasks and enforce policies

**Features:**
- Pre-plan hooks (validate naming, check dependencies)
- Post-plan hooks (create issues, notify team)
- Pre-phase hooks (setup environment, run checks)
- Post-phase hooks (run tests, commit code)


---

## Refactor Skill with Ruff/Radon

**What:** Dedicated skill for code quality analysis and refactoring guidance

**Why Needed:** Systematic approach to improving existing code

**Features:**
- Integrate Ruff for linting
- Integrate Radon for complexity analysis
- Provide refactoring recommendations
- Generate refactoring tasks


---

## PM-Subagent Coordination Mode

**What:** Project manager agent that coordinates multiple implementation agents

**Why Needed:** Handle complex features requiring parallel work streams

**Features:**
- Coordinate multiple agents
- Manage dependencies
- Track overall progress
- Resolve conflicts


---

## Split cfw-planning into Separate Plugin

**What:** Extract cfw-planning skill into its own independent plugin

**Why Needed:** Better skill information hit-rate and independent versioning

**Features:**
- Separate cfw-planning plugin
- Independent updates and releases
- Improved discoverability
- Reduced main plugin complexity


## Constitution Frontmatter and Selective Loading

**What:** Add YAML frontmatter to constitution files for metadata and context-based selective loading

**Why Needed:** Not all constitution files are relevant for every command. Loading all files wastes tokens on irrelevant standards.

**Features:**
- Add frontmatter to each constitution file with description and tags
- Create script/subagent to select relevant files based on context
- `/write-plan`, `/amend-plan` and `/implement-plan` loads only dev and planning-related constitution files
- `/read-constitution` accepts arguments to specify which files to load
- Optional: Constitution-reader subagent with read-constitution skill for retrieval without bloating context

**Example frontmatter:**
```yaml
---
tags: [planning, architecture]
description: Architectural design principles
---
```

## Beads Integration for Task Management

**What:** Explore integrating Beads (git-backed graph issue tracker) with CWF for enhanced task tracking and dynamic discovery

**IMPORTANT LIMITATION:** Beads is an issue tracker for tasks, NOT a planning system. It cannot replace plan.md (architectural rationale, design decisions, scope definition) - only tasklist.md (task tracking). plan.md remains essential for capturing the "WHY" behind implementation choices.

**Why Needed:** Markdown TODOs are "write-only memory" for agents. Dependencies exist only in prose, making it impossible to query for ready work. Agents can't dynamically track discovered bugs/TODOs during implementation without breaking out of the tasklist structure.

**What Beads Provides (Task-Level Only):**
- Git-backed database (`.beads/issues.jsonl`) with local SQLite cache for fast queries
- Graph-based dependencies (blocks, related, parent-child, discovered-from)
- Agent-optimized JSON output and hash-based IDs
- Ready-work detection (`bd ready --json` finds tasks with no open blockers)
- Dynamic task discovery: Agents file new issues mid-implementation, linking to parent work
- Multi-session memory without re-reading prose
- Audit trail: Every change logged with timestamps and authorship
- Hierarchical task structure: Parent epics with child tasks (bd-a3f8.1, bd-a3f8.2)

**What Beads DOESN'T Provide Natively:**
- No human-friendly planning document format
- Architectural rationale must be populated from plan.md into issue descriptions
- Design context stored in Feature/Epic descriptions, not separate document
- In Option 2: plan.md provides the initial "WHY", which gets loaded into Beads descriptions

**Integration Options:**

**Option 1: Beads Replaces Tasklist**
- **plan.md**: Architectural rationale, defines phases and their context (Same as now)
- **Beads**: Phases as epics, tasks as children of epics
- **tasklist.md**: Optional - can generate reviewable view from Beads if needed
- Agent works from Beads (`bd ready --json`), user reviews plan.md + generated tasklist
- Workflow: `/write-plan` creates plan.md + Beads structure and tasklist generation

**Option 2: Full Beads Integration**
- **plan.md**: Initialization document with architectural rationale and phase structure
  - Defines phases with context/goals (like current CWF plan.md)
  - Does NOT define detailed tasks (added during beads initialization)
  - Used once to initialize Beads, then archived
- **Beads**: Plan (feature) → Phases (epics) → Tasks (Task)
- **tasklist.md**: Generated view from Beads for human review if needed
- Workflow: `/write-plan` creates plan.md → user review plan → initializes Beads → plan.md archived 

**Key Difference:** Option 1 keeps phase context in plan.md as a living document. Option 2 uses plan.md to initialize beads and then the plan is not used again.

**Type Conventions:**

- **Feature** → CWF feature (Option 2 only - top-level parent for phases)
- **Epic** → CWF Phase (child of feature in Option 2, standalone in Option 1)
- **Task** → Individual tasklist items (child of phase epic)
- **Bug** → Discovered issues (filed with `--discovered-from`)
- **Chore** → Setup, cleanup, documentation tasks

**Open Questions:**
- How to handle amendments with beads and make them transparent?
- How well can we represent a plan in beads Features and Epics?

