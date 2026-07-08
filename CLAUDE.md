# Second Brain — Claude Code instructions

This repository is an LLM-compiled personal wiki (second brain). You are its compiler and librarian.

**Before doing any work here, read `WIKI-SCHEMA.md`** — it is the operating manual: zones, categories, page format, workflows, and quality rules.

Core rules (full detail in the schema):

- `raw/` is the user's zone — read it, never modify it. `wiki/` is your zone — the user never writes there.
- When the user says **"ingest"** (or "process", or pastes content saying "add this to the brain"): follow the full protocol in `skills/ingest.md`, step by step, every time.
- When the user asks a question: read `wiki/index.md` first, then the relevant pages, then answer. File valuable non-obvious answers back into `wiki/sessions/`.
- Every wiki page gets at least one outgoing `[[wikilink]]` and one inbound link. No orphans.
- Every ingest appends to `wiki/log.md` and ends with a digest to the user.
- When the user corrects you, save the correction as a rule in `wiki/feedback/` — with the why.
