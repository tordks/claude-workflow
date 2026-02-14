# Alternatives & Resources Research

Research conducted February 2026. This document evaluates tools in the Claude Code
ecosystem for inclusion in the README's "Alternatives & Resources" section.

---

## Plan-Driven Development Workflows

Direct alternatives to CWF -- tools that structure AI development through
planning before coding.

### spec-kit (GitHub)

- **URL:** <https://github.com/github/spec-kit>
- **Stars:** 69,676
- **Status:** Very active (v0.0.95, Feb 2026)
- **What it does:** GitHub's official open-source toolkit for Spec-Driven
  Development. Provides templates, a CLI, and prompts for a specification-first
  approach: write a spec, create a technical plan, break into tasks, then have AI
  agents implement. Agent-agnostic -- works with GitHub Copilot, Claude Code,
  Gemini CLI, and others.
- **Relation to CWF:** Most prominent project in the spec-driven space. Similar
  philosophy but delivered as a general-purpose toolkit (templates + CLI) rather
  than a Claude Code plugin with integrated commands and skills.
- **Verdict:** KEEP. Major project, validates the spec-driven approach.

### GSD (Get Shit Done)

- **URL:** <https://github.com/gsd-build/get-shit-done>
- **Stars:** 13,925
- **Status:** Very active (v1.18.0, Feb 2026, rapid release cadence)
- **What it does:** Meta-prompting, context engineering, and spec-driven
  development system for Claude Code. Provides a structured workflow with
  research, requirements, and roadmap phases before coding. Features specialized
  agents (executor, planner, plan-checker, verifier), programmatic gsd-tools for
  verification, and state management in `.planning/`. Trusted by engineers at
  Amazon, Google, Shopify, and Webflow.
- **Relation to CWF:** Closest direct comparison. Both solve the same core
  problem (structuring AI development through planning). GSD is more
  batteries-included with multiple specialized agents and programmatic tooling;
  CWF is lighter-weight with RFC 2119 specifications.
- **Verdict:** ADD. Major direct competitor, very popular and actively
  maintained.

### The Deep Trilogy (deep-plan)

- **URL:** <https://github.com/piercelamb/deep-plan>
- **Stars:** 17
- **Status:** Active (launched Jan-Feb 2026)
- **What it does:** Three Claude Code plugins: `/deep-project` (transforms ideas
  into components), `/deep-plan` (transforms components into plans via research,
  interviews, and multi-LLM review), `/deep-implement` (implements with TDD and
  code review). Born from manually orchestrating a planning workflow that fixed
  Claude Code's tendency to code immediately without planning.
- **Relation to CWF:** Very directly comparable. Same core problem, similar
  solution. Uses multi-LLM review and interview steps; CWF uses single plan
  documents with RFC 2119 specifications. Deep Trilogy is three separate plugins;
  CWF is one integrated plugin with four commands.
- **Verdict:** ADD. Directly comparable plan-first workflow.

### superpowers

- **URL:** <https://github.com/obra/superpowers>
- **Stars:** 51,421
- **Status:** Very active (v4.2.0, Feb 2026)
- **What it does:** Agentic skills framework and software development methodology
  for Claude Code. Provides composable "skills" for TDD, debugging,
  collaboration, and structured planning. Includes commands like `/brainstorm`,
  `/write-plan`, and `/execute-plan`. Skills recently separated into
  `obra/superpowers-skills`.
- **Relation to CWF:** Both provide plan-driven development workflows.
  Superpowers takes a broader approach with 20+ skills; CWF focuses specifically
  on the planning workflow with formal RFC 2119 specifications. Largest community
  plugin for Claude Code.
- **Verdict:** KEEP. Dominant community project.

### BMAD-METHOD

- **URL:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Stars:** 35,590
- **Status:** Very active (v6.0.0-Beta.8, Feb 2026)
- **What it does:** Multi-agent collaboration framework with specialized AI
  agent roles (Analyst, Architect, Product Manager, Scrum Master, Developer). A
  "Scrum Master" agent transforms plans into hyper-detailed development stories,
  which a "Dev" agent implements. v6 introduced "BMad-CORE" (Collaboration
  Optimized Reflection Engine), scale-adaptive intelligence, and custom standalone
  agents. Not Claude Code-specific.
