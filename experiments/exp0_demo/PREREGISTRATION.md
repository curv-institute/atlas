# Preregistration — exp0_demo

**FREEZE THIS FILE BEFORE RUNNING.** Commit it; optionally OpenTimestamp it (see note) so the
prereg is provably blind to the results.

## Hypothesis
Method **A** (a shrinkage estimator) achieves lower held-out prediction error than baseline **B**
(ordinary least squares) on the synthetic task defined in `pilot/run.py`.

## Design
- Synthetic regression: `n_train=64`, `n_test=4000`, `d=40` features, true sparse coefficients,
  Gaussian noise. `n_seeds=200` independent seeds.
- Per seed, fit A and B on train, measure test error on the **held-out** test split (disjoint from
  train — no same-split leakage).
- Primary metric: **relative error reduction** `Δ = (err_B − err_A) / err_B`, reported as a fraction
  (dimensionless), per seed.

## Pre-stated thresholds (with units) — set before any run
- **PASS** iff *both*:
  1. paired sign test of `err_A < err_B` across seeds has **p < 0.01** (two-sided), AND
  2. the **95% bootstrap CI of mean Δ excludes 0** (Δ in dimensionless fraction units).
- Otherwise **FAIL** (or MARGINAL if exactly one of the two holds).
- The metric Δ is a **dimensionless fraction**. It must not be reported in any other unit. (This
  experiment deliberately demonstrates the unit-confound failure mode; see RESULTS.)

## Confounds pre-addressed
- Disjoint train/test splits (no same-split leakage).
- A and B fit on identical data per seed (matched).
- Effect reported with CI + sign test (not a bare point estimate).

## Evaluator
`gate.py` reads `raw.json`, recomputes the two gate conditions, and writes the verdict to
`gate_evaluation.json`. Once-only: it refuses to overwrite an existing verdict unless `--force`.

## Provenance note (optional, recommended)
After committing this file:
`ots stamp PREREGISTRATION.md` (OpenTimestamps) → commit the `.ots`. That timestamps the prereg
against the Bitcoin chain, evidencing it predates the run. Reproducibility (clone-and-run) and
preregistration (blind, timestamped) are distinct guarantees — keep both, conflate neither.
