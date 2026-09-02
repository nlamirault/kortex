# API & Schema Reference

> **Reference** — complete, factual specification of Kortex entities, frontmatter, and
> skills. Consult while working. The authoritative source is `CLAUDE.md`.

## Entity Types

| Type | Purpose | Directory |
|------|---------|-----------|
| `domain` | Broad topic hub pages | `wiki/domains/` |
| `concept` | Ideas, frameworks, mental models | `wiki/concepts/` |
| `source` | Books, papers, articles, talks | `wiki/sources/` |
| `person` | Authors, researchers, thinkers | `wiki/people/` |
| `project` | Tools, codebases, initiatives | `wiki/projects/` |
| `decision` | Architectural or design choices | `wiki/decisions/` |
| `comparison` | Side-by-side analysis | `wiki/comparisons/` |
| `synthesis` | Cross-source analyses (leaves) | `wiki/syntheses/` |
| `pattern` | Recurring failure/winning strategy | `wiki/patterns/` |
| `gap` | Open questions, deficiencies | `wiki/gaps/` |

## Frontmatter Fields

| Field | Values | Notes |
|-------|--------|-------|
| `title` | string | Page title |
| `type` | entity type | See table above |
| `status` | `draft` \| `active` \| `stale` \| `superseded` | `stale` = do not trust unverified |
| `confidence` | `low` \| `medium` \| `high` | Source agreement / verification level |
| `cluster` | domain slug | Owning domain |
| `domain` | `[slug]` | Relevant domains |
| `sources` | `[path or URL]` | Raw provenance |
| `updated` | `YYYY-MM-DD` | Set on every touch |
| `tags` | `[tag]` | Free tags |
| `generated` | `{by, at}` | Authoring model + date |
| `verified` | `[{by, at}]` | Human/agent sign-offs; `[]` = unverified |
| `stale_after` | `YYYY-MM-DD` | Optional expiry; omit for evergreen |

## Skills

| Skill | Trigger | What it does |
|-------|---------|-------------|
| `/today` | Session start | Morning briefing from hot cache + log |
| `/recall` | Before a query | Pre-load relevant wiki pages |
| `/graph <entity>` | Relation query | Traverse Relations SPO tables |
| `/ingest <path>` | New source | Full ingest → 10–15 pages |
| `/ingest --fiche <path>` | Article | Fiche mode → 1 card |
| `/lint` | Weekly / on demand | Health audit |
| `/file-back "<title>"` | Insight from chat | File reusable knowledge |
| `/evolve` | Failures accrued | Wiki → procedure loop |
| `/bootstrap <domain>` | New domain | Create hub + seed concepts |
| `/close` | Session end | Update hot cache, summarize |

## Wikilink Convention

Cross-reference with `[[type:slug]]`, rendered as a relative markdown link:

```
[[concept:zettelkasten]]  →  [Zettelkasten](../concepts/zettelkasten.md)
```

## Inline Markers

- `NOT VERIFIED` — claim has no traceable source.
- `PENDING — escalate to human` — sources conflict; human must resolve.
