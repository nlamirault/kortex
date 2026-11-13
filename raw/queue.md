# Ingest Queue

## Pending

Follow-up entities surfaced by the Agent Plugins fiches (agent-plugins.org + Google blog):

- **Agent Plugins** (concept/project) — ✅ Promoted 2026-10-09 → [wiki/concepts/agent-plugins.md](../wiki/concepts/agent-plugins.md) (was grounded by 2 sources: spec site + Google announcement).
- **Google** (organization) — joins the Agent Plugins TSC as Core Maintainer (Kevin Hou); ships Agents CLI + Data Agent Kit. First Google-org source in AI Protocols. ★ **2nd source:** originally created Agent Substrate (ate.dev, 2026-11-02; now a CNCF Sandbox project). Agent Executor, which is built on Substrate, links to `github.com/google/ax`, but the page text never names Google, so that link is URL-only and does not count as a 3rd source. ★ **3rd source:** launched ARD (Google Developers Blog, Bu & Krishnan, 2026-06-17). It co-authors the spec, holds an ARD Oversight Board seat (Junjie Bu) and runs Google Cloud Agent Registry in Gemini Enterprise Agent Platform, with native ARD support promised "in the coming months". **Promotion candidate.**
- **TSC members** (organization) — Amazon, Cursor, Microsoft, OpenAI, Vercel (Core Maintainers); Amazon/AWS already has an org page.
- **Agents CLI / Data Agent Kit** (project) — Google's first Plugins shippers (expert skills for agent ops; data-cloud skills + MCP servers for BigQuery/Spanner/Cloud SQL).
- **Agentic Resource Discovery (ARD)** (project/concept) — ✅ Promoted 2026-11-03 → [wiki/concepts/agentic-resource-discovery-ard.md](../wiki/concepts/agentic-resource-discovery-ard.md) (site + spec v0.91 + interop + governance pages, and the Google, AWS and Hugging Face launch fiches).
- **AI Catalog** (project) — entry format ARD indexes; `application/agent-plugins+json` proposal points at plugin.json. ★ More grounding (2026-11-03): Google's ARD post says ARD is "built upon the foundational AI Catalog data model" and credits the **AI Catalog Working Group under the Linux Foundation** (repo `github.com/Agent-Card/ai-catalog`). ARD's interop page calls the relationship "compatibility, not dependency" as of **AI Catalog v0.9-RC**, and AgentReady AR-FIND-04 recommends an AI Catalog at `/.well-known/ai-catalog.json`. Ingest the AI Catalog spec itself to settle its version, path and media types.
- **Kevin Hou, Haoyu Wang, Alan Blount** (person) — Google post authors (DeepMind / Cloud Data / Cloud AI).

Follow-up entities surfaced by the ARD concept + fiches (agenticresourcediscovery.org, Google / AWS / Hugging Face blogs):

- **Google Cloud Agent Registry** (project) — hosted registry in Gemini Enterprise Agent Platform: namespaced URNs, agentic egress policies, tool and spec pinning, Agent Identity verifying the trust manifest; native ARD support "in the coming months" as of 2026-06-17. Different product from AWS Agent Registry.
- **AWS Agent Registry** (project) — preview; registries plus records, an admin/publisher/curator/consumer workflow, IAM or JWT authorization, hybrid search, a remote MCP endpoint (AWS blog, 2026-08-24). Folded into the AWS org page for now; promote if a 2nd source appears.
- **hf-discover** (project) — Hugging Face's ARD reference implementation (`github.com/huggingface/hf-discover`): Hub semantic search over Spaces wrapped as ARD entries, reachable via the `hf` CLI, REST `/search` and MCP `/mcp`.
- **Microsoft** (organization) — ARD Oversight Board (Dhruv Chand, also a Maintainer), working-group participant, 10 people in the spec's acknowledgements; also an Agent Plugins TSC member. Two independent mentions now.
- **Cisco** (organization) — ARD Oversight Board (Luca Muscariello); 5 people in the acknowledgements.
- **GoDaddy** (organization) — named among ARD's working-group participants on the home page; 1 person in the acknowledgements.
- **R.V. Guha / Junjie Bu / Shaun Smith** (person) — ARD spec v0.91 authors. Guha chairs the Maintainers as a member at large; Bu (Google) and Smith (Hugging Face) sit on both bodies. Also Srinivas Krishnan (Google post co-author) and Ben Burtenshaw (HF post co-author).
- **ARD spec docs** (source follow-up) — the How ARD works, How to publish, Connect a chatbot and Reference Implementations pages; the JSON Schema / CDDL / OpenAPI files in `ards-project/ard-spec`; and the ADR log (spec cites ADR-0007 for the multi-segment URN namespace). ADR-0008 (MCP media-type rename) and ADR-0010 (loose coupling with AI Catalog, 2026-07-09) were read on 2026-11-03 and cited on the concept page; the other 8 ADRs were not. The repo has no tags or releases yet, so re-check `spec/ard.md`'s version header before citing it. Ingest when wire-level detail is needed.
- **DNS-AID / Agent Naming Service (ANS)** (concept) — cited by ARD v0.91 (informative §5.3.2.1 and attestation scopes: "SCITT/ANS registrations") as federated-routing and naming research. No source describes either yet.

Follow-up entities surfaced by the Agent Skills fiche (agentskills.io):

