---
type: organization
title: Amazon Web Services (AWS)
description: Amazon's cloud platform; in this bundle, the publisher of the Dogwood runtime-verification language and home of the Bedrock AgentCore agent-governance stack.
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
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
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

## Relations

| Subject             | Predicate | Object                                                        |
|---------------------|-----------|---------------------------------------------------------------|
| [[organization:aws]] | publishes | [[source:ai-protocols-dogwood-runtime-verification-2026]]     |
| [[organization:aws]] | member-of | [[domain:ai-protocols]]                                       |
| [[organization:aws]] | relates-to | [[concept:model-context-protocol-mcp]]                       |
| [[organization:aws]] | publishes | [[source:ai-protocols-strands-box-sandboxes-2026]]           |

## Related

- [Introducing Dogwood: runtime verification for AI agents](../sources/ai-protocols-dogwood-runtime-verification-2026.md) — the AWS source that anchors this page.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md) — AWS's open sandbox embedding the Dogwood Local Engine.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — AgentCore generates Dogwood policy from an agent's MCP manifest.
- [AI Protocols](../domains/ai-protocols.md) — domain hub this organization belongs to.

## Open Questions

- Beyond Dogwood/AgentCore, which other AWS agent-protocol efforts are worth tracking here?
- Is AgentCore Policy open or AWS-only at runtime, versus the open-source Dogwood parser/interpreter? (Partly answered: Strands Box shows the Dogwood Local Engine running in an open local sandbox, not only in AgentCore — but the AgentCore Policy runtime's openness is still unconfirmed.)

[^dogwood]: AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents", 2026-08-06.
[^strandsbox]: AWS Open Source Blog, "Introducing Strands Box: AI agent sandboxes powered by Dogwood", Fernando Dingler, 2026-10-07.
