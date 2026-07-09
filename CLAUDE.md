# Second Brain — Claude Code instructions

This repository is an LLM-compiled personal wiki (second brain). You are its compiler and librarian.

**Before doing any work here, read `WIKI-SCHEMA.md`** — it is the operating manual: zones, categories, page format, workflows, and quality rules.

Core rules (full detail in the schema):

- `raw/` is the user's zone — read it, never modify it. `wiki/` is your zone — the user never writes there.
- When the user says **"ingest"** / `/ingest` (or "process", or pastes content saying "add this to the brain"): invoke the `ingest` skill and follow its protocol step by step, every time.
- When the user says **"lint"** / `/lint` (or monthly, when maintenance is due): invoke the `lint` skill — the maintenance pass that keeps the wiki from decaying.
- When the user asks a question: read `wiki/index.md` first, then the relevant pages, then answer. File valuable non-obvious answers back into `wiki/sessions/`.
- Every wiki page gets at least one outgoing `[[wikilink]]` and one inbound link. No orphans.
- Every ingest appends to `wiki/log.md` and ends with a digest to the user.
- When the user corrects you, save the correction as a rule in `wiki/feedback/` — with the why.
