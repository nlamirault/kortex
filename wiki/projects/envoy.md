---
title: Envoy
type: project
status: active
confidence: high
cluster: networking
domain: [networking]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Mesh, Networking]
---

# **What is Envoy?**

Envoy is a high-performance, cloud-native edge and service proxy designed for microservices-based architectures. Developed by Lyft and now part of the **Cloud Native Computing Foundation (CNCF)**, Envoy serves as a **L4/L7 proxy** that provides features like load balancing, observability, and security across distributed systems.

Envoy is often used as a **sidecar proxy** in **service meshes** (e.g., Istio) or as an **API gateway**.

---

# **Envoy Architecture**

Envoy follows a monolithic architecture but operates in a layered and extensible way. The key design principles include:

1. **Process Model** – Runs as a single process but is highly concurrent.
2. **Threading Model** – Uses worker threads for handling requests efficiently.
3. **Asynchronous & Event-driven** – Uses a **non-blocking** event loop.
4. **xDS APIs** – A **control-plane-driven** architecture for dynamic configuration.

---

# **Key Components of Envoy**

Envoy consists of several major components that interact to provide seamless service discovery, routing, and observability:

## **Listeners**

- Entry points for traffic.
- Can be TCP (Layer 4) or HTTP (Layer 7).
- Configured with filters that define behavior.

## **Network Filters**

- Modular processing units for TCP-level traffic.
- Example filters:
    - **TLS Inspector** (detects SSL/TLS).
    - **Mongo Proxy** (filters MongoDB traffic).

## **HTTP Connection Manager (HCM)**

- Manages HTTP/HTTPS requests.
- Implements **HTTP filters** for functionalities like rate-limiting, authentication, and compression.

## **Clusters**

- Groups of upstream endpoints (services).
- Supports **service discovery** (DNS, static, or via xDS APIs).

## **Load Balancer**

- Distributes traffic across clusters.
- Supports **round-robin, least-request, ring hash**, etc.

## **Observability & Telemetry**

- Provides **metrics (Prometheus), logs, and tracing** (Jaeger, Zipkin).
- Supports OpenTelemetry.

## **Control Plane (xDS APIs)**

- Envoy is **config-driven**, and the xDS APIs (e.g., LDS, CDS, RDS, EDS) dynamically control its behavior.
- Example control planes: **Istio’s Pilot, Consul Connect, AWS App Mesh**.

---

## **Envoy Deployment Modes**

1. **Edge Proxy (API Gateway)** – Acts as an ingress gateway for external traffic.
2. **Sidecar Proxy (Service Mesh)** – Runs alongside microservices for security and traffic management.
3. **Middle Proxy** – Sits between services as an L4/L7 proxy.

---

# **Why Use Envoy?**

✅ **Scalability** – Handles thousands of connections efficiently.

✅ **Observability** – Advanced logging, tracing, and monitoring.

✅ **Extensibility** – Supports WebAssembly (WASM) for custom filters.

✅ **Dynamic Configuration** – Uses xDS APIs for real-time updates.

✅ **Security** – Supports TLS, mTLS, and authentication mechanisms.

# **xDS APIs – Dynamic Configuration Mechanism**

Instead of using static config files, Envoy fetches its configurations from a **control plane** via gRPC-based xDS APIs. These include:

- **Listener Discovery Service (LDS)**
    - Defines **inbound listeners** (e.g., HTTP, TCP).
    - Configures **ports**, **protocols**, and **filters**.
- **Route Discovery Service (RDS)**
    - Dynamically updates **routing rules**.
    - Manages **host-based routing, path-based routing**, and **traffic shifting**.
- **Cluster Discovery Service (CDS)**
    - Defines upstream **clusters** dynamically.
    - Enables **blue-green deployments, canary releases**.
- **Endpoint Discovery Service (EDS)**
    - Manages **individual service instances** (endpoints).
    - Provides **health-checking** and **load balancing updates**.
- **Secret Discovery Service (SDS)**
    - Distributes **TLS certificates** for **mTLS** (mutual TLS) encryption.
- **Extension Configuration Discovery Service (ECDS)**
    - Dynamically loads **custom extensions** (e.g., WebAssembly filters).

👉 These APIs allow **zero-downtime updates** and **centralized control** over networking policies.

# **Envoy in a Service Mesh (Istio Example)**

In **service mesh architectures**, Envoy acts as a **sidecar proxy** alongside microservices. A control plane (like Istio) manages traffic, security, and observability.

## **How Envoy Works in Istio?**

1. **Sidecar Injection**
    - Each microservice has an **Envoy proxy** deployed as a **sidecar** (via Kubernetes).
    - The proxy intercepts **all inbound and outbound traffic**.
2. **Service Discovery & Load Balancing**
    - Envoy queries Istio’s **Control Plane** (Pilot) for dynamic routing.
    - Uses **EDS & CDS** for finding healthy upstream instances.
3. **Traffic Management**
    - Istio configures **traffic shifting, circuit breaking**, and **rate limiting** via RDS.
4. **mTLS Encryption**
    - Envoy fetches TLS certs via **SDS**, enabling **zero-trust security**.
5. **Observability & Monitoring**
    - Sends logs and metrics to **Prometheus, Grafana, Jaeger**.
    - Supports **distributed tracing** for debugging.
