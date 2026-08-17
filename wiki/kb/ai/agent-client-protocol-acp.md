---
type: Explanation
title: Agent Client Protocol (ACP)
description: The **Agent Client Protocol (ACP)** is a standard protocol designed to decouple **code editors** (IDEs, text editors) from **AI coding agents**.
tags: ["AI", "Protocol"]
timestamp: 2026-08-17T08:17:00Z
---

## Overview

The [**Agent Client Protocol (ACP)**](https://agentclientprotocol.com/) is a standard protocol designed to decouple **code editors** (IDEs, text editors) from **AI coding agents**.

It defines a common JSON-based interface that allows any editor to integrate with any AI agent, similar to how the **Language Server Protocol (LSP)** standardized the interaction between editors and programming language servers.

![Gemini_Generated_Image_696n0w696n0w696n.png](Explanation%20Agent%20Client%20Protocol%20(ACP)/Gemini_Generated_Image_696n0w696n0w696n.png)

### Why ACP?

- Today, most editor-to-agent integrations are custom-built, leading to fragmentation and duplicated effort.
- ACP eliminates this by providing a **unified protocol** so that:
    - Any editor that speaks ACP can work with any compatible AI agent.
    - Any AI agent can plug into any ACP-enabled editor.
- This enables **interoperability, flexibility, and richer user experiences**.

## Architecture

### 2.1 JSON-RPC over stdio

- The editor (ACP client) launches the agent as a **subprocess**.
- Communication happens via **JSON-RPC** over **stdin/stdout**.
- ACP reuses many object structures from **MCP (Model Context Protocol)** where possible, but extends them with UX-specific types (e.g., to display diffs or render Markdown output).

### 2.2 Core Principles

- **Interoperability**: works across editors and agents without custom integration.
- **UX-first**: supports rich interactions, progress tracking, multi-buffer handling, code diffs, and Markdown rendering.
- **Trusted local execution**: the agent runs locally, with the editor mediating access to resources.
- **Compatibility with MCP**: agents can use MCP to call external tools and fetch contextual data, while ACP handles the editor ↔ agent interaction.

## Components & Structure

### Main Components

1. **Editor / Client**
    - Launches the agent process.
    - Sends JSON-RPC requests (initialization, prompts, commands).
    - Displays agent responses (Markdown, diffs, etc.).
2. **Agent / Server**
    - Receives and interprets requests from the editor.
    - Can call external tools via MCP or other backends.
    - Returns structured responses for user-facing display.
3. **Transport Layer (JSON-RPC over stdio)**
    - Lightweight, language-agnostic, and flexible communication channel.

### Implementation Details

- JSON schema definitions exist to validate messages.
- Early libraries are available in **TypeScript** and **Rust**.
- Example clients and agents already exist for prototyping.

### Next

[Reference: AI / Protocols](Reference%20AI%20Protocols%202631ec0b77e080c1a2c0cc2674e1d75f.md)
