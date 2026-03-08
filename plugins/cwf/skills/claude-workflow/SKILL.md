---
name: claude-workflow
description: >-
  CWF knowledge repository providing spec structure, state format, checkpoint
  definitions, amendment rules, and validation requirements. Load this skill when:
  (1) executing CWF commands like /write-spec, /implement, /amend,
  (2) answering questions about CWF workflow or spec/state format,
  (3) validating spec or state documents,
  (4) understanding phase structure or task conventions.
  This is KNOWLEDGE context, not an action - do NOT confuse with the /write-spec,
  /implement, /amend, or /explore commands which are user-invoked.
---

# Claude Workflow

Knowledge repository for Claude Workflow (CWF).

## Overview

CWF is a spec-driven development workflow using complementary documents that work together to guide feature implementation. All documents are stored in `.cwf/{feature-name}/`.

**Spec Document (`.cwf/{feature-name}/{feature-name}-spec.md`):**

- Captures architectural context and design rationale
- Documents WHY decisions were made and WHAT the solution is
- **Structure defined in `spec.md`**

**State Document (`.cwf/{feature-name}/{feature-name}-state.md`):**

- Provides step-by-step execution guidance
- Documents WHEN to do tasks and HOW to implement them
- **Structure defined in `state.md`**

**Mockup (`.cwf/{feature-name}/{feature-name}-mockup.html`) [Optional]:**

- Visual reference for UI/frontend features
- **Conventions defined in `mockup.md`**

**All documents follow the conformance requirements defined below.**

---

## Conventions

### Feature Naming

Feature names MUST:

- Use kebab-case (lowercase with hyphens)
- Be 1-3 words, concise and descriptive
- Contain only lowercase letters, numbers, and hyphens
- Start with a letter

Feature names MUST NOT contain uppercase, underscores, or start/end with hyphens.

**Validation pattern:** `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`

**Examples:** `query-command`, `user-auth`, `oauth2-flow`

### Directory Structure

CWF planning documents MUST be stored in `.cwf/{feature-name}/`:

```text
.cwf/
└── {feature-name}/
    ├── {feature-name}-spec.md       [REQUIRED]
    ├── {feature-name}-state.md      [REQUIRED]
    └── {feature-name}-mockup.html   [OPTIONAL]
```

The `.cwf/` directory is hidden to keep project root clean. Per-feature subdirectories contain related artifacts.

---

## Conformance and Tailoring

**All CWF planning documents (specs and states) use RFC 2119 keywords to define requirements.**

The specifications in `spec.md` and `state.md` use these keywords as described in RFC 2119.

- **MUST** / **REQUIRED** / **SHALL** - Mandatory requirements for all specs
- **SHOULD** / **RECOMMENDED** - Strongly recommended; include unless there's good reason not to
- **MAY** / **OPTIONAL** - Optional enhancements; include when they add value
- **MUST NOT** / **SHALL NOT** - Absolute prohibitions
- **SHOULD NOT** - Generally inadvisable; avoid unless there's good reason

The agent adjusts document depth naturally based on feature complexity. Simple features get lightweight specs; complex features get detailed ones.

---

## Checkpoints

Checkpoints are end-of-phase validation operations that provide quality control for AI-driven development.

**Checkpoint Types:**

- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality:** Linting, formatting, type checking (project-specific tools)
- **Code complexity:** Complexity analysis (project-specific thresholds)

Human review occurs after checkpoints complete, when "Phase X Complete" is signaled.

**Where checkpoints appear:**

- **Spec:** Checkpoint strategy explains WHY these checkpoints and WHAT tools
- **State:** Checkpoint checklist specifies WHEN to run and HOW to execute

**Key principle:** Checkpoints are validation operations performed after phase task completion but before moving to the next phase. They are distinct from functional tests, which validate feature behavior.

---

## CWF Workflow

The CWF planning workflow follows this command-driven flow:

```text
  /explore (optional) [Human runs]
         ↓
  Design Summary [In conversation]
         ↓
     /write-spec [Human runs]
         ↓
   Spec + State [Agent writes]
         ↓
   /implement [Human runs]
         ↓
  Phase 1 [Agent implements] → Checkpoints [Agent runs] → Review [Human] → ✓ → /clear [Human runs]
         ↓
 Phase 2 [Agent implements] → Checkpoints [Agent runs] → Review [Human] → ✓ → /clear [Human runs]
  [Changes?] → /amend [Human runs] ──┐
         ↓                                │
  Continue development [Agent] ←──────────┘
         ↓
  Feature Complete ✓ [Human confirms]
```

### Stage Breakdown

**1. `/explore` Command (Optional)**

Incrementally builds design summary in conversation with user approval

**2. `/write-spec` Command**

- Generates spec (WHY/WHAT) and state (WHEN/HOW) documents

**3. Phase-by-Phase Implementation**

Repeating cycle per phase:

- Human runs `/implement`, agent reads spec + state
- Agent works through tasks sequentially, marks complete, executes checkpoints
- Agent signals phase completion, stops for human review
- Human reviews, runs `/clear`, then `/implement` again for next phase

Conversation history is lost after `/clear`; only spec, state checkboxes, and committed code persist across cycles.

**4. `/amend` Command (When Needed)**

- Human runs `/amend` when requirements change during development
- Agent adds tasks to incomplete phases, creates new phases, updates spec sections
- Follows amendment safety rules

**5. Feature Completion**

- Agent completes all phases and signals completion
- Human reviews and confirms

## Quick Reference

| Need to understand... | Read This Reference | Contains |
|----------------------|---------------------|----------|
| **Spec document specification** | `references/spec.md` | Spec structure requirements with RFC 2119 keywords |
| **State document specification** | `references/state.md` | State structure requirements with RFC 2119 keywords |
| **Amendment rules and safety** | `references/amendment.md` | Rules for safely modifying specs and states |
| **Mockup conventions** | `references/mockup.md` | When and how to create HTML mockups |

---

**Skill loaded.** CWF planning concepts and patterns are now available.
