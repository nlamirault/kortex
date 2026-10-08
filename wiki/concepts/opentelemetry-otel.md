---
type: concept
title: OpenTelemetry (OTel)
description: Vendor-neutral CNCF standard and wire format (OTLP) for generating, collecting, and exporting telemetry.
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [opentelemetry, otlp, cncf, standard, instrumentation]
---

# OpenTelemetry (OTel)

**OpenTelemetry (OTel)** is a vendor-neutral, open-source observability framework and
specification that standardizes how applications generate, collect, and export telemetry —
traces, metrics, and logs — so instrumentation is written once and works with any compliant
backend.

## Core Idea

OTel decouples instrumentation from the observability vendor. It defines, per language, a
cross-cutting **API** (stable surface that library authors instrument against) and an **SDK**
(the configurable implementation that samples, batches, and exports), plus **OTLP** — the
OpenTelemetry Protocol — a single gRPC/HTTP wire format for shipping all three signals. A
backend that speaks OTLP can receive data from any OTel-instrumented service without bespoke
agents.

OTel was formed in 2019 from the merger of the **OpenTracing** and **OpenCensus** projects,
which had split the field (`NOT VERIFIED` — merger and date from model recall). It is a
Cloud Native Computing Foundation (CNCF) project and one of its most active (`NOT VERIFIED` —
exact CNCF maturity level, e.g. incubating vs graduated, from recall; confirm on ingest).
Signals matured at different rates — tracing stabilized first, then metrics, then logs
(`NOT VERIFIED` — per-signal stability status from recall). The ecosystem also ships the
**Collector** (a standalone receive/process/export pipeline), **semantic conventions**, and
auto-instrumentation agents.

## Key Properties

- Separates a stable **API** (for instrumentation) from a configurable **SDK** (for processing/export).
- **OTLP** is the native wire format carrying traces, metrics, and logs over gRPC or HTTP.
- Vendor- and backend-neutral — the explicit goal is to avoid lock-in to any one observability vendor.
- CNCF-governed; ecosystem includes the Collector, semantic conventions, and auto-instrumentation.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:opentelemetry-otel]] | part-of | [[domain:observability]] |
| [[concept:opentelemetry-otel]] | implements | [[concept:telemetry-signals]] |
| [[concept:opentelemetry-otel]] | implements | [[concept:distributed-tracing]] |
| [[concept:opentelemetry-otel]] | enables | [[concept:instrumentation]] |
| [[concept:opentelemetry-otel]] | requires | [[concept:semantic-conventions]] |

## Related

- [Observability](../domains/observability.md)
- [Telemetry Signals](telemetry-signals.md)
- [Instrumentation](instrumentation.md)
- [Semantic Conventions](semantic-conventions.md)

## Open Questions

- What is OTel's current CNCF maturity level and the production-stability status of each signal?
- How does the OTel Collector fit relative to in-SDK processing — when is a Collector hop worth the extra infrastructure?
