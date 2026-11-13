---
type: project
title: Agent Substrate
description: CNCF Sandbox runtime donated by Google (1.0 and GA on GKE since 2026-11-05) that multiplexes many stateful, sandboxed agent "actors" onto a small pool of warm Kubernetes worker pods, suspending idle actors to snapshot storage and resuming them on any worker, with zero ambient credentials and default-deny networking.
resource: https://github.com/agent-substrate/substrate
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://ate.dev/
    id: ate-site-2026
    title: "Agent Substrate (project site)"
  - resource: https://ate.dev/llms.txt
    id: ate-llms-2026
    title: "Agent Substrate llms.txt (architecture summary + docs map)"
  - resource: https://ate.dev/llms-full.txt
    id: ate-docs-2026
    title: "Agent Substrate documentation bundle (Overview, Architecture and Sandbox Classes pages)"
  - resource: https://github.com/agent-substrate/substrate
    id: ate-repo-2026
    title: "agent-substrate/substrate (GitHub repository metadata)"
  - resource: https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en
    id: google-cncf-2026
    title: "Powering open infrastructure for autonomous agents (Google Cloud Blog)"
    author: Drew Bradstock
  - resource: https://github.com/cncf/sandbox/issues/523
    id: cncf-sandbox-523
    title: "[Sandbox] Agent Substrate (CNCF sandbox application issue metadata)"
  - resource: https://github.com/agent-substrate/substrate/releases
    id: ate-releases-2026-11
    title: "agent-substrate/substrate releases (re-read 2026-11-13)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:10:47Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [agent-substrate, sandbox, kubernetes, gke, gvisor, kata-containers, cloud-hypervisor, microvm, spiffe, suspend-resume, cncf, agents]
---

# Agent Substrate

**Kind:** codebase (control plane + data plane on Kubernetes, `kubectl ate` plugin, gRPC API) · **Lifecycle:** 1.0; `v1.0.0` released 2026-11-05,[^ate-releases-2026-11] GA as "Agent Substrate on GKE" the same day[^google-cncf-2026]
**URL:** https://ate.dev/ · **Repo:** https://github.com/agent-substrate/substrate · **License:** Apache-2.0[^ate-repo-2026] · **GKE:** https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate[^google-cncf-2026]

## What It Does

Agent Substrate is "a secure-by-default runtime for running agents at scale".[^ate-site-2026] Its
llms.txt describes it as "an open source, zero-trust runtime for running millions of stateful
sandboxed agents on Kubernetes with sub-500ms suspend and resume".[^ate-llms-2026] It starts from
the premise that agents are bursty. They spend most of their time waiting for input, run
untrusted logic, and so end up as many single-tenant sandboxes.[^ate-docs-2026] Its docs use
**actor** for one instance of such an "agent-like" workload, which need not be an AI
agent.[^ate-docs-2026]

**Actors multiplexed onto workers.** A larger set of stateful actors is mapped onto a smaller pool
of pre-warmed workers. Actors are addressed as `<atespace>/<actor>` and created from an
`ActorTemplate`. Workers are Kubernetes Pods in a `WorkerPool`.[^ate-llms-2026] An idle actor
checkpoints its memory and filesystem state to object storage (GCS or S3) and releases its
compute.[^ate-llms-2026] A request names its target in the `ate-target-actor: <atespace>/<actor>`
header. `atenet-router` holds ("parks") the request while `ate-api-server` assigns a ready worker,
`atelet` streams the snapshot onto the node, and `ateworker` restores the
sandbox.[^ate-llms-2026] The workers are started in advance so that a resume never waits on the
Kubernetes scheduler.[^ate-docs-2026] The landing page calls resuming on any worker in the pool
**Actor Teleport**. Its demo runs about 250 actors on 8 worker pods.[^ate-site-2026] Google's CNCF
post uses three terms for the same model. **Actors** hold "each agent's memory, files, and
discrete identity". **Workers** are "reusable execution sandboxes drawn from a warm Kubernetes
pool". **Gateways** enforce inbound and outbound access control and inject secrets based on Actor
identity.[^google-cncf-2026]

