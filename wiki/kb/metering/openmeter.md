---
type: Explanation
title: OpenMeter
description: **OpenMeter** (https://openmeter.io/) is an open-source project designed to provide a **real-time usage metering** system. It allows teams—especially in SaaS, platform, and infrastructure companies—to **track and bill usage-based pricing models** eff
tags: ["Billing", "Metering"]
timestamp: 2025-04-17T13:50:00Z
---

# **Overview**

**OpenMeter** ([https://openmeter.io/](https://openmeter.io/)) is an open-source project designed to provide a **real-time usage metering** system. It allows teams—especially in SaaS, platform, and infrastructure companies—to **track and bill usage-based pricing models** effectively. It's built to be scalable, event-driven, and developer-friendly.

At its core, OpenMeter:

- Ingests real-time events (e.g., API calls, compute time, storage usage)
- Aggregates them into usage metrics
- Exposes these metrics through APIs for billing or visualization
- Ensures accurate, deduplicated, and auditable data

# 🔧 Architecture Overview

OpenMeter is built on top of **ClickHouse** and **Kafka**, leveraging the **OpenTelemetry** standard to describe usage events.

Here's a breakdown of its major components:

### 1. **Event Ingestion (via Kafka)**

**Purpose:** Collect real-time usage events

- OpenMeter ingests **OpenTelemetry-based usage events** via Kafka.
- Clients or services publish usage data as **spans** or **logs**, enriched with semantic tags (like `user_id`, `resource_type`, etc.).
- Kafka decouples producers from the rest of the system, ensuring scalability and buffering.

### 2. **Transformer / Normalizer**

**Purpose:** Convert incoming events into a normalized format

- The transformer service processes Kafka messages:
    - Filters relevant usage data
    - Normalizes the structure
    - Adds metadata
- It then writes the transformed events into ClickHouse.

### 3. **Storage Layer (ClickHouse)**

**Purpose:** Efficient storage and querying of usage data

- ClickHouse is chosen for its **high-performance columnar storage** and fast time-series queries.
- Events are written as records with:
    - Customer ID
    - Meter name (e.g., `api_calls`, `data_ingress`)
    - Timestamp
    - Quantity
    - Other relevant tags

### 4. **Meter Definitions (via API or config)**

**Purpose:** Define how usage is aggregated

- A “**meter**” is a unit of billing/usage (like GB transferred or number of emails sent).
- Meters are defined with:
    - A name
    - Aggregation method (sum, count, max, etc.)
    - Grouping tags (e.g., by `customer_id`)
- These definitions are stored and managed via OpenMeter’s API.

### 5. **Query API / SDKs**

**Purpose:** Expose usage metrics for billing and dashboards

- Consumers (like billing systems or admin UIs) query usage data via the API.
- The API performs time-bucketed aggregations on raw events stored in ClickHouse.

### 6. **Deduplication and Idempotency**

**Purpose:** Ensure billing accuracy

- Events carry unique IDs to avoid double-counting.
- Deduplication logic is applied during ingestion to maintain accurate metrics.

![download.png](Explanation%20OpenMeter/download.png)

# 💡 Summary of Key Components

| Component | Tech Stack | Role |
| --- | --- | --- |
| Kafka | Apache Kafka | Event buffer and ingestion pipe |
| Transformer | Go/Python/Custom | Parses and normalizes usage data |
| ClickHouse | ClickHouse | Storage and fast aggregation |
| Meter Registry | REST API | Defines meter rules and aggregations |
| Query Service | REST API | Exposes usage metrics for billing |
| Event Format | OpenTelemetry | Standardized schema for usage events |

### 🧑‍💻 Typical Use Case

1. You emit a usage event whenever a user sends a message on your platform.
2. The event is ingested via Kafka, normalized, and stored in ClickHouse.
3. You define a "message_sent" meter with a `count` aggregation grouped by `user_id`.
4. Your billing system queries OpenMeter’s API to bill customers monthly based on usage.

![753ae01d-d375-4b5a-b4a1-ab82b5c55f1f.png](Explanation%20OpenMeter/753ae01d-d375-4b5a-b4a1-ab82b5c55f1f.png)
