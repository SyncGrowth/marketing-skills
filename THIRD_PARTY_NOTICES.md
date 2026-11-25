# Third-party notices

This repository redistributes and adapts the work of others. This file reproduces the notices those works require and credits the sources that the skills draw on. Provenance of each skill is in [docs/PROVENANCE.md](docs/PROVENANCE.md). License statements were read from each source on 2026-11-25.

## 1. Upstream project

Most skills in `skills/` are adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) at commit `8fd2fcade2fd6629026e9dfe6d133b55b36968b9` (2026-11-23), including its references, scripts, assets and evals. That project is licensed under the MIT License:

```text
MIT License

Copyright (c) 2025 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Upstream credits contributors in some files. Their contributions are distributed by upstream under the same license.

## 2. MIT-licensed works that upstream copied or adapted

These notices apply to the material named, which appears in the skills with the credit lines that upstream wrote. Each is licensed under the MIT permission text reproduced once at the end of this section.

| Copyright notice | Source | Where it appears |
|---|---|---|
| Copyright (c) 2026 Converly (converly.io) | [ConversionKit/conversion-tracking](https://github.com/ConversionKit/conversion-tracking) | Form-detection snippets and GTM recipes in `skills/conversion-tracking/assets/` (adapted) |
| Copyright (c) 2026 Daniel Agrici (AgriciDaniel) | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | Scoring semantics and benchmark-evidence ladder in `skills/ads/references/audit-guardrails.md` (distilled) |
| Copyright (c) 2026 Profound | [retieedra-profound/skills-marketing-library](https://github.com/retieedra-profound/skills-marketing-library) (Profound skills, and the Wispr Flow skills it hosts under `wisprflow/`) | AI visibility references in `skills/ai-seo/references/`, and parts of `copywriting`, `copy-editing`, `analytics`, `influencer-marketing` and `product-marketing` (re-expressed) |
| Copyright (c) 2026 Wafris LLC (d/b/a Knowatoa) | [Knowatoa/ai-visibility-skills](https://github.com/Knowatoa/ai-visibility-skills) | `skills/public-relations/references/podcast-guest-prep.md`, `skills/events/references/speaking.md` (distilled) |
| Copyright (c) 2026 Francesco Mistero | [Kappaemme-git/codex-first-customer-finder-skill](https://github.com/Kappaemme-git/codex-first-customer-finder-skill), [Kappaemme-git/local-client-prospector-skill](https://github.com/Kappaemme-git/local-client-prospector-skill) (the latter is a likely source, upstream names no author) | `skills/prospecting/references/demand-signals.md`, `local-prospecting.md` (re-expressed) |
| Copyright (c) 2026 ScrapeCreators | [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | Outlier-post method in `skills/social/references/listening.md` (adapted) |
| Copyright (c) 2026 Blake Anderson | [blakeandersonw/ai-app-playbook](https://github.com/blakeandersonw/ai-app-playbook) | `skills/paywalls/references/mobile-subscription-paywalls.md` (adapted) |
| Copyright (c) 2026 Elias Stravik | [eliasstravik/gtm-skills](https://github.com/eliasstravik/gtm-skills) (upstream says "toolkit patterns"; the exact repository is not named, so this is a best match) | Patterns in `skills/revops/references/inbound-routing.md`, `skills/prospecting/references/enrichment-playbook.md` |
| Copyright (c) 2025 Alireza Rezvani | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Idea credit only for `skills/events/references/webinar-funnel.md`; the text was written independently |

MIT permission text for every row of this table:

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 3. Other sources credited inside the skills

The skills also credit the following. Upstream describes each as ideas, frameworks, data or formats that were re-expressed in its own words, and no license applies to ideas. If you hold rights in any of this material and believe a file reproduces more than it should, please tell us through the [license or attribution issue form](.github/ISSUE_TEMPLATE/license-or-attribution.yml) and we will fix or remove it.

- Corey Haines, *Founding Marketing* (the upstream author's own book, used in several `marketing-plan`, `marketing-ideas`, `events`, `public-relations`, `community-marketing`, `co-marketing`, `copywriting` and `ads` references).
- Ivan Falco, [ads-skills](https://github.com/ivangfalco/ads-skills) (MIT with the Commons Clause condition, Copyright (c) 2026 Ivan Falco). The playbooks in `skills/ads/references/` and `skills/ad-creative/references/awareness-headlines.md` were written after reading it. Upstream states that all content was rewritten. We measured word-level overlap with the source on 2026-11-25, rewrote the one file with short verbatim runs, and found no substantial verbatim text in any of the six. Nothing from that project is sold here, and this repository is free. The Commons Clause text is in the source repository's LICENSE.
- Dara Denney (Meta creative-type tier list and Claude Cowork practice), Oren John (vlog and "yapping" playbooks), Shiv Sakhuja and the Gooseworks team (iMessage video ad format), Daniel Hangan (`reelclaw-templates` vertical-video specification), Borja (motion video method), Marek Dabrowski and Adlume (paid ads operator guide), ECHELONN and Jackson Blackledge (Google Ads audit checklist), Lily Ray and Amsive, Scrunch, SimilarWeb, Peec AI (AI citation research), Julia Pintar (UGC program), Kyle Poyar (pricing teardowns), Tessa Kriesel (PostHog attribution approach), Cody Schneider, Julien Lieben (ColdIQ), and others named in individual files.

Skills that name real marketers (`marketing-council`) refer to their published work and produce labeled simulations. They do not speak for the people named.
