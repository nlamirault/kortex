---
type: project
title: Agent Sandbox
description: Kubernetes SIG Apps project (kubernetes-sigs/agent-sandbox) giving isolated, stateful, singleton AI-agent workloads a declarative Sandbox CRD, pluggable gVisor/Kata isolation, warm-pool extensions, and Python/Go SDKs.
resource: https://github.com/kubernetes-sigs/agent-sandbox
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agent-sandbox.sigs.k8s.io/
    id: agent-sandbox-site-2026
    title: "Agent Sandbox (project site)"
  - resource: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
    id: agent-sandbox-blog-2026
    title: "Running Agents on Kubernetes with Agent Sandbox (Kubernetes Blog)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-02T00:00:00Z}
verified: []
stale_after: 2027-05-02T00:00:00Z
updated: 2026-11-13
tags: [agent-sandbox, sandbox, kubernetes, crd, gvisor, kata-containers, sig-apps, agents, sdk]
---

# Agent Sandbox

**Kind:** codebase (Kubernetes CRDs + controller + client SDKs) · **Lifecycle:** experimental (in development as of 2026-03-20)
**URL:** https://agent-sandbox.sigs.k8s.io/ · **Repo:** https://github.com/kubernetes-sigs/agent-sandbox

## What It Does

Agent Sandbox provides "a secure and isolated execution layer to safely deploy autonomous AI
agents on Kubernetes that generate and run untrusted code at scale".[^agent-sandbox-site-2026] It
is developed under Kubernetes SIG Apps.[^agent-sandbox-blog-2026] It targets a workload the
launch post calls isolated, stateful and singleton: a mostly idle agent workspace that needs a
persistent identity and a scratchpad for untrusted code. Without it, each agent would need its
own hand-wired StatefulSet of size 1, headless Service and PVC.[^agent-sandbox-blog-2026] The
reasoning behind it is captured in the
[launch post fiche](../sources/ai-protocols-agent-sandbox-kubernetes-2026.md).

**Core vs. extensions.** The core is the `Sandbox` CRD, a lightweight single-container
environment. It has pluggable isolation runtimes, can scale to zero and resume, and keeps a
stable hostname and network identity. The blog's separate Extensions API layer presents three
more resources: `SandboxTemplate` and `SandboxClaim` let a caller claim a sandbox, and
`SandboxWarmPool` keeps pre-provisioned pods so the claim skips the roughly one-second pod cold
start. Releases ship the core components (`manifest.yaml`) and the optional extensions components
(`extensions.yaml`) as separate manifests; the blog does not list which resources each one
contains.[^agent-sandbox-blog-2026]

**Isolation is separate from the API.** The site describes a standardized Kubernetes API that
"fully decouples the execution layer from the underlying isolation technology". It documents two
backends:[^agent-sandbox-site-2026]

- **[gVisor](gvisor.md):** a userspace kernel that intercepts system calls to protect the host.
- **Kata Containers:** hardware virtualization with a dedicated kernel per sandbox, using Kata
  Containers and QEMU.

**SDKs.** Both quickstarts create a sandbox from a named warm pool and run a command in it.

- **Python:** PyPI package `k8s-agent-sandbox`,[^agent-sandbox-blog-2026] imported as
  `k8s_agent_sandbox`. `SandboxClient().create_sandbox(warmpool=…, namespace=…)` returns a
  sandbox with `commands.run(…)` and `terminate()`.[^agent-sandbox-site-2026] In the repo, the
  client lives under `clients/python/agentic-sandbox-client`, a different name from the PyPI
  package.[^agent-sandbox-blog-2026]
- **Go:** module `sigs.k8s.io/agent-sandbox/clients/go/sandbox`, with
  `sandbox.NewClient(ctx, sandbox.Options{WarmPoolName, Namespace})`, `CreateSandbox`, `Run` and
  `DeleteAll`.[^agent-sandbox-site-2026] Only the site shows the Go SDK; the March post mentions
  just Python.

**Use cases, grouped by how long the sandbox lives** (as listed on the site):[^agent-sandbox-site-2026]

