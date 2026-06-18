---
name: add-repo
description: Register a git checkout into this Atlas instance's repo registry (REPOS.md) so /mediate, /snapshot, and cross-repo work know about it. Use when the user says "/add-repo <path>", "register this repo", or "add <path> to the repos Atlas knows about". Takes a path to a git checkout (defaults to the current directory).
---

# /add-repo <path> - register a repo into the Atlas hub

Add a git checkout to `REPOS.md`, the registry of repos this instance governs. Idempotent: if the
repo is already listed, update its row instead of duplicating.

## Steps
1. **Resolve the path** from the argument (default: current directory if none given). Confirm it is a
   git checkout: `git -C <path> rev-parse --is-inside-work-tree`. If not, report and stop.
2. **Gather metadata** (run from `<path>`):
   - `toplevel` = `git -C <path> rev-parse --show-toplevel` (use as the canonical path).
   - `name` = basename of toplevel, or the remote repo name if clearer.
   - `remote` = `git -C <path> remote get-url origin` (use `local-only` if there is no remote).
   - `default_branch` = `git -C <path> symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null` (fallback: the current branch from `git -C <path> branch --show-current`).
   - `role/notes` = ask the user briefly, or infer from the repo README first line.
3. **Write the row.** If `REPOS.md` is missing, create it with the header + table from the template.
   If a row already exists for this toplevel path or remote, **update** it; otherwise **append** a new
   row. Keep the table columns: Name, Path, Remote, Default branch, Role / notes.
4. **Privacy check (public instance).** If this Atlas instance is a public repo and the path is a
   sensitive internal location, do not commit it without the user's ok: offer to record it in a
   gitignored `REPOS.local.md` instead, or store only the remote + a relative name.
5. **Sync knowledge.** Run the `/sync-repo-knowledge` procedure on the toplevel path to populate
   `wiki/topics/<name>.md` with a knowledge page (purpose, structure, state, recent activity).
6. **Report** what was added or updated (name, path, remote, branch) and that knowledge was synced.
   Commit only if asked, and keep the message clear (no agent trailer).

## Notes
- This only registers the repo; it does not clone, modify, or take ownership of it.
- Ownership of areas within a repo is tracked separately in `OWNERSHIP.md` and gated by `/mediate`.
