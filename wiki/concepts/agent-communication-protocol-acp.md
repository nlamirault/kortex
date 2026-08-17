---
title: Agent Communication Protocol (ACP)
type: concept
status: active
confidence: high
cluster: ai
domain: [ai]
sources: [TMP/KB]
updated: 2026-08-17
tags: [AI, Protocol]
---

## What is ACP?

The [**Agent Communication Protocol (ACP)**](https://agentcommunicationprotocol.dev/) is an open protocol designed to enable interoperability between AI agents, applications, and users. It addresses the growing need for a unified way to connect fragmented ecosystems, providing a standardized REST interface for:

- All modalities (text, structured data, multimodal, etc.)
- Synchronous and asynchronous communication
- Streaming interactions
- **Stateful** and **stateless** operations
- **Online** and **offline** agent discovery
- Execution of **long-running tasks**

ACP is **framework-neutral**, meaning agents built with BeeAI, LangChain, CrewAI, or custom code can interact seamlessly.

It is part of **A2A** under the Linux Foundation, with open and transparent governance: https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/

## Architecture & Core Components

### Core Components

- **ACP Client** – used by an agent, application, or service to send requests to the ACP server.
- **ACP Server** – hosts one or more agents and exposes them via a REST interface to clients.

A process can act as both client and server, which provides flexibility and modularity.

### Architecture Models

1. **Single-agent** – simplest form, ideal for local or isolated use cases.
2. **Multi-agent on a single server** – multiple agents exposed under one HTTP endpoint, with routing by metadata. Easier logging, monitoring, and resource sharing.
3. **Distributed multi-server** – agents spread across multiple servers. Enables scalability, fault tolerance, and polyglot deployments.

---

## Agent Run Lifecycle

ACP defines a clear **lifecycle** for each agent execution (“run”):

1. **created** – request received, not yet running.
2. **in-progress** – processing ongoing.
3. **awaiting** – agent is waiting for extra input (via an “Await” request).
4. **completed** – task finished successfully.
5. **failed** – execution failed with error details.
6. **cancelling → cancelled** – graceful interruption of a run.

This allows for **interactive or incremental workflows**, where an agent can pause and request new information mid-execution.

---

## Discovery & Agent Manifest

- **Agent Manifest**: describes agent identity, capabilities, supported content types, metadata (name, description, license), and runtime status. Required for the server to expose an agent to clients.
- **Agent Discovery**: clients can list available agents via the `/agents` REST endpoint or through the Python SDK.

---

## Message Structure & Metadata

ACP uses a **message-part-based** structure (`MessagePart`) with MIME-typed content.

Recent enhancements include:

- **Trajectory Metadata** – records reasoning steps, tool calls, and state transitions for debugging and explainability.
- **Citation Metadata** – tracks the provenance of information, increasing trust and verifiability.
- **`role` parameter** – distinguishes `user`, `agent`, or `agent/{name}`, improving traceability.

### Next

[Reference: AI / Protocols](Reference%20AI%20Protocols%202631ec0b77e080c1a2c0cc2674e1d75f.md)
