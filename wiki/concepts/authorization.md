---
title: Authorization
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: [TMP/KB]
updated: 2025-09-23
tags: [Authorization, Identity]
---

## Overview

**Authorization** is the process of determining what actions or resources a user, system, or application is allowed to access after authentication has been successfully completed. It is a critical component of security in systems, networks, and software applications

## What is Fine-Grained Authorization?

Fine-Grained Authorization (FGA) implies the ability to grant specific users permission to perform certain actions in specific resources.

Well-designed FGA systems allow you to manage permissions for millions of objects and users. These permissions can change rapidly as a system continually adds objects and updates access permissions for its users.

A notable example of FGA is Google Drive: access can be granted either to documents or to folders, as well as to individual users or users as a group, and access rights regularly change as new documents are created and shared with specific users or groups.

### What is Role-Based Access Control?

In [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), permissions are assigned to users based on their role in a system. For example, a user needs the `editor` role to edit content.

RBAC systems enable you to define users, groups, roles, and permissions, then store them in a centralized location. Applications access that information to make authorization decisions.

### What is Attribute-Based Access Control?

In [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC), permissions are granted based on a set of attributes that a user or resource possesses. For example, a user assigned both `marketing` and `manager` attributes is entitled to publish and delete posts that have a `marketing` attribute.

Applications implementing ABAC need to retrieve information stored in multiple data sources - like RBAC services, user directories, and application-specific data sources - to make authorization decisions.

### What is Policy-Based Access Control?

Policy-Based Access Control (PBAC) is the ability to manage authorization policies in a centralized way that’s external to the application code. Most implementations of ABAC are also PBAC.

### What is Relationship-Based Access Control?

[Relationship-Based Access Control](https://en.wikipedia.org/wiki/Relationship-based_access_control) (ReBAC) enables user access rules to be conditional on relations that a given user has with a given object *and* that object's relationship with other objects. For example, a given user can view a given document if the user has access to the document's parent folder.

ReBAC is a superset of RBAC: you can fully implement RBAC with ReBAC. ReBAC also lets you natively solve for ABAC when attributes can be expressed in the form of relationships. For example ‘a user’s manager’, ‘the parent folder’, ‘the owner of a document’, ‘the user’s department’ can be defined as relationships.

OpenFGA extends ReBAC by making it simpler to express additional ABAC scenarios using [Conditions](https://openfga.dev/docs/modeling/conditions) or [Contextual Tuples](https://openfga.dev/docs/modeling/token-claims-contextual-tuples).

ReBAC can also be considered PBAC, as authorization policies are centralized.

## Request Path



## XACML

XACML[1] (eXtensible Access Control Markup Language) is a specification that defines a language for access control, rule circulation, and security policy administration for information systems

### Policy Enforcement Point (PEP)

**Role**: Point at which security decisions are enforced.

**Function**:

The PEP is located where access is requested (e.g., a web service, API, file).

It intercepts the request and asks the PDP whether the action is authorized.

Depending on the PDP's response, it authorizes or denies access.

**Example**: A web server that blocks a user if the PDP says that access to a page is prohibited.

### Policy Decision Point (PDP)

**Role**: Decision point for access.

**Function**:

The PDP receives an access request from the PEP.

It evaluates the policies stored in the PAP and decides whether access should be granted or denied.

It returns the decision (permit, deny, not applicable, indeterminate) to the PEP.

**Example**: A rule engine that checks: “Can user X read document Y?”

### Policy Administration Point (PAP)

**Role**: Point for managing and creating access policies.

**Function**:

The PAP allows administrators to define, modify, or delete policies.

These policies are then stored and used by the PDP to make decisions.

**Example**: A web interface where the administrator defines that “only managers can access financial reports.”

### Policy Information Point (PIP)

**Role**: Point of provision of contextual information for decision-making.

**Function**:

The PIP provides additional data to the PDP so that it can make an informed decision.

This information may include user attributes, resources, context (time, location, etc.).

**Example**: A database containing user roles or an API that provides the user's geographic location.

### 🔗 Simplified summary

| Composant | Rôle clé | Exemple |
| --- | --- | --- |
| PEP | Enforces the decision | Web server that blocks access |
| PDP | Makes the decision | Rules engine that says allow/deny |
| PAP | Manages policies | Administration interface for defining rules |
| PIP | Provides information | Database of user roles, context attributes |

.png)

# Next

https://github.com/jruizaranguren/best-of-digital-identity
