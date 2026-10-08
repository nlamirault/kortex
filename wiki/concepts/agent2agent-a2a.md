---
type: concept
title: Agent2Agent (A2A)
description: Open protocol for interoperability and task delegation between autonomous AI agents across vendors.
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
    id: a2a-aaif-2026
    title: "A New Chapter for A2A (A2A Protocol blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [a2a, agents, interoperability, delegation, governance, aaif]
---

# Agent2Agent (A2A)

Agent2Agent (A2A) is an open protocol enabling autonomous AI agents built by different
vendors or frameworks to discover one another, exchange messages, and delegate tasks.
It was introduced by Google in 2025 (`NOT VERIFIED` — originator and date from model
recall) and, since reaching stable v1.0, moved to vendor-neutral governance as a Growth
Stage project at the **Agentic AI Foundation (AAIF)**, a Linux Foundation-directed body
(sibling projects include MCP, goose, and AGENTS.md).[^a2a-aaif]

## Core Idea

Where MCP connects a single model to its tools, A2A connects *agents to each other*. An
agent publishes an **Agent Card** describing its capabilities and contact methods; other
agents read the card to negotiate modalities and delegate work without manual setup.[^a2a-aaif]
The protocol covers capability discovery, task submission, and streaming of intermediate
results between peer agents.

A2A targets the horizontal interoperability layer: a multi-agent system can be assembled
from agents written in different frameworks, as long as each speaks A2A.

## Key Properties

- Agent-to-agent (peer) rather than model-to-tool communication.
- Capability discovery via a published Agent Card.[^a2a-aaif]
- Task delegation with streamed intermediate results.
- Framework- and vendor-neutral; governed by AAIF (Linux Foundation).[^a2a-aaif]
- Production-adopted: backed by 150+ organizations since stable v1.0; native support in Google Cloud, AWS Bedrock AgentCore Runtime, and Microsoft Azure AI Foundry.[^a2a-aaif]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agent2agent-a2a]] | part-of | [[domain:ai-protocols]] |
| [[concept:agent2agent-a2a]] | contrasts-with | [[concept:model-context-protocol-mcp]] |
| [[concept:agent2agent-a2a]] | described-by | [[source:ai-protocols-a2a-agentic-ai-foundation-2026]] |

## Related

- [AI Protocols](../domains/ai-protocols.md)
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md)
- [Agent Communication Protocol (ACP)](../concepts/agent-communication-protocol-acp.md)
- [A New Chapter for A2A: Joining the Agentic AI Foundation](../sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) — the source for A2A's move to AAIF governance.

## Open Questions

- How do A2A and MCP compose in a single stack — does an agent use MCP internally and A2A externally?
- What is A2A's trust model for delegating sensitive tasks to a third-party agent?
- Who originally authored A2A and when? (origin still `NOT VERIFIED`; the AAIF announcement does not state a prior steward.)

[^a2a-aaif]: A2A Protocol blog, "A New Chapter for A2A: Joining the Agentic AI Foundation", 2026-08-27.
