---
title: Introducing the Personal Agent Consent & Trust Protocol (PACT) — Decagon, 2026
type: source
status: active
confidence: high
cluster: ai
domain: [ai, security]
sources: [https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact]
updated: 2026-10-07
tags: [AI, Protocol, Agents, Authorization, OAuth, Consent]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
key_claims:
  - PACT is an open-source standard for secure, verifiable interactions between personal agents and business agents.
  - It separates a personal agent's identity from its authority to act on a customer's account.
  - It builds on the Agent2Agent (A2A) protocol for communication and OAuth 2.0 for authorization.
  - The personal agent never handles the customer's login credentials; the customer authenticates directly with the business.
  - Decagon co-developed PACT with Instinct, aligned with Meta's Muse-led Personal Agent Protocol working group.
---

# Introducing the Personal Agent Consent & Trust Protocol (PACT)

**Author:** Harry Gao, Gram Liu (Decagon)
**Year:** 2026 (published 2026-10-06)
**Format:** article (company engineering blog)
**Link:** <https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact> — [[person:harry-gao]], [[person:gram-liu]]

## Summary

Decagon announces PACT, an open-source protocol that lets a customer's **personal agent** interact with a **business's AI agent** on the customer's behalf with explicit, verifiable consent — while never exposing the customer's login credentials. PACT layers a consent-and-delegation flow on top of the existing Agent2Agent (A2A) protocol and OAuth 2.0, and deliberately separates *who the personal agent is* (identity) from *what it is allowed to do* on a given account (authority). It was co-developed with Instinct and positioned within the Meta Muse-led Personal Agent Protocol working group.

## Key Ideas

- **Three parties:** the customer's **personal agent**, the **business**, and the **provider** that hosts the business's agent (e.g., Decagon). Requests are routed *through* the business's agent rather than around it.
- **Identity ≠ authority:** PACT verifies the personal agent's identity separately from its delegated authority to act on a specific customer account — the central design separation.
- **Built on existing standards:** A2A for agent-to-agent communication and OAuth 2.0 (device authorization flow) for consent, rather than a new bespoke stack.
- **Three-step flow:** (1) *Discover & connect* via the business's A2A Agent Card, with the personal agent authenticating using a short-lived signed JWT verified against published public keys; (2) *Authenticate customer & obtain consent* via OAuth device authorization — the customer logs in directly with the business and approves scopes, after which the provider issues a short-lived signed **delegation token** binding the customer account, the personal-agent platform, the target business, and the approved scopes; (3) *Act within granted permissions* — each request carries both the personal-agent identity and the customer delegation, the provider verifies both, and replies include **signed receipts** recording the scopes used and actions taken.
- **Business-defined permissions:** businesses declare available scopes (e.g., `orders:read`, `orders:cancel`) on their Agent Card; the business defines what can be delegated.
- **Credentials stay with the business:** the personal agent never touches login credentials — the customer always authenticates directly with the business.
- **Interoperability goal:** a customer's choice of personal agent should not depend on which provider platform a business runs; PACT makes the mechanics consistent across implementations.

## Notable Quotes

> "The personal agent never handles the customer's login credentials."

> "Personal agents need to work across businesses, and businesses need to serve customers using different personal agents."

> "The customer's choice of personal agent shouldn't depend on which platform a business uses."

> "PACT makes those mechanics consistent across implementations."

## Concepts Introduced

- [[concept:personal-agent-consent-trust-protocol-pact]]
- [[concept:personal-agent]]

## Open Questions Raised

- Governance model of the Personal Agent Protocol working group and PACT's standardization path are not detailed. `NOT VERIFIED`
- Exact token formats, signature algorithms, and receipt schema are summarized, not specified, in the blog post. `NOT VERIFIED`
- Relationship/overlap with payment-authorization protocols (AP2, MPP) is not addressed in the post.

## Rhetorical Analysis

**Audience:** practitioners (engineers building personal- and business-agent platforms) and ecosystem decision-makers evaluating agent interoperability standards.
**Style:** advocacy / practitioner — an engineering announcement framing a new open standard, with a concrete three-step protocol walkthrough.
**Epistemic stance:** confident and prescriptive about design choices, while presenting PACT as an open, collaborative work-in-progress.
**Persuasion devices:** reuse-of-established-standards appeal (A2A, OAuth) to signal pragmatism; security framing ("never handles credentials", "signed receipts"); interoperability-for-the-customer framing; authority-by-collaboration (Instinct, Meta's Muse working group).
**Bias indicators:** authored by Decagon, a *provider* that hosts business agents and therefore benefits from becoming the consent/delegation layer; the post normalizes the provider's position in the trust path.

## KnowledgeGraph

### Triples

| Subject | Type_Subject | Predicate | Object | Type_Object | Confidence | Temporality | Source |
|---------|-------------|-----------|--------|-------------|------------|-------------|--------|
| PACT | CONCEPT | implements | A2A | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| PACT | CONCEPT | implements | OAuth 2.0 | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| PACT | CONCEPT | enables | Personal agent ↔ business agent consent | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| PACT | CONCEPT | separates | Identity from authority | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Decagon | ORGANISATION | created | PACT | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| Instinct | ORGANISATION | co-developed | PACT | CONCEPT | 0.85 | STATIQUE | déclaré_article |
| Meta (Muse team) | ORGANISATION | announced | Personal Agent Protocol working group | EVENEMENT | 0.8 | STATIQUE | déclaré_article |
| Harry Gao | PERSONNE | authored | PACT blog post | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Gram Liu | PERSONNE | authored | PACT blog post | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Provider | CONCEPT | issues | Signed delegation token | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |

### Entities

| Entity | Type | Attribute | Value | Action |
|--------|------|-----------|-------|--------|
| PACT | CONCEPT | full name | Personal Agent Consent & Trust Protocol | AJOUT |
| PACT | CONCEPT | license | open-source | AJOUT |
| Decagon | ORGANISATION | role | provider hosting business agents; PACT creator | AJOUT |
| Instinct | ORGANISATION | role | personal-agent company; PACT co-developer | AJOUT |
| Meta | ORGANISATION | product | Muse personal agent; Personal Agent Protocol working group | AJOUT |
| Harry Gao | PERSONNE | role | Member of Technical Staff (ASWE), Decagon | AJOUT |
| Gram Liu | PERSONNE | role | Member of Technical Staff, Decagon | AJOUT |
| Delegation token | TECHNOLOGIE | property | short-lived, signed; binds account+platform+business+scopes | AJOUT |
| A2A Agent Card | TECHNOLOGIE | property | advertises endpoint, auth requirements, available scopes | MISE_A_JOUR |

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-consent-trust-protocol-pact]] | implements | [[concept:agent-to-agent-a2a]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | requires | [[concept:authorization]] |
| [[concept:personal-agent-consent-trust-protocol-pact]] | enables | [[concept:personal-agent]] |
| [[organization:decagon]] | created | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[organization:instinct]] | contributed-to | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[person:harry-gao]] | co-authored | [[source:decagon-pact-2026]] |
| [[person:gram-liu]] | co-authored | [[source:decagon-pact-2026]] |
