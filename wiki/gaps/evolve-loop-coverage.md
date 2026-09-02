---
title: Evolve loop coverage — open questions
type: gap
status: open
confidence: low
cluster: ai
domain: [ai]
sources: [https://arxiv.org/html/2608.27454v1]
updated: 2026-09-01
tags: [self-improvement, evolve, meta]
---

# Gap: Evolve Loop Coverage

**Opened:** 2026-09-01
**Status:** open

## What Is Unknown

The WikiSkill evolution loop ([[decision:adopt-wikiskill-evolution-loop]]) is
adopted but unproven on this wiki. Open questions:

- **What counts as a "recurring" failure?** How many `!failure` entries before a
  pattern page is warranted? The paper had thousands of traces; Kortex has few.
- **Is the sample-query gate meaningful** with no held-out task set? A single
  hand-picked query is weak validation compared to the paper's validation split.
- **Neutral changes.** The paper's strict-improvement gate excludes neutral
  proposals that enable later gains. Kortex's human gate should allow them — but
  the criterion is not yet written down.

## Why It Matters

If the gate is theater, `/evolve` will rubber-stamp changes and the audit trail
loses value. The loop's worth depends on the gate actually filtering.

## Attempted Investigations

- 2026-09-01: loop adopted structurally; no `/evolve` run yet to test the gate.

## Resolution

*(fill in when the first real `/evolve` run — driven by an actual pattern —
validates or refutes the gate)*
