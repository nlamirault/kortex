---
type: project
title: gVisor
description: Open-source application kernel written in Go (OCI runtime `runsc`) that services container system calls in user space so untrusted code never talks to the host kernel directly; originally created by Google, accepted into the CNCF Sandbox in 2026 and used as an isolation backend by Agent Sandbox and Agent Substrate.
resource: https://github.com/google/gvisor
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en
    id: google-cncf-agents-2026
    title: "Powering open infrastructure for autonomous agents (Google Cloud Blog, section \"Isolate untrusted agent code with gVisor\")"
    author: Drew Bradstock
  - resource: https://gvisor.dev/
    id: gvisor-site-2026
    title: "gVisor (project home page)"
  - resource: https://gvisor.dev/docs/
    id: gvisor-docs-2026
    title: "What is gVisor? (gVisor docs)"
  - resource: https://gvisor.dev/docs/architecture_guide/security/
    id: gvisor-security-2026
    title: "Security Model (gVisor docs)"
  - resource: https://gvisor.dev/docs/architecture_guide/platforms/
    id: gvisor-platforms-2026
    title: "Platform Guide (gVisor docs)"
  - resource: https://gvisor.dev/docs/user_guide/checkpoint_restore/
    id: gvisor-checkpoint-2026
    title: "Checkpoint/Restore (gVisor docs)"
  - resource: https://gvisor.dev/blog/2026/10/02/gvisor-cncf/
    id: gvisor-cncf-blog-2026
    title: "gVisor is being donated to CNCF (gVisor blog)"
    author: Etienne Perot & Jing Chen
  - resource: https://gvisor.dev/community/governance/
    id: gvisor-governance-2026
    title: "gVisor governance (community page)"
  - resource: https://github.com/google/gvisor
    id: gvisor-repo-2026
    title: "google/gvisor (GitHub repository metadata, releases, MAINTAINERS.md)"
  - resource: https://github.com/cncf/sandbox/issues/521
    id: cncf-sandbox-521-2026
    title: "[Sandbox] gVisor (CNCF Sandbox application issue #521)"
  - resource: https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/
    id: agent-sandbox-gvisor-2026
    title: "gVisor Isolation (Agent Sandbox docs)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:09:02Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [gvisor, runsc, sandbox, isolation, application-kernel, oci-runtime, kubernetes, checkpoint-restore, cncf, agents]
---

# gVisor

**Kind:** codebase (application kernel + OCI runtime `runsc`) · **Lifecycle:** active; CNCF Sandbox, onboarding in progress as of 2026-11-05
**URL:** https://gvisor.dev/ · **Repo:** https://github.com/google/gvisor · **License:** Apache-2.0[^gvisor-repo-2026]

## What It Does

gVisor "is an application kernel that implements a Linux-like interface. Unlike Linux, it is
written in a memory-safe language (Go) and runs in userspace".[^gvisor-docs-2026] Its home page
now leads with "The Sandbox Kernel for Agents": a "lightweight Linux-compatible userspace kernel
to safely sandbox agents at high density without virtual machine overhead".[^gvisor-site-2026]
The GitHub description still reads "Application Kernel for Containers".[^gvisor-repo-2026]
Google's CNCF post puts the idea in one sentence: gVisor sits "between the container and the
host OS" and handles application system calls in user space "so untrusted code never talks
directly to the host kernel".[^google-cncf-agents-2026]

**`runsc`, the OCI runtime.** gVisor ships an Open Container Initiative runtime called `runsc`
that "integrates with Docker and Kubernetes".[^gvisor-docs-2026] The home page adds containerd
and says it works as "a standard Kubernetes RuntimeClass without requiring custom VM images or
hypervisor network bridges".[^gvisor-site-2026]

**Isolation model.**

- **Sentry:** the largest component, "a application kernel" that "does not pass system calls
  through to the host kernel".[^gvisor-docs-2026] Every supported call has its own
  implementation in the Sentry, and the Sentry may not open new host files or create new host
  sockets.[^gvisor-security-2026]
- **Gofer:** a host process started with each container. It talks to the Sentry over 9P (a
  socket or shared memory). The Sentry runs in a restricted seccomp container without file
  system access, so the Gofer mediates file access.[^gvisor-docs-2026] An option called
  directfs lets the sandbox open files itself.[^gvisor-security-2026]
- **Networking:** gVisor implements the Linux kernel "and its network stack using
  Go".[^gvisor-site-2026] The sandbox reads and writes packets on a virtual ethernet device,
  unless host networking is enabled or networking is off.[^gvisor-security-2026]
