---
type: concept
title: Agentic Resource Discovery (ARD)
description: Open, Apache-2.0 discovery protocol (spec v0.91, status Proposal) that lets an AI client search federated registries for agents, MCP servers, Skills, Plugins and APIs before invoking them over their own protocol; publishers host domain-anchored entries at /.well-known/ard.json.
resource: https://github.com/ards-project/ard-spec
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agenticresourcediscovery.org/
    id: ard-site
    title: "Agentic Resource Discovery Specification (project site home)"
  - resource: https://agenticresourcediscovery.org/spec/
    id: ard-spec
    title: "ARD Specification v0.91 (status: Proposal, 2026-08-26)"
  - resource: https://agenticresourcediscovery.org/interoperability/
    id: ard-interop
    title: "ARD Interoperability (FAQ page)"
  - resource: https://agenticresourcediscovery.org/governance/
    id: ard-governance
    title: "ARD Governance"
  - resource: https://github.com/ards-project/ard-spec
    id: ard-repo
    title: "ards-project/ard-spec (GitHub repo: metadata, spec/ard.md header, ADR-0008, ADR-0010)"
  - resource: https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
    id: ard-google-2026
    title: "Announcing the Agentic Resource Discovery specification (Google Developers Blog)"
  - resource: https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
    id: ard-aws-2026
    title: "Agentic Resource Discovery (ARD): An open specification for agent discovery (AWS blog)"
  - resource: https://huggingface.co/blog/agentic-resource-discovery-launch
    id: ard-hf-2026
    title: "Agentic Resource Discovery: Let agents search for tools, skills, and other agents (Hugging Face blog)"
  - resource: https://www.agentready.org
    id: agentready-2026
    title: "AgentReady v2.0 (October 2026), AR-FIND-04 AI Catalog practice"
  - resource: https://huggingface.co/.well-known/ai-catalog.json
    id: hf-catalog-probe
    title: "Hugging Face ai-catalog.json (live HTTP probe, 2026-11-03)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-03T00:00:00Z}
verified: []
stale_after: 2027-05-03T00:00:00Z
updated: 2026-11-03
tags: [ard, discovery, registry, federation, ai-catalog, mcp, a2a, agent-skills, agent-plugins, trust, search]
---

# Agentic Resource Discovery (ARD)

