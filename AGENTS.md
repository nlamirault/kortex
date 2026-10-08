# Kortex — LLM Wiki Schema

Kortex is a personal knowledge base powered by the LLM Wiki protocol (Karpathy, 2024),
with every wiki page serialized as an [Open Knowledge Format (OKF) **v0.2**](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
concept document. `wiki/` is the OKF bundle. This file is the operational schema.
**Read it before every session.**

---

## The Three-Layer Architecture

![LLM Wiki Architecture by Andrej Karpathy](https://datasciencedojo.com/wp-content/uploads/2026/04/LLM-Wiki-by-Andrej-Karpathy.png)

> "Just as source code compiles once into a binary for repeated execution, raw sources are
> synthesized into a wiki that gets richer with each addition. The wiki becomes
> pre-synthesized, interlinked, and always ready." — Karpathy

The system has three distinct, non-overlapping layers:

```text
┌─────────────────────────────────────────────────────────┐
│  Layer 3 — Schema                                       │
│  AGENTS.md  ← operational rules, entity types,          │
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
| **Schema** (`AGENTS.md`) | Human + LLM | Co-evolved | Operating rules and structure |

**Why this beats RAG:** RAG re-derives knowledge from raw sources on every query. The wiki
is compiled once and enriched continuously — queries hit the synthesized layer, not the raw
documents. Knowledge compounds; it doesn't disappear into chat history.

---

## The Core Operations

```text
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

**Skill:** `/ingest <path>` or `/ingest --fiche <path>` — see `.agents/skills/ingest/SKILL.md` for full workflow.

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
6. Read raw sources **only if**: wiki page is stale (`now >= stale_after`), claim marked
   `NOT VERIFIED`, or sources conflict and must be resolved.

**Skill:** `/query` pre-loads the relevant pages, or just ask in natural language.
For structured relation queries ("what implements X?", "what connects to Y?"), use `/query --graph <entity>` — it traverses `## Relations` SPO tables directly without reading full page text.

---

### Operation 3: Lint

**Trigger:** `/lint` command, or periodically at the user's request.

Periodic health audit of the wiki. Finds drift, decay, and inconsistency before they
compound. Reports are tiered by severity.

**Checks:**

- [ ] Broken `[[wikilinks]]` (target page missing)
- [ ] Orphan pages (not linked from index or any other page)
- [ ] Stale pages (`now >= stale_after`) → CRITICAL, re-verify before trusting
- [ ] Expiring-soon pages (`stale_after` within 30 days) → WARNING
- [ ] `deprecated` pages missing a link to their replacement → WARNING
- [ ] Contradictions between pages → flag both, mark `PENDING — escalate to human`
- [ ] **OKF: unparseable YAML frontmatter** → CRITICAL
- [ ] **OKF: missing or empty `type`** on any non-reserved page → CRITICAL
- [ ] **OKF: `status` outside `draft | stable | deprecated`**
- [ ] **OKF: bare date** (no UTC offset) in `generated.at`, `verified[].at`, `stale_after`
- [ ] **OKF: `sources` entry that is a string or lacks `resource`**
- [ ] **OKF: `verified[].by` without a `human:` / `process:` / `<producer>/<version>` form**
- [ ] **OKF: reserved `index.md`/`log.md` carrying stray frontmatter** (root `index.md` may hold only `okf_version`)
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
| `/session --open` | Session start / resume | Morning briefing from hot cache + recent log |
| `/session --close` | Session end | Update hot cache, verify consistency, summarize |
| `/query` | Any question / before ingest | Pre-load relevant wiki pages and answer with citations |
| `/query --graph <entity>` | Structured relation query | Traverse Relations SPO tables — find connections to/from an entity |
| `/ingest <path>` | New source added | Full ingest: read → create/update pages → link → log. Books, papers, talks. |
| `/ingest --fiche <path>` | Article/blog post added | Fiche mode: single ~400-word card → link → log. Articles, short reads. |
| `/lint` | Weekly or on demand | `make lint` (mechanical OKF + hygiene), then the judgment checks |
| `/file-back "<title>"` | Insight from conversation | Capture and file reusable knowledge to wiki |
| `/bootstrap <domain>` | New domain / cold start | Create domain hub + seed concept stubs; seed the bundle on cold start |

Skills live in `.agents/skills/` (one directory per skill, each holding `SKILL.md`). Read the
skill file for full workflow details.

---

## Session Startup Protocol

Read in this order at the start of every session:

1. **`wiki/hot.md`** — session hot cache; current focus, open questions, active pages
2. **This file** (`AGENTS.md`) — schema and operating rules (skip if familiar)
3. **`wiki/index.md`** — locate pages relevant to the current task
4. **`wiki/overview.md`** — cluster navigation if working across domains
5. **`wiki/domains/<relevant>.md`** — domain hub page if applicable
6. **Follow `[[wikilinks]]`** — navigate to concept/source pages as needed
7. **`raw/` sources** — only when wiki says `NOT VERIFIED`, a page is stale
   (`now >= stale_after`), or a contradiction must be resolved

**Never** read all raw sources at session start. The wiki exists to prevent this.

**Skill:** `/session --open` — automated startup briefing from hot cache + recent log.

---

## Directory Layout

```text
kortex/
├── AGENTS.md              ← this schema (read first)
├── .agents/
│   └── skills/            ← custom session skills (one dir per skill, each holding SKILL.md)
│       ├── session/SKILL.md    ← /session   open/close a work session
│       ├── query/SKILL.md      ← /query     recall pages (+ --graph relations)
│       ├── ingest/SKILL.md     ← /ingest    raw source → wiki pages
│       ├── lint/SKILL.md       ← /lint      wiki health audit (runs make lint)
│       ├── file-back/SKILL.md  ← /file-back capture conversation insight
│       └── bootstrap/SKILL.md  ← /bootstrap new domain / cold-start seed
├── raw/                   ← immutable source documents (read-only)
│   ├── articles/          ← web articles, blog posts
│   ├── papers/            ← academic papers, research
│   ├── repos/             ← code repositories, READMEs
│   ├── transcripts/       ← talks, interviews, podcasts
│   ├── data/              ← datasets, CSVs, structured data
│   └── assets/            ← images, diagrams, attachments
└── wiki/                  ← LLM-maintained synthesis layer (the OKF bundle)
    ├── index.md           ← OKF reserved: catalog; carries `okf_version: "0.2"`, no other frontmatter
    ├── log.md             ← OKF reserved: activity log, newest date first (OKF §9), no frontmatter
    ├── hot.md             ← session hot cache (~500 words, read first) — `type: cache`
    ├── overview.md        ← cluster navigation hub — `type: overview`
    ├── schema.md          ← entity templates and type definitions — `type: schema`
    ├── kb/                ← builder-generated graph nodes (`make kb`) — `type: kb-entity`
    ├── domains/           ← broad topic hub pages (tier-2)
    ├── concepts/          ← ideas, frameworks, mental models (tier-3)
    ├── sources/           ← book/article/paper summaries (tier-4)
    ├── people/            ← authors, researchers, thinkers
    ├── projects/          ← tools, codebases, initiatives
    ├── organizations/     ← companies, foundations, standards bodies
    ├── decisions/         ← architectural and design choices
    ├── comparisons/       ← side-by-side source/tool analysis
    ├── syntheses/         ← cross-source analyses from queries (tier-5, leaves)
    ├── patterns/          ← recurring failure modes / winning strategies
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
| `organization` | Companies, foundations, standards bodies | `wiki/organizations/` |
| `decision` | Architectural or design choices | `wiki/decisions/` |
| `comparison` | Side-by-side analysis of sources or tools | `wiki/comparisons/` |
| `synthesis` | Cross-source analyses filed from queries (leaves) | `wiki/syntheses/` |
| `pattern` | Recurring failure mode or winning strategy | `wiki/patterns/` |
| `gap` | Open questions, unknowns, deficiencies | `wiki/gaps/` |
| `cache` | Session hot cache | `wiki/hot.md` |
| `overview` | Cluster navigation hub | `wiki/overview.md` |
| `schema` | Entity templates / type definitions | `wiki/schema.md` |

**OKF conformance (§11):** `type` is the only always-required OKF key, and **every
non-reserved `.md` file must carry frontmatter with a non-empty `type`** — including
the meta pages above and builder-generated `wiki/kb/*.md` nodes. Only `index.md` and
`log.md` are OKF-**reserved** (no frontmatter; the root `index.md` carries just
`okf_version: "0.2"`). OKF types are not centrally registered and consumers tolerate
unknown types, so the kortex-local `cache`/`overview`/`schema` types are valid.

---

## Frontmatter Template

Every wiki page (except the reserved `log.md` and `index.md`) must begin with
OKF v0.2-conformant frontmatter:

```yaml
---
# — OKF v0.2 core —
type: <entity type>                       # REQUIRED — the only always-required OKF key
title: <page title>                       # recommended
description: <one-line summary>            # recommended
resource: <raw/filename or URL>           # recommended for source/project; omit for abstract concepts
tags: [<tag1>, <tag2>]                     # recommended
sources:                                   # provenance — a LIST OF MAPPINGS, not strings
  - resource: raw/<filename or URL>        #   REQUIRED within each entry (followable artifact / scope)
    id: <stable-key>                       #   label for per-claim footnote attribution
    title: <short source title>
status: <draft | stable | deprecated>      # OKF enum; absent ⇒ stable
generated: {by: anthropic/<model-id>, at: <ISO-8601-with-offset>}
verified: [{by: human:<id>, at: <ISO-8601-with-offset>}]   # [] ⇒ unverified
stale_after: <ISO-8601-with-offset>        # optional — stale when now >= stale_after; omit if evergreen
# — kortex extensions (OKF preserves unknown keys) —
confidence: <low | medium | high>
cluster: <domain slug this page belongs to>
domain: [<relevant domain slug>]
updated: <YYYY-MM-DD>
---
```

**Status values (OKF v0.2 `status` enum — only these three):**

- `draft` — stub or in-progress, not yet complete
- `stable` — current and accurate (OKF default when `status` is absent)
- `deprecated` — replaced or retired; add a markdown link to the replacement page

**Staleness is derived, never a status.** A page is stale when `now >= stale_after`
(OKF §5). To force a page stale immediately, set `stale_after` to the current instant —
do **not** invent a `status: stale`. Lint flags staleness by comparing `stale_after`
against now.

**Confidence values** (kortex extension — orthogonal to OKF trust tiers):

- `high` — multiple sources agree, well-verified
- `medium` — single source or partially verified
- `low` — uncertain, inferred, or unverified — treat claims with caution

**OKF v0.2 provenance & trust fields:**

- `sources` — a **list of mappings**, each with a required `resource` (followable
  artifact or scope descriptor) plus optional `id`, `title`, `author`. Per-claim
  attribution is a markdown footnote whose label matches a `sources[].id`.
- `generated` — `{by, at}`: who authored the content and when it last meaningfully
  changed. `by` follows the OKF actor convention: `<producer>/<version>` for agents
  (e.g. `anthropic/claude-opus-4-8`), `human:<id>` for people, `process:<id>` for jobs.
- `verified` — list of `{by, at}` sign-offs; `[]` ⇒ **unverified**. A `human:<id>`
  actor earns the **human-reviewed** tier; only non-human actors ⇒ **machine-confirmed**.
  A bare name (`nicolas`) without the `human:` prefix never reaches human-reviewed.
- `stale_after` — absolute **ISO 8601 instant with explicit UTC offset** (e.g.
  `2027-04-08T00:00:00Z`), not a bare date. Fast-moving domains: AI protocols 6 months,
  Kubernetes ecosystem 1 year.
- **All OKF timestamps** (`generated.at`, `verified[].at`, `stale_after`) are ISO 8601
  with an explicit UTC offset — never a bare `YYYY-MM-DD`.

**Inline markers:**

- `NOT VERIFIED` — claim has no traceable source; must be verified before trusting
- `PENDING — escalate to human` — contradiction between sources; human must resolve

---

## Wikilink Convention

Cross-references have **two forms**, and the form depends on where the link sits.
GitHub renders standard markdown but **not** `[[wikilink]]` syntax — so bare `[[type:slug]]`
in prose shows up as dead, unclickable text. Never emit it in human-readable content.

### Form 1 — `## Relations` SPO tables → `[[type:slug]]` (machine-readable)

The `## Relations` table is a machine-readable edge list traversed by `/query --graph`. Its Subject
and Object cells **must** use raw `[[type:slug]]` — `/query --graph` parses this exact syntax.

```text
| Subject          | Predicate | Object              |
|------------------|-----------|---------------------|
| [[concept:x402]] | requires  | [[concept:blockchain]] |
```

Valid types: `[[concept:…]]` `[[source:…]]` `[[person:…]]` `[[project:…]]`
`[[decision:…]]` `[[domain:…]]` `[[comparison:…]]` `[[synthesis:…]]` `[[pattern:…]]` `[[gap:…]]`
`[[organization:…]]`.

### Form 2 — Everywhere else → rendered markdown links (clickable)

All human-readable references — inline prose, `## Related` / `## See Also` bullet lists,
`hot.md`, `wiki/index.md`, `## Open Questions` — use standard markdown links so they render
and click on GitHub:

```text
[x402](../concepts/x402.md)
[Machine Payments Protocol (MPP)](../concepts/machine-payments-protocol-mpp.md)
[Tempo](../projects/tempo.md)
```

Path is relative to the current file (`../concepts/`, `../projects/`, `../sources/`,
`../domains/`; from `wiki/` root pages like `hot.md`, drop the `../`). Pick a readable title,
not the slug. An aliased wikilink `[[concept:mcp|MCP]]` becomes `[MCP](../concepts/mcp.md)`.

**Rule of thumb:** if a human reads the line, it's a markdown link. If `/query --graph` parses the
line (Relations table only), it's `[[type:slug]]`.

Every new page must be linked from its parent domain page and from `wiki/index.md`.

**OKF note:** `[[type:slug]]` lives only in the machine-readable `## Relations` table.
OKF (§6) wants cross-concept links as standard markdown and leaves the page **body
free-form**, so the Relations table is a kortex convention *inside* that free-form body —
it does not break OKF conformance, and every human-facing link already uses OKF-style
markdown (Form 2). A `[[type:slug]]` resolves to an OKF concept ID = bundle path, mapping
`type` through the Entity Types directory column (`[[person:x]]` → `people/x`,
`[[concept:x402]]` → `concepts/x402`), not by the literal type word.

---

## OKF v0.2 Conformance

`wiki/` is a conformant OKF v0.2 bundle. A bundle is conformant (OKF §11) when every
non-reserved `.md` has parseable YAML frontmatter, every frontmatter block has a
non-empty `type`, and reserved files follow their structure. Consumers must tolerate
unknown types/keys and broken links — so kortex extensions are safe.

| OKF v0.2 rule | kortex binding |
|---------------|----------------|
| `type` is the only required key | enforced on every non-reserved page (incl. meta + `kb/`) |
| Reserved files: `index.md`, `log.md` | no frontmatter, except root `index.md` carries only `okf_version: "0.2"` (OKF §8) |
| `status` ∈ `draft \| stable \| deprecated` (default `stable`) | adopted; `active`/`stale`/`superseded` retired |
| Staleness derived: `now >= stale_after` | there is **no** `status: stale`; set `stale_after` to now |
| Timestamps ISO 8601 with UTC offset | `generated.at`, `verified[].at`, `stale_after` |
| Actor convention `<producer>/<version>`, `human:<id>` | `generated.by: anthropic/<model>`; `verified.by: human:<id>` |
| `sources` = list of mappings, each with required `resource` | enforced (not a list of strings) |
| `log.md` newest-first, grouped by date | adopted (overrides Karpathy's append-only) |
| Links are markdown; brokenness tolerated | Form 2 markdown links; `[[type:slug]]` confined to Relations tables |

**Trust tiers** (OKF-derived, advisory): no `verified` ⇒ *unverified*; only non-human
actors ⇒ *machine-confirmed*; a `human:<id>` actor ⇒ *human-reviewed*.

**Follow-up (not schema):** (a) — done — `scripts/build_knowledge_base.py` emits a `type` on each
generated `wiki/kb/*.md` node and on `wiki/knowledge-base.md` (`kb-entity` / `kb-index`), and
`scripts/lint_wiki.py` checks only `type` on those generated files. (b) — open — anchor the
builder's `read_frontmatter_title` regex (`build_knowledge_base.py:69`) to a top-level key (line
start, no leading whitespace) so a nested `sources[].title` cannot shadow the page title.

---

## Seven Hard Rules

1. **Update before ending.** Every session that touches knowledge must update relevant wiki
   pages before stopping.
2. **Log every edit.** Every create/update/delete to any wiki page gets a `wiki/log.md`
   entry with date, pages affected, and source referenced. Also add the affected pages to
   the `## By Date` section of `wiki/index.md` under today's date — use the log operation
   tag as suffix (e.g. `[INGEST]`). Batch entries from the same operation on one line.
   Prune entries older than 90 days to a single summary line.
3. **Frontmatter stays current.** Set `updated:` on every touched page. Force an outdated
   page stale immediately by setting `stale_after` to the current instant (OKF staleness
   is derived, not a status) — stale is worse than missing.
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
2. **Stale is worse than missing.** An outdated page actively misleads. Set `stale_after` to now immediately.
3. **One source of truth per fact.** One canonical page; all others wikilink to it. No duplication.
4. **Every fact has provenance.** No traceable source → mark `NOT VERIFIED`.
5. **Contradictions are features.** Flagging a contradiction is more valuable than silently
   resolving it incorrectly.

---

## Log Format

`wiki/log.md` is OKF-reserved (OKF §9): a `# Log` title, then `## YYYY-MM-DD` date
headings **newest first**, each holding bulleted entries. **No frontmatter.** The leading
bold op tag is the attribution convention. This structure overrides the per-entry-heading,
append-at-bottom phrasing from the LLM Wiki article.

```text
# Log

## 2026-05-04

- **[INGEST]** Added "How to Take Smart Notes" by Ahrens — pages: sources/how-to-take-smart-notes.md, concepts/zettelkasten.md, people/niklas-luhmann.md; sources: raw/ahrens-smart-notes.pdf
- **!failure** Paywalled article ingest blocked — pages: none; sources: raw/articles/blocked-article.pdf; note: PDF corrupted, re-download
```

Op tags: `[INIT]` `[INGEST]` `[QUERY]` `[LINT]` `[FILE]` `[UPDATE]` `[BOOTSTRAP]`;
`!failure` for dead-ends. Prune entries older than 90 days to a single summary line under
their date heading (Hard Rule 2).

---

## Index Format

`wiki/index.md` is organized by entity type. Each entry is one line:

```text
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
