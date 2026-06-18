# Operating Guide

The method Atlas encodes (for research *and* development). It is **distilled from failure modes
actually hit** in a real program, generalized for reuse - so it is incomplete by construction and meant to grow
(see §7). It gets the same discipline it preaches: additive, episode-anchored, checklist-shaped.

## 0. The one sentence
Rather be right than impressive: **lead with the instrument, not the law.** Show what was measured
and whether the instrument can even resolve the effect - before any claim about what it means.

## 1. The result lifecycle (the loop that works)
1. **Scope** the question; state what would falsify it.
2. **Cheap pilot first** - smallest run that could show the effect or kill the idea.
3. **Preregister** - freeze hypothesis, metric, units, N, and the pass/fail threshold in a committed
   file *before* the full run. Optionally timestamp it (OpenTimestamps) for blind-prereg provenance.
4. **Build & run** - reproducible from a named artifact (code + data + commit).
5. **Gate** - an evaluator computes a pre-stated verdict to a `gate_evaluation.json` (once-only; the
   evaluator refuses to silently re-run and overwrite).
6. **Adversarially review** (`/council`) - try to *refute* the result before recording it.
7. **Record** the verdict in `CURRENT_STATE.md` - additively. Loop: fix → re-gate, solid → record,
   obstruction/refuted → document and move on. **An obstruction is a valid, publishable outcome.**

## 2. Claim hygiene
- A result is a **candidate**, not a claim, until it clears the §6 checklist. Say "candidate."
- Name the **measured quantity exactly**. A proxy is not the ground truth it proxies.
- State **N, units, and uncertainty (CI)**. No bare point estimates for comparative claims.
- **Pre-state thresholds with units.** No fail-to-pass tuning after seeing the data.
- Distinguish **derived / assumed / conjectured** in any analysis. Don't let an assumption travel as
  a result.

## 3. The confound catalog (rule ← episode)
Add one line per confound that has actually bitten you. Starters (genericized from real episodes):
- **Currency / units** - comparing quantities in different units (e.g. nats/token vs bits/byte) silently
  inflates effects. *A verdict that flips on a unit conversion is a RED FLAG - recompute, don't ship.*
- **Convergence / resolution** - an effect that depends on grid/sample resolution may be a numerical
  artifact; show it survives refinement.
- **Same-corpus / same-split** - train and eval leakage flatters every method. Use disjoint splits.
- **Capacity mismatch** - "A beats B" when A simply has more parameters/budget. Match capacity.
- **Empty-output / cwd reset** - a gate file silently emptied by a subshell/cwd change reads as a
  spurious result; confirm output is non-empty before reporting PASS.

## 4. Thresholds and verdicts
- The threshold is **pre-stated, with units, before the run.** The evaluator emits the verdict; a human
  override of an auto-verdict must be justified in writing.
- **A verdict override that hinges on a unit conversion is a red flag.** This is where confident,
  motivated reasoning sneaks an artifact through as a finding.
- "ALL GATES PASS" must trace to a real, re-runnable evaluator artifact - not a claim in prose.

## 5. Narrative discipline
- The write-up leads with the instrument and the measurement, then the interpretation - clearly labeled
  as interpretation.
- Scope every claim ("under these assumptions", "in this toy regime", "on this dataset").
- Negatives and obstructions are reported plainly, never buried. They are the most trustworthy output.

## 6. The pre-claim checklist (gate before any result becomes a claim)
- [ ] Reproducible from a named artifact (code + data + commit).
- [ ] Not true by construction (tautology check passed).
- [ ] The measured quantity is named exactly; proxies are not called ground truth.
- [ ] N, units, uncertainty (CI) stated; held-out / OOD where relevant.
- [ ] Instrument shown to resolve the effect (power / dynamic range / estimator radius < signal).
- [ ] Seeds + CI + a sign/permutation test for any comparative claim.
- [ ] Confounds ruled out: convergence, currency/granularity, same-corpus, capacity, same-split.
- [ ] Thresholds were pre-stated with units; no fail-to-pass tuning; auto-verdict overrides justified.
- [ ] Gated commands run from a clean shell with an explicit cwd; the gate file is **non-empty** before PASS.
- [ ] Adversarially verified (someone tried to refute it); a *positive* was pre-committed to be broken and survived.
- [ ] Load-bearing numbers re-derived from the raw artifact by an independent route (not trusted from a script/sub-agent).
- [ ] Recorded additively; withdrawals (if any) left in place.

If any box is unchecked, it is a **candidate**, not a claim. Say so.

## 7. Amending this guide
- **Additive, episode-anchored.** When a new way-you-fooled-yourself appears, add a §3 line: the rule +
  the dated episode that earned it. Don't rewrite history; append. A wrong rule is struck in place with
  the reason, never deleted.
- **Earned, not theorized.** A rule enters only when a *real* episode motivates it.
- **Stays a checklist, not an essay.** Each addition must be actionable at the §6 gate.

*Amendment log:* (append `YYYY-MM-DD - rule added/struck - episode`)
- (template) - guide instantiated from Atlas.
