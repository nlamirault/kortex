---
title: Database Models
type: concept
status: draft
confidence: low
cluster: data
domain: [data]
sources: [TMP/KB]
updated: 2025-10-03
tags: [Database]
---

# Models

## 1. **Relational Database (SQL)**

- **Model:** Data stored in **tables (rows & columns)** with relationships between them.
- **Language:** SQL.
- **Strengths:** ACID transactions, strong consistency, mature ecosystem.
- **Examples:** PostgreSQL, MySQL, Oracle, SQL Server.
- **Use cases:** ERP, CRM, e-commerce, accounting.

---

## 2. **Document Database**

- **Model:** Data stored as **documents (JSON, BSON, XML)**, often semi-structured.
- **Strengths:** Flexible schema, good for heterogeneous data.
- **Examples:** MongoDB, Couchbase, ArangoDB.
- **Use cases:** Web apps, product catalogs, user-generated content.

---

## 3. **Key-Value Database**

- **Model:** Simple **key → value** pairs.
- **Strengths:** Extremely fast, low latency, horizontally scalable.
- **Examples:** Redis, DynamoDB, Riak.
- **Use cases:** Caching, user sessions, preference storage.

---

## 4. **Time Series Database (TSDB)**

- **Model:** Optimized for **timestamped data**.
- **Strengths:** High ingestion rate, efficient time-based queries (aggregation, downsampling).
- **Examples:** InfluxDB, TimescaleDB, Prometheus.
- **Use cases:** Observability (metrics, logs, traces), IoT sensors, finance (stock prices).

---

## 5. **Search Engine Database**

- **Model:** **Inverted index** (terms → documents).
- **Strengths:** Full-text search, relevance scoring, typo-tolerance.
- **Examples:** Elasticsearch, OpenSearch, Solr.
- **Use cases:** Search engines, log indexing, product search.

---

## 6. **Vector Database**

- **Model:** Data represented as **embeddings (vectors of numbers)**.
- **Strengths:** Similarity search (cosine, dot product, Euclidean).
- **Examples:** Pinecone, Milvus, Weaviate, pgvector.
- **Use cases:** AI & LLMs (RAG), semantic search, image/audio/video search.

---

## 7. **Graph Database**

- **Model:** **Nodes (entities)** and **edges (relationships)**.
- **Strengths:** Efficient for graph traversal, shortest paths, relationship-heavy queries.
- **Examples:** Neo4j, JanusGraph, Amazon Neptune, ArangoDB.
- **Use cases:** Social networks, fraud detection, knowledge graphs, recommendation engines.

---

## 8. **OLAP Database (Online Analytical Processing)**

- **Model:** Data cubes, multidimensional analytics.
- **Strengths:** Extremely fast for large-scale aggregations.
- **Examples:** ClickHouse, Apache Druid, Snowflake, BigQuery.
- **Use cases:** BI dashboards, reporting, data lakes, analytics.

---

## 9. **Column-Oriented Database**

- **Model:** Data stored **by column instead of row**.
- **Strengths:** Great compression, fast analytical queries on big data.
- **Examples:** Cassandra, HBase, Vertica, Parquet format, ClickHouse.
- **Use cases:** Big Data workloads, analytics, data warehousing.

### 

![ChatGPT Image Oct 3, 2025, 07_52_42 AM.png](Explanation%20Database%20Models/ChatGPT_Image_Oct_3_2025_07_52_42_AM.png)

# Echosystem

![aca6e879-1967-4e5c-8fa4-2798f645e428_1400x900.webp](Explanation%20Database%20Models/aca6e879-1967-4e5c-8fa4-2798f645e428_1400x900.webp)

&

![](https://substackcdn.com/image/fetch/f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1440321e-63dc-4dc7-8db3-27adbf1937ad_4542x3522.png)

[Untitled](Explanation%20Database%20Models/Untitled%20576da0e0bf574cf2a24db00e6c074aa9.csv)
