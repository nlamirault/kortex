---
name: file-back
description: Capture a reusable insight, decision, framework, or synthesis that emerged in conversation and file it permanently into the wiki. Trigger with the /file-back command, "file this back", or after a query produced novel analysis not yet in the wiki.
---

# Skill: /file-back

Captures knowledge that emerged during conversation and files it permanently into the wiki
before it is lost to chat history (Operation 4).

## When to Use

- A conversation produced a reusable insight, decision, framework, or synthesis.
- User says `/file-back "<title>"`, "file this back", or "save this insight".
- After a query that generated novel analysis not yet in the wiki.

## Workflow

1. **Identify the reusable knowledge.** What kind is it?
   - Decision made -> `wiki/decisions/`
   - Framework or mental model discovered -> `wiki/concepts/`
   - Cross-source synthesis -> `wiki/syntheses/`
   - Gap resolved -> update the existing `wiki/gaps/` page
   - Comparison completed -> `wiki/comparisons/`

2. **Determine the target page.** Check `wiki/index.md` — does a page already exist that should
   be updated? If yes, update it. If no, create a new page.

3. **Create or update the page** using the correct template from `wiki/schema.md`. Every claim
   must cite a source (wiki page or raw file). Untraceable claims -> mark `NOT VERIFIED`.

4. **Cite the conversation as the source** in frontmatter — `sources` is a list of mappings,
   each with a required `resource` (OKF v0.2 forbids bare strings):

   ```yaml
   sources:
     - resource: "conversation:YYYY-MM-DD"
       title: "<topic discussed>"
   generated: {by: anthropic/<model-id>, at: <ISO-8601 with UTC offset>}
   verified: []
   updated: <YYYY-MM-DD>
   ```

5. **Link from parent pages:**
   - Add a markdown link from the relevant domain hub page.
   - Add the page to `wiki/index.md` under its entity-type section and to `## By Date`
     (today, suffixed `[FILE]`).
   - Add markdown links from related concept/source pages where applicable.

6. **Record in `wiki/log.md`** (newest-first, under today's `## YYYY-MM-DD` heading):

   ```text
   - **[FILE]** Filed "<title>" — pages: <created/updated page>; sources: conversation:YYYY-MM-DD
   ```

7. **Update `wiki/hot.md`** if this changes the current focus or opens new questions.

## Prompts to Determine Type

When the user calls `/file-back "<title>"` without specifying a type, ask once:

- "Is this a decision (chose X over Y), a framework (mental model), a synthesis (cross-source analysis), or a gap resolution?"
- Pick the answer and proceed — do not enumerate the options back at the user.

## Constraints

- Do NOT file ephemeral details — only reusable knowledge with lasting value.
- Do NOT create placeholder pages — the insight must be fully written now.
- If the insight contradicts an existing wiki page, document both and mark `PENDING — escalate to human`.
- Keep the conversation context as provenance — future sessions need to know where it came from.

## Purpose

Operation 4 (File Back). Captures reusable insight from dialogue before it is lost to chat
history — the wiki's inbound arc from conversation.
