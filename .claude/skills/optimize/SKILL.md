---
name: optimize
description: Make a long/expensive run faster WITHOUT changing the science. Estimate cost from a measured slice, find the real bottleneck by measurement (never guessing), apply the highest-payoff lever (batch width, vectorize, GPU, parallelism, persist/reload), and PROVE result-invariance before/after. Use when the user says "/optimize", "make this faster", "this run is too slow/expensive", or when /research hits a >=2hr / large-compute task.
---

# /optimize — faster, same science

Speed up an expensive run while **proving the result does not change**.

## Procedure
1. **Measure a slice.** Time a small representative slice; extrapolate the full cost. Report the
   estimate before doing anything big.
2. **Find the bottleneck by measurement** — profile / time the stages. Never guess where the time goes.
3. **Apply the highest-payoff lever** for the measured bottleneck:
   - batch width (process many items at once instead of a Python loop),
   - vectorize / use the right BLAS/GPU,
   - parallelize across cores/nodes (mind memory-bandwidth limits — more cores ≠ linear speedup on
     bandwidth-bound kernels),
   - persist/reload expensive intermediates instead of recomputing.
4. **Prove invariance.** Run the old and new paths on the same seed/slice and show the outputs match
   (bit-for-bit, or within a stated tolerance). An optimization that changes the numbers is a
   *different experiment*, not a speedup — stop and flag it.
5. **Record the win** (what changed, the speedup, the invariance check) so it's reusable.

## Rule
Never trade correctness for speed silently. If a lever changes results, it is out of scope for
`/optimize` — surface it as a science change for explicit decision.
