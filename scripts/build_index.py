#!/usr/bin/env python3
"""Regenerate the generated tables from skills.json and each skill's frontmatter.

Blocks between `<!-- generated:NAME:start -->` and `<!-- generated:NAME:end -->`
markers are rewritten in README.md, README.pl.md and docs/PROVENANCE.md.

    python3 scripts/build_index.py          rewrite files
    python3 scripts/build_index.py --check  exit 1 if a file is out of date
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
INDEX = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))


def frontmatter(name: str) -> dict:
    text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    return yaml.safe_load(text[4:end])


def table_skills() -> str:
    lines = []
    for category in INDEX["categories"]:
        members = [(n, e) for n, e in INDEX["skills"].items() if e["category"] == category]
        if not members:
            continue
        lines += ["", f"### {category}", "", "| Skill | What it does | Version |", "|---|---|---|"]
        for name, entry in sorted(members):
            version = frontmatter(name).get("metadata", {}).get("version", "")
            marker = " (original)" if entry["origin"] == "original" else ""
            lines.append(f"| [`{name}`](skills/{name}/SKILL.md){marker} | {entry['summary']} | {version} |")
    return "\n".join(lines).strip("\n")


def table_provenance() -> str:
    credits = INDEX.get("credits", {})
    lines = ["| Skill | Version | Origin | License | Third-party credits kept in the skill |", "|---|---|---|---|---|"]
    for name, entry in sorted(INDEX["skills"].items()):
        version = frontmatter(name).get("metadata", {}).get("version", "")
        if entry["origin"] == "original":
            origin, lic = "Original, SyncGrowth", "MIT"
        else:
            origin, lic = f"Upstream {INDEX['upstream']['commit'][:7]}", "MIT (Corey Haines)"
        lines.append(f"| `{name}` | {version} | {origin} | {lic} | {credits.get(name, 'none')} |")
    return "\n".join(lines)


def counts() -> str:
    total = len(INDEX["skills"])
    original = sum(1 for e in INDEX["skills"].values() if e["origin"] == "original")
    return f"{total} skills ({total - original} adapted from the MIT-licensed upstream, {original} original)"


def total() -> str:
    return str(len(INDEX["skills"]))


BLOCKS = {"skills": table_skills, "provenance": table_provenance, "counts": counts, "total": total}
FILES = [ROOT / "README.md", ROOT / "README.pl.md", ROOT / "docs" / "PROVENANCE.md"]
BLOCK_RE = re.compile(r"(<!-- generated:(\w+):start -->)(.*?)(<!-- generated:\2:end -->)", re.S)
INLINE_BLOCKS = {"counts", "total"}


def render(text: str) -> str:
    def repl(match: re.Match) -> str:
        start, name, _, end = match.groups()
        if name not in BLOCKS:
            raise SystemExit(f"unknown generated block '{name}'")
        body = BLOCKS[name]()
        if name in INLINE_BLOCKS:
            return f"{start}{body}{end}"
        return f"{start}\n{body}\n{end}"

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
