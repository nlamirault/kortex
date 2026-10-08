---
name: query
description: Answer a question from the wiki. Default mode pre-loads the relevant wiki pages into context (reduces hallucination, improves citations). `--graph` instead traverses `## Relations` SPO tables to answer connection queries — "what implements X?", "what relates to Y?", "who created Z?". Trigger before any non-trivial question, or before ingesting a source.
---

# Skill: /query [--graph]

Query the synthesized wiki layer instead of re-deriving from raw sources. Two modes:

- **Default (page recall)** — pre-load the relevant wiki pages, then answer with citations.
- **`--graph`** — traverse `## Relations` tables only and return a structured edge list. Faster
  for connection discovery; use it for "what implements X?", not for concept depth.

---

## Default mode: page recall

Pre-load relevant context before answering. Run before any non-trivial query to reduce
hallucination and improve citation quality.

**Use when:** answering a research question, checking what already exists before an ingest, or
when the user asks about a topic that may already be in the wiki.

### Recall workflow

1. Read `wiki/hot.md` — check Current Focus and Active Pages.
2. Read `wiki/index.md` — scan entries for relevance.
3. Read `wiki/overview.md` — identify the relevant cluster(s).
4. Read the relevant domain hub page(s) in `wiki/domains/`.
5. Follow markdown links to the directly relevant concept and source pages.
6. Report: "Loaded N pages for context: [list]. Ready." Then answer with citations
   (wiki page + raw source).

### Recall constraints

- Read at most 8–10 pages. Stop when context is sufficient.
- Do NOT read raw sources unless a page is stale (`now >= stale_after`) or a claim is `NOT VERIFIED`.
- Read-only during recall.
- If the answer reveals a reusable insight not yet in the wiki, trigger `/file-back`.

---

## `--graph` mode: Relations traversal

Answer structured connection queries by reading `## Relations` SPO tables only — no full page text.

### Graph syntax

```text
/query --graph <entity-slug>              -> all relations touching entity (in + out)
/query --graph <predicate> <entity-slug>  -> filter by predicate
/query --graph <entity-slug> --in         -> only inbound edges (X -> entity)
/query --graph <entity-slug> --out        -> only outbound edges (entity -> X)
/query --graph <entity-slug> --hops 2     -> expand 2 hops (default: 1, max: 2)
```

Entity slug: bare slug (`mcp`) or wikilink form (`[[concept:mcp]]`); strip the `[[type:` prefix.

Predicate vocabularies: concept (`is-a`, `part-of`, `enables`, `implements`, `requires`,
`contrasts-with`, `extends`, `used-by`, `created-by`), person (`created`, `contributed-to`,
`works-at`, `influenced`, `co-authored`, `advocates-for`), project (`implements`, `extends`,
`replaces`, `integrates-with`, `created-by`, `used-by`, `part-of`), fiche (`argues-that`,
`extends`, `contrasts-with`, `implements`, `created-by`, `used-by`, `enables`).

### Graph workflow

1. **Parse** — normalize entity slug (lowercase, strip `[[type:` / `]]`); read predicate filter,
   direction (`--in`/`--out`/both), hops (default 1, max 2).
2. **Candidates** — read `wiki/index.md`; collect concept, project, person, organization, and
   source paths. Prioritize the page whose slug contains the entity, then same-cluster pages.
   Cap at **20 pages** for hop-0.
3. **Scan** — for each candidate, read its `## Relations` table; collect rows where Subject OR
   Object contains the entity slug (substring match). Apply predicate/direction filters.
4. **Hop** (default 1, max 2) — for each new entity surfaced, read its page and scan Relations,
   up to the 20-page cap; never re-scan a read page.
5. **Deduplicate** exact `(S, P, O)` triples, keep first occurrence.
6. **Output** the edge list. Read-only.

### Resolving a type to a page path

`[[type:slug]]` maps through the AGENTS.md Entity Types table, not the literal type word:

| Type | Directory | | Type | Directory |
|------|-----------|-|------|-----------|
| `concept` | `wiki/concepts/` | | `comparison` | `wiki/comparisons/` |
| `source` | `wiki/sources/` | | `synthesis` | `wiki/syntheses/` |
| `person` | `wiki/people/` | | `pattern` | `wiki/patterns/` |
| `project` | `wiki/projects/` | | `gap` | `wiki/gaps/` |
| `organization` | `wiki/organizations/` | | `domain` | `wiki/domains/` |
| `decision` | `wiki/decisions/` | | | |

### Graph output

```text
/query --graph: <entity-slug>  [predicate: <filter>]  [direction: <in|out|both>]

Outbound (<entity> -> *):
  [[type:entity]] <predicate> [[type:object]] — [page title](path)

Inbound (* -> <entity>):
  [[type:subject]] <predicate> [[type:entity]] — [page title](path)

Hop-1 extensions (via <intermediate>):
  [[type:s]] <predicate> [[type:o]] — [page title](path)  (via [[type:intermediate]])

---
Pages read: N / 20  |  Triples found: M  |  Unique entities: K
```

If no Relations tables are found: report it and suggest `make lint` (to find pages missing
`## Relations`) or an `/ingest` to populate them.

### Graph constraints

- Read-only; 20-page cap; 2-hop max.
- Slug matching is substring — prefer the longest match when ambiguous.
- No fabrication: an entity only in body text (not in a Relations table) is "mentioned (no triple)".
- Relations tables live in wiki pages only — never raw sources.

---

## Purpose

The query-side of the raw → wiki → answer loop (recall + graph merged). Both modes hit the
pre-compiled synthesis layer, never the raw sources — the LLM Wiki efficiency claim. Recall
loads page text for depth; `--graph` walks the edge list for connections.
