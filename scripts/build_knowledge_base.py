#!/usr/bin/env python3
"""
build_knowledge_base.py — regenerates wiki/kb/ entity pages and wiki/knowledge-base.md
from ## KnowledgeGraph sections embedded in wiki pages.

Run from the kortex/ root:
    python3 scripts/build_knowledge_base.py
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import date

WIKI_DIR = Path("wiki")
KB_DIR = WIKI_DIR / "kb"
KNOWLEDGE_BASE_MD = WIKI_DIR / "knowledge-base.md"
SKIP_STEMS = {"index", "log", "hot", "overview", "schema", "knowledge-base"}
SKIP_KB_DIR = "kb"


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse_table(lines: list[str]) -> list[dict]:
    """Parse pipe-delimited markdown table into list of dicts."""
    headers: list[str] | None = None
    rows: list[dict] = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        if headers is None:
            headers = cells
        elif all(re.fullmatch(r"[-: ]+", c) for c in cells):
            continue  # separator row
        elif len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
    return rows


def extract_kg(path: Path) -> tuple[list[dict], list[dict]]:
    """Return (triples, entities) from ## KnowledgeGraph section of a wiki page."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    triples: list[dict] = []
    entities: list[dict] = []
    in_kg = False
    current_table: str | None = None
    table_lines: list[str] = []

    def flush():
        nonlocal table_lines
        if current_table == "triples":
            triples.extend(parse_table(table_lines))
        elif current_table == "entities":
            entities.extend(parse_table(table_lines))
        table_lines = []

    for line in lines:
        if re.match(r"^## KnowledgeGraph", line):
            in_kg = True
            continue
        if in_kg and re.match(r"^## ", line):
            flush()
            in_kg = False
            current_table = None
            continue
        if in_kg:
            if re.match(r"^### Triples", line):
                flush()
                current_table = "triples"
            elif re.match(r"^### Entities", line):
                flush()
                current_table = "entities"
            elif line.startswith("|") and current_table:
                table_lines.append(line)

    flush()
    return triples, entities


def collect(wiki_dir: Path) -> tuple[dict, list[dict], dict]:
    """Walk wiki/, collect all KG data. Returns (entities, all_triples, entity_triples)."""
    all_triples: list[dict] = []
    entities: dict[str, dict] = {}  # key=TYPE::name_lower
    entity_triples: dict[str, list] = defaultdict(list)

    for md in sorted(wiki_dir.rglob("*.md")):
        rel = md.relative_to(wiki_dir)
        if rel.parts[0] == SKIP_KB_DIR:
            continue
        if md.stem in SKIP_STEMS:
            continue

        page_triples, page_entities = extract_kg(md)

        for t in page_triples:
            t["_src"] = str(md)
            all_triples.append(t)

        for e in page_entities:
            name = e.get("Entity", "").strip()
            etype = e.get("Type", "").strip()
            if not name or not etype:
                continue
            key = f"{etype}::{name.lower()}"
            if key not in entities:
                entities[key] = {
                    "name": name,
                    "type": etype,
                    "attrs": {},
                    "sources": set(),
                    "out_triples": 0,
                }
            attr = e.get("Attribute", "").strip()
            val = e.get("Value", "").strip()
            if attr and val:
                entities[key]["attrs"][attr] = val
            entities[key]["sources"].add(str(md))

    for t in all_triples:
        subj = t.get("Subject", "").strip()
        stype = t.get("Type_Subject", "").strip()
        obj = t.get("Object", "").strip()
        otype = t.get("Type_Object", "").strip()
        sk = f"{stype}::{subj.lower()}"
        ok = f"{otype}::{obj.lower()}"
        if sk in entities:
            entities[sk]["out_triples"] += 1
        entity_triples[sk].append(("out", t))
        entity_triples[ok].append(("in", t))

    for e in entities.values():
        e["is_major"] = e["out_triples"] >= 3 or len(e["sources"]) >= 3
        e["source_list"] = sorted(e["sources"])
        del e["sources"]

    return entities, all_triples, entity_triples


