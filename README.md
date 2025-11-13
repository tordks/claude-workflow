# Claude Workflow

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Claude Workflow (CWF) defines a plan-driven development workflow for Claude Code with phase-based implementation.

### What Problem Does CWF Solve?

Software development with AI assistants often suffers from three problems:

1. **Lost Context:** Agents lose architectural rationale and design decisions in long contexts and between sessions. Why was this approach chosen? What alternatives were considered? The Agent is stateless and if the context is removed it "forgets".

2. **Inconsistent Structure:** Without conventions, agents implement features differently every time. One session produces 50 tiny tasks, the next creates 3 giant ones. Tests get skipped. Documentation varies. The agent has no memory of what structure worked before — each implementation is a fresh start with unpredictable quality.

3. **Changing Requirements:** Plans become outdated as you discover edge cases, realize better approaches, or receive feedback. Without a safe amendment process, you either ignore the plan (losing its value) or start over (wasting effort). The plan represents the Agents knowledge of the current implementation effort. If it is outdated, erroneous implementation will occur.

4. **Loss of Control:** Agents can make dozens of changes without human interaction. Without explicit checkpoints, you're reviewing tons of work at once — finding the problem in change #47 when you should have caught it in change #3.

## When to use CWF

Claude Code has different modes for different types of work. CWF is a workflow framework that adds structure for complex, multi-session development.

**Use regular chat mode when:**
- Single-session work
- Quick fixes or simple features
- No architectural decisions needed
- Brainstorming

**Use plan mode when:**
- Starting more complex features
- You want to review the work to be done
- You don't want claude to start suggesting edits (plan-mode is read only)

*Plan mode lets Claude read and analyze without editing or executing. Great for careful deliberation before implementation.*


**Use CWF when:**
- Work spans multiple sessions
- Implementation plan might need amendment
- Need reviewable checkpoints with runnable code
- Building features that require commits during implementation


## Installation

Install as plugin in claude code:
1. `/plugin marketplace add tordks/claude-workflow`
2. `/plugin install cwf`


## The Workflow

```
  Planning Discussion
         ↓
     /write-plan
         ↓
   Plan + Tasklist
         ↓
   /implement-plan
         ↓
  Phase 1 → Review → ✓ → /clear
         ↓
 Phase 2 → Review → ✓ → /clear          
  [Changes?] → /amend-plan ──┐
         ↓                   │
  Continue development ←─────┘
         ↓
  Feature Complete ✓
```

## How It Works

CWF preserves context across sessions by storing planning and progress in structured documents, it uses two key mechanisms:

**Skills** provide specialized knowledge to Claude (planning conventions from `cfw-planning`, coding principles from `read-constitution`). They're loaded on-demand to keep context focused.

**Commands** are user-facing workflows like `/write-plan`, `/implement-plan`, and `/amend-plan` that orchestrate the feature development lifecycle. Commands load relevant skills automatically.

### Planning

The workflow begins by describing the feature to be implemented, either by
providing a written file with specifications, or through discussion with the
agent.


After the specifications is solidified, run `/write-plan` to create the planning documents:


- **Plan** (`feature-plan.md`): Captures WHY/WHAT—architectural decisions, design rationale, alternatives considered
- **Tasklist** (`feature-tasklist.md`): Defines WHEN/HOW—sequential phases with checkbox tracking `[x]`

The plan is divided into phases that at the end should produce runnable code. By
default implementation stops after each phase. Togheter this creates a
checkpoint where we can review and evaluate progress. It also enables us
to stay in control over what is implemented and catch errors early.

**TIP:**
- If planning over multiple sessions or you for some reason need to clear or compact context, ask the agent to save the planning to file.
- A plan made in plan-mode can be a great starting point for writing the plan
- You can add description or instructions when writing the plan: `/write-plan user-auth write a plan for phase 1 in my-complex-auth-plan.md`

### Implementation

The `/implement-plan` command starts the implementation of the
feature. The implementation will continue from the next task according to the
tasklist.  This allows continuing implementation from a clear context.  `/clear`
between each phase to not get degraded performance due to filled context.

**TIP:** You can add descriptions and instructions when starting or resuming implementation: `/implement-plan user-auth implement phase 1 and 2, then stop.`


### Amending plans

If requirements change during implementation, or we discover a gap in the plan,
we can amend the plan and tasklist. Start by clearing the context and
describing/discussing the changes to make. When the changes are properly
described run the `/amend-plan` command, which will update that plan and tasklist safely.

