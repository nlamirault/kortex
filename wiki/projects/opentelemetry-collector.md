---
title: OpenTelemetry Collector
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Logging, Monitoring, Observability, OpenTelemetry, Tracing]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# Description

OpenTelemetry Collector is an open-source, unified agent that collects distributed traces, metrics, and logs using standard formats. It is built by the Cloud Native Computing Foundation (CNCF) as part of the OpenTelemetry project.

Here's a high-level overview of the OpenTelemetry Collector architecture:

- **Collector Configuration**: The OpenTelemetry Collector is configured through YAML files or environment variables. Users define various components such as collectors (metrics, traces, logs), exporters (for sending data to backend services), and other advanced configurations.
- **Receivers**: Receivers listen for incoming data from different sources, such as gRPC endpoints, HTTP APIs, or local files. They can process the received data using adapters, which convert it into OpenTelemetry formats (e.g., traces to the OpenTelemetry trace format).
- **Processors**: Processors apply transformations and modifications to the incoming data based on user-defined configurations. For example, they can remove or add metadata fields, filter data based on specific conditions, and perform aggregations or other customizations.
- **Exporters**: Exporters send collected data to various backend services for long-term storage and visualization. OpenTelemetry Collector supports popular backends like Jaeger, Zipkin, Prometheus, Elasticsearch, and more. Users can configure multiple exporters to forward the same data to different backends for redundancy or load balancing.
- **Metrics**: The metrics collector listens for metric streams using a Prometheus-compatible configuration or gRPC endpoints. Metrics are then processed, transformed, and exported to backend services like Prometheus, InfluxDB, or OpenTelemetry Collector's built-in metrics exporter.
- **Traces**: The traces collector listens for incoming traces through various receivers, such as gRPC endpoints, HTTP APIs, or local files. Traces are then processed using processors and exported to backend services like Jaeger, Zipkin, or OpenTelemetry Collector's built-in trace exporter.
- **Logs**: The logs collector listens for incoming log streams through various receivers, such as gRPC endpoints, HTTP APIs, or local files. Logs are then processed using processors and exported to backend services like Elasticsearch, Loki, or OpenTelemetry Collector's built-in logs exporter.
- **Service Discovery**: OpenTelemetry Collector supports service discovery mechanisms like DNS labels, Kubernetes metadata, and service registration protocols (such as Consul) to dynamically discover and configure collectors, receivers, and exporters in different environments.
- **Integrations**: OpenTelemetry Collector includes integrations with popular frameworks, libraries, and systems like Java, .NET, Python, and gRPC to easily collect distributed traces, metrics, and logs using standard formats.
- **Scalability and Flexibility**: The OpenTelemetry Collector architecture is designed for horizontal scaling, allowing users to deploy multiple collector instances for increased performance and reliability. Users can also customize the collector by adding their own custom processors, receivers, exporters, and integrations as needed.

.png)
