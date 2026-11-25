# Google Search Playbook (B2B)

Operating rules for Google Ads when you sell to businesses: what to fund first, how to lay out the account, when to loosen matching, and how to stop automated bidding from optimizing toward worthless form fills. For RSA generation mechanics, see [rsa-output-spec.md](rsa-output-spec.md).

## Contents

- Where to spend first: five intent tiers
- Brand campaign and the pause test
- Search harvests demand, it does not make it
- Campaign layout and budgets
- Defaults to change on new campaigns
- Choosing keywords and match types
- Negatives: starter lists and mechanics
- Weekly query review
- Matching bid strategy to conversion volume
- Feeding CRM outcomes back to Google
- Ad rank levers: Quality Score and landing pages
- Performance Max in B2B
- Benchmarks and a weekly scorecard

## Where to spend first: five intent tiers

Fund the tiers in order. A tier gets budget only once the tier beneath it has shown that its clicks turn into pipeline, not just leads.

1. **Brand.** The searcher already knows you (your name, or your name plus pricing or login). Clicks are cheap and convert best. Keep it running.
2. **High-intent non-brand.** The searcher is ready to buy (for example "cold email software" or "best CRM for agencies"). This is where most of the money should sit.
3. **Competitor.** The searcher is comparing options ("[competitor] alternative", "X vs Y"). Expect higher CPC and weaker conversion, so run it selectively and send traffic to purpose-built comparison pages.
4. **Problem-aware.** The searcher feels the pain but is not yet comparing vendors ("how to scale outbound"). Payback is slow, so wait until tiers 1 and 2 are working.
5. **Broad awareness.** Display, YouTube and wide demand-gen. Last in line, funded only from leftover budget.

Moving to a lower tier before the upper ones are proven is the usual way B2B accounts spend a lot and show nothing in the CRM.

## Brand campaign and the pause test

Bid on your own name by default. If you leave the space empty, a rival will take it, and you will pay for that in lost deals instead of in click costs. One exception: when nobody else bids on your name and your organic listing already dominates the results page, run a pause test. Switch brand ads off and track **total brand conversions, paid plus organic**, not only the paid number. If the total stays flat, the ads were just taking credit for traffic you would have won anyway. If it falls, switch them back on. Give brand its own capped budget; it seldom needs much, and sharing a budget lets it swallow everything (see layout below).

## Search harvests demand, it does not make it

Search only catches people who are already looking. If your category has almost no query volume, say so plainly and move the money upstream (LinkedIn, Meta, YouTube) instead of inventing keywords nobody types. Create the demand on social and video; use Search to be there when it shows up.

## Campaign layout and budgets

Start with four campaign types, each with its **own budget**:

- **Brand**, never on a shared budget.
- **Non-brand high-intent**, a single campaign split into ad groups by the solution being sold.
- **Competitor**, with separate budget and messaging, since its cost and conversion economics differ.
- **Remarketing**, kept apart from Search.

The reason for separate budgets: when campaigns share one, the cheapest and best-converting campaign (always brand) takes the spend, and the campaigns you need data from get starved. The account then looks healthy in aggregate while telling you nothing about the parts that matter.

Ad group rules:

- Use **themed groups, not single-keyword groups.** Put 5 to 15 closely related keywords with a common intent in one group, so a single message can answer all of them. When two keywords need separate landing pages or separate value propositions, they should be split. Run 2 to 3 RSAs per group.
- **Consolidate thin campaigns.** If a campaign cannot reach roughly 15 to 30 conversions a month, automated bidding has too little to learn from, so merge it into a neighbor. In low-volume B2B, a few well-fed campaigns beat an elaborate tree.
- **Avoid self-competition.** The same keyword at the same match type in several ad groups fragments the data and has your own ads bidding against each other. Use negatives so each query has exactly one home.

## Defaults to change on new campaigns

- Turn off Search Partners and the Display Network until you have evidence they pay off.
- Set location targeting to **"Presence"** so only people physically in the target area see ads. The default also includes people who merely show interest in the location.
- Remember that language targeting follows the user's Google interface language, not the language of the query.

## Choosing keywords and match types

Take keyword ideas from the way **buyers phrase their problem**: sales call transcripts, your own search-terms report, rival ad copy. Do not use your internal product vocabulary. Volume is a poor guide on its own; a term searched fifty times a month by clearly motivated buyers can outperform one searched thousands of times with mixed motives. Label every keyword with its intent tier.

**Loosen match types in this order:**

1. Launch high-intent terms on **Phrase and Exact**. Exact already catches close variants, and Phrase is the everyday choice in B2B. Use manual CPC or Maximize Conversions while volume is low.
2. Review the search-terms report every week (see the review routine below).
3. Add **Broad** only when all three hold: the campaign records 30 or more conversions a month, automated bidding is running, and you have a solid negative list. Missing any one of them makes Broad an expensive gift to Google.

**AI Max for Search** follows the same gate. It reaches searches outside your keyword list, may rewrite your ad text to suit the query, and can route clicks to another page on your site (final URL expansion). That suits the longer, more specific questions buyers type today, but in B2B it can drop a prospect on a careers page or a blog post. If you pilot it, exclude URLs that should never receive ad traffic, check the queries and landing pages it picked during the weekly review, and run it against a comparable campaign that does not use it.

## Negatives: starter lists and mechanics

Load these when you build the campaign:

