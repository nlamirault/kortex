# kortex

Personal knowledge base powered by the [LLM Wiki protocol](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Structure

```
kortex/
├── CLAUDE.md        ← operational schema (read first)
├── raw/             ← immutable source documents
└── wiki/            ← LLM-maintained synthesis
    ├── index.md     ← content catalog
    ├── log.md       ← activity log
    ├── schema.md    ← page templates
    └── <domain>/    ← knowledge domain directories
```

## Workflow

| Operation | Trigger |
|-----------|---------|
| **Ingest** | Drop file in `raw/`, say "Ingest `raw/<file>`" |
| **Query** | Ask any question — relevant wiki pages are consulted |
| **Lint** | Say `/lint` — checks for broken links, stale pages, orphans |
| **File back** | Insights from conversation get filed as new wiki pages |

## Getting Started

1. Read `CLAUDE.md` — the operational protocol
2. Add a source to `raw/`
3. Say: "Ingest `raw/<filename>`"
