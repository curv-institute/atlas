#!/usr/bin/env bash
# Atlas style gate: bans common AI-tell typography, diction, and constructions (see STYLE.md).
# Usage: tools/style-check.sh   -> exit 0 = clean, 1 = violations. CI / pre-commit friendly.
set -uo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)"

# Tracked text files, excluding this script and the style doc (which name the banned items).
ALL=$(git ls-files '*.md' '*.mdc' '*.txt' '*.py' '*.yaml' '*.yml' '*.sh' 'LICENSE' 2>/dev/null \
  | grep -vxE 'STYLE\.md|tools/style-check\.sh' || true)
PROSE=$(printf '%s\n' "$ALL" | grep -E '\.(md|mdc|txt)$' || true)

fail=0
flag() {  # label  regex  filelist  [extra grep flag, e.g. -i]
  local label="$1" re="$2" list="$3" gf="${4:-}"
  [ -z "$list" ] && return 0
  local hits
  hits=$(grep ${gf:+$gf} -nP "$re" -- $list 2>/dev/null || true)
  if [ -n "$hits" ]; then printf '\n[%s]\n%s\n' "$label" "$hits"; fail=1; fi
}

# A. Typography (all files)
flag "em dash (U+2014)"        '\x{2014}' "$ALL"
flag "en dash (U+2013)"        '\x{2013}' "$ALL"
flag "smart quotes"            '[\x{201C}\x{201D}\x{2018}\x{2019}]' "$ALL"
flag "ellipsis char (U+2026)"  '\x{2026}' "$ALL"
flag "non-breaking space"      '\x{00A0}' "$ALL"
flag "emoji / decorative"      '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2705}\x{2728}\x{2B50}\x{2B55}\x{FE0F}]' "$ALL"

# B. Diction blocklist (prose only, case-insensitive)
flag "ai-diction" '\b(delv(e|ing)|leverage[sd]?|leveraging|seamless(ly)?|elevate[sd]?|underscore[sd]?|testament|tapestry|realm|showcas(e|es|ed|ing)|pivotal|supercharg(e|ed|ing)|holistic|streamlin(e|es|ed|ing)|game-?changer|cutting-edge|state-of-the-art|foster(s|ed|ing)?|empower(s|ed|ing|ment)?)\b' "$PROSE" -i

# C. Constructions (prose only, case-insensitive)
flag "ai-construction" "\b(but also|worth noting|important to note|in conclusion|let's dive|dive (in|into)|isn't just|is not just|in today's|needless to say|at the end of the day)\b" "$PROSE" -i

if [ "$fail" -ne 0 ]; then
  echo
  echo "Style check FAILED (see STYLE.md). Rephrase the flagged lines."
  exit 1
fi
echo "Style check passed: no banned AI-tells."
