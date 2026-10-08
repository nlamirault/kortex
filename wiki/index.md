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

## People

## Projects

## Organizations

- [Amazon Web Services (AWS)](organizations/aws.md) — cloud vendor; publisher of Dogwood and home of Bedrock AgentCore agent governance.

## Decisions

## Comparisons

## Syntheses

## Patterns

## Gaps

## By Date

### 2026-10-08

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