- **Agent Skills** (concept) — the portable capability-folder format itself (SKILL.md + scripts/references/assets, progressive disclosure). ★ Now 2-source-grounded (agentskills.io + AAIF four-projects release, 2026-10-27: Anthropic → AAIF donation) — promote.
- **Anthropic** (organization) — originator of the Agent Skills format; released as an open standard, contributed to AAIF 2026-10-22 (2 sources). Claude Code is also a supported Agent Substrate workload, with a "Claude Code Multiplexing" tutorial (3 agents on 2 worker pods); that is product usage, not an org claim.
- **SKILL.md specification** (source follow-up) — the full format spec at agentskills.io/specification; ingest for wire-level detail.
- **Agent Skills client roster** (sources) — per-client instruction pages (Claude Code, Cursor, Copilot, Gemini CLI, OpenCode, goose, Codex, …); ingest individually only as needed.

Follow-up entities surfaced by the Clef fiche (Cloudflare decision models):

- **Cloudflare** (organization) — publisher of Clef; hosts Workers AI, AI Gateway, Browser Run. First Cloudflare source — promotion candidate for an org page.
- **Workers AI** (project) — Cloudflare's model-hosting platform where Clef/Clef-flash run.
- **Clef / Clef-flash** (project) — the decision-model family itself (Apache 2.0, Hugging Face).
- **Decision models** (concept) — a model category (narrow, typed, probability-weighted classification) introduced by Typesafe AI / Jev; the core idea behind this fiche.
- **Typesafe AI / Jev** (organization / model) — originators of the "decision model" category and the Jev Decision Index benchmark; Clef is Jev-API compatible.
- **RLCD — Reinforcement Learning for Calibrated Decisions** (concept) — Cloudflare's RL method used as a secondary, calibration-focused training objective for Clef.
- **Michelle Chen, Alex Reneau, Kevin Flansburg** (person) — Clef post authors (Cloudflare).

Follow-up entities surfaced by the Dogwood + Strands Box fiches (not yet created — promote to full pages on demand):

- **Dogwood** (project) — the governance language itself. ★ **Now grounded by 2 sources** (Dogwood fiche + Strands Box embeds it) — promotion candidate.
- **Cedar** (project/concept) — point-in-time policy language Dogwood extends; AgentCore Policy foundation. Now referenced by 2 sources (Dogwood + Strands Box).
- **Amazon Bedrock AgentCore / AgentCore Policy** (project) — embeds Dogwood.
- **Metric First-Order Temporal Logic (MFOTL)** (concept) — formalism behind Dogwood's temporal operators.
- **Runtime verification** (concept) — the field Dogwood draws on.
- **Marc Brooker** (person) — VP & Distinguished Engineer, AWS; author of the Dogwood fiche and the Strands Box companion post.

Follow-up entities surfaced by the Strands Box fiche:

- **Strands Box** (project) — open-source (Apache 2.0, dev preview) agent sandbox embedding the Dogwood Local Engine. Promotion candidate alongside Dogwood.
- **Strands Agents** (project) — the broader effort Box/Dogwood belong to (strandsagents.com); source doesn't define it in detail.
- **Strands Shell** (project) — shell interpreter that is one of Box's policy-enforcement points.
- **Monty** (project) — Python interpreter that is one of Box's policy-enforcement points.
- **macOS Seatbelt** (concept/project) — the OS-level containment mechanism Box starts with.
- **Fernando Dingler** (person) — Principal Engineer, AWS; author of the Strands Box post.

Follow-up entities surfaced by the AgentReady fiche (agentready.org):

- **Ora** (organization) — publisher of AgentReady; runs the measured-agent-behavior studies (1,056-site study, ~50,000-site April 2026 scan, Stripe Link checkout study) and its own agent-readiness ranker. AgentReady v2.0 also names **Ora Directory** as an example ARD registry that indexes published catalogs (re-read 2026-11-03).
- **AgentReady** (concept) — the find/read/act checklist discipline itself, distinct from Ora the org; promotion candidate once a 2nd independent source appears.
- **WebMCP** (concept) — W3C Community Group draft; `Act`-stage practice raised from MAY to SHOULD in v2.0.
- **Web Bot Auth** (concept) — listed among the protocols AgentReady says now serve agents (with MCP, WebMCP, A2A, x402, llms.txt); page doesn't bind it to a specific checklist item — ingest its own spec before claiming more.
- **"AX is the New AEO"** (source, arXiv:2609.34951, published as an Ora blog post + paper, 2026-09) — the study AgentReady explicitly attributes its 99%-dead-end-journeys/2.1×-blocked/23%-more-turns finding to (4 agent stacks, Claude + GPT via Tavily). AgentReady's other headline figures (1,056-site 3.7×-omission-rate study, 82%/47% answer-provenance finding) are separate, unnamed Ora traced-run research — do not conflate with this paper on ingest. Ingest for primary-source detail (NOT VERIFIED here beyond AgentReady's citation).
- **UCP / ACP (agent commerce)** (concept) — payment protocols AgentReady lists as `Act`-stage MAY alongside x402 and Stripe Link; ACP name collides with the existing Agent Communication Protocol (IBM/BeeAI) already in the wiki — disambiguate on ingest. ⚠️ A **third ACP** reading: ARD's interop page mentions "ACP's Agent Registry" of "editor-context agents" that can export `ard.json` feeds. That is plausibly Agent Client Protocol, but the page never expands the acronym. NOT VERIFIED; not linked.
- **NLWeb** (project/concept) — new `Act`-stage MAY practice added in v2.0 (AR-ACT-09). Also appears in ARD spec v0.91 only as an example referral registry URL (`https://finder.nlweb.ai/search`, "Public Agent Finder"); that is illustrative, not a stated deployment.
- **Comparable scanners** (projects) — is-agentic.com, Mintlify Agent Score, Netlify AXIS; mentioned alongside [agentic-seo](../wiki/projects/agentic-seo.md) as companion agent-readiness auditors.

