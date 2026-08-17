---
type: Explanation
title: Model Context Protocol (MCP)
description: - MCP is like a universal translator between AI assistants and your everyday apps.
tags: ["AI", "Protocol"]
timestamp: 2026-01-14T10:08:00Z
---

# What is MCP?

- MCP is like a universal translator between AI assistants and your everyday apps.
- Without MCP: AI is limited to what it learned in training (like using an old encyclopedia).
- With MCP: AI can access live information and perform actions in your apps.

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy081akh1ng31owvdq95j.png)

![Akshay-🚀-on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-dive-in.png](Explanation%20Model%20Context%20Protocol%20(MCP)/Akshay--on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-dive-in.png)

## How MCP Works (Key Components)

- User: Asks questions or makes requests in plain language.
- MCP Client: The chat interface where you type your request.
- AI Model: Understands what you're asking for.
- MCP Servers: Special connectors for each service (Gmail, Drive, etc.).
- Your Apps: Where your actual data lives (emails, files, calendar).
    
    ![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpnsencpst8fkresibw6e.png)
    

![Akshay-🚀-on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-div (1).png](Explanation%20Model%20Context%20Protocol%20(MCP)/Akshay--on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-div_(1).png)

- **Hosts:** Applications the user interacts with (e.g., Claude Desktop, an IDE like Cursor, a custom agent).
- **Clients:** Live within the Host application and manage the connection to one specific MCP server. Maintain a 1:1 to connection.
- **Servers:** External programs that expose Tools, Resources and Prompts via standard API to the AI model via the client.

The current components of MCP servers include:

1. **Tools (Model-controlled):** These are functions (tools) that LLMs can call to perform specific actions, e.g. weather API, basically function calling
2. **Resources (Application-controlled):** These are data sources that LLMs can access, similar to GET endpoints in a REST API. Resources provide data without performing significant computation, no side effects. Part of the context/request
3. **Prompts (User-controlled):** These are pre-defined templates to use tools or resources in the most optimal way. Selected before running inference

## Real-World Example

- You ask: "Summarize the emails about Project X and schedule a team meeting."
- AI understands your request and determines it needs access to emails and calendar.
- MCP Servers fetch the relevant emails and check team availability.
- AI creates a summary and schedules the meeting with proper participants.
    
    ![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1nmhc9r8de8l2ipylvwi.png)
    

![Akshay-🚀-on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-div (3).png](Explanation%20Model%20Context%20Protocol%20(MCP)/Akshay--on-X-MCP-is-like-a-USB-C-port-for-your-AI-applications-Just-as-USB-C-offers-a-standardized-way-to-connect-devices-to-various-accessories-MCP-standardizes-how-your-AI-apps-connect-to-different-data-sources-and-tools-Let-s-div_(3).png)

## Everyday Benefits

- Search through files and emails using conversational language.
- Get personalized recommendations based on your actual documents.
- Schedule meetings with automatic time zone adjustments.
- Draft emails with context from multiple sources.
- Organize information across different apps with a single request.
    
    ![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv0fysq6hfe5aowuzgwt2.png)
    

## Why MCP Matters

- Transforms AI from "information only" to "gets things done."
- Keeps your data secure (MCP only accesses what you permit).
- Creates a standard way for any app to connect with AI.
- Allows developers to build new connections for more services.
    
    ![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9a16lw8gqoz50c2vrqqg.png)
    

## In closing

MCP is basically a bridge between a large language model that you speak with (or chat with) and it provides additional capabilities to that large language model, enabling access to external data and information that it previously did not have access to.

You could have an MCP server connected to Claude Desktop app, allowing it to have search functionality. You could also use MCP to enhance the model's interactions through access to external tools and data sources. Additionally, the MCP allows for read and write of files on your computer, so you could have it create projects, create files, or read files to provide additional context to the chat you're having with Claude.

MCP is part of a broader trend toward making AI assistants more capable through tool use and external connectivity, moving beyond the limitations of their training data.

# Next

[Reference: MCP](Reference%20MCP%201cb1ec0b77e08016bcc7cc818fd6d3ec.md)
