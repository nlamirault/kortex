---
type: cache
title: Session Hot Cache
description: Read silently at every session start. ~500 words. Current focus, active pages, open threads.
updated: 2026-10-08
---

# Kortex — Session Hot Cache

> Read this silently at every session start. Replaces recap conversation.
> Update at session end via `/session --close`.

---

## Current Focus

Bootstrapping the **AI Protocols** domain — open standards connecting LLMs and agents to
tools, each other, and payment rails. Seed scaffold just created; concept pages are
`draft` / `confidence: low` and carry `NOT VERIFIED` claims from model recall. Next step:
`/ingest` real protocol specs/articles to replace recall with cited knowledge.

## Active Pages

- [AI Protocols](domains/ai-protocols.md) — domain hub
- [Tool Use / Function Calling](concepts/tool-use-function-calling.md)
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md)
- [Agent2Agent (A2A)](concepts/agent2agent-a2a.md)
- [Agent Communication Protocol (ACP)](concepts/agent-communication-protocol-acp.md)
- [x402](concepts/x402.md)

## Open Questions

- How do the protocols compose into one stack (tool use + MCP internal, A2A + x402 external)?
- ACP (IBM) — still distinct, or folded into A2A? (`NOT VERIFIED` on the ACP page)
- x402 vs. Agentic Commerce Protocol — competing or complementary payment standards?

## Recent Decisions

- Seed concepts chosen as the 5 most load-bearing protocol primitives, not an exhaustive list.
- Slug convention: `<long-name>-<acronym>` (e.g. `model-context-protocol-mcp`); `x402` stays bare.

## Last Operations

- 2026-10-08 `[BOOTSTRAP]` — created AI Protocols domain + 5 seed concepts.
- 2026-10-08 `[INIT]` — completed bundle scaffold (hot.md, overview.md).

## Known Failures

- None.

## Pending Ingests

- None queued. Drop protocol specs/articles in `raw/` and run `/ingest` to enrich the domain.
