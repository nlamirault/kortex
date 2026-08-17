---
type: Explanation
title: Beyla
description: Grafana Beyla is part of Grafana Labs' open-source observability stack, focusing on "eBPF-based application observability." It is designed to provide insights into application performance metrics and traces without altering application code. Leveragi
tags: ["Monitoring", "Networking", "Observability", "OpenTelemetry", "Tracing"]
timestamp: 2025-02-28T11:01:00Z
---

Grafana Beyla is part of Grafana Labs' open-source observability stack, focusing on "eBPF-based application observability." It is designed to provide insights into application performance metrics and traces without altering application code. Leveraging the extended Berkeley Packet Filter (eBPF) technology, Beyla enables high-fidelity monitoring of applications by gathering low-level data directly from the Linux kernel.

![napkin-selection (13).png](Explanation%20Beyla/napkin-selection_(13).png)

Here's an overview of its architecture:

### 1. **eBPF Integration**

- **eBPF for Data Collection:** Beyla uses eBPF, a powerful Linux kernel technology, to collect metrics and traces directly from the operating system without instrumenting the code. This allows for low-overhead observability, especially useful in environments where application-level metrics are difficult to obtain.
- **Kernel Probes and Tracepoints:** Beyla attaches eBPF probes to functions in the application stack or system calls related to networking, disk I/O, and process scheduling. This approach captures relevant metrics, such as latency, throughput, error rates, and network interactions.

### 2. **User Space Components**

- **Beyla Agent:** This is a lightweight agent that runs on each monitored host. It handles the setup and management of eBPF programs and collects data from them. The Beyla Agent translates raw data from eBPF into structured metrics and traces, suitable for ingestion into observability tools like Grafana.
- **Data Processing Pipeline:** The agent processes data in real time, applying filters and aggregations to reduce data volume while preserving important information. This is critical for maintaining low resource usage, especially in high-throughput environments.

### 3. **Metrics and Traces Export**

- **Prometheus and OpenTelemetry Support:** Beyla is compatible with Prometheus for metrics and OpenTelemetry (OTel) for traces, making it easy to integrate into Grafana’s observability ecosystem. Metrics can be stored in Prometheus, and traces can be sent to a compatible OpenTelemetry endpoint, enabling detailed analysis in Grafana.
- **Customizable Dashboards:** Beyla provides a default Grafana dashboard for visualizing metrics and traces, including latency, request rates, error rates, and other performance metrics. Users can customize dashboards to meet their specific observability requirements.

### 4. **Key Features**

- **Application Performance Monitoring (APM):** Beyla offers a high-level view of application performance with metrics like request durations, error rates, and more, focusing on a distributed microservices environment.
- **Minimal Code Changes:** Because of its reliance on eBPF, Beyla can monitor applications without requiring code changes or manual instrumentation.
- **Resource Efficiency:** Using eBPF minimizes resource consumption, as monitoring logic runs within the kernel. Beyla is designed to reduce the impact on system performance even when monitoring high-throughput applications.

### 5. **Integration with Grafana Stack**

- Beyla seamlessly integrates with other Grafana tools, such as Loki for logs, Tempo for tracing, and Grafana Cloud, providing a full-stack observability solution.
- **Centralized Monitoring and Alerting:** Beyla’s metrics and traces can be centralized in Grafana, enabling monitoring, alerting, and troubleshooting from a single platform.

### Summary

Grafana Beyla’s architecture centers around eBPF-based data collection, processing, and integration with Prometheus and OpenTelemetry. Its low-impact, kernel-level monitoring provides a practical solution for application observability, making it suitable for both traditional and modern cloud-native environments.
