# Kortex Wiki — Index

Content catalog organized by entity type.
Last updated: 2026-08-17

---

## Domains

*(broad topic hubs — start here; see `wiki/overview.md` for cluster map)*

- [AI](domains/ai.md) — agent protocols, MCP, LLM tooling (15 concepts)
- [Blockchain](domains/blockchain.md) — distributed ledger, L1, layers (3 concepts)
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
- [MCP (Model Context Protocol)](concepts/model-context-protocol-mcp.md) — tool/context protocol for LLMs
- [MCP Reference](concepts/mcp.md) — MCP reference
- [Universal Commerce Protocol (UCP)](concepts/universal-commerce-protocol-ucp.md) — commerce protocol for AI
<!-- Kubernetes -->
- [Argo CD](concepts/argo-cd.md) — GitOps continuous delivery
- [Argo Events](concepts/argo-events.md) — event-driven workflows on k8s
- [Argo Events CRDs](concepts/argo-events-crds.md) — EventSource, Sensor CRD reference
- [Argo Rollouts](concepts/argo-rollouts.md) — advanced deployment strategies
- [Argo Workflows](concepts/argo-workflows.md) — container-native workflow engine
- [Argo Workflows CRDs](concepts/argo-workflows-crds.md) — Workflow, CronWorkflow CRD reference
- [AWS Controllers for Kubernetes (ACK)](concepts/aws-controllers-for-kubernetes-ack.md) — manage AWS services from k8s
- [EKS Best Practices](concepts/eks-best-practices.md) — AWS EKS guidance
- [Karpenter](concepts/karpenter.md) — node autoprovisioning
- [KEDA](concepts/keda.md) — event-driven autoscaling
- [KEDA CRDs](concepts/keda-crds.md) — ScaledObject, ScaledJob CRD reference
- [Kro](concepts/kro.md) — Kube Resource Orchestrator
- [Kubernetes Autoscaling](concepts/kubernetes-autoscaling.md) — HPA, VPA, KEDA overview
- [Kubernetes Design Patterns](concepts/kubernetes-design-pattern.md) — common k8s patterns
<!-- Observability -->
- [Alertmanager](concepts/alertmanager.md) — Prometheus alert routing and dedup
- [Beyla](concepts/beyla.md) — eBPF-based auto-instrumentation
- [Grafana](concepts/grafana.md) — metrics/logs/traces visualization
- [Grafana Alloy](concepts/grafana-alloy.md) — OpenTelemetry collector distribution
- [GreptimeDB](concepts/greptimedb.md) — time-series and observability database
- [Heartbeat](concepts/heartbeat.md) — distributed systems health detection
- [Loki](concepts/loki.md) — log aggregation system
- [Mimir](concepts/mimir.md) — long-term Prometheus storage
- [Observability](concepts/observability.md) — logs, traces, metrics overview
- [OpenTelemetry Collector](concepts/opentelemetry-collector.md) — vendor-neutral telemetry pipeline
- [OTTL](concepts/ottl.md) — OpenTelemetry Transformation Language
- [Prometheus](concepts/prometheus.md) — metrics collection and alerting
- [Pyrra](concepts/pyrra.md) — SLO management for Prometheus
- [Quickwit](concepts/quickwit.md) — cloud-native search engine
- [Tempo](concepts/tempo.md) — distributed tracing backend
- [VictoriaLogs](concepts/victorialogs.md) — fast log storage
- [VictoriaMetrics](concepts/victoriametrics.md) — high-performance metrics storage
<!-- Networking -->
- [API Gateway](concepts/api-gateway.md) — API gateway patterns
- [API: REST vs GraphQL](concepts/api-rest-graphql.md) — comparison of API styles
- [Envoy](concepts/envoy.md) — high-performance proxy
- [Ingress vs Gateway API](concepts/ingress-vs-gateway-api.md) — k8s ingress comparison
- [Istio](concepts/istio.md) — service mesh
- [Istio CRDs](concepts/istio-crds.md) — VirtualService, DestinationRule reference
- [NATS](concepts/nats.md) — cloud-native messaging
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
- [Sigstore Cosign](concepts/sigstore-cosign.md) — container image signing
- [Sigstore Fulcio](concepts/sigstore-fulcio.md) — certificate authority
- [Sigstore Rekor](concepts/sigstore-rekor.md) — transparency log
- [SLSA](concepts/slsa.md) — supply chain security levels
- [VEX](concepts/vex.md) — Vulnerability Exploitability eXchange
- [xBOM](concepts/xbom.md) — extended bill of materials
<!-- Data -->
- [ACID](concepts/acid.md) — database transaction properties
- [Change Data Capture](concepts/change-data-capture.md) — CDC patterns
- [ClickHouse](concepts/clickhouse.md) — columnar OLAP database
- [Data Lake / Warehouse / Lakehouse](concepts/data-lake-data-warehouse-data-lakehouse.md)
- [Database Models](concepts/database-models.md) — relational, document, graph overview
- [Dragonfly](concepts/dragonfly.md) — in-memory data store
- [DynamoDB](concepts/dynamodb.md) — AWS managed NoSQL
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
- [OpenMeter](concepts/openmeter.md) — usage metering platform
<!-- WASM -->
- [WasmCloud](concepts/wasmcloud.md) — WebAssembly application platform
<!-- Domotic -->
- [Interrupteur simple](concepts/interrupteur-simple.md) — single-pole switch wiring
- [Interrupteur va-et-vient](concepts/interrupteur-va-et-vient.md) — two-way switch wiring
- [Matter](concepts/matter.md) — smart home protocol
- [Thread](concepts/thread.md) — IoT mesh networking
- [Zigbee](concepts/zigbee.md) — IoT wireless standard

---

## Sources

*(books, papers, articles, talks)*

<!-- add source pages here -->

---

## People

*(authors, researchers, thinkers)*

<!-- add people pages here -->

---

## Projects

*(tools, codebases, initiatives)*

<!-- add project pages here -->

---

## Decisions

*(architectural and design choices for this knowledge base)*

<!-- add decision pages here -->

---

## Comparisons

*(side-by-side analysis of sources, tools, or approaches)*

<!-- add comparison pages here -->

---

## Syntheses

*(cross-source analyses filed from queries)*

- [AI Prompts](syntheses/ai-prompts.md) — how-to for AI prompt engineering

---

## Gaps

*(open questions, unknowns, unresolved topics)*

<!-- add gap pages here -->
