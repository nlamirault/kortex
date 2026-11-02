---
type: source
title: "Running Agents on Kubernetes with Agent Sandbox"
description: Kubernetes blog post introducing Agent Sandbox, a SIG Apps project giving isolated, stateful, singleton AI-agent workloads a declarative Sandbox CRD (gVisor/Kata isolation, scale-to-zero, stable identity) plus warm-pool extensions.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
    id: agent-sandbox-blog-2026
    title: "Running Agents on Kubernetes with Agent Sandbox (Kubernetes Blog)"
    author: Janet Kuo, Justin Santa Barbara
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-02T00:00:00Z}
verified: []
stale_after: 2027-05-02T00:00:00Z
updated: 2026-11-02
tags: [sandbox, agents, kubernetes, crd, isolation, gvisor, kata-containers, sig-apps, agent-sandbox]
---

# Running Agents on Kubernetes with Agent Sandbox

**Auteur :** Janet Kuo, Justin Santa Barbara · **Publié :** 2026-03-20 · **Lien :** https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

AI agents are isolated, stateful, singleton workloads: mostly idle, active in short bursts, and
writing and running untrusted code. Standard Kubernetes primitives only fit that shape if you
hand-assemble a StatefulSet, a headless Service and a PersistentVolumeClaim for each agent. The
post introduces [Agent Sandbox](../projects/agent-sandbox.md), a SIG Apps project that gives this
workload a declarative `Sandbox` CRD. It argues that, with this primitive, Kubernetes becomes the
natural host for long-running agents.[^agent-sandbox-blog-2026]

## Points Clés

- **Abstraction gap:** an agent needs a persistent identity, a secure scratchpad for untrusted code, and a lifecycle that can suspend and resume quickly. A StatefulSet of size 1 plus a headless Service plus a PVC per agent comes close, but it does not scale operationally.[^agent-sandbox-blog-2026]
- **`Sandbox` CRD (core):** a lightweight, single-container environment built on Kubernetes primitives. It offers strong isolation through runtimes such as gVisor or Kata Containers (kernel and network isolation for multi-tenant untrusted execution). It can scale idle sandboxes to zero and resume them where they left off. It also gives each sandbox a stable hostname and network identity, so agents can discover and talk to each other.[^agent-sandbox-blog-2026]
- **Extensions API layer (optional):** kept separate so it can change faster. Starting a pod adds about a second, which breaks an interaction when an idle agent is invoked. `SandboxWarmPool` keeps Sandbox pods pre-provisioned to remove that cold start. A caller issues a `SandboxClaim` against a `SandboxTemplate`, and the controller hands over a pre-warmed, isolated environment.[^agent-sandbox-blog-2026]
- **Install:** the core components and the extensions ship as separate release manifests (`manifest.yaml`, and an optional `extensions.yaml`), both applied with `kubectl` at a pinned release tag. An optional Python SDK installs from PyPI as `k8s-agent-sandbox`. The authors recommend the latest release "as the project is moving fast".[^agent-sandbox-blog-2026]
- **Status (as of 2026-03-20):** "currently in development under SIG Apps", open source and community-driven, discussed in the `#sig-apps` and `#agent-sandbox` Kubernetes Slack channels. The post gives no maturity level, API group/version or license.[^agent-sandbox-blog-2026]

## Citation Notable

> "While you could theoretically approximate this by stringing together a StatefulSet of size 1, a headless Service, and a PersistentVolumeClaim for every single agent, managing this at scale becomes an operational nightmare." — Janet Kuo & Justin Santa Barbara

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-agent-sandbox-kubernetes-2026]] | argues-that | [[project:agent-sandbox]] |
| [[source:ai-protocols-agent-sandbox-kubernetes-2026]] | contrasts-with | [[source:ai-protocols-opensandbox-agent-primitive-2026]] |
| [[source:ai-protocols-agent-sandbox-kubernetes-2026]] | contrasts-with | [[source:ai-protocols-strands-box-sandboxes-2026]] |
| [[source:ai-protocols-agent-sandbox-kubernetes-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Agent Sandbox](../projects/agent-sandbox.md) — the project this post introduces. The project page adds the SDKs, use cases and isolation backends listed on the project site.
- [The Sandbox as an Agent Primitive](ai-protocols-opensandbox-agent-primitive-2026.md) — a contrasting sandbox design. *Editorial comparison: neither source cites the other.* OpenSandbox is an imperative OpenAPI that hides the *provisioning runtime* (Docker or Kubernetes) from the agent. Agent Sandbox runs only on Kubernetes, is declarative (a CRD plus a controller), and hides the *isolation backend* (gVisor or Kata). Neither source says whether OpenSandbox's Kubernetes runtime uses these CRDs. This post (2026-03-20) also predates the OpenSandbox AAIF post (2026-10-22).
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](ai-protocols-strands-box-sandboxes-2026.md) — contrasting, also an editorial comparison. Box contains the agent at the OS level on a developer's machine (starting with macOS Seatbelt) and adds Dogwood policy at its enforcement points. Agent Sandbox provides kernel and network isolation in the cluster through gVisor or Kata, and the post describes no policy layer.
- [AI Protocols](../domains/ai-protocols.md) — adds a Kubernetes-native execution-environment layer next to OpenSandbox and Strands Box.

[^agent-sandbox-blog-2026]: Janet Kuo & Justin Santa Barbara, "Running Agents on Kubernetes with Agent Sandbox", Kubernetes Blog, 2026-03-20.
