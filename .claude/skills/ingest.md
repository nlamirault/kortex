# Skill: /ingest <path>

Full ingest workflow for a single raw source. Reads source → identifies entities → creates/updates wiki pages → links → logs.

## When to Use

- New file dropped in `raw/`
- User says "ingest raw/<filename>" or "/ingest <path>"

## Workflow

1. **Read source fully.** Do not skim. For long documents, read all sections.
2. **Identify all entities:** concepts, people, projects, organisations, decisions, tools mentioned.
3. **Create/update wiki pages** for each entity:
   - New entity → create page from `wiki/schema.md` template for that entity type
   - Existing entity → update the page, bump `updated:` date
4. **Fill in KnowledgeGraph section** on the Source page:
   - `### Triples` — one row per relation extracted from source
   - `### Entities` — one row per entity, tagged AJOUT or MISE_A_JOUR
   - Fill `Rhetorical Analysis` section
5. **Add wikilinks** from related pages to new pages and back.
6. **Update `wiki/index.md`** — add new pages under their entity-type section.
7. **Update `wiki/hot.md`** — set Focus to current ingest, list active pages.
8. **Append to `wiki/log.md`** with `[INGEST]` prefix.

## Log Entry Format

```
## [YYYY-MM-DD] [INGEST] | Added "<title>" by <author>
  └─ pages: <comma-separated list of created/updated pages>
  └─ sources: <raw path>
```

## Quality Checklist

Before finishing ingest:
- [ ] Source page exists in `wiki/sources/` with full frontmatter
- [ ] `## KnowledgeGraph` section filled — no empty tables
- [ ] `## Rhetorical Analysis` section filled
- [ ] Every entity mentioned has a wiki page (or stub) + wikilink
- [ ] All new pages in `wiki/index.md`
- [ ] All new pages wikilinked from their parent domain page
- [ ] `wiki/log.md` appended
- [ ] No `TODO`, `TBD`, `{text}` placeholders left

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
