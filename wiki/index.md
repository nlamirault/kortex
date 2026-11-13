---
okf_version: "0.2"
---

# Kortex Wiki Index

The catalog of this OKF bundle. Every page is listed once under its entity type, and every
write operation also appends to `## By Date`.

## Meta

- [Schema Reference](schema.md) — copy-paste OKF v0.2 templates for every entity type.
- [Hot Cache](hot.md) — session hot cache; read first at session start.
- [Cluster Overview](overview.md) — top-level navigation across domains.

## Domains

- [AI Protocols](domains/ai-protocols.md) — open standards connecting LLMs and agents to tools, each other, and payment rails.
- [Observability](domains/observability.md) — understanding system behavior from telemetry (traces, metrics, logs), standardized by OpenTelemetry.

## Concepts

- [Tool Use / Function Calling](concepts/tool-use-function-calling.md) — foundational primitive: an LLM invoking external functions.
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — standard for connecting an LLM app to tools, data, and context.
- [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — protocol for discovery and task delegation between agents.
- [Agent Communication Protocol (ACP)](concepts/agent-communication-protocol-acp.md) — REST-based agent-to-agent communication (IBM/BeeAI).
- [x402](concepts/x402.md) — revives HTTP 402 for native machine-to-machine payments.
- [Personal Agent Consent & Trust Protocol (PACT)](concepts/personal-agent-consent-trust-protocol-pact.md) — consent + scoped delegation on A2A so a personal agent acts on a user's account with verifiable permission.
- [Personal Agent Protocol (PAP)](concepts/personal-agent-protocol-pap.md) — Meta + Sierra standard for personal-agent↔business connection over MCP/OpenAPI; parallel to PACT.
- [AGENTS.md](concepts/agents-md.md) — open Markdown convention giving AI coding agents per-repo instructions; an AAIF/Linux Foundation project.
- [Agent Plugins](concepts/agent-plugins.md) — open 1.0.0 packaging standard bundling Agent Skills and MCP servers into one portable plugin directory.
- [Agentic Resource Discovery (ARD)](concepts/agentic-resource-discovery-ard.md) — open pre-invocation discovery protocol (v0.91, Proposal): domain-anchored entries at `/.well-known/ard.json`, federated registries with REST `/search`, publisher-authority trust binding; `ai-catalog.json` → `ard.json` drift dated.
- [Telemetry Signals](concepts/telemetry-signals.md) — the three observability data types: traces, metrics, logs.
- [Distributed Tracing](concepts/distributed-tracing.md) — following one request across services via spans and context propagation.
- [OpenTelemetry (OTel)](concepts/opentelemetry-otel.md) — vendor-neutral standard and OTLP wire format for telemetry.
- [Instrumentation](concepts/instrumentation.md) — making code emit telemetry: API/SDK split, auto vs manual.
- [Semantic Conventions](concepts/semantic-conventions.md) — standardized attribute names so telemetry is comparable across services.

## Sources

- [AGENTS.md — open format for guiding coding agents](sources/agents-md-open-format-2026.md) — fiche: Markdown convention for per-repo agent instructions; 60k+ projects; AAIF/Linux Foundation project.
- [Introducing Personal Agent Protocol (Sierra blog)](sources/sierra-personal-agent-protocol-2026.md) — fiche: Meta + Sierra introduce PAP for personal-agent↔business connection over MCP/OpenAPI; parallel to PACT.
- [Introducing PACT (Decagon blog)](sources/decagon-pact-introduction-2026.md) — fiche: Decagon open-sources PACT (with Instinct), a consent/delegation layer on A2A.
- [PACT Protocol Home (openpactprotocol.org)](sources/openpactprotocol-pact-spec-2026.md) — fiche: the PACT spec home — roles, registration→discovery→consent→delegation flow, built on A2A 1.0.
- [Linux Foundation Announces Operational Launch of x402 Foundation](sources/ai-protocols-x402-foundation-launch-2026.md) — fiche: x402 Foundation launches under the Linux Foundation; Coinbase contributes the protocol; ~40 members.
- [A New Chapter for A2A: Joining the Agentic AI Foundation](sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) — fiche: A2A moves to vendor-neutral governance under the Linux Foundation-directed Agentic AI Foundation (AAIF).
- [Introducing Dogwood: runtime verification for AI agents](sources/ai-protocols-dogwood-runtime-verification-2026.md) — fiche: open-source governance language adding temporal (history-aware) rules to agent tool calls, extending Cedar.
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](sources/ai-protocols-strands-box-sandboxes-2026.md) — fiche: AWS open-source agent sandbox pairing OS containment (macOS Seatbelt) with Dogwood policy at network/shell/Python/MCP boundaries.
- [Introducing Clef: open-source decision models (Cloudflare)](sources/ai-protocols-clef-decision-models-2026.md) — fiche: Cloudflare's Clef/Clef-flash decision models return typed, calibrated classifications for fast agent routing; open-sourced (Apache 2.0) and hosted on Workers AI, with an RL fine-tuning service.
- [Agent Skills — standardized way to give AI agents new capabilities](sources/ai-protocols-agent-skills-overview-2026.md) — fiche: open SKILL.md folder format with progressive disclosure (discovery → activation → execution); Anthropic-origin, broadly adopted across coding agents; an AAIF project since 2026-10-22.
- [Agent Plugins — portable package format for skills and MCP servers (spec site)](sources/ai-protocols-agent-plugins-spec-2026.md) — fiche: open 1.0.0 packaging standard (plugin.json + skills/ + mcp.json + reverse-domain extensions); TSC Amazon/Cursor/Microsoft/OpenAI/Vercel.
- [Agent Plugins package your skills, tools, and more (Google blog)](sources/ai-protocols-agent-plugins-google-2026.md) — fiche: Google (Hou/Wang/Blount, 2026-08-06) joins as Core Maintainer; manifest-fragmentation framing, v1 non-goals, ARD/AI Catalog layering, Agents CLI + Data Agent Kit.
- [Agentic Engine Optimization (AEO) — Addy Osmani](sources/addyosmani-agentic-engine-optimization-2026.md) — fiche: docs need structuring for AI coding agents (token budgets, `llms.txt`, `skill.md`, "Copy for AI"), the SEO analogue for agent-readable content.
- [AgentReady — open specification for agent-usable products](sources/ai-protocols-agentready-standard-2026.md) — fiche: Ora's open find/read/act checklist (MUST/SHOULD/MAY) for agent-usable products, backed by large-scale agent-behavior studies; v2.0 adds a MUST-ship-MCP-or-CLI requirement.
- [What Open Responses changes for AI developers](sources/ai-protocols-open-responses-2026.md) — fiche: shared spec based on OpenAI's Responses API so developers target one provider-neutral contract across providers; now an AAIF project.
- [The Sandbox as an Agent Primitive](sources/ai-protocols-opensandbox-agent-primitive-2026.md) — fiche: AAIF's OpenSandbox gives agents a runtime-neutral lifecycle + execution API over Docker/Kubernetes sandboxes, via an in-sandbox `execd` daemon.
- [Training agents for real-world tasks with OpenEnv](sources/ai-protocols-openenv-training-agents-2026.md) — fiche: AAIF's OpenEnv reset/step/state interface for agent-training environments, with case studies on reward-design failure modes.
- [Agentic AI Foundation Announces Four New Projects](sources/ai-protocols-aaif-four-new-projects-2026.md) — fiche: AAIF press release (2026-10-22) taking in Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face), OpenSandbox (Alibaba); 10 hosted projects after year one.
- [Running Agents on Kubernetes with Agent Sandbox](sources/ai-protocols-agent-sandbox-kubernetes-2026.md) — fiche: Kubernetes blog (Kuo & Santa Barbara, 2026-03-20) introducing SIG Apps' Agent Sandbox — a `Sandbox` CRD for isolated, stateful, singleton agent workloads, plus warm-pool extensions.
- [Announcing the Agentic Resource Discovery specification (Google blog)](sources/ai-protocols-ard-google-announcement-2026.md) — fiche: Google (Bu & Krishnan, 2026-06-17) launches ARD; catalogs + registries, four-phase demo, Google Cloud Agent Registry (native ARD "in the coming months").
- [Agentic Resource Discovery (ARD): An open specification for agent discovery (AWS blog)](sources/ai-protocols-ard-aws-agent-registry-2026.md) — fiche: AWS (Damick, Mangal & Talluri, 2026-08-24); AWS Agent Registry (preview) workflow, multi-environment problem, DNS analogy, ARD as complement (stated as expectations).
- [Agentic Resource Discovery: Let agents search (Hugging Face blog)](sources/ai-protocols-ard-hugging-face-discover-2026.md) — fiche: Hugging Face (Burtenshaw & Smith, 2026-06-17); discovery layer in front of MCP/Skills/A2A; `hf-discover` reference implementation via CLI, REST and MCP.
- [Personal Agent Protocol (personalagentprotocol.org)](sources/ai-protocols-personal-agent-protocol-site-2026.md) — fiche: official PAP ("Poppy") site; Apache-2.0, `/.well-known/poppy.json`, OAuth sign-in, one signed Session across APIs/web/company agent, extensions (UCP, Operations); v0.4 = 1.0 release candidate (2026-11-10); 43 listed design partners; dated differences from the Sierra launch post.
- [Powering open infrastructure for autonomous agents (Google Cloud blog)](sources/ai-protocols-google-agents-cncf-donation-2026.md) — fiche: Google (Bradstock, 2026-11-05) donates Agent Substrate, gVisor and OpenRL to the CNCF after their CNCF Sandbox acceptance; Agent Substrate reaches 1.0 and GA on GKE.
- [Welcoming OpenShell to the CNCF: Open Governance to Secure Agentic AI](sources/ai-protocols-openshell-cncf-2026.md) — fiche: CNCF blog (Bryce & Golshan, 2026-11-10); NVIDIA contributes OpenShell as a CNCF Sandbox project; enforcement outside the agent, move to the `ai-openshell` org, Cedar adoption announced.

