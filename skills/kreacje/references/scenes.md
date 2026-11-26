# Choosing scenes

The scene catalog changes between releases; never rely on remembered scene type ids or preset ids, except the price and sale scenes SKILL.md names for regulated values (this skill version is pinned to their catalog). Find scenes at run time: `searchPresets` ranks presets for a goal and query (with `reasons[]` and `needs[]`), `listSceneTypes` gives every scene type's fields, limits, duration range and `whenToUseForAi`.

## One story

One message, 3-6 scenes, in this order:

1. **Hook** (first 2-4 s): the one reason to keep watching: the offer, the news, the problem.
2. **Offer or value**: what it is and why it matters (product photo, the offer, the main benefit).
3. **Proof or details** (optional, 1-2 scenes): benefits, how it works, a real quote or result, event details, photos.
4. **CTA / endcard**: what to do now (buy, book, come, sign up) and where, with the brand logo.

## Goal → story

| Goal | Brief signals | Story |
|---|---|---|
| `promo` | sale, discount, Black Friday, "-30%", promo code, offer | hook with the offer → the reduction in `seasonal.bf-price-drop` (one scene per product) or `seasonal.bf-big-percent` (percentage only), prices only when stated → why or details → CTA with where, sale dates and code in their fields, logo |
| `launch` | new, premiere, "nowość", now available | teaser hook → reveal with a photo → 2-3 benefits → CTA (where, from when) |
| `event` | date, place, workshop, webinar, opening, "wydarzenie" | hook → announcement (title, date, time, place from the brief only) → what happens, who it is for → CTA (register, come) |
| `testimonial` | opinions, reviews, customer story, case | hook → a real quote from the brief or the profile's reviews → a real result or before/after → CTA |
| `explainer` | how, steps, why, "jak" | hook with the question or problem → 2-4 steps or benefits → product or demo → CTA |
| `brand` | about us, values, team, story | hook with the brand promise → photos of the brand's world → values or benefits → endcard with the logo |

A brief that mixes goals: pick the goal its call to action serves.

## Picking presets

- Query `searchPresets` with the goal and the brief's subject (product, service, industry). Read `reasons[]` to see why a preset fits and `needs[]` to see what it requires.
- Prefer scenes whose needs you can meet now: media you have and facts the brief states. A scene built around a price you do not have is a poor pick (`regulated-values.md`).
- Use each story role once; avoid two scenes with the same layout back to back, except one `seasonal.bf-price-drop` per reduced product.
- Seasonal scenes only when the brief is about that sale or calendar occasion (Black Week, Christmas, Easter, Mother's Day, Valentine's Day and more; `searchPresets` finds the occasion presets). Exception, in any season: every price reduction uses `seasonal.bf-price-drop` or `seasonal.bf-big-percent`, and the sale dates, deadlines and discount code of a promotion go to the scenes SKILL.md names for them (`seasonal.bf-end-card`, `seasonal.bf-teaser`, `seasonal.bf-countdown`) (`regulated-values.md`).
- A ready reel fits when its scenes follow your story with at most one scene added or removed. It starts personalized: only reviewed texts that say nothing about this business stay, every other text comes from the brand profile or is left empty with a `personalization.gaps` entry (SKILL.md step 4).

## Duration, format, transitions

- Length: as requested (5-60 s), else 15-30 s; the server refuses more than 60 s. Roughly 3 scenes for 15 s, 5-6 scenes for 25-30 s.
- Keep every scene inside its duration range. Give text time to be read: about 1 s per 3 words on screen plus 1 s. Hooks 2-4 s, endcards 3-5 s.
- Keep the requested format (default 9:16); change it only when the brief asks.
- Transitions: `fade` reads calm, `cut` reads energetic (promotions). Keep one style per draft.
