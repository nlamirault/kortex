---
type: Explanation
title: Sigstore Fulcio
description: **Fulcio** is an **open-source Certificate Authority** specifically designed for **ephemeral certificate issuance** in the context of **automated software signing**.
tags: ["Security", "Supply-Chain"]
timestamp: 2025-04-17T14:18:00Z
---

# Overview

**Fulcio** is an **open-source Certificate Authority** specifically designed for **ephemeral certificate issuance** in the context of **automated software signing**.

Unlike traditional CAs (which manage long-term keys and complex trust chains), Fulcio issues **short-lived X.509 certificates** based on **OIDC-authenticated identities** — no need for developers or CI systems to manage private keys themselves.

## 🧠 High-Level Architecture

Fulcio consists of these core components:

### 1. 🔐 **OIDC Identity Verification Module**

- This component authenticates the requestor using **OpenID Connect** (OIDC).
- Examples of OIDC providers: **GitHub, Google, Microsoft, GitLab, etc.**
- It fetches and validates an **ID token** representing the user’s identity and claims.
- The token must be signed by the trusted identity provider and verified by Fulcio.

### 2. 🔏 **Ephemeral Certificate Issuance Engine**

- After verifying identity, Fulcio generates or accepts a **public key** from the user or client.
- Then it **issues a short-lived X.509 certificate**, binding:
    - The public key
    - The identity claims from the OIDC token (e.g., email, GitHub username)
- The private key used for signing never leaves the client.

### 3. 📜 **Certificate Authority Root/Intermediate Keys**

- Fulcio uses a standard **CA key pair** (root or intermediate) to sign the issued certs.
- The **root certificate** is **publicly available and auditable**, forming the **trust anchor**.
- Clients and verifiers can trust certs issued by Fulcio because they can validate against this trusted root.

### 4. 🪵 **Rekor Integration (Optional but Recommended)**

- Fulcio can optionally **log the issued certificate** into **Rekor**, Sigstore’s public transparency log.
- This ensures **tamper-evident, public auditability** of every issued certificate.

### 5. 📦 **Fulcio Server**

- The Fulcio service is deployed as a **gRPC and/or REST API server**.
- It handles requests for cert issuance, validates tokens, and returns certificates.
- Usually deployed as part of a Sigstore stack (with Rekor and Cosign).
