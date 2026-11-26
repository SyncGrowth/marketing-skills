# Contributing

Thank you for helping. This repository is a collection of marketing skills for AI agents, used with SyncBooster and with other agents. Today it holds one skill, `kreacje`. Corrections, new evals, new skills and better descriptions are all welcome.

## Ground rules

1. **Accuracy first.** Facts that change (prices, limits, platform rules) carry an "as of YYYY-MM" date and a source link. If you cannot source it, leave it out.
2. **Vendor-neutral advice, except where a skill exists for one product.** A skill built around a product, such as `kreacje` for SyncBooster, says so in its description. Every other skill names alternatives next to any tool it mentions. Test: swap the named tool for its nearest competitor. If the text would read as unfair, rewrite it.
3. **No promotion inside skills.** No referral or affiliate links, no tracking parameters, no instructions to add footers, links or calls to action to what the agent writes for the user. If you build a tool you mention, say so in the same sentence. A pull request that breaks this is declined.
4. **Credit what you adapt.** Add a short visible credit line to the file. Do not hide credits in HTML comments. Text you did not write must come from a source whose license allows it, and the credit must name the source and its license. If you adapt MIT-licensed work, add its copyright notice and permission text to a `THIRD_PARTY_NOTICES.md` in the same pull request. Do not paste text from books, courses or paywalled material, even with credit. Ideas and frameworks can be re-expressed in your own words.
5. **No private data.** No client names, personal data, internal paths, tokens, or screenshots with account details.

## Two kinds of skill

Every skill in `skills.json` has an `authoring` value that says where it is edited.

| `authoring` | Where you change it | Example |
|---|---|---|
| `here` | In this repository, by pull request. | A new skill for planning a product launch. |
| `mirror` | In its source repository. This repository keeps a stamped copy. | `kreacje`, edited in the SyncBooster codebase. |

Use `mirror` when the skill names things that only exist in one product and a test in that product can check them. `kreacje` is the example: it names scene types, fields and tools of SyncBooster, and SyncBooster's tests fail when the skill and its scene catalog disagree. Editing the copy here would create two diverging versions, so CI rejects it. A mirrored skill has no pull request edits in this repository except the refresh described below. Reports about it are welcome as issues.

Use `here` for everything else. Keep one place of truth per skill: never add the same skill under `here` and `mirror`.

## Adding a skill written here

A skill is `skills/<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/` and `evals/`.

```text
skills/your-skill/
  SKILL.md          required
  references/       detail loaded on demand, one level deep
  scripts/          code the agent may run, keep it small and readable
  assets/           templates and data
  evals/evals.json  test prompts and assertions
```

Frontmatter uses only the fields of the [Agent Skills specification](https://agentskills.io/specification): `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.

```yaml
---
name: your-skill
description: "When the user wants X, or asks Y or Z: the concrete jobs it covers. For adjacent job A, see skill-a."
metadata:
  version: 1.0.0
---
```

- **name**: lowercase letters, digits and single hyphens, at most 64 characters, equal to the folder name. Names are permanent, because renaming splits installs and breaks links.
- **description**: at most 1024 characters, aim for 500 or fewer. Start with the situation in the user's words, list the jobs, and point to neighboring skills. Agents decide from this text alone whether to load the skill.
- **body**: under 500 lines. Put detail in `references/` and say when to load each file ("Read `references/x.md` when the user asks about Y").
- **metadata values are strings**, so quote anything that is not obviously text.
- **evals**: three to five realistic prompts, each with an `expected_output` and a list of `assertions`. Include at least one near-miss prompt that should *not* trigger the skill.
- Add the skill to `skills.json` with `"authoring": "here"`, one of the listed categories (add a category when none fits), and a summary of at most 120 characters. Then run `python3 scripts/build_index.py` to refresh the tables in the READMEs.
- Add the skill name to the description in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; the validator checks it.

Skills written here follow the house style: plain sentences, no em dashes, no "not X, but Y" constructions, concrete verbs.

## Adding or refreshing a mirrored skill

1. Make the change in the source repository and merge it there. For `kreacje` that is `skills/kreacje/` in the SyncBooster backend, which also needs its own scene catalog checks to pass.
2. Copy the skill folder here unchanged. Delete files that no longer exist at the source.
3. Run `python3 scripts/stamp_mirror.py <name> --source-commit <40-character sha of the source repository>`. It records the commit, the contract and catalog versions from the skill's `skill.json` and a digest of the folder in `skills.json`.
4. Run the checks below, and note the refresh in [CHANGELOG.md](CHANGELOG.md) with the source commit.

For a new mirrored skill, add the `skills.json` entry first with `"authoring": "mirror"` and a `mirror` object holding the `of` text, then run the stamp script.

## Check your work

```bash
pip install pyyaml
python3 scripts/build_index.py      # regenerates the tables in the READMEs
python3 scripts/validate_skills.py  # the same check CI runs
```

The validator checks the frontmatter against the specification, `skills.json`, mirror stamps, relative links, eval files, plugin manifests, secret-shaped strings, private paths, hidden content, and em dashes.

## Pull requests

- One topic per pull request. Describe the user problem and the change in behavior.
- Use [Conventional Commits](https://www.conventionalcommits.org/): `fix(scenes): correct a field name`, `feat(launch): add a readiness checklist`, `docs: clarify install paths`.
- Bump `metadata.version` of a skill written here when you change it (patch for fixes, minor for new guidance) and add a line to [CHANGELOG.md](CHANGELOG.md).
- By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).

## Conduct and security

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Report security issues as described in [SECURITY.md](SECURITY.md), not in public issues.

For anything else, write to kontakt@syncgrowth.pl.
