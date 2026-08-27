# Kortex Wiki — Activity Log

Append-only chronological record of all wiki operations.
Format: `## [YYYY-MM-DD] [OP] | summary`

---

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
