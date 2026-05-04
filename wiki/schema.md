---
title: Wiki Schema Reference
type: index
status: active
updated: 2026-05-04
---

# Wiki Schema Reference

Templates for each entity type. Copy-paste when creating new pages.

---

## Concept Page

```markdown
---
title: <concept name>
type: concept
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
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

## Related

- [[concept:related-concept]]
- [[source:where-this-comes-from]]

## Open Questions

- ?
```

---

## Source Page

```markdown
---
title: <title by author, year>
type: source
status: draft
confidence: high
cluster: <domain-slug>
domain: [<domain-slug>]
sources: [raw/<subdir>/<filename>]
updated: YYYY-MM-DD
tags: []
key_claims:
  - <claim 1>
  - <claim 2>
---

# <Title>

**Author:** <name>
**Year:** <year>
**Format:** book | paper | article | talk | course
**Link:** [[person:author-slug]]

## Summary

2-3 sentence summary.

## Key Ideas

- Idea 1: explanation
- Idea 2: explanation

## Notable Quotes

> "Quote" (p. X)

## Concepts Introduced

- [[concept:slug]]

## Open Questions Raised

- ?
```

---

## Person Page

```markdown
---
title: <person name>
type: person
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# <Person Name>

**Role:** researcher | author | practitioner
**Known for:** one-line summary

## Background

Brief bio.

## Key Contributions

- [[concept:slug]] — explanation
- [[source:slug]] — explanation

## Works

- [[source:book-slug]]
```

---

## Project Page

```markdown
---
title: <project name>
type: project
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# <Project Name>

**Type:** tool | codebase | initiative
**Status:** active | archived | experimental
**URL:** <url>

## What It Does

One paragraph.

## Relevance to Kortex

Why this matters for this knowledge base.

## Related

- [[concept:slug]]
- [[person:slug]]
```

---

## Decision Page

```markdown
---
title: <decision title>
type: decision
status: draft
confidence: high
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# Decision: <Title>

**Date:** YYYY-MM-DD
**Status:** proposed | accepted | rejected | superseded

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

- [[decision:slug]]
```

---

## Domain Hub Page

```markdown
---
title: <domain name>
type: domain
status: active
confidence: high
cluster: <self>
domain: [<self-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# <Domain Name>

One-paragraph description of this knowledge domain.

## In This Cluster

*(list all member concepts — split cluster when > 15 members)*

- [[concept:slug]] — one-line description

## Key Sources

- [[source:slug]] — one-line description

## Key People

- [[person:slug]] — one-line description

## Open Questions

- ?
```

---

## Comparison Page

```markdown
---
title: <thing A> vs <thing B>
type: comparison
status: draft
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# <Thing A> vs <Thing B>

**Purpose of comparison:** one sentence on why this matters.

## Overview

| Dimension | [[concept:thing-a]] | [[concept:thing-b]] |
|-----------|---------------------|---------------------|
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

- [[source:slug]] — supports claim X
```

---

## Synthesis Page

```markdown
---
title: <synthesis title>
type: synthesis
status: active
confidence: medium
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
filed_from_query: true
updated: YYYY-MM-DD
tags: []
---

# <Synthesis Title>

**Filed from:** conversation on YYYY-MM-DD
**Question that prompted this:** one sentence

## Analysis

Cross-source synthesis. Every claim cites a wiki page or raw source.

## Key Findings

- Finding 1 — [[source:slug]]
- Finding 2 — [[concept:slug]]

## Limitations

What this synthesis doesn't cover or where confidence is low.

## Related

- [[domain:slug]]
- [[concept:slug]]
```

---

## Gap Page

```markdown
---
title: <gap description>
type: gap
status: draft
confidence: low
cluster: <domain-slug>
domain: [<domain-slug>]
sources: []
updated: YYYY-MM-DD
tags: []
---

# Gap: <Title>

**Opened:** YYYY-MM-DD
**Status:** open | investigating | resolved

## What Is Unknown

Describe the knowledge gap or open question.

## Why It Matters

Why resolving this gap matters.

## Attempted Investigations

- YYYY-MM-DD: tried X → result

## Resolution

*(fill in when resolved)*

✅ Resolved — YYYY-MM-DD
Evidence: [[source:slug]]
```
