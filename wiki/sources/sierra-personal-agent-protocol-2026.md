---
title: Introducing the Personal Agent Protocol (Sierra, 2026)
type: source
status: active
confidence: high
cluster: ai
domain: [ai]
sources: [https://sierra.ai/blog/introducing-personal-agent-protocol]
updated: 2026-10-07
tags: [AI, Protocol, Agents, Commerce]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
key_claims:
  - PAP is an open standard, led by Meta and Sierra, for direct secure communication between personal AI agents and businesses.
  - It replaces human-style website navigation with machine-to-business connections that complete tasks in seconds, not minutes.
  - Sessions are built on OAuth and carry across channels; the consumer grants read-only or write access.
  - Companies choose the access route — website navigation, API (MCP/OpenAPI), or a company-provided agent.
  - A v0.1 specification is planned for late October 2026, followed by design workshops and a reference implementation.
---

# Introducing the Personal Agent Protocol

**Author:** Bret Taylor and Clay Bavor (Sierra)
**Year:** 2026
**Format:** article (company blog post / protocol announcement)
**Link:** <https://sierra.ai/blog/introducing-personal-agent-protocol>
**Published:** 2026-10-06
**Link:** [[person:bret-taylor]] · [[person:clay-bavor]]

## Summary

Sierra and Meta announce the **Personal Agent Protocol (PAP)**, an open standard for direct,
secure communication between a consumer's personal AI agent and a business. The argument:
personal agents are going mainstream, and the current approach — agents driving websites and
apps like humans — is slow and brittle. PAP defines a layered discovery, session, and
OAuth-authenticated access model so agents complete tasks in seconds while consumers control
what access they grant and companies control what agents may do. A v0.1 specification is
planned for late October 2026, with design workshops and a reference implementation to follow.

## Key Ideas

- **Problem — agents act like humans:** today's personal agents "navigate websites and apps
  like humans," clicking forms and waiting through load times; PAP enables direct
  machine-to-business connections that complete tasks in seconds rather than minutes.
- **Three stakeholder needs:** consumers want "speed, dependability, and trust"; brands want
  visibility into agent activity and control over authorized actions; agent builders want
  consistent, efficient access across many company systems.
- **Layered access model:** (1) discovery of a company's offerings and connection methods on
  its site; (2) session initiation on the user's behalf, starting as a *guest* for basic
  queries; (3) OAuth authentication where the user chooses read-only vs. write; (4) company
  choice of access route — website navigation, API (MCP / OpenAPI), or a company-provided
  agent for conversational tasks.
- **Session continuity on OAuth:** the session "carries across channels, so a question asked
  before sign-in and an order change made afterward are part of the same visit."
- **Two-sided control principle:** "consumers decide what access to give their personal
  agents, and companies set parameters for what those agents can do."
- **Governance & timeline:** v0.1 spec planned late October 2026; design workshops with
  interested parties; an open implementation available to all partners; a reference
  implementation to follow.
- **Planned extensions:** granular per-action permissions, push notifications for real-time
  status, and payment extensions enabling transactions without sharing a credit card.

## Notable Quotes

> "Personal AI is creating a new front door to the enterprise. Brands need a trusted way to
> know who an AI agent represents, what it's authorized to do, its intent, and how to work
> with it securely." — Tony Bates, CEO, Genesys

> "The next era of AI is about persistent agents taking action… our agentic technology allows
> a Muse agent to move across our platform, from finding a home, to securing financing and
> beyond." — Shawn Malhotra, CTO, Rocket

> "When customers send an agent, they expect the same service they'd get themselves… a
> standard way to recognize their customers' agents." — Kevin Miller, Head of Payments, Stripe

## Concepts Introduced

- [[concept:personal-agent-protocol-pap]]

## Open Questions Raised

- The v0.1 spec, governance docs, and reference implementation are announced but not yet
  published as of 2026-10-06. `NOT VERIFIED`
- How PAP's API access route concretely reuses MCP and OpenAPI (transport, auth hand-off) is
  stated only at a high level. `NOT VERIFIED`
- How the planned payment extension relates to existing agent-payment standards
  (AP2, x402, MPP) is unstated. `NOT VERIFIED`
- Beyond the named launch partners (Genesys, Instinct, Rocket, Shopify, Stripe, Walmart),
  adoption breadth is unknown. `NOT VERIFIED`

## Rhetorical Analysis

**Audience:** executives and practitioners — brand/commerce decision-makers and agent builders deciding whether to adopt the standard.
**Style:** advocacy / announcement — a vendor-authored launch post anchored by partner-executive endorsements.
**Epistemic stance:** confident about the design and need; forward-looking and unproven on delivery ("planned," "to follow").
**Persuasion devices:** named-partner social proof (Genesys, Rocket, Shopify, Stripe, Walmart), concrete speed framing ("seconds, not minutes"), appeal to an established standard (OAuth) for trust, two-sided-control framing to reassure both consumers and brands.
**Bias indicators:** co-authored by Sierra's founders and published on Sierra's own blog; Sierra sells enterprise AI agents, so the "new front door to the enterprise" framing aligns with its commercial interest; partner quotes are selected endorsements.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-protocol-pap]] | created-by | [[organization:meta]] |
| [[concept:personal-agent-protocol-pap]] | created-by | [[organization:sierra]] |
| [[concept:personal-agent-protocol-pap]] | requires | OAuth |
| [[concept:personal-agent-protocol-pap]] | part-of | [[concept:ai-protocols]] |
| [[person:bret-taylor]] | co-authored | [[source:sierra-personal-agent-protocol-2026]] |
| [[person:clay-bavor]] | co-authored | [[source:sierra-personal-agent-protocol-2026]] |

*Launch partners named in the source (not yet separate pages): Genesys, Instinct, Rocket, Shopify, [[organization:stripe]], Walmart.*
