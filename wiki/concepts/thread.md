---
title: Thread
type: concept
status: draft
confidence: low
cluster: domotic
domain: [domotic]
sources: [TMP/KB]
updated: 2026-01-06
tags: [Domotic, Protocol]
---

# Overview

**Thread** is a low-power mesh networking protocol, but more modern than Zigbee

The key difference:

👉 **Thread uses IPv6**, meaning devices can communicate natively over IP networks (like the internet).

![thread-data-link-layer.png](Reference%20Thread/thread-data-link-layer.png)

### 🔌 How it works

Thread also creates a **self-healing mesh network**, but:

- it doesn’t rely on a closed, proprietary gateway
- instead, it uses a **Border Router**, often built into devices like:
    - Apple TV / HomePod
    - Google Nest Hub
    - Eero / Nanoleaf routers

The border router simply bridges networks — it is **not a smart-home controller**.

### 👍 Pros

- very low latency
- high reliability
- self-healing mesh network
- designed for modern smart-home use

### 👎 Cons

- still fewer Thread-only devices on the market
- often paired with Matter (see below)
