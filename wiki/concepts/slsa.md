---
title: SLSA
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: []
updated: 2025-04-09
tags: [Security, Supply-Chain]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# **Overview**

**SLSA**, pronounced *"salsa"* **(Supply-chain Levels for Software Artifacts)** is a security framework designed to protect software supply chains from threats such as tampering, vulnerabilities, and insider risks. It establishes a set of security standards for software development, defining levels of security maturity that software artifacts can achieve.

SLSA consists of **four levels (0-4)**, each increasing in security guarantees. It is built around **three key pillars**:

- **Source (Code Integrity)**
- **Build (Build Process Security)**
- **Provenance (Metadata & Auditability).**

It was originally created by Google and is now part of the **Open Source Security Foundation (OpenSSF)**.

# **Supply chain threats**

.svg)

# The 4 SLSA Levels

Each level adds stronger integrity guarantees and trust in the build process:

### 🥇 **SLSA 1 – Provenance**

- The build **must generate provenance metadata** (i.e., information about how and with what the artifact was built).
- It's basic but already useful for traceability.

### 🥈 **SLSA 2 – Scripted Builds**

- The build process must be **automated** and **repeatable**.
- Provenance must be **generated automatically**, not manually.
- Reduces human error and tampering.

### 🥉 **SLSA 3 – Secure and Hermetic Builds**

- The build must be **hermetic** (only uses declared inputs).
- Requires a **hardened CI/CD system** (e.g., restricted GitHub Actions runner).
- Provenance must be **cryptographically signed**.

### 🏆 **SLSA 4 – Reproducible Builds**

- Anyone should be able to **reproduce the exact same artifact** from the source and instructions.
- Provides the **highest level of trust** and protection against tampering or injection.
