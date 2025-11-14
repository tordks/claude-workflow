---
description: Create plan and tasklist from planning discussion
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Bootstrap

1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete, then proceed with instructions below.

**Key references from cfw-planning:**
- `conventions.md` - Feature name format validation
- `plan-spec.md` - Plan document specification with structure and validation requirements
- `tasklist-spec.md` - Tasklist document specification with structure and validation requirements

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

Parse input arguments using the standard parsing pattern from the cfw-planning skill's `parsing-arguments.md` reference.


## Instructions

> **CRITICAL Document Structure Requirements:**
>
> Both plan and tasklist documents MUST include:
> 1. **YAML frontmatter** at the very start with required fields (feature, plan_file, tasklist_file, dates)
> 2. **Usage header** as blockquote after the title explaining how to use the document
>
> See plan-spec.md and tasklist-spec.md "Document Header Structure" sections for exact templates.

### 1. Analyze conversation history and create plan and tasklist documents

Review the conversation history from plan mode and create two documents in the `plans/` directory.

The plan-spec.md and tasklist-spec.md references provide complete structure requirements for both documents. All plans and tasklists MUST follow the same structural requirements defined in the specs.

**Assessing Feature Complexity:**

As you analyze the planning discussion, assess the feature's scope and complexity:
- **Simple features** (bug fixes, single-file changes, small utilities): Brief sections in plan; focused phase breakdown
- **Medium features** (new components, API endpoints, moderate refactoring): Moderate detail in all plan sections; clear phase progression
- **Complex features** (architectural changes, multi-component systems): Comprehensive plan detail with subsections; detailed phase breakdown

Apply consistent detail level across both plan and tasklist. Let the feature's actual scope (components, files, integration points) guide documentation depth.

Write the planning documents following the spec requirements.

**Requirements:**

- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Make sure completing each phase leaves the codebase in a stable state
- Use clear, concise language
- Apply documentation detail appropriate to feature complexity

### 2. Per document Validation

First ensure both documents have required headers (YAML frontmatter and usage header), then validate the written plan and tasklist against plan-spec.md and tasklist-spec.md validation requirements.

### 3. Cross-Document Coherence Validation

Validate the written plan and tasklist for coherency.

**Quick coherence checks:**
1. **Phases match plan** - Each tasklist phase implements components/features described in plan
2. **Files align** - Files in plan's file tree (`[CREATE]`/`[MODIFY]`) appear in tasklist tasks
3. **Tests covered** - Testing approach in plan matches test tasks in tasklist
4. **Deliverables align** - Phase deliverables match plan's Implementation Strategy phase breakdown
5. **Detail consistency** - Both documents use similar documentation depth (avoid over-detailed plan with sparse tasklist or vice versa)

If misalignment found, revise the incoherent document to align before finalizing.
