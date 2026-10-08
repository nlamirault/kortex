---
type: source
title: "Introducing Personal Agent Protocol"
description: Meta and Sierra announce PAP — an open standard for how personal AI agents connect to businesses (auth, consumer-controlled access, company visibility) over web, MCP/OpenAPI, or company-agent routes.
format: fiche
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
tags: [pap, personal-agents, meta, sierra, mcp, openapi, oauth]
---

# Introducing Personal Agent Protocol

**Auteurs :** Bret Taylor, Clay Bavor (Sierra) · **Publié :** 2026-10-06 · **Lien :** https://sierra.ai/blog/introducing-personal-agent-protocol
**Domaine :** [AI Protocols](../domains/ai-protocols.md)

## En Bref

Meta and Sierra introduce the **Personal Agent Protocol (PAP)**, an open standard for how
personal AI agents interact with businesses — covering authentication, consumer control over
agent access, and company visibility into agent activity. Personal agents today drive
websites like humans (loading pages, clicking forms) or fall back to chat; a direct,
authenticated connection could finish the task securely in seconds.[^sierra] It is a parallel
effort to [PACT](../concepts/personal-agent-consent-trust-protocol-pact.md), announced the
same day, but built on MCP/OpenAPI rather than A2A.

## Points Clés

- **Consumer-controlled access:** consumers choose what access their agent gets; companies set limits. Guest sessions handle simple questions; account tasks require sign-in with read-only or write scope.[^sierra]
- **OAuth sessions persist across channels:** a pre-sign-in question and a post-sign-in order change belong to the same visit.[^sierra]
- **Three routes to a business:** website, APIs on **MCP + OpenAPI**, or the company's own agent for conversational tasks — the company chooses which to offer.[^sierra]
- **Roadmap:** granular permissions, push notifications (flight delays, shipments), and payments so agents buy without sharing card details.[^sierra]
- **Status & stewardship:** open standard; Meta + Sierra develop it with partners (Genesys, Instinct, Rocket, Shopify, Stripe, Walmart); a **v0.1 spec** is planned later in the month with workshops + a reference implementation.[^sierra]

## Citation Notable

> "Personal AI is creating a new front door to the enterprise." — Tony Bates, Chairman & CEO, Genesys

## Contradiction Flag

`PENDING — escalate to human`: the Decagon PACT post says PACT is "joining the Personal Agent
Protocol working group, announced by the team behind Meta's Muse." This source names **no
working group**, attributes PAP to **Meta + Sierra**, and calls **"Muse" a Rocket product**.
See [PAP concept → Relation to PACT](../concepts/personal-agent-protocol-pap.md#relation-to-pact).

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:sierra-personal-agent-protocol-2026]] | introduces | [[concept:personal-agent-protocol-pap]] |
| [[source:sierra-personal-agent-protocol-2026]] | builds-on | [[concept:model-context-protocol-mcp]] |
| [[source:sierra-personal-agent-protocol-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Personal Agent Protocol (PAP)](../concepts/personal-agent-protocol-pap.md) — the concept this post introduces.
- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md) — the parallel A2A-based effort announced the same day.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — one of PAP's API routes.
- [AI Protocols](../domains/ai-protocols.md) — the cluster.

[^sierra]: Sierra blog, "Introducing Personal Agent Protocol", Bret Taylor & Clay Bavor, 2026-10-06.
