---
type: source
title: "AGENTS.md — A simple, open format for guiding coding agents"
description: The AGENTS.md project site — a Markdown file at a repo root giving AI coding agents project context; 60k+ projects, broad tool support, stewarded by AAIF under the Linux Foundation.
format: fiche
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
tags: [agents-md, coding-agents, convention, markdown, aaif]
---

# AGENTS.md — A simple, open format for guiding coding agents

**Éditeur :** agents.md (project site) · **Consulté :** 2026-10-08 · **Lien :** https://agents.md/
**Domaine :** [AI Protocols](../domains/ai-protocols.md)

## En Bref

AGENTS.md is a plain **Markdown file at a repository root** that gives AI coding agents
project-specific context — build/test commands, code style, security notes, PR conventions —
in a dedicated place, so the README stays human-facing. The tagline: *"Think of AGENTS.md as a
README for agents."* Used by **60k+ open-source projects** and stewarded by the **Agentic AI
Foundation (AAIF)** under the Linux Foundation.[^agentsmd]

## Points Clés

- **No required structure:** freeform Markdown; agents read the **nearest** AGENTS.md (closest wins), and explicit chat prompts override it.[^agentsmd]
- **Monorepo-friendly:** nested per-subproject files (the main OpenAI repo reportedly ships 88).[^agentsmd]
- **Broad tool support:** OpenAI Codex, Google Jules, Cursor, Aider, goose, Zed, Warp, VS Code, Devin/Windsurf, JetBrains Junie, Gemini CLI, GitHub Copilot coding agent, and more.[^agentsmd]
- **Origin:** ecosystem collaboration (OpenAI Codex, Amp, Google Jules, Cursor, Factory); presented as an open, non-proprietary format.[^agentsmd]
- **Governance:** "AGENTS.md a Series of LF Projects, LLC" — an AAIF/Linux Foundation project, confirming the AAIF-sibling status noted from the A2A announcement.[^agentsmd]

## Citation Notable

> "Think of AGENTS.md as a README for agents."

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:agents-md-open-format-2026]] | describes | [[concept:agents-md]] |
| [[source:agents-md-open-format-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [AGENTS.md](../concepts/agents-md.md) — the concept this site describes.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — a sibling AAIF project.
- [AI Protocols](../domains/ai-protocols.md) — the cluster.

[^agentsmd]: agents.md, "AGENTS.md — A simple, open format for guiding coding agents", consulted 2026-10-08.
