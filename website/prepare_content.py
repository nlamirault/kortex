#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0
"""
prepare_content.py — sync wiki/ into the Astro `docs` content collection.

Transforms applied while copying:
  * drop hot.md, skill-impact.md                     (session / internal scratch)
  * guarantee a frontmatter `title` on every page    (used for nav + <title>)
  * rewrite relative `.md` links -> pretty URLs (`foo.md` -> `foo/`)

`index.md` stays `index.md`; the landing page (src/pages/index.astro) excludes
it from the docs routes and renders its own hero instead.

Usage:
    python3 website/prepare_content.py --src wiki --dst website/src/content/docs
"""

import argparse
import re
import shutil
from pathlib import Path

DROP = {"hot.md", "skill-impact.md"}

# ](target) or ](target#anchor), relative and ending in .md.
LINK_RE = re.compile(r"\]\((?!https?:|mailto:|/|#)([^)\s]+?\.md)(#[^)\s]*)?\)")


def rewrite_links(text: str) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1)[:-3]  # strip .md
        anchor = m.group(2) or ""
        if not target.endswith("/"):
            target += "/"
        return f"]({target}{anchor})"

    return LINK_RE.sub(repl, text)


def title_from_body(text: str, fallback: str) -> str:
    for line in text.splitlines():
        m = re.match(r"#\s+(.+?)\s*$", line)
        if m:
            return m.group(1)
    return fallback.replace("-", " ").replace("_", " ").title()


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def ensure_title(text: str, slug: str) -> str:
    """Guarantee a frontmatter `title:` — nav and <title> rely on it."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            front = text[3:end]
            if any(re.match(r"\s*title\s*:", ln) for ln in front.splitlines()):
                return text
            title = title_from_body(text[end + 4 :], slug)
            return f'---\ntitle: "{esc(title)}"{text[3:]}'
    title = title_from_body(text, slug)
    return f'---\ntitle: "{esc(title)}"\n---\n\n{text}'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--dst", required=True)
    args = ap.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)

    copied = dropped = 0
    for md in sorted(src.rglob("*.md")):
        rel = md.relative_to(src)
        if md.name in DROP:
            dropped += 1
            continue
        text = ensure_title(rewrite_links(md.read_text(encoding="utf-8")), md.stem)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        copied += 1

    assets = 0
    for f in sorted(src.rglob("*")):
        if f.is_dir() or f.suffix == ".md":
            continue
        out = dst / f.relative_to(src)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, out)
        assets += 1

    print(f"  content: {copied} pages, {assets} assets, {dropped} dropped")


if __name__ == "__main__":
    main()
