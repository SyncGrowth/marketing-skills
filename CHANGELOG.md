# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/): a new skill is a minor version, a changed skill a patch, a renamed or removed skill a major version.

## [Unreleased]

## [1.0.0] - not yet released

### Added

- 53 marketing skills adapted from the MIT-licensed [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) at commit `8fd2fca` (2026-11-23), with their references, scripts, assets and evals.
- `social-publishing`: an original release gate for putting approved social posts live, with an optional reference for the SyncBooster MCP server.
- `skills.json` index, generated skill tables in the READMEs, and `docs/PROVENANCE.md`.
- `scripts/validate_skills.py`, run by CI on every push and pull request.
- Claude Code plugin and marketplace manifests.
- English and Polish READMEs, LICENSE, THIRD_PARTY_NOTICES, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, issue forms, pull request template and social preview image.

### Changed

- Removed upstream sponsor placements, upstream maintainer-only product mentions, their disclosure markers, and instructions to repeat them. Related evals were reworded.
- Relative links that pointed at upstream-only folders now use absolute links pinned to the upstream commit.
