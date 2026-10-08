---
name: lint
description: Health audit of the wiki — runs the mechanical OKF v0.2 + hygiene checks (make lint), then the judgment checks a script can't make. Trigger with /lint, weekly, or before a major ingest session.
---

# Skill: /lint

Full health audit of the wiki (Operation 3). The mechanical, deterministic checks live in
`scripts/lint_wiki.py` (`make lint`); this skill runs that first, then adds the judgment calls a
script cannot make. Report by severity tier. Fix CRITICAL immediately.

## When to Use

- User types `/lint`.
- Periodically (suggested: weekly, or when `wiki/log.md` shows no lint in 7+ days).
- Before a major ingest session.

## Step 1 — Run the mechanical checks

```sh
make lint
```

`scripts/lint_wiki.py` deterministically checks and exits non-zero on any CRITICAL:

- **CRITICAL** — unparseable frontmatter; missing/empty `type` on any non-reserved page
  (including `wiki/kb/*.md`).
- **WARNING** — `status` outside `draft | stable | deprecated`; bare-date timestamp (no UTC
  offset) in `generated.at` / `verified[].at` / `stale_after`; `sources` that is a string list
  or lacks `resource`; `verified[].by` not in `human:` / `process:` / `<producer>/<version>`
  form; reserved `index.md` / `log.md` carrying stray frontmatter; placeholder
  (`TODO`/`TBD`/`{text}`/`{N}`); broken markdown or Relations-table link; bare `[[type:slug]]`
  outside a `## Relations` table.
- **INFO** — page missing `updated:`; entity page not listed in `wiki/index.md`.

Take its output as the mechanical half of the report. Fix every CRITICAL before continuing.

## Step 2 — Judgment checks (not mechanizable)

Read the pages the mechanical pass flagged, plus `wiki/hot.md`, and assess:

### Freshness (staleness is derived, never a status)

- Pages where `now >= stale_after` — flag for re-verification before trusting; do NOT write a status.
- Pages where `stale_after` is within 30 days — schedule review.
- Pages in fast-moving domains (AI/protocols: 6mo, Kubernetes: 1yr) lacking `stale_after` — suggest adding one.
- `deprecated` pages missing a markdown link to their replacement.
- `wiki/hot.md` — is Focus still current? Are Active Pages still relevant?

### Knowledge graph quality

- Source pages missing a `## KnowledgeGraph` section, or with empty Triples/Entities tables.
- Concept/project/person pages missing `## Relations`, or with only placeholder rows
  (Subject = `[[concept:this-concept]]`).
- Claims marked `NOT VERIFIED` — list by page.

### Consistency

- Contradictions between pages — the same claim stated differently → mark both
  `PENDING — escalate to human`. Never silently resolve.
- Duplicate canonical pages (same entity under two slugs) — flag for merge.

### Gaps

- Gap pages not yet marked `✅ Resolved` — can any now be resolved from recent ingests?

## Step 3 — Report

```text
/lint report — YYYY-MM-DD

CRITICAL (fix now):
  - [page] [issue]
WARNING (fix soon):
  - [page] [issue]
INFO (low priority):
  - [page] [issue]

Stats (from make lint + judgment):
  Pages audited: N | OKF violations: N | Broken links: N | Orphans: N
  Expired (now >= stale_after): N | Expiring soon (<= 30d): N | NOT VERIFIED: N | Open gaps: N
```

## Step 4 — After the report

1. Fix all CRITICAL issues immediately.
2. Record under today's date at the top of `wiki/log.md` (newest-first):

   ```text
   - **[LINT]** Health audit — pages: <N audited>; sources: none; critical: <N>, warning: <N>, info: <N>
   ```

3. Add any pages fixed during the audit to `wiki/index.md` `## By Date` under today, suffixed `[LINT]`.
4. Update `wiki/hot.md` if open questions or active pages changed.

## Constraints

- Do NOT silently fix contradictions — mark `PENDING — escalate to human`.
- Do NOT delete gap pages — mark resolved gaps `✅ Resolved — YYYY-MM-DD` with evidence.
- Staleness is derived, not a status — never write `status: stale`. Flag expired pages for re-verification.

## Purpose

Operation 3 (Lint). Audits the wiki layer for drift, decay, and contradiction, and checks OKF
v0.2 conformance. The deterministic checks run in `scripts/lint_wiki.py` so they are fast and
reliable; the skill adds only what needs judgment.
