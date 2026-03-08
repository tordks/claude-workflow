# Amendment Reference

Safety rules for modifying CWF specs and state documents during implementation.

## Core Principle

**Completed work is immutable.** Tasks marked `[x]` represent implemented code and form a trusted implementation history. Changing completed work breaks trust in the state document as source of truth and creates confusion about what was actually built.

## Rules

When modifying incomplete tasks (`[ ]`), preserve the task name and ID — only update the description.

## Blocked Operations

Never perform these — reject and explain why:

- **Modify or remove completed tasks** — Code already built. Create new task/phase instead.
- **Add task to completed phase** — All tasks `[x]` means phase done. Create new phase instead.
- **Change completed task ID or name** — These are stable references. Changing breaks cross-references.
