# Argument Parsing Reference

Guide for parsing `$ARGUMENTS` in CWF planning commands (write-plan, amend-plan, implement-plan).

## Overview

All three planning commands accept arguments in the format:
```
/command-name {feature-name} [additional context]
```

This reference provides the standard parsing logic used across all commands.

---

## Parsing Logic

### Step 1: Split Arguments and store feature name

Separate `$ARGUMENTS` into two parts:
1. **First token** - The feature name
2. **Remaining tokens** - Additional context or instructions

**Example:**
- Input: `query-command implement phase 1 and 2`
- feature name: `query-command`
- Remaining: `implement phase 1 and 2`

Store feature name as: `{feature-name}` variable for use throughout the command

---

### Step 2: Handle Additional Context

Everything after the feature name is command-specific context:

**For write-plan:**
- Additional planning guidance or focus areas
- Example: "focus on OAuth2 and JWT"

**For amend-plan:**
- Amendment instructions or changes to make
- Example: "Add caching layer to phase 3"

**For implement-plan:**
- Implementation scope or behavior guidance
- Example: "implement phase 1 and 2, then stop"

---

## Discovery Pattern (No Feature Name Provided)

When `$ARGUMENTS` is empty or doesn't contain a feature name:

### Discovery Command

```bash
ls *-plan.md | sed 's|.*/||; s/-plan\.md$//'
```

This command:
1. Lists all files matching `*-plan.md` in plans/ directory
2. Removes path prefix and `-plan.md` suffix
3. Outputs just the feature names

**Example output:**
```
query-command
user-auth
data-export
```

### Command-Specific Behavior

**write-plan (no discovery):**
- Does NOT list existing plans
- Instead: SUGGEST a feature name based on conversation
- Reason: Creating NEW plans, not selecting existing ones

**amend-plan (with discovery):**
- Lists existing plans
- If only 1 found: use automatically and inform user
- If multiple found: present list, STOP, ask user to select

**implement-plan (with discovery):**
- Lists existing plans
- If only 1 found: use automatically and inform user
- If multiple found: present list with optional progress status, STOP, ask user to select

---

## User Interaction Patterns

### When Multiple Plans Found (amend/implement)

Present list using AskUserQuestion tool:

```markdown
I found multiple plans in the plans/ directory:
1. query-command
2. user-auth
3. data-export

Which plan would you like to {amend|implement}?
```

### When Suggesting Feature Name (write)

```markdown
Based on our conversation about adding document search functionality, I suggest
the feature name: "query-command"

This will create:
- plans/query-command-plan.md
- plans/query-command-tasklist.md

Should I proceed with "query-command" as the feature name?
```

---

## Summary

**Parsing steps:**
1. Split `$ARGUMENTS` into first token + remaining tokens
2. Extract and normalize feature name from first token
3. Validate feature name format (kebab-case, 2-3 words)
4. Store remaining tokens as command-specific context
5. If no feature name: apply command-specific discovery/suggestion behavior