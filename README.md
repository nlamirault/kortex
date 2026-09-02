# kortex

Personal knowledge base powered by the [LLM Wiki protocol](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Wiki pages use [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) v0.2 for structured frontmatter, including provenance (`generated`), human sign-off (`verified`), and freshness expiry (`stale_after`) fields.

## Structure

```
kortex/
├── CLAUDE.md        ← operational schema (read first)
├── raw/             ← immutable source documents
├── wiki/            ← LLM-maintained synthesis
│   ├── index.md     ← content catalog
│   ├── log.md       ← activity log
│   ├── schema.md    ← page templates
│   └── <domain>/    ← knowledge domain directories
└── docs/            ← project documentation (Diátaxis)
    ├── tutorials/   ← learning-oriented
    ├── how-to/      ← task-oriented
    ├── reference/   ← information-oriented
    └── explanation/ ← understanding-oriented
```

## Workflow

| Operation | Trigger |
|-----------|---------|
| **Ingest** | Drop file in `raw/`, say "Ingest `raw/<file>`" |
| **Query** | Ask any question — relevant wiki pages are consulted |
| **Lint** | Say `/lint` — checks for broken links, stale pages, orphans |
| **File back** | Insights from conversation get filed as new wiki pages |

## Documentation

Project documentation lives in [`docs/`](docs/) and follows the
[Diátaxis framework](https://diataxis.fr/), which organizes docs by user need rather
than by file layout:

| Type | Purpose | When to read |
|------|---------|--------------|
| [Tutorials](docs/tutorials/) | Learning-oriented, hands-on lessons | New to Kortex — start here |
| [How-to Guides](docs/how-to/) | Task-oriented, goal-driven steps | You know the basics, need a task done |
| [Reference](docs/reference/) | Information-oriented specifications | Look up entity types, frontmatter, skills |
| [Explanation](docs/explanation/) | Understanding-oriented background | Understand the architecture and design choices |

Start at [`docs/README.md`](docs/README.md) for the navigation index.
Architectural decisions are recorded as ADRs under [`docs/decisions/adr/`](docs/decisions/adr/).

## Getting Started

1. Read `CLAUDE.md` — the operational protocol
2. Add a source to `raw/`
3. Say: "Ingest `raw/<filename>`"
