---
title: Karpenter
type: project
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: []
updated: 2025-04-10
tags: [Autoscaling]
---

# Overview

Karpenter is an open-source project by AWS (but designed to be cloud-agnostic) that acts as a **dynamic Kubernetes cluster autoscaler**. Unlike traditional cluster autoscalers (like the Kubernetes Cluster Autoscaler), Karpenter provides **just-in-time** provisioning of compute resources based on pod requirements and cluster state. It’s built to be fast, extensible, and to better support modern, dynamic workloads.

At a high level, Karpenter:

- Watches for pending pods that can’t be scheduled due to insufficient capacity.
- Determines the best instance types and placement options to accommodate those pods.
- Provisions new nodes **immediately** (in seconds) without needing to pre-scale node groups.
- Automatically deletes underutilized or unneeded nodes.

It’s especially well-suited for **highly dynamic or bursty workloads**, serverless-style infrastructure, and mixed-instance-type deployments.

# Components of Karpenter’s architecture

### **Provisioner (CRD)**

> Type: Kubernetes Custom Resource (CRD)
> 
> 
> **Purpose:** Declarative configuration for provisioning behavior
> 

This is what you (the user/operator) define to configure how Karpenter should provision compute.

Key fields:

- `requirements`: Constraints on instance types, zones, architectures, etc.
- `limits`: Upper bounds on resources like CPU and memory.
- `provider`: Cloud-specific details (subnets, security groups, AMI).
- `ttlSecondsAfterEmpty`: How long to wait before terminating empty nodes.
- `consolidation`: Enables cost optimization by replacing or removing nodes.

Each **Provisioner** is **stateless**, serving as a policy definition.

### **Karpenter Controller Manager**

> Type: Kubernetes controller
> 
> 
> **Purpose:** Reconciles resources, triggers provisioning, manages node lifecycle
> 

Runs as a single **controller process**, but with several internal managers or sub-controllers:

### a. **Scheduling Controller**

- Watches for unschedulable pods.
- Groups (batches) pending pods with similar requirements.
- Invokes the **Bin Packing Algorithm** to figure out the most efficient way to pack them onto potential nodes.
- Computes what instance types and zones are suitable using constraints from the pod + provisioner.

### b. **Cloud Provider Interface (CPI)**

- Abstracts away cloud-specific provisioning logic.
- Default: AWS (via `karpenter-core` + `karpenter-provider-aws`)
- Handles:
    - Instance type discovery
    - Launch template creation
    - Subnet & zone selection
    - Node bootstrap and labeling
    - Spot vs On-demand pricing logic

This component is **pluggable** for other clouds or even on-prem (e.g., via community providers).

### c. **Node Controller (NodeLifecycle)**

- Tracks nodes that were provisioned by Karpenter.
- Watches for idle nodes (no pods running) and terminates them based on `ttlSecondsAfterEmpty`.
- Annotates and labels nodes with metadata for tracking and cleanup.
- Works with the Kubernetes API to cordon and drain before termination.

### d. **Consolidation Controller**

- Continuously evaluates opportunities for **bin-packing** and **cost savings**:
    - Can consolidate workloads onto fewer instances.
    - May trigger a re-provision of smaller/better-fitting instances.
    - Uses Kubernetes eviction API to gracefully move workloads.
- Operates passively (non-disruptively), considering pod disruption budgets and availability.

### e. **Instance Type Selector / Capacity Weigher**

- Filters and ranks instance types based on:
    - Pod resource requirements
    - Cost (if using Spot or On-Demand)
    - Zone/region availability
    - Provisioner constraints

### **Webhook (Mutating/Validating Admission Webhooks)**

> Optional but common
> 
> 
> **Purpose:** Enforces policies or injects defaults when Provisioners are created/updated.
> 

Useful for:

- Setting default node selectors
- Enforcing constraints on Provisioners (e.g., disallowing overly broad configurations)

### **Cloud Provider-Specific Controller (e.g., AWS Controller)**

> Separate component for each cloud
> 
> 
> **Purpose:** Cloud-native provisioning logic, cost awareness, resource discovery
> 

In AWS:

- Resolves subnet/security group selectors
- Integrates with EC2, Auto Scaling Groups (optionally), Launch Templates
- Bootstraps nodes with proper IAM roles, kubelet settings, and tags

This component is coupled with the core Karpenter logic, but can be swapped in a modular fashion for other clouds.

.svg)

# RBAC and IAM

Karpenter runs with:

- Kubernetes RBAC (service account with access to `pods`, `nodes`, `provisioners`, etc.)
- Cloud IAM permissions for provisioning (e.g., `ec2:RunInstances`, `eks:DescribeCluster`, etc.)

Each provisioned node is bootstrapped with a **Karpenter-specific IAM role** using instance profile, enabling access to required cloud APIs.
