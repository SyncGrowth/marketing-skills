# The Operating Check: Weekly Account Review That Ends in a Decision

A routine account review earns its time only when it finishes with a verdict that someone can act on. A page of metrics with no verdict is reporting theater: people read it, nothing changes, and whatever it hinted at keeps costing money.

Run it once a week on every account. Run it daily on accounts that have a live test, a recent launch, or heavy daily spend. With the data already exported it takes about 15 minutes. Read it alongside [audit-guardrails.md](audit-guardrails.md), which sets the standard for what counts as evidence.

## Inputs

Collect the same set each time and compare the same windows: this period against the previous comparable one, or today against the trailing 7 days on a daily run. Also keep the same metrics for the **last 6–8 periods** (weeks for a weekly run, matching weekdays for a daily run). That history is the account's normal range, and the HOLD verdict further down is judged against it.

- Spend, budget and pacing, by campaign
- Impressions, clicks, CPC, CTR, CPM, plus impression share lost to budget and lost to rank
- Conversions, conversion rate, CPA or ROAS and conversion value, each labeled with its attribution window
- For lead gen, lead quality or the downstream result from the CRM
- Frequency and CTR trend on the ads that take the most spend
- Landing page conversion rate split by device (from analytics)
- The change log for the period: who changed what, and when

When something can't be pulled, write **MISSING** next to it and carry on. A guess in its place is worse than a gap.

## The check, in order

Start by deciding whether the numbers can be believed, then follow the money and the visitor through the funnel, and look at outcomes last. Outcomes are the symptom; the earlier stages are where causes live. Stop at the first stage that explains the movement rather than documenting every downstream effect.

**Stage 1. Measurement: can I trust what I'm reading?**
- Compare platform conversion counts against analytics and the CRM
- Look at event match quality, consent rate and the status of offline imports
- Typical culprits: a removed or duplicated tag, a consent banner change, a failed import job

**Stage 2. Delivery: is money going out as planned?**
- Check pacing against budget, daily caps that were hit, limited-delivery flags and impression share lost to budget
- Typical culprits: a budget edit, a cap on a winning campaign, a billing problem

**Stage 3. Traffic: who is the account buying?**
- Review clicks, CPC, CTR and CPM, then new search terms or placements
- Typical culprits: auction pressure, a new competitor, match-type drift, a sudden placement

**Stage 4. After the click: does the page still work?**
- Test page speed, form and checkout errors, and the gap between mobile and desktop conversion rate
- Typical culprits: a recent deploy, a broken form, a script that blocks rendering

**Stage 5. Creative: are the ads wearing out?**
- Compare frequency, each ad's CTR against its own best period, and whether spend piles onto a few old ads
- Typical culprits: a saturated audience, no new concepts entering rotation

**Stage 6. Outcomes: what happened to results?**
- Read conversion rate, CPA or ROAS, conversion value and lead quality, only after the five stages above
- Typical culprits: an offer change, seasonality, weaker leads, attribution lag on the latest days

Hold every movement up against the change log. A metric that shifted the day after a budget edit, a bid strategy switch or a new ad launch most likely shifted because of it.

Accounts with conversion lag undercount the most recent days. Treat those days as unfinished and never call a trend from them alone.

**A single comparison is not a trend.** A week that looks poor next to last week may only mean last week was unusually strong. Before issuing anything other than HOLD on a performance metric, place the current period inside the trailing 6–8 periods. Inside the range is ordinary variance. Outside it, or three or more periods in a row moving the same direction, is a real movement and deserves FIX, TEST or INVESTIGATE. Three kinds of finding skip the baseline because they are facts rather than trends: spend problems, tracking problems, and broken pages. So do explicit stop thresholds set against a target, for example cost per qualified lead above 1.5× TCPL in the [Meta decision system](meta-decision-system.md); those trigger against the target even when the metric sits inside its own recent range.

## The decision

Close each check with one verdict for the account, and optionally one per campaign that moved. Work through these questions in order and take the first one that answers yes:

1. **Is any input I'd need for a performance call unreliable or MISSING?** Verdict: **INVESTIGATE**. Typical triggers are conversions that disagree between platform, analytics and CRM, or a count that jumped with no business reason. Nothing about performance can be concluded until this is settled, so it outranks every other verdict.
2. **Is there a named defect with a known repair?** Verdict: **FIX**. Examples: a broken form, a budget cap on a campaign that is winning, a disapproved ad, a tag that stopped firing.
3. **Is there a hypothesis worth paying to answer?** Verdict: **TEST**. Examples: a new concept against a fatigued ad, a bid strategy change on a campaign with enough volume, a landing page variant.
4. **Otherwise: HOLD.** Change nothing and look again in 24 hours or at the next scheduled check. HOLD is right when the move sits inside the normal range and is not a three-period run or an exempt threshold, when the sample is small, when the campaign is still learning, or when lag explains the dip.

What each verdict must contain:

- **INVESTIGATE** names the number that can't be trusted and the source to reconcile it against.
- **FIX** names both the defect and the repair. "Performance is down" is not a FIX.
- **TEST** states the hypothesis, the metric that will judge it, and when the test stops. A test with no stop condition quietly becomes a permanent change nobody decided on.
- **HOLD** states why, and what result would change the verdict.
- **No verdict moves money by itself.** Changes to budgets, bids, campaign status or tracking go to a person as a draft: current state, proposed change, expected effect, rollback, awaiting approval.

Attach three short lists to every verdict: **facts** (visible in the data), **hypotheses** (inferred, not shown), and **missing data** (what would alter the call).

## The Friday readout

End the week with a note a stakeholder can absorb in about a minute, built from three blocks:

| Block | Contents |
|---|---|
| **Scoreboard** | One line per account or program, tagged green, amber or red against its CPA, ROAS or pipeline target |
| **Drivers** | The two or three biggest movements, each with its probable cause and a confidence rating (high, medium, low) |
| **Calls for next week** | Each decision tagged HOLD, FIX, TEST or INVESTIGATE, with a single line of reasoning |

Cut any metric that nobody will act on: a number belongs in the note only when it backs up a result, a cause or a decision. State plainly any missing data that limits what you can conclude, and flag that every change involving money is waiting on approval.

## Making it a habit

Do the check by hand for the first two weeks before automating any piece. Doing it manually reveals which inputs are painful to get and which verdicts keep recurring, and those are exactly what an automation has to cover. When you are ready to schedule it, the **marketing-loops** skill covers recurring checks that carry state from one run to the next.

---

*Framework lineage: the idea of a fixed-order account check, four-verdict decisions and a short stakeholder readout comes from Marek Dąbrowski's "The Paid Ads Operator's Guide to Claude" (Adlume, 2026-07-16). The structure and wording here are this skill's own, adapted to its guardrails.*
