---
type: source
title: "Introducing Strands Box: AI agent sandboxes powered by Dogwood"
description: Open-source (Apache 2.0, developer preview) AI-agent sandbox pairing OS-level containment (macOS Seatbelt) with Dogwood policy enforced at network, shell, Python, and MCP boundaries.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/
    id: strands-box-aws-2026
    title: "Introducing Strands Box (AWS Open Source Blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [governance, sandbox, agents, containment, dogwood, cedar, mcp, aws, runtime-verification]
---

# Introducing Strands Box: AI agent sandboxes powered by Dogwood

**Auteur :** Fernando Dingler · **Publié :** 2026-10-07 · **Lien :** https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~15 min

## En Bref

Strands Box is an open-source (Apache 2.0, developer preview) sandbox that governs what an AI
agent can do on a developer's machine. It pairs **OS-level containment** (starting with macOS
Seatbelt) as a hard boundary with **[Dogwood](ai-protocols-dogwood-runtime-verification-2026.md)
policy** enforced at the points where actions try to cross it. It matters because isolation
alone cannot express contextual rules ("read logs but don't change infrastructure", "post
updates but not too often") — Box adds those temporal, history-aware rules on top of
containment, outside the agent's own process.[^box]

## Points Clés

- **Two-layer model:** containment sets a hard OS/network boundary; Dogwood policy then governs each action inside it, enforced at network egress (proxy gateway), a Python interpreter (Monty), a Shell interpreter (Strands Shell), and an MCP broker.[^box]
- **Normalized events:** actions are reported uniformly (`fs:read`, `http:request`) regardless of tool, so one rule can cover a file read whether it comes from shell or Python.[^box]
- **Credential injection:** the agent only ever sees placeholder tokens; the gateway swaps in real secrets for permitted requests (bearer, custom header, HTTP Basic, query param, AWS SigV4) — the agent never holds credentials.[^box]
- **Two config files:** `box.toml` describes the environment (command, working dir, filesystem grants, tools, MCP servers, credential bindings); `policy.dw` holds the Dogwood rules.[^box]
- **Enforce from outside the process:** harness permissions run inside the agent and judge tool *calls*; Box enforces at the OS/network boundary and judges their *effects*. Trade-off: interpreters run outside the sandbox, widening the trusted computing base.[^box]

## Citation Notable

> "Box enforces from outside the process, at the OS and network boundary." — Fernando Dingler

## Contradiction — counting responses vs requests · `PENDING — escalate to human`

The example caps Slack posts at three per ten minutes. The rule's temporal clause counts prior
**HTTP-200 responses**, so refused posts are excluded from the budget; the post notes only that
binding on the `::request` event instead would count *attempts* (a refused post would then count
toward the three).[^box] It does **not** discuss concurrent, in-flight, or racing requests.[^box]

This conflicts with the [Dogwood fiche](ai-protocols-dogwood-runtime-verification-2026.md), which
argues rate limits should count **requests**, not responses, precisely so concurrency cannot
bypass the limit (N posts sent at once all pass while no 200s are yet recorded).[^dogwood-contra]
The two AWS sources disagree on how a rate-limit rule should bind, and the Box post never
addresses the concurrency-bypass cost the Dogwood post warns about. **Both positions documented
above; `PENDING — escalate to human`** — resolve against a real Dogwood/Box policy run.

[^dogwood-contra]: AWS Open Source Blog, "Introducing Dogwood: runtime verification for AI agents", 2026-08-06 — "rate limits should count *requests* to resist concurrency bypass" (see [Dogwood fiche](ai-protocols-dogwood-runtime-verification-2026.md), Points Clés).

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-strands-box-sandboxes-2026]] | implements | [[source:ai-protocols-dogwood-runtime-verification-2026]] |
| [[source:ai-protocols-strands-box-sandboxes-2026]] | implements | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-strands-box-sandboxes-2026]] | argues-that | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-strands-box-sandboxes-2026]] | extends | [[domain:ai-protocols]] |
| [[source:ai-protocols-strands-box-sandboxes-2026]] | published-by | [[organization:aws]] |

## Liens Wiki

- [Introducing Dogwood: runtime verification for AI agents](ai-protocols-dogwood-runtime-verification-2026.md) — Box embeds the Dogwood Local Engine and enforces its allow/deny decisions.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — Box ships an MCP broker as one of its four policy-enforcement points.
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — Box governs tool effects at the OS/network boundary rather than the tool call.
- [Amazon Web Services (AWS)](../organizations/aws.md) — publisher; part of the Strands Agents effort.
- [AI Protocols](../domains/ai-protocols.md) — adds an agent-containment/governance layer to the stack.

[^box]: AWS Open Source Blog, "Introducing Strands Box: AI agent sandboxes powered by Dogwood", Fernando Dingler, 2026-10-07. Companion post: https://strandsagents.com/blog/strands-box-the-big-picture (Marc Brooker).
