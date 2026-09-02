# How to Ingest a New Source

> **Task-oriented** — you already know Kortex; this shows the steps to bring a new source
> into the wiki.

## Goal

Add a source document to `raw/` and synthesize it into the wiki.

## Choose a Mode

| Mode | Command | Use for |
|------|---------|---------|
| Full | `/ingest <path>` | Books, papers, talks (>20 min read) → 10–15 pages |
| Fiche | `/ingest --fiche <path>` | Articles, blog posts (<20 min read) → 1 fiche card |

## Steps

1. **Place the source** in the correct `raw/` subfolder (`articles/`, `papers/`,
   `transcripts/`, …).
2. **Run the ingest skill** with the chosen mode:
   ```
   /ingest --fiche raw/articles/<file>
   ```
3. **Verify** the run created or updated pages, added `[[wikilinks]]`, updated
   `wiki/index.md`, and appended an `[INGEST]` entry to `wiki/log.md`.

## Verify

```
git status wiki/
```

New or modified pages under `wiki/` plus a fresh `log.md` entry confirm success.

## Related

- [Getting Started](../tutorials/getting-started.md)
- [API & Schema Reference](../reference/api-reference.md)
