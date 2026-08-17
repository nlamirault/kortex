---
title: OTTL
type: concept
status: active
confidence: high
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-04-28
tags: [Observability, OpenTelemetry]
---

# OpenTelemetry Transform Language

**OTTL** is a **declarative transformation language** created by the OpenTelemetry project.

It lets you define *how* telemetry data (logs, metrics, traces) should be **modified**, **filtered**, **routed**, or **enriched** inside the **OpenTelemetry Collector**.

Think of it like a small, powerful scripting language designed **specifically for telemetry pipelines**, **without** needing to write custom Go processors.

# HighLevel Architecture

Here’s how OTTL fits into the OpenTelemetry Collector pipeline:

```
Receiver → Processor (OTTL Transformations) → Exporter
```

- **Receiver**: Ingests telemetry (e.g., OTLP, Prometheus, FluentBit).
- **Processor**: OTTL applies transformations here.
- **Exporter**: Sends telemetry to your observability backend (e.g., Grafana, Datadog, Splunk).

The most common place to employ OTTL is when you need to filter, enrich, or refine telemetry data through processors. Here are a few notable processors that support OTTL:

- [Transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor): This processor is entirely driven by OTTL, allowing you to perform extensive modifications on incoming traces, metrics, and logs. You can add, remove, or change attributes, calculate new metrics, and even restructure log messages.
- [Filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/filterprocessor): OTTL is used here to define conditions that determine whether specific telemetry data should be dropped or kept.
- [Routing processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/routingprocessor#tech-preview-opentelemetry-transformation-language-statements-as-routing-conditions): OTTL statements act as routing conditions for directing telemetry data to specific exporters based on its content or attributes.
- [Tail sampling processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor): OTTL conditions are used to determine when to sample a trace.

# Components of OTTL

OTTL scripts are made of:

| Component | Description | Example |
| --- | --- | --- |
| **Statements** | The full action to perform | `set(attributes["foo"], "bar") where attributes["env"] == "prod"` |
| **Functions** | Built-in operations like `set`, `delete` | `set()`, `delete_key()`, `replace_match()` |
| **Arguments** | Input to functions (fields, constants, etc.) | `attributes["key"]`, `"value"` |
| **Conditions** | When the function should be applied | `where body == "error"` |
| **Path Expressions** | Navigate telemetry fields | `attributes["http.status_code"]`, `resource.attributes["host.name"]` |

# When You Should Use OTTL

- Enriching telemetry (e.g., adding metadata).
- Cleaning unwanted attributes.
- Normalizing naming conventions.
- Routing data dynamically.
- Lightweight filtering instead of writing new processors.

# Debug

https://github.com/elastic/ottl-playground

# Examples

- https://betterstack.com/community/guides/observability/ottl/
- https://betterstack.com/community/guides/observability/ottl-patterns/
