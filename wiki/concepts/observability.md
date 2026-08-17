---
title: Observability
type: concept
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Alerting, Logging, Monitoring, Observability, Tracing]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
.png)

# Logging

Logging involves recording discrete events within a system, such as incoming requests or database accesses. It typically generates high volumes of data. The ELK stack (Elasticsearch, Logstash, Kibana) is commonly used to build log analysis platforms. Implementing standardized logging formats across teams for efficient search in log datasets.

# Tracing

Tracing provides insight into the journey of requests across system components like APIs, load balancers, services, and databases. It is instrumental in identifying performance bottlenecks. OpenTelemetry offers a unified approach for implementing logging, tracing and metrics within a single architecture.

# Metrics

Metrics represent aggregate data points reflecting a system's operational state, including query rates, API responsiveness, and service latencies. This time-series data is collected in databases like InfluxDB and often processed by tools such as Prometheus, which supports querying and alerting based on specific criteria. Visualization and alerting on metrics can be done in platforms like Grafana, which integrates with various alerting mechanisms like email, SMS, or Slack.

.png)


