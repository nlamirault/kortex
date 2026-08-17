---
title: Kro
type: project
status: draft
confidence: low
cluster: kubernetes
domain: [kubernetes]
sources: []
updated: 2025-05-06
tags: [Kubernetes, Orchestrator]
generated: {by: claude-sonnet-4-6, at: 2026-08-17}
verified: [{by: nicolas, at: 2026-08-17}]
stale_after: 2027-08-17
---
# Overview

Kube Resource Orchestrator (**Kro**) is an open-source, Kubernetes-native project designed to simplify creating and managing complex custom resources for Kubernetes. It provides a powerful abstraction layer that allows you to define complex multi-resource constructs as reusable components in your applications and systems.

## **ResourceGraphDefinition**

This is the fundamental custom resource in kro. It allows you to define a set of resources and how they relate to each other functionally. Once defined, ResourceGraphDefinitions can be applied to a Kubernetes cluster where the kro controller is running. This enables the creation of instances of your ResourceGraphDefinition, which are managed by kro.

# **Controller**

The kro controller is responsible for determining the dependencies between resources, establishing the correct order of operations to create and configure them, and then dynamically creating and managing all of the underlying resources. It handles all of the dependency and configuration ordering of your resources, making it easier to manage complex Kubernetes deployments.

# **Custom APIs**

kro allows you to create and manage custom groups of Kubernetes resources by defining them as a ResourceGraphDefinition. This enables the creation of reusable APIs for deploying multiple resources as a single unit, transforming complex Kubernetes deployments into simple, reusable components[**345**](https://aws.amazon.com/blogs/opensource/introducing-open-source-kro-kube-resource-orchestrator/).
