---
title: FOCUS
type: concept
status: active
confidence: high
cluster: metering
domain: [metering]
sources: []
updated: 2025-02-28
tags: [FinOps]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# **What is FinOps FOCUS?**

[FinOps Open Cost and Usage Specification (FOCUS)](https://focus.finops.org/what-is-focus/) is an open-source standard developed to streamline the way cloud billing data is formatted and handled across multiple cloud platforms. As a technical specification, FOCUS mandates a unified format for cloud bills, which is aimed at simplifying the complexities involved in data normalization, thereby making FinOps practices more efficient. This specification sets clear requirements for cloud vendors to adhere to a single billing file format, significantly reducing the time FinOps practitioners spend on data ingestion and normalization



**Focus in FinOps** means:

1. **Prioritizing Cost-Efficient Architectures**
    - Designing and optimizing workloads to reduce waste and improve cost efficiency.
    - Choosing the right cloud services (e.g., reserved instances, spot instances, autoscaling).
2. **Monitoring & Observability**
    - Using real-time metrics to track cloud spend at a granular level.
    - Implementing cost allocation and tagging strategies for visibility.
3. **Automation & Governance**
    - Enforcing policies through Infrastructure as Code (IaC) and cost-aware CI/CD pipelines.
    - Setting up guardrails to prevent budget overruns (e.g., quotas, alerts).
4. **Balancing Cost, Performance, and Innovation**
    - Ensuring cost optimization does not impact performance or scalability.
    - Continuously improving architectures based on FinOps insights.

# **The FOCUS Specification**

The FOCUS Specification defines clear requirements for cloud vendors to produce consistent cost and usage datasets. FOCUS datasets enable FinOps Practitioners to perform common FinOps [Capabilities(opens in a new tab)](https://www.finops.org/framework/capabilities/) such as [Invoicing & Chargeback(opens in a new tab)](https://www.finops.org/framework/capabilities/invoicing-chargeback/), [Allocation(opens in a new tab)](https://www.finops.org/framework/capabilities/allocation/), [Budgeting(opens in a new tab)](https://www.finops.org/framework/capabilities/budgeting/), [Forecasting(opens in a new tab)](https://www.finops.org/framework/capabilities/forecasting/), etc., using a single set of queries and instructions, no matter the origin of the dataset.

The specification is designed to be used by
- **FinOps Practitioners** - end-user individuals who consume cloud billing data to perform FinOps for their organization
- **Cloud Vendors** - Cloud Service Providers (CSPs), Software-as-a-Service (SaaS) Vendors, and other Independent Software Vendors (ISVs) who generate billing data to send to their customers 
- **FinOps Vendors** - FinOps tool vendors and FinOps service providers who both generate and consume cloud billing data to assist others with performing FinOps
