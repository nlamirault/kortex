# Skill: /evolve

Closes the WikiSkill loop: read the wiki's recorded failures and patterns, propose
**one atomic change** to a skill or operating rule, gate it, and record the outcome.
This is Operation 5 — the Wiki-Maintainer + Skill-Proposer role from
[[decision:adopt-wikiskill-evolution-loop]] (ADR-0001).

## When to Use

- User says `/evolve`, "improve the skills", "learn from failures".
- After several sessions accumulated `!failure` entries or a repeated friction.
- Periodically, like `/lint` — but `/lint` audits the wiki; `/evolve` audits the
  **procedures** (skills + CLAUDE.md rules).

## Inputs to Read (in order)

1. `wiki/skill-impact.md` — the ledger. **Read first.** Never re-propose a change
   already rejected here without new evidence.
2. `wiki/patterns/*.md` — synthesized recurring behaviors.
3. `wiki/log.md` — scan for `!failure` entries not yet promoted to a pattern.
4. `wiki/gaps/` — open questions that a skill/rule change could close.
5. The target skill (`.claude/skills/*.md`) or `CLAUDE.md` section itself.

## Workflow

### Step 1 — Synthesize failures into patterns

For each cluster of related `!failure` log entries **not** already covered by a
pattern page:

- If it recurs (≥2 occurrences, or one severe dead-end likely to repeat) → create
  `wiki/patterns/<slug>.md` using the Pattern template in `wiki/schema.md`:
  root cause + workaround + evidence (link the log entries).
- If it is a one-off with no reuse value → leave it in the log. Do **not** create
  a placeholder pattern (Hard Don't: no placeholder pages).

### Step 2 — Propose ONE atomic change

Pick the single highest-leverage pattern/gap. Propose exactly one change:

- **Atomic:** one skill file, or one CLAUDE.md rule. Not a sweep.
- **Patch-style:** state the exact before → after (append / replace / insert).
- Must trace to a `pattern:` or `gap:` — no motivation, no change.

Do not batch. One `/evolve` run = one proposed change. The paper's proposer is
atomic by design; it prevents tangled diffs and keeps the ledger legible.

### Step 3 — Gate (acceptance check)

A change is accepted only if **both** pass:

- **`lint`** — run `/lint` mentally over the touched files: no broken
  `[[wikilinks]]`, no unfilled placeholders, frontmatter intact, no new orphan.
- **`query`** — pick one representative query the change is meant to help. Confirm
  it still resolves correctly (or now resolves *better*). For a purely structural
  change with no query surface, mark `query n/a` and say why.

Neutral changes (no regression, plausible future benefit) **may** be accepted —
unlike the paper's strict-improvement gate. See [[gap:evolve-loop-coverage]].

If the gate fails → **reject.** Record the rejection; revert the edit.

### Step 4 — Apply or revert

- Accepted → write the edit to the skill/CLAUDE.md.
- Rejected → leave the procedure untouched.

### Step 5 — Record in the ledger

Append one row to `wiki/skill-impact.md` (accepted **or** rejected):

```
| YYYY-MM-DD | <target file> | <one-line change> | [[pattern:slug]] | lint ✓/✗ · query ✓/✗/n/a | ✅ accepted / ❌ rejected |
```

### Step 6 — Log + link

- Append to `wiki/log.md` with prefix `[EVOLVE]`.
- Add the touched files to `wiki/index.md` `## By Date` under today, suffix `[EVOLVE]`.
- If a new pattern was created, add it to `index.md` under Patterns.
- If the change resolved a gap, mark it `✅ Resolved — YYYY-MM-DD` (Hard Rule 5).

## Constraints

- **One atomic change per run.** Resist scope creep.
- **Never delete a ledger row.** Supersede, don't erase.
- **Never re-propose a rejected change** without new evidence — check the ledger.
- **Provenance is mandatory.** A change with no `pattern:`/`gap:` behind it does
  not get proposed.
- If a proposed rule change contradicts an existing CLAUDE.md rule → document both,
  mark `PENDING — escalate to human` (Hard Rule 7). Do not silently override.

## Purpose

Motivated by [[decision:adopt-wikiskill-evolution-loop]] — Kortex's `raw → wiki →
answer` loop never fed the wiki's learnings back into its own procedures. `/evolve`
is that missing arc. Traces to [[gap:evolve-loop-coverage]].
