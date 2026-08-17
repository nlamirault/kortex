---
title: AWS Controllers for Kubernetes (ACK)
type: concept
status: draft
confidence: low
cluster: kubernetes
domain: [kubernetes]
sources: [TMP/KB]
updated: 2026-01-29
tags: [AWS, Kubernetes]
---

## Overview

AWS Controllers for Kubernetes (ACK) enables you to manage AWS services directly from Kubernetes using native Kubernetes APIs and resources. This explanation covers the architecture, core concepts, and design decisions behind ACK.

## Background

Traditionally, managing AWS resources alongside Kubernetes workloads required using separate tools like AWS CLI, CloudFormation, or Terraform. This created a disconnect between application deployment (in Kubernetes) and infrastructure management (outside Kubernetes).

ACK bridges this gap by bringing AWS service management into the Kubernetes control plane, allowing teams to use kubectl and GitOps workflows for both application and infrastructure management.

## Core Concepts

### [Custom Resource Definitions (CRDs)]

[Explanation of how ACK uses CRDs to represent AWS resources]

[How CRDs map to AWS service APIs]

### [Service Controllers]

[Detailed discussion of controller pattern]

[How each ACK controller manages a specific AWS service]

### [Reconciliation Loop]

[Explanation of the reconciliation pattern]

[How ACK ensures desired state matches actual state]

## How It Works

[Conceptual explanation of the end-to-end flow]

1. User defines AWS resource as Kubernetes manifest
2. ACK controller watches for changes
3. Controller calls AWS API to create/update/delete resources
4. Status is synchronized back to Kubernetes

[Use analogies: "ACK acts as a translator between Kubernetes and AWS"]

## Design Decisions

### Why Use Kubernetes CRDs?

[Reasoning behind using Kubernetes as the control plane]

- Unified interface for application and infrastructure
- Native GitOps support
- Familiar tooling (kubectl, Helm, Kustomize)
- RBAC and audit logging built-in

[What problem this solves: Infrastructure-as-Code drift, separate tools]

### Why Separate Controllers per Service?

[Explanation of modular architecture]

- Install only the AWS services you need
- Independent versioning and release cycles
- Reduced blast radius for issues
- Easier maintenance and testing

### Alternatives Considered

#### External Infrastructure Tools (Terraform, CloudFormation)

[Why these were alternatives]

[Why ACK provides better integration for Kubernetes-native workflows]

#### AWS Service Operator for Kubernetes (Deprecated)

[Previous AWS solution]

[Why ACK replaced it with code generation approach]

## Tradeoffs

### Advantages

- **Kubernetes-native experience**: Use kubectl and GitOps tools
- **Unified workflow**: Manage apps and infrastructure together
- **Fine-grained RBAC**: Leverage Kubernetes authorization
- **Declarative**: Idempotent resource management
- **Multi-tenancy**: Namespace isolation for AWS resources

### Disadvantages

- **Learning curve**: Requires understanding both Kubernetes and AWS
- **API coverage**: Not all AWS services supported yet
- **Eventual consistency**: Reconciliation loops have delay
- **Kubernetes dependency**: Requires running Kubernetes cluster
- **Limited cross-region**: Each controller manages resources in one region

[When ACK makes sense: Kubernetes-first organizations, GitOps adoption]

[When to use alternatives: Standalone AWS infrastructure, multi-cloud]

## Common Misconceptions

### Misconception 1: ACK replaces Terraform/CloudFormation

**Wrong**: ACK must be used instead of all other IaC tools

**Correct**: ACK complements existing tools and is best for resources tightly coupled to Kubernetes workloads. Use Terraform/CloudFormation for foundational infrastructure.

### Misconception 2: ACK manages Kubernetes infrastructure

**Wrong**: ACK manages EKS clusters and Kubernetes components

**Correct**: ACK manages AWS services consumed by applications (RDS, S3, SQS, etc.), not the Kubernetes cluster itself. Use eksctl or Terraform for EKS cluster management.

### Misconception 3: All AWS services are supported

**Wrong**: Every AWS service has an ACK controller

**Correct**: ACK is under active development. Check the [official repository](https://github.com/aws-controllers-k8s/community) for supported services.

## Real-World Examples

### Example 1: Application Database Provisioning

A development team deploys their application with a Helm chart that includes both the application Deployment and an RDS database Custom Resource. ACK provisions the RDS instance automatically during helm install.

### Example 2: GitOps-Driven Infrastructure

An SRE team uses ArgoCD to manage both application manifests and ACK resources in Git. Changes to S3 bucket policies or IAM roles follow the same pull request and approval process as application code.

### Example 3: Multi-Tenant SaaS

A SaaS platform creates isolated namespaces per customer. ACK controllers provision customer-specific AWS resources (DynamoDB tables, SNS topics) scoped to each namespace with appropriate IAM permissions.

## Related Concepts

- [Link to Kubernetes Operator Pattern explanation]
- [Link to GitOps explanation]
- [Link to AWS IAM for Service Accounts (IRSA) or EKS Pod Identity reference]
- [Link to how-to guide: Installing and configuring ACK controllers]
- [Link to reference: ACK supported services list]

## Further Reading

- [AWS Controllers for Kubernetes Documentation](https://aws-controllers-k8s.github.io/community/)
- [AWS Blog: Introducing AWS Controllers for Kubernetes](https://aws.amazon.com/blogs/containers/aws-controllers-for-kubernetes-ack/)
- [GitHub: ACK Community Repository](https://github.com/aws-controllers-k8s/community)
- [Kubernetes Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
- [GitOps Principles](https://opengitops.dev/)
