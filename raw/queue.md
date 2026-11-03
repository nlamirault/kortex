# Ingest Queue

## Pending

Follow-up entities surfaced by the Agent Plugins fiches (agent-plugins.org + Google blog):

- **Agent Plugins** (concept/project) — ✅ Promoted 2026-10-09 → [wiki/concepts/agent-plugins.md](../wiki/concepts/agent-plugins.md) (was grounded by 2 sources: spec site + Google announcement).
- **Google** (organization) — joins the Agent Plugins TSC as Core Maintainer (Kevin Hou); ships Agents CLI + Data Agent Kit. First Google-org source in AI Protocols. ★ **2nd source:** originally created Agent Substrate (ate.dev, 2026-11-02; now a CNCF Sandbox project). Agent Executor, which is built on Substrate, links to `github.com/google/ax`, but the page text never names Google, so that link is URL-only and does not count as a 3rd source.
- **TSC members** (organization) — Amazon, Cursor, Microsoft, OpenAI, Vercel (Core Maintainers); Amazon/AWS already has an org page.
- **Agents CLI / Data Agent Kit** (project) — Google's first Plugins shippers (expert skills for agent ops; data-cloud skills + MCP servers for BigQuery/Spanner/Cloud SQL).
- **Agentic Resource Discovery (ARD)** (project/concept) — open discovery protocol treating Plugin as a first-class resource type (pre-invocation layer). ★ Now cited by 2 sources (also the AgentReady fiche, as `/.well-known/ai-catalog.json` MAY) — promotion candidate.
- **AI Catalog** (project) — entry format ARD indexes; `application/agent-plugins+json` proposal points at plugin.json.
- **Kevin Hou, Haoyu Wang, Alan Blount** (person) — Google post authors (DeepMind / Cloud Data / Cloud AI).

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

- **Ora** (organization) — publisher of AgentReady; runs the measured-agent-behavior studies (1,056-site study, ~50,000-site April 2026 scan, Stripe Link checkout study) and its own agent-readiness ranker.
- **AgentReady** (concept) — the find/read/act checklist discipline itself, distinct from Ora the org; promotion candidate once a 2nd independent source appears.
- **WebMCP** (concept) — W3C Community Group draft; `Act`-stage practice raised from MAY to SHOULD in v2.0.
- **Web Bot Auth** (concept) — listed among the protocols AgentReady says now serve agents (with MCP, WebMCP, A2A, x402, llms.txt); page doesn't bind it to a specific checklist item — ingest its own spec before claiming more.
- **"AX is the New AEO"** (source, arXiv:2609.34951, published as an Ora blog post + paper, 2026-09) — the study AgentReady explicitly attributes its 99%-dead-end-journeys/2.1×-blocked/23%-more-turns finding to (4 agent stacks, Claude + GPT via Tavily). AgentReady's other headline figures (1,056-site 3.7×-omission-rate study, 82%/47% answer-provenance finding) are separate, unnamed Ora traced-run research — do not conflate with this paper on ingest. Ingest for primary-source detail (NOT VERIFIED here beyond AgentReady's citation).
- **UCP / ACP (agent commerce)** (concept) — payment protocols AgentReady lists as `Act`-stage MAY alongside x402 and Stripe Link; ACP name collides with the existing Agent Communication Protocol (IBM/BeeAI) already in the wiki — disambiguate on ingest.
- **NLWeb** (project/concept) — new `Act`-stage MAY practice added in v2.0 (AR-ACT-09).
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
- **Hugging Face** (organization) — OpenEnv maintainer org (Spaces hosting, TRL integration); not yet an org page.
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
- **gVisor** (project) — userspace-kernel isolation backend (intercepts syscalls) documented for Agent Sandbox; site has a dedicated page at https://agent-sandbox.sigs.k8s.io/docs/use-cases/gvisor-isolation/. ★ **2nd source:** Agent Substrate's `gvisor` sandbox class (`runsc`; checkpoint/restore needs `--allow-connected-on-save`). Promotion candidate.
- **Kata Containers** (project) — VM-per-sandbox isolation backend (dedicated kernel, QEMU) for Agent Sandbox; https://agent-sandbox.sigs.k8s.io/docs/use-cases/kata-containers-isolation/. ★ **2nd source:** Agent Substrate's `microvm` class runs a Kata guest on the **Cloud Hypervisor** VMM, not QEMU. Promotion candidate.
- **OpenClaw** (project) — always-on agent environment the site runs inside Agent Sandbox ("Agents in Sandbox"); not described further; https://agent-sandbox.sigs.k8s.io/docs/use-cases/openclaw/. Second mention: listed among the agent frameworks Agent Substrate runs (ate.dev). Neither source describes it.
- **Janet Kuo, Justin Santa Barbara** (person) — Agent Sandbox launch-post authors; byline gives GitHub handles only (janetkuo, justinsb), no affiliations.
- **Agent Sandbox docs** (source follow-up) — Getting Started, Sandbox, Runtime Templates, Volumes, Custom Sandbox pages under https://agent-sandbox.sigs.k8s.io/docs/ — ingest for API group/version, CRD fields, license, and maturity, none of which the two ingested pages state.

Follow-up entities surfaced by the Agent Substrate project page (ate.dev + llms.txt + docs bundle + repo):

- **Cloud Native Computing Foundation (CNCF)** (organization) — hosts Agent Substrate and kagent as Sandbox projects. First ingested source to name CNCF hosting. The [OpenTelemetry](../wiki/concepts/opentelemetry-otel.md) concept page also calls OTel a CNCF project, but only from recall (`NOT VERIFIED`), so link it once that claim is verified. As with Kubernetes, the "a Series of LF Projects, LLC" footer is boilerplate, so do not cite it as Linux Foundation governance.
- **kagent** (project) — CNCF Sandbox project; "a Kubernetes-native framework that runs sandboxed, stateful agent workloads on Agent Substrate"; https://github.com/kagent-dev/kagent.
- **Agent Executor** (project) — "a distributed agent runtime: a secure, hyper-scalable agent harness on Agent Substrate"; https://github.com/google/ax.
- **SPIFFE** (concept) — workload-identity standard. Substrate gives each actor a short-lived SPIFFE X.509 cert and authenticates clients over SPIFFE mTLS or OIDC JWTs.
- **OpenFGA** (project) — authorization engine. `ate-api-server` checks every call against an OpenFGA model.
- **Cloud Hypervisor** (project) — the VMM under Substrate's `microvm` class (with Kata). Fold it into the Kata Containers page unless a 2nd source appears.
- **Agent Substrate docs** (source follow-up) — https://ate.dev/llms-full.txt (~516 KB) bundles every guide. The project page drew only on its Overview, Architecture and Sandbox Classes pages. Ingest the Threat Model, Request Parking, Egress Credential Injection and Version Skew Policy pages for detail. Design-doc drift: the Architecture page (marked "[Status: Planned]") still lists identity and policy under "Problems We Haven't Addressed Yet", although the security guides describe both as shipped. Check against the code, or see whether a later Architecture rewrite fixes it.
- **Agent Substrate demo video** (source) — https://www.youtube.com/watch?v=ZEzkCFJkzjY (~250 actors on 8 pods).

## Done

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
