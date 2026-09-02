---
title: Machine Payments Protocol (MPP)
type: concept
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
---

# Machine Payments Protocol (MPP)

**MPP is an open protocol for machine-to-machine payments that revives the HTTP `402 Payment Required` status code so any client can pay as part of the HTTP exchange — no account, API key, or billing relationship set up in advance.** Co-authored by [[project:tempo]] (Tempo Labs) and Stripe.

## Core Idea

Paying for an internet resource — an API call, a dataset, a unit of compute — has always required an account, API key, or billing relationship provisioned ahead of time. That handshake is fine for humans who set it up once, but it blocks autonomous AI agents that need to transact with services they have never seen before. MPP removes the pre-provisioning step: a server responds `402 Payment Required` with machine-readable payment terms, the client pays inline, and the request completes. Payment becomes a native part of the request/response cycle rather than a prerequisite to it.

MPP is deliberately **rail-agnostic and currency-agnostic**. The same protocol surface works over blockchain rails (EVM, [[concept:blockchain-layer-1|Solana]], Stellar, Hedera, NEAR Intents, the Lightning Network, USDC stablecoin) and over traditional processors (Stripe, card networks, ACH, and Tempo's own L1). A separation between abstract *intents* and concrete *methods* keeps the core minimal while allowing each network to plug in its own settlement mechanics.

Its headline primitive is the **session**: an agent authorizes a spending limit upfront, then streams many micropayments continuously against it — without an on-chain transaction per interaction. This is what makes per-API-call agentic billing economically viable at internet scale, where a blockchain settlement per call would be too slow and too expensive.

## Key Properties

- **HTTP-native** — built on the standard `402 Payment Required` status code and a `Payment` HTTP authentication scheme; no bespoke transport required.
- **Modular spec** — split into *Core* (402 semantics, headers, IANA registries), *Intents* (charge, authorize, subscription patterns), *Methods* (network-specific: Tempo, Stripe, ACH), and *Extensions* (discovery, identity).
- **Sessions primitive** — upfront spend authorization + streamed micropayments, avoiding one on-chain tx per call.
- **Transports** — JSON-RPC and [[concept:model-context-protocol-mcp|MCP]] as message-passing transports, wiring MPP into AI-agent infrastructure.
- **Openly licensed** — specifications are CC0 1.0 (public domain); reference tooling is Apache 2.0 or MIT.
- **Draft stage** — spec versions 00–01 as of launch (mainnet March 2026); adopted across 50+ services in its first week (OpenAI, Anthropic, Google Gemini, Dune Analytics).

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:machine-payments-protocol-mpp]] | created-by | [[project:tempo]] |
| [[concept:machine-payments-protocol-mpp]] | extends | [[concept:url-uri-urn]] |
| [[concept:machine-payments-protocol-mpp]] | used-by | [[concept:model-context-protocol-mcp]] |
| [[concept:machine-payments-protocol-mpp]] | contrasts-with | [[concept:agent-payments-protocol-ap2]] |
| [[concept:machine-payments-protocol-mpp]] | contrasts-with | [[concept:x402]] |
| [[concept:machine-payments-protocol-mpp]] | contrasts-with | [[concept:universal-commerce-protocol-ucp]] |

*Note: `extends` HTTP semantics (402 status code) is captured via the URI/URN identifier page; MPP itself defines no new transport.*

## Related

- [[project:tempo]] — the Stripe/Paradigm L1 blockchain that co-authors and settles MPP
- [[concept:agent-payments-protocol-ap2]] — Google-led agentic payment protocol; AP2 signs mandates over A2A/MCP, MPP settles over HTTP 402
- [[concept:universal-commerce-protocol-ucp]] — commerce data/cart standard; complementary layer to MPP's settlement
- [[concept:x402]] — sibling HTTP 402 payment protocol; both revive 402 for machine settlement
- [[concept:model-context-protocol-mcp]] — used as an MPP transport
- [[concept:ai-protocols]] — protocol landscape hub
- [[source:mpp-specs]] — the specification source

## Open Questions

- How does MPP relate to **x402** (also an HTTP-402 agentic-payment scheme)? Both revive 402 — convergence or fragmentation? See [[concept:x402]].
- Does the `session` primitive's off-chain streaming introduce settlement/dispute risk versus per-tx on-chain finality?
- Draft (00–01) — API surface may shift before v1; `stale_after` set to 6 months.
