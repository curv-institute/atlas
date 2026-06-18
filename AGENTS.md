# AGENTS.md — Atlas (agent entry point)

This is the **canonical instruction file for any AI coding agent** working in this repo (Codex,
Claude Code, Gemini CLI, Cursor, opencode, Aider, …). It's plain markdown — read it and follow it.
`CLAUDE.md`, `GEMINI.md`, and `.cursor/rules/` all redirect here so every agent gets the same rules.

Atlas is a documented command surface for rigorous, agent-assisted **research and development** — a
hub that maps and governs many concurrent repos/work areas, where a result or change only counts
after it survives an attempt to break it.

## Orient first (read these)
1. `OPERATING_GUIDE.md` — the method: lifecycle, claim hygiene, confound catalog, pre-claim checklist.
2. `CURRENT_STATE.md` — the single canonical state surface (live claims, withdrawn register, open work). **If anything disagrees with this file, it wins.**
3. `OWNERSHIP.md` — who/what owns which area (consulted before you touch anything — see Workflows § `mediate`).
4. `Home.md` — index of topics/experiments.

## The loop (research *or* development)
Scope → cheap pilot → **preregister** (freeze the bar, with units, before the run) → build/run →
**gate** (an evaluator emits the verdict to a file) → **adversarial review** (try to refute it) →
**record additively** in `CURRENT_STATE.md`. For dev: spec → build → test/verify → review → record.
Pre-state the bar; verify adversarially; record everything additively (withdrawals stay on the page).

## Workflows (portable procedures)
Each is a self-contained procedure in `.claude/skills/<name>/SKILL.md` — **plain markdown any agent
can read and follow.** Claude Code also exposes them as slash commands (`/research` etc.); other
agents: when the user asks for one (or the situation matches), open the file and follow its steps.

| Workflow | Procedure file | Use when |
|----------|----------------|----------|
| **atlas-setup** (alias **onboard**) | `.claude/skills/atlas-setup/SKILL.md` | first-time setup, or change project settings (name, ownership, agents, fleet, remote) |
| **research** | `.claude/skills/research/SKILL.md` | work a task end-to-end through the lifecycle |
| **council**  | `.claude/skills/council/SKILL.md`  | adversarially verify a result / vet a plan / go-no-go |
| **optimize** | `.claude/skills/optimize/SKILL.md` | make a slow/expensive run faster *without changing results* |
| **snapshot** | `.claude/skills/snapshot/SKILL.md` | plain-English status of the whole program |
| **mediate**  | `.claude/skills/mediate/SKILL.md`  | before touching work another thread/area may own |

## Standing rules (all agents)
- **Ownership gate.** Before starting/redoing/prepping work that another thread/area may own, run the
  `mediate` procedure: in-bounds → proceed; out-of-bounds → don't halt-and-wait and don't silently
  overstep — notify the owner with what/why/diff/risk and let them judge (human is fallback owner).
- **Claims vs candidates.** A result is a *candidate* until it clears `OPERATING_GUIDE.md` §6. Say so.
  Name the measured quantity exactly; state N, units, CI. Pre-state thresholds with units.
- **Verification hygiene.** Run gated/verification commands from a clean shell with an explicit
  absolute cwd; confirm the gate/output file is **non-empty** before reporting PASS. Re-derive
  load-bearing numbers from the raw artifact independently.
- **Record additively.** Never delete history; supersede with a banner. Wrong results stay visible in
  the withdrawn register. Evidence/preregistration files are write-once (don't edit; correct via a new file).
- **Conciseness.** Don't flood context with raw tool output — pipe big output to a file and summarize.
- **Git.** Small commits; `pull --rebase` in shared clones; stage only what you changed; attribute
  agent-assisted commits with a trailer.

## Run the demo (any agent / human)
```bash
cd experiments/exp0_demo
uv run pilot/run.py --out raw.json                          # deterministic; raw results + content hash
uv run gate.py --raw raw.json --out gate_evaluation.json    # pre-stated thresholds → PASS/FAIL
cat RESULTS_demo.md                                         # verdict + a worked overclaim→walkback
```

## Optional: multi-machine layer
`fleet/` holds an optional inventory (`fleet.yaml`, copy from `fleet.example.yaml`) + discovery
discipline for running across several machines. See `fleet/AGENTS.md`.