## People

## Projects

- [agentic-seo](projects/agentic-seo.md) — Osmani's MIT-licensed CLI auditing docs for Agentic Engine Optimization (AEO); 10 checks, 0–100 score.
- [Agent Sandbox](projects/agent-sandbox.md) — kubernetes-sigs project: declarative `Sandbox` CRD, gVisor/Kata isolation decoupled from the API, warm pools, Python/Go SDKs.
- [Agent Substrate](projects/agent-substrate.md) — CNCF Sandbox runtime multiplexing suspended stateful actors onto warm Kubernetes workers; gVisor or Kata-on-Cloud-Hypervisor; SPIFFE identity, no in-sandbox credentials, default-deny egress.
- [gVisor](projects/gvisor.md) — user-space application kernel in Go (`runsc` OCI runtime) isolating untrusted container code from the host kernel; CNCF Sandbox (2026); backend for Agent Sandbox and Agent Substrate.
- [OpenShell](projects/openshell.md) — CNCF Sandbox agent runtime (contributed by NVIDIA): trusted supervisor mediating every network request against YAML policy, credentials only for approved endpoints, SMT prover for proposed rules; Cedar proposed as an alternate policy language.

## Organizations

- [Agentic AI Foundation (AAIF)](organizations/agentic-ai-foundation.md) — vendor-neutral foundation hosting MCP, goose, AGENTS.md, A2A, Agent Skills, Open Responses, OpenEnv, OpenSandbox and more (10 projects).
- [Amazon Web Services (AWS)](organizations/aws.md) — cloud vendor; publisher of Dogwood, home of Bedrock AgentCore agent governance and AWS Agent Registry (preview); ARD Oversight Board member.

