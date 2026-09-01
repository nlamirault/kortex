# Skill: /today

Morning session startup. Reads hot cache and recent log to orient quickly without recap conversation.
Replaces 2,000–4,000 tokens of "where were we?" with 650–700 tokens of structured context.

## When to Use

- At the start of a new session
- After a break of more than a few hours
- When resuming work on a topic after switching domains

## Workflow

1. Read `wiki/hot.md` silently — full file.
2. Read the last 10 entries in `wiki/log.md`.
3. Read `raw/queue.md` — count items under `## Pending` and `## Processing`.
4. Read any pages listed in **Active Pages** section of `wiki/hot.md`.
5. Synthesize a session briefing.

## Output Format

```
/today briefing — <YYYY-MM-DD>

Focus:        <current focus from hot.md>
Last worked:  <date of last log entry>
Active pages: <list from hot.md>
Ingest queue: <N pending, N processing>  ← 0/0 if empty; list titles if ≤3

Open questions:
  - <list>

Suggested next steps:
  1. <ingest next queued item if pending > 0>
  2. <based on open questions and active pages>
  3. <based on recent operations>
  4. <optional: lint if last lint was > 7 days ago>

Recent operations (last 5):
  - <from log.md>
```

## Constraints

- Do NOT modify any files during `/today`.
- Keep briefing under 400 words.
- If `wiki/hot.md` is empty or missing sections, note it and suggest running `/close` after next session.
- If `raw/queue.md` is missing, report "queue: not found" — do not create the file.
- If queue has items in `## Processing`, highlight first — it was in-flight when last session ended.
