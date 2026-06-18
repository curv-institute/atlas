# Repositories

The repos this Atlas instance governs. `/add-repo <path>` registers a git checkout here; `/mediate`,
`/snapshot`, and any cross-repo work consult this list. One row per repo.

| Name | Path | Remote | Default branch | Role / notes |
|------|------|--------|----------------|--------------|
| atlas | `.` | https://github.com/curv-institute/atlas | main | this hub (the template itself) |

> Note for a public instance: absolute local paths reveal your directory layout. If that is
> sensitive, keep private registrations in a gitignored `REPOS.local.md` instead of committing them
> here, or record only the remote and a relative name.
