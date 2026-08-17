---
title: Zigbee
type: concept
status: draft
confidence: low
cluster: domotic
domain: [domotic]
sources: []
updated: 2026-01-06
tags: [Domotic, Protocol]
---

# **Overview**

**Zigbee** is a low-power wireless communication protocol created in the early 2000s.

It’s widely used in smart-home devices such as:

- smart bulbs (Philips Hue, Ikea TRÅDFRI, etc.)
- sensors (motion, temperature, door/window)
- smart plugs and switches

## 🔌 How it works

Zigbee uses a **mesh network**:

- mains-powered devices (like plugs) act as repeaters
- this extends range and improves reliability
- battery-powered sensors consume very little energy

## 🧠 Requires a gateway (hub)

Zigbee devices need a **hub to connect to your network**, for example:

- Philips Hue Bridge
- Aqara Hub
- Sonoff ZB Bridge
- or DIY options like **Zigbee2MQTT** or **ZHA**

👉 Without a hub, Zigbee devices **don’t talk directly to Wi-Fi**.

### 👍 Pros

- mature and reliable technology
- very low power consumption
- large ecosystem of devices

### 👎 Cons

- multiple ecosystems, not always cross-compatible
- requires a proprietary or DIY gateway
- compatibility can be confusing
