---
title: Nats
type: project
status: active
confidence: high
cluster: networking
domain: [networking]
sources: []
updated: 2025-04-18
tags: [Messaging]
---

# Description

It's an open-source messaging platform, often used as a **pub/sub, request/reply, and streaming** messaging system.

### **Key Features of NATS**

- **Pub/Sub Messaging Model**: Publishers send messages to subjects, and subscribers receive only the messages for the subjects they care about.
- **Request/Reply Patterns**: Enables simple RPC (Remote Procedure Call) semantics.
- **Streaming (JetStream)**: Offers durable message storage, acknowledgment, and replay features for persistent systems.
- **High Performance**: Extremely fast (millions of messages per second), with low latency.
- **Ease of Use**: Minimal configuration and designed for developers to start quickly.
- **Scalability**: Handles both small applications and large-scale distributed systems.
- **Multi-Language Support**: Compatible with several programming languages, including Python, Go, Java, C#, and more.

# **Core Components of NATS Architecture**

## **NATS Server (gnatsd)**

- The NATS Server, often referred to as **gnatsd**, is the core messaging engine.
- It routes messages between publishers and subscribers based on subjects (topics).
- It supports clustering for high availability and fault tolerance.
- The server is stateless by default, which keeps it lightweight, but JetStream can be used for persistence.

## **Subjects (Topics)**

- Messages in NATS are organized by **subjects**, which are similar to topics in other messaging systems.
- Subjects use a simple string format (e.g., `user.signup` or `metrics.cpu.usage`).
- Wildcards ( and `>`) can be used for flexible subscription matching.

## **NATS Clients**

- NATS provides client libraries for multiple languages (e.g., Go, Python, Java, C#, etc.).
- These libraries allow applications to act as publishers, subscribers, or both.

## **JetStream (Optional)**

- **JetStream** is the persistence layer for NATS. It adds advanced features like:
    - Durable message storage.
    - Acknowledgments for reliable delivery.
    - Replay capabilities for event streaming.
- JetStream is integrated into the same NATS ecosystem.

# 🔐 Authentication & Authorization

## 🔑 Authentication

NATS supports multiple authentication mechanisms:

1. **No Auth** – for dev/testing.
2. **Token-based Auth**:
    
    ```bash
    authorization {
      token: "s3cr3tt0k3n"
    }
    ```
    
3. **Username/Password**:
    
    ```bash
    authorization {
      users = [
        {user: "alice", password: "pwd123"}
      ]
    }
    ```
    
4. **NKEYS** (Recommended):
    - Public-key based auth.
    - Clients sign a challenge using their private key.
    - More secure than passwords.
5. **JWT (Operator Mode)**:
    - Role-based access with decentralized trust
    - Often used with **NATS Account Server (nats-resolver)**.

## 🛂 Authorization

You can define what subjects a user can **publish** to or **subscribe** from:

```bash
authorization {
  users = [
    {
      user: "alice",
      password: "pwd123",
      permissions = {
        publish = ["foo.*"]
        subscribe = ["foo.bar", "baz.>"]
      }
    }
  ]
}
```
