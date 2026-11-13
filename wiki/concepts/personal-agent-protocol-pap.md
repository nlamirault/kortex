---
type: concept
title: Personal Agent Protocol (PAP)
description: Open, Apache-2.0 protocol ("Poppy") for how personal AI agents work with companies. It covers discovery at /.well-known/poppy.json, OAuth sign-in, a signed per-request Session header across APIs (OpenAPI/MCP), web browsing and company-agent conversations, and extensions. Announced on Sierra's blog (2026-10-06) as developed by Meta and Sierra; version 0.4 became the 1.0 release candidate on 2026-11-10.
resource: https://personalagentprotocol.org/
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://sierra.ai/blog/introducing-personal-agent-protocol
    id: sierra-pap-2026
    title: "Introducing Personal Agent Protocol (Sierra blog)"
  - resource: https://personalagentprotocol.org/
    id: pap-site
    title: "Personal Agent Protocol (official site home)"
  - resource: https://personalagentprotocol.org/docs/introduction
    id: pap-intro
    title: "Introduction: what it is, why it exists, principles"
  - resource: https://personalagentprotocol.org/docs/path-to-1
    id: pap-path-to-1
    title: "Path to 1.0 (status updated 2026-11-11; design partners)"
  - resource: https://personalagentprotocol.org/docs/roadmap
    id: pap-roadmap
    title: "Roadmap (areas expected before 1.0)"
  - resource: https://personalagentprotocol.org/docs/changelog
    id: pap-changelog
    title: "Changelog (0.1 on 2026-10-09 to 0.4 on 2026-11-10, draft 1.0)"
  - resource: https://personalagentprotocol.org/docs/1.0/spec
    id: pap-spec
    title: "Personal Agent Protocol specification (draft 1.0)"
  - resource: https://personalagentprotocol.org/docs/0.1/spec
    id: pap-spec-0-1
    title: "Personal Agent Protocol specification 0.1 (frozen), section 4 Sessions and authorization"
  - resource: https://personalagentprotocol.org/docs/1.0/extensions
    id: pap-extensions
    title: "Extensions (index)"
  - resource: https://personalagentprotocol.org/docs/1.0/guides
    id: pap-guides
    title: "Guides (draft 1.0), consent-page guidance only"
  - resource: https://personalagentprotocol.org/docs/demos
    id: pap-demos
    title: "Demos (community-built)"
  - resource: https://personalagentprotocol.org/license
    id: pap-license
    title: "License (Apache 2.0, names and logo excluded)"
  - resource: https://personalagentprotocol.org/license/contributions
    id: pap-contributions
    title: "Contribution and feedback terms"
  - resource: https://github.com/personal-agent-protocol/personal-agent-protocol
    id: pap-repo
    title: "personal-agent-protocol/personal-agent-protocol (GitHub repo and org metadata)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-13T13:09:17Z}
verified: []
stale_after: 2027-05-13T00:00:00Z
updated: 2026-11-13
tags: [pap, poppy, personal-agents, mcp, openapi, oauth, consent, identity, sessions, web-bot-auth, ucp]
---

# Personal Agent Protocol (PAP)

