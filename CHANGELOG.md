# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/): a new skill is a minor version, a changed skill a patch, a renamed or removed skill a major version.

## [Unreleased]

## [2.0.0] - not yet released

The repository now holds one skill, `kreacje`. Removing skills is a major version.

### Removed

- The 53 skills adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT, Copyright (c) 2025 Corey Haines) and the original `social-publishing` skill. Their last state is commit `8eb2834`.
- `THIRD_PARTY_NOTICES.md`, the upstream pin in `skills.json`, the credits table, and the generated provenance table. No third-party material remains in the current files.
- The Corey Haines copyright line from `LICENSE`, for the same reason. Earlier commits keep the notices that applied to them.

### Added

- `kreacje`: drafts a SyncBooster Kreacje reel from a one-sentence brief. Mirror of the SyncBooster backend `skills/kreacje/` at source commit `549d9e33`, contract 2, catalog 7.
- `authoring` and mirror stamp in `skills.json`, `scripts/stamp_mirror.py` and a validator check that fails when a mirrored skill differs from its stamp.
- `docs/PROVENANCE.md`: where each skill is maintained and what happened to the earlier content.

### Changed

- README and README.pl, CONTRIBUTING, AGENTS and the community files are rewritten around the one skill, with room for more.
- `scripts/validate_skills.py` and `scripts/build_index.py` no longer know about upstream origins or per-skill versions. The plugin manifests list the skill by name instead of a skill count.
- Social preview image shows the new scope.

## [1.0.0] - never released

Prepared in the repository history before the refocus. It was never tagged or published as a release.

- 53 marketing skills adapted from upstream and `social-publishing`, with the index, validator, plugin manifests, community files and social preview.
