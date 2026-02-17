---
description: Create plan and tasklist from planning discussion
disable-model-invocation: true
argument-hint: [feature-name] [planning context]
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation. This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

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

- `.cwf/{feature-name}/{feature-name}-plan.md`
- `.cwf/{feature-name}/{feature-name}-tasklist.md`

## Instructions

### 1. Extract Planning Context

If skill `claude-workflow` is not loaded, load it using the Skill tool

Read the following if not already loaded:

- `references/plan-spec.md`
- `references/tasklist-spec.md`
- `references/mockup.md`

**Context Extraction:**

Analyze the conversation to extract:

- Requirements and scope (IN/OUT)
- Design decisions with rationale (WHY)
- Alternatives considered and rejected
- Technical constraints and dependencies
- File and component structure
- Quality tooling (linters, formatters, type checkers, complexity analyzers, dead code analyzers)

Review as much of the conversation as necessary to capture all planning context. Focus particularly on recent messages and any structured outputs (e.g., /explore design summary, input arguments to this command).

**Complexity Assessment:**

Assess feature complexity (Simple/Medium/Complex) using these criteria:

**Simple:**

- 1-2 files affected
- Single component or module
- <5 tasks total
- Minimal external dependencies
- Focus on MUST requirements from specs

**Medium:**

- 3-5 files affected
- 2-3 components involved
- 5-15 tasks total
- Some cross-component integration
- Include MUST + SHOULD requirements

**Complex:**

- 6+ files affected
- 4+ components involved
- 15+ tasks total
- Significant architectural changes or cross-system integration
- Include MUST + SHOULD + MAY requirements

---

### 2. Create Planning Documents

Create `.cwf/{feature-name}/{feature-name}-plan.md`:

- Follow plan-spec.md structure, tailoring depth to feature complexity
- Use extracted context from Section 1
- Use mermaid diagrams where helpful to illustrate architecture, component interactions, or workflows

Create `.cwf/{feature-name}/{feature-name}-tasklist.md`:

- Follow tasklist-spec.md structure, tailoring depth to feature complexity
- Break into phases aligned with plan's Implementation Strategy
- Include checkpoints per SKILL.md guidance
- Stay faithful to discussion, use clear language

### 2.5 Mockup (UI Features)

Assess whether the feature involves UI/frontend work. If so, create or update a mockup when user explicitly requests one OR agent determines visual verification would be valuable.

**If a mockup already exists** (e.g., created during `/explore`):

- Review it against the finalized plan's Solution Design
- Update the mockup if the design has evolved; leave it as-is if it still matches
- Reference mockup inline in plan's Solution Design section

**If no mockup exists:**

- Create `.cwf/{feature-name}/{feature-name}-mockup.html` (single HTML file with inline CSS)
- Reference mockup inline in plan's Solution Design section

---

### 3. Self-Review

Launch a single subagent to review the plan and tasklist for coherence. The subagent reads both documents and checks:

1. **File coverage** — every file marked [CREATE]/[MODIFY]/[REMOVE] in the plan has corresponding tasks in the tasklist
2. **Strategy alignment** — tasklist phases follow the plan's Implementation Strategy and Testing approach
3. **Scope match** — tasklist tasks collectively deliver everything in the plan's Scope (nothing missing, nothing extra)

If the subagent finds issues, fix them inline and move on.

---

### 4. Finalization

Confirm files exist and are valid, then present summary:

```text
Planning documents created successfully! ✅

Created:
- .cwf/{feature-name}/{feature-name}-plan.md
- .cwf/{feature-name}/{feature-name}-tasklist.md
- .cwf/{feature-name}/{feature-name}-mockup.html (if UI feature)

Implementation Structure:
- {N} phases defined
- {M} total tasks

Next Steps:
Run `/implement-plan {feature-name}` to begin phase-by-phase implementation.
```

Done. Wait for user to run `/implement-plan {feature-name}`.
