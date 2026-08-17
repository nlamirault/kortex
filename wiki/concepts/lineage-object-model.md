---
title: Lineage Object Model
type: concept
status: active
confidence: high
cluster: data
domain: [data]
sources: []
updated: 2025-09-01
tags: [DataEngineering]
---

# **Run**

A **Run** represents a **single execution instance** of a job. It is uniquely identified by a `runId` (typically a UUID).

```json
"run": {
  "runId": "abc123",
  "facets": { ... }
```

- `runId`: Unique identifier for that specific run.
- `facets`: Additional metadata (e.g., parent run, nominal time range).

The **Run** is what links together all the metadata for a specific execution — input/output datasets, start/end times, errors, etc.

# **Job**

A **Job** is a logical process that produces or transforms data — like a DAG or task in Airflow or a model in dbt.

```json
"job": {
  "namespace": "airflow",
  "name": "my_etl_job",
  "facets": { ... }
}
```

- `namespace`: Groups jobs by platform or domain (e.g., `airflow`, `dbt`, `spark`)
- `name`: Unique name within the namespace (often DAG/task ID)
- `facets`: Metadata like source code location, version, ownership

# **Dataset**

A **Dataset** is any **data asset** (source or sink) used or produced by a job. Examples: a table in Snowflake, a file in S3, a Kafka topic.

```json
"inputs": [
  {
    "namespace": "s3",
    "name": "s3://my-bucket/data.csv",
    "facets": { ... }
  }
]
```

- `namespace`: System context (e.g., `s3`, `postgres`, `bigquery`)
- `name`: Fully qualified path to the data
- `facets`: Schema, schema version, lifecycle info, etc.

Datasets are either **inputs** or **outputs** in each event.

# **Event**

An **Event** captures a **moment in the lifecycle of a Run**, such as when it starts, completes, or fails.

```json
{
  "eventType": "START",
  "eventTime": "2025-05-14T12:00:00Z",
  "run": { ... },
  "job": { ... },
  "inputs": [ ... ],
  "outputs": [ ... ],
  "producer": "https://github.com/OpenLineage/OpenLineage",
  "facets": { ... }
}

```

- `eventType`: `START`, `COMPLETE`, `FAIL`
- `eventTime`: ISO 8601 timestamp
- `run`, `job`: Refer to the objects above
- `inputs`, `outputs`: Dataset arrays
- `producer`: Identifier for the library/plugin that generated the event
- `facets`: Top-level metadata (e.g., `parentRun`, `externalQuery`, etc.)

# **Facet**

**Facets** are **extensible metadata blobs** attached to any entity (`Run`, `Job`, `Dataset`, or the Event itself). They allow custom or extended info while keeping the model flexible.

### Examples of standard facets:

- `sql`: The SQL query that produced the dataset
- `schema`: Column-level schema of a dataset
- `parentRun`: Parent/child relationship for nested jobs
- `sourceCodeLocation`: URL to source code
- `dataQualityMetrics`: Row counts, null counts, etc.

You can also define **custom facets**, making the model extremely adaptable.

# 🧬 Object Relationships

Here's how the entities relate:

```
        +---------------------+
        |      Job            |
        | (namespace + name)  |
        +----------+----------+
                   |
                   | 1:N
                   v
        +---------------------+
        |       Run           |
        |     (runId)         |
        +----------+----------+
                   |
       +-----------+-----------+
       |                       |
       v                       v
+------------+         +---------------+
|  Inputs    |         |   Outputs     |
| Datasets[] |         |  Datasets[]   |
+------------+         +---------------+
```

Each **Event** binds together a Run, its Job, the Datasets (input/output), and the execution metadata via Facets.

# 📘 Summary Table

| Entity | Purpose | Key Properties |
| --- | --- | --- |
| `Run` | One execution of a job | `runId`, `facets` |
| `Job` | Logical job definition | `namespace`, `name`, `facets` |
| `Dataset` | Data asset (input/output) | `namespace`, `name`, `facets` |
| `Event` | Lifecycle event of a run | `eventType`, `eventTime`, `run`, `job`, `inputs`, `outputs` |
| `Facet` | Extensible metadata | Depends on the type (job/schema/etc) |
