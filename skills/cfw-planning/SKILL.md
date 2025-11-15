---
name: cfw-planning
description: Load for any CWF planning task including: explaining the workflow, answering planning questions, creating plans, amending plans, and implementing features. Contains conventions, phase structure, task formats, validation rules, and templates.
---

# CFW Planning

Knowledge repository for Claude Workflow (CWF).

## Overview

CWF is a plan-driven development workflow using two complementary documents that work together to guide feature implementation:

**Plan Document (`{feature-name}-plan.md`):**
- Captures architectural context and design rationale
- Documents WHY decisions were made and WHAT the solution is
- **Structure defined in `plan-spec.md`**

**Tasklist Document (`{feature-name}-tasklist.md`):**
- Provides step-by-step execution guidance
- Documents WHEN to do tasks and HOW to implement them
- **Structure defined in `tasklist-spec.md`**

**Both documents follow the conformance requirements defined below.**

---

## Conformance Requirements

**All CWF planning documents (plans and tasklists) use these conformance definitions.**

The specifications in `plan-spec.md` and `tasklist-spec.md` use RFC 2119 keywords to define requirements:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

### Conformance Levels

CWF specifications define three conformance levels:

| Level | Requirements | Suitable For |
|-------|--------------|--------------|
| **Level 1 (Minimal)** | MUST requirements only | Simple features, bug fixes, small utilities |
| **Level 2 (Standard)** | MUST + SHOULD requirements | Most features, new components, medium complexity |
| **Level 3 (Comprehensive)** | MUST + SHOULD + MAY requirements | Complex features, major systems, architectural changes |

### Selecting the Right Level

- Simple features (bug fixes, utilities) → Level 1
- Medium features (components, modules) → Level 2
- Complex features (systems, frameworks) → Level 3

### How Conformance Applies

**For Plan Documents** (see `plan-spec.md` for details):
- **Level 1**: Core sections present with minimal detail
- **Level 2**: All sections with adequate design decision rationale
- **Level 3**: Comprehensive sections with extensive documentation

**For Tasklist Documents** (see `tasklist-spec.md` for details):
- **Level 1**: Basic task structure and phase organization
- **Level 2**: Detailed tasks with proper granularity and ordering
- **Level 3**: Comprehensive tasks with extensive checkpoints

**Important:** Both plan and tasklist for a feature SHOULD use the same conformance level

---

## Checkpoints

Checkpoints are end-of-phase validation operations that provide quality control for AI-driven development.

**Purpose:**
- Validate code quality independent of functional testing
- Ensure AI-generated code meets project standards
- Catch issues early before accumulating technical debt

**Checkpoint Types:**
- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality:** Linting, formatting, type checking (project-specific tools)
- **Code complexity:** Complexity analysis (project-specific thresholds)

Human review occurs after checkpoints complete, when "Phase X Complete" is signaled.

**Where checkpoints appear:**
- **Plan:** Checkpoint strategy explains WHY these checkpoints and WHAT tools
- **Tasklist:** Checkpoint checklist specifies WHEN to run and HOW to execute

**Key principle:** Checkpoints are validation operations performed after phase task completion but before moving to the next phase. They are distinct from functional tests, which validate feature behavior.

---

## CWF Workflow

The CWF planning workflow follows this command-driven flow:

```
  /brainstorm (optional) [Human runs]
         ↓
  Design Summary [Agent writes]
         ↓
     /write-plan [Human runs]
         ↓
   Plan + Tasklist [Agent writes]
         ↓
   /implement-plan [Human runs]
         ↓
  Phase 1 [Agent implements] → Checkpoints [Agent runs] → Review [Human] → ✓ → /clear [Human runs]
         ↓
 Phase 2 [Agent implements] → Checkpoints [Agent runs] → Review [Human] → ✓ → /clear [Human runs]
  [Changes?] → /amend-plan [Human runs] ──┐
         ↓                                │
  Continue development [Agent] ←──────────┘
         ↓
  Feature Complete ✓ [Human confirms]
```

### Stage Breakdown

**1. `/brainstorm` Command (Optional)**
- **Human:** Runs `/brainstorm` command (optional step for structured exploration)
- **Agent:**
  - Systematically extracts requirements through guided questions
  - Explores 2-3 alternative approaches with trade-offs
  - Incrementally builds design with validation checkpoints
  - Produces design summary document in `docs/brainstorms/`
- **Outcome:** Complete design context ready for `/write-plan`
- **Note:** Can be skipped in favor of informal planning discussion or written specification

**2. `/write-plan` Command**
- **Human:** Runs `/write-plan` command
- **Agent:** Generates two documents:
  - Plan: Architectural context and WHY/WHAT decisions
  - Tasklist: Step-by-step HOW/WHEN execution guidance
  - Validates structure and consistency between documents

**3. Phase-by-Phase Implementation**

The implementation follows this repeating cycle:

- **Human:** Runs `/implement-plan` command
- **Agent:**
  - Reads plan for architectural understanding
  - Checks tasklist to identify completed tasks and current phase
  - Works through tasks for current phase sequentially
  - Marks tasks complete as work progresses
  - Executes checkpoints (code quality, complexity checks, etc)
  - Signals phase completion for human review at phase boundary
- **Human:**
  - Reviews phase results when agent signals completion
  - Runs `/clear` to start fresh session for next phase
  - **Repeats cycle:** Runs `/implement-plan` again for next phase

**Note:** Conversation history is lost after `/clear`; only plan, tasklist checkboxes, and committed code persist across cycles.

**4. `/amend-plan` Command (When Needed)**
- **Human:** Discusses amendment and runs `/amend-plan` when requirements change during development
- **Agent:**
  - Adds tasks to incomplete phases
  - Creates new phases for additional work
  - Updates plan sections with new context
  - Follows amendment safety rules
- **Agent:** Continues development with amended plan

**5. Feature Completion**
- **Agent:** Completes all phases and signals completion
- **Human:** Reviews and confirms feature is complete (✓)

## Quick Reference

| Need to understand... | Read This Reference | Contains |
|----------------------|---------------------|----------|
| **Plan document specification** | `references/plan-spec.md` | Plan structure requirements (uses conformance levels above) |
| **Tasklist document specification** | `references/tasklist-spec.md` | Tasklist structure requirements (uses conformance levels above) |
| **Amendment rules and safety** | `references/amendment.md` | Rules for safely modifying plans and tasklists |
| **Argument parsing for commands** | `references/parsing-arguments.md` | Command argument parsing logic and discovery patterns |
| **Feature naming and file structure** | `references/conventions.md` | Feature naming and file structure standards |


---

**Skill loaded.** CWF planning concepts and patterns are now available.
