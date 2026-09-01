# Skill: /ingest <path> [--fiche]

Full ingest workflow for a single raw source. Reads source → identifies entities → creates/updates wiki pages → links → logs.

Two modes:
- **Default** — full treatment: 10–15 pages, Rhetorical Analysis, KnowledgeGraph. Use for books, papers, talks.
- **`--fiche`** — single fiche card: 1 page, ~400 words, fast capture. Use for articles, blog posts, short reads.

## When to Use

- New file dropped in `raw/`
- User says "ingest raw/<filename>", "/ingest <path>", or "/ingest --fiche <url-or-path>"
- Choose `--fiche` when: article/blog post, read time < 20 min, < 5 new entities to create

## Workflow

1. **Read source fully.** Do not skim. For long documents, read all sections.
2. **Identify all entities:** concepts, people, projects, organisations, decisions, tools mentioned.
3. **Create/update wiki pages** for each entity:
   - New entity → create page from `wiki/schema.md` template for that entity type
   - Existing entity → update the page, bump `updated:` date
   - For concept/project/person pages: populate `## Relations` table with top 5 SPO triples
     drawn from this source (use wikilinks for Subject and Object; pick from the predicate
     vocabulary in the template comment). Merge with existing relations — no duplicates.
4. **Fill in KnowledgeGraph section** on the Source page:
   - `### Triples` — one row per relation extracted from source
   - `### Entities` — one row per entity, tagged AJOUT or MISE_A_JOUR
   - Fill `Rhetorical Analysis` section
5. **Add wikilinks** from related pages to new pages and back.
6. **Update `wiki/index.md`** — add new pages under their entity-type section.
7. **Update `wiki/hot.md`** — set Focus to current ingest, list active pages.
8. **Append to `wiki/log.md`** with `[INGEST]` prefix.

## Fiche Mode Workflow (`--fiche`)

Optimised for speed. Do NOT do full entity extraction — fiche is the deliverable.

1. **Read source.** Skim for main argument, key points, notable quotes.
2. **Create one fiche page** in `wiki/sources/` using the **Fiche Page** template from `wiki/schema.md`:
   - `## En Bref` — 2–3 sentences: what it argues + why it matters
   - `## Points Clés` — 3–5 concrete bullet claims
   - `## Citation Notable` — best single quote
   - `## Relations` — 3–5 SPO triples (wikilinks to existing pages; do NOT create new pages for unrecognised entities)
   - `## Liens Wiki` — link to existing wiki pages that this fiche enriches
3. **Update existing entity pages** lightly: add fiche to `## Related` or `## Relations` on concept/project pages if strongly relevant. Do NOT create new entity pages for entities not yet in the wiki — add them to `raw/queue.md` as follow-up ingests instead.
4. **Update `wiki/index.md`** — add fiche under Sources.
5. **Append to `wiki/log.md`** with `[INGEST]` prefix and note `(fiche)`.
6. **Update `raw/queue.md`** — move URL from `## Pending` to `## Done` with link to fiche page.

## Log Entry Format

Full ingest:
```
## [YYYY-MM-DD] [INGEST] | Added "<title>" by <author>
  └─ pages: <comma-separated list of created/updated pages>
  └─ sources: <raw path or url>
```

Fiche:
```
## [YYYY-MM-DD] [INGEST] | Fiche — "<title>" by <author>
  └─ pages: wiki/sources/<slug>.md (fiche)
  └─ sources: <url or raw path>
```

## Quality Checklist

**Full ingest — before finishing:**
- [ ] Source page exists in `wiki/sources/` with full frontmatter
- [ ] `## KnowledgeGraph` section filled — no empty tables
- [ ] `## Rhetorical Analysis` section filled
- [ ] Every entity mentioned has a wiki page (or stub) + wikilink
- [ ] Concept/project/person pages have `## Relations` table populated (≥1 row, no placeholder rows)
- [ ] All new pages in `wiki/index.md`
- [ ] All new pages wikilinked from their parent domain page
- [ ] `wiki/log.md` appended
- [ ] No `TODO`, `TBD`, `{text}` placeholders left

**Fiche mode — before finishing:**
- [ ] Fiche page in `wiki/sources/` with `format: fiche` frontmatter
- [ ] `stale_after` set (6mo for AI/protocols, 1yr for k8s, omit for evergreen)
- [ ] `## En Bref` filled — 2–3 sentences, no placeholders
- [ ] `## Points Clés` — 3–5 concrete claims, no vague bullet points
- [ ] `## Relations` — ≥1 real triple with wikilinks to existing pages
- [ ] Fiche in `wiki/index.md` under Sources
- [ ] `raw/queue.md` updated — URL moved to `## Done`
- [ ] `wiki/log.md` appended with `(fiche)` tag

## Naming Conventions

- Source pages: `wiki/sources/<author-slug>-<short-title-slug>-YYYY.md`
- Concept pages: `wiki/concepts/<concept-slug>.md`
- Person pages: `wiki/people/<firstname-lastname.md>`
- Project pages: `wiki/projects/<project-slug>.md`

## Constraints

- Do NOT modify `raw/` — immutable.
- Do NOT create placeholder pages — only pages with real content from this source.
- Mark claims without source citation as `NOT VERIFIED`.
- If source conflicts with existing wiki page, document both positions and mark `PENDING — escalate to human`.
