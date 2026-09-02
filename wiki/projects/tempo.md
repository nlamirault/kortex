---
title: Tempo
type: project
status: active
confidence: high
cluster: blockchain
domain: [blockchain, ai]
sources: [https://paymentauth.org/, https://github.com/tempoxyz/mpp-specs]
updated: 2026-09-02
tags: [Blockchain, Payments, Stablecoin, L1]
generated: {by: claude-opus-4-8, at: 2026-09-02}
verified: []
stale_after: 2027-09-02
---

# Tempo

**Type:** initiative (Layer-1 blockchain)
**Status:** active — mainnet live 2026-03-18
**URL:** https://paymentauth.org/ · https://github.com/tempoxyz/mpp-specs

## What It Does

Tempo is a specialized [Layer-1 blockchain](../concepts/blockchain-layer-1.md) built by **Stripe** and **Paradigm**, engineered exclusively for high-frequency stablecoin transactions at internet scale. Where general-purpose L1s optimize for arbitrary smart contracts, Tempo optimizes for one thing: settling machine-to-machine payments cheaply and fast enough that an AI agent can pay per API call. Tempo Labs co-authored the [Machine Payments Protocol (MPP)](../concepts/machine-payments-protocol-mpp.md) with Stripe and serves as one of its native settlement methods.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[project:tempo]] | is-a | [[concept:blockchain-layer-1]] |
| [[project:tempo]] | implements | [[concept:machine-payments-protocol-mpp]] |
| [[project:tempo]] | part-of | [[domain:blockchain]] |

*Built by Tempo Labs with Stripe + Paradigm; MPP is co-authored by Tempo Labs and Stripe. No `organization` entity type exists in this wiki — Stripe and Paradigm are named in prose.*

## Relevance to Kortex

Tempo is the settlement backbone of the emerging agentic-payments stack. It anchors the [MPP](../concepts/machine-payments-protocol-mpp.md) concept on the blockchain side and gives the [blockchain](../domains/blockchain.md) domain its first concrete project. Design partners at launch included Visa, Mastercard, Deutsche Bank, Standard Chartered, Revolut, Nubank, Shopify, OpenAI, Anthropic, Ramp, and DoorDash — signalling that machine-to-machine commerce is being built by both incumbent finance and frontier-AI labs at once.

## Related

- [Machine Payments Protocol (MPP)](../concepts/machine-payments-protocol-mpp.md) — the protocol Tempo co-authors and settles
- [Layer-1 blockchain](../concepts/blockchain-layer-1.md) — the L1 class Tempo belongs to
- [MPP Specs](../sources/mpp-specs.md) — specification source
- [Blockchain](../domains/blockchain.md) — parent domain
