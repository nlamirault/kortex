#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0
"""Generate CSS design tokens from DESIGN.md — the single source of truth.

DESIGN.md frontmatter owns every token value. This script renders the
`:root { ... }` block of src/styles/global.css from those tokens, so the
stylesheet can never drift from the documented design system.

Usage:
    gen-design-tokens.py            # rewrite global.css :root block in place
    gen-design-tokens.py --check    # exit 1 if global.css is out of date (CI)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("error: PyYAML is required (pip install pyyaml)")

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "DESIGN.md"
CSS = ROOT / "src" / "styles" / "global.css"

# Source of each CSS custom property in the frontmatter:
#   ("c", key) -> colors[key]   ("s", key) -> spacing[key]
#   ("r", key) -> rounded[key]  ("x", key) -> meta.cssExtras[key]
Source = tuple[str, str]
Group = tuple[str, list[tuple[str, Source]]]

GLOBAL_LAYOUT: list[Group] = [
    ("Brand", [
        ("--rust", ("c", "brand")),
        ("--rust-dark", ("c", "brandDark")),
        ("--rust-soft", ("c", "brandSoft")),
        ("--rust-border", ("x", "rust-border")),
    ]),
    ("Canvas", [
        ("--paper", ("c", "background")),
        ("--card", ("c", "surface")),
        ("--white", ("c", "surfaceElevated")),
        ("--surface-alt", ("c", "surfaceAlt")),
        ("--line", ("c", "border")),
    ]),
    ("Ink", [
        ("--ink", ("c", "textPrimary")),
        ("--text", ("c", "text")),
        ("--muted", ("c", "textMuted")),
        ("--subtle", ("c", "textSubtle")),
    ]),
    ("Growth stages", [
        ("--seedling", ("c", "seedling")),
        ("--seedling-soft", ("c", "seedlingSoft")),
        ("--budding", ("c", "budding")),
        ("--budding-soft", ("c", "buddingSoft")),
        ("--evergreen", ("c", "evergreen")),
        ("--evergreen-soft", ("c", "evergreenSoft")),
        ("--archived", ("c", "archived")),
        ("--archived-soft", ("c", "archivedSoft")),
    ]),
    ("Semantic", [
        ("--success", ("c", "success")),
        ("--warning", ("c", "warning")),
        ("--error", ("c", "error")),
        ("--info", ("c", "info")),
        ("--link", ("c", "link")),
        ("--link-border", ("c", "linkBorder")),
    ]),
    ("Shadow", [
        ("--shadow", ("x", "shadow")),
        ("--shadow-subtle", ("x", "shadow-subtle")),
        ("--shadow-lift", ("x", "shadow-lift")),
        ("--focus-ring", ("x", "focus-ring")),
    ]),
    ("Spacing", [
        ("--space-2xs", ("s", "2xs")),
        ("--space-xs", ("s", "xs")),
        ("--space-sm", ("s", "sm")),
        ("--space-md", ("s", "md")),
        ("--space-lg", ("s", "lg")),
        ("--space-xl", ("s", "xl")),
        ("--space-2xl", ("s", "2xl")),
        ("--space-3xl", ("s", "3xl")),
        ("--space-hero", ("s", "hero")),
    ]),
    ("Radius", [
        ("--radius-sm", ("r", "sm")),
        ("--radius-md", ("r", "md")),
        ("--radius-lg", ("r", "lg")),
        ("--radius-xl", ("r", "xl")),
        ("--radius-hero", ("r", "hero")),
        ("--radius-pill", ("r", "pill")),
    ]),
    ("Container", [
        ("--container-max", ("x", "container-max")),
        ("--container-pad", ("x", "container-pad")),
        ("--measure", ("x", "measure")),
    ]),
    ("Typography", [
        ("--font-serif", ("x", "font-serif")),
        ("--font-sans", ("x", "font-sans")),
        ("--font-mono", ("x", "font-mono")),
    ]),
]

ROOT_RE = re.compile(r":root\s*\{.*?\}", re.S)


def load_tokens() -> dict:
    text = DESIGN.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("error: DESIGN.md has no YAML frontmatter")
    return yaml.safe_load(m.group(1))


def resolve(tokens: dict, source: Source) -> str:
    kind, key = source
    groups = {"c": "colors", "s": "spacing", "r": "rounded"}
    if kind in groups:
        value = tokens.get(groups[kind], {}).get(key)
    elif kind == "x":
        value = tokens.get("meta", {}).get("cssExtras", {}).get(key)
    else:  # pragma: no cover
        value = None
    if value is None:
        sys.exit(f"error: token for {source} not found in DESIGN.md")
    return str(value)


def render_root(tokens: dict) -> str:
    lines = [":root {"]
    for i, (group, entries) in enumerate(GLOBAL_LAYOUT):
        if i:
            lines.append("")
        lines.append(f"  /* {group} */")
        for prop, source in entries:
            lines.append(f"  {prop}: {resolve(tokens, source)};")
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    check = "--check" in sys.argv[1:]
    tokens = load_tokens()
    new_root = render_root(tokens)

    text = CSS.read_text()
    if not ROOT_RE.search(text):
        sys.exit(f"error: no :root block found in {CSS}")
    updated = ROOT_RE.sub(lambda _: new_root, text, count=1)
    rel = CSS.relative_to(ROOT)

    if check:
        if updated != text:
            sys.stderr.write(
                f"error: {rel} is out of date with DESIGN.md tokens.\n"
                "       run `make tokens` and commit the result.\n"
            )
            return 1
        print(f"✅ {rel} matches DESIGN.md")
        return 0

    if updated != text:
        CSS.write_text(updated)
        print(f"✅ wrote {rel} from DESIGN.md")
    else:
        print(f"✅ {rel} already up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
