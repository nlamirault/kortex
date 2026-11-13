---
type: source
title: "Personal Agent Protocol (personalagentprotocol.org)"
description: The official Personal Agent Protocol ("Poppy") site — an open, Apache-2.0 protocol for how personal agents and companies work together (discovery at /.well-known/poppy.json, OAuth sign-in, one Session across APIs, web and company-agent conversations, extensions); version 0.4 is the 1.0 release candidate (2026-11-10), with 43 listed design partners.
resource: https://personalagentprotocol.org/
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://personalagentprotocol.org/
    id: pap-site
    title: "Personal Agent Protocol (official site home)"
  - resource: https://personalagentprotocol.org/docs/path-to-1
    id: pap-path-to-1
    title: "Path to 1.0 (status updated 2026-11-11; design partners)"
  - resource: https://personalagentprotocol.org/docs/changelog
    id: pap-changelog
    title: "Changelog (0.1 to 0.4, draft 1.0)"
  - resource: https://personalagentprotocol.org/docs/demos
    id: pap-demos
    title: "Demos (community-built)"
  - resource: https://sierra.ai/blog/introducing-personal-agent-protocol
    id: sierra-pap-2026
    title: "Introducing Personal Agent Protocol (Sierra blog, re-read for its 10/9 update banner)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:09:17Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [pap, poppy, personal-agents, oauth, mcp, openapi, sessions, extensions, ucp]
---

# Personal Agent Protocol (personalagentprotocol.org)

**Auteurs :** "the spec's authors" (not named on any page read) · **Publié :** v0.4 on 2026-11-10; Path to 1.0 status updated 2026-11-11 · **Lien :** https://personalagentprotocol.org/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min (landing page; the spec is much longer)

## En Bref

The official home of the **Personal Agent Protocol**, "Poppy" for short: "an open protocol for
every company and every personal agent".[^pap-site] It argues that agent access to a company is
**all or nothing** today, and offers a range of choices in between: the company decides what
agents can do, and the user decides what their own agent can do for them. The spec and docs are
Apache 2.0. **Version 0.4 is the 1.0 release candidate**, and the authors are taking it to 1.0
with design partners.[^pap-site] The spec mechanics are on the
[PAP concept page](../concepts/personal-agent-protocol-pap.md).

## Points Clés

- **Building blocks.** Discovery uses a document at `/.well-known/poppy.json` plus standard OAuth
  metadata. The user signs in on the company's own page through OAuth. One Session covers API
  calls, conversations and browsing: the agent signs a header on each request with a short-lived
  key, naming the session and a user ID that differs at each company.[^pap-site]
- **The company picks the interfaces.** It can offer OpenAPI, MCP or web pages, plus an optional
  company agent, and each API keeps its own schema. Extensions already add approval of exact
  terms, links and disclosures in messages, and checkout through UCP.[^pap-site]
- **Fast version train.** 0.1 was published on 2026-10-09 as "the first published draft", 0.2 on
  2026-10-24, 0.3 on 2026-11-04 and 0.4 on 2026-11-10 as the release candidate.[^pap-changelog]
  Draft 1.0 takes fixes only: "We're not adding new features until 1.0 is
  published."[^pap-path-to-1]
- **Design partners**, listed alphabetically among those "that have agreed to be listed". There
  are 3 personal agents (Instinct, Meta, OpenAI), 21 companies (Bank of America to Wells Fargo)
  and 19 technology providers, among them Sierra, Stripe, Visa, Okta and Cloudflare. Feedback goes
  through GitHub issues.[^pap-path-to-1]
- **Where it differs from the Sierra launch post (2026-10-06).** No author is named, and Meta and
  Sierra appear as design partners rather than being named as the developers.[^pap-path-to-1] The Session is no
  longer "built on OAuth": 0.3 separated the two.[^pap-changelog] There is no first-party
  reference implementation yet, only community demos.[^pap-demos] The Sierra post now opens with a
  10/9 update: "we shared a draft of Personal Agent Protocol, with 35 new design
  partners".[^sierra-pap-2026] Dates and details are in
  [PAP → Site vs. Sierra announcement](../concepts/personal-agent-protocol-pap.md#site-vs-sierra-announcement-dated).

## Citation Notable

> "Today it is all or nothing: the company blocks the agent, or the agent signs in as the person and can do anything they can." — personalagentprotocol.org

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-personal-agent-protocol-site-2026]] | argues-that | [[concept:personal-agent-protocol-pap]] |
| [[source:ai-protocols-personal-agent-protocol-site-2026]] | extends | [[source:sierra-personal-agent-protocol-2026]] |
| [[source:ai-protocols-personal-agent-protocol-site-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Personal Agent Protocol (PAP)](../concepts/personal-agent-protocol-pap.md): the canonical page for the spec building blocks, versions, governance and the dated differences from the launch post.
- [Introducing Personal Agent Protocol (Sierra blog)](sierra-personal-agent-protocol-2026.md): the 2026-10-06 launch post. This site delivers its promised v0.1 and goes well past it.
- [Personal Agent Consent & Trust Protocol (PACT)](../concepts/personal-agent-consent-trust-protocol-pact.md): its co-developer Instinct is listed as a PAP personal-agent design partner. The working-group question stays `PENDING`.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md): one of the API types a company can list.
- [Agent Skills fiche](ai-protocols-agent-skills-overview-2026.md): the spec's `skill_index` uses the Agent Skills format (see the concept page).
- [AI Protocols](../domains/ai-protocols.md): the cluster.

[^pap-site]: personalagentprotocol.org (home page), consulted 2026-11-13 (page HTML fetched and read directly). The page is undated, and its footer says "Companies in the examples are fictional."
[^pap-path-to-1]: "Path to 1.0", https://personalagentprotocol.org/docs/path-to-1, "Current status, updated November 11, 2026", consulted 2026-11-13. The partner counts (3/21/19) come from counting the list.
[^pap-changelog]: "Changelog", https://personalagentprotocol.org/docs/changelog, consulted 2026-11-13. The relevant entries are the publication line for each version and the 0.3 entry "Session header separate from OAuth" (Breaking).
[^pap-demos]: "Demos", https://personalagentprotocol.org/docs/demos, consulted 2026-11-13. The page says that first-party demos are in development, and that the listed demos "have not been officially reviewed or endorsed".
[^sierra-pap-2026]: Bret Taylor & Clay Bavor, "Introducing Personal Agent Protocol", Sierra blog, 2026-10-06, re-read 2026-11-13. The "Update: On 10/9 …" banner links to https://sierra.ai/blog/poppy, which was not read for this ingest.
