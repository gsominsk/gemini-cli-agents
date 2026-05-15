---
name: skill-installer
description: Install Skills from remote sources (skillsmp.com, and others). Use when the user shares a skill URL or asks to install/download a skill. Triggers on skill URLs (skillsmp.com/skills/...) or phrases like "install this skill", "download this skill", "add this skill". Determines the source automatically from the URL, reads the API key from ~/.gemini/skills-config.json, fetches all skill files, and installs them locally or globally.
---

# Skill Installer

Download and install Skills from remote sources into Gemini CLI.

## Supported Sources

| Source | URL pattern | Reference |
|--------|-------------|-----------|
| SkillsMP | `skillsmp.com/skills/<slug>` | [skillsmp.md](references/skillsmp.md) |

To add a new source: create `references/<source-name>.md` following the same structure as skillsmp.md.

## Config File

API keys live globally in `~/.gemini/skills-config.json`:

```json
{
  "sources": {
    "skillsmp": {
      "api_key": "sk_live_skillsmp_..."
    }
  }
}
```

Read it with: `cat ~/.gemini/skills-config.json`

If the file doesn't exist or the key for the detected source is missing — ask the user to provide the API key, then write/update the config before proceeding.

## Workflow

1. **Narrative Transparency** — Call `update_topic` to inform the user about the installation start and strategic intent.
2. **Detect source** — match URL against known patterns in the table above.
3. **Respect GEMINI.md** — check for any project-specific installation rules or folder overrides.
4. **Load reference** — read the corresponding `references/<source>.md` for source-specific instructions.
5. **Read API key** — `cat ~/.gemini/skills-config.json`, extract key for the detected source.
6. **Resolve files** — follow source reference to get the full list of files to download.
7. **Ask install scope** — confirm with user: local (`.gemini/skills/` in CWD) or global (`~/.gemini/skills/`).
8. **Download & place** — fetch all files preserving directory structure. **Mandatory: Physically copy files; DO NOT use symbolic links.**
9. **Confirm** — list all installed files and final destination path. Use `update_topic` to recap the finished work.

## Security Rules

- **Link Integrity** — Ensure files are physically copied; symbolic links are rejected by the Skill Packaging standard.
- **Script Awareness** — If a skill contains `.sh`, `.py`, or other executable scripts, explicitly list and warn the user before placement.
- **Source Verification** — Only process URLs from sources that have a reference file in `references/` — reject unknown sources.
- **Redirection Safety** — Never follow redirects to a different domain during file download.
- **Size Limits** — If any single downloaded file exceeds 500KB — pause and ask the user before saving.
- **Safe Execution** — Never execute downloaded scripts automatically; list them and let the user decide.
- **Conflict Management** — Never overwrite an existing skill without asking — show diff of what would change.
