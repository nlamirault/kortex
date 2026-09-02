// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0
//
// Kortex wiki site — bespoke Astro theme (devops-graphite design, Tailwind v4).
// Content is synced from ../wiki into src/content/docs by prepare_content.py.

import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  site: "https://nlamirault.github.io",
  base: "/kortex",
  output: "static",
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
