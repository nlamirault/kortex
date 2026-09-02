# Kortex Wiki — Index

Content catalog organized by entity type.
Last updated: 2026-09-01

---

## Domains

*(broad topic hubs — start here; see `wiki/overview.md` for cluster map)*

- [AI](domains/ai.md) — agent protocols, MCP, LLM tooling (16 concepts)
- [Blockchain](domains/blockchain.md) — distributed ledger, L1, layers, Tempo (3 concepts, 1 project)
- [Data](domains/data.md) — databases, data engineering, lineage (9 concepts)
- [Domotic](domains/domotic.md) — smart home: Matter, Zigbee, Thread (5 concepts)
- [Kubernetes](domains/kubernetes.md) — Argo, KEDA, Karpenter, CRDs, patterns (15 concepts)
- [Metering](domains/metering.md) — OpenMeter, FOCUS, FinOps (2 concepts)
- [Networking](domains/networking.md) — Istio, Envoy, NATS, API design (11 concepts)
- [Observability](domains/observability.md) — Prometheus, Loki, Tempo, Grafana stack (17 concepts)
- [Platform](domains/platform.md) — SLI/SLO/SLA, deployment strategies (5 concepts)
- [Security](domains/security.md) — Sigstore, SBOM, SLSA, identity (12 concepts)
- [WASM](domains/wasm.md) — WasmCloud (1 concept)

---

## Concepts

*(ideas, frameworks, mental models)*

