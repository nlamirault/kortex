---
title: AWS Bedrock AgentCore
type: concept
status: active
confidence: high
cluster: ai
domain: [ai]
sources: []
updated: 2025-12-11
tags: [AI, AWS]
---

# Overview

Amazon Bedrock AgentCore is a comprehensive agent platform offered by AWS that enables the creation, deployment, operation, and monitoring of AI agents at the enterprise level in a secure, reliable manner that is interoperable with any framework or model (open-source or proprietary).

This platform:

- eliminates the infrastructure complexity often required for AI agents,
- adds managed services for memory, security, execution, observability, integrated tools, etc.,
- enables you to work with popular frameworks (e.g., CrewAI, LangGraph, LlamaIndex, Strands, OpenAI Agents SDK).

It can be used within or outside of Amazon Bedrock and is not limited to models integrated into Bedrock.

## 🧩 The 7 Core AgentCore Services

Amazon Bedrock AgentCore consists of **seven tightly integrated services**:

1. **AgentCore Runtime** — Serverless execution environment for deploying and scaling agents.
2. **AgentCore Memory** — Short- and long-term memory management for contextual awareness.
3. **AgentCore Identity** — Secure identity and access management for agent–service interaction.
4. **AgentCore Gateway** — Transforms APIs, Lambdas, and services into agent-ready tools.
5. **AgentCore Code Interpreter** — Sandbox for executing code and performing data transformations.
6. **AgentCore Browser Tool** — Secure cloud browser runtime for web automation and scraping.
7. **AgentCore Observability** — Telemetry, logging, and tracing of agent behavior (OpenTelemetry-compatible).

## 🧭 How It All Fits Together

Here’s the interaction model between the 7 services:

- **AgentCore Runtime** hosts and runs agents.
- **AgentCore Memory** and **Identity** connect directly to Runtime for context and authentication.
- **AgentCore Gateway** links Runtime to external systems.
- **Browser Tool** and **Code Interpreter** are specialized tools that extend agent capabilities.
- **Observability** connects across all layers for tracing, metrics, and auditability.



# Next

https://notebooklm.google.com/notebook/9f18c0c9-d599-4c5f-b341-61f7367262da

https://www.workshops.aws/?tag=AgentCore

https://dev.to/aws-heroes/amazon-bedrock-agentcore-gateway-part-1-introduction-1pjl

https://dev.to/aws-heroes/amazon-bedrock-agentcore-runtime-part-1-introduction-e5i
