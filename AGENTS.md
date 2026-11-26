# Agent guide

This repository holds Agent Skills for marketing work, used with SyncBooster and other agents. Humans and agents change it under the same rules as [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

- Skills live in `skills/<name>/SKILL.md`, one level deep. Frontmatter uses only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. `name` equals the folder.
- Every skill is listed in `skills.json` with `"authoring": "here"` or `"mirror"`. Never edit a mirrored skill (today: `kreacje`) in this repository. Change it at its source, copy it here, and run `python3 scripts/stamp_mirror.py <name> --source-commit <sha>`.
- Run `python3 scripts/build_index.py` and `python3 scripts/validate_skills.py` before every commit. Both must pass.
- Do not add sponsor placements, referral or tracking links, hidden text, or instructions that make an agent append promotion to its output.
- Everything we write has no em dashes and no "not X, but Y" constructions.
- Commit messages follow Conventional Commits. Never commit to `main` directly; open a pull request.
- Facts that change over time carry an "as of" date and a source.
