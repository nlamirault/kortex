---
title: openpactprotocol.org — Personal Agent Consent & Trust Protocol (landing page)
type: source
status: active
confidence: high
cluster: ai
domain: [ai, security]
sources: [https://openpactprotocol.org/]
updated: 2026-10-07
tags: [AI, Protocol, Agents, Authorization, OAuth, Consent]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
key_claims:
  - PACT lets personal agents contact brand support systems with cryptographic verification and granular user permissions, without sharing passwords.
  - It models four parties — User, Personal agent, Brand, and Provider — and builds unchanged on A2A 1.0.
  - Agents sign every request with a JWT; brands/providers verify via JWKS-distributed public keys.
  - Consent is an explicit, scoped step the user performs on the brand's login page; the agent never sees the password.
---

# openpactprotocol.org — Personal Agent Consent & Trust Protocol

**Author:** PACT project (openpactprotocol.org)
**Year:** 2026
**Format:** article (project landing page)
**Link:** <https://openpactprotocol.org/>

## Summary

The PACT landing page frames the problem that today personal agents interact with brands as **anonymous browser sessions**, with no way for a brand to know which agent is calling or whether the user authorized it. PACT adds two things on top of A2A: **trust** (the agent cryptographically signs every request) and **consent** (the user grants scoped, short-lived permissions on the brand's own login page, never sharing credentials). It is the canonical home of the protocol announced in the [Decagon blog post](decagon-pact-2026.md).

## Key Ideas

- **Four parties:** **User** (the person), **Personal agent** (agent platform), **Brand** (the business), and **Provider** (hosts support agents for multiple brands). This makes the *User* explicit versus the three-party framing in the announcement blog.
- **Trust = agent signatures:** the agent signs every request with a **JWT**; the provider validates the signature, so the brand knows which agent is calling. Public keys are distributed via **JWKS**.
- **Consent = scoped delegation:** the user logs in with the brand and approves specific actions; the agent receives a **scoped, short-lived delegation token** and acts only within it. This consent step is described as **optional** in the flow.
- **Discovery:** the agent finds a brand's **Agent Card** via a **well-known URL or a registry**.
- **A2A-native:** built on **A2A 1.0** — *"Everything A2A defines works unchanged."*
- **No credential sharing:** the agent never sees the user's password.

## Notable Quotes

> "the agent signs every request, so the Brand knows which agent is calling"

> "the User logs in with the Brand and approves specific actions. The agent never sees their password"

> "Everything A2A defines works unchanged"

## Concepts Introduced

- [[concept:personal-agent-consent-trust-protocol-pact]]
- [[concept:personal-agent]]

## Open Questions Raised

- No governing organization, working group, license, version, GitHub repo, or SDK is named on the landing page. `NOT VERIFIED`
- The Meta Muse-led Personal Agent Protocol working group (from the Decagon blog) is not mentioned here. `PENDING — reconcile sources`
- "Reference implementation" and integration guides are referenced but not linked on the page. `NOT VERIFIED`
- Signed receipts (named in the Decagon blog) are not mentioned on this landing page.

## Rhetorical Analysis

**Audience:** practitioners — engineers on personal-agent platforms and brand/provider support-agent teams.
**Style:** advocacy / practitioner — a concise standard landing page with a parties-and-flow walkthrough.
**Epistemic stance:** confident and pragmatic; leans on A2A reuse ("works unchanged") to lower adoption cost.
**Persuasion devices:** problem framing ("anonymous browser sessions"), standards-reuse appeal (A2A 1.0, JWT, JWKS), security reassurance ("never sees their password").
**Bias indicators:** the page credits Decagon only via a CDN image path with no textual acknowledgment; governance and authorship are unstated, so neutrality/openness claims cannot be verified from the page alone.

## KnowledgeGraph

### Triples

| Subject | Type_Subject | Predicate | Object | Type_Object | Confidence | Temporality | Source |
|---------|-------------|-----------|--------|-------------|------------|-------------|--------|
| PACT | CONCEPT | implements | A2A 1.0 | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| PACT | CONCEPT | uses | JWT request signing | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| PACT | CONCEPT | uses | JWKS public-key distribution | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| PACT | CONCEPT | involves | User | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| PACT | CONCEPT | involves | Brand | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| PACT | CONCEPT | involves | Provider | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Personal agent | CONCEPT | discovers | Agent Card (well-known URL / registry) | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |

### Entities

| Entity | Type | Attribute | Value | Action |
|--------|------|-----------|-------|--------|
| PACT | CONCEPT | parties | User, Personal agent, Brand, Provider | MISE_A_JOUR |
| PACT | CONCEPT | base protocol | A2A 1.0 | MISE_A_JOUR |
| Delegation token | TECHNOLOGIE | property | scoped, short-lived | MISE_A_JOUR |
| Agent Card | TECHNOLOGIE | discovery | well-known URL or registry | MISE_A_JOUR |
| JWKS | TECHNOLOGIE | role | distributes agent public keys for signature verification | AJOUT |

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-consent-trust-protocol-pact]] | implements | [[concept:agent-to-agent-a2a]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | requires | [[concept:authentication]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | enables | [[concept:personal-agent]] |
| [[source:openpactprotocol-org-2026]] | describes | [[concept:personal-agent-consent-trust-protocol-pact]] |
