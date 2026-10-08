# API & Schema Reference

> **Reference** — complete, factual specification of Kortex entities, frontmatter, and
> skills. Consult while working. The authoritative source is `AGENTS.md` (OKF v0.2).

## Entity Types

| Type | Purpose | Directory |
|------|---------|-----------|
| `domain` | Broad topic hub pages | `wiki/domains/` |
| `concept` | Ideas, frameworks, mental models | `wiki/concepts/` |
| `source` | Books, papers, articles, talks | `wiki/sources/` |
| `person` | Authors, researchers, thinkers | `wiki/people/` |
| `project` | Tools, codebases, initiatives | `wiki/projects/` |
| `organization` | Companies, foundations, standards bodies | `wiki/organizations/` |
| `decision` | Architectural or design choices | `wiki/decisions/` |
| `comparison` | Side-by-side analysis | `wiki/comparisons/` |
| `synthesis` | Cross-source analyses (leaves) | `wiki/syntheses/` |
| `pattern` | Recurring failure/winning strategy | `wiki/patterns/` |
| `gap` | Open questions, deficiencies | `wiki/gaps/` |

## Frontmatter Fields

| Field | Values | Notes |
|-------|--------|-------|
| `type` | entity type | **REQUIRED** — OKF's only always-required key |
| `title` | string | Recommended — page title |
| `description` | string | Recommended — one-line summary |
| `resource` | path or URL | Recommended for `source`/`project`; omit for abstract concepts |
| `tags` | `[tag]` | Recommended |
| `sources` | list of `{resource, id?, title?}` | Each entry **must** have `resource` (not a bare string) |
| `status` | `draft` \| `stable` \| `deprecated` | OKF enum; absent ⇒ `stable`. No `stale`/`superseded` |
| `generated` | `{by, at}` | `by`: `<producer>/<version>` (e.g. `anthropic/claude-opus-4-8`); `at`: ISO 8601 + UTC offset |
| `verified` | `[{by, at}]` | `by`: `human:<id>` ⇒ human-reviewed; `[]` = unverified; `at`: ISO 8601 + offset |
| `stale_after` | ISO 8601 + UTC offset | Page is stale when `now >= stale_after`; omit for evergreen |
| `confidence` | `low` \| `medium` \| `high` | kortex ext — source agreement / verification level |
| `cluster` | domain slug | kortex ext — owning domain |
| `domain` | `[slug]` | kortex ext — relevant domains |
| `updated` | `YYYY-MM-DD` | kortex ext — set on every touch |

## Skills

| Skill | Trigger | What it does |
|-------|---------|-------------|
| `/session --open` | Session start | Morning briefing from hot cache + log |
| `/session --close` | Session end | Update hot cache, verify, summarize |
| `/query` | Any question | Pre-load relevant wiki pages, answer with citations |
| `/query --graph <entity>` | Relation query | Traverse Relations SPO tables |
| `/ingest <path>` | New source | Full ingest → 10–15 pages |
| `/ingest --fiche <path>` | Article | Fiche mode → 1 card |
| `/lint` | Weekly / on demand | `make lint` + judgment checks |
| `/file-back "<title>"` | Insight from chat | File reusable knowledge |
| `/bootstrap <domain>` | New domain | Create hub + seed concepts; cold-start seed |

## Wikilink Convention

Cross-reference with `[[type:slug]]`, rendered as a relative markdown link:

```text
[[concept:zettelkasten]]  →  [Zettelkasten](../concepts/zettelkasten.md)
```

## Inline Markers

- `NOT VERIFIED` — claim has no traceable source.
- `PENDING — escalate to human` — sources conflict; human must resolve.
