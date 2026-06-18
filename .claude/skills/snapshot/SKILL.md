---
name: snapshot
description: Produce a short, plain-English status of the whole program - what's solid, what's new since the canonical state, honest negatives/obstructions, and open/next - using fast parallel reads. Explains results in lay terms, never just citing gate names. Use when the user says "/snapshot", "where do things stand", or "current status".
---

# /snapshot - plain-English status of the program

Goal: a short, **simple-English** briefing of the latest state. The reader may not be technical -
explain what results *mean*, don't just cite them.

## Step 1 - Orient (fast, yourself)
Read the canonical surfaces first and note their dates:
- `CURRENT_STATE.md` - live claims, withdrawn register, adoptions, open work.
- `Home.md` - the topic index.
Then find what changed **after** the canonical state's date (recent commits / newest files) - those
are the freshest results that may not be folded in yet. Flag them as not-yet-canonical.

## Step 2 - Fan out (parallel reads)
Launch read-only agents concurrently, each with a tight scope (experiments, topic pages, and each
repo listed in `REPOS.md`), each returning a **plain-English** summary: what was tested, the result,
and whether it's a positive, a negative, an obstruction, or still open. Scale the fleet to the ask.

## Step 3 - Synthesize
Write the briefing:
- **Headline** - the single most important state right now.
- **What's solid** - cleared-the-checklist claims, in lay terms (what it means).
- **What's new since canonical state** - clearly marked if not yet folded in.
- **Honest negatives & obstructions** - reported plainly, never buried.
- **Open / next** - the live questions.

Rules: plain language (gloss any term on first use); never repeat a **withdrawn** number as if live;
date the snapshot and name sources; separate "proven / replicated / toy-scope / open" honestly.