Agentic Resource Discovery (ARD) is an **open discovery protocol for agentic resources**,
licensed Apache 2.0. An AI client asks "What is available for this task?" and a discovery
service answers with matching resources. ARD **sits entirely before invocation**: it helps the
client find a resource, which is then invoked through its own native mechanism.[^ard-site] The
spec, schemas, decision records (ADRs) and conformance tool live in
[`ards-project/ard-spec`](https://github.com/ards-project/ard-spec).[^ard-repo]

## Core Idea

The problem is the **install-first model**. Users or developers "install" or hardcode each agent
before use, and most LLMs pick tools by loading every description into the context window,
which does not scale to thousands or millions of capabilities. ARD moves selection **out of the
LLM into a dedicated search service**. That service can rank on richer signals (representative
queries, publisher identity, compliance metadata, usage patterns) without spending
context-window tokens.[^ard-spec] Google frames the gap as three questions: where the right
capability lives, which one to use, and how to verify it is safe to connect to. Existing
platform registries answer them only inside their own ecosystem, "fragmented and
siloed".[^ard-google-2026]

Discovery runs in **two layers**. In *static discovery*, a publisher describes its resources on
its own domain. In *dynamic discovery*, registries crawl those descriptions and expose a
mandatory HTTP REST search API.[^ard-spec] Google calls the two primitives **catalogs** and
**registries**. Catalogs live under the organization's domain, so domain ownership is the trust
anchor. Registries are "search engines for the agentic web".[^ard-google-2026] AWS compares the
resulting federation to how DNS resolves names across networks.[^ard-aws-2026]

ARD is an **envelope, not a runtime**. It is not MCP, A2A, Skills, AI Catalog or an API runtime,
and it replaces none of them. It is also **not a central catalog**: many discovery services are
expected, each with its own trust, ranking and access policy, and every enterprise can run its
own.[^ard-site] The interoperability page says existing registries, plugin directories and tool
catalogs "become ARD discovery services". It also treats a client's built-in tool search as a
scoped form of the same idea. The two compose: an ARD service can produce a policy-filtered
toolbox that the client's own tool search then ranks over.[^ard-interop]

## Key Properties

**The ARD entry (spec v0.91).** An entry is a JSON-LD node. Its base context is served at
`https://agenticresourcediscovery.org/context/v1`. A publisher MAY add namespaced terms through
`@context`, and those terms become search filters with no change to the spec.[^ard-spec]

| Term | Requirement | Notes |
|------|-------------|-------|
| `identifier` | MUST | Domain-anchored URN `urn:air:<publisher>:[<namespace>:]<agent-name>`, where `<publisher>` is an FQDN |
| `displayName` | MUST | Human-readable name |
| `type` | MUST | Artifact type as an IANA media type |
| `url` or `data` | MUST, exactly one | Reference to the artifact document, or the document inline |
| `representativeQueries` | SHOULD (2–5) | The search signal. Without it the entry cannot be found; conformance tooling warns rather than fails |
| `capabilities` | MAY | Short tool tokens (e.g. `WeatherTool`) for fast structured filtering |
| `description`, `tags`, `version`, `updatedAt`, `metadata`, `trustManifest` | optional | Descriptive terms; `trustManifest` carries identity and attestations |

"Every ARD entry is a well-formed catalog entry, but not every catalog entry is an ARD entry."
The difference is the discovery terms, chiefly `representativeQueries`.[^ard-spec]

- **Artifact-agnostic media types.** `type` is an open media-type string. The recognized types
  are `application/mcp-server-card+json`, `application/a2a-agent-card+json`,
  `application/agent-card+json`, `application/agent-skills+json`, `application/agent-skills+md`,
  `application/agent-skills+zip`/`+gzip`, `application/agent-plugins+zip`/`+gzip`,
  `application/ai-registry+json` (a registry) and `application/ai-catalog+json` (a nested
  catalog). IANA registration is still pending.[^ard-spec]
- **Five publishing mechanisms.** A manifest (`{"entries": [...]}`) at
  `https://{domain}/.well-known/ard.json`, in-page JSON-LD markup, an `Agentmap:` directive in
  `robots.txt`, `<link rel="ard">`, or DNS Service Binding records
  (`_entries._agents.example.com`, `_search._agents.example.com`). A consumer MUST fetch
  `ard.json` and honour `rel="ard"`. Web ingestion is the only pipeline every registry MUST
  support; git, npm and OCI scanning are optional.[^ard-spec]
- **Search API.** `POST /search` takes `query.text` (required), `query.filter` (OR within a
  key, AND across keys), `federation`, `pageSize` (default 10, max 100) and `pageToken`. Each
  result carries a `score` from 0 to 100 and a `source`. `POST /explore` returns facet counts
  and does not federate. `GET /agents` is a deterministic list. Both are optional. Clients find a
  registry's base URL from an entry of type `application/ai-registry+json`. A registry MAY also
  expose search as an MCP tool or an A2A skill, but REST is the floor.[^ard-spec]
- **Federation modes.** `auto` (default) merges upstream results, `referrals` returns results
  plus other registries for the client to follow, and `none` searches only the local index. The
  client chooses the topology.[^ard-spec]
- **Trust that is not tied to one framework.** `trustManifest` is optional. ARD reads only
  `trustManifest.identity`, so SPIFFE, a DID method or an enterprise PKI all fit. The one hard
  rule is **publisher-authority binding**: the identity's trust domain MUST match the URN's
  `<publisher>`. That is the defense against namespace squatting: an entry claiming
  `urn:air:google.com:…` is rejected unless it carries an attestation issued by google.com. ARD
  defines no signing procedure of its own; it defers to the declared `trustSchema`. Attestations
  cover organizational compliance (SOC2-Type2, HIPAA-Audit), SARIF scans, SLSA or in-toto
  provenance, SCITT/ANS receipts and runtime evaluations.[^ard-spec]
- **Relevance is not trust.** The search `score` "MUST NOT be interpreted as a trust,
  compliance, or safety judgment". Authentication belongs to the artifact's own protocol, and
  distribution (OCI, npm) is out of scope.[^ard-spec]
- **Conformance tooling.** The repo ships a JSON Schema 2020-12 for entries and manifests
  (`additionalProperties: true` by design), a CDDL grammar, an OpenAPI 3.1.0 file for the
  registry API, and a zero-dependency `conformance-test` CLI with manifest, publisher and
  registry modes.[^ard-spec] `spec/schemas/` still holds the older `ai-catalog.schema.json` next
  to `ard-entry.schema.json`, and `adr/` holds 10 ADRs.[^ard-repo]
- **No releases yet.** As of 2026-11-03 the repo (created 2026-05-19, Apache-2.0) has no tags or
  GitHub releases. `spec/ard.md` on `main` is still headed v0.91 (Proposal, 2026-08-26), although
  later changes were merged, the most recent push being 2026-10-25. Cite the spec by commit or
  date, not just by version.[^ard-repo]

## Governance

- **Who builds it.** The home page says "a working group with participants from Microsoft,
  Google, Hugging Face, GoDaddy, and others". Its logo wall shows Cisco, Databricks, GitHub,
  GoDaddy, Google, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow and
  Snowflake.[^ard-site] The spec v0.91 authors are Junjie Bu (Google), R.V. Guha and Shaun Smith
  (Hugging Face). Its acknowledgements also list Amazon Web Services but not
  ServiceNow.[^ard-spec] AWS says it "contributed feedback".[^ard-aws-2026] These lists differ
  by page and are kept separate here.
- **Two bodies.** The **Oversight Board** sets direction. It has 4 to 7 members, at most one per
  company, and a company needs a shipping product to qualify; seats cannot be bought. Its
  members are Google (Junjie Bu), Hugging Face (Shaun Smith), Microsoft (Dhruv Chand), Amazon
  (Jeffrey Damick) and Cisco (Luca Muscariello). The **Maintainers** own the spec. They have 5
  to 7 members, at least 2 of them independent, and decide spec changes by majority vote. They
  are R.V. Guha (Chair, at large), Nick Cooper (at large), Junjie Bu, Shaun Smith and Dhruv
  Chand. Term lengths, quorum and how new companies join are "still to be
  decided".[^ard-governance]
- **No neutral host yet.** "Whether to sit ARD under a neutral host — W3C, an AI foundation, or
  similar — is a decision for roughly twelve months out."[^ard-governance] *Editorial:* MCP, A2A,
  AGENTS.md and Agent Skills all sit under the
  [Agentic AI Foundation](../organizations/agentic-ai-foundation.md); ARD does not. The Linux
  Foundation in Google's acknowledgements belongs to the **AI Catalog Working Group**, not to
  ARD.[^ard-google-2026]

## Spec Drift: AI Catalog Path to `ard.json` (dated)

The launch posts and the current spec name different well-known paths and describe the AI
Catalog relationship differently. The project explains both changes itself: ADR-0010 records the
decision to loosen the AI Catalog coupling, and the spec calls the old path its "predecessor". The
table records each claim with its date. This is noted, not escalated.

| Date | Source | What it says |
|------|--------|--------------|
| 2026-06-17 | Google blog | Providers host `ai-catalog.json` at a well-known path. ARD "is built upon the foundational AI Catalog data model".[^ard-google-2026] |
| 2026-06-17 | Hugging Face blog | A "draft" spec. The static manifest is `ai-catalog.json`, the registry API is `POST /search`, and HF publishes at `/.well-known/ai-catalog.json`.[^ard-hf-2026] |
| 2026-07-09 | ADR-0010 (repo) | "Loose coupling" with AI Catalog, decided with the `ai-catalog` working group. `ai-catalog` is a publishing format that should carry only the provider's data, while ARD is a discovery format that aggregates signals from many sources. An ARD entry is "the `ai-catalog` entry core plus flat, namespaced extensions".[^ard-repo] |
| 2026-08-26 | Spec v0.91 (Proposal) | Publishers use `/.well-known/ard.json` and `rel="ard"`. `ai-catalog.json` and the `ai-catalog` link relation are the "predecessor" names, which consumers MAY consult. "A resource that remains only at `/.well-known/ai-catalog.json` may not be found." The entry schema "does not derive from any catalog schema".[^ard-spec] |
| 2026-10 (v2.0) | AgentReady | AR-FIND-04 (MAY) tells publishers to put an AI Catalog at `/.well-known/ai-catalog.json` and link it with `rel="ai-catalog"`. It calls ARD "the registry layer on top", where a registry such as Ora Directory indexes published catalogs. This guidance is newer than v0.91 but uses the predecessor names.[^agentready-2026] |
| consulted 2026-11-03 | Interoperability page | "Compatibility, not dependency": as of AI Catalog v0.9-RC, one document can satisfy both formats. An ARD service MAY ingest an AI Catalog document directly. Where both files list the same identifier, `ard.json` wins.[^ard-interop] |
| probed 2026-11-03 | huggingface.co | `/.well-known/ai-catalog.json` returns 200 (`application/ai-catalog+json`, `specVersion: "1.0"`, 2 entries: the Discover registry and the Hub MCP server card, neither with `representativeQueries`). `/.well-known/ard.json` returns 401.[^hf-catalog-probe] |

*Reading:* a consumer that only reads `ard.json` is fully conformant to v0.91. Today it would not
find the catalog of one of the spec's own authoring organizations. Both HF entries also lack
`representativeQueries`, which v0.91 tooling flags as a warning. AgentReady and ARD v0.91 give
publishers different advice: `ai-catalog.json` versus `ard.json`. They do not contradict each
other on facts, because the interoperability page lets a publisher serve both files with
`ard.json` taking precedence. Serving both is the safe choice until consumers settle on one
path.

## Implementations (as stated by each source)

- **Hugging Face Discover (`hf-discover`).** Shipped as a reference implementation. It searches
  Skills, ML applications and MCP servers through the `hf` CLI, a REST `/search` endpoint and an
  MCP endpoint. See the [Hugging Face fiche](../sources/ai-protocols-ard-hugging-face-discover-2026.md).[^ard-hf-2026]
- **Google Cloud Agent Registry** (Gemini Enterprise Agent Platform). A hosted registry for
  agents, skills and MCP servers. Native ARD support was due "in the coming months" as of
  2026-06-17. See the [Google fiche](../sources/ai-protocols-ard-google-announcement-2026.md).[^ard-google-2026]
- **AWS Agent Registry** (preview). A different product with the same name. AWS says it
  *expects* ARD to complement the registry as the interoperability layer, but does not claim
  that the registry implements ARD. See the [AWS fiche](../sources/ai-protocols-ard-aws-agent-registry-2026.md).[^ard-aws-2026]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agentic-resource-discovery-ard]] | part-of | [[domain:ai-protocols]] |
