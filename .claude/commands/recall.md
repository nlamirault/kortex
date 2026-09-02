# Skill: /recall

Pre-load relevant wiki context before answering a question or starting a task.
Run this before any non-trivial query to reduce hallucination and improve citation quality.

## When to Use

- Before answering a research question
- Before ingesting a new source (check what already exists on the topic)
- When the user asks about a topic that may already be in the wiki

## Workflow

1. Read `wiki/hot.md` — check Current Focus and Active Pages.
2. Read `wiki/index.md` — scan all entries for relevance to the question/topic.
3. Read `wiki/overview.md` — identify which cluster(s) are relevant.
4. Read the relevant domain hub page(s) in `wiki/domains/`.
5. Follow `[[wikilinks]]` to concept and source pages that are directly relevant.
6. Report: "Loaded N pages for context: [list]. Ready."

## Output Format

```
/recall loaded:
- wiki/domains/<domain>.md
- wiki/concepts/<concept>.md
- wiki/sources/<source>.md
Ready to answer.
```

## Constraints

- Read at most 8–10 pages. Stop when context is sufficient.
- Do NOT read raw sources unless a wiki page is marked `status: stale` or `NOT VERIFIED`.
- Do NOT modify any files during recall.

## Purpose

Query-side context loader (Operation 2). Reads the synthesized wiki layer instead
of raw sources — the paper's core efficiency claim: hit pre-compiled knowledge, not
ground truth, on every query. Provenance format mandated by
[[decision:adopt-wikiskill-evolution-loop]].
