---
title: Personal Agent Consent & Trust Protocol (PACT)
type: concept
status: active
confidence: medium
cluster: ai
domain: [ai, security]
sources: [https://openpactprotocol.org/, https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact]
updated: 2026-10-07
tags: [AI, Protocol, Agents, Authorization, OAuth, Consent]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
---

# Personal Agent Consent & Trust Protocol (PACT)

An open-source protocol for secure, verifiable interactions between a customer's **personal agent** and a **business's AI agent**, giving the business explicit proof of customer consent while keeping the customer's login credentials out of the personal agent's hands.

## Core Idea

As personal agents (e.g., [Meta's](../organizations/meta.md) Muse, [Instinct](../organizations/instinct.md), dots) begin acting on customers' behalf — booking travel, managing purchases, resolving support issues — they increasingly need to talk to *business* agents. PACT standardizes that interaction so the business can verify two separate things: **who the personal agent is** (identity) and **what the customer has actually authorized it to do** on their account (authority). Keeping identity and authority distinct is the protocol's central design decision.

PACT does not invent a new transport or auth stack. It layers a consent-and-delegation flow on top of the [Agent2Agent (A2A)](agent-to-agent-a2a.md) protocol for communication and [OAuth 2.0](authorization.md) (device authorization flow) for consent. Requests are routed *through* the business's agent, hosted by a **provider** (e.g., [Decagon](../organizations/decagon.md)), rather than around it. Crucially, the customer always authenticates **directly with the business** — the personal agent never sees the credentials.

## How It Works

Four parties (per the canonical [openpactprotocol.org](../sources/openpactprotocol-org-2026.md) landing page): the **User**, the **personal agent**, the **brand** (the business), and the **provider** hosting the brand's agent. The Decagon announcement framed this as three parties, leaving the User implicit. PACT builds on **A2A 1.0** unchanged — *"Everything A2A defines works unchanged."* Three steps:

1. **Discover & connect.** The personal agent discovers the brand's A2A **Agent Card** via a **well-known URL or a registry**; the card advertises the endpoint, authentication requirements, and available permission **scopes** (e.g., `orders:read`, `orders:cancel`). The personal agent signs every request with a short-lived **JWT**; the provider verifies the signature against public keys distributed via **JWKS**.
2. **Authenticate customer & obtain consent.** The personal agent requests scopes via the **OAuth device authorization flow**, presenting the customer a login link. The customer signs in directly with the business and approves the permissions (the landing page describes this consent step as **optional**). The provider then issues a short-lived, signed **delegation token** binding the verified customer account, the personal-agent platform, the target business, and the approved scopes.
3. **Act within granted permissions.** Each subsequent request carries both the personal-agent identity and the customer delegation. The provider verifies both before running the business agent within the approved scopes. Replies include signed **receipts** recording the scopes used and the actions taken.

## Key Properties

- **Identity separated from authority** — verified independently.
- **Credentials never leave the business** — personal agent is never in the credential path.
- **Business-defined scopes** — the business declares what may be delegated.
- **Short-lived signed tokens** for both personal-agent auth and customer delegation.
- **Auditable** — signed receipts record scopes used and actions taken.
- **Standards-based** — reuses A2A + OAuth 2.0 rather than a bespoke protocol.
- **Provider-interoperable** — a customer's choice of personal agent is independent of the business's provider platform.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-consent-trust-protocol-pact]] | implements | [[concept:agent-to-agent-a2a]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | requires | [[concept:authorization]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | enables | [[concept:personal-agent]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | created-by | [[organization:decagon]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | part-of | [[concept:ai-protocols]] |

## Related

- [AI / Protocols](ai-protocols.md) — the protocol cluster PACT belongs to
- [Personal Agent Protocol (PAP)](personal-agent-protocol-pap.md) — sibling Meta/Sierra standard for the same personal-agent↔business link; PACT is the consent/trust layer, PAP the broader connection standard — see Open Questions
- [Personal Agent](personal-agent.md) — the actor PACT delegates authority to
- [Agent-to-Agent (A2A)](agent-to-agent-a2a.md) — the transport PACT builds on
- [Authorization](authorization.md) — OAuth 2.0 consent model PACT reuses
- [openpactprotocol.org — canonical landing page](../sources/openpactprotocol-org-2026.md)
- [PACT source: Decagon, 2026](../sources/decagon-pact-2026.md) — announcement blog

## Open Questions

- Standardization/governance path via the Personal Agent Protocol working group. `NOT VERIFIED`
- Precise token and receipt schemas, signature algorithms. `NOT VERIFIED`
- Overlap with payment-authorization protocols ([AP2](agent-payments-protocol-ap2.md), [MPP](machine-payments-protocol-mpp.md)).
- Relationship to [PAP](personal-agent-protocol-pap.md) — both announced 2026-10-07 for the personal-agent↔business link, both Meta-adjacent, both OAuth-based. Is PACT a consent/trust profile under PAP, a competing stack, or convergent? `PENDING — reconcile`
