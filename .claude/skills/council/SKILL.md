---
name: council
description: Convene an adversarial review (ideally multi-agent) to verify a result, vet a design, or make a go/no-go call - refute don't confirm, re-derive load-bearing numbers independently, hunt the known confounds, and scrutinize any positive hardest of all. Use when the user says "/council", "adversarially review/verify this", "is this real / break this claim", "vet this plan", or "should we go/no-go on X". Operationalizes OPERATING_GUIDE.md §1.6 / §3 / §6.
---

# /council - adversarial review, verify, or go/no-go

Try to **break** a claim, design, or decision before it becomes a claim. The bias is refutation: a
finding that survives a real attempt to kill it is worth far more than one that was confirmed. Run
as a panel of independent, refutation-minded reviewers (use parallel sub-agents if available).

## Procedure
1. **State the claim precisely** - the exact quantity, scope, N, units, and the artifact it rests on.
2. **Assign independent angles** (one reviewer each; don't let them confirm each other):
   - **Re-derivation** - recompute every load-bearing number from the *raw* artifact by an
     independent route. Trust no number that came only from a script or a sub-agent.
   - **Confound hunt** - walk the `OPERATING_GUIDE.md` §3 catalog: currency/units, convergence/
     resolution, same-corpus/same-split, capacity mismatch, empty-output/cwd. **A verdict that flips
     on a unit conversion is an automatic red flag.**
   - **Instrument check** - can the instrument even resolve the effect? Power / dynamic range / CI vs
     signal. Pre-stated thresholds, no fail-to-pass tuning?
   - **Steelman the null** - try hardest to make the *positive* go away.
3. **Pre-commit the verdict rule** before looking (what evidence = PASS / FAIL / MARGINAL).
4. **Adjudicate** - PASS only if it survives all angles. Return the verdict + the surviving evidence +
   any corrections, and update the §6 checklist.

## Output
A written verdict: claim, attempts to refute, what survived, what was corrected/withdrawn, and the
final PASS / FAIL / MARGINAL with scope. Record withdrawals additively in `CURRENT_STATE.md`.
