# Concepts

## Skills, Commands, and Agents

Claude Code uses three core concepts that work together to extend functionality:

```
┌─────────────────────────────────────────────┐
│              Skills                         │
│  Specialized instructions provided to       │
│  Claude in certain circumstances            │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│            Commands                         │
│  User-facing entry points invoked manually  │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│           Sub-agents                        │
│  Specialized personas that execute          │
│  work in fresh contexts                     │
└─────────────────────────────────────────────┘
```

### Skills

**What:** Specialized instructions you may want to provide to Claude in certain circumstances, but may not always be relevant.

**Purpose:** Store domain-specific knowledge, conventions, or guidelines that enhance Claude's capabilities for particular tasks.

**When to Use:**
- You want to sometimes provide instructions with a relevant skillset
- The knowledge is not universally applicable to all tasks
- You need reusable expertise across multiple commands, sub-agents or sessions

**Examples:**
- Code review guidelines for a specific framework
- Domain-specific terminology and patterns
- Testing conventions for your project
- Language-specific best practices
- How to use tools or technologies
- Reusable scripts

### Slash Commands

**What:** Specialized commands you want to invoke manually

**Purpose:** User-facing entry points that orchestrate workflows or perform predefined operations.

**When to Use:**
- There are specific operations you know you'll want to invoke at certain points
- You want explicit control over when operations execute
- You need to coordinate multiple steps or tools
- You write the same prompt multiple times and want a shorthand for executing it

**Examples:**
- Generate documentation from code
- Run quality checks and formatting
- Create structured plans or specifications
- Execute multi-step workflows

### Sub-agents

**What:** Specialized personas you offload specific work to in fresh contexts backed by full agent instances.

**Purpose:** Keep your main context clean while getting specialized expertise from dedicated agent instances.

**When to Use:**
- You want to prevent context pollution in your main conversation
- You need specialized perspectives (code reviewer, skeptic, testing specialist)
- The task benefits from a fresh context without prior assumptions
- You want concurrent execution of independent tasks

**Common Sub-agent Types:**
- Code reviewers (security, performance, quality)
- Testing specialists (test design, coverage analysis)
- Language/framework specialists (domain expertise)
- Architects (design decisions, trade-off analysis)
- Skeptics (challenge assumptions, find edge cases)

## Progressive Disclosure

Skills and commands can use progressive disclosure to manage token usage efficiently.

### Three-Level Structure

**Level 1: Metadata (YAML Frontmatter)**
- Always loaded when listing/discovering
- Brief description, name, essential metadata
- Helps users and Claude understand what's available

**Level 2: Core Content**
- Loaded when skill/command is invoked
- Essential instructions, conventions, guidelines
- What Claude needs to execute the task

**Level 3: Resources (Optional)**
- Loaded on-demand via explicit references
- Templates, examples, detailed documentation
- Used only when specifically needed


## Design Principles

### Single Source of Truth

Each piece of knowledge lives in exactly one place:
- Domain knowledge → skills
- Workflow logic → commands
- Execution details → agent implementation

Avoid duplication between skills, commands, and documentation.

### Orthogonality

Design components so changes to one don't require changes to others:
- Change skills → commands automatically benefit
- Change commands → skills remain unchanged
- Add new skills → no changes to existing commands

### Explicit Over Implicit

Make relationships and dependencies clear:
- Commands explicitly invoke skills by name, if the skills is known to be required
- Skills explicitly reference resources to load
- Data flow clearly visible in implementation

Avoid implicit coupling or hidden dependencies.

## Implementing This Pattern

### Creating Skills

1. **Identify reusable knowledge** that applies to multiple tasks
2. **Extract into dedicated skill** with clear name and description
3. **Use progressive disclosure** if content is large
4. **Document when to use** the skill

### Creating Commands

1. **Identify user-facing workflows** that need explicit invocation
2. **Load relevant skills** at the start
3. **Orchestrate tools and steps** to accomplish goal
4. **Provide clear feedback** to user

### Using Sub-agents

1. **Identify specialized tasks** that benefit from fresh context
2. **Define clear handoff** with specific instructions
3. **Let agent execute independently** without context pollution
4. **Integrate results** back into main flow

### Common Pitfalls

**Avoid:**
- Duplicating knowledge between skills and commands
- Creating skills that are too specific (not reusable)
- Creating commands that embed knowledge (use skills instead)
- Mixing execution and knowledge in single component

**Prefer:**
- Centralized knowledge in skills
- Workflow orchestration in commands
- Clean handoffs to specialized agents
- Clear separation of concerns
