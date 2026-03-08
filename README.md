# Claude Workflow

[![Version](https://img.shields.io/badge/version-0.3.0-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Claude Workflow (CWF) defines a spec-driven development workflow for Claude Code with phase-based implementation.

## What Problem Does CWF Solve?

When work spans multiple sessions or outgrows a single context window, AI-assisted development breaks down in two ways:

1. **The agent loses context.** Architectural decisions, refined requirements, and implementation progress disappear when context is compacted or a session ends. The next session starts from scratch, and the agent re-derives what was already decided, or worse, decides differently.

2. **The developer loses ownership.** Without a plan to review upfront, the agent makes design decisions implicitly as it codes. Problems compound across files before anyone notices, and the codebase drifts from the developer's intent.

Both stem from the same gap: nothing captures what was decided, what was built, and what remains. CWF fills this gap with spec and state documents, and structures implementation around them:

- **Persistent spec documents** give every session the full picture of architectural decisions, design rationale, and progress so far.
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

**CWF** — persistent spec, multi-session with review checkpoints:

- Build user authentication with OAuth, sessions, and role-based access
- Add a payment integration that touches API, database, and frontend
- Bootstrap and set up an initial version of a greenfield project
- Implement a new feature that requires design decisions and will take multiple sessions to complete

## The Workflow

Based on an input context (specification, design discussion, or exploration), CWF produces a spec and state that break down the work into phases with runnable deliverables. The agent implements phase-by-phase, running quality checkpoints and pausing for human review before proceeding to the next phase.

Each phase is started manually with `/implement`, which continues from the next incomplete task and accepts free-form instructions to control scope. This allows you to pause and resume implementation across sessions without losing context or progress.

```text
       input context (spec draft, design discussion, specification file)
               │
               ├── /explore (optional: iterative discovery
               │             to converge on design before
               │             planning)
               ↓
           /write-spec
               ↓
         Review spec + state
               ↓
        /implement ←───────────┐
               ↓               │
        Execute phase          │ repeat
        tasks                  │ per
               ↓               │ phase
        Run checkpoints        │
               ↓               │
        Human review           │
               ↓               │
            /clear ────────────┘
               ↓ (all phases done)
         Feature complete

    /amend: update documents when requirements change
```

## Getting Started

Install as plugin in Claude Code:

1. `/plugin marketplace add tordks/claude-workflow` - adds repository to your marketplace
2. `/plugin install cwf@claude-workflow` - installs the plugin

To uninstall: `/plugin uninstall cwf@claude-workflow`

### Example usage

```text
# discuss the feature in chat, then create the spec from the conversation
/write-spec redis-queue

# or reference a spec or draft directly
/write-spec redis-queue docs/redis-queue-draft.md

# → creates spec + state in .cwf/redis-queue/
# review the spec before implementing

/implement redis-queue     # phase 1: Redis infra + config

/clear

/implement redis-queue     # phase 2: poller + worker + API rewire

/clear

/amend redis-queue add stale job detection for crashed workers
# → updates spec and state to include stale job recovery

/clear

/implement redis-queue     # continues where we left off
```

See [docs/examples/](docs/examples/) for example spec and state made by `/write-spec`.

## Usage Guide

CWF provides four slash commands that orchestrate the workflow.

### Command Reference

| Command | When to Use | What It Does |
|---------|-------------|--------------|
| `/explore [initial context]` | During planning | Iterative discovery that converges on a design summary |
| `/write-spec [feature-name] [planning context]` | After planning | Creates spec and state from input context |
| `/implement [feature-name] [instructions]` | Start/Resume implementation | Executes tasks phase-by-phase with quality checkpoints |
| `/amend [feature-name] [amendment description]` | Requirements changed or gaps identified | Updates spec/state safely |

`[feature-name]` is optional for `/write-spec`, `/implement`, and `/amend`. `/implement` and `/amend` auto-detect when only one spec exists, otherwise prompt for selection. `/write-spec` suggests a name from conversation context. All additional arguments are optional free-form text.

### Planning

`/write-spec` creates the planning documents in `.cwf/{feature-name}/` at your project root:

- **Spec** `.cwf/{feature-name}/{feature-name}-spec.md`: Captures WHY/WHAT—architectural decisions, design rationale, alternatives considered
- **State** `.cwf/{feature-name}/{feature-name}-state.md`: Tracks WHEN/HOW—sequential phases with task tracking
- **Mockup** `.cwf/{feature-name}/{feature-name}-mockup.html` (optional): Visual reference for UI/frontend features

Example spec and state can be found in [`docs/examples/`](docs/examples/).

**Tips:**

- `/write-spec` works from any input (conversation, spec file, or draft): `/write-spec user-auth auth-spec.md`.
- Be specific. "OAuth2 with Google, PostgreSQL sessions, admin/user roles" beats "build auth".
- You can scope to part of a written spec: `/write-spec user-auth only the auth layer from auth-spec.md`.
- Discuss the feature or draft in chat first. Ask for diagrams (SVG, Mermaid) for schemas or architecture to ensure the agent understands before planning.
- For UI features, request an HTML mockup to verify layout before implementation.
- For multi-session planning, save a summary and reference it when resuming.

### Implementation

Run `/implement` to start implementing the feature. The agent continues from the next incomplete task in the state, allowing you to resume with clear context.

At the end of each phase, the agent runs **checkpoints** to validate quality before proceeding. `/write-spec` picks up on configured tooling and tailors checkpoints to the project. These can for example include:

- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality:** Linting, formatting, type checking
- **Code complexity:** Function size, branching depth, and cyclomatic complexity
- **Dead code:** Verify removed functionality don't leave orphans

Checkpoints catch issues early before they accumulate (e.g., ever-increasing function size or deep nesting). After checkpoints pass, implementation stops for human review before proceeding to the next phase.

**Tips:**

- Pass instructions to scope a run. `/implement user-auth phase 1, 2 and 3` will run phase 1-3 without stopping for review.
- If the session has room, skip `/clear` and write "continue to next phase" to reuse context.
- Run independent phases in parallel with subagents: `/implement user-auth use subagents for phase 1 and 2 in parallel`.

### Amending Specs

If requirements change during implementation or you discover a gap in the spec, use `/amend` to update the spec and state safely.

> **Warning:** Changing implementation without amending the spec causes confusion after `/clear`. The agent treats the spec as its source of truth and will undo or conflict with unamended changes. Always `/amend` before (or immediately after) deviating.

**Tips:**

- For simple changes: `/amend my-cli-tool add --output option`.
- For complex amendments, clear context and discuss amendments before amending.
- If the change invalidates the overall approach, re-plan with `/write-spec` instead.

## Alternatives & Resources

CWF is one approach to agent development workflows. Other frameworks vary in rigor and documentation requirements, but most share the core concept of persisting specifications to maintain context between sessions. Below are some related projects and resources in the Claude Code ecosystem.

### Spec-Driven Development

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
