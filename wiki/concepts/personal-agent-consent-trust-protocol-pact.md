---
type: concept
title: Personal Agent Consent & Trust Protocol (PACT)
description: Open protocol letting a user's personal agent act on their behalf with a business's support agent under verifiable, scoped, user-granted consent — built on A2A 1.0.
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact
    id: decagon-pact-2026
    title: "Introducing PACT (Decagon blog)"
  - resource: https://openpactprotocol.org/
    id: openpact-site-2026
    title: "PACT protocol home (openpactprotocol.org)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [pact, consent, delegation, agents, a2a, oauth, jwt, identity]
---

# Personal Agent Consent & Trust Protocol (PACT)

PACT is an open protocol that lets a **personal agent** (an AI acting for a user) contact a
**business's support agent** with a verifiable identity and act on the user's account only
with permissions the user explicitly granted. It is **built on [A2A](agent2agent-a2a.md)
1.0 and leaves everything A2A defines unchanged**, adding a consent-and-delegation layer on
top.[^openpact][^decagon] Decagon open-sourced it, co-developed with Instinct; the
specification lives at openpactprotocol.org and the code on GitHub.[^decagon]

## Problem

Personal agents (Muse, Instinct, dots) increasingly meet business-side AI agents, but there
is no standard way for the business to (a) verify *which* platform is calling, or (b) confirm
the agent is authorized to act on *this* user's account — without handing over the user's
password. PACT's core move is to **separate the agent's identity from its authority** to act
on a given account.[^decagon][^openpact]

## Roles

- **User** — the person (the principal).
- **Personal agent** — the platform acting for the user.
- **Brand** — the business, whose support agent runs on a Provider.
- **Provider** — builds and hosts support agents for many Brands (e.g. Decagon).[^openpact]

A personal agent registers **once per Provider**, then can reach every Brand that Provider
hosts.[^openpact]

## How It Works

1. **Registration** — the agent gives the Provider its issuer URL + public keys (JWKS) and receives an `audience` string.[^openpact]
2. **Discovery** — the agent fetches the Brand's **A2A Agent Card**, listing the endpoint, auth requirements, and delegation scopes (e.g. `orders:read`, `orders:cancel`).[^openpact][^decagon]
3. **Signed requests** — each request is a short-lived **JWT** carrying a stable, anonymous user id, verified against the agent's JWKS. This proves the platform, not account control.[^openpact][^decagon]
4. **Consent (optional)** — the user signs in on the **Brand's own login page** (never through the agent) and approves each scope individually. The Decagon announcement specifies this uses **OAuth's device-authorization flow**; the spec site describes it generically without naming OAuth.[^decagon][^openpact]
5. **Delegation** — the Provider issues a scoped, short-lived token naming the user, agent, Brand, and granted scopes; responses can include **signed receipts** of scopes used and actions taken.[^decagon]

Without consent, the Brand knows which agent is calling but not the user, so it must still ask for details (e.g. an order number).[^openpact]

## Key Properties

- **Builds on A2A 1.0, unchanged** — PACT is a layer, not a fork.[^openpact]
- **Separates identity (who is calling) from authority (what they may do on an account).**[^decagon]
- **Login stays with the Brand** — the personal agent never sees credentials.[^decagon][^openpact]
- **Reuses existing standards** — A2A, JWT/JWKS, and (per Decagon) OAuth 2.0.[^decagon]
- **Open protocol** — spec public at openpactprotocol.org, code on GitHub; stewardship not yet a named foundation (Decagon + Instinct co-developed; Decagon is joining the Personal Agent Protocol working group).[^decagon]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-consent-trust-protocol-pact]] | builds-on | [[concept:agent2agent-a2a]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | part-of | [[domain:ai-protocols]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | described-by | [[source:decagon-pact-introduction-2026]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | specified-by | [[source:openpactprotocol-pact-spec-2026]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | contrasts-with | [[concept:personal-agent-protocol-pap]] |

## Related

- [Personal Agent Protocol (PAP)](../concepts/personal-agent-protocol-pap.md) — the parallel, same-day Meta + Sierra effort on the same problem, built on MCP/OpenAPI instead of A2A.
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — PACT's base layer; it extends A2A's Agent Card and authorization-required state with consent + delegation.
- [AI Protocols](../domains/ai-protocols.md) — the agent-protocol cluster; PACT is its consent/authority layer.
- [Introducing PACT (Decagon blog)](../sources/decagon-pact-introduction-2026.md) — the announcement source.
- [PACT protocol home (openpactprotocol.org)](../sources/openpactprotocol-pact-spec-2026.md) — the specification source.

## Open Questions

- Who will steward PACT long-term? The spec home names no governing body; the Decagon post says Decagon is joining "the Personal Agent Protocol working group." **`PENDING — escalate to human`:** that post attributes the group to "the team behind Meta's Muse," but the [Sierra PAP announcement](../concepts/personal-agent-protocol-pap.md) names PAP as a Meta + Sierra effort with no working group and calls "Muse" a Rocket product. Does PACT fold into [PAP](../concepts/personal-agent-protocol-pap.md), or are they competing same-name efforts?
- Is the consent flow formally OAuth 2.0 device-authorization (per Decagon) or a PACT-specific flow (the spec site names no OAuth)? `PENDING — reconcile at spec read`.
- How does PACT's delegation model compare with x402's payment authority — are consent and payment separate layers of the same agent-commerce stack?
