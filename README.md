# Claude Workflow

[![Version](https://img.shields.io/badge/version-0.2.2-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Claude Workflow (CWF) defines a plan-driven development workflow for Claude Code with phase-based implementation.

## What Problem Does CWF Solve?

When work spans multiple sessions or outgrows a single context window, AI-assisted development breaks down in two ways:

1. **The agent loses context.** Architectural decisions, refined requirements, and implementation progress disappear when context is compacted or a session ends. The next session starts from scratch, and the agent re-derives what was already decided, or worse, decides differently.

2. **The developer loses ownership.** Without a plan to review upfront, the agent makes design decisions implicitly as it codes. Problems compound across files before anyone notices, and the codebase drifts from the developer's intent.

Both stem from the same gap: nothing captures what was decided, what was built, and what remains. CWF fills this gap with plan and tasklist documents, and structures implementation around them:

- **Persistent plan documents** give every session the full picture of architectural decisions, design rationale, and progress so far.
- **Phase-based implementation** breaks work into sequential phases with concrete deliverables, so scope and sequencing are decided before coding starts.
- **Automated checkpoints** run code quality, complexity, and test checks at phase boundaries, catching issues before they accumulate.
- **Scheduled human review** between phases keeps the developer in control, not just informed.

## When to Use CWF

The workflow should match the complexity of the work. CWF is designed for features that involve architectural decisions, touch multiple components, or span multiple sessions. For quick fixes or single-session work, chat mode or plan mode is more efficient.

**Chat mode** — no upfront planning:

- Fix a null pointer exception
- Add one or more logging statements
- Explore or explain unfamiliar code

**Plan mode** — plan first, then implement in one session:

- Add form validation to the signup page
- Refactor a module to use dependency injection

**CWF** — persistent plan, multi-session with review checkpoints:

- Build user authentication with OAuth, sessions, and role-based access
- Add a payment integration that touches API, database, and frontend
- Bootstrap and set up an initial version of a greenfield project
- Implement a new feature that requires design decisions and will take multiple sessions to complete

## The Workflow

Based on an input context (specification, design discussion, or exploration), CWF produces a plan and tasklist that break down the work into phases with runnable deliverables. The agent implements phase-by-phase, running quality checkpoints and pausing for human review before proceeding to the next phase.

Each phase is started manually with `/implement-plan`, which continues from the next incomplete task and accepts free-form instructions to control scope. This allows you to pause and resume implementation across sessions without losing context or progress.

```text
       input context (plan draft, design discussion, specification file)
               │
               ├── /explore (optional: iterative discovery
               │             to converge on design before
               │             planning)
               ↓
           /write-plan
               ↓
         Review plan + tasklist
               ↓
        /implement-plan ←──────┐
               ↓               │
        Execute phase tasks    │ repeat
               ↓               │ per
        Run checkpoints        │ phase
               ↓               │
        Human review           │
               ↓               │
            /clear ────────────┘
               ↓ (all phases done)
         Feature complete

    /amend-plan: update documents when requirements change
```

## Getting Started

Install as plugin in Claude Code:

1. `/plugin marketplace add tordks/claude-workflow` - adds repository to your marketplace
2. `/plugin install cwf@claude-workflow` - installs the plugin

To uninstall: `/plugin uninstall cwf@claude-workflow`

### Example usage

```text
# discuss the feature in chat, then create the plan from the conversation
/write-plan redis-queue

# or reference a spec or draft directly
/write-plan redis-queue docs/redis-queue-draft.md

# → creates plan + tasklist in .cwf/redis-queue/
# review the plan before implementing

/implement-plan redis-queue     # phase 1: Redis infra + config

/clear

/implement-plan redis-queue     # phase 2: poller + worker + API rewire

/clear

/amend-plan redis-queue add stale job detection for crashed workers
# → updates plan and tasklist to include stale job recovery

/clear

/implement-plan redis-queue     # continues where we left off
```

See [docs/examples/](docs/examples/) for example plan and tasklist made by `/write-plan`.

## Usage Guide

CWF provides four slash commands that orchestrate the workflow. Commands automatically load the `claude-workflow` skill, which provides planning structure, task format, and amendment rules.

### Command Reference

| Command | When to Use | What It Does |
|---------|-------------|--------------|
| `/explore [initial context]` | During planning | Iterative discovery of requirements, approaches, and design converging on a design summary |
| `/write-plan [feature-name] [planning context]` | After planning | Writes planning documents |
| `/implement-plan [feature-name] [instructions]` | Start/Resume implementation | Executes tasks phase-by-phase with quality checkpoints |
| `/amend-plan [feature-name] [amendment description]` | Requirements changed or gaps identified | Updates plan/tasklist safely |

Arguments: `[feature-name]` is optional — auto-detected when only one plan exists, otherwise prompts for selection. Additional arguments are optional free-form text for context or constraints.

### Planning

`/write-plan` creates the planning documents in `.cwf/{feature-name}/` at your project root:

- **Plan** `.cwf/{feature-name}/{feature-name}-plan.md`: Captures WHY/WHAT—architectural decisions, design rationale, alternatives considered
- **Tasklist** `.cwf/{feature-name}/{feature-name}-tasklist.md`: Defines WHEN/HOW—sequential phases with checkbox tracking `[x]`
- **Mockup** `.cwf/{feature-name}/{feature-name}-mockup.html` (optional): Visual reference for UI/frontend features

Example plan and tasklist can be found in [`docs/examples/`](docs/examples/).

**Tips:**

- `/write-plan` works from any input (conversation, spec file, or draft): `/write-plan user-auth auth-spec.md`.
- Be specific. "OAuth2 with Google, PostgreSQL sessions, admin/user roles" beats "build auth".
- You can scope to part of a written spec: `/write-plan user-auth only the auth layer from auth-spec.md`.
- Discuss the feature or draft in chat first. Ask for diagrams (SVG, Mermaid) for schemas or architecture to ensure the agent understands before planning.
- For UI features, request an HTML mockup to verify layout before implementation.
- For multi-session planning, save a summary and reference it when resuming.

### Implementation

Run `/implement-plan` to start implementing the feature. The agent continues from the next incomplete task in the tasklist, allowing you to resume with clear context.

At the end of each phase, the agent runs **checkpoints**—validation operations that ensure code quality before proceeding:

- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality checks:** Linting, formatting, type checking—runs whatever tools the project already uses (e.g., eslint, prettier, mypy, ruff)
- **Complexity checks:** Code complexity analysis—runs if project has complexity tools configured

These checkpoints catch issues early before they accumulate (e.g., ever-increasing function or file size). After checkpoints pass, implementation stops for human review before proceeding to the next phase.

**Tips:**

- Pass instructions to scope a run. `/implement-plan user-auth phase 1, 2 and 3` will run phase 1-3 without stopping for review.
- If the session has room, skip `/clear` and write "continue to next phase" to reuse context.
- Run independent phases in parallel with subagents: `/implement-plan user-auth use subagents for phase 1 and 2 in parallel`.

### Amending Plans

If requirements change during implementation or you discover a gap in the plan, use `/amend-plan` to update the plan and tasklist safely.

> **Warning:** Changing implementation without amending the plan causes confusion after `/clear`. The agent treats the plan as its source of truth and will undo or conflict with unamended changes. Always `/amend-plan` before (or immediately after) deviating.

**Tips:**

- For simple changes: `/amend-plan my-cli-tool add --output option`.
- For complex amendments, clear context and discuss amendments before amending.
- If the change invalidates the overall approach, re-plan with `/write-plan` instead.

## Alternatives & Resources

CWF is one approach to agent development workflows. Other frameworks vary in rigor and documentation requirements, but most share the core concept of persisting specifications to maintain context between sessions. Below are some related projects and resources in the Claude Code ecosystem.

### Plan-Driven Development

- [superpowers](https://github.com/obra/superpowers) - Comprehensive skills library with techniques and patterns that auto-activate through Claude Code's plugin system
- [spec-kit](https://github.com/github/spec-kit) - GitHub's Spec-Driven Development toolkit where specifications become executable artifacts that generate implementations
- [GSD (Get Shit Done)](https://github.com/gsd-build/get-shit-done) - Spec-driven development system with specialized agents, programmatic tooling, and state management
- [BMAD-method](https://github.com/bmad-code-org/BMAD-METHOD) - Human-AI collaboration framework with specialized agents for software development, creativity, and problem-solving
- [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Configuration framework with specialized slash commands, cognitive personas, and behavioral modes
- [spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp) - MCP server for structured spec-driven development with real-time dashboard, VSCode extension, and session caching
- [Claude Pilot](https://github.com/maxritter/claude-pilot) - Development framework with spec-driven workflows, TDD enforcement, persistent memory, and continuous quality checks via hooks

### Multi-Agent Orchestration

- [Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) - Official Anthropic feature: coordinated Claude Code instances with a team lead, shared task list, and dependency tracking
- [Gas Town](https://github.com/steveyegge/gastown) - Workspace manager using git-backed "beads" for persistent state across a fleet of AI agents
- [CLI Agent Orchestrator (AWS)](https://github.com/awslabs/cli-agent-orchestrator) - AWS-backed hierarchical orchestration with supervisor agent coordinating workers in isolated sessions
- [babysitter](https://github.com/a5c-ai/babysitter) - Event-sourced orchestration with quality convergence, human-in-the-loop breakpoints, and pause/resume/recovery
