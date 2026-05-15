# SkillsMP — Source Reference

## URL Pattern

```
https://skillsmp.com/skills/<slug>
```

The slug is the full page identifier, e.g.:
`tech-leads-club-agent-skills-packages-skills-catalog-skills-development-tlc-spec-driven-skill-md`

## Step 1 — Resolve slug to skill metadata via API

```bash
curl -s "https://skillsmp.com/api/v1/skills/search?q=<search-term>" \
  -H "Authorization: Bearer <api_key>"
```

**Note:** The slug from the URL is NOT the search query. Extract a short keyword from it (e.g. `tlc-spec-driven`) and search. Then find the matching object by comparing `id` field against the original slug.

**Alternative:** Use the native `web_fetch` tool to analyze the source page if direct API search encounters Cloudflare issues.

Response structure:
```json
{
  "data": {
    "skills": [
      {
        "id": "<slug>",
        "name": "...",
        "githubUrl": "https://github.com/<owner>/<repo>/tree/<branch>/<path>",
        "stars": 0
      }
    ]
  }
}
```

Match by: `skill.id === slug-from-url`

## Step 2 — Resolve githubUrl to file list

`githubUrl` points to a GitHub tree page, not a raw file. Convert it to a GitHub API contents call:

```
https://github.com/<owner>/<repo>/tree/<branch>/<path>
→
https://api.github.com/repos/<owner>/<repo>/contents/<path>
```

For subdirectories, recurse: if `type === "dir"`, make another contents API call for that path.

Each file object contains:
- `name` — filename
- `type` — "file" or "dir"
- `download_url` — direct URL to raw file content (use this for download)

No auth needed for public GitHub repos via API.

## Step 3 — Download files

```bash
curl -s "<download_url>" > "<destination>/<name>"
```

Preserve the relative directory structure from the GitHub path. **Physical copies only; no symlinks.**

## Skill Directory Naming

Use the `name` field from the API response as the skill folder name (e.g. `tlc-spec-driven`), NOT the full slug.

## Install paths

- Local: `.gemini/skills/<name>/` (relative to current working directory)
- Global: `~/.gemini/skills/<name>/`

## Notes

- SkillsMP pages are behind Cloudflare — direct WebFetch to skillsmp.com/skills/* will 403. Always use the API.
- GitHub raw downloads work without auth for public repos.
- If `githubUrl` points to a private repo, the GitHub API will return 404 — inform the user.
