---
title: Istio
type: project
status: active
confidence: high
cluster: networking
domain: [networking]
sources: [TMP/KB]
updated: 2025-03-20
tags: [Mesh, Networking]
---

# Description

Istio is a **service mesh** that helps manage, secure, and monitor communication between microservices in a distributed system. It acts as a **control plane** for service-to-service networking, providing features like:

- **Traffic Management**: Load balancing, routing, retries, and circuit breaking.
- **Security**: Mutual TLS (mTLS), authentication, and authorization between services.
- **Observability**: Tracing, logging, and metrics collection.
- **Policy Enforcement**: Rate limiting, quotas, and fault injection.

Istio achieves this by deploying a **sidecar proxy (Envoy)** alongside each service in your Kubernetes cluster (or VM-based system). These proxies intercept and manage all network traffic, enabling Istio to enforce policies and collect telemetry.

# **Architecture & Components**

Istio consists of two main parts:

1. **Data Plane** (Handles traffic between services)
2. **Control Plane** (Manages and configures the data plane)

## **1. Data Plane**

The data plane is responsible for managing communication between microservices in the service mesh. It consists of **`Envoy`** proxies deployed as sidecars**:**

- Based on **Envoy**, a high-performance proxy developed by Lyft.
- Intercepts inbound and outbound traffic for services.
- Handles **service discovery, load balancing, traffic routing, security (mTLS), and telemetry**.
- Enforces Istio policies without requiring modifications to applications.

---

### **2. Control Plane**

The control plane manages and configures the data plane proxies. It consists of a single binary called **`istiod`** 

Before v1.5.0, the control plane was built with multiple microservices:: Pilot, Citadel, Galley and Mixer

- **Traffic Management** (Pilot's role) → Configures and manages Envoy proxies for service-to-service communication.
- **Security** (Citadel's role) → Issues **X.509 certificates**, enforces **mTLS**, and handles authentication.
- **Configuration Management** (Galley’s role) → Validates and distributes Istio configuration from Kubernetes CRDs.
- **Telemetry Support** → Works with external observability tools (**Prometheus, Grafana, Jaeger, Kiali**) instead of relying on Mixer.

# **Deployment Model**

1. **Sidecar Proxy Model** (deployed at Swan)
    - Each service gets an **Envoy proxy** (sidecar container).
    - Proxies intercept **all service-to-service traffic**.
2. **Gateway Model**
    - **Ingress Gateway** → Controls external traffic entering the cluster.
    - **Egress Gateway** → Manages outbound traffic from the cluster.

# Istio and Kubernetes

## **1. Interaction with Kubernetes**

`istiod` monitors **Kubernetes API Server** and reacts to configuration changes.

- **Service Discovery**:
    - Watches **Kubernetes Services (Service, Endpoints)** to know which services exist.
    - Automatically updates Envoy sidecars with new service details.
- **Configuration Management**:
    - Watches **Istio Custom Resources (CRDs)** like `VirtualService`, `DestinationRule`, etc.
    - Translates them into Envoy configurations and pushes updates.
- **Security & Certificates**:
    - Uses **Kubernetes Secrets** to store and manage X.509 TLS certificates.
    - Assigns identity to each workload based on **Kubernetes Service Accounts**.
- **Ingress & Egress Gateway Management**:
    - Configures **Ingress Gateway** (for incoming traffic from outside the cluster).
    - Configures **Egress Gateway** (for controlling external API calls).

## **2. Interaction with Envoy Sidecar Proxies**

Each service in the mesh has an **Envoy sidecar** that handles traffic. `istiod` is responsible for configuring these proxies:

- **Bootstrap Configuration** (when a service starts)
    - A new pod with an **Envoy sidecar** starts.
    - Envoy contacts `istiod` to get its initial configuration.
    - `istiod` provides details like:
        - Cluster-wide service discovery
        - Traffic routing rules
        - Security policies
- **Dynamic Updates** (while running)
    - If a new service is added or a routing rule changes, `istiod` pushes an **updated config** to the affected Envoy proxies.
    - This ensures **real-time traffic management** without restarting services.
- **Security & Identity (mTLS)**
    - `istiod` issues **X.509 certificates** to each Envoy sidecar.
    - Sidecars use **mutual TLS (mTLS)** to encrypt traffic between services.
    - Istio verifies service identities based on **Kubernetes Service Accounts**.
- **Telemetry & Observability**
    - `istiod` ensures Envoy collects **metrics, logs, and traces**.
    - Envoy sends data to **Prometheus, Jaeger, Kiali, and Grafana** for monitoring

## **3. Step-by-Step Flow of `istiod` in Action**

1. **Pod Starts** → A new pod is created in Kubernetes.
2. **Sidecar Injection** → Istio automatically adds an **Envoy sidecar** to the pod.
3. **Service Discovery** → `istiod` fetches service details from Kubernetes.
4. **Configuration Push** → `istiod` sends Envoy the correct routing, security, and logging rules.
5. **Secure Communication** → Services communicate via **mTLS** enforced by Envoy.
6. **Real-time Updates** → Any changes in Kubernetes (e.g., a new version of a service) are dynamically sent to Envoy.

# Architecture

![](https://tetrate.io/wp-content/uploads/2023/04/istio-architecture.png)

# Next

[Reference: Istio CRDs](../concepts/istio-crds.md)
