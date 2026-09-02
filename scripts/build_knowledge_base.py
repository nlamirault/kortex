#!/usr/bin/env python3
"""
build_knowledge_base.py — regenerates wiki/kb/ entity pages and wiki/knowledge-base.md
from the knowledge-graph edges embedded in wiki pages.

Two source formats are supported:

  1. Canonical `## Relations` tables (see CLAUDE.md) — a 3-column
     `Subject | Predicate | Object` edge list whose Subject/Object cells use
     `[[type:slug]]` wikilinks. This is the format the wiki is written in.

  2. Legacy `## KnowledgeGraph` sections with `### Triples` / `### Entities`
     subtables (older source pages). Still parsed so their data is not lost.

Entity display names are resolved from the target page's frontmatter `title`
when a wiki page exists for that `[[type:slug]]`.

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

# entity type -> wiki directory (from CLAUDE.md entity-type table)
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
DIR_TYPE = {v: k for k, v in TYPE_DIR.items()}

WIKILINK_RE = re.compile(r"\[\[([a-z]+):([^\]|]+?)(?:\|([^\]]+))?\]\]")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def read_frontmatter_title(path: Path) -> str | None:
    """Cheap YAML-frontmatter `title:` read without a YAML dependency."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    for line in text[3:end].splitlines():
        m = re.match(r"\s*title:\s*(.+)\s*$", line)
        if m:
            return m.group(1).strip().strip("'\"")
    return None


def build_page_index(wiki_dir: Path) -> dict[str, dict]:
    """Map `type::slug` -> {title, path} for every real wiki entity page."""
    index: dict[str, dict] = {}
    for md in sorted(wiki_dir.rglob("*.md")):
        rel = md.relative_to(wiki_dir)
        if len(rel.parts) < 2:
            continue
        etype = DIR_TYPE.get(rel.parts[0])
        if not etype:
            continue
        slug = md.stem
        key = f"{etype}::{slug}"
        index[key] = {
            "title": read_frontmatter_title(md) or slug,
            "path": rel,
        }
    return index


def parse_cell(cell: str) -> dict:
    """Resolve a table cell into a graph node.

    Returns a dict with `is_entity`; when True, also `type`, `slug`, `display`.
    A `[[type:slug]]` (optionally `[[type:slug|Alias]]`) cell is an entity;
    plain text is a literal object (leaf value, not its own node).
    """
    cell = cell.strip()
    m = WIKILINK_RE.search(cell)
    if m:
        etype, slug, alias = m.group(1), m.group(2).strip(), m.group(3)
        note = cell[m.end():].strip()  # trailing gloss, e.g. "(USDC)"
        return {
            "is_entity": True,
            "type": etype,
            "slug": slug,
            "display": (alias or slug).strip(),
            "note": note,
        }
    return {"is_entity": False, "display": cell}


def make_typed_node(name: str, etype: str) -> dict:
    """Node from a legacy KnowledgeGraph cell that carries an explicit type."""
    name = name.strip()
    if not name or not etype:
        return {"is_entity": False, "display": name}
    return {
        "is_entity": True,
        "type": etype.strip().lower(),
        "slug": slugify(name),
        "display": name,
        "note": "",
    }


def parse_table(lines: list[str]) -> list[dict]:
    """Parse a pipe-delimited markdown table into a list of row dicts."""
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


def extract_relations(lines: list[str], src: str) -> list[dict]:
    """Triples from canonical `## Relations` tables."""
    triples: list[dict] = []
    in_section = False
    table: list[str] = []

    def flush() -> None:
        for row in parse_table(table):
            subj = parse_cell(row.get("Subject", ""))
            pred = row.get("Predicate", "").strip()
            obj = parse_cell(row.get("Object", ""))
            if not subj["is_entity"] or not pred:
                continue  # convention: subject is always a typed entity
            triples.append({"subj": subj, "pred": pred, "obj": obj, "src": src})
        table.clear()

    for line in lines:
        if re.match(r"^##\s+Relations\b", line):
            in_section = True
            continue
        if in_section and re.match(r"^##\s+", line):
            flush()
            in_section = False
            continue
        if in_section and line.lstrip().startswith("|"):
            table.append(line)
    if in_section:
        flush()
    return triples