**TIP:** You can add a description of changes after the feature name: `/amend-plan user-auth Add OAuth2 support alongside email/password`. If the amendment don't need a discussion this can be done without clearing context or first dicussing the amendment.

**WARNING:** If we change implementation details mid-development and do not amend
the plan, the agent will not know about them. This means that it after the
context is cleared will assume that we have made no amendments. This is a recipe for
confusion and erroneous implementations.


### Coding Constitution

CWF supports a coding constitution (`.constitution/` directory) that guides implementation quality and consistency. The constitution is automatically loaded by `/write-plan`, `/implement-plan`, `/amend-plan` and by `/read-sontitution`. Example constitution files are available separately:

- **Software Engineering Principles:** DRY, YAGNI, orthogonality, separation of concerns
- **Testing Philosophy:** Test coverage expectations, testing patterns, when to test
- **Language Standards:** Python-specific conventions and best practices


Without shared standards, agents apply inconsistent conventions and make inconsistent quality decisions. The constitution ensures every implementation follows the same engineering principles.

Customize the .constitution for your project's standards.


### Command Reference

| Command | When to Use | Inputs | What It Does |
|---------|-------------|--------|--------------|
| `/write-plan` | After planning discussion | Feature name | Creates plan.md + tasklist.md in plans/ |
| `/implement-plan` | Ready to code or resuming | Feature name | Executes tasks phase-by-phase with checkpoints |
| `/amend-plan` | Requirements changed | Feature name | Updates plan/tasklist safely |
| `/read-constitution` | Need coding principles | None | Loads software engineering standards |


### Skill Reference

| Skill | Contains | How It's Used |
|-------|----------|---------------|
| `cfw-planning` | Planning structure, phase patterns, task format, amendment rules | Loaded by planning commands for consistency |
| `read-constitution` | Engineering fundamentals (DRY, YAGNI, orthogonality), testing philosophy | Loaded by /implement-plan for code quality |

### Tips for Success

**During Planning:**
- Be specific about requiremnents, components, technologies
- Set clear scope (what's IN and OUT)
- Define success criteria

It is all about solidifying our intent and reducing the solution space in which the agent can sample implementation details from.


**During Implementation:**
- Review at phase boundaries before approving
- Use `/amend-plan` when requirements change
- Keep phases small


## Alternatives & Resources

This is just YAADW (Yet Another Agent Development Workflow) that fit my
particular use-case. There are other more and less rigorous frameworks, that
generate different amounts of documentation. What thay all have in common is
that they follow some version of persisting a spec/plan to disk and then use it
to contain context between sessions. The difference is how that is done.

Below are some resources, which I not necessarily recommend. They are here for
me to reference later.

**Development Workflows:**

- [superpowers](https://github.com/obra/superpowers) - Comprehensive skills library with proven techniques and patterns that auto-activate through Claude Code's plugin system
- [spec-kit](https://github.com/github/spec-kit) - Spec-Driven Development toolkit where detailed specifications become executable artifacts that directly generate implementations
- [superclaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Meta-programming framework with 16 specialized agents and 7 behavioral modes for systematic workflow automation
- [BMAD-method](https://github.com/bmad-code-org/BMAD-METHOD) - Human-AI collaboration framework with 19+ specialized agents for software development, creativity, and problem-solving
- [claude-orchestration](https://github.com/mbruhler/claude-orchestration) - Multi-agent workflow orchestration enabling sequential, parallel, and conditional chaining of AI agents with manual checkpoints

**Resources:**

- [awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - Curated list of Claude Skills organized by category (document handling, development, data analysis, scientific research, etc.)
- [claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) - PAtterns for auto-activating skills, modular organization, and scaling AI-assisted development
- [Martin Fowler on Spec-Driven Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) - Conceptual overview of specification-driven AI development approaches
- [claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver) - Prompt enhancement tool that intercepts and enriches vague prompts with targeted clarifying questions
- [armchr](https://github.com/armchr/armchr) - Toolkit with Splitter and Reviewer agents for helping AI better analyze and understand code through logical commit chunking
- [claude-code-switch](https://github.com/foreveryh/claude-code-switch) - Model switching tool supporting multiple AI providers (Claude, Deepseek, KIMI, GLM, Qwen) with intelligent fallback