The Personal Agent Protocol, **"Poppy" for short**, is an open protocol for how personal agents
and companies work together. A company uses it to declare how personal agents can interact with
it. A personal agent uses it to sign in safely and get access to a person's account, "limited to
what that person and the company agree to".[^pap-intro] The launch post (2026-10-06, Bret Taylor
and Clay Bavor of Sierra) presented it as **an open standard Meta and Sierra are developing** with
industry partners. In that post it covers authentication, consumer control over what an agent may
access, and company visibility into agent activity, through a website, APIs or the company's own
agent.[^sierra-pap-2026] The official site, [personalagentprotocol.org](https://personalagentprotocol.org/),
publishes the spec and docs under Apache 2.0. As of 2026-11-11, **version 0.4 is the 1.0 release
candidate**.[^pap-site][^pap-path-to-1] The site frames who builds the protocol differently from
the launch post (see [Site vs. Sierra announcement](#site-vs-sierra-announcement-dated)).

## Problem

Personal agents today drive business websites the way people do, loading pages and clicking
forms, or they fall back to support lines and chat. That is slow and often fails, while a direct,
authenticated connection could complete the task securely in seconds.[^sierra-pap-2026]

The site calls today's situation **"all or nothing"**. Either the agent passes as the user,
signing in with their password and clicking through pages built for people, or the company blocks
it. The user can't limit what the agent does once it is in, and the company can't tell an agent
from a person. As agents do more, companies spend more effort detecting them and agents spend
more effort evading detection.[^pap-intro] PAP targets the points in between. In the site's
example, an airline might let any agent search flights, let signed-in agents see the user's
trips, and require the user's approval before buying a ticket.[^pap-intro]

## How It Works

- **Consumer-controlled access:** the consumer decides what access their agent gets, and the company sets limits. A guest session answers simple questions, and account tasks require sign-in with the read-only or write scope the customer chooses.[^sierra-pap-2026] In the spec, the company describes the scopes it offers in `poppy.json`, and the user approves some or all of the requested scopes on the company's page.[^pap-spec]
- **Sessions, separate from account access:** a Session belongs to one User, at one Company, through one Personal Agent. It ties together activity across APIs, conversations and browsing, signed in or out. The agent declares it with a `Poppy-Session` header, a JWT (`poppy-session+jwt`) that it signs for each request with a delegated key vouched for by a key in its `jwks_uri`. Account access is plain OAuth, and a signed-in request carries an access token as well as the Session header.[^pap-spec] The launch post said "the session is built on OAuth". That matched 0.1, and the two were split in 0.3 (see [the dated differences](#site-vs-sierra-announcement-dated)).[^sierra-pap-2026][^pap-changelog]
- **Routes to a business:** the company's website, its APIs, or the company's own agent for conversational tasks such as warranty claims. The company chooses which routes to offer.[^sierra-pap-2026] The spec defines two API types: `openapi` (an OpenAPI 3.0 or 3.1 description) and `mcp` (a remote MCP server on the Streamable HTTP transport, MCP 2025-06-18 or later). Conversations use PAP's own `poppy` conversation protocol, the only type defined so far.[^pap-spec]
- **Roadmap:** see [Roadmap](#roadmap) below.

## Specification Building Blocks (draft 1.0)

- **Discovery.** A company MUST publish `poppy.json` at `/.well-known/poppy.json` on its domain over HTTPS. The document identifies the organization and lists its APIs, website, company agent, sign-in options and extensions. Standard OAuth protected-resource and authorization-server metadata say where to sign in. Before using the document, the agent checks that `organization.domain` is the host that served it.[^pap-spec][^pap-site]
- **Agent identity.** An agent's `client_id` MUST be an HTTPS URL that returns its metadata document, following the OAuth Client ID Metadata Document (CIMD) draft. The agent authenticates with `private_key_jwt`.[^pap-spec]
- **Sign-in.** Direct Sign-In is the authorization code grant with PKCE, on the company's own page. Device Sign-In is the device authorization grant: the user signs in on another device, such as a phone. Since 0.4, Direct Sign-In is the preferred type.[^pap-spec][^pap-changelog] Mediated Sign-In, where the agent signs in with credentials the user gave it, is a **transitional extension**. The roadmap plans to remove it on a date set when 1.0 is published.[^pap-extensions][^pap-roadmap]
- **Pseudonymous users.** The agent gives each user a stable, opaque User ID per company. It MUST NOT contain or be derived from personal information, so companies can't match users with each other; these are pairwise subject identifiers, as in OIDC Core §8. An optional Agent ID tells apart several agents acting for one user.[^pap-spec]
- **Operator recognition.** Agents SHOULD also sign requests that carry the Session header with an HTTP Message Signature (RFC 9421) using **Web Bot Auth**, so traffic-management infrastructure can authenticate the operator. The spec calls this "compatibility support, not a replacement for the Session header or authorization".[^pap-spec]
- **Web browsing.** In browser join, the agent's browser gets a one-time code from the company, the agent authorizes the code, and the company sets its own cookie, so the access token never passes through the browser. A company can set `web.disabled` to ask agents not to browse.[^pap-spec]
- **Conversations.** Messages are text plus structured data. Both sides say whether a person or an AI is speaking: `author.type` is `human` only for the user's own words. The protocol supports handoff to a person, and Direct Conversations in which the user talks with the company directly.[^pap-spec][^pap-site]
- **Task coverage.** A company can list the tasks it chose not to offer, collect feedback on tasks an agent couldn't do, and publish a `skill_index` of skills in the Agent Skills format. The index follows a pinned revision of a *draft* Agent Skills discovery proposal, which the spec calls "not an adopted Agent Skills standard".[^pap-spec]
- **Extensions.** Extensions are optional and declared per request in a `Poppy-Extensions` header. Plain names are reserved for extensions defined on the site, and others are named with a domain (e.g. `example.com/gift-wrap`). Six are defined: `browser-control` v1, `disclosures` v1, `links` v1, `mediated-sign-in` v1 (transitional), `operations` v3, where the user, or the agent on the user's instruction, approves exact terms and retries never perform an action twice, and `ucp` v1, where shopping happens through the Universal Commerce Protocol.[^pap-extensions]
- **Versions.** Every request with the Session header names its version in `Poppy-Version`. Since 0.4 a company can serve several protocol versions through `supported_versions`.[^pap-changelog]

## Key Properties

- **Open standard** that anyone can implement. Per the launch post, Meta and Sierra develop it with partners.[^sierra-pap-2026] The site lists five principles: build on existing standards (OAuth, JWTs, HTTPS, OpenAPI, MCP) and define something new only where no standard covers the need; "controls, not policy"; secure and private; progressive adoption; extensible.[^pap-intro]
- **Built on MCP, OpenAPI and OAuth, not A2A.** The company-agent route uses PAP's own `poppy` conversation protocol, and agents skip conversation types they don't recognize.[^pap-spec] No site page read for this ingest mentions A2A, and neither does the launch post (text searched 2026-11-13).[^pap-site][^sierra-pap-2026] Contrast with [PACT](personal-agent-consent-trust-protocol-pact.md), which builds on A2A.
- **Company agent is one route among several**, not a mandatory hub.[^sierra-pap-2026]
- **Status:** 0.1 was published on 2026-10-09, 0.2 on 2026-10-24, 0.3 on 2026-11-04, and **0.4 on 2026-11-10 as the 1.0 release candidate**. Each version is frozen at its own URL.[^pap-changelog] Draft 1.0 starts from 0.4 and takes only fixes, which can still break compatibility: "We're not adding new features until 1.0 is published."[^pap-spec][^pap-path-to-1] The launch post had promised v0.1 "later this month", design workshops, and a reference implementation.[^sierra-pap-2026]
- **Implementations:** the Demos page says first-party demos are in development. Until they are ready, it lists three community demos that are "not officially reviewed or endorsed":[^pap-demos]
  - Cliffside Retail, with the in-browser Atlas demo agent (v0.4).
  - Poppy Demo Agent (`github.com/adewale/pda`, v0.3), which also offers a validator for a company's discovery and OAuth metadata.
  - Print with Poppy (`github.com/spenciefy/print-with-poppy`, v0.3), a real store whose orders are approved through Operations and paid on Stripe Checkout.

  The GitHub repo holds the documentation site: a Next.js app with `content/`, `kit/` and `skills/` directories. None of the pages read describe a first-party reference implementation.[^pap-repo]

## Roadmap

- **Launch post (2026-10-06):** more detailed permissions, push notifications (flight delays, shipments), and payments extensions so agents can buy without sharing card details.[^sierra-pap-2026]
- **Site (before 1.0; "direction, not dates or promises"):**[^pap-roadmap]
  - **Payments.** The UCP extension already handles carts, checkout and payment. How payment works with Operations is still open.
  - **Push notifications** and **attachments.** Neither is started in the spec.
  - **Signed approvals.** Today a company relies on the agent's word that the user approved.
  - **Self-hosted personal agents.** Desktop and phone apps are partly covered. Browser extensions are still open.
  - **Dropping Mediated Sign-In.**

## Governance and Licensing

- **License:** the spec and docs, examples included, are under **Apache 2.0**, with a patent license from contributors. The license does not cover the names "Personal Agent Protocol" and "Poppy", the logo, or the site design.[^pap-license] Contributions are licensed under Apache 2.0. Feedback grants "all other members and users of the protocol" a perpetual, royalty-free license.[^pap-contributions]
- **Process:** anyone can implement it and send feedback by opening an issue on GitHub. Each roadmap topic has a GitHub label.[^pap-path-to-1][^pap-roadmap] The repo is `personal-agent-protocol/personal-agent-protocol` (Apache-2.0). The GitHub org was created on 2026-10-13 and the repo on 2026-10-14.[^pap-repo]
- **No steward named:** no page read names a foundation, a working group or the authors. "The spec's authors are working through implementations with several of the design partners."[^pap-path-to-1]
- **Design partners** (listed as of 2026-11-11; "partners that have agreed to be listed"):[^pap-path-to-1]
  - *Personal agents:* Instinct, Meta, OpenAI.
  - *Companies:* Bank of America, BBVA, Chime, Cigna, Comcast, DIRECTV, FOX, Gap Inc., GEICO, Hertz, Insurify, Liberty Mutual, Nordstrom, PayPal/Venmo, Rocket, SiriusXM, Synchrony, Target, United Airlines, Walmart, Wells Fargo.
  - *Technology providers:* 1Password, Adyen, Atomic, Cloudflare, ElevenLabs, Genesys, Klaviyo, Mastercard, NiCE, Notion, Okta, OneSignal, Plaid, Shopify, Sierra, Stripe, Visa, Zapier, Zendesk.

## Site vs. Sierra announcement (dated)

The launch post predates the first spec by three days, so most differences are **dated drift**:
the newer, normative site supersedes the plan, as with ARD's path change. They are recorded here
and not escalated. The [Sierra fiche](../sources/sierra-personal-agent-protocol-2026.md) stays a
dated snapshot.

| Topic | Sierra launch post (2026-10-06)[^sierra-pap-2026] | Site (status 2026-11-11) | Reading |
|-------|-----------------------------------------------|---------------------------|---------|
| Who builds it | "an open standard Meta and Sierra are developing along with industry partners at Genesys, Instinct, Rocket, Shopify, Stripe, and Walmart" | No authors named. Meta is listed as a personal-agent design partner and Sierra as a technology provider, among 43 listed partners.[^pap-path-to-1] | Attribution drift, not a contradiction: the site never denies the post's account. |
| Session | "The session is built on OAuth" | A signed `Poppy-Session` JWT header, separate from OAuth account access.[^pap-spec] | Dated drift. In 0.1, Session Tokens *were* OAuth access tokens and Account Tokens were refresh tokens.[^pap-spec-0-1] 0.3 (2026-11-04) made the "Session header separate from OAuth" (Breaking).[^pap-changelog] |
| Sign-in | "sign in on the company's page or use credentials they have already set up with their personal agent" | Direct Sign-In preferred (0.4). Credential-based Mediated Sign-In is transitional and slated for removal.[^pap-changelog][^pap-roadmap] | Change of direction. |
| Spec | v0.1 "later this month" | 0.1 on 2026-10-09, then 0.4 as the release candidate on 2026-11-10.[^pap-changelog] | Delivered. |
| Reference implementation | "publish a reference implementation to help developers get started" | First-party demos are "being developed", and three community demos are listed.[^pap-demos] | Not yet delivered as of 2026-11-13. |
| Roadmap | More detailed permissions, push notifications, payments | Payments (UCP extension), push notifications, attachments, signed approvals, self-hosted agents, dropping Mediated Sign-In.[^pap-roadmap] | Expanded. "More detailed permissions" is not a named topic. |

The post itself now opens with an update: "On 10/9, we shared a draft of Personal Agent Protocol,
with 35 new design partners including Bank of America, OpenAI, Visa, and United
Airlines".[^sierra-pap-2026]

## Relation to PACT

PAP and [PACT](personal-agent-consent-trust-protocol-pact.md) are **parallel efforts announced on
the same day (2026-10-06)**. Both address the same problem, a personal agent acting on a user's
behalf at a business with consent, but they have different sponsors and technical bases:

- **PAP:** Meta and Sierra per the launch post; built on MCP, OpenAPI and OAuth.[^sierra-pap-2026][^pap-intro]
- **PACT:** Decagon and Instinct; built on A2A and OAuth/JWT.

**`PENDING — escalate to human`:** the Decagon PACT announcement says PACT is "joining the
Personal Agent Protocol working group, announced by the team behind Meta's Muse". The Sierra
post names **no working group** and says PAP is developed by **Meta and Sierra**. Its only "Muse"
mention is a quote from Rocket's CTO: "Our agentic technology, developed with Sierra, allows a
Muse agent to move across our platform".[^sierra-pap-2026] Two questions are unresolved across
the sources: whether PAP (this page) *is* the "Personal Agent Protocol working group" Decagon
refers to, and who owns "Muse".

The official site (2026-11-13) adds evidence but **does not resolve** either question:

- No page read mentions a working group.
- Instinct, PACT's co-developer, is listed as a PAP personal-agent design partner. Decagon is not
  listed, but the list covers only partners "that have agreed to be listed".[^pap-path-to-1]
- "Muse" appears only as the example personal-agent name in the guides' consent-page wording
  ("Muse wants to connect to your Example account").[^pap-guides] The site neither attributes it
  nor covers it with its "Companies in the examples are fictional" disclaimer, which applies to
  companies, not agents.[^pap-site] It does not settle who owns "Muse".

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:personal-agent-protocol-pap]] | builds-on | [[concept:model-context-protocol-mcp]] |
| [[concept:personal-agent-protocol-pap]] | part-of | [[domain:ai-protocols]] |
| [[concept:personal-agent-protocol-pap]] | contrasts-with | [[concept:personal-agent-consent-trust-protocol-pact]] |
| [[concept:personal-agent-protocol-pap]] | described-by | [[source:sierra-personal-agent-protocol-2026]] |
| [[concept:personal-agent-protocol-pap]] | described-by | [[source:ai-protocols-personal-agent-protocol-site-2026]] |

## Related

- [Personal Agent Protocol site fiche](../sources/ai-protocols-personal-agent-protocol-site-2026.md): the official site, with its version train, design partners and differences from the launch post.
- [Introducing Personal Agent Protocol (Sierra blog)](../sources/sierra-personal-agent-protocol-2026.md): the launch post.
- [Personal Agent Consent & Trust Protocol (PACT)](personal-agent-consent-trust-protocol-pact.md): the parallel effort on A2A, with the same problem but a different stack and sponsors.
- [Model Context Protocol (MCP)](model-context-protocol-mcp.md): one of PAP's two API types.
- [Agent Skills fiche](../sources/ai-protocols-agent-skills-overview-2026.md): the format a company's `skill_index` uses.
- [AI Protocols](../domains/ai-protocols.md): the agent-protocol cluster.

## Open Questions

- Is PAP the same effort as the "Personal Agent Protocol working group" Decagon is joining, or a competing standard with the same name? (`PENDING` above.)
- Do PAP (MCP/OpenAPI) and PACT (A2A) converge, coexist or compete as the standard between personal agents and businesses?
- Who owns "Muse": Meta (per Decagon), or Rocket working with Sierra, as the Rocket quote in the Sierra post can be read?
- Who are "the spec's authors", and will PAP move to a neutral host before or after 1.0?
- When does 1.0 ship, and on what date is Mediated Sign-In removed? The roadmap ties the removal date to the 1.0 publication.

[^sierra-pap-2026]: Bret Taylor & Clay Bavor, "Introducing Personal Agent Protocol", Sierra blog, 2026-10-06. First consulted 2026-10-08 and re-read 2026-11-13, when it opened with an "Update: On 10/9 …" banner linking to https://sierra.ai/blog/poppy, which was not read.
[^pap-site]: personalagentprotocol.org (home page), consulted 2026-11-13 (page HTML fetched and read directly). The page is undated, and its footer says "Companies in the examples are fictional."
[^pap-intro]: "Introduction", https://personalagentprotocol.org/docs/introduction, consulted 2026-11-13 (undated page).
[^pap-path-to-1]: "Path to 1.0", https://personalagentprotocol.org/docs/path-to-1, "Current status, updated November 11, 2026", consulted 2026-11-13. The 43-partner total and the 3/21/19 split come from counting the list.
[^pap-roadmap]: "Roadmap", https://personalagentprotocol.org/docs/roadmap, consulted 2026-11-13 (undated page).
[^pap-changelog]: "Changelog", https://personalagentprotocol.org/docs/changelog, consulted 2026-11-13. The relevant entries are the publication line for each version, the 0.3 entries "OAuth and Sessions sections" and "Session header separate from OAuth", and the 0.4 entries "Direct Sign-In preferred" and "Several protocol versions".
[^pap-spec]: "Personal Agent Protocol specification (draft 1.0)", https://personalagentprotocol.org/docs/1.0/spec, consulted 2026-11-13. Sections used: 1.1, 3, 4.1–4.3, 4.8, 5, 5.1–5.3, 6, 7, 8.1, 8.8–8.10 and 9.4.
[^pap-spec-0-1]: "Personal Agent Protocol specification 0.1" (frozen), https://personalagentprotocol.org/docs/0.1/spec, section 4 "Sessions and authorization", consulted 2026-11-13.
[^pap-extensions]: "Extensions", https://personalagentprotocol.org/docs/1.0/extensions, consulted 2026-11-13. Only the index table was read, not the individual extension pages.
[^pap-guides]: "Guides" (draft 1.0), https://personalagentprotocol.org/docs/1.0/guides, consulted 2026-11-13. Only the consent-page guidance that mentions "Muse" was read.
[^pap-demos]: "Demos", https://personalagentprotocol.org/docs/demos, consulted 2026-11-13.
[^pap-license]: "License", https://personalagentprotocol.org/license, consulted 2026-11-13.
[^pap-contributions]: "Contributions", https://personalagentprotocol.org/license/contributions, consulted 2026-11-13.
[^pap-repo]: https://github.com/personal-agent-protocol/personal-agent-protocol, consulted 2026-11-13 through the GitHub API: repo metadata (Apache-2.0, created 2026-10-14, last push 2026-11-11), org metadata (created 2026-10-13) and the top-level directory listing. That the repo holds the documentation site is inferred from the listing (`app/`, `components/`, `content/`, `next.config.ts`) and the repo's `homepage` field.
