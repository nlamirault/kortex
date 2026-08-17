---
title: Argo CD
type: concept
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: [TMP/KB]
updated: 2025-04-08
tags: [Gitops]
---

# Overview

Argo CD is a **declarative, GitOps-based continuous delivery (CD) tool** for Kubernetes. It synchronizes application state defined in a Git repository with the live state in a Kubernetes cluster. This ensures automated, version-controlled, and consistent deployments.

Unlike traditional CI/CD tools, Argo CD **continuously monitors** Kubernetes applications, ensuring that the desired state (defined in Git) is always enforced.

# **Architecture & Components**

Argo CD consists of multiple components that work together to provide **GitOps-based deployment** and synchronization.

![1_MK1v4FgXo-kOWEYqqYd5xQ.gif](Explanation%20Argo%20CD/1_MK1v4FgXo-kOWEYqqYd5xQ.gif)

### **Git Repository (Declarative Source of Truth)**

Argo CD pulls application manifests from a Git repository (or Helm, Kustomize, etc.) and ensures that the live cluster state matches the desired state.

### **API Server (argocd-server)**

- Serves as the **main entry point** for UI, CLI, and external API requests.
- Handles authentication and authorization.
- Exposes a UI for visualization of deployments.

### **Repository Server (argocd-repo-server)**

- Clones Git repositories and renders manifests (Helm, Kustomize, etc.).
- Provides manifests to the Argo CD Application Controller.

### **Application Controller (argocd-application-controller)**

- Monitors running applications in the cluster.
- Compares the desired state (from Git) with the live cluster state.
- Performs automatic or manual synchronization to enforce the desired state.
- Detects drift and triggers alerts when the cluster is out of sync.

### **Dex (Authentication Provider)**

- Provides authentication via **SSO (Single Sign-On)**, LDAP, GitHub, SAML, etc.
- Ensures secure access control to Argo CD.

### **Redis (State Management)**

- Stores temporary/cache data to improve performance.

### **Kubernetes Cluster**

- Argo CD deploys and manages applications inside one or more Kubernetes clusters.
- Supports multi-cluster deployments.

# **How Argo CD Works?**

1. **Developers push application manifests** (YAML files, Helm charts, etc.) to a Git repository.
2. **Argo CD continuously monitors the repository** and detects changes.
3. **If a change is detected**, the Application Controller reconciles the live state with the desired state.
4. **Synchronization is performed**, deploying/updating Kubernetes resources.
5. **Argo CD UI/CLI/API** provides visibility into application state, allowing manual interventions if needed.
