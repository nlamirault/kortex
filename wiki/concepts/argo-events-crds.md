---
title: Argo Events CRDs
type: concept
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: []
updated: 2025-04-09
tags: [Architecture, CRD, Events, Kubernetes]
---

# **Summary of Argo Events CRDs**

| CRD | Purpose |
| --- | --- |
| **EventSource** | Captures events from external sources. |
| **Sensor** | Listens for events and triggers workflows or jobs. |
| **EventBus** | Acts as a message broker for reliable event delivery. |
| **EventBusPolicy** | (New) Provides security and access control for EventBus. |

# **EventSource**

**EventSource** defines how and from where events are collected. It listens to various event producers such as webhooks, Kafka topics, S3 bucket changes, GitHub events, or even cron schedules.

### **🔧 Key Fields**:

- **`type`**: Specifies the event source type (e.g., webhook, Kafka, S3, GitHub, etc.).
- **`service`**: Defines a Kubernetes service to expose the event source (for HTTP-based sources like webhooks).
- **`config`**: Contains specific configuration details for the event source.
- **`eventBusName`**: (Optional) Defines which EventBus to use for delivering events.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: EventSource
metadata:
  name: github-events
spec:
  github:
    example:
      owner: "my-org"
      repository: "my-repo"
      webhook:
        endpoint: "/"
        port: "12000"
      events:
        - "push"
```

# **Sensor**

**Sensor** listens for events from EventSources, processes them, and triggers actions. It acts as the **event router**, ensuring that specific workflows, jobs, or Kubernetes resources are executed when an event occurs.

### **🔧 Key Fields**:

- **`dependencies`**: Defines the event sources this sensor listens to.
- **`triggers`**: Specifies what actions to take when an event is received.
- **`eventBusName`**: (Optional) Defines which EventBus to use.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: github-sensor
spec:
  dependencies:
    - name: github-dependency
      eventSourceName: github-events
      eventName: example
  triggers:
    - template:
        name: argo-workflow-trigger
        k8s:
          operation: create
          source:
            resource:
              apiVersion: argoproj.io/v1alpha1
              kind: Workflow
              metadata:
                generateName: triggered-workflow-
              spec:
                entrypoint: main
                templates:
                  - name: main
                    container:
                      image: alpine
                      command: ["echo", "Triggered by GitHub event!"]
```

# **EventBus**

**EventBus** acts as the messaging layer that delivers events from EventSources to Sensors. It ensures event persistence and guarantees message delivery.

### **🔧 Key Fields**:

- **`nats`**: Defines a NATS-based event bus (default).
- **`kafka`**: Defines a Kafka-based event bus (optional, for high scalability).

```yaml
apiVersion: argoproj.io/v1alpha1
kind: EventBus
metadata:
  name: default
spec:
  nats:
    native: {}
```

# **EventBusPolicy (New in v1.8+)**

- **EventBusPolicy** provides **fine-grained access control** over EventBuses.
- Defines **authorization rules** for which Sensors can consume events from a particular EventBus.
- Helps enforce security by controlling **who can publish or subscribe to events**
