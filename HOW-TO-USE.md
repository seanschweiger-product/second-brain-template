# How to Use This Second Brain

---

## First time here? One command.

Open Claude Code in this folder and type: **`/setup`**

Claude interviews you briefly (3 questions), adapts the wiki categories to *your* work, runs your first ingest with you, and makes the skills work from **any** folder on your machine — one package, done. Safe to re-run anytime; it skips what's already done.

> **Can't see the `.claude` folder?** It's there — files starting with a dot are hidden by default. In Finder press `Cmd+Shift+.` to show them.

---

## Two zones. That's it.

| Zone | Who uses it | What goes there |
|---|---|---|
| `raw/` | **You** | Everything you bring in — meeting notes you write, transcripts, PDFs, decks, HTML files, anything |
| `wiki/` | **Claude** | Compiled knowledge — never write here yourself |

**The rule:** anything that enters the brain goes in `raw/`. Claude reads it and compiles the knowledge into `wiki/`. You browse `wiki/` in Obsidian.

---

## The four workflows

### 1. After a meeting
In Obsidian: create a new note anywhere in `raw/`, write your notes and thoughts freely.
Have the transcript? Drop it in `raw/` as well (same folder, different file).
Then in Claude Code, type: **`/ingest`** (plain "ingest" works too)

### 2. Dropping a batch of files
Drop everything in `raw/`. Type: **`/ingest`**
Claude processes all new files it hasn't seen before, updates the wiki, and logs what changed.

### 3. Asking a question
Type **`/query`** and ask — or just ask plainly. Claude reads `wiki/index.md` first, finds the relevant pages, synthesizes an answer, and cites the pages it used. Every claim traces back to a file in `raw/` — ask *"how do you know?"* and Claude shows you the source quotes.
Example: *"What are my open blockers?"* / *"What do I know about [person]?"*

### 4. Once a month: maintenance
Type: **`/lint`**
Claude sweeps the whole wiki for orphan pages, contradictions, facts that newer sources have overtaken, index gaps, and unanswered questions — fixes the mechanical issues and asks you about the judgment calls. This is what keeps the brain from decaying the way human-maintained wikis do.


---

## How to know it's actually working: check the log

Open `wiki/log.md` in Obsidian. Every ingest is recorded there with the date and what changed.
If the log is empty — nothing was processed. If it's growing — the brain is alive.

---

## Folder structure

```
your-second-brain/
├── HOW-TO-USE.md       ← this file
├── WIKI-SCHEMA.md      ← Claude's operating instructions (you don't need to read this)
├── CLAUDE.md           ← loaded automatically by Claude Code each session
├── .claude/skills/     ← hidden folder (Cmd+Shift+. in Finder shows it)
│   ├── setup/          ← /setup — one-time onboarding: personalize + first ingest + use-from-anywhere
│   ├── ingest/         ← /ingest — the compile step
│   ├── query/          ← /query — answer questions from the wiki, with citations
│   └── lint/           ← /lint — the monthly maintenance pass
├── raw/                ← EVERYTHING you bring in goes here
│   └── processed/      ← Claude moves files here after ingesting them
└── wiki/
    ├── index.md        ← full table of contents
    ├── log.md          ← audit trail of every ingest
    ├── people/         ← one page per person you work with
    ├── meetings/       ← one page per meeting with notes/transcript
    ├── projects/       ← ongoing work, status, blockers
    ├── concepts/       ← domain knowledge and ideas
    ├── feedback/       ← rules you've taught Claude about how to work
    ├── sessions/       ← valuable analyses filed back in
    └── references/     ← pointers to external systems and links
```

---

## What Claude cannot read
- `.mp4` video files → paste key quotes/notes into a `.md` file in `raw/` instead
- `.pptx` → Claude can read the text but not see the slides
- `.docx` → same, text only

---

## One rule
**Never write directly in `wiki/`.** That's Claude's zone. Your writing goes in `raw/`.

## One habit
When Claude gets something wrong — a bad connection, a misread priority — say so. The correction gets saved as a rule in `wiki/feedback/`, and the brain gets permanently better.