- **Job seekers and learners:** jobs, careers, hiring, salary, internship, student, course, tutorial, training, certification.
- **Bargain hunters:** free, cheap.
- **Reference and content seekers:** wiki, reddit, pdf, template, plus informational openers such as "what is", "how to", "examples", "meaning", "definition".
- **Login** as a negative, except inside brand campaigns.
- **Category collisions:** words your category shares with an unrelated field (if you sell sales engagement software, block "employee engagement").
- **Your own brand name** in non-brand campaigns, so brand searches go to the brand campaign.

**How match types behave for negatives:** a negative broad term needs every one of its words in the query, in any order. A negative broad "free trial" therefore does **not** stop a query that has only "free". A negative phrase blocks the words together in order, and a negative exact blocks only that precise query. Most unexpected blocking or leaking comes from forgetting this.

**Restraint:** each negative removes reach, and the loss adds up quickly at B2B volumes. Block what is plainly irrelevant. When a term is merely uncertain, wait for more data before cutting it.

## Weekly query review

Once a week for each campaign, do three passes through the search-terms report:

1. **Waste.** Queries with 3 or more clicks and no conversions: add the clearly irrelevant ones as negatives.
2. **Winners.** Queries that convert but have no keyword of their own: promote them to Exact or Phrase keywords, placed in whichever ad group fits best.
3. **Drift.** Phrase or Broad matches that are being read in a neighboring but wrong sense: tighten the match type or add a negative.

## Matching bid strategy to conversion volume

| Conversions per month (campaign) | Strategy |
|---|---|
| 0 to 15 | Manual CPC, or Maximize Conversions with no target |
| 15 to 30 | Maximize Conversions |
| 30 or more, steady | Target CPA, set at or just above your trailing 30-day actual |
| Revenue values reported back | Target ROAS |

Working rules: smart bidding generally needs about 30 conversions within a 30-day window per campaign before it settles. Keep a tCPA close to what you actually achieve, because a target set too low starves delivery (Google simply stops bidding). Change targets in **steps of 10 to 15% and give each change one to two weeks**. Every adjustment restarts learning, so avoid reacting to short-term noise while a campaign is still learning. On budgets: a campaign can run up to **twice its daily budget** on any single day, since Google evens things out over the month, so an occasional overspend day is normal. A converting campaign that keeps hitting its budget often sees its CPA improve when you raise the budget, because capped smart bidding performs worse.

## Feeding CRM outcomes back to Google

If you do one thing to improve a B2B Google account, make it this: send CRM results (SQL, opportunity, closed-won) back to Google with deal values, using GCLID-based offline conversion import or a native CRM connector. Without it, automated bidding chases form fills and buys you low-quality leads (see the optimize-to-quality trap in [b2b-paid-playbook.md](b2b-paid-playbook.md)). B2B deals close over 60 to 180 days, so counts inside the ad platform cannot tell you the real story alone. Compare them with the CRM every month, and when the two disagree, trust the CRM.

## Ad rank levers: Quality Score and landing pages

Quality Score (1 to 10, per keyword) blends three inputs: how likely the ad is to be clicked, how relevant it is to the query, and how good the landing page is. A low score means paying more to hold the same position, so **repair the weakest component before you raise bids.** Landing page changes that lift it: message match (the headline repeats the ad's promise and the searcher's wording, rather than a generic homepage), a single purpose and single call to action per page, fast loading, and proof visible without scrolling. **Form length acts as an intent filter.** Short forms bring more volume at lower quality; longer qualifying forms bring fewer, better leads. Choose the length to fit whatever event you are passing back as the conversion.

## Performance Max in B2B

Think of the budget order as: brand Search first, then high-intent non-brand Search, then remarketing, then PMax, then broad demand-gen last. PMax gets money only after the cheaper, clearer wins are used up. Do not make it your first campaign, run it on weak tracking, or give it a tiny budget.

When you do run it, set guardrails: account-level **brand exclusions** (otherwise it cannibalizes brand Search and takes credit for it), audience signals built from first-party data, negative keywords from the start, and offline conversions imported *before* you scale spend. Review PMax lead quality in the CRM by campaign. If only half as many of its leads move into pipeline as Search leads do, it looks cheap and is costly in practice. If you do not supply a video, Google will build a poor one for you.

Check for overlap with Search routinely. In a February 2025 study of 503 accounts it manages, Optmyzr (a PPC tool vendor) found 91% had exact keyword overlap between Search and PMax, touching 56% of 5,768 Search campaigns. That measures how common overlap is; it says nothing about how much spend the overlap costs. To size it for your account, compare the PMax search-terms insights against your Search keywords, and look for brand and high-intent terms that Search would win more cheaply.

## Benchmarks and a weekly scorecard

Typical B2B SaaS Search ranges (deliberately wide; anchor to your own first 30 days): brand CTR 8 to 20% and CVR 15 to 40%; non-brand high-intent CTR 2 to 6%, CVR 3 to 10%, CPC $8 to $40+, CPL $80 to $400+; competitor terms cost more per click and convert less than non-brand.

Track exactly eight numbers each week: spend, leads, CPL, lead-to-SQL rate (from the CRM), SQLs, cost per SQL, Search impression share, and the biggest wasted search terms. For diagnosis, compare **Search Lost IS (budget)** with **Lost IS (rank)**: they show whether growth is held back by money or by Ad Rank, which are different problems with different fixes. When those eight look good and are moving the right way, the account is in good shape.

---

*Framework lineage: adapted (re-expressed and restructured) from practitioner playbooks, notably Ivan Falco's ads-skills. Benchmarks are practitioner-reported starting points. Recalibrate against your own account.*
