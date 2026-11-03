---
type: organization
title: Amazon Web Services (AWS)
description: Amazon's cloud platform; in this bundle, the publisher of the Dogwood runtime-verification language, home of the Bedrock AgentCore agent-governance stack and AWS Agent Registry (preview), and an ARD Oversight Board member.
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/
    id: dogwood-aws-2026
    title: "Introducing Dogwood (AWS Open Source Blog)"
  - resource: https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/
    id: strands-box-aws-2026
    title: "Introducing Strands Box (AWS Open Source Blog)"
  - resource: https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
    id: ard-aws-2026
    title: "Agentic Resource Discovery (ARD): An open specification for agent discovery (AWS blog)"
  - resource: https://agenticresourcediscovery.org/governance/
    id: ard-governance
    title: "ARD Governance (Oversight Board membership)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-11-03
tags: [aws, amazon, cloud, agents, governance, bedrock, organization]
---

# Amazon Web Services (AWS)

Amazon's cloud computing division. Within this knowledge base AWS matters as an
**AI-agent infrastructure vendor**: it ships agent-governance tooling and publishes the
research behind it on the AWS Open Source Blog. AWS-the-company's broader cloud business
is out of scope here — pages are added only for material actually ingested into the wiki.

## Relevance to this bundle

- **Publisher of Dogwood** — the open-source (Apache 2.0) runtime-verification language
  for AI agents, released via the AWS Open Source Blog in August 2026.[^dogwood]
- **Bedrock AgentCore** — Dogwood is built into Amazon Bedrock AgentCore Policy today; AWS
  is shipping agent tool-call governance as a managed capability, not just a paper.[^dogwood]
- **MCP-aware** — AgentCore reads an agent's Model Context Protocol tool manifest to
  generate Dogwood's action schema, so AWS's governance layer sits directly on the
  [MCP](../concepts/model-context-protocol-mcp.md) tool boundary.[^dogwood]
- **Publisher of Strands Box** — an open-source (Apache 2.0, developer preview) AI-agent
  sandbox that embeds the Dogwood Local Engine, pairing OS-level containment (macOS Seatbelt)
  with policy enforced at network, shell, Python, and MCP boundaries. Part of the Strands
  Agents effort.[^strandsbox]
- **AWS Agent Registry (preview)** — a curated, searchable catalog of agents, MCP servers, tools,
  agent skills and custom resources. It has a publisher, curator and consumer approval workflow,
  IAM or corporate-JWT authorization, hybrid search and a remote MCP endpoint. Its product
  owners sit in Amazon Bedrock AgentCore and Route 53. AWS positions the open
  [Agentic Resource Discovery (ARD)](../concepts/agentic-resource-discovery-ard.md) spec as the
  cross-environment interoperability layer above it, but in expected terms ("we expect"). It
  does not claim shipped support and says AWS "contributed feedback" to the spec.[^ard-aws-2026]
  Jeffrey Damick holds Amazon's seat on ARD's Oversight Board.[^ard-governance]

## Relations

| Subject             | Predicate | Object                                                        |
|---------------------|-----------|---------------------------------------------------------------|
| [[organization:aws]] | publishes | [[source:ai-protocols-dogwood-runtime-verification-2026]]     |
| [[organization:aws]] | member-of | [[domain:ai-protocols]]                                       |
| [[organization:aws]] | relates-to | [[concept:model-context-protocol-mcp]]                       |
| [[organization:aws]] | publishes | [[source:ai-protocols-strands-box-sandboxes-2026]]           |
| [[organization:aws]] | publishes | [[source:ai-protocols-ard-aws-agent-registry-2026]]          |

## Related

- [Introducing Dogwood: runtime verification for AI agents](../sources/ai-protocols-dogwood-runtime-verification-2026.md) — the AWS source that anchors this page.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md) — AWS's open sandbox embedding the Dogwood Local Engine.
- [Agentic Resource Discovery (ARD): An open specification for agent discovery](../sources/ai-protocols-ard-aws-agent-registry-2026.md) — AWS Agent Registry (preview) and the case for ARD federation across clouds, on-prem and SaaS.
- [Agentic Resource Discovery (ARD)](../concepts/agentic-resource-discovery-ard.md) — the open discovery spec where AWS holds an Oversight Board seat.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — AgentCore generates Dogwood policy from an agent's MCP manifest.
- [AI Protocols](../domains/ai-protocols.md) — domain hub this organization belongs to.

## Open Questions

- Beyond Dogwood/AgentCore, which other AWS agent-protocol efforts are worth tracking here?
- Is AgentCore Policy open or AWS-only at runtime, versus the open-source Dogwood parser/interpreter? (Partly answered: Strands Box shows the Dogwood Local Engine running in an open local sandbox, not only in AgentCore — but the AgentCore Policy runtime's openness is still unconfirmed.)

[^dogwood]: AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents", 2026-08-06.
[^strandsbox]: AWS Open Source Blog, "Introducing Strands Box: AI agent sandboxes powered by Dogwood", Fernando Dingler, 2026-10-07.
[^ard-aws-2026]: AWS Artificial Intelligence Blog, "Agentic Resource Discovery (ARD): An open specification for agent discovery", Jeffrey Damick, Anubhav Mangal & Bhargav Talluri, 2026-08-24.
[^ard-governance]: agenticresourcediscovery.org/governance/, consulted 2026-11-03.