| [[concept:agentic-resource-discovery-ard]] | enables | [[concept:tool-use-function-calling]] |
| [[concept:agentic-resource-discovery-ard]] | contrasts-with | [[concept:model-context-protocol-mcp]] |
| [[concept:agentic-resource-discovery-ard]] | contrasts-with | [[concept:agent2agent-a2a]] |
| [[concept:agentic-resource-discovery-ard]] | enables | [[concept:agent-plugins]] |

## Related

- [AI Protocols](../domains/ai-protocols.md): the cluster.
- [Announcing the ARD specification (Google blog)](../sources/ai-protocols-ard-google-announcement-2026.md): the launch post, covering catalogs and registries, the four demo phases and Google Cloud Agent Registry.
- [ARD and AWS Agent Registry (AWS blog)](../sources/ai-protocols-ard-aws-agent-registry-2026.md): the multi-environment case, the DNS analogy, and federation without migration.
- [ARD at Hugging Face (Hugging Face blog)](../sources/ai-protocols-ard-hugging-face-discover-2026.md): the install-first problem and the `hf-discover` reference implementation.
- [Model Context Protocol (MCP)](model-context-protocol-mcp.md): the execution protocol behind `application/mcp-server-card+json` entries. ARD finds the server and MCP invokes it.
- [Agent2Agent (A2A)](agent2agent-a2a.md): A2A Agent Cards are a recognized entry type (`application/a2a-agent-card+json`).
- [Agent Plugins](agent-plugins.md): packaged plugin archives are a recognized type, matching the Plugins stack's "discover via ARD" layer.
- [Agent Skills fiche](../sources/ai-protocols-agent-skills-overview-2026.md): Skills are indexed as `application/agent-skills+md`, `+json` and `+zip`.
- [Tool Use / Function Calling](tool-use-function-calling.md): ARD moves tool *selection* out of the context window.
- [AgentReady fiche](../sources/ai-protocols-agentready-standard-2026.md): recommends an AI Catalog at `/.well-known/ai-catalog.json` (AR-FIND-04, MAY) with ARD as "the registry layer on top". ARD v0.91 calls that path its predecessor.
- [Amazon Web Services (AWS)](../organizations/aws.md): holds an Oversight Board seat (Jeffrey Damick) and publishes the AWS post.

