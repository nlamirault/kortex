---
type: cache
title: Session Hot Cache
description: Read silently at every session start. ~500 words. Current focus, active pages, open threads.
updated: 2026-10-08
---

# Kortex — Session Hot Cache

> Read this silently at every session start. Replaces recap conversation.
> Update at session end via `/session --close`.

---

## Current Focus

Ingested (fiche) the AWS **Dogwood** blog post into the **AI Protocols** domain — an
open-source governance language adding temporal, history-aware rules to agent tool calls
(extends Cedar with MFOTL operators; action schema from MCP manifest). Follow-up entities
(Dogwood, Cedar, AgentCore, MFOTL, runtime-verification, Marc Brooker) parked in
`raw/queue.md` for promotion to full pages on demand.

Prior thread: **Observability** domain seed scaffold (`draft` / `confidence: low`, `NOT
VERIFIED` recall claims) still awaits real OTel-spec ingests.

## Active Pages

- [Dogwood fiche](sources/ai-protocols-dogwood-runtime-verification-2026.md) — latest ingest
- [AI Protocols](domains/ai-protocols.md) — domain hub
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — enriched by the fiche
- [Observability](domains/observability.md) — domain hub (prior thread)

## Open Questions

- Observability: how do the three signals converge toward a unified data model, and what is each signal's current OTel stability?
- Observability: where should telemetry be processed — in-SDK, at a Collector, or at the backend?
- Carried over (AI Protocols): protocol stack composition; ACP vs A2A convergence; x402 vs Agentic Commerce Protocol.

## Recent Decisions

- Seed concepts chosen as the 5 most load-bearing protocol primitives, not an exhaustive list.
- Slug convention: `<long-name>-<acronym>` (e.g. `model-context-protocol-mcp`, `opentelemetry-otel`); `x402` stays bare.
- Observability: OTel **Collector** deferred to `projects/opentelemetry-collector.md` on `/ingest` — it's a binary, a `project` not a `concept`. Do NOT seed it under `concepts/`. Instrumentation took the 5th concept slot instead.

## Last Operations

- 2026-10-08 `[BOOTSTRAP]` — created Observability domain + 5 seed concepts.
- 2026-10-08 `[BOOTSTRAP]` — created AI Protocols domain + 5 seed concepts.
- 2026-10-08 `[INIT]` — completed bundle scaffold (hot.md, overview.md).

## Known Failures

- None.

## Pending Ingests

- None queued. Drop OTel specs/docs/articles (or AI protocol specs) in `raw/` and run `/ingest` to enrich a domain.
