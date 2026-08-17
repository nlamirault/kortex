---
title: Mimir
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Monitoring, Observability, OpenTelemetry]
---

# Description

Grafana Mimir is an open-source, highly scalable, and operationally simple long-term storage for Prometheus. Mimir provides long-term storage, querying, and horizontal scalability for Prometheus metrics.

.png)

Here's a high-level overview of its architecture:

- **Distributed Hash Table (DHT)**: Mimir uses a DHT to distribute and store index and chunk information across the cluster, ensuring that the data is evenly balanced and can be easily scaled out by adding more nodes.
- **Ingesters**: These components are responsible for handling incoming write requests. They temporarily store the incoming samples in memory and periodically flush them to the long-term storage backend. Mimir's ingesters also handle queries for recent data that has not yet been flushed.
- **Distributors**: Distributors are the initial contact point for write requests. They are responsible for accepting samples from Prometheus, hashing them to ensure consistent distribution, and sending them to the appropriate ingesters.
- **Queriers**: Queriers handle read requests. They fetch data from both ingesters (for recent data) and long-term storage (for historical data), aggregate it, and return the final result to the user.
- **Rulers and Alertmanagers**: These components are responsible for evaluating recording and alerting rules against the data in Mimir, as well as handling alerts and notifications.
- **Long-term Storage**: Mimir supports various backends for long-term storage of metrics, such as Amazon S3, Google Cloud Storage, and other S3-compatible object stores. The data is stored in a compressed and efficient format.
- **Compactors**: The compactors apply various optimizations to the stored data, such as compressing time series and applying retention policies.
- **Store-gateways**: These components provide a caching layer in front of the long-term storage, which helps to reduce latency and improve query performance.
- **Query-frontend**: The query-frontend is an optional component that can be used to improve the performance of read operations. It acts as a caching layer and query scheduler, batching and splitting queries to improve efficiency.
- **Consul or Etcd (optional)**: These are used for service discovery and to store the ring state, which keeps track of the health and status of the various components in the Mimir cluster.

# Architecture

.png)

### **Writing metrics**

- All metrics are initially fed into the ***Distributor***. Its main job is to confirm that the metrics are in proper format and to select the ***Ingester*** to forward them to.
- The data is then submitted to the ***Ingester***. It generates data blocks in its memory (the same blocks we discussed earlier — effectively, the Prometheus blocks).
- Once a block is full, Mimir finalizes it, saves it to disk, and sends it to S3 for long-term storage.
- Once the metrics are written to S3, ***Compactor*** comes into play to optimize the block storage. It merges one-hour blocks into two-hour blocks, and so on.

.png)

### **Reading metrics**

This is where things get a little more complicated.

All the queries end up in the ***Query** **Frontend***. It:

- checks the cache for a ready-made response to the query received and returns it if the data is found;
- if no data is found, the query is forwarded to ***Querier***.

*Querier* retrieves the query from the ***Query Frontend*** and prepares the data required to execute that query. To do so, it requests them first from ***Ingester*** and then from the ***Store Gateway***, which acts as the S3 data gateway.

.png)

### **Store gateway**

The data blocks are stored in S3. When launched, the ***Store Gateway*** downloads the parts of blocks with IDs that match the label sets. This is typically 5–10% of the total data volume.

When a data request comes in:

- ***Store Gateway*** accesses the local label and ID match data to figure out which data should be retrieved from which S3 blocks.
- Next, it pulls the required metrics and submits them to ***Querier***.
- The data reaches the ***Query Frontend***, which performs PromQL calculations and serves the results to the user.
