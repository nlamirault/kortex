---
type: concept
title: Model Context Protocol (MCP)
description: Open protocol standardizing how LLM applications connect to external tools, data, and context.
status: draft
confidence: low
cluster: ai-protocols
domain: [ai-protocols]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [mcp, tools, context, interoperability]
---

# Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open protocol that standardizes how LLM
applications connect to external tools, data sources, and context. Introduced by
Anthropic in late 2024 (`NOT VERIFIED` — date from model recall), it defines a
client–server architecture where a host application runs MCP clients that connect to
MCP servers exposing resources, tools, and prompts.

## Core Idea

MCP solves the N×M integration problem: without a standard, every LLM application must
build bespoke connectors to every tool or data source. MCP defines one protocol so any
compliant client can talk to any compliant server. This is analogous to how USB-C
standardized device connectivity (`NOT VERIFIED` — framing from model recall).

The protocol separates three primitives a server can expose: **resources** (data the
model can read), **tools** (functions the model can call), and **prompts** (reusable
templates). Transport is typically JSON-RPC over stdio or HTTP (`NOT VERIFIED`).

## Key Properties

- Client–server architecture; a host runs one client per connected server.
- Three server primitives: resources, tools, prompts.
- Transport-agnostic messaging, commonly JSON-RPC (`NOT VERIFIED`).
- Vendor-neutral and open — adopted beyond its originator.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:model-context-protocol-mcp]] | part-of | [[domain:ai-protocols]] |
| [[concept:model-context-protocol-mcp]] | enables | [[concept:tool-use-function-calling]] |
| [[concept:model-context-protocol-mcp]] | contrasts-with | [[concept:agent2agent-a2a]] |

## Related

- [AI Protocols](../domains/ai-protocols.md)
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md)
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md)
- [Introducing Dogwood: runtime verification for AI agents](../sources/ai-protocols-dogwood-runtime-verification-2026.md) — governs MCP tool calls; action schema generated from the MCP tool manifest.
- [Personal Agent Protocol (PAP)](../concepts/personal-agent-protocol-pap.md) — uses MCP + OpenAPI as one of its routes for a personal agent to reach a business.
- [AGENTS.md](../concepts/agents-md.md) — a sibling AAIF project; MCP connects agents to tools, AGENTS.md tells them how to work in a repo.
- [Agent Plugins spec fiche](../sources/ai-protocols-agent-plugins-spec-2026.md) — packages MCP servers via `mcp.json` (explicit transports) alongside Skills in one portable directory.
- [Agent Plugins (Google blog) fiche](../sources/ai-protocols-agent-plugins-google-2026.md) — announces Plugins 1.0.0 + Google as Core Maintainer; independent-failure rule (bad MCP entry skips, skills still load).

## Open Questions

- How does MCP's permission/consent model handle untrusted third-party servers?
- Where is the boundary between MCP (model↔tool) and A2A (agent↔agent) — do they overlap or compose?
