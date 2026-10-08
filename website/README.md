<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
SPDX-License-Identifier: Apache-2.0
-->

# Kortex Website

The public face of the [Kortex](../AGENTS.md) knowledge garden — an
[Astro](https://astro.build) static site served on **Cloudflare Workers**,
rendered directly from the `wiki/` OKF v0.2 bundle.

## What it does

- Renders every real entity page (`concepts`, `domains`, `sources`,
  `organizations`) from `../wiki` as a styled page. Builder-generated
  `wiki/kb/**` nodes and reserved `index.md` / `log.md` are excluded.
- Shows a **growth badge** on each page — 🌱 seedling → 🌿 budding → 🌳 evergreen
  → 🍂 archived — computed from OKF `status` + `confidence` (see `DESIGN.md`).
- Serves every page as clean **Markdown** to agents via `Accept: text/markdown`
  (the Cloudflare Worker converts the built HTML at the edge).

## Stack

| Piece | Choice |
|-------|--------|
| Framework | Astro (SSG, no UI framework) |
| Content | `astro:content` glob loader over `../wiki` |
| Hosting | Cloudflare Workers (static assets + `worker.js`) |
| Design | `DESIGN.md` → `make tokens` → `src/styles/global.css` |
| Theme | Digital Garden (Fraunces + Inter + JetBrains Mono) |

## Develop

```sh
make install     # bun install
make dev         # astro dev server
make build       # tokens-check + astro build → dist/
make check       # astro check (types + content schema)
make tokens      # regenerate global.css tokens from DESIGN.md
make deploy-dry  # validate the Worker without deploying
make deploy      # wrangler deploy
```

## Design tokens

`DESIGN.md` is the single source of truth for colors, spacing, radius and type.
Edit its frontmatter, then `make tokens` rewrites the `:root {}` block of
`src/styles/global.css`. CI runs `make tokens-check` to catch drift.

## Known limitations (v1)

- `[[type:slug]]` relations tables render as literal text (machine-readable form).
- No public domain yet, so `astro.config` `site` and `@astrojs/sitemap` are off.
