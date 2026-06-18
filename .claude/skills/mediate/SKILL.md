---
name: mediate
description: Ownership-aware gate for work that may belong to another thread/session. Decide in-bounds vs out-of-bounds; if in-bounds, allow; if out-of-bounds, do NOT halt-and-wait and do NOT just proceed — notify the current owner with full details and let them judge whether the work should be done. Use when about to start/redo/prep work, edit files, or run experiments another thread may own, or when the user says "/mediate", "who owns this", "is this in bounds".
---

# /mediate — ownership-aware work gating (route, don't halt)

Before doing work that may belong to another thread/session, decide **in-bounds** (this session owns
it) vs **out-of-bounds** (another thread owns it). The point is to **not block on the human** and
**not silently overstep** — for out-of-bounds work, notify the *owner* with enough detail to decide.

## Step 1 — Identify ownership
Consult, in order: `OWNERSHIP.md` → any session-rename declaration ("this session owns X") →
repo/dir conventions (experiment dirs, manuscript, shared surfaces). Classify the target work as
**IN-BOUNDS**, **SHARED/UNOWNED**, or **OUT-OF-BOUNDS**. If genuinely indeterminate → treat as
OUT-OF-BOUNDS.

## Step 2 — Route
- **IN-BOUNDS** → allow; proceed with normal rigor.
- **SHARED/UNOWNED** → read-only / low-risk additive edits fine; anything destructive or that another
  session is building on → treat as OUT-OF-BOUNDS.
- **OUT-OF-BOUNDS** → do **not** do the work. File a mediation request (Step 3); continue with
  in-bounds work meanwhile (don't idle).

## Step 3 — Mediation request (out-of-bounds)
Write what the owner needs to decide without re-deriving context:
- **What** (specific change/run, exact paths) · **Why** · **The change** (diff/command/steps so "yes"
  is one action) · **Blast radius / reversibility** · **Recommended verdict** (your honest call + reason).
Route it to the owner's channel (a decisions inbox if you have one, else a `MEDIATION/REQ-<date>-<slug>.md`
note + a notification). **Owner unknown/unreachable → the human maintainer is the fallback owner.**
Do not proceed without explicit approval.

## Step 4 — Record
Log the verdict (owner + decision + date). If approved, do the work and attribute it to the request.
If declined/deferred, leave the area untouched and note it.

## Contract
In-bounds → allow. Out-of-bounds → notify the owner with what/why/diff/risk/recommendation and let
**them** judge. Never halt-and-wait on the human for an owner's call; never silently overstep.
