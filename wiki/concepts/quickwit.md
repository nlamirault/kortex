---
title: Quickwit
type: concept
status: active
confidence: high
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Logging, Observability, OpenTelemetry, Tracing]
---

Quickwit is an open-source, distributed search engine designed for large-scale datasets such as logs and events. It is built with a focus on cost-efficiency and is optimized for large-scale indexation and searches.



Here's a high-level overview of its architecture:

- **Storage Layer**: Quickwit is built to work with distributed object storage systems like Amazon S3, Google Cloud Storage, or MinIO. It stores indexes and data in these systems, which allows it to scale horizontally and manage costs effectively.
- **Indexing Pipeline**: Quickwit ingests data from various sources, processes it, and then creates an inverted index. This index is optimized for search performance and is stored in the object storage. Quickwit uses a columnar storage format, which improves query performance and reduces costs by reading only the necessary data.
- **Distributed Architecture**: Quickwit is designed to be distributed from the ground up. It can scale out its indexing and query capabilities across multiple nodes. This is achieved through a combination of stateless services and the use of object storage, which inherently supports high concurrency and distributed access.
- **Search Nodes**: These nodes are responsible for handling search queries. They fetch the necessary index data from object storage, execute the search, and return the results. Search nodes can be scaled independently based on the query load.
- **Indexing Nodes**: These nodes handle the ingestion of new data, building, and updating the indexes. They can also be scaled independently based on the ingestion load.
- **Split Management**: Quickwit introduces the concept of "splits," which are subsets of the index. Splits allow Quickwit to manage and scale the index efficiently. They can be independently created, updated, and distributed across the storage and nodes.
- **Metastore**: The metastore is a component that keeps track of all the metadata related to the indexes, splits, and the overall state of the system. It can be backed by various database systems and is critical for coordinating the distributed operations of Quickwit.
- **Query Language**: Quickwit supports a powerful query language that allows users to perform full-text searches, filter results, and aggregate data. This makes it suitable for complex log analytics use cases.
- **CLI and API**: Quickwit provides a command-line interface (CLI) for managing the system and ingesting data. It also exposes an HTTP API for search queries, which can be integrated with other applications or used by web-based UIs.
- **Streaming and Batching**: Quickwit can ingest data both in real-time (streaming) and in batch mode. This flexibility allows it to handle various types of workloads and use cases.
- **Cost-Efficiency**: The architecture is designed to optimize for cost. By leveraging object storage and a columnar format, Quickwit minimizes the amount of data read during queries, which can significantly reduce costs in cloud environments.

.png)
