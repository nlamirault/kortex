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

Bootstrapping the **Observability** domain — understanding system behavior from telemetry
(traces, metrics, logs), standardized by OpenTelemetry. Seed scaffold just created; concept
pages are `draft` / `confidence: low` and carry `NOT VERIFIED` claims from model recall. Next
step: `/ingest` real OTel specs/docs/articles to replace recall with cited knowledge.

## Active Pages

- [Observability](domains/observability.md) — domain hub
- [Telemetry Signals](concepts/telemetry-signals.md)
- [Distributed Tracing](concepts/distributed-tracing.md)
- [OpenTelemetry (OTel)](concepts/opentelemetry-otel.md)
- [Instrumentation](concepts/instrumentation.md)
- [Semantic Conventions](concepts/semantic-conventions.md)

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
