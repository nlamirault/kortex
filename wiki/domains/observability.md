---
type: domain
title: Observability
description: Understanding system behavior from telemetry — traces, metrics, and logs — standardized by OpenTelemetry.
status: stable
confidence: high
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [observability, opentelemetry, tracing, metrics, logs, telemetry]
---

# Observability

This domain tracks how engineers understand the internal state of a running system from the
data it emits — rather than from logging into boxes or reproducing failures locally.
"Observability" borrows from control theory: a system is observable when its internal state
can be inferred from its external outputs. In practice that means instrumenting services to
produce **telemetry** — traces, metrics, and logs — and shipping it to backends where it can
be queried, correlated, and alerted on.

The organizing standard for this domain is **OpenTelemetry (OTel)**, a vendor-neutral CNCF
project that unifies the generation, collection, and export of telemetry behind one set of
APIs, SDKs, and wire formats (OTLP). Before OTel the field was fragmented across competing,
incompatible libraries; OTel's bet is that instrumentation should be written once and work
with any backend. This domain is OTel-centric but the concepts (signals, tracing, semantic
conventions) generalize to any observability stack.

A useful mental map: **telemetry signals** are the raw data types (traces, metrics, logs);
**distributed tracing** follows one request across service boundaries; **instrumentation** is
how code is made to emit signals; **semantic conventions** make the emitted data comparable
across services and vendors; and **OpenTelemetry** is the standard that ties all of it
together.

## In This Cluster

- [Telemetry Signals](../concepts/telemetry-signals.md) — the three primary data types (traces, metrics, logs) and how they correlate.
- [Distributed Tracing](../concepts/distributed-tracing.md) — following a single request across services via spans and context propagation.
- [OpenTelemetry (OTel)](../concepts/opentelemetry-otel.md) — vendor-neutral standard and OTLP wire format for telemetry.
- [Instrumentation](../concepts/instrumentation.md) — making code emit telemetry: API vs SDK, automatic vs manual.
- [Semantic Conventions](../concepts/semantic-conventions.md) — standardized attribute names so telemetry is comparable across services.

## Key Sources

None yet — pending first `/ingest` of an OpenTelemetry spec, book, or article into this domain.

## Key People

None yet — pending first `/ingest`.

## Open Questions

- How do the three signals converge — is OTel moving toward a unified data model where logs, spans, and metric exemplars share one context?
- Where should telemetry be processed: in-process in the SDK, at a Collector, or at the backend — and what are the cost/control trade-offs?
- How mature is each signal in OTel today (tracing vs metrics vs logs vs profiling), and which are production-stable?
