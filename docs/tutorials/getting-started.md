# Getting Started with Kortex

> **Learning-oriented** — by the end of this tutorial you will have added your first
> source to Kortex and queried the wiki for an answer.

## What You'll Learn

- What the three layers of Kortex are
- How to drop a raw source and ingest it
- How to ask the wiki a question

## Prerequisites

- Kortex cloned locally
- Claude Code running in the project root

## Step 1 — Understand the Layers

Kortex has three layers:

1. **Raw** (`raw/`) — immutable source documents you drop in.
2. **Wiki** (`wiki/`) — the LLM-maintained synthesis layer.
3. **Schema** (`CLAUDE.md`) — the operating rules.

You add to `raw/`. The LLM maintains `wiki/`. You never edit `raw/` after the fact.

## Step 2 — Add a Source

Drop a file into the matching `raw/` subfolder — for example an article into
`raw/articles/`.

<!-- TODO: replace with a real example file the reader can use -->

## Step 3 — Ingest It

Run the ingest skill:

```
/ingest --fiche raw/articles/<your-file>
```

This reads the source, creates or updates wiki pages, links them, and logs the operation.

## Step 4 — Ask a Question

Just ask in natural language:

```
What did <source> say about <topic>?
```

The LLM reads the synthesized wiki pages — not the raw source — and answers with citations.

## What's Next

- [Ingest a New Source](../how-to/example-task.md) — the task-focused version
- [Three-Layer Architecture](../explanation/architecture.md) — why it works this way
