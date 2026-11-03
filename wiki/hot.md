---
type: cache
title: Session Hot Cache
description: Read silently at every session start. ~500 words. Current focus, active pages, open threads.
updated: 2026-11-03
---

# Kortex — Session Hot Cache

> Read this silently at every session start. Replaces recap conversation.
> Update at session end via `/session --close`.

---

## Current Focus

**Agentic Resource Discovery (ARD): search for agent resources before invoking them.** Promoted ARD
from the queue to a **concept page**, grounded on the project site (home, spec v0.91,
interoperability and governance pages), plus **3 fiches** for the Google, AWS and Hugging Face
posts. ARD is an open, Apache-2.0 protocol that **sits entirely before invocation**. A client asks
"what is available for this task?" and a registry answers. The client then calls the resource over
its own protocol (MCP, A2A, Skills, an API). Spec v0.91 has status **Proposal**, is dated
2026-08-26 and is authored by Junjie Bu (Google), R.V. Guha and Shaun Smith (HF). It defines
**JSON-LD entries**: a domain-anchored `urn:air:<publisher>:…` identifier, an IANA media-type
`type`, `url` or `data`, and 2–5 `representativeQueries` as the search signal. There are 5
publishing mechanisms, and **REST `POST /search` is mandatory** with federation modes
`auto`/`referrals`/`none`. **Publisher-authority binding** stops namespace squatting, and the
relevance score MUST NOT be read as trust. **Governance:** an Oversight Board (Google, HF,
Microsoft, Amazon, Cisco) plus Maintainers chaired by Guha, with a neutral host "roughly twelve
months out", so ARD is **not under AAIF**. **Dated drift, noted and not escalated:** the June
launch posts used `/.well-known/ai-catalog.json` and called ARD "built upon" AI Catalog, while
v0.91 moved to `/.well-known/ard.json` and calls it "compatibility, not dependency". AgentReady
v2.0 (October) still recommends `ai-catalog.json`, and HF still serves only `ai-catalog.json`
(probed today). Google Cloud Agent Registry and AWS Agent Registry are **different products**,
and **neither is recorded as shipping ARD yet**. **Google and Hugging Face are now promotion
candidates** (3 and 2 sources). AI Catalog, hf-discover, both Agent Registries, Microsoft, Cisco
and the spec authors are parked.

Prior: **Agent Substrate: a runtime that multiplexes many sandboxed agents onto few pods.** Ingested
ate.dev as a **new project page**, grounded in the landing page, llms.txt, three sections of the
docs bundle and GitHub repo metadata. Substrate is a **CNCF Sandbox** project that "was
originally created by Google" (Apache-2.0). It maps many stateful **actors** onto a small
`WorkerPool` of warm pods. An idle actor checkpoints its memory and filesystem to GCS/S3. On a
request, `atenet-router` parks the call while a worker restores the snapshot, so the **Kubernetes
API stays off the request path**. Only infrastructure is a CRD (`ate.dev/v1`). Actors and
policies live in PostgreSQL behind a gRPC API, the **opposite design choice** to Agent Sandbox's
CRD per sandbox. Its two sandbox classes are `gvisor` (`runsc`) and `microvm` (Kata on Cloud
Hypervisor); plain containers are unsupported. Security is zero-trust: SPIFFE identity, **no
credentials in the sandbox** (the egress gateway injects them), default-deny networking,
`EgressPolicy` allowlists and OpenFGA authorization. It is the first Kubernetes-native sandbox in
the wiki with egress allowlists and credential injection built in (Strands Box does gateway
injection locally). The <500 ms resume, 500+/s and 10× figures are project-reported. Status: the
site says pre-1.0, and the repo tagged `v1.0.0-rc.1` on 2026-10-29. Noted as design-doc drift:
the Architecture page (marked Planned) still lists identity and policy as unaddressed. Agent
Sandbox's comparison table now has 4 rows. **gVisor, Kata and Google now each have 2 sources**
(promotion candidates). The **Kubernetes domain bootstrap trigger is met** and waits on the human. CNCF,
kagent, Agent Executor, SPIFFE, OpenFGA and Cloud Hypervisor are parked in the queue.

