#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0
#
# Build (or serve) the Kortex website. Driven by the repo-root Makefile
# (`make site-build`, `make site-preview`) and usable directly.
#
#   ./website/build.sh            build the static site into website/dist
#   ./website/build.sh --serve    start the Astro dev server (localhost:4321)
#
# Astro outputs to dist/; the Cloudflare Worker (wrangler.jsonc) serves dist/.

set -euo pipefail

cd "$(dirname "$0")"

# Prefer bun; fall back to npm so the build works without bun installed.
if command -v bun >/dev/null 2>&1; then
  PM="bun"
  PX="bunx"
  RUN="bun run"
elif command -v npm >/dev/null 2>&1; then
  PM="npm"
  PX="npx --yes"
  RUN="npm run"
else
  echo "error: neither bun nor npm found on PATH" >&2
  exit 1
fi

# Install dependencies on first run (or after a clean).
if [ ! -d node_modules ]; then
  echo "[build.sh] installing dependencies with ${PM}"
  "${PM}" install
fi

# Regenerate design tokens from DESIGN.md (single source of truth).
if command -v python3 >/dev/null 2>&1; then
  python3 hack/gen-design-tokens.py
else
  echo "[build.sh] warning: python3 not found — skipping token regeneration" >&2
fi

if [ "${1:-}" = "--serve" ]; then
  echo "[build.sh] starting Astro dev server on http://localhost:4321"
  exec ${RUN} dev -- --host --port 4321
fi

echo "[build.sh] building static site into dist/"
exec ${RUN} build
