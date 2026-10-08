// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// A bare `updated: 2026-10-08` in OKF frontmatter is parsed by YAML into a
// Date; `sources: []` or a list of mappings; `generated`/`verified` are nested.
// The schema stays permissive: OKF makes only `type` required.
const dateish = z.union([z.string(), z.date()]).optional();

const actor = z.object({ by: z.string(), at: dateish }).passthrough();

const wiki = defineCollection({
  // Render the real OKF bundle. Exclude reserved files (index/log — no `type`),
  // the meta pages, and wiki/kb/** (builder-generated duplicate graph nodes).
  loader: glob({
    base: '../wiki',
    pattern: [
      '{concepts,domains,sources,organizations}/**/*.md',
    ],
  }),
  schema: z
    .object({
      type: z.string(),
      title: z.string().optional(),
      description: z.string().optional(),
      status: z.enum(['draft', 'stable', 'deprecated']).default('stable'),
      confidence: z.enum(['low', 'medium', 'high']).optional(),
      format: z.string().optional(),
      cluster: z.string().optional(),
      domain: z.array(z.string()).optional(),
      tags: z.array(z.string()).optional(),
      sources: z.array(z.any()).optional(),
      generated: actor.optional(),
      verified: z.array(actor).optional(),
      stale_after: dateish,
      updated: dateish,
    })
    .passthrough(),
});

export const collections = { wiki };
