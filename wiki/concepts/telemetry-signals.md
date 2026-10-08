---
type: concept
title: Telemetry Signals
description: The three primary observability data types — traces, metrics, and logs — plus emerging signals like profiles.
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [telemetry, signals, traces, metrics, logs, observability]
---

# Telemetry Signals

A **telemetry signal** is a category of data a system emits about its own behavior. The
classical "three pillars" of observability are **traces**, **metrics**, and **logs**; each
answers a different question, and their real power is in correlation.

## Core Idea

The three signals are complementary, not redundant:

- **Metrics** are numeric measurements aggregated over time (counters, gauges, histograms).
  They are cheap to store and fast to query, and answer *"is something wrong, and how much?"* —
  e.g. request rate, error rate, p99 latency. They lose per-request detail to aggregation.
- **Traces** capture the path of a single request as it flows across services, as a tree of
  timed **spans**. They answer *"where is the time going, and which hop failed?"* See
  [Distributed Tracing](distributed-tracing.md).
- **Logs** are timestamped records of discrete events, from free-text lines to structured
  key-value events. They answer *"what exactly happened here?"* at a point in time.

The value compounds when signals share context: a metric spike links to exemplar traces, a
span carries its correlated logs via trace and span IDs. OpenTelemetry's long-term direction
is a unified data model where this correlation is built in rather than bolted on
(`NOT VERIFIED` — framing from model recall). **Profiles** (continuous profiling) are an
emerging fourth signal in OTel (`NOT VERIFIED` — stability status from recall; confirm on
ingest).

## Key Properties

- Three classical signals: metrics (aggregated numbers), traces (per-request spans), logs (events).
- Correlated by shared identifiers — trace ID / span ID link logs and traces; exemplars link metrics to traces.
- Different cost/detail trade-offs: metrics cheap + coarse, traces + logs rich + expensive.
- In OpenTelemetry each signal has its own API, SDK, and maturity level, unified under OTLP.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:telemetry-signals]] | part-of | [[domain:observability]] |
| [[concept:telemetry-signals]] | requires | [[concept:instrumentation]] |

## Related

- [Observability](../domains/observability.md)
- [Distributed Tracing](distributed-tracing.md)
- [OpenTelemetry (OTel)](opentelemetry-otel.md)
- [Instrumentation](instrumentation.md)

## Open Questions

- Is the "three pillars" framing outdated — should signals be seen as views over one event stream rather than three separate stores?
- What is the current OTel stability status of logs and profiles relative to traces and metrics?
