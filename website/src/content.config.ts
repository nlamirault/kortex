// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0

import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Wiki pages carry rich OKF frontmatter; keep title/description typed and let
// everything else pass through untouched.
export const collections = {
  docs: defineCollection({
    loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/docs" }),
    schema: z
      .object({
        title: z.string().optional(),
        description: z.string().optional(),
      })
      .passthrough(),
  }),
};
