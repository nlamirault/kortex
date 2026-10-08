---
type: source
title: "Introducing Dogwood: runtime verification for AI agents"
description: Open-source governance language that enforces temporal (history-aware) rules on AI agent tool calls, extending Cedar with MFOTL operators.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/
    id: dogwood-aws-2026
    title: "Introducing Dogwood (AWS Open Source Blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [governance, policy, agents, runtime-verification, cedar, mcp, aws]
---

# Introducing Dogwood: runtime verification for AI agents

**Auteur :** Marc Brooker, Joseph Tassarotti, Jean-Baptiste Tristan · **Publié :** 2026-08-06 · **Lien :** https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~12 min

## En Bref

Dogwood is an open-source (Apache 2.0) governance language that states which tool calls an AI
agent may make and enforces those rules at the tool-call boundary — the point of highest risk.
Where Cedar decides each authorization in isolation (point-in-time), Dogwood adds **temporal
clauses** that look back over an agent's recent event history, so rules can express
prerequisites, rate limits, ordering, and spending caps. It matters because agent safety lives
at the tool boundary, and sequence-aware rules are exactly what per-request access control
cannot express.

## Points Clés

- **Superset of Cedar:** any syntactically valid Cedar policy is a valid Dogwood policy — no migration needed; deny-by-default and `forbid`-over-`permit` semantics are preserved.[^dogwood]
- **Temporal operators** (`formerly`, `count_within`, `count_distinct_within`, `sum_within`, `bind`) are macros over Metric First-Order Temporal Logic (MFOTL), the formalism from runtime verification.[^dogwood]
- **Events, not isolated requests:** each tool call emits a request + response event (args + principal); rate limits should count *requests* to resist concurrency bypass.[^dogwood]
- **Action schema is generated from the agent's MCP tool manifest** — Dogwood reads the same tool definitions the agent exposes over Model Context Protocol.[^dogwood]
- **Shipping + roadmap:** built into Amazon Bedrock AgentCore Policy today; parser/validator/reference-interpreter released; roadmap adds absolute-time windows, liveness, and multi-agent orchestration. Not yet accepting direct contributions.[^dogwood]

## Citation Notable

> "Dogwood combines the powerful features of MFOTL with Cedar's support for point-in-time authorization." — Brooker, Tassarotti & Tristan

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-dogwood-runtime-verification-2026]] | argues-that | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-dogwood-runtime-verification-2026]] | implements | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-dogwood-runtime-verification-2026]] | extends | [[domain:ai-protocols]] |
| [[source:ai-protocols-dogwood-runtime-verification-2026]] | published-by | [[organization:aws]] |

## Liens Wiki

- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — Dogwood generates its action schema from an agent's MCP tool manifest.
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — Dogwood governs exactly the tool-call boundary this concept describes.
- [AI Protocols](../domains/ai-protocols.md) — adds a governance/policy layer to the agent-protocol stack.
- [Amazon Web Services (AWS)](../organizations/aws.md) — publisher; ships Dogwood in Bedrock AgentCore.

[^dogwood]: AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents", 2026-08-06.
