---
title: HarnessRouter
type: project
status: active
confidence: medium
cluster: ai
domain: [ai]
sources: [https://unifiedharnessprotocol.org/]
updated: 2026-09-23
tags: [AI, Protocol, Agents, Harness, Reference-Implementation]
generated: {by: claude-opus-4-8, at: 2026-09-23}
verified: []
stale_after: 2027-03-23
---

# HarnessRouter

**Type:** codebase (reference implementation)
**Status:** active
**URL:** <https://unifiedharnessprotocol.org/>

## What It Does

HarnessRouter is the open-source project associated with the
[[concept:unified-harness-protocol-uhp]], published on GitHub. It advances alongside the
specification and conformance suite, serving as the reference implementation against which
UHP's HTTP contract, task lifecycle, streaming, and conformance behaviour are demonstrated.
Per UHP's governance, the specification, reference implementation, and conformance suite
advance together.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:harnessrouter]] | implements | [[concept:unified-harness-protocol-uhp]] |
| [[project:harnessrouter]] | part-of | UHP project (spec + suite + impl) |
| [[project:harnessrouter]] | integrates-with | [[concept:agent-harness]] |

*Predicates: `implements`, `extends`, `replaces`, `integrates-with`, `created-by`, `used-by`, `part-of`.*

## Relevance to Kortex

The canonical way to see UHP work end to end. Anyone evaluating the protocol for driving
interchangeable coding-agent harnesses would start from HarnessRouter and the published
conformance report rather than the prose spec alone.

## Related

- [[concept:unified-harness-protocol-uhp]]
- [[concept:agent-harness]]
- [[source:uhp-website-2026]]
