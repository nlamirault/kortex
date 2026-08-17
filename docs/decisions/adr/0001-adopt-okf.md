---
adr: 0001
status: ✅ Accepted
deciders: nlamirault
consulted:
informed:
date: 2026-08-17
spdx-license: Apache-2.0
---

# ADR-0001: Adopt Open Knowledge Format (OKF)

## Context

Kortex is an LLM-maintained wiki built on the Karpathy LLM Wiki protocol. Pages are synthesized from raw
sources by an LLM and written into `wiki/`. As the wiki scales, a structural trust problem emerges: nothing
in the page frontmatter distinguishes a freshly LLM-synthesized draft from a human-reviewed page, or a
current page from one that went stale after an upstream spec changed.

The existing fields (`status`, `confidence`) are editorially maintained but carry no machine-readable
provenance — no record of who authored the content, who (if anyone) verified it, or when it should be
re-checked. Without this, the wiki has no trust gradient: all pages look equally authoritative, and stale
content accumulates silently.

The goal is a minimal, standards-based addition to frontmatter that solves provenance, verification, and
freshness without redesigning the existing schema.

## Considered Options

1. **Adopt OKF v0.2** — add `generated`, `verified`, and `stale_after` fields from the
   [Open Knowledge Format specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
2. **Custom provenance fields** — define bespoke fields (`author`, `reviewed_by`, `expires`) with the same
   semantics but no external standard
3. **No provenance tracking** — keep the status quo; rely on `status` and `confidence` for quality signals

## Pros and Cons

### 1. Adopt OKF v0.2

**Pros:**

- ✅ Established open standard with clear semantics and external documentation
- ✅ Three fields cover all three trust dimensions: authorship, verification, freshness
- ✅ `stale_after` enables automated lint checks and GitHub Actions freshness workflows
- ✅ `verified` creates an explicit human sign-off record — empty list is an unambiguous "not reviewed" signal
- ✅ Additive — fits alongside existing frontmatter without schema conflicts
- ✅ Model ID in `generated.by` creates an audit trail correlating page quality with model capability

**Cons:**

- ❌ Migration cost: all existing pages must be updated (one-time, done in PR #4)
- ❌ `stale_after` requires editorial discipline — omitting it for fast-moving domains silently loses the signal
- ❌ No write-time enforcement; lint catches drift after the fact

### 2. Custom provenance fields

**Pros:**

- ✅ No external dependency; field names can be tailored to Kortex conventions

**Cons:**

- ❌ Bespoke schema — no external documentation, no ecosystem tooling
- ❌ Must design and maintain the spec ourselves; semantics of `verified` and `stale_after` are non-trivial to get right
- ❌ Produces the same three fields under different names — reinvents OKF without the benefit of standardization

### 3. No provenance tracking

**Pros:**

- ✅ Zero migration cost; no schema changes

**Cons:**

- ❌ Trust degrades silently as the wiki scales — all pages look equally authoritative
- ❌ No machine-readable signal for freshness; `/lint` cannot automate stale-page detection
- ❌ Human reviewers cannot tell at a glance whether a page has been verified

## Decision

We will adopt **Option 1 — OKF v0.2**.

OKF v0.2 is the right fit because it directly solves all three trust dimensions (authorship, verification,
freshness) with a minimal, well-specified addition to frontmatter. The bespoke alternative (Option 2)
produces the same fields under different names with no additional benefit. The status quo (Option 3) lets
the trust problem compound as the wiki grows.

The three OKF fields are additive and non-breaking. The migration cost is a one-time operation on existing
pages. `stale_after` is optional, so evergreen content carries no unnecessary overhead.

## Consequences

### Positive

- ✅ Every wiki page carries explicit authorship (`generated`) and review state (`verified`)
- ✅ Fast-moving domains (AI protocols, Kubernetes) can set `stale_after` and surface in lint output
  automatically when they expire
- ✅ Readers — human or LLM — can apply a trust tier to pages without reading their full content
- ✅ The audit trail in `generated.by` enables future analysis of which model produced which content

### Negative

- ❌ All existing pages required a one-time migration to add the three fields (completed in PR #4)
- ❌ `stale_after` discipline must be enforced by convention in `CLAUDE.md`, not by tooling

### Neutral

- ↔️ `stale_after` is optional — omit for evergreen content, set for fast-moving domains
- ↔️ `verified: []` is the correct default for new LLM-synthesized pages; it is not an error, just an
  honest signal that human review has not yet happened

## References

- [OKF specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
- [PR #4: feat/okf — Add OKF trust signal fields](https://github.com/nlamirault/kortex/pull/4)
