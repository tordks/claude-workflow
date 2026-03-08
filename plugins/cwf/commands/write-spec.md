---
description: Create spec and state from planning discussion
disable-model-invocation: true
argument-hint: [feature-name] [planning context]
---

# Spec Command

Formalize the planning discussion into structured documentation. This command is run AFTER iterating with Claude on the design (via `/explore`, plan mode, or conversation). The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the spec has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/write-spec {feature-name} [planning context]`

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

- `.cwf/{feature-name}/{feature-name}-spec.md`
- `.cwf/{feature-name}/{feature-name}-state.md`

**Overwrite guard:**

Before creating files, check if `.cwf/{feature-name}/` already exists. If it does:

- Inform the user that a spec already exists for this feature
- Suggest using `/amend {feature-name}` to update the existing spec
- STOP unless the user explicitly confirms they want to overwrite

## Instructions

### 1. Extract Planning Context

If skill `claude-workflow` is not loaded, load it using the Skill tool

Read the following if not already loaded:

- `references/spec.md`
- `references/state.md`
- `references/mockup.md`

**Context Extraction:**

Analyze the conversation to extract:

- Requirements and scope (IN/OUT)
- Design decisions with rationale (WHY)
- Alternatives considered and rejected
- Technical constraints and dependencies
- File and component structure
- Testing expectations (level, strategy, what to test)
- Quality tooling (linters, formatters, type checkers, complexity analyzers, dead code analyzers)

Review as much of the conversation as necessary to capture all planning context. Focus particularly on recent messages and any structured outputs (e.g., /explore design summary, input arguments to this command).


**Gap Check:**

If any of the following are unclear or missing from the conversation, use AskUserQuestion to clarify before creating documents:

- Testing expectations (level of testing, what types of tests)
- Development approach (when multiple strategies or technology choices seem equally valid)
- Scope boundaries (when IN/OUT is ambiguous)

**Complexity Assessment:**

Assess feature complexity to tailor document depth:

| Criteria | Simple | Medium | Complex |
|----------|--------|--------|---------|
| Files affected | 1-2 | 3-5 | 6+ |
| Components | 1 | 2-3 | 4+ |
| Tasks | <5 | 5-15 | 15+ |
| Dependencies | Minimal | Some cross-component | Cross-system |
| Spec depth | MUST only | MUST + SHOULD | MUST + SHOULD + MAY |

---

### 2. Create Planning Documents

Create `.cwf/{feature-name}/{feature-name}-spec.md`:

- Follow spec.md structure, tailoring depth to feature complexity
- Use extracted context from Section 1
- Use mermaid diagrams where helpful to illustrate architecture, component interactions, or workflows

Create `.cwf/{feature-name}/{feature-name}-state.md`:

- Follow state.md structure, tailoring depth to feature complexity
- Break into phases aligned with spec's Implementation Strategy
- Include checkpoints per SKILL.md guidance
- Stay faithful to discussion, use clear language

### 2.5 Mockup (UI Features)

Assess whether the feature involves UI/frontend work. If so, create or update a mockup when user explicitly requests one OR agent determines visual verification would be valuable.

**If a mockup already exists** (e.g., created during `/explore`):

- Review it against the finalized spec's Solution Design
- Update the mockup if the design has evolved; leave it as-is if it still matches
- Reference mockup inline in spec's Solution Design section

**If no mockup exists:**

- Create `.cwf/{feature-name}/{feature-name}-mockup.html` (single HTML file with inline CSS)
- Reference mockup inline in spec's Solution Design section

---

### 3. Self-Review

Launch a single subagent to review the spec and state for coherence. The subagent reads both documents and checks:

1. **File coverage** — every file marked [CREATE]/[MODIFY]/[REMOVE] in the spec has corresponding tasks in the state
2. **Strategy alignment** — state phases follow the spec's Implementation Strategy and Testing approach
3. **Scope match** — state tasks collectively deliver everything in the spec's Scope (nothing missing, nothing extra)
4. **Task IDs** — all tasks use `[PX.Y]` format with sequential numbering within each phase

If the subagent finds issues, fix them inline and move on.

---

### 4. Finalization

Confirm files exist and are valid, then present summary:

```text
Planning documents created!
- .cwf/{feature-name}/{feature-name}-spec.md
- .cwf/{feature-name}/{feature-name}-state.md
- {N} phases, {M} total tasks

Next: Run `/implement {feature-name}` to begin implementation.
```
