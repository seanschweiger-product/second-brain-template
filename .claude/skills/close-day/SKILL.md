---
name: close-day
description: End-of-day close against the brain — what was actually done, tomorrow's task, one log entry. Use when the user says "/close-day" or wants to wrap up the working day.
---

# /close-day — close the day (2 lines + 1 log entry)

Paths are relative to the brain root.

0. Meeting check (report only, NO ingest): if `raw/` contains unprocessed
   files, mention it in one line ("N file(s) waiting in raw/ — say ingest").
   Never ingest during /close-day.
1. Reply with EXACTLY two lines:
   - **Done:** what was actually completed today (verified facts only — if the
     day's task wasn't finished, say so plainly).
   - **Tomorrow:** what tomorrow's /start-day task will be, so the morning
     needs zero thinking.
2. Append one dated entry to `wiki/log.md` recording: what was done, decisions
   made, and tomorrow's task. This is the ONLY written artifact — no other
   documents.
3. Update the "Today" line in `wiki/projects/current-status.md` if it's stale
   (see /start-day for the page format if it doesn't exist yet).

Rules: no achievements inflation — "restarted a server" is a chore, not an
achievement.
