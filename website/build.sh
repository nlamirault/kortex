#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0
#
# Build the Kortex wiki into a static website with Astro (bespoke theme).
#
#   website/build.sh            # build static site into website/dist
#   website/build.sh --serve    # dev server on http://localhost:4321
#
# Requires: node + npm, python3.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE="${ROOT}/website"

for bin in node npm python3; do
  if ! command -v "${bin}" >/dev/null 2>&1; then
    echo "error: '${bin}' not found in PATH" >&2
    echo "  install: brew install node" >&2
    exit 1
  fi
done

echo "==> Rebuilding knowledge-base entity pages"
(cd "${ROOT}" && python3 scripts/build_knowledge_base.py)

echo "==> Syncing wiki/ into Astro content"
python3 "${SITE}/prepare_content.py" --src "${ROOT}/wiki" --dst "${SITE}/src/content/docs"

cd "${SITE}"

echo "==> Installing dependencies"
if [ -f package-lock.json ]; then
  npm ci
else
  npm install --no-audit --no-fund
fi

if [ "${1:-}" = "--serve" ]; then
  echo "==> Serving dev server on http://localhost:4321"
  exec npm run dev
fi

echo "==> Building static site into website/dist"
npm run build

echo "==> Building Pagefind search index"
npx --yes pagefind --site dist

echo "==> Done: website/dist"