## Decisions

## Comparisons

## Syntheses

## Patterns

## Gaps

## By Date

### 2026-11-13

- [Personal Agent Protocol site fiche](sources/ai-protocols-personal-agent-protocol-site-2026.md), [Personal Agent Protocol (PAP)](concepts/personal-agent-protocol-pap.md) — `[INGEST]` (fiche + concept enriched); "Poppy" spec building blocks, 0.1→0.4 RC version train, design partners, dated drift vs the Sierra post (session/OAuth split in 0.3) — also touched [AI Protocols](domains/ai-protocols.md)
- [Welcoming OpenShell to the CNCF](sources/ai-protocols-openshell-cncf-2026.md), [OpenShell](projects/openshell.md) — `[INGEST]` (fiche + project); NVIDIA contributes OpenShell to the CNCF (Sandbox); supervisor-mediated sandboxes, YAML policy + SMT prover, Cedar proposed as an alternate policy language (RFC 0020, open) — also touched [Agent Sandbox](projects/agent-sandbox.md), [Agent Substrate](projects/agent-substrate.md), [AI Protocols](domains/ai-protocols.md)
- [gVisor](projects/gvisor.md) — `[INGEST]` (project); Google Cloud CNCF-donation post (gVisor section) + gvisor.dev docs + repo + CNCF issue #521: Sentry/Gofer isolation, `systrap`/KVM platforms, checkpoint/restore, CNCF Sandbox timeline — also touched [Agent Sandbox](projects/agent-sandbox.md) (gVisor links), [AI Protocols](domains/ai-protocols.md)
- [Powering open infrastructure for autonomous agents (Google Cloud blog)](sources/ai-protocols-google-agents-cncf-donation-2026.md), [Agent Substrate](projects/agent-substrate.md) — `[INGEST]` (fiche + project update); Agent Substrate, gVisor and OpenRL donated to the CNCF after Sandbox acceptance; Agent Substrate `v1.0.0` (2026-11-05) and GA on GKE — also touched [AI Protocols](domains/ai-protocols.md)

