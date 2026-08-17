---
title: VictoriaMetrics
type: concept
status: active
confidence: high
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-04-14
tags: [Monitoring, Observability]
---

VictoriaMetrics is an open-source time series database and monitoring system built specifically for Prometheus style time series data

![k8s-stack-overview.png](Explanation%20VictoriaMetrics/k8s-stack-overview.png)

Here's a high-level overview of VictoriaMetrics' architecture:

- **Data Ingestion**: VictoriaMetrics ingests time series data through various receivers, such as the Prometheus storage API or local files. The data is then processed and converted into the VictoriaMetrics' native format, which includes a compressed delta encoding for efficient storage and querying.
- **Sharding**: For large-scale deployments, VictoriaMetrics supports sharding to distribute data across multiple nodes. Each node is responsible for storing and querying a specific subset of the data based on a chosen shard key. This allows for horizontal scalability and high performance.
- **Compression**: VictoriaMetrics compresses time series data using a combination of delta encoding, zstd compression, and other optimizations to minimize storage requirements and reduce network traffic during queries. This results in faster data transfer and lower resource usage.
- **Query Engine**: The VictoriaMetrics query engine uses an inverted index for fast lookups, allowing it to quickly filter time series data based on labels and time ranges. It also supports PromQL-like queries using the VictoriaMetrics PromQL engine, which offers similar functionality as Prometheus but with improved performance due to its optimized storage format and indexing structure.
- **Data Model**: The data model in VictoriaMetrics is inspired by Prometheus and supports label-based time series data, where each time series has a set of key-value labels associated with it. This allows for efficient filtering and querying based on specific label values.
Integration: VictoriaMetrics integrates seamlessly with popular monitoring tools like Grafana and Prometheus, allowing users to easily visualize their time series data in these platforms. It also supports various backends for long-term storage and archival, such as HDFS, S3, or local files.
- **Security**: VictoriaMetrics offers security features like SSL encryption for API requests, access control lists, and other security best practices to ensure the confidentiality and integrity of your time series data.
- **Performance**: VictoriaMetrics is designed with performance in mind, offering fast query responses even when dealing with large datasets. Its optimized storage format, efficient indexing, and support for parallel query processing help it outperform traditional time series databases in many use cases.

Components:

- [vmagent](https://docs.victoriametrics.com/vmagent/) - lightweight agent for receiving metrics via [pull-based](https://docs.victoriametrics.com/vmagent/#how-to-collect-metrics-in-prometheus-format) and [push-based](https://docs.victoriametrics.com/vmagent/#how-to-push-data-to-vmagent) protocols, transforming and sending them to the configured Prometheus-compatible remote storage systems such as VictoriaMetrics.
- [vmalert](https://docs.victoriametrics.com/vmalert/) - a service for processing Prometheus-compatible alerting and recording rules.
- [vmalert-tool](https://docs.victoriametrics.com/vmalert-tool/) - a tool for validating alerting and recording rules.
- [vmauth](https://docs.victoriametrics.com/vmauth/) - authorization proxy and load balancer optimized for VictoriaMetrics products.
- [vmgateway](https://docs.victoriametrics.com/vmgateway/) - auhtorization proxy with per-[tenant](https://docs.victoriametrics.com/cluster-victoriametrics/#multitenancy) rate limiting cababilities.
- [vmctl](https://docs.victoriametrics.com/vmctl/) - a tool for migrating and copying data between different storage systems for metrics.
- [vmbackup](https://docs.victoriametrics.com/vmbackup/), [vmrestore](https://docs.victoriametrics.com/vmrestore/) and [vmbackupmanager](https://docs.victoriametrics.com/vmbackupmanager/) - tools for creating backups and restoring from backups for VictoriaMetrics data.
- `vminsert`, `vmselect` and `vmstorage` - components of [VictoriaMetrics cluster](https://docs.victoriametrics.com/cluster-victoriametrics/)
