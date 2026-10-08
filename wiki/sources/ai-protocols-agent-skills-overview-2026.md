---
type: source
title: "Agent Skills — standardized way to give AI agents new capabilities"
description: The agentskills.io home — Agent Skills as an open folder-based format (SKILL.md + scripts/references) loaded via progressive disclosure; originated at Anthropic, broadly adopted across coding agents.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://agentskills.io/
    id: agentskills-2026
    title: "Agent Skills Overview (agentskills.io)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [agent-skills, skill-md, agents, capability-format, anthropic, progressive-disclosure]
---

# Agent Skills — standardized way to give AI agents new capabilities

**Éditeur :** agentskills.io (project site) · **Consulté :** 2026-10-08 · **Lien :** https://agentskills.io/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

Agent Skills are a lightweight, **open folder-based format** (`SKILL.md` + optional scripts,
references, assets) that packages procedural knowledge and team-specific context so agents can
load it on demand. Skills load via **progressive disclosure** (discovery → activation →
execution), keeping context footprint small. The format originated at **Anthropic**, was
released as an open standard, and is now supported by a large client roster (Claude Code,
Cursor, VS Code, GitHub Copilot, Gemini CLI, OpenCode, goose, Codex, and more).[^agentskills]

## Points Clés

- **Folder format:** a skill is a folder with a required `SKILL.md` (metadata `name` + `description` minimum, plus instructions); optional `scripts/`, `references/`, `assets/` bundles. Full docs at the site's Quickstart and Specification pages.[^agentskills]
- **Progressive disclosure in 3 stages:** (1) Discovery — agents load only name+description at startup; (2) Activation — matching task reads full `SKILL.md`; (3) Execution — agent follows instructions, running bundled code/refs as needed.[^agentskills]
- **Why:** agents lack reliable context for real work; skills give them **domain expertise**, **repeatable multi-step workflows**, and **cross-product reuse** (build once, use across any compatible agent).[^agentskills]
- **Broad adoption claimed:** dozens of listed clients with per-client instruction links (Junie, Gemini CLI, OpenCode, Cursor, Amp, Copilot, VS Code, Claude Code, Codex, goose, Kiro, Spring AI, and more); open development via GitHub + Discord.[^agentskills]
- **Positioning vs per-repo instructions:** unlike a repo-root instruction file (AGENTS.md tells an agent *how to work in this repo*), a skill is a **portable capability package** loadable across products — complementary, not competing.[^agentskills]

## Citation Notable

> "A standardized way to give AI agents new capabilities and expertise."

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-agent-skills-overview-2026]] | contrasts-with | [[concept:agents-md]] |
| [[source:ai-protocols-agent-skills-overview-2026]] | enables | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-agent-skills-overview-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [AGENTS.md](../concepts/agents-md.md) — per-repo instruction file; closest sibling convention (portable skill vs repo-root context).
- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — skills package repeatable multi-step procedures that include tool calls.
- [AI Protocols](../domains/ai-protocols.md) — the cluster.

[^agentskills]: agentskills.io, "Agent Skills Overview", consulted 2026-10-08.
