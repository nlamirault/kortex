---
type: source
title: "Agent Plugins — portable package format for skills and MCP servers (spec site)"
description: The agent-plugins.org home — Agent Plugins 1.0.0 as an open vendor-neutral packaging standard (plugin.json + skills/ + mcp.json + reverse-domain extensions) for portable Agent Skills and MCP servers.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agent-plugins.org/
    id: agent-plugins-spec-2026
    title: "Agent Plugins (agent-plugins.org)"
generated: {by: opencode/muse-spark-1.3-free, at: 2026-10-09T12:00:00Z}
verified: []
stale_after: 2027-04-09T00:00:00Z
updated: 2026-10-09
tags: [agent-plugins, packaging, agent-skills, mcp, interoperability, plugin-format]
---

# Agent Plugins — portable package format for skills and MCP servers (spec site)

**Éditeur :** agent-plugins.org (spec site) · **Consulté :** 2026-10-09 · **Lien :** https://agent-plugins.org/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

Agent Plugins 1.0.0 is an **open, vendor-neutral packaging standard** for bundling reusable
agent components — **Agent Skills** and **MCP servers** — into one portable plugin directory.
It fixes per-client wrapper fragmentation (same components, rearranged per client) by defining
a small **interoperability floor**: a required `plugin.json` manifest plus fixed locations
(`skills/`, `mcp.json`), with distribution, installation, permissions, UX, and
client-specific capabilities deliberately left to each client.[^spec]

## Points Clés

- **Portable package layout:** a plugin is a directory — required `plugin.json` (plugin identity + target spec version) plus optional components at fixed paths: `skills/` (Agent Skills per the Agent Skills spec), `mcp.json` (stdio, Streamable HTTP, or legacy HTTP+SSE servers), and reverse-domain extension namespaces (e.g. `com.example.client/hooks/`) for client-owned behavior.[^spec]
- **Problem framed as wrapper drift:** clients invented their own plugin formats around identical underlying components, forcing authors to rearrange or duplicate packages per client; the spec standardizes only the portable core.[^spec]
- **Explicit scope floor:** shared components get one predictable structure; distribution, installation, permissions, user experience, and client-specific capabilities stay under each client's control.[^spec]
- **Extension escape hatch:** reverse-domain namespaces let individual clients add behavior without changing the portable core; clients that don't recognize a namespace ignore it.[^spec]
- **Open governance:** openly licensed, developed in public; initial Technical Steering Committee of Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel; proposals via GitHub Discussions, sync via Discord; spec/schemas/governance in the `agentplugins/agent-plugins-spec` repo.[^spec]

## Citation Notable

> "Agent Plugins defines a small interoperability floor for the parts that can be portable across clients." — agent-plugins.org

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-agent-plugins-spec-2026]] | extends | [[source:ai-protocols-agent-skills-overview-2026]] |
| [[source:ai-protocols-agent-plugins-spec-2026]] | implements | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-agent-plugins-spec-2026]] | enables | [[concept:tool-use-function-calling]] |

## Liens Wiki

- [Agent Skills fiche](../sources/ai-protocols-agent-skills-overview-2026.md) — the Skills format this spec packages (`skills/` follows the Agent Skills specification).
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — the server format this spec packages (`mcp.json` declares MCP servers).
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — packaged skills/scripts/servers ultimately drive tool calls.
- [AGENTS.md](../concepts/agents-md.md) — sibling packaging-vs-instruction contrast: portable plugin core vs per-repo/per-client behavior.
- [AI Protocols](../domains/ai-protocols.md) — the cluster.

[^spec]: agent-plugins.org, "Agent Plugins", consulted 2026-10-09.
