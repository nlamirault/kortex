---
title: Istio CRDs
type: concept
status: active
confidence: high
cluster: networking
domain: [networking]
sources: []
updated: 2025-04-09
tags: [CRD, Kubernetes, Networking]
---

# **Istio CRDs**

| **CRD** | **Purpose** |
| --- | --- |
| `VirtualService` | Defines **traffic routing** rules |
| `DestinationRule` | Configures **subsets, load balancing, and circuit breaking** |
| `Gateway` | Manages **Ingress/Egress traffic** |
| `ServiceEntry` | Allows **external service access** |
| `Sidecar` | Restricts **sidecar proxy scope** |
| `PeerAuthentication` | Defines **mTLS policies** |
| `RequestAuthentication` | Enforces **JWT authentication** |
| `AuthorizationPolicy` | Defines **access control rules** |
| `Telemetry` | Configures **metrics, logs, and tracing** |

# **Traffic Management CRDs**

Used to control **routing, load balancing, retries, and fault injection**.

## **VirtualService**

- Defines traffic routing rules for a service.
- Controls HTTP, TCP, and gRPC traffic.
- Can define host-based routing, path-based routing, retries, timeouts, and fault injection.

Example: Routing 80% of traffic to `v1`, 20% to `v2`

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - route:
    - destination:
        host: reviews
        subset: v1
      weight: 80
    - destination:
        host: reviews
        subset: v2
      weight: 20
```

## **DestinationRule**

- Configures policies for traffic routed by a `VirtualService`.
- Defines subsets (e.g., v1, v2) for services.
- Controls load balancing, connection pool settings, and circuit breaking.

Example: Setting up subsets for `v1` and `v2`, using round-robin load balancing

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
```

## **Gateway**

- Manages ingress (incoming) and egress (outgoing) traffic.
- Works at the edge of the service mesh.
- Used for TLS termination, HTTP/HTTPS routing, and external access.

Example: Defining an Ingress Gateway for external traffic

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-ingress-gateway
spec:
  selector:
    istio: ingressgateway  # Selects the Istio ingress gateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - myapp.example.com

```

### **ServiceEntry**

- Allows services inside the mesh to talk to external services.
- Used for accessing external APIs (e.g., Stripe, Google APIs, etc.).
- Can enforce mTLS and monitoring for external traffic.

Example: Allowing traffic to an external API (`api.external.com`)

```yaml
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: external-api
spec:
  hosts:
  - api.external.com
  location: MESH_EXTERNAL  # External service
  ports:
  - number: 443
    name: https
    protocol: HTTPS

```

### **Sidecar**

- Controls which services an Envoy sidecar should proxy.
- By default, Istio sidecars handle all traffic in the namespace, but `Sidecar` can restrict this scope.

Example: Limiting a sidecar proxy to only talk to `reviews` and `ratings` services

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Sidecar
metadata:
  name: reviews-sidecar
spec:
  workloadSelector:
    labels:
      app: reviews
  egress:
  - hosts:
    - "./ratings.default.svc.cluster.local"

```

# Security CRDs

### **PeerAuthentication**

- Defines mTLS settings between services.
- Can enable strict mTLS (mutual TLS) or allow mixed TLS modes.

Example: Enforcing strict mTLS on all services

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT

```

### **RequestAuthentication**

- Handles JWT authentication for HTTP requests.
- Used to verify JWT tokens before allowing requests.

Example: Enforcing JWT authentication

```yaml
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: jwt-auth
spec:
  selector:
    matchLabels:
      app: myapp
  jwtRules:
  - issuer: "https://my-auth-provider.com"
    jwksUri: "https://my-auth-provider.com/.well-known/jwks.json"

```

### **AuthorizationPolicy**

- Defines fine-grained access control rules.
- Controls who can access which services, based on roles, IPs, or JWT claims.

Example: Allowing only users with the "admin" role to access `reviews`

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: reviews-access
spec:
  selector:
    matchLabels:
      app: reviews
  rules:
  - from:
    - source:
        requestPrincipals: ["admin@example.com"]

```

# Telemetry & Observability CRDs

### **Telemetry (New in Istio 1.17+)**

- Configures metrics, logging, and tracing (replaces old Mixer-based telemetry).
- Controls which metrics and logs are collected.

Example: Enabling access logs for all services

```yaml
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: default
spec:
  accessLogging:
  - providers:
    - name: envoy

```
