---
title: Ingress vs Gateway API
type: concept
status: active
confidence: high
cluster: networking
domain: [networking]
sources: [TMP/KB]
updated: 2025-03-28
tags: [Kubernetes, Networking]
---

# **Kubernetes Ingress vs Gateway API: Key Differences**

Kubernetes **Ingress** and **Gateway API** are both used to manage external traffic into a Kubernetes cluster, but they differ in flexibility, extensibility, and capabilities.

## **Overview of Both Concepts**

| Feature | Kubernetes Ingress | Gateway API |
| --- | --- | --- |
| **Purpose** | Manages external traffic to services inside the cluster via HTTP/S routing. | Provides a more extensible and role-oriented API for managing traffic (HTTP, TCP, TLS, etc.). |
| **API Stability** | Stable and widely used. | Newer and still evolving (Beta in Kubernetes 1.26+). |
| **Flexibility** | Limited to HTTP/HTTPS routing. | Supports more protocols (HTTP, TCP, UDP, TLS, etc.). |
| **Architecture** | Uses Ingress controllers (e.g., NGINX, Traefik). | Uses Gateways, Listeners, Routes, and Filters for modularity. |
| **Multi-Tenancy** | Not well-suited for multi-tenant environments. | Better for multi-tenancy with more granular roles and permissions. |

## **Key Differences in Detail**

### **Architecture**

- **Ingress**:
    - Defines routing rules that are implemented by an **Ingress Controller** (e.g., NGINX, HAProxy, Traefik).
    - A single Ingress resource manages multiple services but lacks fine-grained control.
- **Gateway API**:
    - Introduces **Gateways**, which are infrastructure resources that define how traffic enters the cluster.
    - **Routes** (e.g., `HTTPRoute`, `TCPRoute`, etc.) define traffic rules separately from the Gateway.
    - Supports **multiple GatewayClasses**, enabling different load balancers/providers within the same cluster.

### **Protocol Support**

- **Ingress**: Primarily supports **HTTP and HTTPS**.
- **Gateway API**: Supports **HTTP, HTTPS, TCP, UDP, and TLS**, making it more versatile.

### **Role-Based Configuration**

- **Ingress**: All routing rules are typically defined in one Ingress object, leading to potential conflicts.
- **Gateway API**: Uses separate resources (`Gateway`, `GatewayClass`, `Routes`), allowing teams to manage networking independently.

### **Extensibility & Expressiveness**

- **Ingress**: Harder to extend; mostly HTTP-based; lacks native support for features like retries, request transformations, and advanced traffic shaping.
- **Gateway API**: More extensible with CRDs like `HTTPRoute` for better control over routing, load balancing, and policy enforcement.

[](https://app.notion.com)



# **When to Use What?**

| Scenario | Use Ingress | Use Gateway API |
| --- | --- | --- |
| Simple HTTP-based routing | ✅ | ✅ |
| Advanced traffic policies (e.g., retries, traffic splitting) | ❌ | ✅ |
| Multi-protocol support (TCP, UDP, etc.) | ❌ | ✅ |
| Multi-tenancy (different teams managing networking) | ❌ | ✅ |
| Need for vendor neutrality & extensibility | ❌ | ✅ |

# **Conclusion**

- **Ingress** is simpler and widely adopted, making it a good choice for basic use cases.
- **Gateway API** is the future of Kubernetes networking, providing more flexibility, protocol support, and modularity.
