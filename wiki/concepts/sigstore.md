---
title: Sigstore
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: []
updated: 2025-04-17
tags: [Security, Supply-Chain]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# Overview

**Sigstore** is an open-source project backed by the Linux Foundation. It provides tools to **sign, verify, and log software artifacts** (like container images, binaries, packages, etc.) in a **secure and transparent** way, without needing to manage long-term private keys manually.

The goal: **Make software signing easy and widely adopted** by simplifying cryptographic operations and auditability.

Linux Foundation Sigstore Aims to Be the **Let's Encrypt of Code Signing**

# Architecture

Sigstore is composed of **three core components**:

1. **Fulcio** – Ephemeral Certificate Authority (CA)
2. **Rekor** – Immutable transparency log
3. **Cosign** – CLI tool for signing/verifying artifacts

These components work together to create a **secure, verifiable, and automated** signing workflow

## **Fulcio** – Ephemeral Certificate Authority

- **Fulcio** issues **short-lived X.509 certificates** based on **OIDC identity tokens** (from GitHub Actions, Google, etc.).
- No long-term key pair is needed — identity is proven via a trusted OIDC provider.
- Once verified, Fulcio issues a certificate that binds the **signing key to the identity** (e.g., GitHub user, CI pipeline).

🔐 **Benefits**: No manual key management, reduced attack surface, and enhanced automation.

## **Rekor** – Transparency Log

- **Rekor** is a **public, immutable log** (like a simplified blockchain) where signing events are recorded.
- Stores:
    - Signatures
    - Certificates
    - Artifact metadata
- Built using a **Merkle tree**, ensuring **auditability and tamper-evidence**.

📜 This provides **transparency and traceability**, even if a certificate is later compromised.

## **Cosign – CLI for Signing & Verifying**

- **Cosign** is the command-line interface used to:
    - Sign container images and other artifacts
    - Verify signatures
    - Store signatures as OCI metadata (in Docker registries)
    - Integrate with Fulcio and Rekor for full transparency and trust

💡 You can use Cosign **with or without** Fulcio, but using all components together unlocks the full Sigstore workflow — no private key management required.

# End-to-End Workflow

Here’s a simplified example of how Sigstore components work together:

1. 👤 A developer or CI system authenticates via OIDC.
2. 🔐 **Fulcio** issues a short-lived cert bound to that identity.
3. 🖊️ **Cosign** uses the cert to sign the artifact (e.g., Docker image).
4. 🪵 The signature and cert are recorded in **Rekor**.
5. 👀 Anyone can later verify:
    - The artifact's signature is valid
    - It came from the claimed identity
    - It is logged in Rekor (proving time and integrity)

# Use Cases

- CI/CD pipelines (e.g., GitHub Actions signing releases)
- Software Supply Chain security (e.g., SLSA compliance)
- Signing and verifying container images
- Kubernetes + Sigstore integrations (e.g., with Kyverno or Gatekeeper)
- Protecting release processes from tampering or impersonation

# Next

[Explanation: Sigstore Cosign](../projects/sigstore-cosign.md)

[Explanation: Sigstore Fulcio](../projects/sigstore-fulcio.md)

[Explanation: Sigstore Rekor](../projects/sigstore-rekor.md)
