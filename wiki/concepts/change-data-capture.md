---
title: Change Data Capture
type: concept
status: draft
confidence: low
cluster: data
domain: [data]
sources: []
updated: 2025-05-19
tags: [Database]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# **Overview**

**Change Data Capture (CDC)** is a technique used to **track and capture changes (inserts, updates, deletes)** made to a database so that downstream systems can react to those changes in near real-time or batch mode.

Think of it as a way to **stream or sync changes** from a source database to another system (like a data warehouse, analytics platform, or microservices architecture) without needing to constantly re-query the entire table.

### Why Use CDC?

- **Efficient**: Instead of polling the whole table, you get only the delta (changes).
- **Low Latency**: Near real-time replication or event streaming.
- **Data Consistency**: Helps maintain consistent data across systems.
- **Audit Trails**: Track who changed what and when (depending on implementation).
- **Microservices & Event-Driven Systems**: Trigger events when data changes.

# 🛠️ Common CDC Implementation Methods

Each CDC model captures changes in a different way. Here's a breakdown of the main approaches:

| Model | Description | Pros | Cons |
| --- | --- | --- | --- |
| **1. Log-based CDC** | Reads changes directly from the database’s transaction log (binlog, WAL, redo log). | High performance, no impact on DB, captures all changes | Needs DB access to logs, not supported by all DBs |
| **2. Trigger-based CDC** | Uses database triggers to capture changes in audit tables. | Fine-grained control, works with any DB | Adds load to the DB, complex to manage |
| **3. Query-based CDC** | Periodically queries the DB to detect changes (usually by comparing states or using timestamps). | Simple to implement | Inefficient at scale, risk of missing changes |
| **4. Timestamp-based CDC** | Relies on columns like `updated_at` or `created_at` to detect recent changes. | Easy to use if data model supports it | Can miss updates if timestamps aren't updated consistently |
| **5. Hybrid CDC** | Combines two or more approaches (e.g., log-based + timestamp). | More robust and flexible | Added complexity |
| **6. Middleware-based CDC** | Hooks into ORMs or application-level code to track data changes. | Fine-grained control at app level | Not scalable, not DB-independent |

# ⚙️ Use Cases

- Replicating from **OLTP to OLAP** systems (e.g., from PostgreSQL to Snowflake).
- Feeding **event streams** to Kafka or similar brokers.
- Keeping **caches or search indexes (like Elasticsearch)** in sync.
- Maintaining **audit logs**.
- Building **real-time dashboards** or **data lakes**.

## 🔧 Open Source CDC Tools (and Related Platforms)

Here’s a comparison of open-source and community tools you can consider when building a CDC platform:

| Tool | Model | Language | Notes |
| --- | --- | --- | --- |
| **Debezium** | Log-based | Java | Industry-standard, supports MySQL, Postgres, MongoDB, SQL Server, etc. Runs with Kafka Connect but can work standalone |
| **Redpanda Connect** | Log-based (via Kafka Connect interface) | C++ / WASM | Modern Kafka replacement, supports Debezium integration via Redpanda Connect |
| **Olake** ([olake.io](https://olake.io/)) | Likely Hybrid (details limited) | N/A | Provides real-time ingestion into Iceberg/Lakehouse-like storage. Focused on observability and storage integration |
| **Sequin** ([sequinstream.com](https://sequinstream.com/)) | Cloud CDC for SaaS apps | Elixir | Focused on syncing SaaS sources like Stripe, Postgres, etc. into warehouse |
| **Airbyte** | Trigger/Log-based | Java | ETL/ELT platform with CDC capabilities using Debezium or custom connectors |
| **RudderStack** | Hybrid | Go | Primarily analytics/event streaming, supports CDC from Postgres and MySQL |
| **Materialize** | Log-based (via upstream connectors) | Rust | Not a CDC tool itself, but can consume CDC streams and offer SQL views |
| **Estuary** | Log-based (via connectors) | Rust | Connects to databases and SaaS sources, pushes to stream processors or warehouses |
| **PipelineWise** | Query/Timestamp-based | Python | Built on Singer; uses periodic polling for CDC |
| **Arroyo** | Stream Processing | Rust | Not a CDC tool but consumes CDC-style event streams and transforms them |
| **Fluvio** | Transport | Rust | Used as a replacement for Kafka for transport of CDC events |
| **Substrait + Delta/Arrow/Parquet** | Storage | N/A | Not directly CDC, but helpful in processing structured change logs |
