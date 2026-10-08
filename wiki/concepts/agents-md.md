---
type: concept
title: AGENTS.md
description: A simple, open Markdown format giving AI coding agents project-specific context (build/test commands, conventions) in a dedicated file — "a README for agents." Stewarded by AAIF under the Linux Foundation.
status: stable
confidence: high
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agents.md/
    id: agentsmd-2026
    title: "AGENTS.md — open format for guiding coding agents"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [agents-md, coding-agents, convention, markdown, aaif, linux-foundation]
---

# AGENTS.md

AGENTS.md is **a simple, open format for guiding coding agents**: a plain Markdown file at a
repository root that gives AI coding agents project-specific context and instructions — build
steps, tests, code style, security notes, PR/commit conventions.[^agentsmd] The tagline sums it
up: *"Think of AGENTS.md as a README for agents."*

## Problem

AI coding agents need detailed, project-specific guidance (how to build, test, and follow
conventions). That material clutters a README or is irrelevant to human contributors. AGENTS.md
gives agents a **dedicated, predictable place** for it, keeping the README concise and
human-facing.[^agentsmd]

## Key Properties

- **Plain Markdown at the repo root** — no required fields or headings.[^agentsmd]
- **Typical contents:** build/test commands, code style, testing instructions, security considerations, PR/commit guidelines.[^agentsmd]
- **Nearest-file precedence:** agents read the closest AGENTS.md in the directory tree; explicit user chat prompts override it. Monorepos ship nested per-subproject files (the main OpenAI repo reportedly has 88).[^agentsmd]
- **Complements, doesn't replace, README:** README targets humans; AGENTS.md targets agents.[^agentsmd]
- **Backward compatible:** existing agent-doc files can be renamed to AGENTS.md with a symlink; Aider and Gemini CLI can be configured to load it.[^agentsmd]

## Adoption & Governance

- **Scale:** used by **60k+ open-source projects** per the site.[^agentsmd]
- **Tool support (listed):** OpenAI Codex, Google Jules, Factory, Aider, goose, opencode, Zed, Warp, VS Code, Cognition Devin & Windsurf, UiPath, JetBrains Junie, Amp, Cursor, RooCode, Gemini CLI, Kilo Code, Phoenix, Semgrep, GitHub Copilot coding agent, Ona, Augment Code.[^agentsmd]
- **Origin:** emerged from ecosystem collaboration (OpenAI Codex, Amp, Google Jules, Cursor, Factory).[^agentsmd]
- **Stewardship:** **Agentic AI Foundation (AAIF) under the Linux Foundation** — copyright line reads "AGENTS.md a Series of LF Projects, LLC." This confirms the AAIF-sibling claim noted on the [A2A](agent2agent-a2a.md) page.[^agentsmd]

> **Self-reference:** this knowledge base's own operational schema is an `AGENTS.md` at the repo root — a live instance of the format.[^repo]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agents-md]] | part-of | [[domain:ai-protocols]] |
| [[concept:agents-md]] | described-by | [[source:agents-md-open-format-2026]] |
| [[concept:agents-md]] | relates-to | [[concept:model-context-protocol-mcp]] |

## Related

- [AI Protocols](../domains/ai-protocols.md) — AGENTS.md is the agent-instruction convention in this cluster.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — a sibling AAIF project; MCP connects agents to tools, AGENTS.md tells them how to work in a repo.
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — another AAIF project; A2A's page first surfaced AGENTS.md as an AAIF sibling.
- [AGENTS.md — open format for guiding coding agents](../sources/agents-md-open-format-2026.md) — the source.
- [Agent Skills — standardized way to give AI agents new capabilities](../sources/ai-protocols-agent-skills-overview-2026.md) — portable skill folders (SKILL.md + progressive disclosure); contrasts with per-repo AGENTS.md instructions.

## Open Questions

- Does AGENTS.md define any schema beyond "freeform Markdown," or is the lack of required structure intentional and permanent?
- How do nested-file precedence rules interact when multiple agents with different conventions operate in one monorepo?

[^agentsmd]: agents.md, "AGENTS.md — A simple, open format for guiding coding agents", consulted 2026-10-08.
[^repo]: kortex repository — `AGENTS.md` at the repo root serves as this bundle's operational schema (verifiable in-repo).
