---
title: Tempo
type: concept
status: active
confidence: high
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Observability, OpenTelemetry, Tracing]
---

# Description

Grafana Tempo is an open-source, high-volume, and minimal-dependency distributed tracing backend. It is designed to be a robust and cost-effective solution for storing and querying massive amounts of trace data.

.png)

Here's an overview of its architecture:

- **Distributed Tracing Data Sources**: These are various services and applications instrumented with distributed tracing libraries (like Jaeger, Zipkin, OpenTelemetry) that send trace data to Tempo.
- **Distributors**: When traces are received, they first hit the distributors. Distributors are responsible for batching and sharding the trace data before it's forwarded to ingesters. They ensure that each trace id ends up at the same ingester.
- **Ingester**: Ingester nodes are the workhorses that process the incoming trace data. They write the trace data to a local WAL (Write-Ahead Log) and then to the backend object store. Ingester nodes also hold the traces in memory until they are flushed to the object store, allowing for quick querying of recent trace data.
- **Querier**: When a user queries for a trace, the query is handled by a querier node. The querier fetches the trace ID's list of blocks from the index and then retrieves the full trace data from the object store.
- **Query Frontend**: An optional component that can be used to accelerate queries. It acts as a reverse proxy for queriers, providing query sharding and parallelization, result caching, and retries.
- **Compactor**: The compactor applies retention policies and compacts traces in the backend object store, reducing storage requirements and optimizing query performance.
- **Backend Object Store**: This is where the actual trace data is stored long-term. Tempo is designed to work with any S3-compatible backend, such as Amazon S3, Google Cloud Storage, or MinIO.
- **Query UI**: Grafana itself can be used to query and visualize traces stored in Tempo. Tempo is integrated with Grafana's Explore feature, which allows users to search for traces by ID and visualize them.
