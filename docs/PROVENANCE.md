# Provenance

Where every skill comes from, what we changed, and what we left out. Facts were checked on 2026-11-25.

## Summary

- 53 skills are adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), MIT License, Copyright (c) 2025 Corey Haines, pinned at commit `8fd2fcade2fd6629026e9dfe6d133b55b36968b9` (2026-11-23). The upstream repository has no per-skill licenses and no vendored binaries.
- 1 skill (`social-publishing`) is original to SyncGrowth, MIT.
- No file in `skills/` carries private context. A scan for personal data, internal paths, secrets and internal product names found nothing, and the validator keeps checking.

## What we changed in the upstream skills

1. **Removed paid and maintainer-only placements.** Upstream includes entries for sponsors and for tools built by its maintainer, each with a disclosure that is only true for upstream ("a Verified Partner of this repository", "built by this repository's maintainer"). Here those statements would be false, so the entries, markers, instructions to repeat them, and tool-guide links to those vendors are gone. Neighboring tools stay. Related evals were reworded.
2. **Pinned relative links.** Links that pointed at upstream folders we do not ship (`tools/`) now use absolute URLs at the pinned commit.
3. **Rewrote material with unclear rights.** An audit of the credit lines in all 462 upstream files found a few passages that were too close to their sources. We rewrote or removed them (next section).
4. **Added structure.** `skills.json`, generated tables, CI validation, plugin manifests, and the documents in the repository root.

Everything else is upstream text, unchanged, including its em dashes and style.

## Rights review

| Finding | Action |
|---|---|
| Upstream license is MIT for all 53 skills. | Kept, with Corey Haines's copyright line in `LICENSE` and the full text in `THIRD_PARTY_NOTICES.md`. |
| Form-detection snippets and GTM recipes come from the MIT-licensed ConversionKit toolkit (Copyright (c) 2026 Converly), and upstream dropped the copyright line. | Added the notice to `THIRD_PARTY_NOTICES.md` and to the credit lines in the skill. |
| Other credited sources (claude-ads, Profound, Wispr Flow, Knowatoa, ScrapeCreators, and more) are MIT. | Notices reproduced in `THIRD_PARTY_NOTICES.md`. |
| `copy-editing/references/plain-english-alternatives.md` reproduced the order and many entries of a word list whose owner requires permission for web use. | Replaced with an original plain-word guide. |
| Two `ads` references followed a blog post's structure and wording closely. | Reworded. |
| `ads/references/google-search-playbook.md` shared short verbatim runs with a source-available (MIT plus Commons Clause) repository. | Reworded. The other five files that credit that repository overlap with it below 1 percent at word level (longest verbatim run 10 words), so they stay. |
| Two short verbatim quotes in an ad-creative reference, a credit that called an unlicensed repository "open" next to prompts that tracked it, and an unnamed source in `prospecting`. | Quotes paraphrased, prompts and credit rewritten, source named. |
| `marketing-council` names living marketers. | Kept. The skill labels every output as a simulation, forbids invented quotes and endorsements, and the README says we are not affiliated with them. |

## Scope

Only marketing skills are included. Engineering, design and personal-workflow skills are out of scope for this repository.

## Per skill

