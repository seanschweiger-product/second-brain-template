---
name: ingest
description: Compile new raw sources into the wiki. Use when the user says "ingest" or "process", drops files in raw/, or pastes content saying "add this to the brain". Follows the full intake protocol — orient, extract, connect, write, index, log, digest.
---

# Ingest — compile raw sources into the wiki

> Follow every step, in order, every time. Token cost is not a reason to skip steps.

---

## Step 1 — Orient (before reading anything new)

Read `wiki/index.md` to load the current state of the brain.
Know what pages exist, what people are tracked, what projects are active.
This is mandatory — never ingest blind.

---

## Step 2 — Identify what's new

Scan `raw/` for files **not in `raw/processed/` and not listed in `wiki/log.md`**.
Those are unprocessed. Process them one by one.
If the user pasted content directly — treat that as the source.

---

## Step 3 — For each new source, answer these questions explicitly

Before writing anything to the wiki, answer all of these:

**Content questions:**
- What type of source is this? (meeting note / document / analysis / decision / transcript)
- What date does this content belong to?
- Who is mentioned? (list every person by name)
- What decisions were made or confirmed?
- What problems or blockers were surfaced?
- What tasks or action items came out of this?
- What new concepts, tools, or terms appear that don't have a wiki page yet?

**Connection questions (the most important):**
- Which existing wiki pages does this information touch? (check every category: people, meetings, projects, concepts, feedback, references)
- Does this update, confirm, or contradict anything already in the wiki?
- What non-obvious connections exist? (e.g. something said in a meeting that connects to a strategic concept page)

---

## Step 3b — Enrich via connected data sources (if connectors are available)

> Skip this step only if this Claude Code setup has no connected tools (Slack, Jira, Confluence, Calendar, Drive, etc.). If connectors exist, this step is mandatory, not optional.

After answering the Step 3 questions from the raw file, **actively query connected tools** for every entity that appears — a person, a ticket, a topic, a decision, a doc. Skipping a connector means missing real data that exists nowhere else.

**The hard rule: every entity gets checked against every connector, not just the "obvious" one.** It's tempting to map name→chat, ticket→issue tracker, topic→docs and stop — that's a sequential checklist, and it's exactly how real cross-source connections get missed. A person's real picture often lives split across three or four connectors at once (a chat message references a ticket which links a doc which was discussed in a calendar meeting).

Starting points per entity type (not a ceiling — go past these):

| Entity | Start with... | Then also check |
|---|---|---|
| A person | Chat (their messages + mentions of them) | Issue tracker (tickets owned/commented), Calendar (meetings), Docs (pages authored) |
| A ticket | Issue tracker (status, comments, assignee) | Chat (threads discussing it), Docs (linked process docs) |
| A shared file link | The file itself (read the content) | Whatever the content points to — other links, names, tickets inside it |
| A topic | Chat (recent messages) | Docs (relevant pages), Issue tracker (tagged tickets), Calendar (meetings about it) |
| An action item for the user | Calendar (is it scheduled) | Chat (who assigned it, any thread), Issue tracker (if it maps to a ticket) |

If a connector fails or returns nothing: note it explicitly in the digest. "Searched chat for X — no results" is better than silence.

### Never give up on something unclear — investigate first

If a transcript, message, or doc contains a word, acronym, or name you don't recognize: **do not stop and flag it as unknown**. Before writing "unclear" anywhere:

1. Search for it across every connector you have — all of them, not just the one that seems most likely.
2. If a link, doc ID, or ticket number appears anywhere near it, open it.
3. Only after exhausting these paths — and still coming up empty — write it as "uncertain" with what you tried and what came back empty.

A term that "looks hard to figure out" is usually one search or one opened link away from resolved.

### Keep status pages honest

Any living status page must reflect what actually happened, not a snapshot from days ago. Every ingest that touches a status page: verify each row is still accurate before leaving it — don't just append.

---

## Step 4 — Write to the wiki

For each existing page that's touched: open it, add the new information, update the `updated:` date.
For each new entity (person, project, concept): create a new page using the standard format from `WIKI-SCHEMA.md`.
If the source is a meeting transcript/notes: create the meeting page first (`wiki/meetings/YYYY-MM-DD-<slug>.md`), then propagate the synthesis into people/concept/project pages.
Add `[[wikilinks]]` for every connection identified in Step 3.
Every new page must link to at least one existing page. No orphans.

---

## Step 5 — Update index and log

Add any new pages to `wiki/index.md` under the correct category.

Append to `wiki/log.md`:
```
## [YYYY-MM-DD] ingest | [source filename or description]
**Pages updated:** [list]
**Pages created:** [list or "none"]
**Links added:** [page → page, page → page]
**Uncertain connections:** [anything not obvious — flag for the user to review]
```

---

## Step 6 — Categorize, rename, and move the file

Never drop a file loose into `raw/processed/` — every processed file gets a category folder and a conventional name, so nothing is ever buried in an unsorted pile.

**6a. Pick the category folder by content type:**

| Folder | What goes there |
|---|---|
| `raw/processed/meetings/` | Meeting transcripts and post-meeting debriefs |
| `raw/processed/docs/` | External documents: decks, PDFs, guides, exports |
| `raw/processed/research/` | Research and investigation outputs saved as sources |
| `raw/processed/notes/` | The user's own reflections and thought dumps |

If a file genuinely fits none of these, propose a new category folder to the user rather than forcing a bad fit.

**6b. Rename to the convention:** `YYYY-MM-DD-<topic>-<source>.<ext>` — date first (the content's date, not today's), short kebab-case topic, source suffix when relevant (e.g. `-gemini`, `-fathom`, transcript tool name). Example: `Alex _ Sam Monday, July 13⋅11_30am.txt` → `2026-07-13-alex-sam-fathom.txt`.

**6c. Move it** from `raw/` to the category folder, and **cite the new path** (`raw/processed/<category>/<new name>`) in every wiki page written in Step 4 — the provenance trail must point at the file's final resting place.

This is the proof of completion. If a file is still in `raw/`, it hasn't been processed.

---

## Step 7 — Output a digest to the user

After every ingest, produce this summary in the chat:

```
Ingested: [filename or description]
─────────────────────────────────
Pages updated:  [list]
Pages created:  [list or none]
Links added:    [A → B, C → D]
Moved to:       raw/processed/[category]/[new conventional name]
─────────────────────────────────
Uncertain:      [flag anything you weren't sure how to connect]
```

This is the user's audit trail for the session. They read it, correct anything wrong, and the brain improves.

---

## Quality rules

- Never invent connections that aren't supported by the source text
- If a connection feels right but isn't explicit, put it in "Uncertain" — don't silently add it
- If a source contradicts an existing wiki page, note the contradiction explicitly on both pages — don't silently overwrite
- If a source mentions a person not yet in the wiki, create their page even if the information is minimal
- Token cost is not a reason to skip steps — do the full protocol every time
