---
title: Authentication
type: concept
status: active
confidence: high
cluster: security
domain: [security]
sources: []
updated: 2025-04-14
tags: [Authentication, Identity]
---

# Authentication

Authentication is the process of verifying the identity of a user, system, or device before granting access to a resource. It ensures that the entity requesting access is who they claim to be. Authentication typically precedes **authorization**, which determines what actions the authenticated entity is allowed to perform.

# **Types of Authentication**

Different authentication methods exist to ensure security, each with varying levels of reliability and ease of use.

## Single-Factor Authentication (SFA)

**What it is:** Authentication based on a single method, typically a password.

**Example:** Logging into a website with just a username and password.

**Weakness:** Easily compromised if passwords are weak or reused.

## **Multi-Factor Authentication (MFA)**

**What it is:** Uses multiple authentication factors to verify identity.

**Example:** Entering a password **(something you know)** + receiving a one-time code on your phone **(something you have)**.

**Strength:** Increases security by requiring multiple proofs of identity.

## **Two-Factor Authentication (2FA)** *(A subset of MFA)*

**What it is:** Requires exactly **two** authentication factors from different categories.

**Example:** Logging in with a password and confirming via an authentication app (Google Authenticator).

**Use Case:** Online banking, email accounts, corporate logins.

## **Password-Based Authentication**

**What it is:** The most common method, using a combination of a username and password.

**Example:** Logging into Facebook with an email and password.

**Weakness:** Vulnerable to brute-force attacks, phishing, and password leaks.

## **Biometric Authentication**

**What it is:** Uses unique biological traits for verification.

**Types:**

- **Fingerprint scan** (smartphones, secure facilities)
- **Face recognition** (Face ID on iPhones)
- **Iris or retina scan** (high-security environments)
- **Voice recognition** (smart assistants)🔹 **Strength:** Hard to fake, convenient, and does not require remembering passwords.

## **Token-Based Authentication**

**What it is:** Users authenticate once and receive a token for subsequent access.

**Example:** OAuth 2.0 (used in "Sign in with Google/Facebook" logins).

**Use Case:** API security, web authentication.

## **One-Time Passwords (OTP)**

**What it is:** A temporary password valid for a single use.

**Example:** Receiving a login code via SMS or email.

**Use Case:** Banking transactions, 2FA authentication.

## **Certificate-Based Authentication**

**What it is:** Uses digital certificates to verify identity.

**Example:** SSL/TLS certificates for secure website connections.

**Use Case:** VPN access, secure email communication.

## **Smart Card Authentication**

**What it is:** Uses a physical smart card containing encrypted credentials.

**Example:** Employee ID cards for secure building access.

**Use Case:** Corporate environments, government agencies.
