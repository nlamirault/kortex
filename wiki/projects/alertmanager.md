---
title: Alertmanager
type: project
status: active
confidence: high
cluster: observability
domain: [observability]
sources: []
updated: 2025-02-28
tags: [Alerting, Observability]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
---
# Description

Alertmanager is a component of the Prometheus monitoring system that handles alerts sent by Prometheus server and takes care of deduplicating, grouping, and routing them to the correct receiver integration such as email, Slack, PagerDuty, …. It also takes care of silencing and inhibition of alerts.

.png)

Here's a high-level overview of its components and how they interact:

- **Alert Ingestion**: Prometheus servers send alerts to Alertmanager using a simple HTTP-based API. Alerts can also be sent from other sources using the same API or client libraries.
- **Grouping**: Incoming alerts are grouped based on their labels and configuration settings. Grouping prevents notification noise by aggregating similar alerts into a single notification.
- **Inhibition**: Alertmanager supports inhibition rules, which are rules that silence notifications for certain alerts if certain other alerts are already firing. This helps reduce alert noise when a primary issue might cause cascading secondary issues.
- **Silencing**: Users can manually silence alerts based on matchers. Silenced alerts will not send out notifications, but they're still visible in the Alertmanager UI and API.
- **Routing**: Alerts are routed to specific receivers based on their labels and the routing tree defined in the configuration. Routing can direct different types of alerts to different teams or notification methods.
- **Notification**: Once alerts are processed, Alertmanager sends notifications through receivers. Receivers are integration points with various notification channels like email, Slack, PagerDuty, OpsGenie, and more.
- **Deduplication**: Alertmanager deduplicates alerts, ensuring that repeat notifications are not sent for the same alert group during a specified time window.
- **API/UI**: Alertmanager provides a web UI and an API for users to view and manage alerts, silences, and inhibition rules. The API is also used for configuration reloads and status information.
- **Persistence**: Alertmanager stores its state (alerts, silences, etc.) on disk to ensure it retains information across restarts.
- **High Availability**: Alertmanager supports a high-availability configuration, where multiple instances of Alertmanager form a cluster. They communicate with each other to synchronize state and ensure that each instance has the same view of alerts, silences, and so on. This also ensures that notifications are not duplicated across instances.
