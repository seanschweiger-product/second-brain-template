---
name: query
description: Answer a question from the wiki following the full query protocol. Use when the user asks what the brain/wiki knows about a topic, person, meeting, project, or decision — especially mid-session, when index-first discipline tends to drift.
---

# Query — answer from the wiki, not from memory

> The wiki is the source of truth. Never answer brain-content questions from conversation memory or general knowledge — re-read the pages even if you think you remember them.

## Protocol — follow in order

1. **Read `wiki/index.md` first.** Pick candidate pages by their hook column.
2. **Read the direct hit + adjacent pages in parallel.** A meeting question usually also needs the person page; a project question usually needs its spec + working log. Read 2–3 pages in one shot instead of hopping sequentially.
3. **Trust page-level warnings.** Pages flag garbled transcripts, unresolved names, and "do not use as source" notes. Carry those caveats into the answer — don't launder uncertain facts into confident ones.
4. **Follow `[[wikilinks]]` if the answer is incomplete** — one more targeted hop, not an open-ended crawl.
5. **If the wiki doesn't answer it**: grep `raw/` before saying "not found". If raw has it but the wiki doesn't, that's an ingest gap — say so and offer to run `/ingest`.
6. **Cite sources**: name the wiki pages used. Cite wiki pages, not raw files, unless raw was the only source.
7. **Answers must be verifiable.** If the user asks "how do you know?" or challenges quality, spot-check the load-bearing claims directly against the source file(s) in `raw/` and show the evidence quotes.
8. **Decide explicitly whether the answer earns a sessions file** — and state the decision in one line either way:
   - **File it** (`wiki/sessions/YYYY-MM-DD-topic.md` + index row) only if the answer is new **cross-page synthesis** not already written on any single page and valuable later.
   - **Don't file** pure retrieval of one page — it would duplicate the page.

## Rules

- `raw/` is immutable — read, never modify.
- A filed sessions page needs an index row and at least one outgoing `[[wikilink]]`.
