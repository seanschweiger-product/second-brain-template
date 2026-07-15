# Second Brain — an LLM-compiled personal wiki

**Download Obsidian. Take this. Run.**

This is a template for a *second brain* that maintains itself. You drop raw material in (meeting notes, transcripts, documents, half-formed thoughts) and an LLM agent — Claude Code — compiles it into a persistent, synthesized, interlinked wiki that you browse in [Obsidian](https://obsidian.md). Knowledge **accumulates and compounds** instead of being re-derived every session.

The pattern comes from two things Andrej Karpathy published in April 2026: his [X post on LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595) and the follow-up ["LLM Wiki" idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) on GitHub Gist. The analogy is compilation: raw notes are source code, the LLM is the compiler, the wiki is the optimized build output — compile once, query cheaply forever.

---

## The idea in one picture

```
you                          Claude Code                      you
 │                                │                            │
 │  drop anything into raw/      │                            │
 ├───────────────────────────────▶                            │
 │        say "ingest"           │  reads, synthesizes,       │
 │                                │  cross-references,        │
 │                                │  writes wiki/ pages       │
 │                                ├───────────────────────────▶
 │                                │        browse in Obsidian │
```

**Your job:** curate sources, ask questions, direct analysis.
**Claude's job:** ingest, synthesize, cross-reference, maintain, answer.

You never write in `wiki/`. Claude never writes in `raw/`. That separation is the whole system.

---

## Quick start (5 minutes)

1. Install [Claude Code](https://claude.com/claude-code) if you don't have it.
2. **Copy-paste this into a terminal:**
   ```bash
   git clone https://github.com/seanschweiger-product/second-brain-template.git ~/second-brain
   cd ~/second-brain
   claude
   ```
3. Type **`/setup`** and follow along. Claude does the rest with you: a short interview, adapting the brain to your work, compiling your first note, setting up Obsidian, and making everything work from any folder on your machine.

*(Obsidian is just the nicest way to **look at** the brain — the brain itself is plain markdown files and works fully without it.)*

> Want your own copy on GitHub (recommended, so your brain is backed up — in a **private** repo)? Use the **Use this template** button at the top of this page, and clone *your* repo's URL instead in step 2.

From then on, the loop is:

- **After a meeting / reading something / having an idea** → write or drop a file anywhere in `raw/`
- **`/ingest`** → Claude processes everything new, updates pages, links them, logs the change
- **Ask questions** → *"What are my open blockers?"*, *"What do I know about X?"* — Claude reads the wiki first, then answers
- **`/lint` (monthly)** → maintenance pass: orphans, contradictions, superseded claims, index gaps, open questions

---

## What's in the box

| File / folder | What it is |
|---|---|
| `HOW-TO-USE.md` | The human manual. Two zones, three workflows. Read this one. |
| `WIKI-SCHEMA.md` | The **operating manual for Claude** — categories, page format, workflows, quality rules. This file *is* the system. |
| `CLAUDE.md` | Auto-loaded by Claude Code every session; points Claude at the schema. |
| `.claude/skills/setup/` | The `/setup` slash command — one-time onboarding: personalize the schema, first ingest, and use-from-any-folder install. |
| `.claude/skills/ingest/` | The `/ingest` slash command — the full compile protocol. |
| `.claude/skills/query/` | The `/query` slash command — answer questions from the wiki with citations; every claim traceable back to `raw/`. |
| `.claude/skills/lint/` | The `/lint` slash command — the maintenance pass (orphans, contradictions, superseded claims, data gaps…). |
| `raw/` | Your zone. Everything you capture goes here. Processed files get a dated name and move to `raw/processed/{meetings,docs,research,notes}/`. |
| `wiki/` | Claude's zone. Compiled knowledge: people, meetings, projects, concepts, feedback, sessions, references. |
| `wiki/index.md` | Table of contents — Claude's entry point for every question. |
| `wiki/log.md` | Audit trail of every ingest. If it's growing, the brain is working. |

---

## Why this works when note-taking apps don't

- **No filing decisions at capture time.** Everything goes in `raw/`. The compiler decides where knowledge belongs.
- **Synthesis, not storage.** A meeting transcript becomes: a meeting page, updates to each attendee's person page, updates to touched projects, new concept pages — all wikilinked.
- **No orphans.** Every page must link to at least one other page. The graph stays connected, so retrieval stays cheap.
- **An audit trail.** Every ingest appends to `wiki/log.md`. You can always see what the compiler did and correct it — and the corrections themselves become rules in `wiki/feedback/`.
- **Maintenance is a command, not a chore.** Human wikis die because the maintenance burden grows faster than the value. Here maintenance is `/lint` — a periodic pass that finds orphans, contradictions, superseded claims, and open questions, at near-zero cost to you.
- **The schema evolves with you.** `WIKI-SCHEMA.md` isn't fixed doctrine. When you notice the system failing you, tell Claude to update the schema. The brain learns how to be a brain.

---

## Make it yours

The categories (`people`, `meetings`, `projects`, `concepts`, `feedback`, `sessions`, `references`) fit knowledge-work — but they're just directories listed in `WIKI-SCHEMA.md`. A researcher might want `papers/` and `experiments/`; a student might want `courses/`. Edit the schema's category table, create the folders, and Claude follows the new rules from the next session.

If you use Claude Code with connected tools (Slack, Jira, Google Drive, Calendar…), `skills/ingest.md` includes an optional enrichment step: every entity in a raw file gets cross-checked against your connectors, so the wiki captures context that exists nowhere in the file itself.

---

## Credits & license

- Pattern: [Andrej Karpathy](https://karpathy.ai) — the [LLM Knowledge Bases post on X](https://x.com/karpathy/status/2039805659525644595) (Apr 3, 2026) and the [LLM Wiki idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (GitHub Gist, Apr 4, 2026).
- Built and battle-tested by [Sean Schweiger](https://github.com/seanschweiger-product) as a daily-driver work brain, then extracted into this template.
- Licensed under the [MIT License](LICENSE) — use it, fork it, share it freely; just keep the credit.
