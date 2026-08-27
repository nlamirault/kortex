# Kortex — LLM Wiki Schema

Kortex is a personal knowledge base powered by the LLM Wiki protocol (Karpathy, 2024).
This file is the operational schema. **Read it before every session.**

---

## The Three-Layer Architecture

![LLM Wiki Architecture by Andrej Karpathy](https://datasciencedojo.com/wp-content/uploads/2026/04/LLM-Wiki-by-Andrej-Karpathy.png)

> "Just as source code compiles once into a binary for repeated execution, raw sources are
> synthesized into a wiki that gets richer with each addition. The wiki becomes
> pre-synthesized, interlinked, and always ready." — Karpathy

The system has three distinct, non-overlapping layers:

```
┌─────────────────────────────────────────────────────────┐
│  Layer 3 — Schema                                       │
│  CLAUDE.md  ← operational rules, entity types,          │
│               workflows, and agent behavior              │
├─────────────────────────────────────────────────────────┤
│  Layer 2 — Wiki                                         │
│  wiki/      ← LLM-maintained synthesis: entity pages,   │
│               concept pages, summaries, cross-refs       │
├─────────────────────────────────────────────────────────┤
│  Layer 1 — Raw Sources                                  │
│  raw/       ← immutable ground truth: PDFs, articles,   │
│               notes — never modified by LLM              │
└─────────────────────────────────────────────────────────┘
```

| Layer | Owner | Mutability | Purpose |
|-------|-------|-----------|---------|
| **Raw Sources** (`raw/`) | Human | Immutable | Ground truth documents |
| **Wiki** (`wiki/`) | LLM | Actively maintained | Pre-synthesized knowledge |
| **Schema** (`CLAUDE.md`) | Human + LLM | Co-evolved | Operating rules and structure |

**Why this beats RAG:** RAG re-derives knowledge from raw sources on every query. The wiki
is compiled once and enriched continuously — queries hit the synthesized layer, not the raw
documents. Knowledge compounds; it doesn't disappear into chat history.

---

## The Three Operations

```
  raw/                wiki/               user
   │                    │                  │
   │──[new source]──►   │                  │
   │    INGEST           │                  │
   │         creates/updates pages          │
   │                    │◄─────[question]──┤
   │                    │      QUERY        │
   │                    │──[answer+cite]──► │
   │                    │                  │
   │                    │◄─[/lint]─────────┤
   │                    │      LINT         │
   │                    │──[health report]►│
   │                    │                  │
   │                    │◄─[insight]───────┤
   │                    │    FILE BACK      │
   │                    │  (files to wiki)  │
```

### Operation 1: Ingest

**Trigger:** New file dropped in `raw/` → say `"Ingest raw/<filename>"` or `/ingest --fiche <url>` for articles.

Two modes — choose before starting:

| Mode | Command | Use for | Output |
|------|---------|---------|--------|
| Full | `/ingest <path>` | Books, papers, talks (>20 min read) | 10–15 wiki pages |
| Fiche | `/ingest --fiche <path>` | Articles, blog posts (<20 min read) | 1 fiche card |

**Full ingest steps:**
1. Read source fully — do not skim.
2. Identify all entities mentioned (concepts, people, projects, decisions).
3. Create new wiki pages or update existing ones for each entity.
4. Add `[[wikilinks]]` from related pages to new pages and back.
5. Update `wiki/index.md` with new entries.
6. Append to `wiki/log.md` with prefix `[INGEST]`.

**Fiche steps:** read → one fiche card (En Bref + Points Clés + Relations) → update index → log → mark queue done.

**Skill:** `/ingest <path>` or `/ingest --fiche <path>` — see `.claude/skills/ingest.md` for full workflow.

---

### Operation 2: Query

**Trigger:** User asks any question about the knowledge base.

Rather than going back to raw sources, the LLM reads relevant wiki pages and synthesizes
an answer with citations. If the answer reveals a reusable insight not yet in the wiki,
it is filed back as a new page automatically.

**Steps:**
1. Read `wiki/index.md` to locate relevant pages.
2. Follow `[[wikilinks]]` to related pages as needed.
3. Synthesize answer with explicit citations (wiki page + source).
4. If answer is novel and reusable → trigger File Back.
5. Append to `wiki/log.md` with prefix `[QUERY]` only if new pages were created.
6. Read raw sources **only if**: wiki page is `status: stale`, claim marked `NOT VERIFIED`,
   or sources conflict and must be resolved.

**Skill:** Natural language — no slash command needed. Just ask.

---

### Operation 3: Lint

**Trigger:** `/lint` command, or periodically at the user's request.

Periodic health audit of the wiki. Finds drift, decay, and inconsistency before they
compound. Reports are tiered by severity.

**Checks:**
- [ ] Broken `[[wikilinks]]` (target page missing)
- [ ] Orphan pages (not linked from index or any other page)
- [ ] Stale pages (`status: stale` or `updated` date old)
- [ ] Expired pages (`stale_after` < today) → CRITICAL, mark `status: stale`
- [ ] Expiring-soon pages (`stale_after` within 30 days) → WARNING
- [ ] Contradictions between pages → flag both, mark `PENDING — escalate to human`
- [ ] Missing frontmatter fields
- [ ] Claims without source citations → mark `NOT VERIFIED`
- [ ] Unfilled template placeholders (`TODO`, `TBD`, `{text}`)
- [ ] Pages not in `wiki/index.md`

**Output:** Severity-tiered report. Fix critical issues immediately; log all findings.

**Skill:** `/lint` — runs the full lint workflow and produces a structured report.

---

### Operation 4: File Back

**Trigger:** A conversation yields a reusable insight, decision, or synthesis.

Captures knowledge that emerges during dialogue — decisions made, frameworks discovered,
analyses completed — and files it permanently into the wiki before it is lost to chat
history.

**Steps:**
1. Identify the reusable knowledge (decision, framework, synthesis, analysis).
2. Determine the correct entity type and target page.
3. Create new wiki page or append to existing one.
4. Cite the conversation as source (date + topic).
5. Link from relevant parent pages and `wiki/index.md`.
6. Append to `wiki/log.md` with prefix `[FILE]`.

**Skill:** `/file-back "<title>"` — prompts for entity type and files the current
conversation insight as a wiki page.

---

## Skills Reference

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `/today` | Session start | Morning briefing from hot cache + recent log |
| `/recall` | Before any query | Pre-load relevant wiki pages into context |
| `/ingest <path>` | New source added | Full ingest: read → create/update pages → link → log. Books, papers, talks. |
| `/ingest --fiche <path>` | Article/blog post added | Fiche mode: single ~400-word card → link → log. Articles, short reads. |
| `/lint` | Weekly or on demand | Health audit: broken links, orphans, stale, contradictions |
| `/file-back "<title>"` | Insight from conversation | Capture and file reusable knowledge to wiki |
| `/bootstrap <domain>` | Starting a new domain | Create domain hub + seed concept stubs + log |
| `/close` | Session end | Update hot cache, verify consistency, summarize |

Skills live in `.claude/skills/`. Read the skill file for full workflow details.

---

## Session Startup Protocol

Read in this order at the start of every session:

1. **`wiki/hot.md`** — session hot cache; current focus, open questions, active pages
2. **This file** (`CLAUDE.md`) — schema and operating rules (skip if familiar)
3. **`wiki/index.md`** — locate pages relevant to the current task
4. **`wiki/overview.md`** — cluster navigation if working across domains
5. **`wiki/domains/<relevant>.md`** — domain hub page if applicable
6. **Follow `[[wikilinks]]`** — navigate to concept/source pages as needed
7. **`raw/` sources** — only when wiki says `NOT VERIFIED`, `status: stale`, or a
   contradiction must be resolved

**Never** read all raw sources at session start. The wiki exists to prevent this.

**Skill:** `/today` — automated startup briefing from hot cache + recent log.

---

## Directory Layout

```
kortex/
├── CLAUDE.md              ← this schema (read first)
├── .claude/
│   └── skills/            ← custom session skills
│       ├── today.md       ← /today  morning startup briefing
│       ├── close.md       ← /close  end-of-session routine
│       └── recall.md      ← /recall pre-load wiki context before answering
├── raw/                   ← immutable source documents (read-only)
│   ├── articles/          ← web articles, blog posts
│   ├── papers/            ← academic papers, research
│   ├── repos/             ← code repositories, READMEs
│   ├── transcripts/       ← talks, interviews, podcasts
│   ├── data/              ← datasets, CSVs, structured data
│   └── assets/            ← images, diagrams, attachments
└── wiki/                  ← LLM-maintained synthesis layer
    ├── index.md           ← content catalog by category
    ├── log.md             ← append-only activity log
    ├── hot.md             ← session hot cache (~500 words, read first)
    ├── overview.md        ← cluster navigation hub
    ├── schema.md          ← entity templates and type definitions
    ├── domains/           ← broad topic hub pages (tier-2)
    ├── concepts/          ← ideas, frameworks, mental models (tier-3)
    ├── sources/           ← book/article/paper summaries (tier-4)
    ├── people/            ← authors, researchers, thinkers
    ├── projects/          ← tools, codebases, initiatives
    ├── decisions/         ← architectural and design choices
    ├── comparisons/       ← side-by-side source/tool analysis
    ├── syntheses/         ← cross-source analyses from queries (tier-5, leaves)
    └── gaps/              ← open questions and deficiencies
```

---

## Entity Types

Every wiki page must be one of these types (set in frontmatter):

| Type | Purpose | Directory |
|------|---------|-----------|
| `domain` | Broad topic areas — hub pages | `wiki/domains/` |
| `concept` | Ideas, frameworks, mental models | `wiki/concepts/` |
| `source` | Books, papers, articles, talks | `wiki/sources/` |
| `person` | Authors, researchers, thinkers | `wiki/people/` |
| `project` | Tools, codebases, initiatives | `wiki/projects/` |
| `decision` | Architectural or design choices | `wiki/decisions/` |
| `comparison` | Side-by-side analysis of sources or tools | `wiki/comparisons/` |
| `synthesis` | Cross-source analyses filed from queries (leaves) | `wiki/syntheses/` |
| `gap` | Open questions, unknowns, deficiencies | `wiki/gaps/` |
| `log` | Special — only `wiki/log.md` | — |
| `index` | Special — only `wiki/index.md` | — |

---

## Frontmatter Template

Every wiki page (except `log.md` and `index.md`) must begin with:

```yaml
---
title: <page title>
type: <entity type>
status: <draft | active | stale | superseded>
confidence: <low | medium | high>
cluster: <domain slug this page belongs to>
domain: [<relevant domain slug>]
sources: [<raw/filename or URL>]
updated: <YYYY-MM-DD>
tags: [<tag1>, <tag2>]
generated: {by: <model-id>, at: <YYYY-MM-DD>}
verified: [{by: <name>, at: <YYYY-MM-DD>}]
stale_after: <YYYY-MM-DD>          # optional — omit for evergreen content
---
```

**Status values:**
- `draft` — stub or in-progress, not yet complete
- `active` — current and accurate
- `stale` — source changed or update needed; do not trust without verification
- `superseded` — replaced by another page (add link to replacement)

**Confidence values:**
- `high` — multiple sources agree, well-verified
- `medium` — single source or partially verified
- `low` — uncertain, inferred, or unverified — treat claims with caution

**OKF v0.2 trust signal fields:**
- `generated` — records which model (or human) authored the page and when. Always set on LLM-synthesized pages. Format: `{by: claude-sonnet-4-6, at: 2026-08-17}`
- `verified` — list of human or agent sign-offs. Empty list `[]` means unverified. Add an entry when a human reviews and confirms the page. Format: `[{by: nicolas, at: 2026-08-17}]`
- `stale_after` — absolute expiry date after which the page must be re-verified. Omit for stable/evergreen content. Set for fast-moving domains: AI protocols (6 months), Kubernetes ecosystem (1 year).

**Inline markers:**
- `NOT VERIFIED` — claim has no traceable source; must be verified before trusting
- `PENDING — escalate to human` — contradiction between sources; human must resolve

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
[[comparison:zettelkasten-vs-para]]
[[synthesis:pkm-tool-comparison-2026]]
[[gap:unresolved-spaced-repetition-debate]]
```

Render as markdown links: `[Zettelkasten](../concepts/zettelkasten.md)`

Every new page must be wikilinked from its parent domain page and from `wiki/index.md`.

---

## Seven Hard Rules

1. **Update before ending.** Every session that touches knowledge must update relevant wiki
   pages before stopping.
2. **Log every edit.** Every create/update/delete to any wiki page gets a `wiki/log.md`
   entry with date, pages affected, and source referenced. Also add the affected pages to
   the `## By Date` section of `wiki/index.md` under today's date — use the log operation
   tag as suffix (e.g. `[INGEST]`). Batch entries from the same operation on one line.
   Prune entries older than 90 days to a single summary line.
3. **Frontmatter stays current.** Set `updated:` on every touched page. Mark outdated
   pages `status: stale` immediately — stale is worse than missing.
4. **Link new pages.** Every new page must be in `wiki/index.md` and wikilinked from at
   least one parent page.
5. **Gaps don't disappear.** Mark resolved gaps `✅ Resolved — YYYY-MM-DD` with evidence.
   Preserve the history; never delete the gap entry.
6. **Trace every claim.** Every factual claim must reference a raw source file or another
   wiki page. Untraceable claims are marked `NOT VERIFIED`.
7. **Flag contradictions, don't guess.** When sources conflict, document **both** positions
   with file references and mark `PENDING — escalate to human`. Never silently pick one.

---

## Hard Don'ts

- Do **not** read all raw sources at session start — the wiki prevents this
- Do **not** leave template placeholders (`TODO`, `TBD`, `{text}`, `{N}`)
- Do **not** modify files in `raw/` — they are immutable ground truth
- Do **not** create placeholder wiki pages — only create pages with real content
- Do **not** duplicate wiki content in multiple pages — one canonical page, others link to it
- Do **not** treat the wiki as append-only — update existing pages, don't just add
- Do **not** skip wiki updates for "small" changes — all changes get logged

---

## Anti-Corruption Rules

1. **Code/source is truth.** When wiki and source disagree, update the wiki — not the source.
2. **Stale is worse than missing.** An outdated page actively misleads. Mark stale immediately.
3. **One source of truth per fact.** One canonical page; all others wikilink to it. No duplication.
4. **Every fact has provenance.** No traceable source → mark `NOT VERIFIED`.
5. **Contradictions are features.** Flagging a contradiction is more valuable than silently
   resolving it incorrectly.

---

## Log Format

```
## [YYYY-MM-DD] [OP] | <summary>
  └─ pages: <list of affected wiki pages>
  └─ sources: <list of raw sources or URLs consulted>
```

Example:
```
## [2026-05-04] [INGEST] | Added "How to Take Smart Notes" by Ahrens
  └─ pages: sources/how-to-take-smart-notes.md, concepts/zettelkasten.md, people/niklas-luhmann.md
  └─ sources: raw/ahrens-smart-notes.pdf
```

Operations: `[INIT]` `[INGEST]` `[QUERY]` `[LINT]` `[FILE]` `[UPDATE]` `[BOOTSTRAP]`

**Failure logging:** Use `!failure` tag when a dead-end is hit:
```
## [2026-05-04] !failure | Attempted ingest of paywalled article — blocked
  └─ pages: none
  └─ sources: raw/articles/blocked-article.pdf
  └─ note: PDF was corrupted; try re-downloading
```

---

## Index Format

`wiki/index.md` is organized by entity type. Each entry is one line:

```
- [Page Title](path/to/page.md) — one-line description
```

---

## Bootstrap Checklist

When starting a new knowledge domain (`/bootstrap <domain>`):

- [ ] Create domain hub page in `wiki/domains/<slug>.md`
- [ ] Add domain to `wiki/index.md` under Domains
- [ ] Identify 3–5 seed concepts for the domain
- [ ] Create stub pages for each seed concept in `wiki/concepts/`
- [ ] Link seed concepts from domain hub page
- [ ] Append `[BOOTSTRAP]` entry to `wiki/log.md`
