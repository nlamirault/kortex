---
title: Machine Payments Protocol Specifications (MPP), Tempo Labs & Stripe, 2026
type: source
status: active
confidence: high
cluster: ai
domain: [ai, blockchain]
sources: [https://paymentauth.org/, https://github.com/tempoxyz/mpp-specs]
updated: 2026-09-02
tags: [AI, Protocol, Payments, Blockchain]
generated: {by: claude-opus-4-8, at: 2026-09-02}
verified: []
stale_after: 2027-03-02
key_claims:
  - MPP is an open protocol for machine-to-machine payments over HTTP, reviving the 402 Payment Required status code.
  - Co-authored by Tempo Labs and Stripe; specs are CC0, tooling Apache-2.0/MIT.
  - The session primitive lets an agent authorize a spend limit once and stream micropayments without a per-call on-chain tx.
---

# Machine Payments Protocol Specifications (MPP)

**Author:** Tempo Labs & Stripe (co-authored)
**Year:** 2026 (mainnet 2026-03-18; spec drafts 00–01)
**Format:** specification / documentation site
**Link:** https://paymentauth.org/ · repo `tempoxyz/mpp-specs`

## Summary

The MPP specifications define an open, rail- and currency-agnostic standard for machine-to-machine payments that occur inline over HTTP via the `402 Payment Required` status code. Co-authored by Tempo Labs and Stripe alongside the Stripe/Paradigm-built Tempo L1 blockchain, MPP targets agentic payments — AI agents paying per API call, dataset, or unit of compute — without any pre-provisioned account or API key.

## Key Ideas

- **HTTP 402 revival:** payment terms are returned in a `402` response with a `Payment` HTTP auth scheme; the client pays as part of the request/response cycle.
- **Layered spec:** *Core* (402 semantics, headers, IANA registries) → *Intents* (charge, authorize, subscription) → *Methods* (Tempo, Stripe, ACH, EVM, Solana, Stellar, Hedera, NEAR Intents, Lightning, USDC) → *Extensions* (discovery, identity).
- **Sessions:** authorize a spending limit upfront, then stream continuous micropayments with no on-chain transaction per interaction.
- **Transports:** JSON-RPC and [MCP](../concepts/model-context-protocol-mcp.md), connecting settlement to AI-agent infrastructure.
- **Design principles:** "minimal protocol designed for safe extension," network/method/currency agnosticism, "durable by design."

## Notable Quotes

> "The open protocol for machine-to-machine payments." — MPP README

> "Paying for an internet resource, such as an API call, a dataset, or a unit of compute, still typically requires an account, API key, or billing relationship set up in advance. MPP lets any client pay as part of the HTTP exchange using the native `402 Payment Required` status code." — MPP README

## Concepts Introduced

- [Machine Payments Protocol (MPP)](../concepts/machine-payments-protocol-mpp.md)
- [Tempo](../projects/tempo.md)

## Open Questions Raised

- Relationship to Coinbase's x402 (also HTTP-402-based) — convergence or competing standard?
- Off-chain session streaming vs on-chain finality: settlement/dispute trade-offs?

## Rhetorical Analysis

**Audience:** practitioner — protocol implementers, payment engineers, AI-agent builders.
**Style:** advocacy + technical specification — standards-body register with a clear promotional frame around the "machine payments" era.
**Epistemic stance:** certain on design, hedged on maturity (self-labelled draft 00–01).
**Persuasion devices:** appeal to open standards (CC0), incumbent-authority co-authorship (Stripe), reuse of an existing web primitive (402) rather than inventing transport, breadth of supported rails.
**Bias indicators:** authored by Tempo Labs and Stripe, who directly benefit from adoption — Tempo is a named settlement method; framing favours the Tempo/Stripe stack even as the spec claims rail-agnosticism.

## KnowledgeGraph

### Triples

| Subject | Type_Subject | Predicate | Object | Type_Object | Confidence | Temporality | Source |
|---------|-------------|-----------|--------|-------------|------------|-------------|--------|
| MPP | CONCEPT | co-authored-by | Tempo Labs | ORGANISATION | 1.0 | STATIQUE | déclaré_article |
| MPP | CONCEPT | co-authored-by | Stripe | ORGANISATION | 1.0 | STATIQUE | déclaré_article |
| MPP | CONCEPT | uses-transport | MCP | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| MPP | CONCEPT | reuses | HTTP 402 Payment Required | TECHNOLOGIE | 1.0 | ATEMPOREL | déclaré_article |
| Tempo | PROJET | built-by | Stripe + Paradigm | ORGANISATION | 1.0 | STATIQUE | déclaré_article |
| Tempo | PROJET | settles | MPP | CONCEPT | 0.9 | ATEMPOREL | inféré |
| MPP | CONCEPT | contrasts-with | AP2 | CONCEPT | 0.7 | ATEMPOREL | inféré |

### Entities

| Entity | Type | Attribute | Value | Action |
|--------|------|-----------|-------|--------|
| Machine Payments Protocol (MPP) | CONCEPT | status | draft 00–01 | AJOUT |
| Tempo | PROJET | class | L1 stablecoin blockchain | AJOUT |
| Stripe | ORGANISATION | role | co-author, payment method | AJOUT |
| Paradigm | ORGANISATION | role | co-builder of Tempo L1 | AJOUT |
| MCP | CONCEPT | role | MPP transport | MISE_A_JOUR |
| HTTP 402 | TECHNOLOGIE | role | core status code | AJOUT |
| AP2 | CONCEPT | relation | contrasting payment protocol | MISE_A_JOUR |
