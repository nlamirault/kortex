---
type: concept
title: Instrumentation
description: Making code emit telemetry — the API/SDK split and the automatic vs manual spectrum.
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [instrumentation, auto-instrumentation, sdk, api, observability]
---

# Instrumentation

**Instrumentation** is the act of making code emit telemetry — adding the calls (or attaching
the agents) that produce spans, metrics, and logs as the program runs. Without instrumentation
there is no observability data to collect.

## Core Idea

Instrumentation sits on a spectrum from automatic to manual:

- **Automatic (auto-)instrumentation** attaches to known libraries and frameworks — HTTP
  servers, database clients, RPC layers — without code changes, often via a language agent,
  bytecode manipulation, or monkey-patching. It gives broad baseline coverage cheaply but
  knows nothing about domain-specific logic.
- **Manual instrumentation** is code the developer writes against the telemetry API to create
  custom spans, record business metrics, and attach meaningful attributes. It captures what
  matters to the application but costs developer effort.

In OpenTelemetry this maps onto the **API/SDK split**: library authors and app developers call
the stable **API** to emit signals, while the **SDK** (installed by the application) decides
how those signals are sampled, batched, and exported. Code instrumented against the API alone
is a no-op until an SDK is configured — which lets libraries ship instrumentation without
forcing a telemetry dependency on their users (`NOT VERIFIED` — API-no-op behavior from model
recall; confirm on ingest). In practice teams combine auto-instrumentation for breadth with
manual spans for the paths they care about.

## Key Properties

- Spectrum from zero-code auto-instrumentation to hand-written manual spans and metrics.
- Auto gives broad library coverage; manual gives domain-specific, high-value signal.
- OTel's API/SDK split lets instrumentation be a no-op until an SDK is wired in.
- Instrumentation quality bounds observability — you can only query what you emit.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:instrumentation]] | part-of | [[domain:observability]] |
| [[concept:instrumentation]] | enables | [[concept:telemetry-signals]] |
| [[concept:instrumentation]] | enables | [[concept:distributed-tracing]] |
| [[concept:instrumentation]] | requires | [[concept:semantic-conventions]] |

## Related

- [Observability](../domains/observability.md)
- [Telemetry Signals](telemetry-signals.md)
- [OpenTelemetry (OTel)](opentelemetry-otel.md)
- [Semantic Conventions](semantic-conventions.md)

## Open Questions

- Where is the right line between auto and manual instrumentation for a typical service?
- How much runtime overhead does auto-instrumentation add, and when does it become unacceptable?
