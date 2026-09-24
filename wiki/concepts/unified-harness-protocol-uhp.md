---
title: Unified Harness Protocol (UHP)
type: concept
status: active
confidence: high
cluster: ai
domain: [ai]
sources: [https://unifiedharnessprotocol.org/]
updated: 2026-09-23
tags: [AI, Protocol, Agents, Harness]
generated: {by: claude-opus-4-8, at: 2026-09-23}
verified: []
stale_after: 2027-03-23
---

# Unified Harness Protocol (UHP)

[**UHP**](https://unifiedharnessprotocol.org/) is an open standard for running complete
agent **harnesses** as shared infrastructure — a universal translation layer that lets
applications drive any conformant harness through one HTTP interface.

## Core Idea

Where a model API gives you *a turn* (messages in, tokens out, and tools you must run
yourself), UHP gives you *a task*: work goes in, and a running agent uses its own tools,
keeps its own session, and hands back results and files. This shifts the integration
boundary up a level — from "call a model" to "delegate to a runtime."

The problem UHP targets is fragmentation: every product independently decides how to
discover, configure, and drive harnesses (Codex, Claude Code, Gemini CLI, Hermes, and
others). UHP answers those questions once, so harnesses and their surrounding modules
become **plug-ins** — portable, interchangeable, and reusable across applications through
a single unified interface.

Its task surface is deliberately shaped like the OpenAI Responses API: a conformant server
MUST accept the subset of that request body described in the Tasks chapter, so existing
SDKs, streaming parsers, and UI components work unchanged. UHP extends that surface
*additively* via `metadata` fields and supplementary object types, never redefining
existing fields.

## Key Properties

- **HTTP contract only** — no hosted service, account, licence key, or call-home required;
  a conformant server can run wholly on your own machine and keys.
- **Responses-API-compatible** task surface with additive extensions.
- **Streaming via Server-Sent Events**; final event carries the complete `response` object
  including produced files.
- **Session continuation** via `previous_response_id`.
- **11 versioned spec chapters** (current version `2026-09-12`), machine-readable in
  OpenAPI 3.1 + JSON Schema 2020-12.
- **Conformance-driven**: 75 runnable checks define what "conformant" means; unspecified
  behaviour a client depends on is treated as a specification bug.
- **License:** Apache 2.0.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:unified-harness-protocol-uhp]] | standardizes | [[concept:agent-harness]] |
| [[concept:unified-harness-protocol-uhp]] | extends | OpenAI Responses API |
| [[concept:unified-harness-protocol-uhp]] | contrasts-with | Model APIs (turn vs task) |
| [[project:harnessrouter]] | implements | [[concept:unified-harness-protocol-uhp]] |
| [[concept:unified-harness-protocol-uhp]] | part-of | [[concept:ai-protocols]] |

*Predicates: `is-a`, `part-of`, `enables`, `implements`, `requires`, `contrasts-with`, `extends`, `used-by`, `created-by`.*

## Related

- [[concept:agent-harness]] — the runtime UHP drives
- [[concept:ai-protocols]] — sibling standards (MCP, A2A, ACP, AG-UI)
- [[concept:model-context-protocol-mcp]] — standardizes tools *into* an agent; UHP is a layer above
- [[concept:agent-client-protocol-acp]] — client↔agent editor integration; adjacent scope
- [[project:harnessrouter]] — open-source reference implementation
- [[source:uhp-website-2026]] — where this comes from

## Open Questions

- How does UHP's harness-selection and plugin-install model interact with MCP tool
  servers a harness already speaks? `NOT VERIFIED`
- Adoption beyond the HarnessRouter reference implementation is unclear as of 2026-09. `NOT VERIFIED`
