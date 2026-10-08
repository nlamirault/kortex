---
type: domain
title: AI Protocols
description: Open protocols for connecting LLMs and autonomous agents to tools, data, each other, and payment rails.
status: stable
confidence: high
cluster: ai-protocols
domain: [ai-protocols]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [ai-protocols, agents, interoperability, tools, payments]
---

# AI Protocols

This domain tracks the emerging standards that let LLMs and autonomous agents interact
with the outside world and with each other: how a model calls a tool, how an application
connects a model to data and context, how agents built by different vendors delegate
tasks to one another, and how agents pay for resources. The layer is young and
fast-moving (6-month staleness window), with overlapping and sometimes converging
standards from Anthropic, Google, IBM, Coinbase, and others.

A useful mental map: **tool use** is the primitive (model → function); **MCP** connects
one model to its tools and data (model ↔ tools); **A2A** and **ACP** connect agents to
each other (agent ↔ agent); **x402** lets agents transact (agent ↔ payment rail).

## In This Cluster

- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — the foundational primitive: an LLM invoking external functions via structured output.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — standard for connecting an LLM application to external tools, data, and context.
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — open protocol for discovery and task delegation between autonomous agents.
- [Agent Communication Protocol (ACP)](../concepts/agent-communication-protocol-acp.md) — REST-based agent-to-agent communication (IBM/BeeAI; acronym is overloaded).
- [x402](../concepts/x402.md) — revives HTTP 402 to enable native machine-to-machine payments.
- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md) — consent + scoped delegation layer on A2A, so a personal agent acts on a user's account with verifiable permission.
- [Personal Agent Protocol (PAP)](../concepts/personal-agent-protocol-pap.md) — Meta + Sierra standard for personal-agent↔business connection over MCP/OpenAPI; parallel to PACT (contradiction flagged).
- [AGENTS.md](../concepts/agents-md.md) — open Markdown convention giving coding agents per-repo instructions; an AAIF/Linux Foundation project.

## Key Sources

- [Introducing Strands Box: AI agent sandboxes powered by Dogwood](../sources/ai-protocols-strands-box-sandboxes-2026.md) — AWS's open sandbox pairing OS containment with Dogwood policy.
- [Introducing Dogwood: runtime verification for AI agents](../sources/ai-protocols-dogwood-runtime-verification-2026.md) — history-aware (temporal) governance language extending Cedar at the tool-call boundary.
- [AGENTS.md — open format for guiding coding agents](../sources/agents-md-open-format-2026.md) — per-repo instructions for coding agents; an AAIF project.
- [Sierra — Introducing the Personal Agent Protocol](../sources/sierra-personal-agent-protocol-2026.md) — PAP source (Meta + Sierra).
- [Decagon — Introducing PACT](../sources/decagon-pact-introduction-2026.md) / [openpactprotocol.org spec](../sources/openpactprotocol-pact-spec-2026.md) — PACT sources.
- [x402 Foundation operational launch](../sources/ai-protocols-x402-foundation-launch-2026.md) — Linux Foundation stewardship of x402.
- [A2A joins the Agentic AI Foundation](../sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) — A2A governance under AAIF.

## Organizations

- [Amazon Web Services (AWS)](../organizations/aws.md) — publisher of Dogwood; ships agent tool-call governance via Bedrock AgentCore.

## Key People

None yet — pending first `/ingest`.

## Open Questions

- How do these protocols compose into a single stack — does an agent speak tool use + MCP internally and A2A + x402 externally?
- Which standards are converging (ACP → A2A) and which are genuinely competing?
- Where are the trust and security boundaries when delegating tasks or payments to third-party agents/servers?
