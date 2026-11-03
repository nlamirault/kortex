---
type: source
title: "Agentic Resource Discovery (ARD): An open specification for agent discovery (AWS blog)"
description: AWS (Damick, Mangal & Talluri, 2026-08-24) presents AWS Agent Registry (preview) as a curated in-account catalog. It argues that multi-cloud, on-prem and SaaS estates need ARD as a shared spec so that "publishers describe once and consumers discover everywhere", likened to DNS.
format: fiche
status: stable
confidence: medium
cluster: ai-protocols
domain: [ai-protocols]
sources:
  - resource: https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
    id: ard-aws-2026
    title: "Agentic Resource Discovery (ARD): An open specification for agent discovery"
generated: {by: anthropic/claude-opus-5-5, at: 2026-11-03T00:00:00Z}
verified: []
stale_after: 2027-05-03T00:00:00Z
updated: 2026-11-03
tags: [ard, discovery, aws, agent-registry, bedrock-agentcore, federation, dns, mcp]
---

# Agentic Resource Discovery (ARD): An open specification for agent discovery (AWS blog)

**Auteurs :** Jeffrey Damick (Principal Software Engineer, Amazon Route 53), Anubhav Mangal (Principal Product Manager, Amazon Bedrock AgentCore), Bhargav Talluri (Senior Manager, Product Management: Route 53 and agent identity and discovery in AWS Agent Registry) · **Publié :** 2026-08-24 · **Lien :** https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
**Domaine :** [AI Protocols](../domains/ai-protocols.md) · **Lecture :** ~5 min

## En Bref

AWS presents **AWS Agent Registry** (preview) as the answer to discovery *inside* an AWS
environment. It then argues that enterprises spread across clouds, on-prem and SaaS need a
shared specification so that "publishers describe once and consumers discover everywhere". That
specification is ARD. The post casts ARD as the interoperability layer, with Agent Registry's
access controls remaining the enforcement point. The framing is forward-looking ("we expect"):
AWS says only that it "contributed feedback during the spec's development".[^ard-aws-2026] The
spec itself is on the [ARD concept page](../concepts/agentic-resource-discovery-ard.md).

## Points Clés

- **AWS Agent Registry (preview)** catalogs agents, MCP servers, tools, agent skills and custom
  resources. It is built on *registries* and *registry records*. A registry has its own
  authorization and approval settings and can be org-wide or split by resource type, stage or
  team; cross-account sharing extends it to a whole AWS Organization. A record describes what a
  resource is, what it does and how to reach it.[^ard-aws-2026]
- **A four-role workflow.** An administrator creates the registry and sets authorization (IAM, or
  a JWT from the corporate identity provider). A publisher submits records. A curator approves,
  rejects or deprecates them. Consumers, human or AI agent, search what has been approved.
  Enterprise features: curation, hybrid semantic and keyword search, a remote **MCP endpoint**,
  and flexible authorization.[^ard-aws-2026]
- **The multi-environment problem.** Each environment has its own registry, naming convention and
  metadata schema, so connecting them takes "bespoke connectors for every pair of registries".
  A shared format and protocol remove that per-pair work.[^ard-aws-2026]
- **The DNS analogy.** ARD enables federation across registries "analogous to how the Domain Name
  System (DNS) enables name resolution across networks". Local registries federate "without
  requiring bilateral agreements or proprietary connectors".[^ard-aws-2026]
- **A complement, not a replacement, and stated as expectations.** The post lists three
  benefits. *Federate without migrating.* *Discover globally, control locally*: the publisher
  controls what is in its catalog, who sees it and when access is revoked. *Public discovery*:
  any organization can publish a catalog on its own domain. The post does not claim that ARD
  support in the registry has shipped.[^ard-aws-2026]

## Citation Notable

> "If every registry describes resources in the same format and exposes discovery through a common protocol, publishers describe once and consumers discover everywhere." — Jeffrey Damick, Anubhav Mangal & Bhargav Talluri

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[source:ai-protocols-ard-aws-agent-registry-2026]] | argues-that | [[concept:agentic-resource-discovery-ard]] |
| [[source:ai-protocols-ard-aws-agent-registry-2026]] | created-by | [[organization:aws]] |

## Liens Wiki

- [Agentic Resource Discovery (ARD)](../concepts/agentic-resource-discovery-ard.md): the spec this post positions Agent Registry against. ARD's governance page lists Jeffrey Damick as Amazon's Oversight Board member.
- [Amazon Web Services (AWS)](../organizations/aws.md): the publisher. This adds Agent Registry to AWS's agent stack next to Dogwood, Strands Box and Bedrock AgentCore.
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md): the registry serves search over a remote MCP endpoint and indexes MCP servers.
- [Announcing the ARD specification (Google blog)](ai-protocols-ard-google-announcement-2026.md): Google's launch post. Google Cloud also has a product called "Agent Registry"; it is a different product.
- [ARD at Hugging Face (Hugging Face blog)](ai-protocols-ard-hugging-face-discover-2026.md): the shipped reference implementation, for contrast with AWS's stated expectations.
- [AI Protocols](../domains/ai-protocols.md): the cluster.

[^ard-aws-2026]: Jeffrey Damick, Anubhav Mangal & Bhargav Talluri, "Agentic Resource Discovery (ARD): An open specification for agent discovery", AWS Artificial Intelligence Blog (category Amazon Bedrock AgentCore), 2026-08-24, consulted 2026-11-03 (page HTML fetched and read directly; author roles from the post's "About the authors").
