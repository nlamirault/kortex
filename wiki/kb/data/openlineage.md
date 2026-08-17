---
type: Explanation
title: OpenLineage
description: **OpenLineage** is an **open standard** for collecting metadata about data job executions. It allows you to **track the flow of data** across pipelines — from **source to transformation to destination** — making it easier to understand dependencies, 
tags: ["DataEngineering"]
timestamp: 2025-05-14T08:29:00Z
---

# Overview

**OpenLineage** is an **open standard** for collecting metadata about data job executions. It allows you to **track the flow of data** across pipelines — from **source to transformation to destination** — making it easier to understand dependencies, troubleshoot issues, and ensure compliance.

It is maintained under the **LF AI & Data Foundation** and acts as a **standard protocol** for metadata and lineage interoperability between different data tools like Airflow, Spark, dbt, etc.

Homepage: https://openlineage.io/

![with-ol-24a6cabbc0e0f1e78456b4c5028061ff.svg](Explanation%20OpenLineage/with-ol-24a6cabbc0e0f1e78456b4c5028061ff.svg)

# Architecture

The architecture is built around **three major components**:

1. **Producers**
2. **Transport Layer**
3. **Consumers (Backends)**

Here's a simplified conceptual diagram:

```
+-------------------+       +------------------+       +-------------------+
|    Job Runner     | ----> |  OpenLineage API | ----> | Lineage Backend   |
| (e.g. Airflow)    |       | (Event Transport)|       | (e.g. Marquez)    |
+-------------------+       +------------------+       +-------------------+
         |                          |                          |
         v                          v                          v
     OpenLineage             Events in JSON            Visualization, Audit
     Integration            (via HTTP/Kafka)               Query APIs, etc.

```

## **Producers**

These are the **tools that emit lineage events**. They are integrated into job orchestration or execution engines, such as:

- **Apache Airflow** (via the `openlineage-airflow` plugin)
- **Apache Spark** (via the `openlineage-spark` listener)
- **dbt**
- **Kedro**
- and others.

A producer captures events at key lifecycle moments of a job:

- **START**
- **COMPLETE**
- **FAIL**

The event payload includes metadata like:

- Job name and namespace
- Input/output datasets
- Execution timestamps
- Run IDs
- Contextual parameters (e.g., SQL queries, task IDs)

These are formatted as structured **JSON messages**.

## **Transport Layer**

This is the **communication layer** that delivers lineage events from producers to consumers.

Supported transports include:

- **HTTP API** (default)
- **Kafka** (for scalable, asynchronous delivery)
- Other transports could be implemented as needed.

All messages follow a **standardized JSON schema** defined by the OpenLineage specification. This ensures interoperability across tools and languages.

## **Consumers (Backends)**

These systems **receive and store lineage events** for analysis, display, and integration.

- [**Marquez**](https://github.com/MarquezProject/marquez): the reference open-source backend.
    - Stores lineage metadata
    - Provides a REST API and a UI
    - Supports querying datasets, jobs, and runs
- **Other integrations**:
    - **DataHub**
    - **Amundsen**
    - **Collibra**
    - These tools can ingest OpenLineage events to enhance their data catalogs and governance workflows.

# Object Model

Defines the structure and relationships of the metadata entities used to represent data lineage.

This object model is designed to be **platform-agnostic**, **extensible**, and **machine-readable**, using a JSON schema to describe standardized events emitted by data jobs.

# Next

[Reference: Lineage Object Model](Reference%20Lineage%20Object%20Model%201f31ec0b77e080c98de5c260815885d5.md)
