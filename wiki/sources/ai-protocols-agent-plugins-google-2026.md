---
type: source
title: "Agent Plugins package your skills, tools, and more (Google Developers blog)"
description: Google (Hou/Wang/Blount, 2026-08-06) announces Agent Plugins 1.0.0, joins as Core Maintainer, and details the manifest-fragmentation problem, minimal packaging rules, explicit v1 non-goals, ecosystem layering, and first Google shippers.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
    id: agent-plugins-google-2026
    title: "Agent Plugins package your skills, tools, and more"
generated: {by: opencode/muse-spark-1.3-free, at: 2026-10-09T12:00:00Z}
verified: []
stale_after: 2027-04-09T00:00:00Z
updated: 2026-10-09
tags: [agent-plugins, google, packaging, agent-skills, mcp, discovery, ai-catalog]
---

# Agent Plugins package your skills, tools, and more (Google Developers blog)

**Auteurs :** Kevin Hou, Haoyu Wang, Alan Blount (Google) · **Publié :** 2026-08-06 · **Lien :** https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~10 min

## En Bref

Google announces **Agent Plugins 1.0.0** and joins its Technical Steering Committee as a Core
Maintainer (Kevin Hou). The post frames the core problem as **manifest fragmentation** — portable
Skills and MCP servers trapped in per-client wrappers, forcing forks that drift — and presents
the fix (one directory, two-line manifest, fixed locations, independent failure, explicit
transports, extension namespaces), an explicit v1 non-scope, an ecosystem layering
(discover → describe → package → run), and two shipping Google products (Agents CLI, Data Agent Kit).[^google]

## Points Clés

- **The problem is the manifest, not the components:** Skills and MCP servers are each portable alone; the per-client box (layout, top-level metadata, MCP config shape, transport inference) forces a fork per client and the copies drift.[^google]
- **Minimal packaging rules:** two-line `plugin.json` (`$schema` + `name`); no relocating components, no inline declarations, no configurable discovery path or precedence; missing `skills/` loads what exists; a failing `mcp.json` entry is skipped without taking skills down (independent failure); every MCP entry carries an explicit transport type (stdio, Streamable HTTP, legacy HTTP+SSE).[^google]
- **When NOT to use a plugin:** a single MCP server for a single client is still just `mcp.json`; a single skill needs no plugin — plugins earn their keep when components belong together and must travel together.[^google]
- **Deliberate v1 non-goals:** no install mechanism, distribution protocol, permission model, sandboxing, trust/provenance verification, or UX — named in the spec's future considerations; installation/policy/enterprise controls/approval UX differ genuinely across IDEs, CLIs, and managed platforms.[^google]
- **Ecosystem layering (each independently adoptable):** find via **Agentic Resource Discovery** (Plugin as first-class resource type alongside agents/MCP servers/Skills), describe via **AI Catalog** (`application/agent-plugins+json` proposal), package via Agent Plugins, run via MCP + Agent Skills; shipping in **Agents CLI** (expert skills for agent building/ops) and **Data Agent Kit** (BigQuery/Spanner/Cloud SQL skills + servers).[^google]

## Citation Notable

> "Packaging is unglamorous infrastructure, and unglamorous infrastructure is exactly the kind of thing that should be shared rather than reinvented five times." — Kevin Hou, Haoyu Wang, Alan Blount

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-agent-plugins-google-2026]] | extends | [[source:ai-protocols-agent-plugins-spec-2026]] |
| [[source:ai-protocols-agent-plugins-google-2026]] | implements | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-agent-plugins-google-2026]] | enables | [[concept:tool-use-function-calling]] |

## Liens Wiki

- [Agent Plugins spec fiche](../sources/ai-protocols-agent-plugins-spec-2026.md) — the normative 1.0.0 packaging standard this post announces and adopts.
- [Agent Skills fiche](../sources/ai-protocols-agent-skills-overview-2026.md) — the Skills execution contract packaged inside plugins.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — the tool/service execution contract packaged inside plugins.
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — what packaged skills + servers ultimately drive.
- [AI Protocols](../domains/ai-protocols.md) — the cluster.

[^google]: Kevin Hou, Haoyu Wang & Alan Blount, "Agent Plugins package your skills, tools, and more", Google Developers Blog, 2026-08-06, consulted 2026-10-09.
