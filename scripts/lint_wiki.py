#!/usr/bin/env python3
"""
lint_wiki.py — mechanical OKF v0.2 conformance + hygiene checks for wiki/.

Deterministic checks only; the judgment calls (contradictions, duplicate canonical
pages, whether hot.md's focus is current, gap resolution, NOT VERIFIED review) stay
in the /lint skill. This script is the `lint` half of that workflow.

Checks, by severity:
  CRITICAL  unparseable frontmatter; missing/empty `type` on a non-reserved page
            (including wiki/kb/*.md).
  WARNING   status outside draft|stable|deprecated; bare-date timestamp (no UTC
            offset) in generated.at / verified[].at / stale_after; `sources` that is
            a string list or lacks `resource`; verified[].by not in
            human:/process:/<producer>/<version> form; reserved index.md/log.md with
            stray frontmatter; placeholder (TODO/TBD/{text}/{N}); broken markdown or
            Relations-table link; bare [[type:slug]] outside a ## Relations table.
  INFO      page missing `updated:`; entity page not listed in wiki/index.md.

Exit code: non-zero if any CRITICAL is found; 0 otherwise (and 0 if wiki/ is absent).

Run from the kortex/ root:
    python3 scripts/lint_wiki.py
"""

import re
import sys
from pathlib import Path

import yaml

WIKI_DIR = Path("wiki")
RESERVED = {"index.md", "log.md"}
# schema.md is a template catalogue: its <...>, {...} and ../dir/slug.md are intentional.
TEMPLATE_EXEMPT = {"schema.md"}