def write_entity_page(entity: dict, triples: list, kb_dir: Path) -> None:
    slug = slugify(entity["name"])
    today = date.today().isoformat()
    lines = [
        "---",
        f"title: {entity['name']}",
        "type: kb-entity",
        f"entity_type: {entity['type']}",
        "status: auto-generated",
        f"updated: {today}",
        f"sources: {entity['source_list']}",
        "---",
        "",
        f"# {entity['name']}",
        "",
        f"**Type:** {entity['type']}  ",
        f"**Tier:** {'Major ★' if entity['is_major'] else 'Minor'}  ",
        f"**Outgoing triples:** {entity['out_triples']}  ",
        f"**Source pages:** {len(entity['source_list'])}",
        "",
    ]

    if entity["attrs"]:
        lines += ["## Attributes", ""]
        for attr, val in entity["attrs"].items():
            lines.append(f"- **{attr}:** {val}")
        lines.append("")

    outgoing = [t for d, t in triples if d == "out"]
    incoming = [t for d, t in triples if d == "in"]

    if outgoing:
        lines += [
            "## Outgoing Relations", "",
            "| Predicate | Object | Type | Confidence | Temporality | Source |",
            "|-----------|--------|------|------------|-------------|--------|",
        ]
        for t in outgoing:
            src = Path(t["_src"]).name
            lines.append(
                f"| {t.get('Predicate','')} | {t.get('Object','')} | "
                f"{t.get('Type_Object','')} | {t.get('Confidence','')} | "
                f"{t.get('Temporality','')} | {src} |"
            )
        lines.append("")

    if incoming:
        lines += [
            "## Incoming Relations", "",
            "| Subject | Type | Predicate | Confidence | Source |",
            "|---------|------|-----------|------------|--------|",
        ]
        for t in incoming:
            src = Path(t["_src"]).name
            lines.append(
                f"| {t.get('Subject','')} | {t.get('Type_Subject','')} | "
                f"{t.get('Predicate','')} | {t.get('Confidence','')} | {src} |"
            )
        lines.append("")

    lines += ["## Source Pages", ""]
    for sp in entity["source_list"]:
        try:
            rel = Path(sp).relative_to(WIKI_DIR)
            lines.append(f"- [{rel}](../{rel})")
        except ValueError:
            lines.append(f"- {sp}")
    lines.append("")

    (kb_dir / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_entity_index(entities: dict, kb_dir: Path) -> None:
    today = date.today().isoformat()
    sorted_e = sorted(entities.values(), key=lambda e: e["name"].lower())
    lines = [
        "---",
        "title: Entity Index",
        "type: kb-index",
        "status: auto-generated",
        f"updated: {today}",
        "---",
        "",
        "# Entity Index",
        "",
        f"*{len(entities)} entities — auto-generated*",
        "",
    ]
    current_letter = ""
    for e in sorted_e:
        letter = (e["name"][0].upper() if e["name"] else "?")
        if letter != current_letter:
            lines += [f"## {letter}", ""]
            current_letter = letter
        tier = "★" if e["is_major"] else "·"
        lines.append(f"- {tier} [{e['name']}]({slugify(e['name'])}.md) — {e['type']}")
    (kb_dir / "_index-entities.md").write_text("\n".join(lines), encoding="utf-8")


def write_type_indexes(entities: dict, kb_dir: Path) -> None:
    today = date.today().isoformat()
    by_type: dict[str, list] = defaultdict(list)
    for e in sorted(entities.values(), key=lambda e: e["name"].lower()):
        by_type[e["type"]].append(e)

    for etype, elist in sorted(by_type.items()):
        slug_type = slugify(etype)
        lines = [
            "---",
            f"title: {etype} Index",
            "type: kb-index",
            "status: auto-generated",
            f"updated: {today}",
            "---",
            "",
            f"# {etype}",
            "",
            f"*{len(elist)} entities*",
            "",
        ]
        for e in elist:
            tier = "★" if e["is_major"] else "·"
            lines.append(f"- {tier} [{e['name']}]({slugify(e['name'])}.md)")
        (kb_dir / f"_index-type-{slug_type}.md").write_text("\n".join(lines), encoding="utf-8")


def write_dashboard(entities: dict, all_triples: list) -> None:
    today = date.today().isoformat()
    major = [e for e in entities.values() if e["is_major"]]
    minor = [e for e in entities.values() if not e["is_major"]]
    by_type: dict[str, list] = defaultdict(list)
    for e in entities.values():
        by_type[e["type"]].append(e)
    top10 = sorted(entities.values(), key=lambda e: e["out_triples"], reverse=True)[:10]

    lines = [
        "---",
        "title: Knowledge Base Dashboard",
        "type: kb-dashboard",
        "status: auto-generated",
        f"updated: {today}",
        "---",
        "",
        "# Knowledge Base Dashboard",
        "",
        f"*Auto-generated by `scripts/build_knowledge_base.py` on {today}*",
        "",
        "## Stats",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total entities | {len(entities)} |",
        f"| Major entities (★) | {len(major)} |",
        f"| Minor entities | {len(minor)} |",
        f"| Total triples | {len(all_triples)} |",
        "",
        "## Entities by Type",
        "",
        "| Type | Count | Index |",
        "|------|-------|-------|",
    ]
    for etype, elist in sorted(by_type.items(), key=lambda x: -len(x[1])):
        lines.append(f"| {etype} | {len(elist)} | [→](kb/_index-type-{slugify(etype)}.md) |")

    lines += [
        "",
        "## Top Entities by Degree",
        "",
        "| Entity | Type | Outgoing | Sources |",
        "|--------|------|----------|---------|",
    ]
    for e in top10:
        lines.append(
            f"| [{e['name']}](kb/{slugify(e['name'])}.md) | {e['type']} "
            f"| {e['out_triples']} | {len(e['source_list'])} |"
        )

    lines += [
        "",
        "## Navigation",
        "",
        "- [All entities alphabetical](kb/_index-entities.md)",
    ]
    for etype in sorted(by_type):
        lines.append(f"- [{etype}](kb/_index-type-{slugify(etype)}.md)")
    lines.append("")

    KNOWLEDGE_BASE_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not WIKI_DIR.exists():
        print("Error: wiki/ not found. Run from kortex/ root.", file=sys.stderr)
        sys.exit(1)

    print("Scanning wiki/ for KnowledgeGraph sections...")
    entities, all_triples, entity_triples = collect(WIKI_DIR)
    print(f"  {len(entities)} entities, {len(all_triples)} triples")

    KB_DIR.mkdir(exist_ok=True)
    for f in KB_DIR.glob("*.md"):
        f.unlink()

    for key, entity in entities.items():
        write_entity_page(entity, entity_triples[key], KB_DIR)
    print(f"  Wrote {len(entities)} entity pages → wiki/kb/")

    write_entity_index(entities, KB_DIR)
    write_type_indexes(entities, KB_DIR)
    print("  Wrote indexes → wiki/kb/_index-*.md")

    write_dashboard(entities, all_triples)
    print(f"  Dashboard → {KNOWLEDGE_BASE_MD}")
    print("Done.")


if __name__ == "__main__":
    main()
