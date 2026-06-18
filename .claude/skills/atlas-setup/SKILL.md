---
name: atlas-setup
description: Guided setup/reconfigure wizard for an Atlas-based project - walks the user through naming, canonical state, ownership, which CLI agents + agent files, the optional fleet layer, memory seeding, the first experiment, and git/remote/attribution, confirming before anything destructive or outward-facing. Use when the user says "/atlas-setup", "/onboard", "set up this project", "configure Atlas", or "change the project settings". Re-runnable (idempotent) to adjust settings later, not just first-time.
---

# /atlas-setup  (alias: /onboard) - guided project setup & reconfigure

Walk the user through making this Atlas template *their* project - or changing settings later. Ask
**one focused question at a time** (or small grouped sets), apply each change, confirm before
anything destructive (deleting files, renaming) or outward-facing (creating/pushing a remote), and
finish with a summary + a single commit. Re-runnable: if a setting is already configured, show its
current value and offer to change it.

Start by telling the user what this will do and that nothing irreversible happens without a confirm.
Then go section by section; skip any the user says is already fine.

## 1. Identity
- Project **name** → update `README.md` title + intro, and propose renaming the repo directory
  (confirm before `git mv`/`mv`).
- **Domain**: research / development / both → adjust the README framing wording.
- **Attribution**: keep the upstream "distilled from … Atlas / Curv Institute" credit (the MIT
  license asks reusers to retain it) and add the user's own org/author line.

## 2. Canonical state (`CURRENT_STATE.md`)
- Set the `As of:` date.
- Seed §1 live claims, §5 open questions with the user's real starting state; clear the example rows.
- Leave §3 withdrawn-claims register empty (it fills as work is retracted).

## 3. Ownership (`OWNERSHIP.md`)
- Fill the areas table: who/what owns which repo/experiment/surface (one owner per active area).
- Confirm the **mediation channel** for out-of-bounds requests (a decisions inbox dir, or the default
  `MEDIATION/REQ-*.md` notes) and who the **fallback owner** is.

## 4. Agents & agent files
- Ask which CLI agents the team uses (Claude Code, Codex, Gemini, Cursor, Aider, …).
- `AGENTS.md` is canonical for all; confirm `CLAUDE.md` / `GEMINI.md` / `.cursor/rules/` redirects are
  present for the ones in use (add any missing). Review `.claude/settings.json` defaults.

## 5. Fleet layer (optional, `fleet/`)
- Single machine? → offer to remove `fleet/` (confirm) and drop its mention from README/AGENTS.
- Multi-machine? → `cp fleet/fleet.example.yaml fleet/fleet.yaml` and help fill it. **Remind: real
  IPs/MACs go only in `fleet.yaml` (gitignored), never in the committed example.**

## 6. Memory (`memory/`)
- Seed a real **maintainer profile** (`user`) and any standing **feedback** (how they like to work).
- Clear/replace the `memory/examples/*` files; keep `MEMORY.md` as the index (one line per memory).

## 7. First experiment
- Keep `experiments/exp0_demo` as a reference, or archive it.
- Scaffold the user's first experiment dir from the demo's shape: `PREREGISTRATION.md` (freeze before
  running), `pilot/run.py`, `gate.py`, `RESULTS_*.md`. Don't run anything heavy without confirmation.

## 8. Git, remote, license
- Set repo-local `user.email` / `user.name`.
- Confirm `LICENSE` + attribution; review `.gitignore`.
- **Remote (outward-facing - confirm explicitly):** offer to create a GitHub repo (`gh repo create`)
  and push; ask public vs private-first and the org/account. Do NOT push without an explicit yes.

## 9. Confirm & commit
- Summarize every change made. Run the demo (`uv run …`) if experiments were touched, to confirm the
  repo still works. Commit with a clear message + attribution trailer. Leave any push to §8's confirm.

## Rules
- One change at a time; show current value before changing it; never delete or push without a confirm.
- Keep responses tight; pipe any large output to a file and summarize.
