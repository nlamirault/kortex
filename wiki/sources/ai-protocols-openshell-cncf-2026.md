---
type: source
title: "Welcoming OpenShell to the CNCF: Open Governance to Secure Agentic AI"
description: CNCF blog post (KubeCon + CloudNativeCon NA 2026) welcoming NVIDIA's OpenShell, an open source runtime that governs autonomous AI agents with policy enforced outside the agent, as a CNCF Sandbox project moving to a vendor-neutral ai-openshell organization and adopting Cedar.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/
    id: openshell-cncf-2026
    title: "Welcoming OpenShell to the CNCF (CNCF Blog)"
    author: Jonathan Bryce, Ali Golshan
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:12:06Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [openshell, sandbox, agents, governance, policy, cedar, cncf, nvidia, kubecon]
---

# Welcoming OpenShell to the CNCF: Open Governance to Secure Agentic AI

**Auteur :** Jonathan Bryce (CNCF), Ali Golshan (NVIDIA) · **Publié :** 2026-11-10 · **Lien :** https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~4 min

## En Bref

At KubeCon + CloudNativeCon North America, the CNCF welcomed [OpenShell](../projects/openshell.md)
as a Sandbox project. NVIDIA contributed it as "an open source runtime for securing and governing
autonomous AI agents".[^openshell-cncf-2026] The post argues that agents need real capability
without unchecked access to data, secrets or networks, so enforcement has to sit outside the
agent, in the infrastructure it runs on. It also argues that this governing layer should be
shared and vendor-neutral, which is the case for putting it under a foundation.[^openshell-cncf-2026]

## Points Clés

- **Enforcement outside the agent:** OpenShell "manages and monitors agent behavior" and enforces policy-based boundaries on what an agent can do. The post presents this as enforcement "right within the infrastructure that the agents run on", not inside the agent.[^openshell-cncf-2026]
- **Cedar as policy language (the post's claim):** OpenShell "is adopting Cedar, another CNCF project, as its policy language", which the authors call "a great example of CNCF projects building on one another".[^openshell-cncf-2026] *Dated check, 2026-11-13:* the repository still documents a YAML policy format, and Cedar is an open RFC for an **alternate** policy language. The [project page](../projects/openshell.md#policy) has the detail.
- **Governance and contributors:** core contributors from NVIDIA, Red Hat, Docker and Canonical have worked on OpenShell "since its inception". The project has adopted the CNCF Code of Conduct, runs a public RFC process, and follows a governance model "with explicit vendor-neutrality commitments". NVIDIA's core engineering continues.[^openshell-cncf-2026]
- **Move to a neutral organization:** the code moves from NVIDIA's GitHub repository to the neutral `ai-openshell` organization. Working groups and SIGs will form around integrated components and cross-cutting topics such as observability. OpenShell exposes extension points for providers, compute, governance and approval workflows, policy enforcement, isolation and credential management, so teams can adopt it incrementally.[^openshell-cncf-2026]
- **Where help is wanted:** reference extensions with conformance tests, real-world policy patterns (approval flows, egress rules, per-tenant policies) and feedback on the Cedar approach. Also wanted: isolation coverage across Linux, macOS and Kubernetes (including confidential computing), metrics, traces and audit events "aligned with OpenTelemetry", and release engineering (reproducible builds, SBOMs, signing), which "support Incubation requirements".[^openshell-cncf-2026]

## Citation Notable

> "Agents are becoming part of cloud native infrastructure, and the layer that governs them should be shared, vendor-neutral, and open to everyone who depends on it." — Jonathan Bryce & Ali Golshan

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-openshell-cncf-2026]] | argues-that | [[project:openshell]] |
| [[source:ai-protocols-openshell-cncf-2026]] | contrasts-with | [[project:agent-substrate]] |
| [[source:ai-protocols-openshell-cncf-2026]] | contrasts-with | [[source:ai-protocols-strands-box-sandboxes-2026]] |
| [[source:ai-protocols-openshell-cncf-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [OpenShell](../projects/openshell.md): the project this post welcomes. The project page adds the architecture (gateway, supervisor, sandbox), the YAML policy model and prover, the SDKs and the dated status from the repository and CNCF records.
- [Agent Substrate](../projects/agent-substrate.md): another CNCF Sandbox agent runtime, originally created by Google. *Editorial contrast: the post does not mention it.* Substrate multiplexes suspended actors onto warm Kubernetes workers. OpenShell puts a trusted supervisor outside each sandbox and mediates every network request against policy.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](ai-protocols-strands-box-sandboxes-2026.md): the closest design already in the wiki, also an editorial comparison. Both keep real credentials out of the agent and enforce policy at the network boundary. Box's policy language, Dogwood, extends Cedar; OpenShell plans to adopt Cedar itself.
- [Introducing Dogwood: runtime verification for AI agents](ai-protocols-dogwood-runtime-verification-2026.md): extends Cedar with temporal operators. Cedar is now named by this post as well as by the Dogwood and Strands Box fiches.
- [Agent Sandbox](../projects/agent-sandbox.md): kubernetes-sigs `Sandbox` CRD. Its page holds the wiki's sandbox comparison table, which has no OpenShell row yet.
- [OpenTelemetry (OTel)](../concepts/opentelemetry-otel.md): the post asks for metrics, traces and audit events aligned with OpenTelemetry.
- [AI Protocols](../domains/ai-protocols.md): adds a governance-focused agent runtime under CNCF to the cluster.

[^openshell-cncf-2026]: Jonathan Bryce (CNCF) & Ali Golshan (NVIDIA), "Welcoming OpenShell to the CNCF: Open Governance to Secure Agentic AI", CNCF Blog, 2026-11-10, read 2026-11-13.