def extract_knowledge_graph(lines: list[str], src: str) -> list[dict]:
    """Triples from legacy `## KnowledgeGraph` -> `### Triples` subtables."""
    triples: list[dict] = []
    in_kg = False
    in_triples = False
    table: list[str] = []

    def flush() -> None:
        for row in parse_table(table):
            subj = make_typed_node(
                row.get("Subject", ""), row.get("Type_Subject", row.get("Subject_Type", ""))
            )
            pred = row.get("Predicate", "").strip()
            obj_type = row.get("Type_Object", row.get("Object_Type", "")).strip()
            obj = (
                make_typed_node(row.get("Object", ""), obj_type)
                if obj_type
                else parse_cell(row.get("Object", ""))
            )
            if not subj["is_entity"] or not pred:
                continue
            triples.append({"subj": subj, "pred": pred, "obj": obj, "src": src})
        table.clear()

    for line in lines:
        if re.match(r"^##\s+KnowledgeGraph\b", line):
            in_kg = True
            continue
        if in_kg and re.match(r"^##\s+", line):
            flush()
            in_kg = in_triples = False
            continue
        if in_kg and re.match(r"^###\s+Triples\b", line):
            flush()
            in_triples = True
            continue
        if in_kg and re.match(r"^###\s+", line):
            flush()
            in_triples = False
            continue
        if in_kg and in_triples and line.lstrip().startswith("|"):
            table.append(line)
    if in_kg:
        flush()
    return triples


def collect(wiki_dir: Path, page_index: dict) -> tuple[dict, list[dict], dict]:
    """Walk wiki/, collect all edges. Returns (entities, triples, entity_edges)."""
    all_triples: list[dict] = []

    for md in sorted(wiki_dir.rglob("*.md")):
        rel = md.relative_to(wiki_dir)
        if rel.parts[0] == SKIP_KB_DIR or md.stem in SKIP_STEMS:
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        src = str(rel)
        all_triples.extend(extract_relations(lines, src))
        all_triples.extend(extract_knowledge_graph(lines, src))

    entities: dict[str, dict] = {}
    entity_edges: dict[str, list] = defaultdict(list)

    # Seed one entity per wiki page, so the graph covers the whole wiki — not
    # only pages that happen to carry a `## Relations` table. Relations below
    # then enrich these with edges (deduped by the shared `type::slug` key).
    for key, page in page_index.items():
        etype, slug = key.split("::", 1)
        entities[key] = {
            "name": page["title"],
            "type": etype,
            "slug": slug,
            "wiki_path": page["path"],
            "sources": {str(page["path"])},
            "out": 0,
            "in": 0,
        }

    def touch(node: dict, src: str) -> str | None:
        if not node["is_entity"]:
            return None
        key = f"{node['type']}::{node['slug']}"
        page = page_index.get(key)
        if key not in entities:
            entities[key] = {
                "name": page["title"] if page else node["display"],
                "type": node["type"],
                "slug": node["slug"],
                "wiki_path": page["path"] if page else None,
                "sources": set(),
                "out": 0,
                "in": 0,
            }
        entities[key]["sources"].add(src)
        return key

    for t in all_triples:
        sk = touch(t["subj"], t["src"])
        ok = touch(t["obj"], t["src"])
        if sk:
            entities[sk]["out"] += 1
            entity_edges[sk].append(("out", t))
        if ok:
            entities[ok]["in"] += 1
            entity_edges[ok].append(("in", t))

    for e in entities.values():
        e["is_major"] = e["out"] >= 3 or len(e["sources"]) >= 3
        e["source_list"] = sorted(e["sources"])
        del e["sources"]

    return entities, all_triples, entity_edges


def obj_label(node: dict) -> str:
    """Display label for an object cell in a relation table."""
    if node["is_entity"]:
        label = node["display"]
        return f"{label} {node['note']}".strip() if node.get("note") else label
    return node["display"]


