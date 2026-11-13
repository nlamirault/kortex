---
type: project
title: OpenShell
description: CNCF Sandbox runtime contributed by NVIDIA that runs autonomous AI agents in kernel-confined sandboxes behind a trusted supervisor. It enforces declarative YAML policy on files, processes and every network connection, adds real credentials only for approved endpoints, and checks proposed network rules with an SMT-based prover; Cedar is proposed as an alternate policy language.
resource: https://github.com/NVIDIA/OpenShell
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/
    id: openshell-cncf-2026
    title: "Welcoming OpenShell to the CNCF (CNCF Blog)"
  - resource: https://github.com/NVIDIA/OpenShell
    id: openshell-repo-2026
    title: "NVIDIA/OpenShell (README, GOVERNANCE.md, MAINTAINERS.md, rfc/README.md, repository and release metadata)"
  - resource: https://github.com/NVIDIA/OpenShell/tree/main/docs
    id: openshell-docs-2026
    title: "OpenShell docs source (about/overview, about/architecture, how-it-works/policies/overview, how-it-works/policies/prover)"
  - resource: https://github.com/ai-openshell
    id: openshell-org-2026
    title: "ai-openshell GitHub organization (profile README, repository list)"
  - resource: https://github.com/ai-openshell/.project
    id: openshell-dotproject-2026
    title: "ai-openshell/.project (CNCF project.yaml and maintainers.yaml)"
  - resource: https://www.cncf.io/projects/openshell/
    id: cncf-openshell-page-2026
    title: "OpenShell (CNCF project page)"
  - resource: https://github.com/cncf/sandbox/issues/522
    id: cncf-sandbox-522
    title: "[Sandbox] OpenShell (CNCF Sandbox application and TOC vote)"
  - resource: https://www.cncf.io/projects/cedar/
    id: cncf-cedar-page-2026
    title: "Cedar (CNCF project page)"
  - resource: https://github.com/NVIDIA/OpenShell/issues/4610
    id: openshell-rfc-0020
    title: "RFC 0020, Cedar as an alternate sandbox policy language (issue #4610) and related Cedar pull requests"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:12:06Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [openshell, sandbox, agents, governance, policy, landlock, seccomp, smt, cedar, kubernetes, cncf, nvidia]
---

# OpenShell

**Kind:** codebase (gateway control plane, per-sandbox supervisor, CLI, SDKs; Rust) · **Lifecycle:** active; CNCF Sandbox; `v0.1.8` latest stable release as of 2026-11-13
**URL:** https://docs.nvidia.com/openshell/latest/ · **Repo:** https://github.com/NVIDIA/OpenShell (moving to https://github.com/ai-openshell) · **License:** Apache-2.0[^openshell-repo-2026]

## What It Does

The README calls OpenShell "the safe, private runtime for fleets of autonomous AI
agents".[^openshell-repo-2026] Agents are most useful when they can read files, install
packages, call APIs and use credentials. OpenShell lets them do that without giving them
unrestricted access to data, secrets or the network: "You declare what each agent can touch in a
policy, and OpenShell enforces it".[^openshell-repo-2026] The CNCF launch post frames the same
idea as enforcement "outside of the agents, right within the infrastructure that the agents run
on".[^openshell-cncf-2026] The [launch post fiche](../sources/ai-protocols-openshell-cncf-2026.md)
covers the governance argument.

The docs name two mechanisms:[^openshell-docs-2026]

- **Kernel-level enforcement.** Each agent runs in an isolated sandbox. Kernel controls confine
  its files and system calls, and every network connection passes a policy check before it leaves
  the sandbox. The agent gets credential placeholders; real credentials are added only to
  requests bound for approved endpoints.
- **Formally verified policy changes.** Before a policy change is approved, a prover flags risky
  new access, such as reaching a new host with credentials or calling a new API method, so the
  change waits for human review.

### Architecture

The **gateway** is the control plane. It authenticates users, stores sandbox state, delivers
policy and settings, attaches providers and coordinates connections into
sandboxes.[^openshell-docs-2026] When a sandbox is created, a **compute driver** provisions two
pieces on opposite sides of an isolation boundary:[^openshell-docs-2026]

