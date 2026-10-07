# Kortex — Session Hot Cache

> Read this silently at every session start. ~500 words. Replaces recap conversation.
> Update this file at session end via `/close`.

---

## Current Focus

*(What is the active work or research thread?)*

Ingested the **Personal Agent Protocol (PAP)** — open standard (Meta + Sierra) for direct,
secure communication between a consumer's personal AI agent and a business, replacing
human-style website navigation with OAuth-authenticated machine-to-business sessions.
New: [PAP](concepts/personal-agent-protocol-pap.md), [source](sources/sierra-personal-agent-protocol-2026.md),
[Bret Taylor](people/bret-taylor.md), [Clay Bavor](people/clay-bavor.md),
[Meta](organizations/meta.md), [Sierra](organizations/sierra.md).
Sits in the AI protocols cluster alongside MCP/A2A/UCP — the consumer-agent↔business layer.

Prior: **Unified Harness Protocol (UHP)** — an open standard for driving complete
agent harnesses as shared infrastructure (task-in / running-agent-out, Responses-API-shaped).
[UHP](concepts/unified-harness-protocol-uhp.md), [Agent Harness](concepts/agent-harness.md),
[HarnessRouter](projects/harnessrouter.md), [UHP source](sources/uhp-website-2026.md).

Earlier: two HTTP-402 payment protocols in the agentic-payments cluster:
- **Machine Payments Protocol (MPP)** — machine-to-machine payments by Tempo Labs & Stripe. [MPP](concepts/machine-payments-protocol-mpp.md), [Tempo](projects/tempo.md), [MPP Specs](sources/mpp-specs.md).
- **x402** — internet-native payment protocol (HTTP 402 + stablecoin settlement). [x402](concepts/x402.md), [x402.org source](sources/x402-org-2026.md).

---

## Open Questions

*(Unresolved questions blocking progress or needing investigation)*

- None yet.

---

## Recent Decisions

*(Decisions made in recent sessions — schema changes, direction pivots)*

- 2026-09-01: Adopted WikiSkill evolution loop (ADR-0001) — `/evolve`, `patterns/`, `skill-impact.md`, `## Purpose` on all skills.
- 2026-05-04: Initialized wiki structure using Karpathy LLM Wiki protocol v1.
- 2026-05-04: Added `confidence`, `cluster` frontmatter fields to all entity types.
- 2026-05-04: Added `comparisons/` entity type for side-by-side source analysis.

---

## Last Operations

*(Last 3–5 operations from `wiki/log.md` — copy on `/close`)*

- `[INGEST]` 2026-10-07 — Personal Agent Protocol (PAP), Meta/Sierra: concept + source + 2 people + 2 orgs
- `[INGEST]` 2026-09-23 — Unified Harness Protocol (UHP) landing page + spec index
- `[UPDATE]` 2026-09-01 — Adopted WikiSkill evolution loop (ADR-0001): /evolve, patterns/, skill-impact ledger
- `[INIT]` 2026-05-04 — Bootstrapped Kortex wiki structure
- `[UPDATE]` 2026-05-04 — Expanded schema with Three-Layer Architecture and operations

---

## Active Pages

*(Pages currently being built or needing follow-up)*

- `wiki/concepts/personal-agent-protocol-pap.md` — new, medium confidence; v0.1 spec/governance/reference-impl all `NOT VERIFIED` (announced, not yet published). Re-verify after late-Oct-2026 spec drop.
- `wiki/people/{bret-taylor,clay-bavor}.md` — new; bios kept minimal, prior roles `NOT VERIFIED`
- `wiki/concepts/unified-harness-protocol-uhp.md` — new, unverified; verify against the 11-chapter spec + conformance suite
- `wiki/projects/harnessrouter.md` — new, medium confidence; GitHub URL/details inferred from landing page, `NOT VERIFIED`
- `wiki/concepts/machine-payments-protocol-mpp.md` — new, unverified; verify against spec before trusting
- `wiki/projects/tempo.md` — new, unverified
- `concepts/x402.md` — facilitator role + supported chains still `NOT VERIFIED`; confirm from primary sources
- `wiki/overview.md` — stub, needs clusters as domains are added
- `wiki/hot.md` — this file, update on `/close`

---

## Pending Ingests

*(mirrors `raw/queue.md` pending count — update on `/close`)*

- raw/queue.md: 0 pending

---

## Known Failures

*(Dead-ends recorded to prevent repetition)*

- None yet.
