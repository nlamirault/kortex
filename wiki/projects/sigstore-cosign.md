---
title: Sigstore Cosign
type: project
status: active
confidence: high
cluster: security
domain: [security]
sources: []
updated: 2025-04-17
tags: [Security, Supply-Chain]
---

# Overview

**Cosign** is an open-source CLI tool developed by Sigstore that allows developers and CI systems to:

- **Sign** container images (and other OCI artifacts)
- **Verify** those signatures
- **Attach metadata**, attestations, and SBOMs
- **Store signatures** in container registries (alongside the image itself)

Cosign is designed to work **seamlessly with Fulcio and Rekor**, enabling a fully keyless and transparent signing experience.

# 🧠 Cosign Architecture Overview

Cosign is primarily a **client-side tool**, but it plays a central role in coordinating with:

- **Fulcio** (to get ephemeral signing certificates)
- **Rekor** (to publish signatures and certs in a transparency log)
- **OCI Registries** (to store and fetch signatures)

Here are its main components and how they work together 👇

# 🧩 Key Components of Cosign

### 1. 🖥️ **CLI Interface**

- The core of Cosign is a command-line tool (`cosign`) that developers or CI pipelines use.
- Common commands:
    - `cosign sign`
    - `cosign verify`
    - `cosign attach sbom`
    - `cosign generate-key-pair` (if you're using keys manually)
- The CLI is used to initiate signing/verification operations and manage configurations.

### 2. 🔐 **Signing Engine**

Cosign can sign using:

- **Keyless mode** (default in modern setups):
    - Authenticates with an OIDC identity provider (e.g., GitHub Actions)
    - Gets an ephemeral cert from **Fulcio**
    - Signs with a short-lived key
- **Key-pair mode** (fallback or for local dev):
    - Uses locally stored private key and password-protected key file (`cosign.key`)

Signing output:

- Signature
- Optional certificate (if using Fulcio)
- Optional metadata (e.g., SBOM, SLSA attestation)

### 3. 🪵 **Rekor Integration**

- When signing an artifact, Cosign **uploads the signature + cert** to **Rekor**.
- Rekor stores it in a public transparency log and returns:
    - A UUID (log index)
    - A timestamp
    - An inclusion proof (from the Merkle tree)
- This ensures that every signing action is **auditable and publicly verifiable**.

### 4. 📦 **OCI Registry Integration**

- Cosign stores:
    - **Signatures**
    - **Certificates**
    - **Attestations**
- Directly **in the OCI registry** alongside the container image using OCI-standard objects.

For example, the signature for `nginx:latest` is stored as:

```
ghcr.io/your-org/nginx:latest.sig
```

This makes it easy to distribute and verify artifacts **using the same infrastructure as the container images themselves** (e.g., Docker Hub, GHCR, ECR).

### 5. 🕵️ **Verification Engine**

Cosign can **verify**:

- That a signature matches a specific image
- That it was created by a specific identity (via Fulcio certs)
- That it exists in Rekor (transparency proof)

Supports verifying:

- Signature validity
- Certificate trust
- Rekor log inclusion
- OIDC identity claims