- **Sandbox** (untrusted side, next to the agent): launches the agent as an owned child, identifies
  the calling program from trusted `/proc` data, and forwards TCP and DNS traffic. It never makes
  policy decisions.
- **Supervisor** (trusted side): checks each request against policy, supplies credentials,
  resolves DNS, opens approved connections and keeps the link to the gateway.

The two talk over the **OpenShell Sandbox Protocol**: one HTTP/2 connection, authenticated with
TLS and a sandbox JWT, that carries a separate stream per TCP connection. The agent cannot run
before the supervisor confirms the boundary. If the supervisor connection drops, the agent is
frozen, and it is terminated if recovery misses its deadline.[^openshell-docs-2026] An outer
network fence denies all workload egress except that channel, so the agent cannot reach a
service, the gateway, DNS or another private address directly.[^openshell-docs-2026] The gateway
issues a gateway JWT and a sandbox JWT per sandbox run (a "generation"); a restart issues fresh
tokens.[^openshell-docs-2026]

Each runtime builds the fence with its own tools, but none of them decides what is allowed. That
always belongs to the shared supervisor and policy engine, "which is why the same policy behaves
the same way everywhere".[^openshell-docs-2026]

| Runtime | Where the supervisor runs | Channel to the sandbox | How direct egress is blocked |
|---|---|---|---|
| Docker / Podman | Its own container | Authenticated Unix socket on a driver-owned volume | Workload container has networking turned off |
| Kubernetes | Its own pod | Private service with server-authenticated TLS and a sandbox JWT | `NetworkPolicy` allows only the supervisor service |
| VM | A process on the host | Authenticated vsock | Guest has no network device |

In "the current Linux backend" the workload runs as one non-root identity with no Linux
capabilities. **Landlock** limits filesystem access, and **seccomp user notification** stages
network operations.[^openshell-docs-2026] The docs describe these two controls for the Linux
backend only. The quickstart supports Linux, macOS on Apple Silicon, and Windows with WSL 2
(experimental), with Docker, Podman or host virtualization. For native Windows through Microsoft
MXC, the README points to a separate build and runtime guide that lists current
limitations.[^openshell-repo-2026] On Kubernetes, the gateway is
installed with Helm and the CNI must enforce `NetworkPolicy`.[^openshell-repo-2026]

**Agent traces.** When an operator enables the agent trace relay, the sandbox points the agent's
OpenTelemetry SDK at the reserved address `192.0.0.8:4318`. The supervisor answers that address
itself, tags each batch with the sandbox ID and forwards it to the operator's collector, so the
agent needs no egress rule for it.[^openshell-docs-2026] This links the project to the
[OpenTelemetry](../concepts/opentelemetry-otel.md) thread.

### Policy

A sandbox policy is a YAML file that sets `version: 1` and has up to five more top-level
sections. OpenShell denies anything the policy does not allow.[^openshell-docs-2026]

| Section | Controls | Enforced by | Takes effect |
|---|---|---|---|
| `filesystem_policy` | Paths processes can read, or read and write | Landlock LSM | At sandbox startup |
| `landlock` | Whether the sandbox still starts if the filesystem rules cannot be applied | Sandbox runtime | At sandbox startup |
| `process` | User and group of sandbox processes | Docker and Podman | At sandbox creation |
| `network_policies` | Destinations each binary can reach, and the requests it can send | Sandbox network proxy | While the sandbox runs |
| `network_middlewares` | Extra inspection, transformation or blocking of allowed traffic | Sandbox network proxy | While the sandbox runs |

Only the network rules and middleware can change while a sandbox runs. The active policy comes
from the first source available, in this order: a gateway-wide global policy, the sandbox's saved
policy, a policy shipped in the image, then OpenShell's restrictive default. Attached providers
can add network rules on top; the result is called the *effective* policy.[^openshell-docs-2026]

**Prover and advisor.** The prover "uses an SMT solver to check whether policies satisfy
specified properties". Its guarantees cover only the policy features its model represents. It
runs two checks:[^openshell-docs-2026]