Prior: **Agent Sandbox: a Kubernetes-native agent sandbox.** Ingested the Kubernetes blog launch post
(Janet Kuo & Justin Santa Barbara, 2026-03-20) as a fiche, and the project site
(agent-sandbox.sigs.k8s.io) as a **new project page** grounded by both sources. SIG Apps argues
that agents are **isolated, stateful, singleton** workloads: mostly idle, with a persistent
identity and running untrusted code. That shape otherwise means a StatefulSet of size 1, a
headless Service and a PVC per agent, which the post calls an "operational nightmare" at scale.
The **core `Sandbox` CRD** is a single-container environment with gVisor/Kata isolation,
scale-to-zero with resume, and a stable hostname/network identity. **Optional extensions**
(`SandboxTemplate` / `SandboxClaim` / `SandboxWarmPool`) hand out pre-warmed pods to remove the
roughly one-second pod cold start. The Python (`k8s-agent-sandbox`) and Go SDKs both claim
sandboxes from a warm pool. The site lists use cases by sandbox lifetime, from short-lived code
execution to always-lived OpenClaw. This is the **third sandbox in the cluster**. An editorial
comparison: Strands Box offers local OS containment plus Dogwood policy; OpenSandbox hides the
*provisioning runtime* behind an OpenAPI; Agent Sandbox hides the *isolation backend* behind a
declarative CRD. Neither source states a license, API version or maturity, and the "in
development" status is dated 2026-03-20. No contradictions. SIG Apps, gVisor, Kata, OpenClaw,
both authors, the docs sub-pages and a **Kubernetes domain candidate** are parked in the queue.

Prior: **Agent Skills is now an AAIF project.** Ingested the **AAIF four-new-projects press release**
(AGNTCon + MCPCon NA, 2026-10-22): Anthropic contributed **Agent Skills** to the Agentic AI
Foundation, alongside **Open Responses** (OpenAI), **OpenEnv** (Hugging Face), and **OpenSandbox**
(Alibaba) — 10 hosted projects after year one (founding: MCP, goose, AGENTS.md; plus A2A, Agent
Router, agentgateway). Agent Skills fiche updated (governance bullet, 2nd source, `part-of` AAIF).
**AAIF promoted to an organization page** (7 grounding sources); the Linux Foundation link stays
footnoted to the A2A/AGENTS.md fiches because the release text never names the LF. OpenSandbox and
OpenEnv Relations fixed `created-by`→`part-of` AAIF (release names Alibaba/Hugging Face as
contributors). Agent Skills concept now 2-source-grounded — next promotion candidate.

Prior: ingested **Open Responses** (AAIF blog, Angie Jones, 2026-10-27) into **AI Protocols**: an open,
provider-neutral spec built on the **shape of OpenAI's Responses API** so a developer targets one
request/response contract instead of maintaining a separate adapter per provider (OpenAI
Responses API, Anthropic Messages API, Google `generateContent`). Switching provider/model becomes
**configuration, not a code branch**; the agent still owns tool execution and permissions, and no
model retraining is implied — the spec governs only the wire-level API. Provider-specific features
(hosted search tools, timing/cache events) ship as **namespaced extensions** agents can safely
ignore if unsupported. Already implemented: **Databricks Model Serving** exposes an Open Responses
endpoint fronting Claude/Gemini/open models; **Vercel AI Gateway** exposes an OpenResponses API.
The spec now sits under the **Agentic AI Foundation (AAIF)** — the same vendor-neutral governance
pattern already seen with A2A and AGENTS.md, **grounding AAIF with a 4th source**. Fiche
back-linked `extends`→Tool Use/Function Calling (standardizes the tool-call contract itself) and
`contrasts-with`→MCP (adjacent layer: MCP connects model↔tools/data, Open Responses standardizes
the model-provider API contract). Open Responses concept (single-source), Databricks, Vercel, and
Angie Jones parked in queue.

