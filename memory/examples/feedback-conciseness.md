---
name: response-conciseness
description: "Keep responses tight; never flood context with raw tool output - pipe big output to a file and summarize"
metadata:
  type: feedback
---

Never dump large command output into a response. For sweeps, scans, log tails, or big diffs: write
to a file (e.g. `/tmp/…`), then report only the lines that matter + counts.

**Why:** large raw output burns the output-token ceiling and the context window, and reads as noise.
In long sessions context is precious.

**How to apply:** redirect spew-prone commands to a file and `grep`/summarize; lead with the answer;
a verdict + the few load-bearing numbers beats a wall of text. (Example memory - adapt or delete.)
