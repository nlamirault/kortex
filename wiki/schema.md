---
type: schema
title: Wiki Schema Reference
description: Copy-paste OKF v0.2 templates for every kortex entity type.
updated: 2026-10-08
---

# Wiki Schema Reference

Templates for each entity type. Copy-paste when creating a new page, then fill every
`<placeholder>`. All templates are OKF v0.2-conformant (see `AGENTS.md`):

- `type:` is the only always-required key.
- `status:` is one of `draft | stable | deprecated` (absent ⇒ `stable`). Staleness is derived
  from `stale_after`, never a status.
- `sources:` is a **list of mappings**, each with a required `resource:` — never a list of strings.
- `generated` / `verified[].at` / `stale_after` are ISO 8601 with an explicit UTC offset.
- Outside a `## Relations` table, every cross-reference is a **markdown link**
  `[Title](../dir/slug.md)`, never a bare `[[type:slug]]` (GitHub does not render wikilinks).

---

## Concept Page

```markdown
---
type: concept
title: <concept name>
description: <one-line summary>
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Concept Name>

One-sentence definition.

## Core Idea

2-3 paragraphs explaining the concept.

## Key Properties

- Property 1
- Property 2

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:this-concept]] | predicate | [[type:slug]] |

Keep to the top 5 relations. Predicates: `is-a`, `part-of`, `enables`, `implements`,
`requires`, `contrasts-with`, `extends`, `used-by`, `created-by`.

## Related

- [Related concept](../concepts/related-concept.md)
- [Where this comes from](../sources/where-this-comes-from.md)

## Open Questions

- ?
```

---

## Source Page

```markdown
---
type: source
title: <title by author, year>
description: <one-line summary>
status: draft
confidence: high
cluster: <domain-slug>
domain: [<domain-slug>]
sources:
  - resource: raw/<subdir>/<filename>
    id: <stable-key>
    title: <short source title>
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
stale_after: <ISO-8601 with UTC offset>   # 6mo AI/protocols, 1yr k8s; omit if evergreen
updated: YYYY-MM-DD
tags: []
key_claims:
  - <claim 1>
  - <claim 2>
---

# <Title>

**Author:** <name> · **Year:** <year> · **Format:** book | paper | article | talk | course
**Author page:** [<author name>](../people/author-slug.md)

## Summary

2-3 sentence summary.

## Key Ideas

- Idea 1: explanation
- Idea 2: explanation

## Notable Quotes

> "Quote" (p. X)

## Concepts Introduced

- [<concept>](../concepts/slug.md)

## Open Questions Raised

- ?

## Rhetorical Analysis

**Audience:** <practitioner | researcher | executive | general>
**Style:** <academic | practitioner | polemic | advocacy | narrative>
**Epistemic stance:** <certain | hedged | speculative | contrarian>
**Persuasion devices:** <data-heavy, anecdote-first, authority appeals, aphorisms, ...>
**Bias indicators:** <funding, affiliation, prior positions that may color claims>

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:this-source]] | argues-that | [[type:slug]] |

## KnowledgeGraph

### Triples

| Subject | Type_Subject | Predicate | Object | Type_Object | Confidence | Temporality | Attribution |
|---------|--------------|-----------|--------|-------------|------------|-------------|-------------|

Confidence: 0.0–1.0. Temporality: `static | dynamic | timeless`. Attribution: `stated | inferred`.

### Entities

| Entity | Type | Attribute | Value | Action |
|--------|------|-----------|-------|--------|

`Type_Subject` / `Type_Object` / `Type` use the canonical English entity types:
`concept | source | person | project | organization | decision | comparison | synthesis | pattern | gap`.
Each MUST match the type used for that same entity in the `## Relations` `[[type:slug]]`, and the
entity name must slugify to that same slug — otherwise `scripts/build_knowledge_base.py` creates
phantom duplicate nodes in `wiki/kb/`. Action: `AJOUT` (new) | `MISE_A_JOUR` (update existing).
```

---

## Fiche Page

Use for articles, blog posts, short reads — fast single-pass capture. Use the Source Page for
books, papers, and long-form content.

```markdown
---
type: source
title: <article title>
description: <one-line summary>
format: fiche
status: stable
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources:
  - resource: <url or raw/articles/<slug>.md>
    id: <stable-key>
    title: <short source title>
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
stale_after: <ISO-8601 with UTC offset>   # 6mo AI/protocols, 1yr k8s; omit if evergreen
updated: YYYY-MM-DD
tags: []
---

# <Title>

**Auteur :** <name> · **Publié :** <YYYY-MM-DD> · **Lien :** <url>
**Domaine :** [<domain>](../domains/slug.md) · **Lecture :** ~N min

## En Bref

2–3 sentences. What does this argue, and why does it matter for this domain?

## Points Clés

- **Point 1:** one sentence with a concrete claim
- **Point 2:** one sentence with a concrete claim
- **Point 3:** one sentence with a concrete claim

(3–5 points max — if you need more, use the Source Page instead.)

## Citation Notable

> "Quote that captures the core argument." — Author

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[type:slug]] | predicate | [[type:slug]] |

Predicates: `argues-that`, `extends`, `contrasts-with`, `implements`, `created-by`, `used-by`,
`enables`. 3–5 triples max.

## Liens Wiki

- [<concept>](../concepts/slug.md) — why linked
- [<project>](../projects/slug.md) — why linked
```

**Naming:** `wiki/sources/<domain>-<short-title>-YYYY.md` (same as the Source Page).

| Signal | Use Fiche | Use Source Page |
|--------|-----------|-----------------|
| Format | Article, blog post, thread | Book, paper, talk transcript |
| Read time | < 20 min | > 20 min |
| Entity density | < 5 new entities | > 5 new entities |
| Depth needed | Quick capture | Deep synthesis |

---

## Person Page

```markdown
---
type: person
title: <person name>
description: <one-line summary>
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Person Name>

