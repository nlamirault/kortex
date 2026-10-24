---
type: project
title: agentic-seo
description: MIT-licensed CLI that audits documentation/websites for Agentic Engine Optimization (AEO) — discoverability and parseability by AI coding agents — scored across 10 checks.
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://github.com/addyosmani/agentic-seo
    id: agentic-seo-repo-2026
    title: "agentic-seo (GitHub repository)"
generated: {by: anthropic/claude-sonnet-5, at: 2026-10-24T00:00:00Z}
verified: []
stale_after: 2027-04-24T00:00:00Z
updated: 2026-10-24
tags: [agentic-seo, aeo, audit-tool, llms-txt, agents-md, cli]
---

# agentic-seo

**Kind:** tool (npm CLI) · **Lifecycle:** active
**URL:** https://github.com/addyosmani/agentic-seo

## What It Does

`agentic-seo` is Addy Osmani's MIT-licensed, API-key-free CLI that audits a documentation site
for [Agentic Engine Optimization](../sources/addyosmani-agentic-engine-optimization-2026.md) —
whether content is discoverable, parseable, and token-efficient for AI coding agents such as
Claude Code, Cursor, Cline, and Aider. It auto-detects the site's framework (Next.js,
Docusaurus, Astro, Hugo, Jekyll, VitePress, MkDocs, Sphinx, and others), parses HTML with
Cheerio and Markdown with Remark, and counts real tokens per page with `gpt-tokenizer` to
simulate what an agent would see on fetch. It runs 10 checks across 5 weighted categories
(discovery, content structure, token economics, capability signaling, UX bridge) and returns a
0–100 score with an A–F grade. An `init` subcommand scaffolds the missing files (`llms.txt`,
`AGENTS.md`, `skill.md`, `agent-permissions.json`); a `--json --threshold N` mode is built for
CI gating.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:agentic-seo]] | implements | [[source:addyosmani-agentic-engine-optimization-2026]] |
| [[project:agentic-seo]] | integrates-with | [[concept:agents-md]] |

## Relevance to Kortex

A concrete, runnable implementation of the AEO checklist — useful as a lint/CI gate if kortex's
own [website](../domains/ai-protocols.md) publishes agent-facing docs (`llms.txt`, `AGENTS.md`
presence, token budgets per page).

## Related

- [Agentic Engine Optimization (AEO) — Addy Osmani](../sources/addyosmani-agentic-engine-optimization-2026.md) — the companion essay this tool operationalizes.
- [AGENTS.md](../concepts/agents-md.md) — one of the files the `agents-md` check looks for and `init` can scaffold.
- [AI Protocols](../domains/ai-protocols.md) — domain cluster.
