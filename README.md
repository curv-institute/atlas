# Open Research Skeleton

A reusable repository skeleton for **rigorous, agent-assisted research** — the kind where a
result only becomes a claim after it survives an attempt to kill it. It encodes a working method
into files an AI coding agent (e.g. Claude Code) and a human can both operate: a living operating
guide, a canonical state surface, preregistration + verification gates, adversarial review, and a
typed memory of lessons learned.

It ships with a **runnable demo experiment** (`experiments/exp0_demo`, numpy-only, runs in seconds)
that walks the whole lifecycle — preregister → run → gate → adversarial review catches a planted
overclaim → additive walkback — so you can see the method work end to end before adopting it.

> Distilled from the working practice of the **Curv Institute** research program and generalized
> for reuse. See `OPERATING_GUIDE.md` for the method and `CONTRIBUTING.md` for the discipline.

## The idea in one sentence
Rather be right than impressive: lead with the instrument, pre-state the threshold, verify
adversarially, and record everything additively — withdrawals stay on the page.

## What's here
| Path | What it is |
|------|------------|
| `OPERATING_GUIDE.md` | The method: result lifecycle, claim hygiene, confound catalog, pre-claim checklist, amendment protocol. **Living document.** |
| `CURRENT_STATE.md` | The single canonical state surface: live claims, the **withdrawn-claims register**, adoptions/closures. |
| `Home.md` | Index of every topic/wiki page. |
| `OWNERSHIP.md` | Who/what owns which area — consulted by the `/mediate` skill. |
| `.claude/skills/` | Agent workflows: `/research`, `/council`, `/optimize`, `/snapshot`, `/mediate`. |
| `wiki/topics/` | Hand-edited topic pages (no build pipeline; the files *are* the wiki). |
| `experiments/exp0_demo/` | A runnable toy that exercises the full lifecycle. |
| `memory/` | Typed, persistent lessons (`user` / `feedback` / `project` / `reference`) + index. |
| `fleet/` | *Optional* multi-machine layer: a sanitized inventory + infra discovery discipline. |

## Quick start
```bash
# 1. See the method work end to end (needs `uv`: https://docs.astral.sh/uv/)
cd experiments/exp0_demo
uv run pilot/run.py --out raw.json          # deterministic; writes raw results + a content hash
uv run gate.py --raw raw.json --out gate_evaluation.json   # evaluates pre-stated thresholds → PASS/FAIL
cat RESULTS_demo.md                          # the verdict, and the worked overclaim→walkback

# 2. Adopt it for your own work
#    - rename the repo; empty CURRENT_STATE.md to your starting state
#    - write your first PREREGISTRATION.md before you run anything
#    - drive it with an agent: open in Claude Code and run /research on your task list
```

## How to adopt (5 steps)
1. **Fork & rename.** Replace this README's specifics; keep `OPERATING_GUIDE.md` and the skills.
2. **Seed `CURRENT_STATE.md`** with what you currently believe and what's still open.
3. **Preregister before running.** Copy `experiments/exp0_demo/PREREGISTRATION.md` as your template; freeze it (commit, optionally OpenTimestamp) *before* collecting data.
4. **Gate, then review.** Run your evaluator to a `gate_evaluation.json`; then run `/council` to try to refute the result before you write it down as a claim.
5. **Record additively.** Wins and withdrawals both stay in `CURRENT_STATE.md`. Never delete history; supersede it.

## License
Code and docs: see `LICENSE` (MIT). Please keep the attribution line above when reusing the method.
