# Ownership

Manifest of who/what owns which area. The `/mediate` skill consults this before touching anything,
so parallel threads/sessions don't collide. Keep it current.

## How it's read
- **In-bounds** (the active session owns the area) → proceed.
- **Out-of-bounds** (another thread owns it) → do **not** halt-and-wait and do **not** silently
  overstep. Notify the owner with what/why/diff/risk and let *them* judge. (See `.claude/skills/mediate`.)

## Areas
| Area / path | Owner | Notes |
|-------------|-------|-------|
| `experiments/exp0_demo/` | _(unassigned)_ | the demo; safe to edit |
| `experiments/<your-exp>/` | _(thread/session name)_ | one owner per active experiment |
| `CURRENT_STATE.md` | shared | additive edits only; pull before editing |
| `OPERATING_GUIDE.md` | shared | additive, episode-anchored amendments only |
| `paper/` or `manuscript/` | _(assign explicitly)_ | freeze before external review |

## Conventions
- A session may be *renamed* to declare ownership ("this session owns exp-foo").
- If ownership is genuinely indeterminate, treat the work as out-of-bounds and mediate.
- Owner of last resort: the human maintainer.