- **Boundary check:** the policy grants nothing beyond a boundary policy. It runs through the
  `openshell-prover` CLI, which is "primarily intended for agents", for example a parent agent
  checking a subagent's policy, or a CI job.
- **Proposal risk check:** runs automatically each time an agent proposes a network rule through
  the **policy advisor**. It flags risky additions such as cloud metadata addresses or new
  destinations for provider credentials, and any finding blocks auto-approval.

**Cedar (proposed, not shipped).** The launch post says OpenShell "is adopting Cedar, another CNCF
project, as its policy language".[^openshell-cncf-2026] The CNCF project page confirms Cedar is a
CNCF project: it was accepted on 2025-10-08 at the Sandbox level.[^cncf-cedar-page-2026] As of
2026-11-13 the repository tells a narrower story. The documented format is still YAML. Cedar
exists as **RFC 0020, "Cedar as an alternate sandbox policy language"**, an open issue from
2026-10-15. It grew out of an open feature issue from 2026-10-12, "Cedar as a policy language in
OpenShell". The pull requests that propose the RFC text and add Cedar support are open too:
"support Cedar as an alternate sandbox policy language" and "support Cedar in development
builds".[^openshell-rfc-0020] So "its policy language" in the post describes the direction, not
the current release. Re-check when RFC 0020 is accepted.

### Integration surface

- **Extension points:** the post lists providers, compute, governance and approval workflows,
  policy enforcement, isolation and credential management.[^openshell-cncf-2026] The repo
  documents middleware, interceptors, compute drivers and an isolation-backend
  interface.[^openshell-repo-2026][^openshell-docs-2026]
- **Providers** bind a service name to a stored credential, including for inference. The
  supervisor hands it out only where policy allows.[^openshell-docs-2026]
- **SDKs** connect applications to a gateway; they do not install the CLI:[^openshell-repo-2026]
  - Python: `openshell` (PyPI)
  - TypeScript: `@nvidia/openshell-sdk` (GitHub Packages)
  - Go: `github.com/ai-openshell/sdk-go`
  - Rust: `openshell-sdk`, installed from a git tag
- **Agent Skills:** `npx skills add NVIDIA/OpenShell` installs public skills that teach a coding
  agent to drive the CLI, write sandbox policies and debug gateways and inference
  routing.[^openshell-repo-2026] This is the [Agent Skills](../sources/ai-protocols-agent-skills-overview-2026.md)
  format in use.
- **Use cases** in the docs include running Claude Code, OpenCode, Codex or GitHub Copilot CLI with
  constrained file and network access, and treating policy YAML as version-controlled,
  auditable security controls.[^openshell-docs-2026]
- **Telemetry:** OpenShell collects anonymous, category-and-count telemetry by default. It can be
  turned off on the gateway (`OPENSHELL_TELEMETRY_ENABLED=false`) or compiled
  out.[^openshell-repo-2026]

### Status and governance

- **CNCF Sandbox, in three dated steps.** The TOC vote on the sandbox application passed on
  2026-09-26: 72.73% of TOC members holding a binding vote were in favor, against a 66%
  threshold.[^cncf-sandbox-522]
  The CNCF project page gives that same date as acceptance at the Sandbox
  level.[^cncf-openshell-page-2026] The onboarding issue opened on 2026-10-02, after the
  contribution agreement; that is the date in `.project`'s `maturity_log`.[^cncf-sandbox-522][^openshell-dotproject-2026]
  The public welcome came on 2026-11-10 at KubeCon + CloudNativeCon North
  America.[^openshell-cncf-2026] These are different milestones, not conflicting dates.
- **Repository and releases.** `NVIDIA/OpenShell` was created on 2026-02-24. `v0.1.0` shipped on
  2026-09-25 and `v0.1.8` on 2026-11-10; `v0.1.9-pre.3` is tagged.[^openshell-repo-2026] The README
  announces "a stable release cadence" for 0.1.x.[^openshell-repo-2026]
