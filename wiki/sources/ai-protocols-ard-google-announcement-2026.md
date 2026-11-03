---
type: source
title: "Announcing the Agentic Resource Discovery specification (Google Developers blog)"
description: Google (Junjie Bu & Srinivas Krishnan, 2026-06-17) launches ARD, an open spec for publishing, discovering and verifying AI capabilities across the web. It covers catalogs on the publisher's own domain, registries as search engines, a four-phase runtime demo, and Agent Registry in Gemini Enterprise Agent Platform.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
    id: ard-google-2026
    title: "Announcing the Agentic Resource Discovery specification"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-03T00:00:00Z}
verified: []
stale_after: 2027-05-03T00:00:00Z
updated: 2026-11-03
tags: [ard, discovery, google, agent-registry, ai-catalog, trust, registries, federation]
---

# Announcing the Agentic Resource Discovery specification (Google Developers blog)

**Auteurs :** Junjie Bu (Senior Staff Software Engineer) & Srinivas Krishnan (Distinguished Software Engineer), Google · **Publié :** 2026-06-17 · **Lien :** https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

Google launches **Agentic Resource Discovery (ARD)**, "an open specification for publishing,
discovering, and verifying AI capabilities across the web", developed with industry partners.
The post argues that the agentic web lacks a layer for **cross-organizational discovery plus
trust**. Platform registries exist, but each stays inside its own ecosystem. ARD standardizes
publishing under an organization's own domain and indexing across federated registries. It then
"steps out of the way" and the agent connects over the tool's native protocol.[^ard-google-2026]
The spec mechanics are on the [ARD concept page](../concepts/agentic-resource-discovery-ard.md).

## Points Clés

- **Three questions agents cannot answer today:** where the right capability lives, which one to
  use, and how to verify it is safe to connect to. The worked example is an operations agent in a
  live incident. It needs observability, documentation, deployment history and ticketing, and
  possibly specialized troubleshooting agents.[^ard-google-2026]
- **Two primitives.** *Catalogs* are hosted under the organization's domain, so "ownership of
  that domain serves as the cryptographic foundation for identity and trust". *Registries* are
  "search engines for the agentic web". They crawl catalogs, index them, and return matches
  together with the metadata needed to verify the publisher.[^ard-google-2026]
- **Four phases in the demo.** (1) The provider hosts an `ai-catalog.json` at a well-known path,
  listing MCP servers, A2A agents, OpenAPI tools or nested catalogs. (2) The client either sends
  a plain-language intent to a registry or fetches a known partner's catalog directly. (3) It
  verifies the publisher's cryptographic identity from attached trust metadata. (4) It connects
  directly over the native protocol or API.[^ard-google-2026] *Dated:* spec v0.91 (2026-08-26)
  renamed the path to `/.well-known/ard.json` (see the
  [concept page](../concepts/agentic-resource-discovery-ard.md)).
- **Google Cloud Agent Registry** (Gemini Enterprise Agent Platform) offers hosted search,
  discovery and hosting for agents, skills and MCP servers. Its governance features are globally
  unique namespaced URNs, agentic egress policies, and pinning of tools and specs. Agent Identity
  verifies the "trust manifest" for compliance such as HIPAA. Authenticated publisher onboarding
  is coming "soon". **Native ARD support was due "in the coming months"**, so it had not shipped
  when the post was published.[^ard-google-2026]
- **Lineage.** The spec is Apache 2.0 and "built upon the foundational AI Catalog data model".
  The post thanks the **AI Catalog Working Group under the Linux Foundation**.[^ard-google-2026]
  That is the working group's host, not ARD's: ARD has its own governance and no neutral host
  yet. ARD's ADR-0010 (2026-07-09) later chose a "loose coupling", and the interoperability page
  now calls the relationship "compatibility, not dependency". These points are sourced on the
  [concept page](../concepts/agentic-resource-discovery-ard.md).

## Citation Notable

> "What's missing is a standard way for agents to discover capabilities across organizational boundaries and establish trust in what they find." — Junjie Bu & Srinivas Krishnan

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-ard-google-announcement-2026]] | argues-that | [[concept:agentic-resource-discovery-ard]] |
| [[source:ai-protocols-ard-google-announcement-2026]] | enables | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-ard-google-announcement-2026]] | contrasts-with | [[concept:model-context-protocol-mcp]] |

## Liens Wiki

- [Agentic Resource Discovery (ARD)](../concepts/agentic-resource-discovery-ard.md): the canonical page for entry terms, search API, federation, trust binding, governance and the path drift.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) / [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md): native protocols that catalogs list and that the agent connects over after discovery.
- [Agent Plugins (Google blog) fiche](ai-protocols-agent-plugins-google-2026.md): a Google post from 2026-08-06 that places ARD as the "discover" layer above AI Catalog, Plugins and MCP/Skills.
- [ARD and AWS Agent Registry (AWS blog)](ai-protocols-ard-aws-agent-registry-2026.md): AWS's take. Note that its *AWS* Agent Registry is a different product from Google's.
- [ARD at Hugging Face (Hugging Face blog)](ai-protocols-ard-hugging-face-discover-2026.md): the other launch-day post, with a shipped reference implementation.
- [AI Protocols](../domains/ai-protocols.md): the cluster.

[^ard-google-2026]: Junjie Bu & Srinivas Krishnan, "Announcing the Agentic Resource Discovery specification", Google Developers Blog, 2026-06-17, consulted 2026-11-03 (page HTML fetched and read directly). The post's logo wall is an image and was not transcribed.
