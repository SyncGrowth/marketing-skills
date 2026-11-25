# Contributing

Thank you for helping. This repository is a curated set of marketing skills for AI agents. Corrections to advice, new evals, new skills, and better descriptions are all welcome.

## Ground rules

1. **Accuracy first.** Facts that change (prices, limits, platform rules) carry an "as of YYYY-MM" date and a source link. If you cannot source it, leave it out.
2. **Vendor-neutral advice.** When a skill names a tool, name its closest alternatives next to it. Test: swap the named tool for its nearest competitor. If the text would read as unfair, rewrite it.
3. **No promotion inside skills.** No referral or affiliate links, no tracking parameters, no instructions to add footers, links or calls to action to what the agent writes for the user, and no sponsor placements. If you build a tool you mention, say so in the same sentence. A pull request that breaks this is declined.
4. **Credit what you adapt.** Add a short visible credit line to the file. Do not hide credits in HTML comments. Text you did not write must come from a source whose license allows it, and you must add it to [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Do not paste text from books, courses, or paywalled material, even with credit. Ideas and frameworks can be re-expressed in your own words.
5. **No private data.** No client names, personal data, internal paths, tokens, or screenshots with account details.

## Adding or changing a skill

A skill is `skills/<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/`, and `evals/`.

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
- Add the skill to `skills.json` with a category, a summary of at most 120 characters, and `"origin"`.

Original skills written here follow the house style: plain sentences, no em dashes, no "not X, but Y" constructions, concrete verbs.

## Check your work

```bash
pip install pyyaml
python3 scripts/build_index.py      # regenerates the tables in the READMEs
python3 scripts/validate_skills.py  # the same check CI runs
```

The validator checks the frontmatter against the specification, `skills.json`, relative links, eval files, plugin manifests, secret-shaped strings, private paths, sponsor markers, hidden content, and em dashes in files we author.

## Pull requests

- One topic per pull request. Describe the user problem and the change in behavior.
- Use [Conventional Commits](https://www.conventionalcommits.org/): `fix(cro): correct form field guidance`, `feat(social-publishing): add story preview step`, `docs: clarify install paths`.
- Bump `metadata.version` of a skill you change (patch for fixes, minor for new guidance) and add a line to [CHANGELOG.md](CHANGELOG.md).
- By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).

## Syncing with upstream

Most skills come from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills). To update a skill, diff it against the commit recorded in `skills.json`, apply the upstream change, re-run the neutralization rules above (no sponsor placements, no maintainer-only claims, no unresolved relative links), update the pinned commit, and note it in the changelog. Improvements that are not specific to this repository are best sent upstream first.

## Conduct and security

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Report security issues as described in [SECURITY.md](SECURITY.md), not in public issues.
