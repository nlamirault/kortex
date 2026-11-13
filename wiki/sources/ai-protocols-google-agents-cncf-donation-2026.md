---
type: source
title: "Powering open infrastructure for autonomous agents"
description: Google Cloud blog post (2026-11-05) announcing the donation of Agent Substrate, gVisor and OpenRL to the CNCF after their CNCF Sandbox acceptance, with Agent Substrate reaching 1.0 and going GA on GKE.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en
    id: google-cncf-2026
    title: "Powering open infrastructure for autonomous agents (Google Cloud Blog)"
    author: Drew Bradstock
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:10:47Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [agent-substrate, gvisor, openrl, cncf, cncf-sandbox, gke, google, kubernetes, sandbox, agents, rl-post-training]
---

# Powering open infrastructure for autonomous agents

**Auteur :** Drew Bradstock (VP Product Management, Orchestration & Kubernetes, Google Cloud) · **Publié :** 2026-11-05 · **Lien :** https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~8 min (estimate)

## En Bref

Google announces the donation of three projects that started at Google to the CNCF: [Agent
Substrate](../projects/agent-substrate.md), gVisor and OpenRL. The post argues that agents running
at scale need the same open foundation and neutral governance that Kubernetes and the CNCF gave
containers in the 2010s. It also marks Agent Substrate 1.0 and its general availability as
"Agent Substrate on GKE".[^google-cncf-2026]

## Points Clés

- **Donation and onboarding:** "Today, we are announcing the donation of Agent Substrate, gVisor, and OpenRL, three open source projects that started at Google, to the CNCF following their acceptance last month into the CNCF Sandbox." Each project "is now working through CNCF Sandbox onboarding with community maintainers and independent build infrastructure". The post gives no exact acceptance date.[^google-cncf-2026]
- **Agent Substrate 1.0 and GKE GA:** the post splits the runtime into **Actors** (each agent's memory, files and identity), **Workers** ("reusable execution sandboxes drawn from a warm Kubernetes pool") and **Gateways** (inbound and outbound access control, plus secrets injected by Actor identity). An Actor is restored onto any Worker "in under 500 milliseconds". Isolation is "Cloud Hypervisor microVMs or gVisor". GA means a managed capability on Google Cloud, or the open-source code on "any Kubernetes cluster". The post also claims more than 100 contributors since public development started in May 2026, Nous Research building Hermes Enterprise on it, and kagent running on it. Its 10x density and 500+ activations per second figures come without a methodology.[^google-cncf-2026]
- **gVisor:** open sourced by Google in 2018, it is "a lightweight application kernel written in Go" and runs "millions of sandboxes every day underneath GKE Sandbox and Cloud Run". Ant Group, Modal and Tines have committed to join its maintainers. OpenAI, Tencent and NVIDIA continue to contribute. It is "on a path toward Incubation".[^google-cncf-2026]
- **OpenRL:** "a clean, self-hosted Python post-training loop directly to your Kubernetes cluster". A training loop uses four primitives (`sample`, `forward_backward`, `optim_step`, `save_state`) "through a Tinker compatible API". It "started in February as a research preview"; the post does not give the year.[^google-cncf-2026]
- **Positioning:** "Donating Agent Substrate, gVisor, and OpenRL to the CNCF reaffirms Google's commitment to open collaboration and co-investment." Google expects adoption to follow the Kubernetes pattern. For teams that want microVMs through an API without running clusters, Agent Substrate "complements" Agent Compute Engine, described as Google's "Titanium microVM service". The post claims no integration between the two.[^google-cncf-2026]

## Citation Notable

> "Vendor-neutral ownership lets cloud providers, hardware vendors, and independent software companies participate in the future growth of agentic workloads equally." — Drew Bradstock (Google Cloud)

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-google-agents-cncf-donation-2026]] | argues-that | [[project:agent-substrate]] |
| [[source:ai-protocols-google-agents-cncf-donation-2026]] | contrasts-with | [[source:ai-protocols-aaif-four-new-projects-2026]] |
| [[source:ai-protocols-google-agents-cncf-donation-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Agent Substrate](../projects/agent-substrate.md): the project page now records the 1.0 release, the GKE GA and the CNCF onboarding from this post. It reconciles them with the ate.dev reading of 2026-11-02 (pre-1.0, `v1.0.0-rc.1`).
- [Agentic AI Foundation Announces Four New Projects](ai-protocols-aaif-four-new-projects-2026.md): a contrasting foundation donation. *Editorial comparison: neither post cites the other.* OpenSandbox, a sandbox lifecycle API, went to AAIF on 2026-10-22. Agent Substrate, a sandbox runtime, goes to the CNCF in this post.
- [Agent Sandbox](../projects/agent-sandbox.md): not mentioned in the post. Do not confuse it with **GKE Sandbox**, the GKE feature the post says runs on gVisor.
- [AI Protocols](../domains/ai-protocols.md): agent runtime infrastructure under CNCF governance.

[^google-cncf-2026]: Drew Bradstock, "Powering open infrastructure for autonomous agents", Google Cloud Blog, 2026-11-05 (HTML title: "Open infrastructure for autonomous agents comes to CNCF"), https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en, read 2026-11-13.