- **Not a filter:** gVisor "is **not a syscall filter** (e.g. `seccomp-bpf`), nor a wrapper over
  Linux isolation primitives". The docs call it "a merged guest kernel and VMM, or as seccomp on
  steroids".[^gvisor-docs-2026]
- **Defense in depth:** gVisor "sandboxes itself from the host using Linux's isolation
  capabilities".[^gvisor-site-2026] Unsafe code is confined to files ending in `unsafe.go`, CGo
  is banned (the Sentry is a pure Go binary), and the Sentry is fuzzed
  continuously.[^gvisor-security-2026]
- **Limits:** no protection against hardware side channels; resource-exhaustion defense relies
  on host cgroups; "A sandbox is not a substitute for a secure
  architecture".[^gvisor-security-2026]

**Platforms (how system calls are intercepted).**[^gvisor-platforms-2026]

| Platform | Mechanism | Status |
|----------|-----------|--------|
| `systrap` | seccomp `SECCOMP_RET_TRAP` sends `SIGSYS` to the calling thread | Default since mid-2023; better inside a VM or without virtualization support |
| KVM | Sentry acts as both guest OS and VMM | Best performance on bare metal |
| `ptrace` | `PTRACE_SYSEMU` | "no longer supported and is expected to eventually be removed" |

gVisor runs on x86 and ARM, on VMs or bare metal, and "does not require virtualization
support".[^gvisor-site-2026]

**Checkpoint/restore and accelerators.** `runsc checkpoint --image-path=<path>` saves a
container's state to a file (`--leave-running` keeps it running), and `runsc restore` starts a
new container from it. Docker's `docker checkpoint create` / `docker start --checkpoint` also
work. Restore can load data in the background. Checkpoints can be triggered from inside the
sandbox through `/proc/gvisor/checkpoint`. GPU containers are checkpointed with
cuda-checkpoint, which does not support arm64. Host-network sockets that were connected at
checkpoint time return `ECONNRESET` after restore.[^gvisor-checkpoint-2026] gVisor supports
CUDA on NVIDIA GPUs and TPUs by relaying driver operations to the host kernel drivers, with
"near-native performance and zero memory copying overhead".[^gvisor-site-2026] That figure is
project-reported.

**Trade-offs.** Isolation comes "at the price of reduced application compatibility and higher
per-system call overhead". gVisor "may provide poor performance for system call heavy
workloads", and it does not implement every system call, `/proc` file or `/sys`
file.[^gvisor-docs-2026]