- **Relation to CWF:** Similar philosophy (structured planning artifacts drive
  implementation). BMAD goes further with multiple agent personas and opinionated
  agile methodology. Broader scope, not Claude Code-specific.
- **Verdict:** KEEP. Very popular, validates plan-driven approach.

### cc-blueprint-toolkit

- **URL:** <https://github.com/croffasia/cc-blueprint-toolkit>
- **Stars:** 181
- **Status:** Active (updated within last 2 weeks)
- **What it does:** Claude Code plugin for "smart blueprint-driven development."
  AI analyzes codebase patterns, creates comprehensive implementation plans, then
  delivers production-ready code with tests. Features codebase pattern analysis,
  auto task breakdown, smart research agents.
- **Relation to CWF:** Another plan-driven development tool. Focuses on pattern
  analysis of existing code to generate blueprints; CWF is more about
  spec-driven planning from requirements.
- **Verdict:** ADD. Relevant plan-driven alternative, though smaller.

### claude-code-spec-workflow (Pimzino)

- **URL:** <https://github.com/Pimzino/claude-code-spec-workflow>
- **Stars:** 3,422 (MCP version: 3,885)
- **MCP version:** <https://github.com/Pimzino/spec-workflow-mcp>
- **Status:** Limited updates on Claude Code version; focus shifted to MCP version
- **What it does:** Spec-driven development workflow plugin. Features a structured
  pipeline: Requirements -> Design -> Tasks -> Implementation (new features), and
  Report -> Analyze -> Fix -> Verify (bug fixes). Includes steering documents and
  session-based caching.
- **Relation to CWF:** Similar spec-first pipeline. Development focus has shifted
  to the MCP version with a web dashboard and VS Code extension.
- **Verdict:** ADD. Relevant spec-driven alternative.

### moai-adk

- **URL:** <https://github.com/modu-ai/moai-adk>
- **Stars:** 721
- **Status:** Active (v1.0.0 Production Ready, Jan 2026)
- **What it does:** Comprehensive AI development framework built around SPEC-First
  Development (EARS format), Domain-Driven Development, and Intelligent
  Orchestration with 20+ specialized agents. Rewritten from Python to Go as a
  single zero-dependency binary. 9,800+ tests with 80%+ coverage.
- **Relation to CWF:** SPEC-First approach parallels CWF's plan-driven
  philosophy. More opinionated and heavier-weight. Not Claude Code-specific;
  standalone Go binary.
- **Verdict:** KEEP. Relevant but niche, standalone architecture.

---

## Multi-Agent Orchestration

Tools that coordinate multiple AI agents working together.

### Claude Code Agent Teams (Official Anthropic)

- **URL:** <https://code.claude.com/docs/en/agent-teams>
- **Status:** Research preview / experimental (shipped with Claude Opus 4.6, Feb
  2026)
