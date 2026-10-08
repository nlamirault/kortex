// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0

/**
 * The garden rule: an OKF page's `status` + `confidence` map to a growth stage.
 * This mapping is the single implementation — it must match the table in
 * DESIGN.md ("Growth stages — the garden rule").
 */
export type StageKey = 'seedling' | 'budding' | 'evergreen' | 'archived';

export interface Stage {
  key: StageKey;
  emoji: string;
  label: string;
  hint: string;
}

const STAGES: Record<StageKey, Stage> = {
  seedling: { key: 'seedling', emoji: '🌱', label: 'Seedling', hint: 'Just planted — draft, unverified' },
  budding: { key: 'budding', emoji: '🌿', label: 'Budding', hint: 'Growing — stable, partially verified' },
  evergreen: { key: 'evergreen', emoji: '🌳', label: 'Evergreen', hint: 'Trusted — stable, high confidence' },
  archived: { key: 'archived', emoji: '🍂', label: 'Archived', hint: 'Retired — deprecated' },
};

export function growthStage(
  status: string | undefined,
  confidence: string | undefined,
): Stage {
  if (status === 'deprecated') return STAGES.archived;
  if (status === 'draft') return STAGES.seedling;
  // status === 'stable' (OKF default)
  if (confidence === 'high') return STAGES.evergreen;
  return STAGES.budding;
}

/** A page is stale once `now >= stale_after` (OKF §5). */
export function isStale(staleAfter: string | Date | undefined, now: Date = new Date()): boolean {
  if (!staleAfter) return false;
  const when = staleAfter instanceof Date ? staleAfter : new Date(staleAfter);
  return !Number.isNaN(when.getTime()) && now >= when;
}

/** Human label for an OKF entity type. */
export const TYPE_LABEL: Record<string, string> = {
  concept: 'Concept',
  domain: 'Domain',
  source: 'Source',
  organization: 'Organization',
  person: 'Person',
  project: 'Project',
};
