---
title: GreptimeDB
type: concept
status: draft
confidence: low
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-10-27
tags: [Database, OpenTelemetry]
---

# Architecture Overview

At a high level, GreptimeDB is built as a **modular, horizontally scalable system** with three primary components:

![architecture-3-463d7251dfecb83ef0e89587643952e0.png](Explanation%20GreptimeDB/architecture-3-463d7251dfecb83ef0e89587643952e0.png)

## **Frontend (SQL & API Layer)**

- **Responsibilities**:
    - Accepts client requests: SQL queries, PromQL, OpenTSDB, InfluxDB, or custom APIs.
    - Parses and optimizes queries.
    - Plans distributed execution (via logical & physical plans).
    - Acts as a stateless gateway; it routes queries and writes to the appropriate backend nodes.
- **Interfaces**:
    - SQL (PostgreSQL wire protocol)
    - PromQL (compatible with Prometheus queries)
    - HTTP/GRPC APIs for data ingestion

## **Datanode (Storage + Compute)**

- **Responsibilities**:
    - Performs actual **query execution** and **data ingestion**.
    - Stores data locally in **columnar formats** optimized for TSDB workloads.
    - Implements a **write buffer**, **compaction**, and **flush to disk/S3**.
    - Can run standalone (for local/dev environments) or participate in distributed clusters.
- **Storage Engines**:
    - **Mito**: GreptimeDB's default column-oriented storage engine.
        - Inspired by Apache Parquet & OLAP stores.
        - Optimized for high-throughput writes and compression.
    - Supports **write-ahead logging (WAL)**, **memtables**, and **levelled compaction**.

## **Metasrv (Metadata Service & Coordinator)**

- **Responsibilities**:
    - Maintains **cluster metadata**:
        - Table schemas
        - Region assignments (sharding)
        - Node membership and heartbeats
    - Acts as a **scheduler and coordinator**:
        - Decides where tables and shards (“regions”) live
        - Coordinates cluster rebalance and fault recovery
- **Backed by**:
    - Etcd: Default for production clusters (HA, CP)
    - MySQL: Lightweight alternative for metadata
    - PostgreSQL: Same as above, with more advanced features
    - In memory: Dev/testing only; not persistent

# Core Concepts

### 🔹 **Regions** (Shards)

- Data in GreptimeDB is partitioned into **regions** by time-series key.
- Each region is a horizontal shard—processed and stored independently.
- Regions are distributed across `Datanodes` to ensure scalability.

### 🔹 **Tables and Schemas**

- Each time series is mapped to a logical table with schema:
    - **Timestamp column** (`ts`)
    - **Tag columns** (label dimensions like `host`, `service`)
    - **Field columns** (metrics like `cpu`, `memory`, etc.)

### 🔹 **Ingestion Paths**

GreptimeDB supports ingestion via:

- **OpenTelemetry OTLP** (for metrics)
- **Prometheus remote_write**
- **Telegraf, Vector, or FluentBit**
- **Custom clients using HTTP/gRPC**