**The Kubernetes API stays off the request path.** Kubernetes provisions nodes and worker pods,
which are low-frequency operations. Substrate's own control plane handles high-rate
suspend/resume and scheduling.[^ate-docs-2026] The landing page asks for any Kubernetes **1.37+**
cluster.[^ate-site-2026] Google's post says the open-source code deploys "on any Kubernetes
cluster" and gives no version floor.[^google-cncf-2026] *Editorial reading:* that phrase claims
provider neutrality, not support below 1.37, so the two are not treated as conflicting. Resources
come in two kinds:[^ate-llms-2026]

- **Infrastructure:** `WorkerPool`, `SandboxConfig` and `CSIDriverConfig` are `ate.dev/v1`
  Kubernetes CRDs, reconciled by `atecontroller` and managed with `kubectl`.
- **Workloads and access:** `Atespace`, `ActorTemplate`, `Actor`, `Tag`, `EgressPolicy` and
  `AccessPolicy` live in PostgreSQL behind the gRPC Control API of `ate-api-server`. They are
  managed with `kubectl ate` or gRPC clients.

**Two sandbox classes, and no plain containers.** Each actor runs in a sandbox. "Plain Linux
containers are unsupported".[^ate-llms-2026] Each `WorkerPool` runs one class:[^ate-docs-2026]

- **`gvisor`:** a user-space kernel (`runsc`) that runs on a standard Linux node.
- **`microvm`:** a KVM guest, where Kata Containers runs on the Cloud Hypervisor VMM. Nodes must
  expose `/dev/kvm`.

An actor's first snapshot records which class it ran on, and every later restore uses a worker of
that same class.[^ate-docs-2026] Google's post names the same two boundaries, "Cloud Hypervisor
microVMs or gVisor", and does not mention Kata.[^google-cncf-2026]

**Security model ("zero trust for agents").** Every agent "has an identity, but no credentials,
no open network, and no escape from the sandbox".[^ate-site-2026]

- **Identity:** each actor has a short-lived SPIFFE X.509 certificate and on-demand JWTs.[^ate-site-2026]
- **No credentials in the sandbox:** the egress gateway pulls secrets from pluggable stores and
  injects them into authorized outbound calls, so the agent never holds a
  secret.[^ate-site-2026][^google-cncf-2026]
- **Egress path:** traffic goes through `atunnel`, authenticated with the per-actor certificate,
  to `atenet-egress`. That component enforces `EgressPolicy` host allowlists.[^ate-llms-2026] A
  tutorial covers using Envoy or agentgateway as the egress proxy.[^ate-llms-2026]
- **Default-deny networking:** an actor has no inbound access, no peer-to-peer traffic and no
  path to the control plane. Inbound calls must authenticate at the router.[^ate-site-2026]
- **Authorization:** `ate-api-server` checks every call against an OpenFGA model.[^ate-llms-2026]
- **Single tenancy:** local worker state is scrubbed between runs.[^ate-site-2026]

**Workloads it runs.** An actor is "a standard OCI container whose memory and filesystem persist
across requests". The landing page lists Agent Development Kit, LangChain, Claude Code, Codex,
Hermes, OpenClaw, Antigravity and MCP servers. It names two projects built on Substrate: Agent
Executor (`google/ax`) and kagent (CNCF Sandbox).[^ate-site-2026] One tutorial runs three Claude
Code agents on two worker pods.[^ate-llms-2026] Google's post adds: "Early design partners like
Nous Research are building Hermes Enterprise on it, and it already powers other CNCF projects like
kagent". No source says whether Hermes Enterprise is related to the Hermes on the landing page's
framework list. The post also quotes Tamir Magen, CEO of SPIRITT, on running every customer's
agents on Agent Substrate on GKE.[^google-cncf-2026]

**Figures the project reports.** It reports these on the landing page without methodology: under
500 ms to resume a suspended actor on any ready worker, more than 500 suspend/resume activations
per second, and "10× higher density than standard container runtimes".[^ate-site-2026] Google's
post repeats all three. It says reaching 1.0 "shows that Agent Substrate can accept production
workloads across millions of sandboxes", again without methodology.[^google-cncf-2026] Treat
them as vendor-reported figures.

