# Regulated values (Omnibus)

EU consumer rules (the Omnibus directive; in Poland the price information rules) require every announced price reduction to show the lowest price from the 30 days before the reduction, and forbid fake reviews. A wrong or invented value exposes the brand to fines and its customers to deception. The server marks every regulated field and blocks the render until the user confirms each value. Your job is to never put a wrong value there.

## What is regulated

Any field that holds a price, an old or regular price, a discount amount or percentage, a discount code, the lowest price from the 30 days before a reduction (`priceNote`, or `terms` of `seasonal.bf-big-percent`), a promotion start or end date, a deadline or a countdown target. SKILL.md lists where each value goes; `getDraft` marks these fields `regulated` in `values_to_confirm`. Customer quotes, ratings, results and statistics follow the same rules.

## Rules

1. **Source.** Only the brief or the brand profile (its fields, saved reviews and knowledge documents). Gallery captions, sample texts, earlier drafts and your own knowledge are not sources.
2. **Verbatim.** Copy the figure, currency and date exactly as written: "199 zł" stays "199 zł", "-30%" stays "-30%". You may leave out words around the value that do not fit the field; never change a digit, the currency or the date.
3. **Never compute.** No new price from an old price and a percentage, no percentage from two prices, no absolute date from "do niedzieli", no added year or weekday.
4. **Never confirm.** Everything you write stays for the user to confirm. Never write or imply "potwierdzone", "zgodne z prawem" or "sprawdzone".
5. **Only in its own field.** A regulated value goes only into a field built for it (SKILL.md), never into a headline, kicker, subline, caption, CTA, list item, text overlay or scene title, also not as a repeat of a value its own field already shows. The server checks only the regulated fields, so a value anywhere else reaches the video without the user's confirmation. Write around it: "Zimowe kurtki taniej", "Black Week w Ziarenku", "Zapisy w kawiarni".
6. **Every reduction in `seasonal.bf-price-drop`.** A price reduction (a price shown with an old price or a discount, Black Friday, sale, "-30%", "obniżka", "promocja") uses `seasonal.bf-price-drop`, the scene whose `priceNote` states the lowest price from the 30 days before the reduction. One product per scene; for several products, one scene each. Never `offer.photo-price` with `oldPrice` or a discount `badge` (it has no 30-day field), never a reduced price in `seasonal.bf-deals-list`. `offer.photo-price` is for a regular, not reduced price. Write `priceNote` and `oldPrice` only when the brief or the profile states them; a missing `priceNote` stays empty (it then appears in `to_complete`), the summary asks for it, and the old price never replaces it. Never a placeholder such as "XX zł".
7. **No price stated.** Prefer scenes without price fields. If the story needs one, leave the price field empty for the user.
8. **Percent only.** A brief like "-30% na wszystko" (no price) fits `seasonal.bf-big-percent`: the percentage verbatim in `percent`. Its `terms` line is the scene's 30-day field: what the discount covers, until when, and that it is counted from the lowest price of the 30 days before the reduction; write it only when the brief states what it covers and until when, else leave it empty for the user. Either way the summary asks the user to check the lowest prices from the 30 days before the reduction.
9. **Samples.** No path keeps a regulated sample: `createDraft` from a ready reel, a preset added with `add_preset_scene` and a ready reel MCP `syncbooster_create_creative` starts from all leave every regulated place empty, with a `personalization.gaps` entry: price, old price, discount or percentage (`badge`, `percent`), the 30-day lowest price line (`priceNote`), `terms`, a code, a date or deadline (`kicker`, `dateLine`, `endDate`, the days left `number` of `featured.countdown`). Fill each only with a stated value (it then waits in `values_to_confirm`), else leave it empty for the user; a required one left empty blocks the render (`to_complete`).
10. **Quotes and ratings.** Only real reviews from the brief or the profile, verbatim and attributed as given. Never compose a quote, a name or a star rating. No real review: choose another goal or scene.

## Examples

| Brief | Do | Never |
|---|---|---|
| "Rolka na Black Friday -30% na wszystko" | `seasonal.bf-big-percent` with "-30%"; `terms` empty (no end date stated); summary asks for the end date, the terms and the lowest prices from the 30 days before the reduction | "199 zł → 139 zł", "Najniższa cena z 30 dni: 189 zł", an invented end date, "-30%" in a headline |
| "Kurtka Alpina 399 zł zamiast 499 zł, do niedzieli" | `seasonal.bf-price-drop`: price "399 zł", old price "499 zł", `priceNote` empty; "do niedzieli" in the `kicker` of `seasonal.bf-end-card`; summary: "Uzupełnij najniższą cenę z 30 dni przed obniżką" | `offer.photo-price` with an old price; computing "-20%"; turning "do niedzieli" into "30.11"; "Tylko do niedzieli" in a caption |
| "Kurtka Alpina 399 zł zamiast 499 zł, najniższa cena z 30 dni 459 zł" | `seasonal.bf-price-drop` with all three values verbatim, `priceNote` with "459 zł"; all listed to confirm | rewording the figures; the 30-day price in a subline |
| "Kurtka 399 zł zamiast 499 zł, buty 199 zł zamiast 249 zł" | two `seasonal.bf-price-drop` scenes, one per product, each with its own `priceNote` (empty here) | both in `seasonal.bf-deals-list` |
| "Warsztaty latte art, 150 zł od osoby" | "150 zł" in `price` of `offer.photo-price`; the caption names the workshop without the price | "150 zł od osoby" in a caption or headline |
| "Nowe menu lunchowe" (no price) | scenes without prices, a CTA | "Lunch od 29 zł" |
| "Zrób rolkę z opiniami klientów" (no reviews in the profile) | another story (`brand` or `explainer`); summary asks for real reviews | an invented quote with a name |

## Summary wording

List what you used and what is missing, in the output language. Polish example: "Do potwierdzenia: cena 399 zł, stara cena 499 zł, termin „do niedzieli”. Do uzupełnienia: najniższa cena z 30 dni przed obniżką."