Prior: ingested **AgentReady** (agentready.org, Ora, 2026-10-27) into **AI Protocols**: open,
vendor-neutral spec of what a product should do to be usable by AI agents — a **find → read →
act** checklist (MUST/SHOULD/MAY), strength-ranked from measured agent behavior (250,000 agent
runs), not protocol advocacy. Find: bot-protection access (MUST), sitemap.xml (SHOULD),
`/.well-known/ai-catalog.json` (MAY, new v2.0). Read: answers in initial HTML + real HTTP status
codes incl. 404/429+Retry-After [RFC 6585] (MUST), `llms.txt`/JSON-LD/OpenAPI linked from visited
pages (SHOULD). Act, only if agents should complete tasks: **an MCP server or a CLI (MUST, new
in v2.0 2026-10, AR-ACT-10)**, OAuth-metadata auth [RFC 8414/9728]/OpenAPI/SDKs/WebMCP (SHOULD,
WebMCP raised from MAY in v2.0), agent payments x402/UCP/ACP/Stripe Link/NLWeb (MAY). Findings:
AGENTS.md reached via explicit link 100% of 38 traced fetches (highest of any discovery file,
vs. 86% for `llms.txt`'s 416); an April 2026 scan of ~50K sites found 88% shipped robots.txt/80%
crawler-reachable but only 3% shipped a spec-grade MCP server (~1% passed OAuth+PKCE) — "agents
can read, they cannot act"; across 1,056 sites, unreadable-to-agents businesses got 3.7× more
fact-omitting answers and 1.9× fewer recommendations; 82% of answers traced to a directly-fetched
page (docs pages 47%); 92.3% checkout accuracy over Stripe Link. Shares AEO's (Osmani) underlying
concern but **never cites Osmani or the term AEO** — only echo is Ora's own "AX is the New AEO"
study (arXiv:2609.34951); fiche back-linked `argues-that`→MCP and `argues-that`→AGENTS.md only,
AEO link kept to prose and flagged editorial. Publisher Ora, WebMCP, Web Bot Auth (unbound to a
specific checklist item), UCP/ACP naming collision with existing ACP concept, NLWeb, and the
arXiv study parked in queue; ARD merged into its existing (now 2-source) queue entry.

Prior: ingested **Agentic Engine Optimization (AEO)** (Addy Osmani blog fiche + **agentic-seo**
GitHub project, 2026-10-24) into **AI Protocols**: docs need structuring for AI coding agents,
not just humans — a six-layer stack (access control → discovery → capability signaling →
content formatting → token surfacing → "Copy for AI" button). Token count framed as a
**first-class doc metric** (agents have ~100K–200K context; target <15K quick-starts, <25K API
refs). Per-agent HTTP fingerprints cited (Claude Code `axios`, Cursor `got`, Windsurf `colly`)
for AI-traffic monitoring separate from human analytics. **agentic-seo** is Osmani's companion
MIT CLI implementing the checklist (10 checks, 0–100 score, `init` scaffolds `llms.txt`/
`AGENTS.md`/`skill.md`/`agent-permissions.json`). New fiche + project page; back-linked
`extends`→AGENTS.md and `contrasts-with`→MCP (doc-based vs. direct-integration agent access).
AEO concept itself stays single-source/queued (promotion candidate on a 2nd source); Addy
Osmani, llms.txt, skill.md, agent-permissions.json, and the cited arXiv fingerprint paper
parked in queue.

Prior: ingested (2 fiches) **Agent Plugins 1.0.0** (agent-plugins.org spec site + Google Developers
blog, Hou/Wang/Blount, 2026-08-06) into **AI Protocols**: open, vendor-neutral **packaging**
standard bundling **Agent Skills + MCP servers** into one portable directory (`plugin.json` +
`skills/` + `mcp.json` + reverse-domain client extensions). Fixes manifest fragmentation
(same components, per-client wrappers → fork-and-drift); minimal rules (fixed locations, no
inline declarations, explicit transports, independent failure); v1 non-goals (install, distro,
permissions, sandboxing, trust, UX) left to clients. Google joins the TSC (Amazon, Cursor,
Microsoft, OpenAI, Vercel) as Core Maintainer; ecosystem layering ARD → AI Catalog →
Plugins → MCP/Skills; ships in Agents CLI + Data Agent Kit. No new entity pages (fiche);
Agent Plugins concept now 2-source-grounded (promotion candidate), Google org + TSC members +
ARD/AI Catalog + 3 authors parked in queue.

Prior: ingested (fiche) **Agent Skills** (agentskills.io project site, 2026-10-08) into **AI
Protocols**: Anthropic-originated, open folder-based capability format — a `SKILL.md`
(metadata + instructions) plus optional scripts/references/assets — loaded via 3-stage
**progressive disclosure** (discovery → activation → execution) to keep context footprint
small. Positioned as **portable capability packages** (build once, reuse across compatible
agents: Claude Code, Cursor, Copilot, Gemini CLI, OpenCode, goose, Codex, …), complementing
per-repo instruction files — linked `contrasts-with` → AGENTS.md, `enables` → tool-use.
No new entity pages (fiche); Agent Skills concept, Anthropic org, SKILL.md spec, and client
roster parked in queue.

Prior: ingested (fiche) **Strands Box** (AWS Open Source blog, Fernando Dingler, 2026-10-07) into **AI
Protocols**: open-source (Apache 2.0, dev preview) agent **sandbox** that pairs OS-level
containment (macOS Seatbelt) with **Dogwood** policy enforced at four boundaries — network
proxy, Python (Monty), Shell (Strands Shell), and an MCP broker. Credentials injected by the
gateway (agent sees only placeholders). This **grounds Dogwood with a 2nd source** → Dogwood +
Strands Box are now promotion candidates to full `project` pages. **Live contradiction,
`PENDING — escalate to human`:** Box's Slack rate-limit rule counts HTTP-200 *responses* and
never addresses concurrency, which conflicts with the Dogwood fiche's guidance to count
*requests* so concurrency cannot bypass the limit. Flagged on both the Box and Dogwood fiches;
resolve against a real policy run. New follow-ups parked (Strands Box/Agents/Shell, Monty,
Seatbelt, Fernando Dingler).

Prior: ingested **AGENTS.md** (agents.md) into **AI Protocols**: open Markdown convention giving AI
coding agents per-repo instructions ("a README for agents"), 60k+ projects, **stewarded by
AAIF under the Linux Foundation** — which *confirms* the AAIF-sibling claim from the A2A fiche.
New concept + fiche; linked to MCP (sibling AAIF project). **AAIF is now grounded by 3 ingested
sources** (A2A, AGENTS.md, MCP-sibling) — it's the top queue item, ready to promote to a full
org page.

Prior: ingested **PAP** (Personal Agent Protocol, Meta + Sierra) from the Sierra blog into **AI
Protocols**: open standard for personal-agent↔business connection over **MCP/OpenAPI + OAuth**
— parallel to PACT but a different stack/sponsor. New concept + fiche; linked to MCP (route)
and PACT (contrast). **Live contradiction, `PENDING — escalate to human`:** Decagon's PACT post
says PACT joins "the Personal Agent Protocol working group (team behind Meta's Muse)", but this
Sierra source names PAP as Meta + Sierra, no working group, and "Muse" as a **Rocket** product.
Flagged on PAP, PACT concept, and the Decagon fiche. Entities (Sierra, Meta, Taylor, Bavor,
Genesys/Rocket/Shopify/Walmart) parked; the contested "Muse" is held until resolved.

Prior: ingested **PACT** (Personal Agent Consent & Trust Protocol) from two sources (Decagon blog +
openpactprotocol.org) into **AI Protocols**: an open consent/delegation layer **built on A2A
1.0** letting a user's personal agent act on their account at a business with verifiable,
scoped permission (separates agent identity from account authority; login stays with the
Brand). New concept page + 2 source fiches; A2A page back-linked (PACT builds-on A2A). One
flagged `PENDING`: consent flow is OAuth device-auth per Decagon but the spec site names no
OAuth — reconcile at a real spec read. New orgs (Decagon, Instinct, Personal Agent Protocol
working group, Meta/Muse) parked.

Prior: ingested (fiche) the **x402 Foundation launch** (Linux Foundation) into **AI Protocols**:
Coinbase contributed x402 to a neutral, Linux Foundation-hosted x402 Foundation (~40 members
incl. AWS, Google, Stripe, Visa, Mastercard, Circle). Verified x402's Coinbase origin +
card/stablecoin payment scope + Foundation governance; **HTTP-402 wire mechanics stay `NOT
VERIFIED`** (press release doesn't describe the flow). x402 `draft`→`stable`. Pattern emerging:
both A2A and x402 moved to **Linux Foundation** governance — that org is now the top queue item.

Prior: ingested (fiche) the **A2A → Agentic AI Foundation** announcement into **AI Protocols**:
A2A moves to vendor-neutral governance under AAIF (Linux Foundation-directed; sibling
projects MCP, goose, AGENTS.md). This verified two previously `NOT VERIFIED` claims on the
A2A concept page (foundation governance + Agent Card) and bumped it `draft`→`stable`,
`confidence` low→medium; A2A origin (Google/2025) still unverified. New orgs (AAIF, Linux
Foundation) + Agent Card concept parked in `raw/queue.md`.

Prior: created the **AWS** organization entity from the Dogwood source. Dogwood fiche itself
(temporal tool-call governance, extends Cedar via MFOTL) in `sources/`; follow-ups parked.

Prior thread: **Observability** domain seed scaffold (`draft` / `confidence: low`, `NOT
VERIFIED` recall claims) still awaits real OTel-spec ingests.

## Active Pages

- [Agentic Resource Discovery (ARD)](concepts/agentic-resource-discovery-ard.md) — latest ingest (new concept: pre-invocation discovery, JSON-LD entries, `/.well-known/ard.json`, REST `/search` + federation, publisher-authority trust binding, own governance; dated `ai-catalog.json` → `ard.json` drift)
- [ARD Google fiche](sources/ai-protocols-ard-google-announcement-2026.md) / [ARD AWS fiche](sources/ai-protocols-ard-aws-agent-registry-2026.md) / [ARD Hugging Face fiche](sources/ai-protocols-ard-hugging-face-discover-2026.md) — latest ingest (launch posts: catalogs + registries; AWS Agent Registry + DNS analogy; `hf-discover`)
- [AWS](organizations/aws.md) — enriched (AWS Agent Registry preview; ARD Oversight Board seat)
- [Agent Plugins](concepts/agent-plugins.md) — enriched (ARD link; `agent-plugins+zip`/`+gzip` in ARD v0.91 vs AI Catalog's `+json`)
- [Agent Substrate](projects/agent-substrate.md) — prior ingest (CNCF Sandbox runtime; actors multiplexed onto warm workers; gVisor / Kata-on-Cloud-Hypervisor; zero-trust egress; Architecture-page drift on identity/policy noted)
- [Agent Sandbox](projects/agent-sandbox.md) — enriched (4th row in the sandbox comparison table)
- [Agent Sandbox fiche](sources/ai-protocols-agent-sandbox-kubernetes-2026.md) — latest ingest (Kubernetes blog: Sandbox CRD for isolated/stateful/singleton agents; warm-pool extensions)
- [Agent Sandbox](projects/agent-sandbox.md) — new project page (site + blog; gVisor/Kata backends, Python/Go SDKs, use cases by lifetime, 3-way sandbox comparison)
- [OpenSandbox fiche](sources/ai-protocols-opensandbox-agent-primitive-2026.md) — enriched (contrasts-with Agent Sandbox: provisioning-runtime vs isolation-backend abstraction)
- [Strands Box fiche](sources/ai-protocols-strands-box-sandboxes-2026.md) — enriched (contrasting back-link to Agent Sandbox)
- [AAIF four-new-projects fiche](sources/ai-protocols-aaif-four-new-projects-2026.md) — latest ingest (Agent Skills/Open Responses/OpenEnv/OpenSandbox join AAIF; 10-project roster)
- [Agentic AI Foundation (AAIF)](organizations/agentic-ai-foundation.md) — new org page (promoted from queue)
- [Agent Skills fiche](sources/ai-protocols-agent-skills-overview-2026.md) — enriched (Anthropic → AAIF donation, 2026-10-22)
- [Open Responses fiche](sources/ai-protocols-open-responses-2026.md) — latest ingest (provider-neutral API spec based on OpenAI's Responses API; namespaced extensions; AAIF-stewarded)
- [Tool Use / Function Calling](concepts/tool-use-function-calling.md) — enriched (extends: Open Responses standardizes the tool-call contract across providers)
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — enriched (contrasts-with Open Responses: tool/data connection vs. the model-provider API contract itself)
- [AgentReady fiche](sources/ai-protocols-agentready-standard-2026.md) — latest ingest (find/read/act MUST/SHOULD/MAY checklist, MCP-or-CLI MUST in v2.0, agent-behavior studies)
- [AEO fiche](sources/addyosmani-agentic-engine-optimization-2026.md) — enriched (extended by AgentReady); six-layer stack, token-as-metric, agent HTTP fingerprints
- [agentic-seo](projects/agentic-seo.md) — latest ingest (companion audit CLI, 10 checks, 0–100 score)
- [AGENTS.md](concepts/agents-md.md) — enriched (named an emerging default agent-context format alongside llms.txt/skill.md)
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — enriched (contrasts-with doc-based AEO access)
- [Agent Plugins](concepts/agent-plugins.md) — promoted concept (portable 1.0.0 packaging; contrasts-with AGENTS.md; open questions on shippers + deferred layers)
- [Agent Plugins spec fiche](sources/ai-protocols-agent-plugins-spec-2026.md) — latest ingest (1.0.0 portable packaging: plugin.json + skills/ + mcp.json + client extensions; TSC roster)
- [Agent Plugins (Google blog) fiche](sources/ai-protocols-agent-plugins-google-2026.md) — latest ingest (Google joins TSC; manifest-fragmentation framing; v1 non-goals; ARD/AI Catalog layering; Agents CLI + Data Agent Kit)
- [Model Context Protocol (MCP)](concepts/model-context-protocol-mcp.md) — enriched (Plugins package MCP servers via mcp.json; independent-failure back-links)
- [Agent Skills fiche](sources/ai-protocols-agent-skills-overview-2026.md) — extended by Plugins spec (skills/ follows the Skills spec)
- [AGENTS.md](concepts/agents-md.md) — enriched (contrasting sibling: portable skills vs per-repo instructions)
- [Clef fiche](sources/ai-protocols-clef-decision-models-2026.md) — prior ingest (Cloudflare decision models on Workers AI)
- [Tool Use / Function Calling](concepts/tool-use-function-calling.md) — enriched (Clef = typed decision layer in front of tool selection)
- [Strands Box fiche](sources/ai-protocols-strands-box-sandboxes-2026.md) — prior ingest (sandbox embedding Dogwood)
- [Dogwood fiche](sources/ai-protocols-dogwood-runtime-verification-2026.md) — enriched (used-by Strands Box; 2-source-grounded)
- [AWS](organizations/aws.md) — enriched (+Strands Box, 2nd source)
- [AGENTS.md](concepts/agents-md.md) — new concept (prior ingest; confirms AAIF stewardship)
- [AGENTS.md fiche](sources/agents-md-open-format-2026.md) — source
- [PAP](concepts/personal-agent-protocol-pap.md) — prior ingest (contradiction flag vs PACT)
- [Sierra PAP fiche](sources/sierra-personal-agent-protocol-2026.md) — PAP source
- [PACT](concepts/personal-agent-consent-trust-protocol-pact.md) — prior ingest; now contrasts-with PAP
- [Decagon PACT fiche](sources/decagon-pact-introduction-2026.md) / [openpactprotocol.org fiche](sources/openpactprotocol-pact-spec-2026.md) — PACT sources
- [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — PACT builds on it (back-linked)
- [x402 Foundation fiche](sources/ai-protocols-x402-foundation-launch-2026.md) — prior ingest
- [x402](concepts/x402.md) — enriched; origin + payment scope + governance verified
- [A2A/AAIF fiche](sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) — prior ingest
- [Agent2Agent (A2A)](concepts/agent2agent-a2a.md) — enriched + 2 claims verified by the fiche
- [AWS](organizations/aws.md) — org entity (native A2A via Bedrock AgentCore)
- [AI Protocols](domains/ai-protocols.md) — domain hub
- [Dogwood fiche](sources/ai-protocols-dogwood-runtime-verification-2026.md) — prior ingest
- [Observability](domains/observability.md) — domain hub (prior thread)

## Open Questions

- Observability: how do the three signals converge toward a unified data model, and what is each signal's current OTel stability?
- Observability: where should telemetry be processed — in-SDK, at a Collector, or at the backend?
- Carried over (AI Protocols): protocol stack composition; ACP vs A2A convergence; x402 vs Agentic Commerce Protocol.

## Recent Decisions

- Seed concepts chosen as the 5 most load-bearing protocol primitives, not an exhaustive list.
- Slug convention: `<long-name>-<acronym>` (e.g. `model-context-protocol-mcp`, `opentelemetry-otel`); `x402` stays bare.
- Observability: OTel **Collector** deferred to `projects/opentelemetry-collector.md` on `/ingest` — it's a binary, a `project` not a `concept`. Do NOT seed it under `concepts/`. Instrumentation took the 5th concept slot instead.

## Last Operations

- 2026-11-03 `[INGEST]`+`[FILE]` — ARD concept (site + spec v0.91 + interop + governance) + 3 fiches (Google, AWS, HF); pre-invocation discovery protocol with its own Board and Maintainers (not AAIF); `ai-catalog.json` → `ard.json` drift dated, not escalated; AWS org, Agent Plugins, MCP, A2A, Tool Use, Agent Skills, AgentReady and Agent Plugins (Google) back-linked; AI Catalog, hf-discover, both Agent Registries, Microsoft, Cisco, GoDaddy, spec authors, DNS-AID/ANS parked; Google (3 sources) and Hugging Face (2) now promotion candidates.
- 2026-11-02 `[INGEST]` — Agent Substrate project page (ate.dev + llms.txt + docs bundle + repo); CNCF Sandbox, originally Google; actors/workers, suspend to snapshot + resume on any worker, gVisor or Kata-on-Cloud-Hypervisor, zero-trust egress; Agent Sandbox table extended to 4 rows; Architecture-page drift on identity/policy noted; Kubernetes bootstrap trigger met; CNCF, kagent, Agent Executor, SPIFFE, OpenFGA, Cloud Hypervisor parked.
- 2026-11-02 `[INGEST]` — Agent Sandbox fiche (Kubernetes blog, Kuo & Santa Barbara) + project page (agent-sandbox.sigs.k8s.io); SIG Apps `Sandbox` CRD + warm-pool extensions + Python/Go SDKs; OpenSandbox/Strands Box back-linked (editorial 3-way comparison); SIG Apps, gVisor, Kata, OpenClaw, authors, docs sub-pages, Kubernetes domain candidate parked.
- 2026-10-27 `[INGEST]`+`[FILE]` — AAIF four-new-projects fiche; Agent Skills now an AAIF project (Anthropic-contributed); AAIF org page promoted; OpenSandbox/OpenEnv `created-by`→`part-of` AAIF; Agent Router, agentgateway, goose, Alibaba, Surtani, Soria Parra parked.
- 2026-10-27 `[INGEST]` — Open Responses fiche (AAIF blog, Angie Jones); provider-neutral API spec based on OpenAI's Responses API, namespaced extensions, AAIF-stewarded (4th grounding source); Tool Use/MCP back-linked; Open Responses concept + Databricks + Vercel + Angie Jones parked.
- 2026-10-27 `[INGEST]` — AgentReady fiche (agentready.org, Ora); find/read/act MUST/SHOULD/MAY checklist, v2.0 MCP-or-CLI MUST, agent-behavior studies; AGENTS.md cited directly (100% link-fidelity finding), MCP argued-for; AEO link flagged editorial (no citation on the page); Ora org + AgentReady concept + WebMCP + Web Bot Auth + UCP/ACP + NLWeb + arXiv study parked, ARD merged into existing entry.
- 2026-10-24 `[INGEST]` — AEO fiche (Addy Osmani) + agentic-seo project (GitHub); six-layer stack, token-as-metric, agent HTTP fingerprints; AGENTS.md/MCP back-linked; AEO concept + Addy Osmani + llms.txt/skill.md/agent-permissions.json parked.
- 2026-10-09 `[INGEST]` — Agent Plugins 2 fiches (spec site + Google blog); 1.0.0 portable packaging (Skills + MCP); Google joins TSC; Agent Plugins concept now 2-source-grounded (promote); MCP back-linked.
- 2026-10-09 `[FILE]` — Agent Plugins promoted to concept (2-source-grounded); contrasts-with AGENTS.md; MCP/AGENTS.md back-linked; queue marked promoted.
- 2026-10-08 `[INGEST]` — Agent Skills fiche (agentskills.io); open SKILL.md folder format + progressive disclosure; contrasts-with AGENTS.md, enables tool-use; no new entities.
- 2026-10-08 `[INGEST]` — Clef fiche (Cloudflare); open-source decision models (Clef/Clef-flash) on Workers AI; typed decision layer linked `enables`→tool-use; vendor-reported benchmarks; first Cloudflare source.
- 2026-10-08 `[INGEST]` — Strands Box fiche; sandbox embedding Dogwood; Dogwood now 2-source-grounded (promote); **contradiction PENDING** — rate-limit counts responses vs Dogwood's "count requests" (concurrency bypass).
- 2026-10-08 `[INGEST]` — AGENTS.md: new concept + fiche; confirms AAIF stewardship; AAIF now 3-source-grounded (promote next).
- 2026-10-08 `[INGEST]` — PAP (Sierra): new concept + fiche; linked MCP/PACT; **contradiction PENDING** (working group / "Muse").
- 2026-10-08 `[INGEST]` — PACT (2 sources): new concept + 2 fiches; A2A back-linked; OAuth naming flagged PENDING.
- 2026-10-08 `[INGEST]` — x402 Foundation fiche; verified x402 origin/scope/governance, promoted x402 to stable.
- 2026-10-08 `[INGEST]` — A2A/AAIF fiche; verified 2 A2A claims, promoted A2A to stable.
- 2026-10-08 `[FILE]` — created AWS organization entity.
- 2026-10-08 `[INGEST]` — Dogwood fiche into AI Protocols.
- 2026-10-08 `[BOOTSTRAP]` — created Observability domain + 5 seed concepts.
- 2026-10-08 `[BOOTSTRAP]` — created AI Protocols domain + 5 seed concepts.
- 2026-10-08 `[INIT]` — completed bundle scaffold (hot.md, overview.md).

## Known Failures

- None.

## Pending Ingests

- None queued. Drop OTel specs/docs/articles (or AI protocol specs) in `raw/` and run `/ingest` to enrich a domain.
