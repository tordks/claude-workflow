# Non-Claude-Code Tools & Frameworks

Tools that solve similar problems but are not Claude Code plugins, skills, or
extensions. Included for broader context on the spec-driven / agentic coding
landscape.

Research conducted February 2026. See [alternatives.md](alternatives.md) for
Claude Code-compatible tools.

---

## Agent-Agnostic Development Frameworks

### spec-kit (GitHub)

- **URL:** <https://github.com/github/spec-kit>
- **Stars:** 69,676
- **Status:** Very active (v0.0.95, Feb 2026)
- **What it does:** GitHub's official open-source toolkit for Spec-Driven
  Development. Provides templates, a CLI, and prompts for a specification-first
  approach. Agent-agnostic -- works with GitHub Copilot, Claude Code, Gemini CLI,
  and others.

### BMAD-METHOD

- **URL:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Stars:** 35,590
- **Status:** Very active (v6.0.0-Beta.8, Feb 2026)
- **What it does:** Multi-agent collaboration framework with 21 specialized agent
  roles. Targets Claude Code, Cursor, and Windsurf equally. Not Claude
  Code-specific.

### claude-flow

- **URL:** <https://github.com/ruvnet/claude-flow>
- **Stars:** 14,046
- **Status:** Very active (v3)
- **What it does:** General-purpose multi-agent orchestration platform. Deploys AI
  agent "swarms" with shared memory, consensus protocols, and 175+ MCP tools.
  Supports Claude among many providers. MCP integration is optional.

### VibeCoder (vc) + Beads

- **URL:** <https://github.com/steveyegge/vc>
- **Stars:** 296
- **Beads:** <https://github.com/steveyegge/beads>
- **Beads Stars:** 16,256
- **What it does:** Standalone Go-based orchestration tool managing a "colony" of
  coding agents through a git-backed graph issue tracker (Beads). Uses Claude Code
  as one worker agent among others.

### Vibe-Kanban

- **URL:** <https://github.com/BloopAI/vibe-kanban>
- **Stars:** 21,211
- **Status:** Very active
- **What it does:** Web-based kanban board for orchestrating multiple coding agents
  (Claude Code, Codex, Gemini CLI, Amp) in parallel. Each task gets its own Git
  Worktree and agent.

### context7 (Upstash)

- **URL:** <https://github.com/upstash/context7>
- **Stars:** 45,721
- **Status:** Very active
- **What it does:** MCP server providing up-to-date, version-specific library
  documentation and code examples. Works with any MCP client (Claude Code, Cursor,
  Gemini CLI, etc.).

### awesome-agent-skills (VoltAgent)

- **URL:** <https://github.com/VoltAgent/awesome-agent-skills>
- **Stars:** 7,039
- **What it does:** 300+ agent skills from official dev teams and the community.
  Cross-platform compatible with Claude Code, Codex, Gemini CLI, Cursor, and
  others using the SKILL.md open standard.

### claude-context (zilliztech)

- **URL:** <https://github.com/zilliztech/claude-context>
- **Stars:** 5,333
- **What it does:** MCP server adding semantic code search (hybrid BM25 + dense
  vector) to any MCP-compatible client. Requires Zilliz Cloud and OpenAI API.

---

## Spec-Driven Development

### Amazon Kiro

- **URL:** <https://kiro.dev>
- **Status:** Preview (free; planned pricing $19-39/month)
- **What it does:** AWS's spec-driven agentic IDE (VS Code fork). Workflow:
  natural language requirements -> user stories with acceptance criteria ->
  technical design documents -> trackable implementation tasks. Uses Claude
  Sonnet 4.5.
- **Relation to CWF:** Most directly comparable commercial tool. Both enforce a
  spec-driven, plan-then-implement workflow. Key difference: Kiro is an entire
  IDE; CWF is a lightweight plugin for Claude Code.

### Tessl

- **URL:** <https://tessl.io>
- **Status:** Active (commercial)
- **What it does:** Agent enablement platform pioneering spec-driven development.
  Two products: Tessl Framework (keeps agents on rails using specifications) and
  Tessl Spec Registry (10,000+ specs explaining how to use external libraries,
  preventing API hallucinations).

