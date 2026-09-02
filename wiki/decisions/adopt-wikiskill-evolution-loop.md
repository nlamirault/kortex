---
title: Adopt WikiSkill Evolution Loop
type: decision
status: accepted
confidence: high
cluster: ai
domain: [ai]
sources: [https://arxiv.org/html/2608.27454v1]
updated: 2026-09-01
tags: [adr, self-improvement, skills, wiki-protocol]
generated: {by: claude-opus-4-8, at: 2026-09-01}
verified: []
---

# ADR-0001 — Adopt WikiSkill Evolution Loop

**Date:** 2026-09-01
**Status:** accepted

## Context

Kortex is modeled on the Karpathy LLM Wiki protocol: `raw/` → `wiki/` → answer.
Knowledge compounds in the wiki layer. But the loop **stops at the wiki**.

The WikiSkill paper ([arxiv 2608.27454](https://arxiv.org/html/2608.27454v1))
describes a third arc absent from Kortex: the wiki **feeds back into the
procedures** (skills + operating rules). Its architecture is `raw/` (traces) →
`wiki/` (patterns) → `skills/` (procedures rewritten from patterns), governed by
an audit trail and a validation gate.

Kortex today:

```
raw → wiki → (answer)            ← where we stop
```

Kortex never rewrites its own skills or `CLAUDE.md` rules from what the wiki
learns. Recurring failures logged with `!failure` die in `log.md`; they never
synthesize into a pattern, and no pattern ever drives a procedure change.
`/file-back` enriches the wiki; nothing enriches the machine that maintains it.

## Options Considered

1. **Do nothing.** Keep the loop open. Skills evolve only by ad-hoc manual edit.
   - Pro: no new surface area.
   - Con: the paper's measured +15pt gain comes precisely from closing this loop;
     failures stay ephemeral; changes to skills leave no provenance or rationale.

2. **Full paper port** — inference/maintainer/proposer agents, automated
   validation split, programmatic gating and rollback.
   - Pro: faithful to the paper.
   - Con: Kortex is a single-human knowledge base, not an RL training harness.
     There is no task suite to validate against, no rollout budget. Over-built.

3. **Adapt the loop to a human wiki** *(chosen)* — port the paper's four
   transferable mechanisms, drop the training-harness machinery.

## Decision

Adopt option 3. Close the loop with four mechanisms mapped from the paper:

| Paper mechanism | Kortex implementation |
|-----------------|----------------------|
| `patterns/` evolving from traces | `wiki/patterns/` — recurring failure modes synthesized from `!failure` log entries, with root cause + workaround |
| `PURPOSE.md` per skill | `## Purpose` block in each `.claude/skills/*.md` tracing it to the pattern/gap that motivates it |
| `skill-impact.md` audit trail | `wiki/skill-impact.md` — every skill/rule change: date, diff summary, motivating pattern, validation, accept/reject |
| Gating on validation split | Lightweight gate inside `/evolve`: `/lint` clean **and** one sample query still resolves before a change is accepted |

The loop is driven by one new operation, **`/evolve`** (Operation 5), playing the
paper's Wiki-Maintainer + Skill-Proposer roles: read `patterns/` and open
`!failure` entries → propose one atomic skill/rule change → gate it → record the
outcome in `skill-impact.md`.

`pattern` becomes a wiki entity type alongside `gap`. Patterns differ from gaps:
a gap is *unknown knowledge*; a pattern is a *known recurring behavior* (failure
or winning strategy) with a workaround.

## Deliberately Not Adopted

- **No automated validation split / rollback.** The paper's limitation ("no
  automated wiki pruning", strict-improvement gate excludes neutral proposals)
  bites RL harnesses. Kortex keeps a human in the accept/reject seat.
- **No inference-agent wiki ablation.** The paper withholds wiki access from the
  inference agent during training to prevent shortcut-learning. Irrelevant to a
  human knowledge base — queries *should* read the wiki.

## Consequences

- Failures stop being write-only. `!failure` → `pattern:` → procedure change is
  now a traceable path.
- Every change to a skill or `CLAUDE.md` rule leaves provenance in
  `skill-impact.md` — rejected ideas stay recorded, preventing re-litigation
  (Hard Rule 6 "trace every claim", extended to procedures).
- New surface to maintain: `patterns/`, `skill-impact.md`, `/evolve`. `/lint`
  gains checks for these (orphan patterns, skills missing `## Purpose`).
- Kortex's existing log-pruning (Rule 2, >90d → summary) already answers the
  paper's open "no pruning mechanism" limitation — no change needed there.

## Related

- [[gap:evolve-loop-coverage]] — open questions on the loop
- `wiki/skill-impact.md` — the audit trail this ADR mandates
- `.claude/skills/evolve.md` — the operation this ADR mandates
