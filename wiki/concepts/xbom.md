---
title: xBOM
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: [TMP/KB]
updated: 2025-09-01
tags: [Supply-Chain]
---

The xBOM is a full-stack BOM standard that provides advanced supply chain capabilities for cyber risk reduction, and includes 12 different BOMs spanning the software and hardware ecosystems. The xBOM builds upon the traditional elements of an SBOM to provide a more comprehensive view by including a broader range of components and information related to software-based products.

| **Acronym** | **Name** | **Focus** |
| --- | --- | --- |
| SBOM | Software Bill of Materials | Software |
| SaaSBOM | Software as a Service Bill of Materials | Software |
| CBOM | Cryptography Bill of Materials | Software |
| ML-BOM | Machine Learning Bill of Materials | Software |
| BOV | Bill of Vulnerabilities | Software |
| VDR | Vulnerability Disclosure Report | Software |
| VEX | Vulnerability Exploitability eXchange | Software |
| CRNF | Common Release Notes Format | Software |
| CDXA | CycloneDX Attestations | Software |
| HBOM | Hardware Bill of Materials | Hardware |
| OBOM | Operation Bill of Materials | Operations |
| MBOM | Manufacturing Bill of Materials | Software |

**The 12 BOMs included in CycloneDX xBOM.**

**SBOM (Software Bill of Materials)**

An [SBOM](https://www.reversinglabs.com/glossary/software-bill-of-materials-sbom) is a complete, machine-readable inventory of software components, including metadata, dependencies, and licenses, providing transparency across the software supply chain.

See: [Reference: SBOM](../concepts/sbom.md) 

**SaaSBOM (Software as a Service Bill of Materials)**

[SaaSBOM](https://www.reversinglabs.com/glossary/saas-bom) identifies and inventories cloud-based applications, APIs, endpoints, and data flows to help ensure governance, compliance, and risk mitigation in SaaS environments.

**CBOM (Cryptography Bill of Materials)**

A [CBOM](https://www.reversinglabs.com/glossary/cbom) lists cryptographic assets such as keys, algorithms, and libraries to evaluate crypto agility, policy compliance, and potential vulnerabilities in cryptographic implementations.

**ML-BOM (Machine Learning Bill of Materials)**

ML-BOM provides transparency into machine learning systems by documenting models, datasets, parameters, training processes, and dependencies – enabling better governance and trust in AI development.

**BOV (Bill of Vulnerabilities)**

BOV enables structured sharing of vulnerability data affecting software components, supporting automated analysis, coordination, and remediation across the software ecosystem and threat intelligence systems.

**VDR (Vulnerability Disclosure Report)**

The Vulnerability Disclosure Report (VDR) standardizes how known vulnerabilities are communicated, enhancing collaboration between suppliers, researchers, and consumers during coordinated vulnerability disclosure processes.

**VEX (Vulnerability Exploitability eXchange)**

VEX communicates the exploitability of a vulnerability in a specific context, helping organizations prioritize remediation based on actual exposure, not just CVE presence.

**CRNF (Common Release Notes Format)**

This format standardizes software release notes, allowing automated systems to interpret changes, improvements, and fixes in a structured, machine-readable and developer-friendly format.

**CDXA (CycloneDX Attestations)**

CDXA provides cryptographically verifiable, machine-readable proof of build integrity, policy compliance, and artifact provenance to support secure software development and delivery.

**HBOM (Hardware Bill of Materials)**

HBOM inventories hardware components, firmware, and associated metadata, ensuring security, compliance, and lifecycle management of embedded systems and connected IoT hardware devices. Items are related to, but not contained within software.

**OBOM (Operation Bill of Materials)**

OBOM captures operational configurations, environments, and runtime dependencies that impact system behavior, helping to manage post-deployment risk and ensuring secure and consistent software execution. Items are related to, but not contained within software.

**MBOM (Manufacturing Bill of Materials)**

MBOM outlines the manufacturing and assembly details of software, services, and hardware to ensure traceability, quality assurance, and regulatory compliance throughout the production process. Items are related to, but not contained within software.
