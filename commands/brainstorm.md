---
description: Quick feature exploration before creating plan
---

# Brainstorm Command

Guide conversational exploration of feature requirements and design before formalizing with /write-plan.

## Bootstrap

1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete, then proceed with instructions below.
4. Gain quick repository understanding:
   - Scan project structure (directories, modules, organization)
   - Identify architecture patterns (how things are currently built)
   - Note key dependencies and constraints (libraries, APIs, integrations)
   - Survey existing features (what's already implemented)

**Key reference from cfw-planning:**
- `plan-spec.md` - Understand what context is needed for plan documents

## Context

This command is run BEFORE /write-plan to quickly explore feature requirements and design through natural conversation. The agent first understands the repository context, then asks essential questions to uncover just enough context for /write-plan to create comprehensive planning documents.


## Arguments

**Input**: `$ARGUMENTS`

If arguments are provided, they contain context or initial direction for the brainstorming session. Use this context to inform your questions and exploration.

## Brainstorming Process

Ask questions to uncover just enough context for /write-plan. Adapt questions based on user responses. Stop when sufficient context exists.

### Essential Questions

Adapt these questions based on responses. Ask only what's needed to give /write-plan enough context.

**Approach:** Use targeted exploration during questioning. When asking about components, architecture, or approach, explore relevant code to provide informed suggestions and identify integration points.

**What does this feature do?**
- Understand the core functionality
- If unclear, help clarify with examples or options

**Why this approach?**
- Understand the reasoning or constraints
- If user hasn't considered alternatives, briefly suggest 1-2 options
- Apply YAGNI - challenge unnecessary complexity

**What components are involved?**
- Understand the architecture/structure
- What needs to be created vs modified
- How it integrates with existing code

**How should this be built?**
- Understand implementation strategy
- Incremental approach? Phases?
- What unknowns or risks exist?
- What to tackle first?

**How will it be tested?**
- Understand testing strategy
- Coverage expectations

**Any other important context?**
- Dependencies, constraints, risks
- Performance, security, compatibility requirements
- Anything else needed for /write-plan

### When to Stop

Stop asking questions when you have enough context for /write-plan to create:
- Clear problem statement and solution overview
- Basic architecture understanding
- Key design decisions and rationale
- Implementation strategy
- Testing approach

### Transition to /write-plan

When sufficient context is gathered:

```
This gives us enough to work with. Ready to run /write-plan?
```

If user says yes, confirm they should run `/write-plan [feature-name]`.

If user wants to explore more, continue conversation.

## Guidelines

- **One question at a time:** Don't overwhelm with multiple questions
- **Natural conversation:** Adapt to user's style, not a rigid checklist
- **YAGNI enforcement:** Challenge complexity, prefer simple solutions
- **Software best practices:** Apply DRY, YAGNI, orthogonality principles
- **Flexibility:** Let user guide depth - some need quick exploration, others want thorough discussion
- **No documentation:** No formal brainstorm document needed - conversation provides context for /write-plan