Follow-up entities surfaced by the A2A/AAIF fiche:

- **Agentic AI Foundation (AAIF)** (organization) — Linux Foundation-directed body governing A2A, MCP, goose, AGENTS.md. ★ **Top priority — now grounded by 3 ingested sources** (A2A joined it, AGENTS.md stewarded by it, sibling to MCP). Clears the "real source" bar; ready to promote to a full org page.
- **Linux Foundation** (organization) — parent governance body directing AAIF and hosting the x402 Foundation. (High priority — now behind A2A, x402, and AGENTS.md.)
- **Agent Card** (concept) — A2A capability-advertisement mechanism.

Follow-up entities surfaced by the x402 Foundation fiche:

- **x402 Foundation** (organization) — Linux Foundation-hosted steward of x402; ~40 members.
- **Coinbase** (organization) — original contributor of x402.
- **Circle / Ripple** (organization) — stablecoin issuers cited (USDC, XRP/RLUSD) as x402 settlement rails.

Follow-up entities surfaced by the PACT fiches:

- **Decagon** (organization) — open-sourced PACT; a Provider hosting business support agents.
- **Instinct** (organization) — co-developer of PACT; also a personal-agent platform; also "joining" PAP.
- **Personal Agent Protocol working group** (organization) — group Decagon says it is joining. ⚠️ Conflicts with Sierra PAP source (no working group named) — resolve before creating.

Follow-up entities surfaced by the Sierra PAP fiche:

- **Sierra** (organization) — co-developer of PAP (Bret Taylor, Clay Bavor).
- **Meta** (organization) — co-developer of PAP.
- **Bret Taylor**, **Clay Bavor** (person) — PAP authors (Sierra).
- **Genesys, Rocket, Shopify, Walmart** (organization) — PAP industry partners. (Stripe already queued via x402.)
- **"Muse"** (project) — ⚠️ contested: Meta's (per Decagon) vs Rocket's (per Sierra). Resolve before creating a page.

Follow-up entities surfaced by the AEO fiche (addyosmani.com) + agentic-seo project:

