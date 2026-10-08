---
type: source
title: "Linux Foundation Announces Operational Launch of x402 Foundation"
description: The x402 Foundation launches under the Linux Foundation with ~40 members; Coinbase completes its contribution of the x402 HTTP-native payment protocol to neutral governance.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://x402.org/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications/
    id: x402-foundation-2026
    title: "Linux Foundation Announces Operational Launch of x402 Foundation (press release)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [x402, payments, stablecoin, governance, x402-foundation, linux-foundation, agents]
---

# Linux Foundation Announces Operational Launch of x402 Foundation

**Éditeur :** The Linux Foundation (communiqué, hébergé sur x402.org) · **Publié :** 2026-07-14 (maj 2026-10-01) · **Lien :** https://x402.org/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications/
**Domaine :** [AI Protocols](../domains/ai-protocols.md)

## En Bref

The **x402 Foundation** is now operational under open governance at the **Linux Foundation**,
and **Coinbase has completed its contribution** of the x402 protocol — an open standard for
payments over HTTP that lets AI agents, APIs, and applications send and receive money.
Stewardship moves from a single company to a neutral, community-governed body to avoid
vendor lock-in; this is the payment counterpart to A2A's parallel move to foundation
governance.[^x402]

## Points Clés

- **Governance shift:** control of x402 passes from Coinbase to the Linux Foundation-hosted x402 Foundation, community-governed and vendor-neutral.[^x402]
- **Purpose:** gives AI agents and automated systems a native, secure way to transact — a payment primitive they previously lacked at the protocol layer.[^x402]
- **Payment scope is broad:** supports multiple payment types, from traditional cards to stablecoins (Circle cites USDC; Ripple cites XRP/RLUSD).[^x402]
- **Membership:** ~40 organizations joined since the April 2026 intent-to-launch — premier members include AWS, Google, Stripe, Visa, Mastercard, Cloudflare, Circle, Shopify, American Express, Coinbase.[^x402]
- **Mechanics not detailed:** the release names the protocol but does not describe the HTTP 402 request/settle/retry flow — so x402's on-the-wire mechanics remain `NOT VERIFIED` here.

## Citation Notable

> "AI agents and automated systems are becoming active participants in the global economy." — Jim Zemlin, CEO, Linux Foundation

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-x402-foundation-launch-2026]] | describes | [[concept:x402]] |
| [[source:ai-protocols-x402-foundation-launch-2026]] | extends | [[domain:ai-protocols]] |
| [[source:ai-protocols-x402-foundation-launch-2026]] | mentions | [[organization:aws]] |

## Liens Wiki

- [x402](../concepts/x402.md) — this fiche confirms Coinbase's contribution and the move to x402 Foundation governance; broadens payment scope to cards + stablecoins.
- [AI Protocols](../domains/ai-protocols.md) — the agent-protocol cluster; x402 is its payment rail.
- [Amazon Web Services (AWS)](../organizations/aws.md) — a premier member of the x402 Foundation.

[^x402]: Linux Foundation press release, "Linux Foundation Announces Operational Launch of x402 Foundation", 2026-07-14 (updated 2026-10-01).
