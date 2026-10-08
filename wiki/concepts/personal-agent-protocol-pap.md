---
type: concept
title: Personal Agent Protocol (PAP)
description: Open standard from Meta and Sierra defining how personal AI agents connect to businesses — authentication, consumer-controlled access, and company visibility over web, MCP/OpenAPI, or company-agent routes.
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://sierra.ai/blog/introducing-personal-agent-protocol
    id: sierra-pap-2026
    title: "Introducing Personal Agent Protocol (Sierra blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [pap, personal-agents, mcp, openapi, oauth, consent, identity]
---

# Personal Agent Protocol (PAP)

The Personal Agent Protocol is an **open standard being developed by Meta and Sierra** with
industry partners, defining how personal AI agents interact with businesses: authentication,
consumer control over what an agent may access, and company visibility into agent activity —
over a website, APIs, or the company's own agent.[^sierra] It was announced 2026-10-06 by
Bret Taylor and Clay Bavor (Sierra).

## Problem

Personal agents today drive business websites the way people do — loading pages, clicking
forms — or fall back to support lines and chat. It is slow and often fails. A direct,
authenticated connection could complete the task securely in seconds.[^sierra]

## How It Works

- **Consumer-controlled access:** the consumer decides what access their agent gets; the company sets limits. A guest session answers simple questions; account tasks require sign-in with read-only or write scope the customer chooses.[^sierra]
- **Sessions built on OAuth:** sessions persist across channels, so a pre-sign-in question and a post-sign-in order change belong to the same visit.[^sierra]
- **Three routes to a business:** the company's website, APIs built on **MCP and OpenAPI**, or the company's own agent for conversational tasks (e.g. warranty claims). The company chooses which routes to offer.[^sierra]
- **Roadmap:** more granular permissions, push notifications (flight delays, shipments), and payments so agents can buy without sharing card details.[^sierra]

## Key Properties

- **Open standard** anyone can implement; Meta + Sierra steward it with partners.[^sierra]
- **Built on MCP + OpenAPI + OAuth** — notably **not** A2A (contrast with [PACT](personal-agent-consent-trust-protocol-pact.md), which builds on A2A).[^sierra]
- **Company agent is one route among several**, not the mandatory hub.[^sierra]
- **Status:** a v0.1 specification is planned "later in the month" (as of 2026-10-06), with design workshops and a reference implementation.[^sierra]

## Relation to PACT

PAP and [PACT](personal-agent-consent-trust-protocol-pact.md) are **parallel, same-day
(2026-10-06) efforts** addressing the same problem — personal agents acting on a user's
behalf at a business under consent — but with different sponsors and technical bases:

- **PAP** — Meta + Sierra; built on MCP + OpenAPI + OAuth.[^sierra]
- **PACT** — Decagon + Instinct; built on A2A + OAuth/JWT.

**`PENDING — escalate to human`:** The Decagon PACT announcement says it is "joining the
Personal Agent Protocol working group, announced by the team behind Meta's Muse." This Sierra
source names **no working group**, says PAP is developed by **Meta and Sierra**, and
identifies **"Muse" as a Rocket product** (not Meta's). Whether PAP (this page) *is* the
"Personal Agent Protocol working group" Decagon refers to, and the identity of "Muse", are
unresolved across the two sources.[^sierra]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-protocol-pap]] | builds-on | [[concept:model-context-protocol-mcp]] |
| [[concept:personal-agent-protocol-pap]] | part-of | [[domain:ai-protocols]] |
| [[concept:personal-agent-protocol-pap]] | contrasts-with | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[concept:personal-agent-protocol-pap]] | described-by | [[source:sierra-personal-agent-protocol-2026]] |

## Related

- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md) — the parallel, A2A-based effort; same problem, different stack and sponsors.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — one of PAP's API routes to a business.
- [AI Protocols](../domains/ai-protocols.md) — the agent-protocol cluster.
- [Introducing Personal Agent Protocol (Sierra blog)](../sources/sierra-personal-agent-protocol-2026.md) — the announcement source.

## Open Questions

- Is PAP the same effort as the "Personal Agent Protocol working group" Decagon is joining, or a competing standard of the same name? (`PENDING` above.)
- Do PAP (MCP/OpenAPI) and PACT (A2A) converge, coexist, or compete as the personal-agent↔business standard?
- Who is "Muse" — a Meta product (per Decagon) or a Rocket product (per Sierra)?
