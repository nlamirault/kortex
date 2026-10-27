---
type: source
title: AgentReady — Open Specification for Agent-Usable Products
description: Open, vendor-neutral find/read/act checklist for making a product usable by AI agents, backed by measured-agent-behavior studies from Ora.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://www.agentready.org
    id: agentready-2026
    title: "AgentReady Standard"
generated: {by: anthropic/claude-sonnet-5, at: 2026-10-27T00:00:00Z}
verified: []
stale_after: 2027-04-27T00:00:00Z
updated: 2026-10-27
tags: [agentready, aeo, mcp, llms-txt, agents-md, agent-discoverability, checklist, ora]
---

# AgentReady — Open Specification for Agent-Usable Products

**Auteur :** Ora (ora.ai), developed in the open on GitHub (`agentready-org/standard`, MIT) ·
**Publié :** v1.0.0 2026-04 (announced 2026-03-20), restructured to find/read/act as v1.0 2026-08,
v2.0 2026-10 ·
**Lien :** https://www.agentready.org
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~15 min

## En Bref

AgentReady is an open, vendor-neutral specification of what a product should do to be found,
read, and used by AI agents — "agents are a new class of user." It promotes no single protocol;
its MUST/SHOULD/MAY practices are strength-ranked from measured agent behavior (grounded in
250,000 real agent runs per the site) and revised as that behavior changes.[^agentready]

## Points Clés

- **Three-stage model — find, read, act**, each practice tagged with a stable `AR-*` identifier
  and a strength: *Find* — bot protection/robots.txt (AR-FIND-01, MUST), first-party docs and
  sitemap.xml (AR-FIND-02/03, SHOULD), an AI Catalog (AR-FIND-04, MAY). *Read* — fetchable
  without JavaScript and real HTTP status codes incl. 404 and 429+`Retry-After` [RFC 6585]
  (AR-READ-01/02, MUST), homepage-in-raw-HTML, answering docs pages, fenced/tagged code,
  `.well-known/*`, `llms.txt`, JSON-LD, pricing on a first-party page (AR-READ-03–08/11, all
  SHOULD). *Act*, only if the product should let an agent finish a task — an MCP server or a CLI
  (AR-ACT-10, MUST, added in v2.0); agent-usable auth (OAuth 2.0 with discoverable metadata per
  RFC 8414/RFC 9728 for user-delegated access), a public OpenAPI contract, a standalone MCP
  server, SDKs/CLI, WebMCP (AR-ACT-01/02/03/06/07, SHOULD); MCP Apps, letting agents pay, and an
  NLWeb `/ask` endpoint (AR-ACT-05/08/09, MAY).[^agentready]
- **Two changes broke agents** in Ora's studies: hiding the answer behind JavaScript, and
  blocking access.[^agentready]
- **Discovery files work best explicitly linked, not guessed:** across a traced sample, AGENTS.md
  was reached via an explicit link 100% of the time (38 fetches), `openapi.json` 97% (122),
  `.well-known/*` 93% (383), and `llms.txt` 86% (416).[^agentready]
- **Read access is close to solved, act access is not:** in the April 2026 state of agent
  readiness report (~50,000 sites), 88% shipped a robots.txt and 80% stayed reachable to every
  major AI crawler, but only 3% shipped a spec-grade MCP server and about 1% passed
  OAuth-metadata-and-PKCE checks. "Agents can read. They cannot act."[^agentready]
- **Measured downstream impact (Ora's own traced-run research):** across 1,056 business sites,
  agents unable to read a site answered anyway from web search and third-party pages, and those
  answers were 3.7× as likely to contain none of the facts asked for, while agent-ready
  businesses were recommended 1.9× as often; separately, 82% of answers traced back to a page the
  agent fetched directly, and that page was a docs page 47% of the time, more than any other page
  type.[^agentready]
- **Payments and task completion work when offered:** agents completed 92.3% of test checkouts
  correctly over Stripe Link, 18 of 26 agents scoring at least 90% (Ora research, test mode,
  October 2026).[^agentready]

## Citation Notable

> "Agents are a new class of user."[^agentready]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-agentready-standard-2026]] | argues-that | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-agentready-standard-2026]] | argues-that | [[concept:agents-md]] |

## Liens Wiki

- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — the `Act` stage makes an MCP server (or a CLI) a MUST once a product should complete a task, as of v2.0 (AR-ACT-10).
- [AGENTS.md](../concepts/agents-md.md) — cited directly in the discovery-file linkage data: of 38 traced AGENTS.md fetches, 100% arrived via an explicit link, the highest rate of any discovery file measured.
- [Agentic Engine Optimization (AEO) — Addy Osmani](../sources/addyosmani-agentic-engine-optimization-2026.md) — same underlying concern (structuring a product for AI agents) but AgentReady never names Osmani or AEO; the only textual echo is Ora's own cited study, "AX is the New AEO" — a parallel, not a stated extension. Treat any link between the two as editorial, not sourced.
- [agentic-seo](../projects/agentic-seo.md) — a comparable companion scanner in spirit; AgentReady names its own Ora ranker plus is-agentic.com, Mintlify Agent Score, and Netlify AXIS as scanners, not agentic-seo itself.
- [AI Protocols](../domains/ai-protocols.md) — domain cluster.

[^agentready]: agentready.org, "AgentReady — open specification for agent-usable products", consulted 2026-10-27 (page source fetched and read directly, not via summary). Publisher Ora (ora.ai); spec developed at `agentready-org/standard` (MIT); lists Vercel, Stripe, Auth0, Mintlify, Tavily by Nebius, Google, Elementor, Netlify as collaborators. Most figures above are Ora's own cited traced-run research (37,927 agent journeys / 1,056 sites for the omission-rate finding; a separate traced-run dataset for the 82%/47% answer-provenance finding); only the 99%-dead-end/2.1×-blocked/23%-more-turns finding is explicitly attributed on the page to "AX is the New AEO" (Ora research, arXiv:2609.34951, September 2026) — not independently verified here.
