---
name: start-day
description: Morning standup against the brain — what happened yesterday, today's ONE task, why it matters. Use when the user says "/start-day", "good morning", or asks what today's plan is.
---

# /start-day — start the day (3 lines, nothing else)

Paths are relative to the brain root.

0. Meeting check (report only, NO ingest): if `raw/` contains unprocessed
   files, mention it in one line ("N file(s) waiting in raw/ — say ingest").
   Never ingest during /start-day.
1. Read `wiki/log.md` (last ~40 lines) and `wiki/projects/current-status.md`
   (header + latest entries only).
   - **If `current-status.md` doesn't exist yet** (first run): ask the user for
     their current objective — ONE sentence describing the outcome their work
     is driving toward right now — and create the page:

     ```markdown
     # Current status

     **Objective:** <their sentence>
     **Today:** <date> — <task, filled by this skill>
     ```
2. Reply with EXACTLY three lines, no headers, no options, no questions:
   - **Yesterday:** what actually happened/changed since the last session (one line).
   - **Today:** the ONE task for today — concrete, finishable, chosen by
     highest impact on the current objective. If a calendar-fixed event
     dominates the day, the task prepares for it.
   - **Why:** which part of the objective this advances (one line).
3. Then stop. Do not produce documents. If the user disputes the task, adjust
   in conversation — one round, then execute.

Rules: never invent state — if the log is stale, say so in the Yesterday line.
The task must be something DONE by end of day, not "continue X".