def write_entity_page(entity: dict, edges: list, kb_dir: Path) -> None:
    slug = slugify(f"{entity['type']}-{entity['slug']}")
    today = date.today().isoformat()
    lines = [
        "---",
        f"title: {entity['name']}",
        "type: kb-entity",
        f"entity_type: {entity['type']}",
        "status: auto-generated",
        f"updated: {today}",
        "---",
        "",
        f"# {entity['name']}",
        "",
        f"**Type:** {entity['type']}  ",
        f"**Tier:** {'Major ★' if entity['is_major'] else 'Minor'}  ",
        f"**Degree:** {entity['out']} out / {entity['in']} in  ",
        f"**Source pages:** {len(entity['source_list'])}",
        "",
    ]

    if entity["wiki_path"]:
        lines += [f"**Wiki page:** [{entity['name']}](../{entity['wiki_path']})", ""]

    outgoing = [t for d, t in edges if d == "out"]
    incoming = [t for d, t in edges if d == "in"]

    if outgoing:
        lines += [
            "## Outgoing Relations",
            "",
            "| Predicate | Object | Source |",
            "|-----------|--------|--------|",
        ]
        for t in outgoing:
            lines.append(f"| {t['pred']} | {obj_label(t['obj'])} | {Path(t['src']).name} |")
        lines.append("")

    if incoming:
        lines += [
            "## Incoming Relations",
            "",
            "| Subject | Predicate | Source |",
            "|---------|-----------|--------|",
        ]
        for t in incoming:
            lines.append(f"| {t['subj']['display']} | {t['pred']} | {Path(t['src']).name} |")
        lines.append("")

    lines += ["## Source Pages", ""]
    for sp in entity["source_list"]:
        lines.append(f"- [{sp}](../{sp})")
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
        letter = e["name"][0].upper() if e["name"] else "?"
        if letter != current_letter:
            lines += [f"## {letter}", ""]
            current_letter = letter
        tier = "★" if e["is_major"] else "·"
        slug = slugify(f"{e['type']}-{e['slug']}")
        lines.append(f"- {tier} [{e['name']}]({slug}.md) — {e['type']}")
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
            slug = slugify(f"{e['type']}-{e['slug']}")
            lines.append(f"- {tier} [{e['name']}]({slug}.md)")
        (kb_dir / f"_index-type-{slug_type}.md").write_text("\n".join(lines), encoding="utf-8")


def write_dashboard(entities: dict, all_triples: list) -> None:
    today = date.today().isoformat()
    major = [e for e in entities.values() if e["is_major"]]
    minor = [e for e in entities.values() if not e["is_major"]]
    by_type: dict[str, list] = defaultdict(list)
    for e in entities.values():
        by_type[e["type"]].append(e)
    top10 = sorted(entities.values(), key=lambda e: e["out"], reverse=True)[:10]

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
        slug = slugify(f"{e['type']}-{e['slug']}")
        lines.append(
            f"| [{e['name']}](kb/{slug}.md) | {e['type']} "
            f"| {e['out']} | {len(e['source_list'])} |"
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

    print("Indexing wiki pages...")
    page_index = build_page_index(WIKI_DIR)
    print(f"  {len(page_index)} entity pages")

    print("Scanning wiki/ for Relations / KnowledgeGraph edges...")
    entities, all_triples, entity_edges = collect(WIKI_DIR, page_index)
    print(f"  {len(entities)} entities, {len(all_triples)} triples")

    KB_DIR.mkdir(exist_ok=True)
    for f in KB_DIR.glob("*.md"):
        f.unlink()

    for key, entity in entities.items():
        write_entity_page(entity, entity_edges[key], KB_DIR)
    print(f"  Wrote {len(entities)} entity pages → wiki/kb/")

    write_entity_index(entities, KB_DIR)
    write_type_indexes(entities, KB_DIR)
    print("  Wrote indexes → wiki/kb/_index-*.md")

    write_dashboard(entities, all_triples)
    print(f"  Dashboard → {KNOWLEDGE_BASE_MD}")
    print("Done.")


if __name__ == "__main__":
    main()