- **Move to `ai-openshell` (in progress).** The post says the code moves to the neutral
  `ai-openshell` organization.[^openshell-cncf-2026] As of 2026-11-13, the README and the
  organization profile still say to use `NVIDIA/OpenShell` "until the move is
  complete".[^openshell-repo-2026][^openshell-org-2026] The organization was created on
  2026-07-30. It holds the Go and Python SDKs, a web admin console, reusable workflows, the CNCF
  `.project` metadata, and `cedar` and `cedar-spec` repositories, but not the main
  codebase.[^openshell-org-2026] The `.project` file still lists `NVIDIA/OpenShell` as the primary
  repository and the NVIDIA docs site as the website.[^openshell-dotproject-2026]
- **Governance model.** GOVERNANCE.md lists "vendor neutrality" among its values: "No single
  organization controls project direction or decisions". The Maintainer Council governs through
  lazy consensus, and formal votes are by majority of active maintainers. Maintainers must be
  individual humans: "AI agents, automated systems, service accounts, companies, and other
  organizations cannot be Maintainers". The project follows the CNCF Code of
  Conduct.[^openshell-repo-2026] The public RFC process starts from a GitHub issue; maintainers
  then assign an RFC number. RFCs 0001 through 0023 (not contiguous) sit in
  `rfc/`.[^openshell-repo-2026]
- **Contributors vs. maintainers.** The post names NVIDIA, Red Hat, Docker and Canonical as core
  contributors since inception.[^openshell-cncf-2026] MAINTAINERS.md lists 14 maintainers, 11 from
  NVIDIA and 3 from Red Hat, so Docker and Canonical held no maintainer seat as of
  2026-11-13.[^openshell-repo-2026] GOVERNANCE.md itself names "One organization dominates project
  decisions or Maintainer membership" as a reason to revisit the model.[^openshell-repo-2026] The
  project lead in `.project` is John T. Myers (NVIDIA).[^openshell-dotproject-2026][^openshell-repo-2026]
  *Minor drift:* `.project`'s `maintainers.yaml` lists 13 people and omits Divesh Chowdary, although
  its README says it must stay in sync with MAINTAINERS.md.[^openshell-dotproject-2026]
- **Packaging and community.** It ships on PyPI, snap and Homebrew (`nvidia/openshell/openshell`),
  plus GHCR images for the gateway, supervisor, sandbox, workspace and Helm
  chart.[^openshell-dotproject-2026] Discussion happens in the CNCF Slack channel `#openshell-dev`
  and on `@ai-openshell.org` mailing lists.[^openshell-cncf-2026][^openshell-dotproject-2026]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:openshell]] | implements | [[source:ai-protocols-openshell-cncf-2026]] |
| [[project:openshell]] | integrates-with | [[concept:opentelemetry-otel]] |
| [[project:openshell]] | part-of | [[domain:ai-protocols]] |

## Relevance to Kortex

