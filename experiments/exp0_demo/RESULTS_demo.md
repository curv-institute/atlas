# Results - exp0_demo

> **VERDICT: PASS** (preregistered gate, `gate_evaluation.json`).
> Method A (shrinkage) beats baseline B (OLS) on held-out predictive NLL.
> Effect = **Δ 0.387** (38.7% relative reduction, *dimensionless*), 95% CI **[0.363, 0.412]**,
> paired sign test **p = 1.7e-54** (A better in **197/200** seeds). Artifact: `raw.json`
> (`content_sha256` f6c209...), evaluator `gate.py`. Reproduce: `uv run pilot/run.py && uv run gate.py`.

## Instrument first (OPERATING_GUIDE §0)
The instrument is the per-seed held-out NLL gap with a paired sign test and a bootstrap CI over 200
seeds. It resolves the effect with enormous margin (p≈1e-54), so the dynamic range is not in doubt.
Train and test splits are disjoint (no same-split leakage); A and B see identical data per seed
(matched). The **primary metric is dimensionless** (a relative reduction), which makes the headline
unaffected by unit choices, by design.

## Worked example: an overclaim, caught, and walked back
This is the teaching core of the demo - the failure mode that most often sneaks an artifact through
as a finding (OPERATING_GUIDE §3 currency, §4 red-flag).

**Draft v1 (overclaimed):**
> "Method A saves **2.04 bits/sample** - it is roughly **2× better** than the baseline."

**`/council` refutation (re-derived from `raw.json`):**
1. **Unit error.** `2.04` is `mean_abs_nats` - an absolute NLL gap in **nats**, not bits. `raw.json`'s
   `units` block labels it `nats`; the draft relabeled it "bits." (Nats↔bits differ by 1/ln2≈1.443×;
   silently swapping units is exactly the §3 *currency* confound.)
2. **Scale error.** An absolute NLL *gap* of 2.04 is **not a 2× ratio**. The preregistered metric is
   the **dimensionless relative reduction Δ = 0.387** (a 38.7% reduction), not "2×."
3. **Verdict hygiene (§4).** The "2.04 bits / 2×" framing was never in `PREREGISTRATION.md`; it's a
   post-hoc, mis-united restatement. A claim whose size hinges on a unit/scale conversion is a **red
   flag** - recompute, don't ship.

**Walkback (additive - the overclaim stays visible):**

> ~~"A saves 2.04 bits/sample, ~2× better."~~ **WITHDRAWN** - conflated units (nats reported as bits)
> and scale (absolute NLL gap reported as a ratio). The surviving, preregistered result stands:
> **A reduces held-out NLL by 38.7% (Δ, dimensionless), CI [0.363, 0.412], p≈1.7e-54.**

The withdrawal is also recorded in the program-level register: `CURRENT_STATE.md` §3.

## What this demo demonstrates about the method
- Preregistered, unit-bearing thresholds + a once-only evaluator → a verdict you can trust.
- A **dimensionless** primary metric is immune to the unit confound that killed the bonus claim.
- Adversarial review (`/council`) re-derives load-bearing numbers from the raw artifact and catches
  the overclaim *before* it becomes a claim.
- The withdrawal is recorded **additively** - the record stays honest and the lesson stays reusable.
