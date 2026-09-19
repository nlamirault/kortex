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
import posixpath
import re
import shutil
from pathlib import Path

DROP = {"hot.md", "skill-impact.md"}

# ](target) or ](target#anchor), relative and ending in .md.
LINK_RE = re.compile(r"\]\((?!https?:|mailto:|/|#)([^)\s]+?\.md)(#[^)\s]*)?\)")

# [[type:slug]] or [[type:slug|alias]] — machine-readable wikilinks used in
# `## Relations` SPO tables. Kept raw in wiki/ (parsed by /graph); rewritten to
# clickable pretty-URL links here so the rendered site doesn't show dead text.
WIKILINK_RE = re.compile(r"\[\[([a-z]+):([^\]|]+?)(?:\|([^\]]+?))?\]\]")

# entity type -> wiki subdirectory (must match the folders under wiki/).
TYPE_DIR = {
    "concept": "concepts",
    "source": "sources",
    "person": "people",
    "project": "projects",
    "decision": "decisions",
    "domain": "domains",
    "comparison": "comparisons",
    "synthesis": "syntheses",
    "pattern": "patterns",
    "gap": "gaps",
}


def rewrite_wikilinks(text: str, base: str, titles: dict) -> str:
    """Rewrite `[[type:slug]]` -> `[title](base + dir/slug/)` pretty links.

    Display text is the alias if given, else the target page's title, else a
    humanized slug. Unknown types are left untouched.
    """

    def repl(m: re.Match) -> str:
        typ, slug, alias = m.group(1), m.group(2).strip(), m.group(3)
        directory = TYPE_DIR.get(typ)
        if directory is None or slug not in titles:
            # unknown type, or target page doesn't exist (dangling link / a
            # schema.md syntax example) — leave raw rather than fake a link.
            return m.group(0)
        text_out = (alias or titles[slug]).strip()
        return f"[{text_out}]({base}{directory}/{slug}/)"

    return WIKILINK_RE.sub(repl, text)


def rewrite_links(text: str, src_dir: str, base: str) -> str:
    """Rewrite relative `.md` links to root-absolute pretty URLs.

    Pages are served at pretty URLs (`/base/foo/`), so a page one level deep
    can't use links relative to the wiki root. Resolve each link against its
    source file's directory and emit an absolute, base-prefixed path.
    """

    def repl(m: re.Match) -> str:
        target, anchor = m.group(1)[:-3], m.group(2) or ""  # strip .md
        resolved = posixpath.normpath(posixpath.join(src_dir, target))
        if resolved.startswith(".."):  # escapes the wiki root — leave untouched
            return m.group(0)
        return f"]({base}{resolved}/{anchor})"

    return LINK_RE.sub(repl, text)


def get_title(text: str, slug: str) -> str:
    """Frontmatter `title:` if present, else first H1, else humanized slug."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for ln in text[3:end].splitlines():
                m = re.match(r'\s*title\s*:\s*"?(.+?)"?\s*$', ln)
                if m:
                    return m.group(1)
    return title_from_body(text, slug)


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
    ap.add_argument("--base", default="/", help="site base path (must match astro.config)")
    args = ap.parse_args()
    base = args.base if args.base.endswith("/") else args.base + "/"

    src = Path(args.src)
    dst = Path(args.dst)
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)

    # First pass: index slug -> title so wikilinks can show real page titles.
    titles = {}
    for md in src.rglob("*.md"):
        if md.name in DROP:
            continue
        titles[md.stem] = get_title(md.read_text(encoding="utf-8"), md.stem)

    copied = dropped = 0
    for md in sorted(src.rglob("*.md")):
        rel = md.relative_to(src)
        if md.name in DROP:
            dropped += 1
            continue
        src_dir = "" if str(rel.parent) == "." else rel.parent.as_posix()
        text = rewrite_links(md.read_text(encoding="utf-8"), src_dir, base)
        text = rewrite_wikilinks(text, base, titles)
        text = ensure_title(text, md.stem)
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
