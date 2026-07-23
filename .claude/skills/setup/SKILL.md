---
name: setup
description: One-command onboarding for a fresh clone — personalize the brain to its new owner, run the first ingest together, and make the skills work from any folder. Use when the user says "setup" / /setup, asks you to build or adapt their second brain, or has just cloned this template.
---

# Setup — from fresh clone to a working, personalized brain

One package: interview → personalize → first ingest → global access → crash course. If the brain is already personalized (wiki has real pages, schema already edited), skip to whichever steps are missing — this skill is safe to re-run.

**Moved the brain folder?** Re-run `/setup` from the new location — it rewrites the global pointers with the new path. Also migrate Claude Code's auto-memory: it lives under `~/.claude/projects/<old-path-key>/memory/` and is keyed by folder path, so copy that directory to the new path's key — otherwise Claude starts the new location with blank session memory (nothing is lost; it's just under the old key).

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

## 3. Discovery scan → intake plan (the power step)

An empty brain takes weeks to become useful. This step is a **deep scan of everything obtainable**, followed by a plan for absorbing it — the scan shows what the user's world is actually made of, which no interview can. Get their consent on scope first (it's their machine and their accounts), then be exhaustive, not polite:

**Scan — all of it, in parallel where possible:**

- **Claude's own memories:** every auto-memory on this machine (`~/.claude/projects/*/memory/`, `MEMORY.md` files), personal and project `CLAUDE.md` files, existing `~/.claude/skills/`. This is knowledge Claude already accumulated about them — it belongs in the brain.
- **Every available connector:** Calendar (who do they actually meet, how often), Slack (channels they live in), Jira/Confluence (active projects, docs they own), Drive/Gmail (recent working documents), and anything else connected. Check what's connected rather than assuming.
- **The machine itself:** likely knowledge hotspots — `~/Documents`, `~/Desktop`, `~/Downloads`, notes-app exports, existing Obsidian vaults, meeting-transcript folders (Fathom/Gemini/Zoom downloads). Look for *clusters of knowledge files*, not every byte.

**Report → plan → execute:**

1. Present a **discovery report**: what exists, where, roughly how much, and what it says about how this person works.
2. Propose an **intake plan** shaped by the report + the interview: what to migrate now (durable facts → people/project pages, preferences → `wiki/feedback/` rules), what to copy into `raw/` and batch-ingest, what to schedule for later, what to leave out. The report often reveals that the right categories differ from what the interview suggested — update the schema accordingly.
3. Get approval, then run the full ingest protocol over the approved intake. Everything created follows the schema — linked, indexed, logged. No orphans.

This step is the difference between "hello world" and a working brain on day one. Skip it only if the user has nothing yet — or declines.

## 4. First ingest — together

- If the user has a real document handy, have them drop it in `raw/` and use that.
- Otherwise, **write a short demo note yourself** into `raw/demo-meeting-note.md`: a fictional meeting (clearly invented names — nothing resembling their real colleagues), with 2–3 people, a project, a decision, a blocker, and one concept — enough to produce a nicely linked graph.
- Run the full `/ingest` protocol (read `.claude/skills/ingest/SKILL.md` and follow it exactly).
- Then show them the result: open `wiki/index.md`, point out the pages created and the `[[wikilinks]]`.
- **If a demo note was used: clean up after the tour** — once the user has seen the graph (end of step 5), delete the demo note and every page generated from it, and remove their index/log rows, so no fictional data lingers in the brain. Tell the user you did.

## 5. Obsidian — see the brain (optional, recommended)

- Tell the user up front: **Obsidian is just a comfortable window into the brain — the brain itself is plain markdown files and works fully without it.** Skipping this step loses nothing except the pretty graph; it can be done any time later.
- If they're in: check whether Obsidian is installed (macOS: does `/Applications/Obsidian.app` exist?). If missing, give them the download link — **https://obsidian.md** — and wait while they install (it's a normal app download, takes a minute). If they happen to have Homebrew, `brew install --cask obsidian` saves them the clicks — but don't assume they do.
- Then walk them through it: open Obsidian → *Open folder as vault* → pick the brain folder → open `wiki/index.md` → switch to **graph view**. This is the "your brain is alive" moment.

## 6. Make it work from anywhere

Skills normally load only when a session starts inside this folder. Install global pointers so `/query`, `/ingest`, `/lint` (and `/fathom`, if the user records meetings with Fathom) work from any directory:

- Resolve **BRAIN** = this repo's absolute root path (must contain `WIKI-SCHEMA.md`). BRAIN is a placeholder for that path in the wrapper below — e.g. `/Users/dana/second-brain`.
- Note: the "never `cd`" rule in the wrappers is an instruction to **Claude** for sessions running in *other* folders (stay in the user's project, reach into the brain by absolute path). It changes nothing for the user — starting a session with `cd ~/second-brain` remains the normal way to work inside the brain.
- Ask whether the user records meetings with [Fathom](https://fathom.video). If yes, include `fathom` in the list below; if no or unsure, skip it (it can be added later).
- For each of `query`, `ingest`, `lint` (+ `fathom` if applicable): if `~/.claude/skills/<name>/SKILL.md` exists and points at a *different* brain, stop and ask which brain wins. Otherwise write:

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
- List the installed files back to the user.

## 7. Crash course (close with exactly this, in your own words)

- **Capture:** drop anything in `raw/` → type `/ingest`. From any other folder too — `/ingest` now finds the brain.
- **Ask:** `/query` anything — answers come with citations; ask *"how do you know?"* to see source quotes.
- **Maintain:** `/lint` once a month.
- **Correct:** when Claude gets something wrong, say so — the correction becomes a permanent rule in `wiki/feedback/`.
- Full manual: `HOW-TO-USE.md`.
