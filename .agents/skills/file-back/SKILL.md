# Skill: /file-back "<title>"

Captures knowledge that emerged during conversation and files it permanently into the wiki before it is lost to chat history.

## When to Use

- Conversation produced a reusable insight, decision, framework, or synthesis
- User says `/file-back "<title>"` or "file this back", "save this insight"
- After a query that generated novel analysis not yet in the wiki

## Workflow

1. **Identify the reusable knowledge.** What kind is it?
   - Decision made → `wiki/decisions/`
   - Framework or mental model discovered → `wiki/concepts/`
   - Cross-source synthesis → `wiki/syntheses/`
   - Gap resolved → update existing `wiki/gaps/` page
   - Comparison completed → `wiki/comparisons/`

2. **Determine target page.** Check `wiki/index.md` — does a page already exist that should be updated? If yes, update it. If no, create new page.

3. **Create or update the page** using the correct template from `wiki/schema.md`. Every claim must cite a source (wiki page or raw file). Untraceable claims → mark `NOT VERIFIED`.

4. **Cite conversation as source** in frontmatter: `sources: [conversation YYYY-MM-DD: <topic>]`

5. **Link from parent pages:**
   - Add wikilink from relevant domain hub page
   - Add to `wiki/index.md`
   - Add wikilink from related concept/source pages if applicable

6. **Append to `wiki/log.md`:**

```
## [YYYY-MM-DD] [FILE] | Filed "<title>"
  └─ pages: <created/updated page>
  └─ sources: conversation YYYY-MM-DD
```

7. **Update `wiki/hot.md`** if this changes current focus or opens new questions.

## Prompts to Determine Type

When user calls `/file-back "<title>"` without specifying type, ask:
- "Is this a decision (chose X over Y), a framework (mental model), a synthesis (cross-source analysis), or a gap resolution?"
- Pick the answer, don't enumerate options back at the user.

## Constraints

- Do NOT file ephemeral details — only reusable knowledge with lasting value.
- Do NOT create placeholder pages — the insight must be fully written now.
- If insight contradicts an existing wiki page → document both, mark `PENDING — escalate to human`.
- Keep conversation context as provenance — future sessions need to know where this came from.

## Purpose

Operation 4 (File Back). Captures reusable insight from dialogue before it is lost
to chat history — the wiki's inbound arc from conversation. Provenance format
mandated by [[decision:adopt-wikiskill-evolution-loop]]. Sibling of `/evolve`,
which captures insight about the *procedures* rather than the *knowledge*.
