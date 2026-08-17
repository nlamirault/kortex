---
title: VEX
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: [TMP/KB]
updated: 2025-04-09
tags: [Security, Supply-Chain]
---

# Overview

**VEX** is a **standardized format** (usually in JSON or XML) used by organizations to **share context around whether a specific vulnerability actually applies to their product or environment**.

The main goal is to **reduce the noise** from long vulnerability lists (like from SBOM scans), by specifying **which vulnerabilities are actually exploitable or actionable** in your context.

# What’s in a VEX Document?

A typical VEX file includes:

- **Product/component identification**
- **Vulnerability details** (usually by CVE-ID)
- **Vulnerability status**:
    - `Not affected`
    - `Affected`
    - `Under investigation`
    - `Fixed`
- **Technical justification**
- **Remediation guidance or links**
- **Last updated timestamp**

# How to Use a VEX File

### 1. **When to use it**

If you’re managing an SBOM (Software Bill of Materials) and your vulnerability scanner (like Grype, Trivy, Snyk) flags multiple CVEs, a **VEX file helps you determine which CVEs are actually relevant** to your environment.

### 2. **Steps to Use It**

1. ✅ **Obtain a VEX file** from the software vendor (or create one yourself)
2. 📦 **Link the VEX to your SBOM** (often via identifiers like Package URL or CPE)
3. 🔍 **Compare vulnerability scan results against the VEX**
4. 📉 **Eliminate false positives** and focus on real threats