<!-- AI -->
- [A2A (Agent-to-Agent)](concepts/agent-to-agent-a2a.md) — inter-agent communication protocol
- [AG-UI (Agent-User Interaction Protocol)](concepts/agent-user-interaction-protocol-ag-ui.md) — agent↔UI interaction standard
- [ACP (Agent Client Protocol)](concepts/agent-client-protocol-acp.md) — agent client protocol
- [ACP (Agent Communication Protocol)](concepts/agent-communication-protocol-acp.md) — agent communication standard
- [Agent Payments Protocol (AP2)](concepts/agent-payments-protocol-ap2.md) — payments in agentic systems
- [Agent Skills](concepts/agent-skills.md) — structured agent capabilities
- [Agents.md](concepts/agentsmd.md) — agent metadata spec
- [AI Context Engineering](concepts/ai-context-engineering.md) — context management for LLMs
- [AI Protocols](concepts/ai-protocols.md) — overview of AI communication protocols
- [AWS Bedrock AgentCore](concepts/aws-bedrock-agentcore.md) — AWS managed agent runtime
- [AWS Bedrock Agent Core (Reference)](concepts/aws-bedrock-agent-core.md) — reference for Bedrock Agent Core
- [Machine Payments Protocol (MPP)](concepts/machine-payments-protocol-mpp.md) — HTTP 402 machine-to-machine payments (Tempo/Stripe)
- [MCP (Model Context Protocol)](concepts/model-context-protocol-mcp.md) — tool/context protocol for LLMs
- [MCP Reference](concepts/mcp.md) — MCP reference
- [Universal Commerce Protocol (UCP)](concepts/universal-commerce-protocol-ucp.md) — commerce protocol for AI
<!-- Kubernetes -->
- [Argo Events CRDs](concepts/argo-events-crds.md) — EventSource, Sensor CRD reference
- [Argo Workflows CRDs](concepts/argo-workflows-crds.md) — Workflow, CronWorkflow CRD reference
- [EKS Best Practices](concepts/eks-best-practices.md) — AWS EKS guidance
- [KEDA CRDs](concepts/keda-crds.md) — ScaledObject, ScaledJob CRD reference
- [Kubernetes Autoscaling](concepts/kubernetes-autoscaling.md) — HPA, VPA, KEDA overview
- [Kubernetes Design Patterns](concepts/kubernetes-design-pattern.md) — common k8s patterns
<!-- Observability -->
- [Heartbeat](concepts/heartbeat.md) — distributed systems health detection
- [Observability](concepts/observability.md) — logs, traces, metrics overview
- [OTTL](concepts/ottl.md) — OpenTelemetry Transformation Language
<!-- Networking -->
- [API Gateway](concepts/api-gateway.md) — API gateway patterns
- [API: REST vs GraphQL](concepts/api-rest-graphql.md) — comparison of API styles
- [Ingress vs Gateway API](concepts/ingress-vs-gateway-api.md) — k8s ingress comparison
- [Istio CRDs](concepts/istio-crds.md) — VirtualService, DestinationRule reference
- [OSI Model](concepts/osi-model.md) — network layer reference
- [REST API Authentication Methods](concepts/rest-api-authentication-methods.md) — auth method comparison
- [REST API Best Practices](concepts/rest-api-best-practices.md) — REST design guidance
- [URL / URI / URN](concepts/url-uri-urn.md) — identifier taxonomy
<!-- Security -->
- [Authentication](concepts/authentication.md) — identity verification
- [Authorization](concepts/authorization.md) — access control
- [Digital Identity](concepts/digital-identity.md) — identity reference
- [Encoding vs Encryption vs Tokenization](concepts/encoding-vs-encryption-vs-tokenization.md)
- [SBOM](concepts/sbom.md) — software bill of materials
- [Sigstore](concepts/sigstore.md) — software signing framework
- [SLSA](concepts/slsa.md) — supply chain security levels
- [VEX](concepts/vex.md) — Vulnerability Exploitability eXchange
- [xBOM](concepts/xbom.md) — extended bill of materials
<!-- Data -->
- [ACID](concepts/acid.md) — database transaction properties
- [Change Data Capture](concepts/change-data-capture.md) — CDC patterns
- [Data Lake / Warehouse / Lakehouse](concepts/data-lake-data-warehouse-data-lakehouse.md)
- [Database Models](concepts/database-models.md) — relational, document, graph overview
- [Lineage Object Model](concepts/lineage-object-model.md) — OpenLineage LOM spec
- [OpenLineage](concepts/openlineage.md) — data lineage standard
<!-- Blockchain -->
- [Blockchain](concepts/blockchain.md) — distributed ledger fundamentals
- [Blockchain Layer 1](concepts/blockchain-layer-1.md) — L1 protocol overview
- [Blockchain Layers](concepts/blockchain-layers.md) — layered architecture
<!-- Platform -->
- [12-Factor App](concepts/12-app-factor.md) — cloud-native app methodology
- [Deployment Strategies](concepts/deployment-strategies.md) — blue/green, canary, etc.
- [Fantastic Four of System Design](concepts/fantastic-four-of-system-design.md)
- [SLI / SLO / SLA](concepts/sli-slo-sla.md) — reliability targets
- [TUI](concepts/tui.md) — terminal UI reference
<!-- Metering -->
- [FOCUS](concepts/focus.md) — FinOps open cost schema
<!-- WASM -->
<!-- Domotic -->
- [Interrupteur simple](concepts/interrupteur-simple.md) — single-pole switch wiring
- [Interrupteur va-et-vient](concepts/interrupteur-va-et-vient.md) — two-way switch wiring
- [Matter](concepts/matter.md) — smart home protocol
- [Thread](concepts/thread.md) — IoT mesh networking
- [Zigbee](concepts/zigbee.md) — IoT wireless standard

---

## Sources

*(books, papers, articles, talks)*

- [MPP Specifications (Tempo/Stripe, 2026)](sources/mpp-specs.md) — Machine Payments Protocol spec: HTTP 402 machine-to-machine payments

<!-- add source pages here -->

---

## People

*(authors, researchers, thinkers)*

<!-- add people pages here -->

---

## Projects

*(tools, codebases, initiatives)*