- **Agentic Engine Optimization (AEO)** (concept) — the named framework itself (six-layer stack: access control → discovery → capability signaling → content formatting → token surfacing → "Copy for AI"). Single-source so far (the fiche) — promotion candidate once a second source (e.g. the Lighthouse `llms.txt` check, or Google's AI-optimization guide) is ingested.
- **Addy Osmani** (person) — author of the AEO post and the agentic-seo tool; Member of Technical Staff, Anthropic (Claude Code), per page bio; discloses prior Google Cloud AI affiliation.
- **llms.txt** (concept) — proposed Markdown index format for AI agents; Chrome Lighthouse has an experimental check for it.
- **skill.md** (concept) — capability-declaration format for services (inputs/constraints); distinct from Anthropic's Agent Skills `SKILL.md` folder format already in the wiki — names collide, scopes differ (service-capability doc vs. loadable agent capability).
- **agent-permissions.json** (concept) — emerging spec for declarative automated-access rules (rate limits, preferred endpoints).
- **Developer Experience with AI Coding Agents** (source, arXiv) — the per-agent HTTP-fingerprint research (Claude Code `axios/1.8.4`, Cursor `got`, Windsurf `colly`, etc.) cited by the AEO fiche; https://arxiv.org/html/2604.02544v1.

Follow-up entities surfaced by the Open Responses fiche (aaif.io):

- **Open Responses** (concept) — the spec itself (OpenAI Responses API shape, standardized; extensions mechanism). Single-source so far — promotion candidate once a second independent source (e.g. the openresponses.org spec text, or the Databricks/Vercel implementation posts) is ingested.
- **Agentic AI Foundation (AAIF)** (organization) — ✅ Promoted 2026-10-27 → [wiki/organizations/agentic-ai-foundation.md](../wiki/organizations/agentic-ai-foundation.md) (7th source: AAIF four-projects release).
- **Databricks** (organization) — Model Serving exposes an Open Responses endpoint fronting Claude, Gemini, and open models.
- **Vercel** (organization) — AI Gateway exposes an OpenResponses API.
- **Angie Jones** (person) — author of the Open Responses fiche source (AAIF blog).

Follow-up entities surfaced by the OpenSandbox fiche (aaif.io):

- **OpenSandbox** (project) — the sandbox platform itself (Apache 2.0, multi-language SDKs, Docker + Kubernetes runtimes, lifecycle + execution OpenAPI specs). Single-source so far — promotion candidate once a second source (e.g. the spec repo or a client-SDK doc) is ingested.
- **`execd`** (project/concept) — the in-sandbox execution daemon that carries out commands/file ops from the SDK; minor, fold into the OpenSandbox project page rather than a standalone page.

Follow-up entities surfaced by the OpenEnv fiche (aaif.io):

- **OpenEnv** (project) — the training-environment interface itself (reset/step/state episode API, sync/async clients, MCPEnvironment base class). Single-source so far — promotion candidate once a second source (e.g. the GitHub repo or a Hugging Face doc) is ingested.
- **Turing** (organization) — ran the Calendar Gym case study cited in the fiche; first Turing-org source in AI Protocols.
- **Hugging Face** (organization) — OpenEnv maintainer org (Spaces hosting, TRL integration); not yet an org page. ★ **2nd source (2026-11-03):** ARD co-author (Shaun Smith, spec v0.91 author, Oversight Board member and Maintainer) and publisher of the `hf-discover` reference implementation (HF blog, Burtenshaw & Smith, 2026-06-17). **Promotion candidate.**
- **Reward design / reward hacking** (concept) — the recurring failure mode across the fiche's case studies (proxy metrics diverging from intended behavior); candidate for a `pattern` page if a second instance surfaces elsewhere in the wiki.

Follow-up entities surfaced by the AAIF four-new-projects fiche (aaif.io):

- **Agent Router** (project) — AAIF-hosted project; not described in the release.
- **agentgateway** (project) — AAIF-hosted project; not described in the release. Second mention: Agent Substrate's "Pluggable Egress Networking" tutorial uses Envoy or agentgateway to tunnel and authenticate outbound actor traffic over mTLS (ate.dev/llms.txt, 2026-11-02). That is its first functional description in the wiki.
- **goose** (project) — AAIF founding project; cited by 3+ sources, no page yet.
- **Alibaba** (organization) — contributor of OpenSandbox to AAIF.
- **Manik Surtani** (person) — CTO and co-founder of AAIF.
- **David Soria Parra** (person) — co-creator and lead maintainer of MCP (Anthropic); quoted on the Agent Skills donation.

Follow-up entities surfaced by the Agent Sandbox fiche (kubernetes.io blog) + project page (agent-sandbox.sigs.k8s.io):

- **Kubernetes SIG Apps / Kubernetes** (organization) — the SIG developing Agent Sandbox (`kubernetes-sigs/agent-sandbox`). First Kubernetes source in the wiki. Linux Foundation appears only as footer boilerplate ("Kubernetes a Series of LF Projects, LLC") — do not cite it as governance without a real source.
- **Kubernetes** (domain candidate) — Agent Sandbox is the first `kubernetes-sigs` project ingested; `/bootstrap kubernetes` once a 2nd Kubernetes source lands (AGENTS.md already reserves a 1-year staleness window for the Kubernetes ecosystem). ★ **Trigger met 2026-11-02:** Agent Substrate is the 2nd Kubernetes-native source (Kubernetes 1.37+, `ate.dev/v1` CRDs, a `kubectl ate` plugin). Waiting for the human to run `/bootstrap kubernetes`.
- **gVisor** (project) — ✅ Promoted 2026-11-13 → [wiki/projects/gvisor.md](../wiki/projects/gvisor.md) (Google CNCF-donation post gVisor section + gvisor.dev docs + repo + cncf/sandbox#521 + the Agent Sandbox gVisor Isolation page). Was: userspace-kernel isolation backend (intercepts syscalls) documented for Agent Sandbox; site has a dedicated page at https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/. ★ **2nd source:** Agent Substrate's `gvisor` sandbox class (`runsc`; checkpoint/restore needs `--allow-connected-on-save`, not re-verified on 2026-11-13).
- **Kata Containers** (project) — VM-per-sandbox isolation backend (dedicated kernel, QEMU) for Agent Sandbox; https://agent-sandbox.sigs.k8s.io/docs/use-cases/kata-containers-isolation/. ★ **2nd source:** Agent Substrate's `microvm` class runs a Kata guest on the **Cloud Hypervisor** VMM, not QEMU. Promotion candidate.
- **OpenClaw** (project) — always-on agent environment the site runs inside Agent Sandbox ("Agents in Sandbox"); not described further; https://agent-sandbox.sigs.k8s.io/docs/use-cases/openclaw/. Second mention: listed among the agent frameworks Agent Substrate runs (ate.dev). Neither source describes it.
- **Janet Kuo, Justin Santa Barbara** (person) — Agent Sandbox launch-post authors; byline gives GitHub handles only (janetkuo, justinsb), no affiliations.
- **Agent Sandbox docs** (source follow-up) — Getting Started, Sandbox, Runtime Templates, Volumes, Custom Sandbox pages under https://agent-sandbox.sigs.k8s.io/docs/ — ingest for API group/version, CRD fields, license, and maturity, none of which the two ingested pages state.

Follow-up entities surfaced by the Agent Substrate project page (ate.dev + llms.txt + docs bundle + repo):

- **Cloud Native Computing Foundation (CNCF)** (organization) — hosts Agent Substrate and kagent as Sandbox projects. First ingested source to name CNCF hosting. The [OpenTelemetry](../wiki/concepts/opentelemetry-otel.md) concept page also calls OTel a CNCF project, but only from recall (`NOT VERIFIED`), so link it once that claim is verified. As with Kubernetes, the "a Series of LF Projects, LLC" footer is boilerplate, so do not cite it as Linux Foundation governance.
- **kagent** (project) — CNCF Sandbox project; "a Kubernetes-native framework that runs sandboxed, stateful agent workloads on Agent Substrate"; https://github.com/kagent-dev/kagent.
- **Agent Executor** (project) — "a distributed agent runtime: a secure, hyper-scalable agent harness on Agent Substrate"; https://github.com/google/ax.
- **SPIFFE** (concept) — workload-identity standard. Substrate gives each actor a short-lived SPIFFE X.509 cert and authenticates clients over SPIFFE mTLS or OIDC JWTs. 2nd mention: ARD spec v0.91 names SPIFFE (next to DID methods and enterprise PKI) as a framework a `trustManifest` may declare. It is an example, not a requirement.
- **OpenFGA** (project) — authorization engine. `ate-api-server` checks every call against an OpenFGA model.
- **Cloud Hypervisor** (project) — the VMM under Substrate's `microvm` class (with Kata). Fold it into the Kata Containers page unless a 2nd source appears.
- **Agent Substrate docs** (source follow-up) — https://ate.dev/llms-full.txt (~516 KB) bundles every guide. The project page drew only on its Overview, Architecture and Sandbox Classes pages. Ingest the Threat Model, Request Parking, Egress Credential Injection and Version Skew Policy pages for detail. Design-doc drift: the Architecture page (marked "[Status: Planned]") still lists identity and policy under "Problems We Haven't Addressed Yet", although the security guides describe both as shipped. Check against the code, or see whether a later Architecture rewrite fixes it.
- **Agent Substrate demo video** (source) — https://www.youtube.com/watch?v=ZEzkCFJkzjY (~250 actors on 8 pods).

Follow-up entities surfaced by the PAP site fiche (personalagentprotocol.org, 2026-11-13). The existing PACT and Sierra PAP entries above are not edited here; this block cross-references them:

- **Sierra "Poppy" update post** (source) — https://sierra.ai/blog/poppy. The Sierra launch post now opens with "Update: On 10/9, we shared a draft of Personal Agent Protocol, with 35 new design partners including Bank of America, OpenAI, Visa, and United Airlines" and links here. It was not read; ingest it as a fiche and check whether it names the spec's authors or a steward. Also back-link the [Sierra PAP fiche](../wiki/sources/sierra-personal-agent-protocol-2026.md) to the new site fiche; that was left out of this change set.
- **Meta / Sierra** (organization) — see the "Sierra PAP fiche" entries above. The site does not name them as authors. It lists **Meta as a personal-agent design partner** and **Sierra as a technology provider**, among 43 listed partners. Only the launch post calls them the developers.
- **Instinct** (organization) — see the "PACT fiches" entry above. It is now also **listed on the PAP site** as a personal-agent design partner (Path to 1.0, 2026-11-11), its 3rd mention. Decagon is not on the list, but the list covers only partners "that have agreed to be listed".
- **Personal Agent Protocol working group / "Muse"** — see the entries above. The site names no working group. It uses "Muse" only as the example personal-agent name in the guides' consent-page wording ("Muse wants to connect to your Example account"), without attributing it; the "Companies in the examples are fictional" disclaimer covers companies, not agents. The `PENDING` stays open. The PAP concept page narrows the Sierra-side reading to the verbatim Rocket CTO quote ("allows a Muse agent to move across our platform"). The PACT concept, Decagon fiche, Sierra fiche and hot cache still say "Rocket product"; align them when the `PENDING` is resolved.
- **OpenAI** (organization) — listed on the PAP site as a personal-agent design partner. Also an Agent Plugins TSC member and the origin of the Open Responses API shape, so 3 independent mentions. Promotion candidate.
- **Universal Commerce Protocol (UCP)** (concept) — see the "UCP / ACP (agent commerce)" entry above. 2nd mention: PAP's `ucp` v1 extension lets a company that speaks UCP handle carts, checkout and payment there, while PAP finds the company and signs the user in. The extension page (https://personalagentprotocol.org/docs/1.0/extensions/ucp) was not read.
- **Web Bot Auth** (concept) — see the AgentReady entry above. 2nd mention: PAP spec draft 1.0 §5.3 says personal agents SHOULD sign Session-header requests with an HTTP Message Signature (RFC 9421) using Web Bot Auth (draft-ietf-webbotauth-httpsig-protocol), as compatibility support for traffic-management infrastructure. Promotion candidate once its own spec is read.
- **OAuth Client ID Metadata Document (CIMD)** (concept) — IETF draft (draft-ietf-oauth-client-id-metadata-document). A PAP personal agent's `client_id` MUST be an HTTPS URL that returns its metadata document.
- **Agent Skills discovery proposal** (source follow-up) — `skill_index` in PAP §9.4 follows a pinned revision of https://github.com/jonathanhefner/agentskills/blob/ab2ff8db3d5c9597985b06f94ea3caf1996ce82e/docs/well-known-uri.mdx (schema `0.2.0`). The spec calls it "a draft, not an adopted Agent Skills standard". Relevant to the queued Agent Skills concept.
- **PAP community demos** (project) — Cliffside Retail with the Atlas demo agent (https://www.cliffside-retail.com/atlas, v0.4), Poppy Demo Agent (https://github.com/adewale/pda, v0.3, with a validator and an interop harness), and Print with Poppy (https://github.com/spenciefy/print-with-poppy, v0.3, real orders through Operations and Stripe Checkout). None is endorsed by the PAP authors. Promote one only if it becomes the reference implementation.
- **PAP extension and guide pages** (source follow-up) — the six extension pages (`operations` v3, `ucp`, `mediated-sign-in`, `browser-control`, `links`, `disclosures`), the Guides (`/docs/1.0/guides`, including the Company adoption guide), the Videos page and the implementation kit (`/kit/company`). Only the extensions index and the guides' consent-page passage were read. Ingest the Operations page if signed approvals or payments need wire-level detail.

Follow-up entities surfaced by the gVisor project page (Google CNCF post gVisor section + gvisor.dev + repo + cncf/sandbox#521):

- **GKE Sandbox / Cloud Run** (project) — Google products the post says run "millions of sandboxes every day" on gVisor (vendor-reported); GKE Sandbox docs: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods. gvisor.dev shows a "Powered by gVisor" Cloud Run logo.
- **gVisor maintainer and adopter orgs** (organization) — Ant Group, Modal and Tines "committed to joining gVisor's maintainers" (gVisor blog, 2026-10-02), but MAINTAINERS.md still lists only Google on 2026-11-13: re-check before claiming they joined. OpenAI, Tencent and NVIDIA are continuing contributors. Snowflake and Northflank are named users. Anthropic is named as a user via https://www.anthropic.com/engineering/how-we-contain-claude (not read).
- **Etienne Perot, Jing Chen** (person) — authors of the gVisor CNCF blog post; both listed as Google maintainers in MAINTAINERS.md. Perot filed cncf/sandbox#521.
- **gVisor docs** (source follow-up) — not read on 2026-11-13: filesystem/directfs, GPU, TPU, performance guide, users page, Kubernetes quickstart, plus the Tencent agentic-RL sandbox post (gvisor.dev/blog/2026/04/23) and the Ant Group production post (gvisor.dev/blog/2021/12/02). Ingest these before quoting performance numbers.
- **Agent Sandbox API version** (observation) — the gVisor Isolation page's example `Sandbox` uses `apiVersion: agents.x-k8s.io/v1beta1`. The Agent Sandbox page still says neither of its 2 sources states an API group/version. Fold this in during the Agent Sandbox docs follow-up above.

Follow-up entities surfaced by the Google Cloud CNCF donation fiche (cloud.google.com blog, 2026-11-05):

- **OpenRL** (project) — started at Google, donated to the CNCF with Agent Substrate and gVisor; cncf/sandbox#518 closed 2026-10-20 with `gitvote/passed`. "a clean, self-hosted Python post-training loop directly to your Kubernetes cluster", with four primitives (`sample`, `forward_backward`, `optim_step`, `save_state`) "through a Tinker compatible API"; "started in February as a research preview" (year not stated). Sources: https://openrl.dev, https://opensource.googleblog.com/2026/06/introducing-openrl-a-self-hosted-post-training-api-for-fine-tuning-llms.html.
- **gVisor** (project) — ✅ Promoted 2026-11-13 → [wiki/projects/gvisor.md](../wiki/projects/gvisor.md) (the `feat/gvisor` stream, from this same post plus gvisor.dev, the repo and cncf/sandbox#521). Still open: link it from this fiche and from Agent Substrate's `gvisor` sandbox class. Was: 3rd source after Agent Sandbox and Agent Substrate; cncf/sandbox#521 closed 2026-10-28 with `gitvote/passed`; "on a path toward Incubation". Once merged, link it from the fiche and from Agent Substrate's `gvisor` sandbox class.
- **Cloud Native Computing Foundation (CNCF)** (organization) — ★ **2nd source** for the entry above: Google's donation post names the CNCF Sandbox and onboarding. Promotion candidate.
- **Google** (organization) — ★ **4th source** for the entry above: Agent Substrate, gVisor and OpenRL "started at Google" and are donated to the CNCF.
- **kagent** (project) — ★ **2nd source** for the entry above: Substrate "already powers other CNCF projects like kagent".
- **Agent Compute Engine** (project) — Google's "Titanium microVM service" (fast hibernation, parallel environment-forking); the post says Agent Substrate "complements" it. Deep dive: https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive.
- **Nous Research / Hermes Enterprise** (organization/project) — design partner building Hermes Enterprise on Agent Substrate. No source links it to the "Hermes" on ate.dev's framework list.
- **llm-d** (project) — linked from the post's OpenRL section (https://llm-d.ai). KubeRay (cncf/sandbox#525) is linked in the same list of Sandbox issues.
- **Drew Bradstock** (person) — post author, VP Product Management, Orchestration & Kubernetes (Google Cloud).
- **Linked posts not read** (source follow-up) — Agent Substrate on GKE deep dive (https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke), gVisor's move to the CNCF (https://gvisor.dev/blog/2026/10/02/gvisor-cncf/; ✅ read 2026-11-13 and cited on [wiki/projects/gvisor.md](../wiki/projects/gvisor.md)).

Follow-up entities surfaced by the OpenShell fiche (CNCF blog) + project page (NVIDIA/OpenShell repo, ai-openshell org, CNCF records), 2026-11-13:

- **Cedar** (project/concept) — grounding note for the existing Cedar entry above (not edited here): the CNCF post says OpenShell "is adopting Cedar, another CNCF project, as its policy language", and https://www.cncf.io/projects/cedar/ says Cedar was accepted on 2025-10-08 at the Sandbox level. Cedar is now named by 3 ingested sources (Dogwood, Strands Box, OpenShell). Promotion candidate. Repo: `cedar-policy/cedar` (Apache-2.0).
- **Cloud Native Computing Foundation (CNCF)** (organization) — ★ **3rd source** for the CNCF entry above (after Agent Substrate and Google's donation post; entries not edited here): OpenShell is a CNCF Sandbox project (TOC vote 2026-09-26, cncf/sandbox#522), and the launch post is co-written by Jonathan Bryce (CNCF) and Ali Golshan (NVIDIA) on the CNCF blog. Cedar is also a CNCF Sandbox project. Promotion candidate.
- **OpenShell RFC 0020 — Cedar as an alternate sandbox policy language** (source follow-up) — https://github.com/NVIDIA/OpenShell/issues/4610 (open, 2026-10-15); PRs #4564, #4565, #5006 open. Re-check when accepted or merged, then update the Policy section of [OpenShell](../wiki/projects/openshell.md); until then "adopting Cedar as its policy language" is the post's framing, not the shipped state.
- **OpenShell row in the sandbox comparison table** (wiki edit) — [Agent Sandbox](../wiki/projects/agent-sandbox.md#relevance-to-kortex) holds the canonical table; OpenShell was left out on 2026-11-13 because parallel streams edit it. Suggested cells: runs on Docker, Podman, Kubernetes or a VM (Linux, macOS on Apple Silicon, WSL 2 experimental); hides the runtime behind a shared supervisor and policy engine; Landlock + seccomp on the Linux backend; YAML policy with SMT-prover-checked proposals, Cedar proposed.
- **OpenShell docs** (source follow-up) — read on 2026-11-13: `docs/about/{overview,architecture}.mdx` and `docs/how-it-works/policies/{overview,prover}.mdx` only. Unread and worth ingesting for detail: the policy advisor, network rules, providers and inference, gateways, sandboxes/runtimes, isolation backends, supervisor middleware and gateway interceptors, Kubernetes setup and high availability (experimental multi-tenant supervisor), support matrix, telemetry. Rendered at https://docs.nvidia.com/openshell/latest/.
- **NVIDIA** (organization) — contributed OpenShell to the CNCF; 11 of 14 OpenShell maintainers (MAINTAINERS.md, 2026-11-13); runs the PSIRT contact (`psirt@nvidia.com`). Also on the ARD home-page logo wall ([ARD](../wiki/concepts/agentic-resource-discovery-ard.md#governance)). Ali Golshan (NVIDIA) co-wrote the post.
- **Red Hat** (organization) — OpenShell core contributor since inception; 3 of 14 maintainers; Chris Wright (CTO) quoted in the post saying Red Hat will "help steward OpenShell alongside NVIDIA".
- **Docker / Canonical** (organization) — named by the post as OpenShell core contributors since inception; no maintainer seat as of 2026-11-13. No other wiki source describes either yet.
- **Jonathan Bryce, Ali Golshan** (person) — OpenShell post authors; the byline gives only their affiliations (CNCF, NVIDIA), no titles.
- **Chris Wright** (person) — CTO and SVP of Global Engineering, Red Hat (per the post); quoted on open, auditable controls for agents.
- **Microsoft MXC** (project) — native Windows runtime OpenShell points to through a separate Windows build guide; not described further.
- **OpenShell press coverage** (source, unread) — the CNCF project page links The New Stack ("Why Nvidia gave OpenShell to the CNCF") and TechTarget ("Nvidia, Google agent sandboxes meet within CNCF"). Not read; no claims taken from them. The TechTarget headline suggests a comparison with Agent Substrate worth checking.

## Done

- https://personalagentprotocol.org/ → [wiki/sources/ai-protocols-personal-agent-protocol-site-2026.md](../wiki/sources/ai-protocols-personal-agent-protocol-site-2026.md) (fiche, 2026-11-13; also read /docs/introduction, /docs/path-to-1, /docs/roadmap, /docs/changelog, /docs/1.0/spec, /docs/0.1/spec, /docs/1.0/extensions, /docs/1.0/guides (consent-page passage), /docs/demos, /license, /license/contributions and the GitHub repo metadata; enriched [wiki/concepts/personal-agent-protocol-pap.md](../wiki/concepts/personal-agent-protocol-pap.md))
- https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/ → [wiki/sources/ai-protocols-openshell-cncf-2026.md](../wiki/sources/ai-protocols-openshell-cncf-2026.md) (fiche, 2026-11-13)
- https://github.com/NVIDIA/OpenShell → [wiki/projects/openshell.md](../wiki/projects/openshell.md) (project, 2026-11-13; also read the ai-openshell org and `.project` repo, https://www.cncf.io/projects/openshell/, https://www.cncf.io/projects/cedar/ and cncf/sandbox#522)
- https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en → [wiki/projects/gvisor.md](../wiki/projects/gvisor.md) (project, 2026-11-13; gVisor section only)
- https://gvisor.dev/ → [wiki/projects/gvisor.md](../wiki/projects/gvisor.md) (project, 2026-11-13; also read /docs/, the security, platforms and checkpoint/restore pages, /community/governance/, the 2026-10-02 CNCF blog post, the google/gvisor repo and cncf/sandbox#521)
- https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf?hl=en → [wiki/sources/ai-protocols-google-agents-cncf-donation-2026.md](../wiki/sources/ai-protocols-google-agents-cncf-donation-2026.md) (fiche, 2026-11-13; also updated [wiki/projects/agent-substrate.md](../wiki/projects/agent-substrate.md))

- https://agenticresourcediscovery.org/ → [wiki/concepts/agentic-resource-discovery-ard.md](../wiki/concepts/agentic-resource-discovery-ard.md) (concept, 2026-11-03; also read the /spec/, /interoperability/ and /governance/ pages)
- https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/ → [wiki/sources/ai-protocols-ard-google-announcement-2026.md](../wiki/sources/ai-protocols-ard-google-announcement-2026.md) (fiche, 2026-11-03)
- https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/ → [wiki/sources/ai-protocols-ard-aws-agent-registry-2026.md](../wiki/sources/ai-protocols-ard-aws-agent-registry-2026.md) (fiche, 2026-11-03)
- https://huggingface.co/blog/agentic-resource-discovery-launch → [wiki/sources/ai-protocols-ard-hugging-face-discover-2026.md](../wiki/sources/ai-protocols-ard-hugging-face-discover-2026.md) (fiche, 2026-11-03)

- https://ate.dev/ → [wiki/projects/agent-substrate.md](../wiki/projects/agent-substrate.md) (project, 2026-11-02)
- https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/ → [wiki/sources/ai-protocols-agent-sandbox-kubernetes-2026.md](../wiki/sources/ai-protocols-agent-sandbox-kubernetes-2026.md) (fiche, 2026-11-02)
- https://agent-sandbox.sigs.k8s.io/ → [wiki/projects/agent-sandbox.md](../wiki/projects/agent-sandbox.md) (project, 2026-11-02)

- https://aaif.io/news/agentic-ai-foundation-announces-four-new-projects → [wiki/sources/ai-protocols-aaif-four-new-projects-2026.md](../wiki/sources/ai-protocols-aaif-four-new-projects-2026.md) (fiche, 2026-10-27)
- https://aaif.io/blog/training-agents-for-real-world-tasks-with-openenv → [wiki/sources/ai-protocols-openenv-training-agents-2026.md](../wiki/sources/ai-protocols-openenv-training-agents-2026.md) (fiche, 2026-10-27)
- https://aaif.io/blog/the-sandbox-as-an-agent-primitive → [wiki/sources/ai-protocols-opensandbox-agent-primitive-2026.md](../wiki/sources/ai-protocols-opensandbox-agent-primitive-2026.md) (fiche, 2026-10-27)
- https://aaif.io/blog/what-open-responses-changes-for-ai-developers → [wiki/sources/ai-protocols-open-responses-2026.md](../wiki/sources/ai-protocols-open-responses-2026.md) (fiche, 2026-10-27)
- https://www.agentready.org → [wiki/sources/ai-protocols-agentready-standard-2026.md](../wiki/sources/ai-protocols-agentready-standard-2026.md) (fiche, 2026-10-27)
- https://addyosmani.com/blog/agentic-engine-optimization/ → [wiki/sources/addyosmani-agentic-engine-optimization-2026.md](../wiki/sources/addyosmani-agentic-engine-optimization-2026.md) (fiche, 2026-10-24)
- https://github.com/addyosmani/agentic-seo → [wiki/projects/agentic-seo.md](../wiki/projects/agentic-seo.md) (project, 2026-10-24)
- https://agent-plugins.org/ → [wiki/sources/ai-protocols-agent-plugins-spec-2026.md](../wiki/sources/ai-protocols-agent-plugins-spec-2026.md) (fiche, 2026-10-09)
- https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/ → [wiki/sources/ai-protocols-agent-plugins-google-2026.md](../wiki/sources/ai-protocols-agent-plugins-google-2026.md) (fiche, 2026-10-09)

- https://agentskills.io/ → [wiki/sources/ai-protocols-agent-skills-overview-2026.md](../wiki/sources/ai-protocols-agent-skills-overview-2026.md) (fiche, 2026-10-08)
- https://blog.cloudflare.com/clef-decision-models/ → [wiki/sources/ai-protocols-clef-decision-models-2026.md](../wiki/sources/ai-protocols-clef-decision-models-2026.md) (fiche, 2026-10-08)
- https://agents.md/ → [wiki/sources/agents-md-open-format-2026.md](../wiki/sources/agents-md-open-format-2026.md) (fiche, 2026-10-08)
- https://sierra.ai/blog/introducing-personal-agent-protocol → [wiki/sources/sierra-personal-agent-protocol-2026.md](../wiki/sources/sierra-personal-agent-protocol-2026.md) (fiche, 2026-10-08)
- https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact → [wiki/sources/decagon-pact-introduction-2026.md](../wiki/sources/decagon-pact-introduction-2026.md) (fiche, 2026-10-08)
- https://openpactprotocol.org/ → [wiki/sources/openpactprotocol-pact-spec-2026.md](../wiki/sources/openpactprotocol-pact-spec-2026.md) (fiche, 2026-10-08)
- https://x402.org/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications/ → [wiki/sources/ai-protocols-x402-foundation-launch-2026.md](../wiki/sources/ai-protocols-x402-foundation-launch-2026.md) (fiche, 2026-10-08)
- https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ → [wiki/sources/ai-protocols-a2a-agentic-ai-foundation-2026.md](../wiki/sources/ai-protocols-a2a-agentic-ai-foundation-2026.md) (fiche, 2026-10-08)
- https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/ → [wiki/sources/ai-protocols-dogwood-runtime-verification-2026.md](../wiki/sources/ai-protocols-dogwood-runtime-verification-2026.md) (fiche, 2026-10-08)
- https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/ → [wiki/sources/ai-protocols-strands-box-sandboxes-2026.md](../wiki/sources/ai-protocols-strands-box-sandboxes-2026.md) (fiche, 2026-10-08)