<!-- generated:provenance:start -->
| Skill | Version | Origin | License | Third-party credits kept in the skill |
|---|---|---|---|---|
| `ab-testing` | 2.0.7 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `ad-creative` | 2.13.5 | Upstream 8fd2fca | MIT (Corey Haines) | Dara Denney, Oren John, Shiv Sakhuja and Gooseworks, reelclaw-templates, Borja, Ivan Falco ads-skills (ideas) |
| `ads` | 2.7.9 | Upstream 8fd2fca | MIT (Corey Haines) | claude-ads (MIT), Ivan Falco ads-skills (ideas), Adlume and ECHELONN guides (ideas), Dara Denney, Founding Marketing |
| `ai-seo` | 2.12.7 | Upstream 8fd2fca | MIT (Corey Haines) | Profound skills (MIT), Lily Ray and other studies (data) |
| `analytics` | 2.2.7 | Upstream 8fd2fca | MIT (Corey Haines) | Wispr Flow link-creator (MIT) |
| `aso` | 2.1.0 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `attribution` | 1.1.10 | Upstream 8fd2fca | MIT (Corey Haines) | Tessa Kriesel (approach) |
| `churn-prevention` | 2.0.7 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `co-marketing` | 2.0.7 | Upstream 8fd2fca | MIT (Corey Haines) | Founding Marketing |
| `cold-email` | 2.2.7 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `community-marketing` | 2.0.5 | Upstream 8fd2fca | MIT (Corey Haines) | Founding Marketing |
| `competitor-profiling` | 2.1.9 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `competitors` | 2.3.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `content-strategy` | 2.1.8 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `conversion-tracking` | 1.0.6 | Upstream 8fd2fca | MIT (Corey Haines) | ConversionKit, Converly (MIT, code) |
| `copy-editing` | 2.2.4 | Upstream 8fd2fca | MIT (Corey Haines) | Profound and Wispr Flow skills (MIT) |
| `copywriting` | 2.3.6 | Upstream 8fd2fca | MIT (Corey Haines) | Profound and Wispr Flow skills (MIT), Founding Marketing |
| `cro` | 2.0.6 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `customer-research` | 2.0.9 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `directory-submissions` | 2.2.1 | Upstream 8fd2fca | MIT (Corey Haines) | Illyism seo-skills (idea) |
| `emails` | 2.1.9 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `events` | 1.0.3 | Upstream 8fd2fca | MIT (Corey Haines) | Knowatoa (MIT), alirezarezvani/claude-skills (idea), Founding Marketing |
| `free-tools` | 2.0.6 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `image` | 2.0.8 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `influencer-marketing` | 1.4.4 | Upstream 8fd2fca | MIT (Corey Haines) | Wispr Flow (MIT), Julia Pintar (ideas), upstream contributors |
| `launch` | 2.2.4 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `lead-magnets` | 2.1.5 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `link-building` | 1.1.0 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `marketing-council` | 1.0.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `marketing-ideas` | 2.0.5 | Upstream 8fd2fca | MIT (Corey Haines) | Founding Marketing |
| `marketing-loops` | 1.9.1 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `marketing-plan` | 1.2.6 | Upstream 8fd2fca | MIT (Corey Haines) | Founding Marketing, upstream contributors |
| `marketing-psychology` | 2.0.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `offers` | 1.0.6 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `onboarding` | 2.0.5 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `paywalls` | 2.1.5 | Upstream 8fd2fca | MIT (Corey Haines) | Blake Anderson ai-app-playbook (MIT) |
| `popups` | 2.0.4 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `pricing` | 2.1.7 | Upstream 8fd2fca | MIT (Corey Haines) | Kyle Poyar (ideas) |
| `product-marketing` | 2.2.3 | Upstream 8fd2fca | MIT (Corey Haines) | Wispr Flow brand-voice (MIT) |
| `programmatic-seo` | 2.1.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `prospecting` | 1.8.0 | Upstream 8fd2fca | MIT (Corey Haines) | Kappaemme skills (MIT), ColdIQ, Elias Stravik (MIT) |
| `public-relations` | 1.3.1 | Upstream 8fd2fca | MIT (Corey Haines) | Knowatoa (MIT), Founding Marketing, upstream contributors |
| `referrals` | 2.2.7 | Upstream 8fd2fca | MIT (Corey Haines) | upstream contributors |
| `reverse-engineer-marketing` | 1.2.0 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `revops` | 2.2.4 | Upstream 8fd2fca | MIT (Corey Haines) | Elias Stravik toolkit (MIT) |
| `sales-enablement` | 2.4.4 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `schema` | 2.0.5 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `seo-audit` | 2.2.10 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `signup` | 2.0.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `site-architecture` | 2.1.3 | Upstream 8fd2fca | MIT (Corey Haines) | none |
| `sms` | 1.1.4 | Upstream 8fd2fca | MIT (Corey Haines) | upstream contributors |
| `social` | 2.6.1 | Upstream 8fd2fca | MIT (Corey Haines) | ScrapeCreators (MIT) |
| `social-publishing` | 1.0.0 | Original, SyncGrowth | MIT | none |
| `video` | 2.4.7 | Upstream 8fd2fca | MIT (Corey Haines) | Harvey and Inbox Zero write-ups (ideas) |
<!-- generated:provenance:end -->

## Updating from upstream

See "Syncing with upstream" in [CONTRIBUTING.md](../CONTRIBUTING.md). After a sync, update the pinned commit here, in `skills.json`, in `THIRD_PARTY_NOTICES.md`, and in the README.