### 2026-11-03

- [Agentic Resource Discovery (ARD)](concepts/agentic-resource-discovery-ard.md), [ARD Google fiche](sources/ai-protocols-ard-google-announcement-2026.md), [ARD AWS fiche](sources/ai-protocols-ard-aws-agent-registry-2026.md), [ARD Hugging Face fiche](sources/ai-protocols-ard-hugging-face-discover-2026.md) — `[INGEST]` + `[FILE]` (concept promotion from queue + 3 fiches); open pre-invocation discovery protocol, `ai-catalog.json` → `ard.json` drift dated — also touched [AWS](organizations/aws.md), [Agent Plugins](concepts/agent-plugins.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [Agent2Agent (A2A)](concepts/agent2agent-a2a.md), [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [Agent Skills fiche](sources/ai-protocols-agent-skills-overview-2026.md), [AgentReady fiche](sources/ai-protocols-agentready-standard-2026.md), [Agent Plugins (Google blog) fiche](sources/ai-protocols-agent-plugins-google-2026.md), [AI Protocols](domains/ai-protocols.md)

### 2026-11-02

- [Agent Substrate](projects/agent-substrate.md) — `[INGEST]` (project); CNCF Sandbox runtime (originally Google): actors multiplexed onto warm worker pods, suspend to snapshot + resume on any worker, gVisor or Kata-on-Cloud-Hypervisor, zero-trust egress — also touched [Agent Sandbox](projects/agent-sandbox.md) (4th comparison row), [AI Protocols](domains/ai-protocols.md)
- [Running Agents on Kubernetes with Agent Sandbox](sources/ai-protocols-agent-sandbox-kubernetes-2026.md), [Agent Sandbox](projects/agent-sandbox.md) — `[INGEST]` (fiche + project); Kubernetes SIG Apps `Sandbox` CRD for isolated, stateful, singleton agents; gVisor/Kata decoupled from the API; warm-pool extensions; Python/Go SDKs — also touched [The Sandbox as an Agent Primitive](sources/ai-protocols-opensandbox-agent-primitive-2026.md), [Introducing Strands Box](sources/ai-protocols-strands-box-sandboxes-2026.md), [AI Protocols](domains/ai-protocols.md)

### 2026-10-27

- [Agentic AI Foundation Announces Four New Projects](sources/ai-protocols-aaif-four-new-projects-2026.md), [Agentic AI Foundation (AAIF)](organizations/agentic-ai-foundation.md) — `[INGEST]` (fiche) + `[FILE]` (organization, promoted from queue); Agent Skills contributed by Anthropic to AAIF — also touched [Agent Skills — standardized way to give AI agents new capabilities](sources/ai-protocols-agent-skills-overview-2026.md), [The Sandbox as an Agent Primitive](sources/ai-protocols-opensandbox-agent-primitive-2026.md), [Training agents for real-world tasks with OpenEnv](sources/ai-protocols-openenv-training-agents-2026.md), [AI Protocols](domains/ai-protocols.md)
- [AgentReady — open specification for agent-usable products](sources/ai-protocols-agentready-standard-2026.md) — `[INGEST]` (fiche); open find/read/act MUST/SHOULD/MAY checklist backed by measured-agent-behavior studies (Ora); v2.0 MCP-or-CLI MUST; AEO link kept editorial (not cited on the page) — also touched [Agentic Engine Optimization (AEO)](sources/addyosmani-agentic-engine-optimization-2026.md), [AGENTS.md](concepts/agents-md.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md)
- [What Open Responses changes for AI developers](sources/ai-protocols-open-responses-2026.md) — `[INGEST]` (fiche); OpenAI Responses API shape standardized into a provider-neutral spec, now an AAIF project — also touched [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [AI Protocols](domains/ai-protocols.md)
- [The Sandbox as an Agent Primitive](sources/ai-protocols-opensandbox-agent-primitive-2026.md) — `[INGEST]` (fiche); AAIF's OpenSandbox: runtime-neutral lifecycle/execution API over Docker/Kubernetes sandboxes — also touched [Introducing Strands Box](sources/ai-protocols-strands-box-sandboxes-2026.md), [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [AI Protocols](domains/ai-protocols.md)
- [Training agents for real-world tasks with OpenEnv](sources/ai-protocols-openenv-training-agents-2026.md) — `[INGEST]` (fiche); AAIF's OpenEnv reset/step/state training-environment interface, reward-design case studies — also touched [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [The Sandbox as an Agent Primitive](sources/ai-protocols-opensandbox-agent-primitive-2026.md), [AI Protocols](domains/ai-protocols.md)

### 2026-10-24

- [Agentic Engine Optimization (AEO) — Addy Osmani](sources/addyosmani-agentic-engine-optimization-2026.md), [agentic-seo](projects/agentic-seo.md) — `[INGEST]` (fiche + project); six-layer AEO stack (access control → discovery → capability signaling → content formatting → token surfacing → "Copy for AI"); companion audit CLI (10 checks, 0–100 score) — also touched [AGENTS.md](concepts/agents-md.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md)

### 2026-10-09

- [Agent Plugins](concepts/agent-plugins.md) — `[FILE]` (concept promotion, 2-source-grounded); portable packaging (Skills + MCP); contrasts-with AGENTS.md — also touched [AGENTS.md](concepts/agents-md.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [AI Protocols](domains/ai-protocols.md)
- [Agent Plugins — portable package format (spec site)](sources/ai-protocols-agent-plugins-spec-2026.md), [Agent Plugins package your skills, tools, and more (Google blog)](sources/ai-protocols-agent-plugins-google-2026.md) — `[INGEST]` (2 fiches); 1.0.0 portable packaging (Skills + MCP servers); Google joins TSC; no new entity pages — also touched [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [AI Protocols](domains/ai-protocols.md)

### 2026-10-08

- [Agent Skills — standardized way to give AI agents new capabilities](sources/ai-protocols-agent-skills-overview-2026.md) — `[INGEST]` (fiche); open SKILL.md folder format + progressive disclosure, contrasts with AGENTS.md — also touched [AGENTS.md](concepts/agents-md.md), [AI Protocols](domains/ai-protocols.md)
- [Introducing Clef: open-source decision models (Cloudflare)](sources/ai-protocols-clef-decision-models-2026.md) — `[INGEST]` (fiche); Cloudflare decision models (Clef/Clef-flash) for typed agent routing on Workers AI — also touched [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [AI Protocols](domains/ai-protocols.md)
- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](sources/ai-protocols-strands-box-sandboxes-2026.md) — `[INGEST]` (fiche); AWS agent sandbox embedding Dogwood; **contradiction PENDING** (rate-limit responses vs requests) — also touched [Dogwood fiche](sources/ai-protocols-dogwood-runtime-verification-2026.md), [AWS](organizations/aws.md), [AI Protocols](domains/ai-protocols.md)
- [AGENTS.md](concepts/agents-md.md), [AGENTS.md — open format](sources/agents-md-open-format-2026.md) — `[INGEST]`; confirms AAIF stewardship — also touched [MCP](concepts/model-context-protocol-mcp.md)
- [Personal Agent Protocol (PAP)](concepts/personal-agent-protocol-pap.md), [Introducing Personal Agent Protocol (Sierra blog)](sources/sierra-personal-agent-protocol-2026.md) — `[INGEST]`; contradiction flagged vs PACT (working group / "Muse") — also touched [PACT](concepts/personal-agent-consent-trust-protocol-pact.md), [MCP](concepts/model-context-protocol-mcp.md)
- [Personal Agent Consent & Trust Protocol (PACT)](concepts/personal-agent-consent-trust-protocol-pact.md), [Introducing PACT (Decagon blog)](sources/decagon-pact-introduction-2026.md), [PACT Protocol Home](sources/openpactprotocol-pact-spec-2026.md), [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — `[INGEST]` (PACT, 2 sources)
- [Linux Foundation Announces Operational Launch of x402 Foundation](sources/ai-protocols-x402-foundation-launch-2026.md), [x402](concepts/x402.md) — `[INGEST]` (fiche)
- [A New Chapter for A2A: Joining the Agentic AI Foundation](sources/ai-protocols-a2a-agentic-ai-foundation-2026.md), [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — `[INGEST]` (fiche)
- [Amazon Web Services (AWS)](organizations/aws.md) — `[FILE]` (organization)
- [Dogwood: runtime verification for AI agents](sources/ai-protocols-dogwood-runtime-verification-2026.md) — `[INGEST]` (fiche)
- [Observability](domains/observability.md), [Telemetry Signals](concepts/telemetry-signals.md), [Distributed Tracing](concepts/distributed-tracing.md), [OpenTelemetry (OTel)](concepts/opentelemetry-otel.md), [Instrumentation](concepts/instrumentation.md), [Semantic Conventions](concepts/semantic-conventions.md) — `[BOOTSTRAP]`
- [AI Protocols](domains/ai-protocols.md), [Tool Use / Function Calling](concepts/tool-use-function-calling.md), [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md), [Agent2Agent (A2A)](concepts/agent2agent-a2a.md), [Agent Communication Protocol (ACP)](concepts/agent-communication-protocol-acp.md), [x402](concepts/x402.md) — `[BOOTSTRAP]`
- [Hot Cache](hot.md), [Cluster Overview](overview.md) — `[INIT]`
- [Schema Reference](schema.md) — `[INIT]`
