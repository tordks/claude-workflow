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

The plan-spec.md and tasklist-spec.md references provide complete structure requirements for both documents. See these specifications for detailed templates, examples, and validation criteria.

Write the planning documents.

**Requirements:**

- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Make sure completing each phase leaves the codebase in a stable state
- Use clear, concise language

### 2. Per document Validation

First ensure both documents have required headers (YAML frontmatter and usage header), then validate the written plan and tasklist against plan-spec.md and tasklist-spec.md validation requirements.

### 3. Cross-Document Coherence Validation

Validate the written plan and tasklist for coherency.

**Quick coherence checks:**
1. **Phases match plan** - Each tasklist phase implements components/features described in plan
2. **Files align** - Files in plan's file tree (`[CREATE]`/`[MODIFY]`) appear in tasklist tasks
3. **Tests covered** - Testing approach in plan matches test tasks in tasklist
4. **Deliverables align** - Phase deliverables match plan's Implementation Strategy phase breakdown

If misalignment found, revise the incoherent document to align before finalizing.
