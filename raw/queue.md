# Ingest Queue

## Pending

Follow-up entities surfaced by the Agent Plugins fiches (agent-plugins.org + Google blog):

- **Agent Plugins** (concept/project) — ✅ Promoted 2026-10-09 → [wiki/concepts/agent-plugins.md](../wiki/concepts/agent-plugins.md) (was grounded by 2 sources: spec site + Google announcement).
- **Google** (organization) — joins the Agent Plugins TSC as Core Maintainer (Kevin Hou); ships Agents CLI + Data Agent Kit. First Google-org source in AI Protocols.
- **TSC members** (organization) — Amazon, Cursor, Microsoft, OpenAI, Vercel (Core Maintainers); Amazon/AWS already has an org page.
- **Agents CLI / Data Agent Kit** (project) — Google's first Plugins shippers (expert skills for agent ops; data-cloud skills + MCP servers for BigQuery/Spanner/Cloud SQL).
- **Agentic Resource Discovery (ARD)** (project/concept) — open discovery protocol treating Plugin as a first-class resource type (pre-invocation layer). ★ Now cited by 2 sources (also the AgentReady fiche, as `/.well-known/ai-catalog.json` MAY) — promotion candidate.
- **AI Catalog** (project) — entry format ARD indexes; `application/agent-plugins+json` proposal points at plugin.json.
- **Kevin Hou, Haoyu Wang, Alan Blount** (person) — Google post authors (DeepMind / Cloud Data / Cloud AI).

Follow-up entities surfaced by the Agent Skills fiche (agentskills.io):

- **Agent Skills** (concept) — the portable capability-folder format itself (SKILL.md + scripts/references/assets, progressive disclosure). Promotion candidate on next related ingest.
- **Anthropic** (organization) — originator of the Agent Skills format; released as an open standard.
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
- **Agentic AI Foundation (AAIF)** (organization) — now grounded by a 4th source (A2A, AGENTS.md, MCP-sibling framing, Open Responses). Still top priority for promotion to a full org page.
- **Databricks** (organization) — Model Serving exposes an Open Responses endpoint fronting Claude, Gemini, and open models.
- **Vercel** (organization) — AI Gateway exposes an OpenResponses API.
- **Angie Jones** (person) — author of the Open Responses fiche source (AAIF blog).

## Done

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
