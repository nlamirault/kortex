---
type: source
title: "Introducing Clef: our open-source decision models, and new RL fine-tuning platform"
description: Cloudflare releases Clef and Clef-flash — open-source "decision models" that return bounded, typed, probability-weighted classifications so agent code can route, escalate, or defer to a human — plus an RL fine-tuning service on Workers AI.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://blog.cloudflare.com/clef-decision-models/
    id: clef-cf-2026
    title: "Introducing Clef (Cloudflare Blog)"
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T00:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [decision-models, classification, agents, workers-ai, cloudflare, inference, reinforcement-learning, calibration]
---

# Introducing Clef: our open-source decision models, and new RL fine-tuning platform

**Auteurs :** Michelle Chen, Alex Reneau, Kevin Flansburg · **Publié :** 2026-10-01 · **Lien :** https://blog.cloudflare.com/clef-decision-models/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~10 min

## En Bref

Cloudflare releases **Clef** and **Clef-flash**, a family of open-source *decision models* (not a
protocol) hosted on Workers AI. A decision model answers a narrow question — classify a support
message, label a domain — with a bounded, **typed** output and a probability, so ordinary code can
route a ticket, trigger an escalation, or defer to a person without a slow, open-ended LLM in the
loop.[^clef] It matters to this domain because it gives agents a fast, deterministic **decision
layer** for routing and tool-selection decisions, complementing (not replacing) function-calling.

## Points Clés

- **Decision models vs LLMs:** they return typed answers with probabilities for narrow questions and can add new categories without retraining — unlike open-ended, non-deterministic general LLMs.[^clef]
- **Two variants, vendor-reported leadership:** Clef (precision) and Clef-flash (latency-critical); Cloudflare reports median latency of **209.3 ms** (Clef) and **38.8 ms** (Clef-flash) vs Jev's **524.1 ms**, says Clef leads the **Jev Decision Index**, and that both are **Jev-API compatible**.[^clef]
- **Architecture:** built by **freezing** a Qwen base (Qwen3.8-27B for Clef, Qwen3.5-9B for Clef-flash) and jointly training a routing head with **rank-256 low-rank adapters**; inference does a **prefill-only** pass, then scores the valid schema choices **in parallel** — the decision step is **non-autoregressive**, so no token-by-token text is generated. Adds a **64k** context window (Jev's 32k) and a **vision encoder** for image classification.[^clef]
- **Training for calibration:** label-smoothed cross-entropy plus **Brier loss** for calibration, plus a new RL method, **RLCD (Reinforcement Learning for Calibrated Decisions)**, as a secondary optimization target granting partial credit.[^clef]
- **Open + hosted + tunable:** fully open-sourced on **Hugging Face** under **Apache 2.0** and hosted on **Workers AI**; a new **RL fine-tuning service** ships first via a forward-deployed engineer (FDE) team, with a self-serve platform planned later.[^clef]

In a Cloudflare Threat Intelligence test classifying website domains, Cloudflare reports Clef (with
Browser Run) took **2.2 s** to fetch, render, and classify, while `gpt-oss-120b` took **4.7 s** and
returned only two classifications.[^clef] All benchmark and latency figures come from Cloudflare's
own evaluation.

## Citation Notable

> "A decision model will return typed answers with probabilities (outputs), which your code can use to route the ticket, trigger an escalation, or defer to a human." — Cloudflare Blog

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-clef-decision-models-2026]] | enables | [[concept:tool-use-function-calling]] |
| [[source:ai-protocols-clef-decision-models-2026]] | extends | [[domain:ai-protocols]] |

## Liens Wiki

- [Tool Use / Function Calling](../concepts/tool-use-function-calling.md) — Clef is scored on function-calling and tool-retrieval benchmarks (BFCL, ToolRet, API-Bank); it acts as the typed decision layer in front of tool selection and when-to-call, rather than generating the call itself.
- [AI Protocols](../domains/ai-protocols.md) — adds a fast, deterministic decision/classification layer to the agent stack that sits beneath open-ended LLM reasoning.

[^clef]: Cloudflare Blog, "Introducing Clef: our open-source decision models, and new RL fine-tuning platform", Michelle Chen, Alex Reneau, Kevin Flansburg, 2026-10-01. All benchmark, latency, and architecture figures are vendor-reported from Cloudflare's own evaluation.
