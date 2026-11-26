#!/usr/bin/env python3
"""Regenerate the generated skill tables from skills.json.

Blocks between `<!-- generated:NAME:start -->` and `<!-- generated:NAME:end -->`
markers are rewritten in README.md and README.pl.md.

    python3 scripts/build_index.py          rewrite files
    python3 scripts/build_index.py --check  exit 1 if a file is out of date
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))


def source_cell(entry: dict) -> str:
    if entry["authoring"] == "mirror":
        mirror = entry["mirror"]
        return f"Mirror of {mirror['of']}, catalog {mirror['catalog_version']}"
    return "Written here"


def table_skills() -> str:
    lines = []
    for category in INDEX["categories"]:
        members = [(n, e) for n, e in INDEX["skills"].items() if e["category"] == category]
        if not members:
            continue
        lines += ["", f"### {category}", "", "| Skill | What it does | Source |", "|---|---|---|"]
        for name, entry in sorted(members):
            lines.append(f"| [`{name}`](skills/{name}/SKILL.md) | {entry['summary']} | {source_cell(entry)} |")
    return "\n".join(lines).strip("\n")


BLOCKS = {"skills": table_skills}
FILES = [ROOT / "README.md", ROOT / "README.pl.md"]
BLOCK_RE = re.compile(r"(<!-- generated:(\w+):start -->)(.*?)(<!-- generated:\2:end -->)", re.S)


def render(text: str) -> str:
    def repl(match: re.Match) -> str:
        start, name, _, end = match.groups()
        if name not in BLOCKS:
            raise SystemExit(f"unknown generated block '{name}'")
        return f"{start}\n{BLOCKS[name]()}\n{end}"

    return BLOCK_RE.sub(repl, text)


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for path in FILES:
        if not path.is_file():
            continue
        old = path.read_text(encoding="utf-8")
        new = render(old)
        if new != old:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check:
                path.write_text(new, encoding="utf-8")
    if check and stale:
        print("out of date: " + ", ".join(stale))
        return 1
    if stale:
        print("updated: " + ", ".join(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