- **What it does:** Official first-party Anthropic feature. Coordinates multiple
  Claude Code instances where one session acts as "team lead" assigning tasks and
  synthesizing results. Teammates work independently with their own context
  windows. Shared task list with dependency tracking. Disabled by default; enable
  with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`.
- **Relation to CWF:** Anthropic's official answer to multi-agent coordination.
  The shared task list overlaps conceptually with CWF's tasklist-spec. Key
  difference: Agent Teams is runtime orchestration; CWF is a planning
  methodology. Potentially complementary -- CWF generates plans that Agent Teams
  executes.
- **Verdict:** ADD. Official Anthropic feature, important context for the
  ecosystem.

### Gas Town

- **URL:** <https://github.com/steveyegge/gastown>
- **Stars:** 9,351
- **Status:** Very active (launched Jan 2026)
- **What it does:** Multi-agent workspace manager by Steve Yegge. "The Mayor" is a
  Claude Code instance with full workspace context that organizes work into
  "beads" (git-backed data units) and manages a fleet of AI agents. Solves the
  problem of context windows filling up by persisting work state in git-backed
  hooks.
- **Relation to CWF:** Much larger scope (full workspace management). Requires
  "beads" as a dependency. CWF is lighter weight and plan-document-centric.
- **Verdict:** ADD. Notable project from a prominent voice in the space.

### babysitter

- **URL:** <https://github.com/a5c-ai/babysitter>
- **Stars:** 206
- **Status:** Active
- **What it does:** Deterministic, event-sourced orchestration framework for Claude
  Code. Everything recorded in `.a5c/runs/` for pause/resume/recovery. Features
  quality convergence (tasks iterate until passing quality checks), human-in-the-
  loop breakpoints, agent scoring, and parallel execution.
- **Relation to CWF:** Complementary rather than competitive. CWF focuses on plan
  authoring; babysitter focuses on plan execution (running tasks, gating on
  quality, resuming after failures). More heavyweight with npm packages and its
  own state management.
- **Verdict:** ADD. Interesting complementary orchestration tool.

### claude-flow

- **URL:** <https://github.com/ruvnet/claude-flow>
- **Stars:** 14,046
- **Status:** Very active (v3)
- **What it does:** Multi-agent orchestration platform. Deploys specialized AI
  agent "swarms" with shared memory, consensus protocols, and continuous learning.
  175+ MCP tools. Includes SPARC methodology (Specification, Pseudocode,
  Architecture, Refinement, Completion) with 17 specialized development modes.
- **Relation to CWF:** Large-scope infrastructure framework. Very different
  philosophy from CWF's lightweight plan-document approach.
- **Verdict:** ADD. Popular orchestration platform.

### claude-orchestration

- **URL:** <https://github.com/mbruhler/claude-orchestration>
- **Stars:** 198
- **Status:** Moderate activity
- **What it does:** Claude Code plugin for multi-agent workflow orchestration.
  Provides workflow syntax for sequential pipelines (`step1 -> step2`), parallel
  execution (`[task1 || task2]`), and conditional logic. Supports custom agents
  from `~/.claude/agents/`.
- **Relation to CWF:** Same plugin distribution model. Focused on multi-agent
  orchestration rather than plan-driven workflows. The workflow syntax is a
  distinguishing feature.
- **Verdict:** DROP. Low adoption, less distinctive now that Agent Teams exists.

### VibeCoder (vc) + Beads

- **URL:** <https://github.com/steveyegge/vc>
- **Stars:** 296
- **Beads:** <https://github.com/steveyegge/beads>
- **Beads Stars:** 16,256
- **Status:** Active development (Go rewrite, dogfooding phase)
- **What it does:** Issue-oriented orchestration system managing a "colony" of
  coding agents. All work flows through an issue tracker. Zero heuristics -- all
  decisions delegated to AI. Beads is a distributed, git-backed graph issue
  tracker providing persistent memory for coding agents.
- **Relation to CWF:** Fundamentally different philosophy. Instead of plan
  documents, uses a graph-based issue tracker as source of truth. External
  orchestrator rather than in-Claude plugin.
- **Verdict:** KEEP (beads as memory tool). The vc orchestrator overlaps with
  gastown (same author) and is less mature.

### CLI Agent Orchestrator (AWS)

- **URL:** <https://github.com/awslabs/cli-agent-orchestrator>
- **Stars:** 237
- **Status:** Recently announced, AWS-backed
- **What it does:** AWS-backed multi-agent orchestration framework. Hierarchical
  supervisor agent coordinates specialized workers in isolated tmux sessions.
  Supports Claude Code and Amazon Q CLI. MCP protocol communication.
- **Relation to CWF:** Infrastructure-level tool, not plan-driven. Could serve as
  execution infrastructure.
- **Verdict:** ADD. AWS-backed, notable institutional support.

---

## GitHub Platform Tools

GitHub's native agentic development features.

### GitHub Copilot Coding Agent

- **URL:** <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>
- **Status:** Generally available (GA since Sep 2025)
- **What it does:** Asynchronous autonomous coding agent built into GitHub. Assign
  a GitHub issue to Copilot, it works in a GitHub Actions sandbox, pushes commits
  to a draft PR, runs tests, and requests human review. Supports custom
  instructions via `AGENTS.md`. Recently upgraded to GPT-5.3-Codex (Feb 2026).
- **Verdict:** ADD. Major platform feature, important ecosystem context.

### GitHub Agent HQ

- **URL:** <https://github.com/features/copilot/agents>
- **Status:** Preview (announced Oct 2025)
- **What it does:** Unified control plane for managing multiple AI coding agents
  from different providers (Anthropic, OpenAI, Google, etc.) within GitHub and VS
  Code. "Mission Control" dashboard for assigning work, tracking progress,
  managing permissions. Custom agents via markdown profiles in `.github/agents/`.
- **Verdict:** ADD. Multi-vendor agent orchestration platform.

### GitHub Agentic Workflows (gh-aw)

- **URL:** <https://github.com/github/gh-aw>
- **Status:** Technical preview (Feb 13, 2026)
- **What it does:** Define repository automation in plain Markdown files, compiled
  into GitHub Actions YAML. Executed by AI coding agents (Copilot CLI, Claude
  Code, or OpenAI Codex) triggered by repo events. Frontmatter defines triggers;
  body contains natural language tasks. Developed by GitHub Next and Microsoft
  Research.
- **Verdict:** ADD. GitHub's latest agentic feature, directly relevant.

---

## Agent Memory & Context

Tools for persisting context across sessions.

### claude-mem

- **URL:** <https://github.com/thedotmack/claude-mem>
- **Stars:** 28,126
- **Status:** Very active (trending Feb 2026)
- **What it does:** Automatically captures everything Claude does during coding
  sessions, compresses it with AI (using Claude's Agent SDK), and injects
  relevant context into future sessions. Solves the "amnesia problem."
- **Relation to CWF:** Complementary. CWF's plan documents serve as a form of
  persistent context, but claude-mem provides automatic, continuous memory.
- **Verdict:** ADD. Very popular, solves a real problem.

### episodic-memory

- **URL:** <https://github.com/obra/episodic-memory>
- **Stars:** 250
- **Status:** Active (part of superpowers ecosystem)
- **What it does:** Semantic search for Claude Code conversations. Remember past
  discussions, decisions, and patterns.
- **Verdict:** KEEP. Useful complementary tool.

### beads

- **URL:** <https://github.com/steveyegge/beads>
- **Stars:** 16,256
- **Status:** Active
- **What it does:** Lightweight memory system using a graph-based issue tracker.
  Git-backed data units providing persistent, structured memory for coding agents.
- **Verdict:** KEEP. Interesting memory architecture.

---

## Configuration & Enhancement Frameworks

### SuperClaude

- **URL:** <https://github.com/SuperClaude-Org/SuperClaude_Framework>
- **Stars:** 20,795
- **Status:** Active (v4.1.9, Jan 2026)
- **What it does:** Configuration framework that enhances Claude Code through
  behavioral instruction injection. Provides specialized slash commands,
  "cognitive personas," and development methodologies via TOML-based command
  definitions and CLAUDE.md configurations. Also available as pip package. Has
  variants for Gemini CLI and Codex.
- **Relation to CWF:** Different philosophy. SuperClaude modifies behavior through
  config injection and persona-switching; CWF uses structured plan documents.
- **Verdict:** KEEP. Notable alternative approach.

### compound-engineering-plugin

- **URL:** <https://github.com/EveryInc/compound-engineering-plugin>
- **Stars:** 8,837
- **Status:** Active (backed by Every.to)
- **What it does:** Includes 29 specialized agents, 23 workflow commands, 18
  skills. Reviews code in parallel with 12 subagents. Also includes a CLI that
  converts Claude Code plugins to OpenCode, Cursor, Codex, etc.
- **Relation to CWF:** Broad "engineering toolkit" rather than focused planning
  workflow. The compound approach (many small agents) differs from CWF's
  plan-document-centric approach.
- **Verdict:** ADD. Broad engineering toolkit, interesting multi-agent review.

---

## Developer Resources & Ecosystem

### superpowers-marketplace

- **URL:** <https://github.com/obra/superpowers-marketplace>
- **Stars:** 485
- **Status:** Very active
- **What it does:** Curated Claude Code plugin marketplace. Currently indexes 7
  plugins with 4 capabilities, 3 commands, 23 agents, and 3 skills.
- **Verdict:** KEEP. Primary third-party plugin marketplace.

### superpowers-developing-for-claude-code

- **URL:** <https://github.com/obra/superpowers-developing-for-claude-code>
- **Stars:** 84
- **Status:** Active (v0.3.1, experimental)
- **What it does:** Meta-development plugin providing skills and 42+ official
  Claude Code documentation files for building plugins, skills, MCP servers, and
  extensions. Includes self-update mechanism.
- **Verdict:** KEEP. Useful for plugin developers.

### awesome-claude-skills

- **URL:** <https://github.com/BehiSecc/awesome-claude-skills>
- **Stars:** 5,827
- **What it does:** Curated list of Claude Skills organized by category.
- **Verdict:** KEEP. Community resource.

### awesome-claude-plugins

- **URL:** <https://github.com/quemsah/awesome-claude-plugins>
- **Stars:** 111
- **Status:** Active, auto-updating (Feb 2026)
- **What it does:** Automated collection of Claude Code plugin adoption metrics
  across GitHub repositories using n8n workflows. 4,961 repositories indexed.
- **Verdict:** ADD. Market intelligence resource.

### Martin Fowler on Spec-Driven Development

- **URL:** <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html>
- **What it does:** Conceptual overview of specification-driven AI development.
- **Verdict:** KEEP. Thought leadership.

---

## Items to DROP from Current README

### claude-code-infrastructure-showcase

- **URL:** <https://github.com/diet103/claude-code-infrastructure-showcase>
- **Stars:** 8,888
- **Reason:** Despite high star count, focused on patterns for auto-activating
  skills rather than workflow planning. Tangential to the workflow focus of this
  section. Consider keeping if a broader "Claude Code Resources" section is
  desired.

### claude-code-prompt-improver

- **URL:** <https://github.com/severity1/claude-code-prompt-improver>
- **Stars:** 1,122
- **Reason:** Tangential to workflow planning. Prompt enhancement is a different
  concern than structured development workflows.

### armchr

- **URL:** <https://github.com/armchr/armchr>
- **Stars:** 22
- **Reason:** Niche tool (commit chunking), very low adoption, tangential to
  workflow planning.

### claude-code-switch

- **URL:** <https://github.com/foreveryh/claude-code-switch>
- **Stars:** 446
- **Reason:** Model switching is tangential to development workflows. Utility
  tool, not a workflow alternative or resource.

### claude-context (zilliztech)

- **URL:** <https://github.com/zilliztech/claude-context>
- **Stars:** 5,333
- **Reason:** MCP plugin for semantic code search. Despite decent star count,
  tangential to workflow planning -- more of a general dev tool. Consider keeping
  in a broader "Claude Code Resources" section.

### sourcegraph-amp

- **URL:** <https://sourcegraph.com/amp>
- **Reason:** Commercial agentic coding platform. Tangential to the open-source
  workflow ecosystem. Can be mentioned if a "Commercial Tools" section is desired.

### claude-orchestration

- **URL:** <https://github.com/mbruhler/claude-orchestration>
- **Reason:** Low adoption. Less distinctive now that Claude Code Agent Teams
  provides first-party multi-agent coordination.

---

## Summary of Changes

### New additions (11):

| Tool | Category | Stars | Why Add |
|---|---|---|---|
| GSD | Plan-driven workflow | 13,925 | Major direct competitor, very popular |
| Deep Trilogy | Plan-driven workflow | 17 | Closest philosophical match to CWF (new project) |
| cc-blueprint-toolkit | Plan-driven workflow | 181 | Blueprint-driven alternative |
| claude-code-spec-workflow | Plan-driven workflow | 3,422 | Relevant spec-first alternative |
| Claude Code Agent Teams | Multi-agent orchestration | Official | First-party Anthropic feature |
| Gas Town | Multi-agent orchestration | 9,351 | Prominent multi-agent workspace manager |
| babysitter | Multi-agent orchestration | 206 | Event-sourced execution framework |
| claude-flow | Multi-agent orchestration | 14,046 | Popular swarm platform |
| CLI Agent Orchestrator | Multi-agent orchestration | 237 | AWS-backed |
| claude-mem | Agent memory | 28,126 | Very popular memory tool |
| compound-engineering-plugin | Enhancement framework | 8,837 | Broad engineering toolkit |

### GitHub platform tools (3, new section):

| Tool | Why Add |
|---|---|
| GitHub Copilot Coding Agent | GA autonomous coding agent |
| GitHub Agent HQ | Multi-vendor agent control plane |
| GitHub Agentic Workflows | Markdown-defined automation (Feb 2026) |

### Removals (7):

| Tool | Reason |
|---|---|
| claude-code-infrastructure-showcase (8,888 stars) | Tangential; consider keeping in broader resources section |
| claude-code-prompt-improver | Tangential to workflows |
| armchr | Niche, unclear adoption |
| claude-code-switch | Tangential utility |
| claude-context (5,333 stars) | Tangential; consider keeping in broader resources section |
| sourcegraph-amp | Commercial, tangential |
| claude-orchestration | Low adoption, superseded by Agent Teams |
