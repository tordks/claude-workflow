---
description: Create plan and tasklist from planning discussion
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/write-plan {feature-name} [planning context]`

**Parsing:**
- First token: feature name
- Remaining tokens: optional planning guidance or focus areas
  - Example: `user-auth focus on OAuth2 and session management`

**Feature name requirements:**
- Format: kebab-case (lowercase with hyphens)
- Length: 1-3 words, concise and descriptive
- Characters: lowercase letters, numbers, hyphens only
- Examples: `query-command`, `user-auth`, `auth`, `export`
- Avoid: special characters, uppercase, underscores

**If no feature name provided:**
- Analyze conversation to suggest an appropriate feature name based on discussion
- Present suggestion: "Based on our discussion, I suggest the feature name: '{suggested-name}'"
- Ask user to confirm before creating files

**Feature name usage:**
`{feature-name}` is a placeholder that gets replaced with the extracted feature name throughout this command.

Example file paths:
- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`


## Instructions

### 1. Extract Planning Context

1. If skill `read-constitution` not loaded, load it
2. If skill `cfw-planning` not loaded, load it

Read the following if not already loaded:
- `references/plan-spec.md`
- `references/tasklist-spec.md`

Extract from recent conversation history (last 15-30 messages before this command):
- Requirements and scope (IN/OUT)
- Design decisions with rationale (WHY)
- Alternatives considered and rejected
- Technical constraints and dependencies
- File and component structure

Assess feature complexity (Simple/Medium/Complex) considering:
- Affected components and integration points
- Architectural impact
- Number of stakeholders/systems

This complexity assessment determines documentation depth:
- Simple: Focus on MUST requirements from specs
- Medium: Include MUST + SHOULD requirements
- Complex: Include MUST + SHOULD + MAY requirements

---

### 2. Create Planning Documents

Create `plans/{feature-name}-plan.md`:
- Follow plan-spec.md structure, tailoring depth to feature complexity
- Use extracted context from Section 1

Create `plans/{feature-name}-tasklist.md`:
- Follow tasklist-spec.md structure, tailoring depth to feature complexity
- Break into phases aligned with plan's Implementation Strategy
- Include checkpoints per SKILL.md guidance
- Stay faithful to discussion, use clear language

---

### 3. Validate Documents

**Validate plan**:
1. Validate `plans/{feature-name}-plan.md` against all requirements in plan-spec.md
2. Check each MUST/SHOULD requirement is satisfied
3. Revise and re-validate until all items pass

**Validate tasklist**:
1. Validate `plans/{feature-name}-tasklist.md` against all requirements in tasklist-spec.md
2. Check each MUST/SHOULD requirement is satisfied
3. Revise and re-validate until all items pass

**Validate coherence** between documents:
1. ✓ Each tasklist phase implements components mentioned in plan's Implementation Strategy section
2. ✓ Files marked [CREATE] or [MODIFY] in plan appear as tasks in tasklist (aim for >80%)
3. ✓ Testing types mentioned in plan (unit/integration/e2e) appear as test tasks in tasklist
4. ✓ Phase deliverables in tasklist match Implementation Strategy phase breakdown
5. ✓ Both documents use similar detail level (both use MUST-only OR both include SHOULD/MAY)

Revise either document if any coherence check fails, then re-validate.

---

### 4. Finalization

Confirm both files exist and are valid, then present summary:

```
Planning documents created successfully! ✅

Created:
- plans/{feature-name}-plan.md
- plans/{feature-name}-tasklist.md

Implementation Structure:
- {N} phases defined
- {M} total tasks

Next Steps:
Run `/implement-plan {feature-name}` to begin phase-by-phase implementation.
```

Done. Wait for user to run `/implement-plan {feature-name}`.
