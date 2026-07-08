# LLM Wiki — Operating Schema

> **Read this first.** This document tells Claude Code how to operate this wiki. Load it at the start of every session before doing any wiki work.
>
> **For ingest operations:** follow the full protocol in `skills/ingest.md`.

---

## What this is

A Karpathy-pattern LLM wiki. Raw source documents are compiled by Claude into a persistent, synthesized, interlinked wiki. Knowledge **accumulates and compounds** instead of being re-derived each session.

**The user's job**: curate sources, ask questions, direct analysis.
**Claude's job**: ingest, synthesize, cross-reference, maintain, answer.

---

## Zones

| Zone | Location | Rule |
|---|---|---|
| Raw sources | `raw/` | Notes the user writes, transcripts, PDFs, decks, exports. Claude reads and ingests, never modifies. Processed files move to `raw/processed/`. |
| Compiled knowledge | `wiki/` | Claude writes and maintains. The user reads in Obsidian, never writes here. |
| Schema | `WIKI-SCHEMA.md` (this file) | Evolved together — when the system fails the user, update the schema. |

---

## Categories

| Category | Directory | What lives here |
|---|---|---|
| **People** | `wiki/people/` | Entity pages: role, priorities, working style, key quotes, open action items |
| **Meetings** | `wiki/meetings/` | One page per meeting that has a transcript/notes. The meeting as a unit: who, when, what was said, decisions, action items. People/concept pages hold the synthesis; the meeting page holds the event itself. |
| **Projects** | `wiki/projects/` | Ongoing initiatives with status, deliverables, open questions |
| **Concepts** | `wiki/concepts/` | Domain ideas and patterns worth understanding deeply |
| **Feedback** | `wiki/feedback/` | Rules for how Claude should work — corrections and confirmed approaches, each with a *why* |
| **Sessions** | `wiki/sessions/` | Filed outputs from valuable analyses — discoveries that should compound |
| **References** | `wiki/references/` | Pointers to external systems, ticket keys, docs, URLs |

> Customize freely: these categories fit knowledge-work. Add, rename, or remove rows to match your world — then create/rename the matching directories. This table is the source of truth.

---

## Page format

Every wiki page:

```
---
title: Short page title
category: people | meetings | projects | concepts | feedback | sessions | references
updated: YYYY-MM-DD
---

## [content]

---

## Links
- [[related-page]]
- [[another-page]]
```

**Rule**: every page must have at least one outgoing `[[wikilink]]` and be linked to from at least one other page. No orphans.

---

## Intake workflow — triggered when the user says "ingest"

1. Scan `raw/` for any unprocessed documents (anything not yet in `raw/processed/` and not in `wiki/log.md`)
2. For each new file: read it, identify which wiki pages it touches
3. **If the source is a meeting transcript/notes: ALWAYS create a meeting page first** — `wiki/meetings/YYYY-MM-DD-<slug>.md` with: attendees, date/time, source (+ transcript quality caveat if garbled), what was discussed, decisions, action items (owner-tagged), quotes worth keeping, links to every attendee's people page and touched projects/concepts. Then propagate the synthesis into people/concept/project pages.
4. Update touched pages — add new facts, note contradictions, update the `updated:` date
5. Create new pages if a significant new person, concept, or project appears
6. Update `wiki/index.md` with any new pages
7. Append to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <source description>
   - Key fact 1
   - Key fact 2
   ```
8. Move the processed file to `raw/processed/`

---

## Query workflow — when answering a question

1. Read `wiki/index.md` to identify relevant pages
2. Read those pages
3. Synthesize the answer
4. If the answer is non-obvious and valuable — **file it back** as `wiki/sessions/YYYY-MM-DD-topic.md`
5. **Session handoffs** (end-of-day state dumps) go to `wiki/sessions/YYYY-MM-DD-handoff.md` and get an index row — NEVER loose files at repo root

---

## Lint checklist — run monthly or when asked

- [ ] Orphan pages (no inbound links from anywhere)
- [ ] Stale pages (updated >30 days ago, likely need a refresh)
- [ ] Missing entity pages (people or projects mentioned but no dedicated page)
- [ ] Contradictions (conflicting facts across pages)
- [ ] Index gaps (pages not listed in `wiki/index.md`)
- [ ] Missing cross-references (concepts mentioned but not wikilinked)

---

## Link conventions

- `[[filename]]` for internal links — Obsidian-compatible
- `[[filename|Display Text]]` when the natural phrase differs from the filename
- People pages → link to their projects
- Project pages → link back to people involved
- Concept pages → link to projects/people where the concept applies

---

## Log format

```
## [YYYY-MM-DD] <type> | <description>
- Bullet with key fact or change
```

Types: `ingest` · `create` · `query` · `session` · `lint`
