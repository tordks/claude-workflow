# CWF Design Principles

## Single Source of Truth

Each piece of knowledge lives in exactly one place.

**Application:**

- Domain knowledge → skills
- Workflow logic → skills
- Workflow execution → commands

**Example:** Task structure rules live in `tasklist-spec.md` only. All commands reference this source. Update once → all commands benefit.

## Orthogonality

Design components so changes to one don't require changes to others.

**Application:**

- Change skills → commands automatically benefit
- Change commands → skills remain unchanged
- Add new skills → no changes to existing commands

**Example:** Update `tasklist-spec` to support new task format → commands automatically use new format without code changes.

## Explicit Over Implicit

Make relationships and dependencies clear.

**Application:**

- Commands explicitly invoke skills by name
- Skills explicitly reference resources
- Data flow clearly visible

**Example:** Commands use bootstrap pattern: "1. Load skill, 2. Read plan/tasklist, 3. Execute tasks"
