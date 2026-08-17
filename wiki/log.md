# Kortex Wiki — Activity Log

Append-only chronological record of all wiki operations.
Format: `## [YYYY-MM-DD] [OP] | summary`

---

## [2026-05-04] [INIT] | Bootstrapped Kortex wiki structure
  └─ pages: wiki/index.md, wiki/log.md, wiki/schema.md
  └─ sources: CLAUDE.md (schema)

## [2026-05-04] [UPDATE] | Expanded schema with Three-Layer Architecture, operations, skills, session protocol, anti-corruption rules
  └─ pages: CLAUDE.md, wiki/log.md, wiki/index.md
  └─ sources: karpathy/llm-wiki.md, Alirezajalilii/WIKI_PROTOCOL_V1.md, medium article

## [2026-08-17] [INGEST] | Migrated Notion KB export to OKF format in wiki/kb/
  └─ pages: wiki/kb/index.md, wiki/kb/log.md, wiki/kb/{12 domain dirs}/ (95 entries)
  └─ sources: TMP/KB/ (109 Notion export files)
  └─ note: Domains: AI(15), Kubernetes(15), Observability(17), Security(13), Networking(10), Data(9), Domotic(5), Platform(4), Blockchain(3), Metering(2), WASM(1), General(1)

## [2026-05-04] [UPDATE] | Added hot cache, overview, comparisons, raw subdirs, confidence/cluster frontmatter, failure tags, session skills
  └─ pages: wiki/hot.md, wiki/overview.md, wiki/index.md, wiki/schema.md, CLAUDE.md
  └─ sources: ScrapingArt/Karpathy-LLM-Wiki-Stack