**Why agents (Google's framing).** Google's post argues that agents "run generated shell
commands and unreviewed packages", and that standard containers share the host kernel, which
is "a risky bet for untrusted code". It names three reasons gVisor fits agent
fleets:[^google-cncf-agents-2026]

- **Density:** unlike VMs that preallocate RAM, memory "scales up and down with the workload".
- **GPU, TPU and snapshots:** agents can use accelerators and "pause when idle".
- **Runs anywhere Linux runs:** it needs no nested virtualization. The post cites Northflank
  sandboxing GPU workloads on it for that reason.

**Who runs it (as reported, not checked).** Google's post says gVisor was "Open sourced by
Google in 2018" and "runs millions of sandboxes every day underneath GKE Sandbox and Cloud Run".
It adds that Anthropic and OpenAI use it to contain code execution, that Modal and Snowflake run
their execution sandboxes on it, and that Ant Group and Tencent run it in production at
scale.[^google-cncf-agents-2026] The gVisor blog lists Google, Ant Group, OpenAI and Anthropic as
adopters.[^gvisor-cncf-blog-2026] The adopters' own linked pages were not read. Treat these as
vendor-reported claims.

## How Agent Sandbox and Agent Substrate Use It

Both Kubernetes-native sandboxes in the wiki offer gVisor as one of two isolation backends. The
other is Kata Containers, which has no page yet.

- **[Agent Sandbox](agent-sandbox.md)** selects gVisor per sandbox through the standard
  Kubernetes `runtimeClassName` field. A kustomize overlay injects `runtimeClassName: gvisor`
  under `spec.podTemplate.spec` of a `Sandbox` (`apiVersion: agents.x-k8s.io/v1beta1` in the
  example). The cluster needs gVisor installed first, following gVisor's Kubernetes quickstart.
  Direct pod port-forwarding does not work with gVisor or Kata runtimes, so access goes through
  the Sandbox Router with an `X-Sandbox-ID` header.[^agent-sandbox-gvisor-2026] The page names
  the RuntimeClass `gvisor` but never its handler, so it does not say `runsc` explicitly.
- **[Agent Substrate](agent-substrate.md)** offers a `gvisor` sandbox class (`runsc` on a
  standard Linux node), chosen per `WorkerPool`. An actor's first snapshot pins the class for
  every later restore (see its page). Google's post says users "can choose **Cloud Hypervisor
  microVMs** or **gVisor** as your isolation boundary without changing how you manage agent
  lifecycles".[^google-cncf-agents-2026] The gVisor home page names the link from its side: it can
  "Automatically checkpoint idle sandboxes and seamlessly resume them in milliseconds via
  integration with Agent Substrate".[^gvisor-site-2026] The gVisor blog says it "integrates
  directly with CNCF technologies such as Kubernetes, `containerd`, and Agent
  Substrate".[^gvisor-cncf-blog-2026]

*Editorial reading, not stated by any source:* Agent Sandbox treats gVisor as a pod runtime it
selects. For its `gvisor` class, Substrate also relies on gVisor's checkpoint/restore for
suspend and resume. The `microvm` class does not involve gVisor.

## CNCF Status and Governance

**Timeline.**

| Date | Event | Source |
|------|-------|--------|
| 2018 | Google open-sources gVisor under Apache 2.0 (repo created 2018-04-26) | [^gvisor-cncf-blog-2026][^gvisor-repo-2026] |
| 2026-09-07 | Google files the CNCF Sandbox application, `cncf/sandbox#521` | [^cncf-sandbox-521-2026] |
| 2026-09-22 | TOC vote called | [^cncf-sandbox-521-2026] |
| 2026-09-28 | Vote passes: 72.73% of binding voters in favor, 0% against, 66% threshold. The gVisor blog dates "The application was accepted" to this day | [^cncf-sandbox-521-2026][^gvisor-cncf-blog-2026] |
| 2026-10-02 | gVisor blog announces the donation, "including its name and trademarks" | [^gvisor-cncf-blog-2026] |
| 2026-10-28 | Onboarding issue opened; #521 closed. The issue now carries `contribution-agreement/signed`, and a 2026-09-29 comment says onboarding opens once that label is added. The timeline does not record when the label was added, so the signing date is inferred | [^cncf-sandbox-521-2026] |
| 2026-11-05 | Google announces the donation of gVisor, Agent Substrate and OpenRL "following their acceptance last month into the CNCF Sandbox" | [^google-cncf-agents-2026] |

**Two acceptance dates.** The gVisor blog dates acceptance to 2026-09-28. Google's 2026-11-05
post says "last month", which means October. The CNCF issue records both steps: the TOC vote
passed on 2026-09-28, and formal onboarding began on 2026-10-28. *Editorial reconciliation:*
"last month" most likely refers to the October onboarding step. The primary record explains
the gap, so it is not escalated.

**Maturity.** gVisor is a CNCF Sandbox project; its own footer says so.[^gvisor-site-2026] As of
2026-11-05 it was "working through CNCF Sandbox onboarding" and "on a path toward
Incubation".[^google-cncf-agents-2026] It is not an Incubating project.

**Announced but not yet done (as read on 2026-11-13).**

- **Maintainers:** Ant Group, Modal and Tines "committed to joining gVisor's maintainers".
  OpenAI, Tencent and NVIDIA will continue as contributors, not
  maintainers.[^gvisor-cncf-blog-2026] MAINTAINERS.md still lists 18 active maintainers, all at
  Google.[^gvisor-repo-2026] The governance page says "all active gVisor maintainers are employed
  by a single organization".[^gvisor-governance-2026]
- **Governance:** the blog plans a move to a maintainers-based model, then to "org-based voting,
  thereby preventing Google from having unilateral control".[^gvisor-cncf-blog-2026] The
  governance page already defines a Maintainer Council and org-balanced voting, with one vote
  per employer, for governance decisions. Day-to-day review and merges stay under lazy
  consensus.[^gvisor-governance-2026]
- **Repository:** "The GitHub repository will move out of the `google` GitHub organization". No
  destination is named.[^gvisor-cncf-blog-2026] On 2026-11-13 it was still `google/gvisor`.[^gvisor-repo-2026]
- **Build:** CI moves to GitHub Actions and Buildkite, and Google's internal test infrastructure
  will no longer block PRs.[^gvisor-cncf-blog-2026]

**The kernel-patch argument.** Both posts give the same reason for the donation. Google and
other users carry host Linux kernel patches that bring gVisor's I/O performance close to native
Linux. Kernel maintainers turned them down while gVisor was a single-vendor project. Neutral
CNCF governance is meant to let those patches go
upstream.[^google-cncf-agents-2026][^gvisor-cncf-blog-2026] This is the projects' own account;
the kernel side was not checked.

**Releases.** Tags are dated (`release-YYYYMMDD.N`) and come out about weekly. The latest on
2026-11-13 was `release-20261109.0`, published 2026-11-11.[^gvisor-repo-2026]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:gvisor]] | used-by | [[project:agent-sandbox]] |
| [[project:gvisor]] | used-by | [[project:agent-substrate]] |
| [[project:gvisor]] | part-of | [[domain:ai-protocols]] |

