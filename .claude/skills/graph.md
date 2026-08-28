# Skill: /graph <query>

Traverses `## Relations` SPO tables across wiki pages to answer structured graph queries.
Use for: "what implements X?", "what relates to Y?", "what does Z enable?", "who created W?".

Complements `/recall` (which pre-loads full page text). `/graph` reads Relations tables only
and returns a structured edge list — faster for connection discovery, not for concept depth.

## When to Use

- "What implements [[concept:mcp]]?"
- "What does [[project:prometheus]] relate to?"
- "What is kubernetes-autoscaling connected to?"
- Exploring inbound or outbound edges from any entity
- After ingest — confirm Relations are wired up correctly

## Query Syntax

```
/graph <entity-slug>                    → all relations touching entity (in + out)
/graph <predicate> <entity-slug>        → filter by predicate
/graph <entity-slug> --in               → only inbound edges (X → entity)
/graph <entity-slug> --out              → only outbound edges (entity → X)
/graph <entity-slug> --hops 2           → expand 2 hops (default: 1)
```

**Entity slug:** bare slug (`mcp`, `prometheus`) or wikilink form (`[[concept:mcp]]`).
Strip `[[type:` prefix before matching.

**Valid predicates:**
- Concept: `is-a`, `part-of`, `enables`, `implements`, `requires`, `contrasts-with`, `extends`, `used-by`, `created-by`
- Person: `created`, `contributed-to`, `works-at`, `influenced`, `co-authored`, `advocates-for`
- Project: `implements`, `extends`, `replaces`, `integrates-with`, `created-by`, `used-by`, `part-of`
- Fiche: `argues-that`, `extends`, `contrasts-with`, `implements`, `created-by`, `used-by`, `enables`

## Workflow

### Step 1 — Parse query

Extract:
- **entity slug** — normalize: lowercase, strip `[[type:` prefix and `]]` suffix
- **predicate filter** (optional)
- **direction** — `--in` (inbound only), `--out` (outbound only), default both
- **hops** — default 1, max 2

### Step 2 — Identify candidate pages

Read `wiki/index.md`. Collect paths for all concept, project, person, and source (fiche) pages.
Prioritize:
1. Page whose slug contains the entity slug (most likely to have the entity as Subject)
2. Pages in the same domain cluster
3. All concept + project pages if entity is broad (domain-level)

Limit: **20 pages** for hop-0. Track how many are read.

### Step 3 — Scan Relations tables

For each candidate page:
1. Read the page.
2. Find `## Relations` section. If absent, skip.
3. For each table row: check if Subject OR Object contains the entity slug (substring match on slug part).
4. Collect matching rows as triples: `(Subject, Predicate, Object, source-page-path)`.
5. Apply predicate filter and direction filter if set.

### Step 4 — Hop expansion (default 1 hop, max 2)

For each **new entity** surfaced in step 3 results (entities not yet scanned):
- If that entity has a wiki page and fewer than 20 pages have been read: read it, scan its Relations table.
- Collect additional triples, tag as `(hop-1)` or `(hop-2)`.
- Do NOT re-scan already-read pages.
- Stop when 20-page limit reached.

### Step 5 — Deduplicate

Remove exact-duplicate (S, P, O) triples. Keep first occurrence (by source page).

### Step 6 — Output

Render result (see Output Format). Do NOT modify any files.

## Output Format

```
/graph: <entity-slug>  [predicate: <filter>]  [direction: <in|out|both>]

Outbound (<entity> → *):
  [[type:entity]] <predicate> [[type:object]] — [page title](path)
  …

Inbound (* → <entity>):
  [[type:subject]] <predicate> [[type:entity]] — [page title](path)
  …

Hop-1 extensions (via <intermediate>):
  [[type:s]] <predicate> [[type:o]] — [page title](path)  ← via [[type:intermediate]]
  …

---
Pages read: N / 20  |  Triples found: M  |  Unique entities: K
```

If zero Relations tables found across all pages:
```
/graph: <entity-slug>

No Relations data found. Likely causes:
- Entity pages exist but ## Relations section is empty or placeholder-only
- Run /lint to check: "Concept/project/person pages missing ## Relations"
- Or run /ingest on source pages to populate Relations
```

## Constraints

- **Read-only.** Do NOT modify any files, log, or index.
- **20-page cap.** Stop scanning when reached; note in output.
- **2-hop max.** Never recurse deeper.
- **Slug matching is substring.** `mcp` matches `model-context-protocol-mcp`. Prefer the longest match when ambiguous.
- **No fabrication.** If entity appears only in page body (not in a Relations table), note it as `"mentioned (no triple)"` — do not emit it as a triple.
- **No raw sources.** Relations tables live in wiki pages only.
