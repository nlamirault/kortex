---
title: Personal Agent
type: concept
status: active
confidence: medium
cluster: ai
domain: [ai]
sources: [https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact]
updated: 2026-10-07
tags: [AI, Agents]
generated: {by: claude-opus-4-8, at: 2026-10-07}
verified: []
stale_after: 2027-04-07
---

# Personal Agent

An AI agent that acts **on an individual customer's behalf** across many businesses — booking travel, managing purchases, resolving support issues — as the customer's delegated representative, as opposed to a business agent that represents a company.

## Core Idea

A personal agent is the user-side counterpart to a business's AI agent. Named examples include Meta's **Muse**, **Instinct**, and **dots**. The defining challenge is interoperability and trust: a personal agent must work *across* businesses, and a business must be willing to serve requests from *different* personal-agent platforms — ideally without the customer's choice of agent depending on which provider a given business runs.

That cross-party trust is exactly what [PACT](personal-agent-consent-trust-protocol-pact.md) standardizes: a personal agent proves its identity and carries a scoped, customer-approved delegation, while never touching the customer's login credentials.

## Key Properties

- **Acts for one customer** across many businesses (delegated authority).
- **Platform-diverse** — many competing personal-agent platforms (Muse, Instinct, dots).
- **Needs verifiable consent** to act on a customer's account at a business.
- **Should stay out of the credential path** — authenticates the user via the business, not by holding passwords.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent]] | used-by | [[organization:meta]] |
| [[concept:personal-agent]] | used-by | [[organization:instinct]] |
| [[concept:personal-agent]] | requires | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[concept:personal-agent]] | contrasts-with | [[concept:agent-harness]] |

## Related

- [PACT](personal-agent-consent-trust-protocol-pact.md) — consent/trust protocol for personal↔business agent interaction
- [AI / Protocols](ai-protocols.md)
- [PACT source: Decagon, 2026](../sources/decagon-pact-2026.md)

## Open Questions

- Formal definition / scope boundary vs. general assistant agents. `NOT VERIFIED`
