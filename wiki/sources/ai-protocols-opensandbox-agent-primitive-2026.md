---
type: source
title: "The Sandbox as an Agent Primitive"
description: AAIF post arguing agents should request isolated execution environments through a common, runtime-neutral interface; presents OpenSandbox (Apache 2.0, Docker + Kubernetes) as the implementation.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aaif.io/blog/the-sandbox-as-an-agent-primitive
    id: opensandbox-aaif-2026
    title: "The Sandbox as an Agent Primitive (AAIF Blog)"
generated: {by: anthropic/claude-sonnet-5, at: 2026-10-27T00:00:00Z}
verified: []
stale_after: 2027-04-27T00:00:00Z
updated: 2026-10-27
tags: [sandbox, agents, isolation, docker, kubernetes, aaif, opensandbox]
---

# The Sandbox as an Agent Primitive

**Auteur :** Agentic AI Foundation · **Publié :** 2026-10-22 · **Lien :** https://aaif.io/blog/the-sandbox-as-an-agent-primitive
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~10 min

## En Bref

Agents need isolated execution environments, but tying that need to one provider's bespoke API
locks agents to that provider. The post argues for a common, runtime-neutral sandbox interface
and presents [OpenSandbox](https://aaif.io) — now an Agentic AI Foundation project — as that
interface, split into a lifecycle API and an execution API, backed by Docker or Kubernetes.

## Points Clés

- **OpenSandbox** is an open-source (Apache 2.0) agent isolation platform, now an Agentic AI
  Foundation project, with SDKs for multiple languages and Docker + Kubernetes runtime support.
- The **sandbox protocol** is a pair of OpenAPI specs: a **lifecycle API** (create, pause, resume,
  renew, snapshot, delete) and an **execution API** (commands, code, files, sessions, resource
  measurements).
- Sandbox creation is **asynchronous** — the lifecycle server validates the request, then hands
  provisioning to the configured runtime, which creates a Docker container or Kubernetes workload.
- A daemon, **`execd`**, runs inside every sandbox and carries out the commands and file
  operations the agent sends through the SDK.
- The interface is uniform across runtimes: agents issue the same operations whether the sandbox
  is backed by Docker or Kubernetes, even though the two runtimes provision differently underneath.

## Citation Notable

> "The agent shouldn't have to." — Agentic AI Foundation

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-opensandbox-agent-primitive-2026]] | contrasts-with | [[source:ai-protocols-strands-box-sandboxes-2026]] |
| [[source:ai-protocols-opensandbox-agent-primitive-2026]] | created-by | [[organization:agentic-ai-foundation]] |
| [[source:ai-protocols-opensandbox-agent-primitive-2026]] | extends | [[domain:ai-protocols]] |
| [[source:ai-protocols-opensandbox-agent-primitive-2026]] | argues-that | [[concept:tool-use-function-calling]] |

## Liens Wiki

- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](ai-protocols-strands-box-sandboxes-2026.md) — contrasting sandbox approach: Box is OS-level containment (macOS Seatbelt) plus policy; OpenSandbox is a runtime-neutral provisioning/execution API over Docker/Kubernetes — the two don't compete on the same axis (containment vs. provisioning interface).
- [AI Protocols](../domains/ai-protocols.md) — adds a provider-neutral execution-environment layer to the stack.
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — the sandbox execution API is the surface an agent calls to run code/commands as a tool effect.
