---
title: Keda CRDs
type: concept
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: []
updated: 2025-07-28
tags: [Architecture, Autoscaling, CRD, Kubernetes]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
stale_after: 2027-08-17
---
# **ScaledObject** (for Deployment Scaling)

- Links an external event source (e.g., Kafka, RabbitMQ, AWS SQS) to a **Deployment**.
- Defines the scaling behavior (e.g., min/max replicas, polling interval).

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: example-scaledobject
spec:
  scaleTargetRef:
    name: my-app-deployment
  minReplicaCount: 1
  maxReplicaCount: 10
  triggers:
  - type: kafka
    metadata:
      bootstrapServers: my-cluster-kafka-bootstrap:9092
      topic: my-topic
      consumerGroup: my-group
```

# **ScaledJob** (for Job Scaling)

- Used for batch or event-driven workloads where **Jobs** (not Deployments) need scaling

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledJob
metadata:
  name: example-scaledjob
spec:
  jobTargetRef:
    template:
      spec:
        containers:
        - name: job-container
          image: my-job-image
  minReplicaCount: 0
  maxReplicaCount: 100
  triggers:
  - type: azure-servicebus
    metadata:
      queueName: my-queue
```