<!-- Observability -->
- [Alertmanager](projects/alertmanager.md) — Alertmanager is a component of the Prometheus monitoring system that handles ale
- [Beyla](projects/beyla.md) — Grafana Beyla is part of Grafana Labs' open-source observability stack, focusing
- [Grafana](projects/grafana.md) — Grafana is an open-source platform for monitoring and observability that allows 
- [Grafana Alloy](projects/grafana-alloy.md) — Grafana Alloy is a [OpenTelemetry Collector](https://opentelemetry.io/docs/colle
- [GreptimeDB](projects/greptimedb.md) — At a high level, GreptimeDB is built as a **modular, horizontally scalable syste
- [Loki](projects/loki.md) — Grafana Loki is a horizontally scalable, highly available, multi-tenant log aggr
- [Mimir](projects/mimir.md) — Grafana Mimir is an open-source, highly scalable, and operationally simple long-
- [OpenTelemetry Collector](projects/opentelemetry-collector.md) — OpenTelemetry Collector is an open-source, unified agent that collects distribut
- [Prometheus](projects/prometheus.md) — Prometheus is an open-source systems monitoring and alerting toolkit originally 
- [Pyrra](projects/pyrra.md) — Pyrra is an open-source tool designed to monitor Service Level Objectives (SLOs)
- [Quickwit](projects/quickwit.md) — Quickwit is an open-source, distributed search engine designed for large-scale d
- [Tempo](projects/tempo.md) — Grafana Tempo is an open-source, high-volume, and minimal-dependency distributed
- [VictoriaLogs](projects/victorialogs.md) — VictoriaLogs is an open-source project developed by the same team behind Victori
- [VictoriaMetrics](projects/victoriametrics.md) — VictoriaMetrics is an open-source time series database and monitoring system bui

<!-- Kubernetes -->
- [AWS Controllers for Kubernetes (ACK)](projects/aws-controllers-for-kubernetes-ack.md) — AWS Controllers for Kubernetes (ACK) enables you to manage AWS services directly
- [Argo CD](projects/argo-cd.md) — Argo CD is a **declarative, GitOps-based continuous delivery (CD) tool** for Kub
- [Argo Events](projects/argo-events.md) — **Argo Events** is an event-driven workflow automation framework for Kubernetes.
- [Argo Rollouts](projects/argo-rollouts.md) — **Argo Rollouts** is a Kubernetes controller that provides advanced deployment s
- [Argo Workflows](projects/argo-workflows.md) — Argo Workflows is a **container-native workflow engine** designed for orchestrat
- [Karpenter](projects/karpenter.md) — Karpenter is an open-source project by AWS (but designed to be cloud-agnostic) t
- [Keda](projects/keda.md) — KEDA (Kubernetes Event-Driven Autoscaling) is an open-source project that enable
- [Kro](projects/kro.md) — Kube Resource Orchestrator (**Kro**) is an open-source, Kubernetes-native projec

<!-- Networking -->
- [Envoy](projects/envoy.md) — Envoy is a high-performance, cloud-native edge and service proxy designed for mi
- [Istio](projects/istio.md) — Istio is a **service mesh** that helps manage, secure, and monitor communication
- [Nats](projects/nats.md) — It's an open-source messaging platform, often used as a **pub/sub, request/reply

<!-- Security -->
- [Sigstore Cosign](projects/sigstore-cosign.md) — **Cosign** is an open-source CLI tool developed by Sigstore that allows develope
- [Sigstore Fulcio](projects/sigstore-fulcio.md) — **Fulcio** is an **open-source Certificate Authority** specifically designed for
- [Sigstore Rekor](projects/sigstore-rekor.md) — **Rekor** is a **transparency log server** that records cryptographically signed

<!-- Data -->
- [Clickhouse](projects/clickhouse.md) — ClickHouse is an open-source columnar database management system (DBMS) designed
- [Dragonfly](projects/dragonfly.md)
- [DynamoDB](projects/dynamodb.md) — In 2021, there was a 66-hour Amazon Prime Day shopping event.

<!-- Metering -->
- [OpenMeter](projects/openmeter.md) — **OpenMeter** ([https://openmeter.io/](https://openmeter.io/)) is an open-source

<!-- Blockchain -->
- [Tempo](projects/tempo.md) — Stripe/Paradigm L1 blockchain for stablecoin machine payments; settles MPP

<!-- WASM -->
- [WasmCloud](projects/wasmcloud.md)

<!-- add project pages here -->

---

## Decisions

*(architectural and design choices for this knowledge base — ADRs)*

- [ADR-0001 — Adopt WikiSkill Evolution Loop](decisions/adopt-wikiskill-evolution-loop.md) — close the wiki→procedure feedback loop from arxiv 2608.27454

---

## Comparisons

*(side-by-side analysis of sources, tools, or approaches)*

<!-- add comparison pages here -->

---

## Syntheses

*(cross-source analyses filed from queries)*

- [AI Prompts](syntheses/ai-prompts.md) — how-to for AI prompt engineering

---

## Patterns

*(recurring failure modes / winning strategies — drive `/evolve`)*

<!-- add pattern pages here — none yet; created by /evolve from !failure log entries -->

---

## Meta

*(operational ledgers for the wiki machine itself)*

- [Skill Impact Ledger](skill-impact.md) — audit trail of every skill/rule change (ADR-0001)

---

## Gaps

*(open questions, unknowns, unresolved topics)*

- [Evolve loop coverage](gaps/evolve-loop-coverage.md) — open questions on the WikiSkill loop's gate

---

## By Date

*(recent additions and updates — newest first; derived from `wiki/log.md`)*
*(pruning rule: keep last 90 days visible; collapse older to a single summary line)*

### 2026-09-02
- [MPP](concepts/machine-payments-protocol-mpp.md), [Tempo](projects/tempo.md), [mpp-specs](sources/mpp-specs.md) — ingest Machine Payments Protocol (paymentauth.org); cross-linked from AP2, UCP, ai-protocols, ai + blockchain domains `[INGEST]`

### 2026-09-01
- [ADR-0001](decisions/adopt-wikiskill-evolution-loop.md), [skill-impact.md](skill-impact.md), [patterns/](patterns/), [.claude/skills/evolve.md](../.claude/skills/evolve.md), [gaps/evolve-loop-coverage.md](gaps/evolve-loop-coverage.md) — adopt WikiSkill evolution loop; `pattern` entity type; `## Purpose` added to all 8 skills; CLAUDE.md + schema.md updated `[UPDATE]`

### 2026-08-28
- [.claude/skills/graph.md](../.claude/skills/graph.md), [CLAUDE.md](../CLAUDE.md) — /graph skill for SPO Relations traversal `[UPDATE]`

### 2026-08-27
- [wiki/schema.md](schema.md), [.claude/skills/ingest.md](../.claude/skills/ingest.md), [CLAUDE.md](../CLAUDE.md) — /ingest --fiche mode for articles `[UPDATE]`
- [.claude/skills/close.md](../.claude/skills/close.md) — /close now writes queue count to hot.md Pending Ingests `[UPDATE]`
- [wiki/schema.md](schema.md), [.claude/skills/ingest.md](../.claude/skills/ingest.md), [.claude/skills/lint.md](../.claude/skills/lint.md) — SPO Relations section added to entity page templates `[UPDATE]`
- [.claude/skills/today.md](../.claude/skills/today.md) — /today now reads raw/queue.md for ingest queue count `[UPDATE]`
- [.claude/skills/lint.md](../.claude/skills/lint.md), [CLAUDE.md](../CLAUDE.md) — stale_after expiry checks added to /lint `[UPDATE]`

### 2026-08-17
- [33 project pages](projects/) — tools migrated from concepts; domain hubs rebuilt `[IMPROVE]`
- [11 domain hubs](domains/) — rebuilt with separate concept/project sections `[IMPROVE]`
- [94 concept pages](concepts/) — migrated from Notion KB export `[INGEST]`
- [8 source pages](sources/) — migrated from Notion KB export `[INGEST]`
- [3 people pages](people/) — migrated from Notion KB export `[INGEST]`

### 2026-05-04
- [wiki/index.md](index.md), [wiki/log.md](log.md), [wiki/schema.md](schema.md) — bootstrapped `[INIT]`
- [wiki/hot.md](hot.md), [wiki/overview.md](overview.md) — session infrastructure `[UPDATE]`
- [CLAUDE.md](../CLAUDE.md) — schema expanded with Three-Layer Architecture `[UPDATE]`