**Operations.** The docs map includes guides for observability, SLOs and Prometheus alerting, and
rolling upgrades. Emitted metrics and log events are defined in an OpenTelemetry Weaver
registry,[^ate-llms-2026] which links this project to the
[OpenTelemetry](../concepts/opentelemetry-otel.md) thread in the Observability domain. The docs
also link a GKE installation guide.[^ate-docs-2026]

**Status and governance.**

- **Maturity (timeline):**
  - On 2026-11-02 the site carried a "Pre-1.0" banner: "APIs and behavior may still change
    significantly".[^ate-site-2026] The banner has not been re-checked since the 1.0 release.
  - The repo was created on 2026-05-13 and released `v0.6.0` on 2026-10-22, then
    `v1.0.0-rc.1` on 2026-10-29. As of 2026-11-02 that release candidate was the latest
    tag.[^ate-repo-2026]
  - The repo then released `v1.0.0-rc.2` on 2026-11-04, and `v1.0.0-rc.3` and the final
    `v1.0.0` ("Fully armed and operational") on 2026-11-05.[^ate-releases-2026-11]
  - Google's post of 2026-11-05 says Agent Substrate "has reached its 1.0 milestone and is now
    generally available as Agent Substrate on GKE".[^google-cncf-2026]
- **Community:** "Since public development started in May 2026, the Agent Substrate project has
  grown to more than 100 contributors."[^google-cncf-2026] The May start matches the repo's
  creation date.[^ate-repo-2026]
- **Governance:** the site states: "We are a Cloud Native Computing Foundation sandbox project",
  and the project "was originally created by Google".[^ate-site-2026] The CNCF application issue
  "[Sandbox] Agent Substrate" (cncf/sandbox#523) was opened on 2026-09-08 and closed on 2026-10-20
  with the `gitvote/passed` label.[^cncf-sandbox-523] On 2026-11-05 Google announced the donation
  of Agent Substrate, gVisor and OpenRL to the CNCF, "following their acceptance last month into
  the CNCF Sandbox". Each project "is now working through CNCF Sandbox onboarding with community
  maintainers and independent build infrastructure".[^google-cncf-2026] The fiche records the
  rest of the announcement: [Powering open infrastructure for autonomous agents](../sources/ai-protocols-google-agents-cncf-donation-2026.md).
- **Managed offering:** with the GA of Agent Substrate on GKE, "you can run this runtime as a
  managed capability on Google Cloud or deploy the open-source code on any Kubernetes cluster".
  Google positions Substrate as complementing Agent Compute Engine, its "Titanium microVM
  service" for teams that want microVMs through an API without managing clusters. The post
  claims no integration between the two.[^google-cncf-2026]
- **Not a governance claim:** the footer line "a Series of LF Projects, LLC" is legal boilerplate.
- **Docs status:** llms.txt still marks the Architecture page "[Status: Planned]".[^ate-llms-2026]

**Design-doc drift (noted 2026-11-02):** the Architecture page reads like a design document. Its
section "Problems We Haven't Addressed Yet" still lists "Identity and policy", along with
autoscaling and peer-to-peer state sharing.[^ate-docs-2026] The landing page and llms.txt
describe SPIFFE identity, `EgressPolicy`/`AccessPolicy`, OpenFGA authorization and credential
injection as part of the system, and each has a how-to guide.[^ate-site-2026][^ate-llms-2026] A
planned design page listing open problems does not contradict those guides. Most likely the page
has simply not been updated since those features shipped, but this was not checked against the
code. Google's 1.0 announcement (2026-11-05) also describes Gateways that enforce access control
and inject secrets by Actor identity, which supports that reading.[^google-cncf-2026] The
Architecture page itself was not re-read.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:agent-substrate]] | integrates-with | [[concept:model-context-protocol-mcp]] |
| [[project:agent-substrate]] | part-of | [[domain:ai-protocols]] |

