---
title: Keda
type: project
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Architecture, Autoscaling]
---

# **What is KEDA?**

KEDA (Kubernetes Event-Driven Autoscaling) is an open-source project that enables event-driven scaling in Kubernetes. It extends Kubernetes' native **Horizontal Pod Autoscaler (HPA)** to allow applications to scale **based on external event sources** (e.g., message queues, databases, cloud services).

While Kubernetes' default autoscaling relies on **CPU & memory** usage, KEDA allows scaling based on **custom metrics** derived from external events, making it particularly useful for serverless workloads and event-driven architectures.

# **Architecture & Components**

KEDA consists of two main components:

## **KEDA Agent (Metrics Adapter)**

- Runs as a **Custom Metrics API server** inside Kubernetes.
- Translates external event source metrics into Kubernetes-readable metrics.
- Works alongside Kubernetes’ **Horizontal Pod Autoscaler (HPA)** to determine when to scale up/down pods.
- Enables HPA to access custom metrics from external event sources (e.g., Azure Service Bus, Kafka, AWS SQS).

## **KEDA Controller (Scaler & HPA Manager)**

- Watches for **Scalers** configured in **ScaledObjects** or **ScaledJobs** CRDs (Custom Resources).
- Dynamically activates or deactivates deployments based on external event metrics.
- Ensures that pods scale **only when needed**, reducing resource wastage.
- Manages **event-driven autoscaling policies** defined in Kubernetes.

# **Workflow – How It Works**

1. **User Defines a ScaledObject/ScaledJob**
    - Specifies the deployment/job to scale and the event source (e.g., RabbitMQ, Kafka).
2. **KEDA Monitors the External Event Source**
    - Uses scalers (pre-built or custom) to check event data (e.g., number of messages in a queue).
3. **KEDA Exposes Metrics to Kubernetes HPA**
    - Converts external event data into Kubernetes-readable metrics.
4. **HPA Triggers Scaling Based on Metrics**
    - Increases or decreases replicas dynamically.
5. **Pods Scale to Match Demand**
    - When there are no events, pods scale down to the minimum replica count set.

# Next

[Reference: Keda CRDs](../concepts/keda-crds.md)