## Relevance to Kortex

gVisor is the first project in the wiki that sits *under* the agent sandboxes rather than beside
them. Two of the four sandboxes in the [Agent Sandbox comparison
table](agent-sandbox.md#relevance-to-kortex), Agent Sandbox and Agent Substrate, offer it as one
of two isolation backends. *Editorial:* it is a sibling of Kata Containers, not of the sandbox
APIs.

It is also the first project whose CNCF status is backed by the CNCF's own record (issue #521)
and not only by the project's claim. The CNCF organization page is still queued. The move
repeats a pattern already in this cluster: a single-vendor project moves to neutral governance,
as A2A did with the AAIF and x402 did with the Linux Foundation. *Editorial:* the home page's
switch from "Application Kernel for Containers" to "The Sandbox Kernel for Agents" shows the
project now presents agents as its main use case.

## Related

- [Agent Sandbox](agent-sandbox.md): kubernetes-sigs `Sandbox` CRD; gVisor through `runtimeClassName: gvisor`. Holds the canonical sandbox comparison table.
- [Agent Substrate](agent-substrate.md): CNCF Sandbox runtime with a `gvisor` sandbox class (`runsc`) next to Kata on Cloud Hypervisor.
- [Running Agents on Kubernetes with Agent Sandbox](../sources/ai-protocols-agent-sandbox-kubernetes-2026.md): launch post fiche, which lists gVisor/Kata isolation in the core `Sandbox` CRD.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md): a different layer, local OS containment (macOS Seatbelt) instead of a user-space kernel.
- [AI Protocols](../domains/ai-protocols.md): domain cluster.

[^google-cncf-agents-2026]: Drew Bradstock (VP Product Management, Orchestration & Kubernetes, Google Cloud), "Powering open infrastructure for autonomous agents", Google Cloud Blog, 2026-11-05, https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en, read 2026-11-13. Only the gVisor section and the sentences naming gVisor were used; the Agent Substrate and OpenRL parts were not ingested here.
[^gvisor-site-2026]: gVisor home page, https://gvisor.dev/, read 2026-11-13.
[^gvisor-docs-2026]: "What is gVisor?", https://gvisor.dev/docs/, read 2026-11-13.
[^gvisor-security-2026]: "Security Model", https://gvisor.dev/docs/architecture_guide/security/, read 2026-11-13.
[^gvisor-platforms-2026]: "Platform Guide", https://gvisor.dev/docs/architecture_guide/platforms/, read 2026-11-13.
[^gvisor-checkpoint-2026]: "Checkpoint/Restore", https://gvisor.dev/docs/user_guide/checkpoint_restore/, read 2026-11-13.
[^gvisor-cncf-blog-2026]: Etienne Perot & Jing Chen, "gVisor is being donated to CNCF", gVisor blog, 2026-10-02, https://gvisor.dev/blog/2026/10/02/gvisor-cncf/, read 2026-11-13.
[^gvisor-governance-2026]: gVisor governance page (undated), https://gvisor.dev/community/governance/, read 2026-11-13.
[^gvisor-repo-2026]: GitHub metadata for google/gvisor (license, creation date, description, release tags) and its MAINTAINERS.md, https://github.com/google/gvisor, read 2026-11-13.
[^cncf-sandbox-521-2026]: "[Sandbox] gVisor", CNCF Sandbox application issue #521 (opened 2026-09-07, closed 2026-10-28; labels `gitvote/passed`, `contribution-agreement/signed`), https://github.com/cncf/sandbox/issues/521, read 2026-11-13.
[^agent-sandbox-gvisor-2026]: "gVisor Isolation", Agent Sandbox docs (last modified 2026-09-04), https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/, read 2026-11-13.