## Relevance to Kortex

This is the fourth agent sandbox in the AI Protocols cluster and the second that runs natively on
Kubernetes. The comparison table lives on the [Agent Sandbox](agent-sandbox.md#relevance-to-kortex)
page; it is not copied here. *Editorial comparison: no source compares the two projects.*
Substrate makes the opposite design choice to Agent Sandbox. Agent Sandbox represents each sandbox
as a CRD reconciled by a controller. Substrate keeps actors and policies out of the Kubernetes API
altogether: they live in PostgreSQL behind gRPC, and only worker capacity is a CRD. Both projects
use gVisor and Kata. Agent Sandbox runs Kata on QEMU and Substrate runs it on Cloud Hypervisor.
Substrate is also the first *Kubernetes-native* sandbox in the wiki with egress allowlists and
credential injection built in. Strands Box injects credentials at a gateway too, but it runs
locally and gets its policy from Dogwood.

It is the second Kubernetes-native source in the wiki, which triggers the queued Kubernetes domain
bootstrap. It is also the first ingested source that names CNCF hosting. The
[OpenTelemetry](../concepts/opentelemetry-otel.md) page's CNCF claim comes from recall and is
marked `NOT VERIFIED`. Google's CNCF donation post (2026-11-05) is a second source for CNCF
hosting, which makes the CNCF a promotion candidate in the ingest queue.

## Related

- [Powering open infrastructure for autonomous agents](../sources/ai-protocols-google-agents-cncf-donation-2026.md): Google Cloud blog fiche (2026-11-05). Donation to the CNCF, Sandbox onboarding, 1.0 and GA on GKE.
- [Agent Sandbox](agent-sandbox.md): kubernetes-sigs `Sandbox` CRD with gVisor/Kata backends and warm pools. Holds the canonical sandbox comparison table.
- [The Sandbox as an Agent Primitive](../sources/ai-protocols-opensandbox-agent-primitive-2026.md): OpenSandbox (AAIF), a lifecycle and execution API that works across runtimes.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md): local OS containment plus Dogwood policy.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md): MCP servers are among the workloads Substrate runs as actors.
- [OpenTelemetry (OTel)](../concepts/opentelemetry-otel.md): Substrate defines its metrics and log events as an OTel Weaver registry.
- [AI Protocols](../domains/ai-protocols.md): domain cluster.

[^ate-site-2026]: Agent Substrate project site, https://ate.dev/, read 2026-11-02.
[^ate-llms-2026]: Agent Substrate llms.txt, https://ate.dev/llms.txt, read 2026-11-02.
[^ate-docs-2026]: Agent Substrate documentation bundle, https://ate.dev/llms-full.txt, read 2026-11-02. Only these pages were used: Overview (`/docs/get-started/overview/`, GKE guide link), Architecture (`/docs/concepts/architecture/`, marked "[Status: Planned]" in llms.txt: problem statement, actor/worker decoupling, focused control plane, open problems, ateworker sandbox runtimes) and Sandbox Classes (`/docs/reference/sandbox-classes/`).
[^ate-repo-2026]: GitHub repository metadata for agent-substrate/substrate (license, creation date, release tags), https://github.com/agent-substrate/substrate, read 2026-11-02.
[^google-cncf-2026]: Drew Bradstock, "Powering open infrastructure for autonomous agents", Google Cloud Blog, 2026-11-05, https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en, read 2026-11-13. Fiche: [Powering open infrastructure for autonomous agents](../sources/ai-protocols-google-agents-cncf-donation-2026.md).
[^cncf-sandbox-523]: GitHub issue metadata for cncf/sandbox#523 "[Sandbox] Agent Substrate" (state, created and closed timestamps, labels), https://github.com/cncf/sandbox/issues/523, read 2026-11-13. The issue thread itself was not read.
[^ate-releases-2026-11]: GitHub releases for agent-substrate/substrate (tag names, release names, publication timestamps), https://github.com/agent-substrate/substrate/releases, re-read 2026-11-13. `v1.0.0` was published at 2026-11-05T23:55:26Z.
