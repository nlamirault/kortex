---
type: concept
title: Agent2Agent (A2A)
description: Open protocol for interoperability and task delegation between autonomous AI agents across vendors.
status: draft
confidence: low
cluster: ai-protocols
domain: [ai-protocols]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [a2a, agents, interoperability, delegation]
---

# Agent2Agent (A2A)

Agent2Agent (A2A) is an open protocol enabling autonomous AI agents built by different
vendors or frameworks to discover one another, exchange messages, and delegate tasks.
It was introduced by Google in 2025 (`NOT VERIFIED` — originator and date from model
recall) and later contributed to a foundation for open governance (`NOT VERIFIED`).

## Core Idea

Where MCP connects a single model to its tools, A2A connects *agents to each other*. An
agent publishes an **Agent Card** describing its capabilities and endpoint; other agents
read the card to decide whether and how to delegate work (`NOT VERIFIED` — "Agent Card"
terminology from model recall). The protocol covers capability discovery, task
submission, and streaming of intermediate results between peer agents.

A2A targets the horizontal interoperability layer: a multi-agent system can be assembled
from agents written in different frameworks, as long as each speaks A2A.

## Key Properties

- Agent-to-agent (peer) rather than model-to-tool communication.
- Capability discovery via a published agent description (`NOT VERIFIED`).
- Task delegation with streamed intermediate results.
- Framework- and vendor-neutral.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agent2agent-a2a]] | part-of | [[domain:ai-protocols]] |
| [[concept:agent2agent-a2a]] | contrasts-with | [[concept:model-context-protocol-mcp]] |

## Related

- [AI Protocols](../domains/ai-protocols.md)
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md)
- [Agent Communication Protocol (ACP)](../concepts/agent-communication-protocol-acp.md)

## Open Questions

- How do A2A and MCP compose in a single stack — does an agent use MCP internally and A2A externally?
- What is A2A's trust model for delegating sensitive tasks to a third-party agent?
