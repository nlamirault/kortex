# Kortex Wiki — Overview

Cluster navigation hub. Read after `wiki/index.md` to orient within a domain.
Updated as domains are added. Each cluster described in 2–3 sentences with entry points.

---

## Navigation Tiers

```
Tier 0  wiki/index.md        ← catalog of all pages by type
Tier 1  wiki/overview.md     ← this file — cluster entry points
Tier 2  wiki/domains/*.md    ← hub pages per domain/cluster
Tier 3  wiki/concepts/*.md   ← member concept pages
Tier 4  wiki/sources/*.md    ← evidence layer
Tier 5  wiki/syntheses/*.md  ← cross-source analyses (leaves, not hubs)
```

**Rule:** Syntheses are leaves. They link upward to tier-3 concepts; tier-3 links upward to tier-2 hub.
Split a cluster when its hub exceeds 15 member pages.

---

## Clusters

*(Add one entry per domain hub as domains are bootstrapped)*

| Cluster | Hub Page | Members | Description |
|---------|----------|---------|-------------|
| — | — | — | No clusters yet. Use `/bootstrap <domain>` to add one. |

---

## Cluster Health

| Status | Meaning |
|--------|---------|
| healthy | Hub exists, all members linked, no orphans |
| growing | Hub exists, active ingestion in progress |
| stale | Hub exists but `updated` date > 30 days |
| missing | Concept mentioned 3+ times but no hub page yet |
