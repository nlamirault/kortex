---
title: Skill Impact Ledger
type: index
status: active
updated: 2026-09-01
---

# Skill Impact Ledger

Audit trail for every change to a **skill** (`.claude/skills/*.md`) or an
**operating rule** (`CLAUDE.md`). Mandated by
[[decision:adopt-wikiskill-evolution-loop]] (ADR-0001).

Adapted from the WikiSkill paper's `skill-impact.md`: a complete ground-truth
record of proposals and outcomes so future `/evolve` runs never re-litigate a
rejected change. **Rejected entries stay** — that is the point.

## How to use

- `/evolve` appends one row per proposed change (accepted **or** rejected).
- Manual skill/rule edits also get a row — provenance is not optional.
- `Motivation` links the `pattern:` / `gap:` / `decision:` that drove the change.
- `Gate` records the acceptance check: `lint` = `/lint` clean; `query` = a sample
  query still resolves. Both must pass to accept.
- Never delete a row. Supersede by adding a new row that references the old one.

## Ledger

| Date | Target | Change | Motivation | Gate | Outcome |
|------|--------|--------|------------|------|---------|
| 2026-09-01 | `wiki/` schema, `CLAUDE.md`, 8 skills | Add WikiSkill evolution loop: `patterns/`, `skill-impact.md`, `/evolve`, `## Purpose` blocks, `pattern` entity type | [[decision:adopt-wikiskill-evolution-loop]] | lint ✓ · query n/a (structural) | ✅ accepted |

*(newest first)*
