# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""exp0_demo - runnable lifecycle demo (deterministic, numpy-only).

Task: predict a sparse linear target from d=40 features with only n_train=64 examples.
  B (baseline) = ordinary least squares.   A (method) = ridge (shrinkage), fixed lambda.
Metric: held-out predictive negative log-likelihood (NLL) under a Gaussian, in NATS.
  err_* = mean test NLL (nats);  delta = (err_B - err_A)/err_B  (dimensionless fraction).
We also record abs_nats = err_B - err_A (NATS) - the quantity the RESULTS walkback shows being
unit-confused (nats reported as bits) to manufacture a second, false claim.

Deterministic: fixed seeds; raw per-seed numbers are rounded before hashing so the content hash is
reproducible across machines. Run:  uv run pilot/run.py --out raw.json
"""
from __future__ import annotations
import argparse, hashlib, json, math
import numpy as np

LAMBDA = 10.0          # ridge strength (pre-fixed, part of method A)
N_TRAIN, N_TEST, D = 64, 4000, 40
N_SEEDS = 200
N_NONZERO = 8          # true sparse support
NOISE_SD = 1.0


def one_seed(seed: int, null: bool = False) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    beta = np.zeros(D); idx = rng.choice(D, N_NONZERO, replace=False); beta[idx] = rng.normal(0, 1, N_NONZERO)
    Xtr = rng.normal(0, 1, (N_TRAIN, D)); ytr = Xtr @ beta + rng.normal(0, NOISE_SD, N_TRAIN)
    Xte = rng.normal(0, 1, (N_TEST, D)); yte = Xte @ beta + rng.normal(0, NOISE_SD, N_TEST)

    # B: OLS via lstsq (n=64 > d=40, full column rank -> unique overdetermined solution).
    # A: ridge (shrinkage). With n only modestly above d and a sparse signal, OLS is high-variance;
    # ridge lowers test NLL by variance reduction. That gap is the demo effect.
    bB, *_ = np.linalg.lstsq(Xtr, ytr, rcond=None)
    bA = np.linalg.solve(Xtr.T @ Xtr + LAMBDA * np.eye(D), Xtr.T @ ytr)

    def nll(b, Xt, yt):
        rtr = ytr - Xtr @ b
        s2 = max(float(rtr @ rtr) / N_TRAIN, 1e-6)          # plug-in train residual variance (nats need a scale)
        rte = yt - Xt @ b
        return 0.5 * math.log(2 * math.pi * s2) + float(rte @ rte) / (2 * s2 * len(yt))

    if null:
        # NEGATIVE CONTROL: arm A is the SAME OLS model as B, scored on an independent test draw.
        # No real advantage -> per-seed delta is symmetric noise about 0 -> the gate must FAIL.
        Xte2 = rng.normal(0, 1, (N_TEST, D)); yte2 = Xte2 @ beta + rng.normal(0, NOISE_SD, N_TEST)
        return nll(bB, Xte2, yte2), nll(bB, Xte, yte)
    return nll(bA, Xte, yte), nll(bB, Xte, yte)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="raw.json")
    ap.add_argument("--null", action="store_true",
                    help="negative control: both arms are the same OLS model (no real effect); the gate should FAIL")
    a = ap.parse_args()

    errA = np.empty(N_SEEDS); errB = np.empty(N_SEEDS)
    for i in range(N_SEEDS):
        errA[i], errB[i] = one_seed(1000 + i, null=a.null)
    delta = (errB - errA) / errB
    abs_nats = errB - errA

    # content hash over rounded raw arrays -> reproducible across machines
    payload = np.round(np.stack([errA, errB]), 6).tobytes()
    digest = hashlib.sha256(payload).hexdigest()

    out = {
        "config": {"lambda": LAMBDA, "n_train": N_TRAIN, "n_test": N_TEST, "d": D,
                    "n_seeds": N_SEEDS, "n_nonzero": N_NONZERO, "noise_sd": NOISE_SD,
                    "null_control": a.null},
        "units": {"err": "nats", "delta": "dimensionless_fraction", "abs_nats": "nats"},
        "per_seed": {"err_A": errA.round(6).tolist(), "err_B": errB.round(6).tolist(),
                      "delta": delta.round(6).tolist(), "abs_nats": abs_nats.round(6).tolist()},
        "summary": {"mean_err_A": float(errA.mean()), "mean_err_B": float(errB.mean()),
                     "mean_delta": float(delta.mean()), "mean_abs_nats": float(abs_nats.mean()),
                     "seeds_A_better": int((errA < errB).sum())},
        "content_sha256": digest,
    }
    json.dump(out, open(a.out, "w"), indent=2)
    s = out["summary"]
    print(f"seeds={N_SEEDS}  A_better={s['seeds_A_better']}/{N_SEEDS}  "
          f"mean_delta={s['mean_delta']:.4f} (dimensionless)  mean_abs={s['mean_abs_nats']:.4f} nats")
    print(f"content_sha256={digest}")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
