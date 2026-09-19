# Kortex Wiki — Activity Log

Append-only chronological record of all wiki operations.
Format: `## [YYYY-MM-DD] [OP] | summary`

---

## [2026-09-19] [UPDATE] | Every rendered page now shows its title; merged duplicate AWS Bedrock AgentCore pages
  └─ pages: website/src/layouts/DocsLayout.astro, website/prepare_content.py, wiki/concepts/aws-bedrock-agentcore.md, wiki/concepts/aws-bedrock-agent-core.md (deleted), wiki/index.md, wiki/domains/ai.md, wiki/kb/*
  └─ sources: none
  └─ note: DocsLayout renders frontmatter title as the page <h1>; prepare_content drops title-repeat headings + demotes competing body H1s. aws-bedrock-agent-core (draft stub) merged into aws-bedrock-agentcore (canonical, official spelling).

## [2026-09-19] [UPDATE] | Fixed 5 broken Notion-export links in AI/Protocols page (mangled `%20<hash>.md)` fragments → proper markdown links)
  └─ pages: wiki/concepts/ai-protocols.md
  └─ sources: none

## [2026-09-19] [LINT] | Wiki-wide broken-link scan; fixed 3 bare `[[type:slug]]` prose wikilinks (dead on GitHub render) → markdown links
  └─ pages: wiki/gaps/evolve-loop-coverage.md, wiki/decisions/adopt-wikiskill-evolution-loop.md, wiki/skill-impact.md
  └─ sources: none
  └─ note: schema.md/log.md/index.md `[[..:slug]]` are intentional template examples, left as-is; no other broken relative links found

## [2026-09-19] [UPDATE] | Website build now renders `## Relations` `[[type:slug]]` as clickable pretty-URL links (were dead text on the site, e.g. AP2 page)
  └─ pages: website/prepare_content.py, wiki/concepts/agent-payments-protocol-ap2.md (title whitespace)
  └─ sources: none
  └─ note: rewrite_wikilinks() two-pass slug→title index; only links existing pages, leaves unknown/dangling + schema.md syntax examples raw; source wiki/ [[..]] untouched so /graph still parses

## [2026-09-02] [UPDATE] | Fixed non-rendering `[[type:slug]]` links in agentic-payments cluster; clarified Wikilink Convention
  └─ pages: wiki/concepts/{x402,machine-payments-protocol-mpp,agent-payments-protocol-ap2,universal-commerce-protocol-ucp}.md, wiki/projects/tempo.md, wiki/sources/{mpp-specs,x402-org-2026}.md, wiki/hot.md, CLAUDE.md, .claude/skills/{ingest,lint}.md
  └─ sources: none
  └─ note: Bare `[[type:slug]]` does not render on GitHub. Converted all prose/`## Related`/`## See Also` wikilinks to markdown links `[Title](../dir/slug.md)`; kept `## Relations` SPO tables as `[[type:slug]]` (machine-read by /graph). Split Wikilink Convention into two explicit forms; added ingest step + lint check to prevent recurrence.

## [2026-09-02] [INGEST] | Added Machine Payments Protocol (MPP) by Tempo Labs & Stripe
  └─ pages: wiki/concepts/machine-payments-protocol-mpp.md (new), wiki/projects/tempo.md (new), wiki/sources/mpp-specs.md (new), wiki/concepts/agent-payments-protocol-ap2.md (+Relations), wiki/concepts/universal-commerce-protocol-ucp.md (+Related), wiki/concepts/ai-protocols.md, wiki/domains/ai.md, wiki/domains/blockchain.md, wiki/index.md, wiki/hot.md
  └─ sources: https://paymentauth.org/, https://github.com/tempoxyz/mpp-specs
  └─ note: MPP revives HTTP 402 for machine-to-machine payments; Tempo = Stripe/Paradigm L1 settlement. Draft 00–01, stale_after 6mo. Related to x402 (both HTTP 402) — cross-linked.

## [2026-09-02] [INGEST] | Added "x402.org — Internet-Native Payment Protocol" by x402 Foundation
  └─ pages: wiki/concepts/x402.md (new), wiki/sources/x402-org-2026.md (new), wiki/domains/ai.md, wiki/domains/blockchain.md, wiki/concepts/agent-payments-protocol-ap2.md, wiki/concepts/universal-commerce-protocol-ucp.md, wiki/index.md, wiki/hot.md
  └─ sources: https://x402.org/
  └─ note: HTTP 402 + stablecoin settlement protocol; cross-linked to AP2 (agent-layer) and UCP (commerce-layer) as complementary agentic-payment standards. Coinbase origin + facilitator role marked NOT VERIFIED (not on landing page).

## [2026-09-01] [UPDATE] | Adopt WikiSkill evolution loop (ADR-0001) — close the wiki→procedure feedback arc
  └─ pages: wiki/decisions/adopt-wikiskill-evolution-loop.md (new), wiki/skill-impact.md (new), wiki/gaps/evolve-loop-coverage.md (new), wiki/patterns/ (new dir), .claude/skills/evolve.md (new), .claude/skills/{today,close,recall,ingest,lint,graph,bootstrap,file-back}.md (+ ## Purpose), CLAUDE.md, wiki/schema.md, wiki/index.md
  └─ sources: https://arxiv.org/html/2608.27454v1 (WikiSkill paper)
  └─ note: adds `pattern` entity type, /evolve operation, skill-impact ledger, ## Purpose provenance on all skills, lint+query acceptance gate

## [2026-08-28] [UPDATE] | Add /graph skill — SPO Relations table traversal for graph queries
  └─ pages: .claude/skills/graph.md (new), CLAUDE.md
  └─ sources: none (structural improvement — unlocks Relations tables added in Task 4)

## [2026-08-27] [UPDATE] | Add /ingest --fiche mode for articles and blog posts
  └─ pages: wiki/schema.md, .claude/skills/ingest.md, CLAUDE.md
  └─ sources: none (structural improvement — fiches-veille fiche card pattern)

## [2026-08-27] [UPDATE] | /close now mirrors queue count to hot.md Pending Ingests block
  └─ pages: .claude/skills/close.md
  └─ sources: none (closes queue-visibility loop: /today reads live, /close writes snapshot)

## [2026-08-27] [UPDATE] | Add ## Relations SPO triples to entity page templates and ingest workflow
  └─ pages: wiki/schema.md, .claude/skills/ingest.md, .claude/skills/lint.md
  └─ sources: none (structural improvement — fiches-veille SPO triple pattern on entity pages)

## [2026-08-27] [UPDATE] | Surface raw/queue.md in /today briefing
  └─ pages: .claude/skills/today.md
  └─ sources: none (structural improvement — complete ingest queue visibility at session start)

## [2026-08-27] [UPDATE] | Add stale_after expiry checks to /lint skill and CLAUDE.md lint list
  └─ pages: .claude/skills/lint.md, CLAUDE.md
  └─ sources: none (structural improvement — OKF v0.2 stale_after enforcement)

## [2026-08-27] [UPDATE] | Add chronological index to wiki/index.md; update Hard Rule 2; add Pending Ingests to hot.md
  └─ pages: wiki/index.md, CLAUDE.md, wiki/hot.md
  └─ sources: none (structural improvement — fiches-veille temporal org inspiration)

## [2026-08-17] [IMPROVE] | Reclassify tools, add sources/people, cross-link
  └─ pages: wiki/projects/{33 pages}, wiki/sources/{8 pages}, wiki/people/{3 pages}
  └─ note: tools moved from concepts/ to projects/; domain hubs rebuilt with separate sections

## [2026-08-17] [INGEST] | Migrated Notion KB export into wiki schema (domains + concepts)
  └─ pages: wiki/domains/{11 hubs}, wiki/concepts/{94 pages}, wiki/syntheses/ai-prompts.md
  └─ sources: /Users/nicolas.lamirault/TMP/KB (109 Notion export files, 95 migrated)
  └─ note: Notion types → kortex types: Explanation/Reference→concept, How-to→synthesis; 14 stubs skipped

## [2026-05-04] [INIT] | Bootstrapped Kortex wiki structure
  └─ pages: wiki/index.md, wiki/log.md, wiki/schema.md
  └─ sources: CLAUDE.md (schema)

## [2026-05-04] [UPDATE] | Expanded schema with Three-Layer Architecture, operations, skills, session protocol, anti-corruption rules
  └─ pages: CLAUDE.md, wiki/log.md, wiki/index.md
  └─ sources: karpathy/llm-wiki.md, Alirezajalilii/WIKI_PROTOCOL_V1.md, medium article

## [2026-05-04] [UPDATE] | Added hot cache, overview, comparisons, raw subdirs, confidence/cluster frontmatter, failure tags, session skills
  └─ pages: wiki/hot.md, wiki/overview.md, wiki/index.md, wiki/schema.md, CLAUDE.md
  └─ sources: ScrapingArt/Karpathy-LLM-Wiki-Stack