### moai-adk

- **URL:** <https://github.com/modu-ai/moai-adk>
- **Stars:** 721
- **Status:** Active (v1.0.0 Production Ready, Jan 2026)
- **What it does:** Comprehensive AI development framework built around SPEC-First
  Development (EARS format), Domain-Driven Development, and Intelligent
  Orchestration with 20+ specialized agents. Standalone Go binary.

---

## Autonomous Coding Agents

### ralph

- **URL:** <https://github.com/snarktank/ralph>
- **Stars:** 10,303
- **Status:** Active
- **What it does:** Autonomous AI agent loop that runs repeatedly until all PRD
  items are complete. Creates feature branches, picks highest-priority stories,
  implements them, runs quality checks, commits, and repeats. Works with Claude
  Code as the underlying agent.
- **Note:** Uses Claude Code under the hood but is an external orchestrator, not
  a plugin.

### Devin (Cognition)

- **URL:** <https://devin.ai>
- **Status:** Commercial ($500+/month). $10.2B valuation.
- **What it does:** Autonomous AI software engineer with its own command line,
  browser, and editor. Devin 2.0 features Interactive Planning (generates
  detailed plans users can modify before execution). Cognition acquired Windsurf.

### OpenHands

- **URL:** <https://openhands.dev>
- **What it does:** Open-source, model-agnostic platform for cloud coding agents.
  Agents interact like human developers: writing code, using command line,
  browsing the web. Evaluation harness with 15+ benchmarks (SWE-bench, etc.).

---

## Agentic IDEs & Coding Assistants

### Cline

- **URL:** <https://github.com/cline/cline>
- **Stars:** 57,948
- **What it does:** Open-source VS Code extension with "Plan, Preview, Apply"
  agentic workflow. Plans tasks, shows diffs, and executes with user approval.
  Model-agnostic. Plans are transient, not persisted as structured documents.

### Aider

- **URL:** <https://aider.chat>
- **Stars:** 40,634
- **What it does:** Free, open-source CLI-based AI coding assistant with
  exceptional Git integration and automatic commit messages. Terminal-first
  workflow, model-agnostic.

### Continue.dev

- **URL:** <https://continue.dev>
- **Stars:** 31,391
- **What it does:** Open-source AI coding assistant for VS Code and JetBrains.
  Supports Chat, Plan, and Agent modes. Model-agnostic, MCP support.

### Goose (Block)

- **URL:** <https://github.com/block/goose>
- **Stars:** 30,432
- **What it does:** Open-source (Apache 2.0) extensible AI agent from Block
  (Square). Works with any LLM, supports MCP. Contributed to the Linux
  Foundation's Agentic AI Foundation alongside Anthropic's MCP.

### Roo Code

- **URL:** <https://roocode.com>
- **Stars:** 22,220
- **What it does:** Open-source autonomous AI agent for VS Code with role-based
  modes (Architect, Code, Debug, Ask, Custom). Forked from Cline's codebase.

---

## GitHub Platform Features

### GitHub Copilot Coding Agent

- **URL:** <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>
- **Status:** Generally available (GA since Sep 2025)
- **What it does:** Asynchronous autonomous coding agent built into GitHub. Assign
  a GitHub issue to Copilot, it works in a GitHub Actions sandbox, pushes commits
  to a draft PR, runs tests, and requests human review. Supports `AGENTS.md`.

### GitHub Agent HQ

- **URL:** <https://github.com/features/copilot/agents>
- **Status:** Preview (announced Oct 2025)
- **What it does:** Unified control plane for managing multiple AI coding agents
  from different providers (Anthropic, OpenAI, Google, etc.) within GitHub and VS
  Code. Custom agents via markdown profiles in `.github/agents/`.

### GitHub Agentic Workflows (gh-aw)

- **URL:** <https://github.com/github/gh-aw>
- **Status:** Technical preview (Feb 13, 2026)
- **What it does:** Define repository automation in plain Markdown files, compiled
  into GitHub Actions YAML. Executed by AI coding agents (Copilot CLI, Claude
  Code, or OpenAI Codex) triggered by repo events.
