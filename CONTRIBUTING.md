# Contributing — the record discipline

This repo treats its own history the way it treats results: **additive and honest.**

## Git
- Small, frequent commits with descriptive messages. Commit (or push) only what's asked.
- Direct-to-main is fine for a solo/small program; use the default branch deliberately.
- Attribute agent-assisted commits, e.g. a trailer:
  `Co-Authored-By: <your agent/model> <noreply@example.com>`
- In shared clones, `pull --rebase` before editing; never blanket `git add -A` over another thread's
  staged work — stage only the files you changed.

## The record
- **Never delete history.** Wrong results get a *supersession banner* and stay on the page; the
  withdrawn-claims register in `CURRENT_STATE.md` keeps the old number visible with the reason.
- **Evidence files are write-once.** Preregistration and timestamped/attested files stay byte-verbatim
  (editing breaks provenance and reads as tampering). Correct via a new file + a banner, not an edit.
- **Reproducibility ≠ preregistration.** Clone-and-run reproducibility and blind, timestamped
  preregistration are *distinct* guarantees — never conflate them.

## Verification hygiene
- Run gated/verification commands from a clean shell with an explicit absolute cwd.
- Confirm the gate/output file is **non-empty** before reporting PASS (a subshell/cwd reset can
  silently empty it).
- Re-derive load-bearing numbers from the raw artifact by an independent route before claiming them.

## Adding a lesson
When something fools you, encode it where it will fire next time:
- A new confound → one line in `OPERATING_GUIDE.md` §3 (rule + dated episode).
- A behavioral lesson → a `memory/` file (see `memory/MEMORY.md`).