OpenShell joins [Agent Substrate](agent-substrate.md) as a CNCF Sandbox agent runtime in the
wiki. Its launch post was co-written by the CNCF (Jonathan Bryce) and the contributor, NVIDIA
(Ali Golshan), and published on the CNCF blog.
*Editorial comparison: no source compares these projects.* The wiki's sandbox
comparison table lives on the [Agent Sandbox](agent-sandbox.md#relevance-to-kortex) page. It has
no OpenShell row yet, and that row is parked in the queue.

- **Where the design centers.** Agent Sandbox hides the isolation backend behind a declarative
  CRD. Agent Substrate multiplexes suspended actors onto warm Kubernetes workers. OpenShell centers
  on a trusted supervisor outside each sandbox that mediates every TCP and DNS request. Its
  runtimes (Docker, Podman, Kubernetes, VM) only build and prove the fence. It also runs on a
  developer machine, not only on Kubernetes.
- **Credentials and policy.** Like Substrate's egress credential injection and Strands Box's
  placeholder credentials, OpenShell keeps real secrets out of the agent. Its prover checks policy
  *changes* before they are approved. Dogwood instead checks tool-call *histories* at run time. If
  RFC 0020 lands, Cedar becomes a policy option in OpenShell, while Strands Box already gets
  Cedar semantics through Dogwood, a Cedar superset. That would put one policy language under two
  sandbox designs from different vendors.
- **Governance pattern.** Moving an agent project under a neutral foundation is already familiar
  in this cluster: A2A and AGENTS.md went to the AAIF, and x402 to the Linux Foundation. Here the
  foundation is the CNCF.

## Related

- [Welcoming OpenShell to the CNCF](../sources/ai-protocols-openshell-cncf-2026.md): launch post fiche (enforcement outside the agent, vendor-neutral governance, Cedar).
- [Agent Sandbox](agent-sandbox.md): kubernetes-sigs `Sandbox` CRD with gVisor or Kata backends; holds the canonical sandbox comparison table.
- [Agent Substrate](agent-substrate.md): another CNCF Sandbox agent runtime (originally Google); actors multiplexed onto warm Kubernetes workers, with built-in egress policy and credential injection.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md): local OS containment, placeholder credentials and Dogwood policy at the network, shell, Python and MCP boundaries.
- [Introducing Dogwood: runtime verification for AI agents](../sources/ai-protocols-dogwood-runtime-verification-2026.md): temporal policy language that extends Cedar.
- [The Sandbox as an Agent Primitive](../sources/ai-protocols-opensandbox-agent-primitive-2026.md): OpenSandbox (AAIF), a lifecycle and execution API that works across runtimes.
- [Agent Skills](../sources/ai-protocols-agent-skills-overview-2026.md): the skill format OpenShell uses to teach coding agents its CLI and policy language.
- [OpenTelemetry (OTel)](../concepts/opentelemetry-otel.md): the agent trace relay forwards agents' OTel traces to the operator's collector.
- [AI Protocols](../domains/ai-protocols.md): domain cluster.

[^openshell-cncf-2026]: Jonathan Bryce (CNCF) & Ali Golshan (NVIDIA), "Welcoming OpenShell to the CNCF: Open Governance to Secure Agentic AI", CNCF Blog, 2026-11-10, read 2026-11-13.
[^openshell-repo-2026]: NVIDIA/OpenShell repository, https://github.com/NVIDIA/OpenShell, read 2026-11-13: `README.md`, `GOVERNANCE.md`, `MAINTAINERS.md`, `rfc/README.md` and the `rfc/` listing, plus repository metadata (license, primary language, creation date) and release and tag lists.
[^openshell-docs-2026]: OpenShell documentation source in the repository, read 2026-11-13: `docs/about/overview.mdx`, `docs/about/architecture.mdx`, `docs/how-it-works/policies/overview.mdx` and `docs/how-it-works/policies/prover.mdx`. The rendered pages live under https://docs.nvidia.com/openshell/latest/, which was not fetched directly.
[^openshell-org-2026]: ai-openshell GitHub organization, https://github.com/ai-openshell, read 2026-11-13: organization metadata, `profile/README.md` and the repository list.
[^openshell-dotproject-2026]: ai-openshell/.project, https://github.com/ai-openshell/.project, read 2026-11-13: `project.yaml`, `maintainers.yaml` and `README.md`.
[^cncf-openshell-page-2026]: CNCF project page for OpenShell, https://www.cncf.io/projects/openshell/, read 2026-11-13. Its "Recent" links (The New Stack, TechTarget) were not read.
[^cncf-sandbox-522]: cncf/sandbox issue #522, "[Sandbox] OpenShell", https://github.com/cncf/sandbox/issues/522, read 2026-11-13: vote creation (2026-09-22), vote result (2026-09-26) and onboarding notice (2026-10-02).
[^cncf-cedar-page-2026]: CNCF project page for Cedar, https://www.cncf.io/projects/cedar/, read 2026-11-13.
[^openshell-rfc-0020]: NVIDIA/OpenShell issue #4610, "docs(rfc): RFC 0020, Cedar as an alternate sandbox policy language" (open, 2026-10-15); feature issue #4411, "feat(policy): Cedar as a policy language in OpenShell" (open, 2026-10-12); pull requests #4564 (RFC proposal), #4565 and #5006 (open). Found through a repository search for "cedar" on 2026-11-13; titles and states only, bodies not read.
