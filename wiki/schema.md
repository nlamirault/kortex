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
sources: [raw/<filename>]
updated: YYYY-MM-DD
tags: []
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
sources: []
updated: YYYY-MM-DD
tags: []
---

# <Domain Name>

One-paragraph description of this knowledge domain.

## Core Concepts

- [[concept:slug]] — one-line description

## Key Sources

- [[source:slug]] — one-line description

## Key People

- [[person:slug]] — one-line description

## Open Questions

- ?
```
