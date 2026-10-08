---
type: source
title: "Introducing the Personal Agent Consent & Trust Protocol (PACT)"
description: Decagon open-sources PACT (co-developed with Instinct) — a consent/delegation layer on A2A letting personal agents act on a customer's account with verifiable, scoped permission.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact
    id: decagon-pact-2026
    title: "Introducing PACT (Decagon blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [pact, consent, delegation, decagon, a2a, oauth, agents]
---

# Introducing the Personal Agent Consent & Trust Protocol (PACT)

**Auteur :** Harry Gao, Gram Liu (Decagon, Members of Technical Staff) · **Publié :** 2026-10-06 · **Lien :** https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact
**Domaine :** [AI Protocols](../domains/ai-protocols.md)

## En Bref

Decagon is open-sourcing **PACT**, co-developed with Instinct — a protocol that lets a
customer's **personal agent** act for them when dealing with a business, under explicit,
verifiable consent. Personal agents (Muse, Instinct, dots) now book travel and resolve
issues, meeting business-side agents with no standard way to prove the customer authorized
the interaction. PACT fixes that by separating the agent's **identity** from its **authority**
to act on an account.[^decagon] The post says Decagon is also joining "the Personal Agent
Protocol working group." **`PENDING — escalate to human`:** this post attributes that group
to "the team behind Meta's Muse," but the [Sierra PAP announcement](../concepts/personal-agent-protocol-pap.md)
(same day) names PAP as a Meta + Sierra effort with no working group and calls "Muse" a Rocket
product — the two sources conflict on who convenes it and what "Muse" is.

## Points Clés

- **Three active parties + principal:** the customer's personal agent, the Brand (business), and the Provider hosting the business's agent (e.g. Decagon) — acting for the customer.[^decagon]
- **Discover & connect:** the personal agent reads the Brand's **A2A Agent Card** (endpoint, auth, permission scopes); requests are signed with short-lived **JWTs** — proving the platform, not account control.[^decagon]
- **Consent via OAuth device flow:** the customer signs in directly with the Brand and grants scopes; the agent never sees credentials. The Provider then issues a short-lived delegation token bound to customer + agent + Brand + scopes.[^decagon]
- **Acting within limits:** each request carries identity + delegation; A2A's authorization-required state escalates scope in-conversation; responses include **signed receipts** of scopes used.[^decagon]
- **Design principles:** route through the business's agent, reuse A2A + OAuth 2.0, separate identity from authority, let Brands define permissions, keep login with the Brand.[^decagon]

## Citation Notable

> "PACT gives these interactions explicit, verifiable customer permissions."

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:decagon-pact-introduction-2026]] | introduces | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[source:decagon-pact-introduction-2026]] | builds-on | [[concept:agent2agent-a2a]] |
| [[source:decagon-pact-introduction-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md) — the concept this announcement introduces.
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — PACT builds on A2A's Agent Card and authorization-required state.
- [AI Protocols](../domains/ai-protocols.md) — the cluster PACT joins as a consent/authority layer.

[^decagon]: Decagon blog, "Introducing the Personal Agent Consent & Trust Protocol (PACT)", Harry Gao & Gram Liu, 2026-10-06.
