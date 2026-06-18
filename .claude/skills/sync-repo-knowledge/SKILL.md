---
name: sync-repo-knowledge
description: Read a repo and populate this hub's wiki with a knowledge page about it (purpose, structure, key docs, current state, recent activity, open items). Use when the user says "/sync-repo-knowledge <path>", "sync knowledge from <repo>", or "refresh what Atlas knows about <repo>". Idempotent: re-running refreshes the generated section and leaves hand-edited notes intact. /add-repo calls this after registering a repo.
---

# /sync-repo-knowledge <path> - populate wiki knowledge from a repo

Read a git checkout and write or refresh a topic page at `wiki/topics/<repo-name>.md` summarizing
what this hub should know about it. Idempotent and non-destructive: regenerate only the marked
generated zone; never overwrite hand-edited notes. This summarizes a repo, it does not vendor it in.

## Steps
1. Resolve `<path>` (default: current directory). Confirm it is a git checkout
   (`git -C <path> rev-parse --is-inside-work-tree`); if not, report and stop.
2. `name` = basename of `git -C <path> rev-parse --show-toplevel` (the same canonical basename rule
   as `/add-repo`, so the page filename matches the REPOS row exactly). Target page:
   `wiki/topics/<name>.md`.
3. **Gather knowledge** (read-only; do not modify the source repo):
   - Purpose: the first paragraph of the repo README (README.md / .rst / docs index).
   - Structure: top-level dirs and their role (one line each); key entry points.
   - Canonical state: any `CURRENT_STATE` / `STATUS` / `CHANGELOG` / `ROADMAP` / docs index in the repo.
   - Notable docs: `AGENTS.md` / `CONTRIBUTING` / design notes (one line each).
   - Recent activity: `git -C <path> log -10 --format='%h %ad %s' --date=short`.
   - Open items: counts of `TODO` / `FIXME` / `XXX`; any open-questions or issues docs.
   - Provenance: remote (`git remote get-url origin`), default branch, current HEAD commit.
4. **Write the page in two zones:**
   - A generated zone between `<!-- atlas:generated:start -->` and `<!-- atlas:generated:end -->`
     holding the gathered knowledge plus a provenance line (repo path, remote, synced-at HEAD).
     On re-run, replace ONLY this zone, leaving everything else untouched.
   - A `## Notes (hand-edited)` heading below the markers, created once and never overwritten.
5. **Link it:** add the page under Topics in `Home.md`, and set the repo's `REPOS.md` row Role/notes
   to point at `wiki/topics/<name>.md`, if not already linked.
6. Keep it factual and concise; obey `STYLE.md` (no AI tells). Report what was written. Commit only if asked.

## Notes
- Provenance: the generated zone records the source HEAD so staleness is visible. Re-run to refresh.
- Privacy: for a public Atlas instance, do not paste sensitive internal content into the wiki.
  Summarize at a safe level, or keep the page in a gitignored location.
