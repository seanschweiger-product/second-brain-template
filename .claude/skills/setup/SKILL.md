---
name: setup
description: One-command onboarding for a fresh clone — personalize the brain to its new owner, run the first ingest together, and make the skills work from any folder. Use when the user says "setup" / /setup, asks you to build or adapt their second brain, or has just cloned this template.
---

# Setup — from fresh clone to a working, personalized brain

One package: interview → personalize → first ingest → global access → crash course. If the brain is already personalized (wiki has real pages, schema already edited), skip to whichever steps are missing — this skill is safe to re-run.

## 1. Interview the new owner (short — 3 questions max, one at a time)

Ask, one question at a time, and wait for each answer:

1. **"What's your work? What role, what domain?"**
2. **"What do you want this brain to hold?"** (meetings and people? research papers? courses? clients? ideas?)
3. **"Where does your raw material come from?"** (meeting transcripts, notes apps, PDFs, voice memos → tells you what to expect in `raw/`)

Do NOT interrogate beyond this. The brain personalizes itself further through use.

## 2. Personalize the schema

Based on the answers, adapt the category table in `WIKI-SCHEMA.md`:

- Keep categories that fit (most knowledge-work fits the defaults: people, meetings, projects, concepts, feedback, sessions, references).
- Rename or add what's missing (a researcher → `papers/`, `experiments/`; a student → `courses/`; a freelancer → `clients/`), and create the matching `wiki/<category>/` folders with a `.gitkeep`.
- Show the user the final category table and confirm before writing.

## 3. First ingest — together

- If the user has a real document handy, have them drop it in `raw/` and use that. Otherwise use the included `raw/example-meeting-note.md`.
- Run the full `/ingest` protocol (read `.claude/skills/ingest/SKILL.md` and follow it exactly).
- Then show them the result: open `wiki/index.md`, point out the pages created and the `[[wikilinks]]`, and tell them to open the folder in Obsidian and switch to **graph view** — this is the "your brain is alive" moment.

## 4. Make it work from anywhere

Skills normally load only when a session starts inside this folder. Install global pointers so `/query`, `/ingest`, `/lint` work from any directory:

- Resolve **BRAIN** = this repo's absolute root path (must contain `WIKI-SCHEMA.md`). BRAIN is a placeholder for that path in the wrapper below — e.g. `/Users/dana/second-brain`.
- Note: the "never `cd`" rule in the wrappers is an instruction to **Claude** for sessions running in *other* folders (stay in the user's project, reach into the brain by absolute path). It changes nothing for the user — starting a session with `cd ~/second-brain` remains the normal way to work inside the brain.
- For each of `query`, `ingest`, `lint`: if `~/.claude/skills/<name>/SKILL.md` exists and points at a *different* brain, stop and ask which brain wins. Otherwise write:

```markdown
---
name: <name>
description: <description from BRAIN/.claude/skills/<name>/SKILL.md> Works from any folder.
---

# <name> — global pointer to the second brain

The brain lives at `<BRAIN>`. Works from any working directory — use absolute paths, never `cd`.

1. Read `<BRAIN>/.claude/skills/<name>/SKILL.md` and follow its protocol exactly — it is the single source of truth.
2. Resolve every relative path in it against `<BRAIN>` (e.g. `wiki/index.md` → `<BRAIN>/wiki/index.md`).
```

- For **ingest** only, prepend step 0: *"If the source is pasted text or files outside the brain, copy it into `<BRAIN>/raw/` first (copy — never move or modify the original)."*
- List the three installed files back to the user.

## 5. Crash course (close with exactly this, in your own words)

- **Capture:** drop anything in `raw/` → type `/ingest`. From any other folder too — `/ingest` now finds the brain.
- **Ask:** `/query` anything — answers come with citations; ask *"how do you know?"* to see source quotes.
- **Maintain:** `/lint` once a month.
- **Correct:** when Claude gets something wrong, say so — the correction becomes a permanent rule in `wiki/feedback/`.
- Full manual: `HOW-TO-USE.md`.
