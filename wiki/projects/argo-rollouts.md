---
title: Argo Rollouts
type: project
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: []
updated: 2025-04-14
tags: [Architecture]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
stale_after: 2027-08-17
---
# Overview

**Argo Rollouts** is a Kubernetes controller that provides advanced deployment strategies such as blue-green, canary, and progressive delivery with metric analysis and automated rollbacks.

# **Architecture**

Argo Rollouts extends Kubernetes by adding a new custom resource called `Rollout`, which is an enhanced version of a Kubernetes `Deployment`. It integrates with Kubernetes APIs and other tools such as Prometheus, Datadog, and service meshes like Istio or NGINX for traffic routing.

The architecture consists of the following key components:

## **Argo Rollouts Controller**

- Runs as a Kubernetes deployment.
- Monitors and reconciles `Rollout` resources.
- Interacts with Kubernetes API, Ingress controllers, and service meshes.
- Evaluates metrics to decide progression or rollback.

## **Rollout (CRD)**

- Defines the desired state of the application deployment.
- Supports various deployment strategies (Canary, Blue-Green, etc.).
- Manages ReplicaSets similarly to `Deployment`.

## **Analysis (CRD)**

- Enables automated decision-making based on metrics.
- Defines success and failure conditions for rollouts.
- Supports integrations with monitoring tools (Prometheus, Datadog, New Relic, etc.).

## **Traffic Routing Integrations**

- Supports service meshes (Istio, Linkerd) and ingress controllers (NGINX, ALB) for traffic shifting.
- Enables gradual traffic shifting for canary deployments.

## **Argo Rollouts Kubectl Plugin (`kubectl argo rollouts`)**

- Provides CLI commands to inspect and manage rollouts.
- Offers status checking, promotion, and rollback functionalities.

# **Key Components**

### 1. **Rollout Resource**

- Similar to `Deployment`, but supports advanced strategies.
- Defines the deployment strategy (Canary, Blue-Green, etc.).
- Manages ReplicaSets and their lifecycles.

### 2. **Analysis Template & Runs**

- `AnalysisTemplate`: Defines the metrics and queries for success/failure.
- `AnalysisRun`: Executes an instance of an `AnalysisTemplate`.

### 3. **Traffic Routing Mechanism**

- Uses service mesh (Istio, Linkerd) or ingress controllers (NGINX, ALB) for progressive traffic shifting.

### 4. **Experiments**

- Allows testing different versions of an application simultaneously.
- Runs multiple ReplicaSets with different configurations.

### 5. **Metric Providers**

- Integrates with Prometheus, Datadog, New Relic, and other observability tools.
- Provides real-time metric evaluation for rollouts.

# **Deployment Strategies**

- **Rolling Update:** This is the default Kubernetes deployment strategy where old pods are gradually replaced with new ones while ensuring application availability. It minimizes downtime but lacks fine-grained traffic control, meaning all users eventually experience the new version without incremental monitoring. Additionally, if a functional regression occurs that does not crash the application, Kubernetes does not automatically roll back, making it harder to catch silent failures.
- **Recreate:** In this strategy, the old version is completely shut down before the new version is deployed. This approach ensures a clean state with no overlapping versions, making it ideal for stateful applications or workloads that cannot handle multiple versions running simultaneously. However, it causes downtime during the transition, making it less suitable for applications requiring high availability.
- **Blue-Green Deployment:** This method runs two application versions in parallel - Blue (current) and Green (new). Traffic remains on the Blue version while the Green version undergoes validation. Once the Green version is confirmed stable, traffic is instantly switched over. If issues arise, rolling back is seamless by reverting traffic to the Blue version. This strategy ensures zero downtime but requires additional infrastructure to run both versions simultaneously.



- **Canary Deployment:** This strategy introduces the new version gradually by shifting traffic in small increments while monitoring performance metrics. Initially, a small percentage of traffic (e.g., 5%) is directed to the new version. If no issues arise, the traffic share is increased to 25%, then 50%, until the full transition is completed. If problems are detected, the rollout can be halted or automatically reverted. This approach allows controlled risk mitigation and is often used with service meshes or ingress controllers for more precise traffic routing.


