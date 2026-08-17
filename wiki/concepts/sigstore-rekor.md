---
title: Sigstore Rekor
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: [TMP/KB]
updated: 2025-04-17
tags: [Security, Supply-Chain]
---

# Overview

**Rekor** is a **transparency log server** that records cryptographically signed metadata about software artifacts, such as:

- Signatures
- Certificates
- Hashes
- Provenance documents (e.g., SLSA attestations)

It provides a **tamper-evident**, **immutable**, and **publicly auditable log**, ensuring that **every signing action leaves a trace** — crucial for securing the **software supply chain**.

# 🧠 Rekor’s Core Architecture

Rekor is designed around a **Merkle tree-based append-only log**, inspired by transparency systems like Certificate Transparency (CT). Its components include:

### 1. 🌳 **Transparency Log (Merkle Tree)**

- **Merkle trees** are cryptographic data structures that allow efficient and secure verification of large datasets.
- Every signed entry submitted to Rekor is hashed and **appended to the tree**, preserving order and ensuring **immutability**.
- The **root hash** of the Merkle tree can be independently verified and used to prove inclusion or detect tampering.

### 2. 📥 **Entry Submission API (REST/gRPC)**

- Rekor exposes REST and gRPC APIs that allow clients (e.g., Cosign, Fulcio) to:
    - Submit log entries
    - Query existing entries
    - Retrieve proofs of inclusion
- Common submission types:
    - Signed artifacts
    - Certificates
    - DSSE envelopes
    - In-toto attestations

Example:

```bash
rekor-cli upload --artifact myimage --public-key pubkey.pem --signature sig
```

### 3. 📄 **Log Entries (Types & Schema)**

Each entry in Rekor has a structured format depending on its **kind**:

- `hashedrekord`: For artifact hashes + signatures + public keys
- `rekord`: For raw artifacts and signatures
- `intoto`: For in-toto provenance documents
- `rpm`, `jar`, `apk`, etc.: Language/package-specific formats

Each entry includes:

- Payload (hash, signature, etc.)
- Timestamp
- Public key or certificate
- Optional metadata (e.g., builder identity)

### 4. 🛡️ **Inclusion Proofs**

- Rekor can generate **inclusion proofs** — cryptographic evidence that a specific entry exists in the Merkle tree.
- Clients can use this to **verify that an artifact’s signature has been logged**, and the log hasn’t been tampered with.

### 5. 🔎 **Search & Verification Tools**

- Rekor includes:
    - **rekor-cli** – Command-line tool to interact with the log
    - **Rekor web UI** – Optional frontend for browsing entries
    - **Public API** – To integrate with CI/CD or software verification workflows

# 🔧 How Rekor Works – Step-by-Step

1. 🔐 A signed artifact or certificate is submitted to Rekor (e.g., from Cosign or Gitsign).
2. 🧾 Rekor validates the entry format and stores it in memory.
3. 🌳 The entry is hashed and **added to the Merkle tree**.
4. 🔏 The log entry, index, and proof are written to persistent storage (e.g., PostgreSQL, Redis, or disk).
5. 📜 Rekor returns an **entry UUID**, timestamp, and **Merkle inclusion proof** to the client.
6. 👀 Anyone can **query** or **verify** the entry using Rekor's public endpoints.

# 🗄️ Rekor Storage Backends

Rekor supports multiple storage layers:

| Layer | Purpose |
| --- | --- |
| **Log Storage** | Stores raw entries and Merkle nodes |
| **Index Storage** | Accelerates search by hash or UUID |
| **API Layer** | Exposes gRPC/REST APIs |

Typical setups may use:

- **Disk-based backends** for simple deployments
- **Cloud-native** options (e.g., GCS, DynamoDB) for scalability
