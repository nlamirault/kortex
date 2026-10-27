---
type: organization
title: Agentic AI Foundation (AAIF)
description: Vendor-neutral foundation hosting open agentic-AI standards — MCP, goose, AGENTS.md (founding), A2A, Agent Skills, Open Responses, OpenEnv, OpenSandbox, and more; 10 projects after its first year.
resource: https://aaif.io/
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects
    id: aaif-four-projects-2026
    title: "Agentic AI Foundation Announces Four New Projects (AAIF News)"
  - resource: https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
    id: a2a-aaif-2026
    title: "A New Chapter for A2A: Joining the Agentic AI Foundation"
  - resource: https://agents.md/
    id: agentsmd-2026
    title: "AGENTS.md — A simple, open format for guiding coding agents"
generated: {by: anthropic/claude-opus-5-5, at: 2026-10-27T00:00:00Z}
verified: []
stale_after: 2027-04-27T00:00:00Z
updated: 2026-10-27
tags: [aaif, foundation, governance, open-standards, agents, linux-foundation, organization]
---

# Agentic AI Foundation (AAIF)

The Agentic AI Foundation is the **neutral home for open standards, protocols, and
infrastructure in agentic AI**: vendors contribute de-facto standards they originated, and AAIF
governs them through transparent, multi-party governance.[^aaif4] Within this knowledge base it
is the single most recurring steward in the [AI Protocols](../domains/ai-protocols.md) cluster —
most agent-interop specs ingested so far now sit under it.

## Relevance to this bundle

- **Founding projects:** [MCP](../concepts/model-context-protocol-mcp.md), goose, and
  [AGENTS.md](../concepts/agents-md.md); AAIF launched with these three.[^aaif4]
- **Roster after year one (10 projects):** the founders plus [A2A](../concepts/agent2agent-a2a.md),
  Agent Router, agentgateway, and — announced 2026-10-22 at AGNTCon + MCPCon North America —
  [Agent Skills](../sources/ai-protocols-agent-skills-overview-2026.md) (Anthropic),
  [Open Responses](../sources/ai-protocols-open-responses-2026.md) (OpenAI),
  [OpenEnv](../sources/ai-protocols-openenv-training-agents-2026.md) (Hugging Face), and
  [OpenSandbox](../sources/ai-protocols-opensandbox-agent-primitive-2026.md) (Alibaba).[^aaif4]
- **Contribution model:** projects are *contributed by* an originating company and *hosted by*
  AAIF — e.g. Anthropic donated Agent Skills about a year after launching it.[^aaif4] AAIF is the
  steward, not the author.
- **Linux Foundation link:** the A2A announcement calls AAIF "directed by the Linux
  Foundation"[^a2a], and AGENTS.md's copyright reads "a Series of LF Projects, LLC"[^agentsmd].
  The AAIF four-projects release itself does not mention the Linux Foundation in its text.[^aaif4]
- **Project stages:** A2A was accepted as a **Growth Stage** project[^a2a]; the four-projects
  release states no stage for the new projects. Full stage taxonomy `NOT VERIFIED`.
- **Leadership:** Manik Surtani is CTO and co-founder.[^aaif4]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[organization:agentic-ai-foundation]] | publishes | [[source:ai-protocols-aaif-four-new-projects-2026]] |
| [[organization:agentic-ai-foundation]] | relates-to | [[concept:model-context-protocol-mcp]] |
| [[organization:agentic-ai-foundation]] | relates-to | [[concept:agents-md]] |
| [[organization:agentic-ai-foundation]] | relates-to | [[concept:agent2agent-a2a]] |
| [[organization:agentic-ai-foundation]] | member-of | [[domain:ai-protocols]] |

## Related

- [Agentic AI Foundation Announces Four New Projects](../sources/ai-protocols-aaif-four-new-projects-2026.md) — the roster source anchoring this page.
- [A New Chapter for A2A: Joining the Agentic AI Foundation](../sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) — first AAIF source ingested; Growth Stage + Linux Foundation framing.
- [AGENTS.md — open format for guiding coding agents](../sources/agents-md-open-format-2026.md) — founding project; LF Projects copyright line.
- [AI Protocols](../domains/ai-protocols.md) — domain hub this organization belongs to.

## Open Questions

- What is AAIF's exact legal/governance relationship to the Linux Foundation? Two sources imply it; the AAIF release does not state it.
- What are the project stages (A2A is "Growth Stage") and which stage did each new project enter?
- Agent Router and agentgateway are on the roster but not yet in the wiki — what are they?

[^aaif4]: Agentic AI Foundation, "Agentic AI Foundation Announces Four New Projects: Agent Skills, Open Responses, OpenEnv, and OpenSandbox", press release, 2026-10-22.
[^a2a]: A2A Protocol blog, "A New Chapter for A2A: Joining the Agentic AI Foundation", 2026-08-27.
[^agentsmd]: agents.md, "AGENTS.md — A simple, open format for guiding coding agents", consulted 2026-10-08.
