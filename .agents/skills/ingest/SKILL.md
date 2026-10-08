---
name: ingest
description: Ingest a raw source into the wiki — read fully, extract entities, create/update pages, wire Relations, link, log. Trigger when a new file lands in raw/ or the user says "ingest <path>". Use --fiche for short articles/blog posts.
---

# Skill: /ingest <path> [--fiche]

Full ingest workflow for a single raw source (Operation 1). Reads the source -> identifies
entities -> creates/updates wiki pages -> links -> logs.

Two modes:

- **Default** — full treatment: 10–15 pages, Rhetorical Analysis, KnowledgeGraph. Use for books, papers, talks.
- **`--fiche`** — a single fiche card: 1 page, ~400 words, fast capture. Use for articles, blog posts, short reads.

## When to Use

- A new file dropped in `raw/`.
- User says `ingest raw/<filename>`, `/ingest <path>`, or `/ingest --fiche <url-or-path>`.
- Choose `--fiche` when: article/blog post, read time < 20 min, fewer than 5 new entities to create.

## Full Ingest Workflow

1. **Read the source fully.** Do not skim. For long documents, read all sections.
2. **Identify all entities:** concepts, people, projects, organizations, decisions, tools mentioned.
3. **Create/update wiki pages** for each entity:
   - New entity -> create a page from the matching template in `wiki/schema.md`.
   - Existing entity -> update the page, bump `updated:`.
   - For concept/project/person pages: populate the `## Relations` table with the top 5 SPO
     triples drawn from this source. Subject/Object cells use **raw `[[type:slug]]`** — this
     is the only place that form is allowed (it is machine-read by `/query --graph`). Pick predicates
     from the template vocabulary. Merge with existing relations — no duplicates.
4. **Fill in the KnowledgeGraph section** on the Source page:
   - `### Triples` — one row per relation extracted from the source.
   - `### Entities` — one row per entity, tagged AJOUT or MISE_A_JOUR.
   - Fill the `## Rhetorical Analysis` section.
5. **Cross-link pages** — from related pages to the new pages and back. In prose, `## Related`
   / `## See Also` bullets, and any human-readable text, use **rendered markdown links**
   `[Title](../dir/slug.md)`, never bare `[[type:slug]]` (GitHub does not render wikilinks).
   Raw `[[type:slug]]` belongs only in `## Relations` tables. See AGENTS.md -> Wikilink Convention.
6. **Update `wiki/index.md`** — add new pages under their entity-type section, and add every
   created/updated page to the `## By Date` section under today's date, suffixed `[INGEST]`.
7. **Update `wiki/hot.md`** — set Focus to the current ingest, list the active pages.
8. **Record in `wiki/log.md`** — see Log Entry Format.
9. **Rebuild the knowledge-base nodes** — run `make kb` (invokes
   `scripts/build_knowledge_base.py`) so `wiki/kb/*.md` stays in sync with the Relations graph.

## Fiche Mode Workflow (`--fiche`)

Optimized for speed. Do NOT do full entity extraction — the fiche is the deliverable.

1. **Read the source.** Skim for the main argument, key points, notable quotes.
2. **Create one fiche page** in `wiki/sources/` using the **Fiche Page** template from `wiki/schema.md`:
   - `## En Bref` — 2–3 sentences: what it argues + why it matters.
   - `## Points Clés` — 3–5 concrete bullet claims.
   - `## Citation Notable` — the best single quote.
   - `## Relations` — 3–5 SPO triples using raw `[[type:slug]]` (Relations tables only; do NOT create new pages for unrecognized entities).
   - `## Liens Wiki` — markdown links `[Title](../dir/slug.md)` to existing wiki pages this fiche enriches.
3. **Update existing entity pages** lightly: add the fiche to `## Related` or `## Relations` on
   strongly relevant concept/project pages. Do NOT create new entity pages for entities not yet
   in the wiki — add them to `raw/queue.md` as follow-up ingests instead.
4. **Update `wiki/index.md`** — add the fiche under Sources and to `## By Date` (today, `[INGEST]`).
5. **Record in `wiki/log.md`** with `(fiche)` noted.
6. **Update `raw/queue.md`** — move the URL from `## Pending` to `## Done` with a link to the fiche page.

## Frontmatter on Every Page Written

Every created or updated page carries OKF v0.2 frontmatter (AGENTS.md -> Frontmatter Template):

- `type:` — required.
- `generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}`.
- `verified: []` — unless a human has signed off.
- `sources:` — a list of mappings, each with a required `resource:` (the raw path or URL).
- `stale_after:` — ISO-8601 instant with offset (AI/protocols 6mo, Kubernetes 1yr; omit if evergreen).
- `updated: <YYYY-MM-DD>`.

## Log Entry Format

`wiki/log.md` is newest-first. Insert under today's `## YYYY-MM-DD` heading at the top of the
file (create the heading if it is not already today's):

```text
- **[INGEST]** Added "<title>" by <author> — pages: <comma-separated created/updated>; sources: <raw path or URL>
```

Fiche:

```text
- **[INGEST]** Fiche — "<title>" by <author> (fiche) — pages: wiki/sources/<slug>.md; sources: <raw path or URL>
```

## Quality Checklist

**Full ingest — before finishing:**

- [ ] Source page exists in `wiki/sources/` with full OKF frontmatter.
- [ ] `## KnowledgeGraph` section filled — no empty tables.
- [ ] `## Rhetorical Analysis` section filled.
- [ ] Every entity mentioned has a wiki page (or stub) + link.
- [ ] Concept/project/person pages have a populated `## Relations` table (>= 1 real row).
- [ ] No bare `[[type:slug]]` outside `## Relations` tables — prose/Related/See Also use markdown links.
- [ ] All new pages in `wiki/index.md` (entity section + `## By Date`).
- [ ] All new pages wikilinked from their parent domain page.
- [ ] `wiki/log.md` updated (newest-first).
- [ ] `make kb` run; `wiki/kb/` regenerated.
- [ ] No `TODO`, `TBD`, `{text}` placeholders left.

**Fiche mode — before finishing:**

- [ ] Fiche page in `wiki/sources/` with `type: source` and OKF frontmatter.
- [ ] `stale_after` set (6mo for AI/protocols, 1yr for k8s, omit if evergreen).
- [ ] `## En Bref` filled — 2–3 sentences, no placeholders.
- [ ] `## Points Clés` — 3–5 concrete claims.
- [ ] `## Relations` — >= 1 real triple with `[[type:slug]]` to existing pages.
- [ ] `## Liens Wiki` and any prose use markdown links, not bare `[[type:slug]]`.
- [ ] Fiche in `wiki/index.md` under Sources + `## By Date`.
- [ ] `raw/queue.md` updated — URL moved to `## Done`.
- [ ] `wiki/log.md` updated with `(fiche)`.

## Naming Conventions

- Source pages: `wiki/sources/<author-slug>-<short-title-slug>-YYYY.md`
- Concept pages: `wiki/concepts/<concept-slug>.md`
- Person pages: `wiki/people/<firstname-lastname>.md`
- Project pages: `wiki/projects/<project-slug>.md`

## Constraints

- Do NOT modify `raw/` — it is immutable ground truth.
- Do NOT create placeholder pages — only pages with real content from this source.
- Mark claims without a source citation as `NOT VERIFIED`.
- If the source conflicts with an existing wiki page, document both positions and mark
  `PENDING — escalate to human`. Never silently pick one.

## Purpose

Operation 1 (Ingest). Compiles raw sources into the synthesized wiki layer — the `raw -> wiki`
arc, run once per source so knowledge compounds instead of being re-derived per query.