## Open Questions

- When will publishers on `ai-catalog.json`, Hugging Face included, move to `ard.json`? Will
  major consumers keep reading the predecessor path?
- Will Google Cloud Agent Registry and AWS Agent Registry ship native ARD search and federation,
  and which `federation` mode will they default to?
- Which trust framework becomes the de-facto `trustSchema`? The spec says only that "a future ARD
  profile MAY pin a concrete default scheme".
- Will ARD take a neutral host (W3C, an AI foundation)? The governance page puts the decision
  about twelve months out but is itself undated.
- Is the `okf:` namespace in the spec's query example (`https://openknowledgeformat.org/ns#`) the
  same Open Knowledge Format this bundle conforms to? The spec does not say. ADR-0010's example
  also uses a `text/vnd.okf+markdown` type for a Treasury data entry.
- Which "ACP" does the interoperability page mean by "ACP's Agent Registry" for "editor-context
  agents"? It is not evidently the wiki's
  [Agent Communication Protocol](agent-communication-protocol-acp.md) (IBM/BeeAI lineage).
  NOT VERIFIED.

[^ard-site]: agenticresourcediscovery.org (home page), consulted 2026-11-03. The contributor list is from the logo image's alt text.
[^ard-spec]: "Agentic Resource Discovery Specification: Federated Discovery and Search for Agentic Resources", v0.91, status Proposal, dated 2026-08-26, by Junjie Bu (Google), R.V. Guha and Shaun Smith (Hugging Face). https://agenticresourcediscovery.org/spec/, consulted 2026-11-03. Repo: github.com/ards-project/ard-spec.
[^ard-repo]: https://github.com/ards-project/ard-spec, consulted 2026-11-03 via the GitHub API: repo metadata (Apache-2.0, created 2026-05-19, last push 2026-10-25, no tags or releases); `spec/` and `spec/schemas/` listings; the `spec/ard.md` header; ADR-0008 "Renaming MCP Media Type to application/mcp-server-card+json" (Accepted, undated); ADR-0010 "Loose Coupling Between ARD Entries and AI Catalog Entries" (Accepted, 2026-07-09). The other 8 ADRs were not read.
[^ard-interop]: agenticresourcediscovery.org/interoperability/, consulted 2026-11-03 (undated page).
[^ard-governance]: agenticresourcediscovery.org/governance/, consulted 2026-11-03 (undated page).
[^ard-google-2026]: Junjie Bu & Srinivas Krishnan, "Announcing the Agentic Resource Discovery specification", Google Developers Blog, 2026-06-17, consulted 2026-11-03.
[^ard-aws-2026]: Jeffrey Damick, Anubhav Mangal & Bhargav Talluri, "Agentic Resource Discovery (ARD): An open specification for agent discovery", AWS Artificial Intelligence Blog, 2026-08-24, consulted 2026-11-03.
[^ard-hf-2026]: Ben Burtenshaw & Shaun Smith, "Agentic Resource Discovery: Let agents search for tools, skills, and other agents", Hugging Face blog, 2026-06-17, consulted 2026-11-03. The community comments under the post were not used.
[^agentready-2026]: agentready.org, AgentReady v2.0 (changelog: October 2026), AR-FIND-04 "Publish an AI Catalog and link it", consulted 2026-11-03 (page HTML fetched and read directly).
[^hf-catalog-probe]: HTTP GET of https://huggingface.co/.well-known/ai-catalog.json and https://huggingface.co/.well-known/ard.json, 2026-11-03. This is a point-in-time observation, not a published claim.
