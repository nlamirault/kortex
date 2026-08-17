---
title: Loki
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Logging, Observability, OpenTelemetry]
---

# Description

Grafana Loki is a horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It is designed to be very cost-effective and easy to operate, as it does not index the contents of the logs, but rather a set of labels for each log stream.

.png)

The central component of the architecture, the Loki server, is responsible for storing logs and processing queries. It consists of several key components:

- **Distributor**: The distributor service is responsible for handling incoming log data from agents like Grafana Agent. It's responsible for validating the data and then evenly distributing it across the ingesters.
- **Ingester**: The ingester service batches incoming log data in memory and eventually flushes it to the backend storage. The ingester also handles queries for recent data that is still in memory.
- **Querier**: The querier service handles queries from users. It fetches the log data from both the ingesters (for recent data) and the storage backend (for older data), merges them, and returns the final results.
- **Query Frontend**: an optional service to improve the speed of Querier work: data requests first go to Query Frontend, which breaks large queries into smaller ones and creates a queue of queries, and Querier takes requests from this queue for processing. In addition, the Query Frontend can perform caching of responses, and parts of queries are processed from its cache instead of executing this query on a worker, i.e. Querier
- **Query Scheduler**: an optional service to improve the scaling of Querier and Query Frontend, which takes over the formation of a queue of queries and forwards them to several Query Frontends
- **Index Store**: Loki uses an index store to keep track of the metadata (labels) associated with the log streams. This can be a NoSQL database like DynamoDB or Cassandra or a key-value store like BoltDB.
- **Chunk Store**: The chunk store is where the compressed log data is stored. Loki can use various backends for chunk storage, such as Amazon S3, Google Cloud Storage, or a filesystem.
- **Ruler**: The ruler component is responsible for evaluating alerting and recording rules. It can push alerts to an Alertmanager and create new log streams from existing data based on the recording rules.
- **Compactor**: responsible for compression of index files and [retention](https://grafana.com/docs/loki/latest/operations/storage/retention/) of data in a long-term storage
- **Gateway**: just an Nginx service that is responsible for routing requests to the appropriate Loki services