**Role:** researcher | author | practitioner
**Known for:** one-line summary

## Background

Brief bio.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[person:this-person]] | created | [[type:slug]] |

Keep to the top 5 relations. Predicates: `created`, `contributed-to`, `works-at`, `influenced`,
`co-authored`, `advocates-for`.

## Key Contributions

- [<concept>](../concepts/slug.md) — explanation
- [<source>](../sources/slug.md) — explanation

## Works

- [<book>](../sources/book-slug.md)
```

---

## Project Page

```markdown
---
type: project
title: <project name>
description: <one-line summary>
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Project Name>

**Kind:** tool | codebase | initiative · **Lifecycle:** active | archived | experimental
**URL:** <url>

## What It Does

One paragraph.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:this-project]] | predicate | [[type:slug]] |

Keep to the top 5 relations. Predicates: `implements`, `extends`, `replaces`, `integrates-with`,
`created-by`, `used-by`, `part-of`.

## Relevance to Kortex

Why this matters for this knowledge base.

## Related

- [<concept>](../concepts/slug.md)
- [<person>](../people/slug.md)
```

---

## Decision Page

```markdown
---
type: decision
title: <decision title>
description: <one-line summary>
status: draft
confidence: high
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# Decision: <Title>

**Date:** YYYY-MM-DD · **Lifecycle:** proposed | accepted | rejected | superseded

(The lifecycle line is the ADR decision state — a different axis from the OKF `status` field.)

## Context

What problem prompted this decision.

## Options Considered

1. Option A — pros/cons
2. Option B — pros/cons

## Decision

What was chosen and why.

## Consequences

What changes as a result.

## Related

- [<related decision>](../decisions/slug.md)
```

---

## Domain Hub Page

```markdown
---
type: domain
title: <domain name>
description: <one-line summary>
status: stable
confidence: high
cluster: <self-slug>
domain: [<self-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Domain Name>

One-paragraph description of this knowledge domain.

## In This Cluster

(List all member concepts — split the cluster when it exceeds 15 members.)

- [<concept>](../concepts/slug.md) — one-line description

## Key Sources

- [<source>](../sources/slug.md) — one-line description

## Key People

- [<person>](../people/slug.md) — one-line description

## Open Questions

- ?
```

---

## Comparison Page

```markdown
---
type: comparison
title: <thing A> vs <thing B>
description: <one-line summary>
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Thing A> vs <Thing B>

**Purpose of comparison:** one sentence on why this matters.

## Overview

| Dimension | [Thing A](../concepts/thing-a.md) | [Thing B](../concepts/thing-b.md) |
|-----------|-----------------------------------|-----------------------------------|
| Dimension 1 | | |
| Dimension 2 | | |
| Dimension 3 | | |

## Thing A

Key strengths and weaknesses.

## Thing B

Key strengths and weaknesses.

## When to Use Which

Decision guidance.

## Sources

- [<source>](../sources/slug.md) — supports claim X
```

---

## Synthesis Page

```markdown
---
type: synthesis
title: <synthesis title>
description: <one-line summary>
status: stable
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources:
  - resource: "conversation:YYYY-MM-DD"
    title: <topic discussed>
filed_from_query: true
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# <Synthesis Title>

**Filed from:** conversation on YYYY-MM-DD
**Question that prompted this:** one sentence

## Analysis

Cross-source synthesis. Every claim cites a wiki page or raw source.

## Key Findings

- Finding 1 — [<source>](../sources/slug.md)
- Finding 2 — [<concept>](../concepts/slug.md)

## Limitations

What this synthesis doesn't cover or where confidence is low.

## Related

- [<domain>](../domains/slug.md)
- [<concept>](../concepts/slug.md)
```

---

## Gap Page

```markdown
---
type: gap
title: <gap description>
description: <one-line summary>
status: draft
confidence: low
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
---

# Gap: <Title>

**Opened:** YYYY-MM-DD · **State:** open | investigating | resolved

## What Is Unknown

Describe the knowledge gap or open question.

## Why It Matters

Why resolving this gap matters.

## Attempted Investigations

- YYYY-MM-DD: tried X → result

## Resolution

(Fill in when resolved. Never delete a gap — mark it resolved, per Hard Rule 5.)

✅ Resolved — YYYY-MM-DD
Evidence: [<source>](../sources/slug.md)
```

---

## Pattern Page

A **recurring behavior** — a failure mode or a winning strategy — synthesized from `!failure`
log entries or repeated observation. Distinct from a Gap: a gap is unknown knowledge; a pattern
is known, recurring behavior with a workaround. Patterns drive procedure and skill improvements.

```markdown
---
type: pattern
title: <pattern name>
description: <one-line summary>
status: stable
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
verified: []
updated: YYYY-MM-DD
tags: []
kind: failure | strategy
occurrences: <N>
---

# Pattern: <Title>

**Kind:** failure mode | winning strategy
**First seen:** YYYY-MM-DD · **Occurrences:** N

## Symptom

What is observed when this pattern fires (the failure, or the situation the strategy applies to).

## Root Cause

Why it happens. For a strategy: why it works.

## Workaround / Procedure

The fix, or the reusable procedure. If this became a skill or rule change, link it.

## Evidence

- `wiki/log.md` YYYY-MM-DD `!failure` — <one line>
- `wiki/log.md` YYYY-MM-DD `!failure` — <one line>
```
