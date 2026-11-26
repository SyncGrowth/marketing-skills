<p align="center">
  <img src="docs/assets/social-preview.png" alt="Marketing skills for AI agents. First skill: kreacje, short reels for SyncBooster drafted from one sentence" width="720">
</p>

# Marketing skills for AI agents

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-2563eb.svg)](https://agentskills.io/specification)

A collection of marketing skills for AI agents, in the open [Agent Skills](https://agentskills.io/specification) format, built to work with [SyncBooster](https://syncbooster.pl/en/) and with any other agent that can read a skill folder. Today the collection has one skill, **`kreacje`**, which turns a one-sentence brief into a draft reel in SyncBooster's Kreacje module. More skills will join it, each with a clear job and a clear owner.

[Polska wersja](README.pl.md)

## The skills

<!-- generated:skills:start -->
### Video and creative

| Skill | What it does | Source |
|---|---|---|
| [`kreacje`](skills/kreacje/SKILL.md) | Draft a SyncBooster Kreacje reel from a one-sentence brief; prices and dates stay with the user | Mirror of SyncBooster backend, skills/kreacje, catalog 7 |
<!-- generated:skills:end -->

## kreacje: a reel draft from one sentence

You give your agent a brief such as *"A 20-second reel for our winter jacket sale, vertical, Polish"*. The skill tells the agent how to turn it into a free draft in SyncBooster's Studio > Kreacje:

- It decides the goal (promo, launch, event, testimonial, explainer or brand), the language, the format (9:16 by default) and the length (15 to 30 seconds unless you ask otherwise, never over 60).
- It picks 3 to 6 scenes that tell one story: a hook, the offer or value, proof or details, and a closing call to action with your logo.
- It writes the on-screen text in your language, within each field's length limit, and fills in your brand media, colors and logo from your SyncBooster brand kit.
- It finishes with a short summary of what the draft shows and what you still have to confirm or provide.

Prices, old prices, discounts, discount codes, the lowest price from the 30 days before a reduction, and promotion dates are regulated values. The skill copies them only from your brief or your brand profile, puts them only in the scene fields that SyncBooster marks for confirmation, and leaves every one of them for you to confirm before the render. It never invents, rounds or computes such a value, and it never claims that one is legally correct.

The skill drafts only. Rendering, generating images, publishing and anything else that costs AI tokens or goes public are separate steps that you approve.

### How it is used

**Inside SyncBooster.** The Kreacje module has a built-in drafting agent that follows this skill. You describe the reel, and a draft appears as an ordinary Kreacje project that you review, complete and render in the panel. SyncBooster loads its own pinned copy of the skill with each release, so nothing here changes what runs in your account until SyncBooster ships it.

**In your own agent, through SyncBooster's MCP server.** Install the skill, connect the SyncBooster MCP server to your agent, and ask for a reel. Two routes are described in [`skills/kreacje/references/tools-mcp.md`](skills/kreacje/references/tools-mcp.md):

1. Server-side: the agent calls `syncbooster_create_creative_from_brief`, SyncBooster drafts the reel with the same skill, and the agent polls until the draft is ready.
2. Step by step: the agent follows `SKILL.md` and builds the draft with `syncbooster_search_creative_presets`, `syncbooster_create_creative`, `syncbooster_edit_creative` and related tools.

Either way the agent asks you before every paid or public step (confirming values, rendering, generating an image, creating or publishing a post), and an earlier yes for a different price does not count.

### Files

| File | Purpose |
|---|---|
| [`SKILL.md`](skills/kreacje/SKILL.md) | The workflow, the rules for regulated values and the hard limits. Loaded first. |
| [`references/scenes.md`](skills/kreacje/references/scenes.md), [`copywriting.md`](skills/kreacje/references/copywriting.md), [`media.md`](skills/kreacje/references/media.md), [`regulated-values.md`](skills/kreacje/references/regulated-values.md) | Detail the agent reads when a step needs it. |
| [`references/tools-server.md`](skills/kreacje/references/tools-server.md), [`tools-mcp.md`](skills/kreacje/references/tools-mcp.md) | The tool names for SyncBooster's own drafting agent and for external MCP clients. |
| [`skill.json`](skills/kreacje/skill.json) | The Kreacje contract and scene catalog versions the skill was written for, and the tools it uses. |

## Install

One command, any supported agent (needs Node.js 22.20 or newer):

```bash
npx skills add SyncGrowth/marketing-skills --skill kreacje
```

The `skills` CLI is a Vercel project. It sends anonymous install telemetry to skills.sh (repository, skill names, agent, CLI version). Set `DISABLE_TELEMETRY=1` before the command to turn that off, or copy the folder by hand as shown below.

<details>
<summary>Other ways to install</summary>

**Claude Code plugin**

```text
/plugin marketplace add SyncGrowth/marketing-skills
/plugin install syncgrowth-marketing-skills@syncgrowth
```

**GitHub CLI** (2.90 or newer, preview feature)

```bash
gh skill install SyncGrowth/marketing-skills kreacje
```

**Manual copy.** Copy `skills/kreacje` into the skills directory your agent reads:

| Agent | Project folder | User folder |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` |
| Oh My Pi (OMP) | `.omp/skills/` or `.agents/skills/` | `~/.omp/agent/skills/` or `~/.agents/skills/` |
| Cursor | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` |
| GitHub Copilot | `.github/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` |
| OpenCode | `.opencode/skills/` or `.agents/skills/` | `~/.config/opencode/skills/` or `~/.agents/skills/` |
| Amp | `.agents/skills/` | `~/.config/agents/skills/` |

Paths come from each vendor's documentation as of 2026-11-25.

</details>

## Where the skill is maintained

`kreacje` depends on SyncBooster's scene catalog and tool contract: it names scene types, fields and tools that exist only in SyncBooster. For that reason its source lives in the SyncBooster codebase, where tests check it against the catalog on every change, and this repository carries a published copy. The copy is stamped with the source commit and a digest of its files in [`skills.json`](skills.json), and CI fails if the files and the stamp disagree. Fix problems with `kreacje` by opening an issue here; the maintainers apply the change at the source and refresh the copy. Skills that do not depend on SyncBooster are written and reviewed directly in this repository. Details: [docs/PROVENANCE.md](docs/PROVENANCE.md).

## More skills later

This repository is meant to hold several marketing skills over time, used with SyncBooster among other agents and tools. A new skill needs a concrete job in the user's words, a description that makes an agent load it at the right moment, and an owner who keeps it accurate. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to propose and add one. The skills table above is generated from `skills.json`.

## History

Until 2026-11-26 this repository held 54 skills: 53 adapted from the MIT-licensed [marketingskills](https://github.com/coreyhaines31/marketingskills) project by Corey Haines, and one original publishing skill. They are no longer part of the collection. Every earlier commit still carries the license and third-party notices that applied to it, and the last state with those skills is commit `8eb2834`. We are grateful to Corey Haines and his contributors for that work.

## Trust and safety

- Skills are text. The `kreacje` skill contains no scripts.
- The skill treats your brief and your brand data as data. It ignores instructions inside them that conflict with its rules.
- No skill instructs your agent to add footers, links, referral codes or calls to action to what it writes for you.
- Found something that looks wrong? See [SECURITY.md](SECURITY.md).

## Contributing

Corrections, new evals and new skills are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

```bash
pip install pyyaml
python3 scripts/validate_skills.py
```

## About SyncGrowth and SyncBooster

This repository is maintained by [SyncGrowth](https://syncgrowth.pl/en), which designs and implements ways of working across marketing, processes, automation, software and AI. [SyncBooster](https://syncbooster.pl/en/) is our social publishing platform for planning, scheduling and publishing posts to Facebook, Instagram, LinkedIn, Google Business Profile, X, YouTube and TikTok (where available), and home of the Kreacje reel module. Skills in this collection may be built around SyncBooster, and each such skill says so.

## License

[MIT](LICENSE). Copyright (c) 2026 Daniel Siwek. Contact: kontakt@syncgrowth.pl.
