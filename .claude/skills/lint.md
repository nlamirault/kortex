# Skill: /lint

Full health audit of the wiki. Finds drift, decay, and inconsistency before they compound.

## When to Use

- User types `/lint`
- Periodically (suggested: weekly, or when `wiki/log.md` shows no lint in 7+ days)
- Before a major ingest session

## Workflow

Run all checks below. Collect findings. Report by severity tier. Fix CRITICAL immediately. Log WARNING and INFO for human review.

### Checks

**Structural**
- [ ] Every `.md` in `wiki/` (except `log.md`, `index.md`) has valid YAML frontmatter with all required fields
- [ ] No `TODO`, `TBD`, `{text}`, `{N}` placeholders in any wiki page
- [ ] Every page has `updated:` date set

**Links**
- [ ] Broken `[[wikilinks]]` — target page file does not exist
- [ ] Orphan pages — not linked from `wiki/index.md` AND not wikilinked from any other page
- [ ] Pages present in `wiki/index.md` but file does not exist

**Freshness**
- [ ] Pages with `status: stale` — list them
- [ ] Pages with `updated:` date > 90 days ago and `status: active` — flag as candidate-stale
- [ ] Pages where `stale_after` < today — CRITICAL: page is past expiry; mark `status: stale` and flag for re-verification
- [ ] Pages where `stale_after` is within 30 days from today — WARNING: expiry approaching; schedule review
- [ ] Pages in fast-moving domains (AI/protocols: 6mo, Kubernetes: 1yr) that lack `stale_after` — INFO: add expiry date
- [ ] `wiki/hot.md` — is Focus still current? Are Active Pages still relevant?

**Knowledge Graph**
- [ ] Source pages missing `## KnowledgeGraph` section — flag
- [ ] Source pages with empty Triples or Entities tables — flag
- [ ] Claims marked `NOT VERIFIED` — list by page

**Consistency**
- [ ] Contradictions between pages — same claim stated differently in two pages → mark both `PENDING — escalate to human`
- [ ] Duplicate canonical pages (same entity under two different slugs) — flag for merge

**Gaps**
- [ ] Gap pages marked `status: open` — list; check if any can now be resolved from recent ingests

## Output Format

```
/lint report — YYYY-MM-DD

CRITICAL (fix now):
  - [page] [issue]

WARNING (fix soon):
  - [page] [issue]

INFO (low priority):
  - [page] [issue]

Stats:
  Pages audited: N
  Broken links: N
  Orphans: N
  Stale: N
  Expired (stale_after past): N
  Expiring soon (≤30d): N
  Missing stale_after (fast-moving domain): N
  NOT VERIFIED claims: N
  Open gaps: N
```

## After Report

1. Fix all CRITICAL issues immediately.
2. Append to `wiki/log.md`:

```
## [YYYY-MM-DD] [LINT] | Health audit
  └─ pages: <N pages audited>
  └─ sources: none
  └─ critical: <N>, warning: <N>, info: <N>
  └─ expired: <N>, expiring-soon: <N>
```

3. Update `wiki/hot.md` if open questions or active pages changed.

## Constraints

- Do NOT silently fix contradictions — mark `PENDING — escalate to human`.
- Do NOT delete gap pages — mark resolved gaps with `✅ Resolved — YYYY-MM-DD`.
- Stale status is worse than missing — mark immediately, don't defer.
