---
type: source
title: "A New Chapter for A2A: Joining the Agentic AI Foundation"
description: A2A is accepted as a Growth Stage project at the Linux Foundation-directed Agentic AI Foundation (AAIF), moving the agent-interop protocol to vendor-neutral governance.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
    id: a2a-aaif-2026
    title: "A New Chapter for A2A (A2A Protocol blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [a2a, agents, interoperability, governance, aaif, linux-foundation, mcp]
---

# A New Chapter for A2A: Joining the Agentic AI Foundation

**Auteur :** A2A Protocol team (non signé) · **Publié :** 2026-08-27 · **Lien :** https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~2 min

## En Bref

The Agent2Agent (A2A) protocol has been accepted as a **Growth Stage** project at the
**Agentic AI Foundation (AAIF)**, a body directed by the Linux Foundation. Under AAIF, A2A
becomes a vendor-neutral open standard for how autonomous agents discover one another,
negotiate, and delegate tasks across frameworks. It matters because foundational interop
infrastructure under neutral governance is protected from single-vendor control — the
community, not one company, shapes the roadmap.[^a2a]

## Points Clés

- **Neutral governance:** operating under AAIF (Linux Foundation-directed) shields A2A from single-vendor control; sibling AAIF projects include MCP, goose, and AGENTS.md.[^a2a]
- **Horizontal vs vertical:** A2A handles peer-to-peer agent collaboration; [MCP](../concepts/model-context-protocol-mcp.md) handles vertical integration to internal tools and data — the two are complementary, not competing.[^a2a]
- **Agent cards:** agents publish cards describing capabilities and contact methods, letting other agents read them, negotiate modalities, and delegate work without manual setup.[^a2a]
- **Production adoption:** since stable v1.0, A2A is backed by 150+ organizations and runs in supply chains, financial services, and mobile platforms.[^a2a]
- **Native platform support:** Google Cloud, AWS Bedrock AgentCore Runtime, and Microsoft Azure AI Foundry ship native A2A; ServiceNow, Salesforce, Atlassian, and SAP connect workflows with it; LangGraph, CrewAI, Pydantic AI, AG2, and IBM BeeAI support it.[^a2a]

## Citation Notable

> "Foundational infrastructure must evolve openly and predictably."

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-a2a-agentic-ai-foundation-2026]] | describes | [[concept:agent2agent-a2a]] |
| [[source:ai-protocols-a2a-agentic-ai-foundation-2026]] | contrasts-with | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-a2a-agentic-ai-foundation-2026]] | extends | [[domain:ai-protocols]] |
| [[source:ai-protocols-a2a-agentic-ai-foundation-2026]] | mentions | [[organization:aws]] |

## Liens Wiki

- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — this fiche confirms A2A's move to foundation governance and the Agent Card mechanism.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — the vertical (model↔tools) counterpart to A2A's horizontal (agent↔agent) layer; also an AAIF project.
- [AI Protocols](../domains/ai-protocols.md) — the agent-protocol cluster this governance shift sits in.
- [Amazon Web Services (AWS)](../organizations/aws.md) — AWS Bedrock AgentCore Runtime ships native A2A support.

[^a2a]: A2A Protocol blog, "A New Chapter for A2A: Joining the Agentic AI Foundation", 2026-08-27.
