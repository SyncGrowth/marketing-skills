# Provenance

Where each skill is maintained, and what happened to the earlier content of this repository.

## Where each skill is maintained

| Skill | Edited in | This repository holds |
|---|---|---|
| `kreacje` | The SyncBooster backend, directory `skills/kreacje/` | A copy, stamped in `skills.json` with the source commit, the Kreacje contract and catalog versions, and a digest of the files |

`kreacje` names scene types, fields and tools that exist only in SyncBooster. The SyncBooster backend checks the skill against its scene catalog and tool list in tests and again when the server starts, and it pins the version of the skill that each release uses. Keeping the source next to those checks means a catalog change and the matching skill change land in one reviewed change. This repository is the public home of the skill: where other agents install it from and where people read and discuss it.

SyncBooster does not read this repository at runtime. Changing a file here changes nothing in a running SyncBooster account.

## How the copy stays honest

- `skills.json` holds a `mirror` stamp per mirrored skill: `source_commit`, `contract_version`, `catalog_version` and `content_sha256`, a digest over the sorted file hashes of the skill folder.
- `python3 scripts/validate_skills.py`, run by CI on every push and pull request, recomputes the digest and fails when it differs from the stamp, or when `skill.json` declares other versions than the stamp.
- A refresh is: copy the folder from the source, run `python3 scripts/stamp_mirror.py kreacje --source-commit <sha>`, validate, commit. See [CONTRIBUTING.md](../CONTRIBUTING.md).
- The source repository is private, so the stamp is a record for maintainers, and the digest is what anyone can check here.

A skill written in this repository has `"authoring": "here"` and needs no stamp.

## Earlier content

Until 2026-11-26 the repository held 54 skills (last state: commit `8eb2834`):

- 53 skills adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) at commit `8fd2fcade2fd6629026e9dfe6d133b55b36968b9` (2026-11-23), MIT License, Copyright (c) 2025 Corey Haines, with credit lines for further MIT-licensed sources inside the skills.
- 1 original skill, `social-publishing`, MIT.

All of them were removed in the change that made `kreacje` the first and only skill. No file of that content remains in the tree, so the MIT notices that traveled with it are no longer part of the current files, and `LICENSE` names only the present copyright holder. Every earlier commit keeps the `LICENSE`, `THIRD_PARTY_NOTICES.md` and `docs/PROVENANCE.md` that applied to it, which is where the notices stay readable. The files of the removed skills can be restored from the commit above if a future skill needs them. In that case the notices come back with them, as [CONTRIBUTING.md](../CONTRIBUTING.md) describes.

The remaining repository files (scripts, community files, issue forms) were written for this repository. A comparison of every line longer than 40 characters against the upstream `CONTRIBUTING.md`, `AGENTS.md` and `README.md` found no shared lines.
