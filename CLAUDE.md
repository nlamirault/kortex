# Kortex — LLM Wiki Schema

Kortex is a personal knowledge base powered by the LLM Wiki protocol (Karpathy, 2024).
This file is the operational schema. Read it before every session.

---

## Directory Layout

```
kortex/
├── CLAUDE.md          ← this schema (operational rules)
├── raw/               ← immutable source documents (read-only)
│   └── README.md
└── wiki/              ← LLM-maintained synthesis layer
    ├── index.md       ← content catalog by category
    ├── log.md         ← append-only activity log
    ├── schema.md      ← entity templates and type definitions
    └── <domain>/      ← one directory per knowledge domain
```

**Rules:**
- `raw/` is **read-only**. Never modify, rename, or delete raw sources.
- `wiki/` is **LLM-maintained**. Update proactively; never leave stale after a session.
- This file is **the contract**. Adapt it to new domains, but version changes via log.

---

## Entity Types

Every wiki page must be one of these types (set in frontmatter):

| Type | Purpose | Directory |
|------|---------|-----------|
| `concept` | Ideas, frameworks, mental models | `wiki/concepts/` |
| `source` | Books, papers, articles, talks | `wiki/sources/` |
| `person` | Authors, researchers, thinkers | `wiki/people/` |
| `project` | Tools, codebases, initiatives | `wiki/projects/` |
| `decision` | Architectural or design choices | `wiki/decisions/` |
| `domain` | Broad topic areas (hub pages) | `wiki/domains/` |
| `log` | Special — only `wiki/log.md` | — |
| `index` | Special — only `wiki/index.md` | — |

---

## Frontmatter Template

Every wiki page (except `log.md` and `index.md`) must begin with:

```yaml
---
title: <page title>
type: <entity type>
status: <draft | active | stale | archived>
sources: [<raw/filename or URL>]
updated: <YYYY-MM-DD>
tags: [<tag1>, <tag2>]
---
```

---

## Wikilink Convention

Use `[[type:slug]]` for cross-references:

```
[[concept:zettelkasten]]
[[source:building-a-second-brain]]
[[person:andy-matuschak]]
[[project:obsidian]]
[[decision:flat-vs-hierarchical-structure]]
[[domain:knowledge-management]]
```

Render as markdown links pointing to the correct file path:
`[Zettelkasten](../concepts/zettelkasten.md)`

---

## Four Core Operations

### 1. Ingest

Triggered when a new raw source is added to `raw/`.

1. Read the source fully.
2. Identify entities (concepts, people, projects) mentioned.
3. Create or update the relevant wiki pages.
4. Add cross-references from related existing pages.
5. Update `wiki/index.md`.
6. Append to `wiki/log.md` with prefix `[INGEST]`.

### 2. Query

Triggered when the user asks a question.

1. Identify relevant wiki pages (check index, follow wikilinks).
2. Synthesize an answer with citations to wiki pages and raw sources.
3. If the answer reveals new insight not yet in the wiki, file it back.
4. Append to `wiki/log.md` with prefix `[QUERY]` if new pages were created.

### 3. Lint

Triggered periodically or on demand (`/lint`).

Check for:
- [ ] Broken wikilinks (target page missing)
- [ ] Stale pages (status not updated after source changes)
- [ ] Orphan pages (not linked from index or any other page)
- [ ] Contradictions between pages (document both, flag with `status: conflict`)
- [ ] Missing frontmatter fields
- [ ] Pages with no sources cited

Append findings to `wiki/log.md` with prefix `[LINT]`.

### 4. File Back

Triggered when a conversation yields a reusable insight.

1. Identify the synthesized knowledge (decision, framework, analysis).
2. Create a new wiki page or append to an existing one.
3. Cite the conversation context as the source.
4. Link from relevant parent pages and index.
5. Append to `wiki/log.md` with prefix `[FILE]`.

---

## Seven Hard Rules

1. **Update before ending.** Every session that touches knowledge must update the wiki before stopping.
2. **Log every edit.** Every create/update/delete to any wiki page gets a log entry.
3. **Frontmatter is current.** `updated` date must reflect actual last change.
4. **Link new pages.** Every new page must be linked from `wiki/index.md` and at least one parent page.
5. **Never delete gaps.** Mark unresolved contradictions or unknowns — do not remove them.
6. **Trace every claim.** Every factual claim links to a raw source or another wiki page.
7. **Flag contradictions.** When sources conflict, document both positions and mark `status: conflict`.

---

## Log Format

```
YYYY-MM-DD HH:MM | [OP] | <summary of action>
  └─ pages: <list of affected wiki pages>
  └─ sources: <list of raw sources or URLs consulted>
```

Example:
```
2026-05-04 14:32 | [INGEST] | Added "How to Take Smart Notes" by Ahrens
  └─ pages: sources/how-to-take-smart-notes.md, concepts/zettelkasten.md, people/niklas-luhmann.md
  └─ sources: raw/ahrens-smart-notes.pdf
```

---

## Index Format

`wiki/index.md` is organized by entity type. Each entry is one line:

```
- [Page Title](path/to/page.md) — one-line description
```

---

## Bootstrap Checklist

On first session with a new knowledge domain:

- [ ] Create domain hub page in `wiki/domains/`
- [ ] Add domain to `wiki/index.md`
- [ ] Identify 3-5 seed concepts for that domain
- [ ] Create stub pages for each seed concept
- [ ] Log the bootstrap in `wiki/log.md`
