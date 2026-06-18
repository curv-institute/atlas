# Current State

The single canonical state surface. If a wiki/topic page disagrees with this file, **this file
wins** — point stale pages here. Update it *as work lands*, not only at the end.

_As of: YYYY-MM-DD_

## 1. Live claims (cleared the OPERATING_GUIDE §6 checklist)
| Claim | Scope / caveats | Evidence (artifact + commit) | Date |
|-------|-----------------|------------------------------|------|
| _(example)_ Demo effect A>B holds in the toy regime | toy synthetic data only; not external | `experiments/exp0_demo/gate_evaluation.json` @ `<commit>` | YYYY-MM-DD |

## 2. Candidates (measured, not yet cleared)
| Candidate | What's missing before it's a claim | Owner |
|-----------|------------------------------------|-------|
| _(example)_ … | adversarial review pending | … |

## 3. Withdrawn-claims register (NEVER delete — supersede)
Record anything retracted or reframed, with the reason. Past numbers stay visible so the record is
honest and the lesson is reusable.

| Withdrawn claim | Why withdrawn | Replaced by | Date |
|-----------------|---------------|-------------|------|
| _(example)_ "A beats B by 3×" | unit confound (nats/token reported as bits/byte) inflated the effect ~3× | corrected effect within noise; see RESULTS_demo.md | YYYY-MM-DD |

## 4. Adoptions / closures (settled definitions & decisions)
- _(example)_ Metric M is defined as … (adopted YYYY-MM-DD).

## 5. Open questions / live work
- _(example)_ Does the effect survive at higher resolution? (queued)
