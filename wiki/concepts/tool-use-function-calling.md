---
type: concept
title: Tool Use / Function Calling
description: The foundational mechanism by which an LLM invokes external functions through structured output.
status: draft
confidence: low
cluster: ai-protocols
domain: [ai-protocols]
sources: []
generated: {by: anthropic/claude-opus-4-8, at: 2026-10-08T12:00:00Z}
verified: []
stale_after: 2027-04-08T00:00:00Z
updated: 2026-10-08
tags: [tool-use, function-calling, json-schema, agents]
---

# Tool Use / Function Calling

Tool use (also called function calling) is the foundational mechanism by which a large
language model invokes external functions: the model is given a set of tool definitions
(name, description, and a JSON-Schema parameter spec), and when appropriate it emits a
structured call that the host application executes, returning the result to the model.

## Core Idea

A raw LLM only emits text. Tool use turns that into *action*: the model outputs a
structured request (a function name plus arguments conforming to a schema), the runtime
executes the real function, and the output is fed back so the model can continue
reasoning. This request–execute–observe loop is the primitive on which agents are built.

It is deliberately listed here as the **foundational anchor** of the AI-protocols domain.
Strictly, tool use is an API capability rather than a wire protocol, but every
higher-level protocol in this cluster — MCP, A2A, ACP — presupposes it. Understanding
tool use is prerequisite to understanding why those protocols exist.

## Key Properties

- Tools declared with a name, description, and JSON-Schema parameters.
- Model emits a structured call; the host executes it (model never runs code directly).
- Results are returned to the model to continue a reasoning loop.
- Prerequisite primitive for agentic behavior and for MCP/A2A/ACP.

## Relations

| Subject | Predicate | Object |
|---------|-----------|--------|
| [[concept:tool-use-function-calling]] | part-of | [[domain:ai-protocols]] |
| [[concept:tool-use-function-calling]] | used-by | [[concept:model-context-protocol-mcp]] |

## Related

- [AI Protocols](../domains/ai-protocols.md)
- [Model Context Protocol (MCP)](../concepts/model-context-protocol-mcp.md)

## Open Questions

- Where does raw function calling end and a "protocol" (MCP) begin — what does MCP add over plain tool schemas?
- How do schema-validation failures and hallucinated tool calls get handled across implementations?
