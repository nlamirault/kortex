---
type: concept
title: Agent Communication Protocol (ACP)
description: REST-based protocol for standardized communication between AI agents (IBM/BeeAI lineage).
status: draft
confidence: low
cluster: ai-protocols
domain: [ai-protocols]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [acp, agents, interoperability, rest]
---

# Agent Communication Protocol (ACP)

The Agent Communication Protocol (ACP) is a REST-based protocol for standardized
communication between AI agents, originating from IBM's BeeAI ecosystem (`NOT VERIFIED`
— originator from model recall). It defines how agents are invoked, exchange messages,
and stream results over conventional HTTP.

> **Acronym collision.** "ACP" is overloaded. At least three distinct protocols use it:
> **Agent Communication Protocol** (IBM/BeeAI — this page), **Agent Client Protocol**
> (Zed; editor↔agent), and **Agentic Commerce Protocol** (OpenAI/Stripe; payments).
> This page covers only the first. Always disambiguate by full name.

## Core Idea

ACP aims to let agents communicate through standard REST conventions rather than a
bespoke RPC layer, lowering the barrier for existing web infrastructure to host and call
agents. Its scope overlaps with A2A (peer agent interoperability), and there are reports
that IBM's ACP effort was folded into / aligned with A2A under shared governance in 2025
(`NOT VERIFIED` — consolidation claim from model recall; confirm before relying on it).

## Key Properties

- REST/HTTP-native agent invocation and messaging (`NOT VERIFIED`).
- Scope overlaps A2A — peer agent interoperability.
- Possibly consolidated into A2A governance (`NOT VERIFIED`).

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agent-communication-protocol-acp]] | part-of | [[domain:ai-protocols]] |
| [[concept:agent-communication-protocol-acp]] | contrasts-with | [[concept:agent2agent-a2a]] |

## Related

- [AI Protocols](../domains/ai-protocols.md)
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md)

## Open Questions

- Is IBM's ACP still maintained as a distinct protocol, or merged into A2A? (resolve the `NOT VERIFIED` claim above)
- What concretely distinguishes ACP's REST model from A2A beyond transport conventions?
