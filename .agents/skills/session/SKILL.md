---
name: session
description: Session bookends. `--open` gives a morning briefing from the hot cache + recent log (orient without re-deriving "where were we?"); `--close` refreshes the hot cache and verifies wiki consistency before stopping. Trigger at session start/resume (open) and session end or after an ingest (close).
---

# Skill: /session [--open | --close]

One skill for both ends of a work session. Pick the mode from context when no flag is given:
session start or resume → `--open`; wrapping up or after writing wiki pages → `--close`.

---

## Mode: `--open` (morning briefing)

Reads the hot cache and recent log to orient quickly without a recap conversation. Replaces
2,000–4,000 tokens of "where were we?" with ~650 tokens of structured context.

**Use when:** starting a session, after a break of more than a few hours, or when resuming a
topic after switching domains.

### Open workflow

1. Read `wiki/hot.md` silently — full file.
2. Read the most recent date block in `wiki/log.md` (newest-first, top of file) — last ~10 entries.
3. Read `raw/queue.md` — count items under `## Pending` and `## Processing`.
4. Read any pages listed in the **Active Pages** section of `wiki/hot.md`.
5. Synthesize the briefing.

### Open output

```text
/session --open — <YYYY-MM-DD>

Focus:        <current focus from hot.md>
Last worked:  <date of newest log entry>
Active pages: <list from hot.md>
Ingest queue: <N pending, N processing>   (0/0 if empty; list titles if <= 3)

Open questions:
  - <list>

Suggested next steps:
  1. <ingest next queued item if pending > 0>
  2. <based on open questions and active pages>
  3. <optional: make lint if the last lint was more than 7 days ago>

Recent operations (last 5):
  - <from log.md>
```

### Open constraints

- Read-only. Do NOT modify any files.
- Keep the briefing under 400 words.
- If `wiki/hot.md` is empty or missing sections, note it and suggest a `--close` after the session.
- If `raw/queue.md` is missing, report "queue: not found" — do not create it.
- If the queue has `## Processing` items, highlight them first — they were in-flight at last close.

---

## Mode: `--close` (end-of-session)

Updates `wiki/hot.md` and verifies wiki consistency before closing. Enforces Hard Rule 1
(update before ending).

**Use when:** ending a session that modified wiki pages, after an ingest, or before switching
domains.

### Close workflow

1. **Collect the session summary:** focus, pages created/updated, open questions, decisions,
   any dead-ends or failures.
2. **Update `wiki/hot.md`:**
   - Set **Current Focus** (or "No active focus" if done).
   - Append to **Open Questions** (remove only resolved ones).
   - Append to **Recent Decisions** (keep the last 5).
   - Replace **Last Operations** with the most recent 5 entries from `wiki/log.md`.
   - Update **Active Pages**.
   - Append to **Known Failures** if any dead-ends were hit (and log them as `!failure` in `wiki/log.md`).
   - Read `raw/queue.md` → update **Pending Ingests**: `- raw/queue.md: N pending, N processing`
     (or `- raw/queue.md: not found`).
   - Bump `updated:` in the `wiki/hot.md` frontmatter.
3. **Verify consistency:**
   - All new pages are in `wiki/index.md` (entity section + `## By Date`).
   - All new pages are linked from at least one parent page.
   - `wiki/log.md` has a newest-first entry for every change made.
   - No `TODO`/`TBD`/`{text}` placeholders left in new pages.
   - If source Relations changed, `make kb` was run.
   - Run `make lint` — fix any CRITICAL before closing.
4. **Confirm:** "Session closed. `wiki/hot.md` updated. N pages modified this session."

### Close output

```text
/session --close summary:
- Focus: <what was worked on>
- Pages modified: <list>
- Open questions added: <list or "none">
- Ingest queue: N pending, N processing
- wiki/hot.md: updated
- make lint: clean / N warnings
```

### Close constraints

- Do NOT leave consistency warnings silent — list them in the summary.
- Do NOT remove open questions unless genuinely resolved this session.

---

## Purpose

The Session Startup Protocol and its end-of-session counterpart, merged. `--open` keeps
accumulated state pre-synthesized and always ready; `--close` keeps it accurate for next time.
