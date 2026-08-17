---
title: Prometheus
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Monitoring, Observability, OpenTelemetry]
---

# Description

Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. It has a multi-dimensional data model with time series data identified by metric name and key/value pairs. Prometheus is widely used for its powerful querying language (PromQL), efficient storage, and its integration with the Grafana visualization tool.

Here is an overview of its architecture:

- **Prometheus Server**: The core component that scrapes and stores time series data. The server is responsible for retrieving metrics from configured targets at given intervals, evaluating rule expressions, recording new time series from existing data, and triggering alerts if certain conditions are met.
- **Targets**: These are the endpoints that Prometheus monitors. Targets can be anything that exposes metrics in the format that Prometheus expects. This often includes services with instrumentation implemented using Prometheus client libraries.
- **Service Discovery**: Prometheus supports various service discovery mechanisms to dynamically discover targets in different environments like Kubernetes, EC2, Consul, etc.
- **Storage**: Prometheus stores time series data on local disk in a custom, highly efficient time series database format. It handles the compaction and retention of data.
- **PromQL (Prometheus Query Language)**: Prometheus provides a functional query language called PromQL that lets the user select and aggregate time series data in real-time.
- **Alertmanager**: While not part of the core Prometheus server, Alertmanager handles alerts sent by the Prometheus server. It takes care of deduplication, grouping, and routing them to the correct receiver integration such as email, PagerDuty, or OpsGenie. It also manages silencing and inhibition of alerts.
- **Exporters**: For services that do not natively expose Prometheus metrics, exporters can be used. Exporters are sidecar applications that translate metrics from third-party systems into a format that Prometheus can scrape.
- **Push Gateway**: For supporting short-lived jobs that cannot be scraped, Prometheus provides the Push Gateway. Jobs can push their metrics to the Push Gateway, from which Prometheus can scrape.
- **Client Libraries**: Prometheus has a set of client libraries that you can use to instrument your code and expose internal metrics.
- **Visualization and Tools**: While Prometheus has a built-in expression browser for running PromQL queries and visualizing results, it is commonly used with external tools like Grafana for more sophisticated dashboards. There are also various other community-contributed tools and integrations that extend Prometheus's functionality.
- **HTTP API**: Prometheus provides a rich HTTP API to enable automated access from external systems to the time series data and to various aspects of the Prometheus server, such as the alerting rules.

.png)
