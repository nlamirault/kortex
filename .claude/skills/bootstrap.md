# Skill: /bootstrap <domain>

Creates a new knowledge domain from scratch: hub page, seed concepts, index entries, and log.

## When to Use

- Starting to track a new topic area with no existing wiki coverage
- User says `/bootstrap <domain>` or "start a new domain for <topic>"

## Workflow

1. **Create domain hub page** at `wiki/domains/<slug>.md` using the Domain Hub template from `wiki/schema.md`.
   - Slug: lowercase, hyphen-separated (e.g., `machine-learning`, `knowledge-management`)
   - One-paragraph description of the domain's scope
   - Leave "In This Cluster" initially empty — will fill in step 3

2. **Identify 3–5 seed concepts** for this domain. These are the most fundamental ideas needed to understand the domain. Not exhaustive — just the anchors.

3. **Create stub pages** for each seed concept at `wiki/concepts/<concept-slug>.md`:
   - Use Concept Page template from `wiki/schema.md`
   - Write at least a one-sentence definition and 2-3 bullet Core Ideas — no empty stubs
   - Set `status: draft`, `confidence: low` initially
   - Set `cluster:` and `domain:` to the new domain slug

4. **Link seed concepts from domain hub.** Fill in "In This Cluster" section with wikilinks to all seed concepts.

5. **Add to `wiki/index.md`:**
   - Domain hub under "Domains" section
   - Each seed concept under "Concepts" section

6. **Update `wiki/overview.md`** — add new domain to the cluster navigation.

7. **Append to `wiki/log.md`:**

```
## [YYYY-MM-DD] [BOOTSTRAP] | New domain: <domain name>
  └─ pages: domains/<slug>.md, concepts/<seed1>.md, concepts/<seed2>.md, ...
  └─ sources: none (manual bootstrap)
```

8. **Update `wiki/hot.md`** — set Focus to new domain, list seed concept pages as Active Pages.

## Bootstrap Checklist

- [ ] Domain hub page created with real content (not template placeholders)
- [ ] 3–5 seed concept stubs created (each with definition + core ideas)
- [ ] All seed concepts wikilinked from domain hub
- [ ] Domain hub in `wiki/index.md` under Domains
- [ ] All seed concepts in `wiki/index.md` under Concepts
- [ ] `wiki/overview.md` updated
- [ ] `wiki/log.md` appended with `[BOOTSTRAP]`
- [ ] `wiki/hot.md` updated

## Constraints

- Do NOT create empty stubs — every page needs real content from the bootstrap session.
- Seed concepts should be the 3–5 most load-bearing ideas, not an exhaustive list.
- After bootstrap, run `/ingest` on first relevant raw sources to populate the domain with real knowledge.
