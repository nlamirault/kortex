# Kortex Wiki — Activity Log

Append-only chronological record of all wiki operations.
Format: `## [YYYY-MM-DD] [OP] | summary`

---

## [2026-09-02] [INGEST] | Added Machine Payments Protocol (MPP) by Tempo Labs & Stripe
  └─ pages: wiki/concepts/machine-payments-protocol-mpp.md (new), wiki/projects/tempo.md (new), wiki/sources/mpp-specs.md (new), wiki/concepts/agent-payments-protocol-ap2.md (+Relations), wiki/concepts/universal-commerce-protocol-ucp.md (+Related), wiki/concepts/ai-protocols.md, wiki/domains/ai.md, wiki/domains/blockchain.md, wiki/index.md, wiki/hot.md
  └─ sources: https://paymentauth.org/, https://github.com/tempoxyz/mpp-specs
  └─ note: MPP revives HTTP 402 for machine-to-machine payments; Tempo = Stripe/Paradigm L1 settlement. Draft 00–01, stale_after 6mo. Open: relation to Coinbase x402 (no page yet).

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
