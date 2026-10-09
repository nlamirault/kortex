---
type: cache
title: Session Hot Cache
description: Read silently at every session start. ~500 words. Current focus, active pages, open threads.
updated: 2026-10-09
---

# Kortex — Session Hot Cache

> Read this silently at every session start. Replaces recap conversation.
> Update at session end via `/session --close`.

---

## Current Focus

Ingested (2 fiches) **Agent Plugins 1.0.0** (agent-plugins.org spec site + Google Developers
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
