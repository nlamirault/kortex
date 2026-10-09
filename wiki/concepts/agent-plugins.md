---
type: concept
title: Agent Plugins
description: Open, vendor-neutral packaging standard bundling Agent Skills and MCP servers into one portable plugin directory (plugin.json + fixed locations + client extension namespaces).
status: draft
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agent-plugins.org/
    id: agent-plugins-spec-2026
    title: "Agent Plugins (agent-plugins.org)"
  - resource: https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
    id: agent-plugins-google-2026
    title: "Agent Plugins package your skills, tools, and more"
generated: {by: opencode/muse-spark-1.3-free, at: 2026-10-09T12:00:00Z}
verified: []
stale_after: 2027-04-09T00:00:00Z
updated: 2026-10-09
tags: [agent-plugins, packaging, agent-skills, mcp, interoperability, plugin-format]
---

# Agent Plugins

Agent Plugins is an **open, vendor-neutral packaging standard (v1.0.0)** for bundling reusable
agent components — **Agent Skills** and **MCP servers** — into a single portable plugin directory,
so one package loads consistently across compatible clients.[^spec][^google]

## Core Idea

AI agent clients each invented their own plugin wrapper around identical underlying components:
different directory layouts, different manifest metadata, different MCP config shapes with
transport inferred from object shape. Authors shipping to a second client had to fork the package
and maintain drifting copies of components that were never different. Agent Plugins fixes the
**manifest, not the components** — Skills and MCP servers were each portable alone; the box was not.[^google]

The fix is deliberately small: a plugin is a directory with a required two-line `plugin.json`
(`$schema` + `name`) and components at **fixed locations** — `skills/` (one subdirectory per
skill, in Agent Skills format), `mcp.json` (every server entry carrying an explicit transport:
stdio, Streamable HTTP, or legacy HTTP+SSE) — plus **reverse-domain extension namespaces**
(e.g. `com.example.client/`) where individual clients add hooks, commands, or agents without
touching the portable core. The manifest cannot relocate components or declare them inline;
there is no discovery path to configure and no precedence order to learn. Components fail
independently: a missing `skills/` loads what exists, and a failing MCP entry is skipped and
reported without taking skills down.[^spec][^google]

Version 1 is a package format and nothing more. Install mechanisms, distribution, permission
models, sandboxing, trust/provenance verification, and UX are explicit non-goals (named in the
spec's future considerations), because IDEs, CLIs, and managed enterprise platforms have
genuinely different obligations to their users. Packaging sits in a layered ecosystem where each
layer is independently adoptable: discover via Agentic Resource Discovery (Plugin as a
first-class resource type), describe via AI Catalog (`application/agent-plugins+json`), package
via Agent Plugins, run via MCP + Agent Skills. Governance is open (spec repo, public proposals
via GitHub Discussions, Discord); the Technical Steering Committee's Core Maintainers span
Amazon, Cursor, Microsoft, OpenAI, and Vercel, with Google joining on publication.[^google]

## Key Properties

- **Portable directory:** `plugin.json` + `skills/` + `mcp.json` + reverse-domain client namespaces; unrecognized namespaces are ignored by other clients.[^spec]
- **Single-skill / single-server rule:** one skill needs no plugin, one MCP server for one client is still just `mcp.json` — plugins earn their keep when components belong together and travel together.[^google]
- **Explicit transports:** no guessing stdio vs HTTP from config shape; every `mcp.json` entry declares its type.[^google]
- **Client innovation preserved:** distribution, install, permissions, approval UX, and client-specific capabilities stay under each client's control.[^spec]
- **Shipped by Google first:** Agents CLI (expert skills for agent building/ops) and Data Agent Kit (BigQuery/Spanner/Cloud SQL skills + servers) support the format at launch.[^google]

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:agent-plugins]] | part-of | [[domain:ai-protocols]] |
| [[concept:agent-plugins]] | implements | [[concept:model-context-protocol-mcp]] |
| [[concept:agent-plugins]] | contrasts-with | [[concept:agents-md]] |
| [[concept:agent-plugins]] | enables | [[concept:tool-use-function-calling]] |
| [[concept:agent-plugins]] | described-by | [[source:ai-protocols-agent-plugins-spec-2026]] |

## Related

- [AI Protocols](../domains/ai-protocols.md) — the cluster.
- [Agent Plugins spec fiche](../sources/ai-protocols-agent-plugins-spec-2026.md) — the normative 1.0.0 source.
- [Agent Plugins (Google blog) fiche](../sources/ai-protocols-agent-plugins-google-2026.md) — announcement + adoption source.
- [Agent Skills fiche](../sources/ai-protocols-agent-skills-overview-2026.md) — the Skills format packaged in `skills/`.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) — the server format packaged in `mcp.json`.
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — what packaged skills + servers ultimately drive.
- [AGENTS.md](../concepts/agents-md.md) — sibling contrast: portable plugin core vs per-repo instructions and client-owned behavior.

## Open Questions

- Who else beyond Google ships Plugins support, and does the TSC roster change fast enough to track per-release?
- Do Agents CLI / Data Agent Kit plugins validate against the published JSON Schemas without client-specific drift?
- When (if ever) do the deferred layers — distribution, permissions, trust/provenance — get standardized, and by whom?

[^spec]: agent-plugins.org, "Agent Plugins", consulted 2026-10-09.
[^google]: Kevin Hou, Haoyu Wang & Alan Blount, "Agent Plugins package your skills, tools, and more", Google Developers Blog, 2026-08-06, consulted 2026-10-09.
