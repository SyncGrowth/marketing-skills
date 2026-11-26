#!/usr/bin/env python3
"""Validate the skills in this repository.

Checks every skills/<name>/SKILL.md against the Agent Skills specification
(https://agentskills.io/specification) plus a few repository rules:

* frontmatter parses, only spec fields are used, name matches the folder
* description is 1-1024 characters; metadata is a string-to-string map
* every skill is listed in skills.json and every entry has a folder
* a skill with "authoring": "mirror" carries a mirror stamp that matches its files
  (see docs/PROVENANCE.md and scripts/stamp_mirror.py)
* skill.json and evals/evals.json (when present) are valid JSON
* relative markdown links resolve inside the repository
* no private paths, secret-looking strings or internal product names
* no em dash anywhere in files we write (see AUTHORED_GLOBS)
* .claude-plugin manifests are valid JSON and agree with each other
* hidden content: zero-width or bidi characters, long blank runs, HTML comments in prose
* the README skill table is in sync with skills.json (run scripts/build_index.py)

Exit code 0 means all checks passed. Requires Python 3.9+ and PyYAML.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^(```|~~~)")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")

EM_DASH = "\u2014"

# Files and folders written by us. Everything under skills/ is covered as well.
AUTHORED_GLOBS = [
    "README.md",
    "README.pl.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "AGENTS.md",
    "docs/*.md",
    ".github/**/*.md",
    ".github/**/*.yml",
    "scripts/*.py",
    "skills.json",
]

FORBIDDEN_PATTERNS = [
    (re.compile(r"/home/[a-z0-9_-]+/"), "absolute home path"),
    (re.compile(r"/Users/[A-Za-z0-9_-]+/"), "absolute macOS home path"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "API key shaped string"),
    (re.compile(r"\bghp_[A-Za-z0-9]{20,}"), "GitHub token shaped string"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS key shaped string"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
    (re.compile(r"\b(?:SyncCrew|synccrew|SyncHQ)\b"), "internal product name"),
]

# Files where a forbidden pattern is expected (this script and the docs that explain the rules).
FORBIDDEN_EXEMPT = {
    "scripts/validate_skills.py",
    "docs/PROVENANCE.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
}

TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".mjs", ".js", ".txt", ".html", ".toml", ".sh"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def skill_digest(skill_dir: Path) -> str:
    """sha256 over the sorted lines '<file sha256>  <path inside the skill>'. Used by the mirror stamp."""
    lines = []
    for path in sorted(p for p in skill_dir.rglob("*") if p.is_file()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(skill_dir).as_posix()}\n")
    return hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        err(f"{rel(path)}: missing frontmatter (file must start with '---')")
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        err(f"{rel(path)}: frontmatter is not closed with '---'")
        return None, text
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        err(f"{rel(path)}: frontmatter is not valid YAML: {exc}")
        return None, text
    if not isinstance(data, dict):
        err(f"{rel(path)}: frontmatter must be a YAML mapping")
        return None, text
    return data, text[end + 4 :]


def check_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        err(f"{rel(skill_dir)}: no SKILL.md")
        return
    data, body = parse_frontmatter(skill_file)
    if data is None:
        return

    unknown = set(data) - ALLOWED_FIELDS
    if unknown:
        err(f"{rel(skill_file)}: unsupported frontmatter fields {sorted(unknown)} (allowed: {sorted(ALLOWED_FIELDS)})")

    name = data.get("name")
    if not isinstance(name, str) or not name:
        err(f"{rel(skill_file)}: 'name' is required")
    else:
        if len(name) > 64 or not NAME_RE.match(name):
            err(f"{rel(skill_file)}: name '{name}' must be 1-64 chars of a-z, 0-9 and single hyphens")
        if name != skill_dir.name:
            err(f"{rel(skill_file)}: name '{name}' does not match folder '{skill_dir.name}'")

    desc = data.get("description")
    if not isinstance(desc, str) or not desc.strip():
        err(f"{rel(skill_file)}: 'description' is required and must be a non-empty string")
    else:
        if len(desc) > 1024:
            err(f"{rel(skill_file)}: description is {len(desc)} chars (max 1024)")
        if "\n" in desc.strip():
            warn(f"{rel(skill_file)}: description spans several lines")

    meta = data.get("metadata")
    if meta is not None:
        if not isinstance(meta, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in meta.items()):
            err(f"{rel(skill_file)}: 'metadata' must be a map of string keys to string values (quote version numbers)")
    for field in ("license", "compatibility"):
        if field in data and not isinstance(data[field], str):
            err(f"{rel(skill_file)}: '{field}' must be a string")
    if "compatibility" in data and isinstance(data["compatibility"], str) and len(data["compatibility"]) > 500:
        err(f"{rel(skill_file)}: compatibility is longer than 500 chars")
    if "allowed-tools" in data and not isinstance(data["allowed-tools"], str):
        err(f"{rel(skill_file)}: 'allowed-tools' must be a space-separated string")

    lines = skill_file.read_text(encoding="utf-8").count("\n") + 1
    if lines > 500:
        warn(f"{rel(skill_file)}: {lines} lines (the spec recommends under 500; move detail into references/)")

    skill_json = skill_dir / "skill.json"
    if skill_json.is_file():
        try:
            parsed = json.loads(skill_json.read_text(encoding="utf-8"))
            if parsed.get("name") != skill_dir.name:
                err(f"{rel(skill_json)}: name '{parsed.get('name')}' does not match folder '{skill_dir.name}'")
        except (json.JSONDecodeError, AttributeError) as exc:
            err(f"{rel(skill_json)}: invalid JSON or shape: {exc}")

    evals = skill_dir / "evals" / "evals.json"
    if evals.is_file():
        try:
            parsed = json.loads(evals.read_text(encoding="utf-8"))
            if parsed.get("skill_name") != skill_dir.name:
                err(f"{rel(evals)}: skill_name '{parsed.get('skill_name')}' does not match folder '{skill_dir.name}'")
            if not isinstance(parsed.get("evals"), list) or not parsed["evals"]:
                err(f"{rel(evals)}: 'evals' must be a non-empty list")
        except (json.JSONDecodeError, AttributeError) as exc:
            err(f"{rel(evals)}: invalid JSON or shape: {exc}")


def iter_links(md_path: Path):
    in_fence = False
    for lineno, line in enumerate(md_path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = re.sub(r"`[^`]*`", "", line)
        for match in LINK_RE.finditer(stripped):
            yield lineno, match.group(1)


# Placeholder targets that appear inside templates and examples, not real links.
PLACEHOLDER_TARGETS = {"link", "url", "path", "#"}


def check_links(md_path: Path) -> None:
    for lineno, target in iter_links(md_path):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):  # http:, https:, mailto:, ...
            continue
        if target.startswith("#") or target.startswith("/") or target.lower() in PLACEHOLDER_TARGETS:
            continue
        if any(ch in target for ch in "{}<>$"):
            continue
        path_part = re.split(r"[#?]", target, maxsplit=1)[0]
        if not path_part:
            continue
        resolved = (md_path.parent / path_part).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            err(f"{rel(md_path)}:{lineno}: link '{target}' points outside the repository")
            continue
        if not resolved.exists():
            err(f"{rel(md_path)}:{lineno}: broken relative link '{target}'")


def tracked_files() -> list[Path]:
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-co", "--exclude-standard"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        return [ROOT / p for p in out if (ROOT / p).is_file()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


HIDDEN_CHARS = re.compile("[\u200b-\u200f\u202a-\u202e\u2060-\u2064\ufeff\U000e0000-\U000e007f]")
BLANK_RUN = re.compile(r"\n[ \t]*\n(?:[ \t]*\n){20,}")
GENERATED_MARKER = re.compile(r"<!-- generated:\w+:(?:start|end) -->")
CURL_PIPE = re.compile(r"curl[^\n]*\|\s*(?:ba|z)?sh\b")


def strip_fences(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def check_hidden_content(path: Path, text: str) -> None:
    relpath = rel(path)
    if HIDDEN_CHARS.search(text):
        err(f"{relpath}: zero-width, bidi or tag characters (hidden content)")
    if BLANK_RUN.search(text):
        err(f"{relpath}: run of more than 20 blank lines (can hide text)")
    if path.suffix.lower() == ".md":
        prose = GENERATED_MARKER.sub("", strip_fences(text))
        if "<!--" in prose:
            err(f"{relpath}: HTML comment in prose (hidden from rendered view, read by agents)")
    if CURL_PIPE.search(text) and relpath != "scripts/validate_skills.py":
        warn(f"{relpath}: 'curl | sh' pattern, check that it is intended")


def check_content(files: list[Path]) -> None:
    authored = set()
    for pattern in AUTHORED_GLOBS:
        authored.update(p for p in ROOT.glob(pattern) if p.is_file())
    authored.update(p for p in SKILLS_DIR.rglob("*") if p.is_file())

    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        relpath = rel(path)
        check_hidden_content(path, text)
        if relpath not in FORBIDDEN_EXEMPT:
            for pattern, label in FORBIDDEN_PATTERNS:
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    err(f"{relpath}:{line}: {label} ('{match.group(0)}')")
        if path in authored and EM_DASH in text:
            line = text.count("\n", 0, text.index(EM_DASH)) + 1
            err(f"{relpath}:{line}: em dash in authored copy")


_index_cache: dict | None = None


def load_index() -> dict:
    global _index_cache
    if _index_cache is None:
        path = ROOT / "skills.json"
        if not path.is_file():
            err("skills.json is missing")
            _index_cache = {"skills": {}}
        else:
            try:
                _index_cache = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                err(f"skills.json: invalid JSON: {exc}")
                _index_cache = {"skills": {}}
    return _index_cache


def check_index(skill_names: set[str]) -> None:
    index = load_index()
    listed = set(index.get("skills", {}))
    for name in sorted(skill_names - listed):
        err(f"skills.json: skill '{name}' has a folder but no entry")
    for name in sorted(listed - skill_names):
        err(f"skills.json: entry '{name}' has no folder under skills/")
    categories = set(index.get("categories", []))
    for name, entry in index.get("skills", {}).items():
        for key in ("category", "summary", "authoring"):
            if not entry.get(key):
                err(f"skills.json: '{name}' is missing '{key}'")
        if entry.get("category") and entry["category"] not in categories:
            err(f"skills.json: '{name}' uses category '{entry['category']}' that is not in 'categories'")
        if entry.get("authoring") not in {"here", "mirror"}:
            err(f"skills.json: '{name}' has authoring '{entry.get('authoring')}' (use 'here' or 'mirror')")
        if len(entry.get("summary", "")) > 120:
            err(f"skills.json: '{name}' summary is longer than 120 chars")


def check_mirrors() -> None:
    """A mirrored skill is edited in its source repository, never here. The stamp proves the files are untouched."""
    for name, entry in load_index().get("skills", {}).items():
        skill_dir = SKILLS_DIR / name
        mirror = entry.get("mirror")
        if entry.get("authoring") != "mirror":
            if mirror is not None:
                err(f"skills.json: '{name}' has a mirror stamp but authoring is '{entry.get('authoring')}'")
            continue
        if not isinstance(mirror, dict):
            err(f"skills.json: mirrored skill '{name}' needs a 'mirror' stamp (run scripts/stamp_mirror.py)")
            continue
        for key in ("of", "source_commit", "contract_version", "catalog_version", "content_sha256"):
            if not mirror.get(key):
                err(f"skills.json: '{name}' mirror stamp is missing '{key}'")
        if mirror.get("source_commit") and not COMMIT_RE.match(mirror["source_commit"]):
            err(f"skills.json: '{name}' mirror source_commit must be a full 40-character sha")
        if mirror.get("content_sha256") and not DIGEST_RE.match(mirror["content_sha256"]):
            err(f"skills.json: '{name}' mirror content_sha256 must be 64 hex characters")
        if not skill_dir.is_dir():
            continue
        actual = skill_digest(skill_dir)
        if mirror.get("content_sha256") and mirror["content_sha256"] != actual:
            err(
                f"skills/{name}: files differ from the mirror stamp (stamp {mirror['content_sha256'][:12]}, "
                f"files {actual[:12]}). Mirrored skills change in their source repository; "
                "then run scripts/stamp_mirror.py. See docs/PROVENANCE.md."
            )
        skill_json = skill_dir / "skill.json"
        if skill_json.is_file():
            try:
                declared = json.loads(skill_json.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            for stamp_key, json_key in (("contract_version", "contractVersion"), ("catalog_version", "catalogVersion")):
                if str(declared.get(json_key)) != str(mirror.get(stamp_key)):
                    err(f"skills/{name}/skill.json: {json_key} {declared.get(json_key)!r} differs from the mirror stamp {mirror.get(stamp_key)!r}")


def check_manifests(skill_names: set[str]) -> None:
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    pj = ROOT / ".claude-plugin" / "plugin.json"
    for path in (mp, pj):
        if not path.is_file():
            err(f"{rel(path)} is missing")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"{rel(path)}: invalid JSON: {exc}")
    if mp.is_file() and pj.is_file():
        try:
            m = json.loads(mp.read_text(encoding="utf-8"))
            p = json.loads(pj.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return
        if not m.get("name") or not m.get("owner", {}).get("name") or not m.get("plugins"):
            err("marketplace.json needs name, owner.name and plugins[]")
        reserved = {"agent-skills", "anthropic-agent-skills", "claude-code-plugins", "claude-plugins-official"}
        if m.get("name") in reserved or str(m.get("name", "")).startswith("claudeai-"):
            err(f"marketplace.json: reserved name '{m.get('name')}'")
        pname = p.get("name", "")
        if pname.startswith(("claude-", "anthropic-", "anthropics-", "cc-plugin-")):
            err(f"plugin.json: name '{pname}' uses a reserved prefix")
        listed = {pl.get("name"): pl for pl in m.get("plugins", [])}
        if pname not in listed:
            err(f"plugin.json name '{pname}' is not listed in marketplace.json")
        elif listed[pname].get("description") != p.get("description"):
            err("plugin.json and marketplace.json describe the plugin differently")
        for skill in sorted(skill_names):
            if skill not in p.get("description", ""):
                err(f"plugin.json: description does not mention skill '{skill}'")
        if p.get("version") and m.get("metadata", {}).get("version") and p["version"] != m["metadata"]["version"]:
            err("plugin.json version and marketplace.json metadata.version differ")


def check_readme_in_sync() -> None:
    script = ROOT / "scripts" / "build_index.py"
    if not script.is_file():
        return
    result = subprocess.run([sys.executable, str(script), "--check"], capture_output=True, text=True)
    if result.returncode != 0:
        err("generated tables are out of date: run `python3 scripts/build_index.py`\n" + result.stdout + result.stderr)


def main() -> int:
    if not SKILLS_DIR.is_dir():
        err("skills/ directory is missing")
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.is_dir() else []
    for skill_dir in skill_dirs:
        check_skill(skill_dir)
    names = {p.name for p in skill_dirs}
    check_index(names)
    check_mirrors()
    check_manifests(names)

    files = tracked_files()
    for path in files:
        if path.suffix.lower() == ".md":
            check_links(path)
    check_content(files)
    check_readme_in_sync()

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"\n{len(skill_dirs)} skills checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
