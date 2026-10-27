---
type: source
title: "What Open Responses changes for AI developers"
description: Open Responses standardizes OpenAI's Responses API shape into a shared spec so developers can target one contract across providers; now stewarded by the Agentic AI Foundation.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aaif.io/blog/what-open-responses-changes-for-ai-developers
    id: open-responses-2026
    title: "What Open Responses changes for AI developers (AAIF blog)"
generated: {by: anthropic/claude-sonnet-5, at: 2026-10-27T00:00:00Z}
verified: []
stale_after: 2027-04-27T00:00:00Z
updated: 2026-10-27
tags: [open-responses, aaif, interoperability, api-spec, agents, model-portability]
---

# What Open Responses changes for AI developers

**Auteur :** Angie Jones · **Publié :** 2026-10-22 · **Lien :** https://aaif.io/blog/what-open-responses-changes-for-ai-developers
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~4 min

## En Bref

**Open Responses** turns OpenAI's Responses API shape into a shared, provider-neutral
specification so developers can swap which model/endpoint answers a request by changing
configuration, not by writing a new adapter. It matters because each provider (OpenAI,
Anthropic, Google) currently formats context, tool descriptions, and results differently,
forcing a maintenance burden per integration; Open Responses now sits under the
**Agentic AI Foundation (AAIF)** for neutral evolution.[^openresp]

## Points Clés

- **Adapter fatigue is the problem:** OpenAI's Responses API, Anthropic's Messages API, and Google's `generateContent` API each shape context, tools, and results differently, so multi-provider support means maintaining a separate adapter per API.[^openresp]
- **Endpoint becomes config, not code:** with Open Responses, switching models/providers is a configuration change; the agent still owns tool execution and permission decisions, not the spec.[^openresp]
- **No model retraining required:** the specification governs the wire-level API contract only — adopting it doesn't change or retrain the underlying model.[^openresp]
- **Extensions keep the core stable:** provider-specific features (e.g. hosted search tools, timing/cache events) ship as namespaced extensions; agents can safely ignore extensions they don't support.[^openresp]
- **Already implemented:** Databricks Model Serving exposes an Open Responses endpoint in front of Claude, Gemini, and open models; Vercel AI Gateway exposes an OpenResponses API too.[^openresp]

## Citation Notable

> "AI developers should be able to support models from multiple providers without writing separate code."

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-open-responses-2026]] | extends | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-open-responses-2026]] | contrasts-with | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-open-responses-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — Open Responses standardizes the tool-description/result contract on top of this primitive, across providers.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — MCP standardizes model↔tool/data connections; Open Responses standardizes the model-provider API contract itself — adjacent but distinct layers.
- [A2A joins the Agentic AI Foundation](ai-protocols-a2a-agentic-ai-foundation-2026.md) — same AAIF governance pattern (vendor-neutral stewardship) now applied to Open Responses.
- [AI Protocols](../domains/ai-protocols.md) — the interop-protocol cluster this spec joins.

[^openresp]: Angie Jones, "What Open Responses changes for AI developers", AAIF blog, 2026-10-22.
