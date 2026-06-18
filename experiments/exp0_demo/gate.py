# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""exp0_demo evaluator — recomputes the PRE-STATED gate from raw.json and writes the verdict.

Gate (frozen in PREREGISTRATION.md): PASS iff BOTH
  (1) paired sign test of err_A < err_B has two-sided p < 0.01, AND
  (2) the 95% bootstrap CI of mean delta (dimensionless) excludes 0.
Once-only: refuses to overwrite an existing gate_evaluation.json unless --force.
Run:  uv run gate.py --raw raw.json --out gate_evaluation.json
"""
from __future__ import annotations
import argparse, json, math, os
import numpy as np

P_THRESH = 0.01
BOOT = 2000


def two_sided_sign_p(k: int, n: int) -> float:
    """Exact two-sided binomial p under H0: P(A better)=0.5."""
    def tail_le(x):
        return sum(math.comb(n, j) for j in range(0, x + 1)) / 2**n
    lo = min(k, n - k)
    return min(1.0, 2 * tail_le(lo))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="raw.json")
    ap.add_argument("--out", default="gate_evaluation.json")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if os.path.exists(a.out) and not a.force:
        raise SystemExit(f"{a.out} exists; refusing to overwrite (once-only eval). Use --force to re-run.")

    raw = json.load(open(a.raw))
    errA = np.array(raw["per_seed"]["err_A"]); errB = np.array(raw["per_seed"]["err_B"])
    delta = np.array(raw["per_seed"]["delta"]); n = len(delta)

    k = int((errA < errB).sum())
    p = two_sided_sign_p(k, n)

    rng = np.random.default_rng(0)
    means = np.array([delta[rng.integers(0, n, n)].mean() for _ in range(BOOT)])
    ci_lo, ci_hi = float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))

    cond1 = p < P_THRESH
    cond2 = (ci_lo > 0) or (ci_hi < 0)
    verdict = "PASS" if (cond1 and cond2) else ("MARGINAL" if (cond1 or cond2) else "FAIL")

    out = {
        "verdict": verdict,
        "units_note": "delta is a dimensionless fraction; abs_nats is in NATS. Do not relabel units.",
        "gate_1_sign_test": {"k_A_better": k, "n": n, "p_two_sided": p, "threshold": P_THRESH, "pass": cond1},
        "gate_2_bootstrap_ci": {"mean_delta": float(delta.mean()), "ci95": [ci_lo, ci_hi],
                                 "excludes_zero": cond2},
        "raw_content_sha256": raw.get("content_sha256"),
    }
    json.dump(out, open(a.out, "w"), indent=2)
    print(f"verdict={verdict}  sign-test p={p:.2e} (k={k}/{n})  mean_delta={delta.mean():.4f} "
          f"CI95=[{ci_lo:.4f},{ci_hi:.4f}]")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
