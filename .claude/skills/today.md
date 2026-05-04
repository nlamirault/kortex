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
3. Read any pages listed in **Active Pages** section of `wiki/hot.md`.
4. Synthesize a session briefing.

## Output Format

```
/today briefing — <YYYY-MM-DD>

Focus:       <current focus from hot.md>
Last worked: <date of last log entry>
Active pages: <list from hot.md>

Open questions:
  - <list>

Suggested next steps:
  1. <based on open questions and active pages>
  2. <based on recent operations>
  3. <optional: lint if last lint was > 7 days ago>

Recent operations (last 5):
  - <from log.md>
```

## Constraints

- Do NOT modify any files during `/today`.
- Keep briefing under 400 words.
- If `wiki/hot.md` is empty or missing sections, note it and suggest running `/close` after next session.
