---
type: source
title: "Agentic Resource Discovery: Let agents search for tools, skills, and other agents (Hugging Face blog)"
description: Hugging Face (Ben Burtenshaw & Shaun Smith, 2026-06-17) frames ARD as the discovery layer in front of MCP, Skills and A2A, replacing install-first with intent search. It ships hf-discover, a reference implementation over Hub semantic search exposed via the hf CLI, REST /search and MCP.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://huggingface.co/blog/agentic-resource-discovery-launch
    id: ard-hf-2026
    title: "Agentic Resource Discovery: Let agents search for tools, skills, and other agents"
  - resource: https://github.com/ards-project/ard-spec/blob/main/adr/0008-mcp-media-type-renaming.md
    id: ard-repo
    title: "ARD ADR-0008: Renaming MCP Media Type to application/mcp-server-card+json"
  - resource: https://huggingface.co/.well-known/ai-catalog.json
    id: hf-catalog-probe
    title: "Hugging Face ai-catalog.json (live HTTP probe, 2026-11-03)"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-03T00:00:00Z}
verified: []
stale_after: 2027-05-03T00:00:00Z
updated: 2026-11-03
tags: [ard, discovery, hugging-face, hf-discover, agent-skills, mcp, a2a, spaces, reference-implementation]
---

# Agentic Resource Discovery: Let agents search for tools, skills, and other agents (Hugging Face blog)

**Auteurs :** Ben Burtenshaw & Shaun Smith (Hugging Face) · **Publié :** 2026-06-17 · **Lien :** https://huggingface.co/blog/agentic-resource-discovery-launch
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~6 min

## En Bref

MCP gives agents tools, Skills give them instructions, and A2A gives them other agents. All three
"assume the user already knows which tool, instruction, or agent they need". Hugging Face presents
ARD as the **discovery layer that sits in front of them**: a draft open spec, "not a product or a
marketplace". It replaces *install-first, use-later* with intent-based search that runs outside
the LLM. The post ships the **Hugging Face Discover Tool (`hf-discover`)** as a reference
implementation that wraps Hub search in ARD's envelope.[^ard-hf-2026] The spec mechanics are on
the [ARD concept page](../concepts/agentic-resource-discovery-ard.md).

## Points Clés

- **Install-first does not scale.** Hardcoded MCP URLs and pre-connected plugins work for the few
  tools used daily. The fallback, putting every tool description in the context window, hits the
  context budget, and descriptions "are often too thin to disambiguate well". ARD moves selection
  outside the LLM. Registries index richer signals (publisher identity, representative queries,
  compliance attestations, tags) and expose a REST endpoint.[^ard-hf-2026]
- **The spec as of the post.** A static `ai-catalog.json` manifest at a well-known URL, plus a
  dynamic `POST /search` API for live, ranked discovery.[^ard-hf-2026] *Dated:* spec v0.91
  (2026-08-26) moved the manifest to `/.well-known/ard.json` (see the
  [concept page](../concepts/agentic-resource-discovery-ard.md)).
- **How `hf-discover` works.** It combines the Hub's semantic search over Spaces (the
  `agents=true` flag) with HF Agent Skills. It returns only Spaces whose runtime stage is
  `RUNNING`. The request picks the media type of the result:
  - `application/ai-skill` (the default) is a generated `SKILL.md` that wraps the Space's own
    `agents.md` in name, description and source frontmatter.
  - An MCP entry points at the Space's Gradio MCP endpoint over HTTP.
  - `application/vnd.huggingface.space+json` is the raw Space metadata.

  The MCP type is inconsistent within the post. The prose says `application/mcp-server+json`,
  while the curl example uses `application/mcp-server-card+json`.[^ard-hf-2026] The prose has the
  pre-rename name. ARD's ADR-0008 renamed the type to `-card+json` so that it names the
  discovery card, not the live MCP stream, in parallel with A2A's `a2a-agent-card+json`.[^ard-repo]
  HF's live catalog used the new name on 2026-11-03.[^hf-catalog-probe]
- **Three ways in.** The `hf` CLI: `hf discover search "…"`, with `--json`, `--kind mcp` and
  `--registry-url`. REST: `POST https://huggingface-hf-discover.hf.space/search` with
  `query.text`, `query.filter.type` and `pageSize`. MCP: `/mcp` on the same host. The HF catalog
  is published at `https://huggingface.co/.well-known/ai-catalog.json`.[^ard-hf-2026]
- **The design lesson and next steps.** Because the envelope is driven by media type, "any
  artifact protocol can ride the same envelope without specification-level changes". Discover
  invents no new artifact format; the same Space can surface as a skill or as an MCP server. Next
  on the roadmap: the federation modes (`auto`, `referrals`, `none`) and Hub support for static
  manifests on user and organization profiles.[^ard-hf-2026]

## Citation Notable

> "It is not a product or a marketplace. It is a shared standard that any company can implement independently, and that any agent or tool can participate in." — Ben Burtenshaw & Shaun Smith

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-ard-hugging-face-discover-2026]] | argues-that | [[concept:agentic-resource-discovery-ard]] |
| [[source:ai-protocols-ard-hugging-face-discover-2026]] | contrasts-with | [[concept:model-context-protocol-mcp]] |
| [[source:ai-protocols-ard-hugging-face-discover-2026]] | contrasts-with | [[concept:agent2agent-a2a]] |
| [[source:ai-protocols-ard-hugging-face-discover-2026]] | enables | [[concept:tool-use-function-calling]] |

## Liens Wiki

- [Agentic Resource Discovery (ARD)](../concepts/agentic-resource-discovery-ard.md): the canonical spec page. Shaun Smith co-authored v0.91 and holds HF's Oversight Board seat.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md) / [Agent2Agent (A2A)](../concepts/agent2agent-a2a.md): two of the three invocation protocols ARD "sits in front of".
- [Agent Skills fiche](ai-protocols-agent-skills-overview-2026.md): the third. Discover's default result is a generated `SKILL.md`. The post does not say whether each Space's `agents.md` follows the [AGENTS.md](../concepts/agents-md.md) convention, so the two are not equated here.
- [OpenEnv fiche](ai-protocols-openenv-training-agents-2026.md): another Hugging Face-maintained agent project in this wiki.
- [Announcing the ARD specification (Google blog)](ai-protocols-ard-google-announcement-2026.md): the companion launch-day post.
- [AI Protocols](../domains/ai-protocols.md): the cluster.

[^ard-hf-2026]: Ben Burtenshaw & Shaun Smith, "Agentic Resource Discovery: Let agents search for tools, skills, and other agents", Hugging Face blog, 2026-06-17, consulted 2026-11-03 (page HTML fetched and read directly). The community comments under the post were not used.
[^ard-repo]: ards-project/ard-spec, `adr/0008-mcp-media-type-renaming.md` (status Accepted, undated), consulted 2026-11-03 via the GitHub API.
[^hf-catalog-probe]: HTTP GET of https://huggingface.co/.well-known/ai-catalog.json and https://huggingface.co/.well-known/ard.json, 2026-11-03. This is a point-in-time observation, not a published claim.
