---
okf_version: "0.2"
---

# Kortex Wiki Index

The catalog of this OKF bundle. Every page is listed once under its entity type, and every
write operation also appends to `## By Date`.

## Meta

- [Schema Reference](schema.md) — copy-paste OKF v0.2 templates for every entity type.
- [Hot Cache](hot.md) — session hot cache; read first at session start.
- [Cluster Overview](overview.md) — top-level navigation across domains.

## Domains

- [AI Protocols](domains/ai-protocols.md) — open standards connecting LLMs and agents to tools, each other, and payment rails.
- [Observability](domains/observability.md) — understanding system behavior from telemetry (traces, metrics, logs), standardized by OpenTelemetry.

## Concepts

- [Tool Use / Function Calling](concepts/tool-use-function-calling.md) — foundational primitive: an LLM invoking external functions.
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — standard for connecting an LLM app to tools, data, and context.
- [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — protocol for discovery and task delegation between agents.
- [Agent Communication Protocol (ACP)](concepts/agent-communication-protocol-acp.md) — REST-based agent-to-agent communication (IBM/BeeAI).
- [x402](concepts/x402.md) — revives HTTP 402 for native machine-to-machine payments.
- [Telemetry Signals](concepts/telemetry-signals.md) — the three observability data types: traces, metrics, logs.
- [Distributed Tracing](concepts/distributed-tracing.md) — following one request across services via spans and context propagation.
- [OpenTelemetry (OTel)](concepts/opentelemetry-otel.md) — vendor-neutral standard and OTLP wire format for telemetry.
- [Instrumentation](concepts/instrumentation.md) — making code emit telemetry: API/SDK split, auto vs manual.
- [Semantic Conventions](concepts/semantic-conventions.md) — standardized attribute names so telemetry is comparable across services.

## Sources

## People

## Projects

## Organizations

## Decisions

## Comparisons

## Syntheses

## Patterns

## Gaps

## By Date

### 2026-10-08

- [Observability](domains/observability.md), [Telemetry Signals](concepts/telemetry-signals.md), [Distributed Tracing](concepts/distributed-tracing.md), [OpenTelemetry (OTel)](concepts/opentelemetry-otel.md), [Instrumentation](concepts/instrumentation.md), [Semantic Conventions](concepts/semantic-conventions.md) — `[BOOTSTRAP]`
- [AI Protocols](domains/ai-protocols.md), [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [Agent2Agent (A2A)](concepts/agent2agent-a2a.md), [Agent Communication Protocol (ACP)](concepts/agent-communication-protocol-acp.md), [x402](concepts/x402.md) — `[BOOTSTRAP]`
- [Hot Cache](hot.md), [Cluster Overview](overview.md) — `[INIT]`
- [Schema Reference](schema.md) — `[INIT]`
