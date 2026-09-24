---
title: unifiedharnessprotocol.org — Unified Harness Protocol (landing page)
type: source
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
key_claims:
  - UHP is an open standard for running complete agent harnesses as shared infrastructure.
  - A model API gives you a turn; UHP gives you a task — a running agent with its own tools, session, and files.
  - The task surface is deliberately Responses-API-compatible; conformant servers MUST accept a subset of that request body.
  - The spec has 11 versioned chapters (version 2026-09-12), machine-readable in OpenAPI 3.1 + JSON Schema 2020-12, Apache 2.0.
  - No hosted service, account, or licence key required — a conformant server can run wholly on your own machine.
---

# unifiedharnessprotocol.org — Unified Harness Protocol

**Author:** Unified Harness Protocol project
**Year:** 2026
**Format:** article (project landing page + spec index)
**Link:** <https://unifiedharnessprotocol.org/>

## Summary

The site presents UHP as "an open standard for running complete agent harnesses as shared
infrastructure" — a universal translation layer between harnesses and the applications that
drive them. Its central move is to shift the integration boundary from the *turn* of a model
API to the *task* of a running agent, and to make that surface Responses-API-compatible so
existing tooling works unchanged. It is a draft standard: "stable enough to build on,
versioned so it can change safely."

## Key Ideas

- **Task, not turn:** a model API gives "a turn: messages in, tokens out, tools you have to
  run yourself"; UHP gives "a task: work in, and a running agent that uses its own tools,
  keeps its own session, and hands back results and files."
- **Harnesses as plug-ins:** harnesses and their surrounding modules "become true plug-ins:
  portable, interchangeable, and reusable across applications through one unified interface."
- **Responses-API shape:** "UHP's task surface is deliberately shaped like the OpenAI
  Responses API, and a conformant server MUST accept the subset of that request body
  described in Tasks" — extended additively via `metadata` and new object types.
- **HTTP contract only:** "no hosted service required"; servers may run agents in
  containers, subprocesses, queues, or external infra, wholly on your own machine and keys.
- **Eleven chapters (v2026-09-12):** Architecture, Lifecycle, Harnesses, Plugins, Tasks,
  Streaming, Sessions, Files, Errors, Security, Schema.
- **Conformance-first:** a suite of 75 runnable checks defines conformant implementations;
  machine-readable schemas in OpenAPI 3.1 + JSON Schema 2020-12; Apache 2.0.
- **Governance:** changes follow `GOVERNANCE.md` and `VERSIONING.md`; proposals are prose
  first, with spec, reference implementation, and conformance suite advancing together.

## Notable Quotes

> "A harness is a complete agent runtime — a loop that plans, calls tools, edits files, and reports back."

> "If you find a behaviour the specification does not describe but your client depends on, that is a specification bug."

Example task request from the site:

```json
{
  "input": "Summarise README.md in three bullets.",
  "model": "claude-sonnet-4.6",
  "metadata": { "harness_id": "chrn_…" },
  "stream": true
}
```

## Concepts Introduced

- [[concept:unified-harness-protocol-uhp]]
- [[concept:agent-harness]]

## Open Questions Raised

- The relationship between UHP's Plugins chapter and existing MCP tool servers is not
  detailed on the landing page. `NOT VERIFIED`
- Which harnesses named as examples (Codex, Claude Code, Gemini CLI, Hermes, DeepSeek
  Harness, Pi) actually ship UHP-conformant servers vs. are cited as illustrations. `NOT VERIFIED`
- Authorship / sponsoring organization behind the standard is not stated on the page. `NOT VERIFIED`

## Rhetorical Analysis

**Audience:** practitioners — platform and application engineers integrating coding-agent runtimes.
**Style:** practitioner / advocacy — a specification landing page with a code example and an implementer's checklist.
**Epistemic stance:** hedged-confident — asserts the design firmly ("MUST accept") while explicitly labelling itself a versioned draft ("stable enough to build on").
**Persuasion devices:** appeal to an existing standard (OpenAI Responses API compatibility as a migration on-ramp), conformance-suite rigor (75 checks) as a credibility signal, "no call home / run on your own machine" as a trust/sovereignty appeal, crisp turn-vs-task framing.
**Bias indicators:** self-published by the protocol's own project alongside its reference implementation (HarnessRouter); naming competitor harnesses as examples frames UHP as the neutral layer above them.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:unified-harness-protocol-uhp]] | standardizes | [[concept:agent-harness]] |
| [[concept:unified-harness-protocol-uhp]] | extends | OpenAI Responses API |
| [[concept:unified-harness-protocol-uhp]] | contrasts-with | Model APIs (turn vs task) |
| [[project:harnessrouter]] | implements | [[concept:unified-harness-protocol-uhp]] |
| [[concept:unified-harness-protocol-uhp]] | streams-via | Server-Sent Events |
| [[concept:unified-harness-protocol-uhp]] | part-of | [[concept:ai-protocols]] |
