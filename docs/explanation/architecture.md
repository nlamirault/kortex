# The Three-Layer Architecture

> **Explanation** — the reasoning behind how Kortex is structured. Not a task list; the
> "why" behind the schema.

## The Idea

Kortex implements the **LLM Wiki protocol** (Karpathy, 2024). Its premise: just as source
code compiles once into a binary for repeated execution, raw sources should be synthesized
once into a wiki that is read on every query — instead of being re-derived each time.

## The Three Layers

```
Layer 3 — Schema   (CLAUDE.md)  human + LLM co-evolve  → operating rules
Layer 2 — Wiki     (wiki/)      LLM maintains          → pre-synthesized knowledge
Layer 1 — Raw      (raw/)       human, immutable        → ground truth
```

- **Raw** is immutable ground truth. The LLM never modifies it.
- **Wiki** is the actively maintained synthesis layer. Queries hit this, not raw sources.
- **Schema** (`CLAUDE.md`) encodes the rules and co-evolves with the wiki.

## Why This Beats RAG

RAG re-derives knowledge from raw sources on every query — the synthesis is thrown away
each time. The Kortex wiki is compiled once and enriched continuously. Knowledge compounds
instead of disappearing into chat history.

## Consequences

- **Read the wiki, not the raw sources** at session start. The wiki exists to prevent
  re-reading everything.
- **Stale is worse than missing.** An outdated page actively misleads, so pages are marked
  `stale` immediately when a source changes.
- **Every fact has provenance.** Untraceable claims are marked `NOT VERIFIED`; conflicts are
  flagged `PENDING — escalate to human` rather than silently resolved.

## Related

- [API & Schema Reference](../reference/api-reference.md) — the concrete fields and types
- [ADR 0001 — Adopt OKF](../decisions/adr/0001-adopt-okf.md)
