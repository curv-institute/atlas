---
name: research
description: Autonomously work a research task end-to-end following the operating-guide lifecycle — scope, cheap pilot first, preregister, build/run, gate, then convene /council to verify — looping on the verdict (fix→re-loop, solid→record & next, obstruction/refuted→document & next). Use when the user says "/research", "work this task autonomously", or hands over a goal/backlog. Honors OPERATING_GUIDE.md and OWNERSHIP.md.
---

# /research — work a task end-to-end with the lifecycle

Drive a research task through the `OPERATING_GUIDE.md` §1 lifecycle, self-paced and resumable. The
bias is rigor over speed: a candidate only becomes a claim after it survives `/council`.

## Per task
1. **Check ownership** — run `/mediate` first if the task may touch another thread's area (`OWNERSHIP.md`).
2. **Scope** — state the question and what would falsify it.
3. **Cheap pilot** — the smallest run that could show the effect or kill the idea. If it would take
   hours / heavy compute, stop and confirm (and consider `/optimize`).
4. **Preregister** — freeze hypothesis, metric, **units**, N, and the pass/fail threshold in a
   committed `PREREGISTRATION.md` *before* the full run.
5. **Build & run** — reproducible from a named artifact (code + data + commit). Deterministic seeds.
6. **Gate** — an evaluator computes the pre-stated verdict to `gate_evaluation.json` (once-only).
7. **`/council`** — adversarially verify before recording. Re-derive load-bearing numbers independently.
8. **Record** in `CURRENT_STATE.md`, additively:
   - **Solid** → live claim (with scope + artifact + commit). Next task.
   - **Fix needed** → fix and re-loop from the gate.
   - **Obstruction / refuted** → document the obstruction (a valid outcome) and move on.

## Discipline
- Never run the full/expensive job before the pilot + prereg.
- An API/tooling error is an interruption, never evidence — resume the undone work, don't conclude.
- Keep a short ledger of task → verdict → artifact so the loop is resumable.
- Pipe large run output to files; report summaries (don't flood context).
