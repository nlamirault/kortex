---
title: Argo Workflows CRDs
type: concept
status: active
confidence: high
cluster: kubernetes
domain: [kubernetes]
sources: [TMP/KB]
updated: 2025-04-09
tags: [CRD, Kubernetes]
---

# **Summary Table**

| CRD | Purpose | Scope | Example Use Case |
| --- | --- | --- | --- |
| `Workflow` | Defines a workflow | Namespace | Run an ML training job |
| `WorkflowTemplate` | Reusable workflow template | Namespace | Standardize CI/CD pipelines |
| `CronWorkflow` | Scheduled workflow execution | Namespace | Run database backups every hour |
| `ClusterWorkflowTemplate` | Global reusable workflow template | Cluster-wide | Share workflows across teams |

# **Workflow**

### **Purpose**:

Defines a workflow, specifying the execution logic, templates, and dependencies

### **Components**:

- `metadata.name` → Unique name for the workflow.
- `spec.entrypoint` → Defines the starting template of the workflow.
- `spec.templates` → Defines reusable task templates.
- `container` → Specifies the container image and execution commands.
- `steps` → Defines a sequence of tasks.

### **Execution**:

- The `Workflow` CRD is submitted to Kubernetes.
- The **Workflow Controller** schedules tasks as **Pods**.
- Steps execute sequentially or in parallel based on dependencies.

# **WorkflowTemplate**

### **Purpose**:

Defines reusable workflows that can be referenced by multiple workflows

```yaml
apiVersion: argoproj.io/v1alpha1
kind: WorkflowTemplate
metadata:
  name: reusable-template
spec:
  templates:
    - name: print-message
      container:
        image: alpine
        command: ["echo", "This is a reusable template!"]
```

# CronWorkflow

### **Purpose**:

Schedules workflows to run at specific intervals (similar to Kubernetes CronJobs).

# **ClusterWorkflowTemplate**

### **Purpose**:

Defines reusable workflow templates **at the cluster level** (accessible to all namespaces).

### **Difference from `WorkflowTemplate`**:

- `WorkflowTemplate` is namespace-scoped.
- `ClusterWorkflowTemplate` is **cluster-scoped** (can be used across multiple namespaces).

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ClusterWorkflowTemplate
metadata:
  name: global-template
spec:
  templates:
    - name: say-hello
      container:
        image: alpine
        command: ["echo", "Hello from ClusterWorkflowTemplate!"]
```
