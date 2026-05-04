# Skill: /close

End-of-session routine. Updates `wiki/hot.md` and verifies wiki consistency before closing.
Run this before ending any session where wiki pages were touched.

## When to Use

- At the end of every session that modified wiki pages
- After an ingest operation
- Before switching to a different knowledge domain

## Workflow

1. **Collect session summary:**
   - What was the focus of this session?
   - What pages were created or updated?
   - What questions remain open?
   - What decisions were made?
   - Were any dead-ends or failures hit?

2. **Update `wiki/hot.md`:**
   - Set **Current Focus** to what was worked on (or "No active focus" if done)
   - Append new items to **Open Questions** (do not remove existing ones unless resolved)
   - Append to **Recent Decisions** (keep last 5, trim older)
   - Replace **Last Operations** with the last 5 entries from `wiki/log.md`
   - Update **Active Pages** list
   - Append to **Known Failures** if any dead-ends were hit

3. **Verify wiki consistency:**
   - All new pages are in `wiki/index.md` ✓
   - All new pages are wikilinked from at least one parent ✓
   - `wiki/log.md` has entries for every change made ✓
   - No template placeholders (`TODO`, `TBD`) left in new pages ✓

4. **Confirm:** "Session closed. `wiki/hot.md` updated. N pages modified this session."

## Output Format

```
/close summary:
- Focus: <what was worked on>
- Pages modified: <list>
- Open questions added: <list or "none">
- wiki/hot.md: updated
- Consistency checks: passed / N warnings
```
