# Style: no AI tells

Atlas docs and code avoid the typographic and verbal tics that mark machine-generated text. The
lintable rules (A, B, C) are enforced by `tools/style-check.sh`; run it before committing (it is CI
and pre-commit friendly). Group D is guidance.

## A. Typography (enforced)
- No em dash (U+2014). Use a hyphen, colon, comma, parentheses, or rephrase.
- No en dash (U+2013) in prose. Write ranges as "1 to 3" or "1-3".
- No curly / smart quotes (U+201C, U+201D, U+2018, U+2019). Use straight quotes.
- No ellipsis character (U+2026). Use three dots: "...".
- No emoji or decorative marks (check marks, rockets, sparkles).
- No non-breaking or invisible spaces (U+00A0 and friends).

## B. Diction blocklist (enforced)
Avoid these buzzwords: delve, leverage, seamless, elevate, underscore (as a verb), testament,
tapestry, realm, showcase, pivotal, supercharge, holistic, streamline, game-changer, cutting-edge,
state-of-the-art, foster, empower.

Soft (not gated, but avoid as filler; genuine technical uses are fine): robust, comprehensive,
crucial, harness, boast.

## C. Constructions (enforced)
Avoid: "not only X but also Y"; "it isn't just X, it's Y"; "it's worth noting"; "it's important to
note"; "in conclusion"; "in today's ... world"; "let's dive in" / "dive into"; "needless to say";
"at the end of the day".

## D. Formatting (guidance)
- Sentence-case headings, not Title Case.
- Do not bold reflexively; bold only load-bearing terms.
- Lead with the point; no throat-clearing openers.
- Use rule-of-three sparingly, not as a reflex.

## Running the gate
```bash
tools/style-check.sh        # exit 0 = clean, 1 = violations
```
Wire it into CI or a pre-commit hook. Soft words (above) are intentionally not gated to avoid false
positives on legitimate technical writing; reviewers catch filler uses by eye.
