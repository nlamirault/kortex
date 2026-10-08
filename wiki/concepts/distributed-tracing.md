---
type: concept
title: Distributed Tracing
description: Following a single request across service boundaries as a tree of timed spans linked by propagated context.
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [tracing, spans, context-propagation, distributed-systems]
---

# Distributed Tracing

**Distributed tracing** reconstructs the end-to-end path of a single request as it travels
across multiple services, representing it as a **trace**: a tree of **spans**, where each span
is one timed unit of work (an HTTP handler, a DB query, an RPC call).

## Core Idea

In a microservice architecture a single user action can fan out across dozens of services, so
a per-service log tells you little about *where* a slow or failed request actually went wrong.
Tracing solves this by giving every request a **trace ID** at its entry point and having each
service record a **span** — with a start time, duration, parent span ID, and attributes — all
sharing that trace ID. Reassembled by a backend, the spans form a waterfall showing exactly
which hop was slow or errored.

The mechanism that makes this work across process boundaries is **context propagation**: the
trace ID and parent span ID are injected into outbound request headers (e.g. the W3C
`traceparent` header) and extracted on the receiving side, so the downstream span attaches to
the correct parent (`NOT VERIFIED` — W3C Trace Context detail from model recall). Because
tracing high-volume systems is expensive, **sampling** decides which traces to keep — either
up front (head-based) or after the fact (tail-based).

## Key Properties

- A trace is a DAG/tree of spans sharing one trace ID; each span has duration, parent, and attributes.
- Context propagation carries trace + span IDs across process boundaries, typically via W3C Trace Context headers.
- Sampling (head-based or tail-based) controls cost by keeping only a fraction of traces.
- Spans can carry events and links, and correlate to logs and metrics via the shared trace context.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:distributed-tracing]] | extends | [[concept:telemetry-signals]] |
| [[concept:distributed-tracing]] | part-of | [[domain:observability]] |
| [[concept:distributed-tracing]] | requires | [[concept:instrumentation]] |

## Related

- [Telemetry Signals](telemetry-signals.md)
- [Instrumentation](instrumentation.md)
- [OpenTelemetry (OTel)](opentelemetry-otel.md)
- [Semantic Conventions](semantic-conventions.md)

## Open Questions

- How is sampling best coordinated across services so a trace isn't half-kept (head vs tail trade-offs)?
- How does trace context propagate across async boundaries — message queues, batch jobs, cron?
