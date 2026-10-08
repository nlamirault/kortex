---
type: source
title: "PACT Protocol Home (openpactprotocol.org)"
description: The PACT specification home — defines the User/Personal-agent/Brand/Provider roles and the registration → discovery → signed-request → consent → delegation flow, built on A2A 1.0.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://openpactprotocol.org/
    id: openpact-site-2026
    title: "PACT protocol home (openpactprotocol.org)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [pact, spec, a2a, jwt, jwks, delegation, consent]
---

# PACT Protocol Home (openpactprotocol.org)

**Éditeur :** openpactprotocol.org (project site) · **Consulté :** 2026-10-08 · **Lien :** https://openpactprotocol.org/
**Domaine :** [AI Protocols](../domains/ai-protocols.md)

## En Bref

The project site names the protocol **PACT** ("OpenPACT" is only the domain). PACT lets a
personal agent contact a Brand's support agent with a **verifiable identity** and act only
within the permissions the User granted. It is **built on A2A 1.0 and leaves everything A2A
defines unchanged**, solving two gaps: the Brand can't identify the calling agent, and the
agent can't act on the person's account without their password.[^openpact]

## Points Clés

- **Four roles:** User (person/principal), Personal agent (platform acting for them), Brand (business), Provider (hosts support agents for many Brands). Register once per Provider → reach every Brand it hosts.[^openpact]
- **Registration:** the agent gives the Provider its issuer URL + public keys (JWKS), receives an `audience` string.[^openpact]
- **Discovery:** fetch the Brand's Agent Card (message endpoint + delegation scopes like `orders:read`, `orders:cancel`) via a well-known URL, link, or registry.[^openpact]
- **Signed requests:** short-lived JWT carrying a stable, anonymous User id, verified against JWKS; the Brand returns a `contextId` to continue the conversation.[^openpact]
- **Consent + delegation:** User signs in on the Brand's own login page, approving each scope separately; the agent gets a scoped, short-lived token naming User + agent + Brand + scopes. (The site does **not** name OAuth; the Decagon announcement does.)[^openpact]

## Citation Notable

> PACT "lets a personal agent contact a Brand's support agent with a verifiable identity" and only with the permissions the User granted.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:openpactprotocol-pact-spec-2026]] | specifies | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[source:openpactprotocol-pact-spec-2026]] | builds-on | [[concept:agent2agent-a2a]] |
| [[source:openpactprotocol-pact-spec-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md) — the concept this site specifies.
- [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md) — the unchanged base protocol PACT layers on.
- [AI Protocols](../domains/ai-protocols.md) — the cluster this protocol belongs to.

[^openpact]: openpactprotocol.org, PACT protocol home page, consulted 2026-10-08.
