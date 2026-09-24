---
title: Agent Harness
type: concept
status: active
confidence: high
cluster: ai
domain: [ai]
sources: [https://unifiedharnessprotocol.org/]
updated: 2026-09-23
tags: [AI, Agents, Runtime, Harness]
generated: {by: claude-opus-4-8, at: 2026-09-23}
verified: []
stale_after: 2027-03-23
---

# Agent Harness

An **agent harness** is a complete agent runtime — a loop that plans, calls tools, edits
files, and reports back.

## Core Idea

A harness is the whole running agent, not just the model. It owns the control loop:
receive a task, plan, invoke tools, read and write files, maintain a session, and return
results plus artifacts. This is the unit that ships as a product — Codex, Claude Code,
Gemini CLI, Hermes, DeepSeek Harness, and Pi are all harnesses.

The distinction that matters: a **model API** exposes a *turn* — you send messages, get
tokens back, and run any tool calls yourself. A **harness** exposes a *task* — it runs the
tools, keeps the session, and hands back finished work. Standardizing how applications
drive harnesses is exactly what the [[concept:unified-harness-protocol-uhp]] sets out to
do, turning each harness into an interchangeable plug-in.

## Key Properties

- **Owns its loop** — planning, tool calls, file edits, and reporting happen inside the
  harness, not in the calling application.
- **Stateful session** — keeps conversation/task context across continuations.
- **Produces artifacts** — returns files, not just text.
- **Runs its own tools** — the caller delegates work rather than executing tool calls.
- **Product-shaped** — the harness is what end-user coding agents actually are.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agent-harness]] | is-a | Agent runtime / control loop |
| [[concept:agent-harness]] | contrasts-with | Model API (task vs turn) |
| [[concept:unified-harness-protocol-uhp]] | standardizes | [[concept:agent-harness]] |
| [[concept:agent-harness]] | used-by | Coding-agent products (Codex, Claude Code, Gemini CLI) |
| [[concept:agent-harness]] | uses | [[concept:model-context-protocol-mcp]] |

*Predicates: `is-a`, `part-of`, `enables`, `implements`, `requires`, `contrasts-with`, `extends`, `used-by`, `created-by`.*

## Related

- [[concept:unified-harness-protocol-uhp]] — the standard for driving harnesses
- [[concept:model-context-protocol-mcp]] — how tools plug into a harness
- [[concept:agent-skills]] — packaged capabilities a harness can load
- [[source:uhp-website-2026]] — source of this definition

## Open Questions

- Where is the line between "harness" and "agent framework" (LangGraph, CrewAI)? The UHP
  framing treats the harness as the shippable runtime, but the boundary is not formalized. `NOT VERIFIED`
