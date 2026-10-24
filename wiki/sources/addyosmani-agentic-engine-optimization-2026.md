---
type: source
title: Agentic Engine Optimization (AEO) — Addy Osmani
description: Developer docs need structuring for AI coding agents, not just humans — a discipline Osmani calls Agentic Engine Optimization, the SEO analogue for agent-readable content.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://addyosmani.com/blog/agentic-engine-optimization/
    id: osmani-aeo-2026
    title: "Agentic Engine Optimization (AEO)"
generated: {by: anthropic/claude-sonnet-5, at: 2026-10-24T00:00:00Z}
verified: []
stale_after: 2027-04-24T00:00:00Z
updated: 2026-10-24
tags: [aeo, agentic-seo, llms-txt, agents-md, skill-md, token-economics, documentation]
---

# Agentic Engine Optimization (AEO)

**Auteur :** Addy Osmani · **Publié :** 2026-04-11 · **Lien :** https://addyosmani.com/blog/agentic-engine-optimization/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~15 min

## En Bref

AI coding agents (Claude Code, Cursor, Aider, …) consume documentation in one or two HTTP
fetches, invisible to client-side analytics, with practical context limits of ~100K–200K
tokens — so docs built for human scanning (long pages, nav chrome, deep click paths) truncate,
hallucinate, or fail silently. Osmani names this discipline **Agentic Engine Optimization
(AEO)**, structuring docs for agents the way SEO structures pages for crawlers, and proposes a
six-layer stack plus an audit tool to measure it.[^osmani]

## Points Clés

- **Token count is a first-class doc metric:** target <15K tokens for quick-starts, <25K for
  API reference pages, <20K for conceptual guides; chunk large references by resource/endpoint.[^osmani]
- **Six-layer AEO stack:** access control (`robots.txt`, emerging `agent-permissions.json`) →
  discovery (`llms.txt` as a sitemap for agents, kept under 5K tokens) → capability signaling
  (`skill.md` describing a service's inputs/constraints) → content formatting (clean Markdown,
  `.md` URL suffix, front-loaded outcomes) → token surfacing (counts in `llms.txt`/meta tags) →
  a "Copy for AI" button.[^osmani]
- **Agents fingerprint distinctly:** a cited research paper found per-agent HTTP signatures —
  Claude Code uses `axios/1.8.4`, Cline/Junie use `curl/8.4.0`, Cursor uses `got`, Windsurf uses
  `colly` — enabling AI-traffic monitoring separate from human analytics.[^osmani]
- **[AGENTS.md](../concepts/agents-md.md) is framed as the emerging default** context file for
  coding agents, alongside `llms.txt` and `skill.md`, with Cisco DevNet cited as an adopter.[^osmani]
- **Companion audit tool:** [agentic-seo](../projects/agentic-seo.md), described as "Lighthouse,
  but for agent-readiness," checks llms.txt, robots.txt blocking, token budgets, and Markdown
  availability.[^osmani]

## Citation Notable

> "I think this means token count is now a first-class documentation metric." — Addy Osmani[^osmani]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:addyosmani-agentic-engine-optimization-2026]] | extends | [[concept:agents-md]] |
| [[source:addyosmani-agentic-engine-optimization-2026]] | enables | [[project:agentic-seo]] |
| [[source:addyosmani-agentic-engine-optimization-2026]] | contrasts-with | [[concept:model-context-protocol-mcp]] |

## Liens Wiki

- [AGENTS.md](../concepts/agents-md.md) — named as one of the three emerging agent-context formats (with `llms.txt`, `skill.md`).
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — named as the alternative, direct-integration path to doc-based agent access.
- [agentic-seo](../projects/agentic-seo.md) — Osmani's own audit tool implementing this post's checklist.
- [AI Protocols](../domains/ai-protocols.md) — domain cluster.

[^osmani]: Addy Osmani, "Agentic Engine Optimization (AEO)", addyosmani.com, 2026-04-11, consulted 2026-10-24. Author discloses working at Google Cloud AI; post states it is not official Google Search policy.