STATUS_ENUM = {"draft", "stable", "deprecated"}
PLACEHOLDER_RE = re.compile(r"\bTODO\b|\bTBD\b|\{text\}|\{N\}")
WIKILINK_RE = re.compile(r"\[\[([a-z]+):([^\]|]+?)(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
OFFSET_RE = re.compile(r"(Z|[+-]\d{2}:\d{2})$")

# [[type:slug]] -> directory, per the AGENTS.md Entity Types table.
TYPE_DIR = {
    "concept": "concepts",
    "source": "sources",
    "person": "people",
    "project": "projects",
    "organization": "organizations",
    "decision": "decisions",
    "domain": "domains",
    "comparison": "comparisons",
    "synthesis": "syntheses",
    "pattern": "patterns",
    "gap": "gaps",
}
ENTITY_DIRS = set(TYPE_DIR.values())

findings: list[tuple[str, str, str]] = []  # (severity, page, message)


def report(severity: str, page: Path, message: str) -> None:
    findings.append((severity, str(page), message))


def split_frontmatter(text: str) -> tuple[str | None, int]:
    """Return (raw_frontmatter, body_start_line). raw is None when absent."""
    if not text.startswith("---\n"):
        return None, 0
    end = text.find("\n---", 4)
    if end == -1:
        return None, 0
    raw = text[4:end]
    body_start = text[: end + 4].count("\n") + 1
    return raw, body_start


def code_fence_mask(lines: list[str]) -> list[bool]:
    """True for lines inside a fenced code block (the fence lines included)."""
    mask = [False] * len(lines)
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            mask[i] = True
            in_fence = not in_fence
            continue
        mask[i] = in_fence
    return mask


def relations_mask(lines: list[str]) -> list[bool]:
    """True for lines inside a ## Relations section (heading excluded)."""
    mask = [False] * len(lines)
    in_rel = False
    for i, line in enumerate(lines):
        if re.match(r"^##\s+Relations\b", line):
            in_rel = True
            continue
        if in_rel and re.match(r"^##\s+", line):
            in_rel = False
        mask[i] = in_rel
    return mask


def check_offset(page: Path, label: str, value) -> None:
    if isinstance(value, str) and not OFFSET_RE.search(value.strip()):
        # Tolerate unfilled template-style placeholders like <ISO-8601 ...>.
        if value.strip().startswith("<"):
            return
        report("WARNING", page, f"{label} '{value}' lacks a UTC offset (ISO 8601 required)")


def lint_frontmatter(page: Path, raw: str, generated: bool = False) -> None:
    name = page.name
    try:
        # BaseLoader is safe (strings only — it never constructs Python objects from
        # !!python tags) AND keeps timestamps as strings, so the UTC-offset checks below
        # see the literal text instead of PyYAML-coerced date/datetime objects.
        fm = yaml.load(raw, Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        report("CRITICAL", page, f"unparseable YAML frontmatter: {exc}")
        return
    if not isinstance(fm, dict):
        report("CRITICAL", page, "frontmatter is not a mapping")
        return

    if name == "index.md":
        stray = set(fm) - {"okf_version"}
        if stray:
            report("WARNING", page, f"reserved index.md carries stray frontmatter: {sorted(stray)}")
        return

    # type (required on every non-reserved page, incl. kb/)
    if not fm.get("type"):
        report("CRITICAL", page, "missing or empty `type`")

    # builder-generated nodes (wiki/kb/*, knowledge-base.md) are regenerated by
    # `make kb`; only their `type` is our concern — the rest is the builder's output.
    if generated:
        return

    # status enum
    status = fm.get("status")
    if status is not None and status not in STATUS_ENUM:
        report("WARNING", page, f"status '{status}' outside {sorted(STATUS_ENUM)}")

    # sources: list of mappings, each with a resource
    src = fm.get("sources")
    if src is not None:
        if not isinstance(src, list):
            report("WARNING", page, "`sources` must be a list of mappings")
        else:
            for i, entry in enumerate(src):
                if not isinstance(entry, dict):
                    report("WARNING", page, f"sources[{i}] is a string; must be a mapping with `resource`")
                elif "resource" not in entry:
                    report("WARNING", page, f"sources[{i}] lacks a `resource` key")

    # generated.at
    gen = fm.get("generated")
    if isinstance(gen, dict) and "at" in gen:
        check_offset(page, "generated.at", gen["at"])

    # verified: list of {by, at}
    ver = fm.get("verified")
    if isinstance(ver, list):
        for i, entry in enumerate(ver):
            if not isinstance(entry, dict):
                continue
            by = entry.get("by", "")
            if by and not (
                by.startswith("human:") or by.startswith("process:") or "/" in by
            ):
                report("WARNING", page, f"verified[{i}].by '{by}' not human:/process:/<producer>/<version>")
            if "at" in entry:
                check_offset(page, f"verified[{i}].at", entry["at"])

    # stale_after
    if "stale_after" in fm:
        check_offset(page, "stale_after", fm["stale_after"])

    # updated (hygiene)
    if "updated" not in fm:
        report("INFO", page, "missing `updated:`")


def lint_body(page: Path, lines: list[str], body_start: int) -> None:
    exempt = page.name in TEMPLATE_EXEMPT
    fences = code_fence_mask(lines)
    rels = relations_mask(lines)
    for i, line in enumerate(lines):
        if fences[i]:
            continue
        lineno = body_start + i + 1
        scan = INLINE_CODE_RE.sub("", line)  # drop inline code spans

        if not exempt and PLACEHOLDER_RE.search(scan):
            report("WARNING", page, f"line {lineno}: placeholder ({PLACEHOLDER_RE.search(scan).group(0)})")

        # bare [[type:slug]] outside a Relations table
        for m in WIKILINK_RE.finditer(scan):
            if not rels[i] and not exempt:
                report("WARNING", page, f"line {lineno}: bare [[{m.group(1)}:{m.group(2)}]] outside ## Relations")
            # broken target (checked in both Relations and prose)
            etype, slug = m.group(1), m.group(2).strip()
            directory = TYPE_DIR.get(etype)
            if directory and not exempt:
                target = WIKI_DIR / directory / f"{slug}.md"
                if not target.exists():
                    report("WARNING", page, f"line {lineno}: broken wikilink [[{etype}:{slug}]] -> {target}")

        # broken markdown links to local .md
        if not exempt:
            for m in MD_LINK_RE.finditer(scan):
                dest = m.group(1).split("#", 1)[0].strip()
                if not dest or "://" in dest or dest.startswith("<") or not dest.endswith(".md"):
                    continue
                target = (page.parent / dest).resolve()
                if not target.exists():
                    report("WARNING", page, f"line {lineno}: broken link -> {dest}")


def main() -> int:
    if not WIKI_DIR.is_dir():
        print("lint_wiki: no wiki/ directory — nothing to check.")
        return 0

    log = WIKI_DIR / "log.md"
    if log.exists() and log.read_text(encoding="utf-8").startswith("---\n"):
        report("WARNING", log, "reserved log.md must not carry frontmatter")

    index_text = ""
    index = WIKI_DIR / "index.md"
    if index.exists():
        index_text = index.read_text(encoding="utf-8")

    for md in sorted(WIKI_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()
        raw, body_start = split_frontmatter(text)

        if md.name == "log.md":
            continue  # reserved, handled above
        if raw is None:
            if md.name != "index.md":
                report("CRITICAL", md, "missing frontmatter")
            continue

        rel = md.relative_to(WIKI_DIR)
        generated = rel.parts[0] == "kb" or md.name == "knowledge-base.md"

        lint_frontmatter(md, raw, generated=generated)
        if generated:
            continue  # builder output — skip body and orphan checks

        lint_body(md, lines[body_start:], body_start)

        # orphan: entity page not listed in index.md
        if rel.parts and rel.parts[0] in ENTITY_DIRS and rel.as_posix() not in index_text:
            report("INFO", md, "not listed in wiki/index.md")

    order = {"CRITICAL": 0, "WARNING": 1, "INFO": 2}
    findings.sort(key=lambda f: (order[f[0]], f[1]))
    counts = {"CRITICAL": 0, "WARNING": 0, "INFO": 0}
    for sev, page, msg in findings:
        counts[sev] += 1
        print(f"{sev:8} {page}: {msg}")

    print(
        f"\nlint_wiki: {counts['CRITICAL']} critical, "
        f"{counts['WARNING']} warning, {counts['INFO']} info."
    )
    return 1 if counts["CRITICAL"] else 0


if __name__ == "__main__":
    sys.exit(main())
