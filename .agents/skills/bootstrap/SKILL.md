---
name: bootstrap
description: Create a new knowledge domain from scratch — hub page, 3–5 seed concept stubs, index entries, log. Trigger with /bootstrap <domain> or "start a new domain for <topic>". Also seeds the wiki bundle itself on a cold start.
---

# Skill: /bootstrap <domain>

Creates a new knowledge domain from scratch: a hub page, seed concepts, index entries, and a log
entry. Also seeds the OKF bundle on a cold start (empty or missing `wiki/`).

## When to Use

- Starting to track a new topic area with no existing wiki coverage.
- User says `/bootstrap <domain>` or "start a new domain for <topic>".
- The repository has no `wiki/` directory yet (cold start — run Step 0 first).

## Step 0 — Cold Start (only if `wiki/` or its meta files are missing)

Before bootstrapping a domain, the bundle scaffold must exist. Create whatever is missing, then
record an `[INIT]` entry. Do NOT run this if the files already exist.

- `wiki/index.md` — OKF reserved. Carries only `okf_version: "0.2"`, no other frontmatter.
- `wiki/log.md` — OKF reserved. Starts with `# Log`, no frontmatter.
- `wiki/hot.md` — `type: cache`. Session hot cache sections (Focus, Active Pages, Open Questions, Recent Decisions, Last Operations, Known Failures, Pending Ingests).
- `wiki/overview.md` — `type: overview`. Cluster navigation hub.
- `wiki/schema.md` — `type: schema`. Entity templates (Domain Hub, Concept, Source, Fiche, Person, Project, Decision, Comparison, Synthesis, Pattern, Gap) used by `/ingest`, `/file-back`, and this skill.

Do NOT create `raw/` or `raw/queue.md` — `raw/` is human-owned and immutable. The human
populates the ingest queue; skills only read it.

Record (newest-first, under today's `## YYYY-MM-DD` heading in `wiki/log.md`):

```text
- **[INIT]** Seeded OKF bundle scaffold — pages: index.md, log.md, hot.md, overview.md, schema.md; sources: none
```

## Domain Workflow

1. **Create the domain hub page** at `wiki/domains/<slug>.md` using the Domain Hub template from
   `wiki/schema.md`.
   - Slug: lowercase, hyphen-separated (e.g. `machine-learning`, `knowledge-management`).
   - A one-paragraph description of the domain's scope.
   - Leave "In This Cluster" empty for now — filled in Step 4.

2. **Identify 3–5 seed concepts** for this domain. These are the most fundamental ideas needed to
   understand it — the anchors, not an exhaustive list.

3. **Create stub pages** for each seed concept at `wiki/concepts/<concept-slug>.md`:
   - Use the Concept Page template from `wiki/schema.md`.
   - Write at least a one-sentence definition and 2–3 bullet Core Ideas — no empty stubs.
   - Set `status: draft` and `confidence: low` initially (both valid OKF v0.2 values).
   - Set `cluster:` and `domain:` to the new domain slug.
   - Set `generated: {by: anthropic/<model-id>, at: <ISO-8601 with offset>}`, `verified: []`, `updated:`.

4. **Link seed concepts from the domain hub.** Fill in "In This Cluster" with markdown links to
   all seed concepts.

5. **Update `wiki/index.md`:**
   - Domain hub under the Domains section.
   - Each seed concept under the Concepts section.
   - All created pages under `## By Date` (today, suffixed `[BOOTSTRAP]`).

6. **Update `wiki/overview.md`** — add the new domain to the cluster navigation.

7. **Record in `wiki/log.md`** (newest-first):

   ```text
   - **[BOOTSTRAP]** New domain: <domain name> — pages: domains/<slug>.md, concepts/<seed1>.md, concepts/<seed2>.md, ...; sources: none (manual bootstrap)
   ```

8. **Update `wiki/hot.md`** — set Focus to the new domain, list the seed concept pages as Active Pages.

## Bootstrap Checklist

- [ ] (Cold start only) Bundle scaffold created and `[INIT]` logged.
- [ ] Domain hub page created with real content (not template placeholders).
- [ ] 3–5 seed concept stubs created (each with a definition + core ideas).
- [ ] All seed concepts linked from the domain hub.
- [ ] Domain hub in `wiki/index.md` under Domains.
- [ ] All seed concepts in `wiki/index.md` under Concepts and `## By Date`.
- [ ] `wiki/overview.md` updated.
- [ ] `wiki/log.md` updated with `[BOOTSTRAP]`.
- [ ] `wiki/hot.md` updated.

## Constraints

- Do NOT create empty stubs — every page needs real content from the bootstrap session.
- Seed concepts should be the 3–5 most load-bearing ideas, not an exhaustive list.
- After bootstrap, run `/ingest` on the first relevant raw sources to populate the domain with
  real knowledge.

## Purpose

The domain-seeding operation and the bundle cold-start path. Creates a hub + seed concepts so a
new topic area has a scaffold before real sources arrive.
