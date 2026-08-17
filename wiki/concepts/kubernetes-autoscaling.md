---
title: Kubernetes Autoscaling
type: concept
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: [TMP/KB]
updated: 2025-02-28
tags: [Kubernetes]
---

# **Scaling Methods in Kubernetes**

If you are unfamiliar with scaling in Kubernetes, there are three primary components to understand:

![](https://www.nops.io/wp-content/uploads/2023/06/Different-Methods-for-Autoscaling-in-Kubernetes.png)

![image (1).png](Explanation%20Kubernetes%20Autoscaling/image_(1).png)

# **Cluster Autoscaling**

Kubernetes clusters are constrained by the CPU and memory capacity of their worker nodes. As applications within a cluster scale, they will eventually surpass the cluster's available capacity. The solution to this problem is Cluster Autoscaling. Cluster Autoscaling focuses on the infrastructure layer instead of individual pods. A Cluster Autoscaler will dynamically add or remove new worker nodes to the cluster depending on the current utilization.  The Cluster Autoscaler lives inside the Kubernetes cluster as a Controller that communicates to your Cloud Provider via API calls to provision new servers.

![image.png](Explanation%20Kubernetes%20Autoscaling/image.png)

Tools:

![image (1).png](Explanation%20Kubernetes%20Autoscaling/image_(1)%201.png)

## **Cluster Autoscaler**

Cluster Autoscaler is the standard tool for managing cluster nodes dynamically, and has support for autoscaling Kubernetes across more than twenty different cloud providers.

Benefits:

- Broad applicability with support for more than twenty different cloud providers
- Fast and reliable scale-up behavior

Challenges:

- Node pool configuration is very static
- Limited control over node type selection for scale-up and scale-down events
- Conservative scale-down behavior

## **Karpenter**

[Karpenter](https://karpenter.sh/) is an advanced project that replaces the use of cluster autoscaler. Initially released by AWS in 2021 and [donated to the CNCF in 2023](https://aws.amazon.com/blogs/containers/karpenter-graduates-to-beta/), its stated goals are to take full advantage of cloud capabilities while remaining fast and simple to use.

Karpenter’s approach to cluster autoscaling is designed to improve how clusters respond to dynamic workloads by scaling faster and requiring less manual configuration for optimal outcomes. Unlike the traditional cluster autoscaler that requires users to specifically configure which node instance types to use and reacts slowly to reductions in workload demand, Karpenter automates the selection of specific instance types and responds quickly to opportunities to consolidate nodes, resulting in autoscaling that’s faster, simpler, and more efficient.

At the time of writing, Karpenter is supported on AWS and [Azure](https://github.com/Azure/karpenter-provider-azure). 

[Karpenter v1.0](https://aws.amazon.com/fr/blogs/containers/announcing-karpenter-1-0/) is done in August 2024

Benefits:

- Automates instance selection, enhancing speed and simplifying configuration.
- Proactively manages node scaling for quick adjustments to workload demands.
- Utilizes spot instances intelligently to cut costs without impacting reliability.

Challenges:

- Requires an understanding of cloud services to take full advantage.
- Might involve complexities in managing spot instance volatility.
- A transition from traditional autoscalers could require adjusting existing workflows.

# **Horizontal Pod Autoscaling**

In Kubernetes, applications run in an object known as a "Pod". To scale applications, more "replicas" of the Pod are created.  This can be done manually by an Administrator or dynamically through an object known as a HPA. HPA stands for **Horizontal Pod Autoscaler** which is an object in Kubernetes that monitors your application's metrics, such as CPU usage, and dynamically scales the amount of Pod replicas based on those metrics. This method of scaling is referred to as "scaling out" the application.

![image (3).png](Explanation%20Kubernetes%20Autoscaling/image_(3).png)

Tools:

![image.png](Explanation%20Kubernetes%20Autoscaling/image%201.png)

## Core HPA

The HPA is a core Kubernetes resource type built into the Kubernetes platform. HPA is widely adopted for its simplicity and effectiveness. Horizontal scaling isn’t appropriate for use with all workloads since not all workloads are designed for parallelism, but when HPA can be used, it’s one of the best ways available to ensure automated elasticity on a per-workload basis. HPA is simplest when using Kubernetes’ inbuilt [resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/), setting targets for percent CPU or memory utilization

Benefits:

- Rapid automatic capacity adjustments
- Easy to scale up or scale down pod count based on built-in metrics such as pod CPU or memory usage
- Possible to scale based on more sophisticated or custom metrics

Challenges:

- Not all workloads are designed to be run with parallelism, restricting which workloads are candidates for horizontal scaling
- Setting up custom scaling metrics can be intricate and/or require specific expertise
- Pods still have vertical sizes, but HPA does not assist with decisions around or management of vertical sizing
- The standard HPA cannot be used in conjunction with the standard VPA when both are using the same metric to scale on

## Keda

KEDA is an advanced project that builds on and enhances HPA, effectively replacing the HPA interface. KEDA was originally created to address a critical missing feature of the HPA, scaling on arbitrary indicators or metrics. It became an official CNCF project in 2020

Benefits:

- Enables scaling based on specific events for granular control.
- Offers built-in scalers for easy integration with external events and metrics.
- Allows scaling of workloads down to zero to save resources during idle times.

Challenges:

- Implementing event-driven scaling requires understanding specific events impacting application performance.
- Relies on external events, which might introduce complexity in monitoring and managing scaling conditions.
- Scaling to zero could lead to cold starts, potentially affecting performance when scaling back up.

# **Vertical Pod Autoscaling**

VPA stands for **Vertical Pod Autoscaler**, and it's another tool in your Kubernetes autoscaling arsenal, but unlike HPA, it focuses on adjusting the CPU and Memory requests and limits of individual pods instead of scaling their replicas. This gives you finer-grained control over the resource allocation of your application. VPA's are Kubernetes's strategy for "scaling up" applications.

![image.png](Explanation%20Kubernetes%20Autoscaling/image%202.png)

Tools:

![image.png](Explanation%20Kubernetes%20Autoscaling/image%203.png)

## VPA

The VPA is the most commonly known tooling for vertical autoscaling and is maintained as part of the autoscaler repository alongside the cluster autoscaler.

The simultaneous use of VPA and HPA poses a challenge primarily due to their potentially conflicting actions: HPA scales pod numbers based on usage metrics, while VPA adjusts pod resource requests – requests that then factor into the calculation for usage. This interplay can break the autoscaling strategy unless carefully managed.

Configuring horizontal and vertical scaling to work in concert has been a sought-after project goal for years, but it is not appropriate today to use the standard HPA and VPA implementations together on the same workload.

Benefits:

- Can, in theory, be applied to any and all workloads
- Automatic pod-level resource allocation can free developers from needing to spend time calculating and updating these numbers themselves

Challenges:

- Use requires a VPA resource per workload to autoscale
- It cannot be easily combined with HPA on the same workload
- Any change to the vertical scale (up or down) requires pods to restart and reschedule
- The quality and real-world reliability of VPA’s vertical sizing recommendations are low