| Sandbox lifetime | Use case |
|------------------|----------|
| Short-lived | Code execution: code interpreters, analytics tools, on-demand computation |
| Medium-lived | Coding agents (write, debug and refactor with full dev tooling); computer use (graphical desktops, browsers, GUI apps) |
| Short to medium-lived | CI/CD: isolated testing, validation, automated workflows |
| Always-lived | Agents in Sandbox (OpenClaw): always-on, persistent, long-running agent environments |

**Status and community.** As of 2026-03-20 the project was "currently in development under SIG
Apps".[^agent-sandbox-blog-2026] When read on 2026-11-02, the site gave no maturity level. Neither
source states an API group/version or the code license; the site's documentation is distributed
under CC BY 4.0. Contributions go through GitHub pull requests, discussion happens in the
`#agent-sandbox` Kubernetes Slack channel, and there is a sig-apps mailing
group.[^agent-sandbox-site-2026]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:agent-sandbox]] | implements | [[source:ai-protocols-agent-sandbox-kubernetes-2026]] |
| [[project:agent-sandbox]] | part-of | [[domain:ai-protocols]] |

## Relevance to Kortex

This was the third agent sandbox in the AI Protocols cluster and the first one native to
Kubernetes. [Agent Substrate](agent-substrate.md) (ingested the same day) is the fourth and the
second on Kubernetes. Each hides something different from the agent. *This is an editorial
comparison: no source compares them.*

| | Where it runs | What it hides behind its interface | Isolation | Policy layer |
|---|---|---|---|---|
| [Strands Box](../sources/ai-protocols-strands-box-sandboxes-2026.md) | The developer's machine | Nothing; one local runtime | OS containment (macOS Seatbelt first) | Dogwood at the network, shell, Python and MCP boundaries |
| [OpenSandbox](../sources/ai-protocols-opensandbox-agent-primitive-2026.md) | Docker or Kubernetes | The provisioning runtime, behind lifecycle and execution OpenAPIs | Not described in its fiche | Not described |
| **Agent Sandbox** | Kubernetes only | The isolation backend, behind a declarative CRD and controller | [gVisor](gvisor.md) (userspace kernel) or Kata Containers (VM per sandbox) | None described |
| [Agent Substrate](agent-substrate.md) | Kubernetes 1.37+ (worker pods only) | Which worker an actor runs on: actors suspend to snapshots and resume on any warm pod, behind a gRPC API kept off the Kubernetes API path | [gVisor](gvisor.md) (`runsc`) or Kata Containers on Cloud Hypervisor (KVM microVM); plain containers unsupported | Built in: `EgressPolicy` allowlists, OpenFGA authorization, egress credential injection, SPIFFE identity |

It is also the first `kubernetes-sigs` project in the wiki and a seed for a future Kubernetes
domain (queued).

## Related

- [Running Agents on Kubernetes with Agent Sandbox](../sources/ai-protocols-agent-sandbox-kubernetes-2026.md) — launch post fiche (why agents need a new Kubernetes primitive).
- [The Sandbox as an Agent Primitive](../sources/ai-protocols-opensandbox-agent-primitive-2026.md) — OpenSandbox (AAIF), a sandbox API that works across runtimes.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md) — local OS containment plus Dogwood policy.
- [Agent Substrate](agent-substrate.md) — CNCF Sandbox runtime multiplexing suspended actors onto warm Kubernetes workers; the opposite design choice (workload state out of the Kubernetes API).
- [gVisor](gvisor.md) — user-space application kernel (`runsc`, written in Go) selected through `runtimeClassName: gvisor`; CNCF Sandbox project since 2026.
- [AI Protocols](../domains/ai-protocols.md) — domain cluster.

[^agent-sandbox-site-2026]: Agent Sandbox project site, https://agent-sandbox.sigs.k8s.io/, read 2026-11-02.
[^agent-sandbox-blog-2026]: Janet Kuo & Justin Santa Barbara, "Running Agents on Kubernetes with Agent Sandbox", Kubernetes Blog, 2026-03-20.
