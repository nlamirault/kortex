---
type: source
title: "Agentic AI Foundation Announces Four New Projects: Agent Skills, Open Responses, OpenEnv, and OpenSandbox"
description: AAIF press release (AGNTCon + MCPCon NA, 2026-10-22) taking in Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face), and OpenSandbox (Alibaba) — 10 hosted projects in its first year.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects
    id: aaif-four-projects-2026
    title: "Agentic AI Foundation Announces Four New Projects (AAIF News)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-10-27T00:00:00Z}
verified: []
stale_after: 2027-04-27T00:00:00Z
updated: 2026-10-27
tags: [aaif, governance, agent-skills, open-responses, openenv, opensandbox, anthropic, openai, hugging-face, alibaba]
---

# Agentic AI Foundation Announces Four New Projects

**Auteur :** Agentic AI Foundation (press release) · **Publié :** 2026-10-22 · **Lien :** https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

At AGNTCon + MCPCon North America (San Jose), the [Agentic AI Foundation (AAIF)](../organizations/agentic-ai-foundation.md)
took in four vendor-contributed projects — **Agent Skills** (Anthropic), **Open Responses**
(OpenAI), **OpenEnv** (Hugging Face), and **OpenSandbox** (Alibaba) — bringing it to **10 hosted
projects** one year after launching with three. The pattern: each originating vendor hands a
de-facto standard to neutral governance so its roadmap no longer belongs to one company.[^aaif4]

## Points Clés

- **Agent Skills → AAIF (contributed by Anthropic):** "an open format for giving agents new capabilities and domain expertise" — instructions, scripts, and resources loaded on demand, portable across agent products. Anthropic launched it a year earlier and is now donating it.[^aaif4]
- **Open Responses (OpenAI):** open spec for multi-provider LLM interfaces based on the OpenAI Responses API — shared schema, consistent streaming events, extensible tooling.[^aaif4]
- **OpenEnv (Hugging Face):** framework + community hub for interoperable RL environments, run as containerized services exposing MCP and Gym interfaces; committee spans Hugging Face, Microsoft, Meta-PyTorch, Modal, and others.[^aaif4]
- **OpenSandbox (Alibaba):** general-purpose sandbox platform — multi-language SDKs, unified sandbox APIs, Docker and Kubernetes runtimes; its sandbox protocol defines lifecycle + execution APIs extensible with custom runtimes.[^aaif4]
- **Full roster (10):** the four above join Agent2Agent (A2A), Agent Router, agentgateway, AGENTS.md, goose, and MCP; **MCP, goose, and AGENTS.md** are the founding projects. The release gives no project stages/tiers and no member count, and does not mention the Linux Foundation in its text.[^aaif4]

## Citation Notable

> "A year ago, AAIF launched with three projects and a bet that agentic AI needed a neutral home to thrive." — Manik Surtani, CTO and co-founder, AAIF

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-aaif-four-new-projects-2026]] | created-by | [[organization:agentic-ai-foundation]] |
| [[source:ai-protocols-aaif-four-new-projects-2026]] | describes | [[source:ai-protocols-agent-skills-overview-2026]] |
| [[source:ai-protocols-aaif-four-new-projects-2026]] | describes | [[source:ai-protocols-open-responses-2026]] |
| [[source:ai-protocols-aaif-four-new-projects-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Agentic AI Foundation (AAIF)](../organizations/agentic-ai-foundation.md) — the host body; canonical page for its roster and governance.
- [Agent Skills — standardized way to give AI agents new capabilities](ai-protocols-agent-skills-overview-2026.md) — the format itself; this release records its move from Anthropic to AAIF.
- [What Open Responses changes for AI developers](ai-protocols-open-responses-2026.md), [The Sandbox as an Agent Primitive](ai-protocols-opensandbox-agent-primitive-2026.md), [Training agents for real-world tasks with OpenEnv](ai-protocols-openenv-training-agents-2026.md) — the AAIF launch-week deep dives on the other three new projects.
- [A2A joins the Agentic AI Foundation](ai-protocols-a2a-agentic-ai-foundation-2026.md), [AGENTS.md](../concepts/agents-md.md), [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — earlier AAIF projects already in the wiki.

[^aaif4]: Agentic AI Foundation, "Agentic AI Foundation Announces Four New Projects: Agent Skills, Open Responses, OpenEnv, and OpenSandbox", press release, 2026-10-22.
