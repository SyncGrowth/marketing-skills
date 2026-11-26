#!/usr/bin/env python3
"""Record which source commit a mirrored skill was copied from.

A skill with "authoring": "mirror" in skills.json is edited in its source repository (for
kreacje: the SyncBooster backend, directory skills/kreacje) and copied here unchanged. After
you copy the files, run:

    python3 scripts/stamp_mirror.py kreacje --source-commit <40-character sha of the source repository>

The script writes the commit, the contract and catalog versions from the skill's skill.json and a
digest of the skill folder into skills.json. scripts/validate_skills.py fails when the files and
the digest disagree, so an edit made directly in this repository is caught.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from validate_skills import ROOT, SKILLS_DIR, skill_digest

COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skill")
    parser.add_argument("--source-commit", required=True, help="full 40-character sha in the source repository")
    parser.add_argument("--of", help="human-readable source, default: keep the current value")
    args = parser.parse_args()

    if not COMMIT_RE.match(args.source_commit):
        print("error: --source-commit must be a full 40-character lowercase sha", file=sys.stderr)
        return 1
    index_path = ROOT / "skills.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    entry = index.get("skills", {}).get(args.skill)
    skill_dir = SKILLS_DIR / args.skill
    if entry is None or not skill_dir.is_dir():
        print(f"error: '{args.skill}' is not in skills.json or has no folder", file=sys.stderr)
        return 1
    if entry.get("authoring") != "mirror":
        print(f"error: '{args.skill}' is not a mirrored skill", file=sys.stderr)
        return 1
    declared = json.loads((skill_dir / "skill.json").read_text(encoding="utf-8"))
    previous = entry.get("mirror", {})
    entry["mirror"] = {
        "of": args.of or previous.get("of", ""),
        "source_commit": args.source_commit,
        "contract_version": str(declared["contractVersion"]),
        "catalog_version": str(declared["catalogVersion"]),
        "content_sha256": skill_digest(skill_dir),
    }
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"stamped {args.skill}: source {args.source_commit[:8]}, catalog {entry['mirror']['catalog_version']}, "
          f"digest {entry['mirror']['content_sha256'][:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
