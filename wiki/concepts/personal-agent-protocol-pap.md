---
title: Personal Agent Protocol (PAP)
type: concept
status: active
confidence: medium
cluster: ai
domain: [ai]
sources: [https://sierra.ai/blog/introducing-personal-agent-protocol]
updated: 2026-10-07
tags: [AI, Protocol, Agents, Commerce]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
---

# Personal Agent Protocol (PAP)

[**PAP**](https://sierra.ai/blog/introducing-personal-agent-protocol) is an open
standard — led by **Meta** and **Sierra** — for secure, direct communication between a
consumer's *personal AI agent* and a business, so an agent can complete tasks against a
company's systems without screen-scraping its website like a human.

## Core Idea

Personal agents today act on a user's behalf the slow way: they drive websites and apps as
a person would — clicking forms, waiting through page loads — to book, buy, or ask. PAP
replaces that with a direct machine-to-business connection that completes the same task in
seconds instead of minutes, while keeping the consumer in control of what the agent is
allowed to do and giving the business visibility into who the agent represents and what it
is authorized to do.

The protocol is organized as a layered discovery-and-access model. A personal agent first
**discovers** what a company offers and how to connect (advertised on the company's site).
It then **initiates a session** on the user's behalf, starting as a *guest* for basic
queries. **Authentication** escalates that session: the user decides, via OAuth-based
credentials, whether to grant read-only or write access. Finally the company chooses which
**access route** the agent uses — plain website navigation, an API connection (MCP /
OpenAPI), or a company-provided conversational agent.

Sessions are built on OAuth and carry across channels: a question asked before sign-in and
an order change made after it belong to the same visit. The guiding principle is two-sided
control — "consumers decide what access to give their personal agents, and companies set
parameters for what those agents can do."

## Key Properties

- **Two-sided control** — consumer grants scope (read-only vs. write); business sets the
  parameters and chosen access channels.
- **OAuth-based sessions** that persist across channels (guest → authenticated within one
  visit).
- **Three access routes** — website navigation, API (MCP / OpenAPI), or a company agent for
  conversational tasks.
- **Discovery-first** — agents learn a company's offerings and connection methods from its
  website.
- **Open implementation** available to all partners; v0.1 spec planned for **late October
  2026**, with design workshops and a reference implementation to follow. `NOT VERIFIED`
- **Planned extensions** — granular per-action permissions, push notifications for status,
  and a payment extension enabling transactions without sharing a credit card. `NOT VERIFIED`

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-protocol-pap]] | created-by | [[organization:meta]] |
| [[concept:personal-agent-protocol-pap]] | created-by | [[organization:sierra]] |
| [[concept:personal-agent-protocol-pap]] | requires | OAuth |
| [[concept:personal-agent-protocol-pap]] | part-of | [[concept:ai-protocols]] |
| [[concept:personal-agent-protocol-pap]] | contrasts-with | [[concept:universal-commerce-protocol-ucp]] |

*Predicates: `is-a`, `part-of`, `enables`, `implements`, `requires`, `contrasts-with`, `extends`, `used-by`, `created-by`.*

## Related

- [[concept:ai-protocols]] — sibling standards (MCP, A2A, ACP, AG-UI, UCP)
- [[concept:model-context-protocol-mcp]] — one of PAP's named API access routes (alongside OpenAPI)
- [[concept:universal-commerce-protocol-ucp]] — adjacent agent↔commerce scope; contrast on where authorization sits
- [[concept:agent-payments-protocol-ap2]] — agent-layer payment authorization; relevant to PAP's planned payment extension
- [[organization:meta]], [[organization:sierra]] — lead developers
- [[person:bret-taylor]], [[person:clay-bavor]] — Sierra co-founders, post authors
- [[concept:personal-agent-consent-trust-protocol-pact]] — sibling standard (Decagon) for the same personal-agent↔business link; consent/trust layer — see Open Questions
- [[source:sierra-personal-agent-protocol-2026]] — where this comes from

## Open Questions

- The v0.1 spec, governance model, and reference implementation were announced but not yet
  published as of 2026-10-06. `NOT VERIFIED`
- How PAP's API access route relates to / reuses MCP and OpenAPI concretely (transport,
  auth hand-off) is described only at a high level. `NOT VERIFIED`
- Relationship to the planned payment extension vs. existing agent-payment standards
  (AP2, x402, MPP) is unstated. `NOT VERIFIED`
- Relationship to [PACT](personal-agent-consent-trust-protocol-pact.md) — both announced 2026-10-07 for the personal-agent↔business link, both Meta-adjacent, both OAuth-based. Convergent, competing, or layered (PACT as consent profile under PAP)? `PENDING — reconcile`
