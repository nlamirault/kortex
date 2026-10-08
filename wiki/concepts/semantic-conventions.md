---
type: concept
title: Semantic Conventions
description: Standardized attribute names and values so telemetry is consistent and comparable across services and vendors.
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T13:00:00Z}
verified: []
stale_after: 2027-10-08T00:00:00Z
updated: 2026-10-08
tags: [semantic-conventions, attributes, standardization, interoperability]
---

# Semantic Conventions

**Semantic conventions** are an agreed-upon vocabulary for naming the attributes attached to
telemetry — the keys and value formats that describe HTTP requests, databases, hosts, services,
and more — so that data from different codebases and vendors means the same thing.

## Core Idea

A span attribute is just a key-value pair, and without agreement one service tags
`http.method`, another `httpMethod`, a third `method`. Dashboards, alerts, and queries then
break the moment they cross a service boundary. Semantic conventions fix this by defining
canonical attribute names (e.g. `http.request.method`, `service.name`, `db.system`) and the
required/recommended attributes for each kind of operation, so backends can build generic
visualizations and correlate signals across a whole fleet.

In OpenTelemetry the conventions are a versioned part of the specification, spanning resource
attributes (what produced the telemetry), and per-signal attributes for HTTP, database,
messaging, RPC, and more (`NOT VERIFIED` — current attribute names such as the `http.*`
migration from recall; many were renamed as conventions stabilized, so confirm on ingest).
`service.name` is the one resource attribute conventionally treated as required, since almost
every backend groups telemetry by it. Adhering to conventions is what makes
auto-instrumentation and cross-vendor tooling interoperable rather than bespoke.

## Key Properties

- Define canonical attribute keys and value formats (resource + per-signal: HTTP, DB, messaging, RPC...).
- Versioned alongside the OTel spec; names have evolved as conventions moved to stable.
- Enable generic, portable dashboards/alerts and cross-service correlation.
- `service.name` is effectively mandatory — backends group and route telemetry by it.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:semantic-conventions]] | part-of | [[domain:observability]] |
| [[concept:semantic-conventions]] | enables | [[concept:distributed-tracing]] |

## Related

- [Observability](../domains/observability.md)
- [OpenTelemetry (OTel)](opentelemetry-otel.md)
- [Instrumentation](instrumentation.md)
- [Telemetry Signals](telemetry-signals.md)

## Open Questions

- How do teams handle convention version churn — pinning a version vs tracking stable, and migrating existing dashboards?
- Where do custom, domain-specific attributes belong relative to the standard namespace, and how to avoid collisions?
