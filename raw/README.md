# Raw Sources

This directory contains immutable source documents.

**Rules:**
- Files here are **read-only**. Never modify them.
- Add new sources by dropping files into this directory (or subdirectories).
- After adding a source, trigger **Ingest** in Claude: "Ingest `raw/<filename>`"

## Supported Formats

- Markdown (`.md`)
- Plain text (`.txt`)
- PDF (`.pdf`) — Claude will read directly
- Any format Claude can parse

## Naming Convention

Use lowercase kebab-case with author and year where applicable:

```
ahrens-smart-notes-2017.pdf
matuschak-evergreen-notes-2020.md
hofstadter-godel-escher-bach-1979.txt
```